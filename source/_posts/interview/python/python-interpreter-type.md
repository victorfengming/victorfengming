---
title: "Python 的解释器种类以及相关特点"
cover: "/img/lynk/82.jpg"
date:       2019-11-28
subtitle: "Python大法好"
tags:
	- Python
	- background
	- interview
---



### CPython
当从Python官方网站下载并安装好Python2.7后，就直接获得了一个官方版本的解释器：Cpython，这个解释器是用C语言开发的，所以叫CPython，在命名行下运行python，就是启动CPython解释器，CPython是使用最广的Python解释器。
### IPython
IPython是基于CPython之上的一个交互式解释器，也就是说，IPython只是在交互方式上有所增强，但是执行Python代码的功能和CPython是完全一样的，好比很多国产浏览器虽然外观不同，但内核其实是调用了IE。
### PyPy
PyPy是另一个Python解释器，它的目标是执行速度，PyPy采用JIT技术，对Python代码进行动态编译，所以可以显著提高Python代码的执行速度。
### Jython
Jython是运行在Java平台上的Python解释器，可以直接把Python代码编译成Java字节码执行。
### IronPython
IronPython和Jython类似，只不过IronPython是运行在微软.Net平台上的Python解释器，可以直接把Python代码编译成.Net的字节码。