from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys,os,shutil
import buildConfigUi

file_path = os.path.dirname(os.path.abspath(__file__))
main_path = os.path.join(file_path,'../')
config_path = main_path + '/config/'
lib_path = main_path + '/lib/'

sys.path.append(config_path)
sys.path.append(lib_path)

from getconfig import Getconfig

config_file_backup = file_path + '/config.xml'
config_file =file_path + '/config_operate.xml'
shutil.copyfile(config_file_backup,config_file)


class buildStationConfig(QFrame,QMainWindow):
    def __init__(self, parent = None):
        super(buildStationConfig,self).__init__(parent)
        self.buildConfigWin = buildConfigUi.Ui_buildConfig()
        self.buildConfigWin.setupUi(self)
        self.connect(self.buildConfigWin.buildType_ComboBox, SIGNAL("currentIndexChanged(int)"),self.tokenFill)
        
    def tokenFill(self):
        if self.buildConfigWin.buildType_ComboBox.currentText() == "Public":
            self.buildConfigWin.buildToken_lineEdit.setReadOnly
            print "help"
        elif self.buildConfigWin.buildType_ComboBox.currentText() == "Private":
            self.buildConfigWin.buildToken_lineEdit.setText("")
    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    buildTestWin = buildStationConfig()
    buildTestWin.show()
    sys.exit(app.exec_())