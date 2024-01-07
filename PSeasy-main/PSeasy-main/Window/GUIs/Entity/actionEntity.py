from PyQt5.QtWidgets import QPushButton
from PyQt5 import QtCore, QtGui, QtWidgets

class MyAction():
    def __init__(self, MainWindow,objName,textName,method=None):
        #super().__init__()
        self.entity=QtWidgets.QAction(MainWindow)
        self.entity.setObjectName(objName)
        self.entity.setText(textName)
        self.entity.triggered.connect(method)

    def getEntity(self):
        return self.entity





