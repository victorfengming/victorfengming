---
title: "vim编辑器不能使用backspace问题解决方案"
date:       2019-08-22
subtitle: "在ubuntu系统中"

tags:
	- vim
	- solution
	- ubuntu
	- Linux
---

### 在 ubuntu 的命令行中使用 vi 命令编辑文件，遇到方向键与退格键无法正常使用时可通过如下方式解决 ：

### 第一步
1、打开 /etc/vim/vimrc.tiny 文件，
```cmd
cd /etc/vim  
sudo gedit vimrc.tiny  
```
### 第二步  
在编辑器中  
将“compatible”改成“nocompatible”非兼容模式  
这样就可以解决方向键变 ABCD 的问题了。
### 第三步  
添加 set backspace=2 语句，这样 Backspace 退格键恢复正常使用。  
完美解决  
