---
title: "tornado学习笔记day05"
cover: "/img/lynk/84.jpg"
date:       2019-12-07
subtitle: "访问数据库"
tags:
	- Python
	- solution
	- web
	- tornado
---









# 模板

## 配置模板路径
这个在之前我们已经配置好了,可以参考前面的文章
```python
settings = {
    # 就像upfile就没有,你写了也白扯
    'template_path': os.path.join(BASE_DIR, "templates"),
}
```
## 渲染并返回给客户端

使用render()方法

```python
class HomeIndexHandler(RequestHandler):
    def get(self):
        self.render("home.html")
```
## 变量与表达式

### 语法
- { { var } }
- { { expression } }
### 实例
```python
class HomeIndexHandler(RequestHandler):
    def get(self):
        temp = 100
        # 直接传一个变量就行
        self.render("home.html",num = temp)
        # self.render("home.html")
```

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>主页</title>
</head>
<body>
   <h1>这里是主页</h1>
   { { num } }
   <br>
   <!-- 这里支持加减  -->
   { { num + 1 } }
   { { num + 18 } }

   <!-- 这里需要用模板的注释才能真正的注释掉双大括号 -->
   <!-- 这里一定要注意,这个普通的注释会被加载到页面中 -->
   {# num: { { num } } #}
   <!-- 模板的注释才是真正的注释 -->
   {# num: { { num + 10 } } #}
   <!-- 等号的赋值的不好使的,会报错  -->
   {# num: { { num = 5} } #}
</body>
</html>
```

## 流程控制
### if
#### 格式
单个的if
```angular2html
{ % if表达式 % }
语句
{ % end % }
```
if和else的
```angular2html
{ % if表达式 % }
语句1
{ % else % }
语句2
{ % end % }
```
多个if 的

```angular2html
{ % if表达式1 % }
语句1
{ % elif 表达式2% }
语句2
{ % elif 表达式3% }
语句3
<!--这里面else可有可无-->
{ % end % }
```
#### 实例
```angular2html
{ % if flag == 0% }
flag确实是0
{ % elif flag == 0 % 
语句2
{ % elif flag == 2 % }
flag bug
{ % else % }
baiche
{ % end % }
```
### for
这里面需要注意的是,结束模板语法都是` { % end % }`
```angular2html
{ % for 变量 in 集合 % }
语句
{ % end % }
```
实例:
```angular2html
<ul>
    { % for stu in stus % }
    <li>{ { stu } }</li>
    { % end % }
</ul>
```
### while
这个while很少使用,就不写了


## 函数 
### static_url()
#### 作用
- 获取配置中的静态目录的路径
- 将参数拼接到静态目录后面并返回新的路径
#### 示例
```angular2html
<link rel="stylesheet" href="{ { static_url('css/home.css') } }">
```
#### 优点
- 修改目录的话 只需要修改配置文件中的内容即可,不需要修改各种页面中的URL
- Hash值
    - static_url创建了基于文件内容的Hash值
    - 将其添加到文件的末尾(当一个查询参数)
    - 这个hash值总能够保证,我们每一次加载最新的版本
    - 而不是之前的缓存的版本
    - 不论是开发阶段还是线上阶段,都是很有必要的

## 转义
tornado默认开启自动转义功能,能够防止网站攻击
```python
class TranHandler(RequestHandler):
    def get(self):
        str = "<h1>能不能转义就看这会的了</h1>"
        self.render("trans.html",str = str)
```

```angular2html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>转义</title>
</head>
<body>
{ {str} }
</body>
</html>
```
页面这样显示
```
<h1>能不能转义就看这会的了</h1>
```
### 关闭自动转义
- raw:`{ % raw str % }`这个会关闭一行
- 在页面模板中修改
    - autoescape:`{ % autoescape None % }`
    - 这个不管你三七二十一都关闭了就
- 在配置文件中修改 
    - `autoescape : None` 
    - 当为None时关闭当前项目的自动转义
- escape()函数
    - 这个函数能够在全局转义的条件下再不转义
    - `{ { escape(str) } }`    
    
## 继承
## 静态文件
- static_path
    - 作用
        - 告诉tornado从文件系统中某一个特定的位置提供我们的静态文件
    - 示例:`'static_path': os.path.join(BASE_DIR, "static"),`
    - 请求方式:`http://127.0.0.1:8080/static/html/index.html`
    - 引用其他文件:
    ```angular2html
    <link rel="stylesheet" href="{ {static_url('css/index.css')} }">
    <script src="{ {static_url('js/jquery.js')} }"></script>
    ```
    
- StaticFileHandler 
    - 使用原因:这种请求方式:`http://127.0.0.1:8080/static/html/index.html`对于用户来说,体验不佳
    - 本质: 是tornado预制的用来提供静态资源文件的Handler
    - 作用: 可以通过StaticFileHandler来映射静态资源文件
    - 使用:
        - 第一种写法
        ```python
        (r"/(.*)$", tornado.web.StaticFileHandler,{
                        "path":os.path.join(BASE_DIR,"static/html"),
                    }),
        ```
        - 第二种:
        ```python
        (
            r"/(.*)$",
            tornado.web.StaticFileHandler,
            {
                "path": os.path.join(BASE_DIR, "static/html"),
                "default_filename": "index.html"
            }
        ),
        ``` 
    - 参数:
        - path:用来指定访问提供静态文件根路径
        - default_filename:用来指定访问路由中未指定文件名时,访问哪个静态中的文件
         
    - 注意:
        - 最好在其他路由的最下面写
        - 否则可能会不匹配
        - 其中的路由可以去参考一下[百度](https://www.baidu.com/)的





# 数据库
### 概述
tornado目前没有自己的数据库,需要连接数据库,还得自己去适配
目前python3.6+tornado还没有完善的驱动  

### 磁盘数据库和内存数据库:

比如你以前你的爸爸,那个手机啊,欠费了好几十还不给你停机  
因为数据还没来得及处理,那个话费单,得一条一条处理,他处理不过来,知道么,当你欠费的时候,他还不知道你欠费呢  
现在就不一样了,你的话单数据都在内存里面了,你一旦欠费,马上就给你停机,O(∩_∩)O哈哈~

redis的开源的内存数据库,移动联通都不用这种数据库  
内存数据库是国内06年开始有人在搞  
从13年开始,又出现了一个分布式内存数据库,现在人们都有钱了,数据量大了,一台服务器都存不下了  
14年开始,又升级了一下,这次升级的是硬件,以前用的是万兆网卡,现在更NB了 


### 链接
在应用启动时,创建一个数据库链接实例,供各个requestHandler使用

在requestHandler中,通过self.application来获取对象
