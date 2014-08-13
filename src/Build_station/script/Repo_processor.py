#!/usr/bin/env python
# coding=utf-8
 
#*******************************************************************
#* Copyright (c) 2013 Freescale Semiconductor Inc.
#* All rights reserved.
#*
#* Use of Freescale code is governed by terms and conditions
#* stated in the accompanying licensing statement.
#* Description: git repo operator
#*
#* Revision History:
#* -----------------
#* Code Version    YYYY-MM-DD    Author        Description
#* 0.1             2013-12-06    Armand Wang    Create this file
#*******************************************************************
import os, sys
import logging
import shutil
import subprocess

file_path = os.path.dirname(os.path.abspath(__file__))
main_path = os.path.join(file_path, '/../')
config_path = main_path + '/config/'
lib_path = main_path + '/lib/'
log_path = main_path + '/log/'
tmp_path = main_path + '/temp/'
sys.path.append(lib_path)
sys.path.append(log_path)
from helper import Helper

def update_repo(repo_dir,multi_ck_name,test_type):
    '''
    oobe: clean/reset/checkout master/pull   /checkout branch /pull
    kptk: clean/reset/(default master)pull   /pull core/pull ucosii/pull mcu-sdk/mcu-sdk checkout branch/mcusdk - pull
    '''
    multi_list = multi_ck_name.split(';')
    # common ck name
    ck_name = multi_list[0]
    
    rc = 0
    # remove index file to avoid sync fail
    index_file = repo_dir + '/.git/index.lock'
    try:
        os.remove(index_file)
    except Exception,e:
        pass
        
    # common operation
    cur_dir = os.getcwd()
    os.chdir(repo_dir)
    logging.info( '  -- hard reset --')
    cmd = "git reset --hard"
    reset_ret = Helper.run(cmd)
    logging.info(reset_ret)
    rc = rc or reset_ret
    logging.info( '  -- git clean --')
    cmd = "git clean -fdx"
    i = 0
    clean_ret = 1
    while(i<3 and clean_ret==1):
        if Helper.run(cmd,20) == 0:
            clean_ret = 0
        else:
            i = i + 1
    logging.info(clean_ret)
    rc = rc or clean_ret
    logging.info( '  -- checkout master --')
    cmd = "git checkout master"
    ret = Helper.run(cmd)
    logging.info(ret)
    rc = rc or ret
    logging.info( '  -- pull master --')
    cmd = "git pull"
    pull_ret = Helper.run(cmd)
    logging.info(pull_ret)
    rc = rc or pull_ret

    if test_type == 'oobe' or test_type == 'demo' or test_type == 'ksdk_oobe' or test_type == 'usb' or test_type == 'unit_test':
        ck_name_list = ck_name.split('/')
        logging.info( '  -- checkout --')
        cmd = "git checkout %s" % ck_name_list[0]
        ck_ret = Helper.run(cmd)
        logging.info(ck_ret)
        rc = rc or ck_ret
        logging.info( '  -- pull --')
        cmd = "git pull"
        ret = Helper.run(cmd)
        logging.info(ret)
        # commit id process
        if len(ck_name_list)==2:
            cmd = "git checkout %s" % ck_name_list[1]
            ck_ret = Helper.run(cmd)
            rc = rc or ck_ret
            

        
    if test_type == 'kptk':
        kptk_repo_generator_core = repo_dir +'/generator_psdk/core/'
        kptk_repo_generator_ucosii = repo_dir +'/ucosii/'
        kptk_repo_generator_freertos = repo_dir +'/freertos/'
        kptk_demo_repo_dir = repo_dir +'/mcu-sdk/'
        index_file1 = repo_dir + '/.git/modules/mcu-sdk/index.lock'
        index_file2 = repo_dir + '/.git/modules/freertos/index.lock'
        index_file3 = repo_dir + '/.git/modules/ucosii/index.lock'
        index_file4 = repo_dir + '/.git/modules/generator_psdk/core/index.lock'
        try:
            os.remove(index_file1)
        except Exception,e:
            pass
        try:
            os.remove(index_file2)
        except Exception,e:
            pass
        try:
            os.remove(index_file3)
        except Exception,e:
            pass
        try:
            os.remove(index_file4)
        except Exception,e:
            pass

        
        logging.info('  -- git update generator core --')
        os.chdir(kptk_repo_generator_core)
        cmd = "git checkout master"
        ret = Helper.run(cmd)
        logging.info(ret)
        rc = rc or ret       
        cmd = "git pull"
        ret = Helper.run(cmd)
        logging.info(ret)
        rc = rc or ret
        
        logging.info('  -- git update generator ucosii --')
        os.chdir(kptk_repo_generator_ucosii)
        cmd = "git checkout master"
        ret = Helper.run(cmd)
        logging.info(ret)
        rc = rc or ret
        cmd = "git pull"
        ret = Helper.run(cmd)
        logging.info(ret)
        rc = rc or ret

        logging.info('  -- git update generator freertos --')
        os.chdir(kptk_repo_generator_freertos)
        cmd = "git checkout master"
        ret = Helper.run(cmd)
        logging.info(ret)
        rc = rc or ret
        cmd = "git pull"
        ret = Helper.run(cmd)
        logging.info(ret)
        rc = rc or ret
        
        logging.info('  -- git update mcu-sdk --')
        os.chdir(kptk_demo_repo_dir)
        ck_name_list = ck_name.split('/')
        Helper.run('git reset --hard')
        Helper.run('git clean -fxd')
        cmd = "git checkout %s" % ck_name_list[0]
        ret = Helper.run(cmd)
        logging.info(ret)
        rc = rc or ret
        cmd = "git pull"
        ret = Helper.run(cmd)
        logging.info(ret)
        # commit id process
        if len(ck_name_list)==2:
            cmd = "git checkout %s" % ck_name_list[1]
            ck_ret = Helper.run(cmd)
            rc = rc or ck_ret

        try:
            main_ck_name = multi_list[1]
        except Exception,e:
            logging.info('main repo use default master branch ')
        else:
            os.chdir(repo_dir)
            ck_name_list = main_ck_name.split('/')
            logging.info( '  -- checkout --')
            cmd = "git checkout %s" % ck_name_list[0]
            ck_ret = Helper.run(cmd)
            logging.info(ck_ret)
            rc = rc or ck_ret
            logging.info( '  -- pull --')
            cmd = "git pull"
            ret = Helper.run(cmd)
            logging.info(ret)
            # commit id or tag process
            if len(ck_name_list)==2:
                cmd = "git checkout %s" % ck_name_list[1]
                ck_ret = Helper.run(cmd)
                rc = rc or ck_ret

    
    if rc:
        logging.info('update repo failed')
        os.chdir(cur_dir)
        return 1
    else:
        logging.info('update repo sucessfully')
        os.chdir(cur_dir)
        return 0
def update_and_patch(repo_dir,ck_name,patch,test_type):
    ret = update_repo(repo_dir,ck_name,test_type)
    if ret:
        return 1
    else:
        repo_patch = repo_dir + '/' + os.path.basename(patch)
        shutil.copyfile(patch,repo_patch)
        cur_dir = os.getcwd()
        os.chdir(repo_dir)
        cmd = "git apply %s" % os.path.basename(patch)
        ret = os.system(cmd)
        if ret:
            logging.info('patch failed')
            os.chdir(cur_dir)
            return 1
        else:
            logging.info('patch sucessfully')
            os.chdir(cur_dir)
            return 0
def Check_repo(repo_dir,repo_name):
    cur_dir = os.getcwd()
    try:
        os.chdir(repo_dir)
    except Exception,e:
        logging.info('Repo dir is not exist.Please Check!')
        return 1
    try:
        output=os.popen('git remote -v').read()
        logging.info('check repo output')
        logging.info(output)
        if repo_name in output:
            os.chdir(cur_dir)
            logging.info('find specified repo')
            return 0
        else:
            os.chdir(cur_dir)
            logging.info(repo_dir+'is not the repo specified')
            return 1# not matched
    except Exception,e:
        logging.info('git cmd output excecption')
        os.chdir(cur_dir)
        return 2# specifed dir is not repo
def Clone_repo(DIR,repo_url,test_type):
    cur_dir = os.getcwd()
    os.chdir(DIR)
    cmd = "git clone %s" % repo_url
    ret = Helper.run(cmd,90)
    if ret:
        logging.info('git clone error')
        os.chdir(cur_dir)
        try:
            shutil.rmtree(DIR)
        except Exception,e:
            logging.info('cannot delete fail-repo,please offline this station')
        return (1,None)
    else:
        logging.info('git clone sucessfully')
        os.chdir(cur_dir)
        lst = os.listdir(DIR)
        for der in lst:
            tmp = DIR + '/' + der
            if os.path.isdir(tmp):
                if Check_repo(tmp,repo_url) == 0:
                    # kptk special process
                    if test_type == 'kptk':
                        try:
                            os.chdir(tmp)
                            cmd = "git submodule init"
                            ret_init = Helper.run(cmd)
                            cmd = "git submodule update"
                            ret_update = Helper.run(cmd)
                            os.chdir(cur_dir)
                        except Exception,e:
                            return (1,None)
                        else:
                            return (0,tmp)
                    else:
                        return (0,tmp)

def get_subdir_list(dir_input):
    subdir_list = []
    if os.path.isdir(dir_input):
        for item in os.listdir(dir_input):
            subdir = dir_input + '/' + item
            if os.path.isdir(subdir):
                subdir_list.append(subdir)
    else:
        return subdir_list
    return subdir_list
    
       
