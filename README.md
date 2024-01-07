# PSeasy
# PSeasy 2.0.2
在Window/GUIs文件下直接运行Ui_start.py文件即可

start_rc.py中保存了start界面使用的图像信息, 请不要随意修改

Ui_start.py文件中，通过self.open()调用GUI.py中的win()来实现界面跳转转

* 2023/4/8
将bfilter、min_filter等几个基本功能转化为用按钮类生成

在tools下增加color.py文件用于添加滤镜, 为了使用method的调用，class color被分解成了多个函数

为了更直观地区分滤波器和滤镜两个功能文件，将原来的tool_2改为filters.py

color目前在菜单栏中名字为调色，放在基本功能里，后期如果需要增加更多滤镜功能建议新开一个菜单栏

！！！注意：color.py中RGB通道值为默认值（2，1，1），根据输入来调整的功能还未实现

* 2023/4/13
增加了滤镜功能，滤镜保存在camera.py中，功能界面中所有滤镜在“滤镜”栏下
增加了划定区域操作（GUI.select)，可以在自定义区域内进行图片修改
增加了对比度(color.py中，contrast1（）、contrast2（）、contrast3（）)，功能界面中三种不同对比度在“颜色”栏下
* 2023/4/14
增加了文件缓存的功能，能够在未保存就关闭的情况下缓存图片并在下一次打开时读入。
* 2023/4/19
在tools里增加basic文件，包含3个基础操作：旋转，裁剪，水平翻转
将这3个功能加入了功能界面
修改的文件包括：tools.basic.py GUI.py mainWindow.py
* 2023/5/1
加入了阈值分割功能，选择 0-255 的值输入，生成阈值分割图像
加入了中文文字提取功能，输出到目录下的text.txt文件中
加入了基础旋转、对称、裁剪功能
