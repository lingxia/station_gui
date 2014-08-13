#!/usr/bin/env python
# coding=utf-8
 
#*******************************************************************
#* Copyright (c) 2013 Freescale Semiconductor Inc.
#* All rights reserved.
#*
#* Use of Freescale code is governed by terms and conditions
#* stated in the accompanying licensing statement.
#* Description: send result to ftp
#*
#* Revision History:
#* -----------------
#* Code Version    YYYY-MM-DD    Author        Description
#* 0.1             2013-12-06    Armand Wang    Create this file
#*******************************************************************
import os, sys
import logging
import shutil
import datetime

file_path = os.path.dirname(os.path.abspath(__file__))
main_path = os.path.join(file_path, '/../')
config_path = main_path + '/config/'
lib_path = main_path + '/lib/'
log_path = main_path + '/log/'
tmp_path = main_path + '/temp/'
sys.path.append(lib_path)
sys.path.append(log_path)

from ftper import FTPer
from stafer import STAFer
import station_map
def send_log(host,user,pwd, main_dir, port,directory,remote_dir):
    new_log_dir = directory + '/../new_log'
    if os.path.isdir(new_log_dir):
        shutil.rmtree(new_log_dir)
    shutil.copytree(directory,new_log_dir)
    time_stamp = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
    more_info_dir = new_log_dir + '/more_' + time_stamp
    shutil.copytree(new_log_dir + '/more',more_info_dir)
    shutil.rmtree(new_log_dir + '/more')
    for filename in os.listdir(new_log_dir):
        if os.path.isfile(new_log_dir+'/'+filename):
            new_filename = filename + '_' + time_stamp
            shutil.move(new_log_dir+'/'+filename,new_log_dir+'/'+new_filename)
            filename = new_filename
        if 'ide' in filename or 'Ide' in filename or 'serial' in filename:
            pass
        else:
            if 'more' not in filename:
                shutil.move(new_log_dir+'/'+filename,more_info_dir+'/'+filename)
                
    i = 0
    while i<3:
        try:
            logging.info('Starting send log to Ftp server')
            f = FTPer(host,user,pwd, main_dir, port)
            f.login()
            f.upload_files(new_log_dir,remote_dir)
            i = 3
        except Exception,e:
            i = i +1
            logging.info('Ftp Service Error')
            if i == 3:
                return 1
    logging.info('Send Log Successfully')
    return 0

def notify_scheduler_run(Tomachine,Execute_Result,request_id):
    # 1:buildresult 2: runresult . 1:pass 2:fail
    if Execute_Result == 0:
        Execute_Result = 'pass'
    else:
        Execute_Result = 'fail'
    cmd = 'TASKID ' + request_id + ' RESULTTYPE ' + '2' + ' TESTRESULT ' + station_map.to_scheduler_map[Execute_Result] + ' BINARY -1'
    logging.info('notify cmd: %s'%cmd)
    f = STAFer()
    i = 0
    ret = 1
    while(i<3 and ret==1):
        if f.call_scheduler(Tomachine,cmd)==0:
            ret=0
        else:
            i = i + 1
    if ret:
        logging.info('Notify Error')
        return 1
    else:
        logging.info('Notify Schedule sucessfully!')
        return 0
    
