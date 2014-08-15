# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'configui.ui'
#
# Created: Thu Aug 07 10:57:40 2014
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

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(332, 234)
        self.textEdit = QtGui.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(60, 60, 151, 51))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.okButton = QtGui.QPushButton(Form)
        self.okButton.setGeometry(QtCore.QRect(100, 160, 75, 23))
        self.okButton.setObjectName(_fromUtf8("okButton"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "config", None))
        self.okButton.setText(_translate("Form", "OK", None))

