---
title: "PyQt5学习笔记16-20"
cover: "/img/lynk/39.jpg"
date:       2019-11-01
tags:
	- Python
	- solution
	- basis
	- PyQt5
---

  











# PyQt5的第十六课 - PyQt5载入图片QPixmap应用

### 知识回顾

- 进度条qprogressbar
- 学会使用时钟控件QBasicTimer
- 学会重写事件timerEvent

### 案例:图片的载入与移除
- 加入需要能够载入图片
- 增加移除图片按钮和添加图片按钮
- 当点击相应按钮后会有相应的功能

### 最终图片的显示载体QLabel
- 功能:
- 显示文字
- 显示图片,载入QPixmap
- 默认情况下,label显示区域,是根据图片的大小进行显示的
- 如果设置label大小的话,只会显示图片的部分裁剪区域
- 使用方法:`lbl.setPixmap(图片实例化对象)`
- `lbl.setPixmap(QPixmap("./img/th.jpg"))`
- 如和让图片自适应qlabel标签的区域呢?
### QPixmap类
- 所在类库QtGUI
- 导入
from PyQt5.QtGui import Qpixmap

- 实例化图片对象:
- QPixmap(图片路径) 返回一个实例化图片对象

### 总结强调
- 掌握QPixmap载入图片对象与移除
- 掌握通过QLabel来显示图片与自适应大小


  
# PyQt5的第十七课 - PyQt5下拉列表控件QComboBox
说白了就像以前那个js的地址联动似的
### 知识回顾

- 掌握QPixmap图片对象
- 掌握Qlabel控件装载图和调整图片

### 下拉列表 combobox
- 主要用于选择,比如省市联动选择
- 必须要载入Qcombobox类
- 实例化类为一个对象,对这个对象进行配置,实则就是对下拉列表的配置

```python
combox_1 = QComboBox(myframe1)
combox_1.move(20,0)
```        
- 我们通过addItem来往combobox中装入项目.
```python
combox_1.addItem("请选择省份")
combox_1.addItem("浙江")
combox_1.addItem("江苏")
combox_1.addItem("安徽")
combox_1.addItem("北京")
```
- 我们通过addItem来王combobox中装入项目

用到clear方法将所有项目进行清空


### Combobox点击事件
- 理解为激活actived信号.
- 信号有两种传递方式
- 第一种传递传递字符串,这个实则传递的是选择的文本
`combox_1.activated[str].connect(self.myActived)`
- 第二种:传递整型变量,这个传递的是选择的索引.索引默认从0开始
- 第一项的索引是0,第二项的索引是1,依次类推
- combo1.activated[int].connect(自定义槽方法)

### 案例省市联动选择
- 需要两个下拉列表
- 点击第一个下拉列表后,会联动第二个列表中的内容

### 扩展内容
下拉列表框也可以进行输入,但是需要对方法进行配置
配置setEditable为True:
combo1.setEditable(True)

### 总结强调
- 掌握qcombobox的载入布局与项目加载
- 掌握下拉列表的编辑和对应事件
- 掌握联动的思想

# PyQt5的第十八课 - PyQt5日历控件QCalendarWidget
### 知识回顾

- 掌握了QCombobox下拉框,载入,配置(可编辑,不可编辑)
- 掌握联动的思想(省与市的联动),主要
- 用到actived信号

### 案例描述:日历控件的使用
- 制造一个垂直布局(盒子模型)
- 载入一个日历控件Qcalendarwidget和一个qlabel控件
- 要求在点击日历控件的日期的时候,能够将获取到的日期显示到我们的label上

### 步骤
- 从库文件PyQt5.QtWidgets中导入日历控件
- 对日历控件进行实例化
- `cal = QCalendarWidget()`
- 这里实例化的时候没有载入父容器,我们需要在后期将其载入父容器

### 盒子模型

- 盒子模型,垂直布局
```python
vlo = QVBoxLayout(self)
vlo.addWidget(cal)
```

### 字体设置
- 导入字体类
- 对字体进行实例化,以及将实例化对象载入使用
`lbl.setFont(QFont("华文行楷",20))`

### 日期类型的载入
- 从pyqt5的核心库中载入日期类Qdate
- `from PyQt5.QtCore import QDate`
- 默认的有实例的日期显示格式
`PyQt5.QtCore.QDate(2019, 11, 15)`

### 对日期进行格式化的技巧
- 问题是在我们的槽方法中无法对日期进行代码提示,关键的技巧就是对参数重新格式化为QDate类型就可以了

- 格式化日期使用toString方法来实现.
- 实现的时候,我们有两种方法:
- 方法一:使用y表示年的一位,M表示月,d表示日
`self.lbl.setText(mydate.toString("yyyy-MM-dd"))`
- 方法二:使用系统中的已经定义好的方式
- 这种方式,已经定义好的枚举类
`self.lbl.setText(mydate.toString(1))`或者`self.lbl.setText(mydate.toString(Qt.ISODate))`

### 总结强调
- 掌握日历控件QCalendarWidget的载入与配置.
- 掌握日历控件的信号控制
- 掌握日期格式化的几种方法.



# PyQt5的第十久课 - PyQt5菜单menu应用,新建多窗口
### 知识回顾

- 掌握日历控件QCalendarWidget
- 

### 案例:菜单
- 新建第一窗体
- 一级菜单的配置
- 二级菜单的配置
- 利用菜单功能实现界面跳转实现温馨提示


### 开发思路
- 导入类QMainWindow
- 使用Qmenu菜单类,这个菜单我们可以从窗体本身的方法进行获取
- 利用好Qmeun的功能,来实现多级菜单addAtion这是一个直接产生点击事件的行为
也可以用addMenu功能来增加子菜单
- 每次都要弹出新窗体,这个新窗体,我们要制作成全局的窗体
- 使用QMessagebox 来实现一个简单的帮助


### 一个空的模板
```python
import sys


from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QCalendarWidget, QLabel, QVBoxLayout, QApplication, QWidget
from PyQt5.QtCore import QDate, Qt


class MyClass(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()


    def initUI(self):
        self.setWindowTitle("liujinr")
        self.setGeometry(300,100,400,300)


        self.show()

```
### 载入菜单的简单功能
```python
my_menu = self.menuBar()
my_menu.addAction("新建")
my_menu.addAction("运行")
my_menu.addAction("调试")
my_menu.addAction("帮助")
```
### 子菜单的书写
- 这里要注意,直接将子菜单写在父菜单的下方
- 这样的好处,更多的也可以帮助我们进行二次理解
- 子菜单的添加,通过addMenu功能

### 子菜单的核心代码
```python
my_menu = self.menuBar()
        file_menu = my_menu.addMenu("文件")
        file_menu.addAction('新建')
        recent_file = file_menu.addMenu("最近的")
        recent_file.addAction("文件1")
        recent_file.addAction("文件2")
# 这里注意,子菜单的写法,一级一级下来的
```

### 对于新窗体的建议
- 建议一个窗体就写一个类.那么每一次新的窗体出现的时候,就实例化这个类就OK了
- 注意:想要让这个窗体被一直死循环监听,必须要把这个窗体作为程序的全局变量
- 否则就会出现闪退现象


### 新建一个窗体的写法
- 直接写一个自定义的类窗体
- 将这个类窗体先不要show
- 将这个类窗体在main中进行实例化,作为全局变量
- 在槽的行为中,将这个窗体show出来


### 新建多个窗体
- 这里是思想要实例化多个窗体,且这些窗体都是全局变量
- 这里要考虑用列表作为全局变量
- 此时,我们需要在自定义的类中书写show的代码


### 总结强调
- 掌握菜单栏的书写
- 掌握菜单按钮的单击行为跳转功能
- 掌握子菜单的建立,
- 掌握多窗体的书写
