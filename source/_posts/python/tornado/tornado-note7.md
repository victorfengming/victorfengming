---
title: "tornado学习笔记day07"
cover: "/img/lynk/51.jpg"
date:       2019-12-09
subtitle: "同步与异步"
tags:
	- Python
	- solution
	- web
	- tornado
---









### 同步
#### 概念
同步就是按部就班的依次执行我们的代码  
#### 进阶
但是有些情况我们有一些比较耗时的从操作,比如去别的地方拿点资源,去其他网站请求数据,去访问数据库,上传文件等等,所以这里面优点瑕疵,有小编一一道来  
比如这样

```python
''' 本模块的功能:<同步异步demo>'''

# 这个就相等于一个客户端的请求
import time


# 添加一个耗时的操作
def longIO():
    print("开始耗时操作")
    time.sleep(5)
    print("结束耗时操作")


def reqA():
    print("开始处理reqA")
    longIO()
    print("结束处理reqA")


# 这个就相等于另一个客户端的请求
def reqB():
    print("开始处理reqB")
    print("结束处理reqB")
```
```python
def main():
    # 这就是同步在处理
    reqA()
    reqB()
    while True:
        '''
        # 如果你要想写死循环,你不要直接写死循环,你得睡一睡
        # 为什么要睡一睡呢,因为你要是不睡你会发现你的CPU利用率占100%
        '''
        time.sleep(0.1)
```
```python
if __name__ == '__main__':
    main()
```

结果

```shell script
开始处理reqA
开始耗时操作# 这里等待了5秒钟
结束耗时操作
结束处理reqA
开始处理reqB
结束处理reqB
```
在请求中添加了一个耗时的操作,导致了我们的同步的效率特别低了,这样也体现不出我们tornado高效的优点

```python
'''

       ┌─┐       ┌─┐ + +
    ┌──┘ ┴───────┘ ┴──┐++
    │                 │
    │       ───       │++ + + +
    ███████───███████ │+
    │                 │+
    │       ─┴─       │
    │                 │
    └───┐         ┌───┘
        │         │
        │         │   + +
        │         │
        │         └──────────────┐
        │                        │
        │                        ├─┐
        │                        ┌─┘
        │                        │
        └─┐  ┐  ┌───────┬──┐  ┌──┘  + + + +
          │ ─┤ ─┤       │ ─┤ ─┤
          └──┴──┘       └──┴──┘  + + + +
                 神兽保佑
                代码无BUG!


'''
```
### 异步
你干一件事情的同事又去干另一件事情
#### 概述
对于耗时的操作,会交给别人(另一个线程)处理,我们继续向下执行,当别人结束耗时操作后,再将处理结果返回给我们
#### 回调函数实现异步

异步其实我们已经用了,js里面有一个很明显的异步,就是在我们发ajax的时候,当我们发完ajax就去干别的活去了,后来ajax有响应了我们才搭理他

来来来,代码演示如下:

```python
'''
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by victor
'''
# 本模块的功能:<异步演示demo>


# 这个就相等于一个客户端的请求
import time
import threading
```
```python
''' 添加一个耗时的操作'''

'''
这样就会有一个问题,这个run()函数的返回值我们接受不到
为了解决这个问题,我们需要写一个函数,这个函数叫做回调函数
'''
def longIO(callback):
    def run(cb):
        print("开始耗时操作")
        time.sleep(3)
        print("结束耗时操作")
        cb("victor is a wonderful man")
    threading.Thread(
        target=run,
        args=(callback,)
    ).start()
```
这个longio这部分 ,就像ajax一样都不用我们来写了

```python
def finish(data):
    print("开始处理回调函数")
    print("接受到longIO的数据为：",data)
    print("结束处理回调函数")

def reqA():
    print("开始处理reqA")
    longIO(finish)
    print("结束处理reqA")


# 这个就相等于另一个客户端的请求
def reqB():
    print("开始处理reqB")
    time.sleep(1)
    print("结束处理reqB")
```
```python
def main():
    # 这就是同步在处理
    reqA()
    reqB()
    while True:
        '''
        # 如果你要想写死循环,你不要直接写死循环,你得睡一睡
        # 为什么要睡一睡呢,因为你要是不睡你会发现你的CPU利用率占100%
        '''
        time.sleep(0.1)

if __name__ == '__main__':
    main()
```

异步只是说tornado能处理多个请求了,你浏览器该等还是得等着

#### 协程实现异步
协程还不理解呢,还想实现异步,你就实现就行了

不用管拥护啥了,进程线程你们搞起来都麻烦呢,更别说协程了

##### 版本1
最low的一个初级版本

```python
'''
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by victor
'''
# 本模块的功能:<>


# 这个就相等于一个客户端的请求
import time
import threading

gen = None

# 添加一个耗时的操作
def longIO():
    def run():
        print("开始耗时操作")
        time.sleep(3)
        try:
            global gen
            gen.send("victor is wonderful!!!")
        except StopIteration as e:
            pass

        print("结束耗时操作")
    threading.Thread(
        target=run,
    ).start()
# 这个longio这部分 ,就像ajax一样都不用我们来写了
'''
这样就会有一个问题,这个run()函数的返回值我们接受不到
为了解决这个问题,我们需要写一个函数,这个函数叫做回调函数
'''

def reqA():
    print("开始处理reqA")
    res = yield longIO()
    print("接受到longIO的数据为：",res)
    # 这里就相当于挂起了
    print("结束处理reqA")


# 这个就相等于另一个客户端的请求
def reqB():
    print("开始处理reqB")
    time.sleep(1)
    print("结束处理reqB")

def main():
    # 这就是同步在处理
    global gen
    gen = reqA()    # 生成一个生成器
    next(gen)   # 执行reqA

    reqB()
    while True:
        '''
        # 如果你要想写死循环,你不要直接写死循环,你得睡一睡
        # 为什么要睡一睡呢,因为你要是不睡你会发现你的CPU利用率占100%
        '''
        time.sleep(0.1)

if __name__ == '__main__':
    main()
```
##### 版本2
###### 我们有一个问题
版本1中在调用reqA的时候和reqB的调用方式可不一样的啊
也就数不能将其视为简单的函数,而是需要作为生成器来用,我们想的时候是当成一个普通函数来对待
###### 现实 

```python
global gen
gen = reqA()    # 生成一个生成器
next(gen)   # 执行reqA
```
###### 理想

```python
reqA()   # 仅仅的简单的调用
``` 
这个时候寄需要我们的`装饰器`来登场了

```python
''' 装饰器还会写么'''
def genCoroutine(func):
    # 这个是带有参数的装饰器
    def wapper(*args,**kwargs):
        # 其实说白了还是那三句话
        global gen
        gen = func(*args,**kwargs)  # 生成一个生成器
        next(gen)  # 执行reqA
    return wapper 
```


然后定义的时候


```python
@genCoroutine
def reqA():
    print("开始处理reqA")
    res = yield longIO()
    print("接受到longIO的数据为：",res)
    # 这里就相当于挂起了
    print("结束处理reqA")

```

然后执行的时候

```python
'''这个就相等于另一个客户端的请求 '''
def reqB():
    print("开始处理reqB")
    time.sleep(1)
    print("结束处理reqB")

def main():
    # 这就是同步在处理
    # global gen
    # gen = reqA()    # 生成一个生成器
    # next(gen)   # 执行reqA
    reqA()
    reqB()
    while True:
        '''
        # 如果你要想写死循环,你不要直接写死循环,你得睡一睡
        # 为什么要睡一睡呢,因为你要是不睡你会发现你的CPU利用率占100%
        '''
        time.sleep(0.1)

if __name__ == '__main__':
    main()
```

##### 版本3
其实版本2中还有一个问题,他存在一个全局的gen变量,说白了就是假装让他不再那块儿 

这个是最复杂版本,看看吧

1. 文档说明,导入相关模块

```python
'''
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by victor
'''
# 本模块的功能:<>


import time
import threading

```


2. 定义装饰器(最重要的部分,实现异步,高效,并发的原理)

```python
def genCoroutine(func):
    '''
    这个好多人就屡不清了
    '''
    def wapper(*args, **kwargs):
        '''
        这样的话这个装饰器就麻烦了,因为我还得要这个全局的gen啊
        我需要获得多个生成器
        '''
        gen1 = func()  # reqA的生成器
        gen2 = next(gen1)  # longIO的生成器

        # 在这里面创建我的线程
        # 挂起他
        def run(g):
            # 这个就是执行longIO去了
            res = next(g)
            try:
                gen1.send(res)  # 返回给reqA数据
            except StopIteration as e:
                # 啥都不干
                pass

        threading.Thread(
            target=run, args=(gen2,)
        ).start()

    return wapper
```

3. 最难执行的部分

```python
'''
# 添加一个耗时的操作
# handler获取数据,(数据库,其他服务器,循环耗时)
'''
def longIO():
    '''
    现在你只需要知道你的耗时的操作是啥,
    线程的东西你不用管了
    tornado都帮你弄好了
    '''
    print("开始耗时操作")
    time.sleep(3)
    print("结束耗时操作")
    # 结束耗时操作后的返回数据
    yield "victor is a cool man"
```

4. 被装饰函数定义

```python
@genCoroutine
def reqA():
    print("开始处理reqA")
    res = yield longIO()
    print("接受到longIO的数据为：", res)
    # 这里就相当于挂起了
    print("结束处理reqA")
```

5. 另一个耗时函数

```python
''' 这个就相等于另一个客户端的请求'''
def reqB():
    print("开始处理reqB")
    time.sleep(1)
    print("结束处理reqB")
```

6. 程序入口函数

```python
def main():
    reqA()
    reqB()
    while True:
        time.sleep(0.1)

if __name__ == '__main__':
    main()
```

以后我们不用谢这么复杂的装饰器了,tornado已经帮我们写好了,你只要有异步就用装饰器来装饰一下就OK,其他的都不需要写

tornado里面指正不是这么写代码,不然要是这样写,你们全费了,tornado留下的都是简单易用的

这玩意不是你理解不理解,你一开始指定是不理解,你多用才能懂里面的原理

这个协程中的异步,其实他本质上不是协程,以为他用了多个线程,因为协程的定义是在一个线程里面玩的,只是来理解tornado实现原理