# coding=utf-8
 
#*******************************************************************
#* Copyright (c) 2013 Freescale Semiconductor Inc.
#* All rights reserved.
#*
#* Use of Freescale code is governed by terms and conditions
#* stated in the accompanying licensing statement.
#* Description: staf operation
#*
#* Revision History:
#* -----------------
#* Code Version    YYYY-MM-DD    Author        Description
#* 0.1             2013-12-03    Armand Wang    Create this file
#*******************************************************************

"""
Install STAF Python support by selecting to install "Python support" during the install.
Once STAF Python support is installed, verify that the STAF Python library file exists(c:/STAF/bin/PySTAF.py)
for example:
#ret = STAF_ping("b17496-03")
#ret = STAF_process('local','wang.py')
#ret = STAF_copyfile('local','c:/Perl.zip','c:/Python27/','b17496-07')
"""
import os, sys
file_path = os.path.dirname(os.path.abspath(__file__))
main_path = os.path.join(file_path, '../')
lib_path = main_path + '/lib/'
config_path = main_path + '/config/'
config_file =config_path + 'config.xml'
sys.path.append(lib_path)
from helper import Helper
from getconfig import Getconfig

staf_info = Helper.Get_STAF_info()
if staf_info['exist'] == 'no':
    config = Getconfig(config_file)
    STAF_DIR = config.getValue('STAF_dir')
else:
    STAF_DIR = staf_info['path']
sys.path.append(STAF_DIR+'/bin/')

from PySTAF import *

class STAFer():
    def __init__(self):
        pass
    def ping(self,Tomachine):
        try:
            handle = STAFHandle("STAF_SERVICE")
            result = handle.submit(Tomachine, "ping", "ping")
            if (result.rc != 0):
                return result.rc
            rc = handle.unregister()
        except STAFException, e:
            return e.rc
        return 0
    def call(self,Tomachine,command):
        try:
            handle = STAFHandle("STAF_SERVICE")
            request = "start shell command " + command
            result = handle.submit(Tomachine, "process", request)
            if (result.rc != 0):
                return result.rc
            rc = handle.unregister()
        except STAFException, e:
            return e.rc
        return 0
    def copyfile(self,Tomachine,sourcefile,todir,destmachine):
        try:
            handle = STAFHandle("STAF_SERVICE")
            request = "copy file " + sourcefile + " todirectory "+ todir + " tomachine " + destmachine
            result = handle.submit(Tomachine, "fs", request)
            if (result.rc != 0):
                return result.rc
            rc = handle.unregister()
        except STAFException, e:
            return e.rc
        return 0
    def call_scheduler(self,Tomachine,command):
        # the interface was designed by scheduler.'mcuscheduler' is an external service registered by scheduler.
        try:
            handle = STAFHandle("STAF_SERVICE")
            request = "RESULT " + command
            result = handle.submit(Tomachine, "mcuscheduler", request)
            if (result.rc != 0):
                return result.rc
            rc = handle.unregister()
        except STAFException, e:
            return e.rc
        return 0
    def station_on(self,Tomachine,command):
        # the interface was designed by scheduler.'mcuscheduler' is an external service registered by scheduler.
        try:
            handle = STAFHandle("STAF_SERVICE")
            request = "JOIN " + command
            result = handle.submit(Tomachine, "mcuscheduler", request)
            if (result.rc != 0):
                return result.rc
            rc = handle.unregister()
        except STAFException, e:
            return e.rc
        return 0
    def station_off(self,Tomachine,command):
        # the interface was designed by scheduler.'mcuscheduler' is an external service registered by scheduler.
        try:
            handle = STAFHandle("STAF_SERVICE")
            request = "LEAVE " + command
            result = handle.submit(Tomachine, "mcuscheduler", request)
            if (result.rc != 0):
                return result.rc
            rc = handle.unregister()
        except STAFException, e:
            return e.rc
        return 0

if __name__ == '__main__':
    f = STAFer()
    ret = f.ping('b17496-07')
    print 'ping result: ',ret
    ret = f.call('b17496-07','wang.py')
    print 'call result: ',ret
    ret = f.copyfile('local','c:/Perl.zip','c:/Python27/','b17496-07')
    print 'copy result: ',ret
