import sys
from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QCoreApplication, QDate, Qt, QDateTime
from PQTMainWindow import *
import xlrd


class PQTMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()

        self.setupUi(self)
        self.center()

        self.pushButton_quit.clicked.connect(QCoreApplication.instance().quit)
        self.pushButton_testing.clicked.connect(self.update_date_info)
        self.pushButton_readxlsx.clicked.connect(self.read_xlrd)

        self.statusbar.showMessage("Ready")
        self.actionExit.triggered.connect(qApp.quit)
        self.toolBar.addAction(self.actionExit)

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def update_date_info(self):
        self.textBrowser_info.clear()
        datetime_info = QDateTime.currentDateTime()
        self.textBrowser_info.append(datetime_info.toString("yyyy-MM-dd ap hh:mm:ss"))

    def read_xlrd(self):
        # xlsx 파일 불러오기
        wb = xlrd.open_workbook("TestSheet.xlsx")
        nsheets = wb.nsheets
        sheets = wb.sheets()
        # sheet 수
        print("Number of sheets: {}".format(nsheets))
        # row, column 수
        print("Number of rows: ", sheets[0].nrows)
        print("Number of cols: ", sheets[0].ncols)
        # row, column 의 내용
        print(sheets[0].row_values(0))
        print(sheets[0].row_values(1))
        print(sheets[0].row_values(2))
        print(sheets[0].col_values(0))
        print(sheets[0].col_values(1))
        print(sheets[0].col_values(2))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    PQT_MW = PQTMainWindow()
    PQT_MW.show()
    sys.exit(app.exec_())
