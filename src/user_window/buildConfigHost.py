from PyQt4 import QtGui,QtCore 
import sys,os

file_path = os.path.dirname(os.path.abspath(__file__))
main_path = os.path.join(file_path,'../')
designer_path = main_path + '/designer_window/'
buildStation_path = main_path + '/Build_station/'
config_path = buildStation_path + '/config/'
lib_path = buildStation_path + '/lib/'
pic_path = main_path + '/pic/'

sys.path.append(lib_path)
sys.path.append(designer_path)
sys.path.append(config_path)
sys.path.append(buildStation_path)

from getconfig import Getconfig
from buildConfigUi import Ui_buildConfig
from get_local_config import Get_IDE_info, Get_DP_info
import platform_list
import win32api

config_file_build = config_path + 'config.xml'
config_build_file = Getconfig(config_file_build)

class buildStationConfig(QtGui.QMainWindow):
    def __init__(self, parent = None):
        QtGui.QWidget.__init__(self,parent)
        self.buildConfigWin = Ui_buildConfig()
        self.buildConfigWin.setupUi(self)
        self.setFixedSize(self.width(),self.height())
        
        self.testsuite_select =  platform_list.test_suite
        self.testsuite_existed_seq = []
        self.testsuite_existed_name = []

#*********** MenuBar, ToolBar, StatusBar ************         
        self.menuBar = self.menuBar()
        self.toolBar = self.addToolBar("ToolBar")
        self.statuBar = self.statusBar()
        
#********************* Actions **********************        
        self.saveAct = QtGui.QAction(QtGui.QIcon(pic_path + "/save.png"),"Save",self)
        self.saveAct.setShortcut("Ctrl+S")
        self.saveAct.setStatusTip("Save the Configuration File !")
        self.saveAct.whatsThis()
        self.connect(self.saveAct, QtCore.SIGNAL("triggered()"),self.saveBuild)
        self.connect(self.saveAct, QtCore.SIGNAL("triggered()"),self.saveEvent)
        
        self.quitAct = QtGui.QAction(QtGui.QIcon(pic_path + "/quit.png"),"Quit",self)
        self.quitAct.setShortcut("Ctrl+Q")
        self.quitAct.setStatusTip("Quit the Configuration without saving the File !")
        self.quitAct.whatsThis()
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
        
        self.tokenFlag = True
        self.ide_info = Get_IDE_info()
        self.dapeng_info = Get_DP_info()

        
        self.getPreConfig()
        self.addOrRemoveTestsuite()
        
        self.selectIarAndUv4()
        self.connect(self.buildConfigWin.iarComboBox, QtCore.SIGNAL("activated(int)"),self.addIar)
        self.connect(self.buildConfigWin.uv4ComboBox, QtCore.SIGNAL("activated(int)"),self.addUv4)
        
        self.connect(self.buildConfigWin.gccOpenButton, QtCore.SIGNAL("clicked()"),self.openGcc)
        self.connect(self.buildConfigWin.kdsOpenButton, QtCore.SIGNAL("clicked()"),self.openKds)
        self.connect(self.buildConfigWin.cw10OpenButton, QtCore.SIGNAL("clicked()"),self.openCw)
        self.connect(self.buildConfigWin.mingwOpenButton, QtCore.SIGNAL("clicked()"),self.openMingw)
        
        
#***************some event with messagebox********        
    def closeEvent(self,event):
        reply = QtGui.QMessageBox.warning(self, 'Warning', \
                                           'Are you sure to Quit ? Please make sure your Configurations had been Saved !',\
                                            QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
        if reply == QtGui.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
    
    def saveEvent(self):
        if self.tokenFlag == True:
            QtGui.QMessageBox.information(self,"Information",\
                                            "The Configuration File has been Saved Successfully !", QtGui.QMessageBox.Ok)
        elif self.tokenFlag == False:
            pass
    
    def whatEvent(self):
        QtGui.QMessageBox.information(self,"What is this",\
                                          "This is a GUI to configurate the environment of your Build Stations !",\
                                           QtGui.QMessageBox.Ok)
    
    def howEvent(self):
        QtGui.QMessageBox.information(self,"How to use",\
                                          "Configurate your Build Station to be private or not, give a token if private !" + 
                                          "  Then give the right path or version of each IDE that you need !" + 
                                          " Don't forget to Save the configuration !",\
                                           QtGui.QMessageBox.Ok)
        
#**********private station without set token, show the warning
    
    def tokenWarning(self):
        QtGui.QMessageBox.warning(self, "Warning","Set a token please !", QtGui.QMessageBox.Ok)
                                    
#*********get ide configuration that before********
    def getPreConfig(self):
        iarPre = config_build_file.getValue("iar")
        uv4Pre = config_build_file.getValue("uv4")
        kdsPre = config_build_file.getValue("kds")
        gccPre = config_build_file.getValue("gcc_arm")
        cwPre = config_build_file.getValue("cw10")
        mingwPre = config_build_file.getValue("mingw")
        oobePre = config_build_file.getAttr("FreeMV", "enable")
        ksdkoobePre = config_build_file.getAttr("FreeMV_ksdk", "enable")
        ksvPre = config_build_file.getAttr("FreeKV", "enable")
        demoPre = config_build_file.getAttr("FreeKV_demo", "enable")
        usbPre = config_build_file.getAttr("FreeKV_usb", "enable")
        unittestPre = config_build_file.getAttr("FreeKV_unit_test", "enable")
        tokenPre = config_build_file.getValue("token")
        privatePre = config_build_file.getAttr("token","private")
                
        if iarPre == None:
            self.buildConfigWin.iarLineEdit.setText("")
        else:
            self.buildConfigWin.iarLineEdit.setText(iarPre)
            
        if uv4Pre == None:
            self.buildConfigWin.uv4LineEdit.setText("")
        else:
            self.buildConfigWin.uv4LineEdit.setText(uv4Pre)
            
        if kdsPre == None:
            self.buildConfigWin.kdsLineEdit.setText("")
        else:
            self.buildConfigWin.kdsLineEdit.setText(kdsPre)
        
        if gccPre == None:
            self.buildConfigWin.gccLineEdit.setText("")
        else:
            self.buildConfigWin.gccLineEdit.setText(gccPre)
        
        if cwPre == None:
            self.buildConfigWin.cw10LineEdit.setText("")
        else:
            self.buildConfigWin.cw10LineEdit.setText(cwPre)
        
        if mingwPre == None:
            self.buildConfigWin.mingwLlineEdit.setText("")
        else:
            self.buildConfigWin.mingwLlineEdit.setText(mingwPre)
        
        if privatePre == "yes":
            self.buildConfigWin.tokenLineEdit.setText(tokenPre)
            self.buildConfigWin.privateCheckBox.setCheckState(QtCore.Qt.Checked)
        else:
            pass

                        
        if oobePre == "yes":
            self.testsuite_existed_name.append(self.testsuite_select[0])
            self.testsuite_existed_seq.append(0)
            oobeTestsuite = QtGui.QTreeWidgetItem(self.buildConfigWin.testsuiteTreeWidget)
            editableFlag = oobeTestsuite.flags() 
            oobeTestsuite.setFlags(editableFlag | QtCore.Qt.ItemIsEditable)
            oobeTestsuite.setText(0,self.testsuite_select[0])
        else:
            pass
        
        if ksdkoobePre == "yes":
            self.testsuite_existed_name.append(self.testsuite_select[1])
            self.testsuite_existed_seq.append(1)
            kskdoobeTestsuite = QtGui.QTreeWidgetItem(self.buildConfigWin.testsuiteTreeWidget)
            editableFlag = kskdoobeTestsuite.flags() 
            kskdoobeTestsuite.setFlags(editableFlag | QtCore.Qt.ItemIsEditable)
            kskdoobeTestsuite.setText(0,self.testsuite_select[1])
        else:
            pass
        
        if ksvPre == "yes":
            self.testsuite_existed_name.append(self.testsuite_select[2])
            self.testsuite_existed_seq.append(2)
            ksvTestsuite = QtGui.QTreeWidgetItem(self.buildConfigWin.testsuiteTreeWidget)
            editableFlag = ksvTestsuite.flags() 
            ksvTestsuite.setFlags(editableFlag | QtCore.Qt.ItemIsEditable)
            ksvTestsuite.setText(0,self.testsuite_select[2])
        else:
            pass
        
        if demoPre == "yes":
            self.testsuite_existed_name.append(self.testsuite_select[3])
            self.testsuite_existed_seq.append(3)
            demoTestsuite = QtGui.QTreeWidgetItem(self.buildConfigWin.testsuiteTreeWidget)
            editableFlag = demoTestsuite.flags() 
            demoTestsuite.setFlags(editableFlag | QtCore.Qt.ItemIsEditable)
            demoTestsuite.setText(0,self.testsuite_select[3])
        else:
            pass
        
        if usbPre == "yes":
            self.testsuite_existed_name.append(self.testsuite_select[4])
            self.testsuite_existed_seq.append(4)
            usbTestsuite = QtGui.QTreeWidgetItem(self.buildConfigWin.testsuiteTreeWidget)
            editableFlag = usbTestsuite.flags() 
            usbTestsuite.setFlags(editableFlag | QtCore.Qt.ItemIsEditable)
            usbTestsuite.setText(0,self.testsuite_select[4])
        else:
            pass
        
        if unittestPre == "yes":
            self.testsuite_existed_name.append(self.testsuite_select[5])
            self.testsuite_existed_seq.append(5)
            unittestTestsuite = QtGui.QTreeWidgetItem(self.buildConfigWin.testsuiteTreeWidget)
            editableFlag = unittestTestsuite.flags() 
            unittestTestsuite.setFlags(editableFlag | QtCore.Qt.ItemIsEditable)
            unittestTestsuite.setText(0,self.testsuite_select[5])
        else:
            pass
            


#***********************get dir of iar and uv4**************
    def selectIarAndUv4(self):
        iarList = self.ide_info['iar']
        iarNum = len(iarList)
        for num in range(0,iarNum):
            self.buildConfigWin.iarComboBox.addItem("")
            self.buildConfigWin.iarComboBox.setItemText(num, iarList[num]['version'])
        
        uv4List = self.ide_info['keil']
        uv4Num = len(uv4List)
        for num in range(0,uv4Num):
            self.buildConfigWin.uv4ComboBox.addItem("")
            self.buildConfigWin.uv4ComboBox.setItemText(num, uv4List[num]['version'])
        
#****************************add iar**********************
    def addIar(self):
        iarList = self.ide_info['iar']
        iarIndex = self.buildConfigWin.iarComboBox.currentIndex()
        self.buildConfigWin.iarLineEdit.setText(iarList[iarIndex]['path'])
        
#***************************add uv4***********************
    def addUv4(self):
        uv4List = self.ide_info['keil']
        uv4Index = self.buildConfigWin.uv4ComboBox.currentIndex()
        self.buildConfigWin.uv4LineEdit.setText(uv4List[uv4Index]['path'])
        
        
    
#***************open directory of gcc kds cw mingw**********        
    def openGcc(self): 
        gccDir = QtGui.QFileDialog.getExistingDirectory(self, QtCore.QString(),\
                                                          "C:/",QtGui.QFileDialog.ShowDirsOnly | QtGui.QFileDialog.DontResolveSymlinks)
        self.buildConfigWin.gccLineEdit.setText(gccDir)
        
    def openKds(self): 
        kdsDir = QtGui.QFileDialog.getExistingDirectory(self, QtCore.QString(),\
                                                          "C:/",QtGui.QFileDialog.ShowDirsOnly | QtGui.QFileDialog.DontResolveSymlinks)
        self.buildConfigWin.kdsLineEdit.setText(kdsDir)
        
    def openCw(self): 
        cwDir = QtGui.QFileDialog.getExistingDirectory(self, QtCore.QString(),\
                                                          "C:/",QtGui.QFileDialog.ShowDirsOnly | QtGui.QFileDialog.DontResolveSymlinks)
        self.buildConfigWin.cw10LineEdit.setText(cwDir)
        
    def openMingw(self): 
        mingwDir = QtGui.QFileDialog.getExistingDirectory(self, QtCore.QString(),\
                                                          "C:/",QtGui.QFileDialog.ShowDirsOnly | QtGui.QFileDialog.DontResolveSymlinks)
        self.buildConfigWin.mingwLlineEdit.setText(mingwDir)
        


    def addOrRemoveTestsuite(self):
        length = len(self.testsuite_select)
        
        for num in range(0,length):
            self.buildConfigWin.testSuiteComboBox.addItem("")
            self.buildConfigWin.testSuiteComboBox.setItemText(num,self.testsuite_select[num])
        self.connect(self.buildConfigWin.testSuiteComboBox,QtCore.SIGNAL("activated(int)"),self.testsuiteFill)
        self.connect(self.buildConfigWin.testsuiteTreeWidget, QtCore.SIGNAL("itemActivated(QTreeWidgetItem*,int)"),self.testsuiteGetCurrentItem)
        self.connect(self.buildConfigWin.testSuiteRemoveButton,QtCore.SIGNAL("clicked()"),self.testsuitePlatformRemove)
        self.connect(self.buildConfigWin.testSuiteAddButton, QtCore.SIGNAL("clicked()"),self.testsuiteAdd)
        
    def testsuiteFill(self):
        seq = self.buildConfigWin.testSuiteComboBox.currentIndex()
        if (self.buildConfigWin.testSuiteComboBox.itemText(seq) == self.testsuite_select[seq]) and seq not in self.testsuite_existed_seq:
            self.testsuite_existed_seq.append(seq)
            self.testsuite_existed_name.append(self.testsuite_select[seq])
            self.Testsuite = QtGui.QTreeWidgetItem(self.buildConfigWin.testsuiteTreeWidget)
            editableFlag = self.Testsuite.flags() 
            self.Testsuite.setFlags(editableFlag | QtCore.Qt.ItemIsEditable)
            self.Testsuite.setText(0,self.testsuite_select[seq])
            
    def testsuiteGetCurrentItem(self):
        self.currentItem = self.buildConfigWin.testsuiteTreeWidget.currentItem()
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
            self.buildConfigWin.testsuiteTreeWidget.takeTopLevelItem(self.buildConfigWin.testsuiteTreeWidget.indexOfTopLevelItem(self.currentItemGot))
            self.testsuite_existed_name.remove(self.testsuiteName)
            self.testsuite_existed_seq.remove(self.testsuite_select.index(self.testsuiteName))
            
    def testsuiteAdd(self):
        flag = True
        length = len(self.testsuite_select)
        if self.dapeng_info["exist"] == "no":
            pass
        else:
            freemv_build_path_long = self.dapeng_info['path'] + '/freemvbuild'
            freekv_build_path_long = self.dapeng_info['path'] + '/freekvbuild'
            freekv_demo_build_path_long = self.dapeng_info['path'] + '/freekv_demobuild'
            freemv_build_path = win32api.GetShortPathName(freemv_build_path_long)
            freekv_build_path = win32api.GetShortPathName(freekv_build_path_long)
            freekv_demo_build_path = win32api.GetShortPathName(freekv_demo_build_path_long)
        
        for num in range(0,length):
            try:
                testsuiteIn = self.buildConfigWin.testsuiteTreeWidget.topLevelItem(num).text(0)
                if testsuiteIn == "KSDK-DEMO":
                    config_build_file.setAttr("FreeKV_demo", "enable", "yes")
                    config_build_file.setValue("FreeKV_demo", freekv_demo_build_path)
                    break
                else:
                    config_build_file.setAttr("FreeKV_demo", "enable", "no")                   
            except Exception:
                pass
            
        for num in range(0,length):
            try:
                testsuiteIn = self.buildConfigWin.testsuiteTreeWidget.topLevelItem(num).text(0)
                if testsuiteIn == "KSDK-USB":
                    config_build_file.setAttr("FreeKV_usb", "enable", "yes")
                    config_build_file.setValue("FreeKV_usb", freekv_demo_build_path)
                    break
                else:
                    config_build_file.setAttr("FreeKV_usb", "enable", "no")                   
            except Exception:
                pass

        for num in range(0,length):
            try:
                testsuiteIn = self.buildConfigWin.testsuiteTreeWidget.topLevelItem(num).text(0)
                if testsuiteIn == "KSDK-UnitTest":
                    config_build_file.setAttr("FreeKV_unit_test", "enable", "yes")
                    config_build_file.setValue("FreeKV_unit_test", freekv_demo_build_path)
                    break
                else:
                    config_build_file.setAttr("FreeKV_unit_test", "enable", "no")                   
            except Exception:
                pass
            
        for num in range(0,length):
            try:
                testsuiteIn = self.buildConfigWin.testsuiteTreeWidget.topLevelItem(num).text(0)
                if testsuiteIn == "MQX-OOBE":
                    config_build_file.setAttr("FreeMV", "enable", "yes")
                    config_build_file.setValue("FreeMV", freemv_build_path)
                    break
                else:
                    config_build_file.setAttr("FreeMV", "enable", "no")                   
            except Exception:
                pass               

        for num in range(0,length):
            try:
                testsuiteIn = self.buildConfigWin.testsuiteTreeWidget.topLevelItem(num).text(0)
                if testsuiteIn == "KSDK-MQX-OOBE":
                    config_build_file.setAttr("FreeMV_ksdk", "enable", "yes")
                    config_build_file.setValue("FreeMV_ksdk", freemv_build_path)
                    break
                else:
                    config_build_file.setAttr("FreeMV_ksdk", "enable", "no")                   
            except Exception:
                pass    

        for num in range(0,length):
            try:
                testsuiteIn = self.buildConfigWin.testsuiteTreeWidget.topLevelItem(num).text(0)
                if testsuiteIn == "KSV":
                    config_build_file.setAttr("FreeKV", "enable", "yes")
                    config_build_file.setValue("FreeKV", freekv_build_path)
                    break
                else:
                    config_build_file.setAttr("FreeKV", "enable", "no")                   
            except Exception:
                pass 

        if self.buildConfigWin.testsuiteTreeWidget.topLevelItem(0) == None and flag == True:
            flag = False
            QtGui.QMessageBox.information(self,"Warning","You have not select any Test Suite, please select at least one !",QtGui.QMessageBox.Ok)
        else:
            pass    

        if flag == True:
            QtGui.QMessageBox.information(self,"Information","Add the Test Suites successful !",QtGui.QMessageBox.Ok)           



#****************save configurations of build station***********    
    def saveBuild(self):

#**********************config ides***************************
        iarSet = self.buildConfigWin.iarLineEdit.text()
        if  iarSet.__str__() == "":
            config_build_file.setAttr("IDE", "iar", "no")
            config_build_file.setValue("iar", "")
        else:
            iarShort = win32api.GetShortPathName(iarSet.__str__())
            config_build_file.setAttr("IDE", "iar", "yes")
            config_build_file.setValue("iar", iarShort)

        
        uv4Set = self.buildConfigWin.uv4LineEdit.text()
        if uv4Set.__str__() == "":
            config_build_file.setAttr("IDE", "uv4", "no")
            config_build_file.setValue("uv4", "")
        else:
            uv4Short = win32api.GetShortPathName(uv4Set.__str__())
            config_build_file.setAttr("IDE", "uv4", "yes")
            config_build_file.setValue("uv4", uv4Short)

        
        kdsSet = self.buildConfigWin.kdsLineEdit.text()
        if kdsSet.__str__() == "":
            config_build_file.setAttr("IDE", "kds", "no")
            config_build_file.setValue("kds", "")
        else:
            kdsShort = win32api.GetShortPathName(kdsSet.__str__())
            config_build_file.setAttr("IDE", "kds", "yes")
            config_build_file.setValue("kds", kdsShort)

        
        gccSet = self.buildConfigWin.gccLineEdit.text()
        if gccSet.__str__() == "":
            config_build_file.setAttr("IDE", "gcc_arm", "no")
            config_build_file.setValue("gcc_arm", "")
        else:
            gccShort = win32api.GetShortPathName(gccSet.__str__())
            config_build_file.setAttr("IDE", "gcc_arm", "yes")
            config_build_file.setValue("gcc_arm", gccShort)
        
        
        cwSet = self.buildConfigWin.cw10LineEdit.text()
        if cwSet.__str__() == "":
            config_build_file.setAttr("IDE", "cw10", "no")
            config_build_file.setAttr("IDE", "cw10gcc", "no")
            config_build_file.setValue("cw10", "")
            config_build_file.setValue("cw10gcc", "")
        else:
            cwShort = win32api.GetShortPathName(cwSet.__str__())
            config_build_file.setAttr("IDE", "cw10", "yes")
            config_build_file.setAttr("IDE", "cw10gcc", "yes")
            config_build_file.setValue("cw10", cwShort)
            config_build_file.setValue("cw10gcc", cwShort)

        
        mingwSet = self.buildConfigWin.mingwLlineEdit.text()
        if mingwSet.__str__() == "":
            config_build_file.setValue("mingw", "")
        else:
            mingwShort = win32api.GetShortPathName(mingwSet.__str__())
            config_build_file.setValue("mingw", mingwShort)
          

#**********************config private and token*******************        
        tokenSet = self.buildConfigWin.tokenLineEdit.text()        
        if self.buildConfigWin.privateCheckBox.checkState() == QtCore.Qt.Checked and tokenSet != "":
            self.tokenFlag = True
            config_build_file.setAttr("token", "private", "yes")
            config_build_file.setValue("token", tokenSet.__str__())
        elif self.buildConfigWin.privateCheckBox.checkState() == QtCore.Qt.Checked and tokenSet == "":
            self.tokenFlag = False
            self.tokenWarning()     
        else:
            self.tokenFlag = True
            config_build_file.setAttr("token", "private", "no")
            
        

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    buildTestWin = buildStationConfig()
    buildTestWin.show()
    sys.exit(app.exec_())