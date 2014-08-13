# coding=utf-8
 
#*******************************************************************
#* Copyright (c) 2013 Freescale Semiconductor Inc.
#* All rights reserved.
#*
#* Use of Freescale code is governed by terms and conditions
#* stated in the accompanying licensing statement.
#* Description: builder
#*
#* Revision History:
#* -----------------
#* Code Version    YYYY-MM-DD    Author        Description
#* 0.1             2013-12-20    Armand Wang    Create this file
#*******************************************************************
import os, sys,shutil
import getopt

main_path = os.path.dirname(os.path.abspath(__file__))
config_path = main_path + '/config/'
lib_path = main_path + '/lib/'
log_path = main_path + '/log/'
tmp_path = main_path + '/temp/'
script_path = main_path + '/script/'
history_path = tmp_path + '/history_data/'
sys.path.append(lib_path)
sys.path.append(log_path)
sys.path.append(script_path)



from getconfig import Getconfig
from helper import Helper
from station_on_off import register,offline
import station_map

config_file =config_path + 'config.xml'
config = Getconfig(config_file)
# get configuration
scheduler = config.getValue('Scheduler_IP')
machine_name = config.getValue('machine_name')
machine_type = sys.argv[1] # build_station:0  run_station:1
mac = config.getValue('local_mac')
ip = config.getValue('local_ip')

# public:1  private:2
if config.getAttr('token','private') == 'yes':
    machine_range = '2'
    token = config.getValue('token')
else:
    machine_range = '1'
    token = '-1'

status = sys.argv[2]
# get ide list
ide_list = []
IDE = config.getAttr_list('IDE')
for ide in IDE:
    if IDE[ide] == 'yes':
        ide_list.append(station_map.compiler_map[ide])
if len(ide_list)!=0:
    ide = ','.join(ide_list)
else:
    ide = '-1'
# get hardware debugger
debugger_list = []
DEBUGGER = config.getAttr_list('hardware_debugger')
for debugger in DEBUGGER:
    if DEBUGGER[debugger] == 'yes':
        debugger_list.append(station_map.debugger_map[debugger])
if len(debugger_list)!=0:
    debugger = ','.join(debugger_list)
else:
    debugger = '-1'
# get tools
tool_list = []
tools = config.getChildTagList('tools')
for tool in tools:
    tool = tool.replace('_tool','')
    if config.getAttr(tool,'enable') == 'yes':
        tool_list.append(station_map.tools_map[tool])
if len(tool_list)!=0:
    tool = ','.join(tool_list)
else:
    tool = '-1'
# get platforms
platform_list = []
platforms = config.getChildTagList('device')
for platform in platforms:
    if config.getValue(platform) == 'yes':
        platform_list.append(station_map.platform_map[platform])
if len(platform_list)!=0:
    platform = ','.join(platform_list)
else:
    platform = '-1'
#*************************************************beginning*********************************************
if machine_type == '1':
    print '*******************build station***********************'
elif machine_type == '2':
    print '*******************run station*************************'
else:
    print 'station type error'
    os._exit(1)
if status == 'on':
    print 'registering station...'
    ret = register(scheduler,machine_name,machine_type,mac,ip,ide,debugger,tool,machine_range,platform,token)
    os._exit(ret)
elif status == 'off':
    print 'offline...'
    ret =  offline(config.getValue('Scheduler_IP'),machine_type,mac)
    os._exit(ret)
else:
    print 'pls check argvs'
    os._exit(1)
