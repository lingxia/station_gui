from PyQt4.QtGui import *
from PyQt4.QtCore import *
from  getconfig import Getconfig
import configui
import sys

confile = Getconfig('config.xml')

class configure(QMainWindow):
    
    def __init__(self,parent = None):
        super(configure, self).__init__(parent)
        self.configwin = configui.Ui_Form()
        self.configwin.setupUi(self)
        self.connect(self.configwin.okButton,SIGNAL("clicked()"),self.getValue)
        self.connect(self.configwin.okButton,SIGNAL("clicked()"),self.close)

    def getValue(self):
        plain = self.configwin.textEdit.toPlainText()
        confile.setValue('build', plain.__str__())
        
app = QApplication(sys.argv)
win = configure()
win.show()
sys.exit(app.exec_())        