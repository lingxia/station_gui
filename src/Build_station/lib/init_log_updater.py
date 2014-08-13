#!/usr/bin/env python
# coding=utf-8

#*******************************************************************
#* Copyright (c) 2013 Freescale Semiconductor Inc.
#* All rights reserved.
#*
#* Use of Freescale code is governed by terms and conditions
#* stated in the accompanying licensing statement.
#* Description: logging init
#*
#* Revision History:
#* -----------------
#* Code Version    YYYY-MM-DD    Author        Description
#* 0.1             2013-07-19    Larry Shen    Create this file
#*******************************************************************

import logging
import logging.config
import os

file_path = os.path.dirname(os.path.abspath(__file__))
main_path = os.path.join(file_path, '../')

log_file = main_path + '//log//updater_station.log'
log_conf = main_path + '/config/logger.conf'


logging.config.fileConfig(log_conf, defaults=dict(log_file=log_file))
