from PyQt4 import QtGui,QtCore
from buildQuitTipsUi import Ui_buildQuitTips
import os, sys

class buildQuit(QtGui.QMainWindow):
    def __init__(self, parent = None):
        QtGui.QWidget.__init__(self,parent)
        self.buildQuitWin = Ui_buildQuitTips()
        self.buildQuitWin.setupUi(self)
        self.statuBar = self.statusBar()
        self.setFixedSize(self.width(),self.height())
        
        self.connect(self.buildQuitWin.quitNoButton, QtCore.SIGNAL("clicked()"),self.close)
        self.connect(self.buildQuitWin.quitYesButton, QtCore.SIGNAL("clicked()"),self.close)
        
    def buildQuitTipsShow(self):
        self.show()
        
        
        
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    buildQuitTest = buildQuit()
    buildQuitTest.show()
    sys.exit(app.exec_())
    