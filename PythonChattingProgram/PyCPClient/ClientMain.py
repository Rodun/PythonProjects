import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyCPClient.ClientSocket import *
from PyQt5 import uic

form_class = uic.loadUiType("ClientMainWindow.ui")[0]


class ClientMainWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()

        self.c = PyClientSocket(self)

        self.setupUi(self)

        self.pushButton_connectserver.clicked.connect(self.connectClicked)

    def __del__(self):
        self.c.stop()

    def connectClicked(self):
        if self.c.bConnect == False:
            ip = "127.0.0.1"
            port = "10020"
            if self.c.connectServer(ip, int(port)):
                self.pushButton_connectserver.setText("접속 종료하기")
            else:
                self.c.stop()
                self.pushButton_connectserver.setText("서버 접속하기")
        else:
            self.c.stop()
            self.sendmsg.clear()
            self.recvmsg.clear()
            self.pushButton_connectserver.setText("서버 접속하기")

    def updateMsg(self, msg):
        print("update msg")

    def updateDisconnect(self):
        self.pushButton_connectserver.setText("서버 접속하기")

    def sendMsg(self):
        self.c.send("client test msg")

    def cleaMsg(self):
        print("clear msg")

    def closeEvent(self, e):
        self.c.stop()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ClientMW = ClientMainWindow()
    ClientMW.show()
    app.exec_()

