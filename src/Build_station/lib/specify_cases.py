#!/usr/bin/env python
# coding=utf-8
 
#*******************************************************************
#* Copyright (c) 2013 Freescale Semiconductor Inc.
#* All rights reserved.
#*
#* Use of Freescale code is governed by terms and conditions
#* stated in the accompanying licensing statement.
#* Description: parse applist.yml and specify case
#*
#* Revision History:
#* -----------------
#* Code Version    YYYY-MM-DD    Author        Description
#* 0.1             2013-12-07    Armand Wang    Create this file
#*******************************************************************
import os,sys
file_path = os.path.dirname(os.path.abspath(__file__))
main_path = os.path.join(file_path, '../')
lib_path = main_path + '/lib/'
sys.path.append(lib_path)
import yaml
import logging

def Selector(applist_file,cases_dict):
    '''
    input yml applist file and case dictionary.like{mqx_hello:0,mqx_event:1}
    modify the applist according to cases_dict
    such as:
    ret = Selector('c:/app.yml',{'mqx_hello':14,'mqx_event':15,'mqx_lwdemo':16,})
    if there is case valid,function return 1
    '''
    f = open(applist_file)
    app_list = yaml.load(f)
    f.close()
    app_list_tmp = app_list
    case_list =[]
    def specify_one(casename,value):
        flag =1
        for group_num,app_list_group in enumerate(app_list):
            for app_list_group_name, app_list_group_val in app_list_group.items():
                for group_internal_num,app_list_item in enumerate(app_list_group_val):
                    for app_name, if_enable in app_list_item.items():
                        if app_name == casename:
                            if if_enable != 3:
                                app_list_tmp[group_num][app_list_group_name][group_internal_num][app_name]=value
                                flag = 0
                        else:
                            if app_name not in case_list:
                                app_list_tmp[group_num][app_list_group_name][group_internal_num][app_name]=0
        return flag
    case_valid =0
    for case,enable in cases_dict.items():
        case_list.append(case)
    for case,enable in cases_dict.items():
        if specify_one(case,enable):
            logging.info('This platform do not support: %s'%case)
            case_valid = 1
    handle = open(applist_file,'w')
    yaml.dump(app_list_tmp,handle)
    return case_valid
