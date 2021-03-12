---
title: "python中文件变化监控"
date:       2019-10-10
subtitle: "watchdog"
tags:
	- Python
	- solution
	- system
---





* content
{:toc}






### 起步
在python中文件监控主要有两个库，一个是[pyinotify](https://github.com/seb-m/pyinotify/wiki)，一个是[watchdog](http://pythonhosted.org/watchdog/)。pyinotify依赖于Linux平台的inotify，后者则对不同平台的的事件都进行了封装。因为我主要用于Windows平台，所以下面着重介绍watchdog（推荐大家阅读一下watchdog实现源码，有利于深刻的理解其中的原理）。
watchdog在不同的平台使用不同的方法进行文件检测。在init.py中发现了如下注释：

```
|Inotify|                             Linux 2.6.13+                    ``inotify(7)`` based observer
|FSEvents|                            Mac OS X                         FSEvents based observer
|Kqueue|                              Mac OS X and BSD with kqueue(2)  ``kqueue(2)`` based observer
|WinApi|(ReadDirectoryChangesW)       MS Windows                       Windows API-based observer
|Polling|                             Any                              fallback implementation
```
### 给出示例代码如下：
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

class FileEventHandler(FileSystemEventHandler):
    # 初始化魔术方法
    def __init__(self):
        FileSystemEventHandler.__init__(self)

    # 文件或文件夹移动
    def on_moved(self, event):
        if event.is_directory:
            print("directory moved from {0} to {1}".format(event.src_path,event.dest_path))
        else:
            print("file moved from {0} to {1}".format(event.src_path,event.dest_path))

    # 创建文件或文件夹
    def on_created(self, event):
        if event.is_directory:
            print("directory created:{0}".format(event.src_path))
        else:
            print("file created:{0}".format(event.src_path))

    # 删除文件或文件夹
    def on_deleted(self, event):
        if event.is_directory:
            print("directory deleted:{0}".format(event.src_path))
        else:
            print("file deleted:{0}".format(event.src_path))

    # 移动文件或文件夹
    def on_modified(self, event):
        if event.is_directory:
            print("directory modified:{0}".format(event.src_path))
        else:
            print("file modified:{0}".format(event.src_path))

if __name__ == "__main__":
    # 实例化Observer对象
    observer = Observer()
    event_handler = FileEventHandler()
    # 设置监听目录
    dis_dir = "e:/"
    observer.schedule(event_handler,dis_dir,True)
    observer.start()
    try:
        while True:
            # 设置监听频率(间隔周期时间)
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
```
### 小结
watchdog主要采用观察者模型（废话，从变量命名就可以看出来）。主要有三个角色：observer，event_handler，被监控的文件夹。三者原本是独立的，主要通过observer.schedule函数将三者串起来，意思为observer不断检测调用平台依赖代码对监控文件夹进行变动检测，当发现改变时，通知event_handler处理。最后特别推荐读者有时间可以阅读一下watchdog的源码，写的易懂而且架构很好用
