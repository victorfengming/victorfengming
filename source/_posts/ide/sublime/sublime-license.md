---
title: 'Sublime弹出更新框解决方案'
cover: "/img/lynk/79.jpg"
date:       2019-10-12
tags:
	- ide
	- solution
	- sublime
---


### 起步
很多新手朋友使用sublime,它是一个开源免费和轻量级的编辑器

但是在使用的过程中,它总是会弹出提示你激活或者更新版本的弹出框,每次都要点击关闭它

今天小编就教大家如何去掉这个弹框

### license的配置
首先,直接就打开软件>

在help选项卡中,选择Enter license

输入下面的激活码

```
ZYNGA INC.
50 User License
EA7E-811825
927BA117 84C9300F 4A0CCBC4 34A56B44
985E4562 59F2B63B CCCFF92F 0E646B83
0FD6487D 1507AE29 9CC4F9F5 0A6F32E3
0343D868 C18E2CD5 27641A71 25475648
309705B3 E468DDC4 1B766A18 7952D28C
E627DDBA 960A2153 69A2D98A C87C0607
45DC6049 8C04EC29 D18DFA40 442C680B
1342224D 44D90641 33A3B9F2 46AADB8F
```
sublimetext3会提示license版本不对,点击取消即可
### 配置设置

在设置文件中加入下面一行,来关闭检查更新
```
"update_check":false,
```
更多关于sublime的快捷设置和快捷键可以参考:[sublime快捷键和设置配置(jetbrains习惯)](https://victorfengming.gitee.io/blog/sublime-keybings-settings/)