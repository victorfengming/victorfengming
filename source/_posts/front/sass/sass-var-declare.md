---
title: 'Sass中变量声明'
date:       2019-09-20
tags:
	- web
	- html
	- solution
	- sass
---

### 启航

<div class="content-intro view-box "><p></p><p><code>sass</code>变量的声明和<code>css</code>属性的声明很像:</p>              <pre><a class="code-copy right0" title="复制到剪切板"><i class="icon-copy"></i></a><code class="hljs bash"><span><span class="hljs-variable"><span class="hljs-variable">$highlight</span></span>-color</span><span>: <span><span class="hljs-comment"><span class="hljs-comment">#F90</span></span></span><span class="hljs-comment"><span class="hljs-comment">;</span></span></span></code></pre>              <p>这意味着变量<code>$highlight-color</code>现在的值是<code>#F90</code>。任何可以用作<code>css</code>属性值的赋值都可以用作<code>sass</code>的变量值，甚至是以空格分割的多个属性值，如<code>$basic-border: 1px solidblack;</code>，或以逗号分割的多个属性值，如<code>$plain-font: "Myriad Pro"、Myriad、"HelveticaNeue"、Helvetica、"Liberation Sans"、Arial和sans-serif; sans-serif;</code>。这时变量还没有生效，除非你引用这个变量——我们很快就会了解如何引用。</p><p>与<code>CSS</code>属性不同，变量可以在<code>css</code>规则块定义之外存在。当变量定义在<code>css</code>规则块内，那么该变量只能在此规则块内使用。如果它们出现在任何形式的<code>{...}</code>块中(如<code>@media</code>或者<code>@font-face</code>块)，情况也是如此:</p><pre><a class="code-copy right0" title="复制到剪切板"><i class="icon-copy"></i></a><code class="hljs php"><span>$nav-color</span><span>: <span><span class="hljs-comment"><span class="hljs-comment">#F90</span></span></span><span class="hljs-comment"><span class="hljs-comment">;</span></span></span>
<span>nav</span> {
  <span>$width</span><span>: <span><span class="hljs-number"><span class="hljs-number">100</span></span>px</span>;</span>
  <span>width</span><span>: <span>$width</span>;</span>
  <span>color</span><span>: <span>$nav-color</span>;</span>
}

<span><span class="hljs-comment"><span class="hljs-comment">//编译后</span></span></span>

<span>nav</span> {
  <span>width</span><span>: <span><span class="hljs-number"><span class="hljs-number">100</span></span>px</span>;</span>
  <span>color</span><span>: <span><span class="hljs-comment"><span class="hljs-comment">#F90</span></span></span><span class="hljs-comment"><span class="hljs-comment">;</span></span></span>
}
</code></pre><p>在这段代码中，<code>$nav-color</code>这个变量定义在了规则块外边，所以在这个样式表中都可以像<code>nav</code>规则块那样引用它。<code>$width</code>这个变量定义在了<code>nav</code>的<code>{ }</code>规则块内，所以它只能在<code>nav</code>规则块内使用。这意味着是你可以在样式表的其他地方定义和使用<code>$width</code>变量，不会对这里造成影响。</p><p>只声明变量其实没啥用处，我们最终的目的还是使用它们。上例已介绍了如何使用<code>$nav-color</code>和<code>$width</code>这两个变量，接下来我们将进一步探讨变量的使用方法。</p><br></div>