---
title: "Python实现从文件中读取文件名,并创建文件"
cover: "/img/lynk/98.jpg"
date:       2021-03-08
tags:
	- Python
	- solution
---



## 代码

```python
"""
根据文件内容,创建文件
"""
def newFile(file):
    with open(file, "r", encoding="utf-8") as f1:
        for line in f1:
            print("==================")
            # 新建文件的文件名,最后一行的\n去掉
            newName = line[:-1]
            print(newName)
            with open(newName, "w", encoding="utf-8") as f2:
                f2.write("#"+line)


newFile("D:\\WebstormProjects\\react\\sgg\\README.md")
```

问题分析

这个创建的文件的位置是在脚本的同级目录,但是我这里想要创建到readme.md文件同级目录中
## 升级版本

获取文件夹路径

>os.path.dirname()
>
>

```python
"""
根据文件内容,创建文件
"""
def newFile(file):
    # 获取目录
    dirname = os.path.dirname(file)
    with open(file, "r", encoding="utf-8") as f1:
        for line in f1:
            print("==================")
            # 新建文件的文件名,最后一行的\n去掉
            newName = dirname+"\\"+line[:-1]
            print(newName)
            with open(newName, "w", encoding="utf-8") as f2:
                f2.write("# "+line)


newFile("D:\\WebstormProjects\\react\\sgg\\README.md")
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


## 升级版本
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

# dir 是全路径
# 比如: E:\Projects\PycharmProjects\untitled\test\database\redis\2019-09-25-deepin-install-redis.md
# :param dir:
# :return:

def repSpilt(path):
    return path.replace("\\","\\\\")
"""
根据文件内容,创建文件
"""
def newFile(file):
    # 获取目录
    dirname = os.path.dirname(file)
    with open(file, "r", encoding="utf-8") as f1:
        for line in f1:
            print("=========================================")
            # 新建文件的文件名,最后一行的\n去掉
            newName = dirname+"\\"+line[:-1]
            print(newName)
            with open(newName, "w", encoding="utf-8") as f2:
                f2.write("# "+line[:-3])

if __name__ == '__main__':
    # 获取输入
    print("=========================================")
    print("md文件生成器,通过读取文件中的行数来创建文件")
    print("生成的文件会和源文件同目录")
    print("注意:原有文件会被替换")
    print("请输入源目录文件路径,window用 \ 来分隔文件夹")
    print("| 比如: E:\Projects\PycharmProjects\untitled\md2\catlog.md |")
    sourceFile = input(":")
    newFile(repSpilt(sourceFile))

```

## 利用工具 生成 exe 使用

![](QQ截图20210316212803.png)
![](QQ截图20210316213741.png)
![](QQ截图20210316213906.png)


