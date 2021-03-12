---
title: '关于Sass变量名用中划线还是下划线分隔问题'
date:       2019-09-20
tags:
	- web
	- html
	- solution
	- sass
---

### 开门见山
**这个问题说白了就是你爱用啥用啥,都通用的**


<div class="content-intro view-box "><p></p><p><code>sass</code>的变量名可以与<code>css</code>中的属性名和选择器名称相同，包括中划线和下划线。这完全取决于个人的喜好，有些人喜欢使用中划线来分隔变量中的多个词(如<code>$highlight-color</code>)，而有些人喜欢使用下划线(如<code>$highlight_color</code>)。使用中划线的方式更为普遍，这也是<code>compass</code>和本文都用的方式。</p><p>不过，<code>sass</code>并不想强迫任何人一定使用中划线或下划线，所以这两种用法相互兼容。用中划线声明的变量可以使用下划线的方式引用，反之亦然。这意味着即使<code>compass</code>选择用中划线的命名方式，这并不影响你在使用<code>compass</code>的样式中用下划线的命名方式进行引用:</p><pre><a class="code-copy right0" title="复制到剪切板"><i class="icon-copy"></i></a><code class="hljs php"><span>$link-color</span><span>: blue;</span>
<span>a</span> {
  <span>color</span><span>: <span>$link_color</span>;</span>
}

<span><span class="hljs-comment">//编译后</span></span>

<span>a</span> {
  <span>color</span><span>: blue;</span>
}</code></pre><p>在上例中，<code>$link-color</code>和<code>$link_color</code>其实指向的是同一个变量。实际上，在<code>sass</code>的大多数地方，中划线命名的内容和下划线命名的内容是互通的，除了变量，也包括对混合器和Sass函数的命名。但是在<code>sass</code>中纯<code>css</code>部分不互通，比如类名、ID或属性名。</p><p>尽管变量自身提供了很多有用的地方，但是<code>sass</code>基于变量提供的更为强大的工具才是我们关注的焦点。只有当变量与<code>sass</code>的其他特性一起使用时，才能发挥其全部的潜能。接下来，我们将探讨其中一个非常重要的特性，即规则嵌套。</p><br></div>