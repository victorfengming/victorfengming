---
title: 'tomcat的配置以及使用'
date:       2019-10-21
tags:
	- Java
	- basis
---

### tomcat 概述
Tomcat 服务器是一个免费的开放源代码的Web 应用服务器

### 1.下载
tomcat的官方网站:https://tomcat.apache.org/
### 2.安装
解压缩到哪就行了,不用安装的
### 3.卸载
删除目录即可
### 4.启动
* bin/startup.bat ,双击运行该文件即可
* 访问:在浏览器输入http://localhost:8080 回车访问
        http://othersid:8080 访问别人
* 可能遇到的问题:
    1. 黑窗口一闪而过:
        * 原因: 没有正确配置JAVA_HOME环境变量
        * 解决方案: 正确配置一下环境变量,并将jdk中的bin文件夹的那个就是path中的变量用%JAVA_HOME%来哦替换即可
    2. 启动报错:
        1. 暴力:找到占用的端口号,并且找到对应的进程,杀死该进程
            * netstat -ano
        2. 温柔:修改自身的端口号
            * conf/server.xml
            * <Connector port="8888" protocol="HTTP/1.1"
            connectionTimeout="20000"
            redirectPort="8445"/>
            * 一般会将tomcat默认端口号修改为80.80端口号是`http`协议默认的端口号
                * 好处:在访问的时候,就不用输入端口号了

### 5. 关闭
1. 正常关闭:
    * bin/shutdown.bat
    * ctrl+c
2. 强制关闭:
    * 点击启动窗口的X

### 6.配置
#### 部署项目的方式:
1. 直接将项目放到webapps目录下面即可.
    * /hello: 项目的访问路径-->虚拟路径
    * 简化部署:将项目打成一个war包,再将war包放置到webapps目录下面.
        * war包会自动解压缩
2. 配置conf/server.xml文件
    在<Host>标签体中配置
    ```html
    <Context docBase="D:\hello" path="/hehe" />
    ```
    * docBase:项目存放的路径
    * path:虚拟目录
3. 在conf\Catalina\localhost创建任意名称的xml文件.在文件中编写
```html
<Context docBase="E:\hello" />
```
* 虚拟目录:xml文件的名称    

#### 静态项目和动态项目

* 目录结构
    * java 动态项目的目录结构:
        -- 项目的根目录
            -- web-INF目录:
                -- web.xml:web项目的核心配置文件(下面那俩可以没有,这个得有)
                -- classes目录:放置字节码我呢间的目录
                -- libmul:放置依赖的jar包

#### 将tomcat集成到IDEA中, 并且创建JavaEE的项目,部署项目.

更新