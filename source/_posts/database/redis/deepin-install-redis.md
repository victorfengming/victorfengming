---
title: "一行命令带你安装redis(deepin系统下)"
date:       2019-09-25
tags:
	- Linux
	- deepin
	- database
	- redis
	- nosql
---

### 1.安装Redis服务

`apt-get install redis-server`

### 2.启动服务

`/etc/init.d/redis-server start`

### 3.连接服务

`redis-cli`

### 详细内容
<div class="blog-content-box">
    <div class="article-header-box">
        <div class="article-header">
       

<article class="baidu_pl">
            <div id="article_content" class="article_content clearfix">
                                            <div class="article-copyright">
            <span class="creativecommons">
            <a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/">
                </a>

</span>
        </div>
                                        <link rel="stylesheet" href="https://csdnimg.cn/release/phoenix/template/css/ck_htmledit_views-3019150162.css">
                            <div id="content_views" class="markdown_views">
        <!-- flowchart 箭头图标 勿删 -->
        <svg xmlns="http://www.w3.org/2000/svg" style="display: none;">
            <path stroke-linecap="round" d="M5,0 0,2.5 5,5z" id="raphael-marker-block" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);"></path>
        </svg>
                                <h2 id="nosql和redis的介绍"><a name="t0"></a>NoSQL和redis的介绍</h2>

<p>传统的关系型数据库难以支持当下“三高”的互联网环境，而NoSQL能在高并发，高扩展等方面体现较强的优势，具体体现有以下几点：</p>

<ul>
<li>易扩展性</li>
<li>高负载型（用空间换时间）</li>
<li>灵活多样的数据类型</li>
<li>高可用性</li>
</ul>

<p>redis是NoSQL中的一个比较典型的非关系型数据库，其常用在以下几个方面：</p>

<ul>
<li>缓存机制（最常用）</li>
<li>在线好友列表</li>
<li>任务队列，比如秒杀活动等</li>
<li>应用排行榜</li>
</ul>

<p>接下来将记录我在deepin系统下，安装以及使用redis的步骤。</p>

<h2 id="安装c的编译环境"><a name="t1"></a>安装C的编译环境</h2>

<p>由于redis是C语言开发的，所以对redis进行编译的之前，需要安装C的编译环境。 <br>
在控制台中输入：</p>

<pre class="prettyprint" name="code"><code class="hljs lasso has-numbering" onclick="mdcp.signin(event)" style="position: unset;">sudo apt<span class="hljs-attribute">-get</span> install gcc g<span class="hljs-subst">++</span> <span class="hljs-attribute">-y</span><div class="hljs-button signin" data-title="登录后复制"></div></code><ul class="pre-numbering" style=""><li style="color: rgb(153, 153, 153);">1</li></ul></pre>



<h2 id="解压redis压缩文件"><a name="t2"></a>解压redis压缩文件</h2>

<p>首先下载一个redis的压缩文件，解压到/usr/local目录下</p>



<pre class="prettyprint" name="code"><code class="hljs lasso has-numbering" onclick="mdcp.signin(event)" style="position: unset;">tar <span class="hljs-attribute">-xvf</span> redis<span class="hljs-subst">-</span><span class="hljs-number">3.0</span><span class="hljs-number">.0</span><span class="hljs-built_in">.</span>tar<span class="hljs-built_in">.</span>gz <span class="hljs-attribute">-C</span> /usr/<span class="hljs-built_in">local</span><div class="hljs-button signin" data-title="登录后复制"></div></code><ul class="pre-numbering" style=""><li style="color: rgb(153, 153, 153);">1</li></ul></pre>

<h2 id="编译redis"><a name="t3"></a>编译redis</h2>

<p>进入到redis解压的目录下</p>



<pre class="prettyprint" name="code"><code class="hljs bash has-numbering" onclick="mdcp.signin(event)" style="position: unset;"><span class="hljs-built_in">cd</span> /usr/local/redis-<span class="hljs-number">3.3</span>.<span class="hljs-number">0</span><div class="hljs-button signin" data-title="登录后复制"></div></code><ul class="pre-numbering" style=""><li style="color: rgb(153, 153, 153);">1</li></ul></pre>

<p>使用make命令编译redis</p>



<pre class="prettyprint" name="code"><code class="hljs bash has-numbering" onclick="mdcp.signin(event)" style="position: unset;"><span class="hljs-built_in">sudo</span> make<div class="hljs-button signin" data-title="登录后复制"></div></code><ul class="pre-numbering" style=""><li style="color: rgb(153, 153, 153);">1</li></ul></pre>

<h2 id="安装"><a name="t4"></a>安装</h2>

<p>在redis解压的目录（/usr/local/redis-3.3.0）下，使用如下命令安装redis到/usr/local/redis中</p>



<pre class="prettyprint" name="code"><code class="hljs bash has-numbering" onclick="mdcp.signin(event)" style="position: unset;"><span class="hljs-built_in">sudo</span> make PREFIX=/usr/local/redis install<div class="hljs-button signin" data-title="登录后复制"></div></code><ul class="pre-numbering" style=""><li style="color: rgb(153, 153, 153);">1</li></ul></pre>

<p>其中<code>PREFIX=/usr/local/redis</code>就是制定安装的路径</p>



<h2 id="拷贝配置文件"><a name="t5"></a>拷贝配置文件</h2>

<p>将/usr/local/redis-3.0.0中的redis.conf拷贝到安装目录/usr/local/redis/bin中</p>



<pre class="prettyprint" name="code"><code class="hljs avrasm has-numbering" onclick="mdcp.signin(event)" style="position: unset;">sudo <span class="hljs-keyword">cp</span> redis<span class="hljs-preprocessor">.conf</span> /usr/local/redis/bin/<div class="hljs-button signin" data-title="登录后复制"></div></code><ul class="pre-numbering" style=""><li style="color: rgb(153, 153, 153);">1</li></ul></pre>

<p>用vim修改配置文件中的<code>daemonize no</code>为<code>daemonize yes</code> <br>
注意，该<code>redis.conf</code>可能为只读文件，需要用sudo命令来打开vim进行编辑</p>



<pre class="prettyprint" name="code"><code class="hljs bash has-numbering" onclick="mdcp.signin(event)" style="position: unset;"><span class="hljs-built_in">sudo</span> vim /usr/local/redis/bin/redis.conf<div class="hljs-button signin" data-title="登录后复制"></div></code><ul class="pre-numbering" style=""><li style="color: rgb(153, 153, 153);">1</li></ul></pre>

<h2 id="启动redis"><a name="t6"></a>启动redis</h2>

<p>启动方式分为前端启动和后端启动</p>

<h4 id="前端启动">前端启动</h4>

<p>直接运行bin/redis-server <br>
首先进入<code>/usr/local/redis/bin</code>目录，然后输入<code>./redis-server</code> <br>
启动后的效果如下： <br>
<img src="https://img-blog.csdn.net/20171106121600303?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvdTAxNDIyOTIxNQ==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast" alt="前端启动效果图" title=""> <br>
前端模式启动的缺点是启动完成之后，不能再进行其他操作，如果操作必须使用ctrl+c，同时redis-server程序结束，不推荐这种开启方式。</p>

<h4 id="后端启动">后端启动</h4>

<p>进入redis目录，然后输入<code>./redis-server ./redis.conf</code>，即可启动redis服务端， <br>
然后输入<code>./redis-cli</code>即可进入客户端进行操作</p>



<h2 id="退出redis"><a name="t7"></a>退出redis</h2>

<p>从客户端进入redis之后，输入<code>exit</code>退出</p>                                    </div>
                <link href="https://csdnimg.cn/release/phoenix/mdeditor/markdown_views-095d4a0b23.css" rel="stylesheet">
                    </div>
    </article>
    </div>