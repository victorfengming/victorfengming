---
title: "兄弟会_flask笔记02"
cover: "/img/lynk/1.jpg"
date:       2019-11-29
subtitle: "flask中蓝图定义和介绍"
tags:
	- Python
	- solution
	- web
	- flask
---












# 蓝图
### 什么是蓝图
用于实现单个应用的视图,模板,静态文件的集合
蓝图就是模块化处理的类
### 为什么要用蓝图


随着业务代码的增加,把所有的代码都写进一个程序文件中是非常不合适的

这不仅
### readme.md

微信小程序+flask 项目设计
图书借阅小程序
    图书列表
    图书详情
    图书查询
    图书录入
    图书借阅,归还
    个人中心,借阅信息

flask
    api 小程序api接口服务
    admin    后台管理
        图书管理
            添加
            查询
            修改
            下架
        借阅管理
            查看
            修改
        用户管理
            查看所有注册使用的用户,修改状态
        
        
查询到的数据json格式不能直接转换成为可用的类型

这可咋整        

我们需要处理一下才能转出去

## pymysql复习
1. 连接mysql数据库
2. 创建游标对象
3. 执行sql语句
4. 返回结果
5. 关闭连接

```python

# 导包
import pymysql
 
# 打开数据库连接
db = pymysql.connect("localhost","testuser","test123","TESTDB" )
 
# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()
 
# 使用 execute()  方法执行 SQL 查询 
cursor.execute("SELECT VERSION()")
 
# 使用 fetchone() 方法获取单条数据.
data = cursor.fetchone()
 
print ("Database version : %s " % data)
 
# 关闭数据库连接
db.close()
```

### 下面部分笔记没写


- 课时5：模型的返回问题分析15 分45 秒
- 课时6：封装pymysql36 分43 秒
- 课时7：书籍表设计20 分22 秒
- 课时8：书籍表单设计26 分39 秒
- 课时9：图书信息的添加30 分8 秒
- 课时10：图书管理的列表显示


详情参考:https://github.com/victorfengming/xdh_flask_project

初级程序员是为了实现功能,而中高级程序员是在优化性能

花生壳