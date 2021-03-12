---
title: 'Sass中嵌套属性'
date:       2019-09-20
tags:
	- web
	- html
	- solution
	- sass
---

### 启航

<div class="content-intro view-box "><p></p><p>在<code>sass</code>中，除了CSS选择器，属性也可以进行嵌套。尽管编写属性涉及的重复不像编写选择器那么糟糕，但是要反复写<code>border-style</code><code>border-width</code><code>border-color</code>以及<code>border-*</code>等也是非常烦人的。在<code>sass</code>中，你只需敲写一遍<code>border</code>:</p><pre><a class="code-copy right0" title="复制到剪切板"><i class="icon-copy"></i></a><code class="hljs css"><span><span class="hljs-selector-tag">nav</span></span> {
  <span><span class="hljs-attribute">border</span></span><span>: {
  style: solid;</span>
  <span><span class="hljs-attribute">width</span></span><span>: <span><span class="hljs-number">1px</span></span>;</span>
  <span><span class="hljs-attribute">color</span></span><span>: <span><span class="hljs-number">#ccc</span></span>;</span>
  }
}</code></pre><p>嵌套属性的规则是这样的:把属性名从中划线-的地方断开，在根属性后边添加一个冒号:，紧跟一个<code>{ }</code>块，把子属性部分写在这个<code>{ }</code>块中。就像<code>css</code>选择器嵌套一样，<code>sass</code>会把你的子属性一一解开，把根属性和子属性部分通过中划线-连接起来，最后生成的效果与你手动一遍遍写的<code>css</code>样式一样:</p><pre><a class="code-copy right0" title="复制到剪切板"><i class="icon-copy"></i></a><code class="hljs css"><span><span class="hljs-selector-tag">nav</span></span> <span>{
  <span><span><span class="hljs-attribute">border-style</span></span>:<span> solid</span></span>;
  <span><span><span class="hljs-attribute">border-width</span></span>:<span> <span><span class="hljs-number">1px</span></span></span></span>;
  <span><span><span class="hljs-attribute">border-color</span></span>:<span> <span><span class="hljs-number">#ccc</span></span></span></span>;
<span>}</span></span></code></pre><p>对于属性的缩写形式，你甚至可以像下边这样来嵌套，指明例外规则:</p><pre><a class="code-copy right0" title="复制到剪切板"><i class="icon-copy"></i></a><code class="hljs css"><span><span class="hljs-selector-tag">nav</span></span> {
  <span><span class="hljs-attribute">border</span></span><span>: <span><span class="hljs-number">1px</span></span> solid <span><span class="hljs-number">#ccc</span></span> {
  left: <span><span class="hljs-number">0px</span></span>;</span>
  <span><span class="hljs-attribute">right</span></span><span>: <span><span class="hljs-number">0px</span></span>;</span>
  }
}</code></pre><p>这比下边这种同等样式的写法要好:</p><pre><a class="code-copy right0" title="复制到剪切板"><i class="icon-copy"></i></a><code class="hljs css"><span><span class="hljs-selector-tag">nav</span></span> <span>{
  <span><span><span class="hljs-attribute">border</span></span>:<span> <span><span class="hljs-number">1px</span></span> solid <span><span class="hljs-number">#ccc</span></span></span></span>;
  <span><span><span class="hljs-attribute">border-left</span></span>:<span> <span><span class="hljs-number">0px</span></span></span></span>;
  <span><span><span class="hljs-attribute">border-right</span></span>:<span> <span><span class="hljs-number">0px</span></span></span></span>;
<span>}</span></span></code></pre><p>属性和选择器嵌套是非常伟大的特性，因为它们不仅大大减少了你的编写量，而且通过视觉上的缩进使你编写的样式结构更加清晰，更易于阅读和开发。</p><p>即便如此，随着你的样式表变得越来越大，这种写法也很难保持结构清晰。有时，处理这种大量样式的唯一方法就是把它们分拆到多个文件中。<code>sass</code>通过对<code>css</code>原有<code>@import</code>规则的改进直接支持了这一特性。</p></div>