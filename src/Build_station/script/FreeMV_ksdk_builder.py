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
workflow_file = script_path + '/FreeMV_workflow.log'
preconfig_workflow_file = script_path + '/FreeMV_workflow_preconfig.log'
import FreeMV_map
from helper import Helper
from specify_cases import Selector
from pickler import SetInfo
class build_execute():
    def __init__(self,
                 para_builder_dir,
                 para_test_type,
                 para_casename,
                 para_target_mode,
                 para_platform,
                 para_compiler,
                 para_request_id,
                 para_timeout,para_app_scope,para_app_value,para_mqx_dir,para_compiler_dir,para_isfirst,para_campaign_id,para_compiler_version,para_mingw_dir):
        self.tool_dir = para_builder_dir
        self.test_type = para_test_type
        self.casename = para_casename
        self.target_mode = para_target_mode
        self.platform = para_platform
        self.compiler = para_compiler
        self.request_id = para_request_id
        self.timeout = para_timeout
        self.result_dir = self.tool_dir + '/result/' + 'latest/'
        self.config_file = self.tool_dir + '/'+ 'settings.py'
        self.generator = self.tool_dir + '/generator/gen2.py'
        self.applist_path = self.tool_dir + '/applist/'
        self.applist = self.tool_dir + '/applist/' + '#' + str(para_campaign_id) + '#_' + para_platform + '.yml'
        self.bin = self.tool_dir + '/tmp/run_dep/binary_path.log'
        self.path_file = self.tool_dir + '/data/sys_data/path.py'
        self.oobe_type_file = self.tool_dir + '/data/sys_data/configure.py'
        self.app_scope = para_app_scope
        self.app_value = para_app_value
        self.mqx_dir = para_mqx_dir + '/rtos/mqx'
        self.compiler_dir = para_compiler_dir
        self.isfirst = para_isfirst
        self.campaign_id = para_campaign_id
        self.mingw_dir = para_mingw_dir
        
        if 'Debug' in self.target_mode:
            self.build_mode = '0'
        else:
            self.build_mode = '1'
    def config(self):
        logging.info('Select oobe type:')
        f = open(self.oobe_type_file,'w')
        f.write('mqx_target = 1')
        f.close()
        logging.info('------1, Deliver Task Configuration to Builder Config_file------')
        platform_pattern = re.compile(r'^platform\s*=\s*.*',re.I)
        target_pattern = re.compile(r'^target\s*=\s*.*',re.I)
        ide_debugger_pattern = re.compile(r'^\s*\(.*,.*\),\s*',re.I)
        workflow_pattern = re.compile(r'^work_flow\s*=\s*.*',re.I)
        build_mode_pattern = re.compile(r'^build_mode\s*=\s*.*',re.I)
        repo_pattern = re.compile(r'^git_repo_path\s*=\s*.*',re.I)
        f = open(self.config_file,'r')
        f1 = open(self.config_file+'_tmp','a')
        # get workflow
        f2 = open(workflow_file,'r')
        workflow= f2.read()
        f2.close()
        f2 = open(preconfig_workflow_file,'r')
        preconfig_workflow = f2.read()
        f2.close()
        for line in f.readlines():
            match = workflow_pattern.search(line)
            if match:
                break
            match = platform_pattern.search(line)
            if match:
                line = 'platform '+ '=' + "'" + self.platform + "'"+ '\n'
                f1.write(line)
                continue
            match = build_mode_pattern.search(line)
            if match:
                line = 'build_mode '+ '=' + "'" + self.build_mode + "'"+ '\n'
                f1.write(line)
                continue
            match = target_pattern.search(line)
            if match:
                line = 'target '+ '=' + "'" + FreeMV_map.build_and_target_map[self.target_mode] + "'"+ '\n'
                f1.write(line)
                continue
            match = ide_debugger_pattern.search(line)
            if match:
                line ='         (' + "'" + FreeMV_map.compiler_map[self.compiler] + "'" + ',' + "'" + '0' + "'" +')'+','+'\n'
                f1.write(line)
                continue
            f1.write(line)
        # decide workflow,generate project file
        
        generate_flag =1
        if self.compiler == 'gcc_arm':
            mqx_lib_dir = self.mqx_dir + '/mqx/build/make/' + 'bsp_' + self.platform
        else:
            mqx_lib_dir = self.mqx_dir + '/mqx/build/' + self.compiler + '/' + 'bsp_' + self.platform
        if os.path.isdir(mqx_lib_dir):
            generate_flag = 0
        else:
            generate_flag = 1
            
        if generate_flag == 1:
            logging.info('---need generate project file---')
            f1.write(preconfig_workflow)
        else:
            f1.write(workflow)
        f.close()
        f1.close()
        shutil.copyfile(self.config_file+'_tmp',self.config_file)
        os.remove(self.config_file+'_tmp')
        logging.info('Configuration Modification Done')
        logging.info('------2, Deliver mqx_dir & ide dir to builder------')
        if self.compiler == 'cw10gcc':
            self.compiler = 'cw10'
        f = open(self.path_file,'r')
        f1 = open(self.path_file+'_tmp','a')
        for line in f.readlines():
            match = repo_pattern.search(line)
            if match:
                line = 'git_repo_path '+ '=' + "'" + self.mqx_dir + "'"+ '\n'
                f1.write(line)
                continue
            # deliver ide path
            if self.compiler+'_path' in line:
                line = self.compiler + '_path '+ '=' + "'" + self.compiler_dir + "'"+ '\n'
                f1.write(line)
                continue
            # deliver mingw path by force(for use of gcc_arm)
            if 'mingw_path' in line:
                line = 'mingw_path '+ '=' + "'" + self.mingw_dir + "'"+ '\n'
                f1.write(line)
                continue
            
            f1.write(line)
        f.close()
        f1.close()
        shutil.copyfile(self.path_file+'_tmp',self.path_file)
        os.remove(self.path_file+'_tmp')
        logging.info('Deliver mqx_dir & ide dir Done')
        
        logging.info('------ 3,Create App List For Builder------')
        # Clean applist of other request
        for file in os.listdir(self.applist_path):
            if '.yml' in file and str(self.campaign_id) not in file:
                print file
                try:
                    os.remove(self.applist_path + file)
                except Exception,e:
                    pass
        if os.path.isfile(self.applist):
            # set applist be current to avoid platform execute disorder.
            SetInfo(self.applist,self.tool_dir)
            ret = Selector(self.applist,{self.casename:int(self.app_value),})
            if ret:
                return ret
            return 0
        else:
            cmd = 'python '+ self.generator + ' ' + self.platform + ' ' + str(self.campaign_id)
            Helper.interact_run(cmd,self.timeout)
            ret = Selector(self.applist,{self.casename:int(self.app_value),})
            if ret:
                return ret
            return 0
    def run(self):
        logging.info('------FreeMV is running------')
        cur_dir = os.getcwd()
        os.chdir(self.tool_dir)
        cmd = 'python freemv.py'
        #Helper.interact_run(cmd,self.timeout)
        os.system(cmd)
        os.chdir(cur_dir)
    def get_result(self):
        result_record_file = ''
        for result_file in os.listdir(self.result_dir):
            if 'result' in result_file:
                result_record_file = result_file
                break
        f = open(self.result_dir+result_record_file,'r')
        content = f.read()
        f.close()
        if '+' in self.casename:
            re_casename = self.casename.replace('+','\+')
        else:
            re_casename = self.casename
        pattern = re.compile(re_casename + r':\s*PASS',re.I)
        match = pattern.search(content)
        if match:
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
                if 'result' not in fname:
                    try:
                        shutil.copyfile(dirName+'/'+fname,log_path+'/'+fname)
                    except Exception,e:
                        pass
