---
title: 'SpringBoot解决方案'
cover: "/img/lynk/18.jpg"
date:       2020-07-14
subtitle: '各种问题' 
author: "victor"
tags:
	- Java
	- basis
	- SpringBoot
---

  

# 配置文件优先级

## 1. 项目内部配置文件

spring boot 启动会扫描以下位置的application.properties或者application.yml文件作为Spring boot的默认配置文件

```
　　–file:./config/
　　–file:./
　　–classpath:/config/
　　–classpath:/
```

![img](928953-20190613113659461-117207878.png)



以上是按照优先级从高到低的顺序，所有位置的文件都会被加载，高优先级配置内容会覆盖低优先级配置内容。

SpringBoot会从这四个位置全部加载主配置文件，如果高优先级中配置文件属性与低优先级配置文件不冲突的属性，则会共同存在—互补配置。

------

我们也可以通过配置spring.config.location来改变默认配置。

java -jar spring-boot-02-config-02-0.0.1-SNAPSHOT.jar --spring.config.location=file:///D:/application.properties,classpath:/,[classpath:/config/](http://classpath/config/)
项目打包好以后，我们可以使用命令行参数的形式，启动项目的时候来指定配置文件的新位置。

指定配置文件和默认加载的这些配置文件共同起作用形成互补配置。
Idea 单测启用自定义配置：添加jvm参数：-Dspring.config.location=file:///D:/project_conf/application.yml -ea

## 2. 外部配置加载顺序

SpringBoot也可以从以下位置加载配置：优先级从高到低；高优先级的配置覆盖低优先级的配置，所有的配置会形成互补配置。

1.命令行参数

- 所有的配置都可以在命令行上进行指定；
- 多个配置用空格分开； –配置项=值

　　java -jar spring-boot-02-config-02-0.0.1-SNAPSHOT.jar --server.port=8087 --server.context-path=/abc

2.来自java:comp/env的JNDI属性 

3.Java系统属性（System.getProperties()） 

4.操作系统环境变量 

5.RandomValuePropertySource配置的random.*属性值

6.jar包外部的application-{profile}.properties或application.yml(带spring.profile)配置文件

7.jar包内部的application-{profile}.properties或application.yml(带spring.profile)配置文件

8.jar包外部的application.properties或application.yml(不带spring.profile)配置文件

9.jar包内部的application.properties或application.yml(不带spring.profile)配置文件

10.@Configuration注解类上的@PropertySource 

11.通过SpringApplication.setDefaultProperties指定的默认属性

[参考官网地址](https://docs.spring.io/spring-boot/docs/1.5.9.RELEASE/reference/htmlsingle/#boot-features-external-config)



原文:[SpringBoot配置文件加载位置与优先级](https://www.cnblogs.com/erbing/p/11015599.html)







# 配置文件加密

Spring-boot项目中properties文件中的密码明文不太安全，

所以想到给明文加密。了解了一下，有一个依赖工具可以实现这个功能。Ulisesbocchio插件

 

***\*1.\**\**添加\**\**maven\**\**依赖：\****

```pom
<dependency>
    <groupId>com.github.ulisesbocchio</groupId>
    <artifactId>jasypt-spring-boot-starter</artifactId>
    <version>1.14</version>
</dependency>
```



 

***\*2.\**\**配置加密密钥或盐值（properties文件中配置）：\****

```
jasypt.encryptor.password=1111111111
```

 

***\*3.\**\**进入本地maven库.m2\repository\org\jasypt\jasypt\1.9.2路径下，执行加密命令：\****

java -cp jasypt-1.9.2.jar org.jasypt.intf.cli.JasyptPBEStringEncryptionCLI input=密码明文 password=***\*1111111111\**** algorithm=PBEWithMD5AndDES

执行命令后会出现加密后密码：

![39d11b56889d67e8781c78bdb12643f1365.jpg](39d11b56889d67e8781c78bdb12643f1365.jpg)

**4.将properties文件中需要加密的数据替换成”ENC(密文)”，如：**

user.password=ENC(LtogooCZuLSM2vE8uKcCnA==)

 

**5.运行代码正常！**

转载于:https://my.oschina.net/kevin2kelly/blog/2254055



**6. 用于生成加密字符tool类**

> 可以写一个类用来生成

```java
package com.travelsky.shopping.console.loca.tool;

import org.jasypt.util.text.BasicTextEncryptor;


public class EncryptorGenerator {
    public static void main(String[] args) {
         BasicTextEncryptor textEncryptor = new BasicTextEncryptor();
    // 加密密钥
    textEncryptor.setPassword("1111111111");
    // 要加密的数据（如数据库的用户名或密码）
    String username = textEncryptor.encrypt("abc");
    String password = textEncryptor.encrypt("123");
    System.out.println("username:" + username);
    System.out.println("password:" + password);
    }
}

```



原文:[使用ulisesbocchio对spring-boot项目properties配置文件信息加密](https://blog.csdn.net/weixin_34241036/article/details/92575297)