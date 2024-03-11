from PIL import Image
from PyQt5.QtGui import QPolygonF

from myThread import *
from qt_material import apply_stylesheet
from pylab import *
from dialog.colorDialog import *
from tools import color, camera, basic,threshold
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
from cache import cache

matplotlib.use("Qt5Agg")


# 图像上显示中文
mpl.rcParams['font.sans-serif'] = ['SimHei']


class win(QMainWindow, Ui_MainWindow):
    def __init__(self):
        # 初始化
        super().__init__()
        self.old_hook = sys.excepthook
        sys.excepthook = self.catch_exceptions

        self.setWindowTitle('图像处理')
        self.setupUi(self)
        self.progressBar = ProgressBar()
        self.statusBar.addPermanentWidget(self.progressBar)
        self.root_dir = os.path.abspath(__file__)[:-7]
        # print(self.root_dir)
        if not os.path.exists(os.path.join(self.root_dir, 'cache')):
            os.makedirs(os.path.join(self.root_dir, 'cache'))
        self.cache = cache(os.path.join(self.root_dir, 'cache'))

        # 全局变量
        self.isopen = False
        if self.cache.empty():
            self.origin = np.array([])
            self.result = np.array([])
        else:
            origin_name = os.path.join(
                self.root_dir, 'cache', self.cache.filelist[0])
            self.origin = np.array(cv2.imdecode(
                np.fromfile(origin_name, dtype=np.uint8), -1))
            self.origin_flash()
            result_name = os.path.join(
                self.root_dir, 'cache', self.cache.filelist[-1])
            self.result = np.array(cv2.imdecode(
                np.fromfile(result_name, dtype=np.uint8), -1))
            self.result_flash()
            self.isopen = True
            self.clear_cache()
        self.imgList = []
        self.haveSaved = True

        self.x_start = None
        self.y_start = None
        self.x_end = None
        self.y_end = None

        self._polygon = None
        self.fileName=None

    def closeEvent(self, event):
        reply1 = QMessageBox.question(
            self, '提示', '确认要退出吗？', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply1 == QMessageBox.Yes:
            if(self.haveSaved == False):
                reply2 = QMessageBox.question(
                    self, '提示', '最新的图片还未保存，确定要退出吗？', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
                if reply2 == QMessageBox.Yes:
                    self.store_cache()
                    event.accept()
                else:
                    event.ignore()
            else:
                event.accept()
        else:
            event.ignore()

    # 测试强化版重置
    def one_step_back(self):
        if len(self.result) == 0:
            return
        #self.result = self.origin
        _ = self.imgList.pop()
        img = self.imgList[-1]
        print("获取成功")
        print(len(self.imgList))
        self.result = img
        self.result_flash()

    def Select(self):
        if self.isopen:
            self.start("绘制矩形")

            # self.result_img_graphicsView.scene.setImage(self.result)
            self.result_img_graphicsView.scene.paint_graph_init(Draw.rect)

            self.result_img_graphicsView.scene.finished.connect(
                self.getCoordinate)

            self.end()
        else:
            QMessageBox(QMessageBox.Warning, '意外输入', '没有打开任何图片！').exec_()

    def SelectArbitrary(self):
        if self.isopen:
            self.start("绘制任意区域")

            # self.result_img_graphicsView.scene.setImage(self.result)
            self.result_img_graphicsView.scene.paint_graph_init(Draw.rect)

            self.result_img_graphicsView.scene.finishedArbitrary.connect(
                self.getPoints)

            self.end()
        else:
            QMessageBox(QMessageBox.Warning, '意外输入', '没有打开任何图片！').exec_()


    def unSelect(self):
        if self.isopen:
            self.x_start = None
            self.y_start = None
            self.x_end = None
            self.y_end = None

            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Information)
            msg_box.setWindowTitle("提示")
            msg_box.setText("取消划定区域成功！")
            msg_box.setStandardButtons(QMessageBox.Ok)
            msg_box.exec_()
        else:
            QMessageBox(QMessageBox.Warning, '意外输入', '没有打开任何图片！').exec_()

    def getCoordinate(self, x_start, y_start, x_end, y_end):

        print("接收成功")
        print(x_start, y_start, x_end, y_end)
        self.x_start = x_start
        self.y_start = y_start
        self.x_end = x_end
        self.y_end = y_end

        self.result_img_graphicsView.scene.finished.disconnect()

        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Information)
        msg_box.setWindowTitle("提示")
        msg_box.setText("划定矩形区域成功！")
        msg_box.setStandardButtons(QMessageBox.Ok)
        msg_box.exec_()

    def getPoints(self, points):
        self._polygon = points
        self.result_img_graphicsView.scene.finishedArbitrary.disconnect()
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Information)
        msg_box.setWindowTitle("提示")
        msg_box.setText("划定任意区域成功！")
        msg_box.setStandardButtons(QMessageBox.Ok)
        msg_box.exec_()
        print("点集合接收成功！")



    def result_reset_clicked(self):
        if len(self.result) == 0:
            return
        self.result = self.origin
        self.imgList.append(self.result)
        self.result_flash()

    # 刷新图像
    def result_flash(self):
        self.result_img_graphicsView.set_img(self.result)
        self.haveSaved = False

    def origin_flash(self):
        self.origin_img_graphicsView.set_img(self.origin)

    # 文件操作action
    def store_cache(self):
        self.cache.in_cache(self.origin)
        for i in range(len(self.imgList)):
            img = self.imgList[i]
            print(img.shape)
            self.cache.in_cache(img)

    def clear_cache(self):
        while not self.cache.empty():
            self.cache.pop_cache()

    def save_img(self):
        result = self.result
        if len(result):
            filepath, _ = QFileDialog.getSaveFileName(
                self, "保存处理结果", "/", '*.png *.jpg *.bmp')
            if filepath:
                print(filepath)
                cv2.imencode('*.png *.jpg *.bmp', result)[1].tofile(filepath)
            self.haveSaved = True
            self.clear_cache()

    def open_img(self):
        self.start("打开")
        fileName, _ = QFileDialog.getOpenFileName(
            self, '打开图像', '', '*.png *.jpg *.bmp')
        if fileName:
            self.fileName=fileName
            self.origin = self.result = color.convertchannel(
                np.array(cv2.imdecode(np.fromfile(fileName, dtype=np.uint8), -1)))
            self.origin_img_graphicsView.set_img(self.origin)
            self.result_img_graphicsView.set_img(self.origin)
            self.imgList.append(self.result)
            print(len(self.imgList))
            self.cache.set_type(fileName[-4:])
            self.isopen = True
        else:
            self.isopen = False
        self.end()
        return

    def processing(self, method):
        self.start("处理中")
        # 图像不为空
        if len(self.result):
            self.result = method(self.result.copy())
            self.result_flash()
        self.end()

    def thread_filter(self, method, isFilter=1):
        if len(self.result):
            if(isFilter):  # filter
                size, ok = QInputDialog.getInt(
                    self, '设置参数', '模糊程度', 3, 3, 11, 2)
                if size % 2 == 0:
                    size += 1
                if ok and size >= 3:
                    self.start("图像处理中...")
                    self.filter_thread = FilterThread(
                        method, self.result, size, self.x_start, self.y_start, self.x_end, self.y_end)
                    self.filter_thread.finished.connect(self.getResult)
                    self.filter_thread.finished.connect(self.signalEnd)
                    self.filter_thread.start()
                elif ok:
                    QMessageBox(QMessageBox.Warning, '意外输入',
                                '参数不合法！参数应该 >=3 ').exec_()

            if(not isFilter):  # Rotate
                rotate, ok = QInputDialog.getInt(self, '设置参数', '旋转角度', 0)
                rotate = rotate % 360
                if ok:
                    self.start("图像处理中...")
                    self.filter_thread = FilterThread(
                        method, self.result, rotate, self.x_start, self.y_start, self.x_end, self.y_end)
                    self.filter_thread.finished.connect(self.getResult)
                    self.filter_thread.finished.connect(self.signalEnd)
                    self.filter_thread.start()
                elif ok:
                    QMessageBox(QMessageBox.Warning, '意外输入',
                                '参数不合法！参数应该 >=3 ').exec_()
        else:
            QMessageBox(QMessageBox.Warning, '意外输入', '没有打开任何图片！').exec_()

    def thread_color(self, method):
        if not self.isopen:
            QMessageBox(QMessageBox.Warning, '意外输入', '没有打开任何图片！').exec_()
        while(True):
            if len(self.result):
                dialog = colorDialog(self)
                if dialog.exec_() == QDialog.Accepted:
                    r, g, b = dialog.get_params()
                    print(r, g, b)

                if 0 <= r <= 200 and 0 <= g <= 200 and 0 <= b <= 200:
                    self.start("图像处理中...")

                    self.color_thread = colorThread(
                        method, self.result, r, g, b, self.x_start, self.y_start, self.x_end, self.y_end)
                    self.color_thread.finished.connect(self.getResult)
                    self.color_thread.finished.connect(self.signalEnd)
                    self.color_thread.start()
                    break
                else:
                    QMessageBox(QMessageBox.Warning, '意外输入',
                                'rgb的值不在可取范围内！请重新输入').exec_()

    def thread_camera(self, method):
        if not self.isopen:
            QMessageBox(QMessageBox.Warning, '意外输入', '没有打开任何图片！').exec_()
        while(True):
            if len(self.result):
                self.camera_thread = cameraThread(
                    method, self.result, self.x_start, self.y_start, self.x_end, self.y_end,self._polygon)
                self.camera_thread.finished.connect(self.getResult)
                self.camera_thread.finished.connect(self.signalEnd)
                self.camera_thread.start()
                break

    def thread_threshold(self,method):
        if not self.isopen:
            QMessageBox(QMessageBox.Warning, '意外输入', '没有打开任何图片！').exec_()
        while(True):
            if len(self.result):
                # print(self.result.shape)
                threshold, ok = QInputDialog.getInt(self, '阈值', '输入阈值(0-255)', 127, 0, 255, 1)
                self.threshold_thread = thresholdThread(
                    method, self.result, threshold,self.x_start, self.y_start, self.x_end, self.y_end,self._polygon)
                self.threshold_thread.finished.connect(self.getResult)
                self.threshold_thread.finished.connect(self.signalEnd)
                self.threshold_thread.start()
                break


    def getResult(self, result):
        self.imgList.append(result)
        print(len(self.imgList))
        self.result = result
        self.result_flash()

    def signalEnd(self, result):
        self.end("处理完成")

    # 定义滤波函数

    def Binary(self):
        if self.isopen:
            self.thread_filter(filters.binary_filter)
        else:
            QMessageBox(QMessageBox.Warning, '意外输入', '没有打开任何图片！').exec_()

    def Max(self):
        if self.isopen:
            self.thread_filter(filters.max_filter)
        else:
            QMessageBox(QMessageBox.Warning, '意外输入', '没有打开任何图片！').exec_()

    def Min(self):
        if self.isopen:
            self.thread_filter(filters.min_filter)
        else:
            QMessageBox(QMessageBox.Warning, '意外输入', '没有打开任何图片！').exec_()

    def Middle(self):
        if self.isopen:
            self.thread_filter(filters.middle_filter)
        else:
            QMessageBox(QMessageBox.Warning, '意外输入', '没有打开任何图片！').exec_()

    def Color(self):
        if self.isopen:
            self.thread_color(color.change_color_all)
        else:
            QMessageBox(QMessageBox.Warning, '意外输入', '没有打开任何图片！').exec_()

    def Contrast1(self):
        if self.isopen:
            self.thread_color(color.add_contrast1)
        else:
            QMessageBox(QMessageBox.Warning, '意外输入', '没有打开任何图片！').exec_()

    def Contrast2(self):
        if self.isopen:
            self.thread_color(color.add_contrast2)
        else:
            QMessageBox(QMessageBox.Warning, '意外输入', '没有打开任何图片！').exec_()

    def Contrast3(self):
        if self.isopen:
            self.thread_color(color.add_contrast3)
        else:
            QMessageBox(QMessageBox.Warning, '意外输入', '没有打开任何图片！').exec_()

    def Autumn(self):
        if self.isopen:
            self.thread_camera(camera.autumn)
        else:
            QMessageBox(QMessageBox.Warning, '意外输入', '没有打开任何图片！').exec_()

    def Bone(self):
        if self.isopen:
            self.thread_camera(camera.bone)
        else:
            QMessageBox(QMessageBox.Warning, '意外输入', '没有打开任何图片！').exec_()

    def Jet(self):
        if self.isopen:
            self.thread_camera(camera.jet)
        else:
            QMessageBox(QMessageBox.Warning, '意外输入', '没有打开任何图片！').exec_()

    def Winter(self):
        if self.isopen:
            self.thread_camera(camera.winter)
        else:
            QMessageBox(QMessageBox.Warning, '意外输入', '没有打开任何图片！').exec_()

    def Rainbow(self):
        if self.isopen:
            self.thread_camera(camera.rainbow)
        else:
            QMessageBox(QMessageBox.Warning, '意外输入', '没有打开任何图片！').exec_()

    def Ocean(self):
        if self.isopen:
            self.thread_camera(camera.ocean)
        else:
            QMessageBox(QMessageBox.Warning, '意外输入', '没有打开任何图片！').exec_()

    def Summer(self):
        if self.isopen:
            self.thread_camera(camera.summer)
        else:
            QMessageBox(QMessageBox.Warning, '意外输入', '没有打开任何图片！').exec_()

    def Spring(self):
        if self.isopen:
            self.thread_camera(camera.spring)
        else:
            QMessageBox(QMessageBox.Warning, '意外输入', '没有打开任何图片！').exec_()

    def Cool(self):
        if self.isopen:
            self.thread_camera(camera.cool)
        else:
            QMessageBox(QMessageBox.Warning, '意外输入', '没有打开任何图片！').exec_()

    def Hsv(self):
        if self.isopen:
            self.thread_camera(camera.hsv)
        else:
            QMessageBox(QMessageBox.Warning, '意外输入', '没有打开任何图片！').exec_()

    def Pink(self):
        if self.isopen:
            self.thread_camera(camera.pink)
        else:
            QMessageBox(QMessageBox.Warning, '意外输入', '没有打开任何图片！').exec_()

    def Hot(self):
        if self.isopen:
            self.thread_camera(camera.hot)
        else:
            QMessageBox(QMessageBox.Warning, '意外输入', '没有打开任何图片！').exec_()

    def Gray(self):
        if self.isopen:
            self.thread_camera(camera.gray)
        else:
            QMessageBox(QMessageBox.Warning, '意外输入', '没有打开任何图片！').exec_()

    def Sketch(self):
        if self.isopen:
            self.thread_camera(camera.sketch)
        else:
            QMessageBox(QMessageBox.Warning, '意外输入', '没有打开任何图片！').exec_()

    def Cartoon(self):
        if self.isopen:
            self.thread_camera(camera.cartoon)
        else:
            QMessageBox(QMessageBox.Warning, '意外输入', '没有打开任何图片！').exec_()

    def Reverse(self):
        if self.isopen:
            self.thread_camera(basic.img_horizontal_reverse)
        else:
            QMessageBox(QMessageBox.Warning, '意外输入', '没有打开任何图片！').exec_()

    def Crop(self):
        if self.isopen:
            self.thread_camera(basic.Crop)
        else:
            QMessageBox(QMessageBox.Warning, '意外输入', '没有打开任何图片！').exec_()

    def Rotate(self):  # need a param rotate
        if self.isopen:
            self.thread_filter(basic.Rotate, 0)
        else:
            QMessageBox(QMessageBox.Warning, '意外输入', '没有打开任何图片！').exec_()

    #阈值函数
    def threshold(self):
        if self.isopen:
            self.thread_threshold(threshold.Threshold)
        else:
            QMessageBox(QMessageBox.Warning, '意外输入', '没有打开任何图片！').exec_()

    #批量处理
    def multiple1(self):

        input_dir=  QFileDialog.getExistingDirectory(self,
                  "选取文件夹",
                  "./")
        print(input_dir)
        output_dir= QFileDialog.getExistingDirectory(self, '选择保存文件夹', './')
        print(output_dir)

        self.multiple_thread = multipleThread(input_dir, output_dir)

        self.multiple_thread.start()
    #文字提取
    def text(self):
        if self.isopen:
            self.text_thread=textThread(self.fileName)
            self.text_thread.start()
        else:
            QMessageBox(QMessageBox.Warning, '意外输入', '没有打开任何图片！').exec_()

        

    # 功能函数

    def catch_exceptions(self, ty, value, traceback):

        QMessageBox(QMessageBox.Critical, 'error', 'sorry,there is an error. please check the code\n'
                    + 'we have return to the latest state').exec_()
        self.end("Error")
        self.old_hook(ty, value, traceback)

    def start(self, msg="excuting"):
        self.progressBar.reset()
        self.statusBar.showMessage(msg)
        self.progressBar.busy()

    def end(self, msg="complete"):
        self.progressBar.done()
        self.statusBar.showMessage(msg)


class ProgressBar(QProgressBar):
    def __init__(self, parent=None, step=8):
        super().__init__(parent)
        self.step = step
        self.setRange(0, step)  # 设置进度条的范围

    def done(self):
        self.setMaximum(self.step)
        self.setValue(self.step)

    def busy(self):
        self.setMaximum(0)
        self.setMinimum(0)

# 添加单个组件的QSS样式


class QSSLoader:
    def __init__(self):
        pass

    @staticmethod
    def read_qss_file(qss_file_name):
        with open(qss_file_name, 'r',  encoding='UTF-8') as file:
            return file.read()


if __name__ == '__main__':
    a = QtWidgets.QApplication(sys.argv)
    window = win()

    # 添加qss主题样式
    apply_stylesheet(a, theme='dark_amber.xml', invert_secondary=True)

    window.show()
    sys.exit(a.exec_())
