from PyCPClient.CommonModule import *
from PyCPClient import ClientSocket

PyCPClient_Title = "PyCPClient"


class PyCPClient(QMainWindow):  # Main Window Class

    def __init__(self):
        super().__init__()

        # -- Widget Initialize --
        self.MenuBar = None
        self.MainWidget = None
        self.setting_menu()
        self.setting_widget()

        # -- Window Setting --
        self.setWindowTitle(PyCPClient_Title)
        self.setGeometry(100, 100, 1000, 500)  # move + resize 기능
        self.show()

        # -- Client Socket register --
        self.CSocket = None
        self.setting_client_socket()

    def setting_menu(self):
        # [1] Menu List
        self.MenuBar = self.menuBar()
        # [1-1] File Menu
        file_menu = self.MenuBar.addMenu("File")
        file_menu.addAction(self.setting_gui_action("Exit", qApp.exit, "Ctrl+Q", "Exit App"))
        # [1-2] Edit Menu
        edit_menu = self.MenuBar.addMenu("Edit")
        edit_menu.addAction(self.setting_gui_action("Edit", qApp.exit))
        # [1-3] View Menu
        view_menu = self.MenuBar.addMenu("View")
        view_menu.addAction(self.setting_gui_action("View", qApp.exit, "Alt+T"))

        # [2] Tool Bar
        tool_bar = self.addToolBar("Exit")
        tool_bar.addAction(self.setting_gui_action("Exit", qApp.exit))

        # [3] Status Bar
        self.statusBar().showMessage("ready")

    def setting_gui_action(self, name, trigger, shortcut="", status_tip=""):
        _Action = QAction(QIcon(""), name, self)
        _Action.setShortcut(shortcut)
        _Action.setStatusTip(status_tip)
        _Action.triggered.connect(trigger)
        return _Action

    def setting_widget(self):
        self.MainWidget = MainClientWidget(self)

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


class MainClientWidget(QWidget):  # Widget Class
    def __init__(self, parent):
        super().__init__()

        self.title_label = QLabel("Title", parent)
        self.title_edit = QLineEdit(parent)
        self.author_label = QLabel("Author", parent)
        self.author_edit = QLineEdit(parent)
        self.review_label = QLabel("Review", parent)
        self.review_edit = QTextEdit(parent)
        self.send_button = QPushButton("Send", parent)
        self.table_widget = QTableWidget(parent)
        self.image_label_1 = QLabel(parent)
        self.open_dialog_button = QPushButton("Open Dialog", parent)

        self.setting_widget(parent)

    def setting_widget(self, parent):
        # [1] First Widget Axis
        default_x = 10
        default_y = 50

        # [2] Input Information
        # [2-1] Title
        self.title_label.setGeometry(default_x, default_y, 50, 20)
        self.title_edit.setGeometry(default_x + 50, default_y, 120, 20)
        # [2-2] Author
        self.author_label.setGeometry(default_x, default_y + 30, 50, 20)
        self.author_edit.setGeometry(default_x + 50, default_y + 30, self.title_edit.width(), self.title_edit.height())
        # [2-3] Review
        self.review_label.setGeometry(default_x, default_y + 60, 50, 20)
        self.review_edit.setReadOnly(True)
        self.review_edit.setOverwriteMode(True)
        self.review_edit.setGeometry(default_x + 50, default_y + 60, 120, 200)

        # [3] Button
        self.send_button.setGeometry(default_x + 120, default_y + 70 + 200, 50, 20)
        self.send_button.clicked.connect(self.on_click_send_btn)

        # [4] Table
        self.table_widget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        col_headers = ["Title", "Author", "Review"]
        self.table_widget.setColumnCount(len(col_headers))
        self.table_widget.setHorizontalHeaderLabels(col_headers)
        self.table_widget.setRowCount(20)
        self.table_widget.setGeometry(default_x + 200, default_y, 200, 400)
        # [4-1] Table Data Setting (feat. CSV)
        self.setting_table_data(self.table_widget)

        # [5] Image
        self.setting_image_label(self.image_label_1, "resources\\Lion.jpg")
        self.image_label_1.setGeometry(450, 50, 200, 200)

        # [6] Dialog
        # [6-1] open Dialog Button
        self.open_dialog_button.setGeometry(450, default_y + 70 + 200, 100, 20)
        self.open_dialog_button.clicked.connect(self.show_dialog)

    def on_click_send_btn(self):
        self.review_edit.setText(self.title_edit.text() + "\n" + self.author_edit.text())

    def setting_table_data(self, table):
        title_csv = []
        author_csv = []
        review_csv = []

        with open("resources\\TestData.csv", "r+") as f:
            for row in csv.DictReader(f):
                title_csv.append(row["Title"])
                author_csv.append(row["Author"])
                review_csv.append(row["Review"])

        print(title_csv)
        print(author_csv)
        print(review_csv)

        for row, (_title, _author, _review) in enumerate(zip(title_csv, author_csv, review_csv)):
            table.setItem(row, 0, QTableWidgetItem(_title))
            table.setItem(row, 1, QTableWidgetItem(_author))
            table.setItem(row, 2, QTableWidgetItem(_review))

        table.resizeColumnsToContents()
        table.resizeRowsToContents()

    def setting_image_label(self, img_lbl, img_path):
        pix_map = QPixmap(img_path)
        img_lbl.setPixmap(pix_map)

    def show_dialog(self):
        test, ok = QInputDialog.getText(self, "input Dialog", "Enter your name:")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = PyCPClient()
    sys.exit(app.exec_())