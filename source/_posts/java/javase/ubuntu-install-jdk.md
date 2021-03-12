---
title: 'ubuntu系统下Java环境JDK的安装'
date:       2019-09-04
tags:
	- Java
	- ubuntu
	- solution
---


### Debian Linux下安装jdk
### 下载压缩包
官网下载对应的.gz包 [点击下载](https://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html)
### 解压文件
创建一个目录用于存放解压后的文件，并解压缩到该目录下

```
sudo mkdir  /opt/java8
sudo tar -zxvf jdk-8u221-linux-x64.tar.gz -C  /opt/java8
```
### 修改环境变量
`sudo vim ~/.bashrc`

### 进入文件，末尾追加如下内容：
```
export JAVA_HOME=/opt/java8/jdk1.8.0_221      //这里要注意目录要换成自己解压的jdk目录
export JRE_HOME=${JAVA_HOME}/jre  
export CLASSPATH=.:${JAVA_HOME}/lib:${JRE_HOME}/lib  
export PATH=${JAVA_HOME}/bin:$PATH
```    
### 使环境变量生效
```
source ~/.bashrc
```
### 设置系统默认jdk
``` 
sudo update-alternatives --install /usr/bin/java java /opt/java8/jdk1.8.0_211/bin/java 300  
sudo update-alternatives --install /usr/bin/javac javac /opt/java8/jdk1.8.0_211/bin/javac 300  
sudo update-alternatives --install /usr/bin/jar jar /opt/java8/jdk1.8.0_211/bin/jar 300   
sudo update-alternatives --install /usr/bin/javah javah /opt/java8/jdk1.8.0_211/bin/javah 300   
sudo update-alternatives --install /usr/bin/javap javap /opt/java8/jdk1.8.0_211/bin/javap 300
```  
然后执行：
```
sudo update-alternatives --config java
```
### 测试是否安装成功
```
java -version
```
### 突发情况
Ubuntu的桌面不显示任何的快捷方式，而且不能往桌面上移动文件和目录。最简单的是重载桌面。 进入终端，执行以下命令：
```
sudo apt-get update
sudo apt-get install --reinstall ubuntu-desktop
sudo apt-get install unity
sudo shutdown -r now
```