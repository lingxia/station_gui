# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'runConfigUi.ui'
#
# Created: Mon Aug 18 17:44:27 2014
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
        runConfig.setWindowModality(QtCore.Qt.WindowModal)
        runConfig.resize(678, 496)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../pic/dapeng.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        runConfig.setWindowIcon(icon)
        runConfig.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.horizontalLayoutWidget = QtGui.QWidget(runConfig)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(190, 70, 291, 51))
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
        self.debuggerListWidget = QtGui.QListWidget(runConfig)
        self.debuggerListWidget.setGeometry(QtCore.QRect(0, 140, 111, 41))
        self.debuggerListWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.debuggerListWidget.setFlow(QtGui.QListView.TopToBottom)
        self.debuggerListWidget.setObjectName(_fromUtf8("debuggerListWidget"))
        item = QtGui.QListWidgetItem()
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8("../pic/jlink.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon3)
        self.debuggerListWidget.addItem(item)
        item = QtGui.QListWidgetItem()
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8("../pic/trace32.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon4)
        self.debuggerListWidget.addItem(item)
        self.debuggerStackedWidget = QtGui.QStackedWidget(runConfig)
        self.debuggerStackedWidget.setGeometry(QtCore.QRect(110, 140, 551, 331))
        self.debuggerStackedWidget.setFrameShape(QtGui.QFrame.Box)
        self.debuggerStackedWidget.setFrameShadow(QtGui.QFrame.Sunken)
        self.debuggerStackedWidget.setMidLineWidth(0)
        self.debuggerStackedWidget.setObjectName(_fromUtf8("debuggerStackedWidget"))
        self.jlinkPage = QtGui.QWidget()
        self.jlinkPage.setObjectName(_fromUtf8("jlinkPage"))
        self.jlinkButton = QtGui.QPushButton(self.jlinkPage)
        self.jlinkButton.setGeometry(QtCore.QRect(20, 20, 41, 21))
        self.jlinkButton.setIconSize(QtCore.QSize(40, 32))
        self.jlinkButton.setFlat(True)
        self.jlinkButton.setObjectName(_fromUtf8("jlinkButton"))
        self.jlinkOpenButton = QtGui.QPushButton(self.jlinkPage)
        self.jlinkOpenButton.setGeometry(QtCore.QRect(290, 20, 75, 23))
        self.jlinkOpenButton.setObjectName(_fromUtf8("jlinkOpenButton"))
        self.jlinkLineEdit = QtGui.QLineEdit(self.jlinkPage)
        self.jlinkLineEdit.setGeometry(QtCore.QRect(90, 20, 181, 20))
        self.jlinkLineEdit.setObjectName(_fromUtf8("jlinkLineEdit"))
        self.jlinkPlatformButton = QtGui.QPushButton(self.jlinkPage)
        self.jlinkPlatformButton.setGeometry(QtCore.QRect(20, 60, 61, 21))
        self.jlinkPlatformButton.setIconSize(QtCore.QSize(40, 40))
        self.jlinkPlatformButton.setFlat(True)
        self.jlinkPlatformButton.setObjectName(_fromUtf8("jlinkPlatformButton"))
        self.jlinkPlatformComboBox = QtGui.QComboBox(self.jlinkPage)
        self.jlinkPlatformComboBox.setGeometry(QtCore.QRect(90, 60, 141, 22))
        self.jlinkPlatformComboBox.setObjectName(_fromUtf8("jlinkPlatformComboBox"))
        self.jlinkTreeWidget = QtGui.QTreeWidget(self.jlinkPage)
        self.jlinkTreeWidget.setGeometry(QtCore.QRect(20, 100, 511, 211))
        self.jlinkTreeWidget.setMouseTracking(True)
        self.jlinkTreeWidget.setFrameShape(QtGui.QFrame.NoFrame)
        self.jlinkTreeWidget.setLineWidth(1)
        self.jlinkTreeWidget.setMidLineWidth(0)
        self.jlinkTreeWidget.setAutoScroll(True)
        self.jlinkTreeWidget.setEditTriggers(QtGui.QAbstractItemView.DoubleClicked|QtGui.QAbstractItemView.EditKeyPressed)
        self.jlinkTreeWidget.setTextElideMode(QtCore.Qt.ElideLeft)
        self.jlinkTreeWidget.setObjectName(_fromUtf8("jlinkTreeWidget"))
        self.jlinkTreeWidget.header().setVisible(True)
        self.jlinkTreeWidget.header().setCascadingSectionResizes(False)
        self.jlinkTreeWidget.header().setDefaultSectionSize(127)
        self.jlinkTreeWidget.header().setHighlightSections(False)
        self.jlinkTreeWidget.header().setMinimumSectionSize(27)
        self.jlinkTreeWidget.header().setStretchLastSection(False)
        self.debuggerStackedWidget.addWidget(self.jlinkPage)
        self.lauterbachPage = QtGui.QWidget()
        self.lauterbachPage.setObjectName(_fromUtf8("lauterbachPage"))
        self.lauterbachPlatformButton = QtGui.QPushButton(self.lauterbachPage)
        self.lauterbachPlatformButton.setGeometry(QtCore.QRect(20, 60, 61, 21))
        self.lauterbachPlatformButton.setIconSize(QtCore.QSize(40, 40))
        self.lauterbachPlatformButton.setFlat(True)
        self.lauterbachPlatformButton.setObjectName(_fromUtf8("lauterbachPlatformButton"))
        self.trace32LineEdit = QtGui.QLineEdit(self.lauterbachPage)
        self.trace32LineEdit.setGeometry(QtCore.QRect(90, 20, 181, 20))
        self.trace32LineEdit.setObjectName(_fromUtf8("trace32LineEdit"))
        self.trace32OpenButton = QtGui.QPushButton(self.lauterbachPage)
        self.trace32OpenButton.setGeometry(QtCore.QRect(290, 20, 75, 23))
        self.trace32OpenButton.setObjectName(_fromUtf8("trace32OpenButton"))
        self.trace32Button = QtGui.QPushButton(self.lauterbachPage)
        self.trace32Button.setGeometry(QtCore.QRect(20, 20, 51, 21))
        self.trace32Button.setIconSize(QtCore.QSize(32, 32))
        self.trace32Button.setFlat(True)
        self.trace32Button.setObjectName(_fromUtf8("trace32Button"))
        self.lauterbachPlatformComboBox = QtGui.QComboBox(self.lauterbachPage)
        self.lauterbachPlatformComboBox.setGeometry(QtCore.QRect(90, 60, 141, 22))
        self.lauterbachPlatformComboBox.setObjectName(_fromUtf8("lauterbachPlatformComboBox"))
        self.lauterbachTreeWidget = QtGui.QTreeWidget(self.lauterbachPage)
        self.lauterbachTreeWidget.setGeometry(QtCore.QRect(20, 100, 511, 211))
        self.lauterbachTreeWidget.setMouseTracking(True)
        self.lauterbachTreeWidget.setFrameShape(QtGui.QFrame.NoFrame)
        self.lauterbachTreeWidget.setLineWidth(1)
        self.lauterbachTreeWidget.setMidLineWidth(0)
        self.lauterbachTreeWidget.setAutoScroll(True)
        self.lauterbachTreeWidget.setEditTriggers(QtGui.QAbstractItemView.DoubleClicked|QtGui.QAbstractItemView.EditKeyPressed)
        self.lauterbachTreeWidget.setTextElideMode(QtCore.Qt.ElideLeft)
        self.lauterbachTreeWidget.setObjectName(_fromUtf8("lauterbachTreeWidget"))
        self.lauterbachTreeWidget.header().setVisible(True)
        self.lauterbachTreeWidget.header().setCascadingSectionResizes(False)
        self.lauterbachTreeWidget.header().setDefaultSectionSize(169)
        self.lauterbachTreeWidget.header().setHighlightSections(False)
        self.lauterbachTreeWidget.header().setMinimumSectionSize(27)
        self.lauterbachTreeWidget.header().setStretchLastSection(False)
        self.debuggerStackedWidget.addWidget(self.lauterbachPage)
        self.removeButton = QtGui.QPushButton(runConfig)
        self.removeButton.setGeometry(QtCore.QRect(10, 300, 75, 23))
        self.removeButton.setIconSize(QtCore.QSize(20, 20))
        self.removeButton.setObjectName(_fromUtf8("removeButton"))
        self.addButton = QtGui.QPushButton(runConfig)
        self.addButton.setGeometry(QtCore.QRect(10, 340, 75, 23))
        self.addButton.setObjectName(_fromUtf8("addButton"))
        self.line = QtGui.QFrame(runConfig)
        self.line.setGeometry(QtCore.QRect(0, 120, 681, 16))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))

        self.retranslateUi(runConfig)
        self.debuggerStackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(runConfig)
        runConfig.setTabOrder(self.privateCheckBox, self.tokenButton)
        runConfig.setTabOrder(self.tokenButton, self.tokenLineEdit)
        runConfig.setTabOrder(self.tokenLineEdit, self.jlinkPlatformButton)

    def retranslateUi(self, runConfig):
        runConfig.setWindowTitle(_translate("runConfig", "Run Configuration", None))
        runConfig.setStatusTip(_translate("runConfig", "GUI of Run Station Configuration", None))
        self.privateCheckBox.setStatusTip(_translate("runConfig", "If you want configurate a private station, checked the box", None))
        self.tokenButton.setStatusTip(_translate("runConfig", "If the station is private, please set a token", None))
        self.tokenLineEdit.setStatusTip(_translate("runConfig", "If the station is private, please set a token", None))
        self.debuggerListWidget.setStatusTip(_translate("runConfig", "Configurate of Debugger -- Jlink or Lauterbach", None))
        __sortingEnabled = self.debuggerListWidget.isSortingEnabled()
        self.debuggerListWidget.setSortingEnabled(False)
        item = self.debuggerListWidget.item(0)
        item.setText(_translate("runConfig", "Jlink", None))
        item = self.debuggerListWidget.item(1)
        item.setText(_translate("runConfig", "Lauterbach", None))
        self.debuggerListWidget.setSortingEnabled(__sortingEnabled)
        self.jlinkButton.setStatusTip(_translate("runConfig", "Jlink is required when use gdb(e.g. C:/SEGGER/JLinkARM_V480g)", None))
        self.jlinkButton.setText(_translate("runConfig", "Jlink", None))
        self.jlinkOpenButton.setStatusTip(_translate("runConfig", "Configurate your Jlink path", None))
        self.jlinkOpenButton.setText(_translate("runConfig", "Open", None))
        self.jlinkLineEdit.setStatusTip(_translate("runConfig", "Configurate your Jlink path", None))
        self.jlinkPlatformButton.setStatusTip(_translate("runConfig", "Select the platforms you need", None))
        self.jlinkPlatformButton.setText(_translate("runConfig", "Platform", None))
        self.jlinkTreeWidget.setStatusTip(_translate("runConfig", "Configurate your Platforms with Jlink", None))
        self.jlinkTreeWidget.headerItem().setText(0, _translate("runConfig", "Platform", None))
        self.jlinkTreeWidget.headerItem().setText(1, _translate("runConfig", "Device_Type", None))
        self.jlinkTreeWidget.headerItem().setText(2, _translate("runConfig", "Debug_Port", None))
        self.jlinkTreeWidget.headerItem().setText(3, _translate("runConfig", "Serial_Port", None))
        self.lauterbachPlatformButton.setStatusTip(_translate("runConfig", "Select the platforms you need", None))
        self.lauterbachPlatformButton.setText(_translate("runConfig", "Platform", None))
        self.trace32LineEdit.setStatusTip(_translate("runConfig", "Configurate your Trace32 path", None))
        self.trace32OpenButton.setStatusTip(_translate("runConfig", "Configurate your Trace32 path", None))
        self.trace32OpenButton.setText(_translate("runConfig", "Open", None))
        self.trace32Button.setStatusTip(_translate("runConfig", "Trace32 is required when use lauterbach(e.g. C:/T32)", None))
        self.trace32Button.setText(_translate("runConfig", "Trace32", None))
        self.lauterbachTreeWidget.setStatusTip(_translate("runConfig", "Configurate your Platforms with Lauterbach", None))
        self.lauterbachTreeWidget.headerItem().setText(0, _translate("runConfig", "Platform", None))
        self.lauterbachTreeWidget.headerItem().setText(1, _translate("runConfig", "Device_Type", None))
        self.lauterbachTreeWidget.headerItem().setText(2, _translate("runConfig", "Serial_Port", None))
        self.removeButton.setStatusTip(_translate("runConfig", "Remove the platform that do not need", None))
        self.removeButton.setText(_translate("runConfig", "Remove", None))
        self.addButton.setStatusTip(_translate("runConfig", "Add all the platforms that you selected", None))
        self.addButton.setText(_translate("runConfig", "Add", None))

