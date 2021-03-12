---
title: "git工具基础"
date:       2019-08-17
tags:
	- Git
	- basis
---













<!-- # git工具起步 -->
### 关于版本控制
版本控制是一种记录一个或若干文件内容变化，以便将来查阅特定版本修订情况的系统。
### 本地版本控制系统
版本控制在开发中都是不可避免的问题，最简单的常规方法是通过拷贝整个项目进行控制以及更改，但是这种方法会存在这很多弊端
比如说，多人协同工作开发过程中版本的合并问题，找回历史版本的时候有可能会混淆各个版本之间的改动的区别。
就算你加上了修改的时间作为项目的名称还是有点瑕疵的
<br>
这时候，为了解决这个问题，好早以前就开发了许多种本地版本控制系统，大多都是采用某种简单的数据库来记录文件的历次更新差异
<br>
<img src="https://gitee.com/progit/figures/18333fig0101-tn.png">
<br>
比如有一种叫做rcs，说白了就是保存并管理文件补丁（patch）。
文件补丁是一种特定格式的文本文件，记录着对应文件修订前后的内容变化。
所以，根据每次修订后的补丁，rcs可以通过不断打补丁，计算出各个版本的文件内容。
### 集中化的版本控制系统
但是现在会出现一个问题，就是说我要是在本地管理我的版本的时候，只能我自己用，如果多人协同开发就费劲了
于是，集中化的版本控制系统CVCS应运而生。这种系统的话，都带着一个单一的集中管理的服务器，用于保存所有文件的修订版本，而协同工作的人们都通过客户端连到这台服务器，取出最新的文件或者提交更新，这样就使用起来十分方便了。到现在，这已成为版本控制系统的标准做法（见图 1-2）。
<br>
<img src="https://gitee.com/progit/figures/18333fig0102-tn.png">
<br>
这种方式好处很多，比如任何人都可以在修改项目的时候能够看到其他人都在修改什么，管理员可以方便管理每个人的修改权限，而且维护服务端也比本地端的更加方便
<br>
但是这种方式也有点缺点，就是如果服务器的磁盘出现故障，最坏会导致整个项目全部丢失，而这时本地端可能会没有全部的项目来进行恢复的
而git的clone方式，会解决这个问题，因为git的克隆操作会将服务端的项目所有记录到本地化。
### 分布版本控制
这种就是现在主流的类型了，git就是最具有代表性的


### 协议
本地协议
SSH 协议
Git 协议
HTTP/S 协议




### 有用的链接地址 
[git checkout 命令详解](https://www.cnblogs.com/kuyuecs/p/7111749.html)   
[参与github上开源项目的大致流程和注意事项](https://www.cnblogs.com/metoy/p/4097001.html)   
[Git SSH公钥配置](https://www.cnblogs.com/yangshifu/p/9919817.html)  
[初次使用git配置以及git如何使用ssh密钥（将ssh密钥添加到github）](https://www.cnblogs.com/superGG1990/p/6844952.html)  
[github上分支的合并](https://www.cnblogs.com/leilei0327/p/8688244.html)  
[参与github上开源项目的大致流程和注意事项](https://www.cnblogs.com/metoy/p/4097001.html)  
[git fetch命令](https://www.yiibai.com/git/git_fetch.html)  
[git 醉拳版本](https://blog.csdn.net/shimazhuge/article/details/52759429)
[git 最全命令](https://blog.csdn.net/weixin_39220472/article/details/82712490)
[Git-分支-变基](https://git-scm.com/book/zh/v2/Git-%E5%88%86%E6%94%AF-%E5%8F%98%E5%9F%BA)
