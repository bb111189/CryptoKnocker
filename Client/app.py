import sys
from PyQt4 import QtCore, QtGui
from clientUI import Ui_CrytoKnocker
from keyGeneratorUI import KeyGeneratorUI
import keyGeneratorUI


class StartQT4(QtGui.QMainWindow):
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
        self.ui = Ui_CrytoKnocker()
        self.ui.setupUi(self)

        self.setIconImage()

        self.ui.Knock.clicked.connect(self.knockServer);
        self.ui.Lock.clicked.connect(self.lockServer);
        self.ui.actionAdd_Private_Key.triggered.connect(self.openKeyGen);
        self.ui.actionExit.triggered.connect(QtGui.qApp.quit);

    def knockServer(self):
        self.ui.label_6.setText("Port open")
        print self.ui.UserField.text()
        print self.ui.ServerField.text()
        print self.ui.PortField.text()
        print self.ui.OTPField.text()
        print "hi"

        QtCore.QTimer.singleShot(3000, self.hideLabelText)

    def lockServer(self):
        self.ui.label_6.setText("Port closed")
        print self.ui.UserField.text()
        print self.ui.ServerField.text()
        print self.ui.PortField.text()
        print self.ui.OTPField.text()
        print "bye"

        QtCore.QTimer.singleShot(3000, self.hideLabelText)

    def openKeyGen(self):
        self.keygenWindow = KeyGeneratorUI(self)
        self.keygenWindow.show()

    def hideLabelText(self):
        self.ui.label_6.setText("")

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = StartQT4()
    myapp.show()
    sys.exit(app.exec_())