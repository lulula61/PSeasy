from myThread import FilterThread, colorThread, cameraThread
from qt_material import apply_stylesheet
from pylab import *
from dialog.colorDialog import *
from tools import color, camera
from tools import filters
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
import os
import sys
import cv2
import matplotlib

from mainWindow import Ui_MainWindow
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMainWindow, QProgressBar, QInputDialog, QMessageBox

from view import Draw

class cache():
    def __init__(self, pth):
        self.cache_pth = pth
        for root, dir, file in os.walk(pth):
            file.sort(key=lambda x:int(x[:-4]))
            self.filelist = file
        self.type = ''
        if len(self.filelist):
            self.type = self.filelist[0][-4:]

    def set_type(self, t):
        self.type = t
        print(self.type)

    def in_cache(self, img):
        print(img.dtype)
        length = len(self.filelist)
        img_name = os.path.join(self.cache_pth, str(length) + self.type)
        print(img_name)
        cv2.imencode(self.type, np.array(img))[1].tofile(img_name)
        self.filelist.append(str(length) + self.type)
        self.filelist.sort(key=lambda x:int(x[:-4]))
    
    def pop_cache(self):
        length = len(self.filelist) - 1
        img_name = os.path.join(self.cache_pth, str(length) + self.type)
        os.remove(img_name)
        self.filelist.pop(length)

    def empty(self):
        return (len(self.filelist) == 0)