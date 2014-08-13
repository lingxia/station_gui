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
from get_local_config import Get_BasicSoftware_info
from judger import check_stationid_result,check_stationstaf_result,check_stationtools_result,\
     check_stationrepo_result,check_stationserial_result,check_stationide_result,check_syspath_result,\
     check_stafcfg_result,check_mingw_result,check_jlink_result
from helper import Helper

build_config_file = config_path + 'config.xml'
run_config_file = main_path + '../Run_station/config/config.xml'

pass_pic = file_path + '/pic/pass.jpg'
fail_pic = file_path + '/pic/fail.jpg'
unknown_pic = file_path + '/pic/unknown.jpg'
check_result = 0


def get_pass_pic():
    image=wx.Image(pass_pic,wx.BITMAP_TYPE_JPEG)
    w = image.GetWidth()
    h = image.GetHeight()
    image2 = image.Scale(w/4, h/4)
    temp=image2.ConvertToBitmap()
    return temp

def get_fail_pic():
    image=wx.Image(fail_pic,wx.BITMAP_TYPE_JPEG)
    w = image.GetWidth()
    h = image.GetHeight()
    image2 = image.Scale(w/4, h/4)
    temp=image2.ConvertToBitmap()
    return temp

def get_unknown_pic():
    image=wx.Image(unknown_pic,wx.BITMAP_TYPE_JPEG)
    w = image.GetWidth()
    h = image.GetHeight()
    image2 = image.Scale(w/4, h/4)
    temp=image2.ConvertToBitmap()
    return temp

class SubclassDialog_station(wx.Dialog):
    def __init__(self):
        wx.Dialog.__init__(self, None, -1, 'DaPeng: message', 
                size=(300, 150),pos=(650,350))
        text = port_label = wx.StaticText(self, -1, "Error could be ingnored safely?",pos=(40,30))
        font = wx.Font(12,wx.NORMAL,wx.NORMAL, wx.NORMAL)
        text.SetFont(font)
        okButton = wx.Button(self, wx.ID_OK, 'OK', pos=(70, 80))
        cancelButton = wx.Button(self, wx.ID_CANCEL, 'Cancel',pos=(170, 80))
        cancelButton.SetDefault()




class EnvFrame(wx.Frame): 
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, 'DaPeng Environment Verificaiton',size=(600,800),pos=(300,50),style=wx.DEFAULT_FRAME_STYLE)
        panel = wx.Panel(self)
        error_info = 'Error infomation:\n\n'
        
        # Basic Software check
        basic_software = Get_BasicSoftware_info()
        self.staticLine1 = wx.StaticLine(panel,pos=(20,20),size=(500,1))
         
        # --python
        python_label = wx.StaticText(panel, -1, "Python2.7:",pos=(20,35))
        font = wx.Font(14,wx.NORMAL,wx.NORMAL, wx.NORMAL)
        python_label.SetFont(font)
        if basic_software['python2.7'] == 'yes':
            self.bmp_python = wx.StaticBitmap(panel,bitmap=get_pass_pic(),pos=(140,35),size=(40,24))
        else:
            self.bmp_python = wx.StaticBitmap(panel,bitmap=get_fail_pic(),pos=(140,35),size=(40,24))
            error_info += 'python version 2.7.x is required!\n'

        # --perl
        perl_label = wx.StaticText(panel, -1, "Perl:",pos=(20,70))
        perl_label.SetFont(font)
        if basic_software['perl'] == 'yes':
            self.bmp_perl = wx.StaticBitmap(panel,bitmap=get_pass_pic(),pos=(140,70),size=(40,24))
        else:
            self.bmp_perl = wx.StaticBitmap(panel,bitmap=get_fail_pic(),pos=(140,70),size=(40,24))
            error_info += 'perl not found!\n'

        # --Git
        git_label = wx.StaticText(panel, -1, "Git:",pos=(20,105))
        git_label.SetFont(font)
        if basic_software['git'] == 'yes':
            self.bmp_git = wx.StaticBitmap(panel,bitmap=get_pass_pic(),pos=(140,105),size=(40,24))
        else:
            self.bmp_git = wx.StaticBitmap(panel,bitmap=get_fail_pic(),pos=(140,105),size=(40,24))
            error_info += 'git not found!!\n' 

        # --ruby
        git_label = wx.StaticText(panel, -1, "ruby:",pos=(20,140))
        git_label.SetFont(font)
        if basic_software['ruby'] == 'yes':
            self.bmp_ruby = wx.StaticBitmap(panel,bitmap=get_pass_pic(),pos=(140,140),size=(40,24))
        else:
            self.bmp_ruby = wx.StaticBitmap(panel,bitmap=get_fail_pic(),pos=(140,140),size=(40,24))
            error_info += 'ruby not found!!\n' 

        self.staticLine2 = wx.StaticLine(panel,pos=(20,180),size=(500,1))






        # communication point check
        if is_build:
            addr_check = check_stationid_result(0)
        else:
            addr_check = check_stationid_result(1)
        # --ip
        ip_label = wx.StaticText(panel, -1, "IP:",pos=(300,35))
        font = wx.Font(14,wx.NORMAL,wx.NORMAL, wx.NORMAL)
        ip_label.SetFont(font)
        if addr_check[0]['ip'] == 'yes':
            self.bmp_ip = wx.StaticBitmap(panel,bitmap=get_pass_pic(),pos=(420,35),size=(40,24))
        else:
            self.bmp_ip = wx.StaticBitmap(panel,bitmap=get_fail_pic(),pos=(420,35),size=(40,24))
            error_info += addr_check[0]['error_info']

        # --mac
        mac_label = wx.StaticText(panel, -1, "MAC:",pos=(300,70))
        font = wx.Font(14,wx.NORMAL,wx.NORMAL, wx.NORMAL)
        mac_label.SetFont(font)
        if addr_check[1]['mac'] == 'yes':
            self.bmp_mac = wx.StaticBitmap(panel,bitmap=get_pass_pic(),pos=(420,70),size=(40,24))
        else:
            self.bmp_mac = wx.StaticBitmap(panel,bitmap=get_fail_pic(),pos=(420,70),size=(40,24))
            error_info += addr_check[1]['error_info']

        # --hostname
        hostname_label = wx.StaticText(panel, -1, "HostName:",pos=(300,105))
        font = wx.Font(14,wx.NORMAL,wx.NORMAL, wx.NORMAL)
        hostname_label.SetFont(font)
        if addr_check[2]['hostname'] == 'yes':
            self.bmp_hostname = wx.StaticBitmap(panel,bitmap=get_pass_pic(),pos=(420,105),size=(40,24))
        else:
            self.bmp_hostname = wx.StaticBitmap(panel,bitmap=get_fail_pic(),pos=(420,105),size=(40,24))
            error_info += addr_check[2]['error_info']







        #functional point check
        font = wx.Font(14,wx.NORMAL,wx.NORMAL, wx.NORMAL)
        build_label = wx.StaticText(panel, -1, "build:",pos=(140,200))
        run_label = wx.StaticText(panel, -1, "run:",pos=(230,200))

        # --tools
        freemv_label = wx.StaticText(panel, -1, "tools:",pos=(20,230))
        freemv_label.SetFont(font)
        build_label.SetFont(font)
        run_label.SetFont(font)
        if is_build:
            freemv_info = check_stationtools_result(0)
            if freemv_info.has_key('error'):
                self.bmp_freemv_build = wx.StaticBitmap(panel,bitmap=get_fail_pic(),pos=(140,230),size=(40,24))
                error_info += freemv_info['error_info']
            else:
                self.bmp_freemv_build = wx.StaticBitmap(panel,bitmap=get_pass_pic(),pos=(140,230),size=(40,24))
        if is_run:
            freemv_info = check_stationtools_result(1)
            if freemv_info.has_key('error'):
                self.bmp_freemv_run = wx.StaticBitmap(panel,bitmap=get_fail_pic(),pos=(230,230),size=(40,24))
                error_info += freemv_info['error_info']
            else:
                self.bmp_freemv_run = wx.StaticBitmap(panel,bitmap=get_pass_pic(),pos=(230,230),size=(40,24))
        # --system path
        syspath_label = wx.StaticText(panel, -1, "SYS_PATH:",pos=(300,230))
        syspath_label.SetFont(font)
        if is_build:
            if check_syspath_result(0) == 0:
                self.bmp_path_build = wx.StaticBitmap(panel,bitmap=get_pass_pic(),pos=(420,230),size=(40,24))
            else:
                self.bmp_path_build = wx.StaticBitmap(panel,bitmap=get_fail_pic(),pos=(420,230),size=(40,24))
                error_info += '***can not find Build station system path!\n\n'
        if is_run:
            if check_syspath_result(1) == 0:
                self.bmp_path_run = wx.StaticBitmap(panel,bitmap=get_pass_pic(),pos=(480,230),size=(40,24))
            else:
                self.bmp_path_run = wx.StaticBitmap(panel,bitmap=get_fail_pic(),pos=(480,230),size=(40,24))
                error_info += '***can not find Run station system path!\n\n'
                
                
        # --staf
        staf_label = wx.StaticText(panel, -1, "STAF:",pos=(20,265))
        staf_label.SetFont(font)
        if is_build:
            staf_info = check_stationstaf_result(0)
            if staf_info['staf'] == 'yes':
                self.bmp_staf_build = wx.StaticBitmap(panel,bitmap=get_pass_pic(),pos=(140,265),size=(40,24))
            else:
                self.bmp_staf_build = wx.StaticBitmap(panel,bitmap=get_fail_pic(),pos=(140,265),size=(40,24))
                error_info += staf_info['error_info']
        if is_run:
            staf_info = check_stationstaf_result(1)
            if staf_info['staf'] == 'yes':
                self.bmp_staf_run = wx.StaticBitmap(panel,bitmap=get_pass_pic(),pos=(230,265),size=(40,24))
            else:
                self.bmp_staf_run = wx.StaticBitmap(panel,bitmap=get_fail_pic(),pos=(230,265),size=(40,24))
                error_info += staf_info['error_info']

        # -- staf cfg
        staf_env_label = wx.StaticText(panel, -1, "STAF_ENV:",pos=(300,265))
        staf_env_label.SetFont(font)
        if is_build:
            if check_stafcfg_result(0) == 0:
                self.bmp_cfg_build = wx.StaticBitmap(panel,bitmap=get_pass_pic(),pos=(420,265),size=(40,24))
            else:
                self.bmp_cfg_build = wx.StaticBitmap(panel,bitmap=get_fail_pic(),pos=(420,265),size=(40,24))
                error_info += '***STAF permission config error!\n\n'
        if is_run:
            if check_stafcfg_result(1) == 0:
                self.bmp_cfg_run = wx.StaticBitmap(panel,bitmap=get_pass_pic(),pos=(480,265),size=(40,24))
            else:
                self.bmp_cfg_run = wx.StaticBitmap(panel,bitmap=get_fail_pic(),pos=(480,265),size=(40,24))
                error_info += '***STAF permission config error!\n\n'


        # --repo
        repo_label = wx.StaticText(panel, -1, "repository:",pos=(20,300))
        repo_label.SetFont(font)
        if is_build:
            repo_info = check_stationrepo_result(0)
            if repo_info.has_key('error'):
                self.bmp_repo = wx.StaticBitmap(panel,bitmap=get_fail_pic(),pos=(140,300),size=(40,24))
                error_info += repo_info['error_info']
            else:
                self.bmp_repo = wx.StaticBitmap(panel,bitmap=get_pass_pic(),pos=(140,300),size=(40,24))
                
        # --serial
        
        ser_label = wx.StaticText(panel, -1, "SerialPort:",pos=(20,335))
        ser_label.SetFont(font)
        if is_run:
            ser_info = check_stationserial_result(1)
            if ser_info['serial_port'] == 'yes':
                self.bmp_ser = wx.StaticBitmap(panel,bitmap=get_pass_pic(),pos=(230,335),size=(40,24))
            else:
                self.bmp_ser = wx.StaticBitmap(panel,bitmap=get_fail_pic(),pos=(230,335),size=(40,24))
                error_info += ser_info['error_info']
                
        self.staticLine3 = wx.StaticLine(panel,pos=(20,380),size=(500,1))


        # --ide info
        if is_build:
            whole_info = check_stationide_result(0)
        else:
            whole_info = check_stationide_result(1)
        ide_info = whole_info[0]
        error_info += whole_info[1]

        iar_label = wx.StaticText(panel, -1, "IAR:",pos=(20,400))
        iar_label.SetFont(font)
        if ide_info.has_key('iar'):
            if ide_info['iar'] == 'yes':
                self.bmp_iar = wx.StaticBitmap(panel,bitmap=get_pass_pic(),pos=(140,400),size=(40,24))
            elif ide_info['iar'] == 'version_error':
                self.bmp_iar = wx.StaticBitmap(panel,bitmap=get_unknown_pic(),pos=(140,400),size=(40,24))
            else:
                self.bmp_iar = wx.StaticBitmap(panel,bitmap=get_fail_pic(),pos=(140,400),size=(40,24))

        uv4_label = wx.StaticText(panel, -1, "UV4:",pos=(20,435))
        uv4_label.SetFont(font)
        if ide_info.has_key('uv4'):
            if ide_info['uv4'] == 'yes':
                self.bmp_uv4 = wx.StaticBitmap(panel,bitmap=get_pass_pic(),pos=(140,435),size=(40,24))
            elif ide_info['uv4'] == 'version_error':
                self.bmp_uv4 = wx.StaticBitmap(panel,bitmap=get_unknown_pic(),pos=(140,435),size=(40,24))
            else:
                self.bmp_uv4 = wx.StaticBitmap(panel,bitmap=get_fail_pic(),pos=(140,435),size=(40,24))

        cw10_label = wx.StaticText(panel, -1, "CW10:",pos=(20,470))
        cw10_label.SetFont(font)
        if ide_info.has_key('cw10'):
            if ide_info['cw10'] == 'yes':
                self.bmp_cw10 = wx.StaticBitmap(panel,bitmap=get_pass_pic(),pos=(140,470),size=(40,24))
            elif ide_info['cw10'] == 'version_error':
                self.bmp_cw10 = wx.StaticBitmap(panel,bitmap=get_unknown_pic(),pos=(140,470),size=(40,24))
            else:
                self.bmp_cw10 = wx.StaticBitmap(panel,bitmap=get_fail_pic(),pos=(140,470),size=(40,24))
        
        
        gcc_label = wx.StaticText(panel, -1, "Gcc-Arm:",pos=(20,505))
        gcc_label.SetFont(font)
        if ide_info.has_key('gcc_arm'):
            if ide_info['gcc_arm'] == 'yes':
                self.bmp_gcc_arm = wx.StaticBitmap(panel,bitmap=get_pass_pic(),pos=(140,505),size=(40,24))
            elif ide_info['gcc_arm'] == 'version_error':
                self.bmp_gcc_arm = wx.StaticBitmap(panel,bitmap=get_unknown_pic(),pos=(140,505),size=(40,24))
            else:
                self.bmp_gcc_arm = wx.StaticBitmap(panel,bitmap=get_fail_pic(),pos=(140,505),size=(40,24))
            # mingw check
            mingw_label = wx.StaticText(panel, -1, "MINGW:",pos=(300,300))
            mingw_label.SetFont(font)
            if is_build:
                if check_mingw_result(0) == 0:
                    self.bmp_mingw_build = wx.StaticBitmap(panel,bitmap=get_pass_pic(),pos=(420,300),size=(40,24))
                else:
                    self.bmp_mingw_build = wx.StaticBitmap(panel,bitmap=get_fail_pic(),pos=(420,300),size=(40,24))
                    error_info += '***mingw dir error!\n\n'
            if is_run:
                if check_mingw_result(1) == 0:
                    self.bmp_mingw_run = wx.StaticBitmap(panel,bitmap=get_pass_pic(),pos=(480,300),size=(40,24))
                else:
                    self.bmp_mingw_run = wx.StaticBitmap(panel,bitmap=get_fail_pic(),pos=(480,300),size=(40,24))
                    error_info += '***mingw dir error!\n\n'
                # check jlink(since jlink dir may be used in gbd)
                jlink_label = wx.StaticText(panel, -1, "JLINK:",pos=(300,335))
                jlink_label.SetFont(font)
                if check_jlink_result(1) == 0:
                    self.bmp_jlink_run = wx.StaticBitmap(panel,bitmap=get_pass_pic(),pos=(480,335),size=(40,24))
                else:
                    self.bmp_jlink_run = wx.StaticBitmap(panel,bitmap=get_unknown_pic(),pos=(480,335),size=(40,24))
                    error_info += '***jlink dir error!(if do not use gdb as debugger,could be ignored safely.)\n\n'

        kds_label = wx.StaticText(panel, -1, "KDS:",pos=(300,400))
        kds_label.SetFont(font)
        if ide_info.has_key('kds'):
            if ide_info['kds'] == 'yes':
                self.bmp_kds = wx.StaticBitmap(panel,bitmap=get_pass_pic(),pos=(420,400),size=(40,24))
            elif ide_info['kds'] == 'version_error':
                self.bmp_kds = wx.StaticBitmap(panel,bitmap=get_unknown_pic(),pos=(420,400),size=(40,24))
            else:
                self.bmp_kds = wx.StaticBitmap(panel,bitmap=get_fail_pic(),pos=(420,400),size=(40,24))


        self.staticLine4 = wx.StaticLine(panel,pos=(20,550),size=(500,1))

        # error info
        content=wx.TextCtrl(panel,pos=(20,570),size=(500,120),style=wx.TE_MULTILINE|wx.HSCROLL)
        content.SetValue(error_info)
        # finish botton

        
        self.button = wx.Button(panel, label='OK', pos=(450, 700), size=(50, 25))
        self.Bind(wx.EVT_BUTTON, self.finish, self.button)
        global check_result
        if error_info != 'Error infomation:\n\n':
            check_result = 5

        
        
    def finish(self,event):
        global check_result
        if check_result:
            dialog = SubclassDialog_station()
            result = dialog.ShowModal()
            if result == wx.ID_OK:
                check_result = 0
            dialog.Destroy()
        self.Close()




        
                
if os.path.isfile(station_type_file):
    f = file(station_type_file,'rb')
    station_info = pickle.load(f)
    # {'build_station':'yes','run_Station':'no'}
    if station_info['build_station'] == 'yes':
        is_build = True
    else:
        is_build = False
    if station_info['run_station'] == 'yes':
        is_run = True
    else:
        is_run = False
else:
    is_build = True
    is_run = True

app = wx.App()
frame = EnvFrame(parent=None, id=-1)
frame.Show()
app.MainLoop()
os._exit(check_result)
