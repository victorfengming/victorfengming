---
title: 'Sublime运行代码'
date:       2019-09-18
subtitle: 'open in browser快捷键设置'
tags:
	- ide
	- solution
	- sublime
---


### 起步
很多小伙伴使用sublime写前端html文件,但是在浏览器打开时,可能会遇到一些问题

比如,不能点击open in browser 实现在浏览器中打开

今天小编就教大家安装一个插件,实现快捷键在浏览器中打开刚编写的html文件

### 安装view in browser插件
首先,直接就打开软件>

按快捷键 `ctrl+shift+P`

### 选择`Package Control`

然后再搜索框输入：pcip

此时我们看见了第一个首选的插件Package Control:Install Package，我们直接回车就好，稍等片刻会再次出现一个搜索框，

### 安装View In Browser插件

输入:view,没有安装的朋友此时框框第一个插件会是[View In Browser],

直接回车即可，如果已经安装了View In Browser插件的会像我一样没有展示那个插件。

### 设置运行代码快捷键

上面我们安装好了view in browser插件，接下来我们开始设置快捷键。

设置的快捷键是"ctrl+shift+b"

点击Preferences > key Bindings 

### 然后在右边空白框的"[]"括号中间内输入：

 { "keys": ["ctrl+shift+b"], "command": "open_in_browser" },

然后ctrl+s保存关闭窗口。
### 最最最关键的一步了
设置html文件默认的打开方式为chrome

然后就成了