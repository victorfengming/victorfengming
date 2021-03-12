---
title: "python高级编程技巧"
cover: "/img/lynk/55.jpg"
date:       2019-12-05
subtitle: "MOOC"
tags:
	- Python
	- solution
	- basis
---
  
  
### 如何在列表,字典,集合中根据条件筛选数据 

方法1:通过迭代来进行判断筛选

解决方案
函数式编程:

### 如何统计序列中元素的出现频度

解决方案:使用collections.Counter对象

将序列传入Counter的构造器,得到Counter对象是元素频度的字典
Counter.most_common(n)方法得到频度最高的n个元素的列表

### 如何感觉字典中的值的大小,对字典中的项进行排序

解决方案:使用内置函数sorted
1. 利用zip将字典数据转换成为元组
2. 传递sorted哈数的key参数

### 如何快速找到多个字典中的多个公共键(key)?

利用集合(set)的交集操作
step1:使用字典的viewkeys()方法,得到一个字典keys的集合
step2:使用map函数,得到所有字典的keys的集合
step3:使用reduce函数,取得所有字典的keys的集合的交集

### 如何让字典保持有序

使用collections.OrderedDict
以OrderedDict替代内置字典Dict,依次将选手的成绩存入OrderedDict

### 如何实现历史记录功能

使用容量为n的队列存储历史记录
使用标准库collections中的deque,它是以双端循环队列
程序退出前,可以使用pickle将队列对象存入文件,在此运行程序时将其导入

### 如何实现可迭代对象和迭代器对象
有可迭代对象,得到迭代器

通过列表调用迭代器接口
通过字符串调用迭代器接口


### 如何使用生成器函数实现可迭代对象

将该类的__iter__方法实现成生成器函数,每次yield返回一个素数


### 如何读写csv数据

使用python标准库中的csv模块,可以使用起哄reader和write完成csv文件的读写

### 如何读写json数据

使用python标准库中的json模块,可以使用loads,dumps函数可以完成json数据的读写

### 如何解析和构建xml文档

使用python标准库中的xml.etree.ElementTree,其中的parse函数可以解析xml文档



### 如何读写Excel文件

使用第三方库xlrd,xlwt,这两个库分别用于Excel的读写



