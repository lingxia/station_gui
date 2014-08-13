# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'buildConfigUi.ui'
#
# Created: Wed Aug 13 23:57:08 2014
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

class Ui_buildConfig(object):
    def setupUi(self, buildConfig):
        buildConfig.setObjectName(_fromUtf8("buildConfig"))
        buildConfig.resize(521, 494)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("dapeng.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        buildConfig.setWindowIcon(icon)
        self.comboBox = QtGui.QComboBox(buildConfig)
        self.comboBox.setGeometry(QtCore.QRect(160, 200, 69, 22))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))

        self.retranslateUi(buildConfig)
        QtCore.QMetaObject.connectSlotsByName(buildConfig)

    def retranslateUi(self, buildConfig):
        buildConfig.setWindowTitle(_translate("buildConfig", "Build Configuration", None))
        buildConfig.setWhatsThis(_translate("buildConfig", "<html><head/><body><p><br/></p></body></html>", None))

