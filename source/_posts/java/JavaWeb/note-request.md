---
title: 'JavaWeb笔记06'
cover: "/img/lynk/45.jpg"
date:       2019-11-15
subtitle:   "请求相关"
tags:
	- Java
	- basis
	
---
  

  

  
  
  
  

  
  
  

## 请求的转发
### 概念
一个web组件 将未处理完毕的的请求,通过tomcat转交给另一个web组件处理
### 步骤
1. 获取请求转发器
```java
RequestDispatcher rd = request.getRequestDispatcher("转发的地址)
```
2. 通过转发器 发起转发
```
rd.forward(request,response)
```
### 转发流程
步骤1: 范文
### 特点:
1. 转发过程中,多个servlet之间共享一份请求信息,共享一个响应对象
2. 转发只能发生在同一个服务器中(转发无法实现跨域)
3. 无论转发发生多少次,对于浏览器来说,只发起过一次请求,并且只接到了一次响应
4. 相对于重定向来说,效率更高
## 请求的重新定向
### 概念
响应时,告知浏览器新的请求地址,浏览器接收到自动请求新的地址
比如你在京東中登录后,会直接重定向到首页中,不用你点击了
### 步骤
```java
response.sendRedirect("重定向地址")
```
### 流程
步骤1: 当浏览器
### 特点
1. 重定向会产生新的请求和新的响应
2. 使用重定向,可以在多个服务器之间发生(可以实现跨域操作)
3. 浏览器地址栏的内容,会发生改变
4. 相对于请求转发而言,效率较低