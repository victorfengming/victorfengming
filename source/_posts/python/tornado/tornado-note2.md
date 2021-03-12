---
title: "tornado学习笔记day02"
cover: "/img/lynk/59.jpg"
date:       2019-12-06
subtitle: "进阶与提升"
tags:
	- Python
	- solution
	- web
	- tornado
---










#  整理基础工程
- 请看第一天的配置文件目录,搭建了一个框架的基础目录
#  Application
##  settings
###  debug
####  作用
可以设置tornado是否工作在调试模式下面,默认为false,即工作在生产模式下
####  true的特性:
#####  自动重启:
- tornado程序会监控源代码文件,会自动重启服务器,减少我们手动重启的次数,提高开发效率
- 如果保存后有错误,导致重启失败,修改好后,不会再重启了,需要我们手动进行重新启动
- 在debug开启后,那四个特性咱也不太会啊,咱就想着能够重启就得了,那这可咋整,这个时候我们可以通过`"autoreload" : True`设置,仅仅有第一个特性
#####  取消缓存编译的模板:
- 单独设置:`compiled_template_cache = False`
- ,这个默认值为`true`,这里要注意不是说我`debug`设置默认为啥,里面就默认都是啥
- 你改完了模板的内容,它得加载你改了的啊,不能还用缓存的内容,要不然你看不到修改的新结果,这可不行
- 虽然出于性能考虑,老也重新加载有点儿慢,但是没事儿,毕竟开发中也不差这一点资源
#####  取消缓存静态文件的HASH值
- 单独设置:`static_hash_cache = False`
- css文件每次后面都有一个哈希值,这个哈希值能缓存
- 这样我们都能重新加载这个css就OK了
#####  提供追踪信息
- 如果我们的IndexHandler里面抛出了一个异常,但是他自己没有捕获这个异常,就会生成一个追踪的页面
- 单独设置:`serve_traceback = True`
###  template_path: 
设置模板文件目录
###  static_path : 
设置静态文件目录
###  auto_escape : 
当为None时,关闭项目的自动转义
### cookie_secret:
配置安全cookie秘钥
### xsrf_cookie:
当为True,开启XSRF保护
### login_url
用于定义登录的路径,默认找这里
## 路由
- `(r"/", index.IndexHandler),`
- 传的参数在路由那嘎达的字典类型的数据

        
        
        
```

D:.
│  config.py
│  readme.md
│  server.py
│  application.py
│  
├─.idea
│  │  .gitignore
│  │  itcast_tornado.iml
│  │  misc.xml
│  │  modules.xml
│  │  vcs.xml
│  │  workspace.xml
│  │
│  └─inspectionProfiles
│          profiles_settings.xml
│
├─static # 静态资源文件夹    
├─templates # 模板文件
├─upfile  # 上传文件
│
└─views # 视图
   │  index.py # 首页视图
   └─ __init__.py

```




## version1.0
创建一个`index.py`文件在`views`包下面,内容如下
```python
from tornado.web import RequestHandler


class IndexHandler(RequestHandler):
    def get(self):
        self.write("main page info tornado!")

```
在`server.py`文件中修改如下
```python
import tornado.web
import tornado.ioloop
import tornado.httpserver
import tornado.options
import config
from views.index import IndexHandler

if __name__ == '__main__':
    app = tornado.web.Application(
        [
            (r"/", IndexHandler)
        ]
    )
    httpServer = tornado.httpserver.HTTPServer(app)
    httpServer.bind(config.options["port"])
    httpServer.start(1)
    tornado.ioloop.IOLoop.current().start()

```
其中的`config.py`不用动
```python
options = {
    "port": 8080,
    "list": ["good", "nice", "handsome"]
}
```

## version2.0

创建一个`application.py`的文件,内容如下
```python
import tornado.web
from views.index import IndexHandler

class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/", IndexHandler)
        ]
        super(Application,self).__init__(handlers)
```

然后服务端这么改
```python
import tornado.ioloop
import tornado.httpserver
import tornado.options

import config
from application import Application


if __name__ == '__main__':
    app = Application()
    httpServer = tornado.httpserver.HTTPServer(app)
    httpServer.bind(config.options["port"])
    httpServer.start(1)
    tornado.ioloop.IOLoop.current().start()

```

视图都不用动
```python
from tornado.web import RequestHandler


class IndexHandler(RequestHandler):
    def get(self):
        self.write("main page info tornado!")
```

因为tornado不是Django那种大而全的,而是小而精的

所以配置也不用怎么动
```python
# 参数
options = {
    "port": 8080
}

# 配置
settings = {
    # static_path = "/",
    "debug" : True
}
```

成了这就

然后我们再配置一个路由`home`  
在application里面直接加就OK
```python
import tornado.web
from views import index

class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/", index.IndexHandler),
            (r"/home", index.HomeHandler),
        ]
        super(Application,self).__init__(handlers)
```
然后在视图中再创建一个对应的类
```python
from tornado.web import RequestHandler


class IndexHandler(RequestHandler):
    def get(self):
        self.write("main page info tornado!")

class HomeHandler(RequestHandler):
    def get(self):
        self.write(" this is home page content!")
```
重启服务即可在浏览器中访问`http://127.0.0.1:8080/home`看到结果

## 配置路径
Django中的那个BASE_DIRS挺好用的,我们也想有一个,那我们也可以整

```python
import os
BASE_DIR = os.path.dirname(__file__)

# 参数
options = {
    "port": 8080
}

# 配置
settings = {
    # 这写key的名字可不是随便起的奥,是写好的,
    # 就像upfile就没有,你写了也白扯
    'static_path' : os.path.join(BASE_DIR,"static"),
    'template_path' : os.path.join(BASE_DIR,"templates"),
    "debug" : True
}
```

## 路由参数的传递

传递的方式和Django差不多,但也有不同之处,这里直接上代码

路由里面这样发

```python
import tornado.web
from views import index

class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/", index.IndexHandler),
            (r"/sunck", index.SunckHandler,{'name':"victor",'age':19}),
        ]
        super(Application,self).__init__(handlers)
```

视图里面这样接
```python
from tornado.web import RequestHandler


class IndexHandler(RequestHandler):
    def get(self):
        self.write("main page info tornado!")


class SunckHandler(RequestHandler):
    # 该方法会在HTTP方法之前调用
    def initialize(self,age,name) -> None:
        self.age = age
        self.name = name

    def get(self):
        print(self.age)
        print(self.name)
        self.write("sunck page info tornado!")

```

这里不能再get方法中直接加上参数接受

需要重写initialize方法,来对成员属性进行定义
