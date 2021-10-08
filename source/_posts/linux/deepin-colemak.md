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


在创建一个colemak.desktop

```shell
[Desktop Entry]

Type=Application

Exec=/home/victor/Desktop/qidong.sh

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



```shell
clear lock

keycode  10 = 1 exclam 1 exclam
keycode  11 = 2 at 2 at
keycode  12 = 3 numbersign 3 numbersign
keycode  13 = 4 dollar 4 dollar
keycode  14 = 5 percent 5 percent
keycode  15 = 6 asciicircum 6 asciicircum
keycode  16 = 7 ampersand 7 ampersand
keycode  17 = 8 asterisk 8 asterisk
keycode  18 = 9 parenleft 9 parenleft
keycode  19 = 0 parenright 0 parenright
keycode  20 = minus underscore minus underscore
keycode  21 = equal plus equal plus
keycode  22 = BackSpace BackSpace BackSpace BackSpace
keycode  23 = Tab ISO_Left_Tab Tab ISO_Left_Tab
keycode  24 = q Q q Q
keycode  25 = w W w W
keycode  26 = f F f F
keycode  27 = p P p P
keycode  28 = g G g G
keycode  29 = j J j J
keycode  30 = l L l L
keycode  31 = u U u U
keycode  32 = y Y y Y
keycode  33 = semicolon colon semicolon colon
keycode  34 = bracketleft braceleft bracketleft braceleft
keycode  35 = bracketright braceright bracketright braceright
keycode  36 = Return NoSymbol Return
keycode  37 = Control_L NoSymbol Control_L
keycode  38 = a A a A
keycode  39 = r R r R
keycode  40 = s S s S
keycode  41 = t T t T
keycode  42 = d D d D
keycode  43 = h H h H
keycode  44 = n N n N
keycode  45 = e E e E
keycode  46 = i I i I
keycode  47 = o O o O
keycode  48 = apostrophe quotedbl apostrophe quotedbl
keycode  49 = grave asciitilde grave asciitilde
keycode  50 = Shift_L NoSymbol Shift_L
keycode  51 = backslash bar backslash bar
keycode  52 = z Z z Z
keycode  53 = x X x X
keycode  54 = c C c C
keycode  55 = v V v V
keycode  56 = b B b B
keycode  57 = k K k K
keycode  58 = m M m M
keycode  59 = comma less comma less
keycode  60 = period greater period greater
keycode  61 = slash question slash question
keycode  62 = Shift_R NoSymbol Shift_R
keycode  64 = Alt_L Meta_L Alt_L Meta_L
keycode  65 = space NoSymbol space
keycode  66 = BackSpace BackSpace Delete Delete
keycode 105 = Control_R NoSymbol Control_R
keycode 108 = Mode_switch NoSymbol Mode_switch
keycode 133 = Super_L NoSymbol Super_L
keycode 134 = Super_R NoSymbol Super_R
keycode 135 = Menu NoSymbol Menu

```