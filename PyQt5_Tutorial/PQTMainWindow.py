# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PQTMain.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(727, 560)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../Users/김동현/.designer/backup/wild_puma.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_quit = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_quit.setGeometry(QtCore.QRect(540, 420, 81, 31))
        self.pushButton_quit.setObjectName("pushButton_quit")
        self.pushButton_testing = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_testing.setGeometry(QtCore.QRect(530, 20, 121, 41))
        self.pushButton_testing.setStyleSheet("color: rgb(35, 20, 255);\n"
"background-color: rgb(156, 255, 156);\n"
"font: 75 11pt \"Consolas\";")
        self.pushButton_testing.setObjectName("pushButton_testing")
        self.pushButton_readxlsx = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_readxlsx.setGeometry(QtCore.QRect(530, 90, 111, 41))
        self.pushButton_readxlsx.setObjectName("pushButton_readxlsx")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 491, 441))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.textBrowser_info = QtWidgets.QTextBrowser(self.tab)
        self.textBrowser_info.setGeometry(QtCore.QRect(10, 10, 411, 341))
        self.textBrowser_info.setObjectName("textBrowser_info")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 727, 21))
        self.menubar.setObjectName("menubar")
        self.menufile = QtWidgets.QMenu(self.menubar)
        self.menufile.setObjectName("menufile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setStatusTip("")
        self.actionOpen.setShortcut("")
        self.actionOpen.setShortcutContext(QtCore.Qt.WindowShortcut)
        self.actionOpen.setObjectName("actionOpen")
        self.actionExit = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("exit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionExit.setIcon(icon1)
        self.actionExit.setObjectName("actionExit")
        self.menufile.addAction(self.actionOpen)
        self.menufile.addAction(self.actionExit)
        self.menufile.addSeparator()
        self.menubar.addAction(self.menufile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_quit.setToolTip(_translate("MainWindow", "<html><head/><body><p>프로그램 종료</p></body></html>"))
        self.pushButton_quit.setText(_translate("MainWindow", "Quit"))
        self.pushButton_testing.setText(_translate("MainWindow", "Testing"))
        self.pushButton_readxlsx.setText(_translate("MainWindow", "read xlsx"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Tab 1"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Tab 2"))
        self.menufile.setTitle(_translate("MainWindow", "File"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionExit.setStatusTip(_translate("MainWindow", "Exit Application"))
        self.actionExit.setShortcut(_translate("MainWindow", "Ctrl+X"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

