---
title: "deepin系统安装design compiler"
cover: "/img/lynk/97.jpg"
date:       2019-08-29
tags:
	- Linux
	- deepin
---

### 关于deepin系统安装design compiler的问题解答
Design Compiler是Synopsys综合软件的核心产品。它提供约束驱动时序最优化，并支持众多的设计类型，把设计者的HDL描述综合成与工艺相关的门级设计；它能够从速度、面积和功耗等方面来优化组合电路和时序电路设计，并支持平直或层次化设计.

然而这个软件是基于Linux系统下面的,所以对于一些不经常接触Linux系统的小伙伴们来说,安装这个软件有一定的难度,尤其是在国产的deepin系统下面安装,网上的教程大多数都是在red hat系统或者是ubuntu的系统下面的  

本文列出了 安装design compiler可能会遇到的问题的相应解决办法,redhat系统下面的安装可以参考

secreat data:034f 0000 4db0 0000 2fc0
mac:000c29e1c6fa
hostname:yanganhan
password:

1.sudo apt-get install yum

2.开启权限，新建文件
  usr/synopsys/pt2016、dc2016、scl、license、installer
  其中installer中放入安装文件：pt2016、dc2016、scl、installer3.2
  (运行,解压出安装文件：./SynopsysInstaller3.2.run    /usr/syonpsys/installer/installer3.2)
  在etc/yum.repos.d/放入.repo源文件

3.sudo apt-get install -y lsb-base lsb-core

4.sudo apt-get install lsb

5.sudo apt-get install csh

6.安装：./installer   X3——分别安装dc,scl,pt

7.破解

8（缺libtiff.so.3）
  /usr/lib/i386-linux-gnu/(将libtiff.so.5复制一份改为libtiff.so.3）
  sudo ln -s /usr/lib/i386-linux-gnu/libtiff.so.4  /usr/lib/i386-linux-gnu/libtiff.so.3
  sudo ln -s /usr/lib/i386-linux-gnu/libtiff.so.5  /usr/lib/i386-linux-gnu/libtiff.so.3

9（缺libpng12.so.0）sudo apt-get install libpng12-0

10.lmstat -c /usr/synopsys/license/synopsys.dat
  lmgrd -c /usr/synopsys/license/synopsys.dat

11(备用杀进程license maneger）lmdown -c /usr/synopsys/license/synopsys.dat




