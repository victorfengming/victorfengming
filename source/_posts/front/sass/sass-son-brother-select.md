---
title: 'Sass中子组合选择器和同层组合选择器：>、+和~'
date:       2019-09-20
tags:
	- web
	- html
	- solution
	- sass
---

### 启航

<div class="content-intro view-box "><p></p><p>上边这三个组合选择器必须和其他选择器配合使用，以指定浏览器仅选择某种特定上下文中的元素。</p><pre><a class="code-copy right0" title="复制到剪切板"><i class="icon-copy"></i></a><code class="hljs css"><span><span class="hljs-selector-tag">article</span></span> <span><span class="hljs-selector-tag">section</span></span> <span>{ <span><span><span class="hljs-attribute">margin</span></span>:<span> <span><span class="hljs-number">5px</span></span> </span></span></span>}
<span><span class="hljs-selector-tag">article</span></span> &gt; <span><span class="hljs-selector-tag">section</span></span> <span>{ <span><span><span class="hljs-attribute">border</span></span>:<span> <span><span class="hljs-number">1px</span></span> solid <span><span class="hljs-number">#ccc</span></span> </span></span></span>}</code></pre><p>你可以用子组合选择器&gt;选择一个元素的直接子元素。上例中，第一个选择器会选择article下的所有命中section选择器的元素。第二个选择器只会选择article下紧跟着的子元素中命中section选择器的元素。</p><p>在下例中，你可以用同层相邻组合选择器<code>+</code>选择<code>header</code>元素后紧跟的<code>p</code>元素:</p><pre><a class="code-copy right0" title="复制到剪切板"><i class="icon-copy"></i></a><code class="hljs css"><span><span class="hljs-selector-tag">header</span></span> + <span><span class="hljs-selector-tag">p</span></span> <span>{ <span><span><span class="hljs-attribute">font-size</span></span>:<span> <span><span class="hljs-number">1.1em</span></span> </span></span></span>}</code></pre><p>你也可以用同层全体组合选择器<code>~</code>，选择所有跟在<code>article</code>后的同层<code>article</code>元素，不管它们之间隔了多少其他元素:</p><pre><a class="code-copy right0" title="复制到剪切板"><i class="icon-copy"></i></a><code class="hljs css"><span><span class="hljs-selector-tag">article</span></span> ~ <span><span class="hljs-selector-tag">article</span></span> <span>{ <span><span><span class="hljs-attribute">border-top</span></span>:<span> <span><span class="hljs-number">1px</span></span> dashed <span><span class="hljs-number">#ccc</span></span> </span></span></span>}</code></pre><p>这些组合选择器可以毫不费力地应用到<code>sass</code>的规则嵌套中。可以把它们放在外层选择器后边，或里层选择器前边:</p><pre><a class="code-copy right0" title="复制到剪切板"><i class="icon-copy"></i></a><code class="hljs bash"><span>article</span> {
  ~ <span>article</span> { <span>border-top</span><span>: <span>1px</span> dashed <span><span class="hljs-comment">#ccc</span></span><span class="hljs-comment"> }</span>
  &gt; </span><span><span>section</span></span><span> { </span><span><span>background</span></span><span>: <span><span class="hljs-comment">#eee</span></span><span class="hljs-comment"> }</span>
  </span><span><span>dl</span></span><span> &gt; {
    </span><span><span>dt</span></span><span> { </span><span><span>color</span></span><span>: <span><span class="hljs-comment">#333</span></span><span class="hljs-comment"> }</span>
    </span><span><span>dd</span></span><span> { </span><span><span>color</span></span><span>: <span><span class="hljs-comment">#555</span></span><span class="hljs-comment"> }</span>
  }
  </span><span><span>nav</span></span><span> + &amp; { </span><span><span>margin-top</span></span><span>: <span>0</span> }
}</span></code></pre><p><code>sass</code>会如你所愿地将这些嵌套规则一一解开组合在一起:</p><pre><a class="code-copy right0" title="复制到剪切板"><i class="icon-copy"></i></a><code class="hljs css"><span><span class="hljs-selector-tag">article</span></span> ~ <span><span class="hljs-selector-tag">article</span></span> <span>{ <span><span><span class="hljs-attribute">border-top</span></span>:<span> <span><span class="hljs-number">1px</span></span> dashed <span><span class="hljs-number">#ccc</span></span> </span></span></span>}
<span><span class="hljs-selector-tag">article</span></span> &gt; <span><span class="hljs-selector-tag">footer</span></span> <span>{ <span><span><span class="hljs-attribute">background</span></span>:<span> <span><span class="hljs-number">#eee</span></span> </span></span></span>}
<span><span class="hljs-selector-tag">article</span></span> <span><span class="hljs-selector-tag">dl</span></span> &gt; <span><span class="hljs-selector-tag">dt</span></span> <span>{ <span><span><span class="hljs-attribute">color</span></span>:<span> <span><span class="hljs-number">#333</span></span> </span></span></span>}
<span><span class="hljs-selector-tag">article</span></span> <span><span class="hljs-selector-tag">dl</span></span> &gt; <span><span class="hljs-selector-tag">dd</span></span> <span>{ <span><span><span class="hljs-attribute">color</span></span>:<span> <span><span class="hljs-number">#555</span></span> </span></span></span>}
<span><span class="hljs-selector-tag">nav</span></span> + <span><span class="hljs-selector-tag">article</span></span> <span>{ <span><span><span class="hljs-attribute">margin-top</span></span>:<span> <span><span class="hljs-number">0</span></span> </span></span></span>}</code></pre><p>在<code>sass</code>中，不仅仅<code>css</code>规则可以嵌套，对属性进行嵌套也可以减少很多重复性的工作。</p></div>