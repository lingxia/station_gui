# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'buildConfigUi.ui'
#
# Created: Fri Aug 15 20:37:36 2014
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
        buildConfig.resize(418, 471)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../pic/dapeng.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
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
        self.line1 = QtGui.QFrame(buildConfig)
        self.line1.setGeometry(QtCore.QRect(0, 110, 571, 16))
        self.line1.setFrameShape(QtGui.QFrame.HLine)
        self.line1.setFrameShadow(QtGui.QFrame.Sunken)
        self.line1.setObjectName(_fromUtf8("line1"))
        self.ideLabel = QtGui.QLabel(buildConfig)
        self.ideLabel.setGeometry(QtCore.QRect(110, 120, 201, 31))
        self.ideLabel.setObjectName(_fromUtf8("ideLabel"))
        self.verticalLayoutWidget = QtGui.QWidget(buildConfig)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(30, 160, 84, 281))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.ideVLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.ideVLayout.setMargin(0)
        self.ideVLayout.setObjectName(_fromUtf8("ideVLayout"))
        self.iarButton = QtGui.QPushButton(self.verticalLayoutWidget)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8("../pic/iar.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.iarButton.setIcon(icon3)
        self.iarButton.setIconSize(QtCore.QSize(32, 32))
        self.iarButton.setAutoDefault(False)
        self.iarButton.setDefault(False)
        self.iarButton.setFlat(True)
        self.iarButton.setObjectName(_fromUtf8("iarButton"))
        self.ideVLayout.addWidget(self.iarButton)
        self.uv4Button = QtGui.QPushButton(self.verticalLayoutWidget)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8("../pic/uv4.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.uv4Button.setIcon(icon4)
        self.uv4Button.setIconSize(QtCore.QSize(32, 32))
        self.uv4Button.setFlat(True)
        self.uv4Button.setObjectName(_fromUtf8("uv4Button"))
        self.ideVLayout.addWidget(self.uv4Button)
        self.gccButton = QtGui.QPushButton(self.verticalLayoutWidget)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8("../pic/gcc.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.gccButton.setIcon(icon5)
        self.gccButton.setIconSize(QtCore.QSize(32, 32))
        self.gccButton.setFlat(True)
        self.gccButton.setObjectName(_fromUtf8("gccButton"))
        self.ideVLayout.addWidget(self.gccButton)
        self.kdsButton = QtGui.QPushButton(self.verticalLayoutWidget)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8("../pic/kds.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.kdsButton.setIcon(icon6)
        self.kdsButton.setIconSize(QtCore.QSize(32, 32))
        self.kdsButton.setFlat(True)
        self.kdsButton.setObjectName(_fromUtf8("kdsButton"))
        self.ideVLayout.addWidget(self.kdsButton)
        self.cw10Button = QtGui.QPushButton(self.verticalLayoutWidget)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(_fromUtf8("../pic/codewarrior.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cw10Button.setIcon(icon7)
        self.cw10Button.setIconSize(QtCore.QSize(32, 32))
        self.cw10Button.setFlat(True)
        self.cw10Button.setObjectName(_fromUtf8("cw10Button"))
        self.ideVLayout.addWidget(self.cw10Button)
        self.mingwButton = QtGui.QPushButton(self.verticalLayoutWidget)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(_fromUtf8("../pic/mingw.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.mingwButton.setIcon(icon8)
        self.mingwButton.setIconSize(QtCore.QSize(25, 25))
        self.mingwButton.setFlat(True)
        self.mingwButton.setObjectName(_fromUtf8("mingwButton"))
        self.ideVLayout.addWidget(self.mingwButton)
        self.verticalLayoutWidget_2 = QtGui.QWidget(buildConfig)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(120, 150, 181, 311))
        self.verticalLayoutWidget_2.setObjectName(_fromUtf8("verticalLayoutWidget_2"))
        self.ideLineEditVLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget_2)
        self.ideLineEditVLayout.setMargin(0)
        self.ideLineEditVLayout.setObjectName(_fromUtf8("ideLineEditVLayout"))
        self.iarLineEdit = QtGui.QLineEdit(self.verticalLayoutWidget_2)
        self.iarLineEdit.setObjectName(_fromUtf8("iarLineEdit"))
        self.ideLineEditVLayout.addWidget(self.iarLineEdit)
        self.uv4LineEdit = QtGui.QLineEdit(self.verticalLayoutWidget_2)
        self.uv4LineEdit.setObjectName(_fromUtf8("uv4LineEdit"))
        self.ideLineEditVLayout.addWidget(self.uv4LineEdit)
        self.gccLineEdit = QtGui.QLineEdit(self.verticalLayoutWidget_2)
        self.gccLineEdit.setObjectName(_fromUtf8("gccLineEdit"))
        self.ideLineEditVLayout.addWidget(self.gccLineEdit)
        self.kdsLineEdit = QtGui.QLineEdit(self.verticalLayoutWidget_2)
        self.kdsLineEdit.setObjectName(_fromUtf8("kdsLineEdit"))
        self.ideLineEditVLayout.addWidget(self.kdsLineEdit)
        self.cw10LineEdit = QtGui.QLineEdit(self.verticalLayoutWidget_2)
        self.cw10LineEdit.setObjectName(_fromUtf8("cw10LineEdit"))
        self.ideLineEditVLayout.addWidget(self.cw10LineEdit)
        self.lineEdit = QtGui.QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.ideLineEditVLayout.addWidget(self.lineEdit)
        self.verticalLayoutWidget_3 = QtGui.QWidget(buildConfig)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(310, 150, 77, 311))
        self.verticalLayoutWidget_3.setObjectName(_fromUtf8("verticalLayoutWidget_3"))
        self.ideComboBoxVLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget_3)
        self.ideComboBoxVLayout.setMargin(0)
        self.ideComboBoxVLayout.setObjectName(_fromUtf8("ideComboBoxVLayout"))
        self.iarComboBox = QtGui.QComboBox(self.verticalLayoutWidget_3)
        self.iarComboBox.setObjectName(_fromUtf8("iarComboBox"))
        self.ideComboBoxVLayout.addWidget(self.iarComboBox)
        self.uv4ComboBox = QtGui.QComboBox(self.verticalLayoutWidget_3)
        self.uv4ComboBox.setObjectName(_fromUtf8("uv4ComboBox"))
        self.ideComboBoxVLayout.addWidget(self.uv4ComboBox)
        self.gccOpenButton = QtGui.QPushButton(self.verticalLayoutWidget_3)
        self.gccOpenButton.setObjectName(_fromUtf8("gccOpenButton"))
        self.ideComboBoxVLayout.addWidget(self.gccOpenButton)
        self.kdsOpenButton = QtGui.QPushButton(self.verticalLayoutWidget_3)
        self.kdsOpenButton.setObjectName(_fromUtf8("kdsOpenButton"))
        self.ideComboBoxVLayout.addWidget(self.kdsOpenButton)
        self.cw10OpenButton = QtGui.QPushButton(self.verticalLayoutWidget_3)
        self.cw10OpenButton.setObjectName(_fromUtf8("cw10OpenButton"))
        self.ideComboBoxVLayout.addWidget(self.cw10OpenButton)
        self.mingwOpenButton = QtGui.QPushButton(self.verticalLayoutWidget_3)
        self.mingwOpenButton.setObjectName(_fromUtf8("mingwOpenButton"))
        self.ideComboBoxVLayout.addWidget(self.mingwOpenButton)

        self.retranslateUi(buildConfig)
        QtCore.QMetaObject.connectSlotsByName(buildConfig)
        buildConfig.setTabOrder(self.privateCheckBox, self.tokenButton)
        buildConfig.setTabOrder(self.tokenButton, self.tokenLineEdit)
        buildConfig.setTabOrder(self.tokenLineEdit, self.iarButton)
        buildConfig.setTabOrder(self.iarButton, self.iarLineEdit)
        buildConfig.setTabOrder(self.iarLineEdit, self.iarComboBox)
        buildConfig.setTabOrder(self.iarComboBox, self.uv4Button)
        buildConfig.setTabOrder(self.uv4Button, self.uv4LineEdit)
        buildConfig.setTabOrder(self.uv4LineEdit, self.uv4ComboBox)
        buildConfig.setTabOrder(self.uv4ComboBox, self.gccButton)
        buildConfig.setTabOrder(self.gccButton, self.gccLineEdit)
        buildConfig.setTabOrder(self.gccLineEdit, self.gccOpenButton)
        buildConfig.setTabOrder(self.gccOpenButton, self.kdsButton)
        buildConfig.setTabOrder(self.kdsButton, self.kdsLineEdit)
        buildConfig.setTabOrder(self.kdsLineEdit, self.kdsOpenButton)
        buildConfig.setTabOrder(self.kdsOpenButton, self.cw10Button)
        buildConfig.setTabOrder(self.cw10Button, self.cw10LineEdit)
        buildConfig.setTabOrder(self.cw10LineEdit, self.cw10OpenButton)
        buildConfig.setTabOrder(self.cw10OpenButton, self.mingwButton)
        buildConfig.setTabOrder(self.mingwButton, self.lineEdit)
        buildConfig.setTabOrder(self.lineEdit, self.mingwOpenButton)

    def retranslateUi(self, buildConfig):
        buildConfig.setWindowTitle(_translate("buildConfig", "Build Configuration", None))
        buildConfig.setStatusTip(_translate("buildConfig", "GUI of Build Station Configuration", None))
        buildConfig.setWhatsThis(_translate("buildConfig", "<html><head/><body><p><br/></p></body></html>", None))
        self.privateCheckBox.setStatusTip(_translate("buildConfig", "If you want configurate a private station, checked the box", None))
        self.tokenButton.setStatusTip(_translate("buildConfig", "If the station is private, please set a token", None))
        self.tokenLineEdit.setStatusTip(_translate("buildConfig", "If the station is private, please set a token", None))
        self.ideLabel.setStatusTip(_translate("buildConfig", "Configurate the IDEs that needed", None))
        self.ideLabel.setText(_translate("buildConfig", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">IDE Configuration</span></p></body></html>", None))
        self.iarButton.setStatusTip(_translate("buildConfig", "Configurate your IAR path", None))
        self.iarButton.setText(_translate("buildConfig", "IAR", None))
        self.uv4Button.setStatusTip(_translate("buildConfig", "Configurate your UV4 path", None))
        self.uv4Button.setText(_translate("buildConfig", "UV4", None))
        self.gccButton.setStatusTip(_translate("buildConfig", "Configurate your GCC path", None))
        self.gccButton.setText(_translate("buildConfig", "GCC", None))
        self.kdsButton.setStatusTip(_translate("buildConfig", "Configurate your KDS path", None))
        self.kdsButton.setText(_translate("buildConfig", "KDS", None))
        self.cw10Button.setStatusTip(_translate("buildConfig", "Configurate your Code Worrior path", None))
        self.cw10Button.setText(_translate("buildConfig", "CW", None))
        self.mingwButton.setStatusTip(_translate("buildConfig", "MinGW is required when use gcc_arm (e.g. C:/MinGW)", None))
        self.mingwButton.setText(_translate("buildConfig", "MinGW", None))
        self.iarLineEdit.setStatusTip(_translate("buildConfig", "Configurate your IAR path", None))
        self.uv4LineEdit.setStatusTip(_translate("buildConfig", "Configurate your UV4 path", None))
        self.gccLineEdit.setStatusTip(_translate("buildConfig", "Configurate your GCC path", None))
        self.kdsLineEdit.setStatusTip(_translate("buildConfig", "Configurate your KDS path", None))
        self.cw10LineEdit.setStatusTip(_translate("buildConfig", "Configurate your Code Worrior path", None))
        self.lineEdit.setStatusTip(_translate("buildConfig", "Configurate your MinGW path", None))
        self.iarComboBox.setStatusTip(_translate("buildConfig", "Select the lastest version of IAR", None))
        self.uv4ComboBox.setStatusTip(_translate("buildConfig", "Select the lastest version of UV4", None))
        self.gccOpenButton.setStatusTip(_translate("buildConfig", "Configurate your GCC path", None))
        self.gccOpenButton.setText(_translate("buildConfig", "Open", None))
        self.kdsOpenButton.setStatusTip(_translate("buildConfig", "Configurate your KDS path", None))
        self.kdsOpenButton.setText(_translate("buildConfig", "Open", None))
        self.cw10OpenButton.setStatusTip(_translate("buildConfig", "Configurate your Code Worrior path", None))
        self.cw10OpenButton.setText(_translate("buildConfig", "Open", None))
        self.mingwOpenButton.setStatusTip(_translate("buildConfig", "Configurate your MinGW path", None))
        self.mingwOpenButton.setText(_translate("buildConfig", "Open", None))

