# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUIs.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from view import View
from PyQt5 import QtCore, QtGui, QtWidgets
import Entity.actionEntity as Entity
from Entity.buttonEntity import MyButton


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1115, 669)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSizeConstraint(
            QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(7)
        self.verticalLayout.setObjectName("verticalLayout")

        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(
            13, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()

        self.verticalLayout_8.setContentsMargins(0, 0, 0, -1)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.origin_img_graphicsView = View(self.centralwidget)
        self.origin_img_graphicsView.setObjectName("origin_img_graphicsView")
        self.verticalLayout_8.addWidget(self.origin_img_graphicsView)

        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")

        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)

        self.verticalLayout_8.addLayout(self.horizontalLayout_3)
        self.horizontalLayout.addLayout(self.verticalLayout_8)
        spacerItem1 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.result_img_graphicsView = View(self.centralwidget)
        self.result_img_graphicsView.setObjectName("result_img_graphicsView")
        self.verticalLayout_9.addWidget(self.result_img_graphicsView)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_4.addWidget(self.pushButton)
        self.verticalLayout_9.addLayout(self.horizontalLayout_4)
        self.horizontalLayout.addLayout(self.verticalLayout_9)
        spacerItem2 = QtWidgets.QSpacerItem(
            13, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)

        # 创建元素
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1115, 26))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_basic = QtWidgets.QMenu(self.menubar)
        self.menu_basic.setObjectName("menu_basic")
        self.menu_filter = QtWidgets.QMenu(self.menubar)
        self.menu_filter.setObjectName("menu_filter")
        self.menu_color = QtWidgets.QMenu(self.menubar)
        self.menu_color.setObjectName("menu_color")
        self.menu_camera = QtWidgets.QMenu(self.menubar)
        self.menu_camera.setObjectName("menu_camera")
        self.menu_Select = QtWidgets.QMenu(self.menubar)
        self.menu_Select.setObjectName("menu_Select")
        self.menu_threshold=QtWidgets.QMenu(self.menubar)
        self.menu_threshold.setObjectName("menu_threshold")
        # self.menu_multiple = QtWidgets.QMenu(self.menubar)
        # self.menu_multiple.setObjectName("menu_multiple")
        self.menu_text = QtWidgets.QMenu(self.menubar)
        self.menu_text.setObjectName("menu_text")

        MainWindow.setMenuBar(self.menubar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.toolBar_2 = QtWidgets.QToolBar(MainWindow)
        self.toolBar_2.setObjectName("toolBar_2")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar_2)
        self.toolBar_3 = QtWidgets.QToolBar(MainWindow)
        self.toolBar_3.setObjectName("toolBar_3")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar_3)

        self.open = Entity.MyAction(
            MainWindow, "open", "打开", MainWindow.open_img).getEntity()
        self.save = Entity.MyAction(
            MainWindow, "save", "保存", MainWindow.save_img).getEntity()

        self.opening = QtWidgets.QAction(MainWindow)
        self.opening.setObjectName("opening")
        self.closing = QtWidgets.QAction(MainWindow)
        self.closing.setObjectName("closing")

        # 定义动作选项
        # 滤波
        self.binary = Entity.MyAction(
            MainWindow, "binary", "留边去噪", MainWindow.Binary).getEntity()
        self.max = Entity.MyAction(
            MainWindow, "max", "去除椒噪声", MainWindow.Max).getEntity()
        self.min = Entity.MyAction(
            MainWindow, "min", "去除盐噪声", MainWindow.Min).getEntity()
        self.middle = Entity.MyAction(
            MainWindow, "middle", "一般去噪", MainWindow.Middle).getEntity()

        # 颜色
        self.color = Entity.MyAction(
            MainWindow, "color", "调色", MainWindow.Color).getEntity()
        self.contrast1 = Entity.MyAction(
            MainWindow, "contrast1", "对比度1", MainWindow.Contrast1).getEntity()
        self.contrast2 = Entity.MyAction(
            MainWindow, "contrast2", "对比度2", MainWindow.Contrast2).getEntity()
        self.contrast3 = Entity.MyAction(
            MainWindow, "contrast3", "对比度3", MainWindow.Contrast3).getEntity()

        # 滤镜
        self.autumn = Entity.MyAction(
            MainWindow, "autumn", "autumn", MainWindow.Autumn).getEntity()
        self.bone = Entity.MyAction(
            MainWindow, "bone", "bone", MainWindow.Bone).getEntity()
        self.jet = Entity.MyAction(
            MainWindow, "jet", "jet", MainWindow.Jet).getEntity()
        self.winter = Entity.MyAction(
            MainWindow, "winter", "winter", MainWindow.Winter).getEntity()
        self.rainbow = Entity.MyAction(
            MainWindow, "rainbow", "rainbow", MainWindow.Rainbow).getEntity()
        self.ocean = Entity.MyAction(
            MainWindow, "ocean", "ocean", MainWindow.Ocean).getEntity()
        self.summer = Entity.MyAction(
            MainWindow, "summer", "summer", MainWindow.Summer).getEntity()
        self.spring = Entity.MyAction(
            MainWindow, "spring", "spring", MainWindow.Spring).getEntity()
        self.cool = Entity.MyAction(
            MainWindow, "cool", "cool", MainWindow.Cool).getEntity()
        self.hsv = Entity.MyAction(
            MainWindow, "hsv", "hsv", MainWindow.Hsv).getEntity()
        self.pink = Entity.MyAction(
            MainWindow, "pink", "pink", MainWindow.Pink).getEntity()
        self.hot = Entity.MyAction(
            MainWindow, "hot", "hot", MainWindow.Hot).getEntity()
        self.gray = Entity.MyAction(
            MainWindow, "gray", "gray", MainWindow.Gray).getEntity()
        self.sketch = Entity.MyAction(
            MainWindow, "sketch", "sketch", MainWindow.Sketch).getEntity()
        self.cartoon = Entity.MyAction(
            MainWindow, "cartoon", "cartoon", MainWindow.Cartoon).getEntity()

        # 基本操作：旋转、裁剪、翻转
        self.rotate = Entity.MyAction(
            MainWindow, "rotate", "旋转", MainWindow.Rotate).getEntity()
        self.crop = Entity.MyAction(
            MainWindow, "crop", "裁剪(需要先划定区域)", MainWindow.Crop).getEntity()
        self.reverse = Entity.MyAction(
            MainWindow, "reverse", "水平翻转", MainWindow.Reverse).getEntity()

        # 划定区域
        self.select = Entity.MyAction(
            MainWindow, "select", "划定矩形区域", MainWindow.Select).getEntity()

        # self.selectArbitrary = Entity.MyAction(
            # MainWindow, "selectArbitrary", "划定任意区域", MainWindow.SelectArbitrary).getEntity()

        # 取消划定
        self.unSelect = Entity.MyAction(
            MainWindow, "unSelect", "取消划定区域", MainWindow.unSelect).getEntity()


        #阈值操作
        self.threshold= Entity.MyAction(
            MainWindow, "threshold", "给定阈值分割", MainWindow.threshold).getEntity()

        #批量处理
        # self.multiple1=Entity.MyAction(
            # MainWindow,"multiple1","批量处理1",MainWindow.multiple1).getEntity()
        #文字提取
        self.text = Entity.MyAction(
            MainWindow, "text", "文字提取", MainWindow.text).getEntity()


        # 测试,只需要一行就能定义完所有功能
        # self.testAction1 = Entity.MyAction(MainWindow, "test", "niumomo",MainWindow.Binary).getEntity()
        # 返回上一步
        self.reset = MyButton(self.centralwidget, "reset2",
                              "LastStep", MainWindow.one_step_back).getEntity()
        self.horizontalLayout_4.addWidget(self.reset)

        # 为 按钮 绑定函数
        self.menu.addAction(self.open)
        self.menu.addAction(self.save)
        # 滤波
        self.menu_filter.addAction(self.binary)
        self.menu_filter.addAction(self.max)
        self.menu_filter.addAction(self.min)
        self.menu_filter.addAction(self.middle)
        # 颜色
        self.menu_color.addAction(self.color)
        self.menu_color.addAction(self.contrast1)
        self.menu_color.addAction(self.contrast2)
        self.menu_color.addAction(self.contrast3)
        # 滤镜
        self.menu_camera.addAction(self.autumn)
        self.menu_camera.addAction(self.bone)
        self.menu_camera.addAction(self.jet)
        self.menu_camera.addAction(self.winter)
        self.menu_camera.addAction(self.rainbow)
        self.menu_camera.addAction(self.ocean)
        self.menu_camera.addAction(self.summer)
        self.menu_camera.addAction(self.spring)
        self.menu_camera.addAction(self.cool)
        self.menu_camera.addAction(self.hsv)
        self.menu_camera.addAction(self.pink)
        self.menu_camera.addAction(self.hot)
        self.menu_camera.addAction(self.gray)
        self.menu_camera.addAction(self.sketch)
        self.menu_camera.addAction(self.cartoon)
        # 选择
        self.menu_Select.addAction(self.select)
        # self.menu_Select.addAction(self.selectArbitrary)
        self.menu_Select.addAction(self.unSelect)
        # 基本操作
        self.menu_basic.addAction(self.rotate)
        self.menu_basic.addAction(self.reverse)
        self.menu_basic.addAction(self.crop)

        #阈值操作
        self.menu_threshold.addAction(self.threshold)
        #批量处理
        # self.menu_multiple.addAction(self.multiple1)
        #文字提取
        self.menu_text.addAction(self.text)

        # 这里添加菜单
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_basic.menuAction())
        self.menubar.addAction(self.menu_filter.menuAction())
        self.menubar.addAction(self.menu_color.menuAction())
        self.menubar.addAction(self.menu_camera.menuAction())
        self.menubar.addAction(self.menu_Select.menuAction())
        self.menubar.addAction(self.menu_threshold.menuAction())
        # self.menubar.addAction(self.menu_multiple.menuAction())
        self.menubar.addAction(self.menu_text.menuAction())

        # 这里添加顶部工具栏。

        # self.toolBar.addAction(self.save)
        # self.toolBar.addSeparator()

        self.retranslateUi(MainWindow)

        self.pushButton.clicked.connect(MainWindow.result_reset_clicked)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "图像处理"))

        self.pushButton.setText(_translate("MainWindow", "重置(Reset)"))

        self.menu.setTitle(_translate("MainWindow", "文件(&F)"))
        self.menu_basic.setTitle(_translate("MainWindow", "基本操作(&B)"))
        self.menu_filter.setTitle(_translate("MainWindow", "去噪(&P)"))
        self.menu_color.setTitle(_translate("MainWindow", "颜色(&C)"))
        self.menu_camera.setTitle(_translate("MainWindow", "滤镜(&V)"))
        self.menu_Select.setTitle(_translate("MainWindow", "划定区域(&S)"))
        self.menu_threshold.setTitle(_translate("MainWindow", "阈值(&T)"))
        # self.menu_multiple.setTitle(_translate("MainWindow", "批量处理(&S)"))
        self.menu_text.setTitle(_translate("MainWindow", "中文文字提取(&W)"))


        # self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        # self.toolBar_2.setWindowTitle(_translate("MainWindow", "toolBar_2"))
        # self.toolBar_3.setWindowTitle(_translate("MainWindow", "toolBar_3"))

        # 打开、保存按钮
        # self.open.setText(_translate("MainWindow", "打开"))
        # self.save.setText(_translate("MainWindow", "保存"))

        # 测试action集成类
        # self.testAction1=Entity(MainWindow,"test","niumomo").getEntity()
