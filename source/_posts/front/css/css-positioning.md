---
title: 'CSS中的定位'
cover: "/img/lynk/2.jpg"
date:       2019-09-05
tags:
	- css
	- web
	- solution
---














[点击这里跳转W3c原文链接](https://www.w3school.com.cn/css/css_positioning.asp)  

<div id="maincontent">

<h1>CSS 定位 (Positioning)</h1>

<div id="tpn">
<ul class="prenext">
<li class="pre"><a href="/css/css_margin_collapsing.asp" title="CSS 外边距合并">CSS 外边距合并</a></li>
<li class="next"><a href="/css/css_positioning_relative.asp" title="CSS 相对定位">CSS 相对定位</a></li>
</ul>
</div>


<div id="intro">
<p><strong>CSS 定位 (Positioning) 属性允许你对元素进行定位。</strong></p>
</div>


<div>
<h2>CSS 定位和浮动</h2>

<p>CSS 为定位和浮动提供了一些属性，利用这些属性，可以建立列式布局，将布局的一部分与另一部分重叠，还可以完成多年来通常需要使用多个表格才能完成的任务。</p>

<p>定位的基本思想很简单，它允许你定义元素框相对于其正常位置应该出现的位置，或者相对于父元素、另一个元素甚至浏览器窗口本身的位置。显然，这个功能非常强大，也很让人吃惊。要知道，用户代理对 CSS2 中定位的支持远胜于对其它方面的支持，对此不应感到奇怪。</p>

<p>另一方面，CSS1 中首次提出了浮动，它以 Netscape 在 Web 发展初期增加的一个功能为基础。浮动不完全是定位，不过，它当然也不是正常流布局。我们会在后面的章节中明确浮动的含义。</p>
</div>


<div>
<h2>一切皆为框</h2>

<p>div、h1 或 p 元素常常被称为块级元素。这意味着这些元素显示为<em>一块内容</em>，即“块框”。与之相反，span 和 strong 等元素称为“行内元素”，这是因为它们的内容显示在行中，即“行内框”。</p>

<p>您可以使用 <a href="/cssref/pr_class_display.asp" title="CSS display 属性">display 属性</a>改变生成的框的类型。这意味着，通过将 display 属性设置为 block，可以让行内元素（比如 &lt;a&gt; 元素）表现得像块级元素一样。还可以通过把 display 设置为 none，让生成的元素根本没有框。这样的话，该框及其所有内容就不再显示，不占用文档中的空间。</p>

<p>但是在一种情况下，即使没有进行显式定义，也会创建块级元素。这种情况发生在把一些文本添加到一个块级元素（比如 div）的开头。即使没有把这些文本定义为段落，它也会被当作段落对待：</p>

<pre>&lt;div&gt;
some text
&lt;p&gt;Some more text.&lt;/p&gt;
&lt;/div&gt;
</pre>

<p>在这种情况下，这个框称为无名块框，因为它不与专门定义的元素相关联。</p>

<p>块级元素的文本行也会发生类似的情况。假设有一个包含三行文本的段落。每行文本形成一个无名框。无法直接对无名块或行框应用样式，因为没有可以应用样式的地方（注意，行框和行内框是两个概念）。但是，这有助于理解在屏幕上看到的所有东西都形成某种框。</p>
</div>


<div>
<h2>CSS 定位机制</h2>

<p>CSS 有三种基本的定位机制：普通流、浮动和绝对定位。</p>

<p>除非专门指定，否则所有框都在普通流中定位。也就是说，普通流中的元素的位置由元素在 (X)HTML 中的位置决定。</p>

<p>块级框从上到下一个接一个地排列，框之间的垂直距离是由框的垂直外边距计算出来。</p>

<p>行内框在一行中水平布置。可以使用水平内边距、边框和外边距调整它们的间距。但是，垂直内边距、边框和外边距不影响行内框的高度。由一行形成的水平框称为<em>行框（Line Box）</em>，行框的高度总是足以容纳它包含的所有行内框。不过，设置行高可以增加这个框的高度。</p>

<p>在下面的章节，我们会为您详细讲解相对定位、绝对定位和浮动。</p>
</div>


<div>
<h2>CSS position 属性</h2>

<p>通过使用 <a href="/cssref/pr_class_position.asp" title="CSS position 属性">position 属性</a>，我们可以选择 4 种不同类型的定位，这会影响元素框生成的方式。</p>

<p>position 属性值的含义：</p>

<dl class="define">
<dt>static</dt>
<dd>元素框正常生成。块级元素生成一个矩形框，作为文档流的一部分，行内元素则会创建一个或多个行框，置于其父元素中。</dd>

<dt>relative</dt>
<dd>元素框偏移某个距离。元素仍保持其未定位前的形状，它原本所占的空间仍保留。</dd>

<dt>absolute</dt>
<dd>元素框从文档流完全删除，并相对于其包含块定位。包含块可能是文档中的另一个元素或者是初始包含块。元素原先在正常文档流中所占的空间会关闭，就好像元素原来不存在一样。元素定位后生成一个块级框，而不论原来它在正常流中生成何种类型的框。</dd>

<dt>fixed</dt>
<dd>元素框的表现类似于将 position 设置为 absolute，不过其包含块是视窗本身。</dd>
</dl>

<p class="tip"><span>提示：</span>相对定位实际上被看作普通流定位模型的一部分，因为元素的位置相对于它在普通流中的位置。</p>
</div>


<div class="example">
<h2>实例</h2>
<dl>
<dt><a target="_blank" href="/tiy/t.asp?f=csse_position_relative">定位：相对定位</a></dt>
<dd>本例演示如何相对于一个元素的正常位置来对其定位。</dd>

<dt><a target="_blank" href="/tiy/t.asp?f=csse_position_absolute">定位：绝对定位</a></dt>
<dd>本例演示如何使用绝对值来对元素进行定位。</dd>

<dt><a target="_blank" href="/tiy/t.asp?f=csse_position_fixed">定位：固定定位</a></dt>
<dd>本例演示如何相对于浏览器窗口来对元素进行定位。</dd>

<dt><a target="_blank" href="/tiy/t.asp?f=csse_position_top">使用固定值设置图像的上边缘</a></dt>
<dd>本例演示如何使用固定值设置图像的上边缘。</dd>

<dt><a target="_blank" href="/tiy/t.asp?f=csse_position_top_percent">使用百分比设置图像的上边缘</a></dt>
<dd>本例演示如何使用百分比值设置图像的上边缘。</dd>

<dt><a target="_blank" href="/tiy/t.asp?f=csse_position_bottom">使用像素值设置图像的底部边缘</a></dt>
<dd>本例演示如何使用像素值设置图像的底部边缘。</dd>

<dt><a target="_blank" href="/tiy/t.asp?f=csse_position_bottom_percent">使用百分比设置图像的底部边缘</a></dt>
<dd>本例演示如何使用百分比值设置图像的底部边缘。</dd>

<dt><a target="_blank" href="/tiy/t.asp?f=csse_position_left">使用固定值设置图像的左边缘</a></dt>
<dd>本例演示如何使用固定值设置图像的左边缘。</dd>

<dt><a target="_blank" href="/tiy/t.asp?f=csse_position_left_percent">使用百分比设置图像的左边缘</a></dt>
<dd>本例演示如何使用百分比值设置图像的左边缘。</dd>

<dt><a target="_blank" href="/tiy/t.asp?f=csse_position_right">使用固定值设置图像的右边缘</a></dt>
<dd>本例演示如何使用固定值设置图像的右边缘。</dd>

<dt><a target="_blank" href="/tiy/t.asp?f=csse_position_right_percent">使用百分比设置图像的右边缘</a></dt>
<dd>本例演示如何使用百分比值设置图像的右边缘。</dd>

<dt><a target="_blank" href="/tiy/t.asp?f=csse_overflow">如何使用滚动条来显示元素内溢出的内容</a></dt>
<dd>本例演示当元素内容太大而超出规定区域时，如何设置溢出属性来规定相应的动作。</dd>

<dt><a target="_blank" href="/tiy/t.asp?f=csse_pos_overflow_hidden">如何隐藏溢出元素中溢出的内容</a></dt>
<dd>本例演示在元素中的内容太大以至于无法适应指定的区域时，如何设置 overflow 属性来隐藏其内容。</dd>

<dt><a target="_blank" href="/tiy/t.asp?f=csse_pos_overflow_auto">如何设置浏览器来自动地处理溢出</a></dt>
<dd>本例演示如何设置浏览器来自动地处理溢出。</dd>

<dt><a target="_blank" href="/tiy/t.asp?f=csse_clip">设置元素的形状</a></dt>
<dd>本例演示如何设置元素的形状。此元素被剪裁到这个形状内，并显示出来。</dd>

<dt><a target="_blank" href="/tiy/t.asp?f=csse_vertical-align">垂直排列图象</a></dt>
<dd>本例演示如何在文本中垂直排列图象。</dd>

<dt><a target="_blank" href="/tiy/t.asp?f=csse_zindex2">Z-index</a></dt>
<dd>Z-index可被用于将在一个元素放置于另一元素之后。</dd>

<dt><a target="_blank" href="/tiy/t.asp?f=csse_zindex1">Z-index</a></dt>
<dd>上面的例子中的元素已经更改了Z-index。</dd>
</dl>
</div>


<div>
<h2>CSS 定位属性</h2>

<p>CSS 定位属性允许你对元素进行定位。</p>

<table class="dataintable">
  <tbody><tr>
    <th>属性</th>
    <th>描述</th>
  </tr>
  <tr>
    <td><a href="/cssref/pr_class_position.asp">position</a></td>
    <td>把元素放置到一个静态的、相对的、绝对的、或固定的位置中。</td>
  </tr>
  <tr>
    <td><a href="/cssref/pr_pos_top.asp">top</a></td>
    <td>定义了一个定位元素的上外边距边界与其包含块上边界之间的偏移。</td>
  </tr>
  <tr>
    <td><a href="/cssref/pr_pos_right.asp">right</a></td>
    <td>定义了定位元素右外边距边界与其包含块右边界之间的偏移。</td>
  </tr>
  <tr>
    <td><a href="/cssref/pr_pos_bottom.asp">bottom</a></td>
    <td>定义了定位元素下外边距边界与其包含块下边界之间的偏移。</td>
  </tr>
  <tr>
    <td><a href="/cssref/pr_pos_left.asp">left</a></td>
    <td>定义了定位元素左外边距边界与其包含块左边界之间的偏移。</td>
  </tr>
  <tr>
    <td><a href="/cssref/pr_pos_overflow.asp">overflow</a></td>
    <td>设置当元素的内容溢出其区域时发生的事情。</td>
  </tr>
  <tr>
    <td><a href="/cssref/pr_pos_clip.asp">clip</a></td>
    <td>设置元素的形状。元素被剪入这个形状之中，然后显示出来。</td>
  </tr>
  <tr>
    <td><a href="/cssref/pr_pos_vertical-align.asp">vertical-align</a></td>
    <td>设置元素的垂直对齐方式。</td>
  </tr>
  <tr>
    <td><a href="/cssref/pr_pos_z-index.asp">z-index</a></td>
    <td>设置元素的堆叠顺序。</td>
  </tr>
</tbody></table>
</div>


<div id="bpn">
<ul class="prenext">
<li class="pre"><a href="/css/css_margin_collapsing.asp" title="CSS 外边距合并">CSS 外边距合并</a></li>
<li class="next"><a href="/css/css_positioning_relative.asp" title="CSS 相对定位">CSS 相对定位</a></li>
</ul>
</div>


<div id="ad_footer">
<a id="ad_footer_link" href="https://gio.ren/w/JoODXE9Y" title="VUE 进阶教程" target="_blank">VUE 进阶教程</a>
</div>

</div>

