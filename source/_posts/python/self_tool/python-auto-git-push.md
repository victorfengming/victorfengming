---
title: "Python实现一行代码推本地git到远程仓库"
date:       2019-09-08
tags:
	- Python
	- solution
	- Git
---





* content
{:toc}






### 普通的方式
刚刚学会git的你想要将你修改的code的文件push到远程仓库中的时候
```
git add .
git commit -m"本次修改就是啥也没动"
git push origin master
```

### 装13的方式
这三条命令应该是很多小伙伴们必须要输入的  
小编这次就教大家用python写一个简单的脚本  
实现,自动push你的git库中的code  

### 具体实现
首先我们需要一个操作系统的OS模块  
```python
import os
# 调用os的system方法
os.system('git add .')
# 这里的参数就相当于在终端中输入的命令
os.system('git commit -m\"python auto push\"')
# 你可以自己定义自己的 commit 说明内容
os.system('git push origin master')
# 最后push到对应的远程库中的某个分之中,就成了
```
编辑文件后,将文件保存为.py格式,例如`everydaypush.py`  
存到你的git库的根目录中  
在终端中执行:
```
python3 everydaypush.py
```
结果如下:
![python auto git push](/img/posts/python/python-auto-git-push.png)

小编后续会升级和完善相应功能,请持续关注~
