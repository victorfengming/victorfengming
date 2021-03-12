---
title: '各种解决方案汇总'
date:       2020-03-06
tags:
	- entertainment
	- solution
---
  




* content
{:toc}







# 链接汇总


### 20200305

---
- 博客园: [FastAPI框架快速构建高性能的api服务](https://www.jianshu.com/p/fbd1ba0a7ce7)
- 简书: [fastapi教程翻译(一)：了解FastAPI结构](https://www.jianshu.com/p/94710ed35b92)
- 简书: [HTTP request : Content-Type](https://www.jianshu.com/p/fbd1ba0a7ce7)
- 博客园: [四种常见的 POST 提交数据方式对应的content-type取值](https://www.cnblogs.com/wushifeng/p/6707248.html)
- 开源中国: [常用对照表](https://tool.oschina.net/commons)
- 菜鸟教程: [基于go的容器docker](https://www.runoob.com/docker/docker-tutorial.html)

---

- 博客园: [F5与Nginx的区别](https://www.cnblogs.com/sunyuhuan/p/7280085.html)
- 博客园: [一款属于自己的笔记本【vue+gin+elementUI前后端分离开发部署开源项目】](https://www.cnblogs.com/biningooginind/p/12388467.html)

### 20200306


---
- CSDN: [vue中监听input框获取焦点，失去焦点的问题](https://blog.csdn.net/LJFPHP/article/details/83545958)
- 简书: [绑定数据变量](https://www.jianshu.com/p/168530ded423)
- CSDN: [f5 负载均衡初识与配置](https://blog.csdn.net/u012153741/article/details/65442379)

### 20200307


---
- 博客园: [python开发F5相关功能](https://www.cnblogs.com/wangyingblock/p/11905220.html)
- CSDN: [F5（负载均衡）使用配置文档](https://blog.csdn.net/blackawhite/article/details/79644279)
- 官方文档: [F5-SDK](https://f5-sdk.readthedocs.io/en/latest/apidoc/modules.html)
- 官方文档: [F5 Python SDK](https://f5-sdk.readthedocs.io/en/latest/_modules/f5/bigip.html#ManagementRoot)

---
- CSDN: [浅谈服务器集群、负载均衡、与分布式](https://blog.csdn.net/nicewuranran/article/details/52860769)

### 20200316

---

- W3C: [HTTP 请求方法](https://www.w3cschool.cn/http/yerxcfmt.html)

---

# 需求分析
## 需求0
mssql中的login_sid 乱码问题

## 分析
数据库中就乱码了,需要验证在django后台存储时的问题,还是远端服务器中读取数据本身就是乱码了.


## 需求1
当用户输入完,id 的数据时,自动填充下面两个input输入框中对应的内容,由于是管理员操作界面,所以自动填充的内容还可以进行更改

## 实现步骤
0. 需要自动添加的vue-input中的内容[绑定数据变量](https://www.jianshu.com/p/168530ded423)
`v-bind`

0. Vue(js),[vue中监听input框获取焦点，失去焦点的问题](https://blog.csdn.net/LJFPHP/article/details/83545958)

0. 触发对应函数,发送ajax请求

0. 在请求中,访问对应查询接口(需要携带用户输入的参数)

0. django端处理,通过对数据库的查询进行结果的返回(json)

    如果查询失败,返回对应状态码
0. js(vue)端接收数据,解析数据
    - 成功,走第7条
    - 失败,pass

0. 赋值到之前定义好的绑定的数据变量中,

## 需求2
用户通过下拉框实现选择某条记录后,表单中下面两个对应的input中的内容自动填充,由于是管理员操作界面,所以自动填充的内容还可以进行更改



## 分析
0. 在需要自动填充的input框下[绑定数据变量](https://www.jianshu.com/p/168530ded423)
0. 表单加载成功后,自动去调用对应接口
0. django 处理,查询数据,并返回
0. js(vue)接收数据,并赋值到绑定的变量中
0. 自动添加的vue-input中的内容[绑定数据变量](https://www.jianshu.com/p/168530ded423)
`v-bind`

0. Vue(js)端添加监听鼠标失去焦点事件,[vue中监听input框获取焦点，失去焦点的问题](https://blog.csdn.net/LJFPHP/article/details/83545958)

0. 触发对应函数,发送ajax请求

0. 在请求中,访问对应查询接口(需要携带用户输入的参数)

0. django端处理,通过对数据库的查询进行结果的返回(json)

    如果查询失败,返回对应状态码

0. js(vue)端接收数据,解析数据
    - 成功,走第7条
    - 失败,pass

0. 赋值到之前定义好的绑定的数据变量中,

## 需求3
DataBase Oracle中的 Oracle Application  
查询搜索条件  role 中分为 owner 和 admin   
需要在加上这个列的表格后能够通过本列的条件进行搜索  

## 分析

在这个原有的功能中,加上一条判断

```python
role = request.GET.get("role")
# 然后在重新写一个SQL语句,加上where role = %s
```


## f5负载均衡
python配置f5

- 博客园: [python开发F5相关功能](https://www.cnblogs.com/wangyingblock/p/11905220.html)
- CSDN: [F5（负载均衡）使用配置文档](https://blog.csdn.net/blackawhite/article/details/79644279)
- 官方文档: [F5-SDK](https://f5-sdk.readthedocs.io/en/latest/apidoc/modules.html)
- 官方文档: [F5 Python SDK](https://f5-sdk.readthedocs.io/en/latest/_modules/f5/bigip.html#ManagementRoot)


## elk
[ELK(ElasticSearch, Logstash, Kibana)搭建实时日志分析平台](https://my.oschina.net/itblog/blog/547250/)

[ELK原理与介绍](https://www.cnblogs.com/aresxin/p/8035137.html)

## Apache_app分析

根据app_f5中参考

### 路由/视图函数
0. 获取信息并存储到数据库中
0. 显示主界面
    0. 增: post()方法
    0. 删: delete()方法
    0. 改: put()方法
    0. 查: get()方法


### 视图函数步骤
通过被调用的请求参数request获取前端页面中传递过来的参数

连接数据库(调用settings中数据库的常量)

拼接SQL语句(选择要查询出来的字段,加上需要的限制条件,对结果进行排序)

根据不同的方法中的不同功能对数据库进行响应的操作(主要的业业务逻辑)

获取执行结果

返回response信息(try...catch包裹)

如果有异常,返回对应的报错信息


### 目前的进度
新建一个git分支(branch),web_ioms_apache

在apps文件夹中,创建一个新的django-app

在settings配置文件中,加入install app 中

在app_apache中,创建文件urls.py

在IOMS文件夹中的总路由文件urls.py中配置字路由

写两个路由:获取信息,显示 主界面的

创建对应路由的类,并继承APIView

由于接口字段不确定,所以获取字段的部分不能写完整

封装了两个方法,写了一个显示主界面的一个类,其中有post(), delete(), put(), get(), 方法,对应着不同的逻辑,同一个接口路由,请求方式不同,调用的函数不同