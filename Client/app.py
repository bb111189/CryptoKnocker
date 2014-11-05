import sys
from PyQt4 import QtCore, QtGui
from clientUI import Ui_CrytoKnocker
from keyGeneratorDialog import KeyGeneratorUI
from ServerKeyDialog import ServerKeyDialog
import ConfigParser
import clientComms

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
        self.ui.Knock.clicked.connect(self.knockServer)
        self.ui.Lock.clicked.connect(self.lockServer)
        self.ui.actionAdd_Private_Key.triggered.connect(self.openKeyGen)
        self.ui.actionAdd_Server_Public_Key.triggered.connect(self.openAddServerKey)
        self.ui.actionExit.triggered.connect(QtGui.qApp.quit)

    def knockServer(self):
        user =  str(self.ui.UserField.text())
        server =  str(self.ui.ServerField.text())
        port =  str(self.ui.PortField.text())
        OTP = str(self.ui.OTPField.text())

        self.sendKnocks(user, server, port, OTP)

    def lockServer(self):
        user =  str(self.ui.UserField.text())
        server =  str(self.ui.ServerField.text())
        port =  str(self.ui.PortField.text())
        OTP = str(self.ui.OTPField.text())

        self.sendLocks(user, server, port, OTP)

    def sendKnocks(self, user, server,  port, otp):
        if self.isUserExists("User private key", user) and self.isPortNoValid(port) and self.isOTPValid(otp):
            UserPteKeyPath = self.GetUserPublicKey("User private key")[user]

            status = clientComms.talkToServer("OPEN", user, server, port, otp, UserPteKeyPath)
            if(status == True):
                self.printToScreen("Port knock request sent")
            else:
                self.printToScreen("Error. Please try again")

    def sendLocks(self, user, server,  port, otp):
        if self.isUserExists("User private key", user) and self.isPortNoValid(port) and self.isOTPValid(otp):
            UserPteKeyPath = self.GetUserPublicKey("User private key")[user]

            status = clientComms.talkToServer("CLOSED", user, server, port, otp, UserPteKeyPath)
            if(status == True):
                self.printToScreen("Port lock request sent")
            else:
                self.printToScreen("Error. Please try again")

    def openKeyGen(self):
        self.keygenWindow = KeyGeneratorUI(self)
        self.keygenWindow.show()

    def openAddServerKey(self):
        self.addServerKeyWindow = ServerKeyDialog(self)
        self.addServerKeyWindow.show()

    def isUserExists(self, section, user):
        Config = ConfigParser.ConfigParser()
        Config.read("user.ini")
        options = Config.options(section)
        if (user in options):
            return True
        else:
            self.printToScreen("No such user")
            return False

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

    def isPortNoValid(self, portNo):
        try:
            portNo = int(portNo)
        except:
            self.printToScreen("Invalid port number")
            return False

        if(1 <= portNo  and portNo < 65535):
            return  True
        else:
            self.printToScreen("Invalid port number")
            return False

    def isOTPValid(self, OTP):
        try:
            OTP = int(OTP)
        except:
            self.printToScreen("Invalid OTP")
            return False

        if (0 <= OTP and OTP <= 999999):
            return True
        else:
            self.printToScreen("Invalid OTP")
            return False

    def printToScreen(self, text):
        self.ui.label_6.setText(text)
        #QtCore.QTimer.singleShot(3500, self.hideLabelText)

    def hideLabelText(self):
        self.ui.label_6.setText("")

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = StartQT4()
    myapp.show()
    sys.exit(app.exec_())