from PyCPClient.CommonModule import *
from PyCPClient import ClientSocket

PyCPClient_Title = "PyCPClient"


class PyCPClient(QWidget):

    def __init__(self):
        super().__init__()

        # Widget Initialize
        self.MainLayout = None
        self.ChatSrn = None
        self.ConnectBtn = None
        self.SendBtn = None
        self.setting_gui()

        # Window Setting
        self.setWindowTitle(PyCPClient_Title)
        self.setGeometry(600, 300, 400, 600)  # move + resize 기능
        self.show()

        # Client Socket register
        self.CSocket = None
        self.setting_client_socket()

    def setting_gui(self):
        # Main Layout
        self.MainLayout = QGridLayout()

        # Chatting Screen
        self.ChatSrn = QLineEdit("채팅방에 오신걸 환영합니다.")
        self.ChatSrn.setReadOnly(False)
        self.ChatSrn.setAlignment(Qt.AlignRight)
        self.ChatSrn.setMaxLength(15)

        # Connect Button
        self.ConnectBtn = QToolButton()
        self.ConnectBtn.setText("Connect")

        # Send Button
        self.SendBtn = QToolButton()
        self.SendBtn.setText("Send")

        # Add Widget
        self.MainLayout.addWidget(self.ChatSrn, 0, 1)
        self.MainLayout.addWidget(self.ConnectBtn, 1, 0)
        self.MainLayout.addWidget(self.SendBtn, 1, 1)

        # Layout Register
        self.setLayout(self.MainLayout)

    def setting_client_socket(self):
        self.CSocket = ClientSocket.PyClientSocket()
        self.ConnectBtn.clicked.connect(self.CSocket.connect_to_server)
        self.SendBtn.clicked.connect(self.CSocket.send_message("클라에서 접속합니다"))

    def keyPressEvent(self, e):  # 키 입력 이벤트 함수
        if e.key() == Qt.Key_Escape:  # ecs 로 종료
            print("Escape")
            sys.exit()

        elif e.key() == Qt.Key_Enter:
            print("Enter")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = PyCPClient()
    sys.exit(app.exec_())
