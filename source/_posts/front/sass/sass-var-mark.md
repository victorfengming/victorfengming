---
title: 'Sass - 变量($)'
cover: "/img/lynk/21.jpg"
date:       2019-09-23
tags:
	- web
	- html
	- solution
	- sass
---

<script>
window.location.href='https://blog.csdn.net/weixin_44198965/article/details/101110709';
</script>

Sass - 变量($)

基本语法
定义一个 Sass 变量非常简单，变量以美元符号($)开始，赋值像设置 CSS 属性一样：

$new-color: rgb(255,0,0);
1
然后，便可以使用该变量：

div{
  background: $new-color;
}
1
2
3
编译为CSS：

div{
  background: rgb(255,0,0)
}
1
2
3
局部变量
几乎所有语言均存在局部变量与全局变量，当然 Sass 也不例外，同样存在局部变量，请看如下代码：

#main{
    /* 该变量在类中 */
    $new_width: 50px;
    width: $new_width;
}

div{
    /* 尝试访问 => $new_width */
    width: $new_width;
}