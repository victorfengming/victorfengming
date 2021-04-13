---
title: "Python3和Python2中int和long区别"
cover: "/img/lynk/45.jpg"
date:       2019-11-28
tags:
	- Python
	- background
	- interview
---




### LONG长整型
python2有非浮点数准备的int和long类型。

int类型最大值不能超过sys.maxint，而且这个最大值是平台相关的。

可以通过在数字的末尾附上一个Ｌ来定义长整型，显然，它比int类型表示的数字范围更大。

在python3里，只有一种整数类型int,大多数情况下，和python２中的长整型类似。


<table class="table table-hover table-striped" style="border-collapse:collapse;border-spacing:0px;color:rgb(62,63,58);font-family:Roboto, 'Helvetica Neue', Helvetica, Arial, sans-serif;font-size:14px;"><thead><tr><th style="text-align:left;line-height:1.42857;vertical-align:bottom;border-top:0px;border-bottom:2px solid rgb(223,215,202);">
python2</th>
<th style="text-align:left;line-height:1.42857;vertical-align:bottom;border-top:0px;border-bottom:2px solid rgb(223,215,202);">
python3</th>
<th style="text-align:left;line-height:1.42857;vertical-align:bottom;border-top:0px;border-bottom:2px solid rgb(223,215,202);">
备注</th>
</tr></thead><tbody><tr><td style="line-height:1.42857;vertical-align:top;border-top:1px solid rgb(223,215,202);">
x = 1000000000000L</td>
<td style="line-height:1.42857;vertical-align:top;border-top:1px solid rgb(223,215,202);">
x = 1000000000000</td>
<td style="line-height:1.42857;vertical-align:top;border-top:1px solid rgb(223,215,202);">
python2中的十进制长整型在python3中被替换为十进制普通整数</td>
</tr><tr><td style="line-height:1.42857;vertical-align:top;border-top:1px solid rgb(223,215,202);">
x = 0xFFFFFFFFFFFFL</td>
<td style="line-height:1.42857;vertical-align:top;border-top:1px solid rgb(223,215,202);">
x = 0xFFFFFFFFFFFF</td>
<td style="line-height:1.42857;vertical-align:top;border-top:1px solid rgb(223,215,202);">
python2里的十六进制长整型在python3里被替换为十六进制的普通整数</td>
</tr><tr><td style="line-height:1.42857;vertical-align:top;border-top:1px solid rgb(223,215,202);">
long(x)</td>
<td style="line-height:1.42857;vertical-align:top;border-top:1px solid rgb(223,215,202);">
int(x)</td>
<td style="line-height:1.42857;vertical-align:top;border-top:1px solid rgb(223,215,202);">
python3没有long()</td>
</tr><tr><td style="line-height:1.42857;vertical-align:top;border-top:1px solid rgb(223,215,202);">
type(x) is long</td>
<td style="line-height:1.42857;vertical-align:top;border-top:1px solid rgb(223,215,202);">
type(x) is int</td>
<td style="line-height:1.42857;vertical-align:top;border-top:1px solid rgb(223,215,202);">
python3用int判断是否为整型</td>
</tr><tr><td style="line-height:1.42857;vertical-align:top;border-top:1px solid rgb(223,215,202);">
isinstance(x, long)</td>
<td style="line-height:1.42857;vertical-align:top;border-top:1px solid rgb(223,215,202);">
isinstance(x, int)</td>
<td style="line-height:1.42857;vertical-align:top;border-top:1px solid rgb(223,215,202);">
int检查整数类型</td>
</tr></tbody></table>