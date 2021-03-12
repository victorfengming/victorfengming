---
title: "Python中read(),readline(),readlines()区别与用法"
date:       2019-12-01
subtitle: ""
tags:
	- Python
	- solution
	- interview
---







<h2>整理一下python3里面关于read、readline、readlines的方法，有关文件打开模式的内容可以参见我之前的文章</h2>
<blockquote>
    <p>文件 runoob.txt 的内容如下：</p>
</blockquote>
<pre class="line-numbers  language-css"><code class="  language-css">1<span class="token punctuation">:</span>www.runoob.com
2<span class="token punctuation">:</span>www.runoob.com
3<span class="token punctuation">:</span>www.runoob.com
4<span class="token punctuation">:</span>www.runoob.com
5<span class="token punctuation">:</span>www.runoob.com
<span aria-hidden="true"
      class="line-numbers-rows"><span></span><span></span><span></span><span></span><span></span></span></code><button
        class="VJbwyy" type="button" aria-label="复制代码"><i aria-label="icon: copy" class="anticon anticon-copy"><svg
        viewBox="64 64 896 896" focusable="false" class="" data-icon="copy" width="1em" height="1em"
        fill="currentColor" aria-hidden="true"><path
        d="M832 64H296c-4.4 0-8 3.6-8 8v56c0 4.4 3.6 8 8 8h496v688c0 4.4 3.6 8 8 8h56c4.4 0 8-3.6 8-8V96c0-17.7-14.3-32-32-32zM704 192H192c-17.7 0-32 14.3-32 32v530.7c0 8.5 3.4 16.6 9.4 22.6l173.3 173.3c2.2 2.2 4.7 4 7.4 5.5v1.9h4.2c3.5 1.3 7.2 2 11 2H704c17.7 0 32-14.3 32-32V224c0-17.7-14.3-32-32-32zM350 856.2L263.9 770H350v86.2zM664 888H414V746c0-22.1-17.9-40-40-40H232V264h432v624z"></path></svg></i></button></pre>
<h2>1. read方法</h2>
<h3>概述</h3>
<p>read() 方法用于从文件读取指定的字节数，如果未给定或为负则读取所有。</p>
<h3>语法</h3>
<blockquote>
    <p>read() 方法语法如下：</p>
</blockquote>
<pre class="line-numbers  language-css"><code class="  language-css">fileObject.<span
        class="token function">read</span><span class="token punctuation">(</span><span
        class="token punctuation">)</span><span class="token punctuation">;</span> 
<span aria-hidden="true" class="line-numbers-rows"><span></span></span></code><button class="VJbwyy" type="button"
                                                                                      aria-label="复制代码"><i
        aria-label="icon: copy" class="anticon anticon-copy"><svg viewBox="64 64 896 896" focusable="false" class=""
                                                                  data-icon="copy" width="1em" height="1em"
                                                                  fill="currentColor" aria-hidden="true"><path
        d="M832 64H296c-4.4 0-8 3.6-8 8v56c0 4.4 3.6 8 8 8h496v688c0 4.4 3.6 8 8 8h56c4.4 0 8-3.6 8-8V96c0-17.7-14.3-32-32-32zM704 192H192c-17.7 0-32 14.3-32 32v530.7c0 8.5 3.4 16.6 9.4 22.6l173.3 173.3c2.2 2.2 4.7 4 7.4 5.5v1.9h4.2c3.5 1.3 7.2 2 11 2H704c17.7 0 32-14.3 32-32V224c0-17.7-14.3-32-32-32zM350 856.2L263.9 770H350v86.2zM664 888H414V746c0-22.1-17.9-40-40-40H232V264h432v624z"></path></svg></i></button></pre>
<h3>参数</h3>
<p>size -- 从文件中读取的字节数。若无size参数则默认读取全部</p>
<h3>返回值</h3>
<p>返回从字符串中读取的字节。</p>
<h3>实例</h3>
<pre class="line-numbers  language-bash"><code class="  language-bash">#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 打开文件
fo = open("runoob.txt", "rw+")
print "文件名为: ", fo.name

line = fo.read(10)
print "读取的字符串: %s" % (line)

# 关闭文件
fo.close()

#输出
文件名为:  runoob.txt
读取的字符串: 1:www.runo
<span aria-hidden="true"
      class="line-numbers-rows"><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span></span></code><button
        class="VJbwyy" type="button" aria-label="复制代码"><i aria-label="icon: copy" class="anticon anticon-copy"><svg
        viewBox="64 64 896 896" focusable="false" class="" data-icon="copy" width="1em" height="1em"
        fill="currentColor" aria-hidden="true"><path
        d="M832 64H296c-4.4 0-8 3.6-8 8v56c0 4.4 3.6 8 8 8h496v688c0 4.4 3.6 8 8 8h56c4.4 0 8-3.6 8-8V96c0-17.7-14.3-32-32-32zM704 192H192c-17.7 0-32 14.3-32 32v530.7c0 8.5 3.4 16.6 9.4 22.6l173.3 173.3c2.2 2.2 4.7 4 7.4 5.5v1.9h4.2c3.5 1.3 7.2 2 11 2H704c17.7 0 32-14.3 32-32V224c0-17.7-14.3-32-32-32zM350 856.2L263.9 770H350v86.2zM664 888H414V746c0-22.1-17.9-40-40-40H232V264h432v624z"></path></svg></i></button></pre>
<h2>2. readline</h2>
<h3>概述</h3>
<p>readline() 方法用于从文件读取整行，包括 "\n" 字符。如果指定了一个非负数的参数，则返回指定大小的字节数，包括 "\n"
    字符。因为每次仅读取一行，所以读取时占用内存小，比较适合大文件，该方法返回一个字符串对象。</p>
<h3>语法</h3>
<blockquote>
    <p>readline() 方法语法如下：</p>
</blockquote>
<pre class="line-numbers  language-css"><code class="  language-css">fileObject.<span
        class="token function">readline</span><span
        class="token punctuation">(</span><span class="token punctuation">)</span><span
        class="token punctuation">;</span> 
<span aria-hidden="true" class="line-numbers-rows"><span></span></span></code><button class="VJbwyy" type="button"
                                                                                      aria-label="复制代码"><i
        aria-label="icon: copy" class="anticon anticon-copy"><svg viewBox="64 64 896 896" focusable="false" class=""
                                                                  data-icon="copy" width="1em" height="1em"
                                                                  fill="currentColor" aria-hidden="true"><path
        d="M832 64H296c-4.4 0-8 3.6-8 8v56c0 4.4 3.6 8 8 8h496v688c0 4.4 3.6 8 8 8h56c4.4 0 8-3.6 8-8V96c0-17.7-14.3-32-32-32zM704 192H192c-17.7 0-32 14.3-32 32v530.7c0 8.5 3.4 16.6 9.4 22.6l173.3 173.3c2.2 2.2 4.7 4 7.4 5.5v1.9h4.2c3.5 1.3 7.2 2 11 2H704c17.7 0 32-14.3 32-32V224c0-17.7-14.3-32-32-32zM350 856.2L263.9 770H350v86.2zM664 888H414V746c0-22.1-17.9-40-40-40H232V264h432v624z"></path></svg></i></button></pre>
<h3>参数</h3>
<p>size -- 从文件中读取的字节数。</p>
<h3>返回值</h3>
<p>返回从字符串中读取的字节。</p>
<h3>实例</h3>
<pre class="line-numbers  language-bash"><code class="  language-bash">#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 打开文件
fo = open("runoob.txt", "rw+")
print "文件名为: ", fo.name

line = fo.readline()
print "读取第一行 %s" % (line)

line = fo.readline(5)
print "读取的字符串为: %s" % (line)

# 关闭文件
fo.close()

#输出
文件名为:  runoob.txt
读取第一行 1:www.runoob.com

读取的字符串为: 2:www
<span aria-hidden="true"
      class="line-numbers-rows"><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span></span></code><button
        class="VJbwyy" type="button" aria-label="复制代码"><i aria-label="icon: copy" class="anticon anticon-copy"><svg
        viewBox="64 64 896 896" focusable="false" class="" data-icon="copy" width="1em" height="1em"
        fill="currentColor" aria-hidden="true"><path
        d="M832 64H296c-4.4 0-8 3.6-8 8v56c0 4.4 3.6 8 8 8h496v688c0 4.4 3.6 8 8 8h56c4.4 0 8-3.6 8-8V96c0-17.7-14.3-32-32-32zM704 192H192c-17.7 0-32 14.3-32 32v530.7c0 8.5 3.4 16.6 9.4 22.6l173.3 173.3c2.2 2.2 4.7 4 7.4 5.5v1.9h4.2c3.5 1.3 7.2 2 11 2H704c17.7 0 32-14.3 32-32V224c0-17.7-14.3-32-32-32zM350 856.2L263.9 770H350v86.2zM664 888H414V746c0-22.1-17.9-40-40-40H232V264h432v624z"></path></svg></i></button></pre>
<h2>3. readlines</h2>
<h3>概述</h3>
<p>readlines() 方法用于读取所有行(直到结束符 EOF)并返回列表，每行作为一个元素，该列表可以由 Python 的 for... in ... 结构进行处理。但读取大文件会比较占内存。</p>
<ul>
    <li>如果碰到结束符 EOF 则返回空字符串。</li>
</ul>
<h3>语法</h3>
<blockquote>
    <p>readlines() 方法语法如下：</p>
</blockquote>
<pre class="line-numbers  language-css"><code class="  language-css">fileObject.<span
        class="token function">readlines</span><span
        class="token punctuation">(</span> <span class="token punctuation">)</span><span
        class="token punctuation">;</span>
<span aria-hidden="true" class="line-numbers-rows"><span></span></span></code><button class="VJbwyy" type="button"
                                                                                      aria-label="复制代码"><i
        aria-label="icon: copy" class="anticon anticon-copy"><svg viewBox="64 64 896 896" focusable="false" class=""
                                                                  data-icon="copy" width="1em" height="1em"
                                                                  fill="currentColor" aria-hidden="true"><path
        d="M832 64H296c-4.4 0-8 3.6-8 8v56c0 4.4 3.6 8 8 8h496v688c0 4.4 3.6 8 8 8h56c4.4 0 8-3.6 8-8V96c0-17.7-14.3-32-32-32zM704 192H192c-17.7 0-32 14.3-32 32v530.7c0 8.5 3.4 16.6 9.4 22.6l173.3 173.3c2.2 2.2 4.7 4 7.4 5.5v1.9h4.2c3.5 1.3 7.2 2 11 2H704c17.7 0 32-14.3 32-32V224c0-17.7-14.3-32-32-32zM350 856.2L263.9 770H350v86.2zM664 888H414V746c0-22.1-17.9-40-40-40H232V264h432v624z"></path></svg></i></button></pre>
<h3>参数</h3>
<p>无。</p>
<h3>返回值</h3>
<p>返回列表，包含所有的行。</p>
<h3>实例</h3>
<pre class="line-numbers  language-ruby"><code class="  language-ruby"><span
        class="token comment">#!/usr/bin/python</span>
<span class="token comment"># -*- coding: UTF-8 -*-</span>
 
<span class="token comment"># 打开文件</span>
fo <span class="token operator">=</span> open<span class="token punctuation">(</span><span class="token string">"runoob.txt"</span><span
            class="token punctuation">,</span> <span class="token string">"r"</span><span
            class="token punctuation">)</span>
print <span class="token string">"文件名为: "</span><span class="token punctuation">,</span> fo<span
            class="token punctuation">.</span>name
 
<span class="token keyword">for</span> line <span class="token keyword">in</span> fo<span
            class="token punctuation">.</span>readlines<span class="token punctuation">(</span><span
            class="token punctuation">)</span><span
            class="token punctuation">:</span>                          <span class="token comment">#依次读取每行  </span>
    line <span class="token operator">=</span> line<span class="token punctuation">.</span>strip<span
            class="token punctuation">(</span><span
            class="token punctuation">)</span>                             <span
            class="token comment">#去掉每行头尾空白  </span>
    print <span class="token string">"读取的数据为: %s"</span> <span class="token operator">%</span> <span
            class="token punctuation">(</span>line<span class="token punctuation">)</span>
 
<span class="token comment"># 关闭文件</span>
fo<span class="token punctuation">.</span>close<span class="token punctuation">(</span><span
            class="token punctuation">)</span>

<span class="token comment">#输出</span>
文件名为<span class="token punctuation">:</span>  runoob<span class="token punctuation">.</span>txt
读取的数据为<span class="token punctuation">:</span> <span class="token number">1</span><span class="token symbol">:www</span><span
            class="token punctuation">.</span>runoob<span class="token punctuation">.</span>com
读取的数据为<span class="token punctuation">:</span> <span class="token number">2</span><span class="token symbol">:www</span><span
            class="token punctuation">.</span>runoob<span class="token punctuation">.</span>com
读取的数据为<span class="token punctuation">:</span> <span class="token number">3</span><span class="token symbol">:www</span><span
            class="token punctuation">.</span>runoob<span class="token punctuation">.</span>com
读取的数据为<span class="token punctuation">:</span> <span class="token number">4</span><span class="token symbol">:www</span><span
            class="token punctuation">.</span>runoob<span class="token punctuation">.</span>com
读取的数据为<span class="token punctuation">:</span> <span class="token number">5</span><span class="token symbol">:www</span><span
            class="token punctuation">.</span>runoob<span class="token punctuation">.</span>com
<span aria-hidden="true"
      class="line-numbers-rows"><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span></span></code><button
        class="VJbwyy" type="button" aria-label="复制代码"><i aria-label="icon: copy" class="anticon anticon-copy"><svg
        viewBox="64 64 896 896" focusable="false" class="" data-icon="copy" width="1em" height="1em"
        fill="currentColor" aria-hidden="true"><path
        d="M832 64H296c-4.4 0-8 3.6-8 8v56c0 4.4 3.6 8 8 8h496v688c0 4.4 3.6 8 8 8h56c4.4 0 8-3.6 8-8V96c0-17.7-14.3-32-32-32zM704 192H192c-17.7 0-32 14.3-32 32v530.7c0 8.5 3.4 16.6 9.4 22.6l173.3 173.3c2.2 2.2 4.7 4 7.4 5.5v1.9h4.2c3.5 1.3 7.2 2 11 2H704c17.7 0 32-14.3 32-32V224c0-17.7-14.3-32-32-32zM350 856.2L263.9 770H350v86.2zM664 888H414V746c0-22.1-17.9-40-40-40H232V264h432v624z"></path></svg></i></button></pre>
<h2>4. linecache模块</h2>
<blockquote>
    <p>当然，有特殊需求还可以用linecache模块，比如你要输出某个文件的第n行：</p>
</blockquote>
<pre class="line-numbers  language-bash"><code class="  language-bash"># 输出第2行
text = linecache.getline(‘a.txt’,2)
print text
<span aria-hidden="true" class="line-numbers-rows"><span></span><span></span><span></span></span></code><button
        class="VJbwyy" type="button" aria-label="复制代码"><i aria-label="icon: copy" class="anticon anticon-copy"><svg
        viewBox="64 64 896 896" focusable="false" class="" data-icon="copy" width="1em" height="1em"
        fill="currentColor" aria-hidden="true"><path
        d="M832 64H296c-4.4 0-8 3.6-8 8v56c0 4.4 3.6 8 8 8h496v688c0 4.4 3.6 8 8 8h56c4.4 0 8-3.6 8-8V96c0-17.7-14.3-32-32-32zM704 192H192c-17.7 0-32 14.3-32 32v530.7c0 8.5 3.4 16.6 9.4 22.6l173.3 173.3c2.2 2.2 4.7 4 7.4 5.5v1.9h4.2c3.5 1.3 7.2 2 11 2H704c17.7 0 32-14.3 32-32V224c0-17.7-14.3-32-32-32zM350 856.2L263.9 770H350v86.2zM664 888H414V746c0-22.1-17.9-40-40-40H232V264h432v624z"></path></svg></i></button></pre>
<ul>
    <li>处理大文件也比较有效率</li>
</ul>
