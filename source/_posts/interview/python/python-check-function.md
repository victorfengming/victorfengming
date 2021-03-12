---
title: "Python如何判断一个对象是函数还是方法"
cover: "/img/lynk/32.jpg"
date:       2019-11-28
subtitle: "判断对象是否是function的三种方法"
tags:
	- Python
	- solution
	- interview
---



<p>在Python中，判断一个对象是否是方法有如下三种方法。</p>

<h2 id="1-根据call属性判断"><a name="t0"></a>1. 根据“__call__”属性判断</h2>

<p>有时候用python就有这么一种感悟，各种钩子函数就是通过内置的“__”属性实现，python学得好不好，就是对“__”属性理解得透彻不透彻。</p>

<p>python函数在调用时，一定会首先调用其相关“__call__”函数（没有空格），请参见<a href="http://blog.csdn.net/yiifaa/article/details/78035560"
                                                   rel="nofollow">python总结(四)：类装饰器与方法的动态添加</a>中的用法。</p>

<pre class="prettyprint" name="code"><code class="language-python hljs  has-numbering"
                                           onclick="mdcp.copyCode(event)" style="position: unset;">add = <span
        class="hljs-keyword">lambda</span> a, b: a + b
<span class="hljs-comment">#   判断成功</span>
<span class="hljs-keyword">if</span>(hasattr(add, <span class="hljs-string">'__call__'</span>)):
        <span class="hljs-keyword">print</span> add(<span class="hljs-number">1</span>,<span
            class="hljs-number">2</span>)<div class="hljs-button {2}" data-title="复制"></div></code><ul
        class="pre-numbering" style=""><li style="color: rgb(153, 153, 153);">1</li><li
        style="color: rgb(153, 153, 153);">2</li><li style="color: rgb(153, 153, 153);">3</li><li
        style="color: rgb(153, 153, 153);">4</li></ul></pre>


<h2 id="2-利用callable判断"><a name="t1"></a>2. 利用callable判断</h2>

<p>这是一个据传快要废弃的方法，但是在Python 2中依旧很好用，如下：</p>


<pre class="prettyprint" name="code"><code class="language-python hljs  has-numbering"
                                           onclick="mdcp.copyCode(event)" style="position: unset;"><span
        class="hljs-comment">#   判断成功</span>
<span class="hljs-keyword">if</span>(callable(add)):
        <span class="hljs-keyword">print</span> add(<span class="hljs-number">2</span>, <span
            class="hljs-number">2</span>)<div class="hljs-button {2}" data-title="复制"></div></code><ul
        class="pre-numbering" style=""><li style="color: rgb(153, 153, 153);">1</li><li
        style="color: rgb(153, 153, 153);">2</li><li style="color: rgb(153, 153, 153);">3</li></ul></pre>


<h2 id="3-利用isfunction进行判断"><a name="t2"></a>3. 利用isfunction进行判断</h2>

<p>Python的inspect模块包含了大量的与反射、元数据相关的工具函数，isfunction就是其中一种，使用方法如下：</p>


<pre class="prettyprint" name="code"><code class="language-python hljs  has-numbering"
                                           onclick="mdcp.copyCode(event)" style="position: unset;"><span
        class="hljs-keyword">from</span> inspect <span class="hljs-keyword">import</span> isfunction
<span class="hljs-comment">#   判断成功</span>
<span class="hljs-keyword">if</span>(isfunction(add)):
    <span class="hljs-keyword">print</span> add(<span class="hljs-number">5</span>, <span class="hljs-number">5</span>)<div
            class="hljs-button {2}" data-title="复制"></div></code><ul class="pre-numbering" style=""><li
        style="color: rgb(153, 153, 153);">1</li><li style="color: rgb(153, 153, 153);">2</li><li
        style="color: rgb(153, 153, 153);">3</li><li style="color: rgb(153, 153, 153);">4</li></ul></pre>


<h2 id="4-无效的typesmethodtype"><a name="t3"></a>4. 无效的types.MethodType</h2>

<p>出人意料的是types.MethodType竟然无效(版本2.7.14)，如下：</p>


<pre class="prettyprint" name="code"><code class="language-python hljs  has-numbering"
                                           onclick="mdcp.copyCode(event)" style="position: unset;"><span
        class="hljs-keyword">import</span> types
<span class="hljs-comment">#   竟然无效</span>
<span class="hljs-keyword">if</span>(isinstance(add, types.MethodType)):
    <span class="hljs-keyword">print</span> add.__name__<div class="hljs-button {2}" data-title="复制"></div></code><ul
        class="pre-numbering" style=""><li style="color: rgb(153, 153, 153);">1</li><li
        style="color: rgb(153, 153, 153);">2</li><li style="color: rgb(153, 153, 153);">3</li><li
        style="color: rgb(153, 153, 153);">4</li></ul></pre>

<p>在这个引申过程中，还发现了一些有意思的现象，不同的function的输出结果不一样：</p>


<pre class="prettyprint" name="code"><code class="language-bash hljs  has-numbering" onclick="mdcp.copyCode(event)"
                                           style="position: unset;">&gt;&gt;&gt; <span
        class="hljs-built_in">type</span>(format)
&lt;<span class="hljs-built_in">type</span> <span class="hljs-string">'builtin_function_or_method'</span>&gt;
&gt;&gt;&gt; <span class="hljs-built_in">type</span>(add)
&lt;<span class="hljs-built_in">type</span> <span class="hljs-string">'function'</span>&gt;<div class="hljs-button {2}"
                                                                                                data-title="复制"></div></code><ul
        class="pre-numbering" style=""><li style="color: rgb(153, 153, 153);">1</li><li
        style="color: rgb(153, 153, 153);">2</li><li style="color: rgb(153, 153, 153);">3</li><li
        style="color: rgb(153, 153, 153);">4</li></ul></pre>

<p>更有意思的是，type竟然无法对print进行操作，如下：</p>


<pre class="prettyprint" name="code"><code class="hljs haskell has-numbering" onclick="mdcp.copyCode(event)"
                                           style="position: unset;">&gt;&gt;&gt; <span class="hljs-typedef"><span
        class="hljs-keyword">type</span><span class="hljs-container">(<span
        class="hljs-title">print</span>)</span></span>
  <span class="hljs-type">File</span> <span class="hljs-string">"&lt;stdin&gt;"</span>, line <span
            class="hljs-number">1</span>
    <span class="hljs-typedef"><span class="hljs-keyword">type</span><span class="hljs-container">(<span
            class="hljs-title">print</span>)</span></span>
             ^
<span class="hljs-type">SyntaxError</span>: invalid syntax<div class="hljs-button {2}" data-title="复制"></div></code><ul
        class="pre-numbering" style=""><li style="color: rgb(153, 153, 153);">1</li><li
        style="color: rgb(153, 153, 153);">2</li><li style="color: rgb(153, 153, 153);">3</li><li
        style="color: rgb(153, 153, 153);">4</li><li style="color: rgb(153, 153, 153);">5</li></ul></pre>

<p><strong>那print是什么？</strong></p>


<h2 id="结论"><a name="t4"></a>结论</h2>

<p>如何判断一个对象是否是方法，本文提供了3种方法，并发现了一些有意思的现象，再问一遍，print是什么？</p>