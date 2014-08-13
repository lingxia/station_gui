#!/usr/bin/env python
# coding=utf-8
 
#*******************************************************************
#* Copyright (c) 2013 Freescale Semiconductor Inc.
#* All rights reserved.
#*
#* Use of Freescale code is governed by terms and conditions
#* stated in the accompanying licensing statement.
#* Description: FreeMV builder
#*
#* Revision History:
#* -----------------
#* Code Version    YYYY-MM-DD    Author        Description
#* 0.1             2013-12-06    Armand Wang    Create this file
#*******************************************************************
import os, sys,shutil,subprocess
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
from pickler import GetEnvInfo_demo
from getconfig import Getconfig
# init freepv return code
rc = 1


class build_execute():
    def __init__(self,
                 para_builder_dir,
                 para_test_type,
                 para_casename,
                 para_target_mode,
                 para_platform,
                 para_compiler,
                 para_request_id,
                 para_timeout,para_app_scope,para_app_value,para_repo_dir,para_compiler_dir,para_isfirst,para_campaign_id,para_compiler_version,para_mingw_dir):
        self.tool_dir = para_builder_dir
        self.test_type = para_test_type
        self.casename = para_casename
        self.target_mode = para_target_mode
        self.platform = para_platform
        self.compiler = para_compiler
        self.request_id = para_request_id
        self.timeout = para_timeout
        self.result_dir = self.tool_dir + '/log/'
        self.config_file = self.tool_dir + '/config/config.xml'
        self.bin = self.tool_dir + '/temp/binary_path.log'
        self.repo_dir = para_repo_dir
        self.compiler_dir = para_compiler_dir
        self.campaign_id = para_campaign_id
        self.compiler_version = para_compiler_version
        self.mingw_dir = para_mingw_dir

    def config(self):
        logging.info('------1, Deliver Task Configuration to Builder Config_file------')
        try:
            config = Getconfig(self.config_file)
            config.setValue('test_type','usb')
            config.setValue('requestid',str(self.campaign_id))
            config.setValue('app',self.casename)
            config.setValue('build','yes')
            config.setValue('run','no')
            config.setValue('build_and_run','no')
            config.setValue('platform',self.platform)
            config.setValue('IDE',self.compiler)
            config.setValue('target',self.target_mode)
            config.setValue(self.compiler,self.compiler_dir)
            config.setAttr(self.compiler,'version',self.compiler_version)
            # deliver mingw path by force(for use of gcc_arm)
            config.setValue('mingw',self.mingw_dir)
            config.setValue('psdk_demo_dir',self.repo_dir)
            # app_info/pre_configure/build_lib enable
            (app_info_done,pre_configure_done,build_lib_done)= GetEnvInfo_demo(self.tool_dir,self.campaign_id,self.platform,self.compiler,self.target_mode)
            
            if app_info_done:
                config.setValue('app_info','no')
            else:
                config.setValue('app_info','yes')
            if pre_configure_done:
                config.setValue('pre_configure','no')
            else:
                config.setValue('pre_configure','yes')
            if build_lib_done:
                config.setValue('build_lib','no')
            else:
                config.setValue('build_lib','yes')
        except Exception,e:
            return 1
        else:
            return 0
                

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
            f = open(self.bin,'r')
            bin_name = f.read()
            f.close()
            return (0,bin_name)
        else:
            logging.info('------Task Failed------')
            return (1,None)
    def gather_log(self):
        logging.info('------Merge Log------')
        for dirName, subdirList, fileList in os.walk(self.result_dir):
            for fname in fileList:
                if '.gitignore' not in fname:
                    try:
                        shutil.copyfile(dirName+'/'+fname,log_path+'/'+fname)
                    except Exception,e:
                        pass
