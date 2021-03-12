---
title: "(无头的浏览器)是什么鬼?"
date:       2019-12-05
subtitle: "用Python驱动Headless Chrome"
tags:
	- Python
	- background
	- solution
---


原文链接:https://www.jianshu.com/p/11d519e2d0cb


<h1 class="_1RuRku">用Python驱动Headless Chrome</h1>

<article class="_2rhmJa">
    <div class="image-package">
        <div class="image-container" style="max-width: 650px; max-height: 453px; background-color: transparent;">
            <div class="image-container-fill" style="padding-bottom: 69.69%;"></div>
            <div class="image-view" data-width="650" data-height="453"><img
                    data-original-src="//upload-images.jianshu.io/upload_images/618241-fbc4471c5a9bfcf2.png"
                    data-original-width="650" data-original-height="453" data-original-format="image/png"
                    data-original-filesize="163264" data-image-index="0" style="cursor: zoom-in;" class=""
                    src="//upload-images.jianshu.io/upload_images/618241-fbc4471c5a9bfcf2.png?imageMogr2/auto-orient/strip|imageView2/2/w/650/format/webp">
            </div>
        </div>
        <div class="image-caption">headless chrome.png</div>
    </div>
    <blockquote>
        <p>Headless Browser(无头的浏览器)是什么鬼?</p>
    </blockquote>
    <p>简而言之，Headless Browser是没有图形用户界面(GUI)的web浏览器，通常是通过编程或命令行界面来控制的。</p>
    <p>Headless Browser的许多用处之一是自动化可用性测试或测试浏览器交互。如果您正在尝试检查页面在不同的浏览器中呈现的方式，或者确认页面元素在用户启动某个工作流之后出现，那么使用Headless
        Browser可以提供大量的帮助。除此之外，如果内容是动态呈现的(比如通过Javascript)，web抓取等传统的面向web的任务就很难做了。使用Headless
        Browser可以方便地访问这些内容，因为内容的呈现方式与完全浏览器中的内容完全相同。</p>
    <p>基于不同的浏览器，有不同的浏览器引擎。(<a
            href="https://link.jianshu.com?t=http%3A%2F%2Fwww.cnblogs.com%2Fwangjunqiao%2Fp%2F5212561.html"
            target="_blank" rel="nofollow">http://www.cnblogs.com/wangjunqiao/p/5212561.html</a>)</p>
    <p><em>主流浏览器所使用的内核分类</em></p>
    <p>Trident内核：IE,MaxThon,TT,The World,360,搜狗浏览器等<br>
        Gecko内核：Netscape6及以上版本，FF,MozillaSuite/SeaMonkey等<br>
        Presto内核：Opera7及以上<br>
        Webkit内核：Safari,Chrome等</p>
    <p>先让我们看看浏览器处理过程中的每一个步骤：</p>
    <p>1.处理HTML脚本，生成DOM树<br>
        2.处理CSS脚本，生成CSSOM树 （DOM和CSSOM是独立的数据结构）<br>
        3.将DOM树和CSSOM树合并为渲染树<br>
        4.对渲染树中的内容进行布局，计算每个节点的几何外观<br>
        5.将渲染树中的每个节点绘制到屏幕中</p>
    <p>Headless Browser实际就是节约了第4,5步的时间。</p>
    <p>3年前，无头浏览器 PhantomJS 已经如火如荼出现了，紧跟着 NightmareJS
        也成为一名巨星。无头浏览器带来巨大便利性：页面爬虫、自动化测试、WebAutomation...用过PhantomJS的都知道，它的环境是运行在一个封闭的沙盒里面，在环境内外完全不可通信，包括API、变量、全局方法调用等。</p>
    <p><strong>Headless Chrome和Python</strong><br>
        在发布Headless Chrome之前，当你需要自动化浏览器的时候随时都有可能涉及多个窗口或标签，你必须担心CPU和/或内存的使用。这两种方式都与必须从被请求的URL中显示显示的图形的浏览器相关联。</p>
    <p>当使用一个无头的浏览器时，我们不用担心这个。因此，我们可以预期我们编写的脚本的内存开销会降低，执行速度也会更快。<br>
        而Chrome从59版本开始 推出了 headless mode（当时仅支持Mac和Linux），而目前最新的Chrome63版已经开始在windows上支持headless mode。</p>
    <p><strong>安装Headless Chrome 在windows</strong><br>
        Selenium操作chrome浏览器需要有ChromeDriver驱动来协助。<br>
        什么是ChromeDriver？</p>
    <p>ChromeDriver是Chromium
        team开发维护的，它是实现WebDriver有线协议的一个单独的服务。ChromeDriver通过chrome的自动代理框架控制浏览器，建议从以下地址直接下载最新的版本：<strong><a
                href="https://link.jianshu.com?t=https%3A%2F%2Fchromedriver.storage.googleapis.com%2Findex.html%3Fpath%3D2.34%2F"
                target="_blank" rel="nofollow">ChromeDriver 2.34</a></strong><br>
        它才可以支持Chrome v61-63。<br>
        可以将此driver放置于：C:\Program Files\Google\Chrome\Application\ （对应的Chrome安装目录下）</p>
    <p><strong>安装Selenium 在windows</strong><br>
        cmd命令里面运行：<br>
        $pip install selenium</p>
    <p><strong>编写对应的脚本</strong><br>
        编写一个对应的百度搜索的脚本</p>
    <div class="_2Uzcx_">
        <button class="VJbwyy" type="button" aria-label="复制代码"><i aria-label="icon: copy"
                                                                  class="anticon anticon-copy">
            <svg viewBox="64 64 896 896" focusable="false" class="" data-icon="copy" width="1em" height="1em"
                 fill="currentColor" aria-hidden="true">
                <path d="M832 64H296c-4.4 0-8 3.6-8 8v56c0 4.4 3.6 8 8 8h496v688c0 4.4 3.6 8 8 8h56c4.4 0 8-3.6 8-8V96c0-17.7-14.3-32-32-32zM704 192H192c-17.7 0-32 14.3-32 32v530.7c0 8.5 3.4 16.6 9.4 22.6l173.3 173.3c2.2 2.2 4.7 4 7.4 5.5v1.9h4.2c3.5 1.3 7.2 2 11 2H704c17.7 0 32-14.3 32-32V224c0-17.7-14.3-32-32-32zM350 856.2L263.9 770H350v86.2zM664 888H414V746c0-22.1-17.9-40-40-40H232V264h432v624z"></path>
            </svg>
        </i></button>
        <pre class="line-numbers  language-python"><code class="  language-python"><span
                class="token keyword">import</span> os
<span class="token keyword">from</span> selenium <span class="token keyword">import</span> webdriver
<span class="token keyword">from</span> selenium<span class="token punctuation">.</span>webdriver<span
                    class="token punctuation">.</span>common<span class="token punctuation">.</span>keys <span
                    class="token keyword">import</span> Keys
<span class="token keyword">from</span> selenium<span class="token punctuation">.</span>webdriver<span
                    class="token punctuation">.</span>chrome<span class="token punctuation">.</span>options <span
                    class="token keyword">import</span> Options
<span class="token keyword">import</span> time

chrome_options <span class="token operator">=</span> Options<span class="token punctuation">(</span><span
                    class="token punctuation">)</span>
chrome_options<span class="token punctuation">.</span>add_argument<span class="token punctuation">(</span><span
                    class="token string">"--headless"</span><span class="token punctuation">)</span>

base_url <span class="token operator">=</span> <span class="token string">"http://www.baidu.com/"</span>
<span class="token comment">#对应的chromedriver的放置目录</span>
driver <span class="token operator">=</span> webdriver<span class="token punctuation">.</span>Chrome<span
                    class="token punctuation">(</span>executable_path<span class="token operator">=</span><span
                    class="token punctuation">(</span><span class="token string">r'C:\Program Files\Google\Chrome\Application\chromedriver.exe'</span><span
                    class="token punctuation">)</span><span class="token punctuation">,</span> chrome_options<span
                    class="token operator">=</span>chrome_options<span class="token punctuation">)</span>

driver<span class="token punctuation">.</span>get<span class="token punctuation">(</span>base_url <span
                    class="token operator">+</span> <span class="token string">"/"</span><span
                    class="token punctuation">)</span>

start_time<span class="token operator">=</span>time<span class="token punctuation">.</span>time<span
                    class="token punctuation">(</span><span class="token punctuation">)</span>
<span class="token keyword">print</span><span class="token punctuation">(</span><span class="token string">'this is start_time '</span><span
                    class="token punctuation">,</span>start_time<span class="token punctuation">)</span>

driver<span class="token punctuation">.</span>find_element_by_id<span class="token punctuation">(</span><span
                    class="token string">"kw"</span><span class="token punctuation">)</span><span
                    class="token punctuation">.</span>send_keys<span class="token punctuation">(</span><span
                    class="token string">"selenium webdriver"</span><span class="token punctuation">)</span>
driver<span class="token punctuation">.</span>find_element_by_id<span class="token punctuation">(</span><span
                    class="token string">"su"</span><span class="token punctuation">)</span><span
                    class="token punctuation">.</span>click<span class="token punctuation">(</span><span
                    class="token punctuation">)</span>
driver<span class="token punctuation">.</span>save_screenshot<span class="token punctuation">(</span><span
                    class="token string">'screen.png'</span><span class="token punctuation">)</span>

driver<span class="token punctuation">.</span>close<span class="token punctuation">(</span><span
                    class="token punctuation">)</span>

end_time<span class="token operator">=</span>time<span class="token punctuation">.</span>time<span
                    class="token punctuation">(</span><span class="token punctuation">)</span>
<span class="token keyword">print</span><span class="token punctuation">(</span><span class="token string">'this is end_time '</span><span
                    class="token punctuation">,</span>end_time<span class="token punctuation">)</span>
<span aria-hidden="true"
      class="line-numbers-rows"><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span></span></code></pre>
    </div>
    <p>以上的脚本运行完成后，你会在你的当前目录看到一个类似于下面画面的screen.png.</p>
    <br>
    <div class="image-package">
        <div class="image-container" style="max-width: 700px; max-height: 600px; background-color: transparent;">
            <div class="image-container-fill" style="padding-bottom: 75.0%;"></div>
            <div class="image-view" data-width="800" data-height="600"><img
                    data-original-src="//upload-images.jianshu.io/upload_images/618241-e3d8deff450aa43c.png"
                    data-original-width="800" data-original-height="600" data-original-format="image/png"
                    data-original-filesize="73100" data-image-index="1" style="cursor: zoom-in;" class=""
                    src="//upload-images.jianshu.io/upload_images/618241-e3d8deff450aa43c.png?imageMogr2/auto-orient/strip|imageView2/2/w/800/format/webp">
            </div>
        </div>
        <div class="image-caption">screen.png</div>
    </div>
    <p>可以看出上面的写法和直接使用Selenium调用Chrome浏览器的时候极其类似，只是多添加了对chrome_options的重写。</p>
    <p>据运行的试验表明，Headelss 的确比Headed的浏览器在内存消耗，运行时间，CPU占用上面都有一定的优势。</p>
    <div class="image-package">
        <div class="image-container" style="max-width: 700px; max-height: 118px; background-color: transparent;">
            <div class="image-container-fill" style="padding-bottom: 14.499999999999998%;"></div>
            <div class="image-view" data-width="814" data-height="118"><img
                    data-original-src="//upload-images.jianshu.io/upload_images/618241-1a0846f6b318549d.png"
                    data-original-width="814" data-original-height="118" data-original-format="image/png"
                    data-original-filesize="21138" data-image-index="2" style="cursor: zoom-in;" class=""
                    src="//upload-images.jianshu.io/upload_images/618241-1a0846f6b318549d.png?imageMogr2/auto-orient/strip|imageView2/2/w/814/format/webp">
            </div>
        </div>
        <div class="image-caption">headless对比.png</div>
    </div>
    <p>使用Headless Chrome也许能让你的自动化测试运行更快，而且在视觉测试上面也有一定的优势。感兴趣的朋友可以上手试试。</p>
</article>
<div></div>
<div class="_1kCBjS">
    <div class="_18vaTa">
        <div class="_3BUZPB">
            <div class="_2Bo4Th" role="button" tabindex="-1" aria-label="给文章点赞"><i aria-label="ic-like"
                                                                                   class="anticon">
                <svg width="1em" height="1em" fill="currentColor" aria-hidden="true" focusable="false" class="">
                    <use xlink:href="#ic-like"></use>
                </svg>
            </i></div>
            <span class="_1LOh_5" role="button" tabindex="-1" aria-label="查看点赞列表">16人点赞<i aria-label="icon: right"
                                                                                          class="anticon anticon-right"><svg
                    viewBox="64 64 896 896" focusable="false" class="" data-icon="right" width="1em" height="1em"
                    fill="currentColor" aria-hidden="true"><path
                    d="M765.7 486.8L314.9 134.7A7.97 7.97 0 0 0 302 141v77.3c0 4.9 2.3 9.6 6.1 12.6l360 281.1-360 281.1c-3.9 3-6.1 7.7-6.1 12.6V883c0 6.7 7.7 10.4 12.9 6.3l450.8-352.1a31.96 31.96 0 0 0 0-50.4z"></path></svg></i></span>
        </div>
        <div class="_3BUZPB">
            <div class="_2Bo4Th" role="button" tabindex="-1"><i aria-label="ic-dislike" class="anticon">
                <svg width="1em" height="1em" fill="currentColor" aria-hidden="true" focusable="false" class="">
                    <use xlink:href="#ic-dislike"></use>
                </svg>
            </i></div>
        </div>
    </div>
    <div class="_18vaTa"><a class="_3BUZPB _1x1ok9 _1OhGeD" href="/nb/10356021" target="_blank"
                            rel="noopener noreferrer"><i aria-label="ic-notebook" class="anticon">
        <svg width="1em" height="1em" fill="currentColor" aria-hidden="true" focusable="false" class="">
            <use xlink:href="#ic-notebook"></use>
        </svg>
    </i><span>周边工具</span></a>
        <div class="_3BUZPB ant-dropdown-trigger">
            <div class="_2Bo4Th"><i aria-label="ic-others" class="anticon">
                <svg width="1em" height="1em" fill="currentColor" aria-hidden="true" focusable="false" class="">
                    <use xlink:href="#ic-others"></use>
                </svg>
            </i></div>
        </div>
    </div>
</div>
<div class="_19DgIp" style="margin-top:24px;margin-bottom:24px"></div>
<div class="_13lIbp">
    <div class="_191KSt">"想转载的，给杯茶钱呀~~"</div>
    <button type="button" class="_1OyPqC _3Mi9q9 _2WY0RL _1YbC5u"><span>赞赏支持</span></button>
    <span class="_3zdmIj">还没有人赞赏，支持一下</span></div>
<div class="d0hShY"><a class="_1OhGeD" href="/u/42c47cc2c681" target="_blank" rel="noopener noreferrer"><img
        class="_27NmgV"
        src="//upload.jianshu.io/users/upload_avatars/618241/5c425905-46fd-46ac-ba24-192d650f6d33.jpg?imageMogr2/auto-orient/strip|imageView2/1/w/100/h/100/format/webp"
        alt="  "></a>
    <div class="Uz-vZq">
        <div class="Cqpr1X"><a class="HC3FFO _1OhGeD" href="/u/42c47cc2c681" title="CC先生之简书" target="_blank"
                               rel="noopener noreferrer">CC先生之简书</a><span class="_2WEj6j" title="04年入IT坑的老中医/
为学日益 为道日损，损之又损，以至于无为/
一切皆测试">04年入IT坑的老中医/
为学日益 为道日损，损之又损，以至于无为/
一切皆测试</span></div>
        <div class="lJvI3S">
            <span>总资产360 (约33.59元)</span><span>共写了21.3W字</span><span>获得694个赞</span><span>共684个粉丝</span></div>
    </div>
    <button data-locale="zh-CN" type="button" class="_1OyPqC _3Mi9q9"><span>关注</span></button>
</div>