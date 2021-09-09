---
title: '在自己的服务器上搭建git服务'
cover: "/img/lynk/72.jpg"
date:       2021-09-09
tags:
  - git
  - linux
---

# Git 服务器搭建

上一章节中我们远程仓库使用了 Github，Github 公开的项目是免费的，2019 年开始 Github 私有存储库也可以无限制使用。

这当然我们也可以自己搭建一台 Git 服务器作为私有仓库使用。

接下来我们将以 Centos 为例搭建 Git 服务器。

### 1、安装Git

```
$ yum install curl-devel expat-devel gettext-devel openssl-devel zlib-devel perl-devel
$ yum install git
```

接下来我们 创建一个git用户组和用户，用来运行git服务：

```
$ groupadd git
$ useradd git -g git
```

### 2、创建证书登录

收集所有需要登录的用户的公钥，公钥位于id_rsa.pub文件中，把我们的公钥导入到/home/git/.ssh/authorized_keys文件里，一行一个。

如果没有该文件创建它：

```
$ cd /home/git/
$ mkdir .ssh
$ chmod 755 .ssh
$ touch .ssh/authorized_keys
$ chmod 644 .ssh/authorized_keys
```



### 3、初始化Git仓库

首先我们选定一个目录作为Git仓库，假定是/home/gitrepo/victor.git，在/home/gitrepo目录下输入命令：

```
$ cd /home
$ mkdir gitrepo
$ chown git:git gitrepo/
$ cd gitrepo

$ git init --bare victor.git
Initialized empty Git repository in /home/gitrepo/victor.git/
```

以上命令Git创建一个空仓库，服务器上的Git仓库通常都以.git结尾。然后，把仓库所属用户改为git：

```
$ chown -R git:git victor.git
```

### 4、克隆仓库

```
$ git clone git@116.62.194.162:/home/gitrepo/victor.git
Cloning into 'victor'...
warning: You appear to have cloned an empty repository.
Checking connectivity... done.
```

116.62.194.162 为 Git 所在服务器 ip ，你需要将其修改为你自己的 Git 服务 ip。

这样我们的 Git 服务器安装就完成。

# 参考

https://www.runoob.com/git/git-server.html