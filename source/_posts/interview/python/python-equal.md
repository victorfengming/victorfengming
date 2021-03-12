---
title: "python 中None，is和==的深入探讨"
date:       2019-11-28
subtitle: "简书 - 创作你的创作"
tags:
	- Python
	- solution
	- interview
---

原文链接:https://www.jianshu.com/p/627232777efd

<hr>
<p>注： 运行环境：python3.6.6，win10，64位</p>
<h2>1. None</h2>
<p>None是python中的一个特殊的常量，表示一个空的对象，空值是python中的一个特殊值。数据为空并不代表是空对象，例如[],''等都不是None。None和任何对象比较返回值都是False，除了自己。</p>
<pre class="line-numbers  language-python"><code class="python  language-python"><span
        class="token operator">&gt;&gt;</span><span
        class="token operator">&gt;</span> L<span class="token operator">=</span><span
        class="token punctuation">[</span><span class="token punctuation">]</span>
<span class="token operator">&gt;&gt;</span><span class="token operator">&gt;</span> L <span
            class="token keyword">is</span> <span class="token boolean">None</span>
<span class="token boolean">False</span>
<span class="token operator">&gt;&gt;</span><span class="token operator">&gt;</span> L<span
            class="token operator">=</span><span class="token string">''</span>
<span class="token operator">&gt;&gt;</span><span class="token operator">&gt;</span> L <span
            class="token keyword">is</span> <span class="token boolean">None</span>
<span class="token boolean">False</span>
<span aria-hidden="true"
      class="line-numbers-rows"><span></span><span></span><span></span><span></span><span></span><span></span></span></code><button
        class="VJbwyy" type="button" aria-label="复制代码"><i aria-label="icon: copy" class="anticon anticon-copy"><svg
        viewBox="64 64 896 896" focusable="false" class="" data-icon="copy" width="1em" height="1em"
        fill="currentColor" aria-hidden="true"><path
        d="M832 64H296c-4.4 0-8 3.6-8 8v56c0 4.4 3.6 8 8 8h496v688c0 4.4 3.6 8 8 8h56c4.4 0 8-3.6 8-8V96c0-17.7-14.3-32-32-32zM704 192H192c-17.7 0-32 14.3-32 32v530.7c0 8.5 3.4 16.6 9.4 22.6l173.3 173.3c2.2 2.2 4.7 4 7.4 5.5v1.9h4.2c3.5 1.3 7.2 2 11 2H704c17.7 0 32-14.3 32-32V224c0-17.7-14.3-32-32-32zM350 856.2L263.9 770H350v86.2zM664 888H414V746c0-22.1-17.9-40-40-40H232V264h432v624z"></path></svg></i></button></pre>
<p>None有自己的数据类型NontType，你可以将None赋值给任意对象，但是不能创建一个NoneType对象。</p>
<pre class="line-numbers  language-python"><code class="python  language-python"><span
        class="token operator">&gt;&gt;</span><span
        class="token operator">&gt;</span> <span class="token builtin">type</span><span
        class="token punctuation">(</span><span class="token boolean">None</span><span
        class="token punctuation">)</span>
<span class="token operator">&lt;</span><span class="token keyword">class</span> <span
            class="token string">'NoneType'</span><span class="token operator">&gt;</span>
<span class="token operator">&gt;&gt;</span><span class="token operator">&gt;</span> n<span
            class="token operator">=</span>NoneType<span class="token punctuation">(</span><span
            class="token punctuation">)</span>
Traceback <span class="token punctuation">(</span>most recent call last<span class="token punctuation">)</span><span
            class="token punctuation">:</span>
  File <span class="token string">"&lt;input&gt;"</span><span class="token punctuation">,</span> line <span
            class="token number">1</span><span class="token punctuation">,</span> <span
            class="token keyword">in</span> <span class="token operator">&lt;</span>module<span
            class="token operator">&gt;</span>
NameError<span class="token punctuation">:</span> name <span class="token string">'NoneType'</span> <span
            class="token keyword">is</span> <span class="token keyword">not</span> defined
<span aria-hidden="true"
      class="line-numbers-rows"><span></span><span></span><span></span><span></span><span></span><span></span></span></code><button
        class="VJbwyy" type="button" aria-label="复制代码"><i aria-label="icon: copy" class="anticon anticon-copy"><svg
        viewBox="64 64 896 896" focusable="false" class="" data-icon="copy" width="1em" height="1em"
        fill="currentColor" aria-hidden="true"><path
        d="M832 64H296c-4.4 0-8 3.6-8 8v56c0 4.4 3.6 8 8 8h496v688c0 4.4 3.6 8 8 8h56c4.4 0 8-3.6 8-8V96c0-17.7-14.3-32-32-32zM704 192H192c-17.7 0-32 14.3-32 32v530.7c0 8.5 3.4 16.6 9.4 22.6l173.3 173.3c2.2 2.2 4.7 4 7.4 5.5v1.9h4.2c3.5 1.3 7.2 2 11 2H704c17.7 0 32-14.3 32-32V224c0-17.7-14.3-32-32-32zM350 856.2L263.9 770H350v86.2zM664 888H414V746c0-22.1-17.9-40-40-40H232V264h432v624z"></path></svg></i></button></pre>
<h2>2.False</h2>
<p>需要注意一点：</p>
<pre class="line-numbers  language-python"><code class="python  language-python"><span
        class="token operator">&gt;&gt;</span><span
        class="token operator">&gt;</span> a<span class="token operator">=</span><span
        class="token boolean">False</span>
<span class="token operator">&gt;&gt;</span><span class="token operator">&gt;</span> <span
            class="token keyword">not</span> a
<span class="token boolean">True</span>
<span aria-hidden="true" class="line-numbers-rows"><span></span><span></span><span></span></span></code><button
        class="VJbwyy" type="button" aria-label="复制代码"><i aria-label="icon: copy" class="anticon anticon-copy"><svg
        viewBox="64 64 896 896" focusable="false" class="" data-icon="copy" width="1em" height="1em"
        fill="currentColor" aria-hidden="true"><path
        d="M832 64H296c-4.4 0-8 3.6-8 8v56c0 4.4 3.6 8 8 8h496v688c0 4.4 3.6 8 8 8h56c4.4 0 8-3.6 8-8V96c0-17.7-14.3-32-32-32zM704 192H192c-17.7 0-32 14.3-32 32v530.7c0 8.5 3.4 16.6 9.4 22.6l173.3 173.3c2.2 2.2 4.7 4 7.4 5.5v1.9h4.2c3.5 1.3 7.2 2 11 2H704c17.7 0 32-14.3 32-32V224c0-17.7-14.3-32-32-32zM350 856.2L263.9 770H350v86.2zM664 888H414V746c0-22.1-17.9-40-40-40H232V264h432v624z"></path></svg></i></button></pre>
<p>python中数据为空的对象在判断时的结果都为False，其中None，False，0，[]，""，{}，()都相当于False，即<code>not None == not False == not '' == not 0
    == not [] == not {} == not ()</code>。</p>
<h2>3. is 和 ==</h2>
<p>is表示的是对象标识符，用来检查对象的标识符是否一致，即两个对象在内存中的地址是否一致。在使用 <code>a is b</code> 的时候，相当于<code>id(a)==id(b)</code>。<br>
    ==表示两个对象是否相等，相当于调用<code>__eq__()</code>方法，即'a==b' ==&gt; <code>a.__eq__(b)</code>。</p>
<h2>4. Python里和None比较时，为什么是 is None 而不是 == None</h2>
<p>因为None在Python里是个单例对象，一个变量如果是None，它一定和None指向同一个内存地址。</p>
<pre class="line-numbers  language-python"><code class="python  language-python"><span
        class="token operator">&gt;&gt;</span><span
        class="token operator">&gt;</span> a<span class="token operator">=</span><span
        class="token boolean">None</span>
<span class="token operator">&gt;&gt;</span><span class="token operator">&gt;</span> b<span
            class="token operator">=</span><span class="token boolean">None</span>
<span class="token operator">&gt;&gt;</span><span class="token operator">&gt;</span> <span
            class="token builtin">id</span><span class="token punctuation">(</span>a<span
            class="token punctuation">)</span><span
            class="token operator">==</span><span class="token builtin">id</span><span
            class="token punctuation">(</span>b<span class="token punctuation">)</span>
<span class="token boolean">True</span>
<span aria-hidden="true" class="line-numbers-rows"><span></span><span></span><span></span><span></span></span></code><button
        class="VJbwyy" type="button" aria-label="复制代码"><i aria-label="icon: copy" class="anticon anticon-copy"><svg
        viewBox="64 64 896 896" focusable="false" class="" data-icon="copy" width="1em" height="1em"
        fill="currentColor" aria-hidden="true"><path
        d="M832 64H296c-4.4 0-8 3.6-8 8v56c0 4.4 3.6 8 8 8h496v688c0 4.4 3.6 8 8 8h56c4.4 0 8-3.6 8-8V96c0-17.7-14.3-32-32-32zM704 192H192c-17.7 0-32 14.3-32 32v530.7c0 8.5 3.4 16.6 9.4 22.6l173.3 173.3c2.2 2.2 4.7 4 7.4 5.5v1.9h4.2c3.5 1.3 7.2 2 11 2H704c17.7 0 32-14.3 32-32V224c0-17.7-14.3-32-32-32zM350 856.2L263.9 770H350v86.2zM664 888H414V746c0-22.1-17.9-40-40-40H232V264h432v624z"></path></svg></i></button></pre>
<p>is None是判断两个对象在内存中的地址是否一致，== None背后调用的是<strong>eq</strong>，而<strong>eq</strong>可以被重载，下面是一个 is not None但 ==
    None的例子：</p>
<pre class="line-numbers  language-python"><code class="python  language-python"><span
        class="token operator">&gt;&gt;</span><span
        class="token operator">&gt;</span> <span class="token keyword">class</span> <span
        class="token class-name">test</span><span
        class="token punctuation">(</span><span class="token punctuation">)</span><span
        class="token punctuation">:</span>
<span class="token punctuation">.</span><span class="token punctuation">.</span><span class="token punctuation">.</span>     <span
            class="token keyword">def</span> <span class="token function">__eq__</span><span
            class="token punctuation">(</span>self<span class="token punctuation">,</span>other<span
            class="token punctuation">)</span><span class="token punctuation">:</span>
<span class="token punctuation">.</span><span class="token punctuation">.</span><span class="token punctuation">.</span>         <span
            class="token keyword">return</span> <span class="token boolean">True</span>
<span class="token punctuation">.</span><span class="token punctuation">.</span><span class="token punctuation">.</span> 
<span class="token operator">&gt;&gt;</span><span class="token operator">&gt;</span> t<span
            class="token operator">=</span>test<span class="token punctuation">(</span><span
            class="token punctuation">)</span>
<span class="token operator">&gt;&gt;</span><span class="token operator">&gt;</span> t <span
            class="token keyword">is</span> <span class="token boolean">None</span>
<span class="token boolean">False</span>
<span class="token operator">&gt;&gt;</span><span class="token operator">&gt;</span> t <span
            class="token operator">==</span> <span class="token boolean">None</span>
<span class="token boolean">True</span>
<span aria-hidden="true"
      class="line-numbers-rows"><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span></span></code><button
        class="VJbwyy" type="button" aria-label="复制代码"><i aria-label="icon: copy" class="anticon anticon-copy"><svg
        viewBox="64 64 896 896" focusable="false" class="" data-icon="copy" width="1em" height="1em"
        fill="currentColor" aria-hidden="true"><path
        d="M832 64H296c-4.4 0-8 3.6-8 8v56c0 4.4 3.6 8 8 8h496v688c0 4.4 3.6 8 8 8h56c4.4 0 8-3.6 8-8V96c0-17.7-14.3-32-32-32zM704 192H192c-17.7 0-32 14.3-32 32v530.7c0 8.5 3.4 16.6 9.4 22.6l173.3 173.3c2.2 2.2 4.7 4 7.4 5.5v1.9h4.2c3.5 1.3 7.2 2 11 2H704c17.7 0 32-14.3 32-32V224c0-17.7-14.3-32-32-32zM350 856.2L263.9 770H350v86.2zM664 888H414V746c0-22.1-17.9-40-40-40H232V264h432v624z"></path></svg></i></button></pre>
<h2>5. 参考资料</h2>
<ul>
    <li><a href="https://blog.csdn.net/Primeprime/article/details/77186109" target="_blank" rel="nofollow">https://blog.csdn.net/Primeprime/article/details/77186109</a>
    </li>
    <li><a href="https://www.jianshu.com/p/1cc3282bfe29" target="_blank">https://www.jianshu.com/p/1cc3282bfe29</a>
    </li>
</ul>