import sys
from PyQt4 import QtCore, QtGui
from addServerKey import Ui_addServerKey
import ConfigParser
import Tkinter, tkFileDialog
import shutil
import os

class ServerKeyDialog(QtGui.QMainWindow):
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
        self.setWindowTitle("Add server's public key")
        self.ui = Ui_addServerKey()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.uploadServerKey);

    def writeToINI(self, ServerAddress, result):
        cfg = ConfigParser.ConfigParser()
        cfg.read('server.ini')
        if not cfg.has_section('Server public key'):
            cfg.add_section('Server public key')
        cfg.set('Server public key', str(ServerAddress), result)
        f = open('server.ini', 'w')
        cfg.write(f)
        f.close()

    def uploadServerKey(self):
        serverName =  self.ui.lineEdit.text()
        root = Tkinter.Tk()
        root.withdraw()
        file_path = tkFileDialog.askopenfilename()
        dest_path = os.path.abspath('./keys/Server/'+serverName+'.key')
        shutil.copy2(file_path, dest_path)
        self.writeToINI(serverName, dest_path)
        self.ui.statusMsg.setText("Server public key uploaded")
        QtCore.QTimer.singleShot(1500, self.closeServerKeyDialog)

    def closeServerKeyDialog(self):
        self.close()

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    serverKeyDialog = ServerKeyDialog()
    serverKeyDialog.show()
    sys.exit(app.exec_())