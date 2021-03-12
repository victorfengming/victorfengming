---
layout:     post
title:      "java虚拟机的内存分配和垃圾回收"
cover: "/img/lynk/59.jpg"
date:       2021-03-09
author:     "victor"
tags:
    - jvm
    - java
---











## 1.为什么会有JAVA虚拟机？
java源程序.java文件经过javac编译成.class文件，.class文件将由java虚拟机，解释成机器码（不同平台的机器码不同），利用机器码操作硬件和操作系统

## 2.什么是JAVA虚拟机？
java虚拟机是执行.class（字节码）文件的虚拟（机）程序进程，ps:我自己把它理解成window系统的一个进程,这个进程其实就相当于一个虚拟机（java虚拟机）

## 3.为什么我们要学习JAVA虚拟机
日常的的开发中，我们只关注于写java代码，而并没有关心java虚拟机的相关操作，而未了进一步提升自己，对Java语言的深入理解，并对未来的如果出现内存溢出等问题奠定基础，还有个目的是为了面试\(^o^)/ 

## 4.JAVA虚拟机的体系结构

![img](20190810220710364.jpg)

图中画区域的是所有线程所共享的（方法区，堆，执行引擎，本地接口）

### 方法区

方法区（Method Area）：方法区是各个线程共享的区域，用于存储已经被虚拟机加载的类信息（即加载类时需要加载的信息，包括版本、field、方法、接口等信息）、final常量、静态变量、编译器即时编译的代码等。

关于方法区不太理解的，我稍后写些例子。。。。

### 堆

堆（heap）:也叫java堆。在JVM所管理的内存中，堆区是最大的一块，堆区也是Java GC机制所管理的主要内存区域，堆区由所有线程共享，在虚拟机启动时创建。堆区的存在是为了存储对象实例，原则上讲，所有的对象都在堆区上分配内存。比如new出来的对象、方法的成员变量。

一般的，根据Java虚拟机规范规定，堆内存需要在逻辑上是连续的（在物理上不需要），在实现时，可以是固定大小的，也可以是可扩展的，目前主流的虚拟机都是可扩展的。如果在执行垃圾回收之后，仍没有足够的内存分配，也不能再扩展，将会抛出OutOfMemoryError:Java heap space异常。

### 虚拟机栈

虚拟机栈（JVM Stack）：也叫java栈。一个线程的每个方法在执行的同时，都会创建一个栈帧（Statck Frame），栈帧中存储的有局部变量表、操作站、动态链接、方法出口等，当方法被调用时，栈帧在JVM栈中入栈，当方法执行完成时，栈帧出栈。

局部变量表中存储着方法的相关局部变量，包括各种基本数据类型，对象的引用，返回地址等。在局部变量表中，只有long和double类型会占用2个局部变量空间（Slot，对于32位机器，一个Slot就是32个bit），其它都是1个Slot。需要注意的是，局部变量表是在编译时就已经确定好的，方法运行所需要分配的空间在栈帧中是完全确定的，在方法的生命周期内都不会改变。

　　虚拟机栈中定义了两种异常，如果线程调用的栈深度大于虚拟机允许的最大深度，则抛出StatckOverFlowError（栈溢出）；不过多数Java虚拟机都允许动态扩展虚拟机栈的大小(有少部分是固定长度的)，所以线程可以一直申请栈，直到内存不足，此时，会抛出OutOfMemoryError（内存溢出）。

　　每个线程对应着一个虚拟机栈，因此虚拟机栈也是线程私有的。

### 本地方法区

本地方法区（Native Method Statck）：本地方法栈在作用，运行机制，异常类型等方面都与虚拟机栈相同，唯一的区别是：虚拟机栈是执行Java方法的，而本地方法栈是用来执行native方法的，在很多虚拟机中（如Sun的JDK默认的HotSpot虚拟机），会将本地方法栈与虚拟机栈放在一起使用。

本地方法栈也是线程私有的。

### 程序计数器

程序计数器（Program Counter Register）：程序计数器是一个比较小的内存区域，用于指示当前线程所执行的字节码执行到了第几行，可以理解为是当前线程的行号指示器。字节码解释器在工作时，会通过改变这个计数器的值来取下一条语句指令。

　　每个程序计数器只用来记录一个线程的行号，所以它是线程私有（一个线程就有一个程序计数器）的。

　　如果程序执行的是一个Java方法，则计数器记录的是正在执行的虚拟机字节码指令地址；如果正在执行的是一个本地（native，由C语言编写完成）方法，则计数器的值为Undefined，由于程序计数器只是记录当前指令地址，所以不存在内存溢出的情况，因此，程序计数器也是所有JVM内存区域中唯一一个没有定义OutOfMemoryError的区域。

## 5**.为什么要进行垃**圾回收

   程序在进行方法调用的时候，在堆中不停的开辟内存，直到内存OutOfMemoryError（内存溢出）。

## **6.什么对象需要垃圾回收**
Java堆和方法区是“线程共享”的，随着虚拟机的启动而存在，这部分内存的分配和回收是动态的，我们只有在程序运行时才知道创建了哪些对象，需要多少内存，GC针对的就是这部分内存的回收                                                                                         

java栈，本地方法栈，程序计数器都是线程私有的，随着线程生而生，灭而灭，所以不参与垃圾回收

1. 当程序运行时，首先通过类装载器加载字节码文件，经过解析后装入方法区！在方法区中存了类的各种信息，包括类变量、类常量及方法。对于同一个方法的调用，同一个类的不同实例调用的都是存在方法区的同一个方法。类变量的生命周期从程序开始运行时创建，到程序终止运行时结束！ 
1. 当程序中new一个对象时，这个对象存在堆中，对象的变量存在栈中，指向堆中的引用！对象的成员变量都存在堆中，当对象被回收时，对象的成员变量随之消失！ 
1. 当方法调用时，JVM会在栈中分配一个栈桢，存储方法的局部变量。当方法调用结束时，局部变量消失！

类变量：属于类的属性信息，与类的实例无关，多个实例共用同一个类变量，存在与方法区中。类变量用static修饰，包括静态变量和常量。静态变量有默认初始值，常量必须声明同时初始化。成员变量：属于实例的变量，只与实例有关，写在类下面，方法外，非static修饰。成员变量会随着成员的创建而生存，随着成员的回收而销毁。

局部变量：声明在方法中，没有默认初始值，随着方法的调用而创建，存储于栈中，随着方法调用的结束而销毁


## 7.什么时间回收

​    如果对象在申请空间的时候，空间不足，就会触发垃圾回收，如果还有空间，暂时不会进行垃圾回收

## 8.如何判断要垃圾回收

   **引用计数法：**给对象添加一个引用计数器，每当有一个地方引用它，计数器就+1,；当引用失效时，计数器就-1；任何时刻计数器都为0的对象就是不能再被使用

![img](aHR0cHM6Ly91c2VyLWdvbGQtY2RuLnhpdHUuaW8vMjAxNy85LzQvNGMyODlhMjI0Y2I0OTQ0ZTQ5OWZiNWJmZDMzZTU5MmY_aW1hZ2VWaWV3Mi8wL3cvMTI4MC9oLzk2MC9mb3JtYXQvd2VicC9pZ25vcmUtZXJyb3IvMQ.webp)

从图中可以看出，如果不下小心直接把 Obj1-reference 和 Obj2-reference 置 null。则在 Java 堆当中的两块内存依然保持着互相引用无法回收。

**可达性分析算法：**通过一系列的名为“GC Roots”的对象作为起始点，从这些节点开始向下搜索，搜索所走过的路径称为引用链（Reference Chain），当一个对象到 GC Roots 没有任何引用链相连时，则证明此对象是不可用的。

![img](aHR0cHM6Ly91c2VyLWdvbGQtY2RuLnhpdHUuaW8vMjAxNy85LzQvNThiZmFjMTVjYTZkMzA3NmRlZjUxNzRlZDVjYTVhOTk_aW1hZ2VWaWV3Mi8wL3cvMTI4MC9oLzk2MC9mb3JtYXQvd2VicC9pZ25vcmUtZXJyb3IvMQ.webp)

在java中可以作为GC Roots的对象有以下几种：

1. 虚拟机栈中引用的对象
2. 方法区中类静态属性引用的对象
3. 方法区中常量引用的对象
4. 本地方法栈中JNI（Native方法）引用的对象

 引用分类

无论是引用计数法还是可达性分析算法，判断是否存活都与“引用”有关。在JDK1.2之后分为  强引用、软引用、弱引用、虚引用。

强引用（strong Reference）  就是普通的new对象引用  比如：String str =new String("hello World");只要引用一直被调用，jvm哪怕是抛出内存溢出也不会回收这个对象。

软引用(softReference)  用来描述一些不必须的对象。当jvm内存吃紧的时候，才会回收这个对象，如果内存还是不够，就会抛出内存溢出异常。

弱引用（weakReference）比软引用还要弱，只要进行垃圾回收，就被回收掉。

虚引用（PhantomReference ）无法通过虚引用获取一个对象的实例，为一个对象设置虚引用关联的唯一目的就是能在这个对象被收集器回收时收到一个系统通知。


# 9.垃圾回收算法
 标记-清除算法（mark-sweep）

定义：分为标记和清除两个阶段。首先标记出所有需要回收的对象，在标记完成后统一回收被标记的对象。 
地位：是最基础的垃圾回收算法，后面的几种垃圾回收算法都是基于这种思路并对其不足进行改进而得到的。 
缺点： 
   - 效率问题。标记和清除过程的效率都不高。 
   - 空间问题。标记清除之后会产生大量不连续的内存碎片，空间碎片太多可能导致，程序分配较大对象时无法找到足够              的连续内存，不得不提前出发另一次垃圾收集动作。


![MarkdownPhotos/master/CSDNBlogs/JVM/mark-sweep.png](aHR0cHM6Ly9yYXcuZ2l0aHVidXNlcmNvbnRlbnQuY29tL3BhbndlaWkvTWFya2Rvd25QaG90b3MvbWFzdGVyL0NTRE5CbG9ncy9KVk0vbWFyay1zd2VlcC5wbmc.png)



**复制算法（copying）**

定义：将可用内存按容量划分为大小相等的两块，每次只使用其中一块。当这一块的内存用完了，就将存活着的对象复制到         另一块上面，然后再把已经使用过的内存空间一次清理掉。 
优点：解决了标记-清除算法的效率问题。复制算法使得每次都是针对其中的可用内存的半区进行内存回收，内存分配时也           不用考虑内存碎片等复杂情况，只要移动堆顶指针，按顺序分配内存即可，实现简单，运行高效。 
缺点： 
 - 浪费空间。将内存缩小为原来的一半，代价太高昂。 
 - 效率问题。在对象存活率较高时，需要执行较多的复制操作，效率会变低。 
应用：回收新生代 
     现在的商用虚拟机都采用这种算法来回收新生代。因为新生代中的对象大部分很快就死亡，所以并不需要按照1:1的比例划分内存空间，而是将内存分为一块较大的 Eden 空间和两块较小的 Survivor 空间。每次使用 Eden 和其中的一块 Survivor。当回收时，将 Eden 和 Survivor 中还存活的对象一次性拷贝到另外一块 Survivor 空间上，最后清理掉 Eden 和刚才用过的 Survivor 空间。Hotspot 虚拟机默认 Eden 和 Survivor 的大小比例是8:1，也就是每次新生代中可用内存空间为整个新生代容量的90%（80% + 10%），只有10%的内存是会被“浪费”的。当然，无法保证每次回收都只有不多于10%的对象存活，如果10%的Survivor 空间不够用，可以临时使用老年代的内存。


![img](20190811085633283.png)

 **标记整理算法**（mark-compact）

  定义：标记过程仍然与“标记-清除”算法一样，但后续步骤不是直接对可回收对象进行清理，而是让所有存活的对象向一端移动，然后直接清理掉边界以外的内存。 

 优点：解决了复制算法的空间和效率问题。 
  应用：现在的商用虚拟机都采用这种算法来**回收老年代**。 

![MarkdownPhotos/master/CSDNBlogs/JVM/mark-compact.png](aHR0cHM6Ly9yYXcuZ2l0aHVidXNlcmNvbnRlbnQuY29tL3BhbndlaWkvTWFya2Rvd25QaG90b3MvbWFzdGVyL0NTRE5CbG9ncy9KVk0vbWFyay1jb21wYWN0LnBuZw.png)

分代收集算法（Generational Collection）**

      定义：根据对象的存活周期的不同将内存划分为几块。一般是把 Java 堆分为新生代和老年代，这样就可以根据各个年代的特点，采用最适当的收集算法。对于新生代，每次垃圾收集时会有大批对象死去，只有少量存活，所以选择复制算法，只需要少量存活对象的复制成本就可以完成收集。对于老年代，对象存活率高、没有额外空间对它进行分配担保，必须使用“标记-清理”或“标记-整理”算法进行回收。 
      优点：可以根据实际情况选择具体的算法 
      应用：现在的商用虚拟机的垃圾回收都采用这种算法。


​     

上面我已经讲到了JAVA垃圾回收针对的主要是java堆的回收，下面说明下java堆的分代回收

**java堆分为，年轻代，老年代，和永久代，在java8中，将永久代替换成了元空间（Metespace）**

![img](aHR0cHM6Ly93d3cuY29kZXI0LmNvbS93cC1jb250ZW50L3VwbG9hZHMvMjAxOC8wMy8xLmpwZw.jfif)

**新生代**
主要用来存储新创建的对象，内存较小，MinorGC频繁。新生代又分为三个区域：Eden、ServivorFrom、ServivorTo。 
Eden：当对象在堆创建时，一般进入Eden。如果新创建的对象占用内存很大，则直接分配到老年代。当Eden区内存不够时会触发MinorGC，对新生代区进行一次垃圾回收。 
ServivorFrom：上一次GC的幸存者，作为这一次MinorGC的被扫描者。 
ServivorTo：保留了这一次MinorGC后的幸存者。 
MinorGC：采用复制算法。 

1. 扫描Eden和ServivorFrom，将存活的对象复制到ServivorTo，并将这些对象的年龄+1。（如果ServivorTo已经满，则复制到老年代。） 
2. 扫描ServivorFrom时，如果对象已经经过了几次的扫描仍然存活，达到了老年代的标准，JVM会将其移到老年代。 
3. 扫描完毕后，清空Eden和ServivorFrom，然后交换ServivorFrom和ServivorTo，即ServicorTo成为下一次GC时的ServicorFrom区。


![img](aHR0cHM6Ly93d3cuY29kZXI0LmNvbS93cC1jb250ZW50L3VwbG9hZHMvMjAxOC8wMy8yLmpwZw.jfif)

**老年代**
主要用来存储长时间被引用的对象。它里面存放的是经过几次在新生代进行扫描仍存活的对象。因为老年代对象比较稳定，所以MajorGC频率较小。 
MajorGC：采用标记-整理算法。

在进行MajorGC前一般都先进行了一次MinorGC，使得有新生代的对象晋身入老年代，导致空间不够用时才触发。当无法找到足够大的连续空间分配给新创建的较大对象时也会提前触发一次MajorGC进行垃圾回收腾出空间。

MajorGC的耗时比较长，因为要扫描再回收。MajorGC会产生内存碎片，为了减少内存损耗，我们一般需要进行合并或者标记出来方便下次直接分配。

当老年代也满了装不下的时候，就会抛出OOM（Out of Memory）异常。

原文链接：https://blog.csdn.net/sinat_34454743/article/details/99116013

**永久代**
主要用来存储类元数据信息，如类定义、字节码和常量等。GC不会在主程序运行期对永久代进行清理。Class在被加载的时候被放入永久区域。它和和存放实例的区域不同，GC不会在主程序运行期对永久区域进行清理。所以这也导致了永久代会随着加载的Class的增多而胀满，最终抛出OOM异常。在Java8中，永久代已被元空间取代。再启动JVM时，如果JVM设置了PermSize 和 MaxPermSize 两个参数，参数会被忽略并给出警告。

**元空间**
元空间并不在虚拟机中，而是使用本地内存来存储类元数据信息。因此，默认情况下，元空间的大小仅受本地内存限制。类的元数据放入 native memory, 字符串池和类的静态变量放入java堆中. 这样可以加载多少类的元数据就不再由MaxPermSize控制, 而由系统的实际可用空间来控制。

          注意：堆=新生代+老年代，不包括永久代（方法区）


很多人认为方法区（或者HotSpot虚拟机中的永久代）是没有垃圾收集的，Java虚拟机规范中确实说过可以不要求虚拟机在方法区实现垃圾收集，而且在方法区进行垃圾收集的“性价比”一般比较低：在堆中，尤其是在新生代中，常规应用进行一次垃圾收集一般可以回收70%~95%的空间，而永久代的垃圾收集效率远低于此。

永久代的垃圾收集主要回收两部分内容：废弃常量和无用的类。回收废弃常量与回收Java堆中的对象非常类似。以常量池中字面量的回收为例，假如一个字符串“abc”已经进入了常量池中，但是当前系统没有任何一个String对象是叫做“abc”的，换句话说是没有任何String对象引用常量池中的“abc”常量，也没有其他地方引用了这个字面量，如果在这时候发生内存回收，而且必要的话，这个“abc”常量就会被系统“请”出常量池。常量池中的其他类（接口）、方法、字段的符号引用也与此类似。

判定一个常量是否是“废弃常量”比较简单，而要判定一个类是否是“无用的类”的条件则相对苛刻许多。类需要同时满足下面3个条件才能算是“无用的类”：

该类所有的实例都已经被回收，也就是Java堆中不存在该类的任何实例。

加载该类的ClassLoader已经被回收。

该类对应的java.lang.Class 对象没有在任何地方被引用，无法在任何地方通过反射访问该类的方法。

## 10.垃圾收集器

```
收集算法是内存回收的理论，而垃圾回收器是内存回收的实践
```

![img](aHR0cHM6Ly91c2VyLWdvbGQtY2RuLnhpdHUuaW8vMjAxNy85LzQvMTVmYjc1NDc2MmZmNWRmM2Y3ZjYzZTVjMjZkNGQzYWU_aW1hZ2VWaWV3Mi8wL3cvMTI4MC9oLzk2MC9mb3JtYXQvd2VicC9pZ25vcmUtZXJyb3IvMQ.webp)

**Serial 收集器**

```
这是一个单线程收集器。意味着它只会使用一个 CPU 或一条收集线程去完成收集工作，并且在进行垃圾回收时必须暂停其它所有的工作线程直到收集结束。
```

  ![img](https://imgconvert.csdnimg.cn/aHR0cHM6Ly91c2VyLWdvbGQtY2RuLnhpdHUuaW8vMjAxNy85LzQvYjE4NDk0YjFlNTQ4NTFiYmJkMmVlNTI3NjBjYzM3NTQ_aW1hZ2VWaWV3Mi8wL3cvMTI4MC9oLzk2MC9mb3JtYXQvd2VicC9pZ25vcmUtZXJyb3IvMQ)

**特性**

针对新生代；
采用复制算法；
单线程收集：这个收集器是一个单线程的收集器。“单线程”的意义并不仅仅说明它只会使用一个CPU或一条收集线程去完成垃圾收集工作，更重要的是在它进行垃圾收集时，必须暂停其他所有的工作线程，直到它收集结束。
**应用场景** 
Serial收集器是虚拟机运行在Client模式下的默认新生代收集器。

**优势** 
简单而高效（与其他收集器的单线程比），对于限定单个CPU的环境来说，Serial收集器由于没有线程交互的开销，专心做垃圾收集自然可以获得最高的单线程收集效率。

**参数** 
-XX:+UseSerialGC。Jvm运行在Client模式下的默认值，打开此开关后，使用Serial + Serial Old的收集器组合进行内存回收。



**ParNew收集器**

![img](aHR0cHM6Ly91c2VyLWdvbGQtY2RuLnhpdHUuaW8vMjAxNy85LzQvMTU0NjVmYjJlMTdjYjVkNjY1YzI1YmI5OGFjZmVhOTM_aW1hZ2VWaWV3Mi8wL3cvMTI4MC9oLzk2MC9mb3JtYXQvd2VicC9pZ25vcmUtZXJyb3IvMQ.webp)

**特性** 
ParNew收集器其实就是Serial收集器的多线程版本，除了使用多条线程进行垃圾收集之外，其余行为包括Serial收集器可用的所有控制参数、收集算法、Stop The World、对象分配规则、回收策略等都与Serial收集器完全一样，在实现上，这两种收集器也共用了相当多的代码。

**应用场景** 
1.ParNew收集器是许多运行在Server模式下的虚拟机中首选的新生代收集器。 
除了Serial收集器外，目前只有它能与CMS收集器配合工作。 
在JDK 1.5时期，HotSpot推出了一款在强交互应用中几乎可认为有划时代意义的垃圾收集器——CMS收集器，这款收集器是HotSpot虚拟机中第一款真正意义上的并发收集器，它第一次实现了让垃圾收集线程与用户线程同时工作。 
不幸的是，CMS作为老年代的收集器，却无法与JDK 1.4.0中已经存在的新生代收集器Parallel Scavenge配合工作，所以在JDK 1.5中使用CMS来收集老年代的时候，新生代只能选择ParNew或者Serial收集器中的一个。

**优势**

多线程 
-除了Serial收集器外，目前只有它能与CMS收集器配合工作。
参数

-XX:+UseConcMarkSweepGC：指定使用CMS后，会默认使用ParNew作为新生代收集器
-XX:+UseParNewGC：强制指定使用ParNew
-XX:ParallelGCThreads：指定垃圾收集的线程数量，ParNew默认开启的收集线程与CPU的数量相同





**Serial收集器与ParNew收集器** 
ParNew收集器在单CPU的环境中绝对不会有比Serial收集器更好的效果，甚至由于存在线程交互的开销，该收集器在通过超线程技术实现的两个CPU的环境中都不能百分之百地保证可以超越Serial收集器。然而，随着可以使用的CPU的数量的增加，它对于GC时系统资源的有效利用还是很有好处的。

Parallel Scaveage收集器



```
这是一个新生代收集器，也是使用复制算法实现，同时也是并行的多线程收集器。
```

![img](https://imgconvert.csdnimg.cn/aHR0cHM6Ly91c2VyLWdvbGQtY2RuLnhpdHUuaW8vMjAxNy85LzQvMjU2NDEzNjZiNDNkOTcxMzEwYTBhN2NlZGU0ZTQwNmE_aW1hZ2VWaWV3Mi8wL3cvMTI4MC9oLzk2MC9mb3JtYXQvd2VicC9pZ25vcmUtZXJyb3IvMQ)

**特性**

新生代收集器；
采用复制算法；
多线程收集；
看上去和ParNew收集器一样，它有什么特别之处呢？ 
Parallel Scavenge收集器的特点是它的关注点与其他收集器不同，CMS等收集器的关注点是尽可能地缩短垃圾收集时用户线程的停顿时间，而Parallel Scavenge收集器的目标则是达到一个可控制的吞吐量（Throughput）。 
吞吐量就是CPU用于运行用户代码的时间与CPU总消耗时间的比值，即吞吐量 = 运行用户代码时间 /（运行用户代码时间 + 垃圾收集时间）。 
虚拟机总共运行了100分钟，其中垃圾收集花掉1分钟，那吞吐量就是99%。

**应用场景** 
高吞吐量则可以高效率地利用CPU时间，尽快完成程序的运算任务，主要适合在后台运算而不需要太多交互的任务。

**优势** 
参考特性和应用场景。

**参数**

-XX:+UseParallelGC：Jvm运行在Server模式下的默认值，打开此开关后，使用Parallel Scavenge + Serial Old的收集器组合进行回收；
-XX:+UseParallelOldGC：使用Parallel Scavenge + Parallel Old的收集器组合进行回收；
Parallel Scavenge收集器提供两个参数用于精确控制吞吐量：

-XX:MaxGCPauseMillis。用于控制最大垃圾收集停顿时间。
-XX:GCTimeRatio。设置吞吐量大小
-XX:+UseAdaptiveSizePolicy。开启自适应调节策略。
————————————————

 **GC自适应的调节策略**  

Parallel Scavenge收集器有一个参数-XX:+UseAdaptiveSizePolicy。当这个参数打开之后，就不需要手工指定新生代的大小（-Xmn）、Eden与Survivor区的比例（-XX：SurvivorRatio）、晋升老年代对象年龄（-XX：PretenureSizeThreshold）等细节参数了，虚拟机会根据当前系统的运行情况收集性能监控信息，动态调整这些参数以提供最合适的停顿时间或者最大的吞吐量，这种调节方式称为GC自适应的调节策略（GC Ergonomics）。 
如果对垃圾收集器不太了解，手动优化困难，这是一种值得推荐的方式。

只需要把基本的内存数据设置好（如-Xmx设置最大堆）；
然后使用-XX:MaxGCPauseMillis或-XX:GCTimeRatio给JVM设置一个优化目标；
那些具体细节参数的调节就由JVM自适应完成。



**Serial Old收集器**

```
Serial Old是 Serial收集器的老年代版本
```

![img](aHR0cHM6Ly91c2VyLWdvbGQtY2RuLnhpdHUuaW8vMjAxNy85LzQvYjE4NDk0YjFlNTQ4NTFiYmJkMmVlNTI3NjBjYzM3NTQ_aW1hZ2VWaWV3Mi8wL3cvMTI4MC9oLzk2MC9mb3JtYXQvd2VicC9pZ25vcmUtZXJyb3IvMQ.webp)

**特性**

针对老年代；
采用”标记-整理”算法；
单线程收集；
应用场景

Client模式。主要用于Client模式。
Server模式。Server模式有两大用途： 
在JDK1.5及之前的版本中与Parallel Scavenge收集器搭配使用
作为CMS收集器的后备预案，在并发收集发生Concurrent Mode Failure时使用。

**参数** 
-XX:+UseSerialGC。Jvm运行在Client模式下的默认值，打开此开关后，使用Serial + Serial Old的收集器组合进行内存回收。 

**Parallel Old收集器**

```
Parallel Old 是 Parallel Scavenge 收集器的老年代版本。多线程，使用 标记 —— 整理
```

![img](aHR0cHM6Ly91c2VyLWdvbGQtY2RuLnhpdHUuaW8vMjAxNy85LzQvMjU2NDEzNjZiNDNkOTcxMzEwYTBhN2NlZGU0ZTQwNmE_aW1hZ2VWaWV3Mi8wL3cvMTI4MC9oLzk2MC9mb3JtYXQvd2VicC9pZ25vcmUtZXJyb3IvMQ.webp)



**CMS 收集器**

```
CMS (Concurrent Mark Sweep) 收集器是一种以获取最短回收停顿时间为目标的收集器。基于 标记 —— 清除 算法实现。
```

** **运作步骤** **

 初始标记(CMS initial mark)：标记 GC Roots 能直接关联到的对象
并发标记(CMS concurrent mark)：进行 GC Roots Tracing
重新标记(CMS remark)：修正并发标记期间的变动部分
并发清除(CMS concurrent sweep)

![img](aHR0cHM6Ly91c2VyLWdvbGQtY2RuLnhpdHUuaW8vMjAxNy85LzQvNmY0ZDY4MzY0NGExNTQ1MzdiM2UyM2Q2MGQ0OWMwNzQ_aW1hZ2VWaWV3Mi8wL3cvMTI4MC9oLzk2MC9mb3JtYXQvd2VicC9pZ25vcmUtZXJyb3IvMQ.webp) 

缺点：对 CPU 资源敏感、无法收集浮动垃圾、`标记 —— 清除` 算法带来的空间碎片

**G1 收集器**

```
面向服务端的垃圾回收器。
```

优点：并行与并发、分代收集、空间整合、可预测停顿。

运作步骤:

初始标记(Initial Marking)
并发标记(Concurrent Marking)
最终标记(Final Marking)
筛选回收(Live Data Counting and Evacuation)

![img](aHR0cHM6Ly91c2VyLWdvbGQtY2RuLnhpdHUuaW8vMjAxNy85LzQvNDBhNTc1OTMxYjI1NGE4ZjQwYmI1NDNjMjRlOGZhZGY_aW1hZ2VWaWV3Mi8wL3cvMTI4MC9oLzk2MC9mb3JtYXQvd2VicC9pZ25vcmUtZXJyb3IvMQ.webp)

**垃圾收集器比较**

![img](20190811101310488.png)

上图摘自https://blog.csdn.net/panweiwei1994/article/details/79111432

垃圾收集器参数总结

-XX:+<option> 启用选项
-XX:-<option> 不启用选项
-XX:<option>=<number>
-XX:<option>=<string>

![img](20190811101505207-1615211442360.png)



上图摘自https://blog.csdn.net/panweiwei1994/article/details/79111432
