# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'runConfigUi.ui'
#
# Created: Fri Aug 15 17:58:50 2014
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

class Ui_runConfig(object):
    def setupUi(self, runConfig):
        runConfig.setObjectName(_fromUtf8("runConfig"))
        runConfig.resize(417, 470)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../pic/dapeng.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        runConfig.setWindowIcon(icon)
        self.horizontalLayoutWidget = QtGui.QWidget(runConfig)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(70, 60, 291, 51))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.privateHLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.privateHLayout.setMargin(0)
        self.privateHLayout.setObjectName(_fromUtf8("privateHLayout"))
        self.privateCheckBox = QtGui.QCheckBox(self.horizontalLayoutWidget)
        self.privateCheckBox.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("../pic/private.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.privateCheckBox.setIcon(icon1)
        self.privateCheckBox.setIconSize(QtCore.QSize(28, 28))
        self.privateCheckBox.setShortcut(_fromUtf8(""))
        self.privateCheckBox.setObjectName(_fromUtf8("privateCheckBox"))
        self.privateHLayout.addWidget(self.privateCheckBox)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.privateHLayout.addItem(spacerItem)
        self.tokenButton = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.tokenButton.setText(_fromUtf8(""))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("../pic/token.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tokenButton.setIcon(icon2)
        self.tokenButton.setIconSize(QtCore.QSize(28, 28))
        self.tokenButton.setFlat(True)
        self.tokenButton.setObjectName(_fromUtf8("tokenButton"))
        self.privateHLayout.addWidget(self.tokenButton)
        self.tokenLineEdit = QtGui.QLineEdit(self.horizontalLayoutWidget)
        self.tokenLineEdit.setObjectName(_fromUtf8("tokenLineEdit"))
        self.privateHLayout.addWidget(self.tokenLineEdit)
        self.line2 = QtGui.QFrame(runConfig)
        self.line2.setGeometry(QtCore.QRect(-10, 110, 571, 16))
        self.line2.setFrameShape(QtGui.QFrame.HLine)
        self.line2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line2.setObjectName(_fromUtf8("line2"))
        self.verticalLayoutWidget = QtGui.QWidget(runConfig)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 170, 91, 96))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.jlinkButton = QtGui.QPushButton(self.verticalLayoutWidget)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8("../pic/jlink.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.jlinkButton.setIcon(icon3)
        self.jlinkButton.setIconSize(QtCore.QSize(40, 32))
        self.jlinkButton.setFlat(True)
        self.jlinkButton.setObjectName(_fromUtf8("jlinkButton"))
        self.verticalLayout.addWidget(self.jlinkButton)
        self.trace32Button = QtGui.QPushButton(self.verticalLayoutWidget)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8("../pic/trace32.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.trace32Button.setIcon(icon4)
        self.trace32Button.setIconSize(QtCore.QSize(32, 32))
        self.trace32Button.setFlat(True)
        self.trace32Button.setObjectName(_fromUtf8("trace32Button"))
        self.verticalLayout.addWidget(self.trace32Button)
        self.verticalLayoutWidget_2 = QtGui.QWidget(runConfig)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(120, 170, 181, 91))
        self.verticalLayoutWidget_2.setObjectName(_fromUtf8("verticalLayoutWidget_2"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.jlinkLineEdit = QtGui.QLineEdit(self.verticalLayoutWidget_2)
        self.jlinkLineEdit.setObjectName(_fromUtf8("jlinkLineEdit"))
        self.verticalLayout_2.addWidget(self.jlinkLineEdit)
        self.trace32LineEdit = QtGui.QLineEdit(self.verticalLayoutWidget_2)
        self.trace32LineEdit.setObjectName(_fromUtf8("trace32LineEdit"))
        self.verticalLayout_2.addWidget(self.trace32LineEdit)
        self.verticalLayoutWidget_3 = QtGui.QWidget(runConfig)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(310, 170, 77, 91))
        self.verticalLayoutWidget_3.setObjectName(_fromUtf8("verticalLayoutWidget_3"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setMargin(0)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.jlinkButton_2 = QtGui.QPushButton(self.verticalLayoutWidget_3)
        self.jlinkButton_2.setObjectName(_fromUtf8("jlinkButton_2"))
        self.verticalLayout_3.addWidget(self.jlinkButton_2)
        self.trace32Button_2 = QtGui.QPushButton(self.verticalLayoutWidget_3)
        self.trace32Button_2.setObjectName(_fromUtf8("trace32Button_2"))
        self.verticalLayout_3.addWidget(self.trace32Button_2)

        self.retranslateUi(runConfig)
        QtCore.QMetaObject.connectSlotsByName(runConfig)

    def retranslateUi(self, runConfig):
        runConfig.setWindowTitle(_translate("runConfig", "Run Configuration", None))
        runConfig.setStatusTip(_translate("runConfig", "GUI of Run Station Configuration", None))
        self.privateCheckBox.setStatusTip(_translate("runConfig", "If you want configurate a private station, checked the box", None))
        self.tokenButton.setStatusTip(_translate("runConfig", "If the station is private, please set a token", None))
        self.tokenLineEdit.setStatusTip(_translate("runConfig", "If the station is private, please set a token", None))
        self.jlinkButton.setStatusTip(_translate("runConfig", "Jlink is required when use gdb(e.g. C:/SEGGER/JLinkARM_V480g)", None))
        self.jlinkButton.setText(_translate("runConfig", "Jlink", None))
        self.trace32Button.setStatusTip(_translate("runConfig", "Trace32 is required when use lauterbach(e.g. C:/T32)", None))
        self.trace32Button.setText(_translate("runConfig", "Trace32", None))
        self.jlinkLineEdit.setStatusTip(_translate("runConfig", "Configurate your Jlink path", None))
        self.trace32LineEdit.setStatusTip(_translate("runConfig", "Configurate your Trace32 path", None))
        self.jlinkButton_2.setStatusTip(_translate("runConfig", "Configurate your Jlink path", None))
        self.jlinkButton_2.setText(_translate("runConfig", "Open", None))
        self.trace32Button_2.setStatusTip(_translate("runConfig", "Configurate your Trace32 path", None))
        self.trace32Button_2.setText(_translate("runConfig", "Open", None))
