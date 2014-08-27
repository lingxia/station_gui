import py2exe
import sys,os
from distutils.core import setup
#from xml.etree import ElementTree
#import logging
#from xml.etree.ElementTree import (Element,
#                                   SubElement,
#                                   Comment,
#                                   tostring,
#                                   )
sys.argv.append('py2exe')

file_path = os.path.dirname(os.path.abspath("__file__"))
main_path = os.path.join(file_path,'../')
designer_path = main_path + '/designer_window/'
pic_path = main_path + '/pic/'   
lib_path = main_path + '/Build_station' + '/lib/'
script_path = main_path + '/Build_station' + '/script/'
buildStation_path = main_path + '/Build_station/'
#config_path = buildStation_path + '/config/'


sys.path.append(lib_path)
sys.path.append(designer_path)
sys.path.append(main_path)
sys.path.append(buildStation_path)

import getconfig
import buildConfigUi
import get_local_config
import platform_list
#from getconfig import Getconfig
#from buildConfigUi import Ui_buildConfig
#from get_local_config import Get_IDE_info, Get_DP_info
#import platform_list

#config_file_build = config_path + 'config.xml'
#config_build_file = Getconfig(config_file_build)
#import win32api
#mydata = ["getconfig","buildConfigUi","get_local_config"]
#for files in os.listdir(lib_path):
#	f1 = lib_path + files
#	if os.path.isfile(f1):
#		mydata.append(f1)
py2exe_options = {
	"includes":["sip","PyQt4._qt"],
	"dll_excludes":["MSVCP90.dll"],
	"compressed":1,
	"optimize":2,
	"ascii":0,
#	"packages":["lib_path"],
#	"bundle_files":1,
}
setup(windows = ["buildConfigHost.py"],
#	  data_files = mydata,
      name = "build",
	  version = "1.0",
#	  zipfile = None,
	  options = {"py2exe":py2exe_options}
	  )