---
title: "Django笔记"
cover: "/img/lynk/6.jpg"
date:       2019-12-03
subtitle: "多人博客项目"
tags:
	- Python
	- solution
	- web
	- django
---







# 多人博客项目
## 概述
DjangoMVC架构设计的开源的web快速开发框架

## 优点:
- 能够快速开发,如Auth,Cache,模板
- MVC设计模式
    - 实用的后台管理
    - 自带ORM,Template,Form,Auth核心
- 组件
    - 简洁的URL设计
    - 周边插件丰富
## 缺点:
- 重,因为东西大而全
- 同步阻塞

所以Django的设计目标就是一款大而全,
便于企业快速开发项目,因此应用比较广

## 模板

如果使用react实现前端页面,其实Django就没有必须使用模板,它其实就是一个后台服务程序,接收请求,响应数据。接口设计就可以是纯粹的Restful风格。

模板的目的就是为了可视化| ,将数据按照一定布局格式输出,而不是为了数据处理,所以一般不会有复杂的处理逻辑。模板的引入实现了业务逻辑和显示格式的分离,这样,在开发中,就可以分工协作,页面开发完成页面布局设计,后台开发完成数据处理逻辑的实现。

Python的模板引|擎默认使用Django template language (DTL)构建

## 模板配置

