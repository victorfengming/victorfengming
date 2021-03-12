---
title: "MongoDB数据库笔记01"
cover: "/img/lynk/2.jpg"
date:       2020-02-18
tags:
	- Linux
	- deepin
	- database
	- mongodb
	- nosql
---
  
### 什么是MongoDB ?

[尚硅谷 前端视频_MongoDB夯实基础视频](https://www.bilibili.com/video/av21989676?p=2)


[了解非关系型数据库NoSQL-MongoDB |中国 安装使用以及CRUD操作](https://zhenye-na.github.io/2020/01/27/intro-to-mongodb.html)


SQL
    - 结构化关系查询语言
    - 关系数据库全部同SQL来操作
    
1. 安装MongoDB
    - 安装
    - 配置环境变量
        - 安装路径中的bin文件夹的路径
    - 在C盘根目录
        - 创建一个文件夹 data
        - 在data中创建一个文件夹db
    - 打开cmd命令行窗口
        - 输入 mongodb 启动mongodb服务器
        - 32位注意:
            启动服务器时,需要输入如下内容
                mongod --storageEngine=mmapv1
    - 在打开一个cmd窗口
        - 输入有mongo链接mongodb,出现`>`就成了