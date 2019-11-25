from PyCPClient.CommonModule import *
from PyCPClient import ClientSocket

PyCPClient_Title = "PyCPClient"


class PyCPClient(QWidget):

    def __init__(self):
        super().__init__()

        self.ChatScreen = QLineEdit("채팅방에 오신걸 환영합니다.")
        self.ChatScreen.setReadOnly(False)
        self.ChatScreen.setAlignment(Qt.AlignRight)
        self.ChatScreen.setMaxLength(15)

        self.ConnectBtn = QToolButton()
        self.ConnectBtn.setText("Connect")

        self.SendBtn = QToolButton()
        self.SendBtn.setText("Send")

        self.MainLayout = QGridLayout()
        self.MainLayout.addWidget(self.ChatScreen, 0, 0)
        self.MainLayout.addWidget(self.SendBtn, 1, 0)
        self.MainLayout.addWidget(self.ConnectBtn, 1, 1)

        self.setLayout(self.MainLayout)

        self.setWindowTitle(PyCPClient_Title)
        self.setGeometry(300, 300, 400, 400)  # move + resize 기능
        self.show()

        self.CSocket = ClientSocket.PyClientSocket()
        self.ConnectBtn.clicked.connect(self.CSocket.connect_to_server)
        self.SendBtn.clicked.connect(self.CSocket.send_message("클라에서 접속합니다"))

    def keyPressEvent(self, e):  # 키 입력 이벤트 함수
        if e.key() == Qt.Key_Escape:  # ecs 로 종료
            print("Escape")
            sys.exit()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = PyCPClient()
    sys.exit(app.exec_())
