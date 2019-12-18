import sys
from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QCoreApplication
from PQTMainWindow import *


class PQTMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()

        self.setupUi(self)
        self.center()

        self.pushButton_quit.clicked.connect(QCoreApplication.instance().quit)

        self.statusbar.showMessage("Ready")
        self.actionExit.triggered.connect(qApp.quit)

        self.toolBar.addAction(self.actionExit)

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    PQT_MW = PQTMainWindow()
    PQT_MW.show()
    sys.exit(app.exec_())
