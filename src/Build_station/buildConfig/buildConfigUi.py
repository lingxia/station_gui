# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'buildConfigUi.ui'
#
# Created: Thu Aug 14 18:27:47 2014
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
        buildConfig.resize(444, 513)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("dapeng.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        buildConfig.setWindowIcon(icon)
        self.horizontalLayoutWidget = QtGui.QWidget(buildConfig)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(70, 60, 291, 51))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.privateHLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.privateHLayout.setMargin(0)
        self.privateHLayout.setObjectName(_fromUtf8("privateHLayout"))
        self.privateCheckBox = QtGui.QCheckBox(self.horizontalLayoutWidget)
        self.privateCheckBox.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("private.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.privateCheckBox.setIcon(icon1)
        self.privateCheckBox.setIconSize(QtCore.QSize(28, 28))
        self.privateCheckBox.setShortcut(_fromUtf8(""))
        self.privateCheckBox.setObjectName(_fromUtf8("privateCheckBox"))
        self.privateHLayout.addWidget(self.privateCheckBox)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.privateHLayout.addItem(spacerItem)
        self.tokenLabel = QtGui.QLabel(self.horizontalLayoutWidget)
        self.tokenLabel.setObjectName(_fromUtf8("tokenLabel"))
        self.privateHLayout.addWidget(self.tokenLabel)
        self.tokenLineEdit = QtGui.QLineEdit(self.horizontalLayoutWidget)
        self.tokenLineEdit.setObjectName(_fromUtf8("tokenLineEdit"))
        self.privateHLayout.addWidget(self.tokenLineEdit)
        self.line1 = QtGui.QFrame(buildConfig)
        self.line1.setGeometry(QtCore.QRect(0, 110, 571, 16))
        self.line1.setFrameShape(QtGui.QFrame.HLine)
        self.line1.setFrameShadow(QtGui.QFrame.Sunken)
        self.line1.setObjectName(_fromUtf8("line1"))

        self.retranslateUi(buildConfig)
        QtCore.QMetaObject.connectSlotsByName(buildConfig)

    def retranslateUi(self, buildConfig):
        buildConfig.setWindowTitle(_translate("buildConfig", "Build Configuration", None))
        buildConfig.setWhatsThis(_translate("buildConfig", "<html><head/><body><p><br/></p></body></html>", None))
        self.privateCheckBox.setStatusTip(_translate("buildConfig", "If you want configurate a private station, checked the box", None))
        self.tokenLabel.setStatusTip(_translate("buildConfig", "If the station is private, please set a token", None))
        self.tokenLabel.setText(_translate("buildConfig", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Token</span></p></body></html>", None))
        self.tokenLineEdit.setStatusTip(_translate("buildConfig", "If the station is private, please set a token", None))

