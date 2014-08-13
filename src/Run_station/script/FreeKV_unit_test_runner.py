#!/usr/bin/env python
# coding=utf-8
 
#*******************************************************************
#* Copyright (c) 2013 Freescale Semiconductor Inc.
#* All rights reserved.
#*
#* Use of Freescale code is governed by terms and conditions
#* stated in the accompanying licensing statement.
#* Description: FreeMV runner
#*
#* Revision History:
#* -----------------
#* Code Version    YYYY-MM-DD    Author        Description
#* 0.1             2013-12-06    Armand Wang    Create this file
#*******************************************************************
import os, sys,shutil
import logging
import re

file_path = os.path.dirname(os.path.abspath(__file__))
main_path = file_path + '/../'
config_path = main_path + '/config/'
lib_path = main_path + '/lib/'
log_path = main_path + '/log/'
tmp_path = main_path + '/temp/'
script_path = main_path + '/script/'
sys.path.append(lib_path)
sys.path.append(log_path)
sys.path.append(script_path)

from helper import Helper
from getconfig import Getconfig
# init freepv return code
rc = 1

class run_execute():
    def __init__(self,
                 para_runner_dir,
                 para_test_type,
                 para_casename,
                 para_target_mode,
                 para_platform,
                 para_compiler,
                 para_debugger,
                 para_request_id,
                 para_local_bin,
                 para_serial_port,
                 para_timeout,para_software_debugger,para_software_debugger_dir,para_repo_dir,para_hardware_debugger_dir,para_device_type,para_debug_port,para_compiler_dir):
        self.tool_dir = para_runner_dir
        self.test_type = para_test_type
        self.casename = para_casename
        self.target_mode = para_target_mode
        self.platform = para_platform
        self.compiler = para_compiler
        self.debugger = para_debugger
        self.request_id = para_request_id
        self.local_bin = para_local_bin
        self.serial_port = para_serial_port
        self.timeout = para_timeout
        self.software_debugger = para_software_debugger
        self.software_debugger_dir = para_software_debugger_dir
        self.repo_dir = para_repo_dir
        self.hardware_debugger_dir = para_hardware_debugger_dir
        self.device_type = para_device_type
        self.debug_port = para_debug_port
        self.compiler_dir = para_compiler_dir
        self.result_dir = self.tool_dir + '/log/'
        self.config_file = self.tool_dir + '/config/config.xml'
    def config(self):
        logging.info('------deliver task configuration to runner config_file------')
        config = Getconfig(self.config_file)
        config.setValue('test_type','unit_test')
        config.setValue('app',self.casename)
        config.setValue('build_and_run','no')
        config.setValue('build','no')
        config.setValue('run','yes')
        config.setValue('platform',self.platform)
        config.setValue('IDE',self.compiler)
        config.setValue('debugger',self.debugger)
        config.setValue('target',self.target_mode)
        config.setValue(self.compiler,self.compiler_dir)
        config.setValue(self.software_debugger,self.software_debugger_dir)
        config.setValue('app_info','no')
        config.setValue('pre_configure','no')
        config.setValue('build_lib','no')
        config.setValue('psdk_demo_dir',self.repo_dir)
        config.setValue('binary',self.local_bin)
        config.setAttr(self.platform,'serial_port',self.serial_port)
        config.setAttr(self.platform,'device_type',self.device_type)
        config.setAttr(self.platform,'debug_port',self.debug_port)
        try:
            config.setValue(self.debugger,self.hardware_debugger_dir)
        except Exception,e:
            pass
        
    def run(self):
        logging.info('------FreeKV_demo is running------')
        cur_dir = os.getcwd()
        os.chdir(self.tool_dir)
        cmd = 'python freekv_demo.py'
        global rc
        rc = os.system(cmd)
        os.chdir(cur_dir)
    def get_result(self):
        if rc==0:
            logging.info('------Task Finished Sucessfully------')
            return 0
        else:
            logging.info('------Task Failed------')
            return 1
    def gather_log(self):
        logging.info('------Merge Log------')
        for dirName, subdirList, fileList in os.walk(self.result_dir):
            for fname in fileList:
                if '.gitignore' not in fname:
                    try:
                        shutil.copyfile(dirName+'/'+fname,log_path+'/'+fname)
                    except Exception,e:
                        pass
