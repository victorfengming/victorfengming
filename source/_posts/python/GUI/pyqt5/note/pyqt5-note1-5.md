---
title: "PyQt5学习笔记1-5"
date:       2019-10-31
tags:
	- Python
	- solution
	- basis
	- PyQt5
---





* content
{:toc}







# PyQt5的第一课-环境的准备
一个牛人的博客->[编程创造城市](http://bcczcs.com/blog/)

学什么Java,Python它不香么?

pyqt5,我来了

学习pyqt5中遇到的问题汇总

[python3.6：DLL load failed:找不到指定的模块（from PyQt5 import QtCore）](https://blog.csdn.net/proplume/article/details/88145115)


### 环境的准备

anaconda3+pycharm+pyqt5

这个方式没准备好

所以我用的组合是

UIC用python3.7的,qtdesigner用的是anaconda3中的

清华大学开源镜像站,这个贼JB快(https://pypi.tuna.tsinghua.edu.cn/simple/)

国内清华的镜像安装pyqt5
```cmd
pip install pyqt5 -i https://pypi.tuna.tsinghua.edu.cn/simple
```
国内清华的镜像安装pyqt5-tools
```cmd
pip install pyqt5-tools -i https://pypi.tuna.tsinghua.edu.cn/simple
```
安装完成之后需要在pycharm中配置两个扩展工具
### QTdesigner
- name:QTdesigner
- Program:`
E:\Python37\Lib\site-packages\pyqt5_tools\Qt\bin\designer.exe
`
- Working directory:`$FileDir$`

### PyUIC
- name:PyUIC
- Program:`
E:\Python37\python.exe
`
- Arguments:`-m PyQt5.uic.pyuic $FileName$ -o $FileNameWithoutExtension$.py`
- Working directory:`$FileDir$`


# PyQt5的第二课-hellopyqt5

### 使用QtWidgets写第一个程序,基于pyqt5

- 使用纯代码写第一个PyQt5程序

```python
import sys
from PyQt5.QtWidgets import  QApplication, QWidget

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = QWidget()
    w.resize(400,300)
    w.move(200,300)
    w.setWindowTitle("刘金玉编程")
    w.show()
    sys.exit(app.exec())
```


# PyQt5的第三课 - pyqt5与qtdesigner对照分析

### 空的程序的生成的样子
```python
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'first.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(500, 300)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
```      
 
```python
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by 秋叶夏风

# 本模块的功能:<pyqt5主模块>


# 导入python系统类库
import sys

# 导入pyqt5类用到的类库,QApplication应用程序类,Qwidget控件的基类
from PyQt5.QtWidgets import QApplication,QWidget

# 导入生成界面类的模块
import first

# 这回不写main了
# 直接就实例化一个类,通过构造函数传入一个python的应用参数
print(sys.argv) # 这里打印出包含当前文件绝对路径名称的列表
# sys.argv就是自己的文件名称的列表
app = QApplication(sys.argv)

# 实例化界面基类
w = QWidget()

# 实例化生成的界面的类
form = first.Ui_Form()
# 将生成的窗体控件及配置载入到w控件对象汇总
form.setupUi(w)
# 使用窗体显示
w.show()
# app.exec_()表示程序界面监听事件的开始,是一个死循环
# 这里说白了是一个死循环,就像tkinter中的loop一样
sys.exit(app.exec_())
```
### QT Designer 设计师界面
#####  Geometry属性
- X:代表窗体出现的位置是在屏幕的左上角水平方向0的位置
- Y:代表窗体出现的位置是在屏幕的左上角垂直方向0的位置
- 宽度:窗体宽度(单位像素)
- 高度:窗体高度(单位像素)

#####  ObjectName属性
表示窗体对象的名称,对应到python代码中设置窗体名称的方法
setObjectName
- 窗体对象其实就是指QtWidgets的实例化对象

### 补充PyUIC命令解析
- 使用python.exe解释器
- -mPyQt5.uic.pyuic $FileName$ -o $FileNameWithoutExtension$.py

- 说明: -m表示调用某个模块,这里表示调用PyQt5.uic.pyuic模块
-  $FileName$ 表示需要转换的源文件名称
- o 表示需要生成目标文件,这里使用$FileNameWithoutExtension$表示与源文件相同的文件名称,但是不包含扩展名的目标文件,扩展名,我们通过自己连接.py,最终表示生成的python类型的文件

### Resize函数
- 作用:重新调整大小
- 有两个参数,第一个参数表示宽度值,第二个参数表示高度值
- 举例:form.resize(300,400)

### Move函数
- 作用:调整窗体的位置
- 第一个参数表示水平方向的位置
- 第二个参数表示垂直方向的位置

### Qt中信号的理解(说白了就像js中的事件)

比如说单击事件,某个超时信号等都是qt中的信号,说到底其实就是界面上面发生了某个事件

### 绝对路径
- 绝对路径:从根目录开始的路径
- 相对路径:相对于某个文件目录的路径
- 相对路径往往有一些符号代表:
.点表示当前路径
.. 表示上一层路径
../../上一层的上一层


### show函数
- pyqt5中的show函数的将窗体显示出来

### 总结
-  掌握qtdesigner设计界面与pyuic转换后文件代码的对应关系

-  掌握pyqt5中界面中常用函数的基本用法

-  掌握如何调用生成界面的思想.实则是如何使用pyqt5纯代码写GUI界面的关键.
  

# PyQt5的第四课 - pyqt5设置窗体图标

在pyqt5之前,有pyqt1234不同的版本,我们直接学习pyqt5就行了

pyqt4和pyqt5不互相兼容

现在pyqt4已经放弃开发了

### 知识回顾
1. 纯pyqt5代码来创建窗体程序
2. 掌握理解GUI窗体的开发原理

### python的纯代码编写GUI
最简单代码
```python
import sys
from PyQt5.QtWidgets import QApplication,QWidget
app = QApplication(sys.argv)
w = QWidget()
w.show()
app.exec_()
```

### pyqt5设置窗体图标
- 使用函数setWindowIcon函数
- 设置图标需要类库的导入from PyQt5.QtGui import Qicon
- 将Qicon类利用构造函数进行初始化

### 图标到哪里下载?
- 阿里巴巴图标库
- https://www.iconfont.cn
- 注意:下载图标尽量采用png或者gif格式,可以背景透明
- 在项目中,我们往往会把所有的图标放到同一个文件夹中,然后通过相同路径进行调用.

### QWidget中设置图标与QApplication中设置图标的区别
- 通过QWidget设置出来的窗体的图标,可以是每个窗体一个图标.
- 通过QApplication的`setWindowIcon(QIcon("./img/水枪.png"))`
设置所有的窗体的默认图标

- 注意:在mac系统中只能识别QApplication中设置的图标

### 总结强调
- 1.掌握基本的pyqt5纯代码编写GUI
- 2.设置窗体的图标
- 3.理解QApplication和QWidget设置图标的哟啥不一样的地方

  
# PyQt5的第五课 - pyqt5显示提示框

### 知识回顾
-  利用pyqt5纯代码编写第一个程序
-  掌握了程序图标的设置方法

### 最基本的pyqt5代码
```python
import sys
from PyQt5.QtWidgets import QApplication,QWidget

app = QApplication(sys.argv)
w = QWidget()
w.show()
app.exec_()
```


### 显示提示框
- 使用函数setToolTip
注意:基本上所有的控件,包括窗体都有setToolTip这个函数,这个函数基本上都有

使用格式:
    控件对象setToolTip(这里是需要提示的字符串)

### 按钮控件
- 使用类QPushButton
- 基本使用:实例化一个按钮举例
```
# 按钮
btn = QPushButton("老刘",w)
```
- 格式:
- 声明定义一个实例化对象 的名称 = QPushButton(按钮文字,父容器)

### 系统中文件查找技巧
- 我们可以搜索包含`*ToolTip*`这个关键字的文件,直接搜索,搜不到,在两边加上`*`就能进行模糊搜索

### 如何找到类
-  我们可以通过pycharm上面代码右键找到对应的pyqt5的文件安装所在位置

-  利用模糊查找到我们需要的类所在的pyqt5中的位置

-  到程序中导入找到的类

### 显示框文字样式设置
-  需要导入QToolTip类库

-  通过QToolTip的setFont方法设置文字样式

-  需要导入Qfont类库

-  实例化QFont类进行文字样式设置

-  这个显示设置,是在全局样式上面显示提示效果的,说白了就是先显示后设置也好使

### 总结强调
-  掌握基础pyqt5代码GUI编写

-  掌握显示框设置setToolTip函数

-  掌握显示框文字样式设置

-  掌握代码编写思路



