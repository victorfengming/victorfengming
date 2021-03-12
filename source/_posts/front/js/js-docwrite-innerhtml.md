---
title: 'JS中的document.write和innerHTML区别'
date:       2019-09-06
tags:
	- JavaScript
	- web
	- solution
---


链接：https://www.nowcoder.com/questionTerminal/2c5d8105b2694d85b06eff85e871cf50

来源：牛客网 

### 解释一

document.write是直接写入到页面的内容流，如果在写之前没有调用document.open, 浏览器会自动调用open。

每次写完关闭之后重新调用该函数，会导致页面被重写。

innerHTML则是DOM页面元素的一个属性，代表该元素的html内容。

你可以精确到某一个具体的元素来进行更改。

如果想修改document的内容，则需要修改document.documentElement.innerElement。

innerHTML很多情况下都优于document.write，其原因在于其允许更精确的控制要刷新页面的那一个部分。

### 解释二

1.write是DOM方法,向文档写入HTML表达式或JavaScript代码，可列出多个参数，参数被顺序添加到文档中 ；innerHTML是DOM属性,设置或返回调用元素开始结束标签之间的HTML元素。

2.两者都可向页面输出内容,innerHTML比document.write更灵活。

当文档加载时调用document.write直接向页面输出内容，文档加载结束后调用document.write输出内容会重写整个页面。

通常按照两种的方式使用 write() 方法：一是在使用该方在文档中输出 HTML，二是在调用该方法的的窗口之外的窗口、框架中产生新文档（务必使用close关闭文档）。

在读模式下，innerHTML属性返回与调用元素的所有子节点对应的HTML标记，在写模式下，innerHTML会根据指定的值创建新的DOM树替换调用元素原先的所有子节点。

3.两者都可动态包含外部资源如JavaScript文件

通过document.write插入<script>元素会自动执行其中的脚本；

大多数浏览器中，通过innerHTML插入<script>元素并不会执行其中的脚本。