# -*- coding: cp936 -*-
#*******************************************************************
#* Copyright (c) 2013 Freescale Semiconductor Inc.
#* All rights reserved.
#*
#* Use of Freescale code is governed by terms and conditions
#* stated in the accompanying licensing statement.
#* Description: config UI guide
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
import urllib
import json



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
from getconfig import Getconfig
from helper import Helper


def get_ide_require(config_file):
    ide_info = {}
    try:
        filename,msg = urllib.urlretrieve('http://dapeng/dapeng/getAllCompiler/',reporthook=None)
        f = open(filename,'r')
        content = f.read()
        f.close()
        data = json.loads(content)
        os.remove(filename)
    except Exception,e:
        print e
        return {'iar':'7.10','cw10':'10.5','uv4':'V5.00','cw10gcc':'10.5','gcc_arm':'unknown','kds':'1.0.1'}
    # list -- 0:cw10,1:cw10gcc,2:iar,3:uv4,4:gcc_arm
    ide_info['cw10'] = str(data[0]['requiredversion'])
    ide_info['cw10gcc'] = str(data[1]['requiredversion'])
    ide_info['iar'] = str(data[2]['requiredversion'])
    ide_info['uv4'] = str(data[3]['requiredversion'])
    ide_info['gcc_arm'] = str(data[4]['requiredversion'])
    ide_info['kds'] = str(data[5]['requiredversion'])
    return ide_info

def Get_station_ide(config_file):
    '''
    only return enabled ide
    {'iar':{'version':xxx,'path':xxx}..}
    '''
    config = Getconfig(config_file)
    ide_info = {}
    ide_enable = config.getAttr_list('IDE')
    if ide_enable['iar']=='yes':
        iar_version = config.getAttr('iar','version')
        iar_path = config.getValue('iar')
        ide_info['iar']= {}
        ide_info['iar']['version']= iar_version
        ide_info['iar']['path'] = iar_path
        
    if ide_enable['uv4']=='yes':
        uv4_version = config.getAttr('uv4','version')
        uv4_path = config.getValue('uv4')
        ide_info['uv4']= {}
        ide_info['uv4']['version']= uv4_version
        ide_info['uv4']['path']= uv4_path
        
    if ide_enable['cw10']=='yes':
        cw10_version = config.getAttr('cw10','version')
        cw10_path = config.getValue('cw10')
        ide_info['cw10']= {}
        ide_info['cw10']['version']= cw10_version
        ide_info['cw10']['path']= cw10_path
        
    if ide_enable['cw10gcc']=='yes':
        cw10gcc_version = config.getAttr('cw10gcc','version')
        cw10gcc_path = config.getValue('cw10gcc')
        ide_info['cw10gcc']= {}
        ide_info['cw10gcc']['version']= cw10gcc_version
        ide_info['cw10gcc']['path']= cw10gcc_path
        
    if ide_enable['gcc_arm']=='yes':
        gcc_arm_version = config.getAttr('gcc_arm','version')
        gcc_arm_path = config.getValue('gcc_arm')
        ide_info['gcc_arm']= {}
        ide_info['gcc_arm']['version']= gcc_arm_version
        ide_info['gcc_arm']['path']= gcc_arm_path
        
    if ide_enable['kds']=='yes':
        kds_version = config.getAttr('kds','version')
        kds_path = config.getValue('kds')
        ide_info['kds']= {}
        ide_info['kds']['version']= kds_version
        ide_info['kds']['path']= kds_path

    return ide_info
    
    
def Get_station_id(config_file):
    '''
    {'ip':xxx,'mac':xxx,'hostname':xxx}
    '''
    config = Getconfig(config_file)
    ip = config.getValue('local_ip')
    mac = config.getValue('local_mac')
    hostname = config.getValue('machine_name')
    return {'ip':ip,'mac':mac,'hostname':hostname}
def Get_station_staf(config_file):
    '''
    return staf dir
    '''
    config = Getconfig(config_file)
    return config.getValue('STAF_dir')

def Get_station_mingw(config_file):
    '''
    return staf dir
    '''
    config = Getconfig(config_file)
    return config.getValue('mingw')

def Get_station_jlink(config_file):
    '''
    return staf dir
    '''
    config = Getconfig(config_file)
    return config.getValue('jlink')


def Get_station_tools(config_file):
    '''
    return {'freemv':None,'freepv':dir}
    '''
    # FreeMV
    info_dic = {}
    config = Getconfig(config_file)
    if config.getAttr('FreeMV','enable')=='yes':
        info_dic['FreeMV'] = config.getValue('FreeMV')
    else:
        info_dic['FreeMV'] = None
    # FreeKV  
    if config.getAttr('FreeKV','enable')=='yes':
        info_dic['FreeKV'] = config.getValue('FreeKV')
    else:
        info_dic['FreeKV'] = None
    # FreeKV_demo
    if config.getAttr('FreeKV_demo','enable')=='yes':
        info_dic['FreeKV_demo'] = config.getValue('FreeKV_demo')
    else:
        info_dic['FreeKV_demo'] = None

    return info_dic

def Get_station_repo(config_file):
    '''
    return (mqx-repo,mqx-incomming,mcu_PSDK_test)

    '''
    config = Getconfig(config_file)
    mqx_repo = config.getValue('new_repo')
    mqx_incoming = config.getValue('new_repo2')
    kptk = config.getValue('new_repo3')
    demo = config.getValue('new_repo4')
    return (mqx_repo,mqx_incoming,kptk,demo)

def Get_station_serial(config_file):
    '''
    return serial list
    {'twrk60d100m':1...}
    '''
    serial_info = {}
    config = Getconfig(config_file)
    device_list = config.getChildTagList('device')
    for device in device_list:
        serial_port = config.getAttr(device,'serial_port')
        serial_info[device] = serial_port
    return serial_info
