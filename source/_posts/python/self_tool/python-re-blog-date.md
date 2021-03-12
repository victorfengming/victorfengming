---
title: "Python实现替换博客文章名中的日期到文件中"
date:       2021-03-06
tags:
	- Python
	- solution
---


## 问题分析


事情是这样的

我原来的博客的日期是在文件名中的,而新的模板中的日期是放到了md文件文件头中

我这几百篇博客当然不能手动修改了,于是小编就利用了一个python中的文件操作和re模块写了一个脚本实现了这个替换功能



## 代码如下


```python
'''
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by victor
# Created Time: '2021/3/6 21:05'
'''

# coding=utf-8
import os
import re

"""
---
title: "Flask 概述"
date:       2021-03-06
tags:
    - Python
    - solution
    - web
    - flask
---



"""

"""
---
layout:     keynote
title:      "Example Post using Keynote Layout"
date:       2021-03-06
subtitle:   "Keynote: JavaScript Modularization Journey"
iframe:     "http://huangxuan.me/js-module-7day/"
date:       2015-07-09
author:     "Hux"
header-img: "post-bg-js-version.jpg"
tags:
    - 前端开发
    - JavaScript
---
"""

def alter(file,old_str,new_str):
    newName = re.sub(r'\d\d\d\d-\d\d-\d\d-', "", file)
    with open(file, "r", encoding="utf-8") as f1,open(newName, "w", encoding="utf-8") as f2:
        for line in f1:

            print("old_str>>>",old_str)
            print("new_str>>>",new_str)
            print("line>>>",line)
            print("==================")
            f2.write(line)
            # 判断 line其那面是不是title
            if line[0:6] == "title:":
                # 说明下一行要追加 date了
                f2.write(new_str)
    os.remove(file)
    # 已经重命名了,不用这个了就
    # os.rename("%s.bak" % file, file)

# dir 是全路径
# 比如: E:\Projects\PycharmProjects\untitled\test\database\redis\2019-09-25-deepin-install-redis.md
# :param dir:
# :return:

def movDate(dir):

    newDir = dir
    # 2. 判断是文件
    if os.path.isfile(dir):
        # print("\t\t\t" + dir + "是文件")
        # print(">>>" + dir[-3:])
        # 2.1 判断是md文件

        if dir[-3:] == ".md":
            # 判断是不是日期开头的md文件,正则
            # print("匹配开始-----------",dir)
            # print(re.search('(\d\d\d\d-\d\d-\d\d)-', dir))
            searchObj = re.search('\d\d\d\d-\d\d-\d\d-', dir)
            # 要是有结果
            if searchObj:
                print(dir + "是日期开头的md文件")
                # 暂存 日期
                date_str = searchObj.group(0)[:-1]
                #         date:       2015-07-09
                # os.rename("原文件名","新文件名"）
                # ? 如何生成新文件名???
                # a = re.sub(r'hello', 'i love the', 'hello world')
                # newName = re.sub(r'\d\d\d\d-\d\d-\d\d-',"",dir)
                # os.rename(dir,newName)
                app_str = "date:       "+date_str+"\n"
                # print("日期是 >>> " + app_str)
                alter(dir, "\ntitle:", app_str)


    # 1. 判断是文件夹
    elif os.path.isdir(dir):
        print(dir + "是文件夹")
        # 1.1 获取列表
        for s in os.listdir(dir):
            # 如果需要忽略某些文件夹，使用以下代码
            # if s == "xxx":
            # continue
            newDir = os.path.join(dir, s)
            # 1.2 循环递归
            movDate(newDir)


movDate('E:\\Projects\\PycharmProjects\\untitled\\test\\database\\mysql4')

# 1. 判断是文件夹
# 1.1 获取列表
# 1.2 循环递归
# 2. 判断是文件
# 2.1 判断是md文件
#    2.1.1 获取文件名
#    2.1.2 切割文件名得到日期
#    2.1.3 暂存文件名其那面的日期
#    2.1.4 读取文件 with方法
#    2.1.5 正则匹配 追加一行 文本
#    2.1.6 吧之前的日期放进去
#    2.1.7 退出


'''

       ┌─┐       ┌─┐ + +
    ┌──┘ ┴───────┘ ┴──┐++
    │                 │
    │       ───       │++ + + +
    ███████───███████ │+
    │                 │+
    │       ─┴─       │
    │                 │
    └───┐         ┌───┘
        │         │
        │         │   + +
        │         │
        │         └──────────────┐
        │                        │
        │                        ├─┐
        │                        ┌─┘
        │                        │
        └─┐  ┐  ┌───────┬──┐  ┌──┘  + + + +
          │ ─┤ ─┤       │ ─┤ ─┤
          └──┴──┘       └──┴──┘  + + + +
                 神兽保佑
                代码无BUG!


'''
```

## 参考
+ [python 修改文件内容3种方法](https://www.cnblogs.com/wc-chan/p/8085452.html)
+ [Python 正则表达式](https://www.runoob.com/python/python-reg-expressions.html)
