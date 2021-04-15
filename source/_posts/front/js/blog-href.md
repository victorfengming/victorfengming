---
title: '如何在自己博文中自动跳转到其他链接位置'
cover: "/img/lynk/78.jpg"
date:       2019-09-17
tags:
	- JavaScript
	- web
---




有些小伙伴看我的博客中有自动跳转到其他博文的内容,感觉很厉害

甚至有[同学](https://caoyang7.github.io/)感叹到:这也太好了吧!

### 不多BB,直接上代码

```
<script>
window.location.href='https://victorfengming.gitee.io/2019/09/blog-href/';
</script>
```

### 简单解释(不用仔细看)
其实原理很简单,说破了就感觉很low了

首先,在jekyll的模板中,markdown文件中可以嵌入html标签,在最终的页面上会被渲染成为页面中的元素内容

所以,script标签他也不例外,这样我们只需要在文档加载时,直接进行js的跳转动作就行了

这样你直接将我上面的代码粘贴到你的博客的模板中的md文件中,就直接就成了(其中href后面的地址可以根据你自己的地址来进行更改)

这个小功能看似没什么用,但是对于一些喜欢fock其他人博客的同学,这简直就是神奇的工具啊!!!