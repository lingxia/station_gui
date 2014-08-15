# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'checkui.ui'
#
# Created: Mon Aug 11 14:34:39 2014
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

class Ui_check(object):
    def setupUi(self, check):
        check.setObjectName(_fromUtf8("check"))
        check.resize(539, 382)
        self.checkGraph = QtGui.QGraphicsView(check)
        self.checkGraph.setGeometry(QtCore.QRect(140, 70, 151, 141))
        self.checkGraph.setObjectName(_fromUtf8("checkGraph"))
        self.lineEdit = QtGui.QLineEdit(check)
        self.lineEdit.setGeometry(QtCore.QRect(20, 110, 21, 20))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.okButton = QtGui.QPushButton(check)
        self.okButton.setGeometry(QtCore.QRect(310, 230, 75, 23))
        self.okButton.setObjectName(_fromUtf8("okButton"))
        self.label = QtGui.QLabel(check)
        self.label.setGeometry(QtCore.QRect(70, 110, 46, 13))
        self.label.setObjectName(_fromUtf8("label"))

        self.retranslateUi(check)
        QtCore.QMetaObject.connectSlotsByName(check)

    def retranslateUi(self, check):
        check.setWindowTitle(_translate("check", "check", None))
        self.lineEdit.setText(_translate("check", "iar", None))
        self.okButton.setText(_translate("check", "OK", None))
        self.label.setText(_translate("check", "iar", None))

