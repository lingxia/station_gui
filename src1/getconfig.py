# coding=utf-8
 
#*******************************************************************
#* Copyright (c) 2013 Freescale Semiconductor Inc.
#* All rights reserved.
#*
#* Use of Freescale code is governed by terms and conditions
#* stated in the accompanying licensing statement.
#* Description: get configuration from xml
#*
#* Revision History:
#* -----------------
#* Code Version    YYYY-MM-DD    Author        Description
#* 0.1             2014-01-11    Armand Wang    Create this file
#*******************************************************************

from xml.etree import ElementTree
import logging
from xml.etree.ElementTree import (Element,
                                   SubElement,
                                   Comment,
                                   tostring,
                                   )

class Getconfig():
    def __init__(self,config_file):
        self.config = config_file
    def getall_nodes(self):
        node_list=[]
        try:
            with open(self.config,'rt') as f:
                tree = ElementTree.parse(f)
                node_list = [node
                             for node in tree.iter()
                             ]
            return node_list
        except Exception,e:
            logging.info(e)
            return None
    def getValue(self,tagname):
        node_list = self.getall_nodes()
        for node in node_list:
            if node.tag == tagname:
                return node.text
        logging.info('Can not get value of '+ tagname)
        return None
    def getAttr(self,tagname,Attribute):
        node_list = self.getall_nodes()
        if node_list == None:
            return None
        for node in node_list:
            if node.tag == tagname:
                return node.attrib.get(Attribute)
        logging.info('Can not get value of '+ tagname)
        return None
    def getAttr_list(self,tagname):
        node_list = self.getall_nodes()
        if node_list == None:
            return None
        for node in node_list:
            if node.tag == tagname:
                return node.attrib
        return None
    def getChildTextList(self,father_tag):
        text_list = []
        node_list = self.getall_nodes()
        for node in node_list:
            if node.tag == father_tag:
                for child in node:
                    text_list.append(child.text)
        return text_list
    def getChildTagList(self,father_tag):
        tag_list = []
        node_list = self.getall_nodes()
        for node in node_list:
            if node.tag == father_tag:
                for child in node:
                    tag_list.append(child.tag)
        return tag_list

    def addChild(self,father_tag,child_tag,child_text):
        with open(self.config,'rt') as f:
            tree = ElementTree.parse(f)
            for node in tree.iter():
                if node.tag ==father_tag:
                    child = SubElement(node,child_tag)
                    child.text = child_text
                tree.write(self.config)
    def setValue(self,tagname,value):
        with open(self.config,'rt') as f:
            tree = ElementTree.parse(f)
            for node in tree.iter():
                if node.tag == tagname:
                    node.text = value
            tree.write(self.config)
    def setAttr(self,tagname,Attribute,value):
        with open(self.config,'rt') as f:
            tree = ElementTree.parse(f)
            for node in tree.iter():
                if node.tag == tagname:
                    node.attrib[Attribute] = value
            tree.write(self.config)
