#!/usr/bin/env python
# coding=utf-8
 
#*******************************************************************
#* Copyright (c) 2013 Freescale Semiconductor Inc.
#* All rights reserved.
#*
#* Use of Freescale code is governed by terms and conditions
#* stated in the accompanying licensing statement.
#* Description: get local config
#*
#* Revision History:
#* -----------------
#* Code Version    YYYY-MM-DD    Author        Description
#* 0.1             2014-2-15    Armand Wang    Create this file
#*******************************************************************
import os, sys
import logging
import socket
import re

file_path = os.path.dirname(os.path.abspath(__file__))
main_path = os.path.join(file_path, '/../')
config_path = main_path + '/config/'
lib_path = main_path + '/lib/'
log_path = main_path + '/log/'
tmp_path = main_path + '/temp/'
sys.path.append(lib_path)
sys.path.append(log_path)
import _winreg
import win32api
import win32con


def GetMac():
    '''
    First connection is default.
    '''
    if os.name == 'nt':
        try:
            ret = ''
            CmdLine = 'ipconfig /all'
            r = os.popen(CmdLine).read()
            if r:
                L = re.findall('Physical Address.*?([0-9,A-F]{2}-[0-9,A-F]{2}-[0-9,A-F]{2}-[0-9,A-F]{2}-[0-9,A-F]{2}-[0-9,A-F]{2})', r)
                if len(L) > 0:
                    ret = L[0]
        except:
            pass
        
    elif os.name == "posix":
        try:
            ret = ''
            CmdLine = 'ifconfig'
            r = os.popen(CmdLine).read()
            if r:
                L = re.findall('HWaddr.*?([0-9,A-F]{2}:[0-9,A-F]{2}:[0-9,A-F]{2}:[0-9,A-F]{2}:[0-9,A-F]{2}:[0-9,A-F]{2})', r)
                if len(L) > 0:
                    ret = L[0]
        except:
            pass
    else:
        pass
    return ret

def Get_IDE_info():
    '''
    return ide info {keil:[{path:xxxxx,version:xxx,'short_path':xxx}],iar:[{path:xxxxx,version:xxx,'short_path':xxx}],cw10:[{path:xxxxx,version:xxx,'short_path':xxx}]}
    or {keil:['not found'],iar:['not found'],cw10:['not found']}
    '''
    # only one keil info on one PC
    ide_info = {}
    ide_info['keil']=[]
    ide_info['iar']=[]
    ide_info['cw10']=[]
    try:
        key = _winreg.OpenKey(_winreg.HKEY_LOCAL_MACHINE,r"SOFTWARE\Keil\Products\MDK")
        uv4_path,type = _winreg.QueryValueEx(key,"Path")
        uv4_version,type = _winreg.QueryValueEx(key,"Version")
        uv4_path = uv4_path.replace('\\','/')
        info_dic = {'path':uv4_path.replace('ARM','UV4'),'version':uv4_version}
        info_dic['short_path'] = win32api.GetShortPathName(uv4_path.replace('ARM','UV4'))
    except Exception,e:
        info_dic = {}
    ide_info['keil'].append(info_dic)

    # may more than one iar info on one PC
    try:
        key = _winreg.OpenKey(_winreg.HKEY_LOCAL_MACHINE,r"SOFTWARE\IAR Systems\Embedded Workbench\5.0\Locations")
        try:
            i=0
            while 1:
                subkey_name = r"SOFTWARE\IAR Systems\Embedded Workbench\5.0\Locations" + "\\" + _winreg.EnumKey(key,i)
                subkey = _winreg.OpenKey(_winreg.HKEY_LOCAL_MACHINE,subkey_name)
                iar_path,type = _winreg.QueryValueEx(subkey,"InstallPath")
                iar_path = iar_path.replace('\\','/')
                try:
                    subkey_name = r"SOFTWARE\IAR Systems\Embedded Workbench\5.0\Locations" + "\\" + _winreg.EnumKey(key,i) + r"\Product Families\ARM\10.EW"
                    subkey = _winreg.OpenKey(_winreg.HKEY_LOCAL_MACHINE,subkey_name)
                    iar_version,type = _winreg.QueryValueEx(subkey,"Version")
                except Exception,e:
                    iar_version = 'unknown'
                info_dic = {'path':iar_path,'version':iar_version}
                info_dic['short_path'] = win32api.GetShortPathName(iar_path)
                ide_info['iar'].append(info_dic)
                i+=1
        except WindowsError,e:
            pass
    except Exception,e:
        pass

    # may more than one cw10 info on one PC
    try:
        key = _winreg.OpenKey(_winreg.HKEY_LOCAL_MACHINE,r"SOFTWARE\Freescale\CodeWarrior\Product Versions")
        try:
            i=0
            while 1:
                subkey_name = r"SOFTWARE\Freescale\CodeWarrior\Product Versions" + "\\" + _winreg.EnumKey(key,i)
                subkey = _winreg.OpenKey(_winreg.HKEY_LOCAL_MACHINE,subkey_name)
                cw10_path,type = _winreg.QueryValueEx(subkey,"Path")
                cw10_path = cw10_path.replace('\\','/')
                cw10_version,type = _winreg.QueryValueEx(subkey,"Version")
                info_dic = {'path':cw10_path,'version':cw10_version}
                info_dic['short_path'] = win32api.GetShortPathName(cw10_path)
                ide_info['cw10'].append(info_dic)
                i+=1
        except WindowsError,e:
            pass
    except Exception,e:
        pass

    # only one kds on pc
    try:
        key = _winreg.OpenKey(_winreg.HKEY_LOCAL_MACHINE,r"SOFTWARE\Freescale\Kinetis Design Studio")
        kds_path,type = _winreg.QueryValueEx(key,"Path")
        kds_version,type = _winreg.QueryValueEx(key,"Version")
        kds_path = kds_path.replace('\\','/')
        info_dic = {'path':kds_path,'version':kds_version}
    except Exception,e:
        pass
    else:
        ide_info['kds'].append(info_dic)

    # arm-gcc,ds5 land blank
    ide_info['gcc_arm'] = []
    ide_info['ds5'] = []
    return ide_info
def GetPCconfig():
    '''
    {'hostname':xxx,'ip':xxx,'mac':xxx}
    '''
    config_dic = {}
    # fullname = socket.getfqdn(socket.gethostname())
    config_dic['hostname']=socket.gethostname()
    # internal ip
    config_dic['ip']=socket.gethostbyname(socket.gethostname())
    config_dic['mac'] = GetMac()
    return config_dic
def Get_STAF_info():
    '''
    return{'exist':'yes','path':xxx,'version':xxx,'short_path':xxx}
    or {'exist':'no','path':xxx,'version':xxx,'short_path':xxx}
    '''
    staf_info = {}
    try:
        try:
            key = win32api.RegOpenKey(win32con.HKEY_LOCAL_MACHINE,r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\STAF", 0, win32con.KEY_ALL_ACCESS)
            staf_path,type = win32api.RegQueryValue(key, "InstallLocation")
            staf_version,type = win32api.RegQueryValue(key, "DisplayVersion")
        except Exception, e:
            key = win32api.RegOpenKey(win32con.HKEY_LOCAL_MACHINE,r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\STAF", 0, win32con.KEY_ALL_ACCESS|win32con.KEY_WOW64_64KEY)
            staf_path,type = win32api.RegQueryValueEx(key, "InstallLocation")
            staf_version,type = win32api.RegQueryValueEx(key, "DisplayVersion")

        staf_info['path'] = staf_path.replace('\\','/')
        staf_info['short_path'] = win32api.GetShortPathName(staf_path.replace('\\','/'))
        staf_info['version'] = staf_version
        staf_info['exist'] = 'yes'
    except Exception,e:
        staf_info['exist'] = 'no'
    return staf_info

def Get_TRACE32_info():
    '''
    return{'exist':'yes','path':xxx,'short_path':xxx}
    or {'exist':'no','path':xxx,'short_path':xxx}
    '''
    trace32_info = {}
    try:
        key = _winreg.OpenKey(_winreg.HKEY_LOCAL_MACHINE,r"SOFTWARE\Microsoft\Windows\CurrentVersion\App Paths\TRACE32")
        trace32_path,type = _winreg.QueryValueEx(key,"Path")
        trace32_info['path'] = trace32_path.replace('\\','/')
        trace32_info['short_path'] = win32api.GetShortPathName(trace32_path.replace('\\','/'))
        trace32_info['exist'] = 'yes'
    except Exception,e:
        trace32_info['exist'] = 'no'
    return trace32_info

def Get_serial_info():
    '''
    return [COM1,COM2,...]
    '''
    serial_info = []
    try:
        key = _winreg.OpenKey(_winreg.HKEY_LOCAL_MACHINE,r"HARDWARE\DEVICEMAP\SERIALCOMM")
        try:
            i=0
            while 1:
                serial_info.append( _winreg.EnumValue(key,i)[1])
                i+=1
        except WindowsError,e:
            pass
    except Exception,e:
        pass
    return serial_info

def Get_BasicSoftware_info():
    '''
    return {'python2.7':'yes','perl':'yes','git':'yes'}
    '''
    software_info = {}
    try:
        key = _winreg.OpenKey(_winreg.HKEY_LOCAL_MACHINE,r"SOFTWARE\Python\PythonCore\2.7")
        software_info['python2.7']='yes'
    except Exception,e:
        software_info['python2.7']='no'
        
    try:
        key = _winreg.OpenKey(_winreg.HKEY_LOCAL_MACHINE,r"SOFTWARE\RubyInstaller")
        software_info['ruby']='yes'
    except Exception,e:
        software_info['ruby']='no'

    try:
        key = _winreg.OpenKey(_winreg.HKEY_LOCAL_MACHINE,r"SOFTWARE\Perl")
        software_info['perl']='yes'
    except Exception,e:
        software_info['perl']='no'

    try:
        CmdLine = 'git --version'
        r = os.popen(CmdLine).read()
        if 'git version' in r and 'msysgit' in r:
            software_info['git']='yes'
        else:
            software_info['git']='no'
    except Exception,e:
        software_info['git']='no'


    return software_info

#print Get_IDE_info()
#print Get_STAF_info()
#print Get_TRACE32_info()
#print Get_BasicSoftware_info()
