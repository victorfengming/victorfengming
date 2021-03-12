---
title: "兄弟会_flask笔记01"
date:       2019-11-28
subtitle: "flask项目搭建 基本使用"
tags:
	- Python
	- solution
	- web
	- flask
---





* content
{:toc}






# 课程介绍
### 前言
我们用flask是写后台的

如果你看一个小程序很好看,你可以把他爬下来,或者通过技术的手段

工具,实现反编译

---

举例:"网易严选" 网页端 pc端 app 甚至微信小程序

你的手机里面的程序都会产生文件,所以你才会越用越卡

node.js开发的一个工具,能反编译成一个差不多的东西

这个能快到什么程度呢,一个比较熟练的人,一天之内包括分编译,能把这个程序调试的差不多

比如这个:[牛刀云](http://www.newdao.net/)包括[猪八戒网](https://shenyang.zbj.com/),都行

我们要做的就是使用flask做后台给小程序提供接口,小程序任意类型的都能做

# 虚拟环境
### 在这之前我们需要学一个虚拟环境：
VirtualEnv用于在一台机器上创建多个独立的Python虚拟运行环境，多个Python环境相互独立，互不影响，它能够：

- 在没有权限的情况下安装新套件
- 不同应用可以使用不同的套件版本
- 套件升级不影响其他应用

详情在这里:[Python中的虚拟环境-virtualenv](https://victorfengming.gitee.io/2019/11/18/python-venv/)

其实这个虚拟环境也有缺点,就是他只能用于python,我们可以在了解一个叫做
docker这个东东

docker就相当于硬件级的环境,这个可以快速的部署,它适合在大型的集群的上面才能显示他的优势

### 在python3中还有一种方法
安装python3的虚拟环境包
```shell
sudo apt-get install python3-venv
```
创建虚拟环境
```shell
python3 -m venv v1
```

使用虚拟环境(激活)
```shell
source v1/bin/activate
```

导出虚拟环境记录文件
```shell
pip freeze > requirements.txt
```
我又傻了,以后venv这个文件夹都不用往github上面推了

直接推一个`requirements.txt`文件就够了,小到没朋友

# Flask介绍
Flask翻译,烧瓶,不是辣椒奥,这里要强调一下

犀牛角形状的水壶

---

之所以选中Python（大蟒蛇的意思）作为该编程语言的名字，是取自英国20世纪70年代首播的电视喜剧《蒙提.派森干的飞行马戏团》（Monty Python's Flying Circus）

吉多曾经参与过ABC语言的设计,不是说人家圣诞节真的没事儿才开发的python

不仅就你知道的C语言,还有A ,B语言,C++,C--,C#,这个ABC是一个语言

所以python开发参考了很多语言的特点,结合自己的经验

90年正式诞生第一个版本,2.7,和3.4两个比较大的版本


### 概念
Flask是基于Werkzeug，Jinja 2和良好意图的基于Python的微框架

微框架中的“微”意味着 Flask 旨在保持核心简单而易于扩展。

Flask 不会替你做出太多决策——比如使用何种数据库。

而那些 Flask 所选择的——比如使用何种模板引擎——则很容易替换。

除此之外的一切都由可由你掌握。如此，Flask 可以与您珠联璧合

Flask 也许是“微小”的，但它已准备好在需求**繁杂**的生产环境中投入使用

---

官网地址 Flask http://flask.pocoo.org/


### 起步

第一个flask程序如下:
```python
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run()

```

简单吧!连上空格都算上,一共就不到10行代码,就能helloworld


### 解析

`__name__`是一个魔术变量
 
 
一个工具:POSTMan

它能够默认任何请求方式


### Pymysql
这个玩意是python连接mysql数据库进行操作的工具api

### SQLAlchemy

用于管理数据库的工具

这玩意能操作各种数据库,跟pymysql比起来更高一级

如果要连接mysql数据库,还是需要调pymysql的

它是python编程语言下的一款开源软件,提供了SQL工具包以及对象关系映射(ORM)工具

SQLAlchemy


### 使用Flask-SQLAlchemy管理数据库

Flask-SQLAlchem这玩意是在flask框架中使用SQLAlchemy一个工具包,产品,它依赖SQLAlchemy

Flask-SQLAlchemy 是一个 Flask 扩展，简化了在 Flask 程序中使用 SQLAlchemy 的操作。

SQLAlchemy 是一个很强大的关系型数据库框架，支持多种数据库后台。

SQLAlchemy 提 供了高层 ORM，也提供了使用数据库原生 SQL 的低层功能
 
 
 
### 模型操作(连接数据库)
在mysql数据库中创建一个数据库名为`myapp`

创建一个python文件`models.py`内容如下

```python
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:@127.0.0.1:3306/myapp"
# 如果设置成 True (默认情况)，Flask-SQLAlchemy 将会追踪对象的修改并且发送信号。
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

# 绑定app至SQLAlchemy
db = SQLAlchemy(app)



#会员模型
class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(100),unique=True)
    pwd= db.Column(db.String(100))
    email= db.Column(db.String(100))
    phone= db.Column(db.String(11))
    info= db.Column(db.Text)
    face = db.Column(db.String(255))
    addtime = db.Column(db.DateTime,default=datetime.now)

    # def __repr__(self):
    # return '<User %r>' % self.username

if __name__ == "__main__":
    db.create_all()
```
 
 
在第5行那里需要加上`+pymysql`,不然就报错,因为没有`mysqldb`

但是你还不能装`mysqldb`,因为你装不上,都改名字了这个包

这里需要格外的注意,假装画一个重点符号

然后直接用python执行这个models.py脚本,你就会神奇的发现

你的`myapp`数据库中的多了一张表,里面字段都整好了,完美!

### 数据库的增删改查
在创建一个数据库,专门用来操作的
```python
class Stu(db.Model):
    __tablename__ = 'Stu'

    id = db.Column(db.Integer,primary_key=True)
    sname = db.Column(db.String(10))
    email = db.Column(db.String(50))
    age = db.Column(db.Integer)


if __name__ == "__main__":
    # 创建数据表
    db.create_all()
```
#### 先手动在数据中整一条数据试试查询

```python
'''
查询数据
'''
res = User.query.all()
print(res)
print('-'*80)
print(dir(res[0]))
print('-'*80)
# print(type(res[0]).__dict__)

```

#### 增加

向数据库插入数据分为三个步骤:

- 创建 Python 对象
- 把它添加到会话
- 提交会话

```python
'''
数据的添加
'''
# 1先创建一个模型对象
s = Stu()
s.sname = '战三'
s.email = 'zssag@163.com'
s.age = 18
# db 是之前的实例化的对象
# 这里的session不是session仅仅表示会话的意思
db.session.add(s)
# 你要知道,这不是一个人开发的啊
# 那你学django的时候是那样用的,这回这样用,
# 那就这样了,用人家的东西就得挺着
# 那要完全都一样全写一个样,就用一个框架不就oK了么
# 这个要求是SQLAlchemy要求的,
# 这个时候还可以捕获异常,db.rollback还可以回滚,也就是说自带了事务处理了
db.session.commit()

# 2数据添加.
# 这个数据实际上应该从表单中添加过来的,
# 所以我们假装构建一个这样的数据
data = {'sname':'lisi','email':'lsasdfghafsgh@qq.com','age':21}
# **拆参数,这个经常用,得理解
s = Stu(**data)
db.session.add(s)
db.session.commit()
```

### 删除
删除记录是十分类似的，使用 delete() 代替 add():
```python

'''
先获取对象
'''
ob = Stu.query.get(2)
db.session.delete(ob)
db.session.commit()
```    

### 修改
    
```python
'''
先找到要改的
'''
ob = Stu.query.get(1)
ob.sname = '张三'
db.session.add(ob)
db.session.commit()
```    


### 查询数据
那么我们怎么从数据库中查询数据？为此，Flask-SQLAlchemy 在您的 Model 类上提供了 query 属性。

当您访问它时，您会得到一个新的所有记录的查询对象。

在使用 all() 或者 first() 发起查询之前可以使用方法 filter() 来过滤记录。

如果您想要用主键查询的话，也可以使用 get()。

---

下面的查询假设数据库中有如下条目:id

<table>
<thead>
<tr>
<th style="text-align:left">id</th>
<th style="text-align:left">username</th>
<th style="text-align:left">email</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align:left">1</td>
<td style="text-align:left">admin</td>
<td style="text-align:left"><a href="mailto:admin%40example.com" target="_blank">admin@example.com</a></td>
</tr>
<tr>
<td style="text-align:left">2</td>
<td style="text-align:left">peter</td>
<td style="text-align:left"><a href="mailto:peter%40example.org" target="_blank">peter@example.org</a></td>
</tr>
<tr>
<td style="text-align:left">3</td>
<td style="text-align:left">guest</td>
<td style="text-align:left"><a href="mailto:guest%40example.com" target="_blank">guest@example.com</a></td>
</tr>
</tbody>
</table>



#### 通过用户名查询用户:
```shell
>>> peter = User.query.filter_by(username='peter').first()
>>> peter.id
1
>>> peter.email
u'peter@example.org'
```
#### 同上但是查询一个不存在的用户名返回None:
```shell
>>> missing = User.query.filter_by(username='missing').first()
>>> missing is None
True
```
#### 使用更复杂的表达式查询一些用户:
```shell
>>> User.query.filter(User.email.endswith('@example.com')).all()
[<User u'admin'>, <User u'guest'>]
```
#### 按某种规则对用户排序:
```shell
>>> User.query.order_by(User.username)
[<User u'admin'>, <User u'guest'>, <User u'peter'>]
```
#### 限制返回用户的数量:
```shell
>>> User.query.limit(1).all()
[<User u'admin'>]
```
#### 用主键查询用户:
```shell
>>> User.query.get(1)
<User u'admin'>
```


### 在视图中查询
当您编写 Flask 视图函数，对于不存在的条目返回一个 404 错误是非常方便的。因为这是一个很常见的问题，Flask-SQLAlchemy 为了解决这个问题提供了一个帮助函数。

---

可以使用get_or_404()来代替get()，使用first_or_404()来代替first()。这样会抛出一个 404 错误，而不是返回None:
```python
@app.route('/user/<username>')
def show_user(username):
    user = User.query.filter_by(username=username).first_or_404()
    return render_template('show_user.html', user=user)
```