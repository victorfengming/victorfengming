---
title: 'JavaWeb笔记04'
cover: "/img/lynk/78.jpg"
date:       2019-11-13
subtitle:   "解决GET与POST乱码问题"
tags:
	- Java
	- basis
---
  
  
* content  
{:toc}  
  
  
  
  

## 解决GET与POST乱码问题:
### 请求的乱码问题
- GET:tomcat8版本之前,get请求会乱码
```
正常文字 --> UTF-8编码 --> 字节数组 --> ISO-8859-1 编码 --> 乱码文字
正常文字 <-- UTF-8编码 <-- 字节数组 <-- ISO-8859-1 编码 <-- 乱码文字
```
- 解决乱码的两种格式:
    - 格式1:可用于tomcat8版本之前的GET请求编码 以及 所有版本的POST请求乱码:
解决方案: 将乱码的文字,按照乱码的编码ISO-8859-1转换为字节数组,在按照正常的白马UTF-8组装为文字;
    - 格式2:格式1,解决乱码适用于参数较少的情况,如果参数过多,解决起来极其麻烦
    tomcat为我们提供了设置请求体编码的方式:
    注意: 只有POST请求,才有请求体
    格式:`request.setCharacterEncoding("UTF-8);`
- 注意:
    - 解决请求乱码的代码,必须运行在获取参数之前`request.setCharacterEncoding(""")`    
### 响应的乱码问题
- 方式1:设置网页的内容类型,以及网页的编码格式:`response.setContentType("text/html;charset=utf-8");`
- 方式2:设置网页的编码格式(因为没有设置网页内容类型为html,所以浏览器根被就不把他当html解析,当然就乱码了)`response.setCharacterEncoding("UTF-8");`

    
### 作业:
1. 编写注册页面
    - 要求:连接数据库,将表单的数据提交到servlet,在通过servlet将数据插入到数据库user29表格中
2. 编写登录页面
    - 要求: 连接数据库,将表单的数据与user29表格中数据对比,匹配提示登录成功,否则提示登录失败
3. 编写修改密码页面
    - 要求: 连接数据库,将表单的数据提交到servlet,在通过servlet修改数据库中user29表格的数据
4. 编写主页:
    - 要求: 查询数据库user29表格,将表格中所有数据,展示到浏览器中      
    
### 作业实现
#### 项目地址:
https://github.com/victorfengming/xdl_javaweb       
#### 采用技术:
- JDBC  + 连接池
- Tomcat  +   Servlet   
- Oracle   