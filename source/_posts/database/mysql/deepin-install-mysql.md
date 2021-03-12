---
title: "一行命令带你安装mysql(deepin系统下)"
date:       2019-09-25
tags:
	- Linux
	- deepin
	- database
	- mysql
---


`sudo apt-get install mysql-server mysql-client`

测试：`mysql -u root -p XXX`

`service mysql start`

`service mysql stop`

`service mysql restart`

注释：安装时提示无法安装等信息，原因是没有更新源（apt-get install update）