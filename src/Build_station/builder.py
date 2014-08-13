# coding=utf-8
 
#*******************************************************************
#* Copyright (c) 2013 Freescale Semiconductor Inc.
#* All rights reserved.
#*
#* Use of Freescale code is governed by terms and conditions
#* stated in the accompanying licensing statement.
#* Description: builder
#*
#* Revision History:
#* -----------------
#* Code Version    YYYY-MM-DD    Author        Description
#* 0.1             2013-12-08    Armand Wang    Create this file
#*******************************************************************
import os, sys,shutil
import logging
import getopt
import datetime

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
from Send_result import send_result,notify_scheduler_build



logging.info('------check argv------')
try:
    opts,args = getopt.getopt(sys.argv[1:],'e:m:c:t:p:r:',['is_first=','campaign=','needrun=',])
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
        request_id = options['-r']
        isfirst = options['--is_first']
        campaign_id = options['--campaign']
        needrun = int(options['--needrun'])
        logging.info('------Configuration as Below------')
        logging.info('Test_Type  : '+test_type)
        logging.info('Casename   : '+casename)
        logging.info('Target_mode: '+target_mode)
        logging.info('Platform   : '+platform)
        logging.info('Compiler   : '+compiler)
        logging.info('Request_id : '+request_id)
        logging.info('first build: '+isfirst)
        logging.info('-----------------------------------')

        

start_time = datetime.datetime.now()
time_result_folder = start_time.strftime('%Y-%m-%d-%H-%M-%S')
logging.info('------Create Task Configuration ---------')
# get builder name
builder_name = Helper.Executor_Name(test_type)
logging.info('---builder---         : %s'%builder_name)
# remote log path
remote_log_path = '/' + 'build_log/' + campaign_id + '/' + request_id + '/' + test_type + '_' + casename + '_' + platform + '_' + compiler + '/' 
logging.info('---remote_log_path--- : %s'%remote_log_path)

# log file
log_file = log_path + '/more/build_station.log'
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
local_bin = None
remote_bin = 'default'


logging.info('-----------------------------------')


logging.info('------Run : 1,Check Configuration------')
if config.getAttr(builder_name,'enable') == 'yes' and config.getAttr('IDE',compiler) == 'yes':
    logging.info('Run : 2,Create Builder')
    builder_module_name = builder_name + '_builder'
    builder_dir = config.getValue(builder_name)
    app_scope = config.getValue('default_app_scope')
    app_value = config.getValue('default_app_value')
    timeout = int(config.getValue('executor_timeout'))
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
    compiler_dir = config.getValue(compiler)
    compiler_version = config.getAttr(compiler,'version')
    # mingw is required when use gcc_arm as compiler
    mingw_dir = config.getValue('mingw')
    __import__(builder_module_name)
    builder_module = sys.modules[builder_module_name]
    Builder = builder_module.build_execute(builder_dir,
                                       test_type,
                                       casename,
                                       target_mode,
                                       platform,
                                       compiler,
                                       request_id,
                                       timeout,app_scope,app_value,repo_dir,compiler_dir,isfirst,campaign_id,compiler_version,mingw_dir)
    logging.info('Run : 3,Call Builder')
    try:
        ret = Builder.config()
        if ret == 0:
            Builder.run()
            (sof,bin_dir) = Builder.get_result()
            # binary name must be processed
            if sof == 0:
                bin_dir = bin_dir.replace('\n','')
                logging.info(bin_dir)
                Execute_Result = sof
                local_bin = bin_dir
                local_bin = bin_dir.replace('"','')
                remote_bin = '/' + 'bin/' + campaign_id + '/'+ request_id + '/' + test_type + '_' + casename + '_' + platform + '_' + compiler + '/' + os.path.basename(local_bin)
            Builder.gather_log()
    except Exception,e:
        logging.info('BUILDER EXCEPTION:')
        logging.info(e)
        send_result(config.getValue('host'),
                    config.getValue('user'),
                    config.getValue('pwd'),
                    '/',
                    21,
                    log_path,
                    remote_log_path,Execute_Result,local_bin,remote_bin,needrun)
        notify_scheduler_build(config.getValue('Scheduler_IP'),Execute_Result,str(request_id),remote_bin)
        #shutil.copytree(log_path,history_path)
        os._exit(1)
    logging.info('Run : 4,Sendresult/Notify Scheduler/Store log')
    send_result(config.getValue('host'),
                config.getValue('user'),
                config.getValue('pwd'),
                '/',
                21,
                log_path,
                remote_log_path,Execute_Result,local_bin,remote_bin,needrun)
    notify_scheduler_build(config.getValue('Scheduler_IP'),Execute_Result,str(request_id),remote_bin)
    #shutil.copytree(log_path,history_path)
    os._exit(Execute_Result)

    
else:
    logging.info('resource not enough to execute the task')
    send_result(config.getValue('host'),
             config.getValue('user'),
             config.getValue('pwd'),
             '/',
             21,
             log_path,
             remote_log_path,Execute_Result,local_bin,remote_bin,needrun)
    notify_scheduler_build(config.getValue('Scheduler_IP'),Execute_Result,str(request_id),remote_bin)
    #shutil.copytree(log_path,history_path)
    os._exit(1)
