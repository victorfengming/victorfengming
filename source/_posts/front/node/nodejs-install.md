---
title: "ubuntu系统下nodejs的安装"
date:       2019-08-27
tags:
	- node
	- background
	- solution
	- ubuntu
---





* content
{:toc}







## nodejs安装
推荐使用方法1进行安装
### 方法1：
```
curl -sL https://deb.nodesource.com/setup_8.x | sudo -E bash -
sudo apt-get install -y nodejs
```
##### 如果安装nodejs 9.x版本
```
curl -sL https://deb.nodesource.com/setup_9.x | sudo -E bash -
sudo apt-get install -y nodejs
```
方法一使用了NodeSource提供的二进制包进行安装，NodeSource提供了常用的Linux系统（Ubuntu,CentOS,RedHat,Debian等）安装Node的二进制包，具体简介可以访问Linux通过二进制包安装nodejs

### 方法2：  
在nodejs官方网站download页面中选择需要使用的版本,可以选择LTS或current,选择对应系统右键复制链接地址
![node官网](/img/posts/node/node-install.png)  

如果需要下载历史版本可以选择download页面底部PreviousReleases,也可以直接访问http://nodejs.org/dist/或https://nodejs.org/download/release/  

![historyversion](/img/posts/node/node-install2.png)

当然你也可以使用[淘宝](https://www.taobao.com/)npm镜像下载对应的[node版本](https://npm.taobao.org/mirrors/node/)  

##### 下载nodejs压缩文件  
`wget https://nodejs.org/dist/v8.1.0/node-v8.1.0-linux-x64.tar.xz`
##### 解压  
`tar -xvf node-v8.1.0-linux-x64.tar.xz`

##### 切换并查看当前node所在路径
```
cd node-v8.1.0-linux-x64/bin
pwd
```
##### 查看node版本
`./node -v`

##### 将node和npm设置为全局
```
sudo ln /home/ubuntu/node-v8.1.0-linux-x64/bin/node /usr/local/bin/node
sudo ln /home/ubuntu/node-v8.1.0-linux-x64/bin/npm /usr/local/bin/npm
pwd
```

### 方法3
也可以使用ubuntu自带apt-get安装,安装后使用node -v查看版本  
```
sudo apt-get install nodejs-legacy nodejs
sudo apt-get install npm
```

安装完成
推荐使用方法一，直接安装在系统环境/usr/bin目录下，之后使用npm -g安装其他插件也会安装到/usr/lib/node_modules’(需要使用sudo权限)‘。
如果使用方法二，将nodejs路径链接到/usr/local/bin目录下，则每次npm -g安装插件都会安装在nodejs原路径下的node_modules(比如/home/ubuntu/node-v8.1.0-linux-x64/lib/node_modules)，每次代码中引用插件也需要到此目录下去找

原文链接：https://blog.csdn.net/w20101310/article/details/73135388