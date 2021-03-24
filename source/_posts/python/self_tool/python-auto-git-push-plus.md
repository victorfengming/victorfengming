---
title: "Python实现自动推本地github博客到远程仓库"
cover: "/img/lynk/31.jpg"
date:       2019-09-08
tags:
	- Python
	- solution
	- Git
	- system
---












### 以前的简单版本
通过python中的os模块操作系统命令  
详情可参考:[Python实现一行代码推本地git到远程仓库](https://victorfengming.gitee.io/blog/python-auto-git-push/)

### 升级版本
本次加入了监听文件修改功能  
这样脚本只需在后台运行,即可检测到对应的文件夹中的内容是否变化

如果变化,则调用自动push函数,即可实现推本地仓库到远程中

### 依赖库的配置
这里我们需要用到一个库watchdog

关于它的安装和使用可以参考:[python中文件变化监控-watchdog](https://victorfengming.gitee.io/blog/python-listen-dir/)

### 代码如下:
```python
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by victor

# 本模块的功能:<检测文件夹变化>

# 导入watchdog对应模块
from watchdog.observers import Observer
from watchdog.events import *
# 导入时间模块
import time
# 导入系统模块
import os


def push(change):
    print('-'*76)
    os.system('git add .')
    os.system('git commit -m\"auto'+change+'\"')
    os.system('git push -u origin master')
    print('-'*76)


class FileEventHandler(FileSystemEventHandler):
    # 初始化魔术方法
    def __init__(self):
        FileSystemEventHandler.__init__(self)

    # 文件或文件夹移动
    def on_moved(self, event):
        if event.is_directory:
            print("directory moved from {0} to {1}".format(event.src_path, event.dest_path))
        else:
            print("file moved from {0} to {1}".format(event.src_path, event.dest_path))
            # 这里我们只判断文件修改,如需加入文件夹修改,只需在上面的if条件中调用push函数即可
            push("文件移动: {0} to {1}".format(event.src_path, event.dest_path))

    # 创建文件或文件夹
    def on_created(self, event):
        if event.is_directory:
            print("directory created:{0}".format(event.src_path))
        else:
            print("file created:{0}".format(event.src_path))
            push("创建文件:{0}".format(event.src_path))

    # 删除文件或文件夹
    def on_deleted(self, event):
        if event.is_directory:
            print("directory deleted:{0}".format(event.src_path))
        else:
            print("file deleted:{0}".format(event.src_path))
            push("删除文件:{0}".format(event.src_path))

    # 移动文件或文件夹
    def on_modified(self, event):
        if event.is_directory:
            print("directory modified:{0}".format(event.src_path))
        else:
            print("file modified:{0}".format(event.src_path))
            push("文件修改:{0}".format(event.src_path))


if __name__ == "__main__":
    # 实例化Observer对象
    observer = Observer()
    event_handler = FileEventHandler()
    # 设置监听目录
    dis_dir = "./_posts/"
    observer.schedule(event_handler, dis_dir, True)
    observer.start()
    try:
        while True:
            # 设置监听频率(间隔周期时间)
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

```
