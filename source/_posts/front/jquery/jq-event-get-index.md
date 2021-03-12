---
title: 'jquery点击事件获取该元素在整个一类元素中的索引值'
date:       2019-09-07
tags:
	- JavaScript
	- web
	- jQuery
---

<div class="htmledit_views" id="content_views">
                                            
<pre style="font-family:'新宋体';font-size:13px;background:#FFFFFF;">有一类div标签，class为pointbox，数量不等，有多个。我需要在点击某一个标签的时候实时获取该标签在这类标签中索引值，以便进行其他操作。</pre>
<pre style="font-family:'新宋体';font-size:13px;background:#FFFFFF;">代码很简单：</pre>
<pre style="font-family:'新宋体';font-size:13px;background:#FFFFFF;">$(<span style="color:#a31515;">".pointbox"</span>).click(<span style="color:#0000FF;">function</span>&nbsp;()&nbsp;{
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 
&nbsp;&nbsp;<span style="color:#0000FF;">var</span>&nbsp;index=$(<span style="color:#a31515;">".pointbox"</span>).index($(<span style="color:#0000FF;">this</span>));
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 
});</pre>
<pre style="font-family:'新宋体';font-size:13px;background:#FFFFFF;">但是比较实用,送你啦,拿去不谢!</pre>
</div>