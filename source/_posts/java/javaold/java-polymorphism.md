---
title: 'Java中的多态'
cover: "/img/lynk/59.jpg"
date:       2019-10-11
tags:
	- Java
	- basis
	- oop
---

<div class="content-intro view-box "><h3>Java 多态</h3> <hr> <p>多态是同一个行为具有多个不同表现形式或形态的能力。 </p> <p>多态性是对象多种表现形式的体现。</p> <p> 比如我们说"宠物"这个对象，它就有很多不同的表达或实现，比如有小猫、小狗、蜥蜴等等。那么我到宠物店说"请给我一只宠物"，服务员给我小猫、小狗或者蜥蜴都可以，我们就说"宠物"这个对象就具备多态性。 </p> <p>接下来让我们通过实例来了解Java的多态。</p> <h4>例子</h4> <pre lang="java"><code class="java hljs"><span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">interface</span> <span class="hljs-title">Vegetarian</span></span>{}
<span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Animal</span></span>{}
<span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Deer</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Animal</span> <span class="hljs-keyword">implements</span> <span class="hljs-title">Vegetarian</span></span>{}
</code></pre> <p> 因为Deer类具有多重继承，所以它具有多态性。以上实例解析如下： </p> <ul> <li> 一个 Deer IS-A（是一个） Animal</li> <li> 一个 Deer IS-A（是一个） Vegetarian</li> <li> 一个 Deer IS-A（是一个） Deer</li> <li> 一个 Deer IS-A（是一个）Object</li> </ul> <p>在Java中，所有的对象都具有多态性，因为任何对象都能通过IS-A测试的类型和Object类。</p><p> 访问一个对象的唯一方法就是通过引用型变量。</p><p> 引用型变量只能有一种类型，一旦被声明，引用型变量的类型就不能被改变了。</p><p> 引用型变量不仅能够被重置为其他对象，前提是这些对象没有被声明为final。还可以引用和它类型相同的或者相兼容的对象。它可以声明为类类型或者接口类型。</p> <p>当我们将引用型变量应用于Deer对象的引用时，下面的声明是合法的： </p> <pre lang="java"><code class="java hljs">Deer d = <span class="hljs-keyword">new</span> Deer();
Animal a = d;
Vegetarian v = d;
Object o = d;
</code></pre> <p>所有的引用型变量d,a,v,o都指向堆中相同的Deer对象。</p> <hr> <h3>虚方法</h3> <p>我们将介绍在Java中，当设计类时，被重写的方法的行为怎样影响多态性。</p><p> 我们已经讨论了方法的重写，也就是子类能够重写父类的方法。</p><p> 当子类对象调用重写的方法时，调用的是子类的方法，而不是父类中被重写的方法。</p><p> 要想调用父类中被重写的方法，则必须使用关键字super。</p> <pre lang="java"><code class="java hljs"><span class="hljs-comment">/* 文件名 : Employee.java */</span>
<span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Employee</span>
</span>{
   <span class="hljs-keyword">private</span> String name;
   <span class="hljs-keyword">private</span> String address;
   <span class="hljs-keyword">private</span> <span class="hljs-keyword">int</span> number;
   <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-title">Employee</span><span class="hljs-params">(String name, String address, <span class="hljs-keyword">int</span> number)</span>
   </span>{
      System.out.println(<span class="hljs-string">"Constructing an Employee"</span>);
      <span class="hljs-keyword">this</span>.name = name;
      <span class="hljs-keyword">this</span>.address = address;
      <span class="hljs-keyword">this</span>.number = number;
   }
   <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">mailCheck</span><span class="hljs-params">()</span>
   </span>{
      System.out.println(<span class="hljs-string">"Mailing a check to "</span> + <span class="hljs-keyword">this</span>.name
       + <span class="hljs-string">" "</span> + <span class="hljs-keyword">this</span>.address);
   }
   <span class="hljs-function"><span class="hljs-keyword">public</span> String <span class="hljs-title">toString</span><span class="hljs-params">()</span>
   </span>{
      <span class="hljs-keyword">return</span> name + <span class="hljs-string">" "</span> + address + <span class="hljs-string">" "</span> + number;
   }
   <span class="hljs-function"><span class="hljs-keyword">public</span> String <span class="hljs-title">getName</span><span class="hljs-params">()</span>
   </span>{
      <span class="hljs-keyword">return</span> name;
   }
   <span class="hljs-function"><span class="hljs-keyword">public</span> String <span class="hljs-title">getAddress</span><span class="hljs-params">()</span>
   </span>{
      <span class="hljs-keyword">return</span> address;
   }
   <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">setAddress</span><span class="hljs-params">(String newAddress)</span>
   </span>{
      address = newAddress;
   }
   <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">int</span> <span class="hljs-title">getNumber</span><span class="hljs-params">()</span>
   </span>{
     <span class="hljs-keyword">return</span> number;
   }
}
</code></pre> <p>假设下面的类继承Employee类：</p> <pre lang="java"><code class="java hljs"><span class="hljs-comment">/* 文件名 : Salary.java */</span>
<span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Salary</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Employee</span>
</span>{
   <span class="hljs-keyword">private</span> <span class="hljs-keyword">double</span> salary; <span class="hljs-comment">//Annual salary</span>
   <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-title">Salary</span><span class="hljs-params">(String name, String address, <span class="hljs-keyword">int</span> number, <span class="hljs-keyword">double</span>
      salary)</span>
   </span>{
       <span class="hljs-keyword">super</span>(name, address, number);
       setSalary(salary);
   }
   <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">mailCheck</span><span class="hljs-params">()</span>
   </span>{
       System.out.println(<span class="hljs-string">"Within mailCheck of Salary class "</span>);
       System.out.println(<span class="hljs-string">"Mailing check to "</span> + getName()
       + <span class="hljs-string">" with salary "</span> + salary);
   }
   <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">double</span> <span class="hljs-title">getSalary</span><span class="hljs-params">()</span>
   </span>{
       <span class="hljs-keyword">return</span> salary;
   }
   <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">setSalary</span><span class="hljs-params">(<span class="hljs-keyword">double</span> newSalary)</span>
   </span>{
       <span class="hljs-keyword">if</span>(newSalary &gt;= <span class="hljs-number">0.0</span>)
       {
          salary = newSalary;
       }
   }
   <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">double</span> <span class="hljs-title">computePay</span><span class="hljs-params">()</span>
   </span>{
      System.out.println(<span class="hljs-string">"Computing salary pay for "</span> + getName());
      <span class="hljs-keyword">return</span> salary/<span class="hljs-number">52</span>;
   }
}
</code></pre> <p>现在我们仔细阅读下面的代码，尝试给出它的输出结果：</p> <pre lang="java"><code class="java hljs"><span class="hljs-comment">/* 文件名 : VirtualDemo.java */</span>
<span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">VirtualDemo</span>
</span>{
   <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">static</span> <span class="hljs-keyword">void</span> <span class="hljs-title">main</span><span class="hljs-params">(String [] args)</span>
   </span>{
      Salary s = <span class="hljs-keyword">new</span> Salary(<span class="hljs-string">"Mohd Mohtashim"</span>, <span class="hljs-string">"Ambehta, UP"</span>, <span class="hljs-number">3</span>, <span class="hljs-number">3600.00</span>);
      Employee e = <span class="hljs-keyword">new</span> Salary(<span class="hljs-string">"John Adams"</span>, <span class="hljs-string">"Boston, MA"</span>, <span class="hljs-number">2</span>, <span class="hljs-number">2400.00</span>);
      System.out.println(<span class="hljs-string">"Call mailCheck using Salary reference --"</span>);
      s.mailCheck();
      System.out.println(<span class="hljs-string">"\n Call mailCheck using Employee reference--"</span>);
      e.mailCheck();
    }
}
</code></pre> <p>以上实例编译运行结果如下：</p> <pre lang="java"><code class="java hljs">Constructing an Employee
Constructing an Employee
Call mailCheck using Salary reference --
Within mailCheck of Salary <span class="hljs-class"><span class="hljs-keyword">class</span>
<span class="hljs-title">Mailing</span> <span class="hljs-title">check</span> <span class="hljs-title">to</span> <span class="hljs-title">Mohd</span> <span class="hljs-title">Mohtashim</span> <span class="hljs-title">with</span> <span class="hljs-title">salary</span> 3600.0

<span class="hljs-title">Call</span> <span class="hljs-title">mailCheck</span> <span class="hljs-title">using</span> <span class="hljs-title">Employee</span> <span class="hljs-title">reference</span>--
<span class="hljs-title">Within</span> <span class="hljs-title">mailCheck</span> <span class="hljs-title">of</span> <span class="hljs-title">Salary</span> <span class="hljs-title">class</span>
<span class="hljs-title">Mailing</span> <span class="hljs-title">check</span> <span class="hljs-title">to</span> <span class="hljs-title">John</span> <span class="hljs-title">Adams</span> <span class="hljs-title">with</span> <span class="hljs-title">salary</span> 2400.0
</span></code></pre> <p>例子中，我们实例化了两个Salary对象。一个使用Salary引用s，另一个使用Employee引用。</p><p> 编译时，编译器检查到mailCheck()方法在Salary类中的声明。</p><p> 在调用s.mailCheck()时，Java虚拟机(JVM)调用Salary类的mailCheck()方法。</p><p> 因为e是Employee的引用，所以调用e的mailCheck()方法则有完全不同的结果。</p><p> 当编译器检查e.mailCheck()方法时，编译器检查到Employee类中的mailCheck()方法。</p><p> 在编译的时候，编译器使用Employee类中的mailCheck()方法验证该语句， 但是在运行的时候，Java虚拟机(JVM)调用的是Salary类中的mailCheck()方法。</p><p> 该行为被称为虚拟方法调用，该方法被称为虚拟方法。</p><p> Java中所有的方法都能以这种方式表现，借此，重写的方法能在运行时调用，不管编译的时候源代码中引用变量是什么数据类型。</p></div>