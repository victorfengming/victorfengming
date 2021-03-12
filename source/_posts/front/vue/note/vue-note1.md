---
title: "Vue.js笔记01"
cover: "/img/lynk/36.jpg"
date:       2020-01-15
subtitle: "初识Vue.js"
tags:
	- JavaScript
	- web
	- vue
---

# 一. 邂逅Vuejs
## 1.1 认识Vuejs
-[ ] 为什么学习Vue
-[ ] Vue读音
-[x] Vue的渐进式
-[ ] Vue特点
## 1.2 安装Vuejs
-[x] CDN引入
-[x] 下载引入
-[x] npm安装
## 1.3 Vue的初体验
-[x] Hello Vuejs
    - Mustache语法-> 体验Vue的响应式
-[x] Vue 列表展示
    - v-for
    - 后面给数组追加元素的时候,新的元素也可以中渲染出来
-[x] Vue 计数器小案例
    - 事件监听:click->methods
## 1.4 Vue中的MVVM
## 1.5 创建Vue时,options可以放那些东西
-[x] el:
-[x] data:
-[x] methods:
-[x] 生命周期函数
# 二. 插值语法
-[x] Mustache语法
-[ ] v-once
-[x] v-html
-[ ] v-text
-[ ] v-pre:{ {} }
-[ ] v-cloak:斗篷
# 三. v-bind
## 3.1 v-bind绑定基本属性
-[x] v-bind:sr
-[x] :href
## 3.2 v-bind动态绑定class
-[x] 对象语法: 作业:class='{类名:boolean}'
-[x] 数组语法
# 四. 计算属性
## 案例一:firstName+lastName

页面

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">

    <script src="https://cdn.jsdelivr.net/npm/vue"></script>

    <title>Title</title>

</head>
<body>
<!--作业需求,:点击我们列表中的哪一项,那么该项的文字变成红色-->
<!--最大的div-->
<div id="app">
    <h3>{{firstName}}{{lastName}}</h3>
    <h3>{{firstName+lastName}}</h3>
<!--    这个不用加小括号-->
    <h3>{{fullName}}</h3>
    <h3>{{getFullName()}}</h3>
</div>

    <script src="./index.js"></script>
</body>
</html>
```

js


```js
const app = new Vue({
    el: '#app',
    data: {
        firstName: "victor",
        lastName: "fengming",
    },
    computed: {
    //    这里一般不加动词的函数
        fullName: function () {
            return this.firstName + this.lastName
        },

    },
    methods: {
        getFullName: function () {
            return this.firstName + this.lastName
        },
    }
});

```
## 案例二:books -> price

页面
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">

    <script src="https://cdn.jsdelivr.net/npm/vue"></script>

    <title>Title</title>

</head>
<body>
<!--最大的div-->
<div id="app">
    <h3>总价格:{{totalPrice}}</h3>
</div>
<script src="./index.js"></script>
</body>
</html>
```

js

```js
const app = new Vue({
    el: '#app',
    data: {
        books: [
            {id: 110, name: "Unix编程艺术", price: 24},
            {id: 111, name: "代码大全", price: 25},
            {id: 112, name: "深入理解计算机", price: 675},
            {id: 113, name: "现代操作系统", price: 565},
        ],
    },
    computed: {
        // 高级函数
        // filter/map/reduce,
        totalPrice: function () {
            // // 普通的low逼写法
            // let result = 0;
            // for (let i = 0; i < this.books.length; i++) {
            //     result += this.books[i].price
            // }
            // return result;
            // // ES6写法1
            // for (let i in this.books) {
            //     books[i]
            // }
            // // ES6写法2
            // for (let book of this.books) {
            //     book
            // }
            // return this.books.reduce();
        },
        //    计算属性和method在执行的时候有很大区别,
        //    这个计算属性不会多次执行
        //    他是有缓存的,
    },
    methods: {
        getmessage: function () {
            return this.message
        },
    }
});

```
[ori_link](https://www.bilibili.com/video/av89760569?p=23)

# var和let
JavaScript设计的缺陷,在设计之初没有想过现在发展的这么完善

let具有块级作用域,而var没有

ES5中没有闭包,ES6中加入了闭包

没有闭包就会导致在for循环的时候i被不必要的更新
# const的使用
常量尽量用const,优先使用const,只有需要改变的才使用let