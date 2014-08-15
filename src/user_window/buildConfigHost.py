from PyQt4 import QtGui,QtCore 
import sys,os,shutil

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

config_file_backup = config_path + 'config.xml'
config_file = config_path + 'config_operate.xml'
shutil.copyfile(config_file_backup,config_file)


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
        self.whatMessage.setText("This is a GUI to configurate the environment of your Build Stations !")
        
        
        self.howMessage = QtGui.QMessageBox()
        self.howMessage.setWindowTitle("How to Use")
        self.howMessage.setIcon(self.howMessage.Information)
        self.howMessage.setText("Configurate your Build Station to be private or not, give a token if private!"
                                + "  Then give the right path or version of each IDE that you need!"
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
        self.quitAct.whatsThis()
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


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    buildTestWin = buildStationConfig()
    buildTestWin.show()
    sys.exit(app.exec_())