---
title: "CentOS7 安装Graphite"
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