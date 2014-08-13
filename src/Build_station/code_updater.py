# coding=utf-8
 
#*******************************************************************
#* Copyright (c) 2013 Freescale Semiconductor Inc.
#* All rights reserved.
#*
#* Use of Freescale code is governed by terms and conditions
#* stated in the accompanying licensing statement.
#* Description: get / config / update source code
#*
#* Revision History:
#* -----------------
#* Code Version    YYYY-MM-DD    Author        Description
#* 0.1             2013-12-09    Armand Wang    Create this file
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
config_file =config_path + 'config.xml'
local_patch = tmp_path + 'patch'
generator_file = script_path + 'project_generator.py'
# clean log file
if os.path.exists(log_path):
    shutil.rmtree(log_path)
os.mkdir(log_path)

# delete tool optimize record file
tool_dir = main_path + '/../..'
freemv_record_file = tool_dir + '/freemvbuild/tmp/PreCase.pkl'
freekv_record_file = tool_dir + '/freekvbuild/temp/EnvRecord.pkl'
freekv_demo_record_file = tool_dir + '/freekv_demobuild/temp/EnvRecord.pkl'
try:
    os.remove(freemv_record_file)
except Exception,e:
    pass

try:
    os.remove(freekv_record_file)
except Exception,e:
    pass

try:
    os.remove(freekv_demo_record_file)
except Exception,e:
    pass



import init_log_updater
from getconfig import Getconfig
from helper import Helper
from Down_binary import down_from_ftp
from Down_package import down_package
from Send_result import send_result,notify_scheduler_build
from Repo_processor import Check_repo,Clone_repo,update_repo,update_and_patch,get_subdir_list

start_time = datetime.datetime.now()
time_result_folder = start_time.strftime('%Y-%m-%d-%H-%M-%S')
config = Getconfig(config_file)
Execute_Result = 0 # pass is default

logging.info('------check argv------')
try:
    opts,args = getopt.getopt(sys.argv[1:],'t:r:m:b:n:f:p:l:')
except getopt.GetoptError:
    logging.info('wrong argv')
    os._exit(1)
options = dict(opts)
request_id = options['-r']
test_type = options['-t']
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


if '-m' in options and '-n' in options and '-b' in options and '-l' in options:
    logging.info('------git mode------')
    repo_url = options['-n']
    ck_name = options['-b']
    platform_list = options['-l'].split(',')
    logging.info('1,------get repository ------')
    remote_log_dir = '/update_log/git/' + request_id + '/'
    new_repo_dir = config.getValue('NEW_repo_dir')
    already_clone_repo = get_subdir_list(new_repo_dir)
    whole_repo_list = already_clone_repo + config.getChildTextList('repo_list')
    flag = 0
    for repo in whole_repo_list:
        if Check_repo(repo,repo_url) == 0:
            logging.info('------repo is local------')
            config.setValue(repo_item,repo)
            logging.info('find it in repo_list,current repo: %s'%repo)
            flag = 1
            break
    if flag == 0:
        logging.info('------repo need clone------')# make sure repo url is read-only mode
        if not os.path.isdir(config.getValue('NEW_repo_dir')):
            os.mkdir(config.getValue('NEW_repo_dir'))
        (ret,newrepo_dir) = Clone_repo(config.getValue('NEW_repo_dir'),repo_url,test_type)
        if ret == 0:
            config.setValue(repo_item,newrepo_dir)
            logging.info('already clone,current repo: %s'%newrepo_dir)
            logging.info('add this repo to new repo list')
            config.addChild('repo_list','new_repo',newrepo_dir)
        else:
            Execute_Result = 1
    logging.info('2,------config repo ------')
    if '-p' in options:
        remote_patch = options['-p']
        logging.info('need patch,downloading......')
        ret = down_from_ftp(config.getValue('host'),
                            config.getValue('user'),
                            config.getValue('pwd'),
                            '/',
                            21,
                            local_patch,
                            remote_patch)
        if ret:
            logging.info('get patch failed')
            Execute_Result = 1
        else:
            ret = update_and_patch(config.getValue(repo_item),ck_name,local_patch,test_type)
            if ret:
                logging.info('config repo or apply patch failed')
                Execute_Result = 1
    else:
        if Execute_Result !=1:
            logging.info('do not need patch')
            ret = update_repo(config.getValue(repo_item),ck_name,test_type)
            if ret:
                logging.info('config repo failed')
                Execute_Result = 1


    logging.info('3,------send log------')
    #send_result(config.getValue('host'),
                #config.getValue('user'),
                #config.getValue('pwd'),
                #'/',
                #21,
                #log_path,
                #remote_log_dir,1,None,None,2)
    logging.info('4,------notify cmd_generator------')
    if Execute_Result == 1:
        logging.info('notify scheduler')
        notify_scheduler_build(config.getValue('Scheduler_IP'),8,str(request_id),'default')
    # return result,0:pass,1:fail
    os._exit(Execute_Result)




    
        
elif '-m' in options and '-f' in options:
    logging.info('------ftp mode------')
    remote_log_dir = '/update_log/ftp/' + request_id + '/'
    remote_dir = options['-f']
    local_dir = config.getValue('NEW_repo_dir')+ '_'+time_result_folder + '/'
    logging.info('1,------get package------')
    ret = down_package(config.getValue('host'),
                       config.getValue('user'),
                       config.getValue('pwd'),
                       '/',
                       21,
                       local_dir,
                       remote_dir)
    if ret:
        logging.info('------get package failed------')
        Execute_Result = 1
    else:
        config.setValue(repo_item,local_dir)
    logging.info('2,------sendlog------')
    #send_result(config.getValue('host'),
                #config.getValue('user'),
                #config.getValue('pwd'),
                #'/',
                #21,
                #log_path,
                #remote_log_dir,1,None,None,2)
    if Execute_Result == 1:
        logging.info('notify scheduler')
        notify_scheduler_build(config.getValue('Scheduler_IP'),8,str(request_id),'default')
    os._exit(Execute_Result)
else:
    logging.info('argv is not enough')
    os._exit(1)
    
