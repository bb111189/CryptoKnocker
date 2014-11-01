__author__ = 'Junhaaooooo'
import sys
from PyQt4 import QtCore, QtGui
from genPopUp import Ui_genPopup

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

    def generateKey(self):
        print self.ui.lineEdit.text()
        self.ui.label_2.setText("Keys generated")
        print "generated"

        QtCore.QTimer.singleShot(3000, self.closeKeyGen)

    def closeKeyGen(self):
        self.close()

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    keyGen = KeyGeneratorUI()
    keyGen.show()
    sys.exit(app.exec_())