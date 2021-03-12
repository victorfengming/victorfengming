---
title: "GitBook简介"
cover: "/img/lynk/57.jpg"
date:       2020-03-04
subtitle: "带你制作精美的电子书"
tags:
	- Git
	- base
---







原文链接： https://www.jianshu.com/p/421cc442f06c

## 概念
GitBook 是一个基于 Node.js 的命令行工具，可使用 Github/Git 和 Markdown 来制作精美的电子书，GitBook 并非关于 Git 的教程。


## 背景
由于之前都把零散的知识都写在 Gist 上，要查找的时候不是很系统化，所以打算挪到 GitBook 上来统一管理，而且 GitBook 写完编译后可以生成静态页面发布到博客上，逼格满满的样子。


## GitBook 准备工作
### 安装 Node.js
GitBook 是一个基于 Node.js 的命令行工具，下载安装 Node.js，安装完成之后，你可以使用下面的命令来检验是否安装成功。

```
$ node -v
v7.7.1
```

### 安装 GitBook
输入下面的命令来安装 GitBook。

```
$ npm install gitbook-cli -g
```

安装完成之后，你可以使用下面的命令来检验是否安装成功。

```
$ gitbook -V
CLI version: 2.3.2
GitBook version: 3.2.3
```

更多详情请参照 [GitBook 安装文档](https://links.jianshu.com/go?to=https%3A%2F%2Fgithub.com%2FGitbookIO%2Fgitbook%2Fblob%2Fmaster%2Fdocs%2Fsetup.md) 来安装 GitBook。


### 编辑器
可以用 VsCode、Typora 等自己喜欢的来编辑。

## 先睹为快
GitBook 准备工作做好之后，我们进入一个你要写书的目录，输入如下命令。

```
$ gitbook init
warn: no summary file in this book
info: create README.md
info: create SUMMARY.md
info: initialization is finished
```

