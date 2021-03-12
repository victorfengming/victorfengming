---
title: '基于autohotkey的colmak布局配置'
date:       2020-01-10
subtitle: '一个极客的键盘布局'
tags:
	- entertainment
	- solution
---


## 前言
大部分同学使用的键盘布局都是QWERTY布局

而科学研究表明,可能这个设计不是最高效率的布局,甚至的有意为了降低打字的效率而研究的，那么当初为什么要这么设计呢？  
关于键盘布局历史故事的详细内容，可以参考：[知乎:键盘布局有哪些种？各种布局的设计出发点是什么？](https://www.zhihu.com/question/20121876/answer/129017959)


**今天小编给大家介绍另一种布局**

## colemak布局

这种键盘布局,根据热力图显示,我们打字中经常使用的按键（比如元音字母a,o,e,i,u）都会被设计在键盘的中间的一排中,这样可以减少我们在打字的过程中的手指的移动,打字的效率自然就会提高

切换这种布局的方式有很多，经过小编汗水亲测以及对比，autohotkey是其中最好的解决方案，因为他是通过脚本进行按键的替换，所以在使用的时候你不需要局限于输入法，你可以使用colmak输入英文，也可以使用它来输入中文（拼音输入）。  
万事开头难，你一开始使用他一定会不适应的，但是只要你坚持打到3个星期，我相信，这个时候你的打字速度足够满足正常的输入需求了。
## autohotkey介绍

AutoHotkey 是一个自动化软件工具，通过热键、热字串或设定的条件自动执行重复性工作。首页 发现 等你来答 登录 加入知乎 AutoHotkey AutoHotkey 是一个自动化软件工具，通过热键、热字串或设定的条件自动执行重复性工作 .

更多详细信息也可以参考[autohotkey官网](https://www.autohotkey.com/) 或者 [中文文档](http://ahkcn.sourceforge.net/docs/AutoHotkey.htm)
## autohotkey安装
在使用autohotkey之前,我们需要进行下载安装

https://autohotkey.com/download/ahk-install.exe

安装后会有文档提示,这里我们可以看[在线的文档](https://wyagd001.github.io/zh-cn/docs/Tutorial.htm#s11),因为这里面有指定语言,可以翻译成中文来阅读

## 如何创建一个脚本
这里面有很多的语法,我们需要实现的功能是创建一个替换键盘位置的脚本,所以不需要过多的了解这个语法和基本数据类型以及流程控制和函数中

```
右键点桌面空白处.
点击"新建"菜单.
点击里面的"AutoHotkey Script"新建一个脚本.
给脚本命名. 备注: 文件名必须带 .ahk 后缀, 例如 MyScript.ahk
找到刚刚新建的脚本并右键点击它.
点击"Edit Script".
一个新窗口被弹出, 也许是记事本. 如果是这样就成功了!
现在你已经创建了一个脚本, 我们需要加点内容到脚本中. 如果需要用到内置命令, 函数和变量, 请查看第 5 节.

这是一个使用 Send 命令创建的一个包含热键的简单脚本, 当你按下热键后, 它会向窗口发送一段文字.

^j::
Send, My First Script
Return
S↓
稍后我们将进行更深入的研究. 在此之前, 我们先解释一下上面的代码:

第一行: ^j:: 是热键. ^ 代表 Ctrl, j 是字母 J. 任何在 :: 左边 的字符表示您需要按下的热键.
第二行: Send, My First Script 表示如何发送按键. Send 是命令, 任何在逗号(,) 之后的内容将会被键入.
第三行: Return. Return 将会成为你最好的朋友. 它将停止执行之后的代码. 当你的脚本包含越来越多的东西时, 使用 Return 会避免很多问题.
保存文件.
双击桌面上的文件来运行它, 打开记事本或者其他可以输入文字的地方然后按下 Ctrl 和 J.
太好了! 你的第一个脚本完成了. 给自己一些奖励, 然后返回阅读本教程的其余部分.
```

## autohotkey使用
其实autohotkey的功能十分的强大,我们这次只是会使用其中的最最基础的功能

我写的脚本代码如下
```ahk
/*
* author:@victorfegming
* address:gitee.com/victorfengming
* 项目下载:https://gitee.com/victorfengming/colmak_autohotkey
* 博客地址:https://victorfengming.gitee.io/
*/


;先看效果:替换后的布局
/*
 `~  1 2 3 4 5 6 7 8 9 0 - = backsp
Tab   Q W F P G J L U Y ; [ ]  \
Back   A R S T D H N E I O " Enterr
LShift  Z X C V B K M , . / RShiftt
Ctrl Win Alt  Space Alt Menu Fn Ctrl
*/

/*

   l u y
 h n e i o '

   up↑down
<< ← ↓ → >> del

*/


;colemak的对应QWERTY键位
e::f
r::p
t::g
y::j
u::l
i::u
o::y
p::;
s::r
d::s
f::t
g::d
j::n
k::e
l::i
`;::o
n::k
; 这里的替换不会影响组合的修饰符
; 比如现在按Ctrl+F就是Ctrl+F,不会是原来的Ctrl+E

;这里是替换大写和退格
CapsLock::BackSpace
;大写切换不会经常用,平时用shift
LShift & CapsLock::CapsLock
;强烈建议这里换成删除,因为删除的按键距离主键盘过远,影响打字效率

;Alt 的 方向组合
<!i::send {up}
<!k::send {Down}
<!j::send {Left}
<!l::send {Right}
<!'::send {Del}
;<h-o> =>> Home End
<!h::send {Home}
<!`;::send {End}


;Alt shift组合方向键
<+<!i::send {Shift down}{up}
<+<!k::send {Shift down}{Down}
<+<!j::send {Shift down}{Left}
<+<!l::send {Shift down}{Right}
<+<!h::send {Shift down}{Home}
<+<!`;::send {Shift down}{End}

;Alt ctrl组合方向键
<^<!i::send {Ctrl down}{up}
<^<!k::send {Ctrl down}{Down}
<^<!j::send {Ctrl down}{Left}
<^<!l::send {Ctrl down}{Right}
<^<!h::send {Ctrl down}{Home}
<^<!`;::send {Ctrl down}{End}

;Alt Ctrl Shift 组合方向键
<^<+<!i::send {Ctrl down}{Shift down}{up}
<^<+<!k::send {Ctrl down}{Shift down}{Down}
<^<+<!j::send {Ctrl down}{Shift down}{Left}
<^<+<!l::send {Ctrl down}{Shift down}{Right}
<^<+<!h::send {Ctrl down}{Shift down}{Home}
<^<+<!`;::send {Ctrl down}{Shift down}{End}

;Alt + ly page↑page↓
<!u::send {PgUp}
<!o::send {PgDn}

;禁止方向键，提醒使用主键盘
up::return
Down::return
Left::return
Right::return


/*
相关知识点:
- 原文地址:http://ahkcn.sourceforge.net/docs/AutoHotkey.htm
- 映射表地址:http://ahkcn.sourceforge.net/docs/KeyList.htm
- :: 表示映射
- send 发送组合键
- `符号用来转义;分号
- 修饰符 Ctrl Alt Shift 对应 ^+!
- down表示按下的状态
- &表示组合键
- <表示只有左边的修饰符生效
- return 啥也不干
*/

```

然后将脚本文件保存成Unicode编码,在桌面双击即可执行脚本

执行过后,你会发现,你的键位立即生效了

如果你想停止,或者暂停,也可以在window的任务栏中,找到对应的图标

右击的菜单中进行相应的设置

如果你想打包成可执行文件,发给没有安装autohotkey的计算机中亦可以使用

操作方式很easy,在脚本文件中右击,选择Compile Script,即可在当前文件夹,生成一个与脚本文件同名的exe可执行文件

## 编辑器
支持autohotkey语法高亮的编辑器很多,小编使用的是sublime

关于它的插件的安装,可以参考[这里](https://packagecontrol.io/packages/AutoHotkey) 

## 项目源代码地址
码云：https://gitee.com/victorfengming/colmak_autohotkey

感觉有帮助的伙伴可以给小编`star`一下


