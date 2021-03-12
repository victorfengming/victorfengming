---
title: '啥是静默注释'
date:       2019-09-20
subtitle: '在sass中'
tags:
	- web
	- html
	- solution
	- sass
---

### css中的注释
<div class="content-bg">
<div class="content-intro view-box "><p></p><p><code>css</code>中注释的作用包括帮助你组织样式、以后你看自己的代码时明白为什么这样写，以及简单的样式说明。但是，你并不希望每个浏览网站源码的人都能看到所有注释。</p>

<h3>sass中的注释</h3>

<p><code>sass</code>另外提供了一种不同于<code>css</code>标准注释格式<code>/* ... */</code>的注释语法，即静默注释，其内容不会出现在生成的<code>css</code>文件中。静默注释的语法跟<code>JavaScript</code><code>Java</code>等类<code>C</code>的语言中单行注释的语法相同，它们以<code>//</code>开头，注释内容直到行末。</p><pre><a class="code-copy right0" title="复制到剪切板"><i class="icon-copy"></i></a><code class="hljs cpp"><span>body</span> {
  <span>color</span><span>: <span>#<span class="hljs-number">333</span></span>;</span> <span><span class="hljs-comment">// 这种注释内容不会出现在生成的css文件中</span></span>
  <span>padding</span><span>: <span><span class="hljs-number">0</span></span>;</span> <span><span class="hljs-comment">/* 这种注释内容会出现在生成的css文件中 */</span></span>
}</code></pre><p>实际上，<code>css</code>的标准注释格式<code>/* ... */</code>内的注释内容亦可在生成的<code>css</code>文件中抹去。当注释出现在原生<code>css</code>不允许的地方，如在<code>css</code>属性或选择器中，<code>sass</code>将不知如何将其生成到对应<code>css</code>文件中的相应位置，于是这些注释被抹掉。</p><pre><a class="code-copy right0" title="复制到剪切板"><i class="icon-copy"></i></a><code class="hljs php"><span>body</span> {
  <span>color</span> <span><span class="hljs-comment">/* 这块注释内容不会出现在生成的css中 */</span></span><span>: <span><span class="hljs-comment">#333</span></span><span class="hljs-comment">;</span></span>
  <span>padding</span><span>: <span><span class="hljs-number">1</span></span>;</span> <span><span class="hljs-comment">/* 这块注释内容也不会出现在生成的css中 */</span></span> <span class="hljs-number">0</span>;
}
</code></pre><p>你已经掌握了<code>sass</code>的静默注释，了解了保持<code>sass</code>条理性和可读性的最基本的三个方法:嵌套、导入和注释。现在，我们要进一步学习新特性，这样我们不但能保持条理性还能写出更好的样式。首先要介绍的内容是:使用混合器抽象你的相关样式。</p></div>
<div style="clear:both"></div>
</div>