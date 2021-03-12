---
title: "python中的单例模式"
cover: "/img/lynk/62.jpg"
date:       2018-11-10
tags:
	- Python
	- solution
	- basis
---

### 单例模式
单例模式（Singleton Pattern）是一种常用的软件设计模式，该模式的主要目的是确保某一个类只有一个实例存在。当你希望在整个系统中，某个类只能出现一个实例时（如软件配置类，无论在软件的什么地方实例化，永远都是那一个对象），单例模式就能派上用场。比如，Python 日志模块中的日志对象，或者异步通讯框架 twisted 里面的反应堆(reactor)，都是典型的单例模式——尽管它们不一定是下面这种方法实现的。

### python可以使用装饰器的方法使用单例模式：

```python
def Singleton(cls):
    _instance = {}

    def _singleton(*args, **kargs):
        if cls not in _instance:
            _instance[cls] = cls(*args, **kargs)
        return _instance[cls]

    return _singleton

@Singleton
class Config(object):
    pass

cfg1 = Config()
cfg2 = Config()

print(cfg1 is cfg2)

```

### 结果如下
```cmd
D:\Python37\python.exe D:/PycharmProjects/QT_pro/re_demo.py
True

Process finished with exit code 0
```