---
title: "tornado学习笔记day04"
date:       2019-12-07
subtitle: "执行顺序"
tags:
	- Python
	- solution
	- web
	- tornado
---



* content
{:toc}





# 响应输出 -> write
### 原型
#### self.write()函数
源码中是这样定义的
```python
def write(self, chunk: Union[str, bytes, dict]) -> None:
```
### 作用
将chunk数据写到缓冲区

### 刷新缓冲区的四种方式
- 程序中断
- 手动刷新
- 缓冲区满了
- 遇到\n

当你写了一个print之后,不是直接就显示在黑屏中断上面的,而是先到缓冲区走一个趟

只是我们python演示不了,这个得用C语言来演示,还得是Linux系统才行,两种条件都不具备

### C程序演示
这里我们需要gcc或者g++(编译C++的)
```python
# include<stdio.h>
int main(){
    while(1){
        printf("hello");
        sleep(0.05);
    }
    return 0;
}
```
### 基础
代码演示
```python
class WriteHandler(RequestHandler):

    def get(self):
        self.write("write page info tornado!")
        self.write("write page nicie tornado!")
        self.write("write page coll tornado!")
        self.write("write page beautiful tornado!")
        '''
        你会发现他们是连着的,因为我都写在了缓冲区里面
        '''
        # 刷新缓冲区, 并关闭当前请求通道
        self.finish()
        # 如果我不写他,当我们的程序结束,他也会刷新了
        # 下面这行就写丢了
        self.write("write page wonderful tornado!")
```
### 利用write方法写JSON数据
在Django那时候是不是有JsonResponse  
比如在豆瓣影评  
当我们往下滚轮的时候请求JSON数据  
在本地通过创建DOM的方式进行加载的


# 接口调用顺序
## 方法
### initialize()

### prepare()
- 作用: 预处理方法,在执行对应的请求方法之前调用
- 注意: 
    - 任何一种HTTP请求,都会执行prepare()方法
    - 这个prepare有点想Django里面的中间件,但是中间件能够在之前或者之后来执行
    - 这个只是在HTTP方法之前执行
    - 能够用于一些,比如反爬虫,我要是不想让你正常请求,不给你响应内容,那我这里直接来个error直接跳过write就OK了
    - 判断用户是否符合规格
### HTTP方法

#### get(参数在URL后面)
- 优点:速度快
- 缺点:承载的数据量低,安全性相对低

#### post(参数单独打包)
- 优点:速度慢
- 缺点:承载的数据量高,安全性相对高了那么一丢丢
- 一般用于修改服务器上面的数据,使用post,其他的就用get吧

#### head
类似get请求,只不过响应中没有具体的内容,用于获取报头的,一般你不会用
#### delete
请求服务器删除指定的资源的
#### put
从客户端向服务器传送指定的内容
#### patch
请求修改局部内容
#### options
返回URL支持所有的HTTP方法


### set_default_headers()方法
### write_error()方法
### on_finish()方法
- 作用:在请求处理结束后调用
- 应用:
    - 我们能在改方法中进行一个资源的清理释放
    - 或者说一个日志的处理
这个内存释放,我们通常不处理,以为这个python也有自带的垃圾回收机制
    - 我们可以对于数据分析的原资料
    - 比如对于访客的身份统计,喜好判断,对于调整本站的内容排行有所参考
- 注意:
    - 尽量不要在该方法中进行相应输出    
    - 这里做的是服务器内部的一些处理,不能关客户端的事儿
    
## 我们可以进行打印出来看一看
```python
class IndexHandler(RequestHandler):
    def initialize(self) -> None:
        print("init_initialize")

    def prepare(self):
        print("prepare")

    def get(self):
        print("get_start")
        self.write("main page info tornado!")

    def set_default_headers(self) -> None:
        print(":set_default_headers")

    def write_error(self, status_code: int, **kwargs: Any) -> None:
        print("write_error")

    def on_finish(self) -> None:
        print("on_finish")

```    

执行的结果顺序如下


```shell script
:set_default_headers
init_initialize
prepare
get_start
on_finish
```


另一种方式,带有错误的情况


```python
class IndexHandler(RequestHandler):

    def initialize(self) -> None:
        print("init_initialize")

    def prepare(self):
        print("prepare")

    def get(self):
        self.send_error(500)
        print("get_start")
        self.write("main page info tornado!")

    def set_default_headers(self) -> None:
        print(":set_default_headers")

    def write_error(self, status_code: int, **kwargs: Any) -> None:
        print("write_error")
        self.write("服务器内部错误!!!")

    def on_finish(self) -> None:
        print("on_finish")
```


执行的结果顺序如下


```shell script
:set_default_headers
init_initialize
prepare
:set_default_headers
write_error
on_finish
get_start
```



## 执行的顺序总结
- 在正常情况下,没抛出错误时
    - :set_default_headers:设置头
    - init_initialize:初始化处理
    - prepare:预处理,预处理也需要头,所以在他后面
    - get_start:开始处理
    - on_finish:善后
- 抛出错误时
    - set_default_headers:
    - init_initialize:
    - prepare:
    - set_default_headers:又重新执行了一遍头,这里
    - write_error:
    - on_finish:
    - get_start:

这个顺序你得记住,其实也不用,你要是忘了就回来看就行了,但是你要理解其中的每个函数的作用

