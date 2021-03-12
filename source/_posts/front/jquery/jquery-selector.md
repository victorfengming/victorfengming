---
title: 'jQuery中的选择器'
cover: "/img/lynk/99.jpg"
date:       2019-08-31
tags:
	- JavaScript
	- web
	- basis
	- jQuery
---













### jq选择器大全

<table class="dataintable">
<tbody><tr>
<th>选择器</th>
<th>实例</th>
<th>选取</th>
</tr>

<tr>
<td><a href="https://www.w3school.com.cn/jquery/selector_all.asp" title="jQuery * 选择器">*</a></td>
<td>$("*")</td>
<td>所有元素</td>
</tr>

<tr>
<td><a href="https://www.w3school.com.cn/jquery/selector_id.asp" title="jQuery # 选择器">#<i>id</i></a></td>
<td>$("#lastname")</td>
<td>id="lastname" 的元素</td>
</tr>

<tr>
<td><a href="https://www.w3school.com.cn/jquery/selector_class.asp" title="jQuery . 选择器">.<i>class</i></a></td>
<td>$(".intro")</td>
<td>所有 class="intro" 的元素</td>
</tr>

<tr>
<td><a href="https://www.w3school.com.cn/jquery/selector_element.asp" title="jQuery element 选择器"><i>element</i></a></td>
<td>$("p")</td>
<td>所有 &lt;p&gt; 元素</td>
</tr>

<tr>
<td>.<i>class</i>.<i>class</i></td>
<td>$(".intro.demo")</td>
<td>所有 class="intro" 且 class="demo" 的元素</td>
</tr>

<tr>
<td style="background-color:#fff;">&nbsp;</td>
<td style="background-color:#fff;">&nbsp;</td>
<td style="background-color:#fff;">&nbsp;</td>
</tr>

<tr>
<td><a href="https://www.w3school.com.cn/jquery/selector_first.asp" title="jQuery :first 选择器">:first</a></td>
<td>$("p:first")</td>
<td>第一个 &lt;p&gt; 元素</td>
</tr>

<tr>
<td><a href="https://www.w3school.com.cn/jquery/selector_last.asp" title="jQuery :last 选择器">:last</a></td>
<td>$("p:last")</td>
<td>最后一个 &lt;p&gt; 元素</td>
</tr>

<tr>
<td><a href="https://www.w3school.com.cn/jquery/selector_even.asp" title="jQuery :even 选择器">:even</a></td>
<td>$("tr:even")</td>
<td>所有偶数 &lt;tr&gt; 元素</td>
</tr>

<tr>
<td><a href="https://www.w3school.com.cn/jquery/selector_odd.asp" title="jQuery :odd 选择器">:odd</a></td>
<td>$("tr:odd")</td>
<td>所有奇数 &lt;tr&gt; 元素</td>
</tr>

<tr>
<td style="background-color:#fff;">&nbsp;</td>
<td style="background-color:#fff;">&nbsp;</td>
<td style="background-color:#fff;">&nbsp;</td>
</tr>

<tr>
<td><a href="https://www.w3school.com.cn/jquery/selector_eq.asp" title="jQuery :eq() 选择器">:eq(<i>index</i>)</a></td>
<td>$("ul li:eq(3)")</td>
<td>列表中的第四个元素（index 从 0 开始）</td>
</tr>

<tr>
<td><a href="https://www.w3school.com.cn/jquery/selector_gt.asp" title="jQuery :gt 选择器">:gt(<i>no</i>)</a></td>
<td>$("ul li:gt(3)")</td>
<td>列出 index 大于 3 的元素</td>
</tr>

<tr>
<td><a href="https://www.w3school.com.cn/jquery/selector_lt.asp" title="jQuery :lt 选择器">:lt(<i>no</i>)</a></td>
<td>$("ul li:lt(3)")</td>
<td>列出 index 小于 3 的元素</td>
</tr>

<tr>
<td>:not(<i>selector</i>)</td>
<td>$("input:not(:empty)")</td>
<td>所有不为空的 input 元素</td>
</tr>

<tr>
<td style="background-color:#fff;">&nbsp;</td>
<td style="background-color:#fff;">&nbsp;</td>
<td style="background-color:#fff;">&nbsp;</td>
</tr>

<tr>
<td><a href="https://www.w3school.com.cn/jquery/selector_header.asp" title="jQuery :header 选择器">:header</a></td>
<td>$(":header")</td>
<td>所有标题元素 &lt;h1&gt; - &lt;h6&gt;</td>
</tr>

<tr>
<td><a href="https://www.w3school.com.cn/jquery/selector_animated.asp" title="jQuery :animated 选择器">:animated</a></td>
<td>&nbsp;</td>
<td>所有动画元素</td>
</tr>

<tr>
<td style="background-color:#fff;">&nbsp;</td>
<td style="background-color:#fff;">&nbsp;</td>
<td style="background-color:#fff;">&nbsp;</td>
</tr>

<tr>
<td><a href="https://www.w3school.com.cn/jquery/selector_contains.asp" title="jQuery :contains 选择器">:contains(<i>text</i>)</a></td>
<td>$(":contains('W3School')")</td>
<td>包含指定字符串的所有元素</td>
</tr>

<tr>
<td><a href="https://www.w3school.com.cn/jquery/selector_empty.asp" title="jQuery :empty 选择器">:empty</a></td>
<td>$(":empty")</td>
<td>无子（元素）节点的所有元素</td>
</tr>

<tr>
<td>:hidden</td>
<td>$("p:hidden")</td>
<td>所有隐藏的 &lt;p&gt; 元素</td>
</tr>

<tr>
<td><a href="https://www.w3school.com.cn/jquery/selector_visible.asp" title="jQuery :visible 选择器">:visible</a></td>
<td>$("table:visible")</td>
<td>所有可见的表格</td>
</tr>

<tr>
<td style="background-color:#fff;">&nbsp;</td>
<td style="background-color:#fff;">&nbsp;</td>
<td style="background-color:#fff;">&nbsp;</td>
</tr>

<tr>
<td>s1,s2,s3</td>
<td>$("th,td,.intro")</td>
<td>所有带有匹配选择的元素</td>
</tr>

<tr>
<td style="background-color:#fff;">&nbsp;</td>
<td style="background-color:#fff;">&nbsp;</td>
<td style="background-color:#fff;">&nbsp;</td>
</tr>

<tr>
<td><a href="https://www.w3school.com.cn/jquery/selector_attribute.asp" title="jQuery [attribute] 选择器">[<i>attribute</i>]</a></td>
<td>$("[href]")</td>
<td>所有带有 href 属性的元素</td>
</tr>

<tr>
<td><a href="https://www.w3school.com.cn/jquery/selector_attribute_equal_value.asp" title="jQuery [attribute=value] 选择器">[<i>attribute</i>=<i>value</i>]</a></td>
<td>$("[href='#']")</td>
<td>所有 href 属性的值等于 "#" 的元素</td>
</tr>

<tr>
<td><a href="https://www.w3school.com.cn/jquery/selector_attribute_notequal_value.asp" title="jQuery [attribute!=value] 选择器">[<i>attribute</i>!=<i>value</i>]</a></td>
<td>$("[href!='#']")</td>
<td>所有 href 属性的值不等于 "#" 的元素</td>
</tr>

<tr>
<td><a href="https://www.w3school.com.cn/jquery/selector_attribute_end_value.asp" title="jQuery [attribute$=value] 选择器">[<i>attribute</i>$=<i>value</i>]</a></td>
<td>$("[href$='.jpg']")</td>
<td>所有 href 属性的值包含以 ".jpg" 结尾的元素</td>
</tr>

<tr>
<td style="background-color:#fff;">&nbsp;</td>
<td style="background-color:#fff;">&nbsp;</td>
<td style="background-color:#fff;">&nbsp;</td>
</tr>

<tr>
<td><a href="https://www.w3school.com.cn/jquery/selector_input.asp" title="jQuery :input 选择器">:input</a></td>
<td>$(":input")</td>
<td>所有 &lt;input&gt; 元素</td>
</tr>

<tr>
<td><a href="https://www.w3school.com.cn/jquery/selector_input_text.asp" title="jQuery :text 选择器">:text</a></td>
<td>$(":text")</td>
<td>所有 type="text" 的 &lt;input&gt; 元素</td>
</tr>

<tr>
<td><a href="https://www.w3school.com.cn/jquery/selector_input_password.asp" title="jQuery :password 选择器">:password</a></td>
<td>$(":password")</td>
<td>所有 type="password" 的 &lt;input&gt; 元素</td>
</tr>

<tr>
<td><a href="https://www.w3school.com.cn/jquery/selector_input_radio.asp" title="jQuery :radio 选择器">:radio</a></td>
<td>$(":radio")</td>
<td>所有 type="radio" 的 &lt;input&gt; 元素</td>
</tr>

<tr>
<td><a href="https://www.w3school.com.cn/jquery/selector_input_checkbox.asp" title="jQuery :checkbox 选择器">:checkbox</a></td>
<td>$(":checkbox")</td>
<td>所有 type="checkbox" 的 &lt;input&gt; 元素</td>
</tr>

<tr>
<td><a href="https://www.w3school.com.cn/jquery/selector_input_submit.asp" title="jQuery :submit 选择器">:submit</a></td>
<td>$(":submit")</td>
<td>所有 type="submit" 的 &lt;input&gt; 元素</td>
</tr>

<tr>
<td><a href="https://www.w3school.com.cn/jquery/selector_input_reset.asp" title="jQuery :reset 选择器">:reset</a></td>
<td>$(":reset")</td>
<td>所有 type="reset" 的 &lt;input&gt; 元素</td>
</tr>

<tr>
<td><a href="https://www.w3school.com.cn/jquery/selector_input_button.asp" title="jQuery :button 选择器">:button</a></td>
<td>$(":button")</td>
<td>所有 type="button" 的 &lt;input&gt; 元素</td>
</tr>

<tr>
<td><a href="https://www.w3school.com.cn/jquery/selector_input_image.asp" title="jQuery :image 选择器">:image</a></td>
<td>$(":image")</td>
<td>所有 type="image" 的 &lt;input&gt; 元素</td>
</tr>

<tr>
<td><a href="https://www.w3school.com.cn/jquery/selector_input_file.asp" title="jQuery :file 选择器">:file</a></td>
<td>$(":file")</td>
<td>所有 type="file" 的 &lt;input&gt; 元素</td>
</tr>

<tr>
<td style="background-color:#fff;">&nbsp;</td>
<td style="background-color:#fff;">&nbsp;</td>
<td style="background-color:#fff;">&nbsp;</td>
</tr>

<tr>
<td><a href="https://www.w3school.com.cn/jquery/selector_input_enabled.asp" title="jQuery :enabled 选择器">:enabled</a></td>
<td>$(":enabled")</td>
<td>所有激活的 input 元素</td>
</tr>

<tr>
<td><a href="https://www.w3school.com.cn/jquery/selector_input_disabled.asp" title="jQuery :disabled 选择器">:disabled</a></td>
<td>$(":disabled")</td>
<td>所有禁用的 input 元素</td>
</tr>

<tr>
<td><a href="https://www.w3school.com.cn/jquery/selector_input_selected.asp" title="jQuery :selected 选择器">:selected</a></td>
<td>$(":selected")</td>
<td>所有被选取的 input 元素</td>
</tr>

<tr>
<td><a href="https://www.w3school.com.cn/jquery/selector_input_checked.asp" title="jQuery :checked 选择器">:checked</a></td>
<td>$(":checked")</td>
<td>所有被选中的 input 元素</td>
</tr>
</tbody></table>