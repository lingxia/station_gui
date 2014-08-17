from PyQt4 import QtGui,QtCore 
import sys,os,shutil

file_path = os.path.dirname(os.path.abspath(__file__))
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

class runStationConfig(QtGui.QMainWindow):
    def __init__(self,parent = None):         
        QtGui.QWidget.__init__(self,parent)
        self.runConfigWin = Ui_runConfig()
        self.runConfigWin.setupUi(self)
        self.setFixedSize(self.width(), self.height())
        self.bars()
        self.debuggerSelect()

#*********** MenuBar, ToolBar, StatusBar ************
    def bars(self):         
        self.menuBar = self.menuBar()
        self.toolBar = self.addToolBar("ToolBar")
        self.statuBar = self.statusBar()
        self.actions()
        self.addActions()

#**********************MessageBox********************
    def messageBox(self):       
        self.quitMessage = QtGui.QMessageBox()
        self.quitMessage.setWindowTitle("Warning")
        self.quitMessage.setIcon(self.quitMessage.Warning)
        self.quitMessage.setText("The Configuration File has not been Saved ! Are you sure to Quit ?")
        self.quitMessage.setStandardButtons(self.quitMessage.Yes | self.quitMessage.No)
        self.quitMessage.setDefaultButton(self.quitMessage.No)
        
        self.whatMessage = QtGui.QMessageBox()
        self.whatMessage.setWindowTitle("What's this")
        self.whatMessage.setIcon(self.whatMessage.Information)
        self.whatMessage.setText("This is a GUI to configurate the environment of your Run Stations !")
        
        self.howMessage = QtGui.QMessageBox()
        self.howMessage.setWindowTitle("How to Use")
        self.howMessage.setIcon(self.howMessage.Information)
        self.howMessage.setText("Configurate your Run Station to be private or not, give a token if private !"
                                + "  Then give the right path of each Debugger that you need and add the Platforms you need !"
                                + " Don't forget to Save the configuration !")

#********************* Actions ********************** 
    def actions(self):
        self.messageBox()      
        self.saveAct = QtGui.QAction(QtGui.QIcon(pic_path + "/save.png"),"Save",self)
        self.saveAct.setShortcut("Ctrl+S")
        self.saveAct.setStatusTip("Save the Configuration File and Quit the Configuration")
        self.saveAct.whatsThis()
        self.connect(self.saveAct, QtCore.SIGNAL("triggered()"),self.close)
        
        self.quitAct = QtGui.QAction(QtGui.QIcon(pic_path + "/quit.png"),"Quit",self)
        self.quitAct.setShortcut("Ctrl+Q")
        self.quitAct.setStatusTip("Quit the Configuration without saving the File")
        self.saveAct.whatsThis()
        self.connect(self.quitAct, QtCore.SIGNAL("triggered()"),self.quitMessage.exec_)
        
        self.whatAct = QtGui.QAction(QtGui.QIcon(pic_path + "/what.png"),"What's this?",self)
        self.whatAct.setShortcut("Ctrl+W")
        self.whatAct.setStatusTip("Brief Introdution of this GUI")
        self.whatAct.whatsThis()
        self.connect(self.whatAct, QtCore.SIGNAL("triggered()"),self.whatMessage.exec_)
        
        self.howAct = QtGui.QAction(QtGui.QIcon(pic_path + "/use.png"),"How to use?",self)
        self.howAct.setShortcut("Ctrl+U")
        self.howAct.setStatusTip("Brief Usage of this GUI")
        self.howAct.whatsThis()
        self.connect(self.howAct, QtCore.SIGNAL("triggered()"),self.howMessage.exec_)
        
        
#****************add Menus and Actions**************
    def addActions(self):
        self.fileMenu = self.menuBar.addMenu("File")
        self.fileMenu.addAction(self.saveAct)
        self.fileMenu.addAction(self.quitAct)
        
        self.helpMenu = self.menuBar.addMenu("Help")
        self.helpMenu.addAction(self.whatAct)
        self.helpMenu.addAction(self.howAct)
        
        self.toolBar.addAction(self.saveAct)
        self.toolBar.addAction(self.quitAct)
        
        
#***************add Platform and Device_Type********
    def addPlaforms(self):
        self.device = platform_list.device_type
        self.platform = platform_list.platform_list
        self.platform_existed = []
        length = len(self.platform)
        
#        for num in range(0,length):
#            self.runConfigWin.platformComboBox.addItem("")
#            self.runConfigWin.platformComboBox.setItemText(num,self.platform[num])
#        
#        self.connect(self.runConfigWin.platformComboBox, QtCore.SIGNAL("activated(int)"),self.platform_fill)
# 
#            
#    def platform_fill(self):
#        seq = self.runConfigWin.platformComboBox.currentIndex()
#        if (self.runConfigWin.platformComboBox.itemText(seq) == self.platform[seq]) and seq not in self.platform_existed:
#            self.platform_existed.append(seq)
#            self.currentPlatformItem = self.runConfigWin.platformListWidget.insertItem(0, self.platform[seq])
#            print self.currentPlatformItem
#            self.currentDeviceItem = self.runConfigWin.deviceListWidget.insertItem(0, self.device[seq])
#            print self.currentDeviceItem


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
        


        
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    runTestWin = runStationConfig()
    runTestWin.show()
    sys.exit(app.exec_())
        
        