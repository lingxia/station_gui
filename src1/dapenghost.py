from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys, os
import dapengui,pulldownhost
import platform_list
from getconfig import Getconfig


confile = Getconfig("config.xml")

class dapeng(QMainWindow):
    
    def __init__(self, parent = None):
        super(dapeng, self).__init__(parent)
        self.ide = platform_list.ide_list
        self.pullwin = pulldownhost.pullframe()
        self.dapengwin = dapengui.Ui_MainWindow()
        self.dapengwin.setupUi(self)
        self.dapengwin.iarcomboBox.addItem("")
        self.dapengwin.iarcomboBox.addItem("")
        self.dapengwin.iarcomboBox.setItemText(1,self.ide[0])
        self.dapengwin.uv4comboBox.addItem("")
        self.dapengwin.uv4comboBox.addItem("")
        self.dapengwin.uv4comboBox.setItemText(1,self.ide[2])
        self.connect(self.dapengwin.iarcomboBox,SIGNAL("activated(int)"),self.fillbank)
        self.connect(self.dapengwin.uv4comboBox,SIGNAL("activated(int)"),self.fillbank)
        self.connect(self.dapengwin.saveButton,SIGNAL("clicked()"),self.getValue)
#        self.connect(self.dapengwin.nextButton,SIGNAL("clicked()"),self.pullwin.shownpull)
        self.connect(self.dapengwin.saveButton,SIGNAL("clicked()"),self.close)
        
    
    def fillbank(self):
        if self.dapengwin.iarcomboBox.currentText() == "iar":
            self.dapengwin.iarlineEdit.setText("C:\IARSystems\EmbeddedWorkbench72")
        if self.dapengwin.uv4comboBox.currentText() == "uv4":
            self.dapengwin.uv4lineEdit.setText("C:\Keil_v5\UV4")

    def getValue(self):
        iarText = self.dapengwin.iarlineEdit.displayText()
        confile.setValue('iar',iarText.__str__())
        uv4Text = self.dapengwin.uv4lineEdit.displayText()
        confile.setValue('uv4',uv4Text.__str__())
    
    def showndapeng(self):
        self.show()

        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    dapengwin = dapeng()
    dapengwin.show()
    sys.exit(app.exec_())