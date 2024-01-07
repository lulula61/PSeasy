from PyQt5.QtWidgets import QPushButton
from PyQt5 import QtCore, QtGui, QtWidgets

class MyButton():
    def __init__(self, centralwidget,objName,textName,method=None):
        #super().__init__()
        self.entity=QtWidgets.QPushButton(centralwidget)
        self.entity.setObjectName(objName)
        self.entity.setText(textName)
        self.entity.clicked.connect(method)

    def getEntity(self):
        return self.entity