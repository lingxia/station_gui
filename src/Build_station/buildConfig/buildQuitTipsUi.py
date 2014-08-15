# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'buildQuitTipsUi.ui'
#
# Created: Fri Aug 15 10:24:29 2014
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

class Ui_buildQuitTips(object):
    def setupUi(self, buildQuitTips):
        buildQuitTips.setObjectName(_fromUtf8("buildQuitTips"))
        buildQuitTips.resize(357, 252)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("pics/dapeng.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        buildQuitTips.setWindowIcon(icon)
        self.buildQuitTextBrowser = QtGui.QTextBrowser(buildQuitTips)
        self.buildQuitTextBrowser.setGeometry(QtCore.QRect(40, 50, 281, 81))
        self.buildQuitTextBrowser.setAutoFillBackground(False)
        self.buildQuitTextBrowser.setFrameShape(QtGui.QFrame.VLine)
        self.buildQuitTextBrowser.setFrameShadow(QtGui.QFrame.Plain)
        self.buildQuitTextBrowser.setObjectName(_fromUtf8("buildQuitTextBrowser"))
        self.horizontalLayoutWidget = QtGui.QWidget(buildQuitTips)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(100, 170, 160, 41))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.quitButtonHLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.quitButtonHLayout.setMargin(0)
        self.quitButtonHLayout.setObjectName(_fromUtf8("quitButtonHLayout"))
        self.quitYesButton = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.quitYesButton.setDefault(False)
        self.quitYesButton.setFlat(False)
        self.quitYesButton.setObjectName(_fromUtf8("quitYesButton"))
        self.quitButtonHLayout.addWidget(self.quitYesButton)
        self.quitNoButton = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.quitNoButton.setObjectName(_fromUtf8("quitNoButton"))
        self.quitButtonHLayout.addWidget(self.quitNoButton)

        self.retranslateUi(buildQuitTips)
        QtCore.QMetaObject.connectSlotsByName(buildQuitTips)

    def retranslateUi(self, buildQuitTips):
        buildQuitTips.setWindowTitle(_translate("buildQuitTips", "Attention", None))
        self.buildQuitTextBrowser.setStatusTip(_translate("buildQuitTips", "Tips", None))
        self.buildQuitTextBrowser.setWhatsThis(_translate("buildQuitTips", "A Warning when Quit the Build Configuration", None))
        self.buildQuitTextBrowser.setHtml(_translate("buildQuitTips", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">The Configuration File has not been Saved ! </span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">Are you sure to Quit ?</span></p></body></html>", None))
        self.quitYesButton.setStatusTip(_translate("buildQuitTips", "Yes = Quit", None))
        self.quitYesButton.setText(_translate("buildQuitTips", "Yes", None))
        self.quitNoButton.setStatusTip(_translate("buildQuitTips", "No = Not Quit", None))
        self.quitNoButton.setText(_translate("buildQuitTips", "No", None))

