---
title: "tornado学习笔记day01"
date:       2019-12-05
subtitle: "高并发性能web框架"
tags:
	- Python
	- solution
	- web
	- tornado
---


* content
{:toc}




## tornado的安装
这里我使用的是[虚拟环境](https://victorfengming.gitee.io/2019/11/18/python-venv/)中的[pip](https://victorfengming.gitee.io/2019/10/12/python-install-pip/)安装,配合[清华大学镜像源](https://victorfengming.gitee.io/2019/11/20/pip-conf/)安装的

```shell
pip install tornado -i https://pypi.tuna.tsinghua.edu.cn/simple
```

## 我的第一个tornado程序
```python
import tornado.web
import tornado.ioloop


class IndexHandler(tornado.web.RequestHandler):
    '''
    主页处理函数
    '''
    def get(self):
        self.write("hello tornado!")


if __name__ == '__main__':
    app = tornado.web.Application([(r"/",IndexHandler)])
    app.listen(8000)
    tornado.ioloop.IOLoop.current().start()

```

在tornado中,直接执行就行,不用加任何参数也OK

因为在里面已经帮你创建了一个服务器了

## 初始tornado
### 什么是tornado
 
全称tornado web server ,是一种web服务器软件的开源版本

### 特点
作为web 框架,是一个轻量级的web框架,类似于另一个python web 框架 web.py,其拥有一部非阻塞IO的处理方式

作为 web 服务器,tornado 有较为出色的抗负载能力,官方用nginx反向dialing的方式部署tornado和其他python web 应用框架进行对比,结果最大浏览量超过第二名近40%

### 使用场景
- 用户量大,高并发
- 大量的HTTP持久连接
    - 使用同一个TCP连接来发送和接收多个HTTP请求/应答,而不是为每一个新的请求/应答打开新的连接方式
    - 对于HTTP1.0,可以在请求的包头(Header)中添加Connection: Keep-Alive。
    - 对于HTTP 1.1，所有的连接默认都是持久连接。
 
 
### C10K
上面的高并发的为题,通常用C10K这一概念来描述.C10K-Concurrently handling ten thousand connections ,即并发10000个连接,对于单台服务器而言,根本无法承担,而采用多台服务器分布式又意味着高昂的成本

### 性能
tornado在设计之初就考虑到了性能因素,旨在解决C10K问题,这样的设计使得其成为一个拥有非常高性能的解决方案(服务器与框架的集合体) 
 
### tornado和django对比
#### django
django是走大而全的方向,注重的是高效开发,它最出名的是其全自动化的管理后台:只需要使用起ORM,做简单的对象定义,它就能自动生成数据库结构,以及全功能的管理后台

Django提供的方便,也意味着Django内置的ORM跟框架内的其他模板耦合程度高,应用程序必须使用Django内置的ORM,否则就不能享受到框架内提供的种种基于其ORM的便利

特点:
- session功能
- 后台管理
- ORM
#### tornado
tornado走的是少而精的方向,注重的是性能的优越,它最出名的是异步非阻塞的设计方式
特点
- HTTP服务器
- 异步编程
- webSockets


### 第一个程序的批注解释1.0
```python
import tornado.web
'''
tornado的基础web框架模块
'''
import tornado.ioloop
'''
tornado的核心IO循环模块,
封装了Linux的epoll和BSD的kqueue
这个是tornado高效的基础
'''


# 业务处理类
# 类比Django的视图
class IndexHandler(tornado.web.RequestHandler):
    '''
    主页处理函数
    '''

    # 处理GET请求的
    def get(self):
        '''
        这个get不是随便写的,是框架提前定义好的
        :return:
        '''
        # 对应HTTP请求的方法
        # 给浏览器响应信息
        self.write("hello tornado!")


if __name__ == '__main__':
    # 这个路由和django差不多,只不过这个调用的是一个类
    # 实例化app应用对象
    # Application是tornado框架的核心,与服务器对接的接口
    # 里面保存了路由映射表,有一个listen方法,用来创建一个HTTP服务器的实例,并绑定了端口
    app = tornado.web.Application([(r"/",IndexHandler)])

    # 这个只是绑定在8000端口,注意:并没有进行监听奥
    app.listen(8000)
    # tornado的启动方式
    # IOLoop.current():返回当前线程的IO实例
    # IOLoop.start(): 启动实例的IO循环,同时开启监听
    tornado.ioloop.IOLoop.current().start()

```


### 第一个程序的批注解释2.0
```python
import tornado.web
'''
tornado的基础web框架模块
'''
import tornado.ioloop
'''
tornado的核心IO循环模块,
封装了Linux的epoll和BSD的kqueue
这个是tornado高效的基础
'''

# 引入httpserver模块
import tornado.httpserver

# 业务处理类
# 类比Django的视图
class IndexHandler(tornado.web.RequestHandler):
    '''
    主页处理函数
    '''

    # 处理GET请求的
    def get(self):
        '''
        这个get不是随便写的,是框架提前定义好的
        :return:
        '''
        # 对应HTTP请求的方法
        # 给浏览器响应信息
        self.write("main page info tornado!")


if __name__ == '__main__':
    # 这个路由和django差不多,只不过这个调用的是一个类
    # 实例化app应用对象
    # Application是tornado框架的核心,与服务器对接的接口
    # 里面保存了路由映射表,有一个listen方法,用来创建一个HTTP服务器的实例,并绑定了端口
    app = tornado.web.Application([(r"/",IndexHandler)])

    # 这个只是绑定在8000端口,注意:并没有进行监听奥
    # app.listen(8000)
    # 实例化一个http服务器对象
    httpServer = tornado.httpserver.HTTPServer(app)
    # 绑定端口
    httpServer.listen(8000)
    # 这个和上面的listen可不一样,两个对象的方法,不同
    # 说白了,上面的一行,相当于我们这个两行代码的和
    # 这也就是tornado不用像Django那样加上runserver参数启动服务器了
    # 以为代码中写了

    tornado.ioloop.IOLoop.current().start()


```



### 第一个程序的批注解释3.0
```python
import tornado.web
import tornado.ioloop
import tornado.httpserver


class IndexHandler(tornado.web.RequestHandler):
    '''
    主页处理函数
    '''
    
    def get(self):
        '''
        这个get不是随便写的,是框架提前定义好的
        :return:
        '''
        
        
        self.write("main page info tornado!")

if __name__ == '__main__':
    app = tornado.web.Application([(r"/",IndexHandler)])
    

    httpServer = tornado.httpserver.HTTPServer(app)
    
    # httpServer.listen(8000)
    # 这里不用listen了,我们用bind
    # 将服务器绑定到指定的端口上
    httpServer.bind(8000)
    # 这里我写几个就开几个进程
    '''
    默认开启一个进程
    如果大于0,开启多个进程
    值为none或者小于等于0的话,就开启对应硬件机器CPU核心数的子进程
    '''
    httpServer.start(5)
    # 这个bind和start加一起就相当于 httpServer.listen(8000)了
    # 近期你可以多些一点,以为你要对于创建服务器的流程有一个了解,以后随便写


    # app.listen() 只能在单继承模式中使用
    '''
    多进程: 虽然tornado给我们提供了一次性启动多进程的方式,
        但是由于一些原因,我们不建议使用这种方式,来启动多进程,
        而是手动启动多进程,并且还能绑定多个端口
    多进程有三个问题:
        1. 每个紫禁城都会从父进程中复制出一份IOloop的实例,
            如果在创建紫禁城钱,修改了IOloop,会影响到所有的紫禁城实例
        2. 所有的进程都是由一个命令启动的,无法做到在不停止服务的情况下修改代码,这样不好
        3. 所有进程共享一个端口,想要进行监控,有点难
    我自己来启动的话,能在一个进程运行后,修改源代码,来单独在运行一遍,也OK
    '''

    tornado.ioloop.IOLoop.current().start()

```




### 第一个程序的批注解释4.0
```python
import tornado.web
import tornado.ioloop
import tornado.httpserver
import tornado.options

"""
通常如果程序非正常结束
就会出现:"通常每个套接字地址(协议/网络地址/端口)只允许使用一次"
这是因为端口没有没释放
这时我们的debug模式还没开启

tornado为我们提供了一tornado.option模块
用于全局参数的定义/存储/转换
option:
    不让端口写死,让option这个值从外部传进来
基础方法与属性:
help : 其实就是选项变量的帮助提示信息,一般不用         
"""

# 这个函数的原型
'''
def define(
    name: str,
    default: Any = None,
    type: type = None,
    help: str = None,
    metavar: str = None,
    multiple: bool = False,
    group: str = None,
    callback: Callable[[Any], None] = None,
) -> None:
'''
# 这个函数的功能
'''
用来定义option选项变量的方法
'''
# 参数
'''
name : 选项变量名,必须保证其唯一性,否则会爆出一个option already define 错误
default : 设置选项变量的默认值,如果不传,默认为none
type : 设置选项变量的类型,比如int,从命令行或者配置文件导入参数时,
    tornado会根据输入的数据类型的值进行转换
    会根据类型转换成对应的值,转换不成,会报错,那么就有问题了
    可以:int float str datetime timedelta
    如果没有设置type,会根据default的值进行转换,
    如果default没有设置,他就不进行转换
multiple : 设置选项变量是否可以为多个值,默认为false    
'''

# 好我们可以先写一个
tornado.options.define("port", default=8000, type=int)
# 我们要接受一个列表,列表里面的元素的字符串类型,默认给个空
tornado.options.define("list", default=[], type=str,multiple=True)

# 然后我们还有一个属性
'''
tornado.options.options
全局的options对象
所有定义的选项变量都会作为改对象的属性
'''

# 获取参数的方法
'''
我们不是把这些参数赋值了么,我们还要把这些参数存储起来
tornado.options.parse_command_line()
    作用:
        转换命令行参数,将命令行参数抓换成为option的属性
'''


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("main page info tornado!")


if __name__ == '__main__':
    # 转换命令行参数,并保存在tornado.options.options里面
    tornado.options.parse_command_line()
    # 可以打印一下list
    print('list->',tornado.options.options.list)
    app = tornado.web.Application([(r"/", IndexHandler)])

    httpServer = tornado.httpserver.HTTPServer(app)
    # 使用变量的值
    httpServer.bind(tornado.options.options.port)

    httpServer.start(1)

    tornado.ioloop.IOLoop.current().start()

    # 这样我们在启动的时候就能不需要修改代码就能指定端口号了
    # 代码能少改就少改变
    '''
    (venv) D:\PycharmProjects\itcast_tornado>python 01.py --port=9000 --list=good,nice,handsome,cool
    list-> ['good', 'nice', 'handsome', 'cool']
    [I 191205 17:13:54 web:2246] 200 GET / (127.0.0.1) 1.00ms
    [W 191205 17:13:54 web:2246] 404 GET /favicon.ico (127.0.0.1) 1.00ms
    '''
```

### 创建配置文件方式
`在linux里面,所有的东西都是文件,就算他是目录,都是文件`

创建一个名为config的普通文件,位置在py文件的旁边

内容如下:
```python
port = 7000
list = ["good","nice","handsome"]
```

程序中这样写:
```python
tornado.options.parse_config_file("config")
# 因为是同级目录,所以相对路径直接写就OK了
```

然后正常运行程序就OK了
```shell
D:\PycharmProjects\itcast_tornado\venv\Scripts\python.exe D:/PycharmProjects/itcast_tornado/01.py
list-> ['good', 'nice', 'handsome']
[I 191205 17:27:21 web:2246] 200 GET / (127.0.0.1) 0.00ms
[W 191205 17:27:21 web:2246] 404 GET /favicon.ico (127.0.0.1) 0.00ms
```

我们现在有两种方式来获得参数,一种是命令行的一种是文件的,但是以后我们要使用哪种方式呢,???  

都不是...  

说明:  
    因为这个配置文件要按照python 的语法要求来进行书写  
    调用参数的时候,不支持字典类型  
    
最终版本:  
创建一个名为config.py的文件  
内容如下:  
```python
# 参数 字典类型的了

options = {
    "port": 8080,
    "list": ["good", "nice", "handsome"]
}

```    

脚本这样写:
```python
import tornado.web
import tornado.ioloop
import tornado.httpserver
import tornado.options
import config

# 获取参数的方法
# 好我们可以先写一个
tornado.options.define("port", default=8000, type=int)
# 我们要接受一个列表,列表里面的元素的字符串类型,默认给个空
tornado.options.define("list", default=[], type=str, multiple=True)


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("main page info tornado!")


if __name__ == '__main__':

    # 可以打印一下list
    print('list->', config.options["list"])
    app = tornado.web.Application([(r"/", IndexHandler)])

    httpServer = tornado.httpserver.HTTPServer(app)
    # 使用变量的值
    httpServer.bind(config.options["port"])

    httpServer.start(1)

    tornado.ioloop.IOLoop.current().start()

```

这个config可以写成模板,其中可以包含各种配置信息,不仅仅局限于这点儿

### 日志
当我们使用parse_command_line()或者parse_config_file(path)方法时

tornado会默认开启logging模块功能,向我们的屏幕打印一些相关信息

如果有处女座不想看这个信息,可以这样

比如是从普通文件中导入的那种,要在后面再加上一句:
```python
tornado.options.parse_config_file("config")
tornado.options.options.loggings = None
```


