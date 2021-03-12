---
title: 'Emmet的html语法'
date:       2019-09-11
tags:
	- web
	- html
	- solution
---

**所有操作按下“tab”键即可瞬间完成**

### 元素
1.在编辑器中输入元素名称，即可自动补全生成 HTML 标签，即使不是标准的 HTML 标签。   
2.输入：! 或者 html:5 或者 html:4s 或者 html:4t 将自动补全html基本结构
### 嵌套操作
1.使用“>”生成子元素
```
// 输入
div>ul>li

// 按下TAB键
<div>
    <ul>
        <li></li>
    </ul>
</div>
```
2.使用“+”生成兄弟元素
```
// 输入
div+p+bq

// 按下TAB键
<div></div>
<p></p>
<blockquote></blockquote>
```
3.使用“^”生成父元素
```
// 输入
div+div>p>span+em^bq

// 按下TAB键
<div></div>
<div>
    <p><span></span><em></em></p>
    <blockquote></blockquote>
</div>
```
4.使用“*”生成多个相同元素
```
// 输入
div>ul>li*5

// 按下TAB键
<div>
    <ul>
        <li></li>
        <li></li>
        <li></li>
        <li></li>
        <li></li>
    </ul>
</div>
```
5.使用“()”将元素分组
```
// 输入
// "+" 后面的元素与括号中的第一个元素属于兄弟关系
div>(header>ul>li*2)+footer>p

//按下TAB键
<div>
    <header>
        <ul>
            <li></li>
            <li></li>
        </ul>
    </header>
    <footer>
        <p></p>
    </footer>
</div>
```

### 属性操作
1.id与class：元素与 id 属性值之间用 “#” 分隔，与 class 属性值之间用 “.” 分隔
```
// 输入
div#header+div.page+div#footer.class1.class2.class3

// 按下TAB键
<div id="header"></div>
<div class="page"></div>
<div id="footer" class="class1 class2 class3"></div>
```
2.使用“[]”标记其他属性
```
// 输入
td[title='hello' colspan=3]

// 按下TAB键
<td title="hello" colspan="3"></td>
```
3.用“$”符号实现1到n的自动编号（“*”实现多个元素）
```
// 输入
li.item$*3

// 按下TAB键
<li class="item1"></li>
<li class="item2"></li>
<li class="item3"></li>
```
可在 “$” 后添加 “@n” 修改编号的起始值为n。
```
// 输入
li.item$@3*3

// 按下TAB键
<li class="item3"></li>
<li class="item4"></li>
<li class="item5"></li>
```
可在 “$” 后添加 “@-” 修改编号的方向。
```
// 输入
li.item$@-3*3

// 按下TAB键
<li class="item5"></li>
<li class="item4"></li>
<li class="item3"></li>
```
4.用“{}”添加文本内容
```
// 输入
a[href=me.htm]{click me}

// 按下TAB键
<a href="me.htm">click me</a>
```
更多简写方法不断更新中，关注我即可获取最新消息哦～