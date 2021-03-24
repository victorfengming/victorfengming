---
title: "node的第一个程序"
cover: "/img/lynk/11.jpg"
date:       2019-08-27
tags:
	- node
	- background
	- server
	- basis
---


### helloworld
首先你要保证你的环境中已经安装好node了，关于node的安装可以参考[ubuntu系统下nodejs的安装](https://victorfengming.gitee.io/blog/nodejs-install/)
第一个Node.js程序：Hello World！
### 脚本模式(写入js文件)  
以下是我们的第一个Node.js程序：  
新建一个扩展名为js的文件，添加内容如下  
`console.log("Hello World");`  
保存该文件，文件名为helloworld.js  
切换到该文件的目录，并通过node命令来执行： 
`node helloworld.js`
程序执行后，正常的话，就会在终端输出`Hello World`。

### 交互模式(命令行)
打开终端，键入node进入命令交互模式，可以输入一条代码语句后立即执行并显示结果，例如：

```
$ node
> console.log('Hello World!');
Hello World!
```