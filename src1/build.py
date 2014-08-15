# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'build.ui'
#
# Created: Fri Aug 08 19:07:40 2014
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

class Ui_build(object):
    def setupUi(self, build):
        build.setObjectName(_fromUtf8("build"))
        build.resize(400, 300)
        self.buildcheckBox = QtGui.QCheckBox(build)
        self.buildcheckBox.setGeometry(QtCore.QRect(80, 80, 70, 17))
        self.buildcheckBox.setObjectName(_fromUtf8("buildcheckBox"))
        self.runcheckBox = QtGui.QCheckBox(build)
        self.runcheckBox.setGeometry(QtCore.QRect(80, 110, 70, 17))
        self.runcheckBox.setObjectName(_fromUtf8("runcheckBox"))
        self.buildandruncheckBox = QtGui.QCheckBox(build)
        self.buildandruncheckBox.setGeometry(QtCore.QRect(80, 140, 191, 17))
        self.buildandruncheckBox.setObjectName(_fromUtf8("buildandruncheckBox"))
        self.saveButton = QtGui.QPushButton(build)
        self.saveButton.setGeometry(QtCore.QRect(80, 190, 75, 23))
        self.saveButton.setObjectName(_fromUtf8("saveButton"))

        self.retranslateUi(build)
        QtCore.QMetaObject.connectSlotsByName(build)

    def retranslateUi(self, build):
        build.setWindowTitle(_translate("build", "build", None))
        self.buildcheckBox.setText(_translate("build", "build", None))
        self.runcheckBox.setText(_translate("build", "run", None))
        self.buildandruncheckBox.setText(_translate("build", "build and run", None))
        self.saveButton.setText(_translate("build", "Save", None))

