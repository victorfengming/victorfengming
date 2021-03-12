---
title: 'jQuery手动触发事件-trigger()方法'
date:       2019-09-08
tags:
	- JavaScript
	- web
	- jQuery
---

<div id="maincontent">

<div class="backtoreference">
<p><a href="/jquery/jquery_ref_events.asp" title="jQuery 参考手册 - 事件">jQuery 事件参考手册</a></p>
</div>


<div>
<h3>实例</h3>

<p>触发 input 元素的 select 事件：</p>

<pre>$("button").click(function(){
  $("input").trigger("select");
});
</pre>

<p class="tiy"><a target="_blank" href="/tiy/t.asp?f=jquery_event_trigger">亲自试一试</a></p>
</div>


<div>
<h3>定义和用法</h3>

<p>trigger() 方法触发被选元素的指定事件类型。</p>
</div>


<div>
<h3>触发事件</h3>

<p>规定被选元素要触发的事件。</p>

<h3>语法</h3>

<pre>$(<i>selector</i>).trigger(<i>event</i>,[<i>param1</i>,<i>param2</i>,...])</pre>

<p class="tiy"><a target="_blank" href="/tiy/t.asp?f=jquery_event_trigger">亲自试一试</a></p>

<table class="dataintable">
<tbody><tr>
<th style="width:25%;">参数</th>
<th>描述</th>
</tr>

<tr>
<td><i>event</i></td>
<td>
    <p>必需。规定指定元素要触发的事件。</p>
    <p>可以使自定义事件（使用 bind() 函数来附加），或者任何标准事件。</p>
</td>
</tr>

<tr>
<td>[<i>param1</i>,<i>param2</i>,...]</td>
<td>
    <p>可选。传递到事件处理程序的额外参数。</p>
    <p>额外的参数对自定义事件特别有用。</p>
</td>
</tr>
</tbody></table>
</div>


<div>
<h3>使用 Event 对象来触发事件</h3>

<p>规定使用事件对象的被选元素要触发的事件。</p>

<h3>语法</h3>

<pre>$(<i>selector</i>).trigger(<i>eventObj</i>)</pre>

<p class="tiy"><a target="_blank" href="/tiy/t.asp?f=jquery_event_trigger_object">亲自试一试</a></p>

<table class="dataintable">
<tbody><tr>
<th style="width:25%;">参数</th>
<th>描述</th>
</tr>

<tr>
<td><i>eventObj</i></td>
<td>必需。规定事件发生时运行的函数。</td>
</tr>
</tbody></table>
</div>


<div class="backtoreference">
<p><a href="/jquery/jquery_ref_events.asp" title="jQuery 参考手册 - 事件">jQuery 事件参考手册</a></p>
</div>


</div>