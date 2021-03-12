---
title: "matplotlib绘图相关"
date:       2019-02-19
title: "数据的直观表达-->图形展示"
tags:
	- Python
	- basis
	- data_analysis
---
  






  
  
  
## 第一部分  
### chapter01 matplotlib和numpy起步
```python
'''
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by victor
# Created Time: '2020/2/14 10:39'
'''
# 用于测试matplotlib

import matplotlib.pyplot as plt
# plt.plot([1,2,3],[3,2,1])
# plt.show()
plt.plot([1,2,3,4],[-4,-3,-2,-1])
plt.show()


'''
numpy是python开源的数值计算扩展
可用来储存和处理大型矩阵,比python自身的数据结构要高效
numpy将python变成了一种免费强大的MATLAB系统
'''

# ndarray 创建 一般有三种方式
'''
1. 从python的基础数据对象进行转化
2. 通过numpy内生成的函数生成
3. 从硬盘(文件)读取数据
'''
# 索引和切片(类似于列表的操作)

# 常用函数
'''
min,max,median,mean,variance,sort
'''
```
  
### chapter02 matplotlib中计算各种值
```python
import numpy as np

c = np.random.randint(1,100,10)

print(c)
#
# # 求最大值
# print(np.max(c))
# print(c.max())
# # 求最小值
# print(np.min(c))
# print(c.min())
# # 求均值
# print(np.mean(c))
# print(c.mean())
# # 求方差
# print(np.var(c))
# print(c.var())

# np.save('x.npy',c) # 存为.npy文件

c = np.load('x.npy')
print(c)
```
  
### chapter03 matplotlib绘制散点图
```python
'''
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by victor
# Created Time: '2020/2/14 11:09'
这回我们来画散点图,散点图最大的特点就是能体现相关性,比如正相关,负相关,和不相关
'''

import numpy as np
import matplotlib.pyplot as plt


# # 正相关的
# height = [161,172,182,175,173,165]
# weight = [50,58,80,70,69,55]
#
# plt.scatter(height,weight)
# plt.show()



# # 不相关的
# N = 1000
#
# x1 = np.random.randn(N)
# y1 = np.random.randn(N)
# plt.scatter(x1,y1)
# plt.show()


# # 正相关的
# N = 1000
# x1 = np.random.randn(N)
# y1 = x1 + np.random.randn(N)*0.5
# plt.scatter(x1,y1)
# plt.show()

# 负相关的
N = 1000
x1 = np.random.randn(N)
y1 = - x1 + np.random.randn(N)*0.5
plt.scatter(x1,y1,s=50,alpha = 0.5,c='r',marker='<')
plt.show()

'''
图表能够十分直观的体现出数据之间的关系,
'''

# 散点图的外观调整
'''
1. 颜色 c
2. 点大小 s
3. 透明度 alpha
4. 点形状,marker
'''
```
  
### chapter04 matplotlib绘制折线图
```python
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10,10,5)
y = x**2

plt.plot(x,y)
plt.show()
```  


### chapter05 matplotlib绘制条形图

```python
'''
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by victor
# Created Time: '2020/2/14 14:03'
本节我们来画条形图
'''

# 概念:条形图其实就是使用长方形的长度来显示变量大小的图表

# 用来比较多个数据的大小,通常利于数据集较少的分析
# 例如不同季度的销量,不同国家的人口等yufengmengyufengmengyufengmeng


import numpy as np
import matplotlib.pyplot as plt

N = 5
y = [20,10,30,25,15]

# index = np.arange(N)
# # pl = plt.bar(x=index,height=y,color='green',width=0.5)
# # pl2 = plt.bar(x=0,bottom=index,width=y,color="red",height=0.5,orientation="horizontal")
# pl2 = plt.bar(x=0,bottom=index,width=y,color="red",height=0.5)
# # pl3 = plt.barh(y=0,width=y,index=index)
# plt.show()

index = np.arange(4)

sales_BJ = [52,55,63,53]
sales_SH = [44,66,55,41]

bar_width = 0.3

plt.bar(index,sales_BJ,bar_width,color="b")
plt.bar(index+bar_width,sales_SH,bar_width,color="r")
plt.show()
```

### chapter06 matplotlib绘制直方图

```python
'''
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by victor
# Created Time: '2020/2/14 17:47'
直方图
'''

# import numpy as np
# import matplotlib.pyplot as plt
#
# '''
# 直方图是由一系列高度不等的纵向条形组成,表示数据分布情况
# 这里需要注意和条形图区分
# 直方图通常表示连续变化的数据
# 条形图通常用于展示不同类型的数据,而且这个类别通常是不连续的
# 说白了就是直方图,中间没有空
# '''
#
# mu = 100
# sigma = 20
# x = mu+ sigma*np.random.randn(20000)
#
# # print(x)
# # plt.hist(x,bins=10)
# '''
# The 'normed' kwarg was deprecated in Matplotlib 2.1 and will be removed in 3.1. Use 'density' instead.
#   plt.hist(x,bins=10,color='red',normed=True)
#   '''
# # plt.hist(x,bins=50,color='green',density=True)
# plt.hist(x,bins=500,color='green')
# # 这里bins表示有几个条装的柱形
# plt.show()
#


# 一个双变量的直方图

import numpy as np
import matplotlib.pyplot as plt

x = np.random.randn(1000)+2
y = np.random.randn(1000)+3

plt.hist2d(x,y,bins=40)
plt.show()
```

### chapter07 matplotlib绘制饼状图

```python
'''
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by victor
# Created Time: '2020/2/14 23:12'
这节我们来练习画饼状图,的饼状图用于显示各项的大小和总和的比例
饼状图中的数据点显示为整个饼状图的百分比
如前十大品牌占市场份额图
'''

import numpy as np
import matplotlib.pyplot as plt

labels = 'A','B','C','D'
fracs = [15,30,45,10]
explode = [0.2,0,0,0.2]

# 在python2中,好像默认不是正圆,那么要想整成正圆,就要这样写法
plt.axes(aspect=1)  # 这行我就不知道有什么用,感觉是毛用没有啊


plt.pie(x=fracs,labels=labels,autopct='%.0f%%',explode=explode,shadow=True)
# 这个autopct是python中的格式化字符串
# explode能够突出显示某几块儿的值
# shadow是阴影

# pyth'onpythonpytho'n python python python pyth'on python pyhto'n pythio

'''
def pie(
        x, explode=None, labels=None, colors=None, autopct=None,
        pctdistance=0.6, shadow=False, labeldistance=1.1,
        startangle=None, radius=None, counterclock=True,
        wedgeprops=None, textprops=None, center=(0, 0), frame=False,
        rotatelabels=False, *, data=None):
    return gca().pie(
        '''

plt.show()


```

### chapter08 matplotlib绘制箱型图

```python
'''
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by victor
# Created Time: '2020/2/14 23:34'
本节课我们画箱型图
箱型图又称之为盒须图,盒式图或者箱线图
是一种用作显示一组数据分散情况资料的统计图
上边缘,上四分位数,中位数,下四分位数,下边缘,异常值
'''

import numpy as np
import matplotlib.pyplot as plt

a = [42,55,79,68,15,98]
b = [32,59,77,100,92,88,5,0]
c = [92,98,78,65,97,100,0]

plt.boxplot(
    (a,c,b),  # 数据
    labels = ('a','c','b'),  # 标签

    showfliers = True,  # 是否显示异常值，默认显示
    whis = 1.5,  # 指定异常值参数：默认1.5倍四分位差
    showmeans = True, # 是否显示平均值，默认不显示
    meanline = True, # 是否用线标示平均值，默认用点

    widths = 0.5, # 柱子宽度

    vert = True, # 默认True纵向，False横向
    patch_artist = True,  # 是否填充颜色
    boxprops = {'facecolor':'#ffff00','color':'green'}, # 箱体样式
)

plt.grid(linewidth=0.2)
plt.show()
```
### chapter09 matplotlib中的颜色

```python
'''
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by victor
# Created Time: '2020/2/15 11:29'
这回我们来玩颜色,八种内建颜色缩写
    b:blue
    g:green
    r:red
    c:cyan
    m:magenta
    y:yellow
    k:black
    w:white
其他颜色表示方法
    灰色阴影
    html十六进制
    RGB元祖

'''


import numpy as np
import matplotlib.pyplot as plt

y = np.arange(1,5)
y2 = np.arange(2,4)
y3 = np.arange(3,7)
y4 = np.arange(3,1)
# plt.plot(y)
# plt.plot(y,color='green')
plt.plot(y+1,color='m',marker='o')
plt.plot(y+2,color='0.6',marker='^')
plt.plot(y+3,color='#ff00ff',marker='D')
plt.plot(y+4,color=(0.1,0.2,0.3),marker='p')

plt.show()

'''
默认颜色是蓝色
'''

```
## 第二部分

### chapter10 面向对象 VS MATLAB style 

```python
'''
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by victor
# Created Time: '2020/2/15 11:43'
'''

'''
面向对象 VS MATLAB style 
三种方式优劣
- pyplot:简单易用,交互使用时方便,可以根据命令实时作图.但是底层的定制能力不足.
- pylab: 完全封装,环境最接近Matlab.不推荐使用
- 面向对象: (Object-Oriented)的方式:接近Matplotlib基础和底层的方式.难度稍大.但是定制能力强,而且是matplotlib的精髓
总结: 实战中推荐,根据需求,综合使用pyplot和OO的方式,显示导入numpy
常用模块导入代码:
import matplotlib.pyplot as plt
import numpy as np

'''

#
# from pylab import *
#
# x = arange(0,10,1)
# y = randn(len(x))
#
# plot(x,y)
# title('pylib')
#
# show()
#
# # 这种方式写起来很像matlab,但是我们不推荐使用

# # 第二种方式(我们之前的方式)
# import matplotlib.pyplot as plt
# import numpy as np
#
# x = np.arange(0,10,1)
# y = np.random.randn(len(x))
#
# plt.plot(x,y)
# plt.title('pyplot')
# plt.show()

# 第三种方式(面向对象方式)
import matplotlib.pyplot as plt
import numpy as np
'''
解决Python使用matplotlib绘图时出现的中文乱码问题
最近使用学习Python中使用matplotlib绘图时发现控制台报如下问题，可知是中文字体问题
'''
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号

x = np.arange(0,10,1)
y = np.random.randn(len(x))


fig = plt.figure()
ax = fig.add_subplot(111)

l = plt.plot(x,y)
t = ax.set_title("面向对象方式!~!!")


plt.show()

```


### chapter11 matplotlib面向对象简介 

```python
'''
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by victor
# Created Time: '2020/2/15 12:04'
'''

'''
matplotlib面向对象简介
    FigureCanvas    画布
    Figure          图
    Axes            坐标轴
'''


import matplotlib.pyplot as plt
import numpy as np

x = np.arange(1,100)

fig = plt.figure()

ax1 = fig.add_subplot(221)
ax1.plot(x,np.log(x))
ax1 = fig.add_subplot(222)
ax1.plot(x,x*x)
ax1 = fig.add_subplot(223)
ax1.plot(-x,2*x)
ax1 = fig.add_subplot(224)
ax1.plot(-x,x**2)

plt.show()
```


### chapter12 figure 多图 

```python
'''
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by victor
# Created Time: '2020/2/15 22:00'
本节我们讨论figure 多图
'''


import matplotlib.pyplot as plt

fig1 =  plt.figure()

ax1 = fig1.add_subplot(111)

ax1.plot([1,2,3],[3,2,1])

fig2 =  plt.figure()

ax2 = fig2.add_subplot(111)

ax2.plot([1,2,3],[3,2,1])

plt.show()

```

### chapter13 网格 

```python
'''
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by victor
# Created Time: '2020/2/15 22:05'
这回我们画网格
'''

# 如何画网格呢?其实就是一句话
# plt.grid(True)

# 定制化网格

# 命令行的方式
# import matplotlib.pyplot as plt
#
# fig1 =  plt.figure()
#
# ax1 = fig1.add_subplot(111)
#
# ax1.plot([1,2,3],[3,2,1])
#
# fig2 =  plt.figure()
#
# ax2 = fig2.add_subplot(111)
#
# ax2.plot([1,2,3],[3,2,1])
# plt.grid(True)
# plt.grid(color='g')
# plt.grid(linewidth='2')
# # plt.grid(linestyle='--')
# plt.grid(linestyle='-.')
# plt.show()

# 面向对象的方式绘制网格
import matplotlib.pyplot as plt
import numpy as np

# 生成一个图形对象
fig = plt.figure()

x = np.arange(0,10,1)

ax = fig.add_subplot(111)

plt.plot(x,x**2)

ax.grid(color = 'g')

plt.show()

'''
面向对象是没有交互的效果的
'''

```


### chapter14 图例 legend 

```python
'''
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by victor
# Created Time: '2020/2/15 22:15'
这节我们学习图例 legend
'''


# 同样的是有两种方式,一种是plt的方式,一种是面向对象的方式
# # 第一种方式
# import matplotlib.pyplot as plt
# import numpy as np
#
# x = np.arange(1,11,1)
# plt.plot(x,x**2,label='Normal')
# plt.plot(x,x*2,label='Fast')
# plt.plot(x,1.5**x,label='Faster')
# plt.legend()
# # 加上这个就有图例了,能够将上面的label中的内容作为图例的解释上去
# '''
# 图例还有一些参数
# 比如位置参数,图例搁哪噶达显示
# '''
# plt.show()


# # 第一点一种方式
# import matplotlib.pyplot as plt
# import numpy as np
#
# x = np.arange(1,11,1)
# plt.plot(x,x**2)
# plt.plot(x,x*2)
# plt.plot(x,1.5**x)
# plt.legend(['Normal','fast','slower'])
#
# plt.show()

# 第二种面向对象的方式
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(1,11,1)
fig = plt.figure()
ax = fig.add_subplot(111)

l, = plt.plot(x,x*x)

# 1------------------------------------------------
# ax.legend(['ax legnsd'])
# 2------------------------------------------------
l.set_label('label via method')
ax.legend()
# ------------------------------------------------
plt.show()
```


### chapter15 坐标轴的范围 

```python
'''
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by victor
# Created Time: '2020/2/15 22:32'
'''

# 今天我们来调整一下坐标轴的范围
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-10,11,1)

plt.plot(x,x*x)
# plt.axis([-5,10,0,100])
# axis 调整两个
# plt.axis(xmin=-2)
# xlim 调整单独的一个
plt.xlim([-6,9])
plt.ylim([-5,79])
plt.show()
```

### chapter16 坐标轴的刻度

```python
'''
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by victor
# Created Time: '2020/2/15 22:39'
'''


# 调整坐标轴的刻度

import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-10,11,1)

plt.plot(x,x*x)
ax = plt.gca()  # 获取当前图形的坐标轴
# ax.locator_params(nbins = 25)
ax.locator_params('x',nbins = 25)
'''
这个面向对象是没有交互功能的
所以不能再运行后再python控制台进行设定
如果想要设置就需要使用plt自带的函数来进行设定
'''
plt.show()

```