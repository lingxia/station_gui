# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'buildConfigUi.ui'
#
# Created: Wed Aug 13 17:23:26 2014
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
        buildConfig.resize(537, 503)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("dapeng.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        buildConfig.setWindowIcon(icon)
        buildConfig.setFrameShape(QtGui.QFrame.StyledPanel)
        buildConfig.setFrameShadow(QtGui.QFrame.Raised)
        self.buildType_ComboBox = QtGui.QComboBox(buildConfig)
        self.buildType_ComboBox.setGeometry(QtCore.QRect(150, 30, 69, 22))
        self.buildType_ComboBox.setObjectName(_fromUtf8("buildType_ComboBox"))
        self.buildType_ComboBox.addItem(_fromUtf8(""))
        self.buildType_ComboBox.addItem(_fromUtf8(""))
        self.buildType_Lable = QtGui.QLabel(buildConfig)
        self.buildType_Lable.setGeometry(QtCore.QRect(10, 30, 141, 21))
        self.buildType_Lable.setObjectName(_fromUtf8("buildType_Lable"))
        self.buildToken_label = QtGui.QLabel(buildConfig)
        self.buildToken_label.setGeometry(QtCore.QRect(250, 30, 91, 21))
        self.buildToken_label.setObjectName(_fromUtf8("buildToken_label"))
        self.buildToken_lineEdit = QtGui.QLineEdit(buildConfig)
        self.buildToken_lineEdit.setGeometry(QtCore.QRect(350, 30, 151, 20))
        self.buildToken_lineEdit.setReadOnly(False)
        self.buildToken_lineEdit.setObjectName(_fromUtf8("buildToken_lineEdit"))

        self.retranslateUi(buildConfig)
        QtCore.QMetaObject.connectSlotsByName(buildConfig)

    def retranslateUi(self, buildConfig):
        buildConfig.setWindowTitle(_translate("buildConfig", "Build Configuration", None))
        self.buildType_ComboBox.setItemText(0, _translate("buildConfig", "Private", None))
        self.buildType_ComboBox.setItemText(1, _translate("buildConfig", "Public", None))
        self.buildType_Lable.setText(_translate("buildConfig", "<html><head/><body><p><span style=\" font-size:12pt;\">Build Station Type</span></p></body></html>", None))
        self.buildToken_label.setText(_translate("buildConfig", "<html><head/><body><p><span style=\" font-size:12pt;\">Build Token</span></p></body></html>", None))

