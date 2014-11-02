import sys
from PyQt4 import QtCore, QtGui
from clientUI import Ui_CrytoKnocker
from keyGeneratorUI import KeyGeneratorUI
import ConfigParser

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
        user =  str(self.ui.UserField.text())
        server =  str(self.ui.ServerField.text())
        port =  str(self.ui.PortField.text())
        OTP = str(self.ui.OTPField.text())

        if self.isUserExists("User private key", user):
            UserPteKey = self.GetUserPublicKey("User private key")[user]
            print UserPteKey

            #Meed to pass to nich script with the following parameter: User, Server, Port, OTP, User's private key
            self.ui.label_6.setText("Port open")
            QtCore.QTimer.singleShot(3000, self.hideLabelText
)

    def lockServer(self):
        user =  str(self.ui.UserField.text())
        server =  str(self.ui.ServerField.text())
        port =  str(self.ui.PortField.text())
        OTP = str(self.ui.OTPField.text())

        if self.isUserExists("User private key", user):
            UserPteKey = self.GetUserPublicKey("User private key")[user]
            print UserPteKey

            #Meed to pass to nich script with the following parameter: User, Server, Port, OTP, User's private key
            self.ui.label_6.setText("Port closed")
            QtCore.QTimer.singleShot(3000, self.hideLabelText)

    def openKeyGen(self):
        self.keygenWindow = KeyGeneratorUI(self)
        self.keygenWindow.show()

    def hideLabelText(self):
        self.ui.label_6.setText("")

    def isUserExists(self, section, user):
        Config = ConfigParser.ConfigParser()
        Config.read("user.ini")
        options = Config.options(section)
        return user in options


    def GetUserPublicKey(self, section):
        Config = ConfigParser.ConfigParser()
        Config.read("user.ini")
        dict1 = {}
        options = Config.options(section)
        for option in options:
            try:
                dict1[option] = Config.get(section, option)
            except:
                dict1[option] = None
        return dict1


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = StartQT4()
    myapp.show()
    sys.exit(app.exec_())