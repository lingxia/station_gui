#!/usr/bin/env python
# coding=utf-8
 
#*******************************************************************
#* Copyright (c) 2013 Freescale Semiconductor Inc.
#* All rights reserved.
#*
#* Use of Freescale code is governed by terms and conditions
#* stated in the accompanying licensing statement.
#* Description: send result to ftp server
#*
#* Revision History:
#* -----------------
#* Code Version    YYYY-MM-DD    Author        Description
#* 0.1             2013-12-06    Armand Wang    Create this file
#*******************************************************************
import os, sys
import subprocess
import time

file_path = os.path.dirname(os.path.abspath(__file__))
main_path = os.path.join(file_path, '/../')
config_path = main_path + '/config/'
lib_path = main_path + '/lib/'
log_path = main_path + '/log/'
tmp_path = main_path + '/temp/'
sys.path.append(lib_path)
sys.path.append(log_path)

start_staf_file = file_path + '/staf.vbs'

def reset_staf():
    subprocess.Popen('staf local shutdown shutdown')
    time.sleep(2)
    os.system(start_staf_file)
    time.sleep(2)

def start_staf():
    os.system(start_staf_file)
    time.sleep(2)

def end_staf():
    subprocess.Popen('staf local shutdown shutdown')
    time.sleep(2)
