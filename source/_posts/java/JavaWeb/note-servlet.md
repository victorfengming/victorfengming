---
title: 'JavaWeb笔记03'
date:       2019-11-12
subtitle: 'Servlet'
tags:
	- Java
	- basis
	
	- JDBC
---
  
  
* content  
{:toc}  
  
  
  
  


# 今日内容
1. Servlet
2. HTTP协议
3. Request

## Servlet
### 概念
### 步骤
### 执行原理
### 生命周期
### Servlet3.0注解配置
### Servlet的体系结构
- Servlet -- 接口
    - GenericServlet -- 抽象类:将Servlet接口中其他方法做了默认空实现,只将service()方法作为抽象
        - 将来定义Servlet类时候,可以继承GenericServlet,实现service()方法即可
    - HTTPServlet -- 抽象类:对http协议的一种封装,简化操作
        1. 定义类继承httpservlet方法
        2. 腹泻doGet/doPost方法
### Servlet相关配置
1. urlpattern:Servlet访问路径
    - 一个Servlet可以定义多个访问路径:`@WebServlet({"/d4","/dd4","/ddd4"})`
    - 路径定义规则:
        1. `/xxx`
        2. `/xxx/xxx`
        3. `*.do`*说白了就是通配符,这里注意前面不要加`/`


## HTTP:
### 概念:Hyper Text Transfer Protocol 超文本传输协议
- 传输协议: 定义了,客户端和服务器端通信时,发送数据的格式
- 特点:
    1. 基于TCP/IP 的高级协议
    2. 默认端口:80
    3. 基于请求/响应模型的:一次请求对应一次响应
    4. 无状态的:每次请求之间相互独立,不能交互数据
- 历史版本:
    - 1.0: 每一次请求响应都会建立新的链接
    - 1.1: 复用

### 请求消息数据格式:
1. 请求行
    - 请求方式 请求url 请求协议/版本 GET/login.html HTTP/1.1
    - 请求方式:
        - HTTP协议有7种请求方式,常用的有2种
             - GET:
                1. 请求参数在请求行中,在url后
                2. 请求的url长度有限制的
                3. 不太安全
             - POST:
                1. 请求参数在请求体中
                2. 请求的url长度没有限制的
                3. 相对的安全(其实对于有心人来说,都是能看到的)             
2. 请求头(客户端告诉服务器的一些信息,头是固定的,值是不一样的)
    - 请求头名称:请求头值  
    - 常见的请求头:
        1. User-Agent: 浏览器告诉服务器,我访问你使用的浏览器版本信息
            - 可以在服务端获取该头的信息,解决浏览器的兼容性问题
        2. Referer:http://localhost/login.html
            - 告诉服务器,我(当前的请求)从哪里来?
                - 作用:
                    1. 防盗链:
                    2. 统计工作    
3. 请求空行
    - 空行,用于分割POST的请求头和请求体的
4. 请求体(正文)  
    - 封装POST请求消息的请求体的      
    - get方式的没有请求体的
    - post方式的请求体是带了一些参数`username=zhangsan`
### 响应消息数据格式:

登录

#### 请求和响应的过程
1. tomcat服务器会根据请求url的资源路径,创建对应的ServletDemo1对象
2. tomcat服务器,会创建request和response对象,request对象中封装请求消息数据
3. tomcat将request和response两个对象传递给service方法,并且调用service方法. 
4. 程序员(我们),可以通过request对象获取请求消息数据,通过通过response对象设置响应消息数据
5. 服务器在给浏览器做出响应之前,会从response对象中拿程序员

### request:
1. request对象和response对象的原理
    1. request和response对象是有服务器创建的,我们来使用它们
    2. request对象是来获取请求消息的response是来设置响应消息
2. request对象继承体系结构
```java
ServletRequest -- 接口    
    | 继承
HTTPServletRequest -- 接口
    | 实现
org.apache.catalina.connector.RequestFacade类(tomcat)
```
3. request:功能
    1. 获取请求消息数据
        1. 获取请求行数据
            - GET/day14/demo1?name=zhangsan HTTP/1.1
            - 方法:
                1. 获取请求方式:GET
                    - String getMethod();
                2. 获取虚拟目录:day14
                    - String getContextPath()
                3. 获取Servlet路径:/demo1
                    - Stirng getServletPath
                4. 获取get方式请求参数:name = zhangsan
                    - String getQueryString()
                5. 获取请求URI:/day14/demo1
                    - String getRequestURI()
                    - StringBuffer getRequestURL():`http://loaclhost/day14/demo1`
                    - url:统一资源定位符:`http://loaclhost/day14/demo1`(中华人民共和国)
                    - uri:统一资源标识符:`/day14/demo1`(共和国)
                    我现在要说的是,uri比url大,同意吧,就像上面的比喻
                6. 获取协议版本:HTTP/1.1
                    - String getProtocol()
                7. 获取客户机的IP地址
                    - String getRemoteAddr()
        2. 获取请求头数据
        3. 获取请求体数据
    2. 其他功能    