# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'successui.ui'
#
# Created: Mon Aug 11 13:59:44 2014
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

class Ui_logon_2(object):
    def setupUi(self, logon_2):
        logon_2.setObjectName(_fromUtf8("logon_2"))
        logon_2.resize(224, 86)
        self.logon = QtGui.QTextBrowser(logon_2)
        self.logon.setGeometry(QtCore.QRect(0, 0, 311, 231))
        self.logon.setOpenLinks(True)
        self.logon.setObjectName(_fromUtf8("logon"))

        self.retranslateUi(logon_2)
        QtCore.QMetaObject.connectSlotsByName(logon_2)

    def retranslateUi(self, logon_2):
        logon_2.setWindowTitle(_translate("logon_2", "Dialog", None))
        self.logon.setHtml(_translate("logon_2", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Logon Successful</span></p></body></html>", None))

