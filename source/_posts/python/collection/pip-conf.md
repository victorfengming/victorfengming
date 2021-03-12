---
title: "pip配置"
cover: "/img/lynk/93.jpg"
date:       2019-11-20
subtitle: "默认使用国内镜像地址"
tags:
	- Python
	- solution
	- basis
---

pycharm用户看[这里](https://blog.csdn.net/kermitJam/article/details/82315974)

很多小伙伴在ubuntu系统下,使用pip安装会很慢

以为安装源在国外服务器上面

今天小编就教大家配置成让pip默认从国内源中寻找安装包

首先Ctrl+Alt+T打开终端


进入家目录
```Shell
cd ~
```
在家目录中创建一个文件夹,命名为`.pip`
```Shell
mkdir .pip
```
进入目录,并创建一个名为`pip.conf`的文件
```Shell
cd .pip
touch pip.conf
```

使用vim编辑文件内容,如下
```Shell
[global]
index-url = https://pypi.tuna.tsinghua.edu.cn/simple
[install]
trusted-host=mirrors.aliyun.com
```

使用wq保存并退出,即可

在以后使用pip安装python模块的时候,默认就从国内来进行安装了,赶紧去试一下吧!

附加:豆瓣源

```
https://pypi.douban.com/simple
```