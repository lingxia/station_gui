#!/usr/bin/env python
# coding=utf-8
 
#*******************************************************************
#* Copyright (c) 2013 Freescale Semiconductor Inc.
#* All rights reserved.
#*
#* Use of Freescale code is governed by terms and conditions
#* stated in the accompanying licensing statement.
#* Description: download binary file from ftp/staf
#*
#* Revision History:
#* -----------------
#* Code Version    YYYY-MM-DD    Author        Description
#* 0.1             2013-12-06    Armand Wang    Create this file
#*******************************************************************
import os, sys
import logging

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
def down_from_ftp(host,user,pwd,main_dir,port,local_bin,remote_bin):
    try:
        f = FTPer(host,user,pwd, main_dir, port)
        f.login()
        f.download_file(local_bin,remote_bin)
    except Exception,e:
        logging.info('Ftp Service Error')
        logging.info(e)
        return 1
    if os.path.isfile(local_bin):
        logging.info('Binary is ready')
        return 0
    else:
        return 1
def down_from_staf(Tomachine,sourcefile,todir,destmachine):
    f = STAFer()
    ret = f.copyfile(Tomachine,sourcefile,todir,destmachine)
    if ret:
        return 1
    else:
        return 0
    
