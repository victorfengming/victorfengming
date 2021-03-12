---
title: 'jQuery中的事件'
cover: "/img/lynk/62.jpg"
date:       2019-08-31
tags:
	- JavaScript
	- web
	- basis
	- jQuery
---













### jQuery 事件方法
事件方法会触发匹配元素的事件，或将函数绑定到所有匹配元素的某个事件。

### 触发实例：

`$("button#demo").click()`  
上面的例子将触发 id="demo" 的 button 元素的 click 事件。

### 绑定实例：

`$("button#demo").click(function(){$("img").hide()})`  
上面的例子会在点击 id="demo" 的按钮时隐藏所有图像。

<table class="dataintable">
<tbody><tr>
<th style="width:35%;">方法</th>
<th>描述</th>
</tr>

<tr>
<td><a href="https://www.w3school.com.cn/jquery/event_bind.asp" title="jQuery 事件 - bind() 方法">bind()</a></td>
<td>向匹配元素附加一个或更多事件处理器</td>
</tr>

<tr>
<td><a href="https://www.w3school.com.cn/jquery/event_blur.asp" title="jQuery 事件 - blur() 方法">blur()</a></td>
<td>触发、或将函数绑定到指定元素的 blur 事件</td>
</tr>


<tr>
<td><a href="https://www.w3school.com.cn/jquery/event_change.asp" title="jQuery 事件 - change() 方法">change()</a></td>
<td>触发、或将函数绑定到指定元素的 change 事件</td>
</tr>

<tr>
<td><a href="https://www.w3school.com.cn/jquery/event_click.asp" title="jQuery 事件 - click() 方法">click()</a></td>
<td>触发、或将函数绑定到指定元素的 click 事件</td>
</tr>

<tr>
<td><a href="https://www.w3school.com.cn/jquery/event_dblclick.asp" title="jQuery 事件 - dblclick() 方法">dblclick()</a></td>
<td>触发、或将函数绑定到指定元素的 double click 事件</td>
</tr>

<tr>
<td><a href="https://www.w3school.com.cn/jquery/event_delegate.asp" title="jQuery 事件 - delegate() 方法">delegate()</a></td>
<td>向匹配元素的当前或未来的子元素附加一个或多个事件处理器</td>
</tr>

<tr>
<td><a href="https://www.w3school.com.cn/jquery/event_die.asp" title="jQuery 事件 - die() 方法">die()</a></td>
<td>移除所有通过 live() 函数添加的事件处理程序。</td>
</tr>

<tr>
<td><a href="https://www.w3school.com.cn/jquery/event_error.asp" title="jQuery 事件 - error() 方法">error()</a></td>
<td>触发、或将函数绑定到指定元素的 error 事件</td>
</tr>

<tr>
<td><a href="https://www.w3school.com.cn/jquery/event_isdefaultprevented.asp" title="jQuery 事件 - isDefaultPrevented() 方法">event.isDefaultPrevented()</a></td>
<td>返回 event 对象上是否调用了 event.preventDefault()。</td>
</tr>

<tr>
<td><a href="https://www.w3school.com.cn/jquery/event_pagex.asp" title="jQuery 事件 - pageX 属性">event.pageX</a></td>
<td>相对于文档左边缘的鼠标位置。</td>
</tr>

<tr>
<td><a href="https://www.w3school.com.cn/jquery/event_pagey.asp" title="jQuery 事件 - pageY 属性">event.pageY</a></td>
<td>相对于文档上边缘的鼠标位置。</td>
</tr>

<tr>
<td><a href="https://www.w3school.com.cn/jquery/event_preventdefault.asp" title="jQuery 事件 - preventDefault() 方法">event.preventDefault()</a></td>
<td>阻止事件的默认动作。</td>
</tr>

<tr>
<td><a href="https://www.w3school.com.cn/jquery/event_result.asp" title="jQuery 事件 - result 属性">event.result</a></td>
<td>包含由被指定事件触发的事件处理器返回的最后一个值。</td>
</tr>

<tr>
<td><a href="https://www.w3school.com.cn/jquery/event_target.asp" title="jQuery 事件 - target 属性">event.target</a></td>
<td>触发该事件的 DOM 元素。</td>
</tr>

<tr>
<td><a href="https://www.w3school.com.cn/jquery/event_timeStamp.asp" title="jQuery 事件 - timeStamp 属性">event.timeStamp</a></td>
<td>该属性返回从 1970 年 1 月 1 日到事件发生时的毫秒数。</td>
</tr>

<tr>
<td><a href="https://www.w3school.com.cn/jquery/event_type.asp" title="jQuery 事件 - type 属性">event.type</a></td>
<td>描述事件的类型。</td>
</tr>

<tr>
<td><a href="https://www.w3school.com.cn/jquery/event_which.asp" title="jQuery 事件 - which 属性">event.which</a></td>
<td>指示按了哪个键或按钮。</td>
</tr>

<tr>
<td><a href="https://www.w3school.com.cn/jquery/event_focus.asp" title="jQuery 事件 - focus() 方法">focus()</a></td>
<td>触发、或将函数绑定到指定元素的 focus 事件</td>
</tr>

<tr>
<td><a href="https://www.w3school.com.cn/jquery/event_keydown.asp" title="jQuery 事件 - keydown() 方法">keydown()</a></td>
<td>触发、或将函数绑定到指定元素的 key down 事件</td>
</tr>

<tr>
<td><a href="https://www.w3school.com.cn/jquery/event_keypress.asp" title="jQuery 事件 - keypress() 方法">keypress()</a></td>
<td>触发、或将函数绑定到指定元素的 key press 事件</td>
</tr>

<tr>
<td><a href="https://www.w3school.com.cn/jquery/event_keyup.asp" title="jQuery 事件 - keyup() 方法">keyup()</a></td>
<td>触发、或将函数绑定到指定元素的 key up 事件</td>
</tr>

<tr>
<td><a href="https://www.w3school.com.cn/jquery/event_live.asp" title="jQuery 事件 - live() 方法">live()</a></td>
<td>为当前或未来的匹配元素添加一个或多个事件处理器</td>
</tr>

<tr>
<td><a href="https://www.w3school.com.cn/jquery/event_load.asp" title="jQuery 事件 - load() 方法">load()</a></td>
<td>触发、或将函数绑定到指定元素的 load 事件</td>
</tr>

<tr>
<td><a href="https://www.w3school.com.cn/jquery/event_mousedown.asp" title="jQuery 事件 - mousedown() 方法">mousedown()</a></td>
<td>触发、或将函数绑定到指定元素的 mouse down 事件</td>
</tr>

<tr>
<td><a href="https://www.w3school.com.cn/jquery/event_mouseenter.asp" title="jQuery 事件 - mouseenter() 方法">mouseenter()</a></td>
<td>触发、或将函数绑定到指定元素的 mouse enter 事件</td>
</tr>

<tr>
<td><a href="https://www.w3school.com.cn/jquery/event_mouseleave.asp" title="jQuery 事件 - mouseleave() 方法">mouseleave()</a></td>
<td>触发、或将函数绑定到指定元素的 mouse leave 事件</td>
</tr>

<tr>
<td><a href="https://www.w3school.com.cn/jquery/event_mousemove.asp" title="jQuery 事件 - mousemove() 方法">mousemove()</a></td>
<td>触发、或将函数绑定到指定元素的 mouse move 事件</td>
</tr>

<tr>
<td><a href="https://www.w3school.com.cn/jquery/event_mouseout.asp" title="jQuery 事件 - mouseout() 方法">mouseout()</a></td>
<td>触发、或将函数绑定到指定元素的 mouse out 事件</td>
</tr>

<tr>
<td><a href="https://www.w3school.com.cn/jquery/event_mouseover.asp" title="jQuery 事件 - mouseover() 方法">mouseover()</a></td>
<td>触发、或将函数绑定到指定元素的 mouse over 事件</td>
</tr>

<tr>
<td><a href="https://www.w3school.com.cn/jquery/event_mouseup.asp" title="jQuery 事件 - mouseup() 方法">mouseup()</a></td>
<td>触发、或将函数绑定到指定元素的 mouse up 事件</td>
</tr>

<tr>
<td><a href="https://www.w3school.com.cn/jquery/event_one.asp" title="jQuery 事件 - one() 方法">one()</a></td>
<td>向匹配元素添加事件处理器。每个元素只能触发一次该处理器。</td>
</tr>

<tr>
<td><a href="https://www.w3school.com.cn/jquery/event_ready.asp" title="jQuery 事件 - ready() 方法">ready()</a></td>
<td>文档就绪事件（当 HTML 文档就绪可用时）</td>
</tr>

<tr>
<td><a href="https://www.w3school.com.cn/jquery/event_resize.asp" title="jQuery 事件 - resize() 方法">resize()</a></td>
<td>触发、或将函数绑定到指定元素的 resize 事件</td>
</tr>

<tr>
<td><a href="https://www.w3school.com.cn/jquery/event_scroll.asp" title="jQuery 事件 - scroll() 方法">scroll()</a></td>
<td>触发、或将函数绑定到指定元素的 scroll 事件</td>
</tr>

<tr>
<td><a href="https://www.w3school.com.cn/jquery/event_select.asp" title="jQuery 事件 - select() 方法">select()</a></td>
<td>触发、或将函数绑定到指定元素的 select 事件</td>
</tr>

<tr>
<td><a href="https://www.w3school.com.cn/jquery/event_submit.asp" title="jQuery 事件 - submit() 方法">submit()</a></td>
<td>触发、或将函数绑定到指定元素的 submit 事件</td>
</tr>

<tr>
<td><a href="https://www.w3school.com.cn/jquery/event_toggle.asp" title="jQuery 事件 - toggle() 方法">toggle()</a></td>
<td>绑定两个或多个事件处理器函数，当发生轮流的 click 事件时执行。</td>
</tr>

<tr>
<td><a href="https://www.w3school.com.cn/jquery/event_trigger.asp" title="jQuery 事件 - trigger() 方法">trigger()</a></td>
<td>所有匹配元素的指定事件</td>
</tr>

<tr>
<td><a href="https://www.w3school.com.cn/jquery/event_triggerhandler.asp" title="jQuery 事件 - triggerHandler() 方法">triggerHandler()</a></td>
<td>第一个被匹配元素的指定事件</td>
</tr>

<tr>
<td><a href="https://www.w3school.com.cn/jquery/event_unbind.asp" title="jQuery 事件 - unbind() 方法">unbind()</a></td>
<td>从匹配元素移除一个被添加的事件处理器</td>
</tr>

<tr>
<td><a href="https://www.w3school.com.cn/jquery/event_undelegate.asp" title="jQuery 事件 - undelegate() 方法">undelegate()</a></td>
<td>从匹配元素移除一个被添加的事件处理器，现在或将来</td>
</tr>

<tr>
<td><a href="https://www.w3school.com.cn/jquery/event_unload.asp" title="jQuery 事件 - unload() 方法">unload()</a></td>
<td>触发、或将函数绑定到指定元素的 unload 事件</td>
</tr>
</tbody></table>