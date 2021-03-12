---
title: 'spring笔记01'
cover: "/img/lynk/18.jpg"
date:       2020-07-14
subtitle: '' 
tags:
	- Java
	- basis
	
	- Spring
---

  
  
* content  
{:toc}  
  
  
  
  

### Spring 简介
Spring框架由Rod Johnson开发,2004年发布了 Spring框架的第一版.Spring是一个从实际开发中抽取出来的框架,因此它完成了大量开发中的通用步骤,留给开发者的仅仅是与特定应用相关的部分,从而大大提高了企业应用的开发效率.

Spring总结起来优点如下:
- 低侵入式设计,代码的污染极低.
- 独立于各种应用服务器,基于Spring框架的应用,可以真正实现Write Once,Run Anywhere的承诺.
- Spring的IoC容器降低了业务对象替换的复杂性,提高了组件之间的解耦.
- Spring的AOP支持允许将一些通用任务如安全,事务,日志等进行集中式管理,从而提供了更好的复用.
- Spring的高度开发性,并不强制应用完全依赖于Spring,开发者可自由选用Spring框架的部分或全部.

Spring框架的组成结构图如下所示:

![Spring组成结构图](/img/posts/java/spring/spring01.png)

### Spring 的核心机制
#### 管理Bean
程序主要是通过Spring容器来访问容器中的Bean,ApplicationContext是Spring容器最常用的接口,该接口如下两个实现类:

- ClassPathXMLApplicationContext:从类加载路径下搜索配置文件,并根据配置文件来创建Spring容器.
- FileSystemXMLApplicationContext:从文件系统的相对路径或绝对路径下去搜索配置文件,并根据配置文件来创建Spring容器.

```java
public class BeanTest{
    public static void main(String args[]) throws Exception{
        ApplicationContext ctx = new ClassPathXmlApplicationContext("beans.xml");
        Person p = ctx.getBean("person", Person.class);
        p.say();
    }
}
```

### Eclipse 使用 Spring
在eclipse等IDE工具中,用户可以自建User Library,然后把Spring的Jar包都放入其中,当然也可以将Jar包直接放在项目的/WEB-INF/lib目录下,但是如果使用User Library,在项目发布时,需要将用户库所引用的Jar文件随应用一起发布,就是将User Library所使用的Jar复制到/WEB-INF/lib 目录下,这是因为对于一个Web应用,Eclipse部署Web应用时不会将用户库的Jar文件复制到/WEB-INF/lib下,需要手动复制.

### 依赖注入
Spring框架的核心功能有两个:
- Spring容器作为超级大工厂,负责创建,管理所有的Java对象,这些Java对象被称为Bean.
- Spring容器管理容器中Bean之间的依赖关系,Spring使用一种被称为"依赖注入的方式来管理Bean之间的依赖关系.

使用依赖注入,不仅可以为Bean注入普通的属性值,还可以注入其他Bean的引用.依赖注入是一种优秀的解耦方式,其可以让Bean以配置文件组织在一起,而不是以硬编码的方式耦合在一起.
















