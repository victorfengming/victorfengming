---
title: 'Java中final关键字的几种用法'
date:       2019-10-11
tags:
	- Java
	- basis
---

<div class="post">
    
  <div class="clear"></div>
  <div class="postBody">
    
<div id="cnblogs_post_body" class="blogpost-body ">
    <p>在java的关键字中，<strong>static</strong>和<strong>final</strong>是两个我们必须掌握的关键字。不同于其他关键字，他们都有多种用法，而且在一定环境下使用，可以提高程序的运行性能，优化程序的结构。下面我们来了解一下<strong>final</strong>关键字及其用法。</p>
<h2>final关键字</h2>
<p>在java中，final的含义在不同的场景下有细微的差别，但总体上来说，它指的是“<strong>这是不可变的</strong>”。下面，我们来讲final的四种主要用法。</p>
<h3>1.修饰数据</h3>
<p>在编写程序时，我们经常需要说明一个数据是不可变的，我们成为常量。在java中，用final关键字修饰的变量，只能进行一次赋值操作，并且在生存期内不可以改变它的值。更重要的是，final会告诉编译器，这个数据是不会修改的，那么编译器就可能会在编译时期就对该数据进行替换甚至执行计算，这样可以对我们的程序起到一点优化。不过在针对基本类型和引用类型时，final关键字的效果存在细微差别。我们来看下面的例子：</p>
<div class="cnblogs_code"><div class="cnblogs_code_toolbar"><span class="cnblogs_code_copy"><a href="javascript:void(0);" onclick="copyCnblogsCode(this)" title="复制代码"><img src="//common.cnblogs.com/img/copycode.gif" alt="复制代码"></a></span></div>
<pre><span style="color: #008080;"> 1</span> <span style="color: #0000ff;">class</span><span style="color: #000000;"> Value {
</span><span style="color: #008080;"> 2</span>     <span style="color: #0000ff;">int</span><span style="color: #000000;"> v;
</span><span style="color: #008080;"> 3</span>     <span style="color: #0000ff;">public</span> Value(<span style="color: #0000ff;">int</span><span style="color: #000000;"> v) {
</span><span style="color: #008080;"> 4</span>         <span style="color: #0000ff;">this</span>.v =<span style="color: #000000;"> v;
</span><span style="color: #008080;"> 5</span> <span style="color: #000000;">    }
</span><span style="color: #008080;"> 6</span> <span style="color: #000000;">}
</span><span style="color: #008080;"> 7</span> 
<span style="color: #008080;"> 8</span> <span style="color: #0000ff;">public</span> <span style="color: #0000ff;">class</span><span style="color: #000000;"> FinalTest {
</span><span style="color: #008080;"> 9</span>     
<span style="color: #008080;">10</span>     <span style="color: #0000ff;">final</span> <span style="color: #0000ff;">int</span> f1 = 1<span style="color: #000000;">;
</span><span style="color: #008080;">11</span>     <span style="color: #0000ff;">final</span> <span style="color: #0000ff;">int</span><span style="color: #000000;"> f2;
</span><span style="color: #008080;">12</span>     <span style="color: #0000ff;">public</span><span style="color: #000000;"> FinalTest() {
</span><span style="color: #008080;">13</span>         f2 = 2<span style="color: #000000;">;
</span><span style="color: #008080;">14</span> <span style="color: #000000;">    }
</span><span style="color: #008080;">15</span> 
<span style="color: #008080;">16</span>     <span style="color: #0000ff;">public</span> <span style="color: #0000ff;">static</span> <span style="color: #0000ff;">void</span><span style="color: #000000;"> main(String[] args) {
</span><span style="color: #008080;">17</span>         <span style="color: #0000ff;">final</span> <span style="color: #0000ff;">int</span> value1 = 1<span style="color: #000000;">;
</span><span style="color: #008080;">18</span>         <span style="color: #008000;">//</span><span style="color: #008000;"> value1 = 4;</span>
<span style="color: #008080;">19</span>         <span style="color: #0000ff;">final</span> <span style="color: #0000ff;">double</span><span style="color: #000000;"> value2;
</span><span style="color: #008080;">20</span>         value2 = 2.0<span style="color: #000000;">;
</span><span style="color: #008080;">21</span>         <span style="color: #0000ff;">final</span> Value value3 = <span style="color: #0000ff;">new</span> Value(1<span style="color: #000000;">);
</span><span style="color: #008080;">22</span>         value3.v = 4<span style="color: #000000;">;
</span><span style="color: #008080;">23</span> <span style="color: #000000;">    }
</span><span style="color: #008080;">24</span> }</pre>
<div class="cnblogs_code_toolbar"><span class="cnblogs_code_copy"><a href="javascript:void(0);" onclick="copyCnblogsCode(this)" title="复制代码"><img src="//common.cnblogs.com/img/copycode.gif" alt="复制代码"></a></span></div></div>
<p>上面的例子中，我们先来看一下main方法中的几个final修饰的数据，在给value1赋初始值之后，我们无法再对value1的值进行修改，final关键字起到了常量的作用。从value2我们可以看到，final修饰的变量可以不在声明时赋值，即可以先声明，后赋值。value3时一个引用变量，这里我们可以看到final修饰引用变量时，只是限定了引用变量的引用不可改变，即不能将value3再次引用另一个Value对象，但是引用的对象的值是可以改变的，从内存模型中我们看的更加清晰：</p>
<p><img src="https://images2015.cnblogs.com/blog/1055692/201701/1055692-20170130101552386-541665575.jpg" alt=""></p>
<p>上图中，final修饰的值用粗线条的边框表示它的值是不可改变的，我们知道引用变量的值实际上是它所引用的对象的地址，也就是说该地址的值是不可改变的，从而说明了为什么引用变量不可以改变引用对象。而实际引用的对象实际上是不受final关键字的影响的，所以它的值是可以改变的。</p>
<p>另一方面，我们看到了用final修饰成员变量时的细微差别，因为final修饰的数据的值是不可改变的，所以我们必须确保在使用前就已经对成员变量赋值了。因此对于final修饰的成员变量，我们有且只有两个地方可以给它赋值，一个是声明该成员时赋值，另一个是在构造方法中赋值，在这两个地方我们必须给它们赋初始值。</p>
<p>最后我们需要注意的一点是，同时使用static和final修饰的成员在内存中只占据一段不能改变的存储空间。</p>
<h3>2.修饰方法参数</h3>
<p>前面我们可以看到，如果变量是我们自己创建的，那么使用final修饰表示我们只会给它赋值一次且不会改变变量的值。那么如果变量是作为参数传入的，我们怎么保证它的值不会改变呢？这就用到了final的第二种用法，即在我们编写方法时，可以在参数前面添加final关键字，它表示在整个方法中，我们不会（实际上是不能）改变参数的值：</p>
<div class="cnblogs_code"><div class="cnblogs_code_toolbar"><span class="cnblogs_code_copy"><a href="javascript:void(0);" onclick="copyCnblogsCode(this)" title="复制代码"><img src="//common.cnblogs.com/img/copycode.gif" alt="复制代码"></a></span></div>
<pre><span style="color: #0000ff;">public</span> <span style="color: #0000ff;">class</span><span style="color: #000000;"> FinalTest {

    </span><span style="color: #008000;">/*</span><span style="color: #008000;"> ... </span><span style="color: #008000;">*/</span>

    <span style="color: #0000ff;">public</span> <span style="color: #0000ff;">void</span> finalFunc(<span style="color: #0000ff;">final</span> <span style="color: #0000ff;">int</span> i, <span style="color: #0000ff;">final</span><span style="color: #000000;"> Value value) {
        </span><span style="color: #008000;">//</span><span style="color: #008000;"> i = 5; 不能改变i的值
        </span><span style="color: #008000;">//</span><span style="color: #008000;"> v = new Value(); 不能改变v的值</span>
        value.v = 5; <span style="color: #008000;">//</span><span style="color: #008000;"> 可以改变引用对象的值</span>
<span style="color: #000000;">    }
}</span></pre>
<div class="cnblogs_code_toolbar"><span class="cnblogs_code_copy"><a href="javascript:void(0);" onclick="copyCnblogsCode(this)" title="复制代码"><img src="//common.cnblogs.com/img/copycode.gif" alt="复制代码"></a></span></div></div>
<h3>3.修饰方法</h3>
<p>第三种方式，即用final关键字修饰方法，它表示该方法不能被覆盖。这种使用方式主要是从设计的角度考虑，即明确告诉其他可能会继承该类的程序员，不希望他们去覆盖这个方法。这种方式我们很容易理解，然而，关于private和final关键字还有一点联系，这就是类中所有的private方法都隐式地指定为是final的，由于无法在类外使用private方法，所以也就无法覆盖它。</p>
<h3>4.修饰类</h3>
<p>了解了final关键字的其他用法，我们很容易可以想到使用final关键字修饰类的作用，那就是用final修饰的类是无法被继承的。</p>
<p>上面我们讲解了final的四种用法，然而，对于第三种和第四种用法，我们却甚少使用。这不是没有道理的，从final的设计来讲，这两种用法甚至可以说是鸡肋，因为对于开发人员来讲，如果我们写的类被继承的越多，就说明我们写的类越有价值，越成功。即使是从设计的角度来讲，也没有必要将一个类设计为不可继承的。Java标准库就是一个很好的反例，特别是Java 1.0/1.1中Vector类被如此广泛的运用，如果所有的方法均未被指定为final的话，它可能会更加有用。如此有用的类，我们很容易想到去继承和重写他们，然而，由于final的作用，导致我们对Vector类的扩展受到了一些阻碍，导致了Vector并没有完全发挥它应有的全部价值。</p>
<h2>总结</h2>
<p>final关键字是我们经常使用的关键字之一，它的用法有很多，但是并不是每一种用法都值得我们去广泛使用。它的主要用法有以下四种：</p>
<ol>
<li>用来修饰数据，包括成员变量和局部变量，该变量只能被赋值一次且它的值无法被改变。对于成员变量来讲，我们必须在声明时或者构造方法中对它赋值；</li>
<li>用来修饰方法参数，表示在变量的生存期中它的值不能被改变；</li>
<li>修饰方法，表示该方法无法被重写；</li>
<li>修饰类，表示该类无法被继承。</li>
</ol>
<p>上面的四种方法中，第三种和第四种方法需要谨慎使用，因为在大多数情况下，如果是仅仅为了一点设计上的考虑，我们并不需要使用final来修饰方法和类。</p>
</div>
