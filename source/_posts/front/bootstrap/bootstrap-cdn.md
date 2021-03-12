---
title: "快速部署Bootstrap环境"
cover: "/img/lynk/61.jpg"
date:       2019-09-19
tags:
	- web
	- basis
	- Bootstrap
---


### 快速部署
使用 Bootstrap CDN嵌入4行代码就能完成导入！ 

### 步骤一:1行 CSS
复制下面的 <link> 样式表粘贴到网页 <head> 里面，并放在其它CSS文件之前.
```html
<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
```
### 步骤二:3行 JS
全局组件运行在 jQuery 组件上，其中包括 Popper.js, 以及系统内置 JavaScript 插件. 建议将 `<script>` 的结束放在页面的 `</body>` 之前以符合新移动WEB规范，并遵循下面代码的先后顺序。

您可以引用 jQuery 精简版,兼容完整版，并无二异。

```html
<script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>
```
这里列出了需要JQuery、Bootstrap.js、Popper.js组件清单，如果你不熟悉组件可以继续查看本文档的其它部份的示例源码。