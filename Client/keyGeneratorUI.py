__author__ = 'Junhaaooooo'
import sys
from PyQt4 import QtCore, QtGui
from genPopUp import Ui_genPopup
from Crypto.PublicKey import RSA
import ConfigParser
import os

class KeyGeneratorUI(QtGui.QMainWindow):
    def setIconImage(self):
        app_icon = QtGui.QIcon()
        app_icon.addFile('images/cryptoknocker_resize.png', QtCore.QSize(16, 16))
        app_icon.addFile('images/cryptoknocker_resize.png', QtCore.QSize(24, 24))
        app_icon.addFile('images/cryptoknocker_resize.png', QtCore.QSize(32, 32))
        app_icon.addFile('images/cryptoknocker_resize.png', QtCore.QSize(48, 48))
        app_icon.addFile('images/cryptoknocker_resize.png', QtCore.QSize(256, 256))
        app.setWindowIcon(app_icon)

    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.setWindowTitle("Generate new pair of key")
        self.ui = Ui_genPopup()
        self.ui.setupUi(self)
        self.ui.generateButton.clicked.connect(self.generateKey);

    def generateRSAKeyPair(self, userName):
        privFileName = "./keys/private/" + userName + ".key"
        pubFileName = "./keys/public/" + userName + ".key"

        rsakeys = RSA.generate(2048)
        privHandle = open(privFileName, 'wb')
        privHandle.write(rsakeys.exportKey())
        privHandle.close()

        pubHandle = open(pubFileName, 'wb')
        pubHandle.write(rsakeys.publickey().exportKey())
        pubHandle.close()

        return os.path.abspath(privFileName), os.path.abspath(pubFileName)

    def writeToINI(self, userName, result):
        cfg = ConfigParser.ConfigParser()
        cfg.read('user.ini')
        if not cfg.has_section('User private key'):
            cfg.add_section('User private key')
        if not cfg.has_section('User public key'):
            cfg.add_section('User public key')
        cfg.set('User private key', str(userName), result[0])
        cfg.set('User public key', str(userName), result[1])
        f = open('user.ini', 'w')
        cfg.write(f)
        f.close()

    def generateKey(self):
        userName =  self.ui.lineEdit.text()
        if (userName != ""):
            result = self.generateRSAKeyPair(userName)
            self.writeToINI(userName, result)
            self.ui.label_2.setText("Keys generated")
            QtCore.QTimer.singleShot(3000, self.closeKeyGen)

        else:
            self.ui.label_2.setText("Please enter a user name")

    def closeKeyGen(self):
        self.close()

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    keyGen = KeyGeneratorUI()
    keyGen.show()
    sys.exit(app.exec_())