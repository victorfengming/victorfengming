---
title: "2019 Python 面试 100 问"
cover: "/img/lynk/34.jpg"
date:       2019-12-05
subtitle: "全是干货分享"
tags:
	- Python
	- solution
	- interview
---





<meta itemprop="url" content="https://juejin.im/post/5cfd1d0d6fb9a07eaf2b844d">
<meta itemprop="headline" content="2019 Python 面试 100 问">
<meta itemprop="keywords" content="Python">
<meta itemprop="datePublished" content="2019-06-09T14:53:04.194Z">
<meta itemprop="image" content="https://b-gold-cdn.xitu.io/icon/icon-128.png">
<div itemprop="author" itemscope="itemscope" itemtype="http://schema.org/Person">
    <meta itemprop="name" content="zone">
    <meta itemprop="url" content="https://juejin.im/user/57b5caa1c4c971005f943975">
</div>
<div itemprop="publisher" itemscope="itemscope" itemtype="http://schema.org/Organization">
    <meta itemprop="name" content="掘金">
    <div itemprop="logo" itemscope="itemscope" itemtype="https://schema.org/ImageObject">
        <meta itemprop="url" content="https://b-gold-cdn.xitu.io/icon/icon-white-180.png">
        <meta itemprop="width" content="180">
        <meta itemprop="height" content="180">
    </div>
</div>
<div data-v-0526462d="" class="author-info-block"><a data-v-0526462d="" href="/user/57b5caa1c4c971005f943975"
                                                     target="_blank" rel="" class="avatar-link">
    <div data-v-10f5e1e2="" data-v-762a6aba="" data-v-0526462d=""
         data-src="https://user-gold-cdn.xitu.io/2016/11/29/87e4d156ebc6f2901cb96d320004af0e?imageView2/1/w/100/h/100/q/85/format/webp/interlace/1"
         class="lazy avatar avatar loaded"
         style="background-image: url(&quot;https://user-gold-cdn.xitu.io/2016/11/29/87e4d156ebc6f2901cb96d320004af0e?imageView2/1/w/100/h/100/q/85/format/webp/interlace/1&quot;);"></div>
</a>
    <div data-v-0526462d="" class="author-info-box"><a data-v-db47c888="" data-v-0526462d=""
                                                       href="/user/57b5caa1c4c971005f943975" target="_blank" rel=""
                                                       class="username username ellipsis">zone<a data-v-0ba9b815=""
                                                                                                 data-v-db47c888=""
                                                                                                 href="/book/5c90640c5188252d7941f5bb/section/5c9065385188252da6320022"
                                                                                                 target="_blank"
                                                                                                 rel=""
                                                                                                 class="rank"><img
            data-v-0ba9b815="" src="https://b-gold-cdn.xitu.io/v3/static/img/lv-2.f597b88.svg" alt="lv-2"></a></a>
        <div data-v-0526462d="" class="meta-box">
            <time data-v-0526462d="" datetime="2019-06-09T14:53:04.194Z"
                  title="Sun Jun 09 2019 22:53:04 GMT+0800 (中国标准时间)" class="time">2019年06月09日
            </time>
            <span data-v-0526462d="" class="views-count">阅读 3019</span><!----></div>
    </div>
    <button data-v-0bccdb0e="" data-v-0526462d="" class="follow-button follow">关注</button>
</div><!----><h1 data-v-0526462d="" class="article-title">2019 Python 面试 100 问</h1>
<div data-v-0526462d="" data-id="5cfd1d506fb9a07eaf2b844e" itemprop="articleBody" class="article-content"><h2
        class="heading" data-id="heading-0">以下内容出自小程序「编程面试题库」，本文首发于公众号「zone7」</h2>
    <p></p>
    <figure><img class="lazyload inited loaded"
                 data-src="https://user-gold-cdn.xitu.io/2019/6/9/16b3cb978e19876a?imageView2/0/w/1280/h/960/format/webp/ignore-error/1"
                 data-width="1087" data-height="455"
                 src="https://user-gold-cdn.xitu.io/2019/6/9/16b3cb978e19876a?imageView2/0/w/1280/h/960/format/webp/ignore-error/1">
        <figcaption></figcaption>
    </figure>
    <p></p>
    <h2 class="heading" data-id="heading-1">0 遇到过得反爬虫策略以及解决方法?</h2>
    <p>1.通过headers反爬虫
        2.基于用户行为的发爬虫：(同一IP短时间内访问的频率)
        3.动态网页反爬虫(通过ajax请求数据，或者通过JavaScript生成)
        4.对部分数据进行加密处理的(数据是乱码)</p>
    <h3 class="heading" data-id="heading-2">解决方法：</h3>
    <p>对于基本网页的抓取可以自定义headers,添加headers的数据
        使用多个代理ip进行抓取或者设置抓取的频率降低一些，
        动态网页的可以使用selenium + phantomjs 进行抓取
        对部分数据进行加密的，可以使用selenium进行截图，使用python自带的pytesseract库进行识别，但是比较慢最直接的方法是找到加密的方法进行逆向推理。</p>
    <h2 class="heading" data-id="heading-3">1 urllib 和 urllib2 的区别？</h2>
    <ul>
        <li>urllib
            和urllib2都是接受URL请求的相关模块，但是urllib2可以接受一个Request类的实例来设置URL请求的headers，urllib仅可以接受URL。urllib不可以伪装你的User-Agent字符串。
        </li>
        <li>urllib提供urlencode()方法用来GET查询字符串的产生，而urllib2没有。这是为何urllib常和urllib2一起使用的原因。</li>
    </ul>
    <h2 class="heading" data-id="heading-4">2 列举网络爬虫所用到的网络数据包，解析包？</h2>
    <ul>
        <li>网络数据包 urllib、urllib2、requests</li>
        <li>解析包 re、xpath、beautiful soup、lxml</li>
    </ul>
    <h2 class="heading" data-id="heading-5">3 简述一下爬虫的步骤？</h2>
    <ol>
        <li>确定需求；</li>
        <li>确定资源；</li>
        <li>通过url获取网站的返回数据；</li>
        <li>定位数据；</li>
        <li>存储数据。</li>
    </ol>
    <h2 class="heading" data-id="heading-6">4 遇到反爬机制怎么处理？</h2>
    <h2 class="heading" data-id="heading-7">反爬机制:</h2>
    <p>headers方向
        判断User-Agent、判断Referer、判断Cookie。
        将浏览器的headers信息全部添加进去
        注意：Accept-Encoding；gzip,deflate需要注释掉</p>
    <h2 class="heading" data-id="heading-8">5 常见的HTTP方法有哪些？</h2>
    <ul>
        <li>GET：请求指定的页面信息，返回实体主体；</li>
        <li>HEAD:类似于get请求，只不过返回的响应中没有具体的内容，用于捕获报头；</li>
        <li>POST：向指定资源提交数据进行处理请求(比如表单提交或者上传文件)，。数据被包含在请求体中。</li>
        <li>PUT:从客户端向服务端传送数据取代指定的文档的内容；</li>
        <li>DELETE：请求删除指定的页面；</li>
        <li>CONNNECT：HTTP1.1协议中预留给能够将连接方式改为管道方式的代理服务器；</li>
        <li>OPTIONS:允许客户端查看服务器的性能；
            TRACE：回显服务器的请求，主要用于测试或者诊断。
        </li>
    </ul>
    <h2 class="heading" data-id="heading-9">6 说一说redis-scrapy中redis的作用?</h2>
    <p>它是将scrapy框架中Scheduler替换为redis数据库，实现队列管理共享。</p>
    <h3 class="heading" data-id="heading-10">优点：</h3>
    <ol>
        <li>可以充分利用多台机器的带宽；</li>
        <li>可以充分利用多台机器的IP地址。</li>
    </ol>
    <h2 class="heading" data-id="heading-11">7 遇到的反爬虫策略以及解决方法?</h2>
    <ol>
        <li>通过headers反爬虫：自定义headers，添加网页中的headers数据。</li>
        <li>基于用户行为的反爬虫(封IP)：可以使用多个代理IP爬取或者将爬取的频率降低。</li>
        <li>动态网页反爬虫(JS或者Ajax请求数据)：动态网页可以使用 selenium + phantomjs 抓取。</li>
        <li>对部分数据加密处理(数据乱码):找到加密方法进行逆向推理。</li>
    </ol>
    <h2 class="heading" data-id="heading-12">8 如果让你来防范网站爬虫，你应该怎么来提高爬取的难度 ？</h2>
    <ol>
        <li>判断headers的User-Agent；</li>
        <li>检测同一个IP的访问频率；</li>
        <li>数据通过Ajax获取；</li>
        <li>爬取行为是对页面的源文件爬取，如果要爬取静态网页的html代码，可以使用jquery去模仿写html。</li>
    </ol>
    <h2 class="heading" data-id="heading-13">9 scrapy分为几个组成部分？分别有什么作用？</h2>
    <p>分为5个部分；Spiders(爬虫类)，Scrapy Engine(引擎),Scheduler(调度器),Downloader(下载器),Item Pipeline(处理管道)。</p>
    <ul>
        <li>Spiders:开发者自定义的一个类，用来解析网页并抓取指定url返回的内容。</li>
        <li>Scrapy Engine:控制整个系统的数据处理流程，并进行事务处理的触发。</li>
        <li>Scheduler：接收Engine发出的requests，并将这些requests放入到处理列队中，以便之后engine需要时再提供。</li>
        <li>Download：抓取网页信息提供给engine，进而转发至Spiders。</li>
        <li>Item Pipeline:负责处理Spiders类提取之后的数据。
            比如清理HTML数据、验证爬取的数据(检查item包含某些字段)、查重(并丢弃)、将爬取结果保存到数据库中
        </li>
    </ul>
    <h2 class="heading" data-id="heading-14">10 简述一下scrapy的基本流程?</h2>
    <p></p>
    <figure><img alt="image" class="lazyload inited loaded"
                 data-src="https://user-gold-cdn.xitu.io/2019/6/9/16b3cb978e4c62a1?imageView2/0/w/1280/h/960/format/webp/ignore-error/1"
                 data-width="800" data-height="537"
                 src="https://user-gold-cdn.xitu.io/2019/6/9/16b3cb978e4c62a1?imageView2/0/w/1280/h/960/format/webp/ignore-error/1">
        <figcaption></figcaption>
    </figure>
    <p></p>
    <h2 class="heading" data-id="heading-15">scrapy分为9个步骤：</h2>
    <ol>
        <li>Spiders需要初始的start_url或则函数stsrt_requests,会在内部生成Requests给Engine；</li>
        <li>Engine将requests发送给Scheduler;</li>
        <li>Engine从Scheduler那获取requests,交给Download下载；</li>
        <li>在交给Dowmload过程中会经过Downloader Middlewares(经过process_request函数)；</li>
        <li>Dowmloader下载页面后生成一个response，这个response会传给Engine，这个过程中又经过了Downloader
            Middlerwares(经过process_request函数)，在传送中出错的话经过process_exception函数；
        </li>
        <li>Engine将从Downloader那传送过来的response发送给Spiders处理，这个过程经过Spiders Middlerwares(经过process_spider_input函数)；</li>
        <li>Spiders处理这个response，返回Requests或者Item两个类型，传给Engine，这个过程又经过Spiders
            Middlewares(经过porcess_spider_output函数)；
        </li>
        <li>Engine接收返回的信息，如果使Item，将它传给Items Pipeline中；如果是Requests,将它传给Scheduler，继续爬虫；</li>
        <li>重复第三步，直至没有任何需要爬取的数据</li>
    </ol>
    <h2 class="heading" data-id="heading-16">11 python3.5语言中enumerate的意思是</h2>
    <p>对于一个可迭代的（iterable）/可遍历的对象（如列表、字符串），enumerate将其组成一个索引序列，利用它可以同时获得索引和值
        enumerate多用于在for循环中得到计数</p>
    <h2 class="heading" data-id="heading-17">12 你是否了解谷歌的无头浏览器？</h2>
    <p>无头浏览器即headless browser，是一种没有界面的浏览器。既然是浏览器那么浏览器该有的东西它都应该有，只是看不到界面而已。</p>
    <p>Python中selenium模块中的PhantomJS即为无界面浏览器（无头浏览器）:是基于QtWebkit的无头浏览器。</p>
    <h2 class="heading" data-id="heading-18">13 scrapy和scrapy-redis的区别？</h2>
    <p>scrapy是一个爬虫通用框架，但不支持分布式，scrapy-redis是为了更方便的实现scrapy分布式爬虫，而提供了一些以redis为基础的组件</p>
    <h2 class="heading" data-id="heading-19">为什么会选择redis数据库？</h2>
    <p>因为redis支持主从同步，而且数据都是缓存在内存中，所以基于redis的分布式爬虫，对请求和数据的高频读取效率非常高</p>
    <h2 class="heading" data-id="heading-20">什么是主从同步？</h2>
    <p>
        在Redis中，用户可以通过执行SLAVEOF命令或者设置slaveof选项，让一个服务器去复制（replicate）另一个服务器，我们称呼被复制的服务器为主服务器（master），而对主服务器进行复制的服务器则被称为从服务器（slave），当客户端向从服务器发送SLAVEOF命令，要求从服务器复制主服务器时，从服务器首先需要执行同步操作，也即是，将从服务器的数据库状态更新至主服务器当前所处的数据库状态</p>
    <h2 class="heading" data-id="heading-21">14 scrapy的优缺点？为什么要选择scrapy框架？</h2>
    <h3 class="heading" data-id="heading-22">优点：</h3>
    <p>采取可读性更强的xpath代替正则&nbsp;强大的统计和log系统&nbsp;同时在不同的url上爬行&nbsp;支持shell方式，方便独立调试&nbsp;写middleware,方便写一些统一的过滤器&nbsp;通过管道的方式存入数据库</p>
    <h3 class="heading" data-id="heading-23">缺点：</h3>
    <p>基于python爬虫框架，扩展性比较差，基于twisted框架，运行中exception是不会干掉reactor，并且异步框架出错后是不会停掉其他任务的，数据出错后难以察觉</p>
    <h2 class="heading" data-id="heading-24">15 scrapy和requests的使用情况？</h2>
    <p>requests 是 polling 方式的，会被网络阻塞，不适合爬取大量数据</p>
    <p>scapy 底层是异步框架 twisted ，并发是最大优势</p>
    <h2 class="heading" data-id="heading-25">16 描述一下scrapy框架的运行机制？</h2>
    <p>
        从start_urls里面获取第一批url发送请求，请求由请求引擎给调度器入请求对列，获取完毕后，调度器将请求对列交给下载器去获取请求对应的响应资源，并将响应交给自己编写的解析方法做提取处理，如果提取出需要的数据，则交给管道处理，如果提取出url，则继续执行之前的步骤，直到多列里没有请求，程序结束。</p>
    <h2 class="heading" data-id="heading-26">17 写爬虫使用多进程好，还是用多线程好？</h2>
    <p>
        IO密集型代码(文件处理、网络爬虫等)，多线程能够有效提升效率(单线程下有IO操作会进行IO等待，造成不必要的时间浪费，而开启多线程能在线程A等待时，自动切换到线程B，可以不浪费CPU的资源，从而能提升程序执行效率)。在实际的数据采集过程中，既考虑网速和响应的问题，也需要考虑自身机器的硬件情况，来设置多进程或多线程</p>
    <h2 class="heading" data-id="heading-27">18 常见的反爬虫和应对方法？</h2>
    <ol>
        <li>基于用户行为，同一个ip段时间多次访问同一页面&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;利用代理ip，构建ip池</li>
        <li>请求头里的user-agent&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;构建user-agent池（操作系统、浏览器不同，模拟不同用户）</li>
        <li>动态加载（抓到的数据和浏览器显示的不一样），js渲染&nbsp;&nbsp;&nbsp;&nbsp;模拟ajax请求，返回json形式的数据</li>
        <li>selenium / webdriver 模拟浏览器加载</li>
        <li>对抓到的数据进行分析</li>
        <li>加密参数字段&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;会话跟踪【cookie】&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 防盗链设置【Referer</li>
    </ol>
    <h2 class="heading" data-id="heading-28">19 分布式爬虫主要解决什么问题？</h2>
    <p>面对海量待抓取网页，只有采用分布式架构，才有可能在较短时间内完成一轮抓取工作。</p>
    <p>它的开发效率是比较快而且简单的。</p>
    <h2 class="heading" data-id="heading-29">20 如何提高爬取效率？</h2>
    <p>爬虫下载慢主要原因是阻塞等待发往网站的请求和网站返回</p>
    <pre><code class="copyable">    1，采用异步与多线程，扩大电脑的cpu利用率；

    2，采用消息队列模式

    3，提高带宽
<span class="copy-code-btn">复制代码</span></code></pre>
    <h2 class="heading" data-id="heading-30">21 说说什么是爬虫协议？</h2>
    <p>Robots协议（也称为爬虫协议、爬虫规则、机器人协议等）也就是robots.txt，网站通过robots协议告诉搜索引擎哪些页面可以抓取，哪些页面不能抓取。</p>
    <p>Robots协议是网站国际互联网界通行的道德规范，其目的是保护网站数据和敏感信息、确保用户个人信息和隐私不被侵犯。因其不是命令，故需要搜索引擎自觉遵守。</p>
    <h2 class="heading" data-id="heading-31">22 如果对方网站反爬取，封IP了怎么办？</h2>
    <ol>
        <li>放慢抓取熟速度，减小对目标网站造成的压力，但是这样会减少单位时间内的数据抓取量</li>
        <li>使用代理IP（免费的可能不稳定，收费的可能不划算）</li>
    </ol>
    <h2 class="heading" data-id="heading-32">23 有一个jsonline格式的文件file</h2>
    <pre><code class="hljs python copyable" lang="python"><span class="hljs-function"><span
            class="hljs-keyword">def</span> <span class="hljs-title">get_lines</span><span
            class="hljs-params">()</span>:</span>
    <span class="hljs-keyword">with</span> open(<span class="hljs-string">'file.txt'</span>,<span class="hljs-string">'rb'</span>) <span
                class="hljs-keyword">as</span> f:
        <span class="hljs-keyword">return</span> f.readlines()

<span class="hljs-keyword">if</span> __name__ == <span class="hljs-string">'__main__'</span>:
    <span class="hljs-keyword">for</span> e <span class="hljs-keyword">in</span> get_lines():
        process(e) <span class="hljs-comment"># 处理每一行数据</span>
<span class="copy-code-btn">复制代码</span></code></pre>
    <p>现在要处理一个大小为10G的文件，但是内存只有4G，如果在只修改get_lines 函数而其他代码保持不变的情况下，应该如何实现？需要考虑的问题都有那些？</p>
    <pre><code class="hljs python copyable" lang="python"><span class="hljs-function"><span
            class="hljs-keyword">def</span> <span class="hljs-title">get_lines</span><span
            class="hljs-params">()</span>:</span>
    <span class="hljs-keyword">with</span> open(<span class="hljs-string">'file.txt'</span>,<span class="hljs-string">'rb'</span>) <span
                class="hljs-keyword">as</span> f:
        <span class="hljs-keyword">for</span> i <span class="hljs-keyword">in</span> f:
            <span class="hljs-keyword">yield</span> i
<span class="copy-code-btn">复制代码</span></code></pre>
    <p>Pandaaaa906提供的方法</p>
    <pre><code class="hljs python copyable" lang="python"><span class="hljs-keyword">from</span> mmap <span
            class="hljs-keyword">import</span> mmap


<span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">get_lines</span><span
        class="hljs-params">(fp)</span>:</span>
    <span class="hljs-keyword">with</span> open(fp,<span class="hljs-string">"r+"</span>) <span
                class="hljs-keyword">as</span> f:
        m = mmap(f.fileno(), <span class="hljs-number">0</span>)
        tmp = <span class="hljs-number">0</span>
        <span class="hljs-keyword">for</span> i, char <span class="hljs-keyword">in</span> enumerate(m):
            <span class="hljs-keyword">if</span> char==<span class="hljs-string">b"\n"</span>:
                <span class="hljs-keyword">yield</span> m[tmp:i+<span class="hljs-number">1</span>].decode()
                tmp = i+<span class="hljs-number">1</span>

<span class="hljs-keyword">if</span> __name__==<span class="hljs-string">"__main__"</span>:
    <span class="hljs-keyword">for</span> i <span class="hljs-keyword">in</span> get_lines(<span class="hljs-string">"fp_some_huge_file"</span>):
        print(i)
<span class="copy-code-btn">复制代码</span></code></pre>
    <p>要考虑的问题有：内存只有4G无法一次性读入10G文件，需要分批读入分批读入数据要记录每次读入数据的位置。分批每次读取数据的大小，太小会在读取操作花费过多时间。
        <a target="_blank"
           href="https://stackoverflow.com/questions/30294146/python-fastest-way-to-process-large-file"
           rel="nofollow noopener noreferrer">stackoverflow.com/questions/3…</a></p>
    <h2 class="heading" data-id="heading-33">24 补充缺失的代码</h2>
    <pre><code class="hljs python copyable" lang="python"><span class="hljs-function"><span
            class="hljs-keyword">def</span> <span class="hljs-title">print_directory_contents</span><span
            class="hljs-params">(sPath)</span>:</span>
<span class="hljs-string">"""
这个函数接收文件夹的名称作为输入参数
返回该文件夹中文件的路径
以及其包含文件夹中文件的路径
"""</span>
<span class="hljs-keyword">import</span> os
<span class="hljs-keyword">for</span> s_child <span class="hljs-keyword">in</span> os.listdir(s_path):
    s_child_path = os.path.join(s_path, s_child)
    <span class="hljs-keyword">if</span> os.path.isdir(s_child_path):
        print_directory_contents(s_child_path)
    <span class="hljs-keyword">else</span>:
        print(s_child_path)
<span class="copy-code-btn">复制代码</span></code></pre>
    <h2 class="heading" data-id="heading-34">25 输入日期， 判断这一天是这一年的第几天？</h2>
    <pre><code class="hljs python copyable" lang="python"><span class="hljs-keyword">import</span> datetime
<span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">dayofyear</span><span
        class="hljs-params">()</span>:</span>
    year = input(<span class="hljs-string">"请输入年份: "</span>)
    month = input(<span class="hljs-string">"请输入月份: "</span>)
    day = input(<span class="hljs-string">"请输入天: "</span>)
    date1 = datetime.date(year=int(year),month=int(month),day=int(day))
    date2 = datetime.date(year=int(year),month=<span class="hljs-number">1</span>,day=<span class="hljs-number">1</span>)
    <span class="hljs-keyword">return</span> (date1-date2).days+<span class="hljs-number">1</span>
<span class="copy-code-btn">复制代码</span></code></pre>
    <h2 class="heading" data-id="heading-35">26 打乱一个排好序的list对象alist？</h2>
    <pre><code class="hljs python copyable" lang="python"><span class="hljs-keyword">import</span> random
alist = [<span class="hljs-number">1</span>,<span class="hljs-number">2</span>,<span class="hljs-number">3</span>,<span
                class="hljs-number">4</span>,<span class="hljs-number">5</span>]
random.shuffle(alist)
print(alist)
<span class="copy-code-btn">复制代码</span></code></pre>
    <h2 class="heading" data-id="heading-36">27 现有字典 d= {'a':24,'g':52,'i':12,'k':33}请按value值进行排序?</h2>
    <pre><code class="hljs python copyable" lang="python">sorted(d.items(),key=<span
            class="hljs-keyword">lambda</span> x:x[<span class="hljs-number">1</span>])
<span class="copy-code-btn">复制代码</span></code></pre>
    <h2 class="heading" data-id="heading-37">28 字典推导式</h2>
    <pre><code class="hljs python copyable" lang="python">d = {key:value <span class="hljs-keyword">for</span> (key,value) <span
            class="hljs-keyword">in</span> iterable}
<span class="copy-code-btn">复制代码</span></code></pre>
    <h2 class="heading" data-id="heading-38">29 请反转字符串 "aStr"?</h2>
    <pre><code class="hljs python copyable" lang="python">print(<span class="hljs-string">"aStr"</span>[::<span
            class="hljs-number">-1</span>])
<span class="copy-code-btn">复制代码</span></code></pre>
    <h2 class="heading" data-id="heading-39">30 将字符串 "k:1 |k1:2|k2:3|k3:4"，处理成字典 {k:1,k1:2,</h2>
    <pre><code class="hljs python copyable" lang="python">str1 = <span
            class="hljs-string">"k:1|k1:2|k2:3|k3:4"</span>
<span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">str2dict</span><span
        class="hljs-params">(str1)</span>:</span>
    dict1 = {}
    <span class="hljs-keyword">for</span> iterms <span class="hljs-keyword">in</span> str1.split(<span
                class="hljs-string">'|'</span>):
        key,value = iterms.split(<span class="hljs-string">':'</span>)
        dict1[key] = value
    <span class="hljs-keyword">return</span> dict1
<span class="hljs-comment">#字典推导式</span>
d = {k:int(v) <span class="hljs-keyword">for</span> t <span class="hljs-keyword">in</span> str1.split(<span
                class="hljs-string">"|"</span>) <span class="hljs-keyword">for</span> k, v <span
                class="hljs-keyword">in</span> (t.split(<span class="hljs-string">":"</span>), )}
<span class="copy-code-btn">复制代码</span></code></pre>
    <h2 class="heading" data-id="heading-40">31 请按alist中元素的age由大到小排序</h2>
    <pre><code class="hljs python copyable" lang="python">alist = [{<span class="hljs-string">'name'</span>:<span
            class="hljs-string">'a'</span>,<span class="hljs-string">'age'</span>:<span
            class="hljs-number">20</span>},{<span class="hljs-string">'name'</span>:<span
            class="hljs-string">'b'</span>,<span class="hljs-string">'age'</span>:<span
            class="hljs-number">30</span>},{<span class="hljs-string">'name'</span>:<span
            class="hljs-string">'c'</span>,<span class="hljs-string">'age'</span>:<span
            class="hljs-number">25</span>}]
<span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">sort_by_age</span><span
        class="hljs-params">(list1)</span>:</span>
    <span class="hljs-keyword">return</span> sorted(alist,key=<span class="hljs-keyword">lambda</span> x:x[<span
                class="hljs-string">'age'</span>],reverse=<span class="hljs-keyword">True</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
    <h2 class="heading" data-id="heading-41">32 下面代码的输出结果将是什么？</h2>
    <pre><code class="hljs python copyable" lang="python">list = [<span class="hljs-string">'a'</span>,<span
            class="hljs-string">'b'</span>,<span class="hljs-string">'c'</span>,<span
            class="hljs-string">'d'</span>,<span
            class="hljs-string">'e'</span>]
print(list[<span class="hljs-number">10</span>:])
<span class="copy-code-btn">复制代码</span></code></pre>
    <p>
        代码将输出[],不会产生IndexError错误，就像所期望的那样，尝试用超出成员的个数的index来获取某个列表的成员。例如，尝试获取list[10]和之后的成员，会导致IndexError。然而，尝试获取列表的切片，开始的index超过了成员个数不会产生IndexError，而是仅仅返回一个空列表。这成为特别让人恶心的疑难杂症，因为运行的时候没有错误产生，导致Bug很难被追踪到。</p>
    <h2 class="heading" data-id="heading-42">33 写一个列表生成式，产生一个公差为11的等差数列</h2>
    <pre><code class="hljs python copyable" lang="python">print([x*<span class="hljs-number">11</span> <span
            class="hljs-keyword">for</span> x <span class="hljs-keyword">in</span> range(<span
            class="hljs-number">10</span>)])
<span class="copy-code-btn">复制代码</span></code></pre>
    <h2 class="heading" data-id="heading-43">34 给定两个列表，怎么找出他们相同的元素和不同的元素？</h2>
    <pre><code class="hljs python copyable" lang="python">list1 = [<span class="hljs-number">1</span>,<span
            class="hljs-number">2</span>,<span class="hljs-number">3</span>]
list2 = [<span class="hljs-number">3</span>,<span class="hljs-number">4</span>,<span class="hljs-number">5</span>]
set1 = set(list1)
set2 = set(list2)
print(set1 &amp; set2)
print(set1 ^ set2)
<span class="copy-code-btn">复制代码</span></code></pre>
    <h2 class="heading" data-id="heading-44">35 请写出一段python代码实现删除list里面的重复元素？</h2>
    <pre><code class="hljs python copyable" lang="python">l1 = [<span class="hljs-string">'b'</span>,<span
            class="hljs-string">'c'</span>,<span class="hljs-string">'d'</span>,<span
            class="hljs-string">'c'</span>,<span
            class="hljs-string">'a'</span>,<span class="hljs-string">'a'</span>]
l2 = list(set(l1))
print(l2)
<span class="copy-code-btn">复制代码</span></code></pre>
    <p>用list类的sort方法:</p>
    <pre><code class="hljs python copyable" lang="python">l1 = [<span class="hljs-string">'b'</span>,<span
            class="hljs-string">'c'</span>,<span class="hljs-string">'d'</span>,<span
            class="hljs-string">'c'</span>,<span
            class="hljs-string">'a'</span>,<span class="hljs-string">'a'</span>]
l2 = list(set(l1))
l2.sort(key=l1.index)
print(l2)
<span class="copy-code-btn">复制代码</span></code></pre>
    <p>也可以这样写:</p>
    <pre><code class="hljs python copyable" lang="python">l1 = [<span class="hljs-string">'b'</span>,<span
            class="hljs-string">'c'</span>,<span class="hljs-string">'d'</span>,<span
            class="hljs-string">'c'</span>,<span
            class="hljs-string">'a'</span>,<span class="hljs-string">'a'</span>]
l2 = sorted(set(l1),key=l1.index)
print(l2)
<span class="copy-code-btn">复制代码</span></code></pre>
    <p>也可以用遍历：</p>
    <pre><code class="hljs python copyable" lang="python">l1 = [<span class="hljs-string">'b'</span>,<span
            class="hljs-string">'c'</span>,<span class="hljs-string">'d'</span>,<span
            class="hljs-string">'c'</span>,<span
            class="hljs-string">'a'</span>,<span class="hljs-string">'a'</span>]
l2 = []
<span class="hljs-keyword">for</span> i <span class="hljs-keyword">in</span> l1:
    <span class="hljs-keyword">if</span> <span class="hljs-keyword">not</span> i <span class="hljs-keyword">in</span> l2:
        l2.append(i)
print(l2)
<span class="copy-code-btn">复制代码</span></code></pre>
    <h2 class="heading" data-id="heading-45">36 给定两个list A，B ,请用找出A，B中相同与不同的元素</h2>
    <pre><code class="hljs python copyable" lang="python">A,B 中相同元素： print(set(A)&amp;set(B))
A,B 中不同元素:  print(set(A)^set(B))
<span class="copy-code-btn">复制代码</span></code></pre>
    <h2 class="heading" data-id="heading-46">37 python新式类和经典类的区别？</h2>
    <p>a. 在python里凡是继承了object的类，都是新式类</p>
    <p>b. Python3里只有新式类</p>
    <p>c. Python2里面继承object的是新式类，没有写父类的是经典类</p>
    <p>d. 经典类目前在Python里基本没有应用</p>
    <h2 class="heading" data-id="heading-47">38 python中内置的数据结构有几种？</h2>
    <p>a. 整型 int、 长整型 long、浮点型 float、 复数 complex</p>
    <p>b. 字符串 str、 列表 list、 元祖 tuple</p>
    <p>c. 字典 dict 、 集合 set</p>
    <p>d. Python3 中没有 long，只有无限精度的 int</p>
    <h2 class="heading" data-id="heading-48">39 python如何实现单例模式?请写出两种实现方式?</h2>
    <p>第一种方法:使用装饰器</p>
    <pre><code class="hljs python copyable" lang="python"><span class="hljs-function"><span
            class="hljs-keyword">def</span> <span class="hljs-title">singleton</span><span
            class="hljs-params">(cls)</span>:</span>
    instances = {}
    <span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">wrapper</span><span
            class="hljs-params">(*args, **kwargs)</span>:</span>
        <span class="hljs-keyword">if</span> cls <span class="hljs-keyword">not</span> <span
                class="hljs-keyword">in</span> instances:
            instances[cls] = cls(*args, **kwargs)
        <span class="hljs-keyword">return</span> instances[cls]
    <span class="hljs-keyword">return</span> wrapper
    
    
<span class="hljs-meta">@singleton</span>
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Foo</span><span
        class="hljs-params">(object)</span>:</span>
    <span class="hljs-keyword">pass</span>
foo1 = Foo()
foo2 = Foo()
print(foo1 <span class="hljs-keyword">is</span> foo2)  <span class="hljs-comment"># True</span>
<span class="copy-code-btn">复制代码</span></code></pre>
    <p>第二种方法：使用基类
        New 是真正创建实例对象的方法，所以重写基类的new 方法，以此保证创建对象的时候只生成一个实例</p>
    <pre><code class="hljs python copyable" lang="python"><span class="hljs-class"><span
            class="hljs-keyword">class</span> <span class="hljs-title">Singleton</span><span class="hljs-params">(object)</span>:</span>
    <span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">__new__</span><span
            class="hljs-params">(cls, *args, **kwargs)</span>:</span>
        <span class="hljs-keyword">if</span> <span class="hljs-keyword">not</span> hasattr(cls, <span
                class="hljs-string">'_instance'</span>):
            cls._instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
        <span class="hljs-keyword">return</span> cls._instance
    
    
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Foo</span><span
        class="hljs-params">(Singleton)</span>:</span>
    <span class="hljs-keyword">pass</span>

foo1 = Foo()
foo2 = Foo()

print(foo1 <span class="hljs-keyword">is</span> foo2)  <span class="hljs-comment"># True</span>
<span class="copy-code-btn">复制代码</span></code></pre>
    <p>第三种方法：元类，元类是用于创建类对象的类，类对象创建实例对象时一定要调用call方法，因此在调用call时候保证始终只创建一个实例即可，type是python的元类</p>
    <pre><code class="hljs python copyable" lang="python"><span class="hljs-class"><span
            class="hljs-keyword">class</span> <span class="hljs-title">Singleton</span><span
            class="hljs-params">(type)</span>:</span>
    <span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">__call__</span><span
            class="hljs-params">(cls, *args, **kwargs)</span>:</span>
        <span class="hljs-keyword">if</span> <span class="hljs-keyword">not</span> hasattr(cls, <span
                class="hljs-string">'_instance'</span>):
            cls._instance = super(Singleton, cls).__call__(*args, **kwargs)
        <span class="hljs-keyword">return</span> cls._instance


<span class="hljs-comment"># Python2</span>
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Foo</span><span
        class="hljs-params">(object)</span>:</span>
    __metaclass__ = Singleton

<span class="hljs-comment"># Python3</span>
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Foo</span><span
        class="hljs-params">(metaclass=Singleton)</span>:</span>
    <span class="hljs-keyword">pass</span>

foo1 = Foo()
foo2 = Foo()
print(foo1 <span class="hljs-keyword">is</span> foo2)  <span class="hljs-comment"># True</span>

<span class="copy-code-btn">复制代码</span></code></pre>
    <h2 class="heading" data-id="heading-49">40 反转一个整数，例如-123 --&gt; -321</h2>
    <pre><code class="hljs python copyable" lang="python"><span class="hljs-class"><span
            class="hljs-keyword">class</span> <span class="hljs-title">Solution</span><span
            class="hljs-params">(object)</span>:</span>
    <span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">reverse</span><span
            class="hljs-params">(self,x)</span>:</span>
        <span class="hljs-keyword">if</span> <span class="hljs-number">-10</span>&lt;x&lt;<span
                class="hljs-number">10</span>:
            <span class="hljs-keyword">return</span> x
        str_x = str(x)
        <span class="hljs-keyword">if</span> str_x[<span class="hljs-number">0</span>] !=<span
                class="hljs-string">"-"</span>:
            str_x = str_x[::<span class="hljs-number">-1</span>]
            x = int(str_x)
        <span class="hljs-keyword">else</span>:
            str_x = str_x[<span class="hljs-number">1</span>:][::<span class="hljs-number">-1</span>]
            x = int(str_x)
            x = -x
        <span class="hljs-keyword">return</span> x <span class="hljs-keyword">if</span> <span class="hljs-number">-2147483648</span>&lt;x&lt;<span
                class="hljs-number">2147483647</span> <span class="hljs-keyword">else</span> <span
                class="hljs-number">0</span>
<span class="hljs-keyword">if</span> __name__ == <span class="hljs-string">'__main__'</span>:
    s = Solution()
    reverse_int = s.reverse(<span class="hljs-number">-120</span>)
    print(reverse_int)
<span class="copy-code-btn">复制代码</span></code></pre>
    <h2 class="heading" data-id="heading-50">41 设计实现遍历目录与子目录，抓取.pyc文件?</h2>
    <p>第一种方法：</p>
    <pre><code class="hljs python copyable" lang="python"><span class="hljs-keyword">import</span> os

<span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">get_files</span><span
        class="hljs-params">(dir,suffix)</span>:</span>
    res = []
    <span class="hljs-keyword">for</span> root,dirs,files <span class="hljs-keyword">in</span> os.walk(dir):
        <span class="hljs-keyword">for</span> filename <span class="hljs-keyword">in</span> files:
            name,suf = os.path.splitext(filename)
            <span class="hljs-keyword">if</span> suf == suffix:
                res.append(os.path.join(root,filename))

    print(res)

get_files(<span class="hljs-string">"./"</span>,<span class="hljs-string">'.pyc'</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
    <p>第二种方法：</p>
    <pre><code class="hljs python copyable" lang="python"><span class="hljs-keyword">import</span> os

<span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">pick</span><span
        class="hljs-params">(obj)</span>:</span>
    <span class="hljs-keyword">if</span> ob.endswith(<span class="hljs-string">".pyc"</span>):
        print(obj)

<span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">scan_path</span><span
        class="hljs-params">(ph)</span>:</span>
    file_list = os.listdir(ph)
    <span class="hljs-keyword">for</span> obj <span class="hljs-keyword">in</span> file_list:
        <span class="hljs-keyword">if</span> os.path.isfile(obj):
    pick(obj)
        <span class="hljs-keyword">elif</span> os.path.isdir(obj):
            scan_path(obj)

<span class="hljs-keyword">if</span> __name__==<span class="hljs-string">'__main__'</span>:
    path = input(<span class="hljs-string">'输入目录'</span>)
    scan_path(path)
<span class="copy-code-btn">复制代码</span></code></pre>
    <p>第三种方法</p>
    <pre><code class="hljs bash copyable" lang="bash">from glob import iglob


def func(fp, postfix):
    <span class="hljs-keyword">for</span> i <span class="hljs-keyword">in</span> iglob(f<span class="hljs-string">"{fp}/**/*{postfix}"</span>, recursive=True):
        <span class="hljs-built_in">print</span>(i)

<span class="hljs-keyword">if</span> __name__ == <span class="hljs-string">"__main__"</span>:
    postfix = <span class="hljs-string">".pyc"</span>
    func(<span class="hljs-string">"K:\Python_script"</span>, postfix)
<span class="copy-code-btn">复制代码</span></code></pre>
    <h2 class="heading" data-id="heading-51">42 Python-遍历列表时删除元素的正确做法</h2>
    <p>遍历在新在列表操作，删除时在原来的列表操作</p>
    <pre><code class="hljs python copyable" lang="python">a = [<span class="hljs-number">1</span>,<span
            class="hljs-number">2</span>,<span class="hljs-number">3</span>,<span class="hljs-number">4</span>,<span
            class="hljs-number">5</span>,<span class="hljs-number">6</span>,<span class="hljs-number">7</span>,<span
            class="hljs-number">8</span>]
print(id(a))
print(id(a[:]))
<span class="hljs-keyword">for</span> i <span class="hljs-keyword">in</span> a[:]:
    <span class="hljs-keyword">if</span> i&gt;<span class="hljs-number">5</span>:
        <span class="hljs-keyword">pass</span>
    <span class="hljs-keyword">else</span>:
        a.remove(i)
    print(a)
print(<span class="hljs-string">'-----------'</span>)
print(id(a))

<span class="copy-code-btn">复制代码</span></code></pre>
    <pre><code class="hljs python copyable" lang="python"><span class="hljs-comment">#filter</span>
a=[<span class="hljs-number">1</span>,<span class="hljs-number">2</span>,<span class="hljs-number">3</span>,<span
                class="hljs-number">4</span>,<span class="hljs-number">5</span>,<span
                class="hljs-number">6</span>,<span class="hljs-number">7</span>,<span class="hljs-number">8</span>]
b = filter(<span class="hljs-keyword">lambda</span> x: x&gt;<span class="hljs-number">5</span>,a)
print(list(b))
<span class="copy-code-btn">复制代码</span></code></pre>
    <p>列表解析</p>
    <pre><code class="hljs python copyable" lang="python">a=[<span class="hljs-number">1</span>,<span
            class="hljs-number">2</span>,<span class="hljs-number">3</span>,<span class="hljs-number">4</span>,<span
            class="hljs-number">5</span>,<span class="hljs-number">6</span>,<span class="hljs-number">7</span>,<span
            class="hljs-number">8</span>]
b = [i <span class="hljs-keyword">for</span> i <span class="hljs-keyword">in</span> a <span
                class="hljs-keyword">if</span> i&gt;<span class="hljs-number">5</span>]
print(b)
<span class="copy-code-btn">复制代码</span></code></pre>
    <p>倒序删除
        因为列表总是‘向前移’，所以可以倒序遍历，即使后面的元素被修改了，还没有被遍历的元素和其坐标还是保持不变的</p>
    <pre><code class="hljs python copyable" lang="python">a=[<span class="hljs-number">1</span>,<span
            class="hljs-number">2</span>,<span class="hljs-number">3</span>,<span class="hljs-number">4</span>,<span
            class="hljs-number">5</span>,<span class="hljs-number">6</span>,<span class="hljs-number">7</span>,<span
            class="hljs-number">8</span>]
print(id(a))
<span class="hljs-keyword">for</span> i <span class="hljs-keyword">in</span> range(len(a)<span
                class="hljs-number">-1</span>,<span class="hljs-number">-1</span>,<span
                class="hljs-number">-1</span>):
    <span class="hljs-keyword">if</span> a[i]&gt;<span class="hljs-number">5</span>:
        <span class="hljs-keyword">pass</span>
    <span class="hljs-keyword">else</span>:
        a.remove(a[i])
print(id(a))
print(<span class="hljs-string">'-----------'</span>)
print(a)
<span class="copy-code-btn">复制代码</span></code></pre>
    <h2 class="heading" data-id="heading-52">43 字符串的操作题目</h2>
    <p>全字母短句 PANGRAM 是包含所有英文字母的句子，比如：A QUICK BROWN FOX JUMPS OVER THE LAZY DOG. 定义并实现一个方法 get_missing_letter,
        传入一个字符串采纳数，返回参数字符串变成一个 PANGRAM 中所缺失的字符。应该忽略传入字符串参数中的大小写，返回应该都是小写字符并按字母顺序排序（请忽略所有非 ACSII 字符）</p>
    <p><strong>下面示例是用来解释，双引号不需要考虑:</strong></p>
    <p>(0)输入: "A quick brown for jumps over the lazy dog"</p>
    <p>返回： ""</p>
    <p>(1)输入: "A slow yellow fox crawls under the proactive dog"</p>
    <p>返回: "bjkmqz"</p>
    <p>(2)输入: "Lions, and tigers, and bears, oh my!"</p>
    <p>返回: "cfjkpquvwxz"</p>
    <p>(3)输入: ""</p>
    <p>返回："abcdefghijklmnopqrstuvwxyz"</p>
    <pre><code class="hljs python copyable" lang="python"><span class="hljs-function"><span
            class="hljs-keyword">def</span> <span class="hljs-title">get_missing_letter</span><span
            class="hljs-params">(a)</span>:</span>
    s1 = set(<span class="hljs-string">"abcdefghijklmnopqrstuvwxyz"</span>)
    s2 = set(a)
    ret = <span class="hljs-string">""</span>.join(sorted(s1-s2))
    <span class="hljs-keyword">return</span> ret
    
print(get_missing_letter(<span class="hljs-string">"python"</span>))
<span class="copy-code-btn">复制代码</span></code></pre>
    <h2 class="heading" data-id="heading-53">44 可变类型和不可变类型</h2>
    <p>1,可变类型有list,dict.不可变类型有string，number,tuple.</p>
    <p>2,当进行修改操作时，可变类型传递的是内存中的地址，也就是说，直接修改内存中的值，并没有开辟新的内存。</p>
    <p>3,不可变类型被改变时，并没有改变原内存地址中的值，而是开辟一块新的内存，将原地址中的值复制过去，对这块新开辟的内存中的值进行操作。</p>
    <h2 class="heading" data-id="heading-54">45 is和==有什么区别？</h2>
    <p>is：比较的是两个对象的id值是否相等，也就是比较俩对象是否为同一个实例对象。是否指向同一个内存地址</p>
    <p>== ： 比较的两个对象的内容/值是否相等，默认会调用对象的eq()方法</p>
    <h2 class="heading" data-id="heading-55">46 求出列表所有奇数并构造新列表</h2>
    <pre><code class="hljs python copyable" lang="python">a = [<span class="hljs-number">1</span>,<span
            class="hljs-number">2</span>,<span class="hljs-number">3</span>,<span class="hljs-number">4</span>,<span
            class="hljs-number">5</span>,<span class="hljs-number">6</span>,<span class="hljs-number">7</span>,<span
            class="hljs-number">8</span>,<span class="hljs-number">9</span>,<span class="hljs-number">10</span>]
res = [ i <span class="hljs-keyword">for</span> i <span class="hljs-keyword">in</span> a <span
                class="hljs-keyword">if</span> i%<span class="hljs-number">2</span>==<span
                class="hljs-number">1</span>]
print(res)
<span class="copy-code-btn">复制代码</span></code></pre>
    <h2 class="heading" data-id="heading-56">47 用一行python代码写出1+2+3+10248</h2>
    <pre><code class="hljs python copyable" lang="python"><span class="hljs-keyword">from</span> functools <span
            class="hljs-keyword">import</span> reduce
<span class="hljs-comment">#1.使用sum内置求和函数</span>
num = sum([<span class="hljs-number">1</span>,<span class="hljs-number">2</span>,<span
                class="hljs-number">3</span>,<span class="hljs-number">10248</span>])
print(num)
<span class="hljs-comment">#2.reduce 函数</span>
num1 = reduce(<span class="hljs-keyword">lambda</span> x,y :x+y,[<span class="hljs-number">1</span>,<span
                class="hljs-number">2</span>,<span class="hljs-number">3</span>,<span
                class="hljs-number">10248</span>])
print(num1)
<span class="copy-code-btn">复制代码</span></code></pre>
    <h2 class="heading" data-id="heading-57">48 Python中变量的作用域？（变量查找顺序)</h2>
    <p>函数作用域的LEGB顺序</p>
    <p>1.什么是LEGB?</p>
    <p>L： local 函数内部作用域</p>
    <p>E: enclosing 函数内部与内嵌函数之间</p>
    <p>G: global 全局作用域</p>
    <p>B： build-in 内置作用</p>
    <p>python在函数里面的查找分为4种，称之为LEGB，也正是按照这是顺序来查找的</p>
    <h2 class="heading" data-id="heading-58">49 字符串 <code>"123"</code> 转换成 <code>123</code>，不使用内置api，例如
        <code>int()</code></h2>
    <p>方法一： 利用 <code>str</code> 函数</p>
    <pre><code class="hljs python copyable" lang="python"><span class="hljs-function"><span
            class="hljs-keyword">def</span> <span class="hljs-title">atoi</span><span
            class="hljs-params">(s)</span>:</span>
    num = <span class="hljs-number">0</span>
    <span class="hljs-keyword">for</span> v <span class="hljs-keyword">in</span> s:
        <span class="hljs-keyword">for</span> j <span class="hljs-keyword">in</span> range(<span
                class="hljs-number">10</span>):
            <span class="hljs-keyword">if</span> v == str(j):
                num = num * <span class="hljs-number">10</span> + j
    <span class="hljs-keyword">return</span> num
<span class="copy-code-btn">复制代码</span></code></pre>
    <p>方法二： 利用 <code>ord</code> 函数</p>
    <pre><code class="hljs python copyable" lang="python"><span class="hljs-function"><span
            class="hljs-keyword">def</span> <span class="hljs-title">atoi</span><span
            class="hljs-params">(s)</span>:</span>
    num = <span class="hljs-number">0</span>
    <span class="hljs-keyword">for</span> v <span class="hljs-keyword">in</span> s:
        num = num * <span class="hljs-number">10</span> + ord(v) - ord(<span class="hljs-string">'0'</span>)
    <span class="hljs-keyword">return</span> num
<span class="copy-code-btn">复制代码</span></code></pre>
    <p>方法三: 利用 <code>eval</code> 函数</p>
    <pre><code class="hljs python copyable" lang="python"><span class="hljs-function"><span
            class="hljs-keyword">def</span> <span class="hljs-title">atoi</span><span
            class="hljs-params">(s)</span>:</span>
    num = <span class="hljs-number">0</span>
    <span class="hljs-keyword">for</span> v <span class="hljs-keyword">in</span> s:
        t = <span class="hljs-string">"%s * 1"</span> % v
        n = eval(t)
        num = num * <span class="hljs-number">10</span> + n
    <span class="hljs-keyword">return</span> num
<span class="copy-code-btn">复制代码</span></code></pre>
    <p>方法四: 结合方法二，使用 <code>reduce</code>，一行解决</p>
    <pre><code class="hljs python copyable" lang="python"><span class="hljs-keyword">from</span> functools <span
            class="hljs-keyword">import</span> reduce
<span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">atoi</span><span
        class="hljs-params">(s)</span>:</span>
    <span class="hljs-keyword">return</span> reduce(<span class="hljs-keyword">lambda</span> num, v: num * <span
                class="hljs-number">10</span> + ord(v) - ord(<span class="hljs-string">'0'</span>), s, <span
                class="hljs-number">0</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
    <h2 class="heading" data-id="heading-59">50 Given an array of integers</h2>
    <p>给定一个整数数组和一个目标值，找出数组中和为目标值的两个数。你可以假设每个输入只对应一种答案，且同样的元素不能被重复利用。示例:给定nums = [2,7,11,15],target=9 因为
        nums[0]+nums[1] = 2+7 =9,所以返回[0,1]</p>
    <pre><code class="hljs python copyable" lang="python"><span class="hljs-class"><span
            class="hljs-keyword">class</span> <span class="hljs-title">Solution</span>:</span>
    <span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">twoSum</span><span
            class="hljs-params">(self,nums,target)</span>:</span>
        <span class="hljs-string">"""
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """</span>
        d = {}
        size = <span class="hljs-number">0</span>
        <span class="hljs-keyword">while</span> size &lt; len(nums):
            <span class="hljs-keyword">if</span> target-nums[size] <span class="hljs-keyword">in</span> d:
                <span class="hljs-keyword">if</span> d[target-nums[size]] &lt;size:
                    <span class="hljs-keyword">return</span> [d[target-nums[size]],size]
                <span class="hljs-keyword">else</span>:
                    d[nums[size]] = size
                size = size +<span class="hljs-number">1</span>
solution = Solution()
list = [<span class="hljs-number">2</span>,<span class="hljs-number">7</span>,<span class="hljs-number">11</span>,<span
                class="hljs-number">15</span>]
target = <span class="hljs-number">9</span>
nums = solution.twoSum(list,target)
print(nums)
<span class="copy-code-btn">复制代码</span></code></pre>
    <p>
        给列表中的字典排序：假设有如下list对象，alist=[{"name":"a","age":20},{"name":"b","age":30},{"name":"c","age":25}],将alist中的元素按照age从大到小排序
        alist=[{"name":"a","age":20},{"name":"b","age":30},{"name":"c","age":25}]</p>
    <pre><code class="hljs python copyable" lang="python">alist_sort = sorted(alist,key=<span class="hljs-keyword">lambda</span> e: e.__getitem__(<span
            class="hljs-string">'age'</span>),reverse=<span class="hljs-keyword">True</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
    <h2 class="heading" data-id="heading-60">51 python代码实现删除一个list里面的重复元素</h2>
    <pre><code class="hljs python copyable" lang="python"><span class="hljs-function"><span
            class="hljs-keyword">def</span> <span class="hljs-title">distFunc1</span><span
            class="hljs-params">(a)</span>:</span>
    <span class="hljs-string">"""使用集合去重"""</span>
    a = list(set(a))
    print(a)

<span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">distFunc2</span><span
        class="hljs-params">(a)</span>:</span>
    <span class="hljs-string">"""将一个列表的数据取出放到另一个列表中，中间作判断"""</span>
    list = []
    <span class="hljs-keyword">for</span> i <span class="hljs-keyword">in</span> a:
        <span class="hljs-keyword">if</span> i <span class="hljs-keyword">not</span> <span
                class="hljs-keyword">in</span> list:
            list.append(i)
    <span class="hljs-comment">#如果需要排序的话用sort</span>
    list.sort()
    print(list)

<span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">distFunc3</span><span
        class="hljs-params">(a)</span>:</span>
    <span class="hljs-string">"""使用字典"""</span>
    b = {}
    b = b.fromkeys(a)
    c = list(b.keys())
    print(c)

<span class="hljs-keyword">if</span> __name__ == <span class="hljs-string">"__main__"</span>:
    a = [<span class="hljs-number">1</span>,<span class="hljs-number">2</span>,<span class="hljs-number">4</span>,<span
                class="hljs-number">2</span>,<span class="hljs-number">4</span>,<span
                class="hljs-number">5</span>,<span class="hljs-number">7</span>,<span
                class="hljs-number">10</span>,<span
                class="hljs-number">5</span>,<span class="hljs-number">5</span>,<span
                class="hljs-number">7</span>,<span class="hljs-number">8</span>,<span
                class="hljs-number">9</span>,<span class="hljs-number">0</span>,<span class="hljs-number">3</span>]
    distFunc1(a)
    distFunc2(a)
    distFunc3(a)
  
<span class="copy-code-btn">复制代码</span></code></pre>
    <h2 class="heading" data-id="heading-61">52 统计一个文本中单词频次最高的10个单词？</h2>
    <pre><code class="hljs python copyable" lang="python"><span class="hljs-keyword">import</span> re

<span class="hljs-comment"># 方法一</span>
<span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">test</span><span
        class="hljs-params">(filepath)</span>:</span>
    
    distone = {}

    <span class="hljs-keyword">with</span> open(filepath) <span class="hljs-keyword">as</span> f:
        <span class="hljs-keyword">for</span> line <span class="hljs-keyword">in</span> f:
            line = re.sub(<span class="hljs-string">"\W+"</span>, <span class="hljs-string">" "</span>, line)
            lineone = line.split()
            <span class="hljs-keyword">for</span> keyone <span class="hljs-keyword">in</span> lineone:
                <span class="hljs-keyword">if</span> <span class="hljs-keyword">not</span> distone.get(keyone):
                    distone[keyone] = <span class="hljs-number">1</span>
                <span class="hljs-keyword">else</span>:
                    distone[keyone] += <span class="hljs-number">1</span>
    num_ten = sorted(distone.items(), key=<span class="hljs-keyword">lambda</span> x:x[<span
                class="hljs-number">1</span>], reverse=<span class="hljs-keyword">True</span>)[:<span
                class="hljs-number">10</span>]
    num_ten =[x[<span class="hljs-number">0</span>] <span class="hljs-keyword">for</span> x <span class="hljs-keyword">in</span> num_ten]
    <span class="hljs-keyword">return</span> num_ten
    
 
<span class="hljs-comment"># 方法二 </span>
<span class="hljs-comment"># 使用 built-in 的 Counter 里面的 most_common</span>
<span class="hljs-keyword">import</span> re
<span class="hljs-keyword">from</span> collections <span class="hljs-keyword">import</span> Counter


<span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">test2</span><span
        class="hljs-params">(filepath)</span>:</span>
    <span class="hljs-keyword">with</span> open(filepath) <span class="hljs-keyword">as</span> f:
        <span class="hljs-keyword">return</span> list(map(<span class="hljs-keyword">lambda</span> c: c[<span
                class="hljs-number">0</span>], Counter(re.sub(<span class="hljs-string">"\W+"</span>, <span
                class="hljs-string">" "</span>, f.read()).split()).most_common(<span class="hljs-number">10</span>)))
<span class="copy-code-btn">复制代码</span></code></pre>
    <h2 class="heading" data-id="heading-62">53 请写出一个函数满足以下条件</h2>
    <p>该函数的输入是一个仅包含数字的list,输出一个新的list，其中每一个元素要满足以下条件：</p>
    <p>1、该元素是偶数</p>
    <p>2、该元素在原list中是在偶数的位置(index是偶数)</p>
    <pre><code class="hljs python copyable" lang="python"><span class="hljs-function"><span
            class="hljs-keyword">def</span> <span class="hljs-title">num_list</span><span
            class="hljs-params">(num)</span>:</span>
    <span class="hljs-keyword">return</span> [i <span class="hljs-keyword">for</span> i <span
                class="hljs-keyword">in</span> num <span class="hljs-keyword">if</span> i %<span
                class="hljs-number">2</span> ==<span class="hljs-number">0</span> <span
                class="hljs-keyword">and</span> num.index(i)%<span class="hljs-number">2</span>==<span
                class="hljs-number">0</span>]

num = [<span class="hljs-number">0</span>,<span class="hljs-number">1</span>,<span class="hljs-number">2</span>,<span
                class="hljs-number">3</span>,<span class="hljs-number">4</span>,<span
                class="hljs-number">5</span>,<span class="hljs-number">6</span>,<span
                class="hljs-number">7</span>,<span class="hljs-number">8</span>,<span
                class="hljs-number">9</span>,<span class="hljs-number">10</span>]
result = num_list(num)
print(result)
<span class="copy-code-btn">复制代码</span></code></pre>
    <h2 class="heading" data-id="heading-63">54 使用单一的列表生成式来产生一个新的列表</h2>
    <p>该列表只包含满足以下条件的值，元素为原始列表中偶数切片</p>
    <pre><code class="hljs python copyable" lang="python">list_data = [<span class="hljs-number">1</span>,<span
            class="hljs-number">2</span>,<span class="hljs-number">5</span>,<span class="hljs-number">8</span>,<span
            class="hljs-number">10</span>,<span class="hljs-number">3</span>,<span
            class="hljs-number">18</span>,<span class="hljs-number">6</span>,<span class="hljs-number">20</span>]
res = [x <span class="hljs-keyword">for</span> x <span class="hljs-keyword">in</span> list_data[::<span
                class="hljs-number">2</span>] <span class="hljs-keyword">if</span> x %<span
                class="hljs-number">2</span> ==<span class="hljs-number">0</span>]
print(res)
<span class="copy-code-btn">复制代码</span></code></pre>
    <h2 class="heading" data-id="heading-64">55 用一行代码生成[1,4,9,16,25,36,49,64,81,100]</h2>
    <pre><code class="hljs python copyable" lang="python">[x * x <span class="hljs-keyword">for</span> x <span
            class="hljs-keyword">in</span> range(<span class="hljs-number">1</span>,<span
            class="hljs-number">11</span>)]
<span class="copy-code-btn">复制代码</span></code></pre>
    <h2 class="heading" data-id="heading-65">56 输入某年某月某日，判断这一天是这一年的第几天？</h2>
    <pre><code class="hljs python copyable" lang="python"><span class="hljs-keyword">import</span> datetime

y = int(input(<span class="hljs-string">"请输入4位数字的年份:"</span>))
m = int(input(<span class="hljs-string">"请输入月份:"</span>))
d = int(input(<span class="hljs-string">"请输入是哪一天"</span>))

targetDay = datetime.date(y,m,d)
dayCount = targetDay - datetime.date(targetDay.year <span class="hljs-number">-1</span>,<span
                class="hljs-number">12</span>,<span class="hljs-number">31</span>)
print(<span class="hljs-string">"%s是 %s年的第%s天。"</span>%(targetDay,y,dayCount.days))
<span class="copy-code-btn">复制代码</span></code></pre>
    <h2 class="heading" data-id="heading-66">57 两个有序列表，l1,l2，对这两个列表进行合并不可使用extend</h2>
    <pre><code class="hljs python copyable" lang="python"><span class="hljs-function"><span
            class="hljs-keyword">def</span> <span class="hljs-title">loop_merge_sort</span><span
            class="hljs-params">(l1,l2)</span>:</span>
    tmp = []
    <span class="hljs-keyword">while</span> len(l1)&gt;<span class="hljs-number">0</span> <span
                class="hljs-keyword">and</span> len(l2)&gt;<span class="hljs-number">0</span>:
        <span class="hljs-keyword">if</span> l1[<span class="hljs-number">0</span>] &lt;l2[<span
                class="hljs-number">0</span>]:
            tmp.append(l1[<span class="hljs-number">0</span>])
            <span class="hljs-keyword">del</span> l1[<span class="hljs-number">0</span>]
        <span class="hljs-keyword">else</span>:
            tmp.append(l2[<span class="hljs-number">0</span>])
            <span class="hljs-keyword">del</span> l2[<span class="hljs-number">0</span>]
    <span class="hljs-keyword">while</span> len(l1)&gt;<span class="hljs-number">0</span>:
        tmp.append(l1[<span class="hljs-number">0</span>])
        <span class="hljs-keyword">del</span> l1[<span class="hljs-number">0</span>]
    <span class="hljs-keyword">while</span> len(l2)&gt;<span class="hljs-number">0</span>:
        tmp.append(l2[<span class="hljs-number">0</span>])
        <span class="hljs-keyword">del</span> l2[<span class="hljs-number">0</span>]
    <span class="hljs-keyword">return</span> tmp
<span class="copy-code-btn">复制代码</span></code></pre>
    <h2 class="heading" data-id="heading-67">58 给定一个任意长度数组，实现一个函数</h2>
    <p>让所有奇数都在偶数前面，而且奇数升序排列，偶数降序排序，如字符串'1982376455',变成'1355798642'</p>
    <pre><code class="hljs python copyable" lang="python"><span class="hljs-comment"># 方法一</span>
<span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">func1</span><span
        class="hljs-params">(l)</span>:</span>
    <span class="hljs-keyword">if</span> isinstance(l, str):
        l = [int(i) <span class="hljs-keyword">for</span> i <span class="hljs-keyword">in</span> l]
    l.sort(reverse=<span class="hljs-keyword">True</span>)
    <span class="hljs-keyword">for</span> i <span class="hljs-keyword">in</span> range(len(l)):
        <span class="hljs-keyword">if</span> l[i] % <span class="hljs-number">2</span> &gt; <span
                class="hljs-number">0</span>:
            l.insert(<span class="hljs-number">0</span>, l.pop(i))
    print(<span class="hljs-string">''</span>.join(str(e) <span class="hljs-keyword">for</span> e <span
                class="hljs-keyword">in</span> l))

<span class="hljs-comment"># 方法二</span>
<span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">func2</span><span
        class="hljs-params">(l)</span>:</span>
    print(<span class="hljs-string">""</span>.join(sorted(l, key=<span
                class="hljs-keyword">lambda</span> x: int(x) % <span class="hljs-number">2</span> == <span
                class="hljs-number">0</span> <span class="hljs-keyword">and</span> <span
                class="hljs-number">20</span> - int(x) <span class="hljs-keyword">or</span> int(x))))
<span class="copy-code-btn">复制代码</span></code></pre>
    <h2 class="heading" data-id="heading-68">59 写一个函数找出一个整数数组中，第二大的数</h2>
    <pre><code class="hljs python copyable" lang="python"><span class="hljs-function"><span
            class="hljs-keyword">def</span> <span class="hljs-title">find_second_large_num</span><span
            class="hljs-params">(num_list)</span>:</span>
    <span class="hljs-string">"""
    找出数组第2大的数字
    """</span>
    <span class="hljs-comment"># 方法一</span>
    <span class="hljs-comment"># 直接排序，输出倒数第二个数即可</span>
    tmp_list = sorted(num_list)
    print(<span class="hljs-string">"方法一\nSecond_large_num is :"</span>, tmp_list[<span class="hljs-number">-2</span>])
    
    <span class="hljs-comment"># 方法二</span>
    <span class="hljs-comment"># 设置两个标志位一个存储最大数一个存储次大数</span>
    <span class="hljs-comment"># two 存储次大值，one 存储最大值，遍历一次数组即可，先判断是否大于 one，若大于将 one 的值给 two，将 num_list[i] 的值给 one，否则比较是否大于two，若大于直接将 num_list[i] 的值给two，否则pass</span>
    one = num_list[<span class="hljs-number">0</span>]
    two = num_list[<span class="hljs-number">0</span>]
    <span class="hljs-keyword">for</span> i <span class="hljs-keyword">in</span> range(<span
                class="hljs-number">1</span>, len(num_list)):
        <span class="hljs-keyword">if</span> num_list[i] &gt; one:
            two = one
            one = num_list[i]
        <span class="hljs-keyword">elif</span> num_list[i] &gt; two:
            two = num_list[i]
    print(<span class="hljs-string">"方法二\nSecond_large_num is :"</span>, two)
    
    <span class="hljs-comment"># 方法三</span>
    <span class="hljs-comment"># 用 reduce 与逻辑符号 (and, or)</span>
    <span class="hljs-comment"># 基本思路与方法二一样，但是不需要用 if 进行判断。</span>
    <span class="hljs-keyword">from</span> functools <span class="hljs-keyword">import</span> reduce
    num = reduce(<span class="hljs-keyword">lambda</span> ot, x: ot[<span class="hljs-number">1</span>] &lt; x <span
                class="hljs-keyword">and</span> (ot[<span class="hljs-number">1</span>], x) <span
                class="hljs-keyword">or</span> ot[<span class="hljs-number">0</span>] &lt; x <span
                class="hljs-keyword">and</span> (x, ot[<span class="hljs-number">1</span>]) <span
                class="hljs-keyword">or</span> ot, num_list, (<span class="hljs-number">0</span>, <span
                class="hljs-number">0</span>))[<span class="hljs-number">0</span>]
    print(<span class="hljs-string">"方法三\nSecond_large_num is :"</span>, num)
    
    
<span class="hljs-keyword">if</span> __name__ == <span class="hljs-string">'__main___'</span>:
    num_list = [<span class="hljs-number">34</span>, <span class="hljs-number">11</span>, <span
                class="hljs-number">23</span>, <span class="hljs-number">56</span>, <span
                class="hljs-number">78</span>, <span class="hljs-number">0</span>, <span
                class="hljs-number">9</span>, <span class="hljs-number">12</span>, <span
                class="hljs-number">3</span>, <span class="hljs-number">7</span>, <span class="hljs-number">5</span>]
    find_second_large_num(num_list)
<span class="copy-code-btn">复制代码</span></code></pre>
    <h2 class="heading" data-id="heading-69">60 阅读一下代码他们的输出结果是什么？</h2>
    <pre><code class="hljs python copyable" lang="python"><span class="hljs-function"><span
            class="hljs-keyword">def</span> <span class="hljs-title">multi</span><span
            class="hljs-params">()</span>:</span>
    <span class="hljs-keyword">return</span> [<span class="hljs-keyword">lambda</span> x : i*x <span
                class="hljs-keyword">for</span> i <span class="hljs-keyword">in</span> range(<span
                class="hljs-number">4</span>)]
print([m(<span class="hljs-number">3</span>) <span class="hljs-keyword">for</span> m <span
                class="hljs-keyword">in</span> multi()])
<span class="copy-code-btn">复制代码</span></code></pre>
    <p>正确答案是[9,9,9,9]，而不是[0,3,6,9]产生的原因是Python的闭包的后期绑定导致的，这意味着在闭包中的变量是在内部函数被调用的时候被查找的，因为，最后函数被调用的时候，for循环已经完成, i
        的值最后是3,因此每一个返回值的i都是3,所以最后的结果是[9,9,9,9]</p>
    <h2 class="heading" data-id="heading-70">61 统计一段字符串中字符出现的次数</h2>
    <pre><code class="hljs python copyable" lang="python"><span class="hljs-comment"># 方法一</span>
<span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">count_str</span><span
        class="hljs-params">(str_data)</span>:</span>
    <span class="hljs-string">"""定义一个字符出现次数的函数"""</span>
    dict_str = {} 
    <span class="hljs-keyword">for</span> i <span class="hljs-keyword">in</span> str_data:
        dict_str[i] = dict_str.get(i, <span class="hljs-number">0</span>) + <span class="hljs-number">1</span>
    <span class="hljs-keyword">return</span> dict_str
dict_str = count_str(<span class="hljs-string">"AAABBCCAC"</span>)
str_count_data = <span class="hljs-string">""</span>
<span class="hljs-keyword">for</span> k, v <span class="hljs-keyword">in</span> dict_str.items():
    str_count_data += k + str(v)
print(str_count_data)

<span class="hljs-comment"># 方法二</span>
<span class="hljs-keyword">from</span> collections <span class="hljs-keyword">import</span> Counter

print(<span class="hljs-string">""</span>.join(map(<span class="hljs-keyword">lambda</span> x: x[<span
                class="hljs-number">0</span>] + str(x[<span class="hljs-number">1</span>]), Counter(<span
                class="hljs-string">"AAABBCCAC"</span>).most_common())))
<span class="copy-code-btn">复制代码</span></code></pre>
    <h2 class="heading" data-id="heading-71">62 Python中类方法、类实例方法、静态方法有何区别？</h2>
    <p>类方法: 是类对象的方法，在定义时需要在上方使用 @classmethod 进行装饰,形参为cls，表示类对象，类对象和实例对象都可调用</p>
    <p>类实例方法: 是类实例化对象的方法,只有实例对象可以调用，形参为self,指代对象本身;</p>
    <p>静态方法: 是一个任意函数，在其上方使用 @staticmethod 进行装饰，可以用对象直接调用，静态方法实际上跟该类没有太大关系</p>
    <h2 class="heading" data-id="heading-72">63 遍历一个object的所有属性，并print每一个属性名？</h2>
    <pre><code class="hljs python copyable" lang="python"><span class="hljs-class"><span
            class="hljs-keyword">class</span> <span class="hljs-title">Car</span>:</span>
    <span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">__init__</span><span
            class="hljs-params">(self,name,loss)</span>:</span> <span class="hljs-comment"># loss [价格，油耗，公里数]</span>
        self.name = name
        self.loss = loss
    
    <span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">getName</span><span
            class="hljs-params">(self)</span>:</span>
        <span class="hljs-keyword">return</span> self.name
    
    <span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">getPrice</span><span
            class="hljs-params">(self)</span>:</span>
        <span class="hljs-comment"># 获取汽车价格</span>
        <span class="hljs-keyword">return</span> self.loss[<span class="hljs-number">0</span>]
    
    <span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">getLoss</span><span
            class="hljs-params">(self)</span>:</span>
        <span class="hljs-comment"># 获取汽车损耗值</span>
        <span class="hljs-keyword">return</span> self.loss[<span class="hljs-number">1</span>] * self.loss[<span
                class="hljs-number">2</span>]

Bmw = Car(<span class="hljs-string">"宝马"</span>,[<span class="hljs-number">60</span>,<span class="hljs-number">9</span>,<span
                class="hljs-number">500</span>]) <span class="hljs-comment"># 实例化一个宝马车对象</span>
print(getattr(Bmw,<span class="hljs-string">"name"</span>)) <span class="hljs-comment"># 使用getattr()传入对象名字,属性值。</span>
print(dir(Bmw)) <span class="hljs-comment"># 获Bmw所有的属性和方法</span>
<span class="copy-code-btn">复制代码</span></code></pre>
    <h2 class="heading" data-id="heading-73">64 写一个类，并让它尽可能多的支持操作符?</h2>
    <pre><code class="hljs python copyable" lang="python"><span class="hljs-class"><span
            class="hljs-keyword">class</span> <span class="hljs-title">Array</span>:</span>
    __list = []
    
    <span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">__init__</span><span
            class="hljs-params">(self)</span>:</span>
        <span class="hljs-keyword">print</span> <span class="hljs-string">"constructor"</span>
    
    <span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">__del__</span><span
            class="hljs-params">(self)</span>:</span>
        <span class="hljs-keyword">print</span> <span class="hljs-string">"destruct"</span>
    
    <span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">__str__</span><span
            class="hljs-params">(self)</span>:</span>
        <span class="hljs-keyword">return</span> <span class="hljs-string">"this self-defined array class"</span>

    <span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">__getitem__</span><span
            class="hljs-params">(self,key)</span>:</span>
        <span class="hljs-keyword">return</span> self.__list[key]
    
    <span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">__len__</span><span
            class="hljs-params">(self)</span>:</span>
        <span class="hljs-keyword">return</span> len(self.__list)

    <span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">Add</span><span
            class="hljs-params">(self,value)</span>:</span>
        self.__list.append(value)
    
    <span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">Remove</span><span
            class="hljs-params">(self,index)</span>:</span>
        <span class="hljs-keyword">del</span> self.__list[index]
    
    <span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">DisplayItems</span><span
            class="hljs-params">(self)</span>:</span>
        <span class="hljs-keyword">print</span> <span class="hljs-string">"show all items---"</span>
        <span class="hljs-keyword">for</span> item <span class="hljs-keyword">in</span> self.__list:
            <span class="hljs-keyword">print</span> item
    
        
<span class="copy-code-btn">复制代码</span></code></pre>
    <h2 class="heading" data-id="heading-74">65 关于Python内存管理,下列说法错误的是 B</h2>
    <p>A,变量不必事先声明 B,变量无须先创建和赋值而直接使用</p>
    <p>C,变量无须指定类型 D,可以使用del释放资源</p>
    <h2 class="heading" data-id="heading-75">66 Python的内存管理机制及调优手段？</h2>
    <p>内存管理机制: 引用计数、垃圾回收、内存池</p>
    <p>引用计数：引用计数是一种非常高效的内存管理手段，当一个Python对象被引用时其引用计数增加1,</p>
    <p>当其不再被一个变量引用时则计数减1,当引用计数等于0时对象被删除。弱引用不会增加引用计数</p>
    <p>垃圾回收：</p>
    <p>1.引用计数</p>
    <p>
        引用计数也是一种垃圾收集机制，而且也是一种最直观、最简单的垃圾收集技术。当Python的某个对象的引用计数降为0时，说明没有任何引用指向该对象，该对象就成为要被回收的垃圾了。比如某个新建对象，它被分配给某个引用，对象的引用计数变为1，如果引用被删除，对象的引用计数为0,那么该对象就可以被垃圾回收。不过如果出现循环引用的话，引用计数机制就不再起有效的作用了。</p>
    <p>2.标记清除</p>
    <p>调优手段</p>
    <p>1.手动垃圾回收</p>
    <p>2.调高垃圾回收阈值</p>
    <p>3.避免循环引用</p>
    <h2 class="heading" data-id="heading-76">67 内存泄露是什么？如何避免？</h2>
    <p><strong>内存泄漏</strong>指由于疏忽或错误造成程序未能释放已经不再使用的内存。内存泄漏并非指内存在物理上的消失，而是应用程序分配某段内存后，由于设计错误，导致在释放该段内存之前就失去了对该段内存的控制，从而造成了内存的浪费。
    </p>
    <p>有<code>__del__()</code>函数的对象间的循环引用是导致内存泄露的主凶。不使用一个对象时使用: del object 来删除一个对象的引用计数就可以有效防止内存泄露问题。</p>
    <p>通过Python扩展模块gc 来查看不能回收的对象的详细信息。</p>
    <p>可以通过 sys.getrefcount(obj) 来获取对象的引用计数，并根据返回值是否为0来判断是否内存泄露</p>
    <h2 class="heading" data-id="heading-77">68 python常见的列表推导式？</h2>
    <p>[表达式 for 变量 in 列表] 或者 [表达式 for 变量 in 列表 if 条件]</p>
    <h2 class="heading" data-id="heading-78">69 简述read、readline、readlines的区别？</h2>
    <p>read 读取整个文件</p>
    <p>readline 读取下一行</p>
    <p>readlines 读取整个文件到一个迭代器以供我们遍历</p>
    <h2 class="heading" data-id="heading-79">70 什么是Hash（散列函数）？</h2>
    <p><strong>散列函数</strong>（英语：Hash function）又称<strong>散列算法</strong>、<strong>哈希函数</strong>，是一种从任何一种数据中创建小的数字“指纹”的方法。散列函数把消息或数据压缩成摘要，使得数据量变小，将数据的格式固定下来。该函数将数据打乱混合，重新创建一个叫做<strong>散列值</strong>（hash
        values，hash codes，hash sums，或hashes）的指纹。散列值通常用一个短的随机字母和数字组成的字符串来代表</p>
    <h2 class="heading" data-id="heading-80">71 python函数重载机制？</h2>
    <p>函数重载主要是为了解决两个问题。
        1。可变参数类型。
        2。可变参数个数。</p>
    <p>另外，一个基本的设计原则是，仅仅当两个函数除了参数类型和参数个数不同以外，其功能是完全相同的，此时才使用函数重载，如果两个函数的功能其实不同，那么不应当使用重载，而应当使用一个名字不同的函数。</p>
    <p>好吧，那么对于情况 1 ，函数功能相同，但是参数类型不同，python 如何处理？答案是根本不需要处理，因为 python 可以接受任何类型的参数，如果函数的功能相同，那么不同的参数类型在 python
        中很可能是相同的代码，没有必要做成两个不同函数。</p>
    <p>那么对于情况 2 ，函数功能相同，但参数个数不同，python 如何处理？大家知道，答案就是缺省参数。对那些缺少的参数设定为缺省参数即可解决问题。因为你假设函数功能相同，那么那些缺少的参数终归是需要用的。</p>
    <p>好了，鉴于情况 1 跟 情况 2 都有了解决方案，python 自然就不需要函数重载了。</p>
    <h2 class="heading" data-id="heading-81">72 手写一个判断时间的装饰器</h2>
    <pre><code class="hljs python copyable" lang="python"><span class="hljs-keyword">import</span> datetime


<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">TimeException</span><span
        class="hljs-params">(Exception)</span>:</span>
    <span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">__init__</span><span
            class="hljs-params">(self, exception_info)</span>:</span>
        super().__init__()
        self.info = exception_info

    <span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">__str__</span><span
            class="hljs-params">(self)</span>:</span>
        <span class="hljs-keyword">return</span> self.info


<span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">timecheck</span><span
        class="hljs-params">(func)</span>:</span>
    <span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">wrapper</span><span
            class="hljs-params">(*args, **kwargs)</span>:</span>
        <span class="hljs-keyword">if</span> datetime.datetime.now().year == <span class="hljs-number">2019</span>:
            func(*args, **kwargs)
        <span class="hljs-keyword">else</span>:
            <span class="hljs-keyword">raise</span> TimeException(<span class="hljs-string">"函数已过时"</span>)

    <span class="hljs-keyword">return</span> wrapper


<span class="hljs-meta">@timecheck</span>
<span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">test</span><span
        class="hljs-params">(name)</span>:</span>
    print(<span class="hljs-string">"Hello {}, 2019 Happy"</span>.format(name))


<span class="hljs-keyword">if</span> __name__ == <span class="hljs-string">"__main__"</span>:
    test(<span class="hljs-string">"backbp"</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
    <h2 class="heading" data-id="heading-82">73 使用Python内置的filter()方法来过滤？</h2>
    <pre><code class="hljs python copyable" lang="python">list(filter(<span
            class="hljs-keyword">lambda</span> x: x % <span
            class="hljs-number">2</span> == <span class="hljs-number">0</span>, range(<span
            class="hljs-number">10</span>)))
<span class="copy-code-btn">复制代码</span></code></pre>
    <h2 class="heading" data-id="heading-83">74 编写函数的4个原则</h2>
    <p>1.函数设计要尽量短小</p>
    <p>2.函数声明要做到合理、简单、易于使用</p>
    <p>3.函数参数设计应该考虑向下兼容</p>
    <p>4.一个函数只做一件事情，尽量保证函数语句粒度的一致性</p>
    <h2 class="heading" data-id="heading-84">75 函数调用参数的传递方式是值传递还是引用传递？</h2>
    <p>Python的参数传递有：位置参数、默认参数、可变参数、关键字参数。</p>
    <p>函数的传值到底是值传递还是引用传递、要分情况：</p>
    <p>不可变参数用值传递：像整数和字符串这样的不可变对象，是通过拷贝进行传递的，因为你无论如何都不可能在原处改变不可变对象。</p>
    <p>可变参数是引用传递：比如像列表，字典这样的对象是通过引用传递、和C语言里面的用指针传递数组很相似，可变对象能在函数内部改变。</p>
    <h2 class="heading" data-id="heading-85">76 如何在function里面设置一个全局变量</h2>
    <pre><code class="hljs python copyable" lang="python">globals() <span
            class="hljs-comment"># 返回包含当前作用余全局变量的字典。</span>
<span class="hljs-keyword">global</span> 变量 设置使用全局变量
<span class="copy-code-btn">复制代码</span></code></pre>
    <h2 class="heading" data-id="heading-86">77 对缺省参数的理解 ？</h2>
    <p>缺省参数指在调用函数的时候没有传入参数的情况下，调用默认的参数，在调用函数的同时赋值时，所传入的参数会替代默认参数。</p>
    <p>*args是不定长参数，它可以表示输入参数是不确定的，可以是任意多个。</p>
    <p>**kwargs是关键字参数，赋值的时候是以键值对的方式，参数可以是任意多对在定义函数的时候</p>
    <p>不确定会有多少参数会传入时，就可以使用两个参数</p>
    <h2 class="heading" data-id="heading-87">78 带参数的装饰器?</h2>
    <p>带定长参数的装饰器</p>
    <pre><code class="hljs python copyable" lang="python"><span class="hljs-function"><span
            class="hljs-keyword">def</span> <span class="hljs-title">new_func</span><span
            class="hljs-params">(func)</span>:</span>
    <span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">wrappedfun</span><span
            class="hljs-params">(username, passwd)</span>:</span>
        <span class="hljs-keyword">if</span> username == <span class="hljs-string">'root'</span> <span
                class="hljs-keyword">and</span> passwd == <span class="hljs-string">'123456789'</span>:
            print(<span class="hljs-string">'通过认证'</span>)
            print(<span class="hljs-string">'开始执行附加功能'</span>)
            <span class="hljs-keyword">return</span> func()
       	<span class="hljs-keyword">else</span>:
            print(<span class="hljs-string">'用户名或密码错误'</span>)
            <span class="hljs-keyword">return</span>
    <span class="hljs-keyword">return</span> wrappedfun

<span class="hljs-meta">@new_func</span>
<span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">origin</span><span
        class="hljs-params">()</span>:</span>
    print(<span class="hljs-string">'开始执行函数'</span>)
origin(<span class="hljs-string">'root'</span>,<span class="hljs-string">'123456789'</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
    <p>带不定长参数的装饰器</p>
    <pre><code class="hljs python copyable" lang="python"><span class="hljs-function"><span
            class="hljs-keyword">def</span> <span class="hljs-title">new_func</span><span
            class="hljs-params">(func)</span>:</span>
    <span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">wrappedfun</span><span
            class="hljs-params">(*parts)</span>:</span>
        <span class="hljs-keyword">if</span> parts:
            counts = len(parts)
            print(<span class="hljs-string">'本系统包含 '</span>, end=<span class="hljs-string">''</span>)
            <span class="hljs-keyword">for</span> part <span class="hljs-keyword">in</span> parts:
                print(part, <span class="hljs-string">' '</span>,end=<span class="hljs-string">''</span>)
            print(<span class="hljs-string">'等'</span>, counts, <span class="hljs-string">'部分'</span>)
            <span class="hljs-keyword">return</span> func()
        <span class="hljs-keyword">else</span>:
            print(<span class="hljs-string">'用户名或密码错误'</span>)
            <span class="hljs-keyword">return</span> func()
   <span class="hljs-keyword">return</span> wrappedfun

<span class="copy-code-btn">复制代码</span></code></pre>
    <h2 class="heading" data-id="heading-88">79 为什么函数名字可以当做参数用?</h2>
    <p>Python中一切皆对象，函数名是函数在内存中的空间，也是一个对象</p>
    <h2 class="heading" data-id="heading-89">80 Python中pass语句的作用是什么？</h2>
    <p>在编写代码时只写框架思路，具体实现还未编写就可以用pass进行占位，是程序不报错，不会进行任何操作。</p>
    <h2 class="heading" data-id="heading-90">81 有这样一段代码，print c会输出什么，为什么？</h2>
    <pre><code class="hljs python copyable" lang="python">a = <span class="hljs-number">10</span>
b = <span class="hljs-number">20</span>
c = [a]
a = <span class="hljs-number">15</span>
<span class="copy-code-btn">复制代码</span></code></pre>
    <p>答：10对于字符串，数字，传递是相应的值</p>
    <h2 class="heading" data-id="heading-91">82 交换两个变量的值？</h2>
    <pre><code class="hljs python copyable" lang="python">a, b = b, a
<span class="copy-code-btn">复制代码</span></code></pre>
    <h2 class="heading" data-id="heading-92">83 map函数和reduce函数？</h2>
    <pre><code class="hljs python copyable" lang="python">map(<span
            class="hljs-keyword">lambda</span> x: x * x, [<span class="hljs-number">1</span>, <span
            class="hljs-number">2</span>, <span class="hljs-number">3</span>, <span
            class="hljs-number">4</span>])   <span
            class="hljs-comment"># 使用 lambda</span>
<span class="hljs-comment"># [1, 4, 9, 16]</span>
reduce(<span class="hljs-keyword">lambda</span> x, y: x * y, [<span class="hljs-number">1</span>, <span
                class="hljs-number">2</span>, <span class="hljs-number">3</span>, <span class="hljs-number">4</span>])  <span
                class="hljs-comment"># 相当于 ((1 * 2) * 3) * 4</span>
<span class="hljs-comment"># 24</span>
<span class="copy-code-btn">复制代码</span></code></pre>
    <h2 class="heading" data-id="heading-93">84 回调函数，如何通信的?</h2>
    <p>回调函数是把函数的指针(地址)作为参数传递给另一个函数，将整个函数当作一个对象，赋值给调用的函数。</p>
    <h2 class="heading" data-id="heading-94">85 Python主要的内置数据类型都有哪些？ print dir( ‘a ’) 的输出？</h2>
    <p>内建类型：布尔类型，数字，字符串，列表，元组，字典，集合</p>
    <p>输出字符串'a'的内建方法</p>
    <h2 class="heading" data-id="heading-95">86 map(lambda x:xx，[y for y in range(3)])的输出？</h2>
    <pre><code class="hljs python copyable" lang="python">[<span class="hljs-number">0</span>, <span
            class="hljs-number">1</span>, <span class="hljs-number">4</span>]
<span class="copy-code-btn">复制代码</span></code></pre>
    <h2 class="heading" data-id="heading-96">87 hasattr() getattr() setattr() 函数使用详解？</h2>
    <p>hasattr(object,name)函数:</p>
    <p>判断一个对象里面是否有name属性或者name方法，返回bool值，有name属性（方法）返回True，否则返回False。</p>
    <pre><code class="hljs python copyable" lang="python"><span class="hljs-class"><span
            class="hljs-keyword">class</span> <span class="hljs-title">function_demo</span><span
            class="hljs-params">(object)</span>:</span>
    name = <span class="hljs-string">'demo'</span>
    <span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">run</span><span
            class="hljs-params">(self)</span>:</span>
        <span class="hljs-keyword">return</span> <span class="hljs-string">"hello function"</span>
functiondemo = function_demo()
res = hasattr(functiondemo, <span class="hljs-string">"name"</span>) <span
                class="hljs-comment"># 判断对象是否有name属性，True</span>
res = hasattr(functiondemo, <span class="hljs-string">"run"</span>) <span
                class="hljs-comment"># 判断对象是否有run方法，True</span>
res = hasattr(functiondemo, <span class="hljs-string">"age"</span>) <span
                class="hljs-comment"># 判断对象是否有age属性，False</span>
print(res)
<span class="copy-code-btn">复制代码</span></code></pre>
    <p>getattr(object, name[,default])函数：</p>
    <p>获取对象object的属性或者方法，如果存在则打印出来，如果不存在，打印默认值，默认值可选。注意：如果返回的是对象的方法，则打印结果是：方法的内存地址，如果需要运行这个方法，可以在后面添加括号().</p>
    <pre><code class="hljs python copyable" lang="python">functiondemo = function_demo()
getattr(functiondemo, <span class="hljs-string">"name"</span>)<span
                class="hljs-comment"># 获取name属性，存在就打印出来 --- demo</span>
getattr(functiondemo, <span class="hljs-string">"run"</span>) <span class="hljs-comment"># 获取run 方法，存在打印出方法的内存地址</span>
getattr(functiondemo, <span class="hljs-string">"age"</span>) <span class="hljs-comment"># 获取不存在的属性，报错</span>
getattr(functiondemo, <span class="hljs-string">"age"</span>, <span class="hljs-number">18</span>)<span
                class="hljs-comment"># 获取不存在的属性，返回一个默认值</span>
<span class="copy-code-btn">复制代码</span></code></pre>
    <p>setattr(object, name, values)函数：</p>
    <p>给对象的属性赋值，若属性不存在，先创建再赋值</p>
    <pre><code class="hljs python copyable" lang="python"><span class="hljs-class"><span
            class="hljs-keyword">class</span> <span class="hljs-title">function_demo</span><span
            class="hljs-params">(object)</span>:</span>
    name = <span class="hljs-string">"demo"</span>
    <span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">run</span><span
            class="hljs-params">(self)</span>:</span>
        <span class="hljs-keyword">return</span> <span class="hljs-string">"hello function"</span>
functiondemo = function_demo()
res = hasattr(functiondemo, <span class="hljs-string">"age"</span>) <span
                class="hljs-comment"># 判断age属性是否存在，False</span>
print(res)
setattr(functiondemo, <span class="hljs-string">"age"</span>, <span class="hljs-number">18</span>) <span
                class="hljs-comment"># 对age属性进行赋值，无返回值</span>
res1 = hasattr(functiondemo, <span class="hljs-string">"age"</span>) <span class="hljs-comment"># 再次判断属性是否存在，True</span>
<span class="copy-code-btn">复制代码</span></code></pre>
    <p>综合使用</p>
    <pre><code class="hljs python copyable" lang="python"><span class="hljs-class"><span
            class="hljs-keyword">class</span> <span class="hljs-title">function_demo</span><span
            class="hljs-params">(object)</span>:</span>
    name = <span class="hljs-string">"demo"</span>
    <span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">run</span><span
            class="hljs-params">(self)</span>:</span>
        <span class="hljs-keyword">return</span> <span class="hljs-string">"hello function"</span>
functiondemo = function_demo()
res = hasattr(functiondemo, <span class="hljs-string">"addr"</span>) <span class="hljs-comment"># 先判断是否存在</span>
<span class="hljs-keyword">if</span> res:
    addr = getattr(functiondemo, <span class="hljs-string">"addr"</span>)
    print(addr)
<span class="hljs-keyword">else</span>:
    addr = getattr(functiondemo, <span class="hljs-string">"addr"</span>, setattr(functiondemo, <span
                class="hljs-string">"addr"</span>, <span class="hljs-string">"北京首都"</span>))
    print(addr)
<span class="copy-code-btn">复制代码</span></code></pre>
    <h2 class="heading" data-id="heading-97">88 一句话解决阶乘函数？</h2>
    <pre><code class="hljs python copyable" lang="python">reduce(<span class="hljs-keyword">lambda</span> x,y : x*y,range(<span
            class="hljs-number">1</span>,n+<span class="hljs-number">1</span>))
<span class="copy-code-btn">复制代码</span></code></pre>
    <h2 class="heading" data-id="heading-98">89 对设计模式的理解，简述你了解的设计模式？</h2>
    <p>设计模式是经过总结，优化的，对我们经常会碰到的一些编程问题的可重用解决方案。一个设计模式并不像一个类或一个库那样能够直接作用于我们的代码，反之，设计模式更为高级，它是一种必须在特定情形下实现的一种方法模板。
        常见的是工厂模式和单例模式</p>
    <h2 class="heading" data-id="heading-99">90 请手写一个单例</h2>
    <pre><code class="hljs python copyable" lang="python"><span class="hljs-comment">#python2</span>
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">A</span><span
        class="hljs-params">(object)</span>:</span>
    __instance = <span class="hljs-keyword">None</span>
    <span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">__new__</span><span
            class="hljs-params">(cls,*args,**kwargs)</span>:</span>
        <span class="hljs-keyword">if</span> cls.__instance <span class="hljs-keyword">is</span> <span
                class="hljs-keyword">None</span>:
            cls.__instance = objecet.__new__(cls)
            <span class="hljs-keyword">return</span> cls.__instance
        <span class="hljs-keyword">else</span>:
            <span class="hljs-keyword">return</span> cls.__instance
<span class="copy-code-btn">复制代码</span></code></pre>
    <h2 class="heading" data-id="heading-100">91 单例模式的应用场景有那些？</h2>
    <p>单例模式应用的场景一般发现在以下条件下：
        资源共享的情况下，避免由于资源操作时导致的性能或损耗等，如日志文件，应用配置。
        控制资源的情况下，方便资源之间的互相通信。如线程池等，1,网站的计数器 2,应用配置 3.多线程池 4数据库配置 数据库连接池 5.应用程序的日志应用...</p>
    <h2 class="heading" data-id="heading-101">92 用一行代码生成[1,4,9,16,25,36,49,64,81,100]</h2>
    <pre><code class="hljs python copyable" lang="python">print([x*x <span class="hljs-keyword">for</span> x <span
            class="hljs-keyword">in</span> range(<span class="hljs-number">1</span>, <span
            class="hljs-number">11</span>)])
<span class="copy-code-btn">复制代码</span></code></pre>
    <h2 class="heading" data-id="heading-102">93 对装饰器的理解，并写出一个计时器记录方法执行性能的装饰器？</h2>
    <p>装饰器本质上是一个callable object ，它可以让其他函数在不需要做任何代码变动的前提下增加额外功能，装饰器的返回值也是一个函数对象。</p>
    <pre><code class="hljs python copyable" lang="python"><span class="hljs-keyword">import</span> time
<span class="hljs-keyword">from</span> functools <span class="hljs-keyword">import</span> wraps

<span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">timeit</span><span
        class="hljs-params">(func)</span>:</span>
<span class="hljs-meta">    @wraps(func)</span>
    <span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">wrapper</span><span
            class="hljs-params">(*args, **kwargs)</span>:</span>
        start = time.clock()
        ret = func(*args, **kwargs)
        end = time.clock()
        print(<span class="hljs-string">'used:'</span>,end-start)
        <span class="hljs-keyword">return</span> ret
    
    <span class="hljs-keyword">return</span> wrapper
<span class="hljs-meta">@timeit</span>
<span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">foo</span><span
        class="hljs-params">()</span>:</span>
    print(<span class="hljs-string">'in foo()'</span>foo())
<span class="copy-code-btn">复制代码</span></code></pre>
    <h2 class="heading" data-id="heading-103">94 解释以下什么是闭包？</h2>
    <p>在函数内部再定义一个函数，并且这个函数用到了外边函数的变量，那么将这个函数以及用到的一些变量称之为闭包。</p>
    <h2 class="heading" data-id="heading-104">95 函数装饰器有什么作用？</h2>
    <p>装饰器本质上是一个callable
        object，它可以在让其他函数在不需要做任何代码的变动的前提下增加额外的功能。装饰器的返回值也是一个函数的对象，它经常用于有切面需求的场景。比如：插入日志，性能测试，事务处理，缓存。权限的校验等场景，有了装饰器就可以抽离出大量的与函数功能本身无关的雷同代码并发并继续使用。
        详细参考：<a target="_blank" href="https://manjusaka.itscoder.com/2018/02/23/something-about-decorator/"
                rel="nofollow noopener noreferrer">manjusaka.itscoder.com/2018/02/23/…</a></p>
    <h2 class="heading" data-id="heading-105">96 生成器，迭代器的区别？</h2>
    <p>迭代器是遵循迭代协议的对象。用户可以使用 iter() 以从任何序列得到迭代器（如 list, tuple, dictionary, set 等）。另一个方法则是创建一个另一种形式的迭代器 —— generator
        。要获取下一个元素，则使用成员函数 next()（Python 2）或函数 next() function （Python 3） 。当没有元素时，则引发 StopIteration
        此例外。若要实现自己的迭代器，则只要实现 next()（Python 2）或 <code>__next__</code>()（ Python 3）</p>
    <p>生成器（Generator），只是在需要返回数据的时候使用yield语句。每次next()被调用时，生成器会返回它脱离的位置（它记忆语句最后一次执行的位置和所有的数据值）</p>
    <p>区别：
        生成器能做到迭代器能做的所有事，而且因为自动创建iter()和next()方法，生成器显得特别简洁，而且生成器也是高效的，使用生成器表达式取代列表解析可以同时节省内存。除了创建和保存程序状态的自动方法，当发生器终结时，还会自动抛出StopIteration异常。</p>
    <h2 class="heading" data-id="heading-106">97 X是什么类型?</h2>
    <p>X= (i for i in range(10))
        X是 generator类型</p>
    <h2 class="heading" data-id="heading-107">98 请用一行代码 实现将1-N 的整数列表以3为单位分组</h2>
    <pre><code class="hljs python copyable" lang="python">N =<span class="hljs-number">100</span>
<span class="hljs-keyword">print</span> ([[x <span class="hljs-keyword">for</span> x <span
                class="hljs-keyword">in</span> range(<span class="hljs-number">1</span>,<span
                class="hljs-number">100</span>)] [i:i+<span
                class="hljs-number">3</span>] <span class="hljs-keyword">for</span> i <span
                class="hljs-keyword">in</span> range(<span class="hljs-number">0</span>,<span
                class="hljs-number">100</span>,<span
                class="hljs-number">3</span>)])
<span class="copy-code-btn">复制代码</span></code></pre>
    <h2 class="heading" data-id="heading-108">99 Python中yield的用法?</h2>
    <p>
        yield就是保存当前程序执行状态。你用for循环的时候，每次取一个元素的时候就会计算一次。用yield的函数叫generator,和iterator一样，它的好处是不用一次计算所有元素，而是用一次算一次，可以节省很多空间，generator每次计算需要上一次计算结果，所以用yield,否则一return，上次计算结果就没了</p>
</div>
