---
title: 'Sass中父选择器的标识符&'
date:       2019-09-20
tags:
	- web
	- html
	- solution
	- sass
---

### 启航

<div class="content-intro view-box "><p></p><p> 一般情况下，<code>sass</code>在解开一个嵌套规则时就会把父选择器(<code>#content</code>)通过一个空格连接到子选择器的前边(<code>article</code>和<code>aside</code>)形成(<code>#content article</code>和<code>#content aside</code>)。这种在CSS里边被称为后代选择器，因为它选择ID为<code>content</code>的元素内所有命中选择器<code>article</code>和<code>aside</code>的元素。但在有些情况下你却不会希望<code>sass</code>使用这种后代选择器的方式生成这种连接。</p><p>最常见的一种情况是当你为链接之类的元素写<code>:hover</code>这种伪类时，你并不希望以后代选择器的方式连接。比如说，下面这种情况<code>sass</code>就无法正常工作:</p><pre><a class="code-copy right0" title="复制到剪切板"><i class="icon-copy"></i></a><code class="hljs ruby"><span>article</span> <span>a</span> {
  <span><span class="hljs-symbol"><span class="hljs-symbol">color</span></span></span><span><span class="hljs-symbol"><span class="hljs-symbol">:</span></span> blue;</span>
  <span><span class="hljs-symbol"><span class="hljs-symbol">:hover</span></span></span> { <span><span class="hljs-symbol"><span class="hljs-symbol">color</span></span></span><span><span class="hljs-symbol"><span class="hljs-symbol">:</span></span> red }
}</span></code></pre><p>这意味着<code>color: red</code>这条规则将会被应用到选择器<code>article a :hover</code>，<code>article</code>元素内链接的所有子元素在被<code>hover</code>时都会变成红色。这是不正确的！你想把这条规则应用到超链接自身，而后代选择器的方式无法帮你实现。</p><p>解决之道为使用一个特殊的<code>sass</code>选择器，即父选择器。在使用嵌套规则时，父选择器能对于嵌套规则如何解开提供更好的控制。它就是一个简单的<code>&amp;</code>符号，且可以放在任何一个选择器可出现的地方，比如<code>h1</code>放在哪，它就可以放在哪。</p><pre><a class="code-copy right0" title="复制到剪切板"><i class="icon-copy"></i></a><code class="hljs ruby"><span>article</span> <span>a</span> {
  <span><span class="hljs-symbol"><span class="hljs-symbol">color</span></span></span><span><span class="hljs-symbol"><span class="hljs-symbol">:</span></span> blue;</span>
  &amp;<span><span class="hljs-symbol"><span class="hljs-symbol">:hover</span></span></span> { <span><span class="hljs-symbol"><span class="hljs-symbol">color</span></span></span><span><span class="hljs-symbol"><span class="hljs-symbol">:</span></span> red }
}</span></code></pre><p>当包含父选择器标识符的嵌套规则被打开时，它不会像后代选择器那样进行拼接，而是<code>&amp;</code>被父选择器直接替换:</p><pre><a class="code-copy right0" title="复制到剪切板"><i class="icon-copy"></i></a><code class="hljs css"><span><span class="hljs-selector-tag"><span class="hljs-selector-tag">article</span></span></span> <span><span class="hljs-selector-tag"><span class="hljs-selector-tag">a</span></span></span> <span>{ <span><span><span class="hljs-attribute"><span class="hljs-attribute">color</span></span></span>:<span> blue </span></span></span>}
<span><span class="hljs-selector-tag"><span class="hljs-selector-tag">article</span></span></span> <span><span class="hljs-selector-tag"><span class="hljs-selector-tag">a</span></span></span><span><span class="hljs-selector-pseudo"><span class="hljs-selector-pseudo">:hover</span></span></span> <span>{ <span><span><span class="hljs-attribute"><span class="hljs-attribute">color</span></span></span>:<span> red </span></span></span>}</code></pre><p>在为父级选择器添加<code>:hover</code>等伪类时，这种方式非常有用。同时父选择器标识符还有另外一种用法，你可以在父选择器之前添加选择器。举例来说，当用户在使用IE浏览器时，你会通过<code>JavaScript</code>在<code></code>标签上添加一个ie的类名，为这种情况编写特殊的样式如下:</p><pre><a class="code-copy right0" title="复制到剪切板"><i class="icon-copy"></i></a><code class="hljs markdown"><span><span class="hljs-section"><span class="hljs-section">#content</span></span></span><span class="hljs-section"><span class="hljs-section"> </span></span><span><span class="hljs-section"><span class="hljs-section">aside</span></span></span><span class="hljs-section"><span class="hljs-section"> {</span></span>
  <span>color</span><span>: red;</span>
  <span>body</span><span>.ie</span> &amp; { <span>color</span><span>: green }
}
</span></code></pre><pre><a class="code-copy right0" title="复制到剪切板"><i class="icon-copy"></i></a><code class="hljs css">
<span><span class="hljs-comment"><span class="hljs-comment">/*编译后*/</span></span></span>
<span><span class="hljs-selector-id"><span class="hljs-selector-id">#content</span></span></span> <span><span class="hljs-selector-tag"><span class="hljs-selector-tag">aside</span></span></span> <span>{<span><span><span class="hljs-attribute"><span class="hljs-attribute">color</span></span></span>:<span> red</span></span></span>};
<span><span class="hljs-selector-tag"><span class="hljs-selector-tag">body</span></span></span><span><span class="hljs-selector-class"><span class="hljs-selector-class">.ie</span></span></span> <span><span class="hljs-selector-id"><span class="hljs-selector-id">#content</span></span></span> <span><span class="hljs-selector-tag"><span class="hljs-selector-tag">aside</span></span></span> <span>{ <span><span><span class="hljs-attribute"><span class="hljs-attribute">color</span></span></span>:<span> green </span></span></span>}</code></pre><p><code>sass</code>在选择器嵌套上是非常智能的，即使是带有父选择器的情况。当<code>sass</code>遇到群组选择器(由多个逗号分隔开的选择器形成)也能完美地处理这种嵌套。</p><br></div>