---
title: "Python 最常见的 170 道面试题全解析：2019 版(题目列表)"
cover: "/img/lynk/27.jpg"
date:       2019-11-30
subtitle: "全是干货分享"
tags:
	- Python
	- solution
	- interview
---




<div class="rich_media_content" id="js_content">
    <h3 style="color:inherit;line-height:inherit;font-weight:bold;border-bottom:2px solid rgb(239,112,96);font-size:1.3em;">
        <a name="t0"></a><span
            style="font-size:inherit;line-height:inherit;font-weight:normal;background:rgb(239,112,96);color:rgb(255,255,255);">引言</span><span
            style="vertical-align:bottom;border-bottom:36px solid rgb(239,235,233);border-right:20px solid transparent;"> </span>
    </h3>
    <p style="font-size:inherit;color:inherit;line-height:inherit;">最近在刷面试题,所以需要看大量的 Python
        相关的面试题，从大量的题目中总结了很多的知识，同时也对一些题目进行拓展了，但是在看了网上的大部分面试题不是很满意，一个是有些部分还是 Python2
        的代码，另一个就是回答的很简单，有些关键的题目，也没有点出为什么，最重要的是还有一些复制粘贴根本就跑不通，这种相信大家深有体会吧，这样就导致我们可能需要去找其他人发的类似的教程。难受啊，所以我决定针对市面上大多的
        Python 题目做一个分析，同时也希望大家尽可能的做到举一反三，而不是局限于题目本身。大概就这样吧，有你看过的题目也有你没看到过的。</p>
    <h3 style="color:inherit;line-height:inherit;font-weight:bold;border-bottom:2px solid rgb(239,112,96);font-size:1.3em;">
        <a name="t1"></a><span
            style="font-size:inherit;line-height:inherit;font-weight:normal;background:rgb(239,112,96);color:rgb(255,255,255);">通过本场 Chat，你将获得如下知识点：</span><span
            style="vertical-align:bottom;border-bottom:36px solid rgb(239,235,233);border-right:20px solid transparent;"> </span>
    </h3>
    <ul style="margin-left:16px;" class="list-paddingleft-2">
        <li><p><span style="font-size:inherit;color:inherit;line-height:inherit;">掌握 Python 的基础语法</span></p></li>
        <li><p><span style="font-size:inherit;color:inherit;line-height:inherit;">语法常见的 Python 应用场景</span></p></li>
        <li><p><span style="font-size:inherit;color:inherit;line-height:inherit;">掌握 Python 闭包的使用以及装饰器的使用</span></p>
        </li>
        <li><p><span style="font-size:inherit;color:inherit;line-height:inherit;">生成器和迭代器的使用</span></p></li>
        <li><p><span style="font-size:inherit;color:inherit;line-height:inherit;">常见的设计模式的使用</span></p></li>
        <li><p><span style="font-size:inherit;color:inherit;line-height:inherit;">深浅拷贝的区别</span></p></li>
        <li><p><span style="font-size:inherit;color:inherit;line-height:inherit;">线程、进程、协程的使用</span></p></li>
        <li><p><span style="font-size:inherit;color:inherit;line-height:inherit;">了解 Python 中的元编程和反射</span></p></li>
        <li><p><span style="font-size:inherit;color:inherit;line-height:inherit;">常考的数据结构和算法</span></p></li>
        <li><p><span style="font-size:inherit;color:inherit;line-height:inherit;">爬虫相关知识，网络编程基本知识等</span></p></li>
    </ul>
    <h3 style="color:inherit;line-height:inherit;font-weight:bold;border-bottom:2px solid rgb(239,112,96);font-size:1.3em;">
        <a name="t2"></a><span
            style="font-size:inherit;line-height:inherit;font-weight:normal;background:rgb(239,112,96);color:rgb(255,255,255);">所有题目</span><span
            style="vertical-align:bottom;border-bottom:36px solid rgb(239,235,233);border-right:20px solid transparent;"> </span>
    </h3><h4 style="color:inherit;line-height:inherit;font-weight:bold;font-size:1.2em;"><span
        style="font-size:inherit;color:inherit;line-height:inherit;">语言特性</span></h4>
    <p style="font-size:inherit;color:inherit;line-height:inherit;">1.谈谈对 Python 和其他语言的区别<br>2.简述解释型和编译型编程语言<br>3.Python
        的解释器种类以及相关特点？<br>4.说说你知道的Python3 和 Python2 之间的区别？<br>5.Python3 和 Python2 中 int 和 long 区别？<br>6.xrange 和 range
        的区别？</p><h4 style="color:inherit;line-height:inherit;font-weight:bold;font-size:1.2em;"><span
        style="font-size:inherit;color:inherit;line-height:inherit;">编码规范</span></h4>
    <p style="font-size:inherit;color:inherit;line-height:inherit;">7.什么是 PEP8?<br>8.了解 Python 之禅么？<br>9.了解 dosctring 么？<br>10.了解类型注解么？<br>11.例举你知道
        Python 对象的命名规范，例如方法或者类等<br>12.Python 中的注释有几种？<br>13.如何优雅的给一个函数加注释？<br>14.如何给变量加注释？<br>15.Python 代码缩进中是否支持 Tab
        键和空格混用。<br>16.是否可以在一句 import 中导入多个库?<br>17.在给 Py 文件命名的时候需要注意什么?<br>18.例举几个规范 Python 代码风格的工具</p><h4
        style="color:inherit;line-height:inherit;font-weight:bold;font-size:1.2em;"><span
        style="font-size:inherit;color:inherit;line-height:inherit;">数据类型</span></h4><h5
        style="color:inherit;line-height:inherit;font-weight:bold;font-size:1em;"><span
        style="font-size:inherit;color:inherit;line-height:inherit;">字符串</span></h5>
    <p style="font-size:inherit;color:inherit;line-height:inherit;">19.列举 Python 中的基本数据类型？<br>20.如何区别可变数据类型和不可变数据类型<br>21.将"hello
        world"转换为首字母大写"Hello World"<br>22.如何检测字符串中只含有数字?<br>23.将字符串"ilovechina"进行反转<br>24.Python 中的字符串格式化方式你知道哪些？<br>25.有一个字符串开头和末尾都有空格，比如“
        adabdw ”,要求写一个函数把这个字符串的前后空格都去掉。<br>26.获取字符串”123456“最后的两个字符。<br>27.一个编码为 GBK 的字符串 S，要将其转成 UTF-8 编码的字符串，应如何操作？<br>28.s="info:xiaoZhang
        33 shandong",用正则切分字符串输出['info', 'xiaoZhang', '33', 'shandong']<br>27.怎样将字符串转换为小写？<br>28.单引号、双引号、三引号的区别？<br>29.a
        = "你好 &nbsp; &nbsp; 中国 &nbsp;",去除多余空格只留一个空格。</p><h5
        style="color:inherit;line-height:inherit;font-weight:bold;font-size:1em;"><span
        style="font-size:inherit;color:inherit;line-height:inherit;">列表</span></h5>
    <p style="font-size:inherit;color:inherit;line-height:inherit;">30.已知 AList = [1,2,3,1,2],对 AList 列表元素去重，写出具体过程。<br>31.如何实现
        "1,2,3" 变成 ["1","2","3"]<br>32.给定两个 list，A 和
        B，找出相同元素和不同元素<br>33.[[1,2],[3,4],[5,6]]一行代码展开该列表，得出[1,2,3,4,5,6]<br>34.合并列表[1,5,7,9]和[2,2,6,8]<br>35.如何打乱一个列表的元素？
    </p><h5 style="color:inherit;line-height:inherit;font-weight:bold;font-size:1em;"><span
        style="font-size:inherit;color:inherit;line-height:inherit;">字典</span></h5>
    <p style="font-size:inherit;color:inherit;line-height:inherit;">36.字典操作中 del 和 pop 有什么区别<br>37.按照字典的内的年龄排序</p>
    <pre><code class="hljs"></code><div class="hljs-button {2}" data-title="复制"
                                        onclick="hljs.copyCode(event)"></div></pre>
    <p style="font-size:inherit;color:inherit;line-height:inherit;">38.请合并下面两个字典 a = {"A":1,"B":2},b = {"C":3,"D":4}<br>39.如何使用生成式的方式生成一个字典，写一段功能代码。<br>40.如何把元组("a","b")和元组(1,2)，变为字典{"a":1,"b":2}
    </p><h5 style="color:inherit;line-height:inherit;font-weight:bold;font-size:1em;"><span
        style="font-size:inherit;color:inherit;line-height:inherit;">综合</span></h5>
    <p style="font-size:inherit;color:inherit;line-height:inherit;">41.Python 常用的数据结构的类型及其特性？</p>
    <pre style="font-size:inherit;color:inherit;line-height:inherit;"></pre>
    <p style="line-height:18px;font-size:14px;word-spacing:0px;letter-spacing:0px;font-family:Consolas, Inconsolata, Courier, monospace;color:rgb(169,183,198);background:rgb(40,43,46);margin-left:16px;">
        <span class="hljs-section"
              style="font-size:inherit;line-height:inherit;color:rgb(165,218,45);">A：{1:0,2:0,3:0}</span><br><span
            class="hljs-section" style="font-size:inherit;line-height:inherit;color:rgb(165,218,45);">B：{"a":0,&nbsp;"b":0,&nbsp;"c":0}</span><br><span
            class="hljs-section" style="font-size:inherit;line-height:inherit;color:rgb(165,218,45);">C:&nbsp;{(1,2):0,&nbsp;(2,3):0}</span><br><span
            class="hljs-section" style="font-size:inherit;line-height:inherit;color:rgb(165,218,45);">D:&nbsp;{[1,2]:0,&nbsp;[2,3]:0}</span><br>
    </p>
    <p style="font-size:inherit;color:inherit;line-height:inherit;">42.如何将元组("A","B")和元组(1,2),合并成字典{"A":1,"B":2}<br>43.Python
        里面如何实现 tuple 和 list 的转换？<br>44.我们知道对于列表可以使用切片操作进行部分元素的选择，那么如何对生成器类型的对象实现相同的功能呢？<br>45.请将[i for i in
        range(3)]改成生成器<br>46.a="hello"和 b="你好"编码成 bytes 类型<br>47.下面的代码输出结果是什么？</p>
    <pre style="font-size:inherit;color:inherit;line-height:inherit;"></pre>
    <p style="line-height:18px;font-size:14px;word-spacing:0px;letter-spacing:0px;font-family:Consolas, Inconsolata, Courier, monospace;color:rgb(169,183,198);background:rgb(40,43,46);margin-left:16px;">
        <span class="hljs-attr" style="font-size:inherit;line-height:inherit;color:rgb(165,218,45);">a</span>&nbsp;=&nbsp;(<span
            class="hljs-number" style="font-size:inherit;line-height:inherit;color:rgb(174,135,250);">1</span>,<span
            class="hljs-number" style="font-size:inherit;line-height:inherit;color:rgb(174,135,250);">2</span>,<span
            class="hljs-number" style="font-size:inherit;line-height:inherit;color:rgb(174,135,250);">3</span>,[<span
            class="hljs-number" style="font-size:inherit;line-height:inherit;color:rgb(174,135,250);">4</span>,<span
            class="hljs-number" style="font-size:inherit;line-height:inherit;color:rgb(174,135,250);">5</span>,<span
            class="hljs-number" style="font-size:inherit;line-height:inherit;color:rgb(174,135,250);">6</span>,<span
            class="hljs-number" style="font-size:inherit;line-height:inherit;color:rgb(174,135,250);">7</span>],<span
            class="hljs-number" style="font-size:inherit;line-height:inherit;color:rgb(174,135,250);">8</span>)<br><span
            class="hljs-attr" style="font-size:inherit;line-height:inherit;color:rgb(165,218,45);">a[2]</span>&nbsp;=&nbsp;<span
            class="hljs-number" style="font-size:inherit;line-height:inherit;color:rgb(174,135,250);">2</span><br></p>
    <p style="font-size:inherit;color:inherit;line-height:inherit;">48.下面的代码输出的结果是什么?</p>
    <pre style="font-size:inherit;color:inherit;line-height:inherit;"></pre>
    <p style="line-height:18px;font-size:14px;word-spacing:0px;letter-spacing:0px;font-family:Consolas, Inconsolata, Courier, monospace;color:rgb(169,183,198);background:rgb(40,43,46);margin-left:16px;">
        <span class="hljs-attr" style="font-size:inherit;line-height:inherit;color:rgb(165,218,45);">a</span>&nbsp;=&nbsp;(<span
            class="hljs-number" style="font-size:inherit;line-height:inherit;color:rgb(174,135,250);">1</span>,<span
            class="hljs-number" style="font-size:inherit;line-height:inherit;color:rgb(174,135,250);">2</span>,<span
            class="hljs-number" style="font-size:inherit;line-height:inherit;color:rgb(174,135,250);">3</span>,[<span
            class="hljs-number" style="font-size:inherit;line-height:inherit;color:rgb(174,135,250);">4</span>,<span
            class="hljs-number" style="font-size:inherit;line-height:inherit;color:rgb(174,135,250);">5</span>,<span
            class="hljs-number" style="font-size:inherit;line-height:inherit;color:rgb(174,135,250);">6</span>,<span
            class="hljs-number" style="font-size:inherit;line-height:inherit;color:rgb(174,135,250);">7</span>],<span
            class="hljs-number" style="font-size:inherit;line-height:inherit;color:rgb(174,135,250);">8</span>)<br><span
            class="hljs-attr" style="font-size:inherit;line-height:inherit;color:rgb(165,218,45);">a[5]</span>&nbsp;=&nbsp;<span
            class="hljs-number" style="font-size:inherit;line-height:inherit;color:rgb(174,135,250);">2</span><br></p>
    <h4 style="color:inherit;line-height:inherit;font-weight:bold;font-size:1.2em;"><span
            style="font-size:inherit;color:inherit;line-height:inherit;">操作类题目</span></h4>
    <p style="font-size:inherit;color:inherit;line-height:inherit;">49.Python 交换两个变量的值<br>50.在读文件操作的时候会使用 read、readline
        或者 readlines，简述它们各自的左右<br>51.json 序列化时，可以处理的数据类型有哪些？如何定制支持 datetime 类型？<br>52.json 序列化时，默认遇到中文会转换成
        unicode，如果想要保留中文怎么办？<br>53.有两个磁盘文件 A 和 B，各存放一行字母，要求把这两个文件中的信息合并(按字母顺序排列)，输出到一个新文件 C 中。<br>54.如果当前的日期为
        20190530，要求写一个函数输出 N 天后的日期，(比如 N 为 2，则输出 20190601)。<br>55.写一个函数，接收整数参数 n，返回一个函数，函数的功能是把函数的参数和 n 相乘并把结果返回。<br>56.下面代码会存在什么问题，如何改进？
    </p>
    <pre style="font-size:inherit;color:inherit;line-height:inherit;"></pre>
    <p style="line-height:18px;font-size:14px;word-spacing:0px;letter-spacing:0px;font-family:Consolas, Inconsolata, Courier, monospace;color:rgb(169,183,198);background:rgb(40,43,46);margin-left:16px;">
        <span class="hljs-function" style="font-size:inherit;line-height:inherit;color:rgb(248,35,117);"><span
                class="hljs-keyword" style="font-size:inherit;line-height:inherit;">def</span>&nbsp;<span
                class="hljs-title" style="font-size:inherit;line-height:inherit;color:rgb(165,218,45);">strappend</span><span
                class="hljs-params"
                style="font-size:inherit;line-height:inherit;color:rgb(255,152,35);">(num)</span>:</span><br>&nbsp;&nbsp;&nbsp;&nbsp;str=<span
            class="hljs-string" style="font-size:inherit;line-height:inherit;color:rgb(238,220,112);">'first'</span><br>&nbsp;&nbsp;&nbsp;&nbsp;<span
            class="hljs-keyword" style="font-size:inherit;line-height:inherit;color:rgb(248,35,117);">for</span>&nbsp;i&nbsp;<span
            class="hljs-keyword" style="font-size:inherit;line-height:inherit;color:rgb(248,35,117);">in</span>&nbsp;range(num):<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;str+=str(i)<br>&nbsp;&nbsp;&nbsp;&nbsp;<span
            class="hljs-keyword" style="font-size:inherit;line-height:inherit;color:rgb(248,35,117);">return</span>&nbsp;str<br>
    </p>
    <p style="font-size:inherit;color:inherit;line-height:inherit;">57.一行代码输出 1-100 之间的所有偶数。<br>58.with 语句的作用，写一段代码？<br>59.python
        字典和 json 字符串相互转化方法<br>60.请写一个 Python 逻辑，计算一个文件中的大写字母数量</p><h4
        style="color:inherit;line-height:inherit;font-weight:bold;font-size:1.2em;"><span
        style="font-size:inherit;color:inherit;line-height:inherit;">高级特性</span></h4>
    <p style="font-size:inherit;color:inherit;line-height:inherit;">70.函数装饰器有什么作用？请列举说明？<br>71.Python 垃圾回收机制？<br>72.魔法函数
        __call__怎么使用?<br>73.如何判断一个对象是函数还是方法？<br>74.@classmethod 和@staticmethod 用法和区别<br>75.Python 中的接口如何实现？<br>76.Python
        中的反射了解么?<br>77.metaclass 作用？以及应用场景？<br>78.hasattr() getattr() setattr()的用法<br>79.请列举你知道的 Python 的魔法方法及用途。<br>80.如何知道一个
        Python 对象的类型？<br>81.Python 的传参是传值还是传址？<br>82.Python 中的元类(metaclass)使用举例<br>83.简述 any()和 all()方法<br>84.filter
        方法求出列表所有奇数并构造新列表，a = &nbsp;[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]<br>85.什么是猴子补丁？<br>86.在 Python 中是如何管理内存的？<br>87.当退出
        Python 时是否释放所有内存分配？</p><h4 style="color:inherit;line-height:inherit;font-weight:bold;font-size:1.2em;"><span
        style="font-size:inherit;color:inherit;line-height:inherit;">正则表达式</span></h4>
    <p style="font-size:inherit;color:inherit;line-height:inherit;">88.使用正则表达式匹配出&lt;html&gt;&lt;h1&gt;www.baidu.com&lt;/html&gt;中的地址<br>a="张明
        98 分"，用 re.sub，将 98 替换为 100<br>89.正则表达式匹配中(.*)和(.*?)匹配区别？<br>90.写一段匹配邮箱的正则表达式</p><h4
        style="color:inherit;line-height:inherit;font-weight:bold;font-size:1.2em;"><span
        style="font-size:inherit;color:inherit;line-height:inherit;">其他内容</span></h4>
    <p style="font-size:inherit;color:inherit;line-height:inherit;">91.解释一下 python 中 pass 语句的作用？<br>92.简述你对 input()函数的理解<br>93.python
        中的 is 和==<br>94.Python 中的作用域<br>95.三元运算写法和应用场景？<br>96.了解 enumerate 么？<br>97.列举 5 个 Python 中的标准模块<br>98.如何在函数中设置一个全局变量<br>99.pathlib
        的用法举例<br>100.Python 中的异常处理，写一个简单的应用场景<br>101.Python 中递归的最大次数，那如何突破呢？<br>102.什么是面向对象的 mro<br>103.isinstance
        作用以及应用场景？<br>104.什么是断言？应用场景？<br>105.lambda 表达式格式以及应用场景？<br>106.新式类和旧式类的区别<br>107.dir()是干什么用的？<br>108.一个包里有三个模块，demo1.py,
        demo2.py, demo3.py，但使用 from tools import *导入模块时，如何保证只有 demo1、demo3 被导入了。<br>109.列举 5 个 Python 中的异常类型以及其含义<br>110.copy
        和 deepcopy 的区别是什么？<br>111.代码中经常遇到的*args, **kwargs 含义及用法。<br>112.Python
        中会有函数或成员变量包含单下划线前缀和结尾，和双下划线前缀结尾，区别是什么?<br>113.w、a+、wb 文件写入模式的区别<br>114.举例 sort 和 sorted 的区别<br>115.什么是负索引？<br>116.pprint
        模块是干什么的？<br>117.解释一下 Python 中的赋值运算符<br>118.解释一下 Python 中的逻辑运算符<br>119.讲讲 Python 中的位运算符<br>120.在 Python
        中如何使用多进制数字？<br>121.怎样声明多个变量并赋值？</p><h4
        style="color:inherit;line-height:inherit;font-weight:bold;font-size:1.2em;"><span
        style="font-size:inherit;color:inherit;line-height:inherit;">算法和数据结构</span></h4>
    <p style="font-size:inherit;color:inherit;line-height:inherit;">122.已知：</p>
    <pre style="font-size:inherit;color:inherit;line-height:inherit;"></pre>
    <p style="line-height:18px;font-size:14px;word-spacing:0px;letter-spacing:0px;font-family:Consolas, Inconsolata, Courier, monospace;color:rgb(169,183,198);background:rgb(40,43,46);margin-left:16px;">
        <span class="hljs-attr" style="font-size:inherit;line-height:inherit;color:rgb(165,218,45);">AList</span>&nbsp;=&nbsp;[<span
            class="hljs-number" style="font-size:inherit;line-height:inherit;color:rgb(174,135,250);">1</span>,<span
            class="hljs-number" style="font-size:inherit;line-height:inherit;color:rgb(174,135,250);">2</span>,<span
            class="hljs-number" style="font-size:inherit;line-height:inherit;color:rgb(174,135,250);">3</span>]<br><span
            class="hljs-attr" style="font-size:inherit;line-height:inherit;color:rgb(165,218,45);">BSet</span>&nbsp;=&nbsp;{<span
            class="hljs-number" style="font-size:inherit;line-height:inherit;color:rgb(174,135,250);">1</span>,<span
            class="hljs-number" style="font-size:inherit;line-height:inherit;color:rgb(174,135,250);">2</span>,<span
            class="hljs-number" style="font-size:inherit;line-height:inherit;color:rgb(174,135,250);">3</span>}<br></p>
    <p style="font-size:inherit;color:inherit;line-height:inherit;">(1) 从 AList 和 BSet 中 查找 4，最坏时间复杂度那个大？<br>(2) 从 AList
        和 BSet 中 插入 4，最坏时间复杂度那个大？<br>123.用 Python 实现一个二分查找的函数<br>124.python 单例模式的实现方法<br>125.使用 Python 实现一个斐波那契数列<br>126.找出列表中的重复数字<br>127.找出列表中的单个数字<br>128.写一个冒泡排序<br>129.写一个快速排序<br>130.写一个拓扑排序<br>131.python
        实现一个二进制计算<br>132.有一组“+”和“-”符号，要求将“+”排到左边，“-”排到右边，写出具体的实现方法。<br>133.单链表反转<br>134.交叉链表求交点<br>135.用队列实现栈<br>136.找出数据流的中位数<br>137.二叉搜索树中第
        K 小的元素</p><h4 style="color:inherit;line-height:inherit;font-weight:bold;font-size:1.2em;"><span
        style="font-size:inherit;color:inherit;line-height:inherit;">爬虫相关</span></h4>
    <p style="font-size:inherit;color:inherit;line-height:inherit;">138.在 requests 模块中，requests.content 和 requests.text
        什么区别<br>139.简要写一下 lxml 模块的使用方法框架<br>140.说一说 scrapy 的工作流程<br>141.scrapy 的去重原理<br>142.scrapy 中间件有几种类，你用过哪些中间件<br>143.你写爬虫的时候都遇到过什么？反爬虫措施，你是怎么解决的？<br>144.为什么会用到代理？<br>145.代理失效了怎么处理？<br>146.列出你知道
        header 的内容以及信息<br>147.说一说打开浏览器访问 www.baidu.com 获取到结果，整个流程。<br>148.爬取速度过快出现了验证码怎么处理<br>149.scrapy 和 scrapy-redis
        有什么区别？为什么选择 redis 数据库？<br>150.分布式爬虫主要解决什么问题<br>151.写爬虫是用多进程好？还是多线程好？ 为什么？<br>152.解析网页的解析器使用最多的是哪几个<br>153.需要登录的网页，如何解决同时限制
        ip，cookie,session（其中有一些是动态生成的）在不使用动态爬取的情况下？<br>154.验证码的解决（简单的：对图像做处理后可以得到的，困难的：验证码是点击，拖动等动态进行的？）<br>155.使用最多的数据库（mysql，mongodb，redis
        等），对他的理解？</p><h4 style="color:inherit;line-height:inherit;font-weight:bold;font-size:1.2em;"><span
        style="font-size:inherit;color:inherit;line-height:inherit;">网络编程</span></h4>
    <p style="font-size:inherit;color:inherit;line-height:inherit;">156.TCP 和 UDP 的区别？<br>157.简要介绍三次握手和四次挥手<br>158.什么是粘包？
        socket 中造成粘包的原因是什么？ 哪些情况会发生粘包现象？</p><h4
        style="color:inherit;line-height:inherit;font-weight:bold;font-size:1.2em;"><span
        style="font-size:inherit;color:inherit;line-height:inherit;">并发</span></h4>
    <p style="font-size:inherit;color:inherit;line-height:inherit;">159.举例说明 conccurent.future 的中线程池的用法<br>160.说一说多线程，多进程和协程的区别。<br>161.简述
        GIL<br>162.进程之间如何通信<br>163.IO 多路复用的作用？<br>164.select、poll、epoll 模型的区别？<br>165.什么是并发和并行？<br>167.解释什么是异步非阻塞？<br>168.threading.local
        的作用？</p><h4 style="color:inherit;line-height:inherit;font-weight:bold;font-size:1.2em;"><span
        style="font-size:inherit;color:inherit;line-height:inherit;">Git 面试题</span></h4>
    <p style="font-size:inherit;color:inherit;line-height:inherit;">169.说说你知道的 git 命令<br>170.git 如何查看某次提交修改的内容x</p>
    <p style="font-size:inherit;color:inherit;text-align:center;line-height:normal;letter-spacing:1px;"><br></p>
    <p style="text-align:center;line-height:1.75em;margin-left:16px;"><span style="color:rgb(255,255,255);"><strong>扫描二维码即可看答案</strong></span>
    </p>
    <p style="text-align:center;line-height:1.75em;margin-left:16px;"><span style="color:rgb(255,255,255);"><strong>限时只要 9.9 元</strong></span>
    </p>
    <p style="text-align:center;line-height:1.75em;margin-left:16px;"><span style="color:rgb(255,255,255);"><strong>用一杯奶茶钱</strong></span>
    </p>
    <p style="text-align:center;line-height:1.75em;margin-left:16px;"><span style="color:rgb(255,255,255);"><strong>换取一份 0ffer，</strong><strong>值！</strong></span>
    </p>
    <p style="text-align:center;line-height:1.75em;margin-left:16px;"><span
            style="color:rgb(255,255,255);"><strong>?<strong
            style="color:rgb(255,255,255);font-family:'Helvetica Neue', Helvetica, 'Hiragino Sans GB', 'Microsoft YaHei', Arial, sans-serif;font-size:15px;letter-spacing:2px;text-align:center;word-spacing:2px;">?</strong><strong
            style="color:rgb(255,255,255);font-family:'Helvetica Neue', Helvetica, 'Hiragino Sans GB', 'Microsoft YaHei', Arial, sans-serif;font-size:15px;letter-spacing:2px;text-align:center;word-spacing:2px;">?</strong></strong></span>
    </p>
    <p style="text-align:center;"><img class="rich_pages" style="width:350px;"
                                       src="https://ss.csdn.net/p?https://mmbiz.qpic.cn/mmbiz_jpg/0vU1ia3htaaMiaMtvkvZ6DUk5sTjoFgaicJoHhoT59peP1M4ibAwbp3qlMEoQJ0gK2ORS4RhG3xhmO6bpJn0JPqhJg/640?wx_fmt=jpeg"
                                       alt="640?wx_fmt=jpeg"></p>
</div>