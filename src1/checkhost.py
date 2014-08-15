from PyQt4.QtCore import *
from PyQt4.QtGui import *
from getconfig import Getconfig
import checkui
import sys
import successhost

confile = Getconfig("config.xml")

class check(QMainWindow):
    
    def __init__(self, parent = None):
        super(check,self).__init__(parent)
        self.checkwin = checkui.Ui_check()
        self.checkwin.setupUi(self)
        self.iartxt = confile.getValue('iar')
        self.scene = QGraphicsScene()
        self.sucwin = successhost.success()
        self.connect(self.checkwin.okButton, SIGNAL("clicked()"), self.sucwin.showsuc)
        self.connect(self.checkwin.okButton, SIGNAL("clicked()"), self.close)
   
    def loadimage(self):
        if self.iartxt == "C:\IARSystems\EmbeddedWorkbench72":
            self.scene.addPixmap(QPixmap("pass.jpg"))
        else:
            self.scene.addPixmap(QPixmap("fail.jpg"))
        
#        self.checkwin.checkGraph.resize(130,130)
#        self.checkwin.checkGraph.setSceneRect(3.0,3.0,5.0,0.0)
        self.checkwin.checkGraph.setScene(self.scene)
#        self.scene.show()
        
        
    def checkshown(self):
        self.show()
    
    
       
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    checkframe = check()
    checkframe.show()
    sys.exit(app.exec_())