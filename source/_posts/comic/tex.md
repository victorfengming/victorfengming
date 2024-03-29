---
title: '关于TeX排版系统简介'
cover: "/img/lynk/63.jpg"
date:       2020-02-18
subtitle: '概念辨析理解--TEX、LATEX、TEXLive和Lyx的区别和联系'
tags:
	- entertainment
	- base
---




## 先说说TEX和LATEX
### TEX
TEX是诞生于20世纪70年代末到80年代初的一款计算机排版软件，而且是命令行格式的（如下图），用来排版高质量的书籍，特别是包含有数学公式的书籍。TEX以追求高质量为目标，很早就实现了矢量描述的计算机字体、细致的分页断行算法和数学排版功能，因其数学排版能力得到了学术界的广泛使用，也启发了后来复杂的商业计算机排版软件。

### LATEX
LATEX开始于20世纪80年代初，是Leslie Lamport博士为了编写自己的一部书籍而设计的。LATEX是对TEX的封装和拓展，实际上就是用TEX语言编写的一组宏代码，拥有比原来TEX格式（Plain TEX）更为规范的命令和一整套预定义的格式，隐藏了不少排版方面的细节，可以让完全不懂排版理论的学者们也可以比较容易地将书籍和文稿排版出来。

## 再说TEXLive和Lyx

由于TEX/LATEX并不是单独的程序，现在的TEX系统都是复杂的软件包，里面包含各种排版的引擎、编译脚本、格式转换工具、管理界面、配置文件、支持工具、字体及数以千计的宏包和文档。一个TEX发行版就是把所有这样的部件都集合起来，打包发布的软件。

### TEXLive
TEXLive是TEX的一个发行版，它是由TUG（TEX User Group，TEX用户组）发布的，可以在类UNIX/Linux、Mac OS X和Windows等不同的操作系统平台下安装使用，并且提供相当可靠的工作环境。
常用的两种安装方式：
1.从TEXLive光盘进行安装；
2.从网络在线安装（参见本人博文：http://blog.csdn.net/qq_33429968/article/details/62928742）。

### Lyx
Lyx是一个编辑软件，简单点说就是，Lyx = Word面孔 + LaTeX核心。