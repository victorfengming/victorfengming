---
title: '漫话：什么是协程？'
cover: "/img/lynk/97.jpg"
date:       2019-11-18
tags:
	- entertainment
---

<article class="article" id="mp-editor">
    <!-- 政务处理 -->
          <p data-role="original-title" style="display:none">原标题：漫画：什么是协程？</p>
            <blockquote> 
 <p><strong><span style="font-size: 16px;">来自：程序员小灰（微信号：chengxuyuanxiaohui）</span></strong></p> 
</blockquote> 
<p style="text-align: center;"><img src="http://5b0988e595225.cdn.sohucs.com/images/20180622/8dbdcbbb819540c882cabd3ea68b6764.jpeg"></p> 
<p style="text-align: center;"><img src="http://5b0988e595225.cdn.sohucs.com/images/20180622/e637c0d39b70431eb3b2f719cfa3b0db.jpeg"></p> 
<p style="text-align: center;"><span style="font-size: 20px;"><strong>————— 第二天 —————</strong></span></p> 
<p><img width="auto" src="http://5b0988e595225.cdn.sohucs.com/images/20180622/00df3b15b0304b7383970ead818cd94e.jpeg"></p> 
<p><img width="auto" src="http://5b0988e595225.cdn.sohucs.com/images/20180622/e34e7aa5fa45477fb81042100b0aedac.jpeg"></p> 
<p style="text-align: center;"><img src="http://5b0988e595225.cdn.sohucs.com/images/20180622/56033fea3556416da440b44359c8ce68.jpeg"></p> 
<p style="text-align: center;"><img src="http://5b0988e595225.cdn.sohucs.com/images/20180622/c221bbaa328b40e8801a7a5eb89eee64.jpeg"></p> 
<p style="text-align: center;"><img src="http://5b0988e595225.cdn.sohucs.com/images/20180622/2f61ced9e67e49219e99dfa4f71ba07a.jpeg"></p> 
<p style="text-align: center;"><span style="font-size: 16px;">————————————</span></p> 
<p><img width="auto" src="http://5b0988e595225.cdn.sohucs.com/images/20180622/51d5f17023cf4ca1887acd519154d3b8.jpeg"></p> 
<p><img width="auto" src="http://5b0988e595225.cdn.sohucs.com/images/20180622/595a33594f3f46239e653bb87e43a3ae.jpeg"></p> 
<p style="text-align: center;"><img src="http://5b0988e595225.cdn.sohucs.com/images/20180622/73722ba028784b0f82eb19facd5b4efb.jpeg"></p> 
<p style="text-align: center;"><img src="http://5b0988e595225.cdn.sohucs.com/images/20180622/91a32ed35ae445e6b3e8a42919faa12d.jpeg"></p> 
<p style="text-align: center;"><img src="http://5b0988e595225.cdn.sohucs.com/images/20180622/ae146b4471b2486280d675cce6514e49.jpeg"></p> 
<p style="text-align: center;"><img src="http://5b0988e595225.cdn.sohucs.com/images/20180622/6375384b85a544ed87c8cc382ba04cad.jpeg"></p> 
<p style="text-align: left;"><span style="font-size: 20px;"><strong>什么是进程和线程</strong></span></p> 
<p><span style="font-size: 16px;">有一定基础的小伙伴们肯定都知道进程和线程。</span></p> 
<p><span style="font-size: 16px;">进程是什么呢？</span></p> 
<p><span style="font-size: 16px;">直白地讲，进程就是应用程序的启动实例。比如我们运行一个游戏，打开一个软件，就是开启了一个进程。</span></p> 
<p><span style="font-size: 16px;">进程拥有代码和打开的文件资源、数据资源、独立的内存空间。</span></p> 
<p><span style="font-size: 16px;">线程又是什么呢？</span></p> 
<p><span style="font-size: 16px;">线程从属于进程，是程序的实际执行者。一个进程至少包含一个主线程，也可以有更多的子线程。</span></p> 
<p><span style="font-size: 16px;">线程拥有自己的栈空间。</span></p> 
<p style="text-align: center;"><img src="http://5b0988e595225.cdn.sohucs.com/images/20180622/6260a7a0e05c4b19a9b7465c8e56053e.jpeg"></p> 
<p><span style="font-size: 16px;">有人给出了很好的归纳：</span></p> 
<p><strong><span style="font-size: 16px;">对操作系统来说，线程是最小的执行单元，进程是最小的资源管理单元。</span></strong></p> 
<p><span style="font-size: 16px;">无论进程还是线程，都是由操作系统所管理的。</span></p> 
<p><span style="font-size: 16px;">Java中线程具有五种状态：</span></p> 
<p><strong><span style="font-size: 16px;">初始化</span></strong></p> 
<p><strong><span style="font-size: 16px;">可运行</span></strong></p> 
<p><strong><span style="font-size: 16px;">运行中</span></strong></p> 
<p><strong><span style="font-size: 16px;">阻塞</span></strong></p> 
<p><strong><span style="font-size: 16px;">销毁</span></strong></p> 
<p><span style="font-size: 16px;">这五种状态的转化关系如下：</span></p> 
<p style="text-align: center;"><img src="http://5b0988e595225.cdn.sohucs.com/images/20180622/82539cb6fc7b45bd94c4a6e3ad858bf2.png"></p> 
<p><span style="font-size: 16px;">但是，线程不同状态之间的转化是谁来实现的呢？是JVM吗？</span></p> 
<p><span style="font-size: 16px;">并不是。JVM需要通过操作系统内核中的TCB（Thread Control Block）模块来改变线程的状态，这一过程需要耗费一定的CPU资源。</span></p> 
<p><img src="http://5b0988e595225.cdn.sohucs.com/images/20180622/20abc0b6d1b74e3ab6be05ee08595b11.jpeg"></p> 
<p style="text-align: center;"><img src="http://5b0988e595225.cdn.sohucs.com/images/20180622/4731f3c6cb1e47dc9b8caae2977c0136.jpeg"></p> 
<p><strong><span style="font-size: 20px;">进程和线程的痛点</span></strong></p> 
<p><span style="font-size: 16px;">线程之间是如何进行协作的呢？</span></p> 
<p><span style="font-size: 16px;">最经典的例子就是<strong>生产者/消费者模式</strong>：</span></p> 
<p><span style="font-size: 16px;">若干个生产者线程向队列中写入数据，若干个消费者线程从队列中消费数据。</span></p> 
<p style="text-align: center;"><img src="http://5b0988e595225.cdn.sohucs.com/images/20180622/a83040de2d0b491e9e445d981870099a.png"></p> 
<p><span style="font-size: 16px;">如何用java语言实现生产者/消费者模式呢？</span></p> 
<p><span style="font-size: 16px;">让我们来看一看代码：</span></p> 
<p>public class ProducerConsumerTest {</p> 
<ol> 
 <li>public static void main(String args[]) {</li> 
 <li>final Queue&lt;Integer&gt; sharedQueue = new LinkedList();</li> 
 <li>Thread producer = new Producer(sharedQueue);</li> 
 <li>Thread consumer = new Consumer(sharedQueue);</li> 
 <li>producer.start();</li> 
 <li>consumer.start();</li> 
 <li>}</li> 
</ol> 
<p>}</p> 
<p>class Producer extends Thread {</p> 
<ol> 
 <li>private static final int MAX_QUEUE_SIZE = 5;</li> 
 <li></li> 
 <li>private final Queue sharedQueue;</li> 
 <li></li> 
 <li>public Producer(Queue sharedQueue) {</li> 
 <li>super();</li> 
 <li>this.sharedQueue = sharedQueue;</li> 
 <li>}</li> 
 <li></li> 
 <li>@Override</li> 
 <li>public void run() {</li> 
 <li>for (int i = 0; i &lt; 100; i++) {</li> 
 <li>synchronized (sharedQueue) {</li> 
 <li>while (sharedQueue.size() &gt;= MAX_QUEUE_SIZE) {</li> 
 <li>System.out.println("队列满了，等待消费");</li> 
 <li>try {</li> 
 <li>sharedQueue.wait();</li> 
 <li>} catch (InterruptedException e) {</li> 
 <li>e.printStackTrace();</li> 
 <li>}</li> 
 <li>}</li> 
 <li>sharedQueue.add(i);</li> 
 <li>System.out.println("进行生产 : " + i);</li> 
 <li>sharedQueue.notify();</li> 
 <li>}</li> 
 <li>}</li> 
 <li>}</li> 
</ol> 
<p>}</p> 
<p>class Consumer extends Thread {private final Queue sharedQueue; </p> 
<ol> 
 <li>public Consumer(Queue sharedQueue) {</li> 
 <li>super();</li> 
 <li>this.sharedQueue = sharedQueue;</li> 
 <li>}</li> 
 <li></li> 
 <li>@Override</li> 
 <li>public void run() {</li> 
 <li>while(true) {</li> 
 <li>synchronized (sharedQueue) {</li> 
 <li>while (sharedQueue.size() == 0) {</li> 
 <li>try {</li> 
 <li>System.out.println("队列空了，等待生产");</li> 
 <li>sharedQueue.wait();</li> 
 <li>} catch (InterruptedException e) {</li> 
 <li>e.printStackTrace();</li> 
 <li>}</li> 
 <li>}</li> 
 <li>int number = sharedQueue.poll();</li> 
 <li>System.out.println("进行消费 : " + number );</li> 
 <li>sharedQueue.notify();</li> 
 <li>}</li> 
 <li>}</li> 
 <li>}</li> 
</ol> 
<p>}</p> 
<p><span style="font-size: 16px;">这段代码做了下面几件事：</span></p> 
<p><span style="font-size: 16px;">1.定义了一个生产者类，一个消费者类。</span></p> 
<p><span style="font-size: 16px;">2.生产者类循环100次，向同步队列当中插入数据。</span></p> 
<p><span style="font-size: 16px;">3.消费者循环监听同步队列，当队列有数据时拉取数据。</span></p> 
<p><span style="font-size: 16px;">4.如果队列满了（达到5个元素），生产者阻塞。</span></p> 
<p><span style="font-size: 16px;">5.如果队列空了，消费者阻塞。</span></p> 
<p><span style="font-size: 16px;">上面的代码正确地实现了生产者/消费者模式，但是却并不是一个高性能的实现。为什么性能不高呢？原因如下：</span></p> 
<p><span style="font-size: 16px;">1.涉及到同步锁。</span></p> 
<p><span style="font-size: 16px;">2.涉及到线程阻塞状态和可运行状态之间的切换。</span></p> 
<p><span style="font-size: 16px;">3.涉及到线程上下文的切换。</span></p> 
<p><span style="font-size: 16px;">以上涉及到的任何一点，都是非常耗费性能的操作。</span></p> 
<p style="text-align: center;"><img src="http://5b0988e595225.cdn.sohucs.com/images/20180622/36cac4a04ae94cef95ac28435c05ed79.jpeg"></p> 
<p style="text-align: center;"><img src="http://5b0988e595225.cdn.sohucs.com/images/20180622/3d525b2f0c9c48cfbc7edecbf114d9da.jpeg"></p> 
<p><strong><span style="font-size: 20px;">什么是协程</span></strong></p> 
<p><strong><span style="font-size: 16px;">协程，英文Coroutines，是一种比线程更加轻量级的存在。</span></strong><span style="font-size: 16px;">正如一个进程可以拥有多个线程一样，一个线程也可以拥有多个协程。</span></p> 
<p style="text-align: center;"><img src="http://5b0988e595225.cdn.sohucs.com/images/20180622/6765e36cc4604fba897976638af03524.jpeg"></p> 
<p><span style="font-size: 16px;">最重要的是，协程不是被操作系统内核所管理，而完全是由程序所控制（也就是在用户态执行）。</span></p> 
<p><span style="font-size: 16px;">这样带来的好处就是性能得到了很大的提升，不会像线程切换那样消耗资源。</span></p> 
<p><span style="font-size: 16px;">既然协程这么好，它到底是怎么来使用的呢？</span></p> 
<p><span style="font-size: 16px;">由于Java的原生语法中并没有实现协程（某些开源框架实现了协程，但是很少被使用），所以我们来看一看python当中对协程的实现案例，同样以生产者消费者模式为例：</span></p> 
<p><img src="http://5b0988e595225.cdn.sohucs.com/images/20180622/8081394d462340cebbf7a31106f63474.png"></p> 
<p><span style="font-size: 16px;">这段代码十分简单，即使没用过python的小伙伴应该也能基本看懂。</span></p> 
<p><span style="font-size: 16px;">代码中创建了一个叫做consumer的协程，并且在主线程中生产数据，协程中消费数据。</span></p> 
<p><span style="font-size: 16px;">其中 <strong>yield </strong>是python当中的语法。当协程执行到yield关键字时，会暂停在那一行，等到主线程调用send方法发送了数据，协程才会接到数据继续执行。</span></p> 
<p><span style="font-size: 16px;">但是，yield让协程暂停，和线程的阻塞是有本质区别的。协程的暂停完全由程序控制，线程的阻塞状态是由操作系统内核来进行切换。</span></p> 
<p><span style="font-size: 16px;">因此，<strong>协程的开销远远小于线程的开销。</strong></span></p> 
<p style="text-align: center;"><img src="http://5b0988e595225.cdn.sohucs.com/images/20180622/a10f7d4eb8fd4f4b94e3bf4f72821fdd.jpeg"></p> 
<p style="text-align: center;"><img src="http://5b0988e595225.cdn.sohucs.com/images/20180622/1aa0c04319724fd6a2f88c19e255c001.jpeg"></p> 
<p><strong><span style="font-size: 20px;">协程的应用</span></strong></p> 
<p><span style="font-size: 16px;">有哪些编程语言应用到了协程呢？我们举几个栗子：</span></p> 
<p><strong><span style="font-size: 16px;">Lua语言</span></strong></p> 
<p><span style="font-size: 16px;">Lua从5.0版本开始使用协程，通过扩展库coroutine来实现。</span></p> 
<p><strong><span style="font-size: 16px;">Python语言</span></strong></p> 
<p><span style="font-size: 16px;">正如刚才所写的代码示例，python可以通过 yield/send 的方式实现协程。在python 3.5以后，<span style="font-size: 16px;"></span><span style="font-size: 16px;">async/await 成为</span>了更好的替代方案</span><span style="font-size: 16px;">。</span></p> 
<p><strong><span style="font-size: 16px;">Go语言</span></strong></p> 
<p><span style="font-size: 16px;">Go语言对协程的实现非常强大而简洁，可以轻松创建成百上千个协程并发执行。</span></p> 
<p><strong><span style="font-size: 16px;">Java语言</span></strong></p> 
<p><span style="font-size: 16px;">如上文所说，Java语言并没有对协程的原生支持，但是某些开源框架模拟出了协程的功能，有兴趣的小伙伴可以看一看<strong>Kilim框架</strong>的源码：</span></p> 
<p><span style="font-size: 16px;">https://github.com/kilim/kilim</span></p> 
<p style="text-align: center;"><img src="http://5b0988e595225.cdn.sohucs.com/images/20180622/0777cd1a4feb4570ae8527d910854daf.jpeg"></p> 
<p><strong><span style="font-size: 16px;">几点补充：</span></strong></p> 
<p><span style="font-size: 16px;">1.关于协程的概念，小灰也仅仅是知道一些皮毛，希望小伙伴们多多指正。</span></p> 
<p><strong>2.本漫画纯属娱乐，还请大家尽量珍惜当下的工作，切勿模仿小灰的行为哦。</strong></p> 
<p style="text-align: center;"><span style="font-size: 16px;">—————END—————</span></p> 
</article>