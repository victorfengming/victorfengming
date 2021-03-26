---
title: "CentOS7安装Graphite"
date: 2021-03-25 15:55:17
cover: "/img/lynk/91.jpg"
author: "victor"
tags:
    - graphite
    - centos
---


## Graphite简介

Graphite是一个Python编写的企业级开源监控工具，采用django框架，用来收集服务器所有的即时状态，用户请求信息，Memcached命中率,RabbitMQ消息服务器的状态，操作系统的负载状态。

Graphite服务器大约每分钟需要有4800次的跟新操作，它采用简单的文本协议和绘图功能，可以方便的使用在任何操作系统上。

Graphite 自己本身并不收集具体的数据，这些数据收集的具体工作通常由第三方工具或插件完成（如 Ganglia, collectd, statsd, Collectl 等)。

#### 简单来说，Graphite主要做两件事情：

- 实时监控第三方工具传来的数据
- 根据数据绘制图形

#### Graphite包含3个组件，carbon，whisper，graphite webapp其中：

- carbon - 用于监控数据的 Twisted 守护进程
- whisper - 用于存放和操作数据的库
- graphite webapp - 用于绘制图形的Django webapp

关于Graphite的详细官方文档可以参考[Graphite Documentation](http://graphite.readthedocs.io/en/latest/)

## Graphite安装

我安装的环境是`CentOS 7`、`python 2.7.5`

#### 1、修改yum源配置：
```bash
yum install wget

mv /etc/yum.repos.d/CentOS-Base.repo /etc/yum.repos.d/CentOS-Base.repo.backup

cd /etc/yum.repos.d/

wget http://mirrors.163.com/.help/CentOS6-Base-163.repo

yum makecache

yum -y update

```
#### 2、安装pip、carbon 和whisper
```bash
yum -y install epel-release   #安装epel扩展源pip才能安装
yum -y install python-pip
yum -y install python-devel
yum -y install gcc
yum -y install unzip
pip install carbon
pip install whisper
```

#### 3、安装graphite-web
```bash
yum -y install libffi-devel zlib-devel openssl-devel install uwsgi-plugin-python
pip install graphite-web
pip uninstall django
pip install django==1.8
```

4、修改配置文件
```bash
cd /opt/graphite/conf/
ls #查看所有文件，拷贝去除example
cp aggregation-rules.conf.example aggregation-rules.conf
cp blacklist.conf.example blacklist.conf
cp carbon.amqp.conf.example carbon.amqp.conf
cp carbon.conf.example carbon.conf
cp dashboard.conf.example dashboard.conf
cp graphite.wsgi.example graphite.wsgi
cp graphTemplates.conf.example graphTemplates.conf
cp relay-rules.conf.example relay-rules.conf
cp rewrite-rules.conf.example rewrite-rules.conf
cp storage-aggregation.conf.example storage-aggregation.conf
cp storage-schemas.conf.example storage-schemas.conf
cp whitelist.conf.example whitelist.conf
cd /opt/graphite/webapp/graphite
cp local_settings.py.example local_settings.py
cd ../
mv content static
vi uwsgi.ini
```

拷贝如下代码进去，保存退出

```bash
[uwsgi]
# Django-related settings

socket = :8000

buffer-size = 40000

plugins=python
# the base directory (full path)

chdir = /opt/graphite/webapp

# Django s wsgi file

module = graphite.wsgi

# process-related settings

# master

master = true

# maximum number of worker processes

processes = 1

# ... with appropriate permissions - may be needed

# chmod-socket = 664

# clear environment on exit

vacuum = true

```

#### 5、安装uwsgi和nginx
```
yum -y install uwsgi
cd /home/admin/
wget http://nginx.org/download/nginx-1.4.7.tar.gz
tar zxvf nginx-1.4.7.tar.gz
cd nginx-1.4.7
./configure --with-openssl=/usr/include/openssl
vi objs/Makefile   #把第3行的“ -Werror ” 删除，保存，关闭
make
make install
vi /usr/local/nginx/conf/nginx.conf
```


拷贝如下代码进去，保存退出


```bash
user  root;

worker_processes  1;

#error_log  logs/error.log;

#error_log  logs/error.log  notice;

#error_log  logs/error.log  info;

#pid        logs/nginx.pid;

events {

    worker_connections  1024;

}



http {

    include       mime.types;

    default_type  application/octet-stream;

    sendfile        on;

    keepalive_timeout  65;

    server {

        listen       8001;

        server_name  localhost;

        charset     utf-8;

        #access_log  logs/host.access.log  main;

        location / {

            include uwsgi_params;

            uwsgi_pass 127.0.0.1:8000;

             uwsgi_read_timeout 2;

        }

        location /static {

            root  /opt/graphite/webapp;

        }

    }

}
```



#### 6、在网站上找到项目，创建`manage.py`，好进行数据库的操作，和测试显示项目中的问题


```bash
cd /opt/graphite/webapp/
vi manage.py 
```


拷贝如下代码进去，保存退出


```python
#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
     os.environ.setdefault("DJANGO_SETTINGS_MODULE", "graphite.settings")
     from django.core.management import execute_from_command_line
     execute_from_command_line(sys.argv)

```

```bash
pip install scandir
python manage.py migrate
vi /opt/graphite/webapp/graphite/local_settings.py
#取消SECRET_KEY、TIME_ZONE注释，并且修改值：
SECRET_KEY = '@2o8&38gcsb(p*o*dy(fmh!_3-30a1qwq$sadb+6vk243%wj0#'
TIME_ZONE = 'Asia/Shanghai'
#保存退出
```

#### 7、通过manage.py shell修改网站登录的用户名和密码

```bash
python manage.py shell
>>> from django.contrib.auth.models import User
>>> user_list=[x for x in User.objects.all()]
>>> print user_list
#如果user_list不为空
>>>user=user_list[0]
>>>user.username='admin'
>>>user.set_password='123123'
>>>user.save()
#如果user_list为空
>>>quit()
python manage.py createsuperuser
#根据提示创建你的用户
Username (leave blank to use 'root'): admin
Email address: 123123@qq.com
Password:     #输入后不会显示，我输的123123
Password (again):     #输入后不会显示
```


#### 8、启动carbon，carbon会在默认的2003端口接收数据。

```bash
python /opt/graphite/bin/carbon-cache.py start
uwsgi --ini /opt/graphite/webapp/uwsgi.ini 
#再新建一个窗口，启动nginx，或者让uwsgi后台运行，建议测试的时候新建窗口，错误好捕获。启动nginx之前，先关闭防火墙或者开启8001端口。我做测试，就关闭防火墙了。
systemctl disable firewalld #停用防火墙
systemctl stop firewalld    #禁止防火墙
/usr/local/nginx/sbin/nginx           #启动nginx
/usr/local/nginx/sbin/nginx -s reload   #重启nginx
```


#### 9、浏览

网址http://127.0.0.1:8001，出现如下画面，安装成功，如果失败，注意查看nginx的错误日志和uwsgi的提示


![](14.png)



参考：http://tripleday.cn/2016/10/06/graphite/

转载于:

https://blog.csdn.net/aigu1989/article/details/102241677

https://www.cnblogs.com/zhang-ke/p/6878511.html


---



# 官方文檔

翻译从[这里](https://graphite.readthedocs.io/en/latest/overview.html)

# 概述

## Graphite能做什么和不能做什么

Graphite可以做下面两件事情

1. 存储 时间戳 数据
2. 按照你的需求渲染数据到图

Graphite不能够帮你搜集数据,然后下面这些工具 [tools](https://graphite.readthedocs.io/en/latest/tools.html) 可以发送数据到Graphite

尽管这通常需要一点代码，

[sending data](https://graphite.readthedocs.io/en/latest/feeding-carbon.html) 发送数据到Graphite是很容易的

## 关于项目

>Graphite是一个企业级的监控工具,并且能够运行在你的便宜的机器上.

2006的时候,他被 [Chris Davis](mailto:chrismd%40gmail.com) 在 [Orbitz](http://www.orbitz.com/) 设计出来的,当时是作为一个

>副项目，它最终成长为一个基本的监控工具。

2008年，Orbitz允许在开源Apache 2.0许可下发布Graphite。从那以后，克里斯继续致力于Graphite的研究，并将其应用于包括 [Sears](http://www.sears.com/)在内的其他公司,它在这里作为电子商务监控系统的支柱.

到了今天,更多的[公司](https://graphite.readthedocs.io/en/latest/who-is-using.html) 在用它

## 架构概述

Graphite由3个软件组件组成:

- carbon-一个侦听时间序列数据的进程
- whisper - 一个时间序列数据的数据库(和RRD比较相似)
- graphite webapp - 一个[django](http://victorfengming.gitee.io/course/django/)项目,它使用Cairo按需渲染图形

>输入数据非常简单，通常大多数工作都是在一开始收集数据.

随着你发送数据点到carbon,他们马上就可用了,提供一个图形的web app.

>这个webapp 通过几种方式去创建和展示图形(包括简单呐的urlapi)来渲染并且使它很容易嵌入图形在其他网页。

## Graphite 是啥

他是一个高度可扩展的实时绘图系统.作为一个用户,你编写一个 能够收集数字时间序列数据 的应用,并且收集你感兴趣的图形,然后发送到Graphite一个后端的进程, carbon, 他能够存储这个数据在 Graphite的专门的数据库中. 这个数据能够 通过 Graphite的网络接口可视化.

## 什么样的牛马能用这个Graphite

>任何想要跟踪任何东西的值的人都成.如果你有一个能潜在的伴随时间改变的值,并且你可能想要用图来表达,那么Graphite可能可以满足你的需求哦.

说白了,Graphite被设计就是为了处理这种数字时间序列数据.

>举个栗子,Graphite擅长 画这个 股票价格图,因为他们的值是随着时间而改变的.

无论是几个数据点,或者来自数千台服务器的几十个性能指标，那么Graphite就适合您了。

>另外，您不必提前知道这些东西的名字(谁想维护这么大的配置?)

您只需发送一个度量名称、一个时间戳和一个值，Graphite将负责其余的工作!

## Graphite的可扩展性咋样?

从CPU的角度来说,Graphite在前端和后端水平扩展，这意味着您可以简单地添加更多的机器来获得更多的吞吐量.

>它还具有容错性，因为丢失后端机器将导致最小数量的数据丢失(该机器在内存中缓存的任何数据)，并且如果您有足够的剩余容量来处理负载，则不会破坏系统

从I/O的角度说,在负载下，Graphite在许多不同的文件上非常快速地执行许多微小的I/O操作. 这是因为发送给Graphite的每一个不同的指标都被存储到了他自己的数据库文件中,这与很多构建在RRD上面的工具 (drraw, Cacti, Centreon, etc) 相似.

>在事实上,Graphite最初确实使用RRD来存储，直到出现了根本性的限制，需要一种新的存储引擎

高容量(每分钟更新几千个不同的度量)几乎需要一个好的RAID阵列和/或ssd。如果磁盘不能跟上大量的小的写操作(每个数据点只有几个字节，但是大多数标准磁盘每秒不能做超过几千个I/O操作，即使它们很小)，那么Graphite的后端缓存传入的数据。当这种情况发生时，Graphite的数据库引擎whisper允许carbon一次写入多个数据点，从而只以将多余的数据缓存在内存中直到可以写入为代价来提高总体吞吐量。

Graphite还支持[可替代的存储后端](https://graphite.readthedocs.io/en/latest/storage-backends.html) ，可以极大地改变这些特性。

## 这个图表的实时性咋样?

>非常牛逼,甚至在高负荷的情况下,在每个时间间隔的数量指标来远远大于你的存储系统可以执行I / O操作和大量的数据被缓存在存储管道(见以前的问题的解释),Graphite仍然吸引了实时图表。

诀窍在于,当Graphitewebapp接收请求画一个图,它同时检索数据以及从贮前缓存从磁盘(可能是分布式的如果你有多个后端服务器),结合数据来创建一个实时图的两个来源。

## 都谁已经用这个Graphite

>Graphite是Orbitz内部开发的，用于可视化各种操作——关键数据，包括应用程序指标、数据库指标、销售等。

在撰写本文时，Orbitz的生产系统在一个非常快的SAN上的两台niagra-2 Sun服务器上运行时，每分钟可以处理大约16万个不同的指标。

## Graphite是啥写的

Python2写的,Graphite webapp建立在Django web框架上，使用ExtJS javascript GUI工具包。图形呈现是使用Cairo图形库完成的。后端和数据库是用纯Python编写的。

## 哪位大神开发并维护的Graphite

>Graphite最初是由Chris Davis在Orbitz开发的。Orbitz长期以来一直是开源社区的一部分，并发布了其他一些内部开发的产品。

Graphite目前是由一个志愿者团队开发的石墨项目GitHub组织

说白了,就是开源的

## Graphite用没用到RRDtool

> 不，至少从2006年Graphite首次问世以来就没有了

Graphite有自己专门的数据库库whisper，它在设计上与RRD非常相似，但有一个Graphite所需要的细微但根本重要的区别。创建whisper有两个原因。

第一个原因是，RRD是在这样的假设下设计的，即数据总是会定期地插入到数据库中，而这种假设会导致RRD在给出不定期出现的数据时表现出不受欢迎的行为。

创建Graphite是为了方便各种应用程序指标的可视化，这些指标并不总是经常发生，比如当处理一个不常见的请求时，测量延迟并发送给Graphite。

使用RRD，数据被放置到数据库内的一个临时区域中，直到当前时间间隔已通过，才可以访问该区域，并在接下来的时间间隔内将另一个值插入到数据库中。

如果在指定的时间内没有发生这种情况，原始数据点将被覆盖并丢失。现在对于一些指标来说，缺少值可以被正确地解释为0，但是对于延迟等指标则不是这样，因为0表示工作是在0时间内完成的，这与没有工作是不同的。假设延迟为零也会破坏分析，如计算平均延迟等。

编写whisper的第二个原因是性能。

> RRDtool非常快;事实上，它比耳语快得多。

但是RRD(在编写whisper时)的问题是，RRD一次只允许向数据库插入单个值，而编写whisper则允许一次插入多个数据点，将它们压缩到单个写操作中。

这极大地提高了在高负载下的性能，因为Graphite操作的是很多很多的文件，而对于这样小的操作(写一些字节在这里，写一些字节在那里，等等)，瓶颈是由I/O操作的数量造成的。

考虑这样一个场景，Graphite每分钟接收100000个不同的公制值;为了维持这种负载，Graphite必须能够每分钟向磁盘写入这么多的数据点。但假设底层存储每分钟只能处理20,000个I/O操作。

> 有了RRD(写whisper的时候)，就没有机会跟上了。

但是对于whisper，我们可以一直缓存传入的数据，直到我们为一个给定的度量积累了10分钟的数据，然后不用做10个I/O操作来写这10个数据点，whisper可以在一个操作中完成。

我一直提到“在编写whisper时”的原因是RRD现在支持这种行为。然而，只要第一个问题仍然存在，Graphite就会继续使用whisper。

## Graphite的结构图

![](overview.png)

---

暂时翻译到这里,如需阅读更多在 [这里](https://graphite.readthedocs.io/en/latest/install.html)