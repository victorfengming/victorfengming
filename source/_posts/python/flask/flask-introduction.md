---
title: "Flask 概述"
date:       2019-10-08
tags:
	- Python
	- solution
	- web
	- flask
---





* content
{:toc}






### 什么是Web Framework？
Web Application Framework（Web应用程序框架）或简单的Web Framework（Web框架）表示一个库和模块的集合，使Web应用程序开发人员能够编写应用程序，而不必担心协议，线程管理等低级细节。

### 什么是Flask？
Flask是一个用Python编写的Web应用程序框架。 它由 Armin Ronacher 开发，他领导一个名为Pocco的国际Python爱好者团队。 Flask基于Werkzeug WSGI工具包和Jinja2模板引擎。两者都是Pocco项目。

### WSGI
Web Server Gateway Interface（Web服务器网关接口，WSGI）已被用作Python Web应用程序开发的标准。 WSGI是Web服务器和Web应用程序之间通用接口的规范。

### Werkzeug
它是一个WSGI工具包，它实现了请求，响应对象和实用函数。 这使得能够在其上构建web框架。 Flask框架使用Werkzeug作为其基础之一。

### jinja2
jinja2是Python的一个流行的模板引擎。Web模板系统将模板与特定数据源组合以呈现动态网页。

Flask通常被称为微框架。 它旨在保持应用程序的核心简单且可扩展。Flask没有用于数据库处理的内置抽象层，也没有形成验证支持。相反，Flask支持扩展以向应用程序添加此类功能。一些受欢迎的Flask扩展将在本教程后续章节进行讨论。