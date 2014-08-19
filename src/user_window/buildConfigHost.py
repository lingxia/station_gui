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

config_file_build = config_path + 'config.xml'

from getconfig import Getconfig
from buildConfigUi import Ui_buildConfig

config_build_file = Getconfig(config_file_build)

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
        self.quitMessage.setText("Are you sure to Quit ? Please make sure your Configurations had been Saved !")
        self.quitMessage.Yes = self.quitMessage.addButton("Yes", QtGui.QMessageBox.ActionRole)
        self.quitMessage.No = self.quitMessage.addButton("No", QtGui.QMessageBox.ActionRole)
        self.connect(self.quitMessage.Yes, QtCore.SIGNAL("clicked()"),self.close)
        
        self.saveMessage = QtGui.QMessageBox()
        self.saveMessage.setWindowTitle("Information")
        self.saveMessage.setIcon(self.quitMessage.Information)
        self.saveMessage.setText("The Configuration File has been Saved Successfully !") 
                        
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
        self.saveAct.setStatusTip("Save the Configuration File !")
        self.saveAct.whatsThis()
        self.connect(self.saveAct, QtCore.SIGNAL("triggered()"),self.saveMessage.exec_)
        
        self.quitAct = QtGui.QAction(QtGui.QIcon(pic_path + "/quit.png"),"Quit",self)
        self.quitAct.setShortcut("Ctrl+Q")
        self.quitAct.setStatusTip("Quit the Configuration without saving the File !")
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
        
        self.getPreConfig()
        
        self.connect(self.buildConfigWin.gccOpenButton, QtCore.SIGNAL("clicked()"),self.openGcc)
        self.connect(self.buildConfigWin.kdsOpenButton, QtCore.SIGNAL("clicked()"),self.openKds)
        self.connect(self.buildConfigWin.cw10OpenButton, QtCore.SIGNAL("clicked()"),self.openCw)
        self.connect(self.buildConfigWin.mingwOpenButton, QtCore.SIGNAL("clicked()"),self.openMingw)
                             
#*********get ide configuration that before********
    def getPreConfig(self):
        iarPre = config_build_file.getValue("iar")
        uv4Pre = config_build_file.getValue("uv4")
        kdsPre = config_build_file.getValue("kds")
        gccPre = config_build_file.getValue("gcc_arm")
        cwPre = config_build_file.getValue("cw10")
        mingwPre = config_build_file.getValue("mingw")
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
        
        tokenPre = config_build_file.getValue("token")
        privatePre = config_build_file.getAttr("token","private")
        
        if privatePre == "yes":
            self.buildConfigWin.tokenLineEdit.setText(tokenPre)
            self.buildConfigWin.privateCheckBox.setCheckState(QtCore.Qt.Checked)
        elif privatePre == "no":
            return
        
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




if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    buildTestWin = buildStationConfig()
    buildTestWin.show()
    sys.exit(app.exec_())