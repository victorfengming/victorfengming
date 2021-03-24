---
title: "Vue.js+Django 实现前后端分离"
cover: "/img/lynk/97.jpg"
date:       2019-12-11
tags:
	- JavaScript
	- web
	- vue
	- django
	- axios
---












## 准备
### 环境的搭建
- [node.js](https://www.jianshu.com/p/03a76b2e7e00)
- [vue-cli](https://www.jianshu.com/p/06a9f112867d)
- [python](https://victorfengming.gitee.io/blog/python-install-window/)
- [django](https://victorfengming.gitee.io/blog/django-note1/)
### 集成开发环境的搭建
- webstorm
- pycharm
- 安装参考[这里](https://victorfengming.gitee.io/blog/pycharm-install/),激活破解以及设置,可以在我的[github](https://github.com/victorfengming/jetbrains_settings)/[gitee](https://gitee.com/victorfengming/jetbrains_settings)中clone下来    
## 起步

### node.js安装
[官网](https://nodejs.org/zh-cn/)下载exe
傻瓜式下一步即可
### 检查node版本


```
node --version
```
### npm介绍
node的包管理工具,详情可以参考简书:[NPM简介和安装](https://www.jianshu.com/p/1ab15a647e83)

### 检查npm版本


```
npm --version
```
## 入门
### npm换源 - 淘宝源
1.临时使用


```
npm --registry https://registry.npm.taobao.org install express
```


2.持久使用




```
npm config set registry https://registry.npm.taobao.org
// 配置后可通过下面方式来验证是否成功
npm config get registry
// 或npm info express
```



### vue脚手架的安装


```
npm install -g @vue/cli
```

### 安装 @vue/cli-init


```
npm i -g @vue/cli
npm i -g @vue/cli-init
```

## 进阶
### 创建vue项目 
vue初始化基于webpack的my-project项目(项目名不能用大写字母)


```
vue init webpackage project_name
```

#### 下面有一坨选项


```
? Project name my-project
? Project description A Vue.js project
? Author uplyw <xxx@xxx.com>
? Vue build standalone
? Install vue-router? Yes
? Use ESLint to lint your code? No
? Set up unit tests No
? Setup e2e tests with Nightwatch? No
? Should we run `npm install` for you after the project has been created? (recommended) npm
```

[vue init webpack my-project 选项详解](https://blog.csdn.net/AYKMe/article/details/84646571)

### 先运行起来再说


```
npm run dev
```

### 加一个路由
在`router\index.js`中,加上一个


```js
{
  path: '/user',
  name: 'User',
  component: User
},
```

再去`vue_project\src\components`里面创建一个.vue文件,内容如下

```JavaScript
// 这里直接就复制那个Hello的就OK了
```

## 高级
### 易用、简洁且高效的http库
官网在这里:http://axios-js.com/

### 安装axios,实现vue连接django


```
npm install axios --save
```


### vue-cli注册axios
首先在 main.js 中引入 axios


```js
import axios from 'axios'
```

这时候如果在其它的组件中，是无法使用 axios 命令的。所以我们将 axios 改写为 Vue 的原型属性


```js
Vue.prototype.$http= axios
```
在 main.js 中添加了这两行代码之后，就能直接在组件的 methods 中使用 $http命令

例如


```js
methods: {
show() {
  this.$http({
    method: 'get',
    url: '/user',
    data: {
      name: 'virus'
    }
 })
}
```
### 配置 axios
实际上只有 url 是必须的  
对于get请求


```js
axios.get('/user', {
      params:{
            name:"virus"  
      }
})
```
更多详情参考:[vue-cli 引入axios及跨域使用](https://www.jianshu.com/p/e36956dc78b8)
### 然后就访问会报错,别慌


```
Access to XMLHttpRequest at 'http://127.0.0.1:8000/api/test/' from origin 'http://localhost:8080' has been blocked by CORS policy: No 'Access-Control-Allow-Origin' header is present on the requested resource.
```
因为不允许跨站访问,也叫做跨域,这里我们就需要配置一下这个跨域了

这里参考:卖火柴的小女孩的[vue2.0 proxyTable配置，解决跨域](https://segmentfault.com/a/1190000014396546)

## 难点
上面的报错依旧没有解决,这并不是因为解决方案不正确,而是有其他的原因
### 两天未解决的问题
在使用vue和axios进行跨域请求的时候,一直以为是vue这边没有配置好,

尝试了很久,查了很多关于vue跨域的资料,还使用jq中的ajax直接进行访问都不好使

但是访问[这个](https://autumnfish.cn/api/joke)好使,这就证明不是vue+axios和边的问题了,这里仅仅是指定一下url即可,在`config/index.js`中配置的仅仅的让`test.vue`文件中不用写上全部路径

原来是django里面没有设置允许跨域访问的原因,O(∩_∩)O哈哈~
[django解决跨域请求的问题](https://blog.csdn.net/apple9005/article/details/54427902)

### 解决方案 
具体实现如下:
#### 1.安装django-cors-headers


```
pip install django-cors-headers
```

#### 2.在django的设置文件`setting.py`中,加入


```python
INSTALLED_APPS = [
    ...
    'corsheaders'，
    ...
 ] 

MIDDLEWARE_CLASSES = (
    ...
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware', # 注意顺序
    ...
)
#跨域增加忽略
CORS_ALLOW_CREDENTIALS = True
CORS_ORIGIN_ALLOW_ALL = True
CORS_ORIGIN_WHITELIST = (
    '*'
)

CORS_ALLOW_METHODS = (
    'DELETE',
    'GET',
    'OPTIONS',
    'PATCH',
    'POST',
    'PUT',
    'VIEW',
)

CORS_ALLOW_HEADERS = (
    'XMLHttpRequest',
    'X_FILENAME',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
    'Pragma',
)
```
之后报错,别慌!


```
django.core.management.base.SystemCheckError: SystemCheckError: System check identified some issues:

ERRORS:
?: (corsheaders.E013) Origin '*' in CORS_ORIGIN_WHITELIST is missing  scheme or netloc
        HINT: Add a scheme (e.g. https://) or netloc (e.g. example.com).
```
然后在配合的[这个](https://www.cnblogs.com/sea-stream/p/10965147.html)全部解决了问题,完美简直



## 项目的源码地址
gitee:[vue_django_project](https://gitee.com/victorfengming/vue_django_project)  
大家可以clone下来进行参考,如果觉得有用的可以给小编`star`一下,你的支持就是我的动力!
