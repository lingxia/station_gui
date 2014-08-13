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
runner_log_path = log_path + '/runner_log/'
workflow_file = script_path + '/FreeMV_workflow.log'

import FreeMV_map
from helper import Helper
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
                 para_timeout,para_software_debugger,para_software_debugger_dir,para_mqx_dir,para_hardware_debugger_dir,para_device_type,para_debug_port,para_compiler_dir):
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
        self.mqx_dir = para_mqx_dir + '/rtos/mqx/'
        self.hardware_debugger_dir = para_hardware_debugger_dir
        self.device_type = para_device_type
        self.debug_port = para_debug_port
        self.result_dir = self.tool_dir + '/result/' + 'latest/'
        self.config_file = self.tool_dir + '/'+ 'settings.py'
        self.board_config_file = self.tool_dir + '/data/sys_data/'+ 'configure.py'
        self.path_file = self.tool_dir + '/data/sys_data/path.py'
        self.oobe_type_file = self.tool_dir + '/data/sys_data/configure.py'
    def config(self):
        logging.info('------deliver task configuration to runner config_file------')
        platform_pattern = re.compile(r'^platform\s*=\s*.*',re.I)
        target_pattern = re.compile(r'^target\s*=\s*.*',re.I)
        ide_debugger_pattern = re.compile(r'^\s*\(.*,.*\),\s*',re.I)
        port_pattern = re.compile(r'^serial_port\s*=\s*.*',re.I)
        binary_pattern = re.compile(r'^external_binary\s*=\s*.*',re.I)
        casename_pattern = re.compile(r'^external_casename\s*=\s*.*',re.I)
        workflow_pattern = re.compile(r'^work_flow\s*=\s*.*',re.I)
        repo_pattern = re.compile(r'^git_repo_path\s*=\s*.*',re.I)
        
        f = open(self.config_file,'r')
        f1 = open(self.config_file+'_tmp','a')
        f2 = open(workflow_file,'r')
        workflow= f2.read()
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
            match = target_pattern.search(line)
            if match:
                line = 'target '+ '=' + "'" + FreeMV_map.build_and_target_map[self.target_mode] + "'"+ '\n'
                f1.write(line)
                continue
            match = ide_debugger_pattern.search(line)
            if match:
                line ='         (' + "'" + FreeMV_map.compiler_map[self.compiler] + "'" + ',' + "'" + FreeMV_map.hardware_debugger_map[self.debugger] + "'" +')'+','+'\n'
                f1.write(line)
                continue
            match = port_pattern.search(line)
            if match:
                line = 'serial_port '+ '=' + "'" + self.serial_port + "'"+ '\n'
                f1.write(line)
                continue
            match = binary_pattern.search(line)
            if match:
                line = 'external_binary '+ '=' + "'" + Helper.Format_change(self.local_bin) + "'"+ '\n'
                f1.write(line)
                continue
            match = casename_pattern.search(line)
            if match:
                line = 'external_casename '+ '=' + "'" + self.casename + "'"+ '\n'
                f1.write(line)
                continue
            f1.write(line)
        f1.write(workflow)
        f.close()
        f1.close()
        shutil.copyfile(self.config_file+'_tmp',self.config_file)
        os.remove(self.config_file+'_tmp')

        f = open(self.board_config_file,'r')
        f1 = open(self.board_config_file+'_tmp','a')
	board_pattern= re.compile(".*\'" + self.platform+ "\'")
	oobetype_pattern= re.compile("mqx_target")

        for line in f.readlines():
            match = board_pattern.search(line)
            if match:
                line = "        '"+self.platform+"'       :   {'serial_port':\""+self.serial_port+"\",    'debug_port':\""+self.debug_port+"\"},"+ '\n'
                f1.write(line)
                continue

            logging.info('Select oobe type:')
            match = oobetype_pattern.search(line)
            if match:
                line = "mqx_target = 1"+ '\n'
                f1.write(line)
                continue

            f1.write(line)

        f.close()
        f1.close()
        shutil.copyfile(self.board_config_file+'_tmp',self.board_config_file)
        os.remove(self.board_config_file+'_tmp')

        logging.info('Configuration Modification Done')
        
        logging.info('Deliver software_debugger path')
        print self.software_debugger_dir
        if self.software_debugger == 'cw10gcc':
            self.software_debugger = 'cw10'
        f = open(self.path_file,'r')
        f1 = open(self.path_file+'_tmp','a')
        for line in f.readlines():
            if self.debugger in line and self.debugger=='jlink':
                logging.info('set j-link path')
                line = self.debugger + '_path '+ '=' + "'" + self.hardware_debugger_dir + "'"+ '\n'
                f1.write(line)
                continue

            # deliver software debugger path
            if self.software_debugger in line:
                logging.info('set software debug mingw path')
                line = self.software_debugger + '_path '+ '=' + "'" + self.software_debugger_dir + "'"+ '\n'
                f1.write(line)
                continue
            # deliver hardware debugger path (gcc_arm only)
            if self.compiler == 'gcc_arm' and self.debugger in line and self.debugger!='lauterbach':
                line = self.debugger + '_path '+ '=' + "'" + self.hardware_debugger_dir + "'"+ '\n'
                f1.write(line)
                continue
            f1.write(line)
        f.close()
        f1.close()

        shutil.copyfile(self.path_file+'_tmp',self.path_file)
        os.remove(self.path_file+'_tmp')
        logging.info('Deliver software_debugger Done')
        logging.info('deliver mqx_dir to runner')
        f = open(self.path_file,'r')
        f1 = open(self.path_file+'_tmp','a')
        for line in f.readlines():
            match = repo_pattern.search(line)
            if match:
                line = 'git_repo_path '+ '=' + "'" + self.mqx_dir + "'"+ '\n'
                f1.write(line)
                continue
            f1.write(line)
        f.close()
        f1.close()
        shutil.copyfile(self.path_file+'_tmp',self.path_file)
        os.remove(self.path_file+'_tmp')
        logging.info('Deliver mqx_dir done')

        
    def run(self):
        logging.info('------FreeMV is running------')
        cur_dir = os.getcwd()
        os.chdir(self.tool_dir)
        cmd = 'python freemv.py'
        #Helper.interact_run(cmd,self.timeout)
        os.system(cmd)
        os.chdir(cur_dir)
    def get_result(self):
        for result_file in os.listdir(self.result_dir):
            if 'result' in result_file:
                logging.info(result_file)
                break
        f = open(self.result_dir+result_file,'r')
        content = f.read()
        f.close()
        pattern = re.compile(r'run:\s*PASS',re.I)
        match = pattern.search(content)
        if match:
            logging.info('------Task Finished Sucessfully------')
            return 0
        else:
            logging.info('------Task Finished Sucessfully------')
            return 1
    def gather_log(self):
        logging.info('------Merge Log------')
        for dirName, subdirList, fileList in os.walk(self.result_dir):
            for fname in fileList:
                if 'result' not in fname:
                    try:
                        shutil.copyfile(dirName+'/'+fname,log_path+'/'+fname)
                    except Exception,e:
                        pass
