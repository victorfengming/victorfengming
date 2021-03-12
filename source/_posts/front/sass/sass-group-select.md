---
title: 'Sass中群组选择器的嵌套'
cover: "/img/lynk/45.jpg"
date:       2019-09-20
tags:
	- web
	- html
	- solution
	- sass
---

### 启航
<div class="content-bg">
<div class="content-intro view-box "><p></p><p>在<code>CSS</code>里边，选择器<code>h1</code><code>h2</code>和<code>h3</code>会同时命中h1元素、h2元素和h3元素。与此类似，<code>.button</code><code>button</code>会命中button元素和类名为.button的元素。这种选择器称为群组选择器。群组选择器的规则会对命中群组中任何一个选择器的元素生效。</p><pre><a class="code-copy right0" title="复制到剪切板"><i class="icon-copy"></i></a><code class="hljs css"><span><span class="hljs-selector-class">.button</span></span>, <span><span class="hljs-selector-tag">button</span></span> <span>{
  <span><span><span class="hljs-attribute">margin</span></span>:<span> <span><span class="hljs-number">0</span></span></span></span>;
<span>}</span></span></code></pre><p>当看到上边这段代码时，你可能还没意识到会有重复性的工作。但会很快发现:如果你需要在一个特定的容器元素内对这样一个群组选择器进行修饰，情况就不同了。<code>css</code>的写法会让你在群组选择器中的每一个选择器前都重复一遍容器元素的选择器。</p><pre><a class="code-copy right0" title="复制到剪切板"><i class="icon-copy"></i></a><code class="hljs css"><span><span class="hljs-selector-class">.container</span></span> <span><span class="hljs-selector-tag">h1</span></span>, <span><span class="hljs-selector-class">.container</span></span> <span><span class="hljs-selector-tag">h2</span></span>, <span><span class="hljs-selector-class">.container</span></span> <span><span class="hljs-selector-tag">h3</span></span> <span>{ <span><span><span class="hljs-attribute">margin-bottom</span></span>:<span> .<span><span class="hljs-number">8em</span></span> </span></span></span>}</code></pre><p>非常幸运，<code>sass</code>的嵌套特性在这种场景下也非常有用。当<code>sass</code>解开一个群组选择器规则内嵌的规则时，它会把每一个内嵌选择器的规则都正确地解出来:</p><pre><a class="code-copy right0" title="复制到剪切板"><i class="icon-copy"></i></a><code class="hljs"><span>.container</span> {
  <span>h1</span>, <span>h2</span>, <span>h3</span> {<span>margin-bottom</span><span>: .<span>8em</span>}
}</span></code></pre><p>首先<code>sass</code>将<code>.container</code>和<code>h1</code><code>.container</code>和<code>h2</code><code>.container</code>和<code>h3</code>分别组合，然后将三者重新组合成一个群组选择器，生成你前边看到的普通<code>css</code>样式。对于内嵌在群组选择器内的嵌套规则，处理方式也一样:</p><pre><a class="code-copy right0" title="复制到剪切板"><i class="icon-copy"></i></a><code class="hljs"><span>nav</span>, <span>aside</span> {
  <span>a</span> {<span>color</span><span>: blue}
}</span></code></pre><p>首先<code>sass</code>将<code>nav</code>和<code>a</code><code>aside</code>和<code>a</code>分别组合，然后将二者重新组合成一个群组选择器:</p><pre><a class="code-copy right0" title="复制到剪切板"><i class="icon-copy"></i></a><code class="hljs css"><span><span class="hljs-selector-tag">nav</span></span> <span><span class="hljs-selector-tag">a</span></span>, <span><span class="hljs-selector-tag">aside</span></span> <span><span class="hljs-selector-tag">a</span></span> <span>{<span><span><span class="hljs-attribute">color</span></span>:<span> blue</span></span></span>}</code></pre><p>处理这种群组选择器规则嵌套上的强大能力，正是<code>sass</code>在减少重复敲写方面的贡献之一。尤其在当嵌套级别达到两层甚至三层以上时，与普通的<code>css</code>编写方式相比，只写一遍群组选择器大大减少了工作量。</p><p>有利必有弊，你需要特别注意群组选择器的规则嵌套生成的<code>css</code>。虽然<code>sass</code>让你的样式表看上去很小，但实际生成的<code>css</code>却可能非常大，这会降低网站的速度。</p><p>关于选择器嵌套的最后一个方面，我们看看<code>sass</code>如何处理组合选择器，比如&gt;、+和~的使用。你将看到，这种场景下你甚至无需使用父选择器标识符。</p></div>
<div style="clear:both"></div>
</div>