---
title: "Vue.js前后端分离2"
date:       2019-12-13
tags:
	- JavaScript
	- web
	- vue
	- django
	- axios
---












### 内容回顾
#### - 过滤器
##### - 局部的过滤器
```js
// 只能在当前组件内部使用
filters:function(val,a,b){
    // 执行过滤处理逻辑,(添油加醋的内容)
    return xxx;
}
```

##### - 全局的过滤器
```js
// 声明+创建 在任何组件中都能使用
Vue.filter("myTime",function() {
    // 添油加醋的处理
    return xxxx;                
})
```


#### - 生命周期-钩子函数

- beforeCreate这个方法不常用  
- create 组件创建完成,
    - 可以发起ajax(XMLHTTPRequest 简称 XHR axios fetch $.ajax())请求
    - 实现数据驱动视图思想
- beforeMount 挂载
- mounted DOM挂载完成    
- beforeUpdate 获取原始的DOM
- updated 后去更新之后的DOM
- beforeDestroy 组件销毁之前
- destroyed 组件销毁之后
- actived 激活当前组件 Vue提供的内置组件`<keep-alive></keep-alive>`
- deactivated 停用当前组件
### vue-router 核心插件
#### 主要作用: 实现单页面应用,为了用户体验,后端资源过多,可能会出现白屏的现象
现在都用前后端分离,甚至现在有些后端里面的前后台管理都分离了
#### 模板引擎:
node.js express web服务器框架 jade html ejs

python django   jinja2衍生出来的

一般后台语言都有一个模板引擎的东东

{ {  } }

{ % % }

### 模板引擎 VS 前后端分离
#### 模板引擎的
好处:减少DOM操作,你一玩dom就不用谢js的dom操作了    
不好处:随着你的项目越来越大,你的项目在后期不易维护

当你的需求频繁改的时候,你还得写一些js代码,这样你就模板语法和js混合着写了  
要是用这种前后端分离的写法,前端专门就搞这个DOM操作,那就厉害了

等咱们讲完前后端分离,就会发现还是前后端分离好用

#### 前后端分离

分工明确

前端只做前端的事情(页面+交互+兼容+class+封装+优化)
- vue+vue+router+axios+element+ui 前端技术栈  
后端只做后端的事情(接口(表的操作+业务逻辑+封装+class+优化))
- restframework框架+django+sqlite+redis 后端技术栈

你写简历的时候可以把这个技术栈列出来

1. xxx在线教育平台

2. xxx后台管理系统


名字 项目周期 技术栈 项目介绍 项目总结

## vue router
### 下载
这里我们直接用CDN的
### 引包

vue-router依赖vue
`vue-router.js`  
`Vue.component('router-link',{})`  
`router-link router-view`

### 如果是模块化机制 
Vue.use(vue-router)
### 创建实例
```js

let Home = {
    /*
        这里就不多些了        
    */        
}

new VueRouter({
    // 5. 配置路由信息
    routes:[
        {
            path:"/",
            redirect:"/home",
        },
        {
            path:"/home",
            name:"/Home",
            component:Home,
        },
    ]                   
})


new Vue({
    //6. 挂载router对象到vue的实例中
    router        
})
```
### 使用路由
```html
<!--
router-link默认被渲染成a标签 to 属性就会被渲染成href了

-->


<div>
    <router-link to="/">首页</router-link>    
    <!--这个router-link就是我们自定义标签,然后我们换了一个名字,叫组件-->
    <router-link :to="/home" @click.native = "">首页</router-link>    
    路由组件的出口    
    <router-view></router-view>    
        
</div>
```

### 动态路由匹配
`/user/1`    `/user/2` 加载的是同一个组件

```js
routes:[
    {
        path:"/",
        redirect:"/home",
    },
    {
        path:"/user/:id",
        name:"/User",
        component:User,
    },
]               
```
```html
<router-link to="{name:'User',params:{xxx:'front'}}">前端</router-link>    
<router-link to="{name:'User',params:{xxx:'ios'}}">IOS</router-link>    
```

复用的组件 ,监听路由的变化
```js
watch:(to,from)=>{
    to 要进入的页面的路由信息对象
    from 从哪个    
}
```

### 编程式导航
```js
this.$router.push({
    name:"Home"
})
```

vue-router 提供的内置的内容

`router-link`

`router-view`

`this.$route` 路由信息对象
 
`this.$router` 路由对象

## 今日内容
### 获取原生的DOM的方式


```html

<div ref = "alex">哈哈哈</div> 
<p ref="a"></p>
<Home ref="b"></Home>
```

```js
this.$refs.alex
```

### DIY脚手架
下一个东西
脚手架不要下最新的

```
npm i webpack@3.12.0 -g
```
cmd
module.exports = xxx
require()
es6module

```js
import * as a from "./main.js"
```

### vue-cli的使用



### webpack
组件化开发vue-cli

webpack 前端中的工具 ,三大主流工具 之 最主流的

grunt gulp webpack

目前webpack已经占据了主流市场
webpack是一个现代JavaScript应用程序的静态模块打包器.当webpack处理应用程序时,它会递归地构建一个依赖关系,其中包含应用程序需要的每个模块,然后将所有这些模块打包成一个或多个bundle

所有的后端都支持模块化

但是我们的前端是不支持模块化的