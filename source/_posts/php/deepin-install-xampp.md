---
title: 'Deepin 搭建php开发环境'
date:       2019-09-04
tags:
	- php
	- deepin
	- solution
---

<section>
                <div class="before">
                    <div class="other">
                    </div>
                </div>
                <div class="new-box">
                    <div id="mw-content-text" lang="zh-CN" dir="ltr" class="mw-content-ltr"><div id="toc" class="toc"><div id="toctitle"><h3>目录</h3></div>

</div>

<h1><span class="mw-headline" id=".E7.AE.80.E4.BB.8B">简介</span></h1>
<p>本词条意在说明如何快速简便地搭建php开发环境。</p>
<h1><span class="mw-headline" id=".E6.AD.A3.E6.96.87">正文</span></h1>
<p>XAMPP是一个把Apache网页服务器与PHP、Perl,phpMyAdmin及MariaDB集合在一起的安装包，允许用户可以在自己的电脑上轻易的建立网页服务器。  -- 百科</p>
<h3><span class="mw-headline" id=".E5.AE.89.E8.A3.85">安装</span></h3>
<p>下载地址： <a rel="nofollow" class="external free" href="https://www.apachefriends.org">https://www.apachefriends.org</a></p>
<p>我们需要选择XAMPP for linux。此处以xampp-linux-x64-7.3.1-0-installer.run为例进行说明。</p>
<p>下载到本地后，打开安装包所在文件夹，在文件夹空白处右击鼠标选择在终端中打开。
然后在终端中执行以下命令：</p>
<pre><code>    $ sudo ./xampp-linux-x64-7.3.1-0-installer.run</code></pre>
<p>如果提示没有这个命令,则是权限不足,执行:</p>
<pre><code>    $ sudo chmod 777 xampp-linux-x64-7.3.1-0-installer.run</code></pre>
<p>然后重新执行上述命令即可</p>
<p>该命令执行后，xampp图形化安装程序便会启动，根据提示安装即可。</p>
<h3><span class="mw-headline" id=".E5.BC.80.E5.90.AFxampp">开启xampp</span></h3>
<p>1）安装完成之后， 程序会自动运行，此时需要手动点击进入manage server界面，点击启动全部选项。</p>
<p>2）在Deepin系统中，XAMPP程序没有图标，故在日常使用时，需要通过命令行启动。命令行如下</p>
<p>$ sudo ./opt/lampp/lampp start         启动</p>
<p>$ sudo ./opt/lampp/lampp restart     重启</p>
<p>$ sudo ./opt/lampp/lampp stop         停止</p>
<h3><span class="mw-headline" id=".E6.B5.8B.E8.AF.95.E6.98.AF.E5.90.A6.E6.88.90.E5.8A.9F">测试是否成功</span></h3>
<p>打开浏览器，在地址栏输入localhost，能打开welcome to xampp网页</p>
<p>打开浏览器，在地址栏输入localhost、phpmyadmin，能打开phpmyadmin管理网页</p>
<p>以上两项均无问题则说明本次环境搭建成功</p>
<h3><span class="mw-headline" id=".E5.A6.82.E4.BD.95.E4.BD.BF.E7.94.A8.E8.AF.A5.E7.8E.AF.E5.A2.83.E5.BC.80.E5.8F.91PHP.E7.A8.8B.E5.BA.8F">如何使用该环境开发PHP程序</span></h3>
<p>在确保XAMPP成功安装并已启动后，可使用命令行在指定文件夹创建php文件</p>
<p>$ sudo touch /opt/lampp/htdocs/name.php</p>
<p>此处在opt/lampp/htdocs文件夹下创建了一个名为name的php程序</p>
<p>！！！需要注意的事，在opt/lampp/apache2文件夹下也有一个htdocs文件夹，在此文件夹下创建的php文件并不能在浏览器中打开。</p>
<p>！！！只有opt/lampp文件夹下的htdocs文件夹里的php文件能被浏览器打开</p>
<h3><span class="mw-headline" id="PHP.E7.BC.96.E8.BE.91.E5.99.A8.E6.8E.A8.E8.8D.90">PHP编辑器推荐</span></h3>
<p>在Deepin系统中可以方便地使用Sublime Text编辑器进行php的编辑</p>

<!-- 
NewPP limit report
Cached time: 20190903053453
Cache expiry: 86400
Dynamic content: false
CPU time usage: 0.004 seconds
Real time usage: 0.006 seconds
Preprocessor visited node count: 1/1000000
Preprocessor generated node count: 4/1000000
Post‐expand include size: 0/2097152 bytes
Template argument size: 0/2097152 bytes
Highest expansion depth: 1/40
Expensive parser function count: 0/100
-->

<!-- 
Transclusion expansion time report (%,ms,calls,template)
100.00%    0.000      1 - -total
-->

<!-- Saved in parser cache with key mediawiki:pcache:idhash:457-0!*!*!!zh-cn!*!* and timestamp 20190903053453 and revision id 1784
 -->
</div>                </div>
            </section>