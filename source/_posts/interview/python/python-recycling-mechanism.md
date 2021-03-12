---
title: "Python中的垃圾回收机制"
date:       2019-11-28
subtitle: "垃圾分类,从python做起"
tags:
	- Python
	- solution
	- interview
---


<div class="RichText ztext Post-RichText"><h2>一、概述</h2>
    <p>python采用的是<b>引用计数</b>机制为主，<b>标记-清除</b>和<b>分代收集（隔代回收）</b>两种机制为辅的策略。<br></p>
    <blockquote>
        现在的高级语言如java，c#等，都采用了垃圾收集机制，而不再是c，c++里用户自己管理维护内存的方式。自己管理内存极其自由，可以任意申请内存，但如同一把双刃剑，为大量内存泄露，悬空指针等bug埋下隐患。<br>对于一个字符串、列表、类甚至数值都是对象，且定位简单易用的语言，自然不会让用户去处理如何分配回收内存的问题。<br>python里也同java一样采用了垃圾收集机制，不过不一样的是:<br>python采用的是引用计数机制为主，标记-清除和分代收集（隔代回收）两种机制为辅的策略。
    </blockquote>
    <h2>二、引用计数机制</h2>
    <blockquote>
        引用计数法机制的原理是：每个对象维护一个ob_ref字段，用来记录该对象当前被引用的次数，每当新的引用指向该对象时，它的引用计数ob_ref加1，每当该对象的引用失效时计数ob_ref减1，一旦对象的引用计数为0，该对象立即被回收，对象占用的内存空间将被释放。它的缺点是需要额外的空间维护引用计数，这个问题是其次的，不过最主要的问题是它不能解决对象的“循环引用”，因此，也有很多语言比如Java并没有采用该算法做来垃圾的收集机制。
    </blockquote>
    <p>python里每一个东西都是对象，它们的核心就是一个结构体：PyObject</p>
    <p>PyObject是每个对象必有的内容，其中ob_refcnt就是做为引用计数。当一个对象有新的引用时，它的ob_refcnt就会增加，当引用它的对象被删除，它的ob_refcnt就会减少</p>
    <p>引用计数为0时，该对象生命就结束了。</p>
    <p><b>引用计数机制的优点：</b></p>
    <p>1、简单</p>
    <p>2、实时性：一旦没有引用，内存就直接释放了，不用像其他机制得等到特定时机。实时性还带来一个好处：处理回收内存的时间分摊到了平时。</p>
    <p><b>引用计数机制的缺点：</b></p>
    <p>1、维护引用计数消耗资源</p>
    <p>2、循环引用</p>
    <p><b>案例：</b></p>
    <div class="highlight"><pre><code class="language-python3"><span class="kn">import</span> <span
            class="nn">sys</span>
<span class="k">class</span> <span class="nc">A</span><span class="p">():</span>
    <span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span
                class="p">):</span>
        <span class="s1">'''初始化对象'''</span>
        <span class="nb">print</span><span class="p">(</span><span class="s1">'object born id:</span><span
                class="si">%s</span><span class="s1">'</span> <span class="o">%</span><span class="nb">str</span><span
                class="p">(</span><span class="nb">hex</span><span class="p">(</span><span class="nb">id</span><span
                class="p">(</span><span class="bp">self</span><span class="p">))))</span>

<span class="k">def</span> <span class="nf">f1</span><span class="p">():</span>
    <span class="s1">'''循环引用变量与删除变量'''</span>
    <span class="k">while</span> <span class="kc">True</span><span class="p">:</span>
        <span class="n">c1</span><span class="o">=</span><span class="n">A</span><span class="p">()</span>
        <span class="k">del</span> <span class="n">c1</span>

<span class="k">def</span> <span class="nf">func</span><span class="p">(</span><span class="n">c</span><span class="p">):</span>
    <span class="nb">print</span><span class="p">(</span><span class="s1">'obejct refcount is: '</span><span
                class="p">,</span><span class="n">sys</span><span class="o">.</span><span
                class="n">getrefcount</span><span class="p">(</span><span class="n">c</span><span
                class="p">))</span> <span class="c1">#getrefcount()方法用于返回对象的引用计数</span>

<span class="k">if</span> <span class="vm">__name__</span> <span class="o">==</span> <span
                class="s1">'__main__'</span><span class="p">:</span>
   <span class="c1">#生成对象</span>
    <span class="n">a</span><span class="o">=</span><span class="n">A</span><span class="p">()</span>
    <span class="n">func</span><span class="p">(</span><span class="n">a</span><span class="p">)</span>

    <span class="c1">#增加引用</span>
    <span class="n">b</span><span class="o">=</span><span class="n">a</span>
    <span class="n">func</span><span class="p">(</span><span class="n">a</span><span class="p">)</span>

    <span class="c1">#销毁引用对象b</span>
    <span class="k">del</span> <span class="n">b</span>
    <span class="n">func</span><span class="p">(</span><span class="n">a</span><span class="p">)</span>
<span class="c1">#结果</span>
<span class="nb">object</span> <span class="n">born</span> <span class="nb">id</span><span class="p">:</span><span
                class="mh">0x19f5ecb9320</span>
<span class="n">obejct</span> <span class="n">refcount</span> <span class="ow">is</span><span class="p">:</span>  <span
                class="mi">4</span>
<span class="n">obejct</span> <span class="n">refcount</span> <span class="ow">is</span><span class="p">:</span>  <span
                class="mi">5</span>
<span class="n">obejct</span> <span class="n">refcount</span> <span class="ow">is</span><span class="p">:</span>  <span
                class="mi">4</span></code></pre>
    </div>
    <h3><b>导致引用计数+1的情况</b></h3>
    <ul>
        <li>对象被创建，例如a=23</li>
        <li>对象被引用，例如b=a</li>
        <li>对象被作为参数，传入到一个函数中，例如<code>func(a)</code></li>
        <li>对象作为一个元素，存储在容器中，例如<code>list1=[a,a]</code></li>
    </ul>
    <h3><b>导致引用计数-1的情况</b></h3>
    <ul>
        <li>对象的别名被显式销毁，例如<code>del a</code></li>
        <li>对象的别名被赋予新的对象，例如<code>a=24</code></li>
        <li>一个对象离开它的作用域，例如:func函数执行完毕时，func函数中的局部变量（全局变量不会）</li>
        <li>对象所在的容器被销毁，或从容器中删除对象</li>
    </ul>
    <p><b>循环引用导致内存泄露</b></p>
    <div class="highlight"><pre><code class="language-text">def f2():
    '''循环引用'''
    while True:
        c1=A()
        c2=A()
        c1.t=c2
        c2.t=c1
        del c1
        del c2</code></pre>
    </div>
    <ul>
        <li>创建了<code>c1</code>，<code>c2</code>后，这两个对象的引用计数都是<code>1</code>，执行<code>c1.t=c2</code>和<code>c2.t=c1</code>后，引用计数变成<code>2</code>.
        </li>
        <li>在<code>del c1</code>后，内存<code>c1</code>的对象的引用计数变为<code>1</code>，由于不是为<code>0</code>，所以<code>c1</code>的对象不会被销毁,同理，在<code>del
            c2</code>后也是一样的。
        </li>
        <li>虽然它们两个的对象都是可以被销毁的，但是由于循环引用，导致垃圾回收器都不会回收它们，所以就会导致内存泄露。</li>
    </ul>
    <p class="ztext-empty-paragraph"><br></p>
    <h3><b>分代回收</b></h3>
    <ul>
        <li>
            分代回收是一种以空间换时间的操作方式，Python将内存根据对象的存活时间划分为不同的集合，每个集合称为一个代，Python将内存分为了3“代”，分别为年轻代（第0代）、中年代（第1代）、老年代（第2代），他们对应的是3个链表，它们的垃圾收集频率随着对象存活时间的增大而减小。
        </li>
        <li>
            新创建的对象都会分配在<b>年轻代</b>，年轻代链表的总数达到上限时，Python垃圾收集机制就会被触发，把那些可以被回收的对象回收掉，而那些不会回收的对象就会被移到<b>中年代</b>去，依此类推，<b>老年代</b>中的对象是存活时间最久的对象，甚至是存活于整个系统的生命周期内。
        </li>
        <li>同时，分代回收是建立在标记清除技术基础之上。分代回收同样作为Python的辅助垃圾收集技术处理那些容器对象</li>
    </ul>
    <h3><b>垃圾回收</b></h3>
    <p>有三种情况会触发垃圾回收：</p>
    <ol>
        <li>调用<code>gc.collect()</code>,需要先导入<code>gc</code>模块。</li>
        <li>当<code>gc</code>模块的计数器达到阈值的时候。</li>
        <li>程序退出的时候。</li>
    </ol>
    <h3><b>gc模块</b></h3>
    <p>gc模块提供一个接口给开发者设置垃圾回收的选项。上面说到，采用引用计数的方法管理内存的一个缺陷是循环引用，而gc模块的一个主要功能就是解决循环引用的问题。</p>
    <p><b>常用函数</b>：</p>
    <ol>
        <li><code>gc.set_debug(flags)</code> 设置gc的debug日志，一般设置为<code>gc.DEBUG_LEAK</code></li>
        <li><code>gc.collect([generation])</code> <br>显式进行垃圾回收，可以输入参数，<code>0</code>代表只检查第一代的对象，<code>1</code>代表检查一，二代的对象，<code>2</code>代表检查一，二，三代的对象，如果不传参数，执行一个<code>full
            collection</code>，也就是等于传2。返回不可达（unreachable objects）对象的数目。
        </li>
        <li><code>gc.set_threshold(threshold0[, threshold1[, threshold2])</code><br>设置自动执行垃圾回收的频率。</li>
        <li><code>gc.get_count()</code> 获取当前自动执行垃圾回收的计数器，返回一个长度为3的列表</li>
    </ol>
    <p><b>gc实践案例</b></p>
    <div class="highlight"><pre><code class="language-text">def f3():
    '''循环引用'''
    while True:
        c1=A()
        c2=A()
        c1.t=c2
        c2.t=c1
        del c1
        del c2
        #增加垃圾回收机制
        print(gc.garbage)
        print(gc.collect())
        print(gc.garbage)
        time.sleep(10)
#结果
object born id:0x21d1a5dc470
object born id:0x21d1a5dc9e8
[]
4
gc: collectable &lt;A 0x0000021D1A5DC470&gt;
[&lt;__main__.A object at 0x0000021D1A5DC470&gt;, &lt;__main__.A object at 0x0000021D1A5DC9E8&gt;, {'t': &lt;__main__.A object at 0x0000021D1A5DC9E8&gt;}, {'t': &lt;__main__.A object at 0x0000021D1A5DC470&gt;}]
gc: collectable &lt;A 0x0000021D1A5DC9E8&gt;
gc: collectable &lt;dict 0x0000021D1A156C88&gt;
gc: collectable &lt;dict 0x0000021D1A5CABC8&gt;</code></pre>
    </div>
    <h3><b>gc模块的自动垃圾回收机制</b></h3>
    <p>必须要import gc模块，并且is_enable()=True才会启动自动垃圾回收。<br>这个机制的主要作用就是发现并处理不可达的垃圾对象。</p>
    <blockquote>垃圾回收=垃圾检查+垃圾回收</blockquote>
    <p>在Python中，采用分代收集的方法。把对象分为三代，一开始，对象在创建的时候，放在一代中，如果在一次一代的垃圾检查中，该对象存活下来，就会被放到二代中，同理在一次二代的垃圾检查中，该对象存活下来，就会被放到三代中。</p>
    <p>gc模块里面会有一个长度为3的列表的计数器，可以通过<code>gc.get_count()</code>获取。</p>
    <div class="highlight"><pre><code class="language-text">def f4():
    '''垃圾自动回收'''
    print(gc.get_count())
    a=A()
    print(gc.get_count())
    del a
    print(gc.get_count())
#结果
(621, 10, 0)
object born id:0x2ca32a8c588
(624, 10, 0)
(623, 10, 0)</code></pre>
    </div>
    <ul>
        <li><code>621</code>指距离上一次<code>一代</code>垃圾检查，Python分配内存的数目减去释放内存的数目，注意:是内存分配，而不是引用计数的增加。</li>
        <li><code>10</code>指距离上一次<code>二代</code>垃圾检查，<code>一代</code>垃圾检查的次数。</li>
        <li><code>0</code>是指距离上一次<code>三代</code>垃圾检查，<code>二代</code>垃圾检查的次数。</li>
    </ul>
    <h3><b>自动回收阈值</b></h3>
    <p>gc模快有一个自动垃圾回收的阀值，即通过<code>gc.get_threshold</code>函数获取到的长度为3的元组，例如<code>(700,10,10)</code><br>每一次计数器的增加，gc模块就会检查增加后的计数是否达到阀值的数目，如果是，就会执行对应的代数的垃圾检查，然后重置计数器
    </p>
    <p>注意：<br>如果循环引用中，两个对象都定义了<code>__del__</code>方法，gc模块不会销毁这些不可达对象，因为gc模块不知道应该先调用哪个对象的<code>__del__</code>方法，所以为了安全起见，gc模块会把对象放到<code>gc.garbage</code>中，但是不会销毁对象。
    </p>
    <h3><b>标记清除</b></h3>
    <p>标记清除（Mark—Sweep）』算法是一种基于追踪回收（tracing
        GC）技术实现的垃圾回收算法。它分为两个阶段：第一阶段是标记阶段，GC会把所有的『活动对象』打上标记，第二阶段是把那些没有标记的对象『非活动对象』进行回收。那么GC又是如何判断哪些是活动对象哪些是非活动对象的呢？</p>
    <figure data-size="normal">
        <noscript><img src="https://pic1.zhimg.com/v2-543bb871b0eb79e4b6b9186ac1588e34_b.jpg" data-caption=""
                       data-size="normal" data-rawwidth="328" data-rawheight="250" class="content_image" width="328"/>
        </noscript>
        <img src="https://pic1.zhimg.com/80/v2-543bb871b0eb79e4b6b9186ac1588e34_hd.jpg" data-caption=""
             data-size="normal" data-rawwidth="328" data-rawheight="250" class="content_image lazy" width="328"
             data-actualsrc="https://pic1.zhimg.com/v2-543bb871b0eb79e4b6b9186ac1588e34_b.jpg" data-lazy-status="ok">
    </figure>
    <p class="ztext-empty-paragraph"><br></p>
    <p>对象之间通过引用（指针）连在一起，构成一个有向图，对象构成这个有向图的节点，而引用关系构成这个有向图的边。从根对象（root
        object）出发，沿着有向边遍历对象，可达的（reachable）对象标记为活动对象，不可达的对象就是要被清除的非活动对象。根对象就是全局变量、调用栈、寄存器。 mark-sweepg
        在上图中，我们把小黑圈视为全局变量，也就是把它作为root
        object，从小黑圈出发，对象1可直达，那么它将被标记，对象2、3可间接到达也会被标记，而4和5不可达，那么1、2、3就是活动对象，4和5是非活动对象会被GC回收。</p>
    <p>
        标记清除算法作为Python的辅助垃圾收集技术主要处理的是一些容器对象，比如list、dict、tuple，instance等，因为对于字符串、数值对象是不可能造成循环引用问题。Python使用一个双向链表将这些容器对象组织起来。不过，这种简单粗暴的标记清除算法也有明显的缺点：清除非活动的对象前它必须顺序扫描整个堆内存，哪怕只剩下小部分活动对象也要扫描所有对象。</p>
</div>