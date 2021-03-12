---
title: 'servlet的配置以及使用'
cover: "/img/lynk/1.jpg"
date:       2019-10-22
tags:
	- Java
	- basis
---

## servlet:server applet
### * 概念:运行在服务器端的小程序
* servlet就是一个接口,定义了java类被浏览器访问到(tomcat)识别的规则.
* 将来我们自定义一个类,实现servlet接口,复写方法.

### * 快速入门:
1. 创建一个JavaEE项目
javaee7,tomcat路径配置
2. 定义一个类,实现servlet接口
    ```java
    public class ServletDemo1 implements Servlet {
        // 重写方法
    }
    ```
3. 实现接口中的抽象方法
alt+enter
4. 配置servlet

在web.xml中配置
```html
<!--    配置servlet-->
<servlet>
    <servlet-name>demo1</servlet-name>
    <servlet-class>cn.itcast.web.servlet.ServletDemo1</servlet-class>
</servlet>

<!--    写mapping-->
<servlet-mapping>
    <servlet-name>demo1</servlet-name>
    <url-pattern>/demo1</url-pattern>
</servlet-mapping>
```

### 执行原理:
1. 当服务器接收到客户端浏览器的请求后,会解析请求URL路径,获取访问的servlet的资源路径
2. 查找web.xml文件,是否有对应的`<url-pattern>`标签体内容.
3. 如果有,则在找到对应的`<servlet-class>`全类名
4. tomcat会将字节码文件加载进内存,并且创建其对象
5. 调用其方法

### servlet(中的方法)中的生命周期    
1. 被创建: 执行init方法,只执行一次
    * servlet什么时候被创建?
        * 默认情况下,第一次被访问时, servlet被创建
        * 可以配置执行servlet的创建时机
            * 在`<servlet>`标签下配置
                1. 第一次被访问时, 创建
                    * `<load-on-startup>`的值为负数
                2. 在服务器启动时, 创建
                    * `<load-on-startup>`的值为0或者正整数
    * Servlet的`init`方法,只执行一次,说明一个Servlet在内存中只存在一个对象,Servlet是单例的
        * 多个用户同时访问时,可能存在线程安全问题
        * 解决: 尽量不要在Servlet中定义成员变量.即使定义了成员变量,也不要对修改值
2. 提供服务: 执行service方法, 执行多次
    * 每次访问`Servlet`时,Service方法都会被调用一次
3. 被销毁: 执行destroy方法,只执行一次
    * Servlet被销毁时执行.服务器关闭时,Servlet被销毁
    * 只有服务器正常关闭时,才会执行destroy方法
    * destroy方法在Servlet被销毁之前执行,一般用于释放资源(遗言一般死之前说)

* Servlet3.0 :
    * 好处:
        * 支持注解配置.可以不需要web.xml了
    * 步骤:
        1. 创建javaEE项目,选择Servlet的版本3.0以上,可以不创建`web.xml`
        2. 定义一个类,实现Servlet接口
        3. 重写方法
        4. 在类上使用`@webservlet`注解,进行配置
            - `@WebServlet("资源路径)`

### IDEA与tomacat的相关配置
1. IDEA会为每个tomcat部署的项目单独建立一份配置文件
    * 查看控制台的log:
    ```cmd
    Using CATALINA_BASE:   "C:\Users\yangxin\.IntelliJIdea2019.2\system\tomcat\Tomcat_8_5_47_java_web_2"
    ```
2. 工作空间项目 和 tomcat部署的web项目    
    * tomcat 真正访问的是"tomcat部署的web项目","tomcat部署的web项目"对应着"工作空间项目"的web目录下的所有资源
    * WEB-INF目录下的资源不能被浏览器直接访问
3. 断点调试:使用"小虫子"启动(debug启动)
        