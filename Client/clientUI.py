# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'client.ui'
#
# Created: Sun Nov 02 16:12:17 2014
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

class Ui_CrytoKnocker(object):
    def setupUi(self, CrytoKnocker):
        CrytoKnocker.setObjectName(_fromUtf8("CrytoKnocker"))
        CrytoKnocker.resize(280, 390)
        CrytoKnocker.setMinimumSize(QtCore.QSize(280, 390))
        CrytoKnocker.setMaximumSize(QtCore.QSize(280, 390))
        self.centralwidget = QtGui.QWidget(CrytoKnocker)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.UserField = QtGui.QLineEdit(self.centralwidget)
        self.UserField.setGeometry(QtCore.QRect(140, 180, 113, 20))
        self.UserField.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.UserField.setToolTip(_fromUtf8(""))
        self.UserField.setStatusTip(_fromUtf8(""))
        self.UserField.setAccessibleName(_fromUtf8(""))
        self.UserField.setAccessibleDescription(_fromUtf8(""))
        self.UserField.setAutoFillBackground(False)
        self.UserField.setText(_fromUtf8(""))
        self.UserField.setObjectName(_fromUtf8("UserField"))
        self.ServerField = QtGui.QLineEdit(self.centralwidget)
        self.ServerField.setGeometry(QtCore.QRect(140, 210, 113, 20))
        self.ServerField.setObjectName(_fromUtf8("ServerField"))
        self.OTPField = QtGui.QLineEdit(self.centralwidget)
        self.OTPField.setGeometry(QtCore.QRect(140, 270, 113, 20))
        self.OTPField.setObjectName(_fromUtf8("OTPField"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 180, 46, 13))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 210, 81, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 240, 46, 13))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(30, 270, 101, 16))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.PortField = QtGui.QLineEdit(self.centralwidget)
        self.PortField.setGeometry(QtCore.QRect(140, 240, 113, 20))
        self.PortField.setObjectName(_fromUtf8("PortField"))
        self.Knock = QtGui.QPushButton(self.centralwidget)
        self.Knock.setGeometry(QtCore.QRect(150, 300, 75, 23))
        self.Knock.setObjectName(_fromUtf8("Knock"))
        self.Lock = QtGui.QPushButton(self.centralwidget)
        self.Lock.setGeometry(QtCore.QRect(50, 300, 75, 23))
        self.Lock.setObjectName(_fromUtf8("Lock"))
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(70, 10, 141, 161))
        self.label_5.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_5.setAutoFillBackground(False)
        self.label_5.setText(_fromUtf8(""))
        self.label_5.setPixmap(QtGui.QPixmap(_fromUtf8("images/cryptoknocker_resize.png")))
        self.label_5.setScaledContents(True)
        self.label_5.setIndent(1)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(30, 330, 221, 20))
        self.label_6.setText(_fromUtf8(""))
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        CrytoKnocker.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(CrytoKnocker)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 280, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuOptions = QtGui.QMenu(self.menubar)
        self.menuOptions.setObjectName(_fromUtf8("menuOptions"))
        CrytoKnocker.setMenuBar(self.menubar)
        self.actionExit = QtGui.QAction(CrytoKnocker)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.actionAdd_Private_Key = QtGui.QAction(CrytoKnocker)
        self.actionAdd_Private_Key.setObjectName(_fromUtf8("actionAdd_Private_Key"))
        self.actionAdd_Server_Public_Key = QtGui.QAction(CrytoKnocker)
        self.actionAdd_Server_Public_Key.setObjectName(_fromUtf8("actionAdd_Server_Public_Key"))
        self.menuOptions.addSeparator()
        self.menuOptions.addAction(self.actionAdd_Private_Key)
        self.menuOptions.addAction(self.actionAdd_Server_Public_Key)
        self.menuOptions.addAction(self.actionExit)
        self.menubar.addAction(self.menuOptions.menuAction())

        self.retranslateUi(CrytoKnocker)
        QtCore.QMetaObject.connectSlotsByName(CrytoKnocker)

    def retranslateUi(self, CrytoKnocker):
        CrytoKnocker.setWindowTitle(_translate("CrytoKnocker", "CrytoKnocker", None))
        self.label.setText(_translate("CrytoKnocker", "User ID", None))
        self.label_2.setText(_translate("CrytoKnocker", "Server Address", None))
        self.label_3.setText(_translate("CrytoKnocker", "Port", None))
        self.label_4.setText(_translate("CrytoKnocker", "One Time Password", None))
        self.Knock.setText(_translate("CrytoKnocker", "Knock", None))
        self.Lock.setText(_translate("CrytoKnocker", "Lock", None))
        self.menuOptions.setTitle(_translate("CrytoKnocker", "Options", None))
        self.actionExit.setText(_translate("CrytoKnocker", "Exit", None))
        self.actionAdd_Private_Key.setText(_translate("CrytoKnocker", "Add Private Key", None))
        self.actionAdd_Server_Public_Key.setText(_translate("CrytoKnocker", "Add Server Public Key", None))

