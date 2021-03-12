---
title: "PyQt5学习笔记11-15"
cover: "/img/lynk/88.jpg"
date:       2019-11-01
tags:
	- Python
	- solution
	- basis
	- PyQt5
---

  











# PyQt5的第十一课 - PyQt5三原色案例

### 知识回顾

- QGridLayout网格式布局
- 默认索引从0开始
- QTextEdit多行文本框
- 注意:网格布局是可以扩展性的,可以随着系统界面变化而变化的

### 案例目标
制作一个界面如右图.功能是描述三原色.在设计中,我们往往有三原色概念

基本上所哟的颜色都可以由三种颜色调和而成,这三种颜色分别是RGB

,我们使用三个按钮分别表示这个三种颜色,每个按钮都可以有哦两种状态

为蓝色,未选中按钮为默认灰色,在界面中用一个区块(QFrame)来表示颜色

### 思路
- 制作界面采用PyQt5进行布局
- 采用合资布局的方法进行界面布局
- 按钮的状态功能加入
- 设置Qframe的背景颜色
- 设置按钮的点击事件
- 设置三原色情况,最终还是要通过改变Qframe样式来实现颜色变化

### 框架容器QFrame

- 必须使用类库QFrame
- 初始化:
- myframe = QFrame()

- 注意点

- 父容器可以采用后期添加到盒子布局的方式进行设置

- 当然可以可以在初始化的时候设置

- 父容器的设置会影响子容器的生命周期的

### 控件设置CSS风格
- 可以通过setStyleSheet方法来设置
- 这个方法几乎在所丶有的QWidget的控件之上都能实现
- 使用举例:
    myframe.setStyleSheet("QWidget{background-color:black}")
    
- 在setStyleSheet方法中使用CSS类型的字符串

- 这个CSS风格使用格式:

- 需要控制的空阿金标签或者行为,然后写一个大括号{},我们在大括号    内写各类控制某个标签的样式.样式的书写风格就是   `属性:值`

### 按钮是否选中可以选中与不选中的切换
使用setChecable方法,默认情况下这个方法设置的值为false,我们设置为True才行

### 槽函数传参
- 槽函数定义需要看我们的信号源是否有参数
- 信号源中有参数的部分的信号参数我们需要使用中括号
- 使用举例:`btnRed.clicked[bool].connect(self.setColor)`
- 如何传递控件对象?
- 使用self.sender()就会返回触发事件对象本身

### 三原色函数
- 使用QColor来实现

- 红,绿,蓝范围在`[0,255]`之间

- 第1个参数表示红色

- 第2个参数表示绿色

- 第3个参数表示蓝色

### 总结强调
- 掌握三原色函数
- 掌握布局的思想
- 掌握按钮的选择状态
- 掌握信号槽传参和控件事件的传递



  
# PyQt5的第十二课 - PyQt5三原色

### 知识回顾

- 程序中的三原色
- 按钮状态的改变Qpushbutton装填的改变,设置是否选重中checked
- 利用我们已经学过的布局思想

### qlineEdit使用

- 它是一个单行文本框
- 事件:文本改变事件.textchange类似这样的代码的事件.
- 结合qt中基本的信号槽机制
- 注意:信号在传递参数的时候要把小括号改成

### 设置标签宽度自适应

- 标签使用Qlabel
- 使用标签的时候,标签默认的宽度是固定的,当标签文本内容宽度的显示区域的时候
- 超出部分的内容就会进行遮挡.此时我们可以考虑让标签的内容积习难改in自定义区域适应
- 标签区域自适应适应函数adjustsize

### 总结强调
掌握qlineEdit的文本改变事件
掌握文本标签的区域自适应
掌握事件的信号槽关系以及传递参数




  
# PyQt5的第十三课 - PyQt5复选框 QCheckBox控件事件应用

### 知识回顾

- 文本框事件的改变,qlineEdit单行文本框
- 标签自适应adjustsize方法

### 复选框
- 使用控件QCheckBox
- 使用格式
- 变量对象 = QCheckBox(显示文本,父容器)
- 这里的父容器可以是一个QWidget类型

我们案例中的QFrame实际上本质是一个QWidget

### 复选框状态改变信号
- 使用statechanged信号,注意这个信号可以传以参数,这个参数是一个int类型.
- 使用格式:
- `self.复选框.stateChanged[int].connect(self.myState)`
- `复选框.状态改变信号[整型参数].connect(类中的自定义方法)`
- 使用案例:
- `self.ck1.stateChanged[int].connect(self.myState)`

### 如何区分通过信号传递过来的不同控件?
- 直接通过self对象的sender方法就可以进行区分了

### Qt中有很多枚举类表示 
- 比如我们今天学习的选中复选框使用2对应表示为Qt.Checked
- 写成枚举类型的好处就是方便我们阅读代码.

### 总结强调
- 复选框的状态改变事件statechanged
- qt枚举
- 掌握把控件放到容器中qframe

  
# PyQt5的第十四课 - PyQt5滑块控件Qslider的应用

### 知识回顾

- 掌握了复选框QCheckBox
- 枚举类中的值为2
- 在Qframe中的应用

### Qslider控件

- 这个是一个滑块控件.用于方便左右滑动
- 往往这类滑动更多的用于屏幕可以触碰的设备
- 实则就是调用Qslider库
- 进行实例化后进行调用
- 使用格式:
    变量名称 = Qslider(方向,父容器)
- 水平方向值为1,垂直方向值为2(说白了你不写常量,你直接就写1,2都行了)    
- 这个控件可以水平放置,也可以垂直放置Qt.Vertical
- 应用举例:
- QSlider(Qt.Horizontal.self)

### 枚举类的存在类库
- QtCore核心库
- 

### 滑块控件的最值设置(范围设置)
- 最小值设置
- 举例设置最小值为0:
- `sl.setMinimum(0)`
- 最大值设置
- 举例设置最大值为255:
- `sl.setMaximum(255)`

### 滑块的滑动值变化事件
- `滑块的格式:滑块对象名称.valueChanged[int].connect(对应)`
- `sl.valueChanged[int].connect(self.myValue)`

### 总结强调
- 掌握滑块控件Qslider的使用
- 掌握滑块值的事件
- 掌握枚举类库的使用

  
# PyQt5的第十五课 - PyQt5进度条QProgressBar应用

### 知识回顾

- 滑动控件qslider
- 关键:设置最大值,最小值,绝对范围
- 核心类库QtCore,枚举类Qt

### 进度条qprogressbar

使用思想:
- 载入类库
- 初始化对象
- 设置最小值和最大值
- 时钟的使用QBasicTimer,跟槽方法对应类库中的timeevent

### 制作案例
- 界面由进度条和按钮组成
- 进度条的值范围为0-100
- 按钮的状态为:"开始", "暂停","终止"
- 按钮需要控制进度条进度

### 导入时钟类库

`from pyqt5.qtcore import qbasictimer`

### 初始化进度条
```python
# 载入进度条
self.pgb = QProgressBar(self) # 类对象的初始化
self.pgb.move(50,50) # 将进度条移动到指定的位置
self.pgb.resize(300,20) # 设置进度条宽高
```

### 设置进度条的范围
```python
self.pgb.setMinimum(0)  # 设置最小值
self.pgb.setMaximum(100) # 设置最大值
self.pgb.setValue(50)   # 设置当前进度
```

### 时钟控件
- 做用:每搁多少时间执行一次时钟内部的代码
- 时间单位:毫秒
- 1秒 = 1000毫秒

### QBasicTimer控价解析
- isActive方法:返回时钟控件是否开启,如果开启返回true,否则为false
- start方法:使得时钟控件开启来,需要传入时钟间隔,时间单位为毫秒
- 简单的参数使用格式
- start(时间,self)
- stop方法:使得时钟控件关闭.
- timerID方法:返回当前时钟控件的ID,主要用于多个时钟控件使用的时候,区分不同的时钟控件.
- 对应的槽方法是Qwidget控件自带的timerEvent事件.
- 时钟控件的每个多少时间要运行一次的代码就是在timerEvent方法中,我们在使用时钟控件的时候要重写这个方法

### timerEvent方法

```python
# 声明一个时钟控件
self.timer1 = QBasicTimer()
# 开始计时
self.timer1.start(1000,self)
# 这玩意是系统带的,自动就调用它,默认1秒钟一次
def timerEvent(self, e):
    self.pv += 1
    self.pgb.setValue(self.pv)   # 设置当前进度
```

### 时钟控件状态切断的核心代码
```python
if self.timer1.isActive():  # 检测是否开启
        self.timer1.stop(50, self)
        self.btn.setText("开始")  # 这里的按钮的状态显示的是按钮下次的行为
    else:
        self.timer1.start(50, self)
        self.btn.setText("停止")
```

### 总结强调
- 掌握Qprogressbar的控件的配置
- 掌握时钟控件的基本使用QBasicTimer
- 理解按钮控制时钟控件达到进度条的运行的思想.