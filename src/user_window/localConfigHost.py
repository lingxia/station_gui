from PyQt4 import QtGui,QtCore 
import sys,os
import threading, time

file_path = os.path.dirname(os.path.abspath("__file__"))
main_path = os.path.join(file_path,'../')
designer_path = main_path + '/designer_window/'
pic_path = main_path + '/pic/'
config_path_build = main_path + '/Build_station' + '/config/'
config_path_run = main_path + '/Run_station' + '/config/'    
lib_path = main_path + '/Build_station' + '/lib/'
script_path = main_path + '/Build_station' + '/script/'

sys.path.append(designer_path)
sys.path.append(config_path_build)
sys.path.append(config_path_run)
sys.path.append(lib_path)
sys.path.append(script_path)

config_file_build = config_path_build + 'config.xml'
config_file_run = config_path_run + 'config.xml'

from localConfigUi import Ui_localConfig
from get_local_config import GetPCconfig, Get_STAF_info
from getconfig import Getconfig
from common import reset_staf

config_build_file = Getconfig(config_file_build)
config_run_file = Getconfig(config_file_run)


class localEnvConfig(QtGui.QMainWindow):
    def __init__(self, parent = None):
        QtGui.QWidget.__init__(self,parent)
        self.localConfigWin = Ui_localConfig()
        self.localConfigWin.setupUi(self)
        self.setFixedSize(self.width(),self.height())

#*********** MenuBar, ToolBar, StatusBar ************         
        self.menuBar = self.menuBar()
        self.toolBar = self.addToolBar("ToolBar")
        self.statuBar = self.statusBar()

#********************* Actions **********************        
        self.saveAct = QtGui.QAction(QtGui.QIcon(pic_path + "/save.png"),"Save",self)
        self.saveAct.setShortcut("Ctrl+S")
        self.saveAct.setStatusTip("Save the Configuration File !")
        self.saveAct.whatsThis()
        self.connect(self.saveAct, QtCore.SIGNAL("triggered()"),self.saveLocal)
        self.connect(self.saveAct, QtCore.SIGNAL("triggered()"),self.saveEvent)
        
        self.quitAct = QtGui.QAction(QtGui.QIcon(pic_path + "/quit.png"),"Quit",self)
        self.quitAct.setShortcut("Ctrl+Q")
        self.quitAct.setStatusTip("Quit the Configuration without saving the File")
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
        
#****************open staf dir************************
        self.connect(self.localConfigWin.stafOpenButton, QtCore.SIGNAL("clicked()"), self.openStaf)

#****************config the local environment*********
        self.configLocal()
        
#        self.processDialog = QtGui.QProgressDialog()
#        self.processDialog.setBar(QtGui.QProgressBar())
#        self.processDialog.setLabelText("ddddddd")
#        self.processDialog.setMaximum(100)
#        self.processDialog.setMinimum(0)
#        self.processDialog.setMinimumDuration(4)
#        self.processDialog.setMinimumDuration(10)
        
#        self.processbarThread = threading.Thread(name = 'worker',target = self.processBar)
#        self.stafThread = threading.Thread(name = 'staf',target = self.stafReset)
        


    def processBar(self):
        self.processDialog.show()

            
    def stafReset(self):
        reset_staf()
        
#***************some event with messagebox        
    def closeEvent(self,event):
        reply = QtGui.QMessageBox.warning(self, 'Warning', \
                                           'Are you sure to Quit ? Please make sure your Configurations had been Saved !',\
                                            QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
        if reply == QtGui.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
    
    def saveEvent(self):
        QtGui.QMessageBox.information(self,"Information",\
                                          "The Configuration File has been Saved Successfully !",\
                                           QtGui.QMessageBox.Ok)
    
    def whatEvent(self):
        QtGui.QMessageBox.information(self,"What is this",\
                                          "This is a GUI to configurate the Local Environment of your Stations !",\
                                           QtGui.QMessageBox.Ok)
    
    def howEvent(self):
        QtGui.QMessageBox.information(self,"How to use",\
                                          "All the environments will be set by the Station Automatically !" + 
                                          "  If not auto, please set them manually !" + 
                                          " Don't forget to Save the configuration !",\
                                           QtGui.QMessageBox.Ok)
        

        
        
#***************open dir of staf**********************        
    def openStaf(self):
        stafDir = QtGui.QFileDialog.getExistingDirectory(self, QtCore.QString(),\
                                                          "C:/",QtGui.QFileDialog.ShowDirsOnly | QtGui.QFileDialog.DontResolveSymlinks)
        self.localConfigWin.stafLineEdit.setText(stafDir) 
        
      
#****************configurate and save the local environment*********        
    def configLocal(self):
        pcConfig = GetPCconfig()
        staf = Get_STAF_info()
        try:
            ip = pcConfig['ip']
            mac = pcConfig['mac']
            host = pcConfig['hostname']
            stafPath = staf['path']
        except Exception:
            stafPath = None
            
        try:
            self.localConfigWin.ipLineEdit.setText(ip)
            self.localConfigWin.macLineEdit.setText(mac)
            self.localConfigWin.hostLineEdit.setText(host)
            self.localConfigWin.stafLineEdit.setText(stafPath)
        except Exception:
            return 
 
           
    def saveLocal(self):
#*****************save the configurate file*************
        ipSet = self.localConfigWin.ipLineEdit.text()
        config_build_file.setValue("local_ip", ipSet.__str__())
        config_run_file.setValue("local_ip", ipSet.__str__())
        
        macSet = self.localConfigWin.macLineEdit.text()
        config_build_file.setValue("local_mac", macSet.__str__())
        config_run_file.setValue("local_mac", macSet.__str__())
        
        hostSet = self.localConfigWin.hostLineEdit.text()
        config_build_file.setValue("machine_name", hostSet.__str__())
        config_run_file.setValue("machine_name", hostSet.__str__())
        
        stafSet = self.localConfigWin.stafLineEdit.text()
        config_build_file.setValue("STAF_dir", stafSet.__str__())
        config_run_file.setValue("STAF_dir", stafSet.__str__())
        
#*********************restart staf**********************       
        #self.stafThread.start()
#        self.processbarThread.start()
#        reset_staf()
           
        
    


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    localTestWin = localEnvConfig()
    localTestWin.show()
    sys.exit(app.exec_())