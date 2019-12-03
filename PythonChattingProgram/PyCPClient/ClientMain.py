from PyCPClient.CommonModule import *
from PyCPClient import ClientSocket

PyCPClient_Title = "PyCPClient"


class PyCPClient(QMainWindow):

    def __init__(self):
        super().__init__()

        # -Widget Initialize-
        self.MenuBar = None
        self.MainWidget = None
        self.setting_gui()

        # -Window Setting-
        self.setWindowTitle(PyCPClient_Title)
        self.setGeometry(100, 100, 1000, 500)  # move + resize 기능
        self.show()

        # -Client Socket register-
        self.CSocket = None
        self.setting_client_socket()

    def setting_gui(self):
        self.setting_menu()
        self.setting_widget()

    def setting_menu(self):
        # [1]Menu List
        self.MenuBar = self.menuBar()
        # # [1-1] File Menu
        file_menu = self.MenuBar.addMenu("File")
        file_menu.addAction(self.setting_gui_action("Exit", qApp.exit, "Ctrl+Q", "Exit App"))
        # # [1-2] Edit Menu
        edit_menu = self.MenuBar.addMenu("Edit")
        edit_menu.addAction(self.setting_gui_action("Edit", qApp.exit))
        # # [1-3] View Menu
        view_menu = self.MenuBar.addMenu("View")
        view_menu.addAction(self.setting_gui_action("View", qApp.exit, "Alt+T"))

        # [2]Tool Bar
        tool_bar = self.addToolBar("Exit")
        tool_bar.addAction(self.setting_gui_action("Exit", qApp.exit))

        # [3]Status Bar
        self.statusBar().showMessage("ready")

    def setting_widget(self):
        # [2] Widgets
        self.MainWidget = QWidget()

        # [2-1] Set Grid
        grid = QGridLayout()
        grid.setSpacing(10)

        text_edit1 = QTextEdit()
        grid.addWidget(text_edit1, 0, 0, 1, 1)

        text_edit2 = QTextEdit()
        grid.addWidget(text_edit2, 1, 0, 1, 1)

        text_edit3 = QTextEdit()
        grid.addWidget(text_edit3, 1, 1, 4, 4)

        # [2-1] Set Title
        # title = QLabel("Title")
        # grid.addWidget(title, 0, 0, 1, 1)
        # title_edit = QTextEdit()
        # grid.addWidget(title_edit, 0, 1, 1, 1)
        #
        # author = QLabel("Author")
        # grid.addWidget(author, 1, 0, 1, 1)
        # author_edit = QTextEdit()
        # grid.addWidget(author_edit, 1, 1, 1, 1)
        #
        # review = QLabel("review")
        # grid.addWidget(review, 2, 0, 3, 1)
        # review_edit = QTextEdit()
        # grid.addWidget(review_edit, 2, 1, 3, 1)
        #
        # # [4] Setting TableWidget
        # table_widget = QTableWidget()
        # table_widget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        # col_header = ["Title", "Author", "Source"]
        # table_widget.setColumnCount(len(col_header))
        # table_widget.setHorizontalHeaderLabels(col_header)
        # table_widget.setRowCount(10)
        # grid.addWidget(table_widget, 0, 2, 5, 1)

        # End Grid Setting && Main Widget Setting
        self.MainWidget.setLayout(grid)
        self.setCentralWidget(self.MainWidget)

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

        # [4-1] Label
        self.title = QLabel("Title")
        self.title.setGeometry(300, 300, 50, 50)

        # self.author = QLabel("Author")
        # self.author.setGeometry(10, 10, 50, 20)

        # self.review = QLabel("Review")
        # self.author.setGeometry(10, 10, 50, 20)

        # [4-2] Editor
        # self.title_edit = QLineEdit()
        # self.author_edit = QLineEdit()
        # self.review_edit = QTextEdit()

        # # [4-3] Text Browser
        # self.text_browser = QTextEdit()
        # self.text_browser.setOverwriteMode(True)
        # self.text_browser.setReadOnly(True)
        #
        # # [4-4] Table Widget
        # self.table_widget = QTableWidget()
        # self.table_widget.resize(500, 1000)
        # self.table_widget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        # self.set_table_data()

        # self.text_ui()

    def set_table_data(self):
        col_header = ["Title", "Author", "Source"]
        self.table_widget.setColumnCount(len(col_header))
        self.table_widget.setHorizontalHeaderLabels(col_header)
        self.table_widget.setRowCount(10)

    def text_ui(self):
        # [4-2] Button
        # exBtn = QPushButton("exBtn")
        # exBtn.clicked.connect(self.on_click_btn)

        # [4-3] Grid
        grid = QGridLayout()

        grid.addWidget(self.title)
        # grid.addWidget(self.title_edit)
        # grid.addWidget(self.author)
        # grid.addWidget(self.author_edit)
        # grid.addWidget(self.review)
        # grid.addWidget(self.review_edit)
        # grid.addWidget(exBtn)
        # grid.addWidget(self.text_browser)
        # grid.addWidget(self.table_widget)

        self.setLayout(grid)

    def on_click_btn(self):
        self.review_edit.append(self.title_edit.text() + "\n" + self.author_edit.text())
        self.text_browser.append(self.title_edit.text() + "\n" + self.author_edit.text())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = PyCPClient()
    sys.exit(app.exec_())
