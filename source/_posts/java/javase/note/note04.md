---
title: "Java笔记04-核心类库"
date:       2019-10-19
tags:
	- Java
	
---


* content
{:toc}





### Object类
#### 1.1 常用的包
    java.lang包  -该包是Java语言中的核心包,该包中的内容由Java虚拟机自动导入
    如:String类,System类等

    java.util包- 该包是Java语言中的工具包,里面包含了大量的工具类和集合类等

    java.io包 是输入输出包,包括读写各种设备

    java.net包 是网络编程包,包括各种网络编程

    java.sql包 是操作数据库的所有类和接口

Java程序员在编程时,可以使用大量的类库,因此,java编程需要记的很多,对编程能力的本身要求不是特别的高.

### 第三个阶段
从这个阶段开始,我们不需要自己来写一些类了

而是要学习系统给我们写好的一些类了,这部分最好需要随时来查询API文档

#### Object类
1. 基本概念
    java.lang.Object类是所有类层次结构的根类,任何类都是该类的直接或间接子类.
    (也验证了那就话,`万物皆对象`)
2. 常用的方法
```java
    Object() - 使用无参方式构造对象
    boolean equals(Object obj) - 用于判断调用对象是否与参数对象相等
        - 该方法默认比较两个对象的地址,与== 运算符结果相同
        - 为了使得该方法比较两个对象的内容,则需要重写该方法
        - 若该方法重写后,则应该重写hashCode()方法来维护hashCode方法的常规协定
    int hashCode() - 用于获取调用对象的哈希码值(内存地址的编号)
        - 若调用equals方法的结果相等,则各自调用hashCode方法的结果相同
        - 若调用equals方法的结果不相等,则各自调用hashCode方法的结果不相同
        - 为了维护上述的常规协定与equals方法结果保持一致,就需要重写该方法
    String toString()方法 - 用于获取对象的字符串形式
        - 该方法默认返回的字符串为:包名.类名@哈希码值的十六进制形式
        - 为了返回更有意义的数据内容,则需要重写该方法
        - 当字符串内容与引用进行连接时,自动调用toString()方法
        - 当使用print()或println()方法打印引用时,或者用+连接时候,调用该方法
```

### equals方法
equals方法用于判断对象是否"相等"
```java
equals(Object obj)
// 这么定义的好处是,所有的类都能够作为的参数传递进来
// 大不了就形成多态呗!
```
多态无处不在
```
boolean equals(Object obj)
```
要想调用这个方法,这个引用必须是非空的引用,不然会引起空指针异常
```java
自反性: 自个儿跟自个儿比都相等,废话  
对称性: y.equals(x)相等 -> x.equals(y)  
传递性: x与y等,y与z等,那么x与z等  
一致性: x与y等,x还是与y等  
对于空: x(非空).equals(null)结果为false  
```
说白了equals就是比较引用类型的地址信息  
与 == 运算符等价


### 包装类和数学处理类
```java
Person p = new Person();
// 声明Person类型的引用,指向Person类型的对象
int num = 10;
// 声明一个int类型的变量num初始值为10
// Java语言是一门纯面向对象的编程语言

// 对于八种不是对象类型的变量,我们就要想办法把他们包装成面向对象的 -->
```
```java
包装类概念
    由于Java语言是一门纯面向对象的编程语言,而8种基本数据类型声明的变量并不是对象,为了满足Java语言的特性就需要对这些变量进行对象化处理,而实现该功能的相关类就叫做包装类
```
```java
包装类的分类
    int -> java.lang.Integer类
    char -> java.lang.Character类
    其他类型对应的包装类就是首字母变为大写的
```
Integer类
```java
基本概念:
    java.lang.Integer类是int类型的包装类,里面包含了一个int类型的成员变量.
    该类有final关键字修饰表示不能被继承
```
```
常用方法
    Integer(int value) - 根据参数指定的整数构造对象
    Integer(String s) - 根据参数知指定的字符串构造对象
    该类重写了equals(), hashCode() toString()方法
```
### 包装类
基本数据类型,使用起来非常方便,但是没有对应的方法来操作这些数据类型的数据,可以使用一个类,把基本数据类型装起来,在类中定义一些方法,这个类叫做包装类,我们可以使用类中的方法来操作这些基本数据类型的数据

### 装箱与拆箱
* 装箱:
 * 把基本数据类型的数据,包装到包装类中(基本数据类型的数据->包装类)
 * 构造方法:
 *  Integer(int value)
 *  静态方法:
 *
 * 拆箱:
 *  在包装类中取出基本类型数据(包装类->基本类型数据)
 *  成员方法:int intValue() 以int 类型返回该Integer的值
 *


### 基本类型与字符串类型之间的相互转换

* 基本类型 -> 字符串(String)
* 1. 基本类型的值+"" 最简单的方法(工作中常用)
* 2. 包装类的静态方法toString(参数),不是Object类的toString()重载
* 3. String类的静态方法valueOf(参数)
* static String valueOf(int i) 返回int 参数的字符串表示形式
* 字符串(String) -> 基本类型
*  使用包装类的静态方法paresXXX("字符串");
*      Integer类:static int parseInt(String s)
*      Double类: static double parseDouble(String s)

#### String转换成对应的基本数据类型
除了Character类之外,其他所有包装类都具有parseXXX静态方法可以将字符串参数转换为对应的基本类型:
```java
int i = Integer.parseInt(s3);
float ff = Float.parseFloat(s);
long l = Long.parseLong(s);
...
```  


### 学习集合的目标:
1. 会使用集合存储数据
2. 会遍历集合,把数据取出来
3. 掌握每种集合

### 集合框架的学习方式:
1. 学习底层:学习顶层接口/抽象类中共性的方法,所有的子类都可以使用

2. 使用底层:底层不是接口就是抽象类,无法创建对象使用,需要使用底层的子类创建对象使用

### 容器类数据包含结构
继承:子类共性抽取,形成父类(接口)
```java
Collection接口
    List接口
        Vector集合
        ArrayList集合
        LinkedList集合
    Set接口
        TreeSet集合
        HashSet集合(无序)
            LinkedHashSet集合
```
无序的集合(存储和取出元素的顺序有可能不一致)


Collection接口
```java
定义的是所有单列集合中共性的方法
所有的单列集合都可以使用共性的方法
没有带索引的方法
```

List接口
```java
1. 有序集合(存储和取出元素顺序相同)
2. 允许存储重复的元素
3. 有索引,可以使用普通的for循环遍历
```
Set接口
```java
1. 不允许存储重复元素
2. 没有索引(不能使用普遍for循环遍历)
```

### Collection接口
* java.util.Collection
* 所有单列集合的最顶层的接口,里面定义了所有单列集合共性的方法
* 任意的单列集合都可以使用Collection接口中的方法
* 共性的方法
* public boolean add(E e): 把给定的对象添加到当前集合中
* public void clear():清空集合中所有的元素
* public boolean remove(E e):把给定的对象在当前集合中删除
* public boolean contains(E e):判断当前集合中是否包含给定的对象
* public boolean isEmpty(): 判断当前集合是否为空.
* public int size(): 返回集合中元素的个数.
* public Object[] toArray(): 把集合中的元素,存储到数组中.


### Iterator迭代器
在程序开发中,经常需要遍历集合中的所有元素.针对这种需求,JDK专门提供了一个接口`java.util.Iterator`.`Iterator`接口也是Java集合中的一员,但它与`Collection`,`Map`接口有所不同,`Collection`接口与Map接口主要用于存贮元素,而`Iterator`主要用于迭代访问(即遍历)`Collection`中的元素,因此`Iterator`对象也被称为迭代器.

想要遍历`Collection`集合,那么就要获取该集合迭代器完成迭代操作,下面介绍一下获取迭代器的方法:
- `public Iterator iterator()`:获取集合对应的迭代器,用来遍历集合中的元素的.
下面介绍一下迭代的概念:
- 迭代:即`Collection`集合元素的通用获取方式.在取元素之前先要判断集合中有没有元素,如果有,就把这个元素取出来,继续在判断,如果还有就再取出出来.

一直把集合中的所有元素全部取出.这种取出方式专业术语称为`迭代`

`Iterator`接口的常用方法如下:
- `public E next()`:返回迭代的下一个元素.
- `public boolean hasNext()`:如果仍有元素可以迭代,则返回true


 * java.util.Iterator 接口:迭代器(对集合进行遍历)
 * 有两个常用的方法
 * boolean hasNext() 如果仍有元素可以迭代,则返回true
 * E next() 返回迭代的下一个元素
 * 取出集合中的下一个元素
 * Iterator 迭代器,是一个接口,我们无法直接使用,需要使用ITerator接口的实现类对象,获取实现类的方式比较特殊
 * Collection接口中有一个方法,叫iterator(),这个方法返回的就是迭代器的实现类对象
 * Iterator<E> iterator()
 * 返回在此 collection 的元素进行迭代的迭代器