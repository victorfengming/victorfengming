---
title: "tornado学习笔记day03"
cover: "/img/lynk/65.jpg"
date:       2019-12-07
subtitle: "响应输出"
tags:
	- Python
	- solution
	- web
	- tornado
---










#  write:
###  作用:
将chunk中的数据写到输出缓冲区

###  利用write方法写json数据

- 我们自己手动序列化json的那种方式Content-Type 的属性值为text-html
- 而我们采用write自动序列化方式,我们的content-type 属性为application/json


#  set_default_headers():
###  作用:
- 在进入HTTP响应方法之前被调用
- 可以重新写该方法来设置默认的headers
###  注意:
- 在这个HTTP处理方法中使用set_header设置的字段会覆盖set_default_headers()的值
- 这个set_header和set_default_headers()是有执行的先后顺序的,默认那个当然那先就执行了
#  set_status(status_code,reason=none):
###  作用:为响应设置状态码
###  参数:
####  status_code:
- 状态码的值,为int类型
- 如果reason的值为none,则状态码必须为正常值
####  reason
- String类型
- 描述状态码的词组,比如`404 not found` 中的`not found` 

#  重定向 `self.redirect(url)`:
####  作用:
- 比如你有时候写index,有时候不写,都能进到首页里面,这就是重定向的作用
- 重定向到url网址
####  示例:

```python
class RedirectHandler(RequestHandler):
    def get(self):
        # 直接就重定向了
        self.redirect("/")
```

#  `self.send_error(status_code = 500,**kwargs)`:

- 作用:
    - 抛出HTTP错误状态码,默认为500
    - tornado会调用write_error()方法进行处理
    - 对应Django里面自定义404一样
#  `write_error(status_code,**kwargs)`:
- 作用:
    - 用来处理send_error抛出的错误信息,并返回给浏览器错误界面
- 示例:
```python
class ErrorHandler(RequestHandler):
    def write_error(self, status_code: int, **kwargs: Any) -> None:
        if status_code == 500:
            self.write("服务器内部错误500了")
        elif status_code == 404:
            self.write("资源不存在")
        else:
            self.write("我也不知道是啥错误")

    def get(self):
        # 直接就重定向了
        flag = self.get_query_argument("flag")
        if flag == '0':
            print("有错误")
            self.send_error(500)
            # 这里抛出错误,下面就不会执行了

        print("没毛病")

        self.write("you are right!")
```    

  
# 路由的反向解析
这个tornado里面的比Django的反向解析还要简单一点 

给路由起个名字,便于url改变后,跳转链接失效


### 应用端
```python
class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/", index.IndexHandler),
            (r"/sunck", index.SunckHandler,{'name':"victor",'age':19}),


            # 状态码
            (r"/status", index.StatusHandler),
            # 重定向
            (r"/index", index.RedirectHandler),
            # 错误处理
            # iserror?flag=2
            # 如果等于0就说明,有错误,不等于0就说明没有错误
            (r"/iserror", index.ErrorHandler),

            tornado.web.url(r"/kaige",index.KaigeHandler,name='kaige'),
        ]
        super(Application,self).__init__(handlers)
```

### 视图函数
```python
class IndexHandler(RequestHandler):
    def get(self):
        self.write("main page info tornado!")
        self.write("<br>")
        url = self.reverse_url("kaige")
        self.write("<a href='%s'>去另一个页面</a>" % (url))
        # self.write("<a href="+url+">去另一个页面</a>")
``` 

# tornado.Web.RequestHandler

### 利用HTTP协议向服务器传递参数

### 提取uri的特定部分

`http://127.0.0.1:8080/good/nice/handsome/cool`

实例代码,app部分

```python
''' (r"/good/(\w+)/(\w+)/(\w+)", index.GoodHandler),'''
(r"/good/(?P<p1>\w+)/(?P<p3>\w+)/(?P<p2>\w+)", index.GoodHandler),
```

视图函数部分

```python
class GoodHandler(RequestHandler):
    def get(self,p1,p3,p2):
        self.write("GoodHandler kaige !")
        self.write("<br>")
        self.write(p3)
        self.write("<br>")
        self.write(p2)
        self.write("<br>")
        self.write(p1)                  
```

### 查询字符串(GET方式传递参数)

#### `http://127.0.0.1:8080/zhangmanyu?a=1&b=2&c=4`类型
##### 这里有一个方法
```python
def get_query_argument(
        self,
        name: str,
        default: Union[None, str, _ArgDefaultMarker] = _ARG_DEFAULT,
        strip: bool = True,
    ) -> Optional[str]:
```
##### 参数
######  name:
- 从get请求参数中返回指定参数的值
- 如果出现同名参数,理论上这个方法会返回最后一个值
######  default
- 如果我们设置了为未传递name参数,它会返回默认的值
######  strip
- 表示是否过滤掉两边的空白字符
- 默认为True,过滤
#### `http://127.0.0.1:8080/zhangmanyu?a=1&a=2&c=4`类型
- 一般情况下,很少出现这种情况的
- `def get_query_arguments(self, name: str, strip: bool = True) -> List[str]:`
- 参数: 同上
### 请求体携带数据(POST方式传递参数)
- 这个厉害了,比Django方便,不用在定义一路由函数了,直接在类里面加一个方法就就行了
- 原型在这里
```python
def get_body_argument(
        self,
        name: str,
        default: Union[None, str, _ArgDefaultMarker] = _ARG_DEFAULT,
        strip: bool = True,
    ) -> Optional[str]:
```
### 既可以获取GET请求,也可以获取POST请求
- 直接就上原型就OK了,你不仅要学会举一反三,还要自己进行拓展
- 原型在这里
```python
def get_argument(  # noqa: F811
    self,
    name: str,
    default: Union[None, str, _ArgDefaultMarker] = _ARG_DEFAULT,
    strip: bool = True,
) -> Optional[str]:
```
- **其实有时候,有的结构,看源码才能理解的更加的深刻**
- 还有一个多个的,也是这么回事儿
```python
def get_arguments(self, name: str, strip: bool = True) -> List[str]:
```
### 在HTTP报文头中,增加自定义的字段



# request对象
### 作用
- 存储了关于请求的相关信息
### 比如:
- `HTTPServerRequest(protocol='http', host='127.0.0.1:8080', method='GET', uri='/zhuyin', version='HTTP/1.1', remote_ip='127.0.0.1')`    
### 属性
- method: HTTP请求的方式
- host: 被请求的主机名(服务器的主机名) 
- uri: 请求的完整资源地址,包括路径和get查询的参数部分 
- path: 请求的路径部分
- query: 请求参数部分 
- version: 使用的HTTP版本 
- headers: 请求的协议头,字典类型 
- body: 请求体数据(POST) 
- remote_ip: 客户端的ip地址 
- files: 用户上传的文件,字典类型 


# tornado.httputil.HTTPFile对象
- 功能:在我们上传文件中才能看到他
- 作用:
    是收到的文件对象
### 属性:
- filename: 文件的实际名字
- body: 文件的数据实体
- content-type: 上传文件的类型
### 文件上传



首先,先要滤清一个数据结构,就是request.file对象的数据结构


```python
'''
一个request.file对象的结构示例
{
    'file': [
        {'filename': 'a.txt',
         'body': b'suck is a wonderful man',
          'content_type': 'text/plain'
        },

        {'filename': 'reg.md',
          'body': b'x9xa0',
           'content_type': 'application/octet-stream'
        }
    ]
    
    'img': [
        {'filename': 'a.img',
         'body': b'as\dfhg\ahhf\a\\h\ahfh\af',
          'content_type': 'text/plain'
        }
    ]
}
'''

```


然后,用循环来进行遍历!




```python
class UpFileHandler(RequestHandler):

    def get(self):
        self.render("upfile.html")
    def post(self):
        self.write("上传成功!")
        contents = self.request.files
        for content in contents:
            fileArr = contents[content]
            for fileObj in fileArr:
                file_path = os.path.join(BASE_DIR,"upfile/"+fileObj.filename)
                with open(file_path,"wb") as f:
                    f.write(fileObj.body)
                print("文件写入成功")
```



我知道,要是看不懂那就加一点批注呗!



```python


''' 导入系统操作模块,用于存储接受的文件'''
import os
# 导入BASE_DIR,定位到服务器中的绝对路径
from config import BASE_DIR
from tornado.web import RequestHandler


class IndexHandler(RequestHandler):
    def get(self):
        self.write("main page info tornado!")

class UpFileHandler(RequestHandler):
    '''
    用于上传文件的视图类,其中包含显示表单的get方法
    和用于处理上传的POST方法
    '''
    # get方法,加载表单模板
    def get(self):
        self.render("upfile.html")

    # 文件上传指定是POST请求啦
    def post(self):
        # 用于接收上传的信息
        self.write("上传成功!")
        # 通过request.files对象来获取所有文件对象内容
        contents = self.request.files
        # 遍历最大的字典,拿到没个name类型的字典的键
        # 其中content是字典中的键,比如file,img
        for content in contents:
            # 通过键获取值,拿到相同name的文件列表
            # 这个filearr,就是一个list
            fileArr = contents[content]
            # 遍历文件列表
            # 这个fileObj又是一个dict字典类型
            for fileObj in fileArr:
                # 定义存储路径
                # 通过BASE_DIR来获取服务器的绝对位置
                # 其中通过这个fileObj的字典的filename键,
                # 来获取文件名字,来定义存储路径的文件名称
                file_path = os.path.join(BASE_DIR,"upfile/"+fileObj.filename)
                # 写入文件
                with open(file_path,"wb") as f:
                    # 文件的内容就是body
                    f.write(fileObj.body)
                    # TODO 这里还需要处理的就是,用户上传同名文件
                    #  导致文件重新在服务器中覆盖的问题
                print("文件写入成功")
```