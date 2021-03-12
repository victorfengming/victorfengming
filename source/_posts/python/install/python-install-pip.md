---
title: "Python pip 安装与使用"
date:       2018-10-12
tags:
	- Python
	- solution
	- basis
---





* content
{:toc}






### 起步

<div class="article-intro">
                    <p>pip 是 Python 包管理工具，该工具提供了对Python 包的查找、下载、安装、卸载的功能。</p>

<p>目前如果你在 <a target="_blank" href="https://www.python.org">python.org</a> 下载最新版本的安装包，则是已经自带了该工具。</p>

<p>Python 2.7.9 +  或 Python 3.4+  以上版本都自带 pip 工具。</p>
<p>pip 官网：<a href="https://pypi.org/project/pip/" target="_blank">https://pypi.org/project/pip/</a></p>
<p>你可以通过以下命令来判断是否已安装：</p>
<pre class="prettyprint prettyprinted" style=""><span class="pln">pip </span><span class="pun">--</span><span class="pln">version</span></pre>

<p>如果你还未安装，则可以使用以下方法来安装：</p>
<pre class="prettyprint prettyprinted" style=""><span class="pln">$ curl https</span><span class="pun">:</span><span class="com">//bootstrap.pypa.io/get-pip.py -o get-pip.py   # 下载安装脚本</span><span class="pln">
$ sudo python </span><span class="kwd">get</span><span class="pun">-</span><span class="pln">pip</span><span class="pun">.</span><span class="pln">py    </span><span class="com"># 运行安装脚本</span></pre>



<blockquote><p><strong>注意：</strong>用哪个版本的 Python 运行安装脚本，pip 就被关联到哪个版本，如果是 Python3 则执行以下命令：</p>

<pre class="prettyprint prettyprinted" style=""><span class="pln">$ sudo python3 </span><span class="kwd">get</span><span class="pun">-</span><span class="pln">pip</span><span class="pun">.</span><span class="pln">py    </span><span class="com"># 运行安装脚本。</span></pre>

<p>一般情况 pip 对应的是 Python 2.7，pip3 对应的是 Python 3.x。</p></blockquote>




<p>部分 Linux 发行版可直接用包管理器安装 pip，如 Debian 和 Ubuntu：</p>

<pre class="prettyprint prettyprinted" style=""><span class="pln">sudo apt</span><span class="pun">-</span><span class="kwd">get</span><span class="pln"> install python</span><span class="pun">-</span><span class="pln">pip</span></pre>
<h3>pip 最常用命令
</h3>
<p><strong>显示版本和路径</strong></p>
<pre class="prettyprint prettyprinted" style=""><span class="pln">pip </span><span class="pun">--</span><span class="pln">version</span></pre>  

<p><strong>获取帮助</strong></p>

<pre class="prettyprint prettyprinted" style=""><span class="pln">pip </span><span class="pun">--</span><span class="pln">help</span></pre>


<p><strong>升级 pip</strong></p>
<pre class="prettyprint prettyprinted" style=""><span class="pln">pip install </span><span class="pun">-</span><span class="pln">U pip</span></pre>



<blockquote><p>如果这个升级命令出现问题 ，可以使用以下命令：</p>
<pre class="prettyprint prettyprinted" style=""><span class="pln">sudo easy_install </span><span class="pun">--</span><span class="pln">upgrade pip</span></pre> </blockquote>







<p><strong>安装包</strong> </p>
<pre class="prettyprint prettyprinted" style=""><span class="pln">pip install </span><span class="typ">SomePackage</span><span class="pln">              </span><span class="com"># 最新版本</span><span class="pln">
pip install </span><span class="typ">SomePackage</span><span class="pun">==</span><span class="lit">1.0</span><span class="pun">.</span><span class="lit">4</span><span class="pln">       </span><span class="com"># 指定版本</span><span class="pln">
pip install </span><span class="str">'SomePackage&gt;=1.0.4'</span><span class="pln">     </span><span class="com"># 最小版本</span></pre>
<p>比如我要安装 Django。用以下的一条命令就可以，方便快捷。</p>
<pre class="prettyprint prettyprinted" style=""><span class="pln">pip install </span><span class="typ">Django</span><span class="pun">==</span><span class="lit">1.7</span></pre>
<p><strong>升级包</strong> </p>
 <pre class="prettyprint prettyprinted" style=""><span class="pln">pip install </span><span class="pun">--</span><span class="pln">upgrade </span><span class="typ">SomePackage</span></pre>

<p>升级指定的包，通过使用==, &gt;=, &lt;=, &gt;, &lt; 来指定一个版本号。</p>

<p><strong>卸载包</strong> </p>
<pre class="prettyprint prettyprinted" style=""><span class="pln">pip uninstall </span><span class="typ">SomePackage</span></pre>
<p><strong>搜索包</strong></p>
<pre class="prettyprint prettyprinted" style=""><span class="pln">pip search </span><span class="typ">SomePackage</span></pre>
<p><strong>显示安装包信息</strong></p>
<pre class="prettyprint prettyprinted" style=""><span class="pln">pip show </span></pre> 

<p><strong>查看指定包的详细信息</strong></p>
<pre class="prettyprint prettyprinted" style=""><span class="pln">pip show </span><span class="pun">-</span><span class="pln">f </span><span class="typ">SomePackage</span></pre>


<p><strong>列出已安装的包</strong></p>
<pre class="prettyprint prettyprinted" style=""><span class="pln">pip list</span></pre>

<p>
<strong>查看可升级的包</strong></p>
<pre class="prettyprint prettyprinted" style=""><span class="pln">pip list </span><span class="pun">-</span><span class="pln">o</span></pre>

<h3>注意事项</h3>
<p>如果 Python2 和 Python3 同时有 pip，则使用方法如下：</p>
 
<p>Python2：</p>

<pre class="prettyprint prettyprinted" style=""><span class="pln">python2 </span><span class="pun">-</span><span class="pln">m pip install XXX</span></pre>

<p>Python3:</p>

<pre class="prettyprint prettyprinted" style=""><span class="pln">python3 </span><span class="pun">-</span><span class="pln">m pip install XXX</span></pre>
                </div>