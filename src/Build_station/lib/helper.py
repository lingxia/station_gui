#!/usr/bin/env python
# coding=utf-8

#*******************************************************************
#* Copyright (c) 2013 Freescale Semiconductor Inc.
#* All rights reserved.
#*
#* Use of Freescale code is governed by terms and conditions
#* stated in the accompanying licensing statement.
#* Description: helper function.
#*
#* Revision History:
#* -----------------
#* Code Version    YYYY-MM-DD    Author        Description
#* 0.1             2013-06-08    Larry Shen    Create this file
#*******************************************************************

import os, sys
import subprocess
import time
import threading
import _winreg

#file_path = os.path.dirname(os.path.abspath(__file__))
import logging

class Helper:
    @staticmethod
    def run(cmd, timeout=10):
        def timeout_trigger(sub_process):
            logging.info('timeout function trigger')
            os.system('taskkill /T /F /pid '+ str(sub_process.pid))

        timeout = float(timeout)
        logging.info(cmd)
        p = subprocess.Popen(cmd, 0, None, None, None, None, shell=True)
        t = threading.Timer(timeout*60, timeout_trigger, args=(p,))
        t.start()
        p.wait()
        t.cancel()

        ret_val = p.returncode

        return ret_val

    @staticmethod
    def interact_run(cmd, timeout):
        def timeout_trigger(sub_process):
            logging.info('timeout function trigger')
            os.system('taskkill /T /F /pid '+ str(sub_process.pid))

        logging.info(cmd)
        p = subprocess.Popen(cmd, 0, None, None, None, subprocess.PIPE,shell=True)
        t = threading.Timer(timeout*60, timeout_trigger, args=(p,))
        t.start()
        p.wait()
        t.cancel()

        ret_val = p.returncode
        ret_info = p.stderr.readline()

        return (ret_val, ret_info)

    @staticmethod
    def system(cmd):
        logging.info(cmd)
        sys.stdout.flush()
        ret_val = os.system('call ' + cmd)
        return ret_val
    @staticmethod
    def Executor_Name(test_type):
        if test_type == 'oobe':
            return 'FreeMV'
        elif test_type == 'vnv':
            return 'Beart'
        elif test_type == 'kptk':
            return 'FreeKV'
        elif test_type == 'demo':
            return 'FreeKV_demo'
        elif test_type == 'ksdk_oobe':
            return 'FreeMV_ksdk'
        elif test_type == 'usb':
            return 'FreeKV_usb'
        elif test_type == 'unit_test':
            return 'FreeKV_unit_test'
        

    @staticmethod
    def Format_change(origin_string):
        return origin_string.replace('\\','/')

    @staticmethod
    def Get_STAF_info():
        staf_info = {}
        try:
            key = _winreg.OpenKey(_winreg.HKEY_LOCAL_MACHINE,r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\STAF")
            staf_path,type = _winreg.QueryValueEx(key,"InstallLocation")
            staf_version,type = _winreg.QueryValueEx(key,"DisplayVersion")
            staf_info['path'] = staf_path.replace('\\','/')
            staf_info['exist'] = 'yes'
        except Exception,e:
            staf_info['exist'] = 'no'
        return staf_info

