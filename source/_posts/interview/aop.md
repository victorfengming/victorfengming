---
title: "什么是AOP（面向切面编程）"
cover: "/img/lynk/89.jpg"
date:       2018-11-28
subtitle: "Spring提供的关键特性之一"
tags:
	- Python
	- solution
	- interview
	- oop
---

### 起步
这种在运行时，动态地将代码切入到类的指定方法、指定位置上的编程思想就是面向切面的编程。


AOP是Spring提供的关键特性之一。AOP即面向切面编程，是OOP编程的有效补充。使用AOP技术，可以将一些系统性相关的编程工作，独立提取出来，独立实现，然后通过切面切入进系统。从而避免了在业务逻辑的代码中混入很多的系统相关的逻辑——比如权限管理，事物管理，日志记录等等。这些系统性的编程工作都可以独立编码实现，然后通过AOP技术切入进系统即可。从而达到了 将不同的关注点分离出来的效果。本文深入剖析Spring的AOP的原理。

### AOP相关的概念
1） Aspect ：切面，切入系统的一个切面。比如事务管理是一个切面，权限管理也是一个切面；

2） Join point ：连接点，也就是可以进行横向切入的位置；

3） Advice ：通知，切面在某个连接点执行的操作(分为: Before advice , After returning advice , After throwing advice , After (finally) advice , Around advice )；

4） Pointcut ：切点，符合切点表达式的连接点，也就是真正被切入的地方；

### AOP 的实现原理
AOP分为静态AOP和动态AOP。静态AOP是指AspectJ实现的AOP，他是将切面代码直接编译到Java类文件中。动态AOP是指将切面代码进行动态织入实现的AOP。Spring的AOP为动态AOP，实现的技术为： JDK提供的动态代理技术 和 CGLIB(动态字节码增强技术) 。尽管实现技术不一样，但 都是基于代理模式 ， 都是生成一个代理对象 。

作者：breaktian

链接：https://www.jianshu.com/p/3ea60002f290

来源：简书

著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。