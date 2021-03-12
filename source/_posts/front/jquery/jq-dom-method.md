---
title: 'jQuery中的元素方法'
date:       2019-09-07
tags:
	- JavaScript
	- web
	- solution
---













### 先送你一个清单
<table class="dataintable">
<tbody><tr>
<th>函数</th>
<th>描述</th>
</tr>

<tr>
<td><a href="/jquery/dom_element_methods_get.asp" title="jQuery DOM 元素方法 - get() 方法">.get()</a></td>
<td>获得由选择器指定的 DOM 元素。</td>
</tr>

<tr>
<td><a href="/jquery/dom_element_methods_index.asp" title="jQuery DOM 元素方法 - index() 方法">.index()</a></td>
<td>返回指定元素相对于其他指定元素的 index 位置。</td>
</tr>

<tr>
<td><a href="/jquery/dom_element_methods_size.asp" title="jQuery DOM 元素方法 - size() 方法">.size()</a></td>
<td>返回被 jQuery 选择器匹配的元素的数量。</td>
</tr>

<tr>
<td><a href="/jquery/dom_element_methods_toarray.asp" title="jQuery DOM 元素方法 - toArray() 方法">.toArray()</a></td>
<td>以数组的形式返回 jQuery 选择器匹配的元素。</td>
</tr>

</tbody></table>


### 举个栗子
元素结构是这样的  
```
<ul>
  <li></li>
  <li></li>
  <li></li>
</ul>
```

如要获取上述html中li的数量:
```
$("ul > li").length;
```
或使用其size()方法:
```
$("ul > li").size();
```