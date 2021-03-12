---
title: "关于curl的使用详解"
cover: "/img/lynk/87.jpg"
date:       2019-12-05
subtitle: "一种发出网络请求的命令行工具"
tags:
	- Python
	- solution
	- web
---

本文转自:https://www.jianshu.com/p/f05bbd5007d9

<div class="image-package">
    <div class="image-container" style="max-width: 441px; max-height: 97px; background-color: transparent;">
        <div class="image-container-fill" style="padding-bottom: 22.0%;"></div>
        <div class="image-view" data-width="441" data-height="97"><img
                data-original-src="//upload-images.jianshu.io/upload_images/2733312-11e482557148c9b5.png"
                data-original-width="441" data-original-height="97" data-original-format="image/png"
                data-original-filesize="12765" data-image-index="0" style="cursor: zoom-in;" class=""
                src="//upload-images.jianshu.io/upload_images/2733312-11e482557148c9b5.png?imageMogr2/auto-orient/strip|imageView2/2/w/441/format/webp">
        </div>
    </div>
    <div class="image-caption"></div>
</div>
<p>curl 是一种命令行工具，作用是发出网络请求，然后获取数据，显示在"标准输出"（stdout）上面。它支持多种协议，下面列举其常用功能。</p>
<h5>一、查看网页源码</h5>
<p>直接在 curl 命令后加上网址，就可以看到网页源码。以网址 <a href="https://link.jianshu.com?t=http://www.sina.com" target="_blank"
                                     rel="nofollow">www.sina.com</a>为例（选择该网址，主要因为它的网页代码较短）。</p>
<div class="_2Uzcx_">
    <button class="VJbwyy" type="button" aria-label="复制代码"><i aria-label="icon: copy" class="anticon anticon-copy">
        <svg viewBox="64 64 896 896" focusable="false" class="" data-icon="copy" width="1em" height="1em"
             fill="currentColor" aria-hidden="true">
            <path d="M832 64H296c-4.4 0-8 3.6-8 8v56c0 4.4 3.6 8 8 8h496v688c0 4.4 3.6 8 8 8h56c4.4 0 8-3.6 8-8V96c0-17.7-14.3-32-32-32zM704 192H192c-17.7 0-32 14.3-32 32v530.7c0 8.5 3.4 16.6 9.4 22.6l173.3 173.3c2.2 2.2 4.7 4 7.4 5.5v1.9h4.2c3.5 1.3 7.2 2 11 2H704c17.7 0 32-14.3 32-32V224c0-17.7-14.3-32-32-32zM350 856.2L263.9 770H350v86.2zM664 888H414V746c0-22.1-17.9-40-40-40H232V264h432v624z"></path>
        </svg>
    </i></button>
    <pre class="line-numbers  language-xml"><code class="  language-xml">$ curl www.sina.com
<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>html</span><span
        class="token punctuation">&gt;</span></span>
<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>head</span><span
        class="token punctuation">&gt;</span></span><span class="token tag"><span class="token tag"><span
                class="token punctuation">&lt;</span>title</span><span class="token punctuation">&gt;</span></span>301 Moved Permanently<span
                class="token tag"><span class="token tag"><span
                class="token punctuation">&lt;/</span>title</span><span
                class="token punctuation">&gt;</span></span><span
                class="token tag"><span class="token tag"><span
                class="token punctuation">&lt;/</span>head</span><span class="token punctuation">&gt;</span></span>
<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>body</span> <span
        class="token attr-name">bgcolor</span><span class="token attr-value"><span
        class="token punctuation">=</span><span class="token punctuation">"</span>white<span
        class="token punctuation">"</span></span><span class="token punctuation">&gt;</span></span>
<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>center</span><span
        class="token punctuation">&gt;</span></span><span class="token tag"><span class="token tag"><span
                class="token punctuation">&lt;</span>h1</span><span class="token punctuation">&gt;</span></span>301 Moved Permanently<span
                class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>h1</span><span
                class="token punctuation">&gt;</span></span><span class="token tag"><span class="token tag"><span
                class="token punctuation">&lt;/</span>center</span><span
                class="token punctuation">&gt;</span></span>
<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>hr</span><span
        class="token punctuation">&gt;</span></span><span class="token tag"><span class="token tag"><span
                class="token punctuation">&lt;</span>center</span><span class="token punctuation">&gt;</span></span>nginx<span
                class="token tag"><span class="token tag"><span
                class="token punctuation">&lt;/</span>center</span><span
                class="token punctuation">&gt;</span></span>
<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>body</span><span
        class="token punctuation">&gt;</span></span>
<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>html</span><span
        class="token punctuation">&gt;</span></span>

<span aria-hidden="true"
      class="line-numbers-rows"><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span></span></code></pre>
</div>
<p>如果要把这个网页保存下来，可以使用 <code>-o</code> 参数：</p>
<div class="_2Uzcx_">
    <button class="VJbwyy" type="button" aria-label="复制代码"><i aria-label="icon: copy" class="anticon anticon-copy">
        <svg viewBox="64 64 896 896" focusable="false" class="" data-icon="copy" width="1em" height="1em"
             fill="currentColor" aria-hidden="true">
            <path d="M832 64H296c-4.4 0-8 3.6-8 8v56c0 4.4 3.6 8 8 8h496v688c0 4.4 3.6 8 8 8h56c4.4 0 8-3.6 8-8V96c0-17.7-14.3-32-32-32zM704 192H192c-17.7 0-32 14.3-32 32v530.7c0 8.5 3.4 16.6 9.4 22.6l173.3 173.3c2.2 2.2 4.7 4 7.4 5.5v1.9h4.2c3.5 1.3 7.2 2 11 2H704c17.7 0 32-14.3 32-32V224c0-17.7-14.3-32-32-32zM350 856.2L263.9 770H350v86.2zM664 888H414V746c0-22.1-17.9-40-40-40H232V264h432v624z"></path>
        </svg>
    </i></button>
    <pre class="line-numbers  language-ruby"><code class="  language-ruby">$ curl <span
            class="token operator">-</span>o <span class="token punctuation">[</span>文件名<span
            class="token punctuation">]</span> www<span class="token punctuation">.</span>sina<span
            class="token punctuation">.</span>com
<span aria-hidden="true" class="line-numbers-rows"><span></span></span></code></pre>
</div>
<h5>二、自动跳转</h5>
<p>有的网址是自动跳转的。使用 <code>-L</code> 参数，curl 就会跳转到新的网址。</p>
<div class="_2Uzcx_">
    <button class="VJbwyy" type="button" aria-label="复制代码"><i aria-label="icon: copy" class="anticon anticon-copy">
        <svg viewBox="64 64 896 896" focusable="false" class="" data-icon="copy" width="1em" height="1em"
             fill="currentColor" aria-hidden="true">
            <path d="M832 64H296c-4.4 0-8 3.6-8 8v56c0 4.4 3.6 8 8 8h496v688c0 4.4 3.6 8 8 8h56c4.4 0 8-3.6 8-8V96c0-17.7-14.3-32-32-32zM704 192H192c-17.7 0-32 14.3-32 32v530.7c0 8.5 3.4 16.6 9.4 22.6l173.3 173.3c2.2 2.2 4.7 4 7.4 5.5v1.9h4.2c3.5 1.3 7.2 2 11 2H704c17.7 0 32-14.3 32-32V224c0-17.7-14.3-32-32-32zM350 856.2L263.9 770H350v86.2zM664 888H414V746c0-22.1-17.9-40-40-40H232V264h432v624z"></path>
        </svg>
    </i></button>
    <pre class="line-numbers  language-ruby"><code class="  language-ruby">$ curl <span
            class="token operator">-</span><span class="token constant">L</span> www<span
            class="token punctuation">.</span>sina<span
            class="token punctuation">.</span>com
<span aria-hidden="true" class="line-numbers-rows"><span></span></span></code></pre>
</div>
<p>键入上面的命令，结果自动跳转为 <a href="https://link.jianshu.com?t=http://www.sina.com.cn" target="_blank" rel="nofollow">www.sina.com.cn</a>。
</p>
<h5>三、显示头信息</h5>
<p><code>-i</code> 参数可以显示 http response 的头信息，连同网页代码一起。<code>-I</code> 参数则只显示 http response 的头信息。</p>
<div class="_2Uzcx_">
    <button class="VJbwyy" type="button" aria-label="复制代码"><i aria-label="icon: copy" class="anticon anticon-copy">
        <svg viewBox="64 64 896 896" focusable="false" class="" data-icon="copy" width="1em" height="1em"
             fill="currentColor" aria-hidden="true">
            <path d="M832 64H296c-4.4 0-8 3.6-8 8v56c0 4.4 3.6 8 8 8h496v688c0 4.4 3.6 8 8 8h56c4.4 0 8-3.6 8-8V96c0-17.7-14.3-32-32-32zM704 192H192c-17.7 0-32 14.3-32 32v530.7c0 8.5 3.4 16.6 9.4 22.6l173.3 173.3c2.2 2.2 4.7 4 7.4 5.5v1.9h4.2c3.5 1.3 7.2 2 11 2H704c17.7 0 32-14.3 32-32V224c0-17.7-14.3-32-32-32zM350 856.2L263.9 770H350v86.2zM664 888H414V746c0-22.1-17.9-40-40-40H232V264h432v624z"></path>
        </svg>
    </i></button>
    <pre class="line-numbers  language-jsx"><code class="  language-jsx">$ curl <span
            class="token operator">-</span>i www<span class="token punctuation">.</span>sina<span
            class="token punctuation">.</span>com
<span class="token constant">HTTP</span><span class="token operator">/</span><span class="token number">1.1</span> <span
                class="token number">301</span> Moved Permanently
Server<span class="token punctuation">:</span> nginx
Date<span class="token punctuation">:</span> Tue<span class="token punctuation">,</span> <span
                class="token number">23</span> Aug <span class="token number">2016</span> <span
                class="token number">08</span><span class="token punctuation">:</span><span
                class="token number">30</span><span class="token punctuation">:</span><span
                class="token number">16</span> <span class="token constant">GMT</span>
Content<span class="token operator">-</span>Type<span class="token punctuation">:</span> text<span
                class="token operator">/</span>html
Location<span class="token punctuation">:</span> http<span class="token punctuation">:</span><span
                class="token operator">/</span><span class="token regex">/www.sina.com.cn/</span>
Expires<span class="token punctuation">:</span> Tue<span class="token punctuation">,</span> <span class="token number">23</span> Aug <span
                class="token number">2016</span> <span class="token number">08</span><span
                class="token punctuation">:</span><span class="token number">32</span><span
                class="token punctuation">:</span><span class="token number">16</span> <span
                class="token constant">GMT</span>
Cache<span class="token operator">-</span>Control<span class="token punctuation">:</span> max<span
                class="token operator">-</span>age<span class="token operator">=</span><span
                class="token number">120</span>
Age<span class="token punctuation">:</span> <span class="token number">102</span>
Content<span class="token operator">-</span>Length<span class="token punctuation">:</span> <span class="token number">178</span>
<span class="token constant">X</span><span class="token operator">-</span>Cache<span class="token punctuation">:</span> <span
                class="token constant">HIT</span> <span class="token keyword">from</span> xd33<span
                class="token operator">-</span><span class="token number">83.</span>sina<span
                class="token punctuation">.</span>com<span class="token punctuation">.</span>cn

<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>html</span><span
        class="token punctuation">&gt;</span></span><span class="token plain-text">
</span><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>head</span><span
                class="token punctuation">&gt;</span></span><span class="token tag"><span class="token tag"><span
                class="token punctuation">&lt;</span>title</span><span
                class="token punctuation">&gt;</span></span><span
                class="token plain-text">301 Moved Permanently</span><span class="token tag"><span
                class="token tag"><span class="token punctuation">&lt;/</span>title</span><span
                class="token punctuation">&gt;</span></span><span class="token tag"><span class="token tag"><span
                class="token punctuation">&lt;/</span>head</span><span
                class="token punctuation">&gt;</span></span><span class="token plain-text">
</span><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>body</span> <span
                class="token attr-name">bgcolor</span><span class="token attr-value"><span
                class="token punctuation">=</span><span class="token punctuation">"</span>white<span
                class="token punctuation">"</span></span><span class="token punctuation">&gt;</span></span><span
                class="token plain-text">
</span><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>center</span><span
                class="token punctuation">&gt;</span></span><span class="token tag"><span class="token tag"><span
                class="token punctuation">&lt;</span>h1</span><span
                class="token punctuation">&gt;</span></span><span
                class="token plain-text">301 Moved Permanently</span><span class="token tag"><span
                class="token tag"><span class="token punctuation">&lt;/</span>h1</span><span
                class="token punctuation">&gt;</span></span><span class="token tag"><span class="token tag"><span
                class="token punctuation">&lt;/</span>center</span><span
                class="token punctuation">&gt;</span></span><span class="token plain-text">
</span><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>hr</span><span
                class="token punctuation">&gt;</span></span><span class="token tag"><span class="token tag"><span
                class="token punctuation">&lt;</span>center</span><span
                class="token punctuation">&gt;</span></span><span
                class="token plain-text">nginx</span><span class="token tag"><span class="token tag"><span
                class="token punctuation">&lt;/</span>center</span><span
                class="token punctuation">&gt;</span></span><span class="token plain-text">
</span><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>body</span><span
                class="token punctuation">&gt;</span></span><span class="token plain-text">
</span><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>html</span><span
                class="token punctuation">&gt;</span></span><span class="token plain-text">
</span><span aria-hidden="true"
             class="line-numbers-rows"><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span></span></code></pre>
</div>
<h5>四、显示通信过程</h5>
<p><code>-v</code> 参数可以显示一次 http 通信的整个过程，包括端口连接和 http request 头信息。</p>
<div class="_2Uzcx_">
    <button class="VJbwyy" type="button" aria-label="复制代码"><i aria-label="icon: copy" class="anticon anticon-copy">
        <svg viewBox="64 64 896 896" focusable="false" class="" data-icon="copy" width="1em" height="1em"
             fill="currentColor" aria-hidden="true">
            <path d="M832 64H296c-4.4 0-8 3.6-8 8v56c0 4.4 3.6 8 8 8h496v688c0 4.4 3.6 8 8 8h56c4.4 0 8-3.6 8-8V96c0-17.7-14.3-32-32-32zM704 192H192c-17.7 0-32 14.3-32 32v530.7c0 8.5 3.4 16.6 9.4 22.6l173.3 173.3c2.2 2.2 4.7 4 7.4 5.5v1.9h4.2c3.5 1.3 7.2 2 11 2H704c17.7 0 32-14.3 32-32V224c0-17.7-14.3-32-32-32zM350 856.2L263.9 770H350v86.2zM664 888H414V746c0-22.1-17.9-40-40-40H232V264h432v624z"></path>
        </svg>
    </i></button>
    <pre class="line-numbers  language-bash"><code class="  language-bash">$ curl -v www.sina.com
* Rebuilt URL to: www.sina.com/
* Hostname was NOT found in DNS cache
*   Trying 202.108.33.60...
* Connected to www.sina.com (202.108.33.60) port 80 (#0)
&gt; GET / HTTP/1.1
&gt; User-Agent: curl/7.35.0
&gt; Host: www.sina.com
&gt; Accept: */*
&gt;
&lt; HTTP/1.1 301 Moved Permanently
* Server nginx is not blacklisted
&lt; Server: nginx
&lt; Date: Tue, 23 Aug 2016 08:48:14 GMT
&lt; Content-Type: text/html
&lt; Location: http://www.sina.com.cn/
&lt; Expires: Tue, 23 Aug 2016 08:50:14 GMT
&lt; Cache-Control: max-age=120
&lt; Age: 40
&lt; Content-Length: 178
&lt; X-Cache: HIT from xd33-81.sina.com.cn
&lt;
&lt;html&gt;
&lt;head&gt;&lt;title&gt;301 Moved Permanently&lt;/title&gt;&lt;/head&gt;
&lt;body bgcolor="white"&gt;
&lt;center&gt;&lt;h1&gt;301 Moved Permanently&lt;/h1&gt;&lt;/center&gt;
&lt;hr&gt;&lt;center&gt;nginx&lt;/center&gt;
&lt;/body&gt;
&lt;/html&gt;
* Connection #0 to host www.sina.com left intact
<span aria-hidden="true"
      class="line-numbers-rows"><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span></span></code></pre>
</div>
<p>如果觉得上面的信息还不够，那么下面的命令可以查看更详细的通信过程。</p>
<div class="_2Uzcx_">
    <button class="VJbwyy" type="button" aria-label="复制代码"><i aria-label="icon: copy" class="anticon anticon-copy">
        <svg viewBox="64 64 896 896" focusable="false" class="" data-icon="copy" width="1em" height="1em"
             fill="currentColor" aria-hidden="true">
            <path d="M832 64H296c-4.4 0-8 3.6-8 8v56c0 4.4 3.6 8 8 8h496v688c0 4.4 3.6 8 8 8h56c4.4 0 8-3.6 8-8V96c0-17.7-14.3-32-32-32zM704 192H192c-17.7 0-32 14.3-32 32v530.7c0 8.5 3.4 16.6 9.4 22.6l173.3 173.3c2.2 2.2 4.7 4 7.4 5.5v1.9h4.2c3.5 1.3 7.2 2 11 2H704c17.7 0 32-14.3 32-32V224c0-17.7-14.3-32-32-32zM350 856.2L263.9 770H350v86.2zM664 888H414V746c0-22.1-17.9-40-40-40H232V264h432v624z"></path>
        </svg>
    </i></button>
    <pre class="line-numbers  language-ruby"><code class="  language-ruby">$ curl <span
            class="token operator">--</span>trace output<span class="token punctuation">.</span>txt www<span
            class="token punctuation">.</span>sina<span class="token punctuation">.</span>com
<span aria-hidden="true" class="line-numbers-rows"><span></span></span></code></pre>
</div>
<p>或者</p>
<div class="_2Uzcx_">
    <button class="VJbwyy" type="button" aria-label="复制代码"><i aria-label="icon: copy" class="anticon anticon-copy">
        <svg viewBox="64 64 896 896" focusable="false" class="" data-icon="copy" width="1em" height="1em"
             fill="currentColor" aria-hidden="true">
            <path d="M832 64H296c-4.4 0-8 3.6-8 8v56c0 4.4 3.6 8 8 8h496v688c0 4.4 3.6 8 8 8h56c4.4 0 8-3.6 8-8V96c0-17.7-14.3-32-32-32zM704 192H192c-17.7 0-32 14.3-32 32v530.7c0 8.5 3.4 16.6 9.4 22.6l173.3 173.3c2.2 2.2 4.7 4 7.4 5.5v1.9h4.2c3.5 1.3 7.2 2 11 2H704c17.7 0 32-14.3 32-32V224c0-17.7-14.3-32-32-32zM350 856.2L263.9 770H350v86.2zM664 888H414V746c0-22.1-17.9-40-40-40H232V264h432v624z"></path>
        </svg>
    </i></button>
    <pre class="line-numbers  language-ruby"><code class="  language-ruby">$ curl <span
            class="token operator">--</span>trace<span class="token operator">-</span>ascii output<span
            class="token punctuation">.</span>txt www<span class="token punctuation">.</span>sina<span
            class="token punctuation">.</span>com
<span aria-hidden="true" class="line-numbers-rows"><span></span></span></code></pre>
</div>
<p>运行后，打开 output.txt 文件查看。</p>
<h5>五、发送表单信息</h5>
<p>发送表单信息有 GET 和 POST 两种方法。GET 方法相对简单，只要把数据附在网址后面就行。</p>
<div class="_2Uzcx_">
    <button class="VJbwyy" type="button" aria-label="复制代码"><i aria-label="icon: copy" class="anticon anticon-copy">
        <svg viewBox="64 64 896 896" focusable="false" class="" data-icon="copy" width="1em" height="1em"
             fill="currentColor" aria-hidden="true">
            <path d="M832 64H296c-4.4 0-8 3.6-8 8v56c0 4.4 3.6 8 8 8h496v688c0 4.4 3.6 8 8 8h56c4.4 0 8-3.6 8-8V96c0-17.7-14.3-32-32-32zM704 192H192c-17.7 0-32 14.3-32 32v530.7c0 8.5 3.4 16.6 9.4 22.6l173.3 173.3c2.2 2.2 4.7 4 7.4 5.5v1.9h4.2c3.5 1.3 7.2 2 11 2H704c17.7 0 32-14.3 32-32V224c0-17.7-14.3-32-32-32zM350 856.2L263.9 770H350v86.2zM664 888H414V746c0-22.1-17.9-40-40-40H232V264h432v624z"></path>
        </svg>
    </i></button>
    <pre class="line-numbers  language-kotlin"><code class="  language-kotlin">$ curl example<span
            class="token punctuation">.</span>com<span class="token operator">/</span>form<span
            class="token punctuation">.</span>cgi<span class="token operator">?</span><span
            class="token keyword">data</span><span
            class="token operator">=</span>xxx
<span aria-hidden="true" class="line-numbers-rows"><span></span></span></code></pre>
</div>
<p>POST 方法必须把数据和网址分开，curl 就要用到 <code>--data</code> 或者 <code>-d</code> 参数。</p>
<div class="_2Uzcx_">
    <button class="VJbwyy" type="button" aria-label="复制代码"><i aria-label="icon: copy" class="anticon anticon-copy">
        <svg viewBox="64 64 896 896" focusable="false" class="" data-icon="copy" width="1em" height="1em"
             fill="currentColor" aria-hidden="true">
            <path d="M832 64H296c-4.4 0-8 3.6-8 8v56c0 4.4 3.6 8 8 8h496v688c0 4.4 3.6 8 8 8h56c4.4 0 8-3.6 8-8V96c0-17.7-14.3-32-32-32zM704 192H192c-17.7 0-32 14.3-32 32v530.7c0 8.5 3.4 16.6 9.4 22.6l173.3 173.3c2.2 2.2 4.7 4 7.4 5.5v1.9h4.2c3.5 1.3 7.2 2 11 2H704c17.7 0 32-14.3 32-32V224c0-17.7-14.3-32-32-32zM350 856.2L263.9 770H350v86.2zM664 888H414V746c0-22.1-17.9-40-40-40H232V264h432v624z"></path>
        </svg>
    </i></button>
    <pre class="line-numbers  language-kotlin"><code class="  language-kotlin">$ curl <span
            class="token operator">-</span>X POST <span class="token operator">--</span><span
            class="token keyword">data</span> <span
            class="token string">"data=xxx"</span> example<span class="token punctuation">.</span>com<span
            class="token operator">/</span>form<span class="token punctuation">.</span>cgi
<span aria-hidden="true" class="line-numbers-rows"><span></span></span></code></pre>
</div>
<p>如果你的数据没有经过表单编码，还可以让 curl 为你编码，参数是 <code>--data-urlencode</code>。</p>
<div class="_2Uzcx_">
    <button class="VJbwyy" type="button" aria-label="复制代码"><i aria-label="icon: copy" class="anticon anticon-copy">
        <svg viewBox="64 64 896 896" focusable="false" class="" data-icon="copy" width="1em" height="1em"
             fill="currentColor" aria-hidden="true">
            <path d="M832 64H296c-4.4 0-8 3.6-8 8v56c0 4.4 3.6 8 8 8h496v688c0 4.4 3.6 8 8 8h56c4.4 0 8-3.6 8-8V96c0-17.7-14.3-32-32-32zM704 192H192c-17.7 0-32 14.3-32 32v530.7c0 8.5 3.4 16.6 9.4 22.6l173.3 173.3c2.2 2.2 4.7 4 7.4 5.5v1.9h4.2c3.5 1.3 7.2 2 11 2H704c17.7 0 32-14.3 32-32V224c0-17.7-14.3-32-32-32zM350 856.2L263.9 770H350v86.2zM664 888H414V746c0-22.1-17.9-40-40-40H232V264h432v624z"></path>
        </svg>
    </i></button>
    <pre class="line-numbers  language-kotlin"><code class="  language-kotlin">$ curl <span
            class="token operator">-</span>X POST<span class="token operator">--</span><span
            class="token keyword">data</span><span
            class="token operator">-</span>urlencode <span class="token string">"date=April 1"</span> example<span
            class="token punctuation">.</span>com<span class="token operator">/</span>form<span
            class="token punctuation">.</span>cgi
<span aria-hidden="true" class="line-numbers-rows"><span></span></span></code></pre>
</div>
<h5>六、HTTP动词</h5>
<p>curl 默认的 HTTP 动词是 GET，使用 <code>-X</code> 参数可以支持其他动词。</p>
<div class="_2Uzcx_">
    <button class="VJbwyy" type="button" aria-label="复制代码"><i aria-label="icon: copy" class="anticon anticon-copy">
        <svg viewBox="64 64 896 896" focusable="false" class="" data-icon="copy" width="1em" height="1em"
             fill="currentColor" aria-hidden="true">
            <path d="M832 64H296c-4.4 0-8 3.6-8 8v56c0 4.4 3.6 8 8 8h496v688c0 4.4 3.6 8 8 8h56c4.4 0 8-3.6 8-8V96c0-17.7-14.3-32-32-32zM704 192H192c-17.7 0-32 14.3-32 32v530.7c0 8.5 3.4 16.6 9.4 22.6l173.3 173.3c2.2 2.2 4.7 4 7.4 5.5v1.9h4.2c3.5 1.3 7.2 2 11 2H704c17.7 0 32-14.3 32-32V224c0-17.7-14.3-32-32-32zM350 856.2L263.9 770H350v86.2zM664 888H414V746c0-22.1-17.9-40-40-40H232V264h432v624z"></path>
        </svg>
    </i></button>
    <pre class="line-numbers  language-ruby"><code class="  language-ruby">$ curl <span
            class="token operator">-</span><span class="token constant">X</span> <span
            class="token constant">POST</span> www<span class="token punctuation">.</span>example<span
            class="token punctuation">.</span>com
$ curl <span class="token operator">-</span><span class="token constant">X</span> <span
                class="token constant">DELETE</span> www<span class="token punctuation">.</span>example<span
                class="token punctuation">.</span>com
<span aria-hidden="true" class="line-numbers-rows"><span></span><span></span></span></code></pre>
</div>
<h5>七、User Agent字段</h5>
<p>这个字段是用来表示客户端的设备信息。服务器有时会根据这个字段，针对不同设备，返回不同格式的网页，比如手机版和桌面版。<br>
    浏览器的 User Agent 是：</p>
<div class="_2Uzcx_">
    <button class="VJbwyy" type="button" aria-label="复制代码"><i aria-label="icon: copy" class="anticon anticon-copy">
        <svg viewBox="64 64 896 896" focusable="false" class="" data-icon="copy" width="1em" height="1em"
             fill="currentColor" aria-hidden="true">
            <path d="M832 64H296c-4.4 0-8 3.6-8 8v56c0 4.4 3.6 8 8 8h496v688c0 4.4 3.6 8 8 8h56c4.4 0 8-3.6 8-8V96c0-17.7-14.3-32-32-32zM704 192H192c-17.7 0-32 14.3-32 32v530.7c0 8.5 3.4 16.6 9.4 22.6l173.3 173.3c2.2 2.2 4.7 4 7.4 5.5v1.9h4.2c3.5 1.3 7.2 2 11 2H704c17.7 0 32-14.3 32-32V224c0-17.7-14.3-32-32-32zM350 856.2L263.9 770H350v86.2zM664 888H414V746c0-22.1-17.9-40-40-40H232V264h432v624z"></path>
        </svg>
    </i></button>
    <pre class="line-numbers  language-undefined"><code class="  language-undefined">Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.84 Safari/537.36
<span aria-hidden="true" class="line-numbers-rows"><span></span></span></code></pre>
</div>
<p>curl 可以这样模拟：</p>
<div class="_2Uzcx_">
    <button class="VJbwyy" type="button" aria-label="复制代码"><i aria-label="icon: copy" class="anticon anticon-copy">
        <svg viewBox="64 64 896 896" focusable="false" class="" data-icon="copy" width="1em" height="1em"
             fill="currentColor" aria-hidden="true">
            <path d="M832 64H296c-4.4 0-8 3.6-8 8v56c0 4.4 3.6 8 8 8h496v688c0 4.4 3.6 8 8 8h56c4.4 0 8-3.6 8-8V96c0-17.7-14.3-32-32-32zM704 192H192c-17.7 0-32 14.3-32 32v530.7c0 8.5 3.4 16.6 9.4 22.6l173.3 173.3c2.2 2.2 4.7 4 7.4 5.5v1.9h4.2c3.5 1.3 7.2 2 11 2H704c17.7 0 32-14.3 32-32V224c0-17.7-14.3-32-32-32zM350 856.2L263.9 770H350v86.2zM664 888H414V746c0-22.1-17.9-40-40-40H232V264h432v624z"></path>
        </svg>
    </i></button>
    <pre class="line-numbers  language-ruby"><code class="  language-ruby">$ curl <span
            class="token operator">--</span>user<span class="token operator">-</span>agent <span
            class="token string">"[User Agent]"</span> <span class="token punctuation">[</span><span
            class="token constant">URL</span><span class="token punctuation">]</span>
<span aria-hidden="true" class="line-numbers-rows"><span></span></span></code></pre>
</div>
<h5>八、cookie</h5>
<p>使用 <code>--cookie</code> 参数，可以让 curl 发送 cookie。</p>
<div class="_2Uzcx_">
    <button class="VJbwyy" type="button" aria-label="复制代码"><i aria-label="icon: copy" class="anticon anticon-copy">
        <svg viewBox="64 64 896 896" focusable="false" class="" data-icon="copy" width="1em" height="1em"
             fill="currentColor" aria-hidden="true">
            <path d="M832 64H296c-4.4 0-8 3.6-8 8v56c0 4.4 3.6 8 8 8h496v688c0 4.4 3.6 8 8 8h56c4.4 0 8-3.6 8-8V96c0-17.7-14.3-32-32-32zM704 192H192c-17.7 0-32 14.3-32 32v530.7c0 8.5 3.4 16.6 9.4 22.6l173.3 173.3c2.2 2.2 4.7 4 7.4 5.5v1.9h4.2c3.5 1.3 7.2 2 11 2H704c17.7 0 32-14.3 32-32V224c0-17.7-14.3-32-32-32zM350 856.2L263.9 770H350v86.2zM664 888H414V746c0-22.1-17.9-40-40-40H232V264h432v624z"></path>
        </svg>
    </i></button>
    <pre class="line-numbers  language-ruby"><code class="  language-ruby">$ curl <span
            class="token operator">--</span>cookie <span class="token string">"name=xxx"</span> www<span
            class="token punctuation">.</span>example<span class="token punctuation">.</span>com
<span aria-hidden="true" class="line-numbers-rows"><span></span></span></code></pre>
</div>
<p>至于具体的 cookie 的值，可以从 http response 头信息的 <code>Set-Cookie</code> 字段中得到。</p>
<h5>九、增加头信息</h5>
<p>有时需要在 http request 之中，自行增加一个头信息。<code>--header</code> 参数就可以起到这个作用。</p>
<div class="_2Uzcx_">
    <button class="VJbwyy" type="button" aria-label="复制代码"><i aria-label="icon: copy" class="anticon anticon-copy">
        <svg viewBox="64 64 896 896" focusable="false" class="" data-icon="copy" width="1em" height="1em"
             fill="currentColor" aria-hidden="true">
            <path d="M832 64H296c-4.4 0-8 3.6-8 8v56c0 4.4 3.6 8 8 8h496v688c0 4.4 3.6 8 8 8h56c4.4 0 8-3.6 8-8V96c0-17.7-14.3-32-32-32zM704 192H192c-17.7 0-32 14.3-32 32v530.7c0 8.5 3.4 16.6 9.4 22.6l173.3 173.3c2.2 2.2 4.7 4 7.4 5.5v1.9h4.2c3.5 1.3 7.2 2 11 2H704c17.7 0 32-14.3 32-32V224c0-17.7-14.3-32-32-32zM350 856.2L263.9 770H350v86.2zM664 888H414V746c0-22.1-17.9-40-40-40H232V264h432v624z"></path>
        </svg>
    </i></button>
    <pre class="line-numbers  language-cpp"><code class="  language-cpp">$ curl <span
            class="token operator">--</span>header <span class="token string">"Content-Type:application/json"</span> http<span
            class="token operator">:</span><span class="token operator">/</span><span
            class="token operator">/</span>example<span class="token punctuation">.</span>com
<span aria-hidden="true" class="line-numbers-rows"><span></span></span></code></pre>
</div>
<h5>十、HTTP认证</h5>
<p>有些网域需要 HTTP 认证，这时 curl 需要用到 <code>--user</code> 或者 <code>-u</code> 参数。</p>
<div class="_2Uzcx_">
    <button class="VJbwyy" type="button" aria-label="复制代码"><i aria-label="icon: copy" class="anticon anticon-copy">
        <svg viewBox="64 64 896 896" focusable="false" class="" data-icon="copy" width="1em" height="1em"
             fill="currentColor" aria-hidden="true">
            <path d="M832 64H296c-4.4 0-8 3.6-8 8v56c0 4.4 3.6 8 8 8h496v688c0 4.4 3.6 8 8 8h56c4.4 0 8-3.6 8-8V96c0-17.7-14.3-32-32-32zM704 192H192c-17.7 0-32 14.3-32 32v530.7c0 8.5 3.4 16.6 9.4 22.6l173.3 173.3c2.2 2.2 4.7 4 7.4 5.5v1.9h4.2c3.5 1.3 7.2 2 11 2H704c17.7 0 32-14.3 32-32V224c0-17.7-14.3-32-32-32zM350 856.2L263.9 770H350v86.2zM664 888H414V746c0-22.1-17.9-40-40-40H232V264h432v624z"></path>
        </svg>
    </i></button>
    <pre class="line-numbers  language-ruby"><code class="  language-ruby">$ curl <span
            class="token operator">--</span>user name<span class="token symbol">:password</span> example<span
            class="token punctuation">.</span>com
<span aria-hidden="true" class="line-numbers-rows"><span></span></span></code></pre>
</div>
<h5>附录 curl 命令完整的参数</h5>
<div class="_2Uzcx_">
    <button class="VJbwyy" type="button" aria-label="复制代码"><i aria-label="icon: copy" class="anticon anticon-copy">
        <svg viewBox="64 64 896 896" focusable="false" class="" data-icon="copy" width="1em" height="1em"
             fill="currentColor" aria-hidden="true">
            <path d="M832 64H296c-4.4 0-8 3.6-8 8v56c0 4.4 3.6 8 8 8h496v688c0 4.4 3.6 8 8 8h56c4.4 0 8-3.6 8-8V96c0-17.7-14.3-32-32-32zM704 192H192c-17.7 0-32 14.3-32 32v530.7c0 8.5 3.4 16.6 9.4 22.6l173.3 173.3c2.2 2.2 4.7 4 7.4 5.5v1.9h4.2c3.5 1.3 7.2 2 11 2H704c17.7 0 32-14.3 32-32V224c0-17.7-14.3-32-32-32zM350 856.2L263.9 770H350v86.2zM664 888H414V746c0-22.1-17.9-40-40-40H232V264h432v624z"></path>
        </svg>
    </i></button>
    <pre class="line-numbers  language-bash"><code class="  language-bash">$ curl --help
Usage: curl [options...] &lt;url&gt;
Options: (H) means HTTP/HTTPS only, (F) means FTP only
     --anyauth       Pick "any" authentication method (H)
 -a, --append        Append to target file when uploading (F/SFTP)
     --basic         Use HTTP Basic Authentication (H)
     --cacert FILE   CA certificate to verify peer against (SSL)
     --capath DIR    CA directory to verify peer against (SSL)
 -E, --cert CERT[:PASSWD] Client certificate file and password (SSL)
     --cert-type TYPE Certificate file type (DER/PEM/ENG) (SSL)
     --ciphers LIST  SSL ciphers to use (SSL)
     --compressed    Request compressed response (using deflate or gzip)
 -K, --config FILE   Specify which config file to read
     --connect-timeout SECONDS  Maximum time allowed for connection
 -C, --continue-at OFFSET  Resumed transfer offset
 -b, --cookie STRING/FILE  String or file to read cookies from (H)
 -c, --cookie-jar FILE  Write cookies to this file after operation (H)
     --create-dirs   Create necessary local directory hierarchy
     --crlf          Convert LF to CRLF in upload
     --crlfile FILE  Get a CRL list in PEM format from the given file
 -d, --data DATA     HTTP POST data (H)
     --data-ascii DATA  HTTP POST ASCII data (H)
     --data-binary DATA  HTTP POST binary data (H)
     --data-urlencode DATA  HTTP POST data url encoded (H)
     --delegation STRING GSS-API delegation permission
     --digest        Use HTTP Digest Authentication (H)
     --disable-eprt  Inhibit using EPRT or LPRT (F)
     --disable-epsv  Inhibit using EPSV (F)
     --dns-servers    DNS server addrs to use: 1.1.1.1;2.2.2.2
     --dns-interface  Interface to use for DNS requests
     --dns-ipv4-addr  IPv4 address to use for DNS requests, dot notation
     --dns-ipv6-addr  IPv6 address to use for DNS requests, dot notation
 -D, --dump-header FILE  Write the headers to this file
     --egd-file FILE  EGD socket path for random data (SSL)
     --engine ENGINE  Crypto engine (SSL). "--engine list" for list
 -f, --fail          Fail silently (no output at all) on HTTP errors (H)
 -F, --form CONTENT  Specify HTTP multipart POST data (H)
     --form-string STRING  Specify HTTP multipart POST data (H)
     --ftp-account DATA  Account data string (F)
     --ftp-alternative-to-user COMMAND  String to replace "USER [name]" (F)
     --ftp-create-dirs  Create the remote dirs if not present (F)
     --ftp-method [MULTICWD/NOCWD/SINGLECWD] Control CWD usage (F)
     --ftp-pasv      Use PASV/EPSV instead of PORT (F)
 -P, --ftp-port ADR  Use PORT with given address instead of PASV (F)
     --ftp-skip-pasv-ip Skip the IP address for PASV (F)
     --ftp-pret      Send PRET before PASV (for drftpd) (F)
     --ftp-ssl-ccc   Send CCC after authenticating (F)
     --ftp-ssl-ccc-mode ACTIVE/PASSIVE  Set CCC mode (F)
     --ftp-ssl-control Require SSL/TLS for ftp login, clear for transfer (F)
 -G, --get           Send the -d data with a HTTP GET (H)
 -g, --globoff       Disable URL sequences and ranges using {} and []
 -H, --header LINE   Custom header to pass to server (H)
 -I, --head          Show document info only
 -h, --help          This help text
     --hostpubmd5 MD5  Hex encoded MD5 string of the host public key. (SSH)
 -0, --http1.0       Use HTTP 1.0 (H)
     --http1.1       Use HTTP 1.1 (H)
     --http2.0       Use HTTP 2.0 (H)
     --ignore-content-length  Ignore the HTTP Content-Length header
 -i, --include       Include protocol headers in the output (H/F)
 -k, --insecure      Allow connections to SSL sites without certs (H)
     --interface INTERFACE  Specify network interface/address to use
 -4, --ipv4          Resolve name to IPv4 address
 -6, --ipv6          Resolve name to IPv6 address
 -j, --junk-session-cookies Ignore session cookies read from file (H)
     --keepalive-time SECONDS  Interval between keepalive probes
     --key KEY       Private key file name (SSL/SSH)
     --key-type TYPE Private key file type (DER/PEM/ENG) (SSL)
     --krb LEVEL     Enable Kerberos with specified security level (F)
     --libcurl FILE  Dump libcurl equivalent code of this command line
     --limit-rate RATE  Limit transfer speed to this rate
 -l, --list-only     List only mode (F/POP3)
     --local-port RANGE  Force use of these local port numbers
 -L, --location      Follow redirects (H)
     --location-trusted like --location and send auth to other hosts (H)
 -M, --manual        Display the full manual
     --mail-from FROM  Mail from this address (SMTP)
     --mail-rcpt TO  Mail to this/these addresses (SMTP)
     --mail-auth AUTH  Originator address of the original email (SMTP)
     --max-filesize BYTES  Maximum file size to download (H/F)
     --max-redirs NUM  Maximum number of redirects allowed (H)
 -m, --max-time SECONDS  Maximum time allowed for the transfer
     --metalink      Process given URLs as metalink XML file
     --negotiate     Use HTTP Negotiate Authentication (H)
 -n, --netrc         Must read .netrc for user name and password
     --netrc-optional Use either .netrc or URL; overrides -n
     --netrc-file FILE  Set up the netrc filename to use
 -N, --no-buffer     Disable buffering of the output stream
     --no-keepalive  Disable keepalive use on the connection
     --no-sessionid  Disable SSL session-ID reusing (SSL)
     --noproxy       List of hosts which do not use proxy
     --ntlm          Use HTTP NTLM authentication (H)
     --oauth2-bearer TOKEN  OAuth 2 Bearer Token (IMAP, POP3, SMTP)
 -o, --output FILE   Write output to &lt;file&gt; instead of stdout
     --pass PASS     Pass phrase for the private key (SSL/SSH)
     --post301       Do not switch to GET after following a 301 redirect (H)
     --post302       Do not switch to GET after following a 302 redirect (H)
     --post303       Do not switch to GET after following a 303 redirect (H)
 -#, --progress-bar  Display transfer progress as a progress bar
     --proto PROTOCOLS  Enable/disable specified protocols
     --proto-redir PROTOCOLS  Enable/disable specified protocols on redirect
 -x, --proxy [PROTOCOL://]HOST[:PORT] Use proxy on given port
     --proxy-anyauth Pick "any" proxy authentication method (H)
     --proxy-basic   Use Basic authentication on the proxy (H)
     --proxy-digest  Use Digest authentication on the proxy (H)
     --proxy-negotiate Use Negotiate authentication on the proxy (H)
     --proxy-ntlm    Use NTLM authentication on the proxy (H)
 -U, --proxy-user USER[:PASSWORD]  Proxy user and password
     --proxy1.0 HOST[:PORT]  Use HTTP/1.0 proxy on given port
 -p, --proxytunnel   Operate through a HTTP proxy tunnel (using CONNECT)
     --pubkey KEY    Public key file name (SSH)
 -Q, --quote CMD     Send command(s) to server before transfer (F/SFTP)
     --random-file FILE  File for reading random data from (SSL)
 -r, --range RANGE   Retrieve only the bytes within a range
     --raw           Do HTTP "raw", without any transfer decoding (H)
 -e, --referer       Referer URL (H)
 -J, --remote-header-name Use the header-provided filename (H)
 -O, --remote-name   Write output to a file named as the remote file
     --remote-name-all Use the remote file name for all URLs
 -R, --remote-time   Set the remote file's time on the local output
 -X, --request COMMAND  Specify request command to use
     --resolve HOST:PORT:ADDRESS  Force resolve of HOST:PORT to ADDRESS
     --retry NUM   Retry request NUM times if transient problems occur
     --retry-delay SECONDS When retrying, wait this many seconds between each
     --retry-max-time SECONDS  Retry only within this period
     --sasl-ir       Enable initial response in SASL authentication
 -S, --show-error    Show error. With -s, make curl show errors when they occur
 -s, --silent        Silent mode. Don't output anything
     --socks4 HOST[:PORT]  SOCKS4 proxy on given host + port
     --socks4a HOST[:PORT]  SOCKS4a proxy on given host + port
     --socks5 HOST[:PORT]  SOCKS5 proxy on given host + port
     --socks5-hostname HOST[:PORT] SOCKS5 proxy, pass host name to proxy
     --socks5-gssapi-service NAME  SOCKS5 proxy service name for gssapi
     --socks5-gssapi-nec  Compatibility with NEC SOCKS5 server
 -Y, --speed-limit RATE  Stop transfers below speed-limit for 'speed-time' secs
 -y, --speed-time SECONDS  Time for trig speed-limit abort. Defaults to 30
     --ssl           Try SSL/TLS (FTP, IMAP, POP3, SMTP)
     --ssl-reqd      Require SSL/TLS (FTP, IMAP, POP3, SMTP)
 -2, --sslv2         Use SSLv2 (SSL)
 -3, --sslv3         Use SSLv3 (SSL)
     --ssl-allow-beast Allow security flaw to improve interop (SSL)
     --stderr FILE   Where to redirect stderr. - means stdout
     --tcp-nodelay   Use the TCP_NODELAY option
 -t, --telnet-option OPT=VAL  Set telnet option
     --tftp-blksize VALUE  Set TFTP BLKSIZE option (must be &gt;512)
 -z, --time-cond TIME  Transfer based on a time condition
 -1, --tlsv1         Use TLSv1 (SSL)
     --trace FILE    Write a debug trace to the given file
     --trace-ascii FILE  Like --trace but without the hex output
     --trace-time    Add time stamps to trace/verbose output
     --tr-encoding   Request compressed transfer encoding (H)
 -T, --upload-file FILE  Transfer FILE to destination
     --url URL       URL to work with
 -B, --use-ascii     Use ASCII/text transfer
 -u, --user USER[:PASSWORD][;OPTIONS]  Server user, password and login options
     --tlsuser USER  TLS username
     --tlspassword STRING TLS password
     --tlsauthtype STRING  TLS authentication type (default SRP)
 -A, --user-agent STRING  User-Agent to send to server (H)
 -v, --verbose       Make the operation more talkative
 -V, --version       Show version number and quit
 -w, --write-out FORMAT  What to output after completion
     --xattr        Store metadata in extended file attributes
 -q                 If used as the first parameter disables .curlrc


    </code>
    </pre>
</div>
