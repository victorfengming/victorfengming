---
title: "PyQt5案例汇总(简洁版)"
date:       2019-10-31
tags:
	- Python
	- solution
	- basis
	- PyQt5
	- summer
---













### 01菜单栏
```python
import sys
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication
from PyQt5.QtGui import QIcon


class Example(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        exitAct = QAction(QIcon('exit.png'), '&Exit', self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.setStatusTip('Exit application')
        exitAct.triggered.connect(qApp.quit)

        self.statusBar()

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAct)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Simple menu')
        self.show()


app = QApplication(sys.argv)
ex = Example()
sys.exit(app.exec_())
```

### 02菜单栏++
```python
import sys
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QAction
from PyQt5.QtWidgets import qApp
from PyQt5.QtWidgets import QApplication

from PyQt5.QtGui import QIcon


class Demo(QMainWindow):

    def __init__(self):
        # 重新执行父类的初始化方法(默认的一些操作)
        super().__init__()
        # 加入自定义方法
        self.initUI()

    def initUI(self):
        # 设置菜单的图标
        exitAct = QAction(QIcon('exit.png'),'&Exit', self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.setStatusTip('Exit application')
        exitAct.triggered.connect(qApp.quit)

        self.statusBar()

        menubar = self.menuBar()
        file_menu = menubar.addMenu('&File')
        file_menu.addAction(exitAct)

        self.setGeometry(300,300,300,300)
        self.setWindowTitle('简单的菜单')
        self.show()

app = QApplication(sys.argv)
ex = Demo()
app.exec()

```
### 03简单的窗口(细致分析)
```python
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by xiaoming

# 本模块的功能:<>

# 这个简单的小例子展示的是一个小窗口。但是我们可以在这个小窗口上面做很多事情，改变大小，最大化，最小化等，这需要很多代码才能实现。这在很多应用中很常见，没必要每次都要重写这部分代码，Qt已经提供了这些功能。PyQt5是一个高级的工具集合，相比使用低级的工具，能省略上百行代码。


# 导入一些需要的模块
import sys
# 这里面引入了qtwidgets模块,其中包含了基本的用户界面控件
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QWidget

# 创建app对象
app = QApplication(sys.argv)
# 每个pyqt5应用都必须创建一个应用对象
# sys.argv是一组命令行参数的列表
# python可以在shell里运行,这个参数提供对脚本控制的功能
w = QWidget()
# qwidget是用户控件中的基本控件,提供了基本的应用构造器
# 默认情况下,构造器没有父级,没有父级的构造器称为窗口(window)
w.resize(250,450)
# resize这个方法能够改变控件的大小,这里的意思的窗口宽250px,高450px
w.move(300,200)
# move()是修改控件位置的方法.他把控件放置到屏幕坐标的(300,200位置)
# 注:屏幕坐标的原点是屏幕的左上角
w.setWindowTitle('我的第一个窗口')
# 这里给这个窗口添加了一个标题,标题在标题栏展示
# 虽然看起来是废话,但是以后回学习到各种栏,还是要注意一下,多了就懵逼了
w.show()
# show()能让控件在桌面上显示出来.控件在内存中创建,之后才能在显示器上显示出来
sys.exit(app.exec())
# 最后,我们进入了应用的主循环中,事件处理器这个时候开始工作.
# 主循环从窗口上接收事件,并把事件传入到派发到应用控件里.
# 当调用exit()方法或者直接销毁主控件时,主循环就会结束
# sys.exit()方法能确保主循环安全退出.外部环境能通知主控件怎么结束

# exec_()之所以有个下划线,是因为exec是一个python的关键字


```
### 04带窗口图标
```python

# 首先还是要导入对应的模块
import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QIcon


# 之前的例子是过程式编程,python当然支持面向对象编程
# 创建一个类
class Test(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()  # 使用initUI方法创建了一个GUI

    '''
    面向对象编程最重要的三个部分是类(class),数据和方法.
    我们创建了一个类的调用,这个类继承自QWidget.
    这个就意味着,我们调用了两个构造器,一个是这个类本身的,一个是这个类继承的
    super()构造器方法返回父级的对象.__init()方法是构造器的一个方法.
    俗称初始化魔术方法
    '''

    def initUI(self):
        self.setGeometry(300, 200, 700, 400)
        self.setWindowTitle('标题起啥都行')
        self.setWindowIcon(QIcon('logo.png'))
        '''
        上面三个方法都是继承自QWidget类.
        setGeometry() 有两个作用: 把窗口放到屏幕上并且设置窗口大小.
                                参数分别代表屏幕坐标的x y 和窗口大小的长和宽
        setWindowTitle就是设置标题内容,不用多说
        也就是说这个方法是 resize()和move()的合体.
        最后一个方法就是添加图标,先创建一个QIcon对象,然后接受一个路径主辅材作为参数,显示图标
        '''
        self.show()


yingyong = QApplication(sys.argv)
ex1 = Test()
sys.exit(yingyong.exec_())

# 应用和示例的对象创立,主循环开始
```
### 05提示框
```python

# 导入模块
import sys

from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QToolTip
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QApplication

from PyQt5.QtGui import QFont


# 来直接来一个类
class Demo(QWidget):    #继承自QWidget

    # 初始化魔术方法直接上
    def __init__(self):
        # 父类的方法还原
        super().__init__()
        # 执行自己的方法
        self.initUI()
    def initUI(self):
        # 这个字体的话,系统中有的都行
        QToolTip.setFont(QFont('微软雅黑',15))
        # 这个 例子中,我们创建 了一个提示框
        self.setToolTip('不信了还<b>这是一个啥玩意</b>')
        # 这个高,实在是高
        # html中的标签也能应用样式
        # 强，实在是强
        btn = QPushButton('点我',self)
        # 这个静态方法设置了提示框的字体,我们使用了15px的微软雅黑的字体
        btn.setToolTip('君不见黄河之水<br>天上来')
        # 调用setTooltip()创建提示框可以使用富文本格式的内容
        btn.resize(btn.sizeHint())
        btn.move(50,70)

        self.setGeometry(200,150,800,450)
        self.setWindowTitle('标题就是没有标题')
        # 显示
        self.show()

app = QApplication(sys.argv)
ex1 = Demo()
sys.exit(app.exec_())

```


### 06关闭窗口
```python

# 本模块的功能:<>
'''
TODO 要做的可多了
'''
# 关闭一个窗口最直观的方式就是点击标题栏的那个×,这个例子里面
# print(我们展示的是如何用程序关闭一个窗口)
# print(这里我们将解除)到一点single和slots的知识
# 本例子使用的是QPushButton组件类
# QPushButton(string text,Qwidget parent = None)
# text参数是想要显示的按钮名称,parent参数是放在按钮上的组件
# 在我们的例子里面,这个参数是QWidget.应用中的组件都是一层一层(继承而来的)
# 在这个层里,大部分的组件都有自己的父级,没有父级的组件,是顶级的窗口

# 还是tmd要导入对应的包和模块
import sys

from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QApplication

from PyQt5.QtCore import QCoreApplication
# 程序需要QtCore对象

# 上来先来一个类
class Example(QWidget):

    # 初始化魔术方法
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        qbtn = QPushButton('退出就退出',self)
        # 创建一个继承自 QPushButton 的按钮.
        # 第一个参数是按钮的文本,第二个参数是按钮的父级组件
        # 这个例子中,父级组件就是我们创建的继承自QWidget 的 Example 类
        qbtn.clicked.connect(QCoreApplication.instance().quit)
        # 事件传递系统在PyQt5内建的single和slot机制里面.点击按钮之后,信号会被捕捉并给出既定的反应
        # QCoreApplication包含了事件的主循环,它能添加和删除所有的事件
        # instance()创建 了一个它的实例.
        # QCoreApplication是在QApplication里创建的
        # 点击事件和能终止进程并退出应用的quit函数绑定在了一起.
        # 在发送者和接受者之间建立了通讯,发送者就是按钮,接受者就是应用对象
        qbtn.move(50,50)

        self.setGeometry(300,200,250,150)
        self.setWindowTitle("退出按钮练习")
        # 显示
        self.show()

yingyong = QApplication(sys.argv)
ex1 = Example()
sys.exit(yingyong.exec_())
# 这里创建了一个点击之后就退出窗口的按钮

```


### 07消息盒子
```python

# 导入模块
import sys
from PyQt5.QtWidgets import  QWidget
from PyQt5.QtWidgets import  QMessageBox
from PyQt5.QtWidgets import  QApplication

# 创建一个类
class Example(QWidget):

    def __init__(self):
        super().__init__()
        # 执行自己的函数
        self.initUI()

    def initUI(self):
        self.setGeometry(300,200,250,150)
        self.setWindowTitle('消息盒子')
        self.show()

    def closeEvent(self, QCloseEvent):

        reply = QMessageBox.question(self, '消息啊哈!',"你确定你要退出了",QMessageBox.yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            QCloseEvent.accept()
        else:
            QCloseEvent.ignore()

app = QApplication(sys.argv)
demo = Example()
app.exec_()
```


### UI文件生成demo01模块（主窗口）
`test.py`代码如下:
```python
import sys
from PyQt5.QtWidgets import *
# 导入生成的 py模块
from demo01 import *
# 创建app
app = QApplication(sys.argv)
# 实例化主窗口对象
w = QMainWindow()
# 实例化并调用初始化方法
Ui_MainWindow().setupUi(w)
# 显示窗口
w.show()
sys.exit(app.exec_())
pass

```