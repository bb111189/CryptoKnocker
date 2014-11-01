# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'genPopUp.ui'
#
# Created: Sun Nov 02 01:48:05 2014
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

class Ui_genPopup(object):
    def setupUi(self, genPopup):
        genPopup.setObjectName(_fromUtf8("genPopup"))
        genPopup.resize(285, 120)
        genPopup.setMaximumSize(QtCore.QSize(285, 120))
        self.centralwidget = QtGui.QWidget(genPopup)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 30, 61, 20))
        self.label.setObjectName(_fromUtf8("label"))
        self.generateButton = QtGui.QPushButton(self.centralwidget)
        self.generateButton.setGeometry(QtCore.QRect(50, 60, 191, 23))
        self.generateButton.setObjectName(_fromUtf8("generateButton"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(0, 100, 281, 20))
        self.label_2.setText(_fromUtf8(""))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setProperty("toolTipDuration", 1)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(102, 30, 161, 20))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.StatusLabel = QtGui.QLabel(self.centralwidget)
        self.StatusLabel.setGeometry(QtCore.QRect(-10, 90, 291, 20))
        self.StatusLabel.setText(_fromUtf8(""))
        self.StatusLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.StatusLabel.setObjectName(_fromUtf8("StatusLabel"))
        genPopup.setCentralWidget(self.centralwidget)

        self.retranslateUi(genPopup)
        QtCore.QMetaObject.connectSlotsByName(genPopup)

    def retranslateUi(self, genPopup):
        genPopup.setWindowTitle(_translate("genPopup", "Generate key pair", None))
        self.label.setText(_translate("genPopup", "User Name", None))
        self.generateButton.setText(_translate("genPopup", "Generate Public and Private Key Pair", None))

