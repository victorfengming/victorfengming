---
title: 'JavaWeb笔记02'
date:       2019-11-12
subtitle: 'Tomcat'
tags:
	- Java
	- basis
	
	- JDBC
---
  
  
* content  
{:toc}  
  
  
  
  


# 今日内容
1. web相关概念回顾
2. web服务器软件:Tomcat
3. Servlet入门学习

## web相关概念回顾
1. 软件架构
    1. C/S: 客户端/服务器端
    2. B/S: 浏览器/服务器端
2. 资源分类
    1. 静态资源: 所有用户访问后,得到的结果都是一样的,成为静态资源,静态资源可以直接被浏览器解析
        - 如:html, css ,JavaScript
    2. 动态资源:每个用户访问相同资源后,得到的结果可能不一样.称为动态资源,动态资源被访问后,需要先转换为静态资源,在返回给浏览器
        - 如:servlet/jsp,php,asp......
3. 网络通信三要素
    1. IP: 电子设备(计算机)在网络中的唯一标识.
    2. 端口: 应用程序在计算机中的唯一标识.0-65536,建议不要在1024以下,可能被占用了
    3. 传输协议: 规定了数据通信传输的规则
        1. 基础协议:
            1. tcp:安全协议,三次握手.确认双方都在线的情况下再进行数据传输
            2. udp::不安全的协议,广播发送,可能会丢失,但是速度快
            
## web服务器软件:
- 服务器: 安装了服务器软件的计算机
- 服务器软件: 接收用户的请求,处理请求,做出响应
- web服务器软件: 接收用户的请求,处理请求,做出响应
    - 在web服务器软件中,可以部署web项目,让用户通过浏览器来访问这些项目
    - web容器
- 常见的java相关的web服务器软件:
    - webLogic:oracle公司,大型的JavaEE服务器,支持所有的JavaEE规范,收费的
    - webSphere: IBM公司,大型的JavaEE服务器,支持所有的JavaEE规范,收费的
    - JBOSS: JBOSS公司的,大型的JavaEE服务器,支持所有JavaEE规范,收费的
    - Tomcat:Apache基金组织,中小型的JavaEE服务器,仅仅支持少量的JavaEE规范servlet/jsp.开源的,免费的
- JavaEE: Java语言在企业级开发中使用的技术规范的总和,一共规定了13项大的规范
- Tomcat: [tomcat的配置以及使用](https://victorfengming.gitee.io/2019/10/21/tomcat/)

    
## serverlet 
 [servlet的配置以及使用](https://victorfengming.gitee.io/2019/10/22/servlet/)        
                