# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'localConfigUi.ui'
#
# Created: Mon Aug 18 22:53:23 2014
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

class Ui_localConfig(object):
    def setupUi(self, localConfig):
        localConfig.setObjectName(_fromUtf8("localConfig"))
        localConfig.resize(380, 348)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../pic/dapeng.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        localConfig.setWindowIcon(icon)
        self.verticalLayoutWidget = QtGui.QWidget(localConfig)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(30, 70, 81, 251))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.ipLabel = QtGui.QLabel(self.verticalLayoutWidget)
        self.ipLabel.setObjectName(_fromUtf8("ipLabel"))
        self.verticalLayout.addWidget(self.ipLabel)
        self.macLabel = QtGui.QLabel(self.verticalLayoutWidget)
        self.macLabel.setObjectName(_fromUtf8("macLabel"))
        self.verticalLayout.addWidget(self.macLabel)
        self.hostLabel = QtGui.QLabel(self.verticalLayoutWidget)
        self.hostLabel.setObjectName(_fromUtf8("hostLabel"))
        self.verticalLayout.addWidget(self.hostLabel)
        self.stafLabel = QtGui.QLabel(self.verticalLayoutWidget)
        self.stafLabel.setObjectName(_fromUtf8("stafLabel"))
        self.verticalLayout.addWidget(self.stafLabel)
        self.verticalLayoutWidget_2 = QtGui.QWidget(localConfig)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(110, 50, 160, 291))
        self.verticalLayoutWidget_2.setObjectName(_fromUtf8("verticalLayoutWidget_2"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.ipLineEdit = QtGui.QLineEdit(self.verticalLayoutWidget_2)
        self.ipLineEdit.setObjectName(_fromUtf8("ipLineEdit"))
        self.verticalLayout_2.addWidget(self.ipLineEdit)
        self.macLineEdit = QtGui.QLineEdit(self.verticalLayoutWidget_2)
        self.macLineEdit.setObjectName(_fromUtf8("macLineEdit"))
        self.verticalLayout_2.addWidget(self.macLineEdit)
        self.hostLineEdit = QtGui.QLineEdit(self.verticalLayoutWidget_2)
        self.hostLineEdit.setObjectName(_fromUtf8("hostLineEdit"))
        self.verticalLayout_2.addWidget(self.hostLineEdit)
        self.stafLineEdit = QtGui.QLineEdit(self.verticalLayoutWidget_2)
        self.stafLineEdit.setObjectName(_fromUtf8("stafLineEdit"))
        self.verticalLayout_2.addWidget(self.stafLineEdit)
        self.stafOpenButton = QtGui.QPushButton(localConfig)
        self.stafOpenButton.setGeometry(QtCore.QRect(280, 280, 75, 23))
        self.stafOpenButton.setObjectName(_fromUtf8("stafOpenButton"))

        self.retranslateUi(localConfig)
        QtCore.QMetaObject.connectSlotsByName(localConfig)

    def retranslateUi(self, localConfig):
        localConfig.setWindowTitle(_translate("localConfig", "Local Environment Configuration", None))
        localConfig.setStatusTip(_translate("localConfig", "Configurate your Local Environment", None))
        self.ipLabel.setText(_translate("localConfig", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">IP</span></p></body></html>", None))
        self.macLabel.setText(_translate("localConfig", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">MAC</span></p></body></html>", None))
        self.hostLabel.setText(_translate("localConfig", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">HOST</span></p></body></html>", None))
        self.stafLabel.setText(_translate("localConfig", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">STAF</span></p></body></html>", None))
        self.stafOpenButton.setText(_translate("localConfig", "Open", None))

