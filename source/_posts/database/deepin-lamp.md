---
title: "Deepin 下安装 LAMP"
cover: "/img/lynk/15.jpg"
date:       2019-09-25
tags:
	- Linux
	- deepin
	- php
	- database
---


ubuntu/deepin linux 下使用 apt-get 安装所需套的软件 LAMP
### 1. 安装 apacache2 

`apt-get install apache2`
配置文件：/etc/apache2/apache2.conf    

`service apache2 start`

`service apache2 stop`

`service apache2 restart`

### 2. 安装 mysql
`sudo apt-get install mysql-server mysql-client`
    
测试：`mysql -u root -p  XXX`

`service mysql start`

`service mysql stop`

`service mysql restart`

注释：安装时提示无法安装等信息，原因是没有更新源（apt-get install update）

### 3. 安装 php7 
`sudo apt-get install php7.0`


### 4.安装其他模块
```
sudo apt-get install libapache2-mod-php7.0
sudo apt-get install php7.0-mysql
```
### 5 安装Redis
`apt-get install redis-server` 
redis 启动 `redis-server`
redis 客户端 `redis-cli`


PHP 还需要安装一些扩展 还没装好 后期待续 ,如有不足之处多多指教