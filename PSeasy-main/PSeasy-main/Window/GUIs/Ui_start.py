# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\zly17\Desktop\courses\软件工程\Project\PSeasy1.0\start_UI.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 800)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 1200, 800))
        self.label.setStyleSheet("background-image: url(:/images/project-1.0/img/PSeasy.png);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(840, 280, 140, 140))
        self.pushButton.setStyleSheet("QPushButton{      \n"
"background-image: url(:/images/project-1.0/img/button.png);\n"
"border:none;\n"
"border-radius:70px;\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-image: url(:/images/project-1.0/img/pushButton.png);\n"
"border-radius:70px;\n"
"\n"
"}")
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.close_window) #关闭登录窗口
        self.pushButton.clicked.connect(self.open)  # 打开新窗口
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        
    def open(self,m):
        from GUI import win
        self.m = win()
        self.m.show()
    
    def close_window(self):
        Start.close()
    

import start_rc
import sys
from qt_material import apply_stylesheet

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    Start = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(Start)
    apply_stylesheet(app, theme='dark_amber.xml')#,invert_secondary=True)
    Start.show()
    sys.exit(app.exec())
