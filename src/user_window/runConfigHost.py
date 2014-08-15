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
        
#*********** MenuBar, ToolBar, StatusBar ************         
        self.menuBar = self.menuBar()
        self.toolBar = self.addToolBar("ToolBar")
        self.statuBar = self.statusBar()

#**********************MessageBox********************       
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
        self.fileMenu = self.menuBar.addMenu("File")
        self.fileMenu.addAction(self.saveAct)
        self.fileMenu.addAction(self.quitAct)
        
        self.helpMenu = self.menuBar.addMenu("Help")
        self.helpMenu.addAction(self.whatAct)
        self.helpMenu.addAction(self.howAct)
        
        self.toolBar.addAction(self.saveAct)
        self.toolBar.addAction(self.quitAct)
        
        
#***************add Platform and Type_device********
        self.device = platform_list.device_type
        self.platform = platform_list.platform_list
        global length
        length = len(self.platform)
        
        for num in range(0,length):
            self.runConfigWin.platformComboBox.addItem("")
            self.runConfigWin.platformComboBox.setItemText(num,self.platform[num])
        
        
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    runTestWin = runStationConfig()
    runTestWin.show()
    sys.exit(app.exec_())
        
        