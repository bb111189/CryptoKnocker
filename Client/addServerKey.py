# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addServerKey.ui'
#
# Created: Wed Nov 05 13:37:00 2014
#      by: PyQt4 UI code generator 4.11.2
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

class Ui_addServerKey(object):
    def setupUi(self, addServerKey):
        addServerKey.setObjectName(_fromUtf8("addServerKey"))
        addServerKey.resize(320, 150)
        addServerKey.setMinimumSize(QtCore.QSize(320, 150))
        addServerKey.setMaximumSize(QtCore.QSize(320, 150))
        self.centralwidget = QtGui.QWidget(addServerKey)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(50, 90, 221, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(122, 40, 161, 20))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 40, 71, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.statusMsg = QtGui.QLabel(self.centralwidget)
        self.statusMsg.setGeometry(QtCore.QRect(0, 120, 321, 20))
        self.statusMsg.setText(_fromUtf8(""))
        self.statusMsg.setAlignment(QtCore.Qt.AlignCenter)
        self.statusMsg.setObjectName(_fromUtf8("statusMsg"))
        addServerKey.setCentralWidget(self.centralwidget)

        self.retranslateUi(addServerKey)
        QtCore.QMetaObject.connectSlotsByName(addServerKey)

    def retranslateUi(self, addServerKey):
        addServerKey.setWindowTitle(_translate("addServerKey", "Upload server\'s public key", None))
        self.pushButton.setText(_translate("addServerKey", "Choose and upload server\'s public key", None))
        self.label.setText(_translate("addServerKey", "Server address", None))

