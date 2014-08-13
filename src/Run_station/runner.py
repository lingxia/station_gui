# coding=utf-8
 
#*******************************************************************
#* Copyright (c) 2013 Freescale Semiconductor Inc.
#* All rights reserved.
#*
#* Use of Freescale code is governed by terms and conditions
#* stated in the accompanying licensing statement.
#* Description: runner
#*
#* Revision History:
#* -----------------
#* Code Version    YYYY-MM-DD    Author        Description
#* 0.1             2013-12-03    Armand Wang    Create this file
#*******************************************************************
import os, sys,shutil
import logging
import getopt
import datetime
import shutil

main_path = os.path.dirname(os.path.abspath(__file__))
config_path = main_path + '/config/'
lib_path = main_path + '/lib/'
log_path = main_path + '/log/'
tmp_path = main_path + '/temp/'
script_path = main_path + '/script/'
history_path = tmp_path + '/history_data/'
sys.path.append(lib_path)
sys.path.append(log_path)
sys.path.append(script_path)

# clean log file
if os.path.exists(log_path):
    shutil.rmtree(log_path)
os.makedirs(log_path + '/more')


import init_log
from getconfig import Getconfig
from helper import Helper
from Down_binary import down_from_ftp
from Send_result import send_log,notify_scheduler_run



logging.info('------check argv------')
try:
    opts,args = getopt.getopt(sys.argv[1:],'e:m:c:t:p:d:r:',['bin=','campaign=',])
except getopt.GetoptError:
    logging.info('Wrong argv')
    os._exit(1)
else:
    options = dict(opts)
    if len(options)!= 9:
        logging.info('argv overflow or not enough')
        logging.info('please verify:'+str(opts))
        os._exit(1)
    else:
        compiler = options['-e']
        test_type = options['-m']
        casename = options['-c']
        target_mode = options['-t'].replace('#',' ')
        platform = options['-p']
        debugger = options['-d']
        request_id = options['-r']
        campaign_id = options['--campaign']
        remote_bin = options['--bin']
        logging.info('------Configuration as Below------')
        logging.info('Test_Type  : '+test_type)
        logging.info('Casename   : '+casename)
        logging.info('Target_mode: '+target_mode)
        logging.info('Platform   : '+platform)
        logging.info('Compiler   : '+compiler)
        logging.info('Debugger   : '+debugger)
        logging.info('Request_id : '+request_id)
        logging.info('Remote_bin : '+remote_bin)
        logging.info('-----------------------------------')

        
logging.info('------MQX Cloud Test System(run_station)------')
start_time = datetime.datetime.now()
time_result_folder = start_time.strftime('%Y-%m-%d-%H-%M-%S')
logging.info('------Create Task Configuration ---------')
# get runner name
runner_name = Helper.Executor_Name(test_type)
logging.info('---runner---         : %s'%runner_name)
# remote log path
remote_log_path = '/' + 'run_log/' + campaign_id + '/' + request_id + '/' + test_type + '_' + casename + '_' + platform + '_' + debugger+ '/'
logging.info('---remote_log_path---: %s'%remote_log_path)
# local bin
local_bin = tmp_path + '/' + request_id + '/' + os.path.basename(remote_bin)
if os.path.exists(os.path.dirname(local_bin)):
    pass
else:
    os.makedirs(os.path.dirname(local_bin))
logging.info('---local bin---      : %s'%local_bin)
# log file
log_file = log_path + '/more/run_station.log'
logging.info('---log_file---       : %s'%log_file)
# config file
config_file =config_path + 'config.xml'
logging.info('---config file---    : %s'%config_file)
config = Getconfig(config_file)
# history data folder
history_path = history_path + '/' + time_result_folder
logging.info('---history data---   : %s'%history_path)
# result flag
Execute_Result = 1
logging.info('-----------------------------------')


logging.info('------Run : 1,Check Configuration------')
if config.getAttr(runner_name,'enable') == 'yes':
    logging.info('------Run : 2,Get Binary From Ftp Server')
    ret = down_from_ftp(config.getValue('host'),
                        config.getValue('user'),
                        config.getValue('pwd'),
                        '/',
                        21,
                        local_bin,
                        remote_bin)
    if ret:
        logging.info('Get Binary failed')
        send_log(config.getValue('host'),
                 config.getValue('user'),
                 config.getValue('pwd'),
                 '/',
                 21,
                 log_path,
                 remote_log_path)
        notify_scheduler_run(config.getValue('Scheduler_IP'),Execute_Result,str(request_id))
        #shutil.copytree(log_path,history_path)
        os._exit(1)
    else:
        logging.info('Run : 3,Create Runner')
        if debugger == 'lauterbach':
            software_debugger = 'trace32'
        elif compiler == 'gcc_arm':
            software_debugger = 'mingw'
        else:
            software_debugger = compiler
        # ksdk_oobe special process
        if test_type == 'ksdk_oobe':
            software_debugger = 'mingw'
        software_debugger_dir = config.getValue(software_debugger)
        try:
            hardware_debugger_dir = config.getValue(debugger)
        except Exception,e:
            hardware_debugger_dir = 'None'
        compiler_dir = config.getValue(compiler)
        runner_module_name = runner_name + '_runner'
        runner_dir = config.getValue(runner_name)
        # repo item name
        if test_type == 'oobe':
            repo_item = 'MQX_dir'
        elif test_type == 'kptk':
            repo_item = 'kptk_dir'
        elif test_type == 'demo':
            repo_item = 'demo_dir'
        elif test_type == 'ksdk_oobe':
            repo_item = 'demo_dir'
        elif test_type == 'usb':
            repo_item = 'demo_dir'
        elif test_type == 'unit_test':
            repo_item = 'demo_dir'
        else:
            pass

        repo_dir = config.getValue(repo_item)
        timeout = int(config.getValue('executor_timeout'))
        serial_port = config.getAttr(platform,'serial_port')
        device_type = config.getAttr(platform,'device_type')
        debug_port = config.getAttr(platform,'debug_port')
        __import__(runner_module_name)
        runner_module = sys.modules[runner_module_name]
        Runner = runner_module.run_execute(runner_dir,
                                           test_type,
                                           casename,
                                           target_mode,
                                           platform,
                                           compiler,
                                           debugger,
                                           request_id,
                                           local_bin,
                                           serial_port,
                                           timeout,software_debugger,software_debugger_dir,repo_dir,hardware_debugger_dir,device_type,debug_port,compiler_dir)
        logging.info('Run : 4,Call Runner')
        try:
            Runner.config()
            Runner.run()
            Execute_Result = Runner.get_result()
            Runner.gather_log()
        except Exception,e:
            logging.info('RUNNER EXCEPTION:')
            logging.info(e)
            send_log(config.getValue('host'),
                     config.getValue('user'),
                     config.getValue('pwd'),
                     '/',
                     21,
                     log_path,
                     remote_log_path)
            notify_scheduler_run(config.getValue('Scheduler_IP'),Execute_Result,str(request_id))
            #shutil.copytree(log_path,history_path)
            try:
                shutil.rmtree(tmp_path + '/' + request_id)
            except Exception,e:
                pass
            os._exit(1)
            
            
        logging.info('Run : 5,Sendlog/Notify Scheduler/Store log')
        send_log(config.getValue('host'),
                 config.getValue('user'),
                 config.getValue('pwd'),
                 '/',
                 21,
                 log_path,
                 remote_log_path)
        notify_scheduler_run(config.getValue('Scheduler_IP'),Execute_Result,str(request_id))
        #shutil.copytree(log_path,history_path)
        try:
            shutil.rmtree(tmp_path + '/' + request_id)
        except Exception,e:
            pass
        os._exit(Execute_Result)

        
    
else:
    logging.info('resource not enough to execute the task')
    send_log(config.getValue('host'),
             config.getValue('user'),
             config.getValue('pwd'),
             '/',
             21,
             log_path,
             remote_log_path)
    notify_scheduler_run(config.getValue('Scheduler_IP'),Execute_Result,str(request_id))
    #shutil.copytree(log_path,history_path)

    os._exit(1)

    
