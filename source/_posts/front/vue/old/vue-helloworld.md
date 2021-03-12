---
title: "我的第一个Vue程序"
date:       2019-09-18
tags:
	- web
	- vue
	- basis
---

### 废话不多讲,直接就上代码

### index.html
```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <title>VueJS Tutorials</title>
        <link href="styles.css" rel="stylesheet" />
        <script src="https://unpkg.com/vue"></script>
    </head>
    <body>
        <div id="vue-app">
            <h1>{{ greet('afternoon') }}</h1>
            <p>Name: {{ name}}</p>
            <p>Job: {{ job }}</p>
        </div>
    </body>

    <script src="app.js"></script>
</html>
```
### app.js
```JavaScript
new Vue({
    el: '#vue-app',
    data: {
        name: 'Shaun',
        job: 'Ninja'
    },
    methods: {
        greet: function(time){
            return 'Good ' + time + ', ' + this.name;
        }
    }
});

```


### Vue对象中的属性
- el: element 需要获取的元素,一定是html中的跟容器元素  
- data: 用于数据的存储  
- methods: 用于存储各种方法  
- data-binding :给属性绑定对应的值  
- computed: 计算属性,这个性能好,不是全部触发  
    - 操作虚拟dom 比较不同的地方,要是有才触发你这个方法  
    - 只有大量的耗时才使用这个computed属性,比如说搜索  
