---
title: "Django笔记02-进阶"
cover: "/img/lynk/30.jpg"
date:       2019-11-24
subtitle: "可以使Web开发工作愉快并且高效的Web开发框架"
tags:
	- Python
	- solution
	- web
	- django
	- standard
---






# 模型查询
### 查询集
在管理器上调用过滤器方法会返回查询集,查询集表示从数据库中获取的对象集合

查询集经过过滤器筛选后返回新的查询集，因此可以写成链式过滤

惰性执行：创建查询集不会带来任何数据库的访问，直到调用数据时，才会访问数据库

何时对查询集求值：迭代，序列化，与if合用

### 返回查询集的方法，称为过滤器
- all()
- filter()
- exclude()
- order_by()
- values()：一个对象构成一个字典，然后构成一个列表返回
写法：
```python
filter(键1=值1,键2=值2)
# 等价于
filter(键1=值1).filter(键2=值2)
```
- 返回单个值的方法
    - get()：返回单个满足条件的对象
        - 如果未找到会引发"模型类.DoesNotExist"异常
        - 如果多条被返回，会引发"模型类.MultipleObjectsReturned"异常
    - count()：返回当前查询的总条数
    - first()：返回第一个对象
    - last()：返回最后一个对象
    - exists()：判断查询集中是否有数据，如果有则返回True
### 限制查询集
- 查询集返回列表，可以使用下标的方式进行限制，等同于sql中的limit和offset子句
- 注意：不支持负数索引
- 使用下标后返回一个新的查询集，不会立即执行查询
- 如果获取一个对象，直接使用[0]，等同于[0:1].get()，但是如果没有数据，[0]引发IndexError异常，[0:1].get()引发DoesNotExist异常
    ```python
    #这会返回前5个对象 LIMIT 5
    Entry.objects.all()[:5]
    #这将返回第六个到第十个对象 OFFSET 5 LIMIT 5
    Entry.objects.all()[5:10]    
    ```
# 字段查询
- 实现where子名，作为方法filter()、exclude()、get()的参数
- 语法：属性名称__比较运算符=值
- 表示两个下划线，左侧是属性名称，右侧是比较类型
- 对于外键，使用“属性名_id”表示外键的原始值
- 转义：like语句中使用了%与，匹配数据中的%与，在过滤器中直接写，例如：filter(title__contains="%")=>where title like '%\%%'，表示查找标题中包含%的
# 用Q对象进行复杂查找
关键字参数查询 - 输入filter()等 - 是“AND”编辑在一起的。如果您需要执行更复杂的查询（例如，带有OR语句的查询），则可以使用。Qobjects

例如 查询or“或”的对象

```python
# Q对象 
from django.db.models import Q

ob = Goods.objects.filter(Q(id__contains=v)|Q(title__contains=v))
```

# 模型的关系
模型与模型之间的关系 或者理解为 表与表之间的关系
## 例如:班级与学员 文章与类型 新闻与新闻分类
## 有哪些关系?
### 一对一
- 就是一个表中数据与另外一个表中的数据相关联的,并且只与一条数据关联
- 例如: 你来XDL学习,哪个介绍老师,哪分配哪个班级,哪个讲师 反正总之你的各种信息
    - 学生信息: 姓名 性别 年龄 手机号 学历
    - 学员详情信息: 籍贯 住址 家属联系方式...
- 如何实现模型的关系:这就是一对一的关系,有一个学员信息,就有一个详细的信息 一个主表中有一个字段uid,用于存储另一个表的id,这样两个表格就一一对应起来了,这个用于联系两张表格的字段,我们一般称为`外键`,这个外键就是另一张表中的主键ID        - 外键有物理外键,和逻辑外键,我们这个随便写的就是逻辑外键,这个是通过业务逻辑写进去的,使用的时候推荐使用逻辑外键
- 因为物理外键会,不是物理外键,外键会产生表与表直接的强耦合,可能会在并发时造成死锁,会造成程序的阻塞
- 在数据库比较复杂的时候,或者一些大型的网站,绝对不允许使用外键
-  在[58到家MySQL军规升级版](https://victorfengming.gitee.io/blog/mysql-58-rules/)中说过:[禁止使用外键，如果要保证完整性，应由应用程式实现](https://victorfengming.gitee.io/blog/mysql-58-rules/#%E7%A6%81%E6%AD%A2%E4%BD%BF%E7%94%A8%E5%A4%96%E9%94%AE%E5%A6%82%E6%9E%9C%E8%A6%81%E4%BF%9D%E8%AF%81%E5%AE%8C%E6%95%B4%E6%80%A7%E5%BA%94%E7%94%B1%E5%BA%94%E7%94%A8%E7%A8%8B%E5%BC%8F%E5%AE%9E%E7%8E%B0)
- 在[58到家MySQL军规升级版](https://victorfengming.gitee.io/blog/mysql-58-rules/)中提到: [禁止使用select *，只获取必要字段](https://victorfengming.gitee.io/blog/mysql-58-rules/#%E7%A6%81%E6%AD%A2%E4%BD%BF%E7%94%A8select-%E5%8F%AA%E8%8E%B7%E5%8F%96%E5%BF%85%E8%A6%81%E5%AD%97%E6%AE%B5) 
```python
# 在用户详情表中，关联用户表，让两个表的数据产生联系
# 第一个参数：是被关联的模型名称
# 第二个参数：当user用户表中的一条数据被删除的时候
# ，与之对应的详情表数据也会被删除,
# 说白了就是同步记录删除学生了还要啥学生详情啊
uid = models.OneToOneField(Stu, on_delete=models.CASCADE)
# 这里在Stu不用引号,要是换了顺序,
# 就是Stu在下面了,就要加上引号了,不然找不到
# 因为咱们python并没有类或者函数的欲仙加载,毕竟是脚本语言嘛,还想咋地!
# 那你还能在类定义之前去实例化对象啊, 你不得先定义在用啊
```


```python
# 创建视图函数 演示一对一模型关系的操作
def onetoone(request):
   # 添加
    # 创建学员信息
    ob = Stu(sname='李四',age=24)
    ob.save()
    # 添加学员详情信息
    obi = StuInfo()
    obi.jiguan = "山西"
    obi.xueli = '大专'
    # 注意在给外键添加数据时,
    # 只能选择对象,不能设为对象的id
    obi.uid = ob
    obi.save()

    # 查询
    ob = Stu.objects.first()
    print(ob.sname)
    # 与之关联的模型类全小写就可以了
    # ,另一个对象就出来了
    print(ob.stuinfo.xueli)
    # 通过学员 获取学员详情对象
    print(ob.stuinfo.jiguan)

    # 通过学员详情,获取学员信息
    ob = StuInfo.objects.last()
    print(ob.jiguan)
    print(ob.uid)
    print(ob.uid.sname)
    print(ob.uid.age)
    # 有外键的一方使用外键
    # 没有外键的一方,使用类名小写

    # 删除
    # 删除一个表中的记录,应该同步都删除
    ob = StuInfo.objects.last()
    ob.delete()


    return HttpResponse('演示 一对一模型关系的操作')
```
### 一对多
ForeignKey 一对多
举例
一个班级有多个学员,多个学员都在一个班级
一个表中的数据对应另外一个表中的多条数据,
一张表中多个数据对应另外一张表中的一条数据

### 数据库只有两种操作
读 查询(方便但是慢)
写 添加,删除,修改    (不加索引就是最快的,没有任何提了螳螂的东西) 

### 多对多   
一张表中的数据在另一张表中有多个,另一张表中也是有多个在这张表中

比如,一个班级有多个老师授课,一个老师去多个班级授课 

有一本书,标签,一本书有多个标签,一个标签下面有多本书

书籍:

|id|bname|
|---|---|
|1|<<Python3.7从零开始学>>|
|2|<<细说PHP>>|
|3|<<细说Python数据分析>>|
    
标签:

|id|tname|
|---|---|
|1|Python|
|2|PHP|
|3|编程语言|
|4|数据分析|

书籍和标签关系

|bookid|tagid|
|---|---|
|1|1|
|1|3|
|2|2|
|2|3|
|3|1|
|3|3|
|3|4|


Python PHP 编程语言 数据分析    

### 视图中的请求方式
请求报文,响应报文

一键多值情况

### 状态保持
HTTP协议是无状态的：每次请求都是一次新的请求，不会记得之前通信的状态
客户端与服务器端的一次通信，就是一次会话
实现状态保持的方式：在客户端或服务器端存储与会话有关的数据
存储方式包括cookie、session，会话一般指session对象
使用cookie，所有数据存储在客户端，注意不要存储敏感信息
推荐使用sesison方式，所有数据存储在服务器端，在客户端cookie中存储session_id
状态保持的目的是在一段时间内跟踪请求者的状态，可以实现跨页面访问当前请求者的数据
注意：不同的请求者之间不会共享这个数据，与请求者一一对应

### cookie和session
http请求是无状态的请求

请求中并不清楚你上一次请求的情况

在很多情况下需要记住用户的一些状态,

这个时候就需要使用回话跟踪技术,回话控制

#### cookie
是在浏览器中进行数据的保存,并且在每次请求时,会携带保存的数据去访问服务器
    
js是可以获取cookie信息的
    
#### session
sessionid是把数据存在服务端(文件,数据库,内存)
并且声称一个sessionid记录到cookie中,
session依赖cookie,这样更加的安全
cookie只能存储字符串类型的数据,session在python中的啥格式都行
    
