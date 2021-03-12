---
title: "谈谈对Python和其他语言区别"
cover: "/img/lynk/14.jpg"
date:       2019-11-28
subtitle: "从三个方面看Python"
tags:
	- Python
	- background
	- interview
---







<article class="_2rhmJa">
    <h3>从三个方面看Python</h3>
    <ul>
        <li>
            <h4>语言特点</h4>
        </li>
    </ul>
    <blockquote>
        <p>简洁 优雅 省略了各种大括号和分号,还有一些关键字,类型说明</p>
    </blockquote>
    <ul>
        <li>
            <h4>语言类型</h4>
        </li>
    </ul>
    <blockquote>
        <p>解释型语言,运行的时候是一行一行的解释,并运行,所以调试代码很方便,开发效率高.</p>
    </blockquote>
    <ul>
        <li>
            <h4>第三方库</h4>
        </li>
    </ul>
    <blockquote>
        <p>python是开源的,并且python的定位时任由其发展,应用领域很多<br>
            比如Web,运维,自动化测试,爬虫,数据分析,人工智能.Python具有非常完备的<br>
            第三方库</p>
    </blockquote>
    <ul>
        <li>
            <h4>一句话概括Python语言</h4>
        </li>
    </ul>
    <p><em>Python是一门语法简洁优美,功能强大无比,应用领域非常广泛,具有强大完备的第三方库的一门<br>
        弱类型的可移植,可扩展,可嵌入的解释型编程语言</em></p>
    <ul>
        <li>
            <h3>缺点就是</h3>
        </li>
        <li><strong>1. Python的执行速度不够快</strong></li>
    </ul>
    <blockquote>
        <p>Python是一门解释型语言,所以它的速度相较于c/c++ 会慢一些.但是并不影响使用<br>
            因为现在的硬件配置都非常的高,基本没什么影响.除非是一些实时性比较强的程序可能会受到<br>
            一些影响,但是也是有解决办法的,可以嵌入c\c++代码</p>
    </blockquote>
    <ul>
        <li><strong>2.Python的GIL(Global Interpreter Lock)全局解释器锁</strong></li>
    </ul>
    <h4>GIL是什么</h4>
    <p>
        首先明确一点GIL并不是Python的特性,而是解释器的特性.它是Python的解释器Cpython用来做多线程的控制和调度用的全局锁.保证同一个时刻只有一个线程在运行.Python还有一些别的解释器,比如Jpython就没有GIL锁.Cpython现在已经成了python的实现标准,所以我们都说python具有GIL限制.</p>
    <p><em>GIL的问题总体上来说是历史遗留的问题,以前的计算机的程序运行方式是单核多任务的模式,所以为了防止多个任务对同一资源进行同时的操作,竞争资源,才有了全局的解释器锁.但是随着近年来科技的进步,出现了多核,这样的话,全局锁就会限制多线程的并行.</em>
    </p>
    <h4>解决方法</h4>
    <ul>
        <li>使用multiprocessing(多进程)替代Thread(多线程)<br>
            multiprocessing库的的出现弥补了Python多线程并发限制的不足,每个进程都有自己独立的GIL,因此也不会出现进程之间的GIL的争夺.
        </li>
        <li>GIL只是Cpython解释器的产物,当然可以用其他的解释器来替代,但是由于其他的解释器,对C支持的不是很好,多以一直也不是很受欢迎.</li>
        <li>Python社区也在对GIL对于多线程的支持的一些改进.比如增加线程的优先级(高优先级的线程可以迫使其他线程释放所有的GIl锁)</li>
        <li>如果对并行计算性能较高的程序可以考虑把核心部分写成C模块,或者直接用其他语言代替.</li>
    </ul>
    <p>Python和Java相比:</p>
    <blockquote>
        <p>Python比Java要简单.Python是函数为一等公民的语言,而Java是类为一等公民的语言.Python是弱类型语言,而Java是强类型语言.</p>
    </blockquote>
    <p>Python和C相比</p>
    <blockquote>
        <p>对于使用:<br>
            Python的类库齐全并且使用简洁,很少代码实现的功能用C可能要很复杂<br>
            对于速度:<br>
            Python的运行速度相较于C,绝对是很慢了.Python和CPython解释器都是C语言编写的</p>
    </blockquote>
    <ul>
        <li>
            <h4>编译性 和 解释型语言</h4>
        </li>
    </ul>
    <blockquote>
        <p>解释型:就是边解释边执行<br>
            编译性:编译后再执行</p>
    </blockquote>
</article>