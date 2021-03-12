---
title: "Vue.js的安装"
cover: "/img/lynk/61.jpg"
date:       2019-08-30
tags:
	- JavaScript
	- web
	- vue
	- solution
---

### 咱先说说关于兼容性的问题  
Vue 不支持 IE8 及以下版本，因为 Vue 使用了 IE8 无法模拟的 ECMAScript 5 特性。但它支持[所有兼容 ECMAScript 5 的浏览器。](https://caniuse.com/#feat=es5)

### `<script>`标签直接引入
直接用 `<script>` 引入  
直接下载并用 `<script>` 标签引入，Vue 会被注册为一个全局变量。  

这里小编推荐给新手朋友们两种快速简单的方式  

### 本地文件引入
1. 你可以在vue的官网中找到，或者直接点击下面的链接  

在这里小编给大家提供了两个版本：  
<div style="width: 300px; height: 50px; border-radius: 50px; background-color: #42b983; font-size: 24px;"><a href="https://cn.vuejs.org/js/vue.js"><p style="color:#eef; line-height:50px;text-align: center;">开发版本</p></a></div>
这个版本包含完整的警告和调试模式，适用于开发和学习中使用  
<div style="width: 300px; height: 50px; border-radius: 50px; background-color: #42b983; font-size: 24px;"><a href="https://cn.vuejs.org/js/vue.min.js"><p style="color:#eef; line-height:50px;text-align: center;">生产版本</p></a></div>
这个版本适合用于上线的项目，因为这里做了一些压缩和优化，会为你提升性能  

使用时在页面中复制所有代码，存入到本地的文件中，直接在`<script>`标签中引入文件即可  

### 内容分发网络（CDN）方式引入
2. 使用CDN方式导入

- 对于制作原型或学习，你可以这样使用最新版本：  
`<script src="https://cdn.jsdelivr.net/npm/vue"></script>`

- 对于生产环境，我们推荐链接到一个明确的版本号和构建文件，以避免新版本造成的不可预期的破坏：  
`<script src="https://cdn.jsdelivr.net/npm/vue@2.6.10/dist/vue.js"></script>`  

- 如果你使用原生 ES Modules，这里也有一个兼容 ES Module 的构建文件：  
```
<script type="module">
  import Vue from 'https://cdn.jsdelivr.net/npm/vue@2.6.10/dist/vue.esm.browser.js'
</script>
```

### NPM方式
在用 Vue 构建大型应用时推荐使用 NPM 安装。NPM 能很好地和诸如 [webpack](https://webpack.js.org/) 或 [Browserify](http://browserify.org/) 模块打包器配合使用。同时 Vue 也提供配套工具来开发[单文件组件](https://cn.vuejs.org/v2/guide/single-file-components.html)。
```
# 最新稳定版
$ npm install vue
```

### 最后送你一个小彩蛋-Vue Devtools   
在使用 Vue 时，我们推荐在你的浏览器上安装 [Vue Devtools](https://github.com/vuejs/vue-devtools#vue-devtools)。它允许你在一个更友好的界面中审查和调试 Vue 应用

[vue调试工具vue-devtools安装及使用](https://www.cnblogs.com/yuqing6/p/7440549.html)


<style type="text/css">
    
    
</style>