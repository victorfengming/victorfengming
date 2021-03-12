---
title: 'Java笔记14-软件开发流程&设计原则'
cover: "/img/lynk/27.jpg"
date:       2019-10-28
tags:
	- Java
	- basis
	
---









## 今天内容:
- 1.常用的设计原则
- 2.常用的设计模式
- 3.常用的查找算法
- 4.常用的排序算法

## 1.常用的设计原则(记住)    
### 1.1软件的开发流程
    软件开发授权-投标 -> 100万
    1. 编写需求分析文档 => 
    2. 概要设计文档(架构) => 
    3. 详细设计文档(类图) => 
    4. 编码(项目经理分具体任务)
        还要测试  (SVN/GIT)单元测试,模块测试(一般都是美女多一些,对于技术要求比较低) 黑盒测试 白盒测试
    5. 安装和调试
        写使用说明文档
    6. 维护和升级
        软件公司和客户协商(钱要到位)
        还有一锤子买卖的(就是不管维护那种)
        
    如果整个开发周期是半年(可能编码只占一个月的时间)
    架构师把架构架构错了,那就都白干了,重新架构意味着要加班,这种情况不多,因为架构师至少要5年以上经验的
    绝大多是是客户的需求问题,或者是客户要加功能.
    
### 1.2常用的设计原则
### 1. 开放封闭原则(Open Close Principe)
对于扩展开放,对于修改关闭,为了使程序的扩展性好,易于维护
如:
```java
public  class  Person{
    private String name;
    private int age;
    private boolean gender;
    // ...
}
```
不,这样前面美女测试人呢的工作就白做了,所以应该这样
```java
public  class  Person{
    private String name;
    private int age;
    // ...
}
public class SubPerson extends Person{
    private boolean gender;
    //...
}
```
### 2. 里氏代换原则(Liskov Substitution Principe)
- 任何父类可以出现的地方,子类一定可以出现
- 子类is a 父类
- 在以后的开发中多使用继承和多态的理念

    多态的实际意义:
        屏蔽不同子类的差异性,实现通用的编程,产生不同的结果
    如:
```java
public statie void draw(Shape s){
    s.show();
}
ShapeTest.draw(new Rect(1,2,3,4));
ShapeTest.draw(new Circle(5,6,7));
// 父类类型的引用能到的地方,子类的引用也能到
```

### 3.依赖倒转原则(Dependence Inversion Principle)
尽量多依赖于抽象类或接口而不是具体实现类,对子类具有强制性和规范性
如:
```java
publice class Account{
    public double getLix(){
        // ...        
    }
}
publice class FixedAccount extends Account{
    //我这里想重写就重写,以为我的父类也不是抽象的 
}
```
要是这样,就符合了 
```java
publice abstract class Account{
    public abstract double getLix(){
        // ...        
    }
}
publice class FixedAccount extends Account{
    // 这回就不得不继承了
    @Override
    public double getLixi(){} 
}
```

### 4.接口隔离原则(interface segregation principle)
- 尽量依赖于小接口而不是大接口,避免接口的污染
- 可以降低耦合度
- 耦合主要指一个模块于其他模块之间的关联度.
    
如:
```java
public interface Animal{
    public abstract void run();//描述奔跑 行为
    public abstract void fly(); //描述飞行行为
}

public class Dog implements Animal{
    public abstract void run(){...};
    public abstract void fly(){
//        这个方法没法写了
    }
}
```
### 5.迪米特法则(最少知道原则) (Demeter Principe)
- 一个实体应当尽量少于其他实体之间 发生相互作用
- 低耦合,高内聚
- 高内聚就是指将一个实体应当将该实体应该拥有的功能尽量聚集在该实体内部
    
### 6.合成复用原则(Composite Reuse Principe) 
- 尽量多使用合成的方式,而不是继承的方式.
如:
```java
public class A{
    public void show(){...}
    ... ...
}
public class B extends A{
    public void test(){
        // 调用show方法
        show();
    }
    ... ...
    // 这样不推荐,因为java只能单继承,或者说会影响调用show()方法时候的性能,因为继承会继承父类的所有方法
}
```    
升级版
```java
public class A{
    public void show(){...}
    ... ...
}
public class B{
    private A a;
    public void test(){
        // 调用show方法
        a.show()
    }
    ... ...
    // 这样不推荐,因为java只能单继承,或者说会影响调用show()方法时候的性能,因为继承会继承父类的所有方法
}
```    

### 2常用设计模式
2.1 基本概念
- 设计模式是一套被反复使用,多数人知晓的,经过分类编目的,设计经验的总结.
- 设计模式就是一种用于固定场合的固定套路

2.2 常用设计模式
单例设计模式

模板设计模式

工厂方法模式:
    当你需要大量创建对象的时候,你就需要创建一个工厂类,然后创建一个工程方法, 这样可以提高程序的可维护性和扩展性
    
抽象工厂模式    

### 3.常用的查找算法()
- 3.1线性查找算法(重中之重)

- 3.2折半查找算法

### 4.常用的排序算法
冒泡排序算法

比较相邻位置的两个元素,若第一个元素比第二个元素大则交换;

从开始的第一对元素一直到结尾的最后一对元素,经过这一轮找到了最大值并放在了最后;

持续对越来越少的元素进行量量比较,直到所有元素不再发生交换为止;