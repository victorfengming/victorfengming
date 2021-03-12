---
title: "更改Ubuntu默认Python版本方法"
cover: "/img/lynk/25.jpg"
date:       2018-08-19
tags:
	- Python
	- background
	- ubuntu
---












### 查看首先查看Python3默认版本:
```python
victor@victor:/$ python3
Python 3.5.3 (default, Sep 27 2018, 17:25:39) 
[GCC 6.3.0 20170516] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> 
```
### 搜索系统是否已经安装Python3.7:   

victor@victor:/$ `which python3.7`  
`/usr/local/bin/python3.7`  

这样通过which查看python3.7可执行文件的位置，这个目录后面要用

### 在当前用户下修改 Python3 版本：
victor@victor:/$ `alias python3='/usr/local/bin/python3.7'`     
这里填入刚才查询到的路径  
### 一旦完成以上操作，重新登录或者重新加载 .bashrc 文件，使操作生效。  
victor@victor:/$ `. ~/.bashrc`
### 然后就成了，检查一下
```
victor@victor:/$ python3
Python 3.7.0 (default, Aug 30 2019, 14:02:26) 
[GCC 6.3.0 20170516] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> 
```   
整体挺好吧

### 参考文献
博客园：[Fugui：更改Ubuntu默认python版本的方法](https://www.cnblogs.com/yifugui/p/8649864.html)   
简  书：[给我二两面
：更改Ubuntu默认Python版本方法](https://www.jianshu.com/p/9d3033d1b26f)