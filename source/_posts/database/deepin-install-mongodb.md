---
title: "一行命令带你安装mongodb(deepin系统下)"
date:       2019-09-25
tags:
	- Linux
	- deepin
	- database
	- mongodb
	- nosql
---








### 一行命令安装mongodb

`sudo apt-get install mongodb`

### 详细的在下面

<div class="blog-content-box">

<article class="baidu_pl">
            <div id="article_content" class="article_content clearfix">
                                <link rel="stylesheet" href="https://csdnimg.cn/release/phoenix/template/css/ck_htmledit_views-3019150162.css">
                                    <div id="content_views" class="markdown_views">
                <!-- flowchart 箭头图标 勿删 -->
                <svg xmlns="http://www.w3.org/2000/svg" style="display: none;">
                    <path stroke-linecap="round" d="M5,0 0,2.5 5,5z" id="raphael-marker-block" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);"></path>
                </svg>
                                        <p>安装 <br>
下载地址：<a href="https://fastdl.mongodb.org/linux/mongodb-linux-x86_64-2.6.0.tgz" rel="nofollow" data-token="5491b390828b119075d28645562c9a0c">https://fastdl.mongodb.org/linux/mongodb-linux-x86_64-2.6.0.tgz</a>（或者到官网上下载别的版本）</p>

<p>完成下载后，把软件包移动到软件安装的目录下，我这里是/usr/local/。</p>

<p>解压：tar -zxvf mongodb-linux-x86_64-2.6.0.tgz（权限不够，要加sudo，下同）</p>

<p>更改安装目录：mv mongodb-linux-x86_64-2.6.0.tgz mongodb</p>

<p>创建mongodb数据库存放路径：mkdir -p /data/db</p>

<p>创建mongodb数据库日志存放路径：mkdir -p /usr/local/mongodb/log/（存放在安装路径下）</p>

<p>启动服务</p>



<pre class="prettyprint" name="code"><code class="hljs brainfuck has-numbering" onclick="mdcp.signin(event)" style="position: unset;"><span class="hljs-comment">启动mongodb服务：/usr/local/mongodb/bin/mongod</span> <span class="hljs-literal">-</span><span class="hljs-literal">-</span><span class="hljs-comment">dbpath=/data/db</span> <span class="hljs-literal">-</span><span class="hljs-literal">-</span><span class="hljs-comment">logpath=/usr/local/mongodb/log/mongodb</span><span class="hljs-string">.</span><span class="hljs-comment">log</span> <span class="hljs-literal">-</span><span class="hljs-literal">-</span><span class="hljs-comment">logappend</span> <span class="hljs-literal">-</span><span class="hljs-literal">-</span><span class="hljs-comment">port</span> <span class="hljs-comment">27017</span> <span class="hljs-literal">-</span><span class="hljs-literal">-</span><span class="hljs-comment">fork（若出现错误，可能是权限不够）</span>
<span class="hljs-literal">-</span><span class="hljs-literal">-</span><span class="hljs-comment">dbpath</span> <span class="hljs-comment">数据库路径(数据文件)</span>
<span class="hljs-literal">-</span><span class="hljs-literal">-</span><span class="hljs-comment">logpath</span> <span class="hljs-comment">数据库日志文件路径</span>
<span class="hljs-literal">-</span><span class="hljs-literal">-</span><span class="hljs-comment">port</span> <span class="hljs-comment">启用端口号</span>
<span class="hljs-literal">-</span><span class="hljs-literal">-</span><span class="hljs-comment">fork</span> <span class="hljs-comment">在后台运行</span>
<span class="hljs-literal">-</span><span class="hljs-literal">-</span><span class="hljs-comment">auth</span> <span class="hljs-comment">是否需要验证权限登录(用户名和密码)</span><div class="hljs-button signin" data-title="登录后复制"></div></code><ul class="pre-numbering" style=""><li style="color: rgb(153, 153, 153);">1</li><li style="color: rgb(153, 153, 153);">2</li><li style="color: rgb(153, 153, 153);">3</li><li style="color: rgb(153, 153, 153);">4</li><li style="color: rgb(153, 153, 153);">5</li><li style="color: rgb(153, 153, 153);">6</li></ul></pre>

<p>设置mongodb <br>
添加安装路径到path中：</p>



<pre class="prettyprint" name="code"><code class="hljs ruby has-numbering" onclick="mdcp.signin(event)" style="position: unset;"><span class="hljs-variable">$ </span>vim /etc/profile
添加一下代码到文件的最后一行，并保存<span class="hljs-symbol">:</span>
export <span class="hljs-constant">PATH</span>=<span class="hljs-variable">$PATH</span><span class="hljs-symbol">:/usr/local/mongodb/bin</span>
使设置生效：source /etc/profile
进入控制台：mongo（在任意位置）<div class="hljs-button signin" data-title="登录后复制"></div></code><ul class="pre-numbering" style=""><li style="color: rgb(153, 153, 153);">1</li><li style="color: rgb(153, 153, 153);">2</li><li style="color: rgb(153, 153, 153);">3</li><li style="color: rgb(153, 153, 153);">4</li><li style="color: rgb(153, 153, 153);">5</li></ul></pre>

<p>设置mongodb开机自启： <br>
编辑mongodb配置文件，设置启动参数：vim /usr/local/mongodb/mongodb.conf（没有就新建一个）</p>

<p>加入以下参数并保存：</p>



<pre class="prettyprint" name="code"><code class="hljs ini has-numbering" onclick="mdcp.signin(event)" style="position: unset;"><span class="hljs-setting">dbpath=<span class="hljs-value">/data/db #数据库路径</span></span>
<span class="hljs-setting">port=<span class="hljs-value"><span class="hljs-number">27017</span> #端口号</span></span>
<span class="hljs-setting">fork=<span class="hljs-value"><span class="hljs-keyword">true</span> #设置后台运行</span></span>
<span class="hljs-setting">logappend=<span class="hljs-value"><span class="hljs-keyword">true</span></span></span>
<span class="hljs-setting">shardsvr=<span class="hljs-value"><span class="hljs-keyword">true</span></span></span>
<span class="hljs-setting">pidfilepath=<span class="hljs-value">/usr/local/mongodb/mongo.pid</span></span>
<span class="hljs-setting">logpath=<span class="hljs-value">/usr/local/mongodb/log/mongodb.log #日志输出文件路径</span></span>
<span class="hljs-setting">directoryperdb=<span class="hljs-value"><span class="hljs-keyword">true</span></span></span>
<span class="hljs-setting">auth=<span class="hljs-value"><span class="hljs-keyword">false</span> #关闭认证</span></span><div class="hljs-button signin" data-title="登录后复制"></div></code><ul class="pre-numbering" style=""><li style="color: rgb(153, 153, 153);">1</li><li style="color: rgb(153, 153, 153);">2</li><li style="color: rgb(153, 153, 153);">3</li><li style="color: rgb(153, 153, 153);">4</li><li style="color: rgb(153, 153, 153);">5</li><li style="color: rgb(153, 153, 153);">6</li><li style="color: rgb(153, 153, 153);">7</li><li style="color: rgb(153, 153, 153);">8</li><li style="color: rgb(153, 153, 153);">9</li></ul></pre>

<p>打开命令行，输入mongo，即可验证。</p>                                    </div>
                <link href="https://csdnimg.cn/release/phoenix/mdeditor/markdown_views-095d4a0b23.css" rel="stylesheet">
                    </div>
    </article>
    </div>