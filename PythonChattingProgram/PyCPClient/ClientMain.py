from PyCPClient.CommonModule import *
from PyCPClient import ClientSocket

PyCPClient_Title = "PyCPClient"


class PyCPClient(QMainWindow):

    def __init__(self):
        super().__init__()

        # -Widget Initialize-
        self.MenuBar = None
        self.MenuList = {}
        self.setting_gui(["File", "Edit", "View", "Tool"])

        print("Address: {0}".format(self.MenuList.get("File") ) )

        # -Window Setting-
        self.setWindowTitle(PyCPClient_Title)
        self.setGeometry(600, 300, 400, 600)  # move + resize 기능
        self.show()

        # -Client Socket register-
        self.CSocket = None
        self.setting_client_socket()

    def setting_gui(self, menu_name_list):
        # [1]Menu Bar
        self.MenuBar = self.menuBar()

        # [1-1]Menu List
        self.setting_gui_menu(menu_name_list)

    def setting_gui_menu(self, menu_name_list):
        list_count = 0
        while list_count < len(menu_name_list):
            self.MenuList[menu_name_list[list_count]] = self.MenuBar.addMenu(menu_name_list[list_count])
            list_count += 1

        print("[Menu List]\n{0}".format(self.MenuList.items()))

    def setting_client_socket(self):
        self.CSocket = ClientSocket.PyClientSocket()
        # self.ConnectBtn.clicked.connect(self.CSocket.connect_to_server)
        # self.SendBtn.clicked.connect(self.CSocket.send_message("클라에서 접속합니다"))

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
