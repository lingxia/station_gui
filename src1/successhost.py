from PyQt4.QtCore import *
from PyQt4.QtGui import *
import successui
import sys

class success(QMainWindow):
    
    def __init__(self, parent = None):
        super(success, self).__init__(parent)
        self.successwin = successui.Ui_logon_2()
        self.successwin.setupUi(self)
        
    def showsuc(self):
        self.show()
        
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    sucwin = success()
    sucwin.show()
    sys.exit(app.exec_())

        