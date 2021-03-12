---
title: 'Sass中变量的引用'
cover: "/img/lynk/21.jpg"
date:       2019-09-20
tags:
	- web
	- html
	- solution
	- sass
---

### 启航
<div class="content-intro view-box "><p></p><p>凡是<code>css</code>属性的标准值(比如说1px或者bold)可存在的地方，变量就可以使用。<code>css</code>生成时，变量会被它们的值所替代。之后，如果你需要一个不同的值，只需要改变这个变量的值，则所有引用此变量的地方生成的值都会随之改变。</p><pre><a class="code-copy right0" title="复制到剪切板"><i class="icon-copy"></i></a><code class="hljs php"><span>$highlight-color</span><span>: <span><span class="hljs-comment">#F90</span></span><span class="hljs-comment">;</span></span>
<span>.selected</span> {
  <span>border</span><span>: <span><span class="hljs-number">1</span>px</span> solid <span>$highlight-color</span>;</span>
}

<span><span class="hljs-comment">//编译后</span></span>

<span>.selected</span> {
  <span>border</span><span>: <span><span class="hljs-number">1</span>px</span> solid <span><span class="hljs-comment">#F90</span></span><span class="hljs-comment">;</span></span>
}
</code></pre><p>看上边示例中的<code>$highlight-color</code>变量，它被直接赋值给<code>border</code>属性，当这段代码被编译输出<code>css</code>时，<code>$highlight-color</code>会被<code>#F90</code>这一颜色值所替代。产生的效果就是给<code>selected</code>这个类一条1像素宽、实心且颜色值为<code>#F90</code>的边框。</p><p>在声明变量时，变量值也可以引用其他变量。当你通过粒度区分，为不同的值取不同名字时，这相当有用。下例在独立的颜色值粒度上定义了一个变量，且在另一个更复杂的边框值粒度上也定义了一个变量:</p><pre><a class="code-copy right0" title="复制到剪切板"><i class="icon-copy"></i></a><code class="hljs php"><span>$highlight-color</span><span>: <span><span class="hljs-comment">#F90</span></span><span class="hljs-comment">;</span></span>
<span>$highlight-border</span><span>: <span><span class="hljs-number">1</span>px</span> solid <span>$highlight-color</span>;</span>
<span>.selected</span> {
  <span>border</span><span>: <span>$highlight-border</span>;</span>
}

<span><span class="hljs-comment">//编译后</span></span>

<span>.selected</span> {
  <span>border</span><span>: <span><span class="hljs-number">1</span>px</span> solid <span><span class="hljs-comment">#F90</span></span><span class="hljs-comment">;</span></span>
}</code></pre><p>这里，<code>$highlight-border</code>变量的声明中使用了<code>$highlight-color</code>这个变量。产生的效果就跟你直接为<code>border</code>属性设置了一个<code>1px</code> <code>$highlight-color solid</code>的值是一样的。最后，我们来了解一下变量命名的实用技巧，以结束关于变量的介绍。</p><br></div>