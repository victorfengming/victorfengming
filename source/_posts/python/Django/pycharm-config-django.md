---
title: "pycharm中运行django的相关配置"
date:       2019-11-27
subtitle: "Requested setting CACHES, but settings are not configured. 问题解决"
tags:
	- Python
	- solution
	- web
	- django
---



* content
{:toc}





### 起步


小编在使用pycharm写django项目的时候遇到一个问题:

在cmd中能够正常运行django程序,
pycharm 中运行不了django的程序，看错误是：

```shell script
django.core.exceptions.ImproperlyConfigured: 
Requested setting CACHES, but settings are not configured. 
You must either define the environment variable 
DJANGO_SETTINGS_MODULE or call settings.
configure() before accessing settings. 
```

结果百度了半天没结果，最后还是在 老外的网站上找到了答案:
### 解决方案

本来django项目在 python shell 中可以完美运行，在pycharm里面就不行，原因是pycharm 要你配置一个  环境变量  `DJANGO_SETTINGS_MODULE` 这个变量告诉django项目去找哪一个`settings` 文件。  

### 具体的步骤：


1、Run  -->  EditConfigures 

2、找到python一项  具体名字是 Python tests（注意不是django那一个），然后修改里面的Environment variables 添加一项。名称是`DJANGO_SETTINGS_MODULE`  值是  你的settings,比如 `mysite.settings` 。


本文转自:https://www.cnblogs.com/lout/articles/4149591.html