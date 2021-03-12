---
title: 'Java笔记12-函数式接口'
cover: "/img/lynk/38.jpg"
date:       2019-10-29
tags:
	- Java
	- basis
	
---








### 主要内容
- 自定义函数式接口
- 函数式编程
- 常用函数式接口

### 教学目标

- 能够使用@FunctionalInterface注解
- 能够自定义无参无返回值函数式接口
- 能够自定义有参有返回值函数式接口
- 能够理解Lambda延迟执行的特点
- 能够使用Lambda作为方法的参数
- 能够使用Lambda作为方法的返回值
- 能够使用Supplier函数式接口
- 能够使用Consumer函数式接口
- 能够使用Function函数式接口
- 能够使用Predicate函数式接口

# 第一章 函数式接口
### 概念
函数式接口在java中指的是:有且只有一个抽象方法的接口

函数式接口,即适用于函数式编程场景的接口.而java中共的函数式编程体现就是Lambda,所以函数式接口就是可以适用于lambda使用的接口.只有确保接口中有且只有一个宠幸方法,java中的lambda才能顺利地进行推导.

备注:语法糖是指使用更加方便,但是原理不变的代码语法,例如在遍历集合时使用for-each语法,其实底层的实现原理仍然是迭代器,这便是语法糖.从应用应用层面来京,java中的lambda可以被当做是匿名内部类了的语法糖,但是二者原理上是不同的.

    
### 格式
只要确保接口中有且仅有一个抽象方法即可:
```java
修饰符 Interface 接口名称{
    public abstract 返回值类型 方法名称(可选参数信息);
    // 其他非抽象方法内容
}
```    
由于接口当中抽象方法的public abstract 是可以省略的,所以定义一函数式接口很简单:
```java
public Interface MyFunctionalInterface{
    void myMethod();
}
```
### @FunctionalInterface注解
与`@Override`注解的作用类似,Java 8 中专门为函数式接口引入了一个新的注解:`@FunctionInterface`.该注解可用于一个接口的定义上:
```java
@FunctionalInterface
public interface MyFunctionalInterface{
    void myMethod();
}
```
一旦使用该注解来定义接口,编译期将会强制检查该接口是否确实有且仅有一个抽象方法,否则将会报错.需要**注意**的是,即使不使用该注解,主要满足函数式接口的定义,这仍然是一个函数式接口,使用起来都一个B样,只不过`@FunctionalInterface`用起来规范一点,说白了逼格高那么一丢丢

### 自定义函数式接口
对于刚刚定义好的`MyFunctionalInterface`函数式接口,典型使用场景就是作为方法的参数:
```java
public class Demo09FunctionalInterface {
    // 使用自定义的函数式接口作为方法参数
    private static void doSomething(MyFunctionalInterface inter) {
        inter.myMethod(); // 调用自定义的函数式接口方法 
    }
        public static void main (String[]args){
            // 调用使用函数式接口的方法
            doSomething(() ‐ > System.out.println("Lambda执行啦!"));
        }
    }
}
```

# 函数式编程
在兼顾面向对象特性的基础上,Java语言通过Lambda表达式与方法引用等,为开发者打开了函数式编程的大门

下面我们做一个初探
### Lambda的延迟执行
有些场景的代码执行后，结果不一定会被使用，从而造成性能浪费。而Lambda表达式是延迟执行的，这正好可以 作为解决方案，提升性能。
### 性能浪费的日志案例
注:日志可以帮助我们快速的定位问题，记录程序运行过程中的情况，以便项目的监控和优化。 一种典型的场景就是对参数进行有条件使用，例如对日志消息进行拼接后，在满足条件的情况下进行打印输出:
```java
public class Demo01Logger {
       private static void log(int level, String msg) {
           if (level == 1) {
               System.out.println(msg);
} }
       public static void main(String[] args) {
           String msgA = "Hello";
           String msgB = "World";
           String msgC = "Java";
           log(1, msgA + msgB + msgC);
       }
}
```
这段代码存在问题:无论级别是否满足要求，作为 `log` 方法的第二个参数，三个字符串一定会首先被拼接并传入方
法内，然后才会进行级别判断。如果级别不符合要求，那么字符串的拼接操作就白做了，存在性能浪费。
    
备注:SLF4J是应用非常广泛的日志框架，它在记录日志时为了解决这种性能浪费的问题，并不推荐首先进行 字符串的拼接，而是将字符串的若干部分作为可变参数传入方法中，仅在日志级别满足要求的情况下才会进 行字符串拼接。例如: LOGGER.debug("变量{}的取值为{}。", "os", "macOS") ，其中的大括号 {} 为占位 符。如果满足日志级别要求，则会将“os”和“macOS”两个字符串依次拼接到大括号的位置;否则不会进行字 符串拼接。这也是一种可行解决方案，但Lambda可以做到更好。
    
### 体验lambda的更加优化写法    
使用Lambda必然需要一个函数式接口:
```java
@FunctionalInterface
   public interface MessageBuilder {
       String buildMessage();
}
```
然后对 log 方法进行改造:
```java
public class Demo02LoggerLambda {
       private static void log(int level, MessageBuilder builder) {
           if (level == 1) {
               System.out.println(builder.buildMessage());
           } 
       }
       public static void main(String[] args) {
           String msgA = "Hello";
           String msgB = "World";
           String msgC = "Java";
           log(1, () ‐> msgA + msgB + msgC );
       }
}
```
这样一来，只有当级别满足要求的时候，才会进行三个字符串的拼接;否则三个字符串将不会进行拼接。
### 证明lambda的延迟
下面的代码可以通过结果进行验证:
```java
public class Demo03LoggerDelay {
       private static void log(int level, MessageBuilder builder) {
           if (level == 1) {
               System.out.println(builder.buildMessage());
           } 
       }
       public static void main(String[] args) {
           String msgA = "Hello";
           String msgB = "World";
           String msgC = "Java";
           log(2, () ‐> {
               System.out.println("Lambda执行!");
               return msgA + msgB + msgC;
           }); 
       }
}
```
从结果中可以看出，在不符合级别要求的情况下，Lambda将不会执行。从而达到节省性能的效果。 
    
扩展:实际上使用内部类也可以达到同样的效果，只是将代码操作延迟到了另外一个对象当中通过调用方法来完成。而是否调用其所在方法是在条件判断之后才执行的。
    
### 使用Lambda作为参数和返回值    
如果抛开实现原理不说，Java中的`Lambda`表达式可以被当作是匿名内部类的替代品。如果方法的参数是一个函数 式接口类型，那么就可以使用Lambda表达式进行替代。使用Lambda表达式作为方法参数，其实就是使用函数式 接口作为方法参数。
例如 `java.lang.Runnable `接口就是一个函数式接口，假设有一个 `startThread` 方法使用该接口作为参数，那么就 可以使用`Lambda`进行传参。这种情况其实和 `Thread` 类的构造方法参数为 `Runnable` 没有本质区别。
```java
public class Demo04Runnable {
       private static void startThread(Runnable task) {
           new Thread(task).start();
       }
       public static void main(String[] args) {
           startThread(() ‐> System.out.println("线程任务执行!"));
       }       
}
```
类似地，如果一个方法的返回值类型是一个函数式接口，那么就可以直接返回一个Lambda表达式。当需要通过一个方法来获取一个 `java.util.Comparator` 接口类型的对象作为排序器时,就可以调该方法获取。

```java
import java.util.Arrays;
import java.util.Comparator;
public class Demo06Comparator {
       private static Comparator<String> newComparator() {
           return (a, b) ‐> b.length() ‐ a.length();
       }
       public static void main(String[] args) {
           String[] array = { "abc", "ab", "abcd" };
           System.out.println(Arrays.toString(array));
           Arrays.sort(array, newComparator());
           System.out.println(Arrays.toString(array));
        } 
}
```
其中直接return一个Lambda表达式即可
# 常用函数式接口
JDK提供了大量常用的函数式接口以丰富Lambda的典型使用场景，它们主要在 `java.util.function` 包中被提供。 下面是最简单的几个接口及使用示例。
### supplier接口
`java.util.function.Supplier<T> `接口仅包含一个无参的方法: T get() 。用来获取一个泛型参数指定类型的对 象数据。由于这是一个函数式接口，这也就意味着对应的Lambda表达式需要**对外提供**一个符合泛型类型的对象 数据。
```java
import java.util.function.Supplier;
public class Demo08Supplier {
   private static String getString(Supplier<String> function) {
       return function.get();
   }
   public static void main(String[] args) {
       String msgA = "Hello";
       String msgB = "World";
       System.out.println(getString(() ‐> msgA + msgB));
   } 
}
```
### 练习:求数组元素的最大值
题目:
    
使用 Supplier 接口作为方法参数类型，通过Lambda表达式求出int数组中的最大值。提示:接口的泛型请使用 java.lang.Integer 类。
解答:
```java
public class Demo02Test { 
    //定一个方法,方法的参数传递Supplier,泛型使用Integer 
    public static int getMax(Supplier<Integer> sup){
       return sup.get();
    }
    public static void main(String[] args) {
       int arr[] = {2,3,4,52,333,23};
            //调用getMax方法,参数传递Lambda 
       int maxNum = getMax(()‐>{
            //计算数组的最大值 
            int max = arr[0]; for(int i : arr){
                if(i>max){
                   max = i;
                } 
            }
            return max;
       });
       System.out.println(maxNum);
    }
}
```
### Consumer接口
 `java.util.function.Consumer<T> `接口则正好与Supplier接口相反，它不是生产一个数据，而是消费一个数据， 其数据类型由泛型决定。
### 抽象方法:accept
`Consumer` 接口中包含抽象方法 `void accept(T t)` ，意为消费一个指定泛型的数据。基本使用如:
```java
import java.util.function.Consumer;
public class Demo09Consumer {
   private static void consumeString(Consumer<String> function) {
       function.accept("Hello");
   }
   public static void main(String[] args) {
       consumeString(s ‐> System.out.println(s));
   } 
}
```
当然，更好的写法是使用方法引用。
### 默认方法:andThen
如果一个方法的参数和返回值全都是 Consumer 类型，那么就可以实现效果:消费数据的时候，首先做一个操作， 然后再做一个操作，实现组合。而这个方法就是 Consumer 接口中的default方法 andThen 。下面是JDK的源代码:
```java
default Consumer<T> andThen(Consumer<? super T> after) {
       Objects.requireNonNull(after);
       return (T t) ‐> { accept(t); after.accept(t); };
}
```

备注: java.util.Objects 的 requireNonNull 静态方法将会在参数为null时主动抛出 NullPointerException 异常。这省去了重复编写if语句和抛出空指针异常的麻烦。
要想实现组合，需要两个或多个Lambda表达式即可，而 andThen 的语义正是“一步接一步”操作。例如两个步骤组 合的情况:    
```java
import java.util.function.Consumer;
public class Demo10ConsumerAndThen {
   private static void consumeString(Consumer<String> one, Consumer<String> two) {
       one.andThen(two).accept("Hello");
   }
   public static void main(String[] args) {
       consumeString(
            s ‐> System.out.println(s.toUpperCase()),
            s ‐> System.out.println(s.toLowerCase()));
   }
}
```
运行结果将会首先打印完全大写的HELLO，然后打印完全小写的hello。当然，通过链式写法可以实现更多步骤的 组合。

### 练习:格式化打印信息
题目
下面的字符串数组当中存有多条信息，请按照格式“ `姓名:XX。性别:XX。` ”的格式将信息打印出来。要求将打印姓 名的动作作为第一个 `Consumer `接口的Lambda实例，将打印性别的动作作为第二个 `Consumer `接口的Lambda实 例，将两个 `Consumer `接口按照顺序“拼接”到一起。
```java
public static void main(String[] args){
    String[] array = {"迪丽热巴,女","古力娜扎,女","马尔扎哈,男"};
}
```
解答
```java
import java.util.function.Consumer;
public class DemoConsumer {
    public static void main(String[] args) {
        String[] array = { "迪丽热巴,女", "古力娜扎,女", "马尔扎哈,男" };
        printInfo(s ‐> System.out.print("姓名:" + s.split(",")[0]),
        s ‐> System.out.println("。性别:" + s.split(",")[1] + "。"),
        array);
    }
    private static void printInfo(Consumer<String> one, Consumer<String> two, String[] array) {
       for (String info : array) {
    one.andThen(two).accept(info); // 姓名:迪丽热巴。性别:女。 
        }
    } 
}
```

### Predicate接口
有时候我们需要对某种类型的数据进行判断，从而得到一个boolean值结果。这时可以使用
`java.util.function.Predicate<T>` 接口。
### 抽象方法:test
`Predicate` 接口中包含一个抽象方法: `boolean test(T t)` 。用于条件判断的场景:
```java
import java.util.function.Predicate
public class Demo15PredicateTest {
       private static void method(Predicate<String> predicate) {
            boolean veryLong = predicate.test("HelloWorld");
            System.out.println("字符串很长吗:" + veryLong); 
       }
       public static void main(String[] args) {
           method(s ‐> s.length() > 5);
       } 
}
```
条件判断的标准是传入的Lambda表达式逻辑，只要字符串长度大于5则认为很长。
### 默认方法:and
既然是条件判断，就会存在与、或、非三种常见的逻辑关系。其中将两个 Predicate 条件使用“与”逻辑连接起来实 现“**并且**”的效果时，可以使用default方法 and 。其JDK源码为:
```java
default Predicate<T> and(Predicate<? super T> other) {
       Objects.requireNonNull(other);
       return (t) ‐> test(t) && other.test(t);
}
```
如果要判断一个字符串既要包含大写“H”，又要包含大写“W”，那么:
```java
import java.util.function.Predicate;
public class Demo16PredicateAnd {
   private static void method(Predicate<String> one, Predicate<String> two) {
       boolean isValid = one.and(two).test("Helloworld");
       System.out.println("字符串符合要求吗:" + isValid); 
   }
   public static void main(String[] args) {
       method(s ‐> s.contains("H"), s ‐> s.contains("W"));
   } 
}
```
### 默认方法:or
与 `and` 的“与”类似，默认方法 `or` 实现逻辑关系中的“或”。JDK源码为:
```java
default Predicate<T> or(Predicate<? super T> other) {
       Objects.requireNonNull(other);
       return (t) ‐> test(t) || other.test(t);
}
```
如果希望实现逻辑“字符串包含大写H或者包含大写W”，那么代码只需要将“and”修改为“or”名称即可，其他都不变:
```java
import java.util.function.Predicate;
public class Demo16PredicateAnd {
   private static void method(Predicate<String> one, Predicate<String> two) {
       boolean isValid = one.or(two).test("Helloworld");
       System.out.println("字符串符合要求吗:" + isValid); 
   }
   public static void main(String[] args) {
       method(s ‐> s.contains("H"), s ‐> s.contains("W"));
   } 
}
```
### 默认方法:negate
“与”、“或”已经了解了，剩下的“非”(取反)也会简单。默认方法 negate 的JDK源代码为
```java
default Predicate<T> negate() {
       return (t) ‐> !test(t);
}
```
从实现中很容易看出，它是执行了test方法之后，对结果boolean值进行“!”取反而已。一定要在 `test` 方法调用之前
调用 `negate` 方法，正如 `and` 和 `or` 方法一样:
```java
import java.util.function.Predicate;
public class Demo17PredicateNegate {
   private static void method(Predicate<String> predicate) {
       boolean veryLong = predicate.negate().test("HelloWorld");
       System.out.println("字符串很长吗:" + veryLong); 
   }
   public static void main(String[] args) {
       method(s ‐> s.length() < 5);
} 
}
```
### 练习:集合信息筛选 题目
数组当中有多条“姓名+性别”的信息如下，请通过 Predicate 接口的拼装将符合要求的字符串筛选到集合 ArrayList 中，需要同时满足两个条件:
- 1. 必须为女生; 
- 2. 姓名为4个字。

```java
public class DemoPredicate {
       public static void main(String[] args) {
            String[] array = { "迪丽热巴,女", "古力娜扎,女", "马尔扎哈,男", "赵丽颖,女" }; 
       }
}
```
解答
```java
import java.util.ArrayList;
import java.util.List;
import java.util.function.Predicate;
public class DemoPredicate {
   public static void main(String[] args) {
        String[] array = { "迪丽热巴,女", "古力娜扎,女", "马尔扎哈,男", "赵丽颖,女" }; List<String> list = filter(array,
        s ‐> "女".equals(s.split(",")[1]),
        s ‐> s.split(",")[0].length() == 4);
        System.out.println(list);
   }
   private static List<String> filter(String[] array, Predicate<String> one,
                                      Predicate<String> two) {
       List<String> list = new ArrayList<>();
       for (String info : array) {
           if (one.and(two).test(info)) {
               list.add(info);
           } 
       }
       return list;
   }
}
```
