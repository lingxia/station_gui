from PyQt4.QtGui import *
from PyQt4.QtCore import *
import pulldownhost, buildhost
import dapenghost, checkhost
import sys
import qqdpui
import getconfig

class qqdpmain(QToolBox):
    
    def __init__(self, parent = None):
        super(qqdpmain,self).__init__(parent)
        self.qqdpwin = qqdpui.Ui_QToolBox()
        self.qqdpwin.setupUi(self)
        self.pulldown = pulldownhost.pullframe()
        self.dapeng = dapenghost.dapeng()
        self.build = buildhost.buildframe()
        self.check = checkhost.check()
        
        self.connect(self.qqdpwin.pullButton,SIGNAL("clicked()"),self.pulldown.shownpull)
        self.connect(self.qqdpwin.dapengButton,SIGNAL("clicked()"),self.dapeng.showndapeng)
        self.connect(self.qqdpwin.buildButton,SIGNAL("clicked()"),self.build.shownbuild)
        self.connect(self.qqdpwin.checkButton,SIGNAL("clicked()"),self.check.checkshown)
        self.connect(self.qqdpwin.checkButton,SIGNAL("clicked()"),self.check.loadimage)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    dpwin = qqdpmain()
    dpwin.show()
    sys.exit(app.exec_())