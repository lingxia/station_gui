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
config_file = file_path + '/config_operate.xml'
#shutil.copyfile(config_file_backup,config_file)


class buildStationConfig(QMainWindow):
    def __init__(self, parent = None):
        super(buildStationConfig,self).__init__(parent)
        self.buildConfigWin = buildConfigUi.Ui_buildConfig()
        self.buildConfigWin.menuBar = QMenuBar()
        self.fileBar = self.buildConfigWin.menuBar.addMenu("save")
        self.actionBar = self.buildConfigWin.menuBar.addAction("help")
        self.buildConfigWin.menuBar.show()
        self.buildConfigWin.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    buildTestWin = buildStationConfig()
    buildTestWin.show()
    sys.exit(app.exec_())