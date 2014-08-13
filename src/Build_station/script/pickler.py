#*******************************************************************
#* Copyright (c) 2013 Freescale Semiconductor Inc.
#* All rights reserved.
#*
#* Use of Freescale code is governed by terms and conditions
#* stated in the accompanying licensing statement.
#* Description: pickle operation
#*
#* Revision History:
#* -----------------
#* Code Version    YYYY-MM-DD    Author        Description
#* 0.1             2014-03-1    Armand Wang    Create this file
#*******************************************************************
import os,sys
import cPickle as pickle


def SetInfo(applist_name,freemv_dir):
    '''
    {'applist':xxx}
    '''
    try:
        current_applist_file = freemv_dir + '/applist/CurrentApplist.pkl'
        if os.path.isfile(current_applist_file):
            f = file(current_applist_file,'rb')
            whole_info = pickle.load(f)
            f.close()
        else:
            whole_info = {}
        whole_info['applist'] = applist_name
        f = file(current_applist_file,'wb')
        pickle.dump(whole_info,f,True)
        f.close()
    except Exception,e:
        print e
        return 1
    else:
        return 0
def GetEnvInfo(freekv_dir,taskid,platform,ide,target):
    
    if 'Debug' in target:
        target = 'Debug'
    if 'Release' in target:
        target = 'Release'
    # 1 :has been done 0:no
    taskid = str(taskid)
    pickle_file = freekv_dir + '/temp/EnvRecord.pkl'
    try:
        f = file(pickle_file,'rb')
    except Exception,e:
        return (0,0,0)
    else:
        whole_info = pickle.load(f)
        f.close()
        app_info = 0
        pre_configure = 0
        build_lib = 0
        if whole_info.has_key(taskid):
            if whole_info[taskid].has_key(platform):
                if whole_info[taskid][platform].has_key(ide):
                    app_info = 1
                if whole_info[taskid][platform].has_key('pre_configure'):
                    pre_configure = 1
                if whole_info[taskid][platform].has_key(ide+'_'+target):
                    build_lib = 1
                return (app_info,pre_configure,build_lib)
            else:
                return (0,0,0)
        else:
            return (0,0,0)
def GetEnvInfo_demo(freekv_dir,taskid,platform,ide,target):
    if 'Debug' in target:
        target = 'Debug'
    if 'Release' in target:
        target = 'Release'
    # 1 :has been done 0:no
    taskid = str(taskid)
    pickle_file = freekv_dir + '/temp/EnvRecord.pkl'
    try:
        f = file(pickle_file,'rb')
    except Exception,e:
        return (0,0,0)
    else:
        whole_info = pickle.load(f)
        f.close()
        app_info = 0
        pre_configure = 0
        build_lib = 0
        if whole_info.has_key(taskid):
            if whole_info[taskid].has_key(platform):
                if whole_info[taskid][platform].has_key(ide):
                    app_info = 1
                if whole_info[taskid][platform].has_key('pre_configure'):
                    pre_configure = 1
                if whole_info[taskid][platform].has_key(ide+'_'+target):
                    build_lib = 1
                return (app_info,pre_configure,build_lib)
            else:
                return (0,0,0)
        else:
            return (0,0,0)
