---
title: "deepin系统开机自动切换colemak键盘布局"
cover: "/img/lynk/16.jpg"
date:       2021-03-31
author: "victor"
tags:
	- Linux
	- deepin
	- colemak
---


>
> 首先 需要 准备一个启动脚本
> 

比如创建一个名为`qidong.sh`的文件

内容如下

```shell
setxkbmap us -variant colemak
```

将脚本文件粘贴到 `~/.config/autostart`目录下面

![1617188993398](1617188993398.png)

重新启动即可

```shell
reboot
```



参考:

https://blog.csdn.net/BenSYZ/article/details/104520678

http://www.voidcn.com/article/p-bplopzoo-bwq.html

https://baijiahao.baidu.com/s?id=1666002986214880905&wfr=spider&for=pc