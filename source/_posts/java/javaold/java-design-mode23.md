---
title: '23种设计模式汇总整理'
date:       2019-10-16
tags:
	- Java
	- basis
	- summer
---

版权声明：本文为CSDN博主「炸斯特」的原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接及本声明。

原文链接：https://blog.csdn.net/jason0539/article/details/44956775

### 设计模式分为三大类：

<p><span style="color:#333333;"><strong>创建型模式</strong>，共五种：<a href="http://blog.csdn.net/jason0539/article/details/23020989" rel="nofollow" data-token="65341f6416632e8928f1cb4f28ba84dc">工厂方法模式</a>、<a href="http://blog.csdn.net/jason0539/article/details/44976775" rel="nofollow" data-token="ba705163476f7ba1888b5eb7c77a1756">抽象工厂模式</a>、<a href="http://blog.csdn.net/jason0539/article/details/23297037" rel="nofollow" data-token="3cf276cd0c7a9927a5c897ac055364d1">单例模式</a>、<a href="http://blog.csdn.net/jason0539/article/details/44992733" rel="nofollow" data-token="762a8b411ddea056a5714a62cf96ffa7">建造者模式</a>、<a href="http://blog.csdn.net/jason0539/article/details/23158081" rel="nofollow" data-token="a3d2c40eaa10681f49866ca0ddb2a95f">原型模式</a></span></p>

<p><span style="color:#333333;"><strong>结构型模式</strong>，共七种：<a href="http://blog.csdn.net/jason0539/article/details/22468457" rel="nofollow" data-token="594149357bd61da3d0c30e5134992493">适配器模式</a>、<a href="http://blog.csdn.net/jason0539/article/details/22713711" rel="nofollow" data-token="f8c395644e3e802b3e5f97ad1a23e801">装饰者模式</a>、<a href="http://blog.csdn.net/jason0539/article/details/22974405" rel="nofollow" data-token="1ed3eef1b4f4c9cbff2d062e18015830">代理模式</a>、<a href="http://blog.csdn.net/jason0539/article/details/22775311" rel="nofollow" data-token="2de66c42766ed971360fcefdc521d133">外观模式</a>、<a href="http://blog.csdn.net/jason0539/article/details/22568865" rel="nofollow" data-token="60df6a18382fe2ffc0e10fc14e0db6c7">桥接模式</a>、<a href="http://blog.csdn.net/jason0539/article/details/22642281" rel="nofollow" data-token="9554be3e71acd97f8daed4d7911278d6">组合模式</a>、<a href="http://blog.csdn.net/jason0539/article/details/22908915" rel="nofollow" data-token="42c7499405b69fd74792093bfabc5a07">享元模式</a>。</span></p>

<p><span style="color:#333333;"><strong>行为型模式</strong>，共十一种：</span><span style="color:#333333;"><a href="http://blog.csdn.net/jason0539/article/details/45007553" rel="nofollow" data-token="8782115ab39588abcdff2751255fd0a1">策略模式</a>、<a href="http://blog.csdn.net/jason0539/article/details/45037535" rel="nofollow" data-token="01ba7c04b06a4d25708f34c1b64aaac2">模板方法模式</a>、<a href="http://blog.csdn.net/jason0539/article/details/45055233" rel="nofollow" data-token="ede87ced00a8413a68bd03ac5d9acadc">观察者模式</a>、<a href="http://blog.csdn.net/jason0539/article/details/45070441" rel="nofollow" data-token="6e54db68efdc6577bba22716986a97ee">迭代子模式</a>、<a href="http://blog.csdn.net/jason0539/article/details/45091639" rel="nofollow" data-token="d7a67eb2ae9bcc7c411d1dff4884839c">责任链模式</a>、<a href="http://blog.csdn.net/jason0539/article/details/45110355" rel="nofollow" data-token="ca6578abc84fb6c6c445e40a45c9f1c7">命令模式</a>、<a href="http://blog.csdn.net/jason0539/article/details/45126489" rel="nofollow" data-token="db9c9edaa7f7d63f06d6077084aa1a00">备忘录模式</a>、<a href="http://blog.csdn.net/jason0539/article/details/45021055" rel="nofollow" data-token="c58457823044642182d6779ea6d5ff3f">状态模式</a>、<a href="http://blog.csdn.net/jason0539/article/details/45146271" rel="nofollow" data-token="6812d1acd968595cf5c06d403fd895ee">访问者模式</a>、<a href="http://blog.csdn.net/jason0539/article/details/45216585" rel="nofollow" data-token="0bfd29385f0c657f2026931e9129bc1f">中介者模式</a>、解释器模式</span><span style="color:#333333;">。</span></p>

<p><span style="color:#333333;">其实还有两类：并发型模式和线程池模式。</span></p>


## 设计模式的六大原则：

### 总原则－开闭原则

对扩展开放，对修改封闭。在程序需要进行拓展的时候，不能去修改原有的代码，而是要扩展原有代码，实现一个热插拔的效果。所以一句话概括就是：为了使程序的扩展性好，易于维护和升级。

想要达到这样的效果，我们需要使用接口和抽象类等，后面的具体设计中我们会提到这点。

### 1、单一职责原则

不要存在多于一个导致类变更的原因，也就是说每个类应该实现单一的职责，否则就应该把类拆分。

### 2、里氏替换原则（Liskov Substitution Principle）

任何基类可以出现的地方，子类一定可以出现。里氏替换原则是继承复用的基石，只有当衍生类可以替换基类，软件单位的功能不受到影响时，基类才能真正被复用，而衍生类也能够在基类的基础上增加新的行为。

里氏代换原则是对“开-闭”原则的补充。实现“开闭”原则的关键步骤就是抽象化。而基类与子类的继承关系就是抽象化的具体实现，所以里氏代换原则是对实现抽象化的具体步骤的规范。里氏替换原则中，子类对父类的方法尽量不要重写和重载。因为父类代表了定义好的结构，通过这个规范的接口与外界交互，子类不应该随便破坏它。

### 3、依赖倒转原则（Dependence Inversion Principle）

面向接口编程，依赖于抽象而不依赖于具体。写代码时用到具体类时，不与具体类交互，而与具体类的上层接口交互。

### 4、接口隔离原则（Interface Segregation Principle）

每个接口中不存在子类用不到却必须实现的方法，如果不然，就要将接口拆分。使用多个隔离的接口，比使用单个接口（多个接口方法集合到一个的接口）要好。

### 5、迪米特法则（最少知道原则）（Demeter Principle）

一个类对自己依赖的类知道的越少越好。无论被依赖的类多么复杂，都应该将逻辑封装在方法的内部，通过public方法提供给外部。这样当被依赖的类变化时，才能最小的影响该类。

最少知道原则的另一个表达方式是：只与直接的朋友通信。类之间只要有耦合关系，就叫朋友关系。耦合分为依赖、关联、聚合、组合等。我们称出现为成员变量、方法参数、方法返回值中的类为直接朋友。局部变量、临时变量则不是直接的朋友。我们要求陌生的类不要作为局部变量出现在类中。

### 6、合成复用原则（Composite Reuse Principle）

尽量首先使用合成/聚合的方式，而不是使用继承。


