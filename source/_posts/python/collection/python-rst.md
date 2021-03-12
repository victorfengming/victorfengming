---
title: "rst文件是什么鬼?"
date:       2019-12-07
subtitle: "reStructuredText(rst)快速入门语法说明"
tags:
	- Python
	- background
	- solution
---


原文链接:https://www.jianshu.com/p/1885d5570b37


<p><strong>reStructuredText</strong> 是扩展名为.rst的纯文本文件，含义为"重新构建的文本"，也被简称为：RST或reST；是Python编程语言的Docutils项目的一部分，Python
    Doc-SIG (Documentation Special Interest Group)。该项目类似于Java的JavaDoc或Perl的POD项目。 Docutils
    能够从Python程序中提取注释和信息，格式化成程序文档。</p>
<p>.rst
    文件是轻量级标记语言的一种，被设计为容易阅读和编写的纯文本，并且可以借助Docutils这样的程序进行文档处理，也可以转换为HTML或PDF等多种格式，或由Sphinx-Doc这样的程序转换为LaTex、man等更多格式。</p>
<p>本文语法来自<a href="https://link.jianshu.com?t=http://docutils.sourceforge.net/docs/user/rst/quickref.html"
            target="_blank" rel="nofollow">Quick reStructuredText</a></p>
<p>由于格式原因，觉得这个不是很直观的话，可以到我的<a href="https://link.jianshu.com?t=https://github.com/SeayXu/CheatSheet" target="_blank"
                              rel="nofollow">github</a>上查看。</p>
<h1>行内样式</h1>
<h2>斜体</h2>
<p>重点、解释文字</p>
<div class="_2Uzcx_">
    <button class="VJbwyy" type="button" aria-label="复制代码"><i aria-label="icon: copy" class="anticon anticon-copy">
        <svg viewBox="64 64 896 896" focusable="false" class="" data-icon="copy" width="1em" height="1em"
             fill="currentColor" aria-hidden="true">
            <path d="M832 64H296c-4.4 0-8 3.6-8 8v56c0 4.4 3.6 8 8 8h496v688c0 4.4 3.6 8 8 8h56c4.4 0 8-3.6 8-8V96c0-17.7-14.3-32-32-32zM704 192H192c-17.7 0-32 14.3-32 32v530.7c0 8.5 3.4 16.6 9.4 22.6l173.3 173.3c2.2 2.2 4.7 4 7.4 5.5v1.9h4.2c3.5 1.3 7.2 2 11 2H704c17.7 0 32-14.3 32-32V224c0-17.7-14.3-32-32-32zM350 856.2L263.9 770H350v86.2zM664 888H414V746c0-22.1-17.9-40-40-40H232V264h432v624z"></path>
        </svg>
    </i></button>
    <pre class="line-numbers  language-go"><code class="  language-go"><span class="token operator">*</span>重点<span
            class="token punctuation">(</span>emphasis<span class="token punctuation">)</span>通常显示为斜体<span
            class="token operator">*</span>
<span class="token string">`解释文字(interpreted text)通常显示为斜体`</span>
<span aria-hidden="true" class="line-numbers-rows"><span></span><span></span></span></code></pre>
</div>
<p><em>重点(emphasis)通常显示为斜体</em></p>
<h2>粗体</h2>
<p>重点强调</p>
<div class="_2Uzcx_">
    <button class="VJbwyy" type="button" aria-label="复制代码"><i aria-label="icon: copy" class="anticon anticon-copy">
        <svg viewBox="64 64 896 896" focusable="false" class="" data-icon="copy" width="1em" height="1em"
             fill="currentColor" aria-hidden="true">
            <path d="M832 64H296c-4.4 0-8 3.6-8 8v56c0 4.4 3.6 8 8 8h496v688c0 4.4 3.6 8 8 8h56c4.4 0 8-3.6 8-8V96c0-17.7-14.3-32-32-32zM704 192H192c-17.7 0-32 14.3-32 32v530.7c0 8.5 3.4 16.6 9.4 22.6l173.3 173.3c2.2 2.2 4.7 4 7.4 5.5v1.9h4.2c3.5 1.3 7.2 2 11 2H704c17.7 0 32-14.3 32-32V224c0-17.7-14.3-32-32-32zM350 856.2L263.9 770H350v86.2zM664 888H414V746c0-22.1-17.9-40-40-40H232V264h432v624z"></path>
        </svg>
    </i></button>
    <pre class="line-numbers  language-objectivec"><code class="  language-objectivec"><span
            class="token operator">*</span><span
            class="token operator">*</span>重点强调<span class="token punctuation">(</span>strong emphasis<span
            class="token punctuation">)</span>通常显示为粗体<span class="token operator">*</span><span
            class="token operator">*</span>
<span aria-hidden="true" class="line-numbers-rows"><span></span></span></code></pre>
</div>
<p><strong>重点强调(strong emphasis)通常显示为粗体</strong></p>
<h2>等宽</h2>
<div class="_2Uzcx_">
    <button class="VJbwyy" type="button" aria-label="复制代码"><i aria-label="icon: copy" class="anticon anticon-copy">
        <svg viewBox="64 64 896 896" focusable="false" class="" data-icon="copy" width="1em" height="1em"
             fill="currentColor" aria-hidden="true">
            <path d="M832 64H296c-4.4 0-8 3.6-8 8v56c0 4.4 3.6 8 8 8h496v688c0 4.4 3.6 8 8 8h56c4.4 0 8-3.6 8-8V96c0-17.7-14.3-32-32-32zM704 192H192c-17.7 0-32 14.3-32 32v530.7c0 8.5 3.4 16.6 9.4 22.6l173.3 173.3c2.2 2.2 4.7 4 7.4 5.5v1.9h4.2c3.5 1.3 7.2 2 11 2H704c17.7 0 32-14.3 32-32V224c0-17.7-14.3-32-32-32zM350 856.2L263.9 770H350v86.2zM664 888H414V746c0-22.1-17.9-40-40-40H232V264h432v624z"></path>
        </svg>
    </i></button>
    <pre class="line-numbers  language-go"><code class="  language-go"><span class="token string">``</span>行内文本<span
            class="token punctuation">(</span>inline literal<span class="token punctuation">)</span>通常显示为等宽文本，空格可以保留，但是换行不可以。<span
            class="token string">``</span>
<span aria-hidden="true" class="line-numbers-rows"><span></span></span></code></pre>
</div>
<p>行内文本(inline literal)通常显示为等宽文本，空格可以保留，但是换行不可以。</p>
<h1>章节标题</h1>
<p>章节头部由下线(也可有上线)和包含标点的标题 组合创建, 其中下线要至少等于标准文本的长度。</p>
<p>可以表示标题的符号有
    <strong>=</strong>、<strong>-</strong>、<strong>`</strong>、<strong>:</strong>、<strong>'</strong>、<strong>"</strong>、<strong>~</strong>、<strong>^</strong>、<strong>_</strong>
    、<strong>*</strong> 、<strong>+</strong>、 <strong>#</strong>、<strong>&lt;</strong>、<strong>&gt;</strong> 。</p>
<p>对于相同的符号，有上标是一级标题，没有上标是二级标题。</p>
<p>标题最多分六级，可以自由组合使用。</p>
<p>全加上上标或者是全不加上标，使用不同的 6 个符号的标题依次排列，则会依次生成的标题为H1-H6。</p>
<div class="_2Uzcx_">
    <button class="VJbwyy" type="button" aria-label="复制代码"><i aria-label="icon: copy" class="anticon anticon-copy">
        <svg viewBox="64 64 896 896" focusable="false" class="" data-icon="copy" width="1em" height="1em"
             fill="currentColor" aria-hidden="true">
            <path d="M832 64H296c-4.4 0-8 3.6-8 8v56c0 4.4 3.6 8 8 8h496v688c0 4.4 3.6 8 8 8h56c4.4 0 8-3.6 8-8V96c0-17.7-14.3-32-32-32zM704 192H192c-17.7 0-32 14.3-32 32v530.7c0 8.5 3.4 16.6 9.4 22.6l173.3 173.3c2.2 2.2 4.7 4 7.4 5.5v1.9h4.2c3.5 1.3 7.2 2 11 2H704c17.7 0 32-14.3 32-32V224c0-17.7-14.3-32-32-32zM350 856.2L263.9 770H350v86.2zM664 888H414V746c0-22.1-17.9-40-40-40H232V264h432v624z"></path>
        </svg>
    </i></button>
    <pre class="line-numbers  language-python"><code class="  language-python"><span
            class="token operator">==</span><span class="token operator">==</span><span
            class="token operator">==</span><span class="token operator">==</span><span
            class="token operator">=</span>
一级标题
<span class="token operator">==</span><span class="token operator">==</span><span class="token operator">==</span><span
                class="token operator">==</span><span class="token operator">=</span>
二级标题
<span class="token operator">==</span><span class="token operator">==</span><span class="token operator">==</span><span
                class="token operator">==</span><span class="token operator">=</span>

一级标题
<span class="token operator">^</span><span class="token operator">^</span><span class="token operator">^</span><span
                class="token operator">^</span><span class="token operator">^</span><span
                class="token operator">^</span><span class="token operator">^</span><span
                class="token operator">^</span>
二级标题
<span class="token operator">-</span><span class="token operator">-</span><span class="token operator">-</span><span
                class="token operator">-</span><span class="token operator">-</span><span
                class="token operator">-</span><span class="token operator">-</span><span
                class="token operator">-</span><span class="token operator">-</span>
三级标题
<span class="token operator">&gt;&gt;</span><span class="token operator">&gt;&gt;</span><span class="token operator">&gt;&gt;</span><span
                class="token operator">&gt;&gt;</span><span class="token operator">&gt;</span>
四级标题
<span class="token punctuation">:</span><span class="token punctuation">:</span><span class="token punctuation">:</span><span
                class="token punctuation">:</span><span class="token punctuation">:</span><span
                class="token punctuation">:</span><span class="token punctuation">:</span><span
                class="token punctuation">:</span><span class="token punctuation">:</span>
五级标题
<span class="token triple-quoted-string string">'''''''</span><span class="token string">''</span>
六级标题
<span class="token triple-quoted-string string">"""""""</span>"
<span aria-hidden="true"
      class="line-numbers-rows"><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span></span></code></pre>
</div>
<h1>一级标题</h1>
<h2>二级标题</h2>
<h1>一级标题</h1>
<h2>二级标题</h2>
<h3>三级标题</h3>
<h4>四级标题</h4>
<h5>五级标题</h5>
<h6>六级标题</h6>
<hr>
<h1>段落</h1>
<p>段落是被空行分割的文字片段，左侧必须对齐（没有空格，或者有相同多的空格）。</p>
<p>缩进的段落被视为引文。</p>
<h1>列表</h1>
<h2>符号列表(Bullet Lists)</h2>
<p>符号列表可以使用 <strong>-</strong>、 <strong>*</strong>、<strong>+</strong> 来表示。</p>
<p>不同的符号结尾需要加上空行，下级列表需要有空格缩进。</p>
<div class="_2Uzcx_">
    <button class="VJbwyy" type="button" aria-label="复制代码"><i aria-label="icon: copy" class="anticon anticon-copy">
        <svg viewBox="64 64 896 896" focusable="false" class="" data-icon="copy" width="1em" height="1em"
             fill="currentColor" aria-hidden="true">
            <path d="M832 64H296c-4.4 0-8 3.6-8 8v56c0 4.4 3.6 8 8 8h496v688c0 4.4 3.6 8 8 8h56c4.4 0 8-3.6 8-8V96c0-17.7-14.3-32-32-32zM704 192H192c-17.7 0-32 14.3-32 32v530.7c0 8.5 3.4 16.6 9.4 22.6l173.3 173.3c2.2 2.2 4.7 4 7.4 5.5v1.9h4.2c3.5 1.3 7.2 2 11 2H704c17.7 0 32-14.3 32-32V224c0-17.7-14.3-32-32-32zM350 856.2L263.9 770H350v86.2zM664 888H414V746c0-22.1-17.9-40-40-40H232V264h432v624z"></path>
        </svg>
    </i></button>
    <pre class="line-numbers  language-undefined"><code class="  language-undefined">- 符号列表1
- 符号列表2

  + 二级符号列表1

  - 二级符号列表2

  * 二级符号列表3

* 符号列表3

+ 符号列表4
<span aria-hidden="true"
      class="line-numbers-rows"><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span></span></code></pre>
</div>
<ul>
    <li>符号列表1</li>
    <li>符号列表2
        <ul>
            <li>二级符号列表1</li>
        </ul>
        <ul>
            <li>二级符号列表2</li>
        </ul>
        <ul>
            <li>二级符号列表3</li>
        </ul>
    </li>
</ul>
<ul>
    <li>符号列表3</li>
</ul>
<ul>
    <li>符号列表4</li>
</ul>
<h2>枚举(顺序)列表(Enumerated Lists)</h2>
<p>枚举列表算即顺序(序号)列表，可以使用不同的枚举序号来表示列表。</p>
<blockquote>
    <p><strong>可以使用的枚举有：</strong></p>
</blockquote>
<ul>
    <li>阿拉伯数字: 1, 2, 3, ... (无上限)。</li>
    <li>大写字母: A-Z。</li>
    <li>小写字母: a-z。</li>
    <li>大写罗马数字: I, II, III, IV, ..., MMMMCMXCIX (4999)。</li>
    <li>小写罗马数字: i, ii, iii, iv, ..., mmmmcmxcix (4999)。</li>
</ul>
<p>可以为序号添加前缀和后缀，下面的是被允许的。</p>
<p><strong>.</strong> 后缀: "1.", "A.", "a.", "I.", "i."。<br>
    <strong>()</strong> 包起来: "(1)", "(A)", "(a)", "(I)", "(i)"。<br>
    <strong>)</strong> 后缀: "1)", "A)", "a)", "I)", "i)"。</p>
<p>枚举列表可以结合 <strong>#</strong> 自动生成枚举序号。</p>
<div class="_2Uzcx_">
    <button class="VJbwyy" type="button" aria-label="复制代码"><i aria-label="icon: copy" class="anticon anticon-copy">
        <svg viewBox="64 64 896 896" focusable="false" class="" data-icon="copy" width="1em" height="1em"
             fill="currentColor" aria-hidden="true">
            <path d="M832 64H296c-4.4 0-8 3.6-8 8v56c0 4.4 3.6 8 8 8h496v688c0 4.4 3.6 8 8 8h56c4.4 0 8-3.6 8-8V96c0-17.7-14.3-32-32-32zM704 192H192c-17.7 0-32 14.3-32 32v530.7c0 8.5 3.4 16.6 9.4 22.6l173.3 173.3c2.2 2.2 4.7 4 7.4 5.5v1.9h4.2c3.5 1.3 7.2 2 11 2H704c17.7 0 32-14.3 32-32V224c0-17.7-14.3-32-32-32zM350 856.2L263.9 770H350v86.2zM664 888H414V746c0-22.1-17.9-40-40-40H232V264h432v624z"></path>
        </svg>
    </i></button>
    <pre class="line-numbers  language-bash"><code class="  language-bash">1. 枚举列表1
#. 枚举列表2
#. 枚举列表3

(I) 枚举列表1
(#) 枚举列表2
(#) 枚举列表3

A) 枚举列表1
#) 枚举列表2
#) 枚举列表3
<span aria-hidden="true"
      class="line-numbers-rows"><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span></span></code></pre>
</div>
<ol>
    <li>枚举列表1</li>
    <li>枚举列表2</li>
    <li>枚举列表3</li>
</ol>
<p>I. 枚举列表1<br>
    II. 枚举列表2<br>
    III. 枚举列表3</p>
<p>A. 枚举列表1<br>
    B. 枚举列表2<br>
    C. 枚举列表3</p>
<h2>定义列表(Definition Lists)</h2>
<p>定义列表可以理解为解释列表，即名词解释。</p>
<p>条目占一行，解释文本要有缩进；多层可根据缩进实现。</p>
<div class="_2Uzcx_">
    <button class="VJbwyy" type="button" aria-label="复制代码"><i aria-label="icon: copy" class="anticon anticon-copy">
        <svg viewBox="64 64 896 896" focusable="false" class="" data-icon="copy" width="1em" height="1em"
             fill="currentColor" aria-hidden="true">
            <path d="M832 64H296c-4.4 0-8 3.6-8 8v56c0 4.4 3.6 8 8 8h496v688c0 4.4 3.6 8 8 8h56c4.4 0 8-3.6 8-8V96c0-17.7-14.3-32-32-32zM704 192H192c-17.7 0-32 14.3-32 32v530.7c0 8.5 3.4 16.6 9.4 22.6l173.3 173.3c2.2 2.2 4.7 4 7.4 5.5v1.9h4.2c3.5 1.3 7.2 2 11 2H704c17.7 0 32-14.3 32-32V224c0-17.7-14.3-32-32-32zM350 856.2L263.9 770H350v86.2zM664 888H414V746c0-22.1-17.9-40-40-40H232V264h432v624z"></path>
        </svg>
    </i></button>
    <pre class="line-numbers  language-undefined"><code class="  language-undefined">定义1
 这是定义1的内容

定义2
 这是定义2的内容
<span aria-hidden="true"
      class="line-numbers-rows"><span></span><span></span><span></span><span></span><span></span></span></code></pre>
</div>
<p>定义1</p>
<div class="_2Uzcx_">
    <button class="VJbwyy" type="button" aria-label="复制代码"><i aria-label="icon: copy" class="anticon anticon-copy">
        <svg viewBox="64 64 896 896" focusable="false" class="" data-icon="copy" width="1em" height="1em"
             fill="currentColor" aria-hidden="true">
            <path d="M832 64H296c-4.4 0-8 3.6-8 8v56c0 4.4 3.6 8 8 8h496v688c0 4.4 3.6 8 8 8h56c4.4 0 8-3.6 8-8V96c0-17.7-14.3-32-32-32zM704 192H192c-17.7 0-32 14.3-32 32v530.7c0 8.5 3.4 16.6 9.4 22.6l173.3 173.3c2.2 2.2 4.7 4 7.4 5.5v1.9h4.2c3.5 1.3 7.2 2 11 2H704c17.7 0 32-14.3 32-32V224c0-17.7-14.3-32-32-32zM350 856.2L263.9 770H350v86.2zM664 888H414V746c0-22.1-17.9-40-40-40H232V264h432v624z"></path>
        </svg>
    </i></button>
    <pre class="line-numbers  language-undefined"><code class="  language-undefined">这是定义1的内容  
<span aria-hidden="true" class="line-numbers-rows"><span></span></span></code></pre>
</div>
<p>定义2</p>
<div class="_2Uzcx_">
    <button class="VJbwyy" type="button" aria-label="复制代码"><i aria-label="icon: copy" class="anticon anticon-copy">
        <svg viewBox="64 64 896 896" focusable="false" class="" data-icon="copy" width="1em" height="1em"
             fill="currentColor" aria-hidden="true">
            <path d="M832 64H296c-4.4 0-8 3.6-8 8v56c0 4.4 3.6 8 8 8h496v688c0 4.4 3.6 8 8 8h56c4.4 0 8-3.6 8-8V96c0-17.7-14.3-32-32-32zM704 192H192c-17.7 0-32 14.3-32 32v530.7c0 8.5 3.4 16.6 9.4 22.6l173.3 173.3c2.2 2.2 4.7 4 7.4 5.5v1.9h4.2c3.5 1.3 7.2 2 11 2H704c17.7 0 32-14.3 32-32V224c0-17.7-14.3-32-32-32zM350 856.2L263.9 770H350v86.2zM664 888H414V746c0-22.1-17.9-40-40-40H232V264h432v624z"></path>
        </svg>
    </i></button>
    <pre class="line-numbers  language-undefined"><code class="  language-undefined">这是定义2的内容
<span aria-hidden="true" class="line-numbers-rows"><span></span></span></code></pre>
</div>
<h2>字段列表(Field Lists)</h2>
<div class="_2Uzcx_">
    <button class="VJbwyy" type="button" aria-label="复制代码"><i aria-label="icon: copy" class="anticon anticon-copy">
        <svg viewBox="64 64 896 896" focusable="false" class="" data-icon="copy" width="1em" height="1em"
             fill="currentColor" aria-hidden="true">
            <path d="M832 64H296c-4.4 0-8 3.6-8 8v56c0 4.4 3.6 8 8 8h496v688c0 4.4 3.6 8 8 8h56c4.4 0 8-3.6 8-8V96c0-17.7-14.3-32-32-32zM704 192H192c-17.7 0-32 14.3-32 32v530.7c0 8.5 3.4 16.6 9.4 22.6l173.3 173.3c2.2 2.2 4.7 4 7.4 5.5v1.9h4.2c3.5 1.3 7.2 2 11 2H704c17.7 0 32-14.3 32-32V224c0-17.7-14.3-32-32-32zM350 856.2L263.9 770H350v86.2zM664 888H414V746c0-22.1-17.9-40-40-40H232V264h432v624z"></path>
        </svg>
    </i></button>
    <pre class="line-numbers  language-undefined"><code class="  language-undefined">:标题: reStructuredText语法说明

:作者:
 - Seay
 - Seay1
 - Seay2

:时间: 2016年06月21日

:概述: 这是一篇
 关于reStructuredText

 语法说明。
<span aria-hidden="true"
      class="line-numbers-rows"><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span></span></code></pre>
</div>
<p><strong>标题:</strong> reStructuredText语法说明<br>
    <strong>作者:</strong></p>
<ul>
    <li>Seay</li>
    <li>Seay1</li>
    <li>Seay2</li>
</ul>
<p><strong>时间:</strong> 2016年06月21日<br>
    <strong>概述:</strong> 这是一篇 关于reStructuredText<br>
    语法说明。</p>
<h2>选项列表(Option Lists)</h2>
<p>选项列表是一个类似两列的表格，左边是参数，右边是描述信息。当参数选项过长时，参数选项和描述信息各占一行。</p>
<p>选项与参数之间有一个空格，参数选项与描述信息之间至少有两个空格。</p>
<div class="_2Uzcx_">
    <button class="VJbwyy" type="button" aria-label="复制代码"><i aria-label="icon: copy" class="anticon anticon-copy">
        <svg viewBox="64 64 896 896" focusable="false" class="" data-icon="copy" width="1em" height="1em"
             fill="currentColor" aria-hidden="true">
            <path d="M832 64H296c-4.4 0-8 3.6-8 8v56c0 4.4 3.6 8 8 8h496v688c0 4.4 3.6 8 8 8h56c4.4 0 8-3.6 8-8V96c0-17.7-14.3-32-32-32zM704 192H192c-17.7 0-32 14.3-32 32v530.7c0 8.5 3.4 16.6 9.4 22.6l173.3 173.3c2.2 2.2 4.7 4 7.4 5.5v1.9h4.2c3.5 1.3 7.2 2 11 2H704c17.7 0 32-14.3 32-32V224c0-17.7-14.3-32-32-32zM350 856.2L263.9 770H350v86.2zM664 888H414V746c0-22.1-17.9-40-40-40H232V264h432v624z"></path>
        </svg>
    </i></button>
    <pre class="line-numbers  language-cpp"><code class="  language-cpp"><span class="token operator">-</span>a            command<span
            class="token operator">-</span>line option <span class="token string">"a"</span>
<span class="token operator">-</span>b file       options can have arguments
              <span class="token operator">and</span> <span class="token keyword">long</span> descriptions
<span class="token operator">--</span><span class="token keyword">long</span>        options can be <span
                class="token keyword">long</span> also
<span class="token operator">--</span>input<span class="token operator">=</span>file  <span
                class="token keyword">long</span> options can also have
              arguments
<span class="token operator">/</span>V            DOS<span class="token operator">/</span>VMS<span
                class="token operator">-</span>style options too
<span aria-hidden="true"
      class="line-numbers-rows"><span></span><span></span><span></span><span></span><span></span><span></span><span></span></span></code></pre>
</div>
<table>
    <thead>
    <tr>
        <th>参数选项</th>
        <th>描述信息</th>
    </tr>
    </thead>
    <tbody>
    <tr>
        <td>-a</td>
        <td>command-line option "a"</td>
    </tr>
    <tr>
        <td>-b file</td>
        <td>options can have arguments and long descriptions</td>
    </tr>
    <tr>
        <td>--long</td>
        <td>options can be long also</td>
    </tr>
    <tr>
        <td>--input=file</td>
        <td>long options can also have arguments</td>
    </tr>
    <tr>
        <td>/V</td>
        <td>DOS/VMS-style options too</td>
    </tr>
    </tbody>
</table>
<p><em>由于格式问题，这里只是一个示例，实际上时没有上面的表头列和表格竖直线的。</em></p>
<h1>块(Blocks)</h1>
<h2>文字块(Literal Blocks)</h2>
<p>文字块就是一段文字信息，在需要插入文本块的段落后面加上 <strong>::</strong>，接着一个空行，然后就是文字块了。</p>
<p>文字块不能定顶头写，要有缩进，结束标志是，新的一段文本贴开头，即没有缩进。</p>
<div class="_2Uzcx_">
    <button class="VJbwyy" type="button" aria-label="复制代码"><i aria-label="icon: copy" class="anticon anticon-copy">
        <svg viewBox="64 64 896 896" focusable="false" class="" data-icon="copy" width="1em" height="1em"
             fill="currentColor" aria-hidden="true">
            <path d="M832 64H296c-4.4 0-8 3.6-8 8v56c0 4.4 3.6 8 8 8h496v688c0 4.4 3.6 8 8 8h56c4.4 0 8-3.6 8-8V96c0-17.7-14.3-32-32-32zM704 192H192c-17.7 0-32 14.3-32 32v530.7c0 8.5 3.4 16.6 9.4 22.6l173.3 173.3c2.2 2.2 4.7 4 7.4 5.5v1.9h4.2c3.5 1.3 7.2 2 11 2H704c17.7 0 32-14.3 32-32V224c0-17.7-14.3-32-32-32zM350 856.2L263.9 770H350v86.2zM664 888H414V746c0-22.1-17.9-40-40-40H232V264h432v624z"></path>
        </svg>
    </i></button>
    <pre class="line-numbers  language-undefined"><code class="  language-undefined">下面是文字块内容：
::

   这是一段文字块
   同样也是文字块
   还是文字块

这是新的一段。
<span aria-hidden="true"
      class="line-numbers-rows"><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span></span></code></pre>
</div>
<p>下面是文字块内容：</p>
<div class="_2Uzcx_">
    <button class="VJbwyy" type="button" aria-label="复制代码"><i aria-label="icon: copy" class="anticon anticon-copy">
        <svg viewBox="64 64 896 896" focusable="false" class="" data-icon="copy" width="1em" height="1em"
             fill="currentColor" aria-hidden="true">
            <path d="M832 64H296c-4.4 0-8 3.6-8 8v56c0 4.4 3.6 8 8 8h496v688c0 4.4 3.6 8 8 8h56c4.4 0 8-3.6 8-8V96c0-17.7-14.3-32-32-32zM704 192H192c-17.7 0-32 14.3-32 32v530.7c0 8.5 3.4 16.6 9.4 22.6l173.3 173.3c2.2 2.2 4.7 4 7.4 5.5v1.9h4.2c3.5 1.3 7.2 2 11 2H704c17.7 0 32-14.3 32-32V224c0-17.7-14.3-32-32-32zM350 856.2L263.9 770H350v86.2zM664 888H414V746c0-22.1-17.9-40-40-40H232V264h432v624z"></path>
        </svg>
    </i></button>
    <pre class="line-numbers  language-undefined"><code class="  language-undefined">这是一段文字块
同样也是文字块
还是文字块
<span aria-hidden="true" class="line-numbers-rows"><span></span><span></span><span></span></span></code></pre>
</div>
<p>这是新的一段。</p>
<h2>行块(Line Blocks)</h2>
<p>行块对于地址、诗句以及无装饰列表是非常有用的。行块是以 <strong>|</strong> 开头，每一个行块可以是多段文本。</p>
<p><strong>|</strong> 前后各有一个空格。</p>
<div class="_2Uzcx_">
    <button class="VJbwyy" type="button" aria-label="复制代码"><i aria-label="icon: copy" class="anticon anticon-copy">
        <svg viewBox="64 64 896 896" focusable="false" class="" data-icon="copy" width="1em" height="1em"
             fill="currentColor" aria-hidden="true">
            <path d="M832 64H296c-4.4 0-8 3.6-8 8v56c0 4.4 3.6 8 8 8h496v688c0 4.4 3.6 8 8 8h56c4.4 0 8-3.6 8-8V96c0-17.7-14.3-32-32-32zM704 192H192c-17.7 0-32 14.3-32 32v530.7c0 8.5 3.4 16.6 9.4 22.6l173.3 173.3c2.2 2.2 4.7 4 7.4 5.5v1.9h4.2c3.5 1.3 7.2 2 11 2H704c17.7 0 32-14.3 32-32V224c0-17.7-14.3-32-32-32zM350 856.2L263.9 770H350v86.2zM664 888H414V746c0-22.1-17.9-40-40-40H232V264h432v624z"></path>
        </svg>
    </i></button>
    <pre class="line-numbers  language-ruby"><code class="  language-ruby">下面是行块内容：
 <span class="token operator">|</span> 这是一段行块内容
 <span class="token operator">|</span> 这同样也是行块内容
   还是行块内容

这是新的一段。
<span aria-hidden="true"
      class="line-numbers-rows"><span></span><span></span><span></span><span></span><span></span><span></span></span></code></pre>
</div>
<p>下面是行块内容：</p>
<div class="_2Uzcx_">
    <button class="VJbwyy" type="button" aria-label="复制代码"><i aria-label="icon: copy" class="anticon anticon-copy">
        <svg viewBox="64 64 896 896" focusable="false" class="" data-icon="copy" width="1em" height="1em"
             fill="currentColor" aria-hidden="true">
            <path d="M832 64H296c-4.4 0-8 3.6-8 8v56c0 4.4 3.6 8 8 8h496v688c0 4.4 3.6 8 8 8h56c4.4 0 8-3.6 8-8V96c0-17.7-14.3-32-32-32zM704 192H192c-17.7 0-32 14.3-32 32v530.7c0 8.5 3.4 16.6 9.4 22.6l173.3 173.3c2.2 2.2 4.7 4 7.4 5.5v1.9h4.2c3.5 1.3 7.2 2 11 2H704c17.7 0 32-14.3 32-32V224c0-17.7-14.3-32-32-32zM350 856.2L263.9 770H350v86.2zM664 888H414V746c0-22.1-17.9-40-40-40H232V264h432v624z"></path>
        </svg>
    </i></button>
    <pre class="line-numbers  language-undefined"><code class="  language-undefined">这是一段行块内容  
这同样也是行块内容 还是行块内容
<span aria-hidden="true" class="line-numbers-rows"><span></span><span></span></span></code></pre>
</div>
<p>这是新的一段。</p>
<h2>块引用(Block Quotes)</h2>
<p>块引用是通过缩进来实现的，引用块要在前面的段落基础上缩进。</p>
<p>通常引用结尾会加上出处(attribution)，出处的文字块开头是 <strong>--</strong>、<strong>---</strong> 、<strong>—</strong>，后面加上出处信息。</p>
<p>块引用可以使用空的注释 <strong>..</strong> 分隔上下的块引用。</p>
<p>注意在新的块和出处都要添加一个空行。</p>
<div class="_2Uzcx_">
    <button class="VJbwyy" type="button" aria-label="复制代码"><i aria-label="icon: copy" class="anticon anticon-copy">
        <svg viewBox="64 64 896 896" focusable="false" class="" data-icon="copy" width="1em" height="1em"
             fill="currentColor" aria-hidden="true">
            <path d="M832 64H296c-4.4 0-8 3.6-8 8v56c0 4.4 3.6 8 8 8h496v688c0 4.4 3.6 8 8 8h56c4.4 0 8-3.6 8-8V96c0-17.7-14.3-32-32-32zM704 192H192c-17.7 0-32 14.3-32 32v530.7c0 8.5 3.4 16.6 9.4 22.6l173.3 173.3c2.2 2.2 4.7 4 7.4 5.5v1.9h4.2c3.5 1.3 7.2 2 11 2H704c17.7 0 32-14.3 32-32V224c0-17.7-14.3-32-32-32zM350 856.2L263.9 770H350v86.2zM664 888H414V746c0-22.1-17.9-40-40-40H232V264h432v624z"></path>
        </svg>
    </i></button>
    <pre class="line-numbers  language-undefined"><code class="  language-undefined">下面是引用的内容：

    “真的猛士，敢于直面惨淡的人生，敢于正视淋漓的鲜血。”

    --- 鲁迅

..

      “人生的意志和劳动将创造奇迹般的奇迹。”

      — 涅克拉索
<span aria-hidden="true"
      class="line-numbers-rows"><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span></span></code></pre>
</div>
<p>下面是引用的内容：</p>
<div class="_2Uzcx_">
    <button class="VJbwyy" type="button" aria-label="复制代码"><i aria-label="icon: copy" class="anticon anticon-copy">
        <svg viewBox="64 64 896 896" focusable="false" class="" data-icon="copy" width="1em" height="1em"
             fill="currentColor" aria-hidden="true">
            <path d="M832 64H296c-4.4 0-8 3.6-8 8v56c0 4.4 3.6 8 8 8h496v688c0 4.4 3.6 8 8 8h56c4.4 0 8-3.6 8-8V96c0-17.7-14.3-32-32-32zM704 192H192c-17.7 0-32 14.3-32 32v530.7c0 8.5 3.4 16.6 9.4 22.6l173.3 173.3c2.2 2.2 4.7 4 7.4 5.5v1.9h4.2c3.5 1.3 7.2 2 11 2H704c17.7 0 32-14.3 32-32V224c0-17.7-14.3-32-32-32zM350 856.2L263.9 770H350v86.2zM664 888H414V746c0-22.1-17.9-40-40-40H232V264h432v624z"></path>
        </svg>
    </i></button>
    <pre class="line-numbers  language-undefined"><code class="  language-undefined">“真的猛士，敢于直面惨淡的人生，敢于正视淋漓的鲜血。”
—鲁迅

“人生的意志和劳动将创造奇迹般的奇迹。”
—涅克拉索
<span aria-hidden="true"
      class="line-numbers-rows"><span></span><span></span><span></span><span></span><span></span></span></code></pre>
</div>
<h2>文档测试块(Doctest Blocks)</h2>
<p>文档测试块是交互式的Python会话，以 <strong>&gt;&gt;&gt;</strong> 开始，一个空行结束。</p>
<div class="_2Uzcx_">
    <button class="VJbwyy" type="button" aria-label="复制代码"><i aria-label="icon: copy" class="anticon anticon-copy">
        <svg viewBox="64 64 896 896" focusable="false" class="" data-icon="copy" width="1em" height="1em"
             fill="currentColor" aria-hidden="true">
            <path d="M832 64H296c-4.4 0-8 3.6-8 8v56c0 4.4 3.6 8 8 8h496v688c0 4.4 3.6 8 8 8h56c4.4 0 8-3.6 8-8V96c0-17.7-14.3-32-32-32zM704 192H192c-17.7 0-32 14.3-32 32v530.7c0 8.5 3.4 16.6 9.4 22.6l173.3 173.3c2.2 2.2 4.7 4 7.4 5.5v1.9h4.2c3.5 1.3 7.2 2 11 2H704c17.7 0 32-14.3 32-32V224c0-17.7-14.3-32-32-32zM350 856.2L263.9 770H350v86.2zM664 888H414V746c0-22.1-17.9-40-40-40H232V264h432v624z"></path>
        </svg>
    </i></button>
    <pre class="line-numbers  language-python"><code class="  language-python"><span
            class="token operator">&gt;&gt;</span><span class="token operator">&gt;</span> <span
            class="token keyword">print</span> <span class="token string">"This is a doctest block."</span>
This <span class="token keyword">is</span> a doctest block<span class="token punctuation">.</span>
<span aria-hidden="true" class="line-numbers-rows"><span></span><span></span></span></code></pre>
</div>
<div class="_2Uzcx_">
    <button class="VJbwyy" type="button" aria-label="复制代码"><i aria-label="icon: copy" class="anticon anticon-copy">
        <svg viewBox="64 64 896 896" focusable="false" class="" data-icon="copy" width="1em" height="1em"
             fill="currentColor" aria-hidden="true">
            <path d="M832 64H296c-4.4 0-8 3.6-8 8v56c0 4.4 3.6 8 8 8h496v688c0 4.4 3.6 8 8 8h56c4.4 0 8-3.6 8-8V96c0-17.7-14.3-32-32-32zM704 192H192c-17.7 0-32 14.3-32 32v530.7c0 8.5 3.4 16.6 9.4 22.6l173.3 173.3c2.2 2.2 4.7 4 7.4 5.5v1.9h4.2c3.5 1.3 7.2 2 11 2H704c17.7 0 32-14.3 32-32V224c0-17.7-14.3-32-32-32zM350 856.2L263.9 770H350v86.2zM664 888H414V746c0-22.1-17.9-40-40-40H232V264h432v624z"></path>
        </svg>
    </i></button>
    <pre class="line-numbers  language-python"><code class="  language-python"><span
            class="token operator">&gt;&gt;</span><span class="token operator">&gt;</span> <span
            class="token keyword">print</span> <span class="token string">"This is a doctest block."</span>
This <span class="token keyword">is</span> a doctest block<span class="token punctuation">.</span>
<span aria-hidden="true" class="line-numbers-rows"><span></span><span></span></span></code></pre>
</div>
<h1>表格(Tables)</h1>
<p>reStructuredText提供两种表格：网格表（Grid Tables），简单表（Simple Tables）。</p>
<h2>网格表(Grid Tables)</h2>
<p>网格表中使用的符号有：<strong>-</strong>、<strong>=</strong>、<strong>|</strong>、<strong>+</strong>。</p>
<p><strong>-</strong> 用来分隔行， <strong>=</strong> 用来分隔表头和表体行，<strong>|</strong> 用来分隔列，<strong>+</strong> 用来表示行和列相交的节点。
</p>
<div class="_2Uzcx_">
    <button class="VJbwyy" type="button" aria-label="复制代码"><i aria-label="icon: copy" class="anticon anticon-copy">
        <svg viewBox="64 64 896 896" focusable="false" class="" data-icon="copy" width="1em" height="1em"
             fill="currentColor" aria-hidden="true">
            <path d="M832 64H296c-4.4 0-8 3.6-8 8v56c0 4.4 3.6 8 8 8h496v688c0 4.4 3.6 8 8 8h56c4.4 0 8-3.6 8-8V96c0-17.7-14.3-32-32-32zM704 192H192c-17.7 0-32 14.3-32 32v530.7c0 8.5 3.4 16.6 9.4 22.6l173.3 173.3c2.2 2.2 4.7 4 7.4 5.5v1.9h4.2c3.5 1.3 7.2 2 11 2H704c17.7 0 32-14.3 32-32V224c0-17.7-14.3-32-32-32zM350 856.2L263.9 770H350v86.2zM664 888H414V746c0-22.1-17.9-40-40-40H232V264h432v624z"></path>
        </svg>
    </i></button>
    <pre class="line-numbers  language-ruby"><code class="  language-ruby"><span class="token constant">Grid</span> table<span
            class="token punctuation">:</span>

<span class="token operator">+</span><span class="token operator">--</span><span class="token operator">--</span><span
                class="token operator">--</span><span class="token operator">--</span><span
                class="token operator">--</span><span
                class="token operator">--</span><span class="token operator">+</span><span
                class="token operator">--</span><span class="token operator">--</span><span
                class="token operator">--</span><span
                class="token operator">--</span><span class="token operator">--</span><span
                class="token operator">--</span><span
                class="token operator">+</span><span class="token operator">--</span><span
                class="token operator">--</span><span class="token operator">--</span><span
                class="token operator">--</span><span
                class="token operator">--</span><span class="token operator">-</span><span
                class="token operator">+</span>
<span class="token operator">|</span> <span class="token constant">Header</span> <span
                class="token number">1</span>   <span class="token operator">|</span> <span class="token constant">Header</span> <span
                class="token number">2</span>   <span class="token operator">|</span> <span class="token constant">Header</span> <span
                class="token number">3</span>  <span class="token operator">|</span>
<span class="token operator">+</span><span class="token operator">===</span><span class="token operator">===</span><span
                class="token operator">===</span><span class="token operator">===</span><span
                class="token operator">+</span><span class="token operator">===</span><span
                class="token operator">===</span><span
                class="token operator">===</span><span class="token operator">===</span><span
                class="token operator">+</span><span class="token operator">===</span><span
                class="token operator">===</span><span
                class="token operator">===</span><span class="token operator">==</span><span
                class="token operator">+</span>
<span class="token operator">|</span> body row <span class="token number">1</span> <span class="token operator">|</span> column <span
                class="token number">2</span>   <span class="token operator">|</span> column <span
                class="token number">3</span>  <span class="token operator">|</span>
<span class="token operator">+</span><span class="token operator">--</span><span class="token operator">--</span><span
                class="token operator">--</span><span class="token operator">--</span><span
                class="token operator">--</span><span
                class="token operator">--</span><span class="token operator">+</span><span
                class="token operator">--</span><span class="token operator">--</span><span
                class="token operator">--</span><span
                class="token operator">--</span><span class="token operator">--</span><span
                class="token operator">--</span><span
                class="token operator">+</span><span class="token operator">--</span><span
                class="token operator">--</span><span class="token operator">--</span><span
                class="token operator">--</span><span
                class="token operator">--</span><span class="token operator">-</span><span
                class="token operator">+</span>
<span class="token operator">|</span> body row <span class="token number">2</span> <span class="token operator">|</span> <span
                class="token constant">Cells</span> may span columns<span class="token punctuation">.</span><span
                class="token operator">|</span>
<span class="token operator">+</span><span class="token operator">--</span><span class="token operator">--</span><span
                class="token operator">--</span><span class="token operator">--</span><span
                class="token operator">--</span><span
                class="token operator">--</span><span class="token operator">+</span><span
                class="token operator">--</span><span class="token operator">--</span><span
                class="token operator">--</span><span
                class="token operator">--</span><span class="token operator">--</span><span
                class="token operator">--</span><span
                class="token operator">+</span><span class="token operator">--</span><span
                class="token operator">--</span><span class="token operator">--</span><span
                class="token operator">--</span><span
                class="token operator">--</span><span class="token operator">-</span><span
                class="token operator">+</span>
<span class="token operator">|</span> body row <span class="token number">3</span> <span class="token operator">|</span> <span
                class="token constant">Cells</span> may  <span class="token operator">|</span> <span
                class="token operator">-</span> <span class="token constant">Cells</span>   <span
                class="token operator">|</span>
<span class="token operator">+</span><span class="token operator">--</span><span class="token operator">--</span><span
                class="token operator">--</span><span class="token operator">--</span><span
                class="token operator">--</span><span
                class="token operator">--</span><span class="token operator">+</span> span rows<span
                class="token punctuation">.</span> <span class="token operator">|</span> <span
                class="token operator">-</span> contain <span class="token operator">|</span>
<span class="token operator">|</span> body row <span class="token number">4</span> <span class="token operator">|</span>            <span
                class="token operator">|</span> <span class="token operator">-</span> blocks<span
                class="token punctuation">.</span> <span class="token operator">|</span>
<span class="token operator">+</span><span class="token operator">--</span><span class="token operator">--</span><span
                class="token operator">--</span><span class="token operator">--</span><span
                class="token operator">--</span><span
                class="token operator">--</span><span class="token operator">+</span><span
                class="token operator">--</span><span class="token operator">--</span><span
                class="token operator">--</span><span
                class="token operator">--</span><span class="token operator">--</span><span
                class="token operator">--</span><span
                class="token operator">+</span><span class="token operator">--</span><span
                class="token operator">--</span><span class="token operator">--</span><span
                class="token operator">--</span><span
                class="token operator">--</span><span class="token operator">-</span><span
                class="token operator">+</span>
<span aria-hidden="true"
      class="line-numbers-rows"><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span></span></code></pre>
</div>
<p>效果请查看:<a href="https://link.jianshu.com?t=http://docutils.sourceforge.net/docs/user/rst/quickref.html#tables"
            target="_blank" rel="nofollow">这里</a></p>
<h2>简单表(Simple Tables)</h2>
<p>简单表相对于网格表，少了 <strong>|</strong> 和 <strong>+</strong> 两个符号，只用 <strong>-</strong> 和 <strong>=</strong> 表示。</p>
<div class="_2Uzcx_">
    <button class="VJbwyy" type="button" aria-label="复制代码"><i aria-label="icon: copy" class="anticon anticon-copy">
        <svg viewBox="64 64 896 896" focusable="false" class="" data-icon="copy" width="1em" height="1em"
             fill="currentColor" aria-hidden="true">
            <path d="M832 64H296c-4.4 0-8 3.6-8 8v56c0 4.4 3.6 8 8 8h496v688c0 4.4 3.6 8 8 8h56c4.4 0 8-3.6 8-8V96c0-17.7-14.3-32-32-32zM704 192H192c-17.7 0-32 14.3-32 32v530.7c0 8.5 3.4 16.6 9.4 22.6l173.3 173.3c2.2 2.2 4.7 4 7.4 5.5v1.9h4.2c3.5 1.3 7.2 2 11 2H704c17.7 0 32-14.3 32-32V224c0-17.7-14.3-32-32-32zM350 856.2L263.9 770H350v86.2zM664 888H414V746c0-22.1-17.9-40-40-40H232V264h432v624z"></path>
        </svg>
    </i></button>
    <pre class="line-numbers  language-php"><code class="  language-php">Simple table<span
            class="token punctuation">:</span>

<span class="token operator">===</span><span class="token operator">==</span>  <span
                class="token operator">===</span><span class="token operator">==</span>  <span
                class="token operator">===</span><span class="token operator">===</span>
   Inputs     Output
<span class="token operator">--</span><span class="token operator">--</span><span class="token operator">--</span><span
                class="token operator">--</span><span class="token operator">--</span><span
                class="token operator">--</span>  <span
                class="token operator">--</span><span class="token operator">--</span><span
                class="token operator">--</span>
  <span class="token constant">A</span>      <span class="token constant">B</span>    <span
                class="token constant">A</span> <span class="token keyword">or</span> <span
                class="token constant">B</span>
<span class="token operator">===</span><span class="token operator">==</span>  <span
                class="token operator">===</span><span class="token operator">==</span>  <span
                class="token operator">===</span><span class="token operator">===</span>
<span class="token boolean constant">False</span>  <span class="token boolean constant">False</span>  <span
                class="token boolean constant">False</span>
<span class="token boolean constant">True</span>   <span class="token boolean constant">False</span>  <span
                class="token boolean constant">True</span>
<span class="token boolean constant">False</span>  <span class="token boolean constant">True</span>   <span
                class="token boolean constant">True</span>
<span class="token boolean constant">True</span>   <span class="token boolean constant">True</span>   <span
                class="token boolean constant">True</span>
<span class="token operator">===</span><span class="token operator">==</span>  <span
                class="token operator">===</span><span class="token operator">==</span>  <span
                class="token operator">===</span><span class="token operator">===</span>
<span aria-hidden="true"
      class="line-numbers-rows"><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span></span></code></pre>
</div>
<p>效果请查看:<a href="https://link.jianshu.com?t=http://docutils.sourceforge.net/docs/user/rst/quickref.html#tables"
            target="_blank" rel="nofollow">这里</a></p>
<h1>分隔符</h1>
<p>分隔符就是一条水平的横线，是由 4 个 <strong>-</strong> 或者更多组成，需要添加换行。</p>
<div class="_2Uzcx_">
    <button class="VJbwyy" type="button" aria-label="复制代码"><i aria-label="icon: copy" class="anticon anticon-copy">
        <svg viewBox="64 64 896 896" focusable="false" class="" data-icon="copy" width="1em" height="1em"
             fill="currentColor" aria-hidden="true">
            <path d="M832 64H296c-4.4 0-8 3.6-8 8v56c0 4.4 3.6 8 8 8h496v688c0 4.4 3.6 8 8 8h56c4.4 0 8-3.6 8-8V96c0-17.7-14.3-32-32-32zM704 192H192c-17.7 0-32 14.3-32 32v530.7c0 8.5 3.4 16.6 9.4 22.6l173.3 173.3c2.2 2.2 4.7 4 7.4 5.5v1.9h4.2c3.5 1.3 7.2 2 11 2H704c17.7 0 32-14.3 32-32V224c0-17.7-14.3-32-32-32zM350 856.2L263.9 770H350v86.2zM664 888H414V746c0-22.1-17.9-40-40-40H232V264h432v624z"></path>
        </svg>
    </i></button>
    <pre class="line-numbers  language-undefined"><code class="  language-undefined">上面部分

------------

下面部分
<span aria-hidden="true"
      class="line-numbers-rows"><span></span><span></span><span></span><span></span><span></span></span></code></pre>
</div>
<p>上面部分</p>
<hr>
<p>下面部分</p>
<h1>超链接</h1>
<p>介绍各类带有链接性质的超链接</p>
<h2>自动超链接</h2>
<p>reStructuredText会自动将网址生成超链接。</p>
<div class="_2Uzcx_">
    <button class="VJbwyy" type="button" aria-label="复制代码"><i aria-label="icon: copy" class="anticon anticon-copy">
        <svg viewBox="64 64 896 896" focusable="false" class="" data-icon="copy" width="1em" height="1em"
             fill="currentColor" aria-hidden="true">
            <path d="M832 64H296c-4.4 0-8 3.6-8 8v56c0 4.4 3.6 8 8 8h496v688c0 4.4 3.6 8 8 8h56c4.4 0 8-3.6 8-8V96c0-17.7-14.3-32-32-32zM704 192H192c-17.7 0-32 14.3-32 32v530.7c0 8.5 3.4 16.6 9.4 22.6l173.3 173.3c2.2 2.2 4.7 4 7.4 5.5v1.9h4.2c3.5 1.3 7.2 2 11 2H704c17.7 0 32-14.3 32-32V224c0-17.7-14.3-32-32-32zM350 856.2L263.9 770H350v86.2zM664 888H414V746c0-22.1-17.9-40-40-40H232V264h432v624z"></path>
        </svg>
    </i></button>
    <pre class="line-numbers  language-cpp"><code class="  language-cpp">https<span
            class="token operator">:</span><span class="token operator">/</span><span
            class="token operator">/</span>github<span class="token punctuation">.</span>com<span
            class="token operator">/</span>SeayXu<span class="token operator">/</span>
<span aria-hidden="true" class="line-numbers-rows"><span></span></span></code></pre>
</div>
<p><a href="https://link.jianshu.com?t=https://github.com/SeayXu/" target="_blank" rel="nofollow">https://github.com/SeayXu/</a>
</p>
<h2>外部超链接(External Hyperlink)</h2>
<p>引用/参考(reference)，是简单的形式，只能是一个词语，引用的文字不能带有空格。</p>
<div class="_2Uzcx_">
    <button class="VJbwyy" type="button" aria-label="复制代码"><i aria-label="icon: copy" class="anticon anticon-copy">
        <svg viewBox="64 64 896 896" focusable="false" class="" data-icon="copy" width="1em" height="1em"
             fill="currentColor" aria-hidden="true">
            <path d="M832 64H296c-4.4 0-8 3.6-8 8v56c0 4.4 3.6 8 8 8h496v688c0 4.4 3.6 8 8 8h56c4.4 0 8-3.6 8-8V96c0-17.7-14.3-32-32-32zM704 192H192c-17.7 0-32 14.3-32 32v530.7c0 8.5 3.4 16.6 9.4 22.6l173.3 173.3c2.2 2.2 4.7 4 7.4 5.5v1.9h4.2c3.5 1.3 7.2 2 11 2H704c17.7 0 32-14.3 32-32V224c0-17.7-14.3-32-32-32zM350 856.2L263.9 770H350v86.2zM664 888H414V746c0-22.1-17.9-40-40-40H232V264h432v624z"></path>
        </svg>
    </i></button>
    <pre class="line-numbers  language-cpp"><code class="  language-cpp">这篇文章来自我的Github<span
            class="token punctuation">,</span>请参考 reference_。

<span class="token punctuation">.</span><span class="token punctuation">.</span> _reference<span class="token operator">:</span> https<span
                class="token operator">:</span><span class="token operator">/</span><span
                class="token operator">/</span>github<span class="token punctuation">.</span>com<span
                class="token operator">/</span>SeayXu<span class="token operator">/</span>
<span aria-hidden="true" class="line-numbers-rows"><span></span><span></span><span></span></span></code></pre>
</div>
<p>引用/参考(reference)，行内形式，引用的文字可以带有空格或者符号。</p>
<div class="_2Uzcx_">
    <button class="VJbwyy" type="button" aria-label="复制代码"><i aria-label="icon: copy" class="anticon anticon-copy">
        <svg viewBox="64 64 896 896" focusable="false" class="" data-icon="copy" width="1em" height="1em"
             fill="currentColor" aria-hidden="true">
            <path d="M832 64H296c-4.4 0-8 3.6-8 8v56c0 4.4 3.6 8 8 8h496v688c0 4.4 3.6 8 8 8h56c4.4 0 8-3.6 8-8V96c0-17.7-14.3-32-32-32zM704 192H192c-17.7 0-32 14.3-32 32v530.7c0 8.5 3.4 16.6 9.4 22.6l173.3 173.3c2.2 2.2 4.7 4 7.4 5.5v1.9h4.2c3.5 1.3 7.2 2 11 2H704c17.7 0 32-14.3 32-32V224c0-17.7-14.3-32-32-32zM350 856.2L263.9 770H350v86.2zM664 888H414V746c0-22.1-17.9-40-40-40H232V264h432v624z"></path>
        </svg>
    </i></button>
    <pre class="line-numbers  language-cpp"><code class="  language-cpp">这篇文章来自我的Github<span
            class="token punctuation">,</span>请参考 `SeayXu <span class="token operator">&lt;</span>https<span
            class="token operator">:</span><span class="token operator">/</span><span
            class="token operator">/</span>github<span class="token punctuation">.</span>com<span
            class="token operator">/</span>SeayXu<span class="token operator">/</span><span
            class="token operator">&gt;</span>`_。
<span aria-hidden="true" class="line-numbers-rows"><span></span></span></code></pre>
</div>
<p>这篇文章来自我的Github,请参考 <a href="https://link.jianshu.com?t=https://github.com/SeayXu/" target="_blank"
                         rel="nofollow">SeayXu</a>。</p>
<h2>内部超链接|锚点(Internal Hyperlink)</h2>
<div class="_2Uzcx_">
    <button class="VJbwyy" type="button" aria-label="复制代码"><i aria-label="icon: copy" class="anticon anticon-copy">
        <svg viewBox="64 64 896 896" focusable="false" class="" data-icon="copy" width="1em" height="1em"
             fill="currentColor" aria-hidden="true">
            <path d="M832 64H296c-4.4 0-8 3.6-8 8v56c0 4.4 3.6 8 8 8h496v688c0 4.4 3.6 8 8 8h56c4.4 0 8-3.6 8-8V96c0-17.7-14.3-32-32-32zM704 192H192c-17.7 0-32 14.3-32 32v530.7c0 8.5 3.4 16.6 9.4 22.6l173.3 173.3c2.2 2.2 4.7 4 7.4 5.5v1.9h4.2c3.5 1.3 7.2 2 11 2H704c17.7 0 32-14.3 32-32V224c0-17.7-14.3-32-32-32zM350 856.2L263.9 770H350v86.2zM664 888H414V746c0-22.1-17.9-40-40-40H232V264h432v624z"></path>
        </svg>
    </i></button>
    <pre class="line-numbers  language-undefined"><code class="  language-undefined">更多信息参考 引用文档_

这里是其他内容

.. _引用文档:

这是引用部分的内容
<span aria-hidden="true"
      class="line-numbers-rows"><span></span><span></span><span></span><span></span><span></span><span></span><span></span></span></code></pre>
</div>
<p>更多信息参考 <a href="#id1" target="_blank">引用文档</a></p>
<p>这里是其他内容</p>
<p>&lt;h6 id="id1"&gt;&lt;/h6&gt;</p>
<p>这是引用部分的内容</p>
<h2>匿名超链接(Anonymous hyperlink)</h2>
<p>词组(短语)引用/参考(phrase reference)，引用的文字可以带有空格或者符号，需要使用反引号引起来。</p>
<div class="_2Uzcx_">
    <button class="VJbwyy" type="button" aria-label="复制代码"><i aria-label="icon: copy" class="anticon anticon-copy">
        <svg viewBox="64 64 896 896" focusable="false" class="" data-icon="copy" width="1em" height="1em"
             fill="currentColor" aria-hidden="true">
            <path d="M832 64H296c-4.4 0-8 3.6-8 8v56c0 4.4 3.6 8 8 8h496v688c0 4.4 3.6 8 8 8h56c4.4 0 8-3.6 8-8V96c0-17.7-14.3-32-32-32zM704 192H192c-17.7 0-32 14.3-32 32v530.7c0 8.5 3.4 16.6 9.4 22.6l173.3 173.3c2.2 2.2 4.7 4 7.4 5.5v1.9h4.2c3.5 1.3 7.2 2 11 2H704c17.7 0 32-14.3 32-32V224c0-17.7-14.3-32-32-32zM350 856.2L263.9 770H350v86.2zM664 888H414V746c0-22.1-17.9-40-40-40H232V264h432v624z"></path>
        </svg>
    </i></button>
    <pre class="line-numbers  language-go"><code class="  language-go">这篇文章参考的是：<span class="token string">`Quick reStructuredText`</span>__。

<span class="token punctuation">.</span><span class="token punctuation">.</span> __<span
                class="token punctuation">:</span> http<span class="token punctuation">:</span><span
                class="token operator">/</span><span class="token operator">/</span>docutils<span
                class="token punctuation">.</span>sourceforge<span class="token punctuation">.</span>net<span
                class="token operator">/</span>docs<span class="token operator">/</span>user<span
                class="token operator">/</span>rst<span class="token operator">/</span>quickref<span
                class="token punctuation">.</span>html
<span aria-hidden="true" class="line-numbers-rows"><span></span><span></span><span></span></span></code></pre>
</div>
<p>这篇文章来自我的Github,请参考 <a
        href="https://link.jianshu.com?t=http://docutils.sourceforge.net/docs/user/rst/quickref.html"
        target="_blank" rel="nofollow">Quick reStructuredText</a>。</p>
<h2>间接超链接(Indirect Hyperlink)</h2>
<p>间接超链接是基于匿名链接的基础上的，就是将匿名链接地址换成了外部引用名_。</p>
<div class="_2Uzcx_">
    <button class="VJbwyy" type="button" aria-label="复制代码"><i aria-label="icon: copy" class="anticon anticon-copy">
        <svg viewBox="64 64 896 896" focusable="false" class="" data-icon="copy" width="1em" height="1em"
             fill="currentColor" aria-hidden="true">
            <path d="M832 64H296c-4.4 0-8 3.6-8 8v56c0 4.4 3.6 8 8 8h496v688c0 4.4 3.6 8 8 8h56c4.4 0 8-3.6 8-8V96c0-17.7-14.3-32-32-32zM704 192H192c-17.7 0-32 14.3-32 32v530.7c0 8.5 3.4 16.6 9.4 22.6l173.3 173.3c2.2 2.2 4.7 4 7.4 5.5v1.9h4.2c3.5 1.3 7.2 2 11 2H704c17.7 0 32-14.3 32-32V224c0-17.7-14.3-32-32-32zM350 856.2L263.9 770H350v86.2zM664 888H414V746c0-22.1-17.9-40-40-40H232V264h432v624z"></path>
        </svg>
    </i></button>
    <pre class="line-numbers  language-go"><code class="  language-go">SeayXu_ 是 <span class="token string">`我的 GitHub 用户名`</span>__。

<span class="token punctuation">.</span><span class="token punctuation">.</span> _SeayXu<span class="token punctuation">:</span> https<span
                class="token punctuation">:</span><span class="token operator">/</span><span
                class="token operator">/</span>github<span
                class="token punctuation">.</span>com<span class="token operator">/</span>SeayXu<span
                class="token operator">/</span>

__ SeayXu_
<span aria-hidden="true"
      class="line-numbers-rows"><span></span><span></span><span></span><span></span><span></span></span></code></pre>
</div>
<p><a href="https://link.jianshu.com?t=https://github.com/SeayXu/" target="_blank" rel="nofollow">SeayXu</a> 是 <a
        href="https://link.jianshu.com?t=https://github.com/SeayXu/" target="_blank" rel="nofollow">我的 GitHub
    用户名</a>。</p>
<h2>隐式超链接(Implicit Hyperlink)</h2>
<p>小节标题、脚注和引用参考会自动生成超链接地址，使用小节标题、脚注或引用参考名称作为超链接名称就可以生成隐式链接。</p>
<div class="_2Uzcx_">
    <button class="VJbwyy" type="button" aria-label="复制代码"><i aria-label="icon: copy" class="anticon anticon-copy">
        <svg viewBox="64 64 896 896" focusable="false" class="" data-icon="copy" width="1em" height="1em"
             fill="currentColor" aria-hidden="true">
            <path d="M832 64H296c-4.4 0-8 3.6-8 8v56c0 4.4 3.6 8 8 8h496v688c0 4.4 3.6 8 8 8h56c4.4 0 8-3.6 8-8V96c0-17.7-14.3-32-32-32zM704 192H192c-17.7 0-32 14.3-32 32v530.7c0 8.5 3.4 16.6 9.4 22.6l173.3 173.3c2.2 2.2 4.7 4 7.4 5.5v1.9h4.2c3.5 1.3 7.2 2 11 2H704c17.7 0 32-14.3 32-32V224c0-17.7-14.3-32-32-32zM350 856.2L263.9 770H350v86.2zM664 888H414V746c0-22.1-17.9-40-40-40H232V264h432v624z"></path>
        </svg>
    </i></button>
    <pre class="line-numbers  language-go"><code class="  language-go">第一节 介绍
<span class="token operator">==</span><span class="token operator">==</span><span class="token operator">==</span><span
                class="token operator">==</span><span class="token operator">==</span><span
                class="token operator">=</span>

其他内容<span class="token operator">...</span>

隐式链接到 <span class="token string">`第一节 介绍`</span><span class="token boolean">_</span>，即可生成超链接。
<span aria-hidden="true"
      class="line-numbers-rows"><span></span><span></span><span></span><span></span><span></span><span></span></span></code></pre>
</div>
<p>&lt;h6 id="id2"&gt;第一节 介绍&lt;/h6&gt;</p>
<p>其他内容...</p>
<p>隐式链接到 <a href="#id2" target="_blank">第一节 介绍</a>，即可生成超链接。</p>
<h2>替换引用(Substitution Reference)</h2>
<p>替换引用就是用定义的指令替换对应的文字或图片，和内置指令(inline directives)类似。</p>
<div class="_2Uzcx_">
    <button class="VJbwyy" type="button" aria-label="复制代码"><i aria-label="icon: copy" class="anticon anticon-copy">
        <svg viewBox="64 64 896 896" focusable="false" class="" data-icon="copy" width="1em" height="1em"
             fill="currentColor" aria-hidden="true">
            <path d="M832 64H296c-4.4 0-8 3.6-8 8v56c0 4.4 3.6 8 8 8h496v688c0 4.4 3.6 8 8 8h56c4.4 0 8-3.6 8-8V96c0-17.7-14.3-32-32-32zM704 192H192c-17.7 0-32 14.3-32 32v530.7c0 8.5 3.4 16.6 9.4 22.6l173.3 173.3c2.2 2.2 4.7 4 7.4 5.5v1.9h4.2c3.5 1.3 7.2 2 11 2H704c17.7 0 32-14.3 32-32V224c0-17.7-14.3-32-32-32zM350 856.2L263.9 770H350v86.2zM664 888H414V746c0-22.1-17.9-40-40-40H232V264h432v624z"></path>
        </svg>
    </i></button>
    <pre class="line-numbers  language-cpp"><code class="  language-cpp">这是 <span
            class="token operator">|</span>logo<span
            class="token operator">|</span> github的Logo，我的github用户名是<span class="token operator">:</span><span
            class="token operator">|</span>name<span class="token operator">|</span>。

<span class="token punctuation">.</span><span class="token punctuation">.</span> <span class="token operator">|</span>logo<span
                class="token operator">|</span> image<span class="token operator">::</span> https<span
                class="token operator">:</span><span class="token operator">/</span><span
                class="token operator">/</span>help<span class="token punctuation">.</span>github<span
                class="token punctuation">.</span>com<span class="token operator">/</span>assets<span
                class="token operator">/</span>images<span class="token operator">/</span>site<span
                class="token operator">/</span>favicon<span class="token punctuation">.</span>ico
<span class="token punctuation">.</span><span class="token punctuation">.</span> <span class="token operator">|</span>name<span
                class="token operator">|</span> replace<span class="token operator">::</span> SeayXu
<span aria-hidden="true"
      class="line-numbers-rows"><span></span><span></span><span></span><span></span></span></code></pre>
</div>
<p></p>
<p></p>
这是
<div class="image-package">
    <img src="https://help.github.com/assets/images/site/favicon.ico"
         data-original-src="https://help.github.com/assets/images/site/favicon.ico" data-image-index="1"
         style="cursor: zoom-in;">
    <div class="image-caption"></div>
</div>
<p> GitHub的Logo，我的github用户名是:SeayXu。</p>

<h2>脚注引用(Footnote Reference)</h2>
<p>脚注引用，有这几个方式：有手工序号(标记序号123之类)、自动序号(填入#号会自动填充序号)、自动符号(填入*会自动生成符号)。</p>
<p>手工序号可以和#结合使用，会自动延续手工的序号。</p>
<p><strong>#</strong> 表示的方法可以在后面加上一个名称，这个名称就会生成一个链接。</p>
<div class="_2Uzcx_">
    <button class="VJbwyy" type="button" aria-label="复制代码"><i aria-label="icon: copy" class="anticon anticon-copy">
        <svg viewBox="64 64 896 896" focusable="false" class="" data-icon="copy" width="1em" height="1em"
             fill="currentColor" aria-hidden="true">
            <path d="M832 64H296c-4.4 0-8 3.6-8 8v56c0 4.4 3.6 8 8 8h496v688c0 4.4 3.6 8 8 8h56c4.4 0 8-3.6 8-8V96c0-17.7-14.3-32-32-32zM704 192H192c-17.7 0-32 14.3-32 32v530.7c0 8.5 3.4 16.6 9.4 22.6l173.3 173.3c2.2 2.2 4.7 4 7.4 5.5v1.9h4.2c3.5 1.3 7.2 2 11 2H704c17.7 0 32-14.3 32-32V224c0-17.7-14.3-32-32-32zM350 856.2L263.9 770H350v86.2zM664 888H414V746c0-22.1-17.9-40-40-40H232V264h432v624z"></path>
        </svg>
    </i></button>
    <pre class="line-numbers  language-css"><code class="  language-css">脚注引用一 [1]_
脚注引用二 [#]_
脚注引用三 [#链接]_
脚注引用四 [*]_
脚注引用五 [*]_
脚注引用六 [*]_

.. [1] 脚注内容一
.. [2] 脚注内容二
.. [#] 脚注内容三
.. [#链接] 脚注内容四 链接_
.. [*] 脚注内容五
.. [*] 脚注内容六
.. [*] 脚注内容七
<span aria-hidden="true"
      class="line-numbers-rows"><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span></span></code></pre>
</div>
<p>脚注引用一 <a href="#id3" target="_blank">[1]</a>&lt;a id="id9"&gt;&lt;/a&gt;<br>
    脚注引用二 <a href="#id4" target="_blank">[3]</a>&lt;a id="id10"&gt;&lt;/a&gt;<br>
    脚注引用三 <a href="#id5" target="_blank">[4]</a>&lt;a id="id11"&gt;&lt;/a&gt;<br>
    脚注引用四 <a href="#id6" target="_blank">[*]</a>&lt;a id="id12"&gt;&lt;/a&gt;<br>
    脚注引用五 <a href="#id7" target="_blank">[†]</a>&lt;a id="id13"&gt;&lt;/a&gt;<br>
    脚注引用六 <a href="#id8" target="_blank">[‡]</a>&lt;a id="id14"&gt;&lt;/a&gt;</p>
<p><a href="#id9" target="_blank">[1]</a>&lt;a id="id3"&gt;&lt;/a&gt; 脚注内容一<br>
    [2] 脚注内容二<br>
    <a href="#id10" target="_blank">[3]</a>&lt;a id="id4"&gt;&lt;/a&gt; 脚注内容三<br>
    <a href="#id11" target="_blank">[4]</a>&lt;a id="id5"&gt;&lt;/a&gt; 脚注内容四 <a href="#id11" target="_blank">链接</a>
    <br>
    <a href="#id12" target="_blank">[*]</a>&lt;a id="id6"&gt;&lt;/a&gt; 脚注内容五<br>
    <a href="#id13" target="_blank">[†]</a>&lt;a id="id7"&gt;&lt;/a&gt; 脚注内容六<br>
    <a href="#id14" target="_blank">[‡]</a>&lt;a id="id8"&gt;&lt;/a&gt; 脚注内容七</p>
<h2>引用参考(Citation Reference)</h2>
<p>引用参考与上面的脚注有点类似。</p>
<div class="_2Uzcx_">
    <button class="VJbwyy" type="button" aria-label="复制代码"><i aria-label="icon: copy" class="anticon anticon-copy">
        <svg viewBox="64 64 896 896" focusable="false" class="" data-icon="copy" width="1em" height="1em"
             fill="currentColor" aria-hidden="true">
            <path d="M832 64H296c-4.4 0-8 3.6-8 8v56c0 4.4 3.6 8 8 8h496v688c0 4.4 3.6 8 8 8h56c4.4 0 8-3.6 8-8V96c0-17.7-14.3-32-32-32zM704 192H192c-17.7 0-32 14.3-32 32v530.7c0 8.5 3.4 16.6 9.4 22.6l173.3 173.3c2.2 2.2 4.7 4 7.4 5.5v1.9h4.2c3.5 1.3 7.2 2 11 2H704c17.7 0 32-14.3 32-32V224c0-17.7-14.3-32-32-32zM350 856.2L263.9 770H350v86.2zM664 888H414V746c0-22.1-17.9-40-40-40H232V264h432v624z"></path>
        </svg>
    </i></button>
    <pre class="line-numbers  language-css"><code class="  language-css">引用参考的内容通常放在页面结尾处，比如 [One]_，Two_

.. [One] 参考引用一
.. [Two] 参考引用二
<span aria-hidden="true"
      class="line-numbers-rows"><span></span><span></span><span></span><span></span></span></code></pre>
</div>
<p>引用参考的内容通常放在页面结尾处，比如 <a href="#15" target="_blank">[One]</a>&lt;a id="id17"&gt;&lt;/a&gt;，<a href="#16"
                                                                                               target="_blank">Two</a>
</p>
<blockquote>
    <p><a href="#17" target="_blank">[One]</a>&lt;a id="id15"&gt;&lt;/a&gt; 参考引用一<br>
        [Two]&lt;a id="id16"&gt;&lt;/a&gt; 参考引用二</p>
</blockquote>
<h1>注释(Comments)</h1>
<p>注释以 <strong>..</strong> 开头，后面接注释内容即可，可以是多行内容，多行时每行开头要加一个空格。</p>
<div class="_2Uzcx_">
    <button class="VJbwyy" type="button" aria-label="复制代码"><i aria-label="icon: copy" class="anticon anticon-copy">
        <svg viewBox="64 64 896 896" focusable="false" class="" data-icon="copy" width="1em" height="1em"
             fill="currentColor" aria-hidden="true">
            <path d="M832 64H296c-4.4 0-8 3.6-8 8v56c0 4.4 3.6 8 8 8h496v688c0 4.4 3.6 8 8 8h56c4.4 0 8-3.6 8-8V96c0-17.7-14.3-32-32-32zM704 192H192c-17.7 0-32 14.3-32 32v530.7c0 8.5 3.4 16.6 9.4 22.6l173.3 173.3c2.2 2.2 4.7 4 7.4 5.5v1.9h4.2c3.5 1.3 7.2 2 11 2H704c17.7 0 32-14.3 32-32V224c0-17.7-14.3-32-32-32zM350 856.2L263.9 770H350v86.2zM664 888H414V746c0-22.1-17.9-40-40-40H232V264h432v624z"></path>
        </svg>
    </i></button>
    <pre class="line-numbers  language-undefined"><code class="  language-undefined">..
 我是注释内容
 你们看不到我
<span aria-hidden="true" class="line-numbers-rows"><span></span><span></span><span></span></span></code></pre>
</div>
<p>关于 <a
        href="https://link.jianshu.com?t=https://github.com/SeayXu/CheatSheet/blob/master/files/reStructuredText-Directives-Syntax.md"
        target="_blank" rel="nofollow">指令(Directives)</a>，在下一篇中专门做语法说明。</p>
<p>如果有不正确的地方，希望你能指出。</p>
