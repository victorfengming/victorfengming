---
title: "Python的编码命名规则"
date:       2019-11-28
subtitle: "总结前人之精华，去其糟粕"
tags:
	- Python
	- solution
	- interview
---



<article class="_2rhmJa">
    <ul>
        <li>
            <h3>项目名</h3>
        </li>
    </ul>
    <blockquote>
        <p>首字母大写，其余小写单词，若多个单词组合可以添加“_”下划线增加可读性<br>
            Ui_test</p>
    </blockquote>
    <ul>
        <li>
            <h3>包名、模块名</h3>
        </li>
    </ul>
    <blockquote>
        <p>全部小写字母<br>
            package、 module</p>
    </blockquote>
    <ul>
        <li>
            <h3>类名</h3>
        </li>
    </ul>
    <blockquote>
        <p>首字母大写，其它字母小写，若多个单词时，才用驼峰，eg：UserLogin<br>
            class Login :</p>
    </blockquote>
    <ul>
        <li>
            <h3>方法名</h3>
        </li>
    </ul>
    <blockquote>
        <p>小写单词，多个单词时，用下划线分隔单词以增加可读性。<br>
            def user_login():</p>
    </blockquote>
    <ul>
        <li>
            <h3>参数名</h3>
        </li>
    </ul>
    <blockquote>
        <p>小写单词<br>
            def user_login(self):<br>
            如果函数的参数名与保留关键字冲突，在参数名后加一个下划线，比用缩写、错误 的拼写要好。因此 "_print" 比 "prnt" 好。</p>
    </blockquote>
    <ul>
        <li>
            <h3>普通变量名</h3>
        </li>
    </ul>
    <blockquote>
        <p>小写字母，单词之间用<em>分割 或者 遵守驼峰原则命名<br>
            month_pay = 2000<br>
            monthPay = 2000<br>
            <em>注意</em>：<br>
            1.不论是类成员变量还是全局变量，均不使用 m 或 g 前缀。<br>
            2.私有类成员使用单一下划线前缀标识，多定义公开成员，少定义私有成员。<br>
            3.变量名不应带有类型信息，因为Python是动态类型语言。如 iValue、names_list、dict_obj 等都是不好的命名。<br>
            4.</em><em>开头，</em><em>结尾，一般为python的自有变量，不要以这种方式命名<br>
            5.以</em>_开头（2个下划线），是私有实例变量（外部不嫩直接访问），依照情况进行命名</p>
    </blockquote>
    <ul>
        <li>
            <h3>常量</h3>
        </li>
    </ul>
    <blockquote>
        <p>常量定义全部为大写，必要时可用下划线分隔单词以增加可读性。<br>
            constant</p>
    </blockquote>
    <ul>
        <li>
            <h3>命名注意：</h3>
        </li>
    </ul>
    <blockquote>
        <p>不要使用小写字母'l'(el),大写字母'O'(oh),或者小写'i'作为单独变量名称。因为一些字体中，上诉字母和数字很难区分（比如：O和0，l和1）。</p>
    </blockquote>
</article>