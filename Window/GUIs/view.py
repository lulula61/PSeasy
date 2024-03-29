import math
from enum import Enum
import numpy as np
import cv2

from PyQt5.QtCore import Qt, QLine, pyqtSignal
from PyQt5.QtGui import QImage, QPixmap, QColor, QPen, QPainter, QFont, QBrush, QPolygonF, QPainterPath

from PyQt5.QtWidgets import QGraphicsView, QGraphicsPixmapItem, QGraphicsScene,  QGraphicsLineItem, \
    QGraphicsRectItem, QGraphicsEllipseItem, QGraphicsSimpleTextItem, QColorDialog, QInputDialog


class View(QGraphicsView):

    def __init__(self, parent=None):
        super(View, self).__init__(parent)

        self.setRenderHints(QPainter.Antialiasing |  # anti-aliasing
                            QPainter.HighQualityAntialiasing |  # High quality anti-aliasing
                            QPainter.TextAntialiasing |  # Text anti-aliasing
                            QPainter.SmoothPixmapTransform)  # Make the primitive transformation smoother

        # 根据鼠标放大缩小图片
        self.setTransformationAnchor(QGraphicsView.AnchorUnderMouse)
        self.setResizeAnchor(QGraphicsView.AnchorUnderMouse)
        self.setDragMode(QGraphicsView.ScrollHandDrag)
        # 鼠标拖拽
        self.setDragMode(self.RubberBandDrag)
        self.scene = GraphicsScene(self)
        self.setScene(self.scene)

        #piant
        self.path = QPainterPath()
        self.pen = QPen(Qt.red, 2)

    def set_img(self, img):
        del self.scene
        if not type(img) is np.ndarray:
            self.scene = QGraphicsScene()
            self.scene.addWidget(img)
            self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
            self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        else:
            self.scene = GraphicsScene(self)
            img = img.astype(np.uint8)
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            rows, cols, channels = img.shape
            self.scene.setSceneRect(0, 0, cols, rows)
            bytesPerLine = channels * cols
            QImg = QImage(img, cols, rows, bytesPerLine, QImage.Format_RGB888)
            pix = QPixmap.fromImage(QImg)
            item = QGraphicsPixmapItem(pix)
            self.scene.addItem(item)
        self.setScene(self.scene)

    def wheelEvent(self, event):
       #鼠标滚轮事件
        zoomInFactor = 1.25
        zoomOutFactor = 1 / zoomInFactor

        if event.angleDelta().y() > 0:
            zoomFactor = zoomInFactor
        else:
            zoomFactor = zoomOutFactor

        self.scale(zoomFactor, zoomFactor)

    def keyPressEvent(self, event) -> None:
        if event.key() == Qt.Key_Control:
            self.setDragMode(self.ScrollHandDrag)

    def keyReleaseEvent(self, event) -> None:
        if event.key() == Qt.Key_Control:
            self.setDragMode(self.RubberBandDrag)



class GraphicsScene(QGraphicsScene):
    finished = pyqtSignal(float, float, float, float)
    finishedArbitrary=pyqtSignal(QPolygonF)
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent
        # 一些关于网格背景的设置
        self.line = None
        self.grid_size = 20  # 一块网格的大小 （正方形的）
        self.grid_squares = 1  # 网格中正方形的区域个数

        # 一些颜色
        self._color_background = QColor('#F5F0E9')
        self._color_light = QColor('#F7F7F7')
        self._color_dark = QColor('#E4E4E4')
        # 一些画笔
        self._pen_light = QPen(self._color_light)
        self._pen_light.setWidth(1)
        self._pen_dark = QPen(self._color_dark)
        self._pen_dark.setWidth(2)

        # 设置画背景的画笔
        self.setBackgroundBrush(self._color_background)
        self.setSceneRect(0, 0, 2000, 2000)

        # 控制变量
        self.clicked = False
        self.paint = False
        # 设置方法 绘制对象
        self.paint_type = None
        self.set_method = None
        self.paint_item = None
        # self.paint_graph_init(Draw.text)

        #尝试修改任意区域
        self._drawing = False
        self._polygon = QPolygonF()
        self._pen = QPen(QBrush(QColor(255, 0, 0, 255)), 1, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin)
        self._brush = QBrush(QColor(255, 0, 0, 50))



    def paint_graph_init(self, type_num):
        #color, size = self.getFont()
        color=QColor('#F7F7F7')
        size=5
        self.paint = True
        self.paint_type = type_num
        # "<class \'PyQt5.QtWidgets.QGraphicsLineItem\'>"
        if type_num == Draw.line:
            self.paint_item = QGraphicsLineItem()
            self.set_method = self.paint_item.setLine
            print(111)
        # "<class \'PyQt5.QtWidgets.QGraphicsRectItem\'>"
        elif type_num == Draw.rect:
            self.paint_item = QGraphicsRectItem()
            self.set_method = self.paint_item.setRect
            self.paint_item.setBrush(QBrush(color))
            print(222)
        # "<class \'PyQt5.QtWidgets.QGraphicsEllipseItem\'>"
        elif type_num == Draw.circle:
            self.paint_item = QGraphicsEllipseItem()
            self.set_method = self.paint_item.setRect
            self.paint_item.setBrush(QBrush(color))
            print(333)
        elif type_num == Draw.text:
            self.paint_item = QGraphicsSimpleTextItem()
            self.set_method = self.paint_item.setPos

            font = QFont()
            font.setPixelSize(size)
            self.paint_item.setFont(font)
            self.paint_item.setBrush(QBrush(color))
            text, ok = QInputDialog.getText(self.parent, '文本', '输入添加内容')
            if ok and text:
                self.paint_item.setText(text)
            else:
                self.paint_item.setText("")
            print(444)

    # override
    def mousePressEvent(self, event):
        if self.clicked:
            self.clicked = False
            self.paint = False
        if self.paint:
            self.clicked = True
            self.start_pos = event.scenePos()
            print(self.start_pos.x())
            self.addItem(self.paint_item)
            if self.paint_type == Draw.text:
                self.paint_item.setPos(self.start_pos)

            #任意

            self._polygon.append(event.scenePos())


    def mouseMoveEvent(self, event):
        if self.clicked:
            self.end_pos = event.scenePos()
            #print("self.end_pos=", self.end_pos)
            #任意
            self._polygon.append(event.scenePos())

            return

    def mouseReleaseEvent(self, event):
        self.clicked = False
        self.paint = False
        print(self.start_pos.x(), self.start_pos.y(), self.end_pos.x(), self.end_pos.y())
        self.finished.emit(self.start_pos.x(), self.start_pos.y(), self.end_pos.x(), self.end_pos.y())



        print("发送成功")
        #任意

        self._polygon.append(event.scenePos())

        self.finishedArbitrary.emit(self._polygon)

        print(self._polygon)


    def getFont(self):
        color = QColorDialog.getColor()
        size, ok = QInputDialog.getInt(self.parent, '大小', '输入希望添加元素的大小(pix)')
        if ok and size > 0:
            return color, size
        else:
            size = 20
            return color, size

    def drawBackground(self, painter, rect):
        super().drawBackground(painter, rect)

        # 获取背景矩形的上下左右的长度，分别向上或向下取整数
        left = int(math.floor(rect.left()))
        right = int(math.ceil(rect.right()))
        top = int(math.floor(rect.top()))
        bottom = int(math.ceil(rect.bottom()))

        # 从左边和上边开始
        first_left = left - (left % self.grid_size)  # 减去余数，保证可以被网格大小整除
        first_top = top - (top % self.grid_size)

        # 分别收集明、暗线
        lines_light, lines_dark = [], []
        for x in range(first_left, right, self.grid_size):
            if x % (self.grid_size * self.grid_squares) != 0:
                lines_light.append(QLine(x, top, x, bottom))
            else:
                lines_dark.append(QLine(x, top, x, bottom))

        for y in range(first_top, bottom, self.grid_size):
            if y % (self.grid_size * self.grid_squares) != 0:
                lines_light.append(QLine(left, y, right, y))
            else:
                lines_dark.append(QLine(left, y, right, y))

            # 最后把收集的明、暗线分别画出来
        painter.setPen(self._pen_light)
        if lines_light:
            painter.drawLines(*lines_light)

        painter.setPen(self._pen_dark)
        if lines_dark:
            painter.drawLines(*lines_dark)

        # painter.fillRect(rect, Qt.white)
        # painter.setPen(self._pen)
        # painter.setBrush(self._brush)
        #painter.drawPolygon(self._polygon)


class Draw(Enum):
    # 为序列值指定value值
    eraser = 0
    line = 1
    rect = 2
    circle = 3
    text = 4
    pen = 5
