from PyQt4 import QtGui,QtCore 
import sys,os,shutil
from buildConfigUi import Ui_buildConfig

file_path = os.path.dirname(os.path.abspath(__file__))
main_path = os.path.join(file_path,'../')
config_path = main_path + '/config/'
lib_path = main_path + '/lib/'

sys.path.append(config_path)
sys.path.append(lib_path)

from getconfig import Getconfig

config_file_backup = file_path + '/config.xml'
config_file = file_path + '/config_operate.xml'
#shutil.copyfile(config_file_backup,config_file)


class buildStationConfig(QtGui.QMainWindow):
    def __init__(self, parent = None):
        QtGui.QWidget.__init__(self,parent)
        self.buildConfigWin = Ui_buildConfig()
        self.buildConfigWin.setupUi(self)
        self.setFixedSize(self.width(),self.height())

#*********** MenuBar, ToolBar, StatusBar ************         
        self.menuBar = self.menuBar()
        self.toolBar = self.addToolBar("ToolBar")
        self.statuBar = self.statusBar()

#********************* Actions **********************        
        self.saveAct = QtGui.QAction(QtGui.QIcon("pics/save.png"),"&Save",self)
        self.saveAct.setShortcut("Ctrl+S")
        self.saveAct.setStatusTip("Save the Configuration File")
        self.saveAct.whatsThis()
        
        self.quitAct = QtGui.QAction(QtGui.QIcon("pics/quit.png"),"Quit",self)
        self.quitAct.setShortcut("Ctrl+Q")
        self.quitAct.setStatusTip("Quit the Configuration")
        self.saveAct.whatsThis()
        

#****************add Menus and Actions**************
        self.fileMenu = self.menuBar.addMenu("File")
        self.fileMenu.addAction(self.saveAct)
        self.fileMenu.addAction(self.quitAct)
        
        self.toolBar.addAction(self.saveAct)
        self.toolBar.addAction(self.quitAct)  
    

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    buildTestWin = buildStationConfig()
    buildTestWin.show()
    sys.exit(app.exec_())