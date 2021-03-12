---
title: 'Java 重写(Override)与重载(Overload)'
cover: "/img/lynk/11.jpg"
date:       2019-10-11
tags:
	- Java
	- basis
	- oop
---

<div class="content-intro view-box "> <hr> <h3>重写(Override)</h3> <p> 重写是子类对父类的允许访问的方法的实现过程进行重新编写！返回值和形参都不能改变。即外壳不变，核心重写！ </p> <p>重写的好处在于子类可以根据需要，定义特定于自己的行为。</p><p> 也就是说子类能够根据需要实现父类的方法。</p><p> 在面向对象原则里，重写意味着可以重写任何现有方法。实例如下：</p> <pre lang="java"><code class="java hljs"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Animal</span></span>{

   <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">move</span><span class="hljs-params">()</span></span>{
      System.out.println(<span class="hljs-string">"动物可以移动"</span>);
   }
}

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Dog</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Animal</span></span>{

   <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">move</span><span class="hljs-params">()</span></span>{
      System.out.println(<span class="hljs-string">"狗可以跑和走"</span>);
   }
}

<span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">TestDog</span></span>{

   <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">static</span> <span class="hljs-keyword">void</span> <span class="hljs-title">main</span><span class="hljs-params">(String args[])</span></span>{
      Animal a = <span class="hljs-keyword">new</span> Animal(); <span class="hljs-comment">// Animal 对象</span>
      Animal b = <span class="hljs-keyword">new</span> Dog(); <span class="hljs-comment">// Dog 对象</span>

      a.move();<span class="hljs-comment">// 执行 Animal 类的方法</span>

      b.move();<span class="hljs-comment">//执行 Dog 类的方法</span>
   }
}
</code></pre> <p>以上实例编译运行结果如下：</p> <pre lang="java"><code class="java hljs">动物可以移动
狗可以跑和走
</code></pre> <p>在上面的例子中可以看到，尽管b属于Animal类型，但是它运行的是Dog类的move方法。</p><p> 这是由于在编译阶段，只是检查参数的引用类型。</p><p> 然而在运行时，Java虚拟机(JVM)指定对象的类型并且运行该对象的方法。</p><p> 因此在上面的例子中，之所以能编译成功，是因为Animal类中存在move方法，然而运行时，运行的是特定对象的方法。</p><p> 思考以下例子：</p> <pre lang="java"><code class="java hljs"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Animal</span></span>{

   <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">move</span><span class="hljs-params">()</span></span>{
      System.out.println(<span class="hljs-string">"动物可以移动"</span>);
   }
}

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Dog</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Animal</span></span>{

   <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">move</span><span class="hljs-params">()</span></span>{
      System.out.println(<span class="hljs-string">"狗可以跑和走"</span>);
   }
   <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">bark</span><span class="hljs-params">()</span></span>{
      System.out.println(<span class="hljs-string">"狗可以吠叫"</span>);
   }
}

<span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">TestDog</span></span>{

   <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">static</span> <span class="hljs-keyword">void</span> <span class="hljs-title">main</span><span class="hljs-params">(String args[])</span></span>{
      Animal a = <span class="hljs-keyword">new</span> Animal(); <span class="hljs-comment">// Animal 对象</span>
      Animal b = <span class="hljs-keyword">new</span> Dog(); <span class="hljs-comment">// Dog 对象</span>

      a.move();<span class="hljs-comment">// 执行 Animal 类的方法</span>
      b.move();<span class="hljs-comment">//执行 Dog 类的方法</span>
      a.bark();<span class="hljs-comment">//执行 Animal 类的方法</span>
   }
}
</code></pre><p>以上实例编译运行结果如下：</p> <pre lang="java"><code class="java hljs">TestDog.java:<span class="hljs-number">30</span>: cannot find symbol
symbol  : <span class="hljs-function">method <span class="hljs-title">bark</span><span class="hljs-params">()</span>
location: class Animal
                a.<span class="hljs-title">bark</span><span class="hljs-params">()</span></span>;
                 ^
</code></pre> <p>该程序将抛出一个编译错误，因为a的引用类型Animal没有bark方法。</p> <hr> <h3>方法重写的规则</h3> <ul> <li> 参数列表必须完全与被重写方法的相同；</li> <li> 返回类型必须完全与被重写方法的返回类型相同；</li> <li>子类方法的访问权限必须大于或等于父类方法的访问权限。例如：如果父类的一个方法被声明为public，那么在子类中重写该方法就不能声明为protected。</li> <li> 父类的成员方法只能被它的子类重写。</li> <li> 声明为final的方法不能被重写。</li> <li> 声明为static的方法不能被重写，但是能够被再次声明。</li> <li> 子类和父类在同一个包中，那么子类可以重写父类所有方法，除了声明为private和final的方法。</li> <li> 子类和父类不在同一个包中，那么子类只能够重写父类的声明为public和protected的非final方法。</li> <li> 重写的方法能够抛出任何非强制异常，无论被重写的方法是否抛出异常。但是，重写的方法不能抛出新的强制性异常，或者比被重写方法声明的更广泛的强制性异常，反之则可以。</li> <li> 构造方法不能被重写。</li> <li>如果不能继承一个方法，则不能重写这个方法。</li> </ul> <hr><h3>Super关键字的使用</h3> <p> 当需要在子类中调用父类的被重写方法时，要使用super关键字。 </p> <pre lang="java"><code class="java hljs"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Animal</span></span>{

   <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">move</span><span class="hljs-params">()</span></span>{
      System.out.println(<span class="hljs-string">"动物可以移动"</span>);
   }
}

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Dog</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Animal</span></span>{

   <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">move</span><span class="hljs-params">()</span></span>{
      <span class="hljs-keyword">super</span>.move(); <span class="hljs-comment">// 应用super类的方法</span>
      System.out.println(<span class="hljs-string">"狗可以跑和走"</span>);
   }
}

<span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">TestDog</span></span>{

   <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">static</span> <span class="hljs-keyword">void</span> <span class="hljs-title">main</span><span class="hljs-params">(String args[])</span></span>{

      Animal b = <span class="hljs-keyword">new</span> Dog(); <span class="hljs-comment">//</span>
      b.move(); <span class="hljs-comment">//执行 Dog类的方法</span>

   }
}
</code></pre><p>以上实例编译运行结果如下：</p> <pre lang="java"><code class="java hljs">动物可以移动
狗可以跑和走
</code></pre>  <h3>重载(Overload)</h3> <p>重载(overloading) 是在一个类里面，方法名字相同，而参数不同。返回类型呢？可以相同也可以不同。</p> <p>每个重载的方法（或者构造函数）都必须有一个独一无二的参数类型列表。</p> <p>只能重载构造函数</p> <p>重载规则</p> <ul> <li>被重载的方法必须改变参数列表；</li> <li>被重载的方法可以改变返回类型；</li> <li>被重载的方法可以改变访问修饰符；</li> <li>被重载的方法可以声明新的或更广的检查异常；</li> <li>方法能够在同一个类中或者在一个子类中被重载。</li> </ul> <h3>实例</h3> <pre lang="java"><code class="java hljs"><span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Overloading</span> </span>{
 
  <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">int</span> <span class="hljs-title">test</span><span class="hljs-params">()</span></span>{
    System.out.println(<span class="hljs-string">"test1"</span>);
    <span class="hljs-keyword">return</span> <span class="hljs-number">1</span>;
  }
 
  <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">test</span><span class="hljs-params">(<span class="hljs-keyword">int</span> a)</span></span>{
    System.out.println(<span class="hljs-string">"test2"</span>);
  } 
 
  <span class="hljs-comment">//以下两个参数类型顺序不同</span>
  <span class="hljs-function"><span class="hljs-keyword">public</span> String <span class="hljs-title">test</span><span class="hljs-params">(<span class="hljs-keyword">int</span> a,String s)</span></span>{
    System.out.println(<span class="hljs-string">"test3"</span>);
    <span class="hljs-keyword">return</span> <span class="hljs-string">"returntest3"</span>;
  } 
 
  <span class="hljs-function"><span class="hljs-keyword">public</span> String <span class="hljs-title">test</span><span class="hljs-params">(String s,<span class="hljs-keyword">int</span> a)</span></span>{
    System.out.println(<span class="hljs-string">"test4"</span>);
    <span class="hljs-keyword">return</span> <span class="hljs-string">"returntest4"</span>;
  } 
 
  <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">static</span> <span class="hljs-keyword">void</span> <span class="hljs-title">main</span><span class="hljs-params">(String[] args)</span></span>{
    Overloading o = <span class="hljs-keyword">new</span> Overloading();
    System.out.println(o.test());
    o.test(<span class="hljs-number">1</span>);
    System.out.println(o.test(<span class="hljs-number">1</span>,<span class="hljs-string">"test3"</span>));
    System.out.println(o.test(<span class="hljs-string">"test4"</span>,<span class="hljs-number">1</span>));
  }
</code></pre> <hr><h3>重写与重载之间的区别</h3> <table class="reference   "> <tbody> <tr> <th width="72">区别点</th> <th width="80">重载方法</th> <th width="340">重写方法</th> </tr> <tr> <td width="72">参数列表</td> <td width="80">必须修改</td> <td width="340">一定不能修改</td> </tr> <tr> <td width="72">返回类型</td> <td width="80">可以修改</td> <td width="340">一定不能修改</td> </tr> <tr> <td width="72">异常</td> <td width="80">可以修改</td> <td width="340">可以减少或删除，一定不能抛出新的或者更广的异常</td> </tr> <tr> <td width="72">访问</td> <td width="80">可以修改</td> <td width="340">一定不能做更严格的限制（可以降低限制）</td> </tr> </tbody> </table><p><br></p></div>