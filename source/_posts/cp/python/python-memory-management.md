---
title: "深入python内存管理"
cover: "/img/lynk/28.jpg"
date:       2019-11-28
subtitle: "属性在运行时的动态替换"
tags:
	- Python
	- solution
	- interview
---

### 本文目录
1. 对象的内存使用
2. 对象引用对象
3. 引用减少
4. 垃圾回收
5. 分代回收
6. 孤立的引用环
7. 总结


<div class="post-body" itemprop="articleBody" style="opacity: 1; display: block; transform: translateY(0px);">


<p>
    面试中被问到python的内存管理，只是说是python有自己的内存管理机制，有自己的垃圾回收机制，却不能详细作答，面试官表示很遗憾。建议我代码的业务逻辑需要想，但是学习需要深入底层，也有助于扩宽自己的知识面，对自己之后的学习路径有帮助，哈哈，感谢面试官帮我指出自己的不足。</p>
<p>回家马上查资料，先解决这个问题。</p>
<p>首先看看各种python常见面试题上的答案：</p>
<blockquote>
    <p>
        python内存管理是由私有堆空间管理的，所有的python对象和数据结构都存储在私有堆空间中。程序员没有访问堆的权限，只有解释器才能操作。为python的堆空间分配内存的是python的内存管理模块进行的，核心api会提供一些访问该模块的方法供程序员使用。python自有的垃圾回收机制回收并释放没有被使用的内存供别的程序使用。</p>
</blockquote>
<p>如果仅仅问道这，上面的答案也足够了，但是面试官想要了解到更多，可能会衍生一些别的问题，那上面的答案就不够了。</p>
<a id="more"></a>

<p>以下内容： 作者：Vamei 出处：<a href="http://www.cnblogs.com/vamei" target="_blank" rel="noopener">http://www.cnblogs.com/vamei</a>
    欢迎转载，也请保留这段声明。谢谢！</p>
<p>语言的内存管理是语言设计的一个重要方面。他是决定语言性能的重要因素。无论是C的手动管理还是java的垃圾回收，都成为语言重要的特征。下面已python语言为例子，说明一门动态类型的面向对象的语言的内存管理方式。</p>
<hr>
<h3 id="对象的内存使用"><a href="#对象的内存使用" class="headerlink" title="对象的内存使用"></a>对象的内存使用</h3>
<p>赋值语句是语言最常见的功能了。但即使是最简单的赋值语句，也可以很有内涵. 首先看看python的赋值语句：</p>
<div class="highlight-wrap">
    <figure class="highlight python">
        <div class="table-container">
            <table>
                <tbody>
                <tr>
                    <td class="gutter">
                        <pre><span class="line">1</span><br></pre>
                    </td>
                    <td class="code">
                        <pre><span class="line">a = <span class="number">1</span></span><br></pre>
                    </td>
                </tr>
                </tbody>
            </table>
        </div>
    </figure>
    <div class="copy-btn"><i class="fa fa-clipboard"></i></div>
</div>

<p>
    整数“1”为一个对象，存储在内存空间中。a是一个引用。利用赋值语句，将引用a指向对象1。Python是动态类型的语言，对象与引用分离。文章作者比较形象的解释就是：Python像使用“筷子”那样，通过引用来接触和翻动真正的食物——对象。</p>
<p><strong>下面就是一系列的实验了，建议亲自尝试</strong> 可以通过python的内置函数id()，来探索对象在内存的存储。</p>
<div class="highlight-wrap">
    <figure class="highlight shell">
        <div class="table-container">
            <table>
                <tbody>
                <tr>
                    <td class="gutter">
                        <pre><span class="line">1</span><br><span class="line">2</span><br><span
                                class="line">3</span><br><span class="line">4</span><br><span
                                class="line">5</span><br></pre>
                    </td>
                    <td class="code">
                        <pre><span class="line"><span class="meta">&gt;</span><span
                                class="bash">&gt;&gt; a = 1</span></span><br><span class="line"><span class="meta">&gt;</span><span
                                class="bash">&gt;&gt; id(a)</span></span><br><span class="line">140035503539424  # 内存地址的十进制表示</span><br><span
                                class="line"><span class="meta">&gt;</span><span
                                class="bash">&gt;&gt; hex(id(a))</span></span><br><span class="line">'0x7f5c8e71c4e0'  # 内存地址的十六进制表示</span><br></pre>
                    </td>
                </tr>
                </tbody>
            </table>
        </div>
    </figure>
    <div class="copy-btn"><i class="fa fa-clipboard"></i></div>
</div>

<p>在python中整数和短小的字符，python都会缓存这些对象，以便重复使用，当我们创建多个等于1的引用的时候，实际是让所有引用都指向同一个对象：</p>
<div class="highlight-wrap">
    <figure class="highlight shell">
        <div class="table-container">
            <table>
                <tbody>
                <tr>
                    <td class="gutter">
                        <pre><span class="line">1</span><br><span class="line">2</span><br><span
                                class="line">3</span><br></pre>
                    </td>
                    <td class="code">
                        <pre><span class="line"><span class="meta">&gt;</span><span
                                class="bash">&gt;&gt; b = 1</span></span><br><span class="line"><span class="meta">&gt;</span><span
                                class="bash">&gt;&gt; id(b)</span></span><br><span class="line">140035503539424  # 等于上面id(a)的值</span><br></pre>
                    </td>
                </tr>
                </tbody>
            </table>
        </div>
    </figure>
    <div class="copy-btn"><i class="fa fa-clipboard"></i></div>
</div>

<p>对比可以看出a和b实际是指向同一个对象的不同引用。 为了校验两个引用指向同一个对象，我们可以用“is”来判断。is用于判断两个引用所指的对象是否相同。</p>
<div class="highlight-wrap">
    <figure class="highlight python">
        <div class="table-container">
            <table>
                <tbody>
                <tr>
                    <td class="gutter">
                        <pre><span class="line">1</span><br><span class="line">2</span><br><span
                                class="line">3</span><br><span class="line">4</span><br><span
                                class="line">5</span><br><span class="line">6</span><br><span
                                class="line">7</span><br><span class="line">8</span><br><span
                                class="line">9</span><br><span class="line">10</span><br><span
                                class="line">11</span><br><span class="line">12</span><br><span
                                class="line">13</span><br><span class="line">14</span><br><span
                                class="line">15</span><br><span class="line">16</span><br><span
                                class="line">17</span><br><span class="line">18</span><br><span
                                class="line">19</span><br><span class="line">20</span><br><span
                                class="line">21</span><br><span class="line">22</span><br><span
                                class="line">23</span><br><span class="line">24</span><br><span
                                class="line">25</span><br></pre>
                    </td>
                    <td class="code">
                        <pre><span class="line">a = <span class="number">1</span></span><br><span
                                class="line">b = <span class="number">1</span></span><br><span class="line">print(a <span
                                class="keyword">is</span> b)</span><br><span class="line"><span
                                class="literal">True</span></span><br><span class="line"></span><br><span
                                class="line">a = <span class="string">"good"</span></span><br><span class="line">b = <span
                                class="string">"good"</span></span><br><span class="line">print(a <span
                                class="keyword">is</span> b)</span><br><span class="line"><span
                                class="literal">True</span></span><br><span class="line"></span><br><span
                                class="line">a = <span class="string">"very good morning"</span></span><br><span
                                class="line">b = <span class="string">"very good morning"</span></span><br><span
                                class="line">print(a <span class="keyword">is</span> b)</span><br><span
                                class="line"><span class="literal">True</span>   <span class="comment"># 原文在此处就是False，但是我的为True，通过查资料发现是python版本原因</span></span><br><span
                                class="line"><span class="comment"># Python2.3简单整数缓存范围是(-1,100)，Python2.5.4以后简单整数缓存范围至少是(-5,256)。所有的短字符也都在缓存区。</span></span><br><span
                                class="line"></span><br><span class="line">a = <span class="string">"为了校验两个引用指向同一个对象，我们可以用“is”来判断。is用于判断两个引用所指的对象是否相同。"</span></span><br><span
                                class="line">b = <span class="string">"为了校验两个引用指向同一个对象，我们可以用“is”来判断。is用于判断两个引用所指的对象是否相同。"</span></span><br><span
                                class="line">print(a <span class="keyword">is</span> b)</span><br><span
                                class="line"><span class="literal">False</span>  <span class="comment"># 增加了字符串的长度，结果也是False</span></span><br><span
                                class="line"></span><br><span class="line">a = []</span><br><span class="line">b = []</span><br><span
                                class="line">print(a <span class="keyword">is</span> b)</span><br><span
                                class="line"><span class="literal">False</span></span><br></pre>
                    </td>
                </tr>
                </tbody>
            </table>
        </div>
    </figure>
    <div class="copy-btn"><i class="fa fa-clipboard"></i></div>
</div>

<p>
    根据上面的运行结果，可以看到由于python缓存了整数和短字符串，因此每个对象只存有一份。比如所有的1的引用都指向同一对象。即使使用赋值语句，也只是创造了新的引用，而不是对象本身，长的字符串和其他对象可以有多个相同对象，可以使用赋值语句创建出新的对象。</p>
<p>在python中，每个对象都有存有指向该对象的应用总数，即<strong><em>引用计数(reference count)</em></strong> 呢 我们可以使用<code>sys</code>包中的<code>getrefcount()</code>，来查看某个对象的引用计数。需要注意的是，当使用某个引用作为参数，传递给<code>getrefcount()</code>时，会创建一个临时引用，所以结果会比预期多1。
</p>
<div class="highlight-wrap">
    <figure class="highlight python">
        <div class="table-container">
            <table>
                <tbody>
                <tr>
                    <td class="gutter">
                        <pre><span class="line">1</span><br><span class="line">2</span><br><span
                                class="line">3</span><br><span class="line">4</span><br><span
                                class="line">5</span><br><span class="line">6</span><br><span
                                class="line">7</span><br><span class="line">8</span><br></pre>
                    </td>
                    <td class="code">
                        <pre><span class="line"><span class="keyword">from</span> sys <span
                                class="keyword">import</span> getrefcount</span><br><span
                                class="line"></span><br><span class="line">a = [<span class="number">1</span>, <span
                                class="number">2</span>, <span class="number">3</span>]</span><br><span
                                class="line">print(getrefcount(a))</span><br><span class="line"><span
                                class="comment"># 2</span></span><br><span class="line">b = a</span><br><span
                                class="line">print(getrefcount(b))</span><br><span class="line"><span
                                class="comment"># 3</span></span><br></pre>
                    </td>
                </tr>
                </tbody>
            </table>
        </div>
    </figure>
    <div class="copy-btn"><i class="fa fa-clipboard"></i></div>
</div>

<p>由于上述原因，<code>getrefcount()</code>返回的结果分别是2,3，而不是期望的1。</p>
<hr>
<h3 id="对象引用对象"><a href="#对象引用对象" class="headerlink" title="对象引用对象"></a>对象引用对象</h3>
<p>python的一个容器对象（container），比如列表字典等，可以包含多个对象。实际上，容器对象中包含的并不是对象本身，而是指向各个元素对象的引用。</p>
<div class="highlight-wrap">
    <figure class="highlight python">
        <div class="table-container">
            <table>
                <tbody>
                <tr>
                    <td class="gutter">
                        <pre><span class="line">1</span><br><span class="line">2</span><br><span
                                class="line">3</span><br><span class="line">4</span><br><span
                                class="line">5</span><br><span class="line">6</span><br><span
                                class="line">7</span><br><span class="line">8</span><br><span
                                class="line">9</span><br></pre>
                    </td>
                    <td class="code">
                        <pre><span class="line"><span class="class"><span class="keyword">class</span> <span
                                class="title">from_obj</span><span class="params">(object)</span>:</span></span><br><span
                                class="line">    <span class="function"><span class="keyword">def</span> <span
                                class="title">__init__</span><span
                                class="params">(self, to_obj)</span>:</span></span><br><span class="line">        self.to_obj = to_obj</span><br><span
                                class="line">b = [<span class="number">1</span>,<span class="number">2</span>,<span
                                class="number">3</span>]</span><br><span
                                class="line">a = from_obj(b)</span><br><span class="line">print(id(a.to_obj))</span><br><span
                                class="line">print(id(b))</span><br><span class="line"><span class="comment"># 140035473779144</span></span><br><span
                                class="line"><span class="comment"># 140035473779144</span></span><br></pre>
                    </td>
                </tr>
                </tbody>
            </table>
        </div>
    </figure>
    <div class="copy-btn"><i class="fa fa-clipboard"></i></div>
</div>

<p>可以看到a引用了对象b。</p>
<p>对象引用对象是python最基本的构成方式。即使是a = 1这一赋值方式，实际上是让词典的一个键值“a”的元素引用整数对象1。该词典对象用于记录所有的全局引用。该词典引用了整数对象1。我们可以通过内置函数<code>globals()</code>来查看该词典。
    当一个对象a被另一个对象b引用时，a的引用计数将增加1。</p>
<div class="highlight-wrap">
    <figure class="highlight python">
        <div class="table-container">
            <table>
                <tbody>
                <tr>
                    <td class="gutter">
                        <pre><span class="line">1</span><br><span class="line">2</span><br><span
                                class="line">3</span><br><span class="line">4</span><br><span
                                class="line">5</span><br><span class="line">6</span><br><span
                                class="line">7</span><br></pre>
                    </td>
                    <td class="code">
                        <pre><span class="line"><span class="keyword">from</span> sys <span
                                class="keyword">import</span> getrefcount</span><br><span class="line">a = [<span
                                class="number">1</span>, <span class="number">2</span>, <span
                                class="number">3</span>]</span><br><span
                                class="line">print(getrefcount(a))</span><br><span
                                class="line">b = [a, a]</span><br><span
                                class="line">print(getrefcount(a))</span><br><span class="line"><span
                                class="comment"># 2</span></span><br><span class="line"><span
                                class="comment"># 4</span></span><br></pre>
                    </td>
                </tr>
                </tbody>
            </table>
        </div>
    </figure>
    <div class="copy-btn"><i class="fa fa-clipboard"></i></div>
</div>

<p>由于对象b引用了a两次，所以a的引用计数加2。</p>
<p>容器对象引用可能构成很复杂的拓扑结构。我们可以用objgraph包来绘制其引用关系。 objgraph是python的一个第三方包。<a href="http://mg.pov.lt/objgraph/"
                                                                        target="_blank"
                                                                        rel="noopener">objgraph官网</a>。</p>
<div class="highlight-wrap">
    <figure class="highlight bash">
        <div class="table-container">
            <table>
                <tbody>
                <tr>
                    <td class="gutter">
                        <pre><span class="line">1</span><br></pre>
                    </td>
                    <td class="code">
                        <pre><span class="line">pip install objgraph</span><br></pre>
                    </td>
                </tr>
                </tbody>
            </table>
        </div>
    </figure>
    <div class="copy-btn"><i class="fa fa-clipboard"></i></div>
</div>

<p> 使用objgraph需要安装xdot。根据自己的系统发行版本安装。</p>
<div class="highlight-wrap">
    <figure class="highlight bash">
        <div class="table-container">
            <table>
                <tbody>
                <tr>
                    <td class="gutter">
                        <pre><span class="line">1</span><br></pre>
                    </td>
                    <td class="code">
                        <pre><span
                                class="line">sudo pacman -S xdot或者 sudo apt install xdot，sudo yun install xdot</span><br></pre>
                    </td>
                </tr>
                </tbody>
            </table>
        </div>
    </figure>
    <div class="copy-btn"><i class="fa fa-clipboard"></i></div>
</div>

<div class="highlight-wrap">
    <figure class="highlight python">
        <div class="table-container">
            <table>
                <tbody>
                <tr>
                    <td class="gutter">
                        <pre><span class="line">1</span><br><span class="line">2</span><br><span
                                class="line">3</span><br><span class="line">4</span><br><span
                                class="line">5</span><br><span class="line">6</span><br></pre>
                    </td>
                    <td class="code">
                        <pre><span class="line">x = [<span class="number">1</span>, <span
                                class="number">2</span>, <span class="number">3</span>]</span><br><span
                                class="line">y = [x, dict(key1=x)]</span><br><span
                                class="line">z = [y, (x, y)]</span><br><span class="line"></span><br><span
                                class="line"><span class="keyword">import</span> objgraph</span><br><span
                                class="line">objgraph.show_refs([z], filename=<span
                                class="string">'ref_topo.png'</span>)</span><br></pre>
                    </td>
                </tr>
                </tbody>
            </table>
        </div>
    </figure>
    <div class="copy-btn"><i class="fa fa-clipboard"></i></div>
</div>

<p><img src="https://i.loli.net/2019/08/14/Tlr7paBWn3y9jGQ.png" alt="ref_topo.png"></p>
<p>两个对象可能互相引用，从而构成所谓的引用环（reference cycle）</p>
<div class="highlight-wrap">
    <figure class="highlight python">
        <div class="table-container">
            <table>
                <tbody>
                <tr>
                    <td class="gutter">
                        <pre><span class="line">1</span><br><span class="line">2</span><br><span
                                class="line">3</span><br><span class="line">4</span><br><span
                                class="line">5</span><br></pre>
                    </td>
                    <td class="code">
                        <pre><span class="line"><span class="meta">&gt;&gt;&gt; </span>a = []</span><br><span
                                class="line"><span class="meta">&gt;&gt;&gt; </span>b = [a]</span><br><span
                                class="line"><span class="meta">&gt;&gt;&gt; </span>a.append(b)</span><br><span
                                class="line"><span class="meta">&gt;&gt;&gt; </span>a</span><br><span class="line">[[[...]]]</span><br></pre>
                    </td>
                </tr>
                </tbody>
            </table>
        </div>
    </figure>
    <div class="copy-btn"><i class="fa fa-clipboard"></i></div>
</div>

<p>即使是一个对象，只需要自己引用自己，也能构成引用环。</p>
<div class="highlight-wrap">
    <figure class="highlight python">
        <div class="table-container">
            <table>
                <tbody>
                <tr>
                    <td class="gutter">
                        <pre><span class="line">1</span><br><span class="line">2</span><br><span
                                class="line">3</span><br><span class="line">4</span><br></pre>
                    </td>
                    <td class="code">
                        <pre><span class="line"><span class="meta">&gt;&gt;&gt; </span>a = []</span><br><span
                                class="line"><span class="meta">&gt;&gt;&gt; </span>a.append(a)</span><br><span
                                class="line"><span class="meta">&gt;&gt;&gt; </span>print(getrefcount(a))</span><br><span
                                class="line"><span class="number">3</span></span><br></pre>
                    </td>
                </tr>
                </tbody>
            </table>
        </div>
    </figure>
    <div class="copy-btn"><i class="fa fa-clipboard"></i></div>
</div>

<p>引用环会给垃圾回收机制带来很大的麻烦，我将在后面详细叙述这一点。</p>
<hr>
<h3 id="引用减少"><a href="#引用减少" class="headerlink" title="引用减少"></a>引用减少</h3>
<p>某个引用对象的引用计数可能减少。比如使用del关键字删除某个引用</p>
<div class="highlight-wrap">
    <figure class="highlight python">
        <div class="table-container">
            <table>
                <tbody>
                <tr>
                    <td class="gutter">
                        <pre><span class="line">1</span><br><span class="line">2</span><br><span
                                class="line">3</span><br><span class="line">4</span><br><span
                                class="line">5</span><br><span class="line">6</span><br><span
                                class="line">7</span><br></pre>
                    </td>
                    <td class="code">
                        <pre><span class="line"><span class="meta">&gt;&gt;&gt; </span>a = [<span
                                class="number">1</span>, <span class="number">2</span>, <span
                                class="number">3</span>]</span><br><span class="line"><span class="meta">&gt;&gt;&gt; </span>b = a</span><br><span
                                class="line"><span class="meta">&gt;&gt;&gt; </span>print(getrefcount(b))</span><br><span
                                class="line"><span class="number">3</span></span><br><span class="line"><span
                                class="meta">&gt;&gt;&gt; </span><span class="keyword">del</span> a</span><br><span
                                class="line"><span class="meta">&gt;&gt;&gt; </span>print(getrefcount(b))</span><br><span
                                class="line"><span class="number">2</span></span><br></pre>
                    </td>
                </tr>
                </tbody>
            </table>
        </div>
    </figure>
    <div class="copy-btn"><i class="fa fa-clipboard"></i></div>
</div>

<p>del也可以删除容器中的元素，比如：</p>
<div class="highlight-wrap">
    <figure class="highlight python">
        <div class="table-container">
            <table>
                <tbody>
                <tr>
                    <td class="gutter">
                        <pre><span class="line">1</span><br><span class="line">2</span><br><span
                                class="line">3</span><br><span class="line">4</span><br><span
                                class="line">5</span><br><span class="line">6</span><br><span
                                class="line">7</span><br><span class="line">8</span><br><span
                                class="line">9</span><br><span class="line">10</span><br><span
                                class="line">11</span><br></pre>
                    </td>
                    <td class="code">
                        <pre><span class="line"><span class="meta">&gt;&gt;&gt; </span>a = [<span
                                class="number">1</span>,<span class="number">2</span>,<span class="number">3</span>]</span><br><span
                                class="line"><span class="meta">&gt;&gt;&gt; </span><span class="keyword">del</span> a[<span
                                class="number">0</span>]</span><br><span class="line"><span class="meta">&gt;&gt;&gt; </span>print(a)</span><br><span
                                class="line">[<span class="number">2</span>, <span
                                class="number">3</span>]</span><br><span class="line"></span><br><span class="line"><span
                                class="meta">&gt;&gt;&gt; </span>b = {<span class="string">"q"</span>: <span
                                class="number">1</span>, <span class="string">"w"</span>:<span
                                class="number">2</span>}</span><br><span class="line"><span class="meta">&gt;&gt;&gt; </span>b</span><br><span
                                class="line">{<span class="string">'q'</span>: <span class="number">1</span>, <span
                                class="string">'w'</span>: <span class="number">2</span>}</span><br><span
                                class="line"><span class="meta">&gt;&gt;&gt; </span><span class="keyword">del</span> b[<span
                                class="string">"q"</span>]</span><br><span class="line"><span class="meta">&gt;&gt;&gt; </span>b</span><br><span
                                class="line">{<span class="string">'w'</span>: <span class="number">2</span>}</span><br></pre>
                    </td>
                </tr>
                </tbody>
            </table>
        </div>
    </figure>
    <div class="copy-btn"><i class="fa fa-clipboard"></i></div>
</div>

<p>如果某个引用指向对象a，当这个引用被重新定向到其他对象b的时候，对象a的引用计数会减少</p>
<div class="highlight-wrap">
    <figure class="highlight python">
        <div class="table-container">
            <table>
                <tbody>
                <tr>
                    <td class="gutter">
                        <pre><span class="line">1</span><br><span class="line">2</span><br><span
                                class="line">3</span><br><span class="line">4</span><br><span
                                class="line">5</span><br><span class="line">6</span><br><span
                                class="line">7</span><br><span class="line">8</span><br><span
                                class="line">9</span><br><span class="line">10</span><br></pre>
                    </td>
                    <td class="code">
                        <pre><span class="line"><span class="meta">&gt;&gt;&gt; </span><span
                                class="keyword">from</span> sys <span
                                class="keyword">import</span> getrefcount</span><br><span
                                class="line">...</span><br><span class="line"><span
                                class="meta">... </span>a = [<span class="number">1</span>, <span
                                class="number">2</span>, <span class="number">3</span>]</span><br><span
                                class="line"><span class="meta">... </span>b = a</span><br><span class="line"><span
                                class="meta">... </span>print(getrefcount(b))</span><br><span
                                class="line">...</span><br><span class="line"><span
                                class="meta">... </span>a = <span class="number">1</span></span><br><span
                                class="line"><span class="meta">... </span>print(getrefcount(b))</span><br><span
                                class="line"><span class="number">3</span></span><br><span class="line"><span
                                class="number">2</span></span><br></pre>
                    </td>
                </tr>
                </tbody>
            </table>
        </div>
    </figure>
    <div class="copy-btn"><i class="fa fa-clipboard"></i></div>
</div>

<hr>
<h3 id="垃圾回收"><a href="#垃圾回收" class="headerlink" title="垃圾回收"></a>垃圾回收</h3>
<p>当python中的对象越来越多，他占据的内存也会越来越大。不过不需要担心太多，python会在适当的时候启动垃圾<code>回收机制(garbage collection)</code>，将没用的对象清除，在许多语言中都有垃圾回收机制，比如Java和Ruby。
</p>
<p>从基本原理来说，当一个对象的引用计数降为0的时候，说明没有任何引用指向对象，这时候该对象就成为需要被清除的垃圾了。比如某个新建对象，分配给某个引用，引用数为1,当引用被删除之后，引用数为0，那么该对象就可以被垃圾回收。</p>
<div class="highlight-wrap">
    <figure class="highlight python">
        <div class="table-container">
            <table>
                <tbody>
                <tr>
                    <td class="gutter">
                        <pre><span class="line">1</span><br><span class="line">2</span><br></pre>
                    </td>
                    <td class="code">
                        <pre><span class="line">a = [<span class="number">1</span>,<span
                                class="number">2</span>,<span class="number">3</span>]</span><br><span class="line"><span
                                class="keyword">del</span> a</span><br></pre>
                    </td>
                </tr>
                </tbody>
            </table>
        </div>
    </figure>
    <div class="copy-btn"><i class="fa fa-clipboard"></i></div>
</div>

<p><code>del
    a</code>之后已经没有任何引用指向[1,2,3]了，用户不可能通过任何方式接触或者动用这个对象，这个对象如果继续待在内存里，就成了不健康的数据。当python的<strong><em>垃圾回收</em></strong>机制启动的时候，python扫描到这个引用为0的对象，就会将它所占据的内存清空。
</p>
<p>
    然而清理过程是个费力的过程。垃圾回收的时候，python不能进行其他的任务，频繁的垃圾回收，会大大降低python的工作效率。如果内存中的对象不多，就没必要总启动垃圾回收。所以python只会在特定的条件下，<strong><em>自动启动垃圾回收</em></strong>。当python运行的时候，会记录其中分配对象和取消分配对象的次数，两者的差值高于某个阈值的时候，垃圾回收才会启动。
    我们可以通过gc模块的<code>get_threshold()</code>来查看该阈值。</p>
<div class="highlight-wrap">
    <figure class="highlight python">
        <div class="table-container">
            <table>
                <tbody>
                <tr>
                    <td class="gutter">
                        <pre><span class="line">1</span><br><span class="line">2</span><br><span
                                class="line">3</span><br></pre>
                    </td>
                    <td class="code">
                        <pre><span class="line"><span class="meta">&gt;&gt;&gt; </span><span
                                class="keyword">import</span> gc</span><br><span class="line"><span class="meta">&gt;&gt;&gt; </span>gc.get_threshold()</span><br><span
                                class="line">(<span class="number">700</span>, <span class="number">10</span>, <span
                                class="number">10</span>)</span><br></pre>
                    </td>
                </tr>
                </tbody>
            </table>
        </div>
    </figure>
    <div class="copy-btn"><i class="fa fa-clipboard"></i></div>
</div>

<p>返回值中，后面的两个10,是与分代回收相关的阈值，分代回收在后面会讲到。700既是垃圾回收的启动阈值。可以通过gc中的<code>set_threshold()</code>来重新设定。 也可以手动使用<code>gc.collect()</code>启动垃圾回收机制。
</p>
<hr>
<h3 id="分代回收"><a href="#分代回收" class="headerlink" title="分代回收"></a>分代回收</h3>
<p>
    python同时使用了分代（generation）回收的策略。这一策略的基本假设是，存活时间越久的对象，越不可能在后面的程序中变成垃圾。我们的程序往往会产生大量的对象，许多对象很快产生和消失，但也有长期存在被使用的对象，出于信任和效率，对于这样一些对象，我们相信他的用处，所以减少在垃圾回收中扫描他们的频率。</p>
<p>
    python将所有的对象分为0,1,2三代，所有新建的对象都是0代对象，当某一代对象经历过垃圾回收之后，依然存活，那就归入到下一代中，垃圾回收启动时，一定会扫描所有的0代对象。如果0代对象经历过一定次数的垃圾回收，那么就启动对0待和1代的扫描清理，当1代也经历了一定数量的垃圾回收，那就启动对0,1,2，即所有的对象进行扫描。</p>
<p>上面<code>gc.get_threshold()</code>返回的（700,10,10）中后面的两个数，意义就是，每经过10次对0代的垃圾回收，就会配合启动一次对1代的扫描，没经过10次对1代的扫描，才会启动一次对2代的垃圾回收。
</p>
<p>同样可以用set_threshold()来调整，比如对2代对象进行更频繁的扫描。</p>
<div class="highlight-wrap">
    <figure class="highlight python">
        <div class="table-container">
            <table>
                <tbody>
                <tr>
                    <td class="gutter">
                        <pre><span class="line">1</span><br><span class="line">2</span><br></pre>
                    </td>
                    <td class="code">
                        <pre><span class="line"><span class="keyword">import</span> gc</span><br><span class="line">gc.set_threshold(<span
                                class="number">700</span>, <span class="number">10</span>, <span
                                class="number">5</span>)</span><br></pre>
                    </td>
                </tr>
                </tbody>
            </table>
        </div>
    </figure>
    <div class="copy-btn"><i class="fa fa-clipboard"></i></div>
</div>

<hr>
<h3 id="孤立的引用环"><a href="#孤立的引用环" class="headerlink" title="孤立的引用环"></a>孤立的引用环</h3>
<p>引用环的存在会给垃圾回收带来很大的困难，这些引用环可能构成无法使用，但是引用计数不为0的一些对象。</p>
<div class="highlight-wrap">
    <figure class="highlight python">
        <div class="table-container">
            <table>
                <tbody>
                <tr>
                    <td class="gutter">
                        <pre><span class="line">1</span><br><span class="line">2</span><br><span
                                class="line">3</span><br><span class="line">4</span><br><span
                                class="line">5</span><br></pre>
                    </td>
                    <td class="code">
                        <pre><span class="line">a = []</span><br><span class="line">b = [a]</span><br><span
                                class="line">a.append(b)</span><br><span class="line"><span
                                class="keyword">del</span> a</span><br><span class="line"><span
                                class="keyword">del</span> b</span><br></pre>
                    </td>
                </tr>
                </tbody>
            </table>
        </div>
    </figure>
    <div class="copy-btn"><i class="fa fa-clipboard"></i></div>
</div>

<p>上面我们先创建了两个表对象，并引用对方，构成一个引用环。删除了a，b引用之后，这两个对象不可能再从程序中调用，就没有什么用处了。但是由于引用环的存在，这两个对象的引用计数都没有降到0，不会被垃圾回收。 <img
        src="https://i.loli.net/2019/08/14/KZiDkvBopAafMHh.png" alt="孤立的引用环"></p>
<p>为了回收这样的引用环，Python复制每个对象的引用计数，可以记为gc_ref。假设，每个对象i，该计数为gc_ref_i。Python会遍历所有的对象i。对于每个对象i引用的对象j，将相应的gc_ref_j减1。 <img
        src="https://i.loli.net/2019/08/14/SezEXqxlitfMA1P.png" alt="遍历后的结果">
    在结束遍历后，gc_ref不为0的对象，和这些对象引用的对象，以及继续更下游引用的对象，需要被保留。而其它的对象则被垃圾回收。</p>
<hr>
<h3 id="总结"><a href="#总结" class="headerlink" title="总结"></a>总结</h3>
<p>
    python作为一种动态类型的语言，其对象和引用分离，这与面向过程的编程语言有很大的区别。为了有效的释放内存，python内置了垃圾回收的支持。python采用了一种相对简单的垃圾回收机制，即引用计数，并因此需要解决孤立引用环的问题。Python与其它语言既有共通性，又有特别的地方。对该内存管理机制的理解，是提高Python性能的重要一步。</p>

</div>



原文链接:https://zz.zzs7.top/python-memory-management.html