---
title: "Python实现递归修改文件扩展名"
cover: "/img/lynk/49.jpg"
date:       2019-11-17
tags:
	- Python
	- solution
---













### 起步
小编今天将博客中的markdown文件上传到[有道云笔记](https://note.youdao.com/web/)中,发现了一个BUG:有道云中只能识别md文件格式,而markdown扩展的名的文件不能被识别,也就不能直接查看到文件的内容,所以精通python的小编当然有办法解决了,小编写了一个python脚本,轻松的实现了批量重命名操作

### 设计思路
- 首先我们要列出根目录中的文件夹和文件列表
- 判断是否为文件夹
    - 是文件进行更改操作
    - 不是文件,进行递归文件夹 
- 然后获取文件名,去除掉文件名中的扩展名
- 更改为自己制定的新的扩展名


### 代码实现
```python
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by 秋叶夏风

# 本模块的功能:<"批量修改文件扩展名(递归)">


# 导入系统模块
import os


def isFile(filePath):  # 修改文件扩展名
    filename = filePath.split('\\')[-1]  # 拆分文件路径获得文件名
    fatherPath = filePath.replace(filename, '')  # 获得父级路径
    split = os.path.splitext(filename)  # 拆分文件名和扩展名
    newname = split[0] + '.md'  # 生成新文件名
    os.chdir(fatherPath)  # 改变当前工作目录到指定的路径
    os.rename(filename, newname)  # 文件重命名


def openDir(filePath):  # 递归文件夹
    pathDir = os.listdir(filePath)  # 返回包含的文件或文件夹的名字的列表
    for filename in pathDir:  # 遍历列表
        childPath = os.path.join(filePath, filename)
        # 判断是否为文件夹
        if os.path.isfile(childPath):
            isFile(childPath)
        else:
            openDir(childPath)

if __name__ == '__main__':

    rootDir = 'D:\\PycharmProjects\\victorfengming.github.io\\_posts'  # 根目录
    pathDir = os.listdir(rootDir)  # 列出根目录下所有内容

    for allDir in pathDir:  # 遍历列表
        filepath = os.path.join(rootDir, allDir)  # 文件路径合成

        # 判断是否为文件夹
        if os.path.isfile(filepath):
            isFile(filepath)
        else:
            openDir(filepath)
```

