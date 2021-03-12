---
title: "基于django和vue的xdh官网设计"
date:       2020-01-08
subtitle: "一个完美主义的web框架"
tags:
	- Python
	- solution
	- web
	- django
---



* content
{:toc}





# 前言
本项目是使用三段分离的设计
## 前台
使用materialize框架搭建的前台页面,后端使用的django写的接口
## 后台
使用Amazon UI 模板搭建的界面,管理各个部分的内容

## 项目环境
```
python3.7.2
django2.2.9
vue 
axios
jQuery
materialize
mysql
```
# 摘 要
本设计采用前后端分离的设计模式,前端通过vue的axios发送ajax请求来调用后端接口,实现页面的展示,后端使用Python中的django框架来访问数据库,并返回json数据。django是一个完整的开源web开源框架,使用起来能够快速的搭建你想要的网站。本设计中后台管理模板采用amazeUI页面的样式实现。数据库部分采用开源的mysql数据库,由于django操作数据库很方便,所以我们只需要关心框架中的models类的设计即可,只需要关心视图逻辑,后台管理系统即可实现基本的增删改查功能。  

关键词：Python;Vue;Django;ajax;Mysql;
 

 
# 1.	基础环境的简介
## 1.1  Python介绍。
Python是一种跨平台的计算机程序设计语言。是一种面向对象的动态类型语言,最初被设计用于编写自动化脚本(shell),随着版本的不断更新和语言新功能的添加,越来越多被用于独立的、大型项目的开发。
Python的设计哲学是“优雅”、“明确”、“简单”。因此,Perl语言中“总是有多种方法来做同一件事”的理念在Python开发者中通常是难以忍受的。Python开发者的哲学是“用一种方法,最好是只有一种方法来做一件事”。在设计Python语言时,如果面临多种选择,Python开发者一般会拒绝花俏的语法,而选择明确的没有或者很少有歧义的语法。由于这种设计观念的差异,Python源代码通常被认为比Perl具备更好的可读性,并且能够支撑大规模的软件开发。这些准则被称为Python格言。在Python解释器内运行import this可以获得完整的列表。Python是完全面向对象的语言。函数、模块、数字、字符串都是对象。并且完全支持继承、重载、派生、多继承,有益于增强源代码的复用性。 
## 1.2  Python 特点
### 1.易于学习
Python有相对较少的关键字,结构简单,学习起来更加简单。
### 2.易于阅读
Python代码定义的更清晰。
### 3.易于维护
Python的成功在于它的源代码是相当容易维护的。
### 4.一个广泛的标准库
Python的最大的优势之一是丰富的库,跨平台的,兼容很好。
### 5.互动模式

您可以从终端输入执行代码并获得结果的语言,互动的测试和调试代码片断。
### 6.可移植
基于其开放源代码的特性,Python已经被移植（也就是使其工作）到许多平台。
### 7.可扩展
如果你需要一段运行很快的关键代码,或者是想要编写一些不愿开放的算法,你可以使用C或C++完成那部分程序,然后从你的Python程序中调用。
### 8.数据库
Python提供所有主要的商业数据库的接口。
### 9.GUI编程
Python支持GUI可以创建和移植到许多系统调用。
### 10.可嵌入
 你可以将Python嵌入到C/C++程序,让你的程序的用户获得"脚本化"的能力。
## 1.3  Django介绍
Django 是一个高级的 Python 网络框架,可以快速开发安全和可维护的网站。由经验丰富的开发者构建,Django负责处理网站开发中麻烦的部分,因此你可以专注于编写应用程序,而无需重新开发。
它是免费和开源的,有活跃繁荣的社区,丰富的文档,以及很多免费和付费的解决方案。
### 1.3.1 完备性
Django遵循“功能完备”的理念,提供开发人员可能想要“开箱即用”的几乎所有功能。因为你需要的一切都是一个”产品“的一部分,它们都可以无缝结合在一起,遵循一致性设计原则,并且具有广泛和最新的文档.
### 1.3.2 通用性
Django 可以（并已经）用于构建几乎任何类型的网站—从内容管理系统和维基,到社交网络和新闻网站。它可以与任何客户端框架一起工作,并且可以提供几乎任何格式（包括 HTML,Rss源,JSON,XML等）的内容。你正在阅读的网站就是基于Django。

在内部,尽管它为几乎所有可能需要的功能（例如几个流行的数据库,模版引擎等）提供了选择,但是如果需要,它也可以扩展到使用其他组件。
### 1.3.3 安全性
Django 帮助开发人员通过提供一个被设计为“做正确的事情”来自动保护网站的框架来避免许多常见的安全错误。例如,Django提供了一种安全的方式来管理用户账户和密码,避免了常见的错误,比如将session放在cookie中这种易受攻击的做法（取而代之的是cookies只包含一个密钥,实际数据存储在数据库中）或直接存储密码而不是密码哈希。
### 1.3.4 可扩展
Django 使用基于组件的 “无共享” 架构 (架构的每一部分独立于其他架构,因此可以根据需要进行替换或更改). 在不用部分之间有明确的分隔意味着它可以通过在任何级别添加硬件来扩展服务：缓存服务器,数据库服务器或应用程序服务器。一些最繁忙的网站已经成功地缩放了Django,以满足他们的需求（例如Instagram和Disqus,仅举两个例子,可自行添加）。
### 1.3.5 可维护性
Django 代码编写是遵照设计原则和模式,鼓励创建可维护和可重复使用的代码。特别是它使用了不要重复自己（DRY）原则,所以没有不必要的重复,减少了代码的数量。Django还将相关功能分组到可重用的“应用程序”中,并且在较低级别将相关代码分组或模块（ 模型视图控制器 (MVC) 模式).
### 1.3.6 灵活性
Django 是用Python编写的,它在许多平台上运行。这意味着你不受任务特定的服务器平台的限制,并且可以在许多种类的Linux,Windows和Mac OsX 上运行应用程序。此外,Django得到许多网络托管提供商的好评,他们经常提供特定的基础设施和托管Django网站的文档。
## 1.4  Mysql介绍
MySQL 是一个关系型数据库管理系统,由瑞典 MySQL AB 公司开发,目前属于 Oracle 公司。
MySQL 使用的 SQL 语言是用于访问数据库的最常用的标准化语言。
由于 MySQL 数据库体积小、速度快、总体拥有成本低、开放源代码,其有着广泛的应用,一般中小型网站的开发都选择 MySQL 作为网站数据库。由于其社区版的性能卓越,因此搭配 PHP 和 Apache 服务器可组成良好的开发环境。
# 2.	需求分析
建站包括前台功能系统和后台管理系统两大系统组成,分别由不同能力的人 员实现,而前台功能系统是属于 UI 设计类的,后台管理系统是程序类的,因此 本设计选择进行后台管理系统设计。 由于本设计是后台管理系统,主要功能是对前台展示的页面进行增删改查的操作。
本站主要的功能是作为信息的展示和宣传,大体上分为4个页面：首页,课程页,教学特色页和学员风采页。主要功能如下图所示：
 
图2.1 XDH官网需求分析图
## 2.1 首页
首页主要分为以下几部分：
（1）轮播图
（2）兄弟会介绍
（3）兄弟会与传统就业班区别
（4）师资力量
（5）就业喜报
（6）学科介绍
## 2.2 课程介绍
	（1）培训课程,具体学科介绍
	（2）兄弟会具体学科及分级介绍
	（3）兄弟会解决了什么问题
	（4）重点突出兄弟会课程体系与传统培训体系的不同 
	（5）学习的苦VS生活的苦（不吃学习的苦就要吃生活的苦）
## 2.3 教学特色
	（1）办学理念-具有真实交付能力的程序员
	（2）项目驱动式学习-每阶段都有可锻炼的项目
	（3）企业级项目经理指导
	（4）真实的企业级商业项目全程开发
	（5）学习经验分享
	（6）企业文化培训（培养身心健康的程序员）
## 2.4 学员风采
	（1）学员采访视频
	（2）学员感言
	（3）个人博客
	（4）团建活动
	（5）我们的作品
# 3.	Django模型model类的设计
模型设计是整个项目的核心部分,直接决定了项目后续的可行性,这里我们分为两个 app 来进行设计,分别为api和bgapi,一个作为前台的接口,一个是进行后台管理的接口。

## 3.1 导入所需模块

```python
from django.db import models
from django.utils import timezone
```

## 3.2 所有轮播图


```python
class Banner(models.Model):
	img = models.TextField()
	page = models.CharField(max_length=20)
	link = models.CharField(max_length=100)
	is_del = models.IntegerField(default=0)
	join_date = models.DateTimeField(default=timezone.now)
```

## 3.3 工作信息表

```python
class JobInfo(models.Model):
	major = models.CharField(max_length=50,default="")	
    # 专业major 主修,专业 (专指大学)
	school = models.CharField(max_length=50)
	name = models.CharField(max_length=20)
	title = models.CharField(max_length=50)
	img = models.CharField(max_length=200)
	salary = models.CharField(max_length=20)
	date = models.DateField()
	is_del = models.IntegerField(default=0)
	join_date = models.DateTimeField(default=timezone.now)
```

## 3.4 学员感言

```python
class StudentSay(models.Model):
	img = models.CharField(max_length=50)	# 头像图片 avator是头像的意思
	name = models.CharField(max_length=20)
	title = models.CharField(max_length=255)
	content = models.TextField()
	is_del = models.IntegerField(default=0)
	join_date = models.DateTimeField(default=timezone.now)
```

## 3.5 技术社区内容

```python
class Community(models.Model):
	subject = models.CharField(max_length=50)
	type = models.CharField(max_length=50)
	content = models.TextField()
	link = models.TextField()
	is_del = models.IntegerField(default=0)
```

## 3.6 办学特色

```python
class Feature(models.Model):
	img = models.CharField(max_length=250)
	title = models.CharField(max_length=250)
	type = models.CharField(max_length=250)
	content = models.TextField()
	is_del = models.IntegerField(default=0)
	join_date = models.DateTimeField(default=timezone.now)
```

## 3.7 课程内容

```python
class Source(models.Model):
	text = models.CharField(max_length=150)
	link = models.CharField(max_length=250)
	is_del = models.IntegerField(default=0)
	join_date = models.DateTimeField(default=timezone.now)
```

## 3.8 个人博客

```python
class Blog(models.Model):
	name = models.CharField(max_length=20)
	link = models.CharField(max_length=100)
	img = models.CharField(max_length=255)
	title = models.CharField(max_length=255)
	description = models.TextField()
	is_del = models.IntegerField(default=0)
	join_date = models.DateTimeField(default=timezone.now)
```
## 3.9 用于登录token表
```python
class Token(models.Model):
	token_data = models.CharField(max_length=250)
	token_key = models.CharField(max_length=250)
	change_time = models.DateTimeField('最后修改日期',auto_now=True)
```
# 4.	view视图函数
视图函数是本项目的核心,主要负责收到前端ajax的请求,进行初步的处理,然后去数据库中进行增删改查操作,并返回JSON格式的数据给请求方。具体的代码可参考附录II
# 5.	接口文档
前后台分离后,他们两端之间的通讯是通过前台调用后台的接口实现的,所以一份清晰明了的接口文档会增加项目开发的效率,本项目的接口文档如附录中所示,其中包含了接口名称、 接口url、请求方法和请求参数。
# 6.	部署上线
## 6.1 域名
本项目上线前需要购买一个域名,并进行域名的解析,在域名解析前需要先进行网站的备案,只有备案后才能将域名绑定在相应的服务器上面
## 6.2 服务器
本项目的后台采用的是阿里云服务器,使用宝塔工具连接远程服务器,对服务器和数据库进行管理,宝塔Linux面板是提升运维效率的服务器管理软件,支持一键LAMP/LNMP/集群/监控/网站/FTP/数据库/JAVA等100多项服务器管理功能。
有20个人的专业团队研发及维护,经过200多个版本的迭代,功能全,少出错且足够安全,已获得全球百万用户认可安装。
## 6.3 数据库
本项目的数据库使用的是mysql5.7版本,由于mysql具有开源免费等优点,加上宝塔工具的控制,进行数据库的部署也十分的方便。
# 7.	项目总结
本项目通过采用前后端分离的方式来进行设计,能够分离减少各个项目部分之间的耦合性,一方面有利于将项目不同的部分分配给擅长不同领域的开发人员进行开发,另一方面,可以增加后期项目的可维护性。
整个项目用时一周,虽然其中有很多的漏洞,但是在做完整个项目后还是收获了很多的,这能够为以后的学习和工作增添一些经历和项目经验吧。
参考文献
[1]  Django项目实例精解（第2版）作者:[美]安东尼奥米勒 清华大学出版社
[2]  Python Web开发实战 作者:董伟明著 出版社:电子工业出版社
[3]  MySQL 5.7从入门到精通（视频教学版）（第2版）张工厂 清华大学出版社
[4]  Python Django Web典型模块开发实战 作者:寇雪松 出版社:机械工业出版社

# 附录
## 附录I 接口文档
```
后台	接口名称	 接口url	 请求方法	 请求参数
登录	用于管理员登录	/bgapi/login/	post请求	username
　	获取验证码	/bgapi/verification/		
博客	列表	/bgapi/blog/list/	 get请求	　
博客
社区资源	添加	/bgapi/blog/add/	post请求	name=file
	修改	/bgapi/blog/edit/	post请求	name=file
	删除	/bgapi/blog/del/	 get请求	?id=1
	列表	/bgapi/community/list/	 get请求	　
社区资源
轮播图	添加	/bgapi/community/add/	post请求	subject,
	修改	/bgapi/community/edit/	post请求	id,subject,
	删除	/bgapi/community/delete/	 get请求	id
	列表	/bgapi/banner/list/	 get请求	啥也不用
轮播图
学生视频	添加	/bgapi/banner/add/	post请求	name=file
	修改	/bgapi/banner/edit/	post请求	name=file
	删除	/bgapi/banner/del/	 get请求	id
	列表	/bgapi/assessvideo/list/	 get请求	　
学生视频
办学特色	添加	/bgapi/assessvideo/add/	post请求	video,img
	修改	/bgapi/assessvideo/edit/	post请求	video,img
	删除	/bgapi/assessvideo/delete/	 get请求	id
	列表	/bgapi/feature/list/	 get请求	　
办学特色
首页信息	添加	/bgapi/feature/add/	post请求	name=file
	修改	/bgapi/feature/edit/	post请求	name=file
	删除	/bgapi/feature/delete/	 get请求	id
	列表	/bgapi/mainpuretext/list/	 get请求	　
首页信息
首页学科	添加	/bgapi/mainpuretext/add/	post请求	title,content
	修改	/bgapi/mainpuretext/edit/	post请求	id,title,content
	删除	/bgapi/mainpuretext/delete/	 get请求	id
	列表	/bgapi/mainsubject/list/	 get请求	　
首页学科
阶段管理	添加	/bgapi/mainsubject/add/	post请求	name=file
	修改	/bgapi/mainsubject/edit/	post请求	name=file
	删除	/bgapi/mainsubject/delete/	 get请求	id
	列表	/bgapi/stage/list/	 get请求	　
阶段管理
学员感言	添加	/bgapi/stage/add/	post请求	name=file
	修改	/bgapi/stage/edit/	post请求	name=file
	删除	/bgapi/stage/delete/	 get请求	id
	列表	/bgapi/studentsay/list/	 get请求	　
学员感言
学员作品	添加	/bgapi/studentsay/add/	post请求	name=file
	修改	/bgapi/studentsay/edit/	post请求	name=file
	删除	/bgapi/studentsay/delete/	 get请求	id
	列表	/bgapi/studentworks/list/	 get请求	　
学员作品
工作信息	添加	/bgapi/studentworks/add/	post请求	name=file
	修改	/bgapi/studentworks/edit/	post请求	name=file
	删除	/bgapi/studentworks/delete/	 get请求	id
	列表	/bgapi/jobinfo/list/	 get请求	　
工作信息
教师信息	添加	/bgapi/jobinfo/add/	post请求	name=file
	修改	/bgapi/jobinfo/edit/	post请求	name=file
	删除	/bgapi/jobinfo/delete/	 get请求	id
	列表	/bgapi/teacher/list/	 get请求	　
教师信息
课程详情	添加	/bgapi/teacher/add/	post请求	name=file
	修改	/bgapi/teacher/edit/	post请求	name=file
	删除	/bgapi/teacher/delete/	 get请求	id
	列表	/bgapi/coursedetail/list/	 get请求	　
课程详情
活动管理	添加	/bgapi/coursedetail/add/	post请求	name=file
	修改	/bgapi/coursedetail/edit/	post请求	name=file
	删除	/bgapi/coursedetail/delete/	 get请求	id
	列表	/bgapi/activity/list/	 get请求	　
活动管理	添加	/bgapi/activity/add/	post请求	name=file
	修改	/bgapi/activity/edit/	post请求	name=file
	删除	/bgapi/activity/delete/	 get请求	id
```	
## 附录II:视图函数程序代码
课程管理视图函数
```python


from django.forms import model_to_dict
from django.shortcuts import render
from django.http import JsonResponse,HttpResponse

from api.models import CourseDetail,Token
from django.conf import settings


from .utils import add_data,edit_data,delete_data,list_data,check_token,check_md5

def list(request):
    if check_token(request):
        pass
    else:
        u_dict = {
            "status": "509",
            "info": "请先登录!",
        }
        return JsonResponse(u_dict)
    '''
    列表显示视图函数
    :param request:请求参数
    :return:返回json格式数据
    '''
    # # 验证是否登录
    # if check_token(request):
    #     # 如果成了
    #     pass
    # else:
    #     u_dict = {
    #         "status": "509",
    #         "info": "请先登录!",
    #     }
    #     return JsonResponse(u_dict)

    # 验证完了
    u_dict = list_data(CourseDetail)
    response = JsonResponse(u_dict)
    return response


def add(request):
    # 验证是否登录
    if check_md5(request):
        # 如果成了
        pass
    else:
        u_dict = {
            "status": "509",
            "info": "请先登录!",
        }
        return JsonResponse(u_dict)
    # 验证完了
    '''
    添加视图函数
    :param request:请求参数
    :return:返回json格式数据
    '''
    u_dict = add_data(request,CourseDetail)

    return JsonResponse(u_dict)

def edit(request):
    # 验证是否登录
    if check_md5(request):
        # 如果成了
        pass
    else:
        u_dict = {
            "status": "509",
            "info": "请先登录!",
        }
        return JsonResponse(u_dict)
    # 验证完了
    '''
    编辑视图函数
    :param request:请求参数
    :return:返回json格式数据
    '''
    u_dict = edit_data(request,CourseDetail)
    return JsonResponse(u_dict)


def delete(request):
    # 验证是否登录
    if check_token(request):
        # 如果成了
        pass
    else:
        u_dict = {
            "status": "509",
            "info": "请先登录!",
        }
        return JsonResponse(u_dict)
    # 验证完了
    '''
    删除视图函数
    :param request:请求参数
    :return:返回json格式数据
    '''
    u_dict = delete_data(request,CourseDetail)
    return JsonResponse(u_dict)
封装工具类
保存文件
def save_file(file):
    '''
    用于保存文件,返回保存文件的路径
    :param file:
    :return:
    '''
    if file:
        # 上传了头像
        import hashlib
        # 待加密信息(随机数)
        ran_str = str(random.randint(0, 9999999))
        # 创建md5对象
        hl = hashlib.md5()
        to_md5_str = str(time()) + ran_str
        # Tips
        # 此处必须声明encode
        # 若写法为hl.update(str)  报错为： Unicode-objects must be encoded before hashing
        hl.update(to_md5_str.encode(encoding='utf-8'))
        # 加密完的md5字符串
        md5_str = hl.hexdigest()
        # 文件扩展名
        file_extend_name = file.name.split('.').pop()
        # 拼接文件名
        filename = md5_str + '.' + file_extend_name

        with open(f'./media/' + filename, 'wb+') as f:
            f.write(file.read())
        # with open(f'./media/uploads/' + filename, 'wb+') as fp:
        #     fp.write(file.read())
        return filename
    else:
        return ""

删除文件
def del_file(path):
    '''
    用于删除文件,返回删没删成功
    :param path:
    :return:
    '''
    import os
    my_file = settings.BASE_DIR + settings.MEDIA_URL + path
    print(my_file)
    if os.path.exists(my_file):
        # 删除文件,可使用以下两种方法。
        os.remove(my_file)
        return True
    else:
        return False

成功返回数据
def success_response(u_dict):
    '''
    正确返回数据 过滤器
    :param u_dict: 返回的数据主体内容
    :return: 嵌套后的数据
    '''
    u_dict = {
        "status": "200",
        "info": "返回信息成功!",
        "data": u_dict
    }
    return u_dict

返回错误信息
def error_response(u_dict, err_info):
    '''
    返回错误json
    :param u_dict: json返回的主要内容
    :param err_info: 错误提示信息
    :return:
    '''
    u_dict = {
        "status": "500",
        "info": err_info,
        "data": u_dict
    }
    return u_dict

查询数据
def list_data(a_model_object):
    '''
    用于列表返回所有数据库数据
    :param a_model_object: 一个模型对象
    :return: 返回json数据格式的字典dict类型数据
    '''
    print("--------------------------开始列表视图函数---------------------------")
    u_dict = {}
    try:
        u_dict = all_data(a_model_object)

        # 嵌套一层
        u_dict = success_response(u_dict)
    except:
        u_dict = error_response(u_dict, "服务器错误,查询异常!")
    return u_dict
添加数据
def add_data(request, a_model_object):
    '''
    封装的添加方法
    :param request: http的请求request参数
    :param a_model_object: 一个模型对象
    :return: 返回json之前的字典类型的数据
    '''
    print("--------------------------开始添加视图函数---------------------------")
    # 定义返回数据
    u_dict = {

    }
    # 判断请求方式
    if (request.method == 'POST'):
        # try:
        # 开始处理图片
        # 1.获取表单内容
        data = request.POST.dict()
        print(data)

        # 要是有link,那就判断一下是不是真的link
        if "link" in data.keys():
            curr_link = data["link"]
            if check_link(curr_link):
                # 要是链接,啥也不干
                pass
            else:
                # 要是不行,那直接就给踢回去
                u_dict = {
                    "info": "链接类型不正确,请检查格式!",
                    "status": "506"
                }
                return u_dict


        # 先删除token
        data.pop("token")

        # 2. 获取表单中的文件
        file = request.FILES.get('file', None)
        print("file", file)
        # 3. 执行保存文件,并返回文件路径
        # save_file ---> 自定义函数
        path = save_file(file)
        # TODO 这里判断文件类型
        try:
            kind = filetype.guess(settings.BASE_DIR+settings.MEDIA_URL+path)
            print("猜出来的类型是:",kind)
            print("猜出来的类型extension是:",kind.extension)
            print("猜出来的类型mime是:",kind.mime)
            # TODO: write code.....
            # # 判断真的文件类型
            if kind.extension == "png" or kind.extension == "jpg":
                # 要是符合类型的,啥也不干
                pass
            else:
                # 要不是这俩类型
                # 直接我就返回,错误信息
                u_dict = {
                    "info": "图片类型不正确,请上传png或者jpg格式!",
                    "status": "505"
                }
                return u_dict
        except:
            u_dict = {
                "info": "图片类型不正确,请上传png或者jpg格式!",
                "status": "505"
            }
            return u_dict

        if not path:
            data.pop("file")
        # 构建img字段数据
        data["img"] = path
        # data.pop("file")
        # 保存数据
        a_model_object(**data).save()
        # 返回数据内容
        u_dict = {
            "info": "ok",
            "status": "200"
        }
        # except:
        #     u_dict = {
        #         "info": "error",
        #         "status": "500"
        #     }
    if (request.method == 'GET'):
        u_dict = {
            "info": "缺心眼啊,用浏览器访问!",
            "status": "666"
        }
    return u_dict
修改数据
def edit_data(request, a_model_object):
    '''
    用于编辑的封装函数
    :param request: 一个请求的参数
    :param a_model_object: 一个模型类对象
    :return: 返回提示信息的json格式字典dict
    '''
    print("--------------------------开始编辑视图函数---------------------------")
    u_dict = {

    }
    print("request.POST:", request.POST)
    print("request.FILES:", request.FILES)
    if (request.method == 'POST'):
        # 获取修改的id
        data = request.POST.dict()
        print(data)
        # 先删除token
        data.pop("token")

        # 要是有link,那就判断一下是不是真的link
        if "link" in data.keys():
            curr_link = data["link"]
            if check_link(curr_link):
                # 要是链接,啥也不干
                pass
            else:
                # 要是不行,那直接就给踢回去
                u_dict = {
                    "info": "链接类型不正确,请检查格式!",
                    "status": "506"
                }
                return u_dict

        # print(data.__dict__)
        id = data["id"]
        # 获取原来的对象
        obj = a_model_object.objects.get(id=id)
        dict = model_to_dict(obj)
        old_path = dict['img']
        # 2. 获取表单中的文件
        new_file = request.FILES.get('file', None)
        # 判断有没有新文件
        print("new_file:", new_file)
        # 要是有新文件的话
        if new_file:
            # print(new_file)
            # print(type(new_file))
            # print("走的有文件")
            # 删除旧文件
            del_file(old_path)
            # 保存新文件
            path = save_file(new_file)
            print("new_path:", path)
            # 构建img字段数据
            data["img"] = path
        else:
            # print("走的没文件")
            # print(new_file)
            # print(type(new_file))
            # 没有新文件
            data["img"] = old_path
            data.pop("file")

        obj = a_model_object.objects.filter(id=id)
        obj.update(**data)
        # else:
        #     u_dict = {
        #         "info": "删除文件失败!",
        #         "status": "501"
        #     }
        #     return JsonResponse(u_dict)
        # 成功状态码
        u_dict = {
            "info": "ok",
            "status": "200"
        }
    if (request.method == 'GET'):
        # 请求方式不对状态码
        u_dict = {
            "info": "no",
            "status": "666"
        }
    return u_dict
删除数据
def delete_data(request, a_model_object):
    '''
    用于删除封装的方法
    :param request: 一个请求参数
    :param a_model_object: 一个模型对象
    :return: 返回json类型的字典数据
    '''
    u_dict = {
        "info": "default",
        "status": "888"
    }
    print("--------------------------开始删除视图函数---------------------------")
    try:
        # 尝试删除
        id = request.GET.get("id")
        obj = a_model_object.objects.get(id=id)
        # 删除源文件
        # 获取文件路径
        dict = model_to_dict(obj)
        # 删除库
        obj.delete()
        # 原始路径
        old_path = dict['img']
        print("old_path:", old_path)
        # 执行删除
        del_file(old_path)

        u_dict = {
            "info": "ok",
            "status": "200"
        }
    except:
        u_dict = {
            "info": "error",
            "status": "500"
        }
    return u_dict

```