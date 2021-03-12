---
title: "Golang安装"
cover: "/img/lynk/13.jpg"
date:       2020-02-26
subtitle: "Go 安装以及配置"
tags:
	- Golang
	- base
---









Golang安装和配置

# ⼀、Golang安装
## （⼀）、下载
在Mac、Windows和Linux三个平台上都⽀持Golang。您可以从
https://golang.org/dl/下载相应平台的⼆进制⽂件。该⽹站在国内不容易访问，
所以可以访问https://www.studygolang.com/dl 进⾏安装软件的下载。

- Mac OS 从https://golang.org/dl/下载osx安装程序。双击启动安装。按照
提示，这应该在/usr/local/go中安装了Golang，并且还会将⽂件
夹/usr/local/go/bin添加到您的PATH环境变量中。
- Windows 从https://golang.org/dl/下载MSI安装程序。双击启动安装并遵
循提示。这将在位置c中安装Golang:\Go，并且还将添加⽬录c:\Go\bin到您
的path环境变量。
- Linux 从https://golang.org/dl/下载tar⽂件，并将其解压到/usr/local。
将/usr/local/go/bin添加到PATH环境变量中。这应该安装在linux中。

# ⼆、 windows系统下安装和配置环境变量
## （⼀）、安装步骤⾮常简单，⼀路到底
## （⼆）、配置环境变量
### 1、配置环境变量
注意：如果是msi安装⽂件，Go语⾔的环境变量会⾃动设置好。
我的电脑——右键“属性”——“⾼级系统设置”——“环境变量”——“系统变量”
假设GO安装于C盘根⽬录
新建：
- GOROOT：Go安装路径（例：C:\Go）
- GOPATH：Go⼯程的路径（例：E:\go）。如果有多个，就以分号分隔添
加

修改：  
Path：在path中增加：C:\Go\bin;%GOPATH%\bin;
需要把GOPATH中的可执⾏⽬录也配置到环境变量中, 否则你⾃⾏下载的第
三⽅go⼯具就⽆法使⽤了

- ⼯作⽬录就是我们⽤来存放开发的源代码的地⽅，对应的也是Go⾥的
GOPATH这个环境变量。这个环境变量指定之后，我们编译源代码等⽣成的
⽂件都会放到这个⽬录下，GOPATH环境变量的配置参考上⾯的安装Go，配
置到Windows下的系统变量⾥。
- GOPATH之下主要包含三个⽬录: bin、pkg、src。bin⽬录主要存放可执
⾏⽂件; pkg⽬录存放编译好的库⽂件, 主要是*.a⽂件; src⽬录下主要存放go
的源⽂件

### 2、查看是否安装配置成功
使⽤快捷键win+R键，输⼊cmd，打开命令⾏提示符，在命令⾏中输⼊
go env # 查看得到go的配置信息
go version # 查看go的版本号

#三、mac系统安装并配置
## （⼀）、安装
双击pkg包，顺着指引，即可安装成功。 在命令⾏输⼊ go version，获取到go的
版本号，则代表安装成功。
## （⼆）、配置环境变量
- 1、打开终端输⼊cd ~进⼊⽤户主⽬录;
- 2、输⼊ls -all命令查看是否存在.bash_profile;
- 3、存在既使⽤vim .bash_profile 打开⽂件;
- 4、输⼊ i 进⼊vim编辑模式；
- 5、输⼊下⾯代码， 其中 GOPATH: ⽇常开发的根⽬录。GOBIN:是GOPATH下的
bin⽬录。
export GOPATH=/Users/steven/Documents/go_project
export GOROOT= /Usr/local/go
export GOBIN=$GOROOT/bin
export PATH=$PATH:$GOBIN
- 6、点击ESC，并输⼊ :wq 保存并退出编辑。可输⼊vim .bash_profile 查看是否
保存成功。
- 7、输⼊source ~/.bash_profile 完成对golang环境变量的配置，配置成功没有提
示。
- 8、输⼊go env 查看配置结果