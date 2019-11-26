from PyCPServer.CommonModule import *
from PyCPServer import ServerSocket
import time

PyPCServer_Title = "PyPCServer"


class PyCPServer(QWidget):

    def __init__(self):
        super().__init__()

        self.ChatScreen = QLineEdit("이곳은 서버 입니다.")
        self.ChatScreen.setReadOnly(True)
        self.ChatScreen.setAlignment(Qt.AlignRight)
        self.ChatScreen.setMaxLength(15)

        self.ServerOnBtn = QToolButton()
        self.ServerOnBtn.setText("Server On")
        self.ServerOnBtn.clicked.connect(self.wait_client)

        self.MainLayout = QGridLayout()
        self.MainLayout.addWidget(self.ChatScreen, 0, 0)
        self.MainLayout.addWidget(self.ServerOnBtn, 1, 0)

        self.setLayout(self.MainLayout)

        self.setWindowTitle(PyPCServer_Title)
        self.setGeometry(300, 300, 600, 400)  # move + resize 기능
        self.show()

        self.th = ServerSocket.PyServerSocket()

    def keyPressEvent(self, e):  # 키 입력 이벤트 함수
        if e.key() == Qt.Key_Escape:  # ecs 로 종료
            print("Escape")
            sys.exit()
    
    # 접속대기
    def wait_client(self):
        self.ChatScreen.setText("접속 대기중...")
        return


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = PyCPServer()
    sys.exit(app.exec_())
