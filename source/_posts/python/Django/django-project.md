---
title: "Django项目-慕学在线平台"
date:       2020-01-07
subtitle: "Web 开发激动人心且富于创造性"
tags:
	- Python
	- solution
	- web
	- django
---








开发环境：

　　　　python:  3.6.4

　　　　Django: 2.0.2

后台管理：xadmin

### 1.1.项目介绍
系统概括：
```
系统具有完整的用户登录注册以及找回密码功能，拥有完整个人中心。
个人中心: 修改头像，修改密码，修改邮箱，可以看到我的课程以及我的收藏。可以删除收藏，我的消息。
导航栏: 公开课，授课讲师，授课机构，全局搜索。
点击公开课–> 课程列表，排序-搜索。热门课程推荐，课程的分页。
点击课程–> 课程详情页中对课程进行收藏，取消收藏。富文本展示课程内容。
点击开始学习–> 课程的章节信息，课程的评论信息。课程资源的下载链接。
点击授课讲师–>授课讲师列表页，对讲师进行人气排序以及分页，右边有讲师排行榜。
点击讲师的详情页面–> 对讲师进行收藏和分享，以及讲师的全部课程。
导航栏: 授课机构有分页，排序筛选功能。
机构列表页右侧有快速提交我要学习的表单。
点击机构–> 左侧：机构首页,机构课程，机构介绍，机构讲师。
后台管理系统可以切换主题。左侧每一个功能都有列表显示, 增删改查，筛选功能。
课程列表页可以对不同字段进行排序。选择多条记录进行删除操作。
课程列表页：过滤器->选择字段范围等,搜索,导出csv，xml，json。
课程新增页面上传图片，富文本的编辑。时间选择，添加章节，添加课程资源。
日志记录：记录后台人员的操作
```

### 1.2.创建工程
#### 创建工程

```
django-admin startproject MxOnline
```


#### 创建四个app

```
python manage.py startapp users

python manage.py startapp course

python manage.py startapp organization

python manage.py startapp operation
```
然后分别设计每个app的models

### 2.1.users 用户
#### 自定义userProfile

 系统自动生成的user表如下
```
id: 主键, password 密码, last_login Django自动记录用户最后登录时间,。
is_superuser 表明用户是否是超级用户(后台管理会用到)。
username 用户名字段不要随便改动, email 邮箱,
is_staff 表示是否是员工(后台管理会用到)。
is_active 用户是否是激活状态, date_joined 注册时间。
```

users/models.py添加代码:
```python
# users/models.py

from django.db import models
from django.contrib.auth.models import AbstractUser

class UserProfile(AbstractUser):

    gender_choices = (
        ('male','男'),
        ('female','女')
    )

    nick_name = models.CharField('昵称',max_length=50,default='')
    birthday = models.DateField('生日',null=True,blank=True)
    gender = models.CharField('性别',max_length=10,choices=gender_choices,default='female')
    adress = models.CharField('地址',max_length=100,default='')
    mobile = models.CharField('手机号',max_length=11,null=True,blank=True)
    image = models.ImageField(upload_to='image/%Y%m',default='image/default.png',max_length=100)

    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username
```

然后做下面的一些设置

因为Image字段需要用到pillow所以需要安装该库

```
pip install pillow
```


### 注册app

```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'users'
]
```

### 重载AUTH_USER_MODEL
```
AUTH_USER_MODEL = 'users.UserProfile'
```

### 设计数据库为Mysql
```python
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'mxonline',        #数据库名字
        'USER': 'root',          #账号
        'PASSWORD': '123456',      #密码
        'HOST': '127.0.0.1',    #IP
        'PORT': '3306',                   #端口
    }
}
```

### init.py里面导入pymysql模块

# user/__init__.py
```
import pymysql
pymysql.install_as_MySQLdb()
```
### 迁移数据库
```
python manage.py makemigrations

python manage.py migrate
```

### 2.5.把四个app放到一个文件夹
创建package: apps

把之前的四个app全部剪切到apps包里面
** 不要选“Search for references”**
去掉searchfor的勾选。拖进去之后会报错，说找不到那些import的模块了。

解决方案：右键Mark为sourceRoot。根目录下找不到的，会去apps下搜索。

 但是这时候cmd下还是会报错。需要在settings设置

插入第0是希望它先搜索我们app下东西：
```python
import os
import sys
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,os.path.join(BASE_DIR,'apps'))
```
再运行就可以成功启动了


## 三、xadmin后台管理
### 3.1.xadmin的安装
#### django2.0的安装（源码安装方式）：
```
https://github.com/sshwsfc/xadmin/tree/django2
```
把zip文件放到pip目录下，运行下面命令安装：
```
pip install xadmin-django2
```

如果上面安装提示Runtime错误：

更换安装源（使用豆瓣源）
```
pip install -i https://pypi.douban.com/simple xadmin-django2
```

安装成功后，同时也安装了很多依赖的包。

### 3.2.xadmin的设置
 （1）新建Python Package "extra_apps",把源码xadmin文件夹放到extra_apps文件夹下面，此时目录结构如下：
（2）把extra_apps右键mark为Source Root并在settings中加入
```
sys.path.insert(0,os.path.join(BASE_DIR, 'extra_apps'))
```
（3）因为我们用源码的xadmin,所以要卸载之前安装的
卸载
```
(venv) D:\PycharmProjects\edu_platform_django>pip uninstall xadmin
Uninstalling xadmin-2.0.1:
  Would remove:
    d:\pycharmprojects\edu_platform_django\venv\lib\site-packages\xadmin-2.0.1-py3.7.egg-info
    d:\pycharmprojects\edu_platform_django\venv\lib\site-packages\xadmin\*
Proceed (y/n)? y
  Successfully uninstalled xadmin-2.0.1

```
(4)配置路由
把admin改成xadmin
```python
# urls.py

from django.urls import path

import xadmin

urlpatterns = [
    path('xadmin/', xadmin.site.urls),
]
```

(5)注册app

把下面两个app注册到settings.py的INSTALLED_APPS中
```python
'xadmin',
'crispy_forms'
```
(6)重新生成数据库
```
python manage.py makemigrations

python manage.py migrate
```
(7)设置成中文
```
LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False
```

(8)创建一个管理员用户
```
python manage.py createsuperuser
```
现在就可以运行了 
```
python manage.py runserver 
```

访问后台：http://127.0.0.1:8000/xadmin

 可以看到成功进入管理界面
 
### 3.3.users app的models注册
（1）在users下面创建adminx.py,代码如下：
```python
# users/adminx.py

import xadmin

from .models import EmailVerifyRecord

#xadmin中这里是继承object，不再是继承admin
class EmailVerifyRecordAdmin(object):
    pass

xadmin.site.register(EmailVerifyRecord,EmailVerifyRecordAdmin)
```

(2)完善功能，增加显示字段，搜索和过滤

修改users/adminx.py,代码如下：
```python
# users/adminx.py

import xadmin

from .models import EmailVerifyRecord

#xadmin中这里是继承object，不再是继承admin
class EmailVerifyRecordAdmin(object):
    # 显示的列
    list_display = ['code', 'email', 'send_type', 'send_time']
    # 搜索的字段，不要添加时间搜索
    search_fields = ['code', 'email', 'send_type']
    # 过滤
    list_filter = ['code', 'email', 'send_type', 'send_time']

xadmin.site.register(EmailVerifyRecord,EmailVerifyRecordAdmin)
```

### 3.5.xadmin的全局配置
将全局配置修改:

如左上角：django Xadmin。下面的我的公司
主题修改，app名称汉化，菜单收叠。
 使用Xadmin的主题功能。

把全站的配置放在users\adminx.py中:

1）添加主题功能