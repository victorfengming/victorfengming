---
title: "Java中接口的多继承"
date: 2021-03-24 10:51:05
cover: "/img/lynk/12.jpg"
tags:
    - java
---



# Java中接口的多继承

[![img](6d33af4a-cc0f-4e11-ac41-d6135f7e6d8e.png)](https://www.jianshu.com/u/3c084cab313c)


我们知道Java的类只能继承一个类，但可以实现多个接口。但是你知道么？Java中的接口却可以继承多个接口。本文就来说一说Java中接口的多继承。

进入主题之前，先扩展一下。Java为什么只支持单继承呢？

我们不妨假设Java支持多继承，举个例子，在这里有个A类，我们又编写了两个类B类和C类，并且B类和C类分别继承了A类，并且对A类的同一个方法进行了覆盖。如果此时我们再次编写了一个D类，并且D类以多继承的方式同时集成了B类和C类，那么D类也会继承B类和C类从A类中重载的方法，如下图所示。那么问题来了，D类也开始犯迷糊了，我到底应该哪个继承哪个类中的方法呢，因为类是结构性的，这样就会造成结构上的混乱。这就是多继承的菱形继承问题。

![img](5679451-43aab94c4bdff320.png)

同时我们知道C++是支持多继承的，因为它解决了这个问题（我对C++不太熟，查了下资料，好像是通过虚基类实现的吧）。但是Java本着简单的原则，舍弃了多继承。

好，进入正题。我们还是举个实例来演示一下接口的多继承。

燕子是鸟，鸟会飞，也会唱歌。我们来模仿一下：

**一、会飞的接口**



```java
package multiex;

public interface Flyable {
    public void fly();
}
```

**二、会唱歌的接口**



```java
package multiex;

public interface Singable  {
    public void sing();
}
```

**三、鸟的接口**
鸟的接口继承上面两个接口



```java
package multiex;
//虽然这个接口没有定义方法，但是会继承下来两个方法
public interface Bird extends Flyable,Singable {

}
```

**四、燕子类，实现鸟接口**



```java
package multiex;

//燕子类
public class Swallow implements Bird {

    @Override
    public void fly() {
        System.out.println("燕子会飞");
        
    }

    @Override
    public void sing() {
        System.out.println("燕子会唱歌");
    }
}
```

**五、测试类**



```java
package multiex;

public class Main {
    
    public static void main(String[] args) {
        Swallow swallow = new Swallow();
        swallow.fly();
        swallow.sing();
    }
}
```

运行结果：



![img](5679451-5200410893ef3a5e.png)

上面演示了接口的多继承，那么这里存在一个问题。如果多个接口中有重名的方法怎么办？比如如下：



```java
package multiex;

interface A {
    void m();
}
//注意：方法返回值不一样
interface B {
    int m();
}

class C implements A, B {
    public void m() {
        System.out.println("void m()");
    }

    public int m() {
        System.out.println("int m()");
    }
}

public class Test {
    public static void main(String[] args) {
        C c1 = new C();
        c1.m();
    }
}
```

这时，编译将无法通过。如下图所示：



![img](5679451-f1a242d24a2186d4.png)

因为在Java中，
**方法名+参数（不含返回值类型）唯一确定一个方法。**
**方法名+参数（不含返回值类型）唯一确定一个方法。**
**方法名+参数（不含返回值类型）唯一确定一个方法。**

所以当返回值不同时，Java认为这还是同一个方法，会与其中一个接口的返回类型冲突。导致编译错误。

同理，当返回值相同时，那这完全就是同一个方法了，实现类实现一次这个方法就好了。如下图：

![img](5679451-17a504ccd13fbb6f.png)

怎么样？同学你懂了没？