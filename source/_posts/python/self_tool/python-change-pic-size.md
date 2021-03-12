---
title: "Python实现修改图片尺寸"
date:       2019-10-13
tags:
	- Python
	- solution
	- basis
---





* content
{:toc}







### 起步
很多小伙伴从网上找的图片可能图片尺寸与自己的需求不符合

今天小编就教大家使用python写一个简单脚本程序实现修改图片的尺寸
### 环境准备
首先我们需要python环境,它的安装可以参考:[python安装以及版本检测](https://victorfengming.gitee.io/2019/08/19/python-install-window/)

其次我们还需要安装一个python图形化的库PIL

PIL的安装,这里我们使用pip来进行安装,关于pip可以参考:[Python pip 安装与使用](https://victorfengming.gitee.io/2019/10/12/python-install-pip/)

pip安装好后,在终端中执行
```
pip install PIL
```
等待安装完成即可

如果安装了pycharm的同学可以在设置中的解释器栏里面直接进行安装

这里小编推荐使用[pycharm](https://victorfengming.gitee.io/2019/09/26/jetbrains-pycharm-introduce/)进行安装

关于它的安装可以参考:[PyCharm的安装以及破解](https://victorfengming.gitee.io/2019/08/16/pycharm-install/)
### 源码参考

```python
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by victor

# 本模块的功能:<更改图片尺寸>

import os
import os.path
from PIL import Image
'''
filein: 输入图片
fileout: 输出图片
width: 输出图片宽度
height:输出图片高度
type:输出图片类型（png, gif, jpeg...）
'''
def ResizeImage(filein, fileout, width, height, type):
  img = Image.open(filein)
  out = img.resize((width, height),Image.ANTIALIAS)
  #resize image with high-quality
  out.save(fileout, type)
if __name__ == "__main__":
  filein = r'./image/plane.png'
  fileout = r'./image/planesm.png'
  width = 50
  height = 50
  type = 'png'
  ResizeImage(filein, fileout, width, height, type)

```

### 相关推荐

<p>关于Python相关内容感兴趣的读者可查看专题：<br>《<a target="_blank" href="//www.jb51.net/Special/645.htm">Python图片操作技巧总结</a>》<br>《<a target="_blank" href="//www.jb51.net/Special/663.htm">Python数据结构与算法教程</a>》<br>《<a target="_blank" href="//www.jb51.net/Special/648.htm">Python Socket编程技巧总结</a>》<br>《<a target="_blank" href="//www.jb51.net/Special/642.htm">Python函数使用技巧总结</a>》<br>《<a target="_blank" href="//www.jb51.net/Special/636.htm">Python字符串操作技巧汇总</a>》<br>《<a target="_blank" href="//www.jb51.net/Special/520.htm">Python入门与进阶经典教程</a>》<br>《<a target="_blank" href="//www.jb51.net/Special/516.htm">Python文件与目录操作技巧汇总</a>》</p>
