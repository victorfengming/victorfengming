---
title: "markdown简识"
date:       2019-08-17
tags:
	- skills
	- basis
---



* 目录
{:toc}


<!-- # markdown简识 -->

### MarkDown 概述

Markdown是一种可以使用普通文本编辑器编写的标记语言，通过简单的标记语法，它可以使普通文本内容具有一定的格式。

Markdown 语言在 2004 由约翰·格鲁伯（英语：John Gruber）创建。

Markdown 编写的文档可以导出 HTML 、Word、图像、PDF、Epub 等多种格式的文档。

Markdown 编写的文档后缀为 .md, .markdown。

Markdown具有一系列衍生版本，用于扩展Markdown的功能（如表格、脚注、内嵌HTML等等），这些功能原初的Markdown尚不具备，它们能让Markdown转换成更多的格式，例如LaTeX，Docbook。Markdown增强版中比较有名的有Markdown Extra、MultiMarkdown、 Maruku等。这些衍生版本要么基于工具，如Pandoc；要么基于网站，如GitHub和Wikipedia，在语法上基本兼容，但在一些语法和渲染效果上有改动。

### Markdown 应用
Markdown 能被使用来撰写电子书，如：Gitbook。

当前许多网站都广泛使用 Markdown 来撰写帮助文档或是用于论坛上发表消息。例如：GitHub、简书、reddit、Diaspora、Stack Exchange、OpenStreetMap 、SourceForge等。


### Markdown 编辑器
大家可以使用任意的能够编辑文本文档的编辑器来编辑它，因为markdown只是一种文档格式

这里大家可以参考： [整理：几款好用的Markdown编辑器](https://blog.csdn.net/bat67/article/details/72804251)

### Markdown 查看器
这里小编推荐大家使用Typora

Typora 支持 MacOS 、Windows、Linux 平台，且包含多种主题，编辑后直接渲染出效果。

支持导出HTML、PDF、Word、图片等多种类型文件。

Typora 官网：https://typora.io/

### 最最关键的部分
[天凯同学](https://ttk1907.gitee.io/)整理的markdown的一些demo

由于他写的比较全面，这里小编就给出他的链接供大家学习参考

[Markdown实例](https://ttk1907.gitee.io/2019/08/16/markdown-to-application/)

大家可以去参考参考，也可以关注他

### demo

我展示的是一级标题
=================

我展示的是二级标题
-----------------

| 左对齐 | 右对齐 | 居中对齐 |
| :-----| ----: | :----: |
| 单元格 | 单元格 | 单元格 |
| 单元格 | 单元格 | 单元格 |

* 第一项
* 第二项
* 第三项

+ 第一项
+ 第二项
+ 第三项


- 第一项
- 第二项
- 第三项

> 最外层
> > 第一层嵌套
> > > 第二层嵌套

> 区块中使用列表
> 1. 第一项
> 2. 第二项
> + 第一项
> + 第二项
> + 第三项

>one indee
>one index
>>>third index
>>>>fouth index

* 第一项
    > 菜鸟教程
    > 学的不仅是技术更是梦想
* 第二项

*斜体文本*
_斜体文本_
**粗体文本**
__粗体文本__
***粗斜体文本***
___粗斜体文本___

ZHENGTI[^1]NGHAO  

[^1]:正挺好



创建脚注格式类似这样 [^RUNOOB]。

[^RUNOOB]: 菜鸟教程 -- 学的不仅是技术，更是梦想！！！


```python

for i in range(1,100):
    print(i)

def func(self):
    
    pass

```




