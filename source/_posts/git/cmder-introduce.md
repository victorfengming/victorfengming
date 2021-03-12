---
title: "Cmder简介"
date:       2020-03-04
subtitle: "Windows上的程序员神器"
tags:
	- base
	- cmder
---









原文链接:https://zhuanlan.zhihu.com/p/28400466



## 前言
在Windows系统上做开发，总是对其Terminal不满意。无论是CMD还是PowerShell，真是太丑了。现在安利大家一款神器，除了外观好看以外，功能也是强劲的狠。



![](https://pic2.zhimg.com/v2-69ffd0f8964824475ce7b6b518cc3587_1200x500.gif)

![](https://pic4.zhimg.com/80/v2-da7f54e315dcb4f198d7b07ff6d23cd3_720w.jpg)

## 特点
- 便携，解压即可用
- 自带git、ls、curl等命令
- 可设置命令别名
- 丰富的颜色主题（Solarized、Twilight、Ubuntu、xterm、Monokai，甚至接受自定）、可定制字体
- 支持tab分页、同屏多端口（支持水平分割、垂直分割）
- 支持自定terminal，无论是CMD、PowerShell、bash都可以，还可以注入环境变量

![](https://pic4.zhimg.com/v2-69ffd0f8964824475ce7b6b518cc3587_b.jpg)
![](https://pic1.zhimg.com/v2-450db5f7c6c245f53a5b06283b5a5fc0_b.jpg)

## 安装
- 下载链接：[Cmder.net](https://link.zhihu.com/?target=http%3A//cmder.net/)
分别有mini（6MB）和full（84MD）版本，都是portable的，解压即可使用。

占用空间又小，所以直接放在u盘、云盘（像Onedrive、iCloud）里也行，达到多台设备同步设置的效果（我是把设置导出到gist上，更改就手动更新）。

- 解压，双击Cmder.exe运行。

## 外观配置
Font，右键Tab栏空白处，弹出菜单选择Settings，映入眼帘的就是字体设置了。建议使用字体Input Mono、Inconsolata、Consolas、Courier New。还可以加上中文字体，"Main font"设置下方的"Alternative font"添加CJK字体，在设置"Unicode ranges"成CJK的就好了。
Color Schemes，同样是在Settings中，左侧树形菜单中选择Features->Colors，就能来到Scheme设置界面。Cmder自带的Scheme很丰富，也可以通过自定Scheme，应用网络上简洁好看的风格。Github | joonro/ConEmu-Color-Themes提供了当前流行的Scheme安装方式。
Quake Style， 开启后，Cmder就变成了下拉式。按住" ctrl + ` "Cmder就从屏幕上方弹出，焦点转移就收回（可修改成再次按住" ctrl + ` "收回）。开启Quake Style之后极客感很强 !( •̀ ω •́ )!


