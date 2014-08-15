# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qqdpui.ui'
#
# Created: Fri Aug 08 18:44:59 2014
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

class Ui_QToolBox(object):
    def setupUi(self, QToolBox):
        QToolBox.setObjectName(_fromUtf8("QToolBox"))
        QToolBox.resize(263, 461)
        self.logon = QtGui.QWidget()
        self.logon.setGeometry(QtCore.QRect(0, 0, 263, 407))
        self.logon.setObjectName(_fromUtf8("logon"))
        self.pullButton = QtGui.QPushButton(self.logon)
        self.pullButton.setGeometry(QtCore.QRect(10, 20, 75, 23))
        self.pullButton.setObjectName(_fromUtf8("pullButton"))
        self.checkButton = QtGui.QPushButton(self.logon)
        self.checkButton.setGeometry(QtCore.QRect(10, 60, 75, 23))
        self.checkButton.setObjectName(_fromUtf8("checkButton"))
        QToolBox.addItem(self.logon, _fromUtf8(""))
        self.logoff = QtGui.QWidget()
        self.logoff.setGeometry(QtCore.QRect(0, 0, 263, 407))
        self.logoff.setObjectName(_fromUtf8("logoff"))
        self.dapengButton = QtGui.QPushButton(self.logoff)
        self.dapengButton.setGeometry(QtCore.QRect(10, 20, 75, 23))
        self.dapengButton.setObjectName(_fromUtf8("dapengButton"))
        self.buildButton = QtGui.QPushButton(self.logoff)
        self.buildButton.setGeometry(QtCore.QRect(10, 70, 75, 23))
        self.buildButton.setObjectName(_fromUtf8("buildButton"))
        QToolBox.addItem(self.logoff, _fromUtf8(""))

        self.retranslateUi(QToolBox)
        QToolBox.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(QToolBox)

    def retranslateUi(self, QToolBox):
        QToolBox.setWindowTitle(_translate("QToolBox", "qqdp", None))
        self.pullButton.setText(_translate("QToolBox", "pulldown", None))
        self.checkButton.setText(_translate("QToolBox", "check", None))
        QToolBox.setItemText(QToolBox.indexOf(self.logon), _translate("QToolBox", "logon", None))
        self.dapengButton.setText(_translate("QToolBox", "dapeng", None))
        self.buildButton.setText(_translate("QToolBox", "build", None))
        QToolBox.setItemText(QToolBox.indexOf(self.logoff), _translate("QToolBox", "logoff", None))

