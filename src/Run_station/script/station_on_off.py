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

file_path = os.path.dirname(os.path.abspath(__file__))
main_path = os.path.join(file_path, '/../')
config_path = main_path + '/config/'
lib_path = main_path + '/lib/'
log_path = main_path + '/log/'
tmp_path = main_path + '/temp/'
sys.path.append(lib_path)
sys.path.append(log_path)

from stafer import STAFer

def register(Tomachine,machine_name,machine_type,mac,ip,compilers,debuggers,tools,ran,platform,token):
    cmd = 'MACHINENAME ' + machine_name + ' MACHINETYPE ' + machine_type + ' MAC ' + mac + ' IP ' + ip + ' COMPILERS ' + compilers + ' DEBUGGER ' + debuggers + ' TOOLS ' + tools + ' RANGE ' + ran + ' ACCESSTOKEN ' + token + ' PLATFORM ' + platform
    print'cmd: %s'%cmd
    f = STAFer()
    ret = f.station_on(Tomachine,cmd)
    if ret:
        print'register Error'
        return 1
    else:
        print'register sucessfully!'
        return 0
def offline(Tomachine,machine_type,mac):
    cmd = 'MACHINETYPE ' + machine_type + ' MAC ' + mac
    print'cmd: %s'%cmd
    f = STAFer()
    ret = f.station_off(Tomachine,cmd)
    if ret:
        print'offline Error'
        return 1
    else:
        print'offline sucessfully!'
        return 0
