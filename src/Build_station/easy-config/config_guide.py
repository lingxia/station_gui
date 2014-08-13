
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
import time


file_path = os.path.dirname(os.path.abspath(__file__))
main_path = os.path.join(file_path, '../')
updater_path = main_path + '../../updater/'
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
version_file = updater_path + 'version'
configured_version_file = updater_path + 'configured_version'


import wx
import win32api
from get_local_config import Get_IDE_info,GetPCconfig,Get_STAF_info,Get_TRACE32_info,Get_serial_info,Get_DP_info,Get_Gcc_info
from getconfig import Getconfig
from helper import Helper
from stafer import STAFer
from common import reset_staf,start_staf,end_staf


frame_width = 500
frame_height = 410
pre_button_width = 350
af_button_width = 420
workflow_button_height = 260
static_line_height = 290
hint_width = 20
hint_height = 300
build_station = False
run_station = False
build_status = 'None'
run_status = 'None'
freemv_platform_list = []
freekv_platform_list = []
freekv_demo_platform_list = []
freemv_dir_run = ''
freekv_dir_run = ''
freekv_demo_dir_run = ''
oobe_enable = 'no'
kptk_enable = 'no'
demo_enable = 'no'
build_private = 'no'
run_private = 'no'
run_token = ''


#*******************************************************************
#* DaPeng Message Frame
#* 
#* 
#*******************************************************************

class SubclassDialog_station(wx.Dialog):
    def __init__(self):
        wx.Dialog.__init__(self, None, -1, 'DaPeng: message', 
                size=(300, 150),pos=(650,350))
        text = port_label = wx.StaticText(self, -1, "Station Type is required!",pos=(60,30))
        font = wx.Font(12,wx.NORMAL,wx.NORMAL, wx.NORMAL)
        text.SetFont(font)
        okButton = wx.Button(self, wx.ID_OK, 'OK', pos=(110, 80))
        okButton.SetDefault()
class SubclassDialog_statuscheck(wx.Dialog):
    def __init__(self):
        wx.Dialog.__init__(self, None, -1, 'DaPeng: message', 
                size=(300, 150),pos=(650,350))
        text = port_label = wx.StaticText(self, -1, "Please log off first!",pos=(60,30))
        font = wx.Font(12,wx.NORMAL,wx.NORMAL, wx.NORMAL)
        text.SetFont(font)
        okButton = wx.Button(self, wx.ID_OK, 'OK', pos=(110, 80))
        okButton.SetDefault()
class SubclassDialog(wx.Dialog):
    def __init__(self):
        wx.Dialog.__init__(self, None, -1, 'DaPeng: message', 
                size=(300, 150),pos=(650,350))
        text = port_label = wx.StaticText(self, -1, "Platform added sucessfully!",pos=(40,30))
        font = wx.Font(12,wx.NORMAL,wx.NORMAL, wx.NORMAL)
        text.SetFont(font)
        okButton = wx.Button(self, wx.ID_OK, 'OK', pos=(110, 80))
        okButton.SetDefault()
       
class SubclassDialog_config(wx.Dialog):
    def __init__(self):
        global build_status
        global run_status
        wx.Dialog.__init__(self, None, -1, 'DaPeng: message', 
                size=(300, 150),pos=(650,350))
        text = port_label = wx.StaticText(self, -1, "Build station : " + build_status,pos=(85,20))
        text2 = port_label = wx.StaticText(self, -1, "Run station : " + run_status,pos=(85,50))
        okButton = wx.Button(self, wx.ID_OK, 'OK', pos=(110, 80))
        okButton.SetDefault()


#*******************************************************************
#* Station Type selection Frame
#* 
#* 
#*******************************************************************

class stationFrame(wx.Frame): 
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, 'DaPeng Configuration Guide  :  station type',size=wx.DefaultSize,pos=(600,300),style=wx.DEFAULT_FRAME_STYLE)
        panel = wx.Panel(self)
        
        self.staticLine1 = wx.StaticLine(panel,pos=(20,20),size=(350,1))
        self.staticLine2 = wx.StaticLine(panel,pos=(20,190),size=(350,1))

        
        self.build_checkbox = wx.CheckBox(panel, -1, 'Build Station',pos=(100,40),size=(140,60))
        font = wx.Font(14,wx.NORMAL,wx.NORMAL, wx.NORMAL)
        self.build_checkbox.SetFont(font)
        self.build_attr = wx.CheckBox(panel, -1, 'private',pos=(250,65))
        
        self.run_checkbox = wx.CheckBox(panel, -1, 'Run Station',pos=(100,80),size=(140,60))
        font = wx.Font(14,wx.NORMAL,wx.NORMAL, wx.NORMAL)
        self.run_checkbox.SetFont(font)
        self.run_attr = wx.CheckBox(panel, -1, 'private',pos=(250,105))
        
        # next button
        self.button2 = wx.Button(panel, label='>>', pos=(320, 150), size=(50, 25))
        self.Bind(wx.EVT_BUTTON, self.gonext, self.button2)

    def gonext(self, event):
        station_type_info = {'build_station':'no','run_station':'no'}
        global build_station
        build_station=self.build_checkbox.GetValue()
        if build_station:
            station_type_info['build_station']= 'yes'
        global run_station
        run_station = self.run_checkbox.GetValue()
        if run_station:
            station_type_info['run_station']='yes'
            
        global build_private
        global run_private
        if self.build_attr.GetValue():
            build_private = 'yes'
        if self.run_attr.GetValue():
            run_private = 'yes'
        config.setAttr('token','private',build_private)
            
        # record station type
        f = file(station_type_file,'wb')
        pickle.dump(station_type_info,f,True)
        f.close()
        if build_station or run_station:
            frame2 = RepoFrame(parent=None, id=-1)
            frame2.Show()
            self.Close(True)
        else:
            dialog = SubclassDialog_station()
            result = dialog.ShowModal()
            if result == wx.ID_OK:
                dialog.Destroy()
                
#*******************************************************************
#* Code Repository directory selection Frame
#* 
#* 
#*******************************************************************


class RepoFrame(wx.Frame): 
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, 'DaPeng Configuration Guide  :  code repository & token',size=(frame_width,frame_height),pos=(600,300),style=wx.DEFAULT_FRAME_STYLE)
        panel = wx.Panel(self)
        self.staticLine1 = wx.StaticLine(panel,pos=(20,20),size=(450,1))
        self.staticLine2 = wx.StaticLine(panel,pos=(20,static_line_height),size=(450,1))
        
        # repo label
        repo_label = wx.StaticText(panel, -1, "mqx-repo ",(20,40))
        font = wx.Font(14,wx.NORMAL,wx.NORMAL, wx.NORMAL)
        repo_label.SetFont(font)
        repo_label2 = wx.StaticText(panel, -1, "mqx-incomming ",(20,70))
        repo_label2.SetFont(font)
        repo_label3 = wx.StaticText(panel, -1, "mcu_PSDK_test ",(20,100))
        repo_label3.SetFont(font)
        repo_label4 = wx.StaticText(panel, -1, "mcu-sdk ",(20,130))
        repo_label4.SetFont(font)

        repo_label5 = wx.StaticText(panel, -1, "build_token ",(20,190))
        repo_label5.SetFont(font)
        repo_label6 = wx.StaticText(panel, -1, "run_token ",(20,220))
        repo_label6.SetFont(font)


        # repo dir
        self.repo_dir=wx.TextCtrl(panel,pos=(165,40),size=(210,25))
        self.repo_dir2=wx.TextCtrl(panel,pos=(165,70),size=(210,25))
        self.repo_dir3=wx.TextCtrl(panel,pos=(165,100),size=(210,25))
        self.repo_dir4=wx.TextCtrl(panel,pos=(165,130),size=(210,25))
        self.repo_dir5=wx.TextCtrl(panel,pos=(165,190),size=(210,25))
        self.repo_dir6=wx.TextCtrl(panel,pos=(165,220),size=(210,25))
        
        # select buttoon
        self.button = wx.Button(panel, label='select', pos=(380, 40), size=(50, 25))
        self.Bind(wx.EVT_BUTTON, self.choosedir, self.button)
        self.button4 = wx.Button(panel, label='select', pos=(380, 70), size=(50, 25))
        self.Bind(wx.EVT_BUTTON, self.choosedir2, self.button4)
        self.button5 = wx.Button(panel, label='select', pos=(380, 100), size=(50, 25))
        self.Bind(wx.EVT_BUTTON, self.choosedir3, self.button5)
        self.button6 = wx.Button(panel, label='select', pos=(380, 130), size=(50, 25))
        self.Bind(wx.EVT_BUTTON, self.choosedir4, self.button6)

        # next button
        self.button2 = wx.Button(panel, label='>>', pos=(af_button_width, workflow_button_height), size=(50, 25))
        self.Bind(wx.EVT_BUTTON, self.gonext, self.button2)
        # pre button
        self.button3 = wx.Button(panel, label='<<', pos=(pre_button_width, workflow_button_height), size=(50, 25))
        self.Bind(wx.EVT_BUTTON, self.gopre, self.button3)

        # hint message
        hint=wx.TextCtrl(panel,pos=(hint_width,hint_height),size=(450,70),style=wx.TE_MULTILINE|wx.HSCROLL)
        content = 'Prompt Message:\n'
        content += '** Please make sure no blank character in repository path.\n'
        content += '** repository attribute must be read-only !!(do not need acceses right)\n'
        content += '** mqx-repo/mqx-incomming repository : MQX OOBE test\n'
        content += '** mcu_PSDK_test repository : kptk\n'
        content += '** mcu-sdk repository : ksdk demo\n'
        content += '** if above repository does not exist, skip directly.\n'
        content += '** token is password to use current resource as private machine.\n'
        hint.SetValue(content)

    def gopre(self,event):
        frame_pre_repo = stationFrame(parent=None, id=-1)
        frame_pre_repo.Show()
        self.Close(True)

    def choosedir(self, event):
        # dialog
        dialog = wx.DirDialog(None, 'Choose MQX dir:',style=wx.DD_DEFAULT_STYLE | wx.DD_NEW_DIR_BUTTON)
        if dialog.ShowModal() == wx.ID_OK:
            self.repo_dir.SetValue(dialog.GetPath().replace('\\','/'))
            dialog.Destroy()
    def choosedir2(self, event):
        # dialog
        dialog = wx.DirDialog(None, 'Choose MQX dir:',style=wx.DD_DEFAULT_STYLE | wx.DD_NEW_DIR_BUTTON)
        if dialog.ShowModal() == wx.ID_OK:
            self.repo_dir2.SetValue(dialog.GetPath().replace('\\','/'))
            dialog.Destroy()
    def choosedir3(self, event):
        # dialog
        dialog = wx.DirDialog(None, 'Choose KPTK dir:',style=wx.DD_DEFAULT_STYLE | wx.DD_NEW_DIR_BUTTON)
        if dialog.ShowModal() == wx.ID_OK:
            self.repo_dir3.SetValue(dialog.GetPath().replace('\\','/'))
            dialog.Destroy()

    def choosedir4(self, event):
        # dialog
        dialog = wx.DirDialog(None, 'Choose DEMO dir:',style=wx.DD_DEFAULT_STYLE | wx.DD_NEW_DIR_BUTTON)
        if dialog.ShowModal() == wx.ID_OK:
            self.repo_dir4.SetValue(dialog.GetPath().replace('\\','/'))
            dialog.Destroy()

    def gonext(self, event):
        if self.repo_dir.GetValue() != '':
            config.addChild('repo_list','new_repo',self.repo_dir.GetValue())
        if self.repo_dir2.GetValue() != '':
            config.addChild('repo_list','new_repo2',self.repo_dir2.GetValue())
        if self.repo_dir3.GetValue() != '':
            config.addChild('repo_list','new_repo3',self.repo_dir3.GetValue())
        if self.repo_dir4.GetValue() != '':
            config.addChild('repo_list','new_repo4',self.repo_dir4.GetValue())
        if self.repo_dir5.GetValue() != '':
            config.setValue('token',self.repo_dir5.GetValue())

        global run_token
        run_token = self.repo_dir6.GetValue()


        frame2 = PCFrame(parent=None, id=-1)
        frame2.Show()
        self.Close(True)
        

#*******************************************************************
#* Local runtime environment configuration Frame
#* 
#* 
#*******************************************************************

class PCFrame(wx.Frame): 
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, 'DaPeng Configuration Guide  :  local environment',size=(frame_width,frame_height),pos=(600,300),style=wx.DEFAULT_FRAME_STYLE)
        panel = wx.Panel(self)
        self.staticLine1 = wx.StaticLine(panel,pos=(20,20),size=(450,1))
        self.staticLine2 = wx.StaticLine(panel,pos=(20,static_line_height),size=(450,1))

        pc_info = GetPCconfig()
        staf_info = Get_STAF_info()
        if staf_info['exist'] == 'no':
            staf_info = None
        trace32_info = Get_TRACE32_info()
        if trace32_info['exist'] == 'no':
            trace32_info = None

        # mac label
        mac_label = wx.StaticText(panel, -1, "MAC ",(20,40))
        font = wx.Font(14,wx.NORMAL,wx.NORMAL, wx.NORMAL)
        mac_label.SetFont(font)
        # mac 
        self.mac=wx.TextCtrl(panel,pos=(105,40),size=(210,25))
        self.mac.SetValue(pc_info['mac'])
        # ip label
        ip_label = wx.StaticText(panel, -1, "IP ",(20,70))
        ip_label.SetFont(font)
        # ip 
        self.ip=wx.TextCtrl(panel,pos=(105,70),size=(210,25))
        self.ip.SetValue(pc_info['ip'])
        # hostname label
        host_label = wx.StaticText(panel, -1, "HOST ",(20,100))
        host_label.SetFont(font)
        # hostname 
        self.host=wx.TextCtrl(panel,pos=(105,100),size=(210,25))
        self.host.SetValue(pc_info['hostname'])
        # staf label
        staf_label = wx.StaticText(panel, -1, "STAF ",(20,130))
        staf_label.SetFont(font)
        # staf
        self.staf=wx.TextCtrl(panel,pos=(105,130),size=(210,25))
        if staf_info !=None:
            self.staf.SetValue(staf_info['path'])
        else:
            pass
        # staf choose
        self.button_choose = wx.Button(panel, label='select', pos=(320,130), size=(50, 25))
        self.Bind(wx.EVT_BUTTON, self.choosedir, self.button_choose)

        # trace32 label
        trace32_label = wx.StaticText(panel, -1, "Trace32 ",(20,160))
        trace32_label.SetFont(font)
        # trace32
        self.trace32=wx.TextCtrl(panel,pos=(105,160),size=(210,25))
        if trace32_info !=None:
            self.trace32.SetValue(trace32_info['path'])
        else:
            pass
        # trace32 choose
        self.button_choose2 = wx.Button(panel, label='select', pos=(320,160), size=(50, 25))
        self.Bind(wx.EVT_BUTTON, self.choosedir2, self.button_choose2)

        # mingw label
        mingw_label = wx.StaticText(panel, -1, "MINGW ",(20,190))
        mingw_label.SetFont(font)
        # mingw
        self.mingw=wx.TextCtrl(panel,pos=(105,190),size=(210,25))
        # mingw choose
        self.button_choose3 = wx.Button(panel, label='select', pos=(320,190), size=(50, 25))
        self.Bind(wx.EVT_BUTTON, self.choosedir3, self.button_choose3)

        # jlink label
        jlink_label = wx.StaticText(panel, -1, "Jlink ",(20,220))
        jlink_label.SetFont(font)
        # jlink
        self.jlink=wx.TextCtrl(panel,pos=(105,220),size=(210,25))
        # jlink choose
        self.button_choose4 = wx.Button(panel, label='select', pos=(320,220), size=(50, 25))
        self.Bind(wx.EVT_BUTTON, self.choosedir4, self.button_choose4)


        
        # next button
        self.button = wx.Button(panel, label='>>', pos=(af_button_width, workflow_button_height), size=(50, 25))
        self.Bind(wx.EVT_BUTTON, self.gonext, self.button)
        # pre button
        self.button2 = wx.Button(panel, label='<<', pos=(pre_button_width,workflow_button_height), size=(50, 25))
        self.Bind(wx.EVT_BUTTON, self.gopre, self.button2)

        # hint message
        hint=wx.TextCtrl(panel,pos=(hint_width,hint_height),size=(450,70),style=wx.TE_MULTILINE|wx.HSCROLL)
        content = 'Prompt Message:\n'
        content += '** MAC/IP/HOST/STAF will be detected automatically.\n'
        content += '** Trace32 is required when use lauterbach(e.g. c:/T32).\n'
        content += '** MingGW is required when use gcc-arm build(e.g. c:/MinGW).\n'
        content += '** Jlink is required when use gdb(e.g. C:/Program Files/SEGGER/JLinkARM_V480g).\n'
        hint.SetValue(content)


    def choosedir(self, event):
        # dialog
        dialog = wx.DirDialog(None, 'Choose STAF dir:',style=wx.DD_DEFAULT_STYLE | wx.DD_NEW_DIR_BUTTON)
        if dialog.ShowModal() == wx.ID_OK:
            self.staf.SetValue(dialog.GetPath().replace('\\','/'))
            dialog.Destroy()
    def choosedir2(self, event):
        # dialog
        dialog = wx.DirDialog(None, 'Choose TRACE32 dir:',style=wx.DD_DEFAULT_STYLE | wx.DD_NEW_DIR_BUTTON)
        if dialog.ShowModal() == wx.ID_OK:
            self.trace32.SetValue(dialog.GetPath().replace('\\','/'))
            dialog.Destroy()
    def choosedir3(self, event):
        # dialog
        dialog = wx.DirDialog(None, 'Choose MINGW dir:',style=wx.DD_DEFAULT_STYLE | wx.DD_NEW_DIR_BUTTON)
        if dialog.ShowModal() == wx.ID_OK:
            self.mingw.SetValue(dialog.GetPath().replace('\\','/'))
            dialog.Destroy()

    def choosedir4(self, event):
        # dialog
        dialog = wx.DirDialog(None, 'Choose jlink dir:',style=wx.DD_DEFAULT_STYLE | wx.DD_NEW_DIR_BUTTON)
        if dialog.ShowModal() == wx.ID_OK:
            self.jlink.SetValue(dialog.GetPath().replace('\\','/'))
            dialog.Destroy()

    def gopre(self,event):
        frame_pre_pc = RepoFrame(parent=None, id=-1)
        frame_pre_pc.Show()
        self.Close(True)
    def gonext(self, event):
        config.setValue('local_ip',self.ip.GetValue())
        config.setValue('local_mac',self.mac.GetValue())
        config.setValue('machine_name',self.host.GetValue())
        if self.staf.GetValue()!='':
            try:
                config.setValue('STAF_dir',win32api.GetShortPathName(self.staf.GetValue()))
            except Exception,e:
                pass
            # check staf cfg
            staf_cfg_file = self.staf.GetValue() + '/bin/STAF.cfg'
            if os.path.isfile(staf_cfg_file):
                f = open(staf_cfg_file,'r')
                cfg_content = f.read()
                f.close()
                if scheduler in cfg_content:
                    pass
                else:
                    cfg_content = cfg_content + '\ntrust machine ' + scheduler + ' level 5'
                    f = open(staf_cfg_file,'w')
                    f.write(cfg_content)
                    f.close()
                    reset_staf()
            else:
                print 'Could not find STAF config file!'
    
        if self.trace32.GetValue()!='':
            config.setValue('trace32',win32api.GetShortPathName(self.trace32.GetValue()))
        if self.mingw.GetValue()!='':
            config.setValue('mingw',win32api.GetShortPathName(self.mingw.GetValue()))
        if self.jlink.GetValue()!='':
            config.setValue('jlink',win32api.GetShortPathName(self.jlink.GetValue()))


        frame_af_pc = FreeFrame(parent=None, id=-1)
        frame_af_pc.Show()
        self.Close(True)

#*******************************************************************
#* DaPeng Tools directory selection Frame
#* 
#* 
#*******************************************************************

class FreeFrame(wx.Frame): 
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, 'DaPeng Configuration Guide  :  tools',size=(frame_width,frame_height),pos=(600,300),style=wx.DEFAULT_FRAME_STYLE)
        panel = wx.Panel(self)
        self.staticLine1 = wx.StaticLine(panel,pos=(20,20),size=(450,1))
        self.staticLine2 = wx.StaticLine(panel,pos=(20,static_line_height),size=(450,1))

        # tools choice
        self.oobe_checkbox = wx.CheckBox(panel, -1, 'MQX-OOBE',pos=(20,30),size=(90,45))
        self.Bind(wx.EVT_CHECKBOX, self.oobe_checkbox_event, self.oobe_checkbox)

        self.kptk_checkbox = wx.CheckBox(panel, -1, 'KSDK-KSV',pos=(110,30),size=(90,45))
        self.Bind(wx.EVT_CHECKBOX, self.kptk_checkbox_event, self.kptk_checkbox)
        
        self.demo_checkbox = wx.CheckBox(panel, -1, 'KSDK-DEMO',pos=(200,30),size=(90,45))
        self.Bind(wx.EVT_CHECKBOX, self.demo_checkbox_event, self.demo_checkbox)

        
        # tools label
        freemv_label = wx.StaticText(panel, -1, "FreeMV-build ",(20,80))
        font = wx.Font(14,wx.NORMAL,wx.NORMAL, wx.NORMAL)
        freemv_label.SetFont(font)
        freemv_label2 = wx.StaticText(panel, -1, "FreeMV-run ",(20,110))
        freemv_label2.SetFont(font)
    
        freekv_label3 = wx.StaticText(panel, -1, "FreeKV-build ",(20,140))
        freekv_label3.SetFont(font)
        freekv_label4 = wx.StaticText(panel, -1, "FreeKV-run ",(20,170))
        freekv_label4.SetFont(font)

        freekv_demo_label5 = wx.StaticText(panel, -1, "Demo-build ",(20,200))
        freekv_demo_label5.SetFont(font)
        freekv_demo_label6 = wx.StaticText(panel, -1, "Demo-run ",(20,230))
        freekv_demo_label6.SetFont(font)

        # tools dir
        self.freemv=wx.TextCtrl(panel,pos=(150,80),size=(210,25))
        self.freemv.Enable(False)
        self.freemv2=wx.TextCtrl(panel,pos=(150,110),size=(210,25))
        self.freemv2.Enable(False)
        self.freekv=wx.TextCtrl(panel,pos=(150,140),size=(210,25))
        self.freekv.Enable(False)
        self.freekv2=wx.TextCtrl(panel,pos=(150,170),size=(210,25))
        self.freekv2.Enable(False)
        self.freekv_demo=wx.TextCtrl(panel,pos=(150,200),size=(210,25))
        self.freekv_demo.Enable(False)
        self.freekv_demo2=wx.TextCtrl(panel,pos=(150,230),size=(210,25))
        self.freekv_demo2.Enable(False)

        # detect dapeng/freemv
        dapeng_info = Get_DP_info()
        if dapeng_info['exist'] == 'no':
            pass
        else:
            freemv_build_path = dapeng_info['path'] + '/freemvbuild'
            freemv_run_path = dapeng_info['path'] + '/freemvrun'
            freekv_build_path = dapeng_info['path'] + '/freekvbuild'
            freekv_run_path = dapeng_info['path'] + '/freekvrun'
            freekv_demo_build_path = dapeng_info['path'] + '/freekv_demobuild'
            freekv_demo_run_path = dapeng_info['path'] + '/freekv_demorun'

            self.freemv.SetValue(freemv_build_path)
            self.freemv2.SetValue(freemv_run_path)
            self.freekv.SetValue(freekv_build_path)
            self.freekv2.SetValue(freekv_run_path)
            self.freekv_demo.SetValue(freekv_demo_build_path)
            self.freekv_demo2.SetValue(freekv_demo_run_path)


        # choose dir
        self.button_choose = wx.Button(panel, label='select', pos=(380, 80), size=(50, 25))
        self.Bind(wx.EVT_BUTTON, self.choosedir, self.button_choose)
        self.button_choose2 = wx.Button(panel, label='select', pos=(380, 110), size=(50, 25))
        self.Bind(wx.EVT_BUTTON, self.choosedir2, self.button_choose2)
        
        self.button_choose3 = wx.Button(panel, label='select', pos=(380, 140), size=(50, 25))
        self.Bind(wx.EVT_BUTTON, self.choosedir3, self.button_choose3)
        self.button_choose4 = wx.Button(panel, label='select', pos=(380, 170), size=(50, 25))
        self.Bind(wx.EVT_BUTTON, self.choosedir4, self.button_choose4)
        
        self.button_choose5 = wx.Button(panel, label='select', pos=(380, 200), size=(50, 25))
        self.Bind(wx.EVT_BUTTON, self.choosedir5, self.button_choose5)
        self.button_choose6 = wx.Button(panel, label='select', pos=(380, 230), size=(50, 25))
        self.Bind(wx.EVT_BUTTON, self.choosedir6, self.button_choose6)

        # next button
        self.button = wx.Button(panel, label='>>', pos=(af_button_width, workflow_button_height), size=(50, 25))
        self.Bind(wx.EVT_BUTTON, self.gonext, self.button)
        # pre button
        self.button2 = wx.Button(panel, label='<<', pos=(pre_button_width, workflow_button_height), size=(50, 25))
        self.Bind(wx.EVT_BUTTON, self.gopre, self.button2)

        # hint message
        hint=wx.TextCtrl(panel,pos=(hint_width,hint_height),size=(450,70),style=wx.TE_MULTILINE|wx.HSCROLL)
        content = 'Prompt Message:\n'
        content += '** FreeMV(for oobe test)/FreeKV(for kptk test) ,FreeKV_demo(for KSDK DEMO)will be detected automatically.\n'
        content += '** Choose task type of current station(oobe,kptk or both of them).\n'
        hint.SetValue(content)

    def choosedir(self, event):
        # dialog
        dialog = wx.DirDialog(None, 'Choose FreeMV dir:',style=wx.DD_DEFAULT_STYLE | wx.DD_NEW_DIR_BUTTON)
        if dialog.ShowModal() == wx.ID_OK:
            self.freemv.SetValue(dialog.GetPath().replace('\\','/'))
            dialog.Destroy()
    def choosedir2(self, event):
        # dialog
        dialog = wx.DirDialog(None, 'Choose FreeMV dir:',style=wx.DD_DEFAULT_STYLE | wx.DD_NEW_DIR_BUTTON)
        if dialog.ShowModal() == wx.ID_OK:
            self.freemv2.SetValue(dialog.GetPath().replace('\\','/'))
            dialog.Destroy()

    def choosedir3(self, event):
        # dialog
        dialog = wx.DirDialog(None, 'Choose FreeKV dir:',style=wx.DD_DEFAULT_STYLE | wx.DD_NEW_DIR_BUTTON)
        if dialog.ShowModal() == wx.ID_OK:
            self.freekv.SetValue(dialog.GetPath().replace('\\','/'))
            dialog.Destroy()
    def choosedir4(self, event):
        # dialog
        dialog = wx.DirDialog(None, 'Choose FreeKV dir:',style=wx.DD_DEFAULT_STYLE | wx.DD_NEW_DIR_BUTTON)
        if dialog.ShowModal() == wx.ID_OK:
            self.freekv2.SetValue(dialog.GetPath().replace('\\','/'))
            dialog.Destroy()
    def choosedir5(self, event):
        # dialog
        dialog = wx.DirDialog(None, 'Choose FreeKV_demo dir:',style=wx.DD_DEFAULT_STYLE | wx.DD_NEW_DIR_BUTTON)
        if dialog.ShowModal() == wx.ID_OK:
            self.freekv_demo.SetValue(dialog.GetPath().replace('\\','/'))
            dialog.Destroy()
    def choosedir6(self, event):
        # dialog
        dialog = wx.DirDialog(None, 'Choose FreeKV_demo dir:',style=wx.DD_DEFAULT_STYLE | wx.DD_NEW_DIR_BUTTON)
        if dialog.ShowModal() == wx.ID_OK:
            self.freekv_demo2.SetValue(dialog.GetPath().replace('\\','/'))
            dialog.Destroy()
          
    def oobe_checkbox_event(self,event):
        global oobe_enable
        if self.oobe_checkbox.GetValue():
            self.freemv.Enable(True)
            self.freemv2.Enable(True)
            oobe_enable = 'yes'
        else:
            oobe_enable = 'no'
            self.freemv.Enable(False)
            self.freemv2.Enable(False)
    def kptk_checkbox_event(self,event):
        global kptk_enable
        if self.kptk_checkbox.GetValue():
            kptk_enable = 'yes'
            self.freekv.Enable(True)
            self.freekv2.Enable(True)
        else:
            kptk_enable = 'no'
            self.freekv.Enable(False)
            self.freekv2.Enable(False)
            
    def demo_checkbox_event(self,event):
        global demo_enable
        if self.demo_checkbox.GetValue():
            demo_enable = 'yes'
            self.freekv_demo.Enable(True)
            self.freekv_demo2.Enable(True)
        else:
            demo_enable = 'no'
            self.freekv_demo.Enable(False)
            self.freekv_demo2.Enable(False)


    def gopre(self,event):
        frame_pre_free = PCFrame(parent=None, id=-1)
        frame_pre_free.Show()
        self.Close(True)
    def gonext(self, event):

        # record run-tool dir
        global freemv_dir_run
        if self.freemv2.GetValue()!='':
            freemv_dir_run = win32api.GetShortPathName(self.freemv2.GetValue())
        global freekv_dir_run
        if self.freekv2.GetValue()!='':
            freekv_dir_run = win32api.GetShortPathName(self.freekv2.GetValue())
            
        global freekv_demo_dir_run
        if self.freekv_demo2.GetValue()!='':
            freekv_demo_dir_run = win32api.GetShortPathName(self.freekv_demo2.GetValue())

        # record tool dir
        if self.freemv.GetValue()!='':
            config.setValue('FreeMV',win32api.GetShortPathName(self.freemv.GetValue()))
            config.setValue('FreeMV_ksdk',win32api.GetShortPathName(self.freemv.GetValue()))
            config.setAttr('FreeMV','enable',oobe_enable)
            config.setAttr('FreeMV_ksdk','enable',oobe_enable)
            try:
                if os.path.isfile(self.freemv.GetValue() + '/settings.py'):
                    settings_file = self.freemv.GetValue() + '/settings.py'
                else:
                    
                    settings_file = freemv_dir_run + '/settings.py'
                settings_file_current = file_path + '/settings.py'
                shutil.copyfile(settings_file,settings_file_current)
                settings = __import__('settings')
                global freemv_platform_list
                freemv_platform_list = settings.platform_list[:]
                os.remove(settings_file_current)
            except Exception,e:
                pass

        if self.freekv.GetValue()!='':
            config.setValue('FreeKV',win32api.GetShortPathName(self.freekv.GetValue()))
            config.setAttr('FreeKV','enable',kptk_enable)
            try:
                if os.path.isfile(self.freekv.GetValue() + '/platform_list.py'):
                    settings_file = self.freekv.GetValue() + '/platform_list.py'
                else:
                    settings_file = freekv_dir_run + '/platform_list.py'
                settings_file_current = file_path + '/platform_list.py'
                shutil.copyfile(settings_file,settings_file_current)
                settings = __import__('platform_list')
                global freekv_platform_list
                freekv_platform_list = settings.platform_list[:]
                os.remove(settings_file_current)
            except Exception,e:
                pass

        if self.freekv_demo.GetValue()!='':
            config.setValue('FreeKV_demo',win32api.GetShortPathName(self.freekv_demo.GetValue()))
            config.setValue('FreeKV_usb',win32api.GetShortPathName(self.freekv_demo.GetValue()))
            config.setValue('FreeKV_unit_test',win32api.GetShortPathName(self.freekv_demo.GetValue()))
            config.setAttr('FreeKV_demo','enable',demo_enable)
            config.setAttr('FreeKV_usb','enable',demo_enable)
            config.setAttr('FreeKV_unit_test','enable',demo_enable)
            
            try:
                if os.path.isfile(self.freekv_demo.GetValue() + '/platform_list.py'):
                    settings_file = self.freekv_demo.GetValue() + '/platform_list.py'
                else:
                    settings_file = freekv_demo_dir_run + '/platform_list.py'
                settings_file_current = file_path + '/platform_list2.py'
                shutil.copyfile(settings_file,settings_file_current)
                settings = __import__('platform_list2')
                global freekv_demo_platform_list
                freekv_demo_platform_list = settings.platform_list[:]
                os.remove(settings_file_current)
            except Exception,e:
                pass

        frame_af_freemv = IDEFrame(parent=None, id=-1)
        frame_af_freemv.Show()
        self.Close(True)

#*******************************************************************
#* DaPeng IDE selection Frame
#* 
#* 
#*******************************************************************


class IDEFrame(wx.Frame): 
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, 'DaPeng Configuration Guide  :  IDE',size=(frame_width,frame_height),pos=(600,300),style=wx.DEFAULT_FRAME_STYLE)
        panel = wx.Panel(self)
        self.staticLine1 = wx.StaticLine(panel,pos=(20,20),size=(450,1))
        self.staticLine2 = wx.StaticLine(panel,pos=(20,static_line_height),size=(450,1))


        ide_info=Get_IDE_info()
        self.iar_version = 'unknown'
        self.uv4_version = 'unknown'
        self.cw10_version = 'unknown'
        self.gcc_arm_version = 'unknown'
        self.kds_version = 'unknown'
        # IAR(checkbox,text,choice,select)
        self.iar_checkbox = wx.CheckBox(panel, -1, 'IAR',pos=(25,40),size=(90,45))
        font = wx.Font(12,wx.NORMAL,wx.NORMAL, wx.NORMAL)
        self.iar_checkbox.SetFont(font)
        self.Bind(wx.EVT_CHECKBOX, self.iar_checkbox_event, self.iar_checkbox)
        self.iar_text=wx.TextCtrl(panel,pos=(120,52),size=(210,25))
        self.iar_text.Enable(False)
        if len(ide_info['iar'])!= 0:
            self.iar_version_dir = {}
            self.iar_version_list = []
            for info in ide_info['iar']:
                self.iar_version_list.append(info['version'])
                self.iar_version_dir[info['version']] = info['path']
            self.iar_choice = wx.Choice(panel, -1, (350, 53), choices=self.iar_version_list)
            self.Bind(wx.EVT_CHOICE, self.iar_choice_event, self.iar_choice)
        self.iar_button_choose = wx.Button(panel, label='select', pos=(420, 50), size=(50, 25))
        self.Bind(wx.EVT_BUTTON, self.iar_choosedir, self.iar_button_choose)


        # uv4(checkbox,text,choice,select)
        self.uv4_checkbox = wx.CheckBox(panel, -1, 'uv4',pos=(25,80),size=(90,45))
        font = wx.Font(12,wx.NORMAL,wx.NORMAL, wx.NORMAL)
        self.uv4_checkbox.SetFont(font)
        self.Bind(wx.EVT_CHECKBOX, self.uv4_checkbox_event, self.uv4_checkbox)
        self.uv4_text=wx.TextCtrl(panel,pos=(120,92),size=(210,25))
        self.uv4_text.Enable(False)
        if len(ide_info['keil'])!= 0:
            self.uv4_version_dir = {}
            self.uv4_version_list = []
            for info in ide_info['keil']:
                self.uv4_version_list.append(info['version'])
                self.uv4_version_dir[info['version']] = info['path']
            self.uv4_choice = wx.Choice(panel, -1, (350, 93), choices=self.uv4_version_list)
            self.Bind(wx.EVT_CHOICE, self.uv4_choice_event, self.uv4_choice)
        self.uv4_button_choose = wx.Button(panel, label='select', pos=(420, 90), size=(50, 25))
        self.Bind(wx.EVT_BUTTON, self.uv4_choosedir, self.uv4_button_choose)

        # cw10(checkbox,text,choice,select)
        self.cw10_checkbox = wx.CheckBox(panel, -1, 'cw10',pos=(25,120),size=(90,45))
        font = wx.Font(12,wx.NORMAL,wx.NORMAL, wx.NORMAL)
        self.cw10_checkbox.SetFont(font)
        self.Bind(wx.EVT_CHECKBOX, self.cw10_checkbox_event, self.cw10_checkbox)
        self.cw10_text=wx.TextCtrl(panel,pos=(120,132),size=(210,25))
        self.cw10_text.Enable(False)
        if len(ide_info['cw10'])!= 0:
            self.cw10_version_dir = {}
            self.cw10_version_list = []
            for info in ide_info['cw10']:
                self.cw10_version_list.append(info['version'])
                self.cw10_version_dir[info['version']] = info['path']
            self.cw10_choice = wx.Choice(panel, -1, (350, 133), choices=self.cw10_version_list)
            self.Bind(wx.EVT_CHOICE, self.cw10_choice_event, self.cw10_choice)
        self.cw10_button_choose = wx.Button(panel, label='select', pos=(420, 130), size=(50, 25))
        self.Bind(wx.EVT_BUTTON, self.cw10_choosedir, self.cw10_button_choose)

        # gcc_arm(checkbox,text,choice,select)
        self.gcc_arm_checkbox = wx.CheckBox(panel, -1, 'gcc_arm',pos=(25,160),size=(90,45))
        font = wx.Font(12,wx.NORMAL,wx.NORMAL, wx.NORMAL)
        self.gcc_arm_checkbox.SetFont(font)
        self.Bind(wx.EVT_CHECKBOX, self.gcc_arm_checkbox_event, self.gcc_arm_checkbox)
        self.gcc_arm_text=wx.TextCtrl(panel,pos=(120,172),size=(210,25))
        self.gcc_arm_text.Enable(False)
        if len(ide_info['gcc_arm'])!= 0:
            self.gcc_arm_version_dir = {}
            self.gcc_arm_version_list = []
            for info in ide_info['gcc_arm']:
                self.gcc_arm_version_list.append(info['version'])
                self.gcc_arm_version_dir[info['version']] = info['path']
            self.gcc_arm_choice = wx.Choice(panel, -1, (350, 173), choices=self.gcc_arm_version_list)
            self.Bind(wx.EVT_CHOICE, self.gcc_arm_choice_event, self.gcc_arm_choice)
        self.gcc_arm_button_choose = wx.Button(panel, label='select', pos=(420, 170), size=(50, 25))
        self.Bind(wx.EVT_BUTTON, self.gcc_arm_choosedir, self.gcc_arm_button_choose)

        # kds(checkbox,text,choice,select)
        self.kds_checkbox = wx.CheckBox(panel, -1, 'kds',pos=(25,200),size=(90,45))
        font = wx.Font(12,wx.NORMAL,wx.NORMAL, wx.NORMAL)
        self.kds_checkbox.SetFont(font)
        self.Bind(wx.EVT_CHECKBOX, self.kds_checkbox_event, self.kds_checkbox)
        self.kds_text=wx.TextCtrl(panel,pos=(120,212),size=(210,25))
        self.kds_text.Enable(False)
        if len(ide_info['kds'])!= 0:
            self.kds_version_dir = {}
            self.kds_version_list = []
            for info in ide_info['kds']:
                self.kds_version_list.append(info['version'])
                self.kds_version_dir[info['version']] = info['path']
            self.kds_choice = wx.Choice(panel, -1, (350, 213), choices=self.kds_version_list)
            self.Bind(wx.EVT_CHOICE, self.kds_choice_event, self.kds_choice)
        self.kds_button_choose = wx.Button(panel, label='select', pos=(420, 210), size=(50, 25))
        self.Bind(wx.EVT_BUTTON, self.kds_choosedir, self.kds_button_choose)


        # next button
        self.button = wx.Button(panel, label='>>', pos=(af_button_width, workflow_button_height), size=(50, 25))
        self.Bind(wx.EVT_BUTTON, self.gonext, self.button)
        # pre button
        self.button2 = wx.Button(panel, label='<<', pos=(pre_button_width, workflow_button_height), size=(50, 25))
        self.Bind(wx.EVT_BUTTON, self.gopre, self.button2)

        # hint message
        hint=wx.TextCtrl(panel,pos=(hint_width,hint_height),size=(450,70),style=wx.TE_MULTILINE|wx.HSCROLL)
        content = 'Prompt Message:\n'
        content += '** IDE directory/version infomation may not complete.\n'
        content += '** ds5 is not in use.\n'
        content += '** IAR directory e.g. C:/IARSystems/EmbeddedWorkbench6.5.\n'
        content += '** UV4 directory e.g. C:/Keil/UV4.\n'
        content += '** CW10 directory e.g. C:/devsoft/CWMCUv10.5.\n'
        content += '** gcc directory e.g. C:/GNUToolsARMEmbedded/4.72013q3.\n'
        hint.SetValue(content)



    def iar_choice_event(self,event):
        self.iar_text.SetValue(self.iar_version_dir[self.iar_version_list[self.iar_choice.GetSelection()]])
        self.iar_version = self.iar_version_list[self.iar_choice.GetSelection()]
    def iar_checkbox_event(self,event):
        if self.iar_checkbox.GetValue():
            self.iar_text.Enable(True)
        else:
            self.iar_text.Enable(False)
    def iar_choosedir(self,event):
        dialog = wx.DirDialog(None, 'Choose iar dir:',style=wx.DD_DEFAULT_STYLE | wx.DD_NEW_DIR_BUTTON)
        if dialog.ShowModal() == wx.ID_OK:
            self.iar_text.SetValue(dialog.GetPath().replace('\\','/'))
            self.iar_version = "unknown"
            dialog.Destroy()

            
    def uv4_choice_event(self,event):
        self.uv4_text.SetValue(self.uv4_version_dir[self.uv4_version_list[self.uv4_choice.GetSelection()]])
        self.uv4_version = self.uv4_version_list[self.uv4_choice.GetSelection()]
    def uv4_checkbox_event(self,event):
        if self.uv4_checkbox.GetValue():
            self.uv4_text.Enable(True)
        else:
            self.uv4_text.Enable(False)
    def uv4_choosedir(self,event):
        dialog = wx.DirDialog(None, 'Choose uv4 dir:',style=wx.DD_DEFAULT_STYLE | wx.DD_NEW_DIR_BUTTON)
        if dialog.ShowModal() == wx.ID_OK:
            self.uv4_text.SetValue(dialog.GetPath().replace('\\','/'))
            self.uv4_version = 'unknown'
            dialog.Destroy()  

    def cw10_choice_event(self,event):
        self.cw10_text.SetValue(self.cw10_version_dir[self.cw10_version_list[self.cw10_choice.GetSelection()]])
        self.cw10_version = self.cw10_version_list[self.cw10_choice.GetSelection()]
    def cw10_checkbox_event(self,event):
        if self.cw10_checkbox.GetValue():
            self.cw10_text.Enable(True)
        else:
            self.cw10_text.Enable(False)
    def cw10_choosedir(self,event):
        dialog = wx.DirDialog(None, 'Choose cw10 dir:',style=wx.DD_DEFAULT_STYLE | wx.DD_NEW_DIR_BUTTON)
        if dialog.ShowModal() == wx.ID_OK:
            self.cw10_text.SetValue(dialog.GetPath().replace('\\','/'))
            self.cw10_version="unknown"
            dialog.Destroy()  

    def gcc_arm_choice_event(self,event):
        self.gcc_arm_text.SetValue(self.gcc_arm_version_dir[self.gcc_arm_version_list[self.gcc_arm_choice.GetSelection()]])
        self.gcc_arm_version = self.gcc_arm_version_list[self.gcc_arm_choice.GetSelection()]
    def gcc_arm_checkbox_event(self,event):
        if self.gcc_arm_checkbox.GetValue():
            self.gcc_arm_text.Enable(True)
        else:
            self.gcc_arm_text.Enable(False)
    def gcc_arm_choosedir(self,event):
        dialog = wx.DirDialog(None, 'Choose arm-gcc dir:',style=wx.DD_DEFAULT_STYLE | wx.DD_NEW_DIR_BUTTON)
        if dialog.ShowModal() == wx.ID_OK:
            self.gcc_arm_text.SetValue(dialog.GetPath().replace('\\','/'))
            self.gcc_arm_version = Get_Gcc_info(self.gcc_arm_text.GetValue())
            dialog.Destroy()  

    def kds_choice_event(self,event):
        self.kds_text.SetValue(self.kds_version_dir[self.kds_version_list[self.kds_choice.GetSelection()]])
        self.kds_version = self.kds_version_list[self.kds_choice.GetSelection()]
    def kds_checkbox_event(self,event):
        if self.kds_checkbox.GetValue():
            self.kds_text.Enable(True)
        else:
            self.kds_text.Enable(False)
    def kds_choosedir(self,event):
        dialog = wx.DirDialog(None, 'Choose kds dir:',style=wx.DD_DEFAULT_STYLE | wx.DD_NEW_DIR_BUTTON)
        if dialog.ShowModal() == wx.ID_OK:
            self.kds_text.SetValue(dialog.GetPath().replace('\\','/'))
            dialog.Destroy()
    def gopre(self,event):
        frame_pre_ide = FreeFrame(parent=None, id=-1)
        frame_pre_ide.Show()
        self.Close(True)
    def gonext(self, event):
        if self.iar_text.IsEnabled() and self.iar_text.GetValue()!='':
            config.setAttr('IDE','iar','yes')
            config.setValue('iar',win32api.GetShortPathName(self.iar_text.GetValue()))
            config.setAttr('iar','version',self.iar_version)
        else:
            config.setAttr('IDE','iar','no')
            config.setAttr('iar','version',self.iar_version)
            
        if self.uv4_text.IsEnabled() and self.uv4_text.GetValue()!='':
            config.setAttr('IDE','uv4','yes')
            config.setValue('uv4',win32api.GetShortPathName(self.uv4_text.GetValue()))
            config.setAttr('uv4','version',self.uv4_version)
        else:
            config.setAttr('IDE','uv4','no')
            config.setAttr('uv4','version',self.uv4_version)
            
        if self.cw10_text.IsEnabled() and self.cw10_text.GetValue()!='':
            config.setAttr('IDE','cw10','yes')
            config.setAttr('IDE','cw10gcc','yes')
            config.setValue('cw10',win32api.GetShortPathName(self.cw10_text.GetValue()))
            config.setValue('cw10gcc',win32api.GetShortPathName(self.cw10_text.GetValue()))
            config.setAttr('cw10','version',self.cw10_version)
            config.setAttr('cw10gcc','version',self.cw10_version)
        else:
            config.setAttr('IDE','cw10','no')
            config.setAttr('IDE','cw10gcc','no')
            config.setAttr('cw10','version',self.cw10_version)
            config.setAttr('cw10gcc','version',self.cw10_version)

            
        if self.gcc_arm_text.IsEnabled() and self.gcc_arm_text.GetValue()!='':
            config.setAttr('IDE','gcc_arm','yes')
            config.setValue('gcc_arm',win32api.GetShortPathName(self.gcc_arm_text.GetValue()))
            config.setAttr('gcc_arm','version',self.gcc_arm_version)
        else:
            config.setAttr('IDE','gcc_arm','no')
            config.setAttr('gcc_arm','version',self.gcc_arm_version)

        if self.kds_text.IsEnabled() and self.kds_text.GetValue()!='':
            config.setAttr('IDE','kds','yes')
            config.setValue('kds',win32api.GetShortPathName(self.kds_text.GetValue()))
            config.setAttr('kds','version',self.kds_version)
        else:
            config.setAttr('IDE','kds','no')
            config.setAttr('kds','version',self.kds_version)


        frame_af_ide = RUNFrame(parent=None, id=-1)
        frame_af_ide.Show()
        self.Close(True)

#*******************************************************************
#* DaPeng platform related info Frame
#* 
#* 
#*******************************************************************       

class RUNFrame(wx.Frame): 
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, 'DaPeng Configuration Guide  :  Platform',size=(frame_width,frame_height),pos=(600,300),style=wx.DEFAULT_FRAME_STYLE)
        panel = wx.Panel(self)
        self.staticLine1 = wx.StaticLine(panel,pos=(20,20),size=(450,1))
        self.staticLine2 = wx.StaticLine(panel,pos=(20,static_line_height),size=(450,1))

        self.jlink_checkbox = wx.CheckBox(panel, -1, 'jlink',pos=(25,30),size=(50,45))
        font = wx.Font(12,wx.NORMAL,wx.NORMAL, wx.NORMAL)
        self.jlink_checkbox.SetFont(font)
        
        self.pne_checkbox = wx.CheckBox(panel, -1, 'pne',pos=(90,30),size=(50,45))
        font = wx.Font(12,wx.NORMAL,wx.NORMAL, wx.NORMAL)
        self.pne_checkbox.SetFont(font)

        self.lauterbach_checkbox = wx.CheckBox(panel, -1, 'lauterbach',pos=(155,30),size=(100,45))
        font = wx.Font(12,wx.NORMAL,wx.NORMAL, wx.NORMAL)
        self.lauterbach_checkbox.SetFont(font)
        # platform selection
        platform_label = wx.StaticText(panel, -1, "Platform ",(20,75))
        font = wx.Font(12,wx.NORMAL,wx.NORMAL, wx.NORMAL)
        platform_label.SetFont(font)
       
        self.platform=wx.TextCtrl(panel,pos=(105,75),size=(140,25))
        self.whole_platform_list = list(set(freemv_platform_list+freekv_platform_list+freekv_demo_platform_list))
        if len(self.whole_platform_list)!= 0:
            self.platform_choice = wx.Choice(panel, -1, (260, 75), choices=self.whole_platform_list)
            self.Bind(wx.EVT_CHOICE, self.platform_choice_event, self.platform_choice)
        else:
            pass

        # serial port selection
        port_label = wx.StaticText(panel, -1, "SerialPort ",(20,105))
        port_label.SetFont(font)
       
        self.port=wx.TextCtrl(panel,pos=(105,105),size=(140,25))
        self.serial_port_list = Get_serial_info()
        if len(self.serial_port_list)!=0:
            self.serial_choice = wx.Choice(panel, -1, (260, 108), choices=self.serial_port_list)
            self.Bind(wx.EVT_CHOICE, self.serial_choice_event, self.serial_choice)
        else:
            info_label2 = wx.StaticText(panel, -1, "Active serial port not found! ",(20,workflow_button_height))

        # device type
        device_label  = wx.StaticText(panel, -1, "DeviceType ",(20,135))
        device_label.SetFont(font)
        self.device = wx.TextCtrl(panel,pos=(105,135),size=(140,25))
        # debug type
        debug_port_label  = wx.StaticText(panel, -1, "DebugPort ",(20,165))
        debug_port_label.SetFont(font)
        self.debug_port = wx.TextCtrl(panel,pos=(105,165),size=(140,25))


        
        self.add_button = wx.Button(panel, label='Add', pos=(210, workflow_button_height), size=(50, 25))
        self.Bind(wx.EVT_BUTTON, self.addplatform, self.add_button)
        

        # next button
        self.button = wx.Button(panel, label='>>', pos=(af_button_width, workflow_button_height), size=(50, 25))
        self.Bind(wx.EVT_BUTTON, self.gonext, self.button)
        # pre button
        self.button2 = wx.Button(panel, label='<<', pos=(pre_button_width, workflow_button_height), size=(50, 25))
        self.Bind(wx.EVT_BUTTON, self.gopre, self.button2)

        # hint message
        hint=wx.TextCtrl(panel,pos=(hint_width,hint_height),size=(450,70),style=wx.TE_MULTILINE|wx.HSCROLL)
        content = 'Prompt Message:\n'
        content += '** One station,one debugger.\n'
        content += '** Click add button after filling in above blanks.\n'
        content += '** If lauterbach connected,more than one board could be added .\n'
        content += '** Choose platform/serail port in list.\n'
        content += '** If no platform checkbox,please check FreeMV/FreeKV directory.\n'
        content += '** If no serial port checkbox,please check board connection.\n'
        content += '** Device type/Debug port is required when execute kptk-run task .\n'
        content += '** Device type e.g. twrk22f120m:MK22FN512xxx12.\n'
        content += '** Debug port is S/N number when use jlink, USB port when use OpenSDA.\n'
        hint.SetValue(content)


    def addplatform(self,event):
        if self.platform.GetValue()!='' and self.port.GetValue()!='':
            config.addChildAttr('device',self.platform.GetValue(),'yes',{'serial_port':self.port.GetValue(),'debug_port':self.debug_port.GetValue(),'device_type':self.device.GetValue()})
            dialog = SubclassDialog()
            result = dialog.ShowModal()
            if result == wx.ID_OK:
                dialog.Destroy()
    def platform_choice_event(self,event):
        self.platform.SetValue(self.whole_platform_list[self.platform_choice.GetSelection()])
    def serial_choice_event(self,event):
        self.port.SetValue(self.serial_port_list[self.serial_choice.GetSelection()][3:])
    def gopre(self,event):
        frame_pre_run = IDEFrame(parent=None, id=-1)
        frame_pre_run.Show()
        self.Close(True)
    def gonext(self, event):
        if self.jlink_checkbox.GetValue():
            config.setAttr('hardware_debugger','jlink','yes')
        else:
            config.setAttr('hardware_debugger','jlink','no')
        if self.pne_checkbox.GetValue():
            config.setAttr('hardware_debugger','pne','yes')
        else:
            config.setAttr('hardware_debugger','pne','no')
            
        if self.lauterbach_checkbox.GetValue():
            config.setAttr('hardware_debugger','lauterbach','yes')
        else:
            config.setAttr('hardware_debugger','lauterbach','no')
            
        # clean env and overwrite old config file
        global build_status
        global run_status
        if build_station:
            try:
                shutil.copyfile(config_file,build_station_config)
                build_status = 'successful'
            except Exception,e:
                build_status = 'fail'
        if run_station:
            try:
                if freemv_dir_run!='':
                    config.setValue('FreeMV',freemv_dir_run)
                    config.setValue('FreeMV_ksdk',freemv_dir_run)
                if freekv_dir_run!='':
                    config.setValue('FreeKV',freekv_dir_run)
                if freekv_demo_dir_run!='':
                    config.setValue('FreeKV_demo',freekv_demo_dir_run)
                    config.setValue('FreeKV_usb',freekv_demo_dir_run)
                    config.setValue('FreeKV_unit_test',freekv_demo_dir_run)
                if run_private == 'yes':
                    config.setAttr('token','private','yes')
                if run_token!='':
                    config.setValue('token',run_token)

                shutil.copyfile(config_file,run_station_config)
                run_status = 'successful'
            except Exception,e:
                print e
                run_status = 'fail'
        try:
            os.remove(config_file)
        except Exception,e:
            pass
        dialog = SubclassDialog_config()
        result = dialog.ShowModal()
        if result == wx.ID_OK:
            dialog.Destroy()

        # tag configured version
        version = open(version_file,'r').read()
        f= open(configured_version_file,'w')
        f.write(version)
        f.close()
        
        self.Close(True)
        os._exit(0)
            
# backup config.xml
config_file_backup = file_path + '/config.xml'
config_file =file_path + '/config_operate.xml'
shutil.copyfile(config_file_backup,config_file)

# reset build/run config.xml
build_station_config = config_path + 'config.xml'
run_station_config = main_path + '/../Run_station/config/config.xml'


config = Getconfig(config_file)
config_build = Getconfig(build_station_config)
config_run = Getconfig(run_station_config)
mac_build = config_build.getValue('local_mac')
mac_run = config_run.getValue('local_mac')
scheduler = config_build.getValue('Scheduler_IP')

# start staf
start_staf()


# get online status, status must be off line when config
fstaf = STAFer()
(ret,build_station_online) = fstaf.list_activestation(scheduler,1)
(ret,run_station_online) = fstaf.list_activestation(scheduler,2)

if mac_build in build_station_online or mac_run in run_station_online:
    online_status = 1
else:
    online_status = 0
app = wx.App()
if online_status:
    dialog = SubclassDialog_statuscheck()
    result = dialog.ShowModal()
    if result == wx.ID_OK:
        dialog.Destroy()

else:
    frame = stationFrame(parent=None, id=-1)
    frame.Show()
app.MainLoop()

