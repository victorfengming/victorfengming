---
title: "tornado学习笔记day08"
cover: "/img/lynk/17.jpg"
date:       2019-12-09
subtitle: "tornado中的异步"
tags:
	- Python
	- solution
	- web
	- tornado
---









### 概述
应为epoll主要用来解决网络的并发问题,所以tornado中的异步也是主要体现在网络的IO异步上,即异步web请求

### tornado.httpclient.AsyncHTTPClient
tornado提供异步web请求客户端,可以用来进行异步web请求,
这个客户端和服务端是相对来说的,当tornado的Handler去其他位置去请求资源的时候,他就是客户端


### fetch(request, callback=None)
用于执行一个web请求,并异步响应返回一个tornado.httpclient.httpresponse  
request可以是一个url,也可以是一个tornado.httpclient.httprequest对象  
如果插入的是url会自动生成一个request对象
### HTTPRequest
#### 概述
HTTP请求类,该类的构造函数可以接收参数
#### 参数
- url: 字符串类型,要访问的网址,必传
- method: 字符串类型,HTTP请求方式
- headers: 字典类型,或者HTTPHeaders类型
- body: HTTP请求体

### HTTPResponse
#### 响应类
#### 属性
- code: 状态码
- reason: 状态码的描述
- body: 响应的数据
- error: 异常
### @tornado.web.asynchronous
不关闭通讯的通道
```python
'''tornado 6之后弃用'''
@tornado.web.asynchronous
改成
@tornado.gen.coroutine
```
### 示例
#### 回调函数实现异步
代码示例

```python
class Students1Handler(RequestHandler):
    def on_response(self,response):
        print("刚进到on_response里面n")
        if response.error:
            self.send_error(500)
        else:
            print("开始获取data")
            data = json.loads(response.body)
            print("data获取成功")
            self.write(data)
            print("data写入成功")
        self.finish()

    @tornado.gen.coroutine
    def get(self):
        # 获取所有学生的信息
        # time.sleep(30)
        # 创建客户端
        url = "http://127.0.0.1:8080/home"
        print("url是",url)
        client = AsyncHTTPClient()
        print("客户端创建成功")
        client.fetch(url, self.on_response)

        self.write("students info content!")

class HomeHandler(RequestHandler):
    def get(self):
        # 获取所有学生的信息
        self.write("homo page info!")
```
#### 协程实现异步
代码示例1

```python
class Students2Handler(RequestHandler):
    @tornado.gen.coroutine
    def get(self, *args, **kwargs):
        url = "http://s.budejie.com/topic/tag-topic/64/hot/budejie-android-6.6.9/0-20.json?market=xiaomi&ver=6.6.9&visiting=&os=7.1.1&appname=baisibudejie&client=android&udid=863254032906009&mac=02%3A00%3A00%3A00%3A00%3A00"
        client = AsyncHTTPClient()
        res = yield client.fetch(url)
        if res.error:
            self.send_error(500)
        else:
            data = json.loads(res.body)
            self.write(data)
```

代码示例2 , 将异步web请求单独分离出来

```python
class Students3Handler(RequestHandler):
    @tornado.gen.coroutine
    def get(self, *args, **kwargs):
        res = yield self.getData()
        self.write(res)

    @tornado.gen.coroutine
    def getData(self):
        url = "http://s.budejie.com/topic/tag-topic/64/hot/budejie-android-6.6.9/0-20.json?market=xiaomi&ver=6.6.9&visiting=&os=7.1.1&appname=baisibudejie&client=android&udid=863254032906009&mac=02%3A00%3A00%3A00%3A00%3A00"
        client = AsyncHTTPClient()
        res = yield client.fetch(url)
        if res.error:
            ret = {"ret":0}
        else:
            ret = json.loads(res.body)
        raise tornado.gen.Return(ret)
class HomeHandler(RequestHandler):
    def get(self):
        # 获取所有学生的信息
        self.write("homo page info!")
```
