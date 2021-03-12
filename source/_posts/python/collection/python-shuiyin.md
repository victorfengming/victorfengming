---
title: "Python脚本实现图片加水印"
cover: "/img/lynk/13.jpg"
date:       2019-11-25
subtitle: "Pillow库"
tags:
	- Python
	- background
	- solution
---








### 起步
图片是指由图形、图像等构成的平面媒体,有形式的事物，我们看到的，是图画、照片、拓片等的统称。

为了保护一些原创图片的版权,某些时候我们需要在图片上面,加上水印,当然你可以用Photoshop来做,只不过如果图片数量过多,亦或者图片的动态生成的时候,使用ps将会稍有吃力.


今天小编就交大家用python写一个脚本,实现图片加水印

### 环境搭建
python3.7 环境:[python安装以及版本检测](https://victorfengming.gitee.io/2019/08/19/python-install-window/)

pycharm2019:[PyCharm的安装以及破解](https://victorfengming.gitee.io/2019/08/16/pycharm-install/)

pillow库的安装

```
pip install pillow
```


关于pip的安装,可以参考:[Python pip 安装与使用
](https://victorfengming.gitee.io/2019/10/12/python-install-pip/)和[pip配置](https://victorfengming.gitee.io/2019/11/20/pip-conf/)


### 直接就上代码


```python
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by 秋叶夏风

# 本模块的功能:<图片加水印>


# 导入所需要的库
from PIL import Image, ImageDraw, ImageFont

im = Image.open("6.jpg").convert('RGBA')
# 6.jpg的需要加图片的地址
txt = Image.new('RGBA', im.size, (0, 0, 0, 0))
# 定义字体对象
fnt = ImageFont.truetype("c:/Windows/fonts/Tahoma.ttf", 20)
d = ImageDraw.Draw(txt)
# 设置水印内容,字体
d.text((txt.size[0] - 80, txt.size[1] - 30), "shuiyin", font=fnt, fill=(255, 255, 255, 255))
out = Image.alpha_composite(im, txt)
# 显示图片
out.show()

```
