# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pulldownui.ui'
#
# Created: Fri Aug 08 19:00:50 2014
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
        Form.resize(478, 366)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("2.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.comboBox = QtGui.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(40, 60, 121, 31))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.textEdit = QtGui.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(230, 80, 151, 61))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.cleanButton = QtGui.QPushButton(Form)
        self.cleanButton.setGeometry(QtCore.QRect(60, 170, 75, 23))
        self.cleanButton.setObjectName(_fromUtf8("cleanButton"))
        self.saveButton = QtGui.QPushButton(Form)
        self.saveButton.setGeometry(QtCore.QRect(330, 170, 75, 23))
        self.saveButton.setObjectName(_fromUtf8("saveButton"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "pulldown", None))
        self.cleanButton.setText(_translate("Form", "Clean", None))
        self.saveButton.setText(_translate("Form", "Save", None))

