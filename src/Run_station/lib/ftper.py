#!/usr/bin/env python
# coding=utf-8
 
#*******************************************************************
#* Copyright (c) 2013 Freescale Semiconductor Inc.
#* All rights reserved.
#*
#* Use of Freescale code is governed by terms and conditions
#* stated in the accompanying licensing statement.
#* Description: ftp operation function
#*
#* Revision History:
#* -----------------
#* Code Version    YYYY-MM-DD    Author        Description
#* 0.1             2013-12-03    Armand Wang    Create this file
#*******************************************************************

from ftplib import FTP  
import os,sys,string,datetime,time  
import socket
import logging
class FTPer:  
    def __init__(self, hostaddr, username, password, remotedir, port=21):  
        self.hostaddr = hostaddr  
        self.username = username  
        self.password = password  
        self.remotedir  = remotedir  
        self.port     = port  
        self.ftp      = FTP()  
        self.file_list = []  
    def __del__(self):  
        self.ftp.close()   
    def login(self):  
        ftp = self.ftp  
        try:   
            timeout = 300  
            socket.setdefaulttimeout(timeout)  
            ftp.set_pasv(True)  
            logging.info('connecting... ')  
            ftp.connect(self.hostaddr, self.port)  
            logging.info('connected!logging on %s...' %self.hostaddr)    
            ftp.login(self.username, self.password)  
            logging.info('successfully!')
        except Exception:  
            logging.info('connecting or logging failed')  
        try:  
            ftp.cwd(self.remotedir)  
        except(Exception):  
            logging.info ('check out dir failed')
    def path_process(self,path):
        # input '/dir1/dir2/dir3/'
        # output ['dir1','dir1/dir2','dir1/dir2/dir3']
        path = path.split('/')
        while(1):
            try:
                path.remove('')
            except Exception,e:
                break
        path_temp =[]
        for index,value in enumerate(path):
            path_temp.append('/'.join(path[:index+1]))
        return path_temp
  
    def download_file(self, localfile, remotefile):
        logging.info('>>>>>>>>>>>>downloading %s ... ...' %localfile)  
        file_handler = open(localfile, 'wb')  
        self.ftp.retrbinary('RETR %s'%(remotefile), file_handler.write)  
        file_handler.close()  
  
    def download_files(self, localdir='./', remotedir='./'):  
        try:  
            self.ftp.cwd(remotedir)  
        except:  
            logging.info('dir %s not exist，going on...' %remotedir)  
            return  
        if not os.path.isdir(localdir):  
            os.makedirs(localdir)   
        self.file_list = []  
        self.ftp.dir(self.get_file_list)  
        remotenames = self.file_list   
        for item in remotenames:  
            filetype = item[0]  
            filename = item[1]  
            local = os.path.join(localdir, filename)  
            if filetype == 'd':  
                self.download_files(local, filename)  
            elif filetype == '-':  
                self.download_file(local, filename)  
        self.ftp.cwd('..')   
    def upload_file(self, localfile, remotefile):  
        if not os.path.isfile(localfile):  
            return
        remote_path = os.path.dirname(remotefile)
        path_list = self.path_process(remote_path)
        for path in path_list:
            try:
                self.ftp.mkd(path)
            except Exception,e:
                pass
        file_handler = open(localfile, 'rb')  
        self.ftp.storbinary('STOR %s' %remotefile, file_handler)  
        file_handler.close()  
        logging.info('send successfully: %s' %localfile)
    def upload_file1(self, localfile, remotefile):
        self.ftp.cwd('/')
        if not os.path.isfile(localfile):  
            return
        remote_path = os.path.dirname(remotefile)
        path_list = self.path_process(remote_path)
        for path in path_list:
            try:
                self.ftp.mkd(path)
            except Exception,e:
                pass
        file_handler = open(localfile, 'rb')  
        self.ftp.storbinary('STOR %s' %remotefile, file_handler)  
        file_handler.close()  
        logging.info('send successfully: %s' %localfile)  

    def upload_files(self, localdir='./', remotedir = './'):  
        if not os.path.isdir(localdir):  
            return  
        localnames = os.listdir(localdir)
        path_list = self.path_process(remotedir)
        for path in path_list:
            try:
                self.ftp.mkd(path)
            except Exception,e:
                pass
        self.ftp.cwd(remotedir)  
        for item in localnames:  
            src = os.path.join(localdir, item)  
            if os.path.isdir(src):  
                try:  
                    self.ftp.mkd(item)  
                except:  
                    logging.info('dir already exist %s' %item)  
                self.upload_files(src, item)  
            else:  
                self.upload_file(src, item)  
        self.ftp.cwd('..')
  
    def get_file_list(self, line):  
        ret_arr = []  
        file_arr = self.get_filename(line)  
        if file_arr[1] not in ['.', '..']:  
            self.file_list.append(file_arr)  
              
    def get_filename(self, line):  
        pos = line.rfind(':')  
        while(line[pos] != ' '):  
            pos += 1  
        while(line[pos] == ' '):  
            pos += 1  
        file_arr = [line[0], line[pos:]]  
        return file_arr

  
if __name__ == '__main__':  
     hostaddr = '10.192.244.198'
     username = 'ubuntu'
     password = 'ubuntu'
     port  =  21
     rootdir_remote = '/'
     
     f = FTPer(hostaddr, username, password, rootdir_remote, port)
     f.login()
     #f.download_file('c:/wei.txt','/wang.txt')
     #f.download_files('c:/do', '/bin')
     #f.upload_files('c:/yaml','/test/wang/wei/')
     #f.upload_file('c:/arg.py','/bin/76/oobe_mqx_lwdemo_twrk70f120m_iar/2014-01-06-14-27-17/arg2.py')
