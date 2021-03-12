---
title: "关于Python3.7和Python3.6中元组类型数据内存存储问题"
cover: "/img/lynk/41.jpg"
date:       2018-08-16
tags:
	- Python
---












### 关于Python3.7和Python3.6中元组类型数据内存存储问题
小编最近发现了一个瑕疵
当定义一个元组类型的变量后,若在程序后面再定义一个元组变量,这两个元组的内容相同,那么在不同的版本中会出现不同的结果
在Python3.6版本中,解释器将在内存中开辟两个内存空间分别存储两个元组的内容,也就是说,不管后面定义的元组,每个元组都是单独的互补影响的内存空间,用is方法检测结果为False
<br>
### python3.6版本
<br>
<div align="left">
    <img src="/img/posts/technology/20190806224625211tuple.png" >  
</div>
在Python3.7以上版本中,元组将会和数值类型的操作方式类似,若变量内容相同,则只是改变了变量的指向的内存地址,用is方法检测结果为True
<br>
### python3.7版本
<br>
<div align="left">
    <img src="/img/posts/technology/20190806224756626tuple.png" >  
</div>
### python3.8版本
<br>
<div align="left">
    <img src="/img/posts/technology/20190806224651517tuple.png" >  
</div>


