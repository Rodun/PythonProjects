from PyCPClient.CommonModule import *
from PyCPClient import ClientSocket

PyCPClient_Title = "PyCPClient"


class PyCPClient(QMainWindow):

    def __init__(self):
        super().__init__()

        # -Widget Initialize-
        self.MenuBar = None
        self.setting_gui()

        # -Window Setting-
        self.setWindowTitle(PyCPClient_Title)
        self.setGeometry(600, 300, 400, 600)  # move + resize 기능
        self.show()

        # -Client Socket register-
        self.CSocket = None
        self.setting_client_socket()

    def setting_gui(self):
        # [1]Menu Bar
        self.MenuBar = self.menuBar()

        # [1-1]Menu List
        file_menu = self.MenuBar.addMenu("File")
        file_menu.addAction(self.setting_gui_action("Exit", qApp.exit, "Ctrl+Q", "Exit App"))

        edit_menu = self.MenuBar.addMenu("Edit")
        edit_menu.addAction(self.setting_gui_action("Edit", qApp.exit))

        view_menu = self.MenuBar.addMenu("View")
        view_menu.addAction(self.setting_gui_action("View", qApp.exit, "Alt+T"))

        # [2]Tool Bar
        tool_bar = self.addToolBar("Exit")
        tool_bar.addAction(self.setting_gui_action("Exit", qApp.exit))

        # [3]Status Bar
        self.statusBar().showMessage("ready")

        # [4] Widgets
        editor = QtForm()
        self.setCentralWidget(editor)

    def setting_gui_action(self, name, trigger, shortcut="", status_tip=""):
        _Action = QAction(QIcon(""), name, self)
        _Action.setShortcut(shortcut)
        _Action.setStatusTip(status_tip)
        _Action.triggered.connect(trigger)
        return _Action

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


class QtForm(QWidget):
    def __init__(self):
        super().__init__()
        self.text_ui()

    def text_ui(self):
        # [4-1] Label
        title = QLabel("Title")
        author = QLabel("Author")
        review = QLabel("Review")

        # [4-2] Editor
        title_edit = QLineEdit()
        author_edit = QLineEdit()
        review_edit = QTextEdit()

        # [4-3] Grid - Git용 체크
        grid = QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(title, 1, 0)
        grid.addWidget(title_edit, 1, 1)

        grid.addWidget(author, 2, 0)
        grid.addWidget(author_edit, 2, 1)

        grid.addWidget(review, 3, 0)
        grid.addWidget(review_edit, 3, 1, 5, 1)

        self.setLayout(grid)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = PyCPClient()
    sys.exit(app.exec_())
