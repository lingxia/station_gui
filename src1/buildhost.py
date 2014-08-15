from PyQt4.QtGui import *
from PyQt4.QtCore import *
from  getconfig import Getconfig
import build, checkhost
import sys

confile = Getconfig("config.xml")

class buildframe(QMainWindow):
    
    def __init__(self, parent = None):
        super(buildframe, self).__init__(parent)
        self.buildwin = build.Ui_build()
        self.buildwin.setupUi(self)
        self.checkwin = checkhost.check()
        
        self.connect(self.buildwin.buildcheckBox,SIGNAL("stateChanged(int)"),self.getValue)
        self.connect(self.buildwin.runcheckBox,SIGNAL("stateChanged(int)"),self.getValue)
        self.connect(self.buildwin.buildandruncheckBox,SIGNAL("stateChanged(int)"),self.getValue)
        self.connect(self.buildwin.saveButton,SIGNAL("clicked()"),self.close)
#        self.connect(self.buildwin.saveButton,SIGNAL("clicked()"),self.checkwin.checkshown)
#        self.connect(self.buildwin.saveButton,SIGNAL("clicked()"),self.checkwin.loadimage)       
        
    def getValue(self):
        if self.buildwin.buildcheckBox.checkState() == Qt.Checked:
            confile.setValue('build','yes')
        else:
            confile.setValue('build','no')
        if self.buildwin.runcheckBox.checkState() == Qt.Checked:
            confile.setValue('run','yes')
        else:
            confile.setValue('run','no')
        if self.buildwin.buildandruncheckBox.checkState() == Qt.Checked:
            confile.setValue('build_and_run','yes')
        else:
            confile.setValue('build_and_run','no')
            
    def shownbuild(self):
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    buildwin = buildframe()
    buildwin.show()
    sys.exit(app.exec_())