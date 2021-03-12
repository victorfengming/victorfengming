---
title: 'java中最强语法--lambda表达式'
date:       2019-11-10
tags:
	- Java
	- basis
---

### lambda表达式

lambda表达式形式：参数，箭头(->)以及一个表达式，也可以将操作放在代码块{}中。

```java
(String first,String second)->
{
	if(first.length()>second.length()) return 1;
	else if(first.length()<second.length()) return -1;
	else return 0;
}

() -> System.out.pringln("i");
```

对于只有一个抽象方法的接口，需要这种接口的对象时，就可以提供一个lambda表达式。这种接口称为函数式接口。Comparator 就是只有一个方法的接口， 所以可以提供一个lambda 表达式：


函数式接口中可以包含静态方法（已经实现了的方法），默认方法（default），java.lang.Object里的public方法。

```java
Arrays.sort (words ,
	(first , second) -> first.length() - second.length()) ;
```

### 方法引用
```java
Timer t = new Timer(1000, event -> System.out.println(event));
//等价于
Timer t = new Timer(1000, System.out::println);
```



表达式System.out::println是一个方法引用，等价于前面的lambda表达式。主要有3中形式：

```java
//System.out.println == x->System.out.println(x)
object::instanceMethod
//Math.pow(x,y) == (x,y)->Math.pow(x,y)
Class::staticMethod
//String::compareToIgnoreCase == (x,y)->x.compareToIgnoreCase(y)
Class::instanceMethod
```