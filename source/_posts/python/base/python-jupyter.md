---
title: "jupyter浅析"
cover: "/img/lynk/2.jpg"
date:       2019-10-27
tags:
	- Python
	- solution
	- basis
---












### 一、jupyter 起步:简介
Jupyter Notebook是一个开源的Web应用程序，允许用户创建和共享包含代码、方程式、可视化和文本的文档。它的用途包括：数据清理和转换、数值模拟、统计建模、数据可视化、机器学习等等。它具有以下优势：

可选择语言：支持超过40种编程语言，包括Python、R、Julia、Scala等。
分享笔记本：可以使用电子邮件、Dropbox、GitHub和Jupyter Notebook Viewer与他人共享。
交互式输出：代码可以生成丰富的交互式输出，包括HTML、图像、视频、LaTeX等等。
大数据整合：通过Python、R、Scala编程语言使用Apache Spark等大数据框架工具。支持使用pandas、scikit-learn、ggplot2、TensorFlow来探索同一份数据。

### 二、安装与运行
虽然Jupyter可以运行多种编程语言，但Python是安装Jupyter Noterbook的必备条件（Python2.7，或Python3.3以上）。有两种安装方式：使用Anaconda安装或使用pip命令安装。关于安装的全部信息可以在官网读到：安装Jupyter。

#### 2.1使用Anaconda安装

对于小白，强烈建议使用Anaconda发行版安装Python和Jupyter，其中包括Python、Jupyter Notebook和其他常用的科学计算和数据科学软件包。

首先，下载Anaconda。建议下载Anaconda的最新Python 3版本。其次，请按照下载页面上的说明安装下载的Anaconda版本。最后，安装成功！

#### 2.2使用pip命令安装

对于有经验的Python用户，可以使用Python的包管理器pip而不是Anaconda 来安装Jupyter。

如果已经安装了Python3：
```cmd
python3 -m pip install --upgrade pip
python3 -m pip install jupyter
```
如果已经安装了Python2：
```cmd
python -m pip install --upgrade pip
python -m pip install jupyter
```
恭喜，你已经成功安装好了！

#### 2.3运行Jupyter Notebook

成功安装Jupyter Notebook后，在Terminal (Mac / Linux)或Command Prompt(Windows)中运行以下命令就可打开Jupyter Notebook。

jupyter notebook 