---
title: "tornado学习笔记day06"
cover: "/img/lynk/65.jpg"
date:       2019-12-08
subtitle: "应用安全"
tags:
	- Python
	- solution
	- web
	- tornado
---








# 应用安全
### cookie
##### 普通cookie
一般我们的用户表中都有啥呢

你在购物的时候,加入购物车,让你登录,那你登录之后,他怎么知道你登录了呢

token 这个值是随机的,存在`cookie`里面
###### 设置
- 原型: 设置`cookie` 的方法
```python
def set_cookie(
    self,
    name: str,
    value: Union[str, bytes],
    domain: str = None,
    expires: Union[float, Tuple, datetime.datetime] = None,
    path: str = "/",
    expires_days: int = None,
    **kwargs: Any) -> None:
```
- 参数
    - name:我们设置的`cookie`的名字
    - value:cookie的值
    - domain:提交`cookie`时匹配的域名,也就是哪个ip拿过来的
    - path:提交`cookie`时匹配的路径
    - expires:设置`cookie`的有效期,可以是时间磋整数,时间元组,`datetime`类型,为UTC时间
    - expires_days:设置cookie的有效期(天数)但是他的优先级低于expires
- 实例:
    
###### 原理
设置`cookie`实际上是通过设置`header`的`Set-Cookie`来实现的
###### 获取
我们设置完了就要获取,为什么要获取呢,因为以后我们在发送请求就要携带着这个cookie了
- 原型:
```python
def get_cookie(self, name: str, default: str = None) -> Optional[str]:
```
- 参数:
    - name:要获取的cookie 的名称
    - default:如果名为name的获取的cookie不存在,就走这个默认值了
- 示例:



```python
cookie = self.get_cookie("suck","未登录")
print(cookie)
self.write("getcookie page info tornado!")
self.write(cookie)
```


###### 清除
- 原型:



```python
    def clear_cookie(self, name: str, path: str = "/", domain: str = None) -> None:
```
- 作用:
    - 删除名为`name` 的`cookie`,并同时匹配`domain`和`path`的`cookie`
    - 哟时候有可能这个name相同啊,那这个时候就得用path和domain来匹配一下了
- 注意: 
    - 执行cookie删除后,并不是直接就删除了,
    - 而是给cookie设置内容为null空,并删除延迟时间,
    - 真正删除是浏览器自己清理的,浏览器发现他没有用的话就给他删掉了,就看浏览器的了 
- 还有一个原型:
```python
def clear_all_cookies(self, path: str = "/", domain: str = None) -> None:
```   
- 作用:删除同时匹配path和domain的所有cookie    
- 示例:
```python
# 清除cookie
class ClearPCookieHandler(RequestHandler):
    def get(self):
        # 这个删除cookie后,他这次不能决定
        # 是下一次删除了
        # 清除一个cookie
        self.clear_cookie("suck")
        # 清除所有cookie
        self.clear_all_cookies()
        self.write("ClearPCookieHandler page info tornado!")
```
##### 安全cookie
###### 概述:
cookie是存储在客户端浏览器的数据,很容易被篡改,不是很安全

tornado提供了一种对于cookie简易的加密的方法,来防止cookie被恶意篡改


###### 设置:
- 需要为应用配置的进行混淆加密的秘钥  
- 生成一个秘钥: 
我们需要用到一个库`base64`,你需要知道的就是他是加密的就行了,是一个唯一的标识,其他的你就不用管了,因为其他的你想管你也管不着了  
md5 现在已经不安全了,现在有一些网站已经能够在线破解md5了
    
我们在python控制台输入如下代码,即可生成一个uuid    
```python
base64.b64encode(uuid.uuid4().bytes+uuid.uuid4().bytes)
b'j94bbx0zSY6yYkCgawwJ1bzyM4jzDUuKtLyPC/MMmZA='
```
我们需要在配置文件config.py中进行配置  
内容如下
```python
settings = {
    # 这写key的名字可不是随便起的奥,是写好的,
    # 就像upfile就没有,你写了也白扯
    'template_path': os.path.join(BASE_DIR, "templates"),
    'static_path': os.path.join(BASE_DIR, "static"),
    "debug": True,
    # "autoreload" : True
    "cookie_secret":"j94bbx0zSY6yYkCgawwJ1bzyM4jzDUuKtLyPC/MMmZA=",
    # 这个据说一百亿年才能,用完
}
```
然后给你看一个方法,他的原型如下
```python
    def set_secure_cookie(
        self,
        name: str,
        value: Union[str, bytes],
        expires_days: int = 30,
        version: int = None,
        **kwargs: Any
    ) -> None:
```
作用:设置一个带有签名和时间戳的cookie,防止cookie被伪造

实际上是这样写的
```python
# 安全cookie
class SCookieHandler(RequestHandler):
    def get(self):
        self.set_secure_cookie("victor","nice")
        self.write("SCookieHandler page info tornado!")
```

然后我们在浏览器中查看一下cookie的值
```python
Set-Cookie: victor="2|1:0|10:1575853257|6:victor|8:bmljZQ
==|ac4c19c8598fc7c7d07c1484f07a0cc8e1a1adb022d084bcc3d3d4
75129fab63"; expires=Wed, 08 Jan 2020 01:00:57 GMT; Path=/
```
现在这个值,你看不出来内容是啥了  
说明:
- 安全cookie版本,默认使用2
- 默认为0
- 时间戳
- cookie名
- base64cookie编码的值
- 签名值(不带长度说明)
###### 获取:
直接就把原型往这里一扔
```python
    def get_secure_cookie(
        self,
        name: str,
        value: str = None,
        max_age_days: int = 31,
        min_version: int = None,
    ) -> Optional[bytes]:
```
然后我这么写
````python
# 获取安全cookie
class GetSCookieHandler(RequestHandler):
    def get(self):
        sc = self.get_secure_cookie("victor")
        print(sc)
        self.write("getSCookieHandler page info tornado!")
        self.write(sc)
````
如果cookie验证通过,就会返回这个cookie的值,否则返回None

max_age_days不同于expries_days设置的浏览器中cookie的有效时间  
而max_age_days是过滤安全cookie的时间戳,默认是31天


###### 注意:
- 这个安全cookie,也不是绝对安全的,只是一定程度上增加了破解的难度
- 以后cookie中不要存储一些敏感性的数据


### XSRF
#### 跨站请求伪造代码

示例:
```python

# cookie计数
class CookieNumHandler(RequestHandler):
    def get(self):

        count = self.get_cookie("count",None)
        if count:
            # 第n次访问
            count = str(int(count)+1)
            pass
        else:
            # 第一次访问
            # 设置cookie
            count = '0'
        self.set_cookie("count",count)

        self.render("cookienum.html",count = count)
```
页面是这个样子的:
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>搞事情</title>
</head>
<body>
<h1>第{ { count } }次访问</h1>
<p>搞事情网站,我就看看能不能搞坏!!!</p>
<div>
    <img src="http://127.0.0.1:8080/cookienum" alt="">
</div>
</body>
</html>
```
当我们访问搞事情网站的时候,当我们不知情的时候,未授权的情况下,`cookie计数器`网站中的`cookie`被使用,导致`cookie计数器`网站认为是他自己调用了`Handler`逻辑

上一个程序使用的是GET方式模拟的攻击,为了防止这种攻击,一般对于相对安全的操作一般不放在GET请求中.

我们常常使用的是POST请求
#### XSRF保护
同源:同域名同协议同端口
只有同源才让他能访问
#### 开启保护
在配置中添加


```python
"xsrf_cookies":True
```


然后在这里别忘了也整一下


```python
super(Application, self).__init__(
    handlers,
    # 模板路径
    template_path=settings["template_path"],
    # 静态路径
    static_path=settings["static_path"],
    # cookie签名
    cookie_secret=settings["cookie_secret"],
    xsrf_cookies=settings["xsrf_cookies"],
)
```

现在保护一开,谁都别想访问了  
那我们还要干什么?  
我们怎么才能让我们自身的能够进行访问啊
#### 附加
配置文件中的键和值不用一个一个写,直接就`**`打散就OK了
```python
# 是不是傻了,这里直接就** 就行了
super(Application, self).__init__(
    handlers,**settings
)

```
#### 应用
##### 在模板中应用
###### 在form表单中加上这么一句话,模板里面就能用了
```html
{ % module xsrf_form_html() % }
```
###### 完整的就这样了
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Post page</title>
</head>
<body>
    <form action="/postfile" method="post">
        { % module xsrf_form_html() % }
        姓名:<input type="text" name="username">
        <hr/>
        密码:<input type="password" name="password">
        <hr/>
        <input type="submit" value="登录">
    </form>
</body>
</html>
```
###### 作用:
- 为浏览器设置了`_xsrf`的安全`cookie`,这个`cookie`在关闭浏览器后就失效了
- 为模板添加了一个隐藏的输出,隐藏域,名为`_xsrf`,值为`_xsrf`这个`cookie`的值
- 表单中的一个隐藏域,名为...值为...,但是还是不绝对安全
##### 在非模板中应用


###### 手动设置_xsrf的cookie



```python
'''设置XsrfCookieHandler'''
class SetXsrfCookieHandler(RequestHandler):
    def get(self):
        # 设置一个_xsrf的cookie
        self.xsrf_token
        self.finish("OK")
```



###### 第一种

- 我们可以不在页面中写那一行代码  而是写一个`script`的JS代码,其中实现手动的添加一个隐藏`input`
- 手动创建`input`,并设置name的属性值为`_xsrf`,`value`的属性值为名为`_xsrf`的cookie的值

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Post page</title>
</head>
<body>
    <form action="/postfile" method="post">
        <input id="hi" type="hidden" name="_xsrf" value="">
        姓名:<input type="text" name="username">
        <hr/>
        密码:<input type="password" name="password">
        <hr/>
        <input type="submit" value="登录">
    </form>
    <script>
        function getCookie(name) {
            // 这里写的就不用管他是啥意思了
            var cook = document.cookie.match("\\b" + name + "=([^;]*)\\b");
            // 我们要返回的是cookie,不是cook
            // 如果有,那我就拿他的第一个值,就是这个cookie值
            return cook ? cook[1] : undefined
        }
        // 获取cookie
        gc = getCookie("_xsrf");
        console.log(gc);
        document.getElementById("hi").value = gc;
    </script>
</body>

</html>
```
###### 第二种
发起ajax请求:  
我们把这个表单去掉,然后在js中点击这个按钮就发起ajax请求  
我们没有学过原生的ajax吧!那么就需要借助jQuery了吧!

具体代码如下:
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Post page</title>
    <!--    导入jQuery-->
    <script type="text/javascript" charset="utf-8" src="{{static_url('js/jquery.min.js')}}"></script>
</head>
<body>

<input id="hi" type="hidden" name="_xsrf" value="">
姓名:<input type="text" name="username">
<hr/>
密码:<input type="password" name="password">
<hr/>
<input type="submit" value="登录">
<button id="btn" onclick="login()">登录</button>
<script>
    function getCookie(name) {
        // 这里写的就不用管他是啥意思了
        var cook = document.cookie.match("\\b" + name + "=([^;]*)\\b");
        // 我们要返回的是cookie,不是cook
        // 如果有,那我就拿他的第一个值,就是这个cookie值
        return cook ? cook[1] : undefined
    }

    function login() {
        // 发起ajax请求我们有很多种方式
        // 发起post请求我们有两种方式,一种是这个
        $.post("/postfile",
            "_xsrf=" + getCookie("_xsrf") + "&username=" + "victor" + "&passwd=" + "123456",
            // 请求成功后的回调函数
            function (data) {
                alert("ok\\(^o^)/~");
                alert(data);
            }
        );
        // TODO 其实这里要通过DOM元素获取username,和passwd的值的,
        // TODO 因为这里不是作为重点就写了
        /**
         * 这里主要是要带着这个xsrf防护,不然这个是不能给你响应的
         */
    }
</script>
</body>

</html>
```

###### 第三种
其实这种才是最常用的方式,这个`$.post`仅仅只能发起post请求,所携带的参数或者说对于他的控制是比较少的  
`$.ajax`才是最NB的方式

来吧!直接就上代码

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Post page</title>
    <!--    导入jQuery-->
    <script type="text/javascript" charset="utf-8" src="{{static_url('js/jquery.min.js')}}"></script>
</head>
<body>

<input id="hi" type="hidden" name="_xsrf" value="">
姓名:<input type="text" name="username">
<hr/>
密码:<input type="password" name="password">
<hr/>
<input type="submit" value="登录">
<button id="btn" onclick="login()">登录</button>
<script>
    function getCookie(name) {
        // 这里写的就不用管他是啥意思了
        var cook = document.cookie.match("\\b" + name + "=([^;]*)\\b");
        // 我们要返回的是cookie,不是cook
        // 如果有,那我就拿他的第一个值,就是这个cookie值
        return cook ? cook[1] : undefined
    }

    function login() {
        // TODO 这块还是那么回事,数据可以通过DOM来动态获取
        data = {
            "username": "victor",
            "passwd": "123456",
            };
        // 我们需要把我们的数据给他变成一个字符串
        // 这个方法是JS中的东西,不是python,jQuery的
        var data_str = JSON.stringify(data);
        // 这个ajax怎么写呢?,他里面就一个参数,就是一个字典
        $.ajax({
            url: "/postfile",
            // 这个请求方式你写啥,他就是啥,他都能发
            method: "POST",
            data: data_str,
            // 你看吧这个字典中的一个键里面对应的值是函数,
            // 虽然外面就一个字典类型的参数,但是回调函数还是有的
            success: function () {
                alert("ok!!!")
            },
            // 到这里绝壁是不能成功的,因为我这个_xsrf都没写怎么能成功呢
            // 如果想发起请求,我们还需要添加一个headers,也就是请求头
            headers:{
                // 来这个跟着写就对了
                // 这个值就设置成之前那个cookie值就行了
                "X-XSRFToken": getCookie("_xsrf"),
            },
        })
        // 以后发起ajax请求,建议使用这个,功能更加强大

    }
</script>
</body>

</html>
```

###### 问题
其实帅的人是不会用第一种方式写的

需要手动[设置token](https://victorfengming.gitee.io/2019/12/08/tornado-note6/#%E6%89%8B%E5%8A%A8%E8%AE%BE%E7%BD%AE_xsrf%E7%9A%84cookie)  
解决:其实一般我们进入一个网站的时候,通常是不是都先进入主页啊,你进入主页的时候就把这个`xsrf`写进去了

首先我们添加一个进入主页的静态默认页面
```python
(
    r"/(.*)$",
    # 系统这个我们不能用,所以我们继承,
    # tornado.web.StaticFileHandler,
    # 让我们自己写这个继承自系统给我们这个
    index.MyStaticFileHandler,
    {
        "path": os.path.join(BASE_DIR, "static/html"),
        "default_filename": "index.html"
    }
),
```
然后重写StaticFileHandler
```python
from tornado.web import StaticFileHandler

# 设置静态默认
class MyStaticFileHandler(StaticFileHandler):
    # 我们用他的时候只需要重写他的init就可以了
    def __init__(self,*args,**kwargs):
        super(MyStaticFileHandler,self).__init__(*args,**kwargs)
        self.xsrf_token
```
##### 补充
- _xsrf 加一个下划线,我们把他看成是私有的  
- __xsrf就真的是私有的了
### 用户验证
#### 概念
在收到用户请求后,进行一个预先判断用户的认证状态(是否登录),若验证通过正常处理,否则进入登录界面去,滚去登录

#### tornado.web.authenticate 装饰器
tornado将确保这个方法的主体(他修饰的东西)只有合法的用户才能调用
#### get_current_user
我们自己定义一个方法`get_current_user()`  
功能:验证用户的逻辑,应该写在该方法中,  
如果该方法返回的为True说明验证成功,否则验证失败  
验证失败:访客重定向到配置中的所制定的路由(登录界面)  
需要在配置文件`config.py`中写上配置的位置,因为你不一定要跳转到登录界面吧!
```python
"login_url":"/login",
```
这样你要是没登录,他就给你踢到那个页面中了

然后直接就上代码



```python
'''首先 路由是这样的 '''
# 登录界面
tornado.web.url(r"/login", index.LoginHandler,name='login'),
# home页面
(r"/home", index.HomeHandler),
# 一个无名的普通页面,用于测试的
(r"/cart", index.CartHandler),

(
    r"/(.*)$",
    # 系统这个我们不能用,所以我们继承,
    # tornado.web.StaticFileHandler,
    # 让我们自己写这个继承自系统给我们这个
    index.MyStaticFileHandler,
    {
        "path": os.path.join(BASE_DIR, "static/html"),
        "default_filename": "index.html"
    }
),
```



```python
'''登录页面'''
class LoginHandler(RequestHandler):
    def get(self):
        # 进入登录我就要知道我是从哪里进的了
        next = self.get_argument("next","/")
        url = "login" + "?next=" + next
        self.render("login.html", url=url)

    def post(self):
        '''
        咱也不用管是get还是post了
        name = self.get_body_argument("username")
        passwd = self.get_body_argument("passwd")
        '''
        # 直接我就写
        name = self.get_argument("username")
        passwd = self.get_argument("passwd")
        # TODO 这里还是把账号和密码写死了
        if name == "victor" and passwd == "123456":
            # 这个玩意代表从哪个页面跳来的,处理完了
            # 要是没毛病,我还得给你发到那里去
            next = self.get_argument("next", "/")
            # 后面"/"是默认值
            # 重定向走你,但是光重定向不行
            # 我们还得加一个标记
            self.redirect(next + "?flag=logined")
        else:
            next = self.get_argument("next", "/")
            '''
            # 验证失败了,
            # 路由的反向解析,听着挺高大上的
            # 密码输入错误,好几次也得记着人家是从哪里过来的
            '''
            log = self.reverse_url("login")+"?next="+next
            # 我还是得重定向
            self.redirect(log)
```


```python
''' 这个是主页面 '''
class HomeHandler(RequestHandler):
    def get_current_user(self):
        '''
        # 返回True代表验证成功,否则凉凉
        # return False
        # 然后我们这里就能通过之前的flag来判断了
        # 这里还要设置一个默认值否则就是
        # WARNING:tornado.general:400 GET /home (127.0.0.1):
                  Missing argument flag
        '''
        flag = self.get_argument("flag", None)
        # 如果能取到flag,就返回true
        # 要是娶不到,自然就返回False
        return flag

    @tornado.web.authenticated
    def get(self):
        self.render("home.html")
```



```python
''' 这个cart是一个普通的页面'''
class CartHandler(RequestHandler):
    def get_current_user(self):
        return self.get_argument("flag", None)

    @tornado.web.authenticated
    def get(self):
        self.render("cart.html")
```

