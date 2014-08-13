#!/usr/bin/env python
# coding=utf-8

#*******************************************************************
#* Copyright (c) 2013 Freescale Semiconductor Inc.
#* All rights reserved.
#*
#* Use of Freescale code is governed by terms and conditions
#* stated in the accompanying licensing statement.
#* Description: serial helper function.
#*
#* Revision History:
#* -----------------
#* Code Version    YYYY-MM-DD    Author        Description
#* 0.1             2013-07-15    Larry Shen    Create this file
#*******************************************************************

import os, sys

import serial
import string

class SerialHelper:
    def __init__(self):
        self.ser = None

    def open(self, port):
        serial_port = string.atoi(port) - 1
        self.ser = serial.Serial(port=serial_port, baudrate=115200, timeout=90)

    def close(self):
        if self.ser:
            if self.ser.isOpen():
                self.ser.close()
