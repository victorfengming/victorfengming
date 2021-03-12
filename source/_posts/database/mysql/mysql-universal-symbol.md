---
title: "mysql中的通配符使用"
date:       2019-10-09
tags:
	- database
	- mysql
	- solution
---

<div class="content-intro view-box "><p>在mysql查询中，经常会用到通配符，而且mysql的通配符和pgsql是有所不同的，甚至mysql中还可以使用正则表达式。本文就为大家带来mysql查询中通配符的使用。
    <br>
</p>
<p>
    <br>
</p>
<p><b>SQL模式匹配：
</b>
</p>
<p>“_”&nbsp;匹配单个字符,”\_”&nbsp;匹配”_”</p>
<p>“%”&nbsp;匹配任意个字符,包括零个字符</p>
<p>sql模式下的匹配，缺省是对于字母的大小写没有要求，并且sql模式下，“=”或”!=”是不能在模糊匹配中使用的，而是使用&nbsp;like&nbsp;或&nbsp;not&nbsp;like.</p>
<p>例如：</p><pre lang="sql" style="max-width: 100%;"><code class="sql hljs"><span class="hljs-keyword">SELECT</span> * <span class="hljs-keyword">FROM</span> ［<span class="hljs-keyword">user</span>］ <span class="hljs-keyword">WHERE</span> u_name <span class="hljs-keyword">LIKE</span> ‘%三%’;
<span class="hljs-keyword">SELECT</span> * <span class="hljs-keyword">FROM</span> ［<span class="hljs-keyword">user</span>］ <span class="hljs-keyword">WHERE</span> u_name <span class="hljs-keyword">LIKE</span> ‘_三_’;</code></pre>
<p>
    <br>
</p>
<p><b>正则模式匹配：
</b>
</p>
<p>当使用正则匹配时，使用REGEXP和NOT&nbsp;REGEXP操作符（或RLIKE和NOT&nbsp;RLIKE，功能是一样的）。</p>
<p>其中涉及到的字符是：</p>
<p>“.”&nbsp;匹配任何单个的字符。</p>
<p>“[…]” 表示匹配在方括号内的任何字符。如，”[abc]”&nbsp;则匹配”a”、”b”或者”c”，“［a-z］”匹配任何小写字母，而“［0-9］”匹配任何数字。</p>
<p>“&nbsp;*&nbsp;”表示匹配零个或多个在它前面的东西。例如，“x*”匹配任何数量的“x”字符，“［0-9］*”匹配的任何数量的数字，而“.*”匹配任何数量的任何东西。</p>
<p><font color="#ff0000">注意：正则表达式是区分大小写的</font>，但是我们也能使用一个字符类匹配两种写法。例如，“［aA］”匹配小写或大写的“a”而“［a-zA-Z］”匹配两种写法的任何字母。</p>
<p>为了定位一个模式以便它必须匹配被测试值的开始或结尾，在模式开始处使用“^”或在模式的结尾用“$”。</p>
<p>例如：</p>
<p>—&nbsp;查寻以&nbsp;三&nbsp;开头的名字</p><pre lang="sql" style="max-width: 100%;"><code class="sql hljs">FROM ［user］ WHERE u_name REGEXP ‘^三’;</code></pre>
<p>—&nbsp;查寻以&nbsp;三&nbsp;结尾的名字</p><pre lang="sql" style="max-width: 100%;"><code class="sql hljs">FROM ［user］ WHERE u_name REGEXP ‘三$’;</code></pre>
<p>—&nbsp;“重复n次”操作符重写先前的查询：</p><pre lang="sql" style="max-width: 100%;"><code class="sql hljs">FROM ［user］ WHERE u_name REGEXP ‘b{2}$’;</code></pre>
<p><b>推荐阅读：</b>
</p>
<p><a href="https://www.w3cschool.cn/regexp/krli1pr3.html" target="_blank">MySQL正则表达式
</a>
</p>
<p><a href="https://www.w3cschool.cn/mysql/mysql-tutorial.html" target="_blank">MySQL&nbsp;入门教程</a>
</p>
<p>
    <br>
</p>
<p>原文地址：<a rel="nofollow" href="http://www.iamlintao.com/" style="background-color: rgb(255, 255, 255);">26点的博客</a>&nbsp;»&nbsp;<a rel="nofollow" href="http://www.iamlintao.com/2328.html" style="background-color: rgb(255, 255, 255);">mysql查询中通配符的使用</a>
</p>
<p>
    <br>
</p></div>