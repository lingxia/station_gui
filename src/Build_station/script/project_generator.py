#!/usr/bin/env python
# coding=utf-8

#*******************************************************************
#* Copyright (c) 2013 Freescale Semiconductor Inc.
#* All rights reserved.
#*
#* Use of Freescale code is governed by terms and conditions
#* stated in the accompanying licensing statement.
#* Description: pre-configure.
#*
#* Revision History:
#* -----------------
#* Code Version    YYYY-MM-DD    Author        Description
#* 0.1             2013-06-13    Larry Shen    Create this file
#*******************************************************************

import os, sys, logging
import shutil

para_platform = sys.argv[1]
git_repo_dir = sys.argv[2]

logging.info('generate project for %s'%para_platform)
flag = 0
cur_dir = os.getcwd()
os.chdir(git_repo_dir)

logging.info('  -- execute batch generator --')
cmd = "perl generator_new/gutils/mqx_batch.pl file=generator_new/records/mqx_records/projects/" + para_platform + ".yml logcolor=1 loglevel=3"
ret = os.system(cmd)
if ret!=0:
    flag = 1

logging.info('  -- execute project generator --')
cmd = "perl generator_new/gutils/mqx_project.pl file=generator_new/records/mqx_records/projects/" + para_platform + ".yml logcolor=1 loglevel=3"
ret = os.system(cmd)
if ret!=0:
    flag = 1


logging.info('  -- execute workspace generator --')
cmd = "perl generator_new/gutils/mqx_workspace.pl file=generator_new/records/mqx_records/projects/" + para_platform + ".yml logcolor=1 loglevel=3"
ret = os.system(cmd)
if ret!=0:
    flag = 1


logging.info('  -- execute makefile generator --')
cmd = "perl generator_new/gutils/mqx_make.pl file=generator_new/records/mqx_records/projects/" + para_platform + ".yml logcolor=1 loglevel=3"
ret = os.system(cmd)
if ret!=0:
    flag = 1


os._exit(flag)


os.chdir(cur_dir)

logging.info('<done>')
