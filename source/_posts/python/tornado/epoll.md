---
title: "关于Epoll的使用详解"
date:       2019-12-05
subtitle: "Linux内核为处理大批量文件描述符而作了改进的poll"
tags:
	- Python
	- solution
	- web
---



本文转自:https://www.jianshu.com/p/ee381d365a29

<blockquote>
    <p>作者: 大呀大帝国 &lt;/br&gt;<br>
        <a href="https://link.jianshu.com?t=mailto:email:drnijq@126.com" target="_blank" rel="nofollow">email:drnijq@126.com</a>
    </p>
</blockquote>
<h2>1.Epoll简介</h2>
<p>EPOLL 的API用来执行类似poll()的任务。能够用于检测在多个文件描述符中任何IO可用的情况。Epoll API可以用于边缘触发(edge-triggered)和水平触发(level-triggered),
    同时epoll可以检测更多的文件描述符。以下的系统调用函数提供了创建和管理epoll实例：</p>
<ul>
    <li>epoll_create() 可以创建一个epoll实例并返回相应的文件描述符(epoll_create1() 扩展了epoll_create() 的功能)。</li>
    <li>注册相关的文件描述符使用epoll_ctl()</li>
    <li>epoll_wait() 可以用于等待IO事件。如果当前没有可用的事件，这个函数会阻塞调用线程。</li>
</ul>
<p><strong>边缘触发(edge-triggered 简称ET)和水平触发(level-triggered 简称LT)：</strong></p>
<p>epoll的事件派发接口可以运行在两种模式下：边缘触发(edge-triggered)和水平触发(level-triggered)，两种模式的区别请看下面,我们先假设下面的情况：</p>
<ol>
    <li>一个代表管道读取的文件描述符已经注册到epoll实例上了。</li>
    <li>在管道的写入端写入了2kb的数据。</li>
    <li>epoll_wait 返回一个可用的rfd文件描述符。</li>
    <li>从管道读取了1kb的数据。</li>
    <li>调用epoll_wait 完成。</li>
</ol>
<p>如果rfd被设置了ET，在调用完第五步的epool_wait
    后会被挂起，尽管在缓冲区还有可以读取的数据，同时另外一段的管道还在等待发送完毕的反馈。这是因为ET模式下只有文件描述符发生改变的时候，才会派发事件。所以第五步操作，可能会去等待已经存在缓冲区的数据。在上面的例子中，一个事件在第二步被创建，再第三步中被消耗，由于第四步中没有读取完缓冲区，第五步中的epoll_wait可能会一直被阻塞下去。</p>
<p>下面情况下推荐使用ET模式:</p>
<ol>
    <li>使用非阻塞的IO。</li>
    <li>epoll_wait() 只需要在read或者write返回的时候。</li>
</ol>
<p>相比之下，当我们使用LT的时候（默认）,epoll会比poll更简单更快速，而且我们可以使用在任何一个地方。</p>
<h2>2.API介绍</h2>
<p>先简单的看下EPOLL的API</p>
<h3>2.1 创建epoll</h3>
<hr>
<div class="_2Uzcx_">
    <button class="VJbwyy" type="button" aria-label="复制代码"><i aria-label="icon: copy" class="anticon anticon-copy">
        <svg viewBox="64 64 896 896" focusable="false" class="" data-icon="copy" width="1em" height="1em"
             fill="currentColor" aria-hidden="true">
            <path d="M832 64H296c-4.4 0-8 3.6-8 8v56c0 4.4 3.6 8 8 8h496v688c0 4.4 3.6 8 8 8h56c4.4 0 8-3.6 8-8V96c0-17.7-14.3-32-32-32zM704 192H192c-17.7 0-32 14.3-32 32v530.7c0 8.5 3.4 16.6 9.4 22.6l173.3 173.3c2.2 2.2 4.7 4 7.4 5.5v1.9h4.2c3.5 1.3 7.2 2 11 2H704c17.7 0 32-14.3 32-32V224c0-17.7-14.3-32-32-32zM350 856.2L263.9 770H350v86.2zM664 888H414V746c0-22.1-17.9-40-40-40H232V264h432v624z"></path>
        </svg>
    </i></button>
    <pre class="line-numbers  language-c"><code class="c  language-c"><span class="token macro property">#<span
            class="token directive keyword">include</span> <span
            class="token string">&lt;sys/epoll.h&gt;</span></span>

<span class="token keyword">int</span> <span class="token function">epoll_create</span><span
                class="token punctuation">(</span><span class="token keyword">int</span> size<span
                class="token punctuation">)</span><span class="token punctuation">;</span>
<span class="token keyword">int</span> <span class="token function">epoll_create1</span><span class="token punctuation">(</span><span
                class="token keyword">int</span> flags<span class="token punctuation">)</span><span
                class="token punctuation">;</span>
<span aria-hidden="true"
      class="line-numbers-rows"><span></span><span></span><span></span><span></span></span></code></pre>
</div>
<p>epoll_create() 可以创建一个epoll实例。在linux 内核版本大于2.6.8 后，这个<strong><em>size</em></strong> 参数就被弃用了，但是传入的值必须大于0。</p>
<blockquote>
    <p>在 epoll_create () 的最初实现版本时， size参数的作用是创建epoll实例时候告诉内核需要使用多少个文件描述符。内核会使用 size 的大小去申请对应的内存(如果在使用的时候超过了给定的size，
        内核会申请更多的空间)。现在，这个size参数不再使用了（内核会动态的申请需要的内存）。但要注意的是，这个size必须要大于0，为了兼容旧版的linux 内核的代码。</p>
</blockquote>
<p>epoll_create() 会返回新的epoll对象的文件描述符。这个文件描述符用于后续的epoll操作。如果不需要使用这个描述符，请使用close关闭。</p>
<p>epoll_create1()
    如果<strong><em>flags</em></strong>的值是0，epoll_create1()等同于epoll_create()除了过时的size被遗弃了。当然<strong><em>flasg</em></strong>可以使用
    EPOLL_CLOEXEC，请查看 open() 中的O_CLOEXEC来查看 EPOLL_CLOEXEC有什么用。</p>
<p><strong><em>返回值:</em></strong> 如果执行成功，返回一个非负数(实际为文件描述符), 如果执行失败，会返回-1，具体原因请查看error.</p>
<h3>2.2 设置epoll事件</h3>
<hr>
<div class="_2Uzcx_">
    <button class="VJbwyy" type="button" aria-label="复制代码"><i aria-label="icon: copy" class="anticon anticon-copy">
        <svg viewBox="64 64 896 896" focusable="false" class="" data-icon="copy" width="1em" height="1em"
             fill="currentColor" aria-hidden="true">
            <path d="M832 64H296c-4.4 0-8 3.6-8 8v56c0 4.4 3.6 8 8 8h496v688c0 4.4 3.6 8 8 8h56c4.4 0 8-3.6 8-8V96c0-17.7-14.3-32-32-32zM704 192H192c-17.7 0-32 14.3-32 32v530.7c0 8.5 3.4 16.6 9.4 22.6l173.3 173.3c2.2 2.2 4.7 4 7.4 5.5v1.9h4.2c3.5 1.3 7.2 2 11 2H704c17.7 0 32-14.3 32-32V224c0-17.7-14.3-32-32-32zM350 856.2L263.9 770H350v86.2zM664 888H414V746c0-22.1-17.9-40-40-40H232V264h432v624z"></path>
        </svg>
    </i></button>
    <pre class="line-numbers  language-c"><code class="c++ ++  language-c"><span class="token macro property">#<span
            class="token directive keyword">include</span> <span
            class="token string">&lt;sys/epoll.h&gt;</span></span>

<span class="token keyword">int</span> <span class="token function">epoll_ctl</span><span
                class="token punctuation">(</span><span class="token keyword">int</span> epfd<span
                class="token punctuation">,</span> <span class="token keyword">int</span> op<span
                class="token punctuation">,</span> <span class="token keyword">int</span> fd<span
                class="token punctuation">,</span> <span class="token keyword">struct</span> <span
                class="token class-name">epoll_event</span> <span class="token operator">*</span>event<span
                class="token punctuation">)</span><span class="token punctuation">;</span>
<span aria-hidden="true" class="line-numbers-rows"><span></span><span></span><span></span></span></code></pre>
</div>
<p>
    这个系统调用能够控制给定的文件描述符<strong><em>epfd</em></strong>指向的epoll实例，<strong><em>op</em></strong>是添加事件的类型，<strong><em>fd</em></strong>是目标文件描述符。
</p>
<p>有效的op值有以下几种：</p>
<ul>
    <li>EPOLL_CTL_ADD
        在<strong><em>epfd</em></strong>中注册指定的fd文件描述符并能把<strong><em>event</em></strong>和<strong><em>fd</em></strong>关联起来。
    </li>
    <li>EPOLL_CTL_MOD 改变*** fd<strong><em>和</em></strong>evetn***之间的联系。</li>
    <li>EPOLL_CTL_DEL
        从指定的<strong><em>epfd</em></strong>中删除<strong><em>fd</em></strong>文件描述符。在这种模式中<strong><em>event</em></strong>是被忽略的，并且为可以等于NULL。
    </li>
</ul>
<p><strong><em>event</em></strong>这个参数是用于关联制定的<strong><em>fd</em></strong>文件描述符的。它的定义如下：</p>
<div class="_2Uzcx_">
    <button class="VJbwyy" type="button" aria-label="复制代码"><i aria-label="icon: copy" class="anticon anticon-copy">
        <svg viewBox="64 64 896 896" focusable="false" class="" data-icon="copy" width="1em" height="1em"
             fill="currentColor" aria-hidden="true">
            <path d="M832 64H296c-4.4 0-8 3.6-8 8v56c0 4.4 3.6 8 8 8h496v688c0 4.4 3.6 8 8 8h56c4.4 0 8-3.6 8-8V96c0-17.7-14.3-32-32-32zM704 192H192c-17.7 0-32 14.3-32 32v530.7c0 8.5 3.4 16.6 9.4 22.6l173.3 173.3c2.2 2.2 4.7 4 7.4 5.5v1.9h4.2c3.5 1.3 7.2 2 11 2H704c17.7 0 32-14.3 32-32V224c0-17.7-14.3-32-32-32zM350 856.2L263.9 770H350v86.2zM664 888H414V746c0-22.1-17.9-40-40-40H232V264h432v624z"></path>
        </svg>
    </i></button>
    <pre class="line-numbers  language-c"><code class="c  language-c"><span
            class="token keyword">typedef</span> <span class="token keyword">union</span> epoll_data <span
            class="token punctuation">{</span>
    <span class="token keyword">void</span>        <span class="token operator">*</span>ptr<span
                class="token punctuation">;</span>
    <span class="token keyword">int</span>          fd<span class="token punctuation">;</span>
    uint32_t     u32<span class="token punctuation">;</span>
    uint64_t     u64<span class="token punctuation">;</span>
<span class="token punctuation">}</span> epoll_data_t<span class="token punctuation">;</span>

<span class="token keyword">struct</span> <span class="token class-name">epoll_event</span> <span
                class="token punctuation">{</span>
    uint32_t     events<span class="token punctuation">;</span>      <span
                class="token comment">/* Epoll events */</span>
    epoll_data_t data<span class="token punctuation">;</span>        <span class="token comment">/* User data variable */</span>
<span class="token punctuation">}</span><span class="token punctuation">;</span>
<span aria-hidden="true"
      class="line-numbers-rows"><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span></span></code></pre>
</div>
<p><strong><em>events</em></strong>这个参数是一个字节的掩码构成的。下面是可以用的事件：</p>
<ul>
    <li>EPOLLIN - 当关联的文件可以执行 read ()操作时。</li>
    <li>EPOLLOUT - 当关联的文件可以执行 write ()操作时。</li>
    <li>EPOLLRDHUP - (从 linux 2.6.17 开始)当socket关闭的时候，或者半关闭写段的(当使用边缘触发的时候，这个标识在写一些测试代码去检测关闭的时候特别好用)</li>
    <li>EPOLLPRI - 当 read ()能够读取紧急数据的时候。</li>
    <li>EPOLLERR - 当关联的文件发生错误的时候，epoll_wait() 总是会等待这个事件，并不是需要必须设置的标识。</li>
    <li>EPOLLHUP - 当指定的文件描述符被挂起的时候。epoll_wait()
        总是会等待这个事件，并不是需要必须设置的标识。当socket从某一个地方读取数据的时候(管道或者socket),这个事件只是标识出这个已经读取到最后了(EOF)。所有的有效数据已经被读取完毕了，之后任何的读取都会返回0(EOF)。
    </li>
    <li>EPOLLET - 设置指定的文件描述符模式为边缘触发，默认的模式是水平触发。</li>
    <li>EPOLLONESHOT - (从 linux 2.6.17 开始)设置指定文件描述符为单次模式。这意味着，在设置后只会有一次从epoll_wait() 中捕获到事件，之后你必须要重新调用 epoll_ctl()
        重新设置。
    </li>
</ul>
<p><strong><em>返回值：</em></strong>如果成功，返回0。如果失败，会返回-1， <strong><em>errno</em></strong>将会被设置</p>
<p>有以下几种错误：</p>
<ul>
    <li>EBADF - <strong><em>epfd</em></strong> 或者 <strong><em>fd</em></strong> 是无效的文件描述符。</li>
    <li>EEXIST - <strong><em>op</em></strong>是EPOLL_CTL_ADD，同时 <strong><em>fd</em></strong> 在之前，已经被注册到epoll中了。</li>
    <li>EINVAL -
        <strong><em>epfd</em></strong>不是一个epoll描述符。或者<strong><em>fd</em></strong>和<strong><em>epfd</em></strong>相同，或者<strong><em>op</em></strong>参数非法。
    </li>
    <li>ENOENT - <strong><em>op</em></strong>是EPOLL_CTL_MOD或者EPOLL_CTL_DEL，但是<strong><em>fd</em></strong>还没有被注册到epoll上。
    </li>
    <li>ENOMEM - 内存不足。</li>
    <li>EPERM - 目标的<strong><em>fd</em></strong>不支持epoll。</li>
</ul>
<hr>
<h3>2.3 等待epoll事件</h3>
<div class="_2Uzcx_">
    <button class="VJbwyy" type="button" aria-label="复制代码"><i aria-label="icon: copy" class="anticon anticon-copy">
        <svg viewBox="64 64 896 896" focusable="false" class="" data-icon="copy" width="1em" height="1em"
             fill="currentColor" aria-hidden="true">
            <path d="M832 64H296c-4.4 0-8 3.6-8 8v56c0 4.4 3.6 8 8 8h496v688c0 4.4 3.6 8 8 8h56c4.4 0 8-3.6 8-8V96c0-17.7-14.3-32-32-32zM704 192H192c-17.7 0-32 14.3-32 32v530.7c0 8.5 3.4 16.6 9.4 22.6l173.3 173.3c2.2 2.2 4.7 4 7.4 5.5v1.9h4.2c3.5 1.3 7.2 2 11 2H704c17.7 0 32-14.3 32-32V224c0-17.7-14.3-32-32-32zM350 856.2L263.9 770H350v86.2zM664 888H414V746c0-22.1-17.9-40-40-40H232V264h432v624z"></path>
        </svg>
    </i></button>
    <pre class="line-numbers  language-c"><code class="c  language-c"><span class="token macro property">#<span
            class="token directive keyword">include</span> <span
            class="token string">&lt;sys/epoll.h&gt;</span></span>

<span class="token keyword">int</span> <span class="token function">epoll_wait</span><span
                class="token punctuation">(</span><span class="token keyword">int</span> epfd<span
                class="token punctuation">,</span> <span class="token keyword">struct</span> <span
                class="token class-name">epoll_event</span> <span class="token operator">*</span>events<span
                class="token punctuation">,</span>
                      <span class="token keyword">int</span> maxevents<span class="token punctuation">,</span> <span
                class="token keyword">int</span> timeout<span class="token punctuation">)</span><span
                class="token punctuation">;</span>
                      
<span class="token keyword">int</span> <span class="token function">epoll_pwait</span><span
                class="token punctuation">(</span><span class="token keyword">int</span> epfd<span
                class="token punctuation">,</span> <span class="token keyword">struct</span> <span
                class="token class-name">epoll_event</span> <span class="token operator">*</span>events<span
                class="token punctuation">,</span>
                      <span class="token keyword">int</span> maxevents<span class="token punctuation">,</span> <span
                class="token keyword">int</span> timeout<span class="token punctuation">,</span>
                      <span class="token keyword">const</span> sigset_t <span
                class="token operator">*</span>sigmask<span class="token punctuation">)</span><span
                class="token punctuation">;</span>
<span aria-hidden="true"
      class="line-numbers-rows"><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span></span></code></pre>
</div>
<p>epoll_wait
    这个系统调用是用来等待<strong><em>epfd</em></strong>中的事件。<strong><em>events</em></strong>指向调用者可以使用的事件的内存区域。<strong><em>maxevents</em></strong>告知内核有多少个events，必须要大于0.
</p>
<p><strong><em>timeout</em></strong>这个参数是用来制定epoll_wait 会阻塞多少毫秒，会一直阻塞到下面几种情况：</p>
<ol>
    <li>一个文件描述符触发了事件。</li>
    <li>被一个信号处理函数打断，或者timeout超时。</li>
</ol>
<p>当<strong><em>timeout</em></strong>等于-1的时候这个函数会无限期的阻塞下去，当<strong><em>timeout</em></strong>等于0的时候，就算没有任何事件，也会立刻返回。
</p>
<p>struct epoll_event 如下定义:</p>
<div class="_2Uzcx_">
    <button class="VJbwyy" type="button" aria-label="复制代码"><i aria-label="icon: copy" class="anticon anticon-copy">
        <svg viewBox="64 64 896 896" focusable="false" class="" data-icon="copy" width="1em" height="1em"
             fill="currentColor" aria-hidden="true">
            <path d="M832 64H296c-4.4 0-8 3.6-8 8v56c0 4.4 3.6 8 8 8h496v688c0 4.4 3.6 8 8 8h56c4.4 0 8-3.6 8-8V96c0-17.7-14.3-32-32-32zM704 192H192c-17.7 0-32 14.3-32 32v530.7c0 8.5 3.4 16.6 9.4 22.6l173.3 173.3c2.2 2.2 4.7 4 7.4 5.5v1.9h4.2c3.5 1.3 7.2 2 11 2H704c17.7 0 32-14.3 32-32V224c0-17.7-14.3-32-32-32zM350 856.2L263.9 770H350v86.2zM664 888H414V746c0-22.1-17.9-40-40-40H232V264h432v624z"></path>
        </svg>
    </i></button>
    <pre class="line-numbers  language-c"><code class="c  language-c"><span
            class="token keyword">typedef</span> <span class="token keyword">union</span> epoll_data <span
            class="token punctuation">{</span>
    <span class="token keyword">void</span>    <span class="token operator">*</span>ptr<span
                class="token punctuation">;</span>
    <span class="token keyword">int</span>      fd<span class="token punctuation">;</span>
    uint32_t u32<span class="token punctuation">;</span>
    uint64_t u64<span class="token punctuation">;</span>
<span class="token punctuation">}</span> epoll_data_t<span class="token punctuation">;</span>

<span class="token keyword">struct</span> <span class="token class-name">epoll_event</span> <span
                class="token punctuation">{</span>
    uint32_t     events<span class="token punctuation">;</span>    <span class="token comment">/* Epoll events */</span>
    epoll_data_t data<span class="token punctuation">;</span>      <span
                class="token comment">/* User data variable */</span>
<span class="token punctuation">}</span><span class="token punctuation">;</span>
<span aria-hidden="true"
      class="line-numbers-rows"><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span></span></code></pre>
</div>
<p>每次epoll_wait() 返回的时候，会包含用户在epoll_ctl中设置的events。</p>
<p>还有一个系统调用epoll_pwait ()。epoll_pwait()和epoll_wait ()的关系就像select()和
    pselect()的关系。和pselect()一样，epoll_pwait()可以让应用程序安全的等待知道某一个文件描述符就绪或者捕捉到信号。</p>
<p>下面的 epoll_pwait () 调用：</p>
<div class="_2Uzcx_">
    <button class="VJbwyy" type="button" aria-label="复制代码"><i aria-label="icon: copy" class="anticon anticon-copy">
        <svg viewBox="64 64 896 896" focusable="false" class="" data-icon="copy" width="1em" height="1em"
             fill="currentColor" aria-hidden="true">
            <path d="M832 64H296c-4.4 0-8 3.6-8 8v56c0 4.4 3.6 8 8 8h496v688c0 4.4 3.6 8 8 8h56c4.4 0 8-3.6 8-8V96c0-17.7-14.3-32-32-32zM704 192H192c-17.7 0-32 14.3-32 32v530.7c0 8.5 3.4 16.6 9.4 22.6l173.3 173.3c2.2 2.2 4.7 4 7.4 5.5v1.9h4.2c3.5 1.3 7.2 2 11 2H704c17.7 0 32-14.3 32-32V224c0-17.7-14.3-32-32-32zM350 856.2L263.9 770H350v86.2zM664 888H414V746c0-22.1-17.9-40-40-40H232V264h432v624z"></path>
        </svg>
    </i></button>
    <pre class="line-numbers  language-c"><code class="c  language-c">ready <span
            class="token operator">=</span> <span class="token function">epoll_pwait</span><span
            class="token punctuation">(</span>epfd<span class="token punctuation">,</span> <span
            class="token operator">&amp;</span>events<span class="token punctuation">,</span> maxevents<span
            class="token punctuation">,</span> timeout<span class="token punctuation">,</span> <span
            class="token operator">&amp;</span>sigmask<span class="token punctuation">)</span><span
            class="token punctuation">;</span>
<span aria-hidden="true" class="line-numbers-rows"><span></span></span></code></pre>
</div>
<p>在内部等同于:</p>
<div class="_2Uzcx_">
    <button class="VJbwyy" type="button" aria-label="复制代码"><i aria-label="icon: copy" class="anticon anticon-copy">
        <svg viewBox="64 64 896 896" focusable="false" class="" data-icon="copy" width="1em" height="1em"
             fill="currentColor" aria-hidden="true">
            <path d="M832 64H296c-4.4 0-8 3.6-8 8v56c0 4.4 3.6 8 8 8h496v688c0 4.4 3.6 8 8 8h56c4.4 0 8-3.6 8-8V96c0-17.7-14.3-32-32-32zM704 192H192c-17.7 0-32 14.3-32 32v530.7c0 8.5 3.4 16.6 9.4 22.6l173.3 173.3c2.2 2.2 4.7 4 7.4 5.5v1.9h4.2c3.5 1.3 7.2 2 11 2H704c17.7 0 32-14.3 32-32V224c0-17.7-14.3-32-32-32zM350 856.2L263.9 770H350v86.2zM664 888H414V746c0-22.1-17.9-40-40-40H232V264h432v624z"></path>
        </svg>
    </i></button>
    <pre class="line-numbers  language-c"><code class="c  language-c"><span
            class="token function">pthread_sigmask</span><span class="token punctuation">(</span>SIG_SETMASK<span
            class="token punctuation">,</span> <span class="token operator">&amp;</span>sigmask<span
            class="token punctuation">,</span> <span class="token operator">&amp;</span>origmask<span
            class="token punctuation">)</span><span class="token punctuation">;</span>
ready <span class="token operator">=</span> <span class="token function">epoll_wait</span><span
                class="token punctuation">(</span>epfd<span class="token punctuation">,</span> <span
                class="token operator">&amp;</span>events<span class="token punctuation">,</span> maxevents<span
                class="token punctuation">,</span> timeout<span class="token punctuation">)</span><span
                class="token punctuation">;</span>
<span class="token function">pthread_sigmask</span><span class="token punctuation">(</span>SIG_SETMASK<span
                class="token punctuation">,</span> <span class="token operator">&amp;</span>origmask<span
                class="token punctuation">,</span> <span class="token constant">NULL</span><span
                class="token punctuation">)</span><span class="token punctuation">;</span>
<span aria-hidden="true" class="line-numbers-rows"><span></span><span></span><span></span></span></code></pre>
</div>
<p>如果 <strong><em>sigmask</em></strong>为NULL, epoll_pwait()等同于epoll_wait()。</p>
<p><strong><em>返回值：</em></strong>有多少个IO事件已经准备就绪。如果返回0说明没有IO事件就绪，而是timeout超时。遇到错误的时候，会返回-1，并设置 errno。</p>
<p>有以下几种错误:</p>
<ul>
    <li>EBADF - <strong><em>epfd</em></strong>是无效的文件描述符</li>
    <li>EFAULT - 指针<strong><em>events</em></strong>指向的内存没有访问权限</li>
    <li>EINTR - 这个调用被信号打断。</li>
    <li>EINVAL - <strong><em>epfd</em></strong>不是一个epoll的文件描述符，或者<strong><em>maxevents</em></strong>小于等于0</li>
</ul>
<h2>3. 官方demo</h2>
<div class="_2Uzcx_">
    <button class="VJbwyy" type="button" aria-label="复制代码"><i aria-label="icon: copy" class="anticon anticon-copy">
        <svg viewBox="64 64 896 896" focusable="false" class="" data-icon="copy" width="1em" height="1em"
             fill="currentColor" aria-hidden="true">
            <path d="M832 64H296c-4.4 0-8 3.6-8 8v56c0 4.4 3.6 8 8 8h496v688c0 4.4 3.6 8 8 8h56c4.4 0 8-3.6 8-8V96c0-17.7-14.3-32-32-32zM704 192H192c-17.7 0-32 14.3-32 32v530.7c0 8.5 3.4 16.6 9.4 22.6l173.3 173.3c2.2 2.2 4.7 4 7.4 5.5v1.9h4.2c3.5 1.3 7.2 2 11 2H704c17.7 0 32-14.3 32-32V224c0-17.7-14.3-32-32-32zM350 856.2L263.9 770H350v86.2zM664 888H414V746c0-22.1-17.9-40-40-40H232V264h432v624z"></path>
        </svg>
    </i></button>
    <pre class="line-numbers  language-c"><code class="c++ ++  language-c"><span class="token macro property">#<span
            class="token directive keyword">define</span> MAX_EVENTS 10</span>
<span class="token keyword">struct</span> <span class="token class-name">epoll_event</span>  ev<span
                class="token punctuation">,</span> events<span class="token punctuation">[</span>MAX_EVENTS<span
                class="token punctuation">]</span><span class="token punctuation">;</span>
<span class="token keyword">int</span>         listen_sock<span class="token punctuation">,</span> conn_sock<span
                class="token punctuation">,</span> nfds<span class="token punctuation">,</span> epollfd<span
                class="token punctuation">;</span>


<span class="token comment">/* Code to set up listening socket, 'listen_sock',
 * (socket(), bind(), listen()) omitted */</span>

epollfd <span class="token operator">=</span> <span class="token function">epoll_create1</span><span
                class="token punctuation">(</span> <span class="token number">0</span> <span
                class="token punctuation">)</span><span class="token punctuation">;</span>
<span class="token keyword">if</span> <span class="token punctuation">(</span> epollfd <span
                class="token operator">==</span> <span class="token operator">-</span><span
                class="token number">1</span> <span class="token punctuation">)</span>
<span class="token punctuation">{</span>
    <span class="token function">perror</span><span class="token punctuation">(</span> <span class="token string">"epoll_create1"</span> <span
                class="token punctuation">)</span><span class="token punctuation">;</span>
    <span class="token function">exit</span><span class="token punctuation">(</span> EXIT_FAILURE <span
                class="token punctuation">)</span><span class="token punctuation">;</span>
<span class="token punctuation">}</span>

ev<span class="token punctuation">.</span>events   <span class="token operator">=</span> EPOLLIN<span
                class="token punctuation">;</span>
ev<span class="token punctuation">.</span>data<span class="token punctuation">.</span>fd  <span
                class="token operator">=</span> listen_sock<span class="token punctuation">;</span>
<span class="token keyword">if</span> <span class="token punctuation">(</span> <span
                class="token function">epoll_ctl</span><span class="token punctuation">(</span> epollfd<span
                class="token punctuation">,</span> EPOLL_CTL_ADD<span
                class="token punctuation">,</span> listen_sock<span
                class="token punctuation">,</span> <span class="token operator">&amp;</span>ev <span
                class="token punctuation">)</span> <span class="token operator">==</span> <span
                class="token operator">-</span><span class="token number">1</span> <span
                class="token punctuation">)</span>
<span class="token punctuation">{</span>
    <span class="token function">perror</span><span class="token punctuation">(</span> <span class="token string">"epoll_ctl: listen_sock"</span> <span
                class="token punctuation">)</span><span class="token punctuation">;</span>
    <span class="token function">exit</span><span class="token punctuation">(</span> EXIT_FAILURE <span
                class="token punctuation">)</span><span class="token punctuation">;</span>
<span class="token punctuation">}</span>

<span class="token keyword">for</span> <span class="token punctuation">(</span><span
                class="token punctuation">;</span><span class="token punctuation">;</span> <span
                class="token punctuation">)</span>
<span class="token punctuation">{</span>
    nfds <span class="token operator">=</span> <span class="token function">epoll_wait</span><span
                class="token punctuation">(</span> epollfd<span class="token punctuation">,</span> events<span
                class="token punctuation">,</span> MAX_EVENTS<span class="token punctuation">,</span> <span
                class="token operator">-</span><span class="token number">1</span> <span
                class="token punctuation">)</span><span class="token punctuation">;</span>
    <span class="token keyword">if</span> <span class="token punctuation">(</span> nfds <span
                class="token operator">==</span> <span class="token operator">-</span><span
                class="token number">1</span> <span class="token punctuation">)</span>
    <span class="token punctuation">{</span>
        <span class="token function">perror</span><span class="token punctuation">(</span> <span class="token string">"epoll_wait"</span> <span
                class="token punctuation">)</span><span class="token punctuation">;</span>
        <span class="token function">exit</span><span class="token punctuation">(</span> EXIT_FAILURE <span
                class="token punctuation">)</span><span class="token punctuation">;</span>
    <span class="token punctuation">}</span>

    <span class="token keyword">for</span> <span class="token punctuation">(</span> n <span
                class="token operator">=</span> <span class="token number">0</span><span
                class="token punctuation">;</span> n <span class="token operator">&lt;</span> nfds<span
                class="token punctuation">;</span> <span class="token operator">++</span>n <span
                class="token punctuation">)</span>
    <span class="token punctuation">{</span>
        <span class="token keyword">if</span> <span class="token punctuation">(</span> events<span
                class="token punctuation">[</span>n<span class="token punctuation">]</span><span
                class="token punctuation">.</span>data<span class="token punctuation">.</span>fd <span
                class="token operator">==</span> listen_sock <span class="token punctuation">)</span>
        <span class="token punctuation">{</span>
            conn_sock <span class="token operator">=</span> <span class="token function">accept</span><span
                class="token punctuation">(</span> listen_sock<span class="token punctuation">,</span>
                        <span class="token punctuation">(</span><span class="token keyword">struct</span> <span
                class="token class-name">sockaddr</span> <span class="token operator">*</span><span
                class="token punctuation">)</span> <span class="token operator">&amp;</span>local<span
                class="token punctuation">,</span> <span class="token operator">&amp;</span>addrlen <span
                class="token punctuation">)</span><span class="token punctuation">;</span>
            <span class="token keyword">if</span> <span class="token punctuation">(</span> conn_sock <span
                class="token operator">==</span> <span class="token operator">-</span><span
                class="token number">1</span> <span class="token punctuation">)</span>
            <span class="token punctuation">{</span>
                <span class="token function">perror</span><span class="token punctuation">(</span> <span
                class="token string">"accept"</span> <span class="token punctuation">)</span><span
                class="token punctuation">;</span>
                <span class="token function">exit</span><span class="token punctuation">(</span> EXIT_FAILURE <span
                class="token punctuation">)</span><span class="token punctuation">;</span>
            <span class="token punctuation">}</span>
            <span class="token function">setnonblocking</span><span class="token punctuation">(</span> conn_sock <span
                class="token punctuation">)</span><span class="token punctuation">;</span>
            ev<span class="token punctuation">.</span>events   <span class="token operator">=</span> EPOLLIN <span
                class="token operator">|</span> EPOLLET<span class="token punctuation">;</span>
            ev<span class="token punctuation">.</span>data<span class="token punctuation">.</span>fd  <span
                class="token operator">=</span> conn_sock<span class="token punctuation">;</span>
            <span class="token keyword">if</span> <span class="token punctuation">(</span> <span class="token function">epoll_ctl</span><span
                class="token punctuation">(</span> epollfd<span
                class="token punctuation">,</span> EPOLL_CTL_ADD<span
                class="token punctuation">,</span> conn_sock<span class="token punctuation">,</span>
                    <span class="token operator">&amp;</span>ev <span class="token punctuation">)</span> <span
                class="token operator">==</span> <span class="token operator">-</span><span
                class="token number">1</span> <span class="token punctuation">)</span>
            <span class="token punctuation">{</span>
                <span class="token function">perror</span><span class="token punctuation">(</span> <span
                class="token string">"epoll_ctl: conn_sock"</span> <span class="token punctuation">)</span><span
                class="token punctuation">;</span>
                <span class="token function">exit</span><span class="token punctuation">(</span> EXIT_FAILURE <span
                class="token punctuation">)</span><span class="token punctuation">;</span>
            <span class="token punctuation">}</span>
        <span class="token punctuation">}</span> <span class="token keyword">else</span> <span
                class="token punctuation">{</span>
            <span class="token function">do_use_fd</span><span class="token punctuation">(</span> events<span
                class="token punctuation">[</span>n<span class="token punctuation">]</span><span
                class="token punctuation">.</span>data<span class="token punctuation">.</span>fd <span
                class="token punctuation">)</span><span class="token punctuation">;</span>
        <span class="token punctuation">}</span>
    <span class="token punctuation">}</span>
<span class="token punctuation">}</span>
<span aria-hidden="true"
      class="line-numbers-rows"><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span></span></code></pre>
</div>
<h2>4.完整可运行的DEMO</h2>
<div class="_2Uzcx_">
    <button class="VJbwyy" type="button" aria-label="复制代码"><i aria-label="icon: copy" class="anticon anticon-copy">
        <svg viewBox="64 64 896 896" focusable="false" class="" data-icon="copy" width="1em" height="1em"
             fill="currentColor" aria-hidden="true">
            <path d="M832 64H296c-4.4 0-8 3.6-8 8v56c0 4.4 3.6 8 8 8h496v688c0 4.4 3.6 8 8 8h56c4.4 0 8-3.6 8-8V96c0-17.7-14.3-32-32-32zM704 192H192c-17.7 0-32 14.3-32 32v530.7c0 8.5 3.4 16.6 9.4 22.6l173.3 173.3c2.2 2.2 4.7 4 7.4 5.5v1.9h4.2c3.5 1.3 7.2 2 11 2H704c17.7 0 32-14.3 32-32V224c0-17.7-14.3-32-32-32zM350 856.2L263.9 770H350v86.2zM664 888H414V746c0-22.1-17.9-40-40-40H232V264h432v624z"></path>
        </svg>
    </i></button>
    <pre class="line-numbers  language-cpp"><code class="cpp  language-cpp"><span
            class="token macro property">#<span class="token directive keyword">include</span> <span
            class="token string">&lt;stdio.h&gt;</span></span>
<span class="token macro property">#<span class="token directive keyword">include</span> <span class="token string">&lt;sys/epoll.h&gt;</span></span>
<span class="token macro property">#<span class="token directive keyword">include</span> <span class="token string">&lt;sys/socket.h&gt;</span></span>
<span class="token macro property">#<span class="token directive keyword">include</span> <span class="token string">&lt;sys/types.h&gt;</span></span>
<span class="token macro property">#<span class="token directive keyword">include</span> <span class="token string">&lt;netinet/in.h&gt;</span></span>
<span class="token macro property">#<span class="token directive keyword">include</span> <span class="token string">&lt;arpa/inet.h&gt;</span></span>
<span class="token macro property">#<span class="token directive keyword">include</span> <span class="token string">&lt;fcntl.h&gt;</span></span>
<span class="token macro property">#<span class="token directive keyword">include</span> <span class="token string">&lt;unistd.h&gt;</span></span>
<span class="token macro property">#<span class="token directive keyword">include</span> <span class="token string">&lt;netdb.h&gt;</span></span>
<span class="token macro property">#<span class="token directive keyword">include</span> <span class="token string">&lt;errno.h&gt;</span></span>

<span class="token macro property">#<span class="token directive keyword">define</span> MAX_EVENT 20</span>
<span class="token macro property">#<span class="token directive keyword">define</span> READ_BUF_LEN 256</span>

<span class="token comment">/**
 * 设置 file describe 为非阻塞模式
 * @param fd 文件描述
 * @return 返回0成功，返回-1失败
 */</span>
<span class="token keyword">static</span> <span class="token keyword">int</span> make_socket_non_blocking <span
                class="token punctuation">(</span><span class="token keyword">int</span> fd<span
                class="token punctuation">)</span> <span class="token punctuation">{</span>
    <span class="token keyword">int</span> flags<span class="token punctuation">,</span> s<span
                class="token punctuation">;</span>
    <span class="token comment">// 获取当前flag</span>
    flags <span class="token operator">=</span> <span class="token function">fcntl</span><span
                class="token punctuation">(</span>fd<span class="token punctuation">,</span> F_GETFL<span
                class="token punctuation">,</span> <span class="token number">0</span><span
                class="token punctuation">)</span><span class="token punctuation">;</span>
    <span class="token keyword">if</span> <span class="token punctuation">(</span><span
                class="token operator">-</span><span class="token number">1</span> <span
                class="token operator">==</span> flags<span class="token punctuation">)</span> <span
                class="token punctuation">{</span>
        <span class="token function">perror</span><span class="token punctuation">(</span><span class="token string">"Get fd status"</span><span
                class="token punctuation">)</span><span class="token punctuation">;</span>
        <span class="token keyword">return</span> <span class="token operator">-</span><span
                class="token number">1</span><span class="token punctuation">;</span>
    <span class="token punctuation">}</span>

    flags <span class="token operator">|=</span> O_NONBLOCK<span class="token punctuation">;</span>

    <span class="token comment">// 设置flag</span>
    s <span class="token operator">=</span> <span class="token function">fcntl</span><span
                class="token punctuation">(</span>fd<span class="token punctuation">,</span> F_SETFL<span
                class="token punctuation">,</span> flags<span class="token punctuation">)</span><span
                class="token punctuation">;</span>
    <span class="token keyword">if</span> <span class="token punctuation">(</span><span
                class="token operator">-</span><span class="token number">1</span> <span
                class="token operator">==</span> s<span class="token punctuation">)</span> <span
                class="token punctuation">{</span>
        <span class="token function">perror</span><span class="token punctuation">(</span><span class="token string">"Set fd status"</span><span
                class="token punctuation">)</span><span class="token punctuation">;</span>
        <span class="token keyword">return</span> <span class="token operator">-</span><span
                class="token number">1</span><span class="token punctuation">;</span>
    <span class="token punctuation">}</span>
    <span class="token keyword">return</span> <span class="token number">0</span><span
                class="token punctuation">;</span>
<span class="token punctuation">}</span>

<span class="token keyword">int</span> <span class="token function">main</span><span
                class="token punctuation">(</span><span class="token punctuation">)</span> <span
                class="token punctuation">{</span>
    <span class="token comment">// epoll 实例 file describe</span>
    <span class="token keyword">int</span> epfd <span class="token operator">=</span> <span
                class="token number">0</span><span class="token punctuation">;</span>
    <span class="token keyword">int</span> listenfd <span class="token operator">=</span> <span
                class="token number">0</span><span class="token punctuation">;</span>
    <span class="token keyword">int</span> result <span class="token operator">=</span> <span
                class="token number">0</span><span class="token punctuation">;</span>
    <span class="token keyword">struct</span> <span class="token class-name">epoll_event</span> ev<span
                class="token punctuation">,</span> event<span class="token punctuation">[</span>MAX_EVENT<span
                class="token punctuation">]</span><span class="token punctuation">;</span>
    <span class="token comment">// 绑定的地址</span>
    <span class="token keyword">const</span> <span class="token keyword">char</span> <span
                class="token operator">*</span> <span class="token keyword">const</span> local_addr <span
                class="token operator">=</span> <span class="token string">"192.168.0.45"</span><span
                class="token punctuation">;</span>
    <span class="token keyword">struct</span> <span class="token class-name">sockaddr_in</span> server_addr <span
                class="token operator">=</span> <span class="token punctuation">{</span> <span
                class="token number">0</span> <span
                class="token punctuation">}</span><span class="token punctuation">;</span>

    listenfd <span class="token operator">=</span> <span class="token function">socket</span><span
                class="token punctuation">(</span>AF_INET<span class="token punctuation">,</span> SOCK_STREAM<span
                class="token punctuation">,</span> <span class="token number">0</span><span
                class="token punctuation">)</span><span class="token punctuation">;</span>
    <span class="token keyword">if</span> <span class="token punctuation">(</span><span
                class="token operator">-</span><span class="token number">1</span> <span
                class="token operator">==</span> listenfd<span class="token punctuation">)</span> <span
                class="token punctuation">{</span>
        <span class="token function">perror</span><span class="token punctuation">(</span><span class="token string">"Open listen socket"</span><span
                class="token punctuation">)</span><span class="token punctuation">;</span>
        <span class="token keyword">return</span> <span class="token operator">-</span><span
                class="token number">1</span><span class="token punctuation">;</span>
    <span class="token punctuation">}</span>
    <span class="token comment">/* Enable address reuse */</span>
    <span class="token keyword">int</span> on <span class="token operator">=</span> <span
                class="token number">1</span><span class="token punctuation">;</span>
    <span class="token comment">// 打开 socket 端口复用, 防止测试的时候出现 Address already in use</span>
    result <span class="token operator">=</span> <span class="token function">setsockopt</span><span
                class="token punctuation">(</span> listenfd<span class="token punctuation">,</span> SOL_SOCKET<span
                class="token punctuation">,</span> SO_REUSEADDR<span class="token punctuation">,</span> <span
                class="token operator">&amp;</span>on<span class="token punctuation">,</span> <span
                class="token keyword">sizeof</span><span class="token punctuation">(</span>on<span
                class="token punctuation">)</span> <span class="token punctuation">)</span><span
                class="token punctuation">;</span>
    <span class="token keyword">if</span> <span class="token punctuation">(</span><span
                class="token operator">-</span><span class="token number">1</span> <span
                class="token operator">==</span> result<span class="token punctuation">)</span> <span
                class="token punctuation">{</span>
        perror <span class="token punctuation">(</span><span class="token string">"Set socket"</span><span
                class="token punctuation">)</span><span class="token punctuation">;</span>
        <span class="token keyword">return</span> <span class="token number">0</span><span
                class="token punctuation">;</span>
    <span class="token punctuation">}</span>

    server_addr<span class="token punctuation">.</span>sin_family <span class="token operator">=</span> AF_INET<span
                class="token punctuation">;</span>
    inet_aton <span class="token punctuation">(</span>local_addr<span class="token punctuation">,</span> <span
                class="token operator">&amp;</span><span class="token punctuation">(</span>server_addr<span
                class="token punctuation">.</span>sin_addr<span class="token punctuation">)</span><span
                class="token punctuation">)</span><span class="token punctuation">;</span>
    server_addr<span class="token punctuation">.</span>sin_port <span class="token operator">=</span> <span
                class="token function">htons</span><span class="token punctuation">(</span><span
                class="token number">8080</span><span class="token punctuation">)</span><span
                class="token punctuation">;</span>
    result <span class="token operator">=</span> <span class="token function">bind</span><span
                class="token punctuation">(</span>listenfd<span class="token punctuation">,</span> <span
                class="token punctuation">(</span><span class="token keyword">const</span> <span
                class="token keyword">struct</span> <span class="token class-name">sockaddr</span> <span
                class="token operator">*</span><span class="token punctuation">)</span><span class="token operator">&amp;</span>server_addr<span
                class="token punctuation">,</span> <span class="token keyword">sizeof</span> <span
                class="token punctuation">(</span>server_addr<span class="token punctuation">)</span><span
                class="token punctuation">)</span><span class="token punctuation">;</span>
    <span class="token keyword">if</span> <span class="token punctuation">(</span><span
                class="token operator">-</span><span class="token number">1</span> <span
                class="token operator">==</span> result<span class="token punctuation">)</span> <span
                class="token punctuation">{</span>
        <span class="token function">perror</span><span class="token punctuation">(</span><span class="token string">"Bind port"</span><span
                class="token punctuation">)</span><span class="token punctuation">;</span>
        <span class="token keyword">return</span> <span class="token number">0</span><span
                class="token punctuation">;</span>
    <span class="token punctuation">}</span>
    result <span class="token operator">=</span> <span class="token function">make_socket_non_blocking</span><span
                class="token punctuation">(</span>listenfd<span class="token punctuation">)</span><span
                class="token punctuation">;</span>
    <span class="token keyword">if</span> <span class="token punctuation">(</span><span
                class="token operator">-</span><span class="token number">1</span> <span
                class="token operator">==</span> result<span class="token punctuation">)</span> <span
                class="token punctuation">{</span>
        <span class="token keyword">return</span> <span class="token number">0</span><span
                class="token punctuation">;</span>
    <span class="token punctuation">}</span>

    result <span class="token operator">=</span> <span class="token function">listen</span><span
                class="token punctuation">(</span>listenfd<span class="token punctuation">,</span> <span
                class="token number">200</span><span class="token punctuation">)</span><span
                class="token punctuation">;</span>
    <span class="token keyword">if</span> <span class="token punctuation">(</span><span
                class="token operator">-</span><span class="token number">1</span> <span
                class="token operator">==</span> result<span class="token punctuation">)</span> <span
                class="token punctuation">{</span>
        <span class="token function">perror</span><span class="token punctuation">(</span><span class="token string">"Start listen"</span><span
                class="token punctuation">)</span><span class="token punctuation">;</span>
        <span class="token keyword">return</span> <span class="token number">0</span><span
                class="token punctuation">;</span>
    <span class="token punctuation">}</span>

    <span class="token comment">// 创建epoll实例</span>
    epfd <span class="token operator">=</span> <span class="token function">epoll_create1</span><span
                class="token punctuation">(</span><span class="token number">0</span><span
                class="token punctuation">)</span><span class="token punctuation">;</span>
    <span class="token keyword">if</span> <span class="token punctuation">(</span><span
                class="token number">1</span> <span class="token operator">==</span> epfd<span
                class="token punctuation">)</span> <span class="token punctuation">{</span>
        <span class="token function">perror</span><span class="token punctuation">(</span><span class="token string">"Create epoll instance"</span><span
                class="token punctuation">)</span><span class="token punctuation">;</span>
        <span class="token keyword">return</span> <span class="token number">0</span><span
                class="token punctuation">;</span>
    <span class="token punctuation">}</span>

    ev<span class="token punctuation">.</span>data<span class="token punctuation">.</span>fd <span
                class="token operator">=</span> listenfd<span class="token punctuation">;</span>
    ev<span class="token punctuation">.</span>events <span class="token operator">=</span> EPOLLIN <span
                class="token operator">|</span> EPOLLET <span class="token comment">/* 边缘触发选项。 */</span><span
                class="token punctuation">;</span>
    <span class="token comment">// 设置epoll的事件</span>
    result <span class="token operator">=</span> <span class="token function">epoll_ctl</span><span
                class="token punctuation">(</span>epfd<span class="token punctuation">,</span> EPOLL_CTL_ADD<span
                class="token punctuation">,</span> listenfd<span class="token punctuation">,</span> <span
                class="token operator">&amp;</span>ev<span class="token punctuation">)</span><span
                class="token punctuation">;</span>

    <span class="token keyword">if</span><span class="token punctuation">(</span><span
                class="token operator">-</span><span class="token number">1</span> <span
                class="token operator">==</span> result<span class="token punctuation">)</span> <span
                class="token punctuation">{</span>
        <span class="token function">perror</span><span class="token punctuation">(</span><span class="token string">"Set epoll_ctl"</span><span
                class="token punctuation">)</span><span class="token punctuation">;</span>
        <span class="token keyword">return</span> <span class="token number">0</span><span
                class="token punctuation">;</span>
    <span class="token punctuation">}</span>

    <span class="token keyword">for</span> <span class="token punctuation">(</span> <span
                class="token punctuation">;</span> <span class="token punctuation">;</span> <span
                class="token punctuation">)</span> <span class="token punctuation">{</span>
        <span class="token keyword">int</span> wait_count<span class="token punctuation">;</span>
        <span class="token comment">// 等待事件</span>
        wait_count <span class="token operator">=</span> <span class="token function">epoll_wait</span><span
                class="token punctuation">(</span>epfd<span class="token punctuation">,</span> event<span
                class="token punctuation">,</span> MAX_EVENT<span class="token punctuation">,</span> <span
                class="token operator">-</span><span class="token number">1</span><span
                class="token punctuation">)</span><span class="token punctuation">;</span>

        <span class="token keyword">for</span> <span class="token punctuation">(</span><span
                class="token keyword">int</span> i <span class="token operator">=</span> <span
                class="token number">0</span> <span
                class="token punctuation">;</span> i <span class="token operator">&lt;</span> wait_count<span
                class="token punctuation">;</span> i<span class="token operator">++</span><span
                class="token punctuation">)</span> <span class="token punctuation">{</span>
            <span class="token keyword">uint32_t</span> events <span class="token operator">=</span> event<span
                class="token punctuation">[</span>i<span class="token punctuation">]</span><span
                class="token punctuation">.</span>events<span class="token punctuation">;</span>
            <span class="token comment">// IP地址缓存</span>
            <span class="token keyword">char</span> host_buf<span class="token punctuation">[</span>NI_MAXHOST<span
                class="token punctuation">]</span><span class="token punctuation">;</span>
            <span class="token comment">// PORT缓存</span>
            <span class="token keyword">char</span> port_buf<span class="token punctuation">[</span>NI_MAXSERV<span
                class="token punctuation">]</span><span class="token punctuation">;</span>

            <span class="token keyword">int</span> __result<span class="token punctuation">;</span>
            <span class="token comment">// 判断epoll是否发生错误</span>
            <span class="token keyword">if</span> <span class="token punctuation">(</span> events <span
                class="token operator">&amp;</span> EPOLLERR <span class="token operator">||</span> events <span
                class="token operator">&amp;</span> EPOLLHUP <span class="token operator">||</span> <span
                class="token punctuation">(</span><span class="token operator">!</span> events <span
                class="token operator">&amp;</span> EPOLLIN<span class="token punctuation">)</span><span
                class="token punctuation">)</span> <span class="token punctuation">{</span>
                <span class="token function">printf</span><span class="token punctuation">(</span><span
                class="token string">"Epoll has error\n"</span><span class="token punctuation">)</span><span
                class="token punctuation">;</span>
                close <span class="token punctuation">(</span>event<span class="token punctuation">[</span>i<span
                class="token punctuation">]</span><span class="token punctuation">.</span>data<span
                class="token punctuation">.</span>fd<span class="token punctuation">)</span><span
                class="token punctuation">;</span>
                <span class="token keyword">continue</span><span class="token punctuation">;</span>
            <span class="token punctuation">}</span> <span class="token keyword">else</span> <span
                class="token keyword">if</span> <span class="token punctuation">(</span>listenfd <span
                class="token operator">==</span> event<span class="token punctuation">[</span>i<span
                class="token punctuation">]</span><span class="token punctuation">.</span>data<span
                class="token punctuation">.</span>fd<span class="token punctuation">)</span> <span
                class="token punctuation">{</span>
                <span class="token comment">// listen的 file describe 事件触发， accpet事件</span>

                <span class="token keyword">for</span> <span class="token punctuation">(</span> <span
                class="token punctuation">;</span> <span class="token punctuation">;</span> <span
                class="token punctuation">)</span> <span class="token punctuation">{</span> <span
                class="token comment">// 由于采用了边缘触发模式，这里需要使用循环</span>
                    <span class="token keyword">struct</span> <span
                class="token class-name">sockaddr</span> in_addr <span class="token operator">=</span> <span
                class="token punctuation">{</span> <span class="token number">0</span> <span
                class="token punctuation">}</span><span class="token punctuation">;</span>
                    socklen_t in_addr_len <span class="token operator">=</span> <span
                class="token keyword">sizeof</span> <span class="token punctuation">(</span>in_addr<span
                class="token punctuation">)</span><span class="token punctuation">;</span>
                    <span class="token keyword">int</span> accp_fd <span class="token operator">=</span> <span
                class="token function">accept</span><span class="token punctuation">(</span>listenfd<span
                class="token punctuation">,</span> <span class="token operator">&amp;</span>in_addr<span
                class="token punctuation">,</span> <span class="token operator">&amp;</span>in_addr_len<span
                class="token punctuation">)</span><span class="token punctuation">;</span>
                    <span class="token keyword">if</span> <span class="token punctuation">(</span><span
                class="token operator">-</span><span class="token number">1</span> <span
                class="token operator">==</span> accp_fd<span class="token punctuation">)</span> <span
                class="token punctuation">{</span>
                        <span class="token function">perror</span><span class="token punctuation">(</span><span
                class="token string">"Accept"</span><span class="token punctuation">)</span><span
                class="token punctuation">;</span>
                        <span class="token keyword">break</span><span class="token punctuation">;</span>
                    <span class="token punctuation">}</span>
                    __result <span class="token operator">=</span> <span class="token function">getnameinfo</span><span
                class="token punctuation">(</span><span class="token operator">&amp;</span>in_addr<span
                class="token punctuation">,</span> <span class="token keyword">sizeof</span> <span
                class="token punctuation">(</span>in_addr<span class="token punctuation">)</span><span
                class="token punctuation">,</span>
                                           host_buf<span class="token punctuation">,</span> <span class="token keyword">sizeof</span> <span
                class="token punctuation">(</span>host_buf<span class="token punctuation">)</span> <span
                class="token operator">/</span> <span class="token keyword">sizeof</span> <span
                class="token punctuation">(</span>host_buf<span class="token punctuation">[</span><span
                class="token number">0</span><span class="token punctuation">]</span><span
                class="token punctuation">)</span><span class="token punctuation">,</span>
                                           port_buf<span class="token punctuation">,</span> <span class="token keyword">sizeof</span> <span
                class="token punctuation">(</span>port_buf<span class="token punctuation">)</span> <span
                class="token operator">/</span> <span class="token keyword">sizeof</span> <span
                class="token punctuation">(</span>port_buf<span class="token punctuation">[</span><span
                class="token number">0</span><span class="token punctuation">]</span><span
                class="token punctuation">)</span><span class="token punctuation">,</span>
                                           NI_NUMERICHOST <span class="token operator">|</span> NI_NUMERICSERV<span
                class="token punctuation">)</span><span class="token punctuation">;</span>

                    <span class="token keyword">if</span> <span class="token punctuation">(</span><span
                class="token operator">!</span> __result<span class="token punctuation">)</span> <span
                class="token punctuation">{</span>
                        <span class="token function">printf</span><span class="token punctuation">(</span><span
                class="token string">"New connection: host = %s, port = %s\n"</span><span
                class="token punctuation">,</span> host_buf<span
                class="token punctuation">,</span> port_buf<span class="token punctuation">)</span><span
                class="token punctuation">;</span>
                    <span class="token punctuation">}</span>

                    __result <span class="token operator">=</span> <span
                class="token function">make_socket_non_blocking</span><span
                class="token punctuation">(</span>accp_fd<span
                class="token punctuation">)</span><span class="token punctuation">;</span>
                    <span class="token keyword">if</span> <span class="token punctuation">(</span><span
                class="token operator">-</span><span class="token number">1</span> <span
                class="token operator">==</span> __result<span class="token punctuation">)</span> <span
                class="token punctuation">{</span>
                        <span class="token keyword">return</span> <span class="token number">0</span><span
                class="token punctuation">;</span>
                    <span class="token punctuation">}</span>

                    ev<span class="token punctuation">.</span>data<span class="token punctuation">.</span>fd <span
                class="token operator">=</span> accp_fd<span class="token punctuation">;</span>
                    ev<span class="token punctuation">.</span>events <span class="token operator">=</span> EPOLLIN <span
                class="token operator">|</span> EPOLLET<span class="token punctuation">;</span>
                    <span class="token comment">// 为新accept的 file describe 设置epoll事件</span>
                    __result <span class="token operator">=</span> <span class="token function">epoll_ctl</span><span
                class="token punctuation">(</span>epfd<span class="token punctuation">,</span> EPOLL_CTL_ADD<span
                class="token punctuation">,</span> accp_fd<span class="token punctuation">,</span> <span
                class="token operator">&amp;</span>ev<span class="token punctuation">)</span><span
                class="token punctuation">;</span>

                    <span class="token keyword">if</span> <span class="token punctuation">(</span><span
                class="token operator">-</span><span class="token number">1</span> <span
                class="token operator">==</span> __result<span class="token punctuation">)</span> <span
                class="token punctuation">{</span>
                        <span class="token function">perror</span><span class="token punctuation">(</span><span
                class="token string">"epoll_ctl"</span><span class="token punctuation">)</span><span
                class="token punctuation">;</span>
                        <span class="token keyword">return</span> <span class="token number">0</span><span
                class="token punctuation">;</span>
                    <span class="token punctuation">}</span>
                <span class="token punctuation">}</span>
                <span class="token keyword">continue</span><span class="token punctuation">;</span>
            <span class="token punctuation">}</span> <span class="token keyword">else</span> <span
                class="token punctuation">{</span>
                <span class="token comment">// 其余事件为 file describe 可以读取</span>
                <span class="token keyword">int</span> done <span class="token operator">=</span> <span
                class="token number">0</span><span class="token punctuation">;</span>
                <span class="token comment">// 因为采用边缘触发，所以这里需要使用循环。如果不使用循环，程序并不能完全读取到缓存区里面的数据。</span>
                <span class="token keyword">for</span> <span class="token punctuation">(</span> <span
                class="token punctuation">;</span> <span class="token punctuation">;</span><span
                class="token punctuation">)</span> <span class="token punctuation">{</span>
                    ssize_t result_len <span class="token operator">=</span> <span class="token number">0</span><span
                class="token punctuation">;</span>
                    <span class="token keyword">char</span> buf<span class="token punctuation">[</span>READ_BUF_LEN<span
                class="token punctuation">]</span> <span class="token operator">=</span> <span
                class="token punctuation">{</span> <span class="token number">0</span> <span
                class="token punctuation">}</span><span class="token punctuation">;</span>

                    result_len <span class="token operator">=</span> <span class="token function">read</span><span
                class="token punctuation">(</span>event<span class="token punctuation">[</span>i<span
                class="token punctuation">]</span><span class="token punctuation">.</span>data<span
                class="token punctuation">.</span>fd<span class="token punctuation">,</span> buf<span
                class="token punctuation">,</span> <span class="token keyword">sizeof</span> <span
                class="token punctuation">(</span>buf<span class="token punctuation">)</span> <span
                class="token operator">/</span> <span class="token keyword">sizeof</span> <span
                class="token punctuation">(</span>buf<span class="token punctuation">[</span><span
                class="token number">0</span><span class="token punctuation">]</span><span
                class="token punctuation">)</span><span class="token punctuation">)</span><span
                class="token punctuation">;</span>

                    <span class="token keyword">if</span> <span class="token punctuation">(</span><span
                class="token operator">-</span><span class="token number">1</span> <span
                class="token operator">==</span> result_len<span class="token punctuation">)</span> <span
                class="token punctuation">{</span>
                        <span class="token keyword">if</span> <span class="token punctuation">(</span>EAGAIN <span
                class="token operator">!=</span> errno<span class="token punctuation">)</span> <span
                class="token punctuation">{</span>
                            perror <span class="token punctuation">(</span><span class="token string">"Read data"</span><span
                class="token punctuation">)</span><span class="token punctuation">;</span>
                            done <span class="token operator">=</span> <span class="token number">1</span><span
                class="token punctuation">;</span>
                        <span class="token punctuation">}</span>
                        <span class="token keyword">break</span><span class="token punctuation">;</span>
                    <span class="token punctuation">}</span> <span class="token keyword">else</span> <span
                class="token keyword">if</span> <span class="token punctuation">(</span><span
                class="token operator">!</span> result_len<span class="token punctuation">)</span> <span
                class="token punctuation">{</span>
                        done <span class="token operator">=</span> <span class="token number">1</span><span
                class="token punctuation">;</span>
                        <span class="token keyword">break</span><span class="token punctuation">;</span>
                    <span class="token punctuation">}</span>

                    <span class="token function">write</span><span class="token punctuation">(</span>STDOUT_FILENO<span
                class="token punctuation">,</span> buf<span class="token punctuation">,</span> result_len<span
                class="token punctuation">)</span><span class="token punctuation">;</span>
                <span class="token punctuation">}</span>
                <span class="token keyword">if</span> <span class="token punctuation">(</span>done<span
                class="token punctuation">)</span> <span class="token punctuation">{</span>
                    <span class="token function">printf</span><span class="token punctuation">(</span><span
                class="token string">"Closed connection\n"</span><span class="token punctuation">)</span><span
                class="token punctuation">;</span>
                    close <span class="token punctuation">(</span>event<span class="token punctuation">[</span>i<span
                class="token punctuation">]</span><span class="token punctuation">.</span>data<span
                class="token punctuation">.</span>fd<span class="token punctuation">)</span><span
                class="token punctuation">;</span>
                <span class="token punctuation">}</span>
            <span class="token punctuation">}</span>
        <span class="token punctuation">}</span>

    <span class="token punctuation">}</span>
    close <span class="token punctuation">(</span>epfd<span class="token punctuation">)</span><span
                class="token punctuation">;</span>
    <span class="token keyword">return</span> <span class="token number">0</span><span
                class="token punctuation">;</span>
<span class="token punctuation">}</span>
</code></pre>
</div>
