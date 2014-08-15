# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dapengui.ui'
#
# Created: Fri Aug 08 19:04:06 2014
#      by: PyQt4 UI code generator 4.11.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(587, 472)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("2.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 451, 301))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.iartab = QtGui.QWidget()
        self.iartab.setObjectName(_fromUtf8("iartab"))
        self.iarcomboBox = QtGui.QComboBox(self.iartab)
        self.iarcomboBox.setGeometry(QtCore.QRect(20, 60, 69, 22))
        self.iarcomboBox.setObjectName(_fromUtf8("iarcomboBox"))
        self.iarlineEdit = QtGui.QLineEdit(self.iartab)
        self.iarlineEdit.setGeometry(QtCore.QRect(100, 60, 311, 21))
        self.iarlineEdit.setObjectName(_fromUtf8("iarlineEdit"))
        self.tabWidget.addTab(self.iartab, _fromUtf8(""))
        self.uv4tab = QtGui.QWidget()
        self.uv4tab.setObjectName(_fromUtf8("uv4tab"))
        self.uv4comboBox = QtGui.QComboBox(self.uv4tab)
        self.uv4comboBox.setGeometry(QtCore.QRect(20, 80, 69, 22))
        self.uv4comboBox.setObjectName(_fromUtf8("uv4comboBox"))
        self.uv4lineEdit = QtGui.QLineEdit(self.uv4tab)
        self.uv4lineEdit.setGeometry(QtCore.QRect(120, 80, 261, 20))
        self.uv4lineEdit.setObjectName(_fromUtf8("uv4lineEdit"))
        self.tabWidget.addTab(self.uv4tab, _fromUtf8(""))
        self.saveButton = QtGui.QPushButton(self.centralwidget)
        self.saveButton.setGeometry(QtCore.QRect(250, 380, 75, 23))
        self.saveButton.setObjectName(_fromUtf8("saveButton"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "dapeng", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.iartab), _translate("MainWindow", "iar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.uv4tab), _translate("MainWindow", "uv4", None))
        self.saveButton.setText(_translate("MainWindow", "Save", None))

