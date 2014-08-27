from PyQt4 import QtGui,QtCore 
import sys,os

file_path = os.path.dirname(os.path.abspath("__file__"))
main_path = os.path.join(file_path,'../')
designer_path = main_path + '/designer_window/'
runStation_path = main_path + '/Run_station/'
config_path = runStation_path + '/config/'
lib_path = runStation_path + '/lib/'
pic_path = main_path + '/pic/'


sys.path.append(lib_path)
sys.path.append(designer_path)
sys.path.append(config_path)
sys.path.append(runStation_path)

from getconfig import Getconfig
from runConfigUi import Ui_runConfig
import platform_list
from get_local_config import Get_DP_info
import win32api

config_file_run = config_path + 'config.xml'
config_run_file = Getconfig(config_file_run)

class runStationConfig(QtGui.QMainWindow):
    def __init__(self,parent = None):         
        QtGui.QWidget.__init__(self,parent)
        self.runConfigWin = Ui_runConfig()
        self.runConfigWin.setupUi(self)
        self.setFixedSize(self.width(), self.height())
        self.debuggerSelect()
        self.addOrRemovePlaforms()
        self.dapeng_info = Get_DP_info()
        self.tokenFlag = True

#*******************some attributes******************
        self.device = platform_list.device_type
        self.platform_select = platform_list.platform_list
        self.testsuite_select = platform_list.test_suite
        self.testsuite_existed_seq = []
        self.testsuite_existed_name = []
        self.jlink_platform_existed_seq = []
        self.jlink_platform_existed_name = []
        self.lauterbach_platform_existed_seq = []
        self.lauterbach_platform_existed_name = []
                
#*********** MenuBar, ToolBar, StatusBar ************        
        self.menuBar = self.menuBar()
        self.toolBar = self.addToolBar("ToolBar")
        self.statuBar = self.statusBar()

#********************* Actions ********************** 
        self.saveAct = QtGui.QAction(QtGui.QIcon(pic_path + "/save.png"),"Save",self)
        self.saveAct.setShortcut("Ctrl+S")
        self.saveAct.setStatusTip("Save the Configuration File !")
        self.saveAct.whatsThis()
        self.connect(self.saveAct, QtCore.SIGNAL("triggered()"),self.saveRun)
        self.connect(self.saveAct, QtCore.SIGNAL("triggered()"),self.saveEvent)
        
        self.quitAct = QtGui.QAction(QtGui.QIcon(pic_path + "/quit.png"),"Quit",self)
        self.quitAct.setShortcut("Ctrl+Q")
        self.quitAct.setStatusTip("Quit the Configuration without saving the File")
        self.saveAct.whatsThis()
        self.connect(self.quitAct, QtCore.SIGNAL("triggered()"),self.close)
        
        self.whatAct = QtGui.QAction(QtGui.QIcon(pic_path + "/what.png"),"What's this?",self)
        self.whatAct.setShortcut("Ctrl+W")
        self.whatAct.setStatusTip("Brief Introdution of this GUI")
        self.whatAct.whatsThis()
        self.connect(self.whatAct, QtCore.SIGNAL("triggered()"),self.whatEvent)
        
        self.howAct = QtGui.QAction(QtGui.QIcon(pic_path + "/use.png"),"How to use?",self)
        self.howAct.setShortcut("Ctrl+U")
        self.howAct.setStatusTip("Brief Usage of this GUI")
        self.howAct.whatsThis()
        self.connect(self.howAct, QtCore.SIGNAL("triggered()"),self.howEvent)
        
        
#****************add Menus and Actions**************
        self.fileMenu = self.menuBar.addMenu("File")
        self.fileMenu.addAction(self.saveAct)
        self.fileMenu.addAction(self.quitAct)
        
        self.helpMenu = self.menuBar.addMenu("Help")
        self.helpMenu.addAction(self.whatAct)
        self.helpMenu.addAction(self.howAct)
        
        self.toolBar.addAction(self.saveAct)
        self.toolBar.addAction(self.quitAct)
        
        self.testsuiteFlag = True
        self.addOrRemoveTestsuite()
        self.getPreConfig()
        
        self.connect(self.runConfigWin.jlinkOpenButton, QtCore.SIGNAL("clicked()"),self.openJlink)
        self.connect(self.runConfigWin.trace32OpenButton, QtCore.SIGNAL("clicked()"),self.openTrace)
        self.connect(self.runConfigWin.jlinkAddButton, QtCore.SIGNAL("clicked()"),self.saveJlinkPlatform)
        self.connect(self.runConfigWin.traceAddButton, QtCore.SIGNAL("clicked()"),self.saveTracePlatform)
        
        
#***************some event with messagebox***************        
    def closeEvent(self,event):
        reply = QtGui.QMessageBox.warning(self, 'Warning', \
                                           'Are you sure to Quit ? Please make sure your Configurations had been Saved !',\
                                            QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
        if reply == QtGui.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
    
    def saveEvent(self):
        if self.tokenFlag == True and self.testsuiteFlag == True:
            QtGui.QMessageBox.information(self,"Information",\
                                          "The Configuration File has been Saved Successfully !", QtGui.QMessageBox.Ok)
        else:
            pass
    
    def whatEvent(self):
        QtGui.QMessageBox.information(self,"What is this",\
                                          "This is a GUI to configurate the environment of your Run Stations !",\
                                           QtGui.QMessageBox.Ok)
    
    def howEvent(self):
        QtGui.QMessageBox.information(self,"How to use",\
                                          "Configurate your Run Station to be private or not, give a token if private !" + 
                                          "  Then give the right path of each Debugger that you need and add the Platforms you need !" + 
                                          " Don't forget to Save the configuration !",\
                                           QtGui.QMessageBox.Ok)
        
        
#***************add Platform and Device_Type********
    def addOrRemovePlaforms(self):
        self.platform_select = platform_list.platform_list
        length = len(self.platform_select)
        
        for num in range(0,length):
            self.runConfigWin.jlinkPlatformComboBox.addItem("")
            self.runConfigWin.lauterbachPlatformComboBox.addItem("")
            self.runConfigWin.jlinkPlatformComboBox.setItemText(num,self.platform_select[num])
            self.runConfigWin.lauterbachPlatformComboBox.setItemText(num,self.platform_select[num])
        self.connect(self.runConfigWin.jlinkPlatformComboBox,QtCore.SIGNAL("activated(int)"),self.jlinkPlatformAdd)
        self.connect(self.runConfigWin.jlinkTreeWidget, QtCore.SIGNAL("itemActivated(QTreeWidgetItem*,int)"),self.jlinkGetCurrentItem)
        self.connect(self.runConfigWin.jlinkRemoveButton,QtCore.SIGNAL("clicked()"),self.jlinkPlatformRemove)
        self.connect(self.runConfigWin.lauterbachPlatformComboBox,QtCore.SIGNAL("activated(int)"),self.lauterbachPlatformAdd)           
        self.connect(self.runConfigWin.lauterbachTreeWidget, QtCore.SIGNAL("itemActivated(QTreeWidgetItem*,int)"),self.lauterbachGetCurrentItem)
        self.connect(self.runConfigWin.lauterbachRemoveButton,QtCore.SIGNAL("clicked()"),self.lauterbachPlatformRemove)
        
#*****************add platforms with jlink*******************
    def jlinkPlatformAdd(self):
        seq = self.runConfigWin.jlinkPlatformComboBox.currentIndex()
        if (self.runConfigWin.jlinkPlatformComboBox.itemText(seq) == self.platform_select[seq]) and seq not in self.jlink_platform_existed_seq:
            self.jlink_platform_existed_seq.append(seq)
            self.jlink_platform_existed_name.append(self.platform_select[seq])
            self.Platform = QtGui.QTreeWidgetItem(self.runConfigWin.jlinkTreeWidget)
            editableFlag = self.Platform.flags() 
            self.Platform.setFlags(editableFlag | QtCore.Qt.ItemIsEditable)
            self.Platform.setText(0,self.platform_select[seq])
            self.Platform.setText(1,self.device[seq])
            
#************************get current Item****************************
    def jlinkGetCurrentItem(self):
        self.currentItem = self.runConfigWin.jlinkTreeWidget.currentItem()
        if self.currentItem == None:
            pass
        else:
            return self.currentItem
             
#*****************remove a platform of jlink*************************    
    def jlinkPlatformRemove(self):
        self.currentItemGot = self.jlinkGetCurrentItem()
        if self.currentItemGot == None:
            pass
        else:
            self.platformName = self.currentItemGot.text(0)
        if self.platformName in self.jlink_platform_existed_name:
            self.runConfigWin.jlinkTreeWidget.takeTopLevelItem(self.runConfigWin.jlinkTreeWidget.indexOfTopLevelItem(self.currentItemGot))            
            self.jlink_platform_existed_name.remove(self.platformName)
            self.jlink_platform_existed_seq.remove(self.platform_select.index(self.platformName))


#*****************add platforms with lauterbach*******************
    def lauterbachPlatformAdd(self):
        seq = self.runConfigWin.lauterbachPlatformComboBox.currentIndex()
        if (self.runConfigWin.lauterbachPlatformComboBox.itemText(seq) == self.platform_select[seq]) and seq not in self.lauterbach_platform_existed_seq:
            self.lauterbach_platform_existed_seq.append(seq)
            self.lauterbach_platform_existed_name.append(self.platform_select[seq])
            self.Platform = QtGui.QTreeWidgetItem(self.runConfigWin.lauterbachTreeWidget)
            editableFlag = self.Platform.flags() 
            self.Platform.setFlags(editableFlag | QtCore.Qt.ItemIsEditable)
            self.Platform.setText(0,self.platform_select[seq])
            self.Platform.setText(1,self.device[seq])
            
            
            
#************************get current Item****************************
    def lauterbachGetCurrentItem(self):
        self.currentItem = self.runConfigWin.lauterbachTreeWidget.currentItem()
        if self.currentItem == None:
            return
        else:
            return self.currentItem
        
             
#*****************remove a platform of lauterbach*************************    
    def lauterbachPlatformRemove(self):
        self.currentItemGot = self.lauterbachGetCurrentItem()
        if self.currentItemGot == None:
            return
        else:
            self.platformName = self.currentItemGot.text(0)
        if self.platformName in self.lauterbach_platform_existed_name:
            self.runConfigWin.lauterbachTreeWidget.takeTopLevelItem(self.runConfigWin.lauterbachTreeWidget.indexOfTopLevelItem(self.currentItemGot))
            self.lauterbach_platform_existed_name.remove(self.platformName)
            self.lauterbach_platform_existed_seq.remove(self.platform_select.index(self.platformName))

            

#*************Debugger configurate *****************
    def debuggerSelect(self):
        self.jlinkItem = self.runConfigWin.debuggerListWidget.item(0)
        self.lauterbachItem = self.runConfigWin.debuggerListWidget.item(1)
        self.connect(self.runConfigWin.debuggerListWidget, QtCore.SIGNAL("itemClicked(QListWidgetItem*)"),self.debuggerPageShow)        
       

 

#***********Different debugger configurate page*******    
    def debuggerPageShow(self):
        if self.runConfigWin.debuggerListWidget.isItemSelected(self.jlinkItem):
            self.runConfigWin.jlinkPage.show()
            self.runConfigWin.lauterbachPage.hide()
                        
        elif self.runConfigWin.debuggerListWidget.isItemSelected(self.lauterbachItem):
            self.runConfigWin.lauterbachPage.show()
            self.runConfigWin.jlinkPage.hide()

#**********private station without set token, show the warning   
    def tokenWarning(self):
        QtGui.QMessageBox.warning(self, "Warning","Set a token please !", QtGui.QMessageBox.Ok)
        
    def getPreConfig(self):
        tokenPre = config_run_file.getValue("token")
        privatePre = config_run_file.getAttr("token","private")
        
        oobePre = config_run_file.getAttr("FreeMV", "enable")
        ksdkoobePre = config_run_file.getAttr("FreeMV_ksdk", "enable")
        ksvPre = config_run_file.getAttr("FreeKV", "enable")
        demoPre = config_run_file.getAttr("FreeKV_demo", "enable")
        usbPre = config_run_file.getAttr("FreeKV_usb", "enable")
        unittestPre = config_run_file.getAttr("FreeKV_unit_test", "enable")
        
        jlinkPre = config_run_file.getValue("jlink")
        trace32Pre = config_run_file.getValue("trace32")
        jlinkFlagPre = config_run_file.getAttr("hardware_debugger", "jlink")
        trace32FlagPre = config_run_file.getAttr("hardware_debugger", "lauterbach")
        
        if jlinkFlagPre == "yes":
            try:
                self.runConfigWin.jlinkLineEdit.setText(jlinkPre)
            except Exception:
                pass
        else:
            pass
        
        if trace32FlagPre == "yes":
            try:
                self.runConfigWin.trace32LineEdit.setText(trace32Pre)
            except Exception:
                pass
        else:
            pass
        
        if privatePre == "yes":
            self.runConfigWin.tokenLineEdit.setText(tokenPre)
            self.runConfigWin.privateCheckBox.setCheckState(QtCore.Qt.Checked)
        else:
            pass
        
        
        if oobePre == "yes":
            self.testsuite_existed_name.append(self.testsuite_select[0])
            self.testsuite_existed_seq.append(0)
            oobeTestsuite = QtGui.QTreeWidgetItem(self.runConfigWin.testsuiteTreeWidget)
            editableFlag = oobeTestsuite.flags() 
            oobeTestsuite.setFlags(editableFlag | QtCore.Qt.ItemIsEditable)
            oobeTestsuite.setText(0,self.testsuite_select[0])
        else:
            pass
        
        if ksdkoobePre == "yes":
            self.testsuite_existed_name.append(self.testsuite_select[1])
            self.testsuite_existed_seq.append(1)
            kskdoobeTestsuite = QtGui.QTreeWidgetItem(self.runConfigWin.testsuiteTreeWidget)
            editableFlag = kskdoobeTestsuite.flags() 
            kskdoobeTestsuite.setFlags(editableFlag | QtCore.Qt.ItemIsEditable)
            kskdoobeTestsuite.setText(0,self.testsuite_select[1])
        else:
            pass
        
        if ksvPre == "yes":
            self.testsuite_existed_name.append(self.testsuite_select[2])
            self.testsuite_existed_seq.append(2)
            ksvTestsuite = QtGui.QTreeWidgetItem(self.runConfigWin.testsuiteTreeWidget)
            editableFlag = ksvTestsuite.flags() 
            ksvTestsuite.setFlags(editableFlag | QtCore.Qt.ItemIsEditable)
            ksvTestsuite.setText(0,self.testsuite_select[2])
        else:
            pass
        
        if demoPre == "yes":
            self.testsuite_existed_name.append(self.testsuite_select[3])
            self.testsuite_existed_seq.append(3)
            demoTestsuite = QtGui.QTreeWidgetItem(self.runConfigWin.testsuiteTreeWidget)
            editableFlag = demoTestsuite.flags() 
            demoTestsuite.setFlags(editableFlag | QtCore.Qt.ItemIsEditable)
            demoTestsuite.setText(0,self.testsuite_select[3])
        else:
            pass
        
        if usbPre == "yes":
            self.testsuite_existed_name.append(self.testsuite_select[4])
            self.testsuite_existed_seq.append(4)
            usbTestsuite = QtGui.QTreeWidgetItem(self.runConfigWin.testsuiteTreeWidget)
            editableFlag = usbTestsuite.flags() 
            usbTestsuite.setFlags(editableFlag | QtCore.Qt.ItemIsEditable)
            usbTestsuite.setText(0,self.testsuite_select[4])
        else:
            pass
        
        if unittestPre == "yes":
            self.testsuite_existed_name.append(self.testsuite_select[5])
            self.testsuite_existed_seq.append(5)
            unittestTestsuite = QtGui.QTreeWidgetItem(self.runConfigWin.testsuiteTreeWidget)
            editableFlag = unittestTestsuite.flags() 
            unittestTestsuite.setFlags(editableFlag | QtCore.Qt.ItemIsEditable)
            unittestTestsuite.setText(0,self.testsuite_select[5])
        else:
            pass
        
        
#*********************get Pre platform********************        
        platformPre = config_run_file.getChildTagList("device")
        platformPreNum = len(platformPre)
        if jlinkFlagPre == "yes":
            for num in range(0,platformPreNum):
                if config_run_file.getValue(platformPre[num]) == "yes":
                    self.jlink_platform_existed_name.append(platformPre[num])
                    self.jlink_platform_existed_seq.append(self.platform_select.index(platformPre[num]))
                    device_type = config_run_file.getAttr(platformPre[num], "device_type")
                    debug_port = config_run_file.getAttr(platformPre[num], "debug_port")
                    serial_port = config_run_file.getAttr(platformPre[num], "serial_port")
                    jlinkPlatformPre = QtGui.QTreeWidgetItem(self.runConfigWin.jlinkTreeWidget)
                    jlinkEditableFlag = jlinkPlatformPre.flags() 
                    jlinkPlatformPre.setFlags(jlinkEditableFlag | QtCore.Qt.ItemIsEditable)
                    jlinkPlatformPre.setText(0,platformPre[num])
                    jlinkPlatformPre.setText(1,device_type)
                    jlinkPlatformPre.setText(2,debug_port)
                    jlinkPlatformPre.setText(3,serial_port)
                else:
                    pass
        else:
            pass
        
        if trace32FlagPre == "yes":
            for num in range(0,platformPreNum):
                if config_run_file.getValue(platformPre[num]) == "yes":
                    self.lauterbach_platform_existed_name.append(platformPre[num])
                    self.lauterbach_platform_existed_seq.append(self.platform_select.index(platformPre[num]))
                    device_type = config_run_file.getAttr(platformPre[num], "device_type")
                    serial_port = config_run_file.getAttr(platformPre[num], "serial_port")
                    lauterbachPlatformPre = QtGui.QTreeWidgetItem(self.runConfigWin.lauterbachTreeWidget)
                    lauterbachEditableFlag = lauterbachPlatformPre.flags() 
                    lauterbachPlatformPre.setFlags(lauterbachEditableFlag | QtCore.Qt.ItemIsEditable)
                    lauterbachPlatformPre.setText(0,platformPre[num])
                    lauterbachPlatformPre.setText(1,device_type)
                    lauterbachPlatformPre.setText(2,serial_port)
                else:
                    pass
        else:
            pass            
                            
                
            

#******************open dir of jlink and trace32**********
    def openJlink(self):
        jlinkDir = QtGui.QFileDialog.getExistingDirectory(self, QtCore.QString(),\
                                                          "C:/",QtGui.QFileDialog.ShowDirsOnly | QtGui.QFileDialog.DontResolveSymlinks)
        self.runConfigWin.jlinkLineEdit.setText(jlinkDir)        
    
    def openTrace(self):
        traceDir = QtGui.QFileDialog.getExistingDirectory(self, QtCore.QString(),\
                                                          "C:/",QtGui.QFileDialog.ShowDirsOnly | QtGui.QFileDialog.DontResolveSymlinks)
        self.runConfigWin.trace32LineEdit.setText(traceDir)


#*****************following functions are about testsuite*************
    def addOrRemoveTestsuite(self):
        length = len(self.testsuite_select)
        
        for num in range(0,length):
            self.runConfigWin.testSuiteComboBox.addItem("")
            self.runConfigWin.testSuiteComboBox.setItemText(num,self.testsuite_select[num])
        self.connect(self.runConfigWin.testSuiteComboBox,QtCore.SIGNAL("activated(int)"),self.testsuiteFill)
        self.connect(self.runConfigWin.testsuiteTreeWidget, QtCore.SIGNAL("itemActivated(QTreeWidgetItem*,int)"),self.testsuiteGetCurrentItem)
        self.connect(self.runConfigWin.testSuiteRemoveButton,QtCore.SIGNAL("clicked()"),self.testsuitePlatformRemove)
#        self.connect(self.runConfigWin.testSuiteAddButton, QtCore.SIGNAL("clicked()"),self.testsuiteAdd)

    def testsuiteFill(self):
        seq = self.runConfigWin.testSuiteComboBox.currentIndex()
        if (self.runConfigWin.testSuiteComboBox.itemText(seq) == self.testsuite_select[seq]) and seq not in self.testsuite_existed_seq:
            self.testsuite_existed_seq.append(seq)
            self.testsuite_existed_name.append(self.testsuite_select[seq])
            self.Testsuite = QtGui.QTreeWidgetItem(self.runConfigWin.testsuiteTreeWidget)
            editableFlag = self.Testsuite.flags() 
            self.Testsuite.setFlags(editableFlag | QtCore.Qt.ItemIsEditable)
            self.Testsuite.setText(0,self.testsuite_select[seq])
            
    def testsuiteGetCurrentItem(self):
        self.currentItem = self.runConfigWin.testsuiteTreeWidget.currentItem()
        if self.currentItem == None:
            pass
        else:
            return self.currentItem
        
    def testsuitePlatformRemove(self):
        self.currentItemGot = self.testsuiteGetCurrentItem()
        if self.currentItemGot == None:
            pass
        else:
            self.testsuiteName = self.currentItemGot.text(0)
        if self.testsuiteName in self.testsuite_existed_name:
            self.runConfigWin.testsuiteTreeWidget.takeTopLevelItem(self.runConfigWin.testsuiteTreeWidget.indexOfTopLevelItem(self.currentItemGot))
            self.testsuite_existed_name.remove(self.testsuiteName)
            self.testsuite_existed_seq.remove(self.testsuite_select.index(self.testsuiteName))
            
    def testsuiteAdd(self):
        flag = True
#        length = len(self.testsuite_select)
#        if self.dapeng_info["exist"] == "no":
#            pass
#        else:
#            freemv_run_path_long = self.dapeng_info['path'] + '/freemvrun'
#            freekv_run_path_long = self.dapeng_info['path'] + '/freekvrun'
#            freekv_demo_run_path_long = self.dapeng_info['path'] + '/freekv_demorun'
#            freemv_run_path = win32api.GetShortPathName(freemv_run_path_long)
#            freekv_run_path = win32api.GetShortPathName(freekv_run_path_long)
#            freekv_demo_run_path = win32api.GetShortPathName(freekv_demo_run_path_long)
#        
#        for num in range(0,length):
#            try:
#                testsuiteIn = self.runConfigWin.testsuiteTreeWidget.topLevelItem(num).text(0)
#                if testsuiteIn == "KSDK-DEMO":
#                    config_run_file.setAttr("FreeKV_demo", "enable", "yes")
#                    config_run_file.setValue("FreeKV_demo", freekv_demo_run_path)
#                    break
#                else:
#                    config_run_file.setAttr("FreeKV_demo", "enable", "no")                   
#            except Exception:
#                pass
#            
#        for num in range(0,length):
#            try:
#                testsuiteIn = self.runConfigWin.testsuiteTreeWidget.topLevelItem(num).text(0)
#                if testsuiteIn == "KSDK-USB":
#                    config_run_file.setAttr("FreeKV_usb", "enable", "yes")
#                    config_run_file.setValue("FreeKV_usb", freekv_demo_run_path)
#                    break
#                else:
#                    config_run_file.setAttr("FreeKV_usb", "enable", "no")                   
#            except Exception:
#                pass
#
#        for num in range(0,length):
#            try:
#                testsuiteIn = self.runConfigWin.testsuiteTreeWidget.topLevelItem(num).text(0)
#                if testsuiteIn == "KSDK-UnitTest":
#                    config_run_file.setAttr("FreeKV_unit_test", "enable", "yes")
#                    config_run_file.setValue("FreeKV_unit_test", freekv_demo_run_path)
#                    break
#                else:
#                    config_run_file.setAttr("FreeKV_unit_test", "enable", "no")                   
#            except Exception:
#                pass
#            
#        for num in range(0,length):
#            try:
#                testsuiteIn = self.runConfigWin.testsuiteTreeWidget.topLevelItem(num).text(0)
#                if testsuiteIn == "MQX-OOBE":
#                    config_run_file.setAttr("FreeMV", "enable", "yes")
#                    config_run_file.setValue("FreeMV", freemv_run_path)
#                    break
#                else:
#                    config_run_file.setAttr("FreeMV", "enable", "no")                   
#            except Exception:
#                pass               
#
#        for num in range(0,length):
#            try:
#                testsuiteIn = self.runConfigWin.testsuiteTreeWidget.topLevelItem(num).text(0)
#                if testsuiteIn == "KSDK-MQX-OOBE":
#                    config_run_file.setAttr("FreeMV_ksdk", "enable", "yes")
#                    config_run_file.setValue("FreeMV_ksdk", freemv_run_path)
#                    break
#                else:
#                    config_run_file.setAttr("FreeMV_ksdk", "enable", "no")                   
#            except Exception:
#                pass    
#
#        for num in range(0,length):
#            try:
#                testsuiteIn = self.runConfigWin.testsuiteTreeWidget.topLevelItem(num).text(0)
#                if testsuiteIn == "KSV":
#                    config_run_file.setAttr("FreeKV", "enable", "yes")
#                    config_run_file.setValue("FreeKV", freekv_run_path)
#                    break
#                else:
#                    config_run_file.setAttr("FreeKV", "enable", "no")                   
#            except Exception:
#                pass 
#
#        if self.runConfigWin.testsuiteTreeWidget.topLevelItem(0) == None and flag == True:
#            flag = False
#            QtGui.QMessageBox.information(self,"Warning","You have not select any Test Suite, please select at least one !",QtGui.QMessageBox.Ok)
#        else:
#            pass    
#
#        if flag == True:
#            QtGui.QMessageBox.information(self,"Information","Add the Test Suites successful !",QtGui.QMessageBox.Ok)           


#***********************save configuration***************
    def saveRun(self):
        
#***************configurate and save private and token*****************       
        tokenSet = self.runConfigWin.tokenLineEdit.text()        
        if self.runConfigWin.privateCheckBox.checkState() == QtCore.Qt.Checked and tokenSet != "":
            self.tokenFlag = True
            config_run_file.setAttr("token", "private", "yes")
            config_run_file.setValue("token", tokenSet.__str__())
        elif self.runConfigWin.privateCheckBox.checkState() == QtCore.Qt.Checked and tokenSet == "":
            self.tokenFlag = False
            self.tokenWarning()     
        else:
            self.tokenFlag = True
            config_run_file.setAttr("token", "private", "no")
            
            
#*****************************save test suites**************************
        length = len(self.testsuite_select)
        if self.dapeng_info["exist"] == "no":
            pass
        else:
            freemv_run_path_long = self.dapeng_info['path'] + '/freemvrun'
            freekv_run_path_long = self.dapeng_info['path'] + '/freekvrun'
            freekv_demo_run_path_long = self.dapeng_info['path'] + '/freekv_demorun'
            freemv_run_path = win32api.GetShortPathName(freemv_run_path_long)
            freekv_run_path = win32api.GetShortPathName(freekv_run_path_long)
            freekv_demo_run_path = win32api.GetShortPathName(freekv_demo_run_path_long)
        
        for num in range(0,length):
            try:
                testsuiteIn = self.runConfigWin.testsuiteTreeWidget.topLevelItem(num).text(0)
                if testsuiteIn == "KSDK-DEMO":
                    config_run_file.setAttr("FreeKV_demo", "enable", "yes")
                    config_run_file.setValue("FreeKV_demo", freekv_demo_run_path)
                    break
                else:
                    config_run_file.setAttr("FreeKV_demo", "enable", "no")                   
            except Exception:
                pass
            
        for num in range(0,length):
            try:
                testsuiteIn = self.runConfigWin.testsuiteTreeWidget.topLevelItem(num).text(0)
                if testsuiteIn == "KSDK-USB":
                    config_run_file.setAttr("FreeKV_usb", "enable", "yes")
                    config_run_file.setValue("FreeKV_usb", freekv_demo_run_path)
                    break
                else:
                    config_run_file.setAttr("FreeKV_usb", "enable", "no")                   
            except Exception:
                pass

        for num in range(0,length):
            try:
                testsuiteIn = self.runConfigWin.testsuiteTreeWidget.topLevelItem(num).text(0)
                if testsuiteIn == "KSDK-UnitTest":
                    config_run_file.setAttr("FreeKV_unit_test", "enable", "yes")
                    config_run_file.setValue("FreeKV_unit_test", freekv_demo_run_path)
                    break
                else:
                    config_run_file.setAttr("FreeKV_unit_test", "enable", "no")                   
            except Exception:
                pass
            
        for num in range(0,length):
            try:
                testsuiteIn = self.runConfigWin.testsuiteTreeWidget.topLevelItem(num).text(0)
                if testsuiteIn == "MQX-OOBE":
                    config_run_file.setAttr("FreeMV", "enable", "yes")
                    config_run_file.setValue("FreeMV", freemv_run_path)
                    break
                else:
                    config_run_file.setAttr("FreeMV", "enable", "no")                   
            except Exception:
                pass               

        for num in range(0,length):
            try:
                testsuiteIn = self.runConfigWin.testsuiteTreeWidget.topLevelItem(num).text(0)
                if testsuiteIn == "KSDK-MQX-OOBE":
                    config_run_file.setAttr("FreeMV_ksdk", "enable", "yes")
                    config_run_file.setValue("FreeMV_ksdk", freemv_run_path)
                    break
                else:
                    config_run_file.setAttr("FreeMV_ksdk", "enable", "no")                   
            except Exception:
                pass    

        for num in range(0,length):
            try:
                testsuiteIn = self.runConfigWin.testsuiteTreeWidget.topLevelItem(num).text(0)
                if testsuiteIn == "KSV":
                    config_run_file.setAttr("FreeKV", "enable", "yes")
                    config_run_file.setValue("FreeKV", freekv_run_path)
                    break
                else:
                    config_run_file.setAttr("FreeKV", "enable", "no")                   
            except Exception:
                pass 

        if self.runConfigWin.testsuiteTreeWidget.topLevelItem(0) == None:
            self.testsuiteFlag = False
            QtGui.QMessageBox.information(self,"Warning","You have not select any Test Suite, please select at least one !",QtGui.QMessageBox.Ok)
        else:
            self.testsuiteFlag = True   
  


#*******************save platform warning********************
    def saveJlinkPlatform(self):
        
#****************configurate jlink and trace32 path***************
        jlinkSet = self.runConfigWin.jlinkLineEdit.text()
        if jlinkSet.__str__() == "":
            config_run_file.setAttr("hardware_debugger", "jlink", "no")
            config_run_file.setValue("jlink", "")
        else:
            jlinkShort = win32api.GetShortPathName(jlinkSet.__str__())
            config_run_file.setAttr("hardware_debugger", "jlink", "yes")
            config_run_file.setValue("jlink", jlinkShort)
            
        traceSet = self.runConfigWin.trace32LineEdit.text()        
        if traceSet.__str__() == "":
            config_run_file.setAttr("hardware_debugger", "lauterbach", "no")
            config_run_file.setValue("trace32", "")
        else:
            traceShort = win32api.GetShortPathName(traceSet.__str__())
            config_run_file.setAttr("hardware_debugger", "lauterbach", "yes")
            config_run_file.setValue("trace32", traceShort)            

        flagJlink = config_run_file.getAttr("hardware_debugger", "jlink")
        flagTrace = config_run_file.getAttr("hardware_debugger", "lauterbach")
                
        if flagJlink == "yes" and flagTrace == "no":
            if self.runConfigWin.jlinkTreeWidget.topLevelItem(0) == None:
                QtGui.QMessageBox.warning(self,"Warning","You have not add any Platform for Jlink, please add at least one !",QtGui.QMessageBox.Ok)
            else:
                self.savePlatform()
                QtGui.QMessageBox.information(self,"Information","Add platforms for Jlink successful ! Save the configuration please !",QtGui.QMessageBox.Ok)


        elif flagTrace == "no" and flagJlink == "no":
                QtGui.QMessageBox.warning(self,"Warning","You have not chose any debugger, chose one please !",QtGui.QMessageBox.Ok)
        
        elif flagTrace == "yes" and flagJlink == "yes":
                QtGui.QMessageBox.information(self,"Warning","Only one debugger is allowed !",QtGui.QMessageBox.Ok)
                
                
    def saveTracePlatform(self):
        
#****************configurate jlink and trace32 path***************
        jlinkSet = self.runConfigWin.jlinkLineEdit.text()
        if jlinkSet.__str__() == "":
            config_run_file.setAttr("hardware_debugger", "jlink", "no")
            config_run_file.setValue("jlink", "")
        else:
            jlinkShort = win32api.GetShortPathName(jlinkSet.__str__())
            config_run_file.setAttr("hardware_debugger", "jlink", "yes")
            config_run_file.setValue("jlink", jlinkShort)
            
        traceSet = self.runConfigWin.trace32LineEdit.text()        
        if traceSet.__str__() == "":
            config_run_file.setAttr("hardware_debugger", "lauterbach", "no")
            config_run_file.setValue("trace32", "")
        else:
            traceShort = win32api.GetShortPathName(traceSet.__str__())
            config_run_file.setAttr("hardware_debugger", "lauterbach", "yes")
            config_run_file.setValue("trace32", traceShort)            

        flagJlink = config_run_file.getAttr("hardware_debugger", "jlink")
        flagTrace = config_run_file.getAttr("hardware_debugger", "lauterbach")

        if flagTrace == "yes" and flagJlink == "no":
            if self.runConfigWin.lauterbachTreeWidget.topLevelItem(0) == None:
                QtGui.QMessageBox.warning(self,"Warning","You have not add any Platform for Lauterbach, please add at least one !",QtGui.QMessageBox.Ok)
            else:
                self.savePlatform()
                QtGui.QMessageBox.information(self,"Information","Add platforms for Lauterbach successful ! Save the configuration please !",QtGui.QMessageBox.Ok)
        
        elif flagTrace == "no" and flagJlink == "no":
                QtGui.QMessageBox.warning(self,"Warning","You have not chose any debugger, chose one please !",QtGui.QMessageBox.Ok)
        
        elif flagTrace == "yes" and flagJlink == "yes":
                QtGui.QMessageBox.information(self,"Warning","Only one debugger is allowed !",QtGui.QMessageBox.Ok)


#*********************configurate and save platforms********************
    def savePlatform(self):
        platform_len = len(self.platform_select)
        platform_in_config = config_run_file.getChildTagList("device")
        platform_in_len = len(platform_in_config)
        platform_set = []
        platform_set_len = 0
        jlinkFlag = config_run_file.getAttr("hardware_debugger", "jlink")
        traceFlag = config_run_file.getAttr("hardware_debugger", "lauterbach")

#***********************jlink platform configurate*********************
        if jlinkFlag == "yes":
            for num in range(0,platform_len):
                try:
                    platformAdd = self.runConfigWin.jlinkTreeWidget.topLevelItem(num).text(0)
                    platform = platformAdd.__str__()
                    if platform != "":
                        platform_set.append(platform)
                        platform_set_len += 1
                    else:
                            pass
                except Exception:
                    pass
     
            for num in range(0,platform_set_len):
                try:
                    platformSet = self.runConfigWin.jlinkTreeWidget.topLevelItem(num).text(0)       
                    deviceSet = self.runConfigWin.jlinkTreeWidget.topLevelItem(num).text(1)
                    debugSet = self.runConfigWin.jlinkTreeWidget.topLevelItem(num).text(2)
                    serialSet = self.runConfigWin.jlinkTreeWidget.topLevelItem(num).text(3)
                    platformStr = platformSet.__str__()
                    deviceStr = deviceSet.__str__()
                    debugStr = debugSet.__str__()
                    serialStr = serialSet.__str__()
                    platformFlag = config_run_file.getValue(platformStr)
                except Exception:
                    pass
                if platformStr in platform_in_config and platformFlag == "yes":
                    config_run_file.setAttr(platformStr, "debug_port", debugStr)
                    config_run_file.setAttr(platformStr, "serial_port", serialStr)
                    config_run_file.setAttr(platformStr, "device_type", deviceStr)
                elif platformStr in platform_in_config and platformFlag != "yes":
                    config_run_file.setValue(platformStr, "yes")
                    config_run_file.setAttr(platformStr, "debug_port", debugStr)
                    config_run_file.setAttr(platformStr, "serial_port", serialStr)
                    config_run_file.setAttr(platformStr, "device_type", deviceStr)
                elif platformStr not in platform_in_config:
                    platformAttrDic = {"debug_port":debugStr, "device_type":deviceStr,"serial_port":serialStr}
                    config_run_file.addChildAttr("device", platformStr, "yes", platformAttrDic)
                else:
                    pass
            
            for num in range(0,platform_in_len):
                if platform_in_config[num] not in platform_set:
                    config_run_file.setValue(platform_in_config[num], "no")
                else:
                    pass
        else:
            pass

#***********************lauterbach platform configurate************
        if traceFlag == "yes":
            for num in range(0,platform_len):
                try:
                    platformAdd = self.runConfigWin.lauterbachTreeWidget.topLevelItem(num).text(0)
                    platform = platformAdd.__str__()
                    if platform != "":
                        platform_set.append(platform)
                        platform_set_len += 1
                    else:
                            pass
                except Exception:
                    pass
     
            for num in range(0,platform_set_len):
                try:
                    platformSet = self.runConfigWin.lauterbachTreeWidget.topLevelItem(num).text(0)       
                    deviceSet = self.runConfigWin.lauterbachTreeWidget.topLevelItem(num).text(1)
                    serialSet = self.runConfigWin.lauterbachTreeWidget.topLevelItem(num).text(2)
                    platformStr = platformSet.__str__()
                    deviceStr = deviceSet.__str__()
                    debugStr = ""
                    serialStr = serialSet.__str__()
                    platformFlag = config_run_file.getValue(platformStr)
                except Exception:
                    pass
                if platformStr in platform_in_config and platformFlag == "yes":
                    config_run_file.setAttr(platformStr, "debug_port", debugStr)
                    config_run_file.setAttr(platformStr, "serial_port", serialStr)
                    config_run_file.setAttr(platformStr, "device_type", deviceStr)
                elif platformStr in platform_in_config and platformFlag != "yes":
                    config_run_file.setValue(platformStr, "yes")
                    config_run_file.setAttr(platformStr, "debug_port", debugStr)
                    config_run_file.setAttr(platformStr, "serial_port", serialStr)
                    config_run_file.setAttr(platformStr, "device_type", deviceStr)
                elif platformStr not in platform_in_config:
                    platformAttrDic = {"debug_port":debugStr, "device_type":deviceStr,"serial_port":serialStr}
                    config_run_file.addChildAttr("device", platformStr, "yes", platformAttrDic)
                else:
                    pass
            
            for num in range(0,platform_in_len):
                if platform_in_config[num] not in platform_set:
                    config_run_file.setValue(platform_in_config[num], "no")
                else:
                    pass
        else:
            pass
                        
    
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    runTestWin = runStationConfig()
    runTestWin.show()
    sys.exit(app.exec_())
        