---
title: "PyQt5学习笔记6-10"
date:       2019-10-31
tags:
	- Python
	- solution
	- basis
	- PyQt5
---

  











# PyQt5的第六课 - PyQt5类的封装
### 知识回顾
- 掌握纯代码写pyqt5程序
- 显示提示框tooltip功能(这个玩意在所有的控件中都是存在的)

### 代码封装思路
- 分析哪些代码需要封装:需要封装的就是我们对窗体配置的代码
- 利用类的继承特性
- 调用父类Qwidget的构造方法`super().__init__()`
- 调用自己的构造方法

### 用类的方式去实现空的窗口的代码
```python
import sys

from PyQt5.QtWidgets import QWidget,QApplication



class MyClass(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("刘金玉编程")
        self.setGeometry(30,40,300,200)
        self.show()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    c = MyClass()
    app.exec_()
```
### GUI位置大小函数setGeometry

- 这个函数相当于resize函数和remove函数功能的合体
- 函数使用格式:
    控件对象.setGeometry(X轴,Y轴,宽度,高度)
    
### 信号
- 窗体上的信号被app.exec_()死循环监听着.
- 信号至少在QT中针对某个发生的时间的说法
- 槽是QT中发生的具体的某个时间,就是槽
- 窗体上的对GUI界面操作行为都是被监听着的
- GUI是被事件驱动的
    

### 信号槽的简单使用
- 格式:信号源.信号.connect(槽)
- 格式解释:信号源(按钮)信号(clicked).connet(某个事件方法)
- 注意:在绑定信号槽的过程汇总,我们的槽方法可以不加括号的,传递的是方法的引用本身
说白了,我要的是函数,而不是函数的返回值,这里如果想要加上参数,就用lambda 吧!

### 加入了按钮的点击关闭时间的代码    
```python
import sys

from PyQt5.QtWidgets import QWidget, QApplication, QPushButton


class MyClass(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("刘金玉编程")
        self.setGeometry(30,40,300,200)
        btn = QPushButton("关闭",self)
        btn.move(5,6)
        # 将信号发送到一个槽
        # 设置按钮的点击后关闭窗体的时间
        btn.clicked.connect(self.close)
        self.show()

app = QApplication(sys.argv)
c = MyClass()
app.exec_()
```

### 总结强调
1. 掌握类的继承QWidget的基本思想
2. 掌握类的功能封装
3. 掌握setGeometry函数
4. 掌握简单的信号槽的使用



  
# PyQt5的第七课 - PyQt5消息盒子QMessageBox

### 知识回顾

- 使用类进行pyqt5的GUI开发封装
- 使用setGeometry哈数:大小,位置
- 掌握类的继承与内部屌用


### 消息盒子
- 使用类库QMessageBox
- 不同的图标的消息类别:
- 带有图标的消息盒子setGeometry,图标可以是问号question,信息information

-注意:使用消息盒子后,最后会返回一个按钮类型的结果,最后这个结果是我们人机交互的结果

点击按钮出现消息选择框,处理消息选择框的结果
基础类封装的代码
### 重写关闭事件-思路
- 当点击关闭按钮的时候,执行的是窗体的关闭,而窗体的关闭,等同于点击窗口的右上角的按钮的效果.这个效果是QWidget基类所实现的

-提问:我么该如何实现我们自己需要的关闭时候的效果呢?

- 重写父类方法

- 重新写关闭事件
### QMessageBox使用格式
使用格式:
QMessageBox.question(self,"提示title","消息内容","默认选中值")

### 如何阻止事件的关闭 
- 利用传过来的时间对象
- 我们通过输出形式,看到时间对象的属性和方法,猜测到具体的方法
```python
Event.accept()#同意关闭
Event.ignore()#忽略操作
```

### 总结强调
- 掌握的类的封装基本代码



  
# PyQt5的第八课 - PyQt5窗体居中和布局


### 知识回顾
1. 窗体事件的重写,closeEvent事件
2. QMessageBox消息框的使用


### 窗体的居中
- 默认情况下,如果没有添加窗体位置的函数,
- 手动调整到屏幕居中位置
- 通过desktop()函数阿里获取桌面控件的对象QDesktopWidget
- 通过桌面对象的width()函数来获取屏幕的宽度的分辨率


### 标签文本控件
- 使用类库Qlabel
- 使用格式:
lbl = QLabel("编程创造城市",self)


### 绝对布局
- 直接通过move()到某个像素点的位置
- 特点:非常灵活
- 弱点:不能随着窗体的大小而变化


### 总结强调
1. 掌握窗体居中布局的方法
2. 掌握利用绝对布局的方法以及优劣势


  
# PyQt5的第久课 - PyQt5窗体绝对布局和相对布局

### 知识回顾

1. 点到了窗体的绝对布局

2. 窗体的居中方式:根据已知像素,计算窗体的起点位置

- Desktop()函数,这个函数是在QApplication类中的.函数返回的结果QDesktopWidget对象

3. 标签控件的使用
- 想要获取水平方向,调用width函数

- 想要获取垂直方向,调用height函数



### 相对布局
1. 绝对布局是直接将控件载入到窗体的位置就可以了.一般直接采用move函数移动到指定的位置后不变.

2. 相对布局是要将控件放到盒布局中.一般是还要加入一个盒布局.QHboxlayout(水平方向) QVboxlayout(垂直方向),网格布局(QgridBoxla yout)


### 绝对布局与相对布局的不同
- 布局中的控件可以随着窗体的变化而变化
- 布局中的控件之间的距离可以按照比例来调节


### QHBoxLayout

- 要是水平盒布局不好记的话,那你看这个H是不是,中间有一个横的

- 把所有的控件只能在水平反向上面排列,会自动一个一个排列不会重叠,这个是一个特性
- 默认情况下,垂直居中的
- 记忆方式:看H中的横线,就认为是水平布局


### 垂直布局的思想
- 增加弹簧


### 弹簧
- 就是直接使用盒布局的addstretcfh方法就可以了
- Addstretch(弹簧比例)
- 弹簧比例:是指在窗体中进行指定的比例分割.


### 总结强调
1. 掌握相对布局与绝对布局的区别
2. 掌握兼顾地布局中的水平盒布局与垂直盒布局
3. 掌握和布局中的控件比例排布关系




  
# PyQt5的第时课 - PyQt5网格布局QGridLayout

### 知识回顾

- 掌握QHboxLayout水平盒子布局
- 掌握QVboxLayout垂直盒子布局
- 盒子布局,我们可以结合自带的"弹簧功能"addstrach
- LineEdit类库作用:单行文本框

### 网格布局

<table>
    <tr>
        <td>0,0</td><td>0,1</td>
    </tr>
    <tr>
        <td>1,0</td><td>1,1</td>
    </tr>
    <tr>
        <td>2,0</td><td>2,1</td>
    </tr>
</table>

```python
网格布局的使用时需要注意:
1. 要导入类库QGridLayout
2. 该布局的索引默认从0开始
3. 使用网格布局前先要进行类的实例化
```


### 网格布局设置
- 我们其实可以通过网格布局实例化后的对象,直接通过代码提示的方式看到很多我们可以直接实现的方法.

- 比如:我们想要设置网格之间的空间距离,我们呢可以设置setSpacing来设置,

- 举例:Grid.setSpacing(空间的像素值)

- 我们要学会举一反三,通过set的方式设置其他功能

### 多行文本框的

- 使用QTextEdit这个类库
- 使用方法类似于直接对类的实例化

### 总结强调
- 掌握网格布局的思想,QGridLayout
- 掌握新控件多行文本框的使用
- 根据QTDesigner来了解新控件,或者根据pyqt5中提供目录来了解新控件

