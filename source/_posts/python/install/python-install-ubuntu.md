---
title: "ubuntu下安装python3.7"
date:       2018-08-19
tags:
	- Python
	- background
	- ubuntu
---
 
<h3 id="1">1.准备</h3>
<p>在安装之前，请使用以下命令安装Python的先决条件。</p>
<pre data-spm-anchor-id="a2c4e.11153940.0.i2.1e477fd2pcGCTX"><code class="hljs sql" data-spm-anchor-id="a2c4e.11153940.0.i0.1e477fd2pcGCTX">sudo apt-get <span class="hljs-keyword">install</span> <span class="hljs-keyword">build</span>-essential checkinstall
sudo apt-<span class="hljs-keyword">get</span> <span class="hljs-keyword">install</span> libreadline-gplv2-dev libncursesw5-dev libssl-dev \
    libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev</code></pre>
<h3 id="2">2.安装</h3>
<p>使用<a href="https://yq.aliyun.com/go/articleRenderRedirect?url=https%3A%2F%2Fwww.python.org%2F" data-url="https://www.python.org/">python</a>官方站点的以下命令下载Python。您也可以下载最新版本代替下面指定的版本。</p>
<pre><code class="hljs nginx"><span class="hljs-attribute">cd</span> /usr/src
sudo wget https://www.python.org/ftp/python/3.7.0/Python-3.7.0.tgz

sudo tar xzf Python-<span class="hljs-number">3</span>.<span class="hljs-number">7</span>.<span class="hljs-number">0</span>.tgz
</code></pre>
<h3 id="3">3. 编译</h3>
<p>使用下面的命令集来使用altinstall在您的系统上编译python源代码。</p>
<pre><code class="hljs bash"><span class="hljs-built_in">cd</span> Python-3.7.0
sudo ./configure --enable-optimizations
sudo make altinstall</code></pre>
<p>make altinstall用于防止替换默认的python二进制文件/ usr / bin / python。</p>
<h3 id="4">4.检查Python版本</h3>
<pre><code class="hljs css"><span class="hljs-selector-tag">python3</span><span class="hljs-selector-class">.7</span> <span class="hljs-selector-tag">-V</span></code></pre>


### 参考文献  
原文链接：[云栖社区-Ubuntu安装python 3.7](https://yq.aliyun.com/articles/675910) 