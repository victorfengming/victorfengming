---
title: "mooc后台管理系统设计"
date:       2020-01-14
subtitle: "一个完美主义的web框架"
tags:
	- Python
	- solution
	- web
	- django
---







# 摘 要
本设计采用Python中的Django框架实现Mooc后台管理界面设计,django是一个完整的开源web开源框架,使用起来能够快速的搭建你想要的网站,由于django自带后台管理系统,本设计中后台管理模板采用功能更加强大的Xadmin实现。数据库部分采用mysql5.7,由于django中有自带封装的数据库驱动,所以我们只需要关心框架中的models类的设计即可,只需要将数据表中的类型和关系建立好关系,后台管理系统基本上能够实现表的增删改查功能。  

关键词：Python;Django;Xadmin;Mysql;
    
# 前 言
 随着深度学习技术的发展及普及,在线教育领域的发展与人工智能的结合也
是愈发紧密。人工智能+教育便能够把人工智能技术渗透到教学的核心环节中,
模拟特技老师,从根本上改进学习的理念和方式,这是真正意义上的教育变革。


在线教育平台通过 VR、AR 结合 AI 算法与技术,构建识别和优化内容模型,
进而形成虚拟课堂效果,极大改善在线教育“学习体验、效果差”等顽疾；通过
机器视觉、语音语义等技术,自动化批改、归类作业,甚至可以建立一对一的在
线辅导,极大提升行业竞争力。


另外通过科技+教育的深度融合,能够对学生数据进行科学评估,精准发掘
每一个学生在学习上的差别,制定个性化学习方案,实现因材施教,赋予孩子未
来更多可能。


与此同时,AI 技术还可广泛用于学校的校园管理、区域的教育管理及教育
治理等相关领域,在优化企业运营策略、降低企业运营成本方面有着不可替代的
作用。


目前 VIPKID、哒哒英语、掌门 1 对 1、海风教育等众多 K12 在线教育企业,
都已开始布局“AI+教育”产业,随着头部企业涌入,未来教育行业的 AI 浪潮将
更加猛烈。而这个项目就是在这种背景下实施的,进行一次教育推广平台的建设。
# 1.基本储备
## 1.1 Python介绍
Python 是一种解释型、面向对象、动态数据类型的高级程序设计语言。
Python 由 Guido van Rossum 于 1989 年底发明,第一个公开发行版发行于 1991 年。像 Perl 语言一样, Python 源代码同样遵循 GPL(GNU General Public License) 协议。
Python具有以下明显的优点：
### （1）优雅体现在python的格式,比如缩进来确定代码块,可避免编程人员进行复杂的嵌套;
### （2）明确体现在解决问题的方法只有一种最优选项,而perl语言是每个问题有很多最优解,但不利于团队协作;
### (3)有强大的第三方库模块,需要实现复杂功能,只需要调用现有的库,可快速实现功能。20多年的发展,各种库都已经完备,比如:邮件库,爬虫库。
### (4)可跨平台移植,java有Java的虚拟机,python同样;
### (5)是一种面向对象的语言;
### (6)是一种可扩展的语言(与C,C++,Java结合)。
## 1.2 Django介绍
Django 是一个高级的 Python 网络框架,可以快速开发安全和可维护的网站。由经验丰富的开发者构建,Django负责处理网站开发中麻烦的部分,因此你可以专注于编写应用程序,而无需重新开发。
它是免费和开源的,有活跃繁荣的社区,丰富的文档,以及很多免费和付费的解决方案。
### （1）完备性：
Django遵循“功能完备”的理念,提供开发人员可能想要“开箱即用”的几乎所有功能。因为你需要的一切都是一个”产品“的一部分,它们都可以无缝结合在一起,遵循一致性设计原则,并且具有广泛和最新的文档。
### （2）通用性：
Django 可以（并已经）用于构建几乎任何类型的网站—从内容管理系统和维基,到社交网络和新闻网站。它可以与任何客户端框架一起工作,并且可以提供几乎任何格式（包括 HTML,Rss源,JSON,XML等）的内容。你正在阅读的网站就是基于Django。在内部,尽管它为几乎所有可能需要的功能（例如几个流行的数据库,模版引擎等）提供了选择,但是如果需要,它也可以扩展到使用其他组件。
### （3）安全性：
Django 帮助开发人员通过提供一个被设计为“做正确的事情”来自动保护网站的框架来避免许多常见的安全错误。例如,Django提供了一种安全的方式来管理用户账户和密码,避免了常见的错误,比如将session放在cookie中这种易受攻击的做法（取而代之的是cookies只包含一个密钥,实际数据存储在数据库中）或直接存储密码而不是密码哈希。
### （4）可扩展：
Django 使用基于组件的 “无共享” 架构 (架构的每一部分独立于其他架构,因此可以根据需要进行替换或更改). 在不用部分之间有明确的分隔意味着它可以通过在任何级别添加硬件来扩展服务：缓存服务器,数据库服务器或应用程序服务器。一些最繁忙的网站已经成功地缩放了Django,以满足他们的需求（例如Instagram和Disqus,仅举两个例子,可自行添加）。
### （5）可维护性：
Django 代码编写是遵照设计原则和模式,鼓励创建可维护和可重复使用的代码。特别是它使用了不要重复自己（DRY）原则,所以没有不必要的重复,减少了代码的数量。Django还将相关功能分组到可重用的“应用程序”中,并且在较低级别将相关代码分组或模块（ 模型视图控制器 (MVC)模式)。
### （6）灵活性：
Django 是用Python编写的,它在许多平台上运行。这意味着你不受任务特定的服务器平台的限制,并且可以在许多种类的Linux,Windows和Mac OsX 上运行应用程序。此外,Django得到许多网络托管提供商的好评,他们经常提供特定的基础设施和托管Django网站的文档。
## 1.3 Mysql介绍
MYSQL 是一个关系型数据库管理系统,由瑞典 MySQL AB 公司开发,目前属于 Oracle 公司。MySQL 使用的 SQL 语言是用于访问数据库的最常用的标准化语言。
由于 MySQL 数据库体积小、速度快、总体拥有成本低、开放源代码,其有着广泛的应用,一般中小型网站的开发都选择 MySQL 作为网站数据库。由于其社区版的性能卓越,因此搭配 PHP 和 Apache 服务器可组成良好的开发环境。
# 2.需求分析
建站包括前台功能系统和后台管理系统两大系统组成,分别由不同能力的人员实现,而前台功能系统是属于UI设计类的,后台管理系统是程序类的,因此本设计选择进行后台管理系统设计。
由于本设计是后台管理系统,所以需求主要是分为课程管理,认证管理和机构管理三个部分。实现基本功能是对于数据记录的增删改查,附加其它的功能,比如过滤器,排序,分页,筛选等功能。整体建站分析如下图2.1所示：
图2.1 整体建站分析
## 2.1 课程管理模块
课程管理模块涉及到关于本站的课程的管理操作,主要的操作包括：课程管理、课程资源管理、课程评论管理和轮播课程管理等。
根据以上简单分析,其需要编辑和实现的具体数据和变量如下表2.1所示：
表2.1 课程管理模块
分类	内容
Course(课程)	课程名、描述、详情、等级、学习时长等
Lesson(章节)	课程名、章节名、添加时间
Video(视频)	课程名、视频名、添加时间
CourseResource(课程资源)	课程名、名称、资源文件、添加时间
## 2.2 认证和授权管理模块
认证和授权管理模块是关于用户操作的模块,主要的操作包括：用户管理、组管理、权限管理、用户日志管理等。
根据以上简单分析,其需要编辑和实现的具体数据和变量如下表2.2所示：
表2.2 认证和授权管理模块
组别	分类	内容

User	UserProfile(用户信息)	昵称、生日、性别、地址
	EmailVerify(邮箱验证)	验证码、邮箱、发生类型、时间
	Banner(轮廓图)	标题,轮播图、url、顺序


Operation	UserAsk(用户咨询)	名字、手机号、课程名、时间
	CourseComment(用户评论)	用户、课程、评论、时间
	UserFavorite(用户收藏)	用户、数据ID、收藏类型、时间
	UserMessage(用户消息)	接收用户、消息内容、是否已读
	UserCourse(用户课程)	用户、课程、时间
## 2.3 机构管理模块
机构管理模块是关于课程发布机构的模块,由于网站上线后允许不同机构在网站上进行开课活动,因此需要进行机构管理,主要包括：课程机构、课程机构管理、讲轮播图管理等。
根据以上简单分析,其需要编辑和实现的具体数据和变量如下表2.3所示：

表2.3 机构管理模块
分类	内容
CourseOrg(课程机构)	名称、描述、点击数、收藏数、封面
CityDict(城市)	名字、描述、添加时间
Teacher(教师)	所属机构、教师名、工作年限、简介
# 3.Django模型设计
模型设计是整个项目的核心部分,直接决定了项目后续的可行性,这里我们分为四个app来进行设计,分别是users,course,organization,operation,如下图3.1所示：
 
图3.1 django整体模型设计
因此,需要拆成4个app来分别完成以上分析的设计功能,分别是users,course,organization,operation：

```python
python manage.py startapp users
python manage.py startapp course
python manage.py startapp organization
python manage.py startapp operation
```

## 3.1 users用户
系统会自动生成user表单,包括：
id 主键, password 密码, last_login Django自动记录用户最后登录间。
is_superuser 表明用户是否是超级用户(后台管理会用到)。
username 用户名字段不要随便改动, email 邮箱
is_staff 表示是否是员工(后台管理会用到)。
is_active 用户是否是激活状态, date_joined 注册时间。
表3.1 扩展表单
```
表名字	字段名	字段类型	字段长度(max_length)	是否为空	备注	其他
UserProfile
管理员	gender_choices	enum	('male','男'),
('female','女')		性别	
	nick_name	CharField	50		昵称	
	birthday	DateField		True	生日	
	gender	CharField	10		性别	choices=gender_choices
	address	CharField	100		地址	
	mobile	CharField	11	True	手机号	
	image	ImageField	100		图片	upload_to='image/%Y%m'g
	add_time	DateTimeField			添加时间	
	```
给出users/models.py代码如下：
```PYTHON

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
    gender = models.CharField('性别',max_length=10,\
choices=gender_choices,default='female')
    adress = models.CharField('地址',max_length=100,default='')
    mobile = models.CharField('手机号',max_length=11,\
null=True,blank=True)
    image = models.ImageField(upload_to='image/%Y%m',\
default='image/default.png',max_length=100)

    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.username
```
## 3.2 Course 课程
根据上述需求的分析,课程模型的设计如下表3.2所示：
表3.2 course需求表单
```
	degree_choices	enum	("cj", "初级"),
("zj", "中级"),
("gj", "高级")			课程难度
Course
课程	name	CharField	50		True	课程名
	description	CharField	300			课程描述
	introduce	UEditorField	600	''		课程简介
	degree	CharField	2	cj		难度
	image	ImageField	100			封面图
	tag	CharField	10	''		课程标签
	is_banner	BooleanField		False		是否轮播
	course_org	ForeignKey			null=True,blank=True,	所属机构
	category	ForeignKey				课程类别
	teacher	ForeignKey			null=True,blank=True,	讲师
	youneed_know	CharField	300	''		课程须知
	teacher_tell	CharField	300	''		老师告诉你
	learn_times	IntegerField		0		学习时长(分钟)
	students	IntegerField		0		学习人数
	fav_nums	IntegerField		0		收藏人数
	click_nums	IntegerField		0		点击数
	money	DecimalField				价格
	add_time	DateTimeField		datetime.now		添加时间
```

给出course/models.py代码如下：

```python

from datetime import datetime
from django.db import models

class Course(models.Model):
    		DEGREE_CHOICES = (
        		("cj", "初级"),
        		("zj", "中级"),
        		("gj", "高级")
   			 	)
    		name = models.CharField("课程名",max_length=50)
    		desc = models.CharField("课程描述",max_length=300)
    		detail = models.TextField("课程详情")
    		degree = models.CharField('难度',\
choices=DEGREE_CHOICES, max_length=2)
    		learn_times = models.IntegerField("学习时长(分钟数)",default=0)
    		students = models.IntegerField("学习人数",default=0)
    		fav_nums = models.IntegerField("收藏人数",default=0)
    		image = models.ImageField("封面图",upload_to="courses/%Y/%m",\
max_length=100)
    		click_nums = models.IntegerField("点击数",default=0)
    		add_time = models.DateTimeField("添加时间",default=datetime.now,)

    	class Meta:
        	verbose_name = "课程"
        	verbose_name_plural = verbose_name
    	def __str__(self):
        	return self.name
```
## 3.3 Organization机构
根据上述需求的分析,机构模型的设计如下表3.3所示：
表3.3 organzation机构需求表单
```
表名字	字段名	字段类型	字段长度(max_length)	默认值(default)	备注
CourseOrg
课程机构基本信息	name	CharField	50		机构名称
	desc	TextField			机构描述
	click_nums	IntegerField		0	点击数
	ORG_CHOICES	("pxjg", u"培训机构"),
("gx", u"高校"),
("gr", u"个人"),			
	category		choices=ORG_CHOICES		机构类别
	fav_nums	IntegerField		0	收藏数
	image	ImageField	100		封面图
	address	CharField	150		机构地址
	city	CharField			所在城市
	ordernum	CharField			订单数
	money	CharField			总钱数
	teacher_num	CharField			教师数
	add_time	DateTimeField		datetime.now	添加时间
```
给出organization/models.py代码如下：
```python
class CourseOrg(models.Model):
    	name = models.CharField('机构名称',max_length=50)
    	desc = models.TextField('机构描述')
    	click_nums = models.IntegerField('点击数',default=0)
    	fav_nums = models.IntegerField('收藏数',default=0)
    	image = models.ImageField('封面图',upload_to='org/%Y%m',max_length=100)
    	address = models.CharField('机构地址',max_length=150,)
city = models.ForeignKey(CityDict,\
verbose_name='所在城市',on_delete=models.CASCADE)
    	add_time = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name = '课程机构'
        verbose_name_plural = verbose_name
```
3.4 Operation 操作
根据上述需求的分析,操作模型的设计如下表3.4所示：
表3.4 operation需求表单
```
表名字	字段名	字段类型	默认值(default)	备注
UserCourse
用户学习的课程	user	CharField		用户
	course	CharField		课程
	add_time	DateTimeField	datetime.now	添加时间
	IS_FINISHED	((0,"未完成"),
(1,"已完成"))		
	is_finished	IntegerField	0	
```
给出operation/models.py代码如下：
```python
class UserCourse(models.Model):
user = models.ForeignKey(UserProfile,\
verbose_name='用户',on_delete=models.CASCADE)
course = models.ForeignKey(Course,verbose_name='课程',\
on_delete=models.CASCADE)
    	add_time = models.DateTimeField('添加时间', default=datetime.now)

    class Meta:
        verbose_name = '用户课程'
        verbose_name_plural = verbose_name
```

# 4.Xadmin后台管理
## 4.1 Xadmin的安装和设置
可以访问github开源仓库获取到源码进行安装,首先要获得django2.0的zip文件,放置到已经安装好pip工具的安装目录下,其源码访问链接为：
https://github.com/sshwsfc/xadmin/tree/django2
获取到源码后,解压到pip安装目录,然后运行下面命令安装：
pip install xadmin-django2
如果无法访问github开源仓库,可以更换安装源,比如说使用豆瓣源,命令如下：
pip install -i https://pypi.douban.com/simple xadmin-django2
安装完成后,同时也安装了很多依赖的包。
以下进行Xadmin的设置,进行简单分布操作如下：
（1）新建Python Package "extra_apps",把源码xadmin文件夹放到extra_apps文件夹下面,此时目录结构如下：
MxOnline>extra_apps>xadmin>_init_.py
（2）把extra_apps右键mark为Source Root并在settings中加入：
sys.path.insert(0,os.path.join(BASE_DIR, 'extra_apps'))
（3）因为我们用源码的xadmin,所以要卸载之前安装的：
pip uninstall xadmin
（4）配置路由,把admin改成xadmin,代码如下所示：
```python


# urls.py
from django.urls import path
import xadmin
urlpatterns = [
   				 path('xadmin/', xadmin.site.urls),
]
```

（5）注册app,把下面两个app注册到settings.py的INSTALLED_APPS中配置如下：
```
'xadmin',
'crispy_forms'
```

（6）重新生成数据库,运行如下：
```
python manage.py makemigrations
python manage.py migrate
```

（7）设置成中文,在加载的框架中修改如下内容为：
```
LANGUAGE_CODE = 'zh-hans'
TIME_ZONE = 'Asia/Shanghai'
USE_I18N = True
USE_L10N = True
USE_TZ = False
```

（8）创建一个管理员用户,并且启动框架就能进入管理界面,操作命令和管理界面如图4.1所示：
```
python manage.py createsuperuser
python manage.py runserver
```

 
图4.1 框架后台管理界面
## 4.2 模块添加和注册
首先在在users下面创建adminx.py,代码如下：
```python

# users/adminx.py

import xadmin

from .models import EmailVerifyRecord
#xadmin中这里是继承object,不再是继承admin
class EmailVerifyRecordAdmin(object):
    pass

xadmin.site.register(EmailVerifyRecord,EmailVerifyRecordAdmin)
```

创建以上管理后,开始进行根据上节django模型设计的分析内容,开始进行各种功能的创建和注册,以达到最初设计的要求。由于这部分内容比较庞大,在报告中不能一一进行注册的描述占用篇幅,因此只是对部分代表性的功能模块进行注册叙述。

比如将users中Banner也注册进去,则注册代码如下所示：
```python

class BannerAdmin(object):
    	list_display = ['title', 'image', 'url','index', 'add_time']
    	search_fields = ['title', 'image', 'url','index']
    	list_filter = ['title', 'image', 'url','index', 'add_time']

xadmin.site.register(Banner,BannerAdmin)
```

比如说将course注册进去,则注册代码如下所示：
```

# course/adminx.py
import xadmin
from .models import Course, Lesson, Video, CourseResource

class CourseAdmin(object):		#课程
    	list_display = [ 'name','desc','detail',\
'degree','learn_times','students']
    	search_fields = ['name', 'desc', 'detail',\
 'degree', 'students']
    	list_filter = [ 'name','desc','detail','degree',\
'learn_times','students']
class LessonAdmin(object):		 #章节
    	list_display = ['course', 'name', 'add_time']
    	search_fields = ['course', 'name']
    	#这里course__name是根据课程名称过滤
    	list_filter = ['course__name', 'name', 'add_time']
class VideoAdmin(object):		#视频
    	list_display = ['lesson', 'name', 'add_time']
    	search_fields = ['lesson', 'name']
    	list_filter = ['lesson', 'name', 'add_time']
class CourseResourceAdmin(object):	#课程资源
    	list_display = ['course', 'name', 'download', 'add_time']
    	search_fields = ['course', 'name', 'download']
    	list_filter = ['course__name', 'name', 'download', 'add_time']
```

将管理器与model进行注册关联
```python
xadmin.site.register(Course, CourseAdmin)
xadmin.site.register(Lesson, LessonAdmin)
xadmin.site.register(Video, VideoAdmin)
xadmin.site.register(CourseResource, CourseResourceAdmin)
```

将django模型和第二节模块功能设计的内容全部按照规则注册关联后,则整个项目初步完成,只需要进行后台管理操作进行增添删改,补充内容,再进行整体网站的安全检测就可以上线了,设计完成后的空白后台
如下图4.2所示：
 
图4.2 注册完全后的空白后台
# 5．内容填充
进行以上设计后,整体建站的设计基本完成,只需要将要发布的内容在管理后台进行添加发布即可,可对整个网站进行管理。参考mooc网的网上课程的模式,收集一些课程信息在管理后台进行发布,继续打造整个网站,最终结果如下图5.1所示：
 
图5.1 发布课程
# 参考文献
[1]  Django项目实例精解（第2版）作者:[美]安东尼奥米勒 清华大学出版社
[2]  Python Web开发实战 作者:董伟明著 出版社:电子工业出版社
[3]  MySQL 5.7从入门到精通（视频教学版）（第2版）张工厂 清华大学出版社
[4]  Python Django Web典型模块开发实战 作者:寇雪松 出版社:机械工业出版社
 

