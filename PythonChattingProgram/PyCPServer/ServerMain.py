import sys
from PyQt5 import uic
from functools import partial

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

from PyCPServer.ServerSocket import *

form_class = uic.loadUiType("ServerMainWindow.ui")[0]


class ServerMainWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()

        self.s = PyServerSocket(self)

        # self.textBrowser_chatting = QTextBrowser(self)
        # self.listView_users = QListView(self)
        # self.pushButton_sendchat = QPushButton(self)
        # self.pushButton_endchat = QPushButton(self)

        self.setupUi(self)

        self.textBrowser_chatting.setText("")
        self.pushButton_sendchat.clicked.connect(self.btn_clicked_send_chat)
        self.pushButton_endchat.clicked.connect(self.quit_application)
        self.pushButton_serverstart.setCheckable(True)
        self.pushButton_serverstart.toggled.connect(partial(self.btn_clicked_server_start))

    def btn_clicked_server_start(self, state):
        if state:
            ip = "127.0.0.1"
            port = "8081"
            self.s.start(ip, int(port))
            self.pushButton_serverstart.setText("서버 종료")
        else:
            self.s.stop()
            # self.msg.clear()
            self.pushButton_serverstart.setText("서버 실행")

    def updateClient(self):
        print("update client")

    def updateMsg(self, msg):
        print("update msg")

    def btn_clicked_send_chat(self):
        QMessageBox.about(self, "보내기 성공", "클릭")

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.quit_application()

    def quit_application(self):
        print("quit_application")
        self.s.stop()
        sys.exit()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ServerMW = ServerMainWindow()
    ServerMW.show()
    sys.exit(app.exec_())
