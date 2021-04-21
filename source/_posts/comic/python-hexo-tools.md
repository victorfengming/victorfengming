---
title: 'Python实现Hexo工具'
cover: "/img/lynk/84.jpg"
date:       2021-04-17
author:     "victor"
tags:
	- hexo
	- Python
	- node
---

## 写在前面
本工具是通过`Python`脚本实现 `Hexo` 自动 生成 执行 编译 发布的功能

你可以在这里[下载exe](https://victorfengming.gitee.io/file/exe/hexo-tools/hexo-tools-21.4.21.exe) 

## 使用

### 1. exe下载
>将exe文件放在你的任意文件夹中

### 2. file.md
创建 名为`file.md`的文件,在你要写book的目录下

> 注意: 这里file.md文件名不可更改

### 3. 编辑文件内容
类似这样
```markdown
01_JVM内存与垃概述.md
02_如何看术与JVM.md
03_为什学习JVM.md
04_面课程特点.md
```

### 4. 运行

####  hexo-tools-21.4.20.exe

![1618599141367](1618599141367.png)

####  hexo-tools-21.4.21.exe

![1618654713205](1618654713205.png)


### 5. 执行
#### 1：生成md

运行这条选项会根据`file.md`每行的文本生成对应文件

![1618599290568](1618599290568.png)

并且在每个文件中自动加入 一级标题

```markdown
---
title: "qwfp576"
date:   2021-4-18
cover: "/img/lynk/55.jpg"
author: "victor"
---

# qwfp576

```

#### 3. 

这步相当于

在终端直接敲

```shell
hexo clean
hexo g
hexo s
```

编译后,会在当localhost:4000 run

#### 4. git 指令

```shell
git add .
git commit -m\"Commit by hexo tool!!!\"
git push
```

这里 add >>> all

commit的信息的固定的

push时,如果是已经clone下来自己的库,能够直接push

否则要先登录

#### 5. gitee pages

gitee pages 部署,这个update

只有gitee pro 会员才能够 支持自动 更新

但是这里可以通过py提供了一些代码参考

先 tag一个 TODO


## 环境
Python: 3.7

hexo-cli: 4.2.0

Node.js v15.8.0

npm@7.10.0

Pycharm 2021.3

Pyinstaller

Gitee Pages

## Hexo 介绍

一个快速, 简洁且高效的博客框架

让上百个页面在几秒内瞬间完成渲染. Hexo支持Github Flavored Markdown的所有功能, 甚至可以整合Octopress的大多数插件. 并自己也拥有强大的插件系统.

## 实现功能


1. 生成md文件列表,通过读取文件,创建md文件

2. null

3. run 编译 ,html格式以便发布

4. git 自动 push md

5. gitee pages 自动update(dev)



## 代码

### cmder

```python
'''
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by victor
# Created Time: '2021/4/17 0:42'
'''
from datetime import datetime
from random import randint

'''
version: 21.4.21
TODO :         gitee pages auto sync!!!
'''
import os
# import sys
# import re


# dir 是全路径
# 比如: E:\Projects\PycharmProjects\untitled\test\database\redis\2019-09-25-deepin-install-redis.md
# :param dir:
# :return:
class HexoTool:
    def __init__(self,pypath):
        self.sum_file_name = "file.md"
        self.summary_file_name = "SUMMARY.md"
        self.readme_name = "README.md"
        # 当前脚本目录
        # self.pypath = sys.path[0]
        # self.pypath = os.getcwd()
        # self.pypath = input("please input the root path(windows split symbol is \\)\n:")
        self.pypath = pypath
        # self.root_path = self.pypath
        # sour_path source 源 路径
        self.sour_path = self.pypath + "\\" + self.sum_file_name
        # SUMMARY.md 路径
        self.summary_path = self.pypath + "\\" + self.summary_file_name
        print("| self.pypath >>> ",self.pypath)
    def repSpilt(self, path):
        """
        替换路径分隔符
        :param path:
        :return:
        """
        return path.replace("\\", "\\\\")

    def newFile(self, line, dirname):
        '''
        创建文件
        :param line:
        :param dirname:
        :return:
        '''
        print("| gen file >>>")
        # 新建文件的文件名,最后的\n去掉
        newName = dirname + "\\" + line[:-1]
        print("| \t", line[:-1])
        i = datetime.now()
        ran = randint(1,100)
        with open(newName, "w", encoding="utf-8") as f2:
            f2.write("---\n")
            f2.write("title: \"" + line[:-4]+"\"\n")
            f2.write("date:   %s-%s-%s\n" % (i.year, i.month, i.day))
            f2.write("cover: \"/img/lynk/"+str(ran)+".jpg\"\n")
            f2.write("author: \"victor\"\n")
            f2.write("---\n")
            f2.write("\n")
            f2.write("# "+line[:-4]+"\n")

    def for_line(self, file):
        '''
        读取 sm文件,并遍历行
        :param file:
        :return:
        '''
        # 获取目录
        dirname = os.path.dirname(file)
        with open(file, "r", encoding="utf-8") as f1:
            i = 0
            for line in f1:
                if line == "\n":
                    # line 是空行
                    pass
                else:
                    # 判断line是不是最后一行
                    if line[-1] != "\n":
                        # 加上换行
                        line += "\n"

                    i += 1
                    self.newFile(line, dirname)

        print("| gen ", i, "file success!!!")
        print("| path:", dirname)

    def gen_md(self):
        """
        生成md文件
        :return:
        """
        # 获取输入
        print("| -----------------------------------------------------")
        print("| md文件生成器")
        print("| 通过读取file.md文件中的行数来创建文件")
        print("| 生成的文件会和源文件同目录")
        print("| 注意:原有文件会被替换")
        # print("| 请输入源目录文件路径,window用 \ 来分隔文件夹")
        # sourceFile = input(":")

        # E:\Projects\PycharmProjects\untitled\newFile
        # sourceFile = self.pypath + "\\" + "SUMMARY.md"
        sour_path = self.pypath + "\\" + self.sum_file_name
        self.for_line(self.repSpilt(sour_path))
        # os.system('pause')

    def hexo_run(self):
        '''
        运行hexo

        :return:
        '''
        print("| runing...")
        os.chdir(self.pypath)
        os.system("hexo clean")
        os.system("hexo g")
        os.system("hexo s")
        # os.system('pause')

    def replace_sum(self):
        # SUMMARY.md 路径
        # 更新路径
        summary_path = self.pypath + "\\" + self.summary_file_name
        sour_path = self.pypath + "\\" + self.sum_file_name

        # summary_path = self.pypath + "\\" + "SUMMARY.md"
        with open(sour_path, "r", encoding="utf-8") as f1, open(summary_path, "w", encoding="utf-8") as f2:
            i = 0
            for line in f1:
                if line == "\n":
                    # line 是空行
                    pass
                else:
                    # 判断line是不是最后一行
                    i += 1
                    if line[-1] != "\n":
                        # 加上换行
                        line += "\n"
                    f2.write("- [")
                    f2.write(line[:-4])
                    f2.write("](")
                    f2.write(line[:-1])
                    f2.write(")")
                    f2.write("\n")
        print("| gen summary success!!!")
        print("| total effect line:",i)
        # os.system('pause')
    def qucik_git(self):

        os.chdir(self.pypath)
        os.system("git add .")
        os.system("git commit -m\"Commit by Hexo Tools!!!\"")
        os.system("git push")
        # os.system('pause')

    def menu(self):
        # 获取输入
        # print("| =========================================")
        # print("| ================ Hexo tools ================")
        print("| --------------------------- Hexo tools ---------------------------")
        print("| 1：生成md")
        print("| 2: 转换SUMMARY")
        print("| 3: 本地运行")
        print("| 4: 发布Git")
        print("| 0: exit()")
        print("| --------------------------- Hexo tools ---------------------------")
        return input("| choose operation you need：")



if __name__ == '__main__':
    yt = '''
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
    print(yt)
    print("| --------------------------- hexo tools ---------------------------")
    print("| @version: 21.4.23")
    print("| @description: hexo tools auto gen file & build & sync to git")
    print("| @author: victor")
    print("| @site: https://victorfengming.gitee.io/")
    print("| @introduce: https://victorfengming.gitee.io/comic/python-hexo-tools/")
    print("| @readme: https://victorfengming.gitee.io/file/exe/hexo-tools/readme.md")
    print("| @download: https://victorfengming.gitee.io/file/exe/hexo-tools/hexo-tools-21.4.20.exe")
    print("| --------------------------- hexo tools ---------------------------")
    # print("| 注意：使用前请将exe文件放到file.md同级目录下")
    # print("| ========================================")
    # print(os.path.isfile("E:\\Projects\\PycharmProjects\\untitled\\newFiletest\\12.md"))
    # ht = HexoTool(input("please input the root path(windows split symbol is \\)\n:"))
    ht = HexoTool(input("please input the root path(windows split symbol is \\)\n:"))
    while True:
        cho = ht.menu()
        if cho == "1":
            print(1)
            ht.gen_md()
        elif cho == "2":
            print(2)
            ht.replace_sum()
        elif cho == "3":
            print(3)
            ht.hexo_run()
        elif cho == "4":
            print(4)
            ht.qucik_git()
        elif cho == "0":
            # print("| bye~")
            exit(0)



```


```python
# 导包
from tkinter import *
from tkinter import filedialog, messagebox
from hexo_tools import HexoTool

'''

| --------------------------- HexoTool tools ---------------------------
| @version: 21.4.23
| @description: hexo tools auto gen file & build & sync to git
| @author: victor
| @site: https://victorfengming.gitee.io/
| @introduce: https://victorfengming.gitee.io/comic/python-hexo-tools/
| @readme: https://victorfengming.gitee.io/file/exe/hexo-tools/readme.md
| @download: https://victorfengming.gitee.io/file/exe/hexo-tools/hexo-tools-21.4.21.exe
| --------------------------- hexo tools ---------------------------
| TODO : 
|     1. 递归扫描md文件,根据相对路径 生成`SUMMARY.md`
|     2. cmd 日志 放入 tk页面 
|     5. gitee pages auto update by chrome tools 
| --------------------------- hexo tools ---------------------------

'''
class Tk_gui():

    def __init__(self, gt):
        '''
        初始化魔术方法
        用于设置界面的初始状态
        '''
        # 创建tkinter窗口
        self.root = Tk()
        # 设置窗口的标题
        self.root.title('Gitbook Tools')
        # 设置窗口的长和宽,最大值和最小值设置相同,用户不可调整窗口大小
        self.root.minsize(90, 180)
        self.root.maxsize(780, 180)
        self.gt = gt
        self.root_path = ""

        # 初始化
        # 初始化主要url

        # 调用主要逻辑执行函数
        self.main_logic()

    def main_logic(self):
        '''
        主业务逻辑
        :return:
        '''
        # 顶部信息栏
        topp = Frame()
        topp.grid(row=0, column=0)
        # 内容栏
        self.cont = Frame()
        self.cont.grid(row=1, column=0)
        # 输入选项操作
        self.indo = Frame()
        self.indo.grid(row=0, column=1, rowspan=2)

        # 状态栏
        self.stat = Frame()
        self.stat.grid(row=2, column=0)

        # self.get_path()
        self.put_button()

        # 加入主消息循环
        self.root.mainloop()
        # #
        # self.myStdout()  # 实例化重定向类
        # self.restoreStd()  # 恢复标准输出

    def put_button(self):
        '''
        用于绘制顶部菜单
        :param topp:
        :return:
        '''
        # 菜单栏
        # print("| 1：生成md")
        # print("| 2: 转换SUMMARY")
        # print("| 3: 编译>HTML")
        # print("| 4: 发布Git")
        # print("| 0: exit()")
        self.gen_button("设置工作路径", self.get_path).grid(row=0, column=0)
        self.gen_button("生成md", lambda: self.button_run_before(gt.gen_md)()).grid(row=1, column=0)
        # self.gen_button("转换SUMMARY", lambda: self.button_run_before(gt.replace_sum)()).grid(row=2, column=0)
        self.gen_button("localhost运行", lambda: self.button_run_before(gt.hexo_run)()).grid(row=3, column=0)
        self.gen_button("发布Git", lambda: self.button_run_before(gt.qucik_git)()).grid(row=4, column=0)

    def gen_button(self, text, method):
        '''
        生成 button
        :param text:
        :param method:
        :return:
        '''
        return Button(self.cont, text=text, command=method, width=22)

    def get_path(self):
        self.root_path = filedialog.askdirectory()
        print("getpath>>>",self.root_path)
        # 将路径 从 图形类 传入 工具类
        self.gt.pypath = self.root_path


    def button_run_before(self,func):
        # 判断
        # if func != self.get_path and self.root_path == "":
        if self.root_path == "":
            messagebox.showinfo('错误','请先设置工作路径')
            self.get_path()
        else:
            return func
yt = '''
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
print(yt)
print("| --------------------------- hexo tools ---------------------------")
print("| @version: 21.4.21")
print("| @description: hexo tools auto gen file & build & sync to git")
print("| @author: victor")
print("| @site: https://victorfengming.gitee.io/")
print("| @introduce: https://victorfengming.gitee.io/comic/python-hexo-tools/")
print("| @readme: https://victorfengming.gitee.io/file/exe/hexo-tools/readme.md")
print("| @download: https://victorfengming.gitee.io/file/exe/hexo-tools/hexo-tools-21.4.21.exe")
print("| --------------------------- hexo tools ---------------------------")
print("| 注意：使用前请将exe文件放到file.md同级目录下")
# print("| ========================================")
# print(os.path.isfile("E:\\Projects\\PycharmProjects\\untitled\\newFiletest\\12.md"))


# gt = GitbookTool(input("please input the root path(windows split symbol is \\)\n:"))

gt = HexoTool("")

t = Tk_gui(gt)

```