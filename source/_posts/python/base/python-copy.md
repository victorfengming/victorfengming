---
title: "Python3中深拷贝与浅拷贝"
cover: "/img/lynk/51.jpg"
date:       2019-01-14
tags:
	- Python
	- background
	- base
---












# python中关于深拷贝和浅拷贝的详解
### 概述
在python的语法中,有两种变量的拷贝方式
一种是深拷贝,一种是浅拷贝
### 我们先说深拷贝

##### 语法
这里需要通过导入系统的copy模块中的deepcopy才可以
import copy
新的对象 = copy.deepcopy(被拷贝对象)
##### 解释
深拷贝是将操作对象整体复制出来一份,与其原来拷贝的对象没有联系,拷贝后重新分配一个内存地址
对拷贝和的对象进行各种操作,原对象也不收到影响

### 再来说浅拷贝
##### 语法
浅拷贝的语法很多
新的对象 = 被拷贝对象
新的对象 = 被拷贝对象.copy()
新的对象 = lis被拷贝对象t0[:]
import copy
新的对象 = copy.copy(被拷贝对象)
##### 解释	
浅拷贝中,虽然对象本身的地址发生了改变,但是对象中包含的数据还是原来的地址,仅仅是传递过来一个引用
指向了原来对象中的数据,如果改变其中一个对象中的内容,其另一方也会对应更改
(这里需要注意,如果更改的数据类型是不可更改对象,则改变的是其引用,本身没有改变,只是这个位置的数据换成了另一个地址中的)

### 下面看一下代码的测试(小编的测试环境是python3.8版本)

```python

import copy

list0 = [['abc'], '秋叶夏风']
list1 = list0
list2 = list0.copy()
list3 = list0[:]
list4 = copy.copy(list0)
list5 = copy.deepcopy(list0)
list6 = copy.deepcopy(list0)

print('0', list0, '拷贝的对象的地址:', id(list0), '第一个元素的地址:', id(list0[0]))
print('1', list1, '拷贝的对象的地址:', id(list1), '第一个元素的地址:', id(list1[0]))
print('2', list2, '拷贝的对象的地址:', id(list2), '第一个元素的地址:', id(list2[0]))
print('3', list3, '拷贝的对象的地址:', id(list3), '第一个元素的地址:', id(list3[0]))
print('4', list4, '拷贝的对象的地址:', id(list4), '第一个元素的地址:', id(list4[0]))
print('5', list5, '拷贝的对象的地址:', id(list5), '第一个元素的地址:', id(list5[0]))
print('6', list6, '拷贝的对象的地址:', id(list6), '第一个元素的地址:', id(list6[0]))

print('---------------------------------改变拷贝对象的内容--------------------------------')

list1[0] = 1
list2[0] = 2
list3[0] = 3
list4[0][0] = 4
list5[0][0] = 5
list6[0] = 6

print('0', list0, '拷贝的对象的地址:', id(list0), '第一个元素的地址:', id(list0[0]))
print('1', list1, '拷贝的对象的地址:', id(list1), '第一个元素的地址:', id(list1[0]))
print('2', list2, '拷贝的对象的地址:', id(list2), '第一个元素的地址:', id(list2[0]))
print('3', list3, '拷贝的对象的地址:', id(list3), '第一个元素的地址:', id(list3[0]))
print('4', list4, '拷贝的对象的地址:', id(list4), '第一个元素的地址:', id(list4[0]))
print('5', list5, '拷贝的对象的地址:', id(list5), '第一个元素的地址:', id(list5[0]))
print('6', list6, '拷贝的对象的地址:', id(list6), '第一个元素的地址:', id(list6[0]))

```
结果如下:

```python
D:\Python38\python.exe E:/PycharmProjects/python_August/day09/关于列表的拷贝问题.py
0 [['abc'], '秋叶夏风'] 拷贝的对象的地址: 2209540405760 第一个元素的地址: 2209541417472
1 [['abc'], '秋叶夏风'] 拷贝的对象的地址: 2209540405760 第一个元素的地址: 2209541417472
2 [['abc'], '秋叶夏风'] 拷贝的对象的地址: 2209540405888 第一个元素的地址: 2209541417472
3 [['abc'], '秋叶夏风'] 拷贝的对象的地址: 2209541418112 第一个元素的地址: 2209541417472
4 [['abc'], '秋叶夏风'] 拷贝的对象的地址: 2209541417152 第一个元素的地址: 2209541417472
5 [['abc'], '秋叶夏风'] 拷贝的对象的地址: 2209541418176 第一个元素的地址: 2209541417792
6 [['abc'], '秋叶夏风'] 拷贝的对象的地址: 2209541417856 第一个元素的地址: 2209541416896
---------------------------------改变拷贝对象的内容--------------------------------
0 [1, '秋叶夏风'] 拷贝的对象的地址: 2209540405760 第一个元素的地址: 140708592568128
1 [1, '秋叶夏风'] 拷贝的对象的地址: 2209540405760 第一个元素的地址: 140708592568128
2 [2, '秋叶夏风'] 拷贝的对象的地址: 2209540405888 第一个元素的地址: 140708592568160
3 [3, '秋叶夏风'] 拷贝的对象的地址: 2209541418112 第一个元素的地址: 140708592568192
4 [[4], '秋叶夏风'] 拷贝的对象的地址: 2209541417152 第一个元素的地址: 2209541417472
5 [[5], '秋叶夏风'] 拷贝的对象的地址: 2209541418176 第一个元素的地址: 2209541417792
6 [6, '秋叶夏风'] 拷贝的对象的地址: 2209541417856 第一个元素的地址: 140708592568288

Process finished with exit code 0
```


