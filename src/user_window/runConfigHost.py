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

#********************* Actions **********************        
        self.saveAct = QtGui.QAction(QtGui.QIcon(pic_path + "/save.png"),"&Save",self)
        self.saveAct.setShortcut("Ctrl+S")
        self.saveAct.setStatusTip("Save the Configuration File and Quit the Configuration")
        self.saveAct.whatsThis()
        self.connect(self.saveAct, QtCore.SIGNAL("triggered()"),self.close)
        
        self.quitAct = QtGui.QAction(QtGui.QIcon(pic_path + "/quit.png"),"Quit",self)
        self.quitAct.setShortcut("Ctrl+Q")
        self.quitAct.setStatusTip("Quit the Configuration without saving the File")
        self.saveAct.whatsThis()
        self.connect(self.quitAct, QtCore.SIGNAL("triggered()"),self.quitMessage.exec_)
        
        
#****************add Menus and Actions**************
        self.fileMenu = self.menuBar.addMenu("File")
        self.fileMenu.addAction(self.saveAct)
        self.fileMenu.addAction(self.quitAct)
        
        self.toolBar.addAction(self.saveAct)
        self.toolBar.addAction(self.quitAct)
        
        
        
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    runTestWin = runStationConfig()
    runTestWin.show()
    sys.exit(app.exec_())
        
        