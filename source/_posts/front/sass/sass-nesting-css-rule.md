---
title: 'Sass中嵌套CSS的规则'
cover: "/img/lynk/6.jpg"
date:       2019-09-20
tags:
	- web
	- html
	- solution
	- sass
	- css
---

### 启航

<div class="content-intro view-box "><p></p><p><code>css</code>中重复写选择器是非常恼人的。如果要写一大串指向页面中同一块的样式时，往往需要一遍又一遍地写同一个<code>ID</code>:</p><pre><a class="code-copy right0" title="复制到剪切板"><i class="icon-copy"></i></a><code class="hljs css"><span><span class="hljs-selector-id">#content</span></span> <span><span class="hljs-selector-tag">article</span></span> <span><span class="hljs-selector-tag">h1</span></span> <span>{ <span><span><span class="hljs-attribute">color</span></span>:<span> <span><span class="hljs-number">#333</span></span> </span></span></span>}
<span><span class="hljs-selector-id">#content</span></span> <span><span class="hljs-selector-tag">article</span></span> <span><span class="hljs-selector-tag">p</span></span> <span>{ <span><span><span class="hljs-attribute">margin-bottom</span></span>:<span> <span><span class="hljs-number">1.4em</span></span> </span></span></span>}
<span><span class="hljs-selector-id">#content</span></span> <span><span class="hljs-selector-tag">aside</span></span> <span>{ <span><span><span class="hljs-attribute">background-color</span></span>:<span> <span><span class="hljs-number">#EEE</span></span> </span></span></span>}</code></pre><p>像这种情况，<code>sass</code>可以让你只写一遍，且使样式可读性更高。在Sass中，你可以像俄罗斯套娃那样在规则块中嵌套规则块。<code>sass</code>在输出<code>css</code>时会帮你把这些嵌套规则处理好，避免你的重复书写。</p><pre><a class="code-copy right0" title="复制到剪切板"><i class="icon-copy"></i></a><code class="hljs bash"><span><span class="hljs-comment">#content</span></span><span class="hljs-comment"> {</span>
  <span>article</span> {
    <span>h1</span> { <span>color</span><span>: <span><span class="hljs-comment">#333</span></span><span class="hljs-comment"> }</span>
    </span><span><span>p</span></span><span> { </span><span><span>margin-bottom</span></span><span>: <span>1.4em</span> }
  }
  </span><span><span>aside</span></span><span> { </span><span><span>background-color</span></span><span>: <span><span class="hljs-comment">#EEE</span></span><span class="hljs-comment"> }</span>
}
</span></code></pre><pre><a class="code-copy right0" title="复制到剪切板"><i class="icon-copy"></i></a><code class="hljs css"> <span><span class="hljs-comment">/* 编译后 */</span></span>
<span><span class="hljs-selector-id">#content</span></span> <span><span class="hljs-selector-tag">article</span></span> <span><span class="hljs-selector-tag">h1</span></span> <span>{ <span><span><span class="hljs-attribute">color</span></span>:<span> <span><span class="hljs-number">#333</span></span> </span></span></span>}
<span><span class="hljs-selector-id">#content</span></span> <span><span class="hljs-selector-tag">article</span></span> <span><span class="hljs-selector-tag">p</span></span> <span>{ <span><span><span class="hljs-attribute">margin-bottom</span></span>:<span> <span><span class="hljs-number">1.4em</span></span> </span></span></span>}
<span><span class="hljs-selector-id">#content</span></span> <span><span class="hljs-selector-tag">aside</span></span> <span>{ <span><span><span class="hljs-attribute">background-color</span></span>:<span> <span><span class="hljs-number">#EEE</span></span> </span></span></span>}</code></pre><p>上边的例子，会在输出<code>css</code>时把它转换成跟你之前看到的一样的效果。这个过程中，<code>sass</code>用了两步，每一步都是像打开俄罗斯套娃那样把里边的嵌套规则块一个个打开。首先，把<code>#content</code>(父级)这个<code>id</code>放到<code>article</code>选择器(子级)和<code>aside</code>选择器(子级)的前边:</p><pre><a class="code-copy right0" title="复制到剪切板"><i class="icon-copy"></i></a><code class="hljs bash"><span><span class="hljs-comment">#content</span></span><span class="hljs-comment"> {</span>
  <span>article</span> {
    <span>h1</span> { <span>color</span><span>: <span><span class="hljs-comment">#333</span></span><span class="hljs-comment"> }</span>
    </span><span><span>p</span></span><span> { </span><span><span>margin-bottom</span></span><span>: <span>1.4em</span> }
  }
  </span><span><span><span><span class="hljs-comment">#c</span></span><span class="hljs-comment">ontent</span></span></span><span><span class="hljs-comment"> </span></span><span><span><span class="hljs-comment">aside</span></span></span><span><span class="hljs-comment"> { </span></span><span><span><span class="hljs-comment">background-color</span></span></span><span><span class="hljs-comment">: </span><span><span class="hljs-comment">#EEE</span></span><span class="hljs-comment"> }</span>
}
</span></code></pre><pre><a class="code-copy right0" title="复制到剪切板"><i class="icon-copy"></i></a><code class="hljs css"> <span><span class="hljs-comment">/* 编译后 */</span></span>
<span><span class="hljs-selector-id">#content</span></span> <span><span class="hljs-selector-tag">article</span></span> <span><span class="hljs-selector-tag">h1</span></span> <span>{ <span><span><span class="hljs-attribute">color</span></span>:<span> <span><span class="hljs-number">#333</span></span> </span></span></span>}
<span><span class="hljs-selector-id">#content</span></span> <span><span class="hljs-selector-tag">article</span></span> <span><span class="hljs-selector-tag">p</span></span> <span>{ <span><span><span class="hljs-attribute">margin-bottom</span></span>:<span> <span><span class="hljs-number">1.4em</span></span> </span></span></span>}
<span><span class="hljs-selector-id">#content</span></span> <span><span class="hljs-selector-tag">aside</span></span> <span>{ <span><span><span class="hljs-attribute">background-color</span></span>:<span> <span><span class="hljs-number">#EEE</span></span> </span></span></span>}</code></pre><p>然后，<code>#content article</code>里边还有嵌套的规则，<code>sass</code>重复一遍上边的步骤，把新的选择器添加到内嵌的选择器前边。</p><p>一个给定的规则块，既可以像普通的CSS那样包含属性，又可以嵌套其他规则块。当你同时要为一个容器元素及其子元素编写特定样式时，这种能力就非常有用了。</p><pre><a class="code-copy right0" title="复制到剪切板"><i class="icon-copy"></i></a><code class="hljs bash"><span><span class="hljs-comment">#content</span></span><span class="hljs-comment"> {</span>
  <span>background-color</span><span>: <span><span class="hljs-comment">#f5f5f5</span></span><span class="hljs-comment">;</span></span>
  <span>aside</span> { <span>background-color</span><span>: <span><span class="hljs-comment">#eee</span></span><span class="hljs-comment"> }</span>
}</span></code></pre><p>容器元素的样式规则会被单独抽离出来，而嵌套元素的样式规则会像容器元素没有包含任何属性时那样被抽离出来。</p><pre><a class="code-copy right0" title="复制到剪切板"><i class="icon-copy"></i></a><code class="hljs css">
<span><span class="hljs-selector-id">#content</span></span> <span>{ <span><span><span class="hljs-attribute">background-color</span></span>:<span> <span><span class="hljs-number">#f5f5f5</span></span> </span></span></span>}
<span><span class="hljs-selector-id">#content</span></span> <span><span class="hljs-selector-tag">aside</span></span> <span>{ <span><span><span class="hljs-attribute">background-color</span></span>:<span> <span><span class="hljs-number">#eee</span></span> </span></span></span>}</code></pre><p>大多数情况下这种简单的嵌套都没问题，但是有些场景下不行，比如你想要在嵌套的选择器里边立刻应用一个类似于<code>:hover</code>的伪类。为了解决这种以及其他情况，<code>sass</code>提供了一个特殊结构<code>&amp;</code>。</p></div>