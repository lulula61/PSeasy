import os

import cv2
from PyQt5.QtCore import QThread, pyqtSignal
import numpy as np
from easyocr import easyocr

from tools import color

class FilterThread(QThread):
    finished = pyqtSignal(np.ndarray)

    def __init__(self, method, result, size, x1, y1, x2, y2):
        super(FilterThread, self).__init__()
        self.method = method
        self.result = result
        self.size = size
        self.x_start = x1
        self.y_start = y1
        self.x_end = x2
        self.y_end = y2

    def run(self):
        self.result = self.method(self.result.copy(
        ), self.size, self.x_start, self.y_start, self.x_end, self.y_end)
        self.finished.emit(self.result)


class colorThread(QThread):
    finished = pyqtSignal(np.ndarray)

    def __init__(self, method, result, channel_r, channel_g, channel_b, x1, y1, x2, y2):
        super(colorThread, self).__init__()
        self.method = method
        self.result = result
        self.channel_r = channel_r
        self.channel_g = channel_g
        self.channel_b = channel_b
        self.x_start = x1
        self.y_start = y1
        self.x_end = x2
        self.y_end = y2

    def run(self):
        self.result = self.method(self.result.copy(), self.channel_r, self.channel_g,
                                  self.channel_b, self.x_start, self.y_start, self.x_end, self.y_end)
        self.finished.emit(self.result)


class cameraThread(QThread):
    finished = pyqtSignal(np.ndarray)

    def __init__(self, method, result, x1, y1, x2, y2, points):
        super(cameraThread, self).__init__()
        self.method = method
        self.result = result
        self.x_start = x1
        self.y_start = y1
        self.x_end = x2
        self.y_end = y2
        self.points=points

    def run(self):
        self.result = self.method(
            self.result.copy(), self.x_start, self.y_start, self.x_end, self.y_end, self.points)
        self.finished.emit(self.result)

class thresholdThread(QThread):
    finished = pyqtSignal(np.ndarray)

    def __init__(self, method, result, kernel,x1, y1, x2, y2, points=None):
        super(thresholdThread, self).__init__()
        self.method = method
        self.result = result
        self.kernel=kernel
        self.x_start = x1
        self.y_start = y1
        self.x_end = x2
        self.y_end = y2
        self.points=points

    def run(self):
        self.result = self.method(
            self.result.copy(), self.kernel,self.x_start, self.y_start, self.x_end, self.y_end, self.points)
        self.finished.emit(self.result)

class multipleThread(QThread):
        #finished = pyqtSignal(np.ndarray)

        def __init__(self, input_dir,output_dir):
            super(multipleThread, self).__init__()
            self.input_dir=input_dir
            self.output_dir=output_dir

        def run(self):
            image_files = [f for f in os.listdir(self.input_dir) if
                           os.path.isfile(os.path.join(self.input_dir, f)) and f.endswith('.png')]
            print(image_files)
            for file_name in image_files:
                finalPath=os.path.join(self.input_dir, file_name)
                img = color.convertchannel(
                    np.array(cv2.imdecode(np.fromfile(finalPath, dtype=np.uint8), -1)))
                result = color.convertchannel(img)
                result_gray = cv2.cvtColor(result, cv2.COLOR_BGR2GRAY)
                result = cv2.applyColorMap(result_gray, cv2.COLORMAP_OCEAN)

                cv2.imencode('*.png *.jpg *.bmp', result)[1].tofile(self.output_dir+'/'+file_name)

            print("完成了！！")

class textThread(QThread):

    def __init__(self, input_dir):
        super(textThread, self).__init__()
        self.input_dir = input_dir

    def run(self):
        print("子线程开始工作")
        print(self.input_dir)
        reader = easyocr.Reader(['ch_sim', 'en'])
        result = reader.readtext(self.input_dir, detail=0)
        article = ''  # 定义一个空的字符串
        for i in range(len(result)):
            article += result[i]  # 将列表中的字符串依次拼接在一起
        print(article)
        with open('text.txt', 'w', encoding='UTF-8') as file:
            file.write(article)