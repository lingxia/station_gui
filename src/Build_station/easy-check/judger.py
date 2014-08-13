# -*- coding: cp936 -*-
#*******************************************************************
#* Copyright (c) 2013 Freescale Semiconductor Inc.
#* All rights reserved.
#*
#* Use of Freescale code is governed by terms and conditions
#* stated in the accompanying licensing statement.
#* Description: execute judgement
#*
#* Revision History:
#* -----------------
#* Code Version    YYYY-MM-DD    Author        Description
#* 0.1             2014-02-15    Armand Wang    Create this file
#*******************************************************************
import os, sys,shutil
import logging
import getopt
import datetime
import cPickle as pickle
import subprocess


file_path = os.path.dirname(os.path.abspath(__file__))
main_path = os.path.join(file_path, '../')
config_path = main_path + '/config/'
lib_path = main_path + '/lib/'
log_path = main_path + '/log/'
tmp_path = main_path + '/temp/'
script_path = main_path + '/script/'
history_path = tmp_path + '/history_data/'
sys.path.append(lib_path)
sys.path.append(log_path)
sys.path.append(script_path)
station_type_file = main_path + '/../StationType.pkl'

import wx
from get_local_config import Get_IDE_info,GetPCconfig,Get_STAF_info,Get_TRACE32_info,Get_serial_info,Get_BasicSoftware_info
from getconfig import Getconfig
from get_station_config import Get_station_ide,Get_station_id,Get_station_staf,Get_station_tools,\
     Get_station_repo,Get_station_serial,Get_station_mingw,Get_station_jlink,get_ide_require
from helper import Helper
from serial_helper import SerialHelper

build_config_file = config_path + 'config.xml'
run_config_file = main_path + '../Run_station/config/config.xml'



def check_stationid_result(station_type):
    '''
    0: build station
    1: run station
    return [{'ip':yes,'error_info':xxx},{'mac':yes,'error_info':xxx},{'hostname':xxx,'error_info':xxx}]
    '''
    final_data = []
    local_info = GetPCconfig()
    if station_type == 0:
        config_info = Get_station_id(build_config_file)
    else:
        config_info = Get_station_id(run_config_file)
        
    # ip
    if local_info['ip'] == config_info['ip']:
        final_data.append({'ip':'yes'})
    else:
        error_info = '*** ip in config.xml is '+ config_info['ip'] + ' but DaPeng detect '+ local_info['ip'] + ' !\n\n'
        final_data.append({'ip':'no','error_info':error_info})
    # mac
    if local_info['mac'] == config_info['mac']:
        final_data.append({'mac':'yes'})
    else:
        error_info = '*** mac in config.xml is '+ config_info['mac'] + ' but DaPeng detect '+ local_info['mac'] + ' !\n\n'
        final_data.append({'mac':'no','error_info':error_info})
    
    # hostname
    if local_info['hostname'] == config_info['hostname']:
        final_data.append({'hostname':'yes'})
    else:
        error_info = '*** hostname in config.xml is '+ config_info['hostname'] + ' but DaPeng detect '+ local_info['hostname'] + ' !\n\n'
        final_data.append({'hostname':'no','error_info':error_info})
        
    return final_data
def check_stationstaf_result(station_type):
    '''
    0: build station
    1: run station
    return {'staf':no,'error_info':xxx}
    '''
    if station_type == 0:
        config_info = Get_station_staf(build_config_file)
    else:
        config_info = Get_station_staf(run_config_file)
    config_info = config_info.replace('/','')
    local_info = Get_STAF_info()['short_path'].replace('/','')
    if config_info.lower() == local_info.lower():
        return {'staf':'yes'}
    else:
        return {'staf':'no','error_info':'*** staf dir information error!\n\n'}

def check_stationtools_result(station_type):
    '''
    0: build station
    1: run station
    return {'error':no,'error_info':xxx}
    '''
    info_dic = {}
    info_dic['error_info']=''
    if station_type == 0:
        config_info = Get_station_tools(build_config_file)
    else:
        config_info = Get_station_tools(run_config_file)

    # FreeMV check
    if config_info['FreeMV']!=None:
        feature1 = config_info['FreeMV'] + '/' + 'library'
        feature2 = config_info['FreeMV'] + '/' + 'generator'
        if os.path.isdir(feature1) and os.path.isdir(feature2):
            pass
        else:
            info_dic['error'] = 'yes'
            info_dic['error_info'] = '*** could not find FreeMV!\n\n'
    # FreeKV check
    if config_info['FreeKV']!=None:
        feature1 = config_info['FreeKV'] + '/' + 'plugins'
        feature2 = config_info['FreeKV'] + '/' + 'scripts'
        if os.path.isdir(feature1) and os.path.isdir(feature2):
            pass
        else:
            info_dic['error'] = 'yes'
            info_dic['error_info'] += '*** could not find FreeKV!\n\n'
    # FreeKV_demo check
    if config_info['FreeKV_demo']!=None:
        feature1 = config_info['FreeKV_demo'] + '/' + 'plugins'
        feature2 = config_info['FreeKV_demo'] + '/' + 'scripts'
        if os.path.isdir(feature1) and os.path.isdir(feature2):
            pass
        else:
            info_dic['error'] = 'yes'
            info_dic['error_info'] += '*** could not find FreeKV_demo!\n\n'

    return info_dic

    
def check_stationrepo_result(station_type):
    '''
    0: build station
    1: run station
    '''
    if station_type == 0:
        config_info = Get_station_repo(build_config_file)
    else:
        config_info = Get_station_repo(run_config_file)
    info_dic = {}
    info_dic['error_info'] = ''
    # mqx-repo check
    if config_info[0] != None:
        feature1 = config_info[0] + '/' + 'mqx'
        feature2 = config_info[0] + '/' + 'mcc'
        feature3 = config_info[0] + '/' + 'generator_new'
        if os.path.isdir(feature1) and os.path.isdir(feature2) and os.path.isdir(feature3):
            pass
        else:
            info_dic['error'] = 'yes'
            info_dic['error_info'] += '*** could not find mqx-repo!\n\n'
    # mqx-incoming check
    if config_info[1] != None:
        feature1 = config_info[1] + '/' + 'mqx'
        feature2 = config_info[1] + '/' + 'mcc'
        feature3 = config_info[1] + '/' + 'generator_new'
        if os.path.isdir(feature1) and os.path.isdir(feature2) and os.path.isdir(feature3):
            pass
        else:
            info_dic['error'] = 'yes'
            info_dic['error_info'] += '*** could not find mqx-incoming!\n\n'
    # kptk check
    if config_info[2] != None:
        feature1 = config_info[2] + '/' + 'mcu-sdk'
        feature2 = config_info[2] + '/' + 'generator_psdk'
        if os.path.isdir(feature1) and os.path.isdir(feature2):
            pass
        else:
            info_dic['error'] = 'yes'
            info_dic['error_info'] += '*** could not find kptk repo dir!\n\n'

    # demo check
    if config_info[3] != None:
        feature1 = config_info[3] + '/' + 'bin'
        feature2 = config_info[3] + '/' + 'demos'
        if os.path.isdir(feature1) and os.path.isdir(feature2):
            pass
        else:
            info_dic['error'] = 'yes'
            info_dic['error_info'] += '*** could not find demo repo dir!\n\n'

    return info_dic


def check_stationserial_result(station_type):
    '''
    if one serial port open fail,return {'serial_port':'no','error_info':xxx}
    or {'serial_port':'yes','error_info':''}
    '''
    serial = SerialHelper()
    return_info = {'serial_port':'yes','error_info':''}
    if station_type == 0:
        config_info = Get_station_serial(build_config_file)
    else:
        config_info = Get_station_serial(run_config_file)

    if len(config_info)==0:
        return_info['error_info'] = '*** device not found!\n\n'
        return_info['serial_port'] = 'no'
        return return_info
    for platform,serial_port in config_info.items():
        try:
            serial.open(serial_port)
        except Exception,e:
            return_info['error_info']+='*** serial port ' + serial_port + ' of '+platform + ' not active!\n\n'
            return_info['serial_port'] = 'no'
        else:
            serial.close()
    return return_info

def check_stationide_result(station_type):

    '''
    two return value
    {'iar':yes,'cw10':no,'uv4':'version_error'}
    error_info

    yes: dir,version all right
    no : dir wrong
    version_error: dir right but version wrong
    '''
    
    if station_type == 0:
        config_info = Get_station_ide(build_config_file)
    else:
        config_info = Get_station_ide(run_config_file)
    return_info = {}
    error_info = ''
    version_require = get_ide_require(build_config_file)
    if config_info.has_key('iar'):
        feature = config_info['iar']['path'] + '/common/bin/IarBuild.exe'
        if os.path.isfile(feature):
            if config_info['iar']['version'] == version_require['iar']:
                return_info['iar'] = 'yes'
            else:
                return_info['iar'] = 'version_error'
                error_info += '*** iar version error!'+ version_require['iar'] + ' is required.But current version is ' + config_info['iar']['version'] + '!\n\n'
        else:
            return_info['iar'] = 'no'
            error_info += '*** iar dir error!\n\n'
        
    if config_info.has_key('uv4'):
        feature = config_info['uv4']['path'] + '/UV4.exe'
        if os.path.isfile(feature):
            if config_info['uv4']['version'] == version_require['uv4']:
                return_info['uv4'] = 'yes'
            else:
                return_info['uv4'] = 'version_error'
                error_info += '*** uv4 version error! ' + version_require['uv4'] + ' is required.But current version is ' + config_info['uv4']['version'] + '!\n\n'
        else:
            return_info['uv4'] = 'no'
            error_info += '*** uv4 dir error!\n\n'
        

    if config_info.has_key('cw10'):
        feature = config_info['cw10']['path'] + '/MCU/license.dat'
        if os.path.isfile(feature):
            if config_info['cw10']['version'] == version_require['cw10']:
                return_info['cw10'] = 'yes'
                return_info['cw10gcc'] = 'yes'
            else:
                return_info['cw10'] = 'version_error'
                return_info['cw10gcc'] = 'version_error'
                error_info += '*** cw10 version error! ' + version_require['cw10'] + ' is required.But current version is ' + config_info['cw10']['version'] + '!\n\n'
        else:
            return_info['cw10'] = 'no'
            return_info['cw10gcc'] = 'no'
            error_info += '*** cw10 dir error,could not find CW license file!\n\n'
    
    if config_info.has_key('gcc_arm'):
        feature = config_info['gcc_arm']['path'] + '/arm-none-eabi/bin'
        if os.path.isdir(feature):
            if config_info['gcc_arm']['version'] == version_require['gcc_arm']:
                return_info['gcc_arm'] = 'yes'
            else:
                return_info['gcc_arm'] = 'version_error'
                error_info += '*** gcc_arm version error! ' + version_require['gcc_arm'] + ' is required.But current version is ' + config_info['gcc_arm']['version'] + '!\n\n'
        else:
            return_info['gcc_arm'] = 'no'
            error_info += '*** gcc_arm dir error!\n\n'

    if config_info.has_key('kds'):
        feature = config_info['kds']['path'] + '/eclipse'
        if os.path.isdir(feature):
            if config_info['kds']['version'] == version_require['kds']:
                return_info['kds'] = 'yes'
            else:
                return_info['kds'] = 'version_error'
                error_info += '*** kds version error! ' + version_require['kds'] + ' is required.But current version is ' + config_info['kds']['version'] + '!\n\n'
        else:
            return_info['kds'] = 'no'
            error_info += '*** kds dir error!\n\n'
            
    return return_info,error_info

def check_syspath_result(station_type):
    buid_info = os.popen('echo %DPC_BUILD%').read()
    run_info = os.popen('echo %DPC_RUN%').read()
    if station_type == 0:
        if 'Build_station' in buid_info:
            return 0
        else:
            return 1
    else:
        if 'Run_station' in run_info:
            return 0
        else:
            return 1

def check_stafcfg_result(station_type):
    '''
    0: build station
    1: run station
    return 0/1
    '''
    if station_type == 0:
        config_info = Get_station_staf(build_config_file)
        config_build = Getconfig(build_config_file)
        scheduler = config_build.getValue('Scheduler_IP')
    else:
        config_info = Get_station_staf(run_config_file)
        config_run = Getconfig(run_config_file)
        scheduler = config_run.getValue('Scheduler_IP')
    staf_cfg_file = config_info + '/bin/STAF.cfg'
    if os.path.isfile(staf_cfg_file):
        f = open(staf_cfg_file,'r')
        content = f.read()
        f.close()
        if scheduler in content:
            return 0
        else:
            return 1
    else:
        return 1

def check_mingw_result(station_type):
    '''
    0: build station
    1: run station
    return 0/1
    '''
    if station_type == 0:
        config_info = Get_station_mingw(build_config_file)
    else:
        config_info = Get_station_mingw(run_config_file)
    make_file = config_info + '/bin/mingw32-make.exe'
    if os.path.isfile(make_file):
        return 0
    else:
        return 1

def check_jlink_result(station_type):
    '''
    0: build station
    1: run station
    return 0/1
    '''
    if station_type == 0:
        config_info = Get_station_jlink(build_config_file)
    else:
        config_info = Get_station_jlink(run_config_file)
    jlink_file = config_info + '/JLink.exe'
    if os.path.isfile(jlink_file):
        return 0
    else:
        return 1
