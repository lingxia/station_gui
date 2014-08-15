from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys
import pulldownui,buildhost
import platform_list
from  getconfig import Getconfig

confile = Getconfig('config.xml')

class pullframe(QMainWindow):

    def __init__(self, parent = None):
        self.device = platform_list.device_type
        self.platform = platform_list.platform_list
        global length
        length = len(self.platform)
        
        super(pullframe,self).__init__(parent)
        self.buildwin = buildhost.buildframe()
        self.pullwin = pulldownui.Ui_Form()
        self.pullwin.setupUi(self)
        for num in range(0,length):
            self.pullwin.comboBox.addItem("")
            self.pullwin.comboBox.setItemText(num,self.platform[num])
        self.connect(self.pullwin.comboBox,SIGNAL("activated(int)"),self.filltext)
        self.connect(self.pullwin.saveButton,SIGNAL("clicked()"),self.getValue)
        self.connect(self.pullwin.cleanButton,SIGNAL("clicked()"),self.pullwin.textEdit.clear)
#        self.connect(self.pullwin.saveButton,SIGNAL("clicked()"),self.buildwin.shownbuild)
        self.connect(self.pullwin.saveButton,SIGNAL("clicked()"),self.close)        
        
    def filltext(self):
        seq = self.pullwin.comboBox.currentIndex()
        if self.pullwin.comboBox.itemText(seq) == self.platform[seq]:
            self.pullwin.textEdit.setText(self.device[seq])
            
    def getValue(self):
        plain = self.pullwin.comboBox.currentText()
        confile.setValue('platform', plain.__str__())
        
    def shownpull(self):
        self.show()
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    pullwin = pullframe()
    pullwin.show()
    sys.exit(app.exec_())

            