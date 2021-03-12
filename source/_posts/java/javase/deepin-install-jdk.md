---
title: 'Deepin下java开发环境部署'
cover: "/img/lynk/9.jpg"
date:       2019-09-04
tags:
	- Java
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

<h3><span class="mw-headline" id=".E7.AE.80.E4.BB.8B">简介</span></h3>
<p>本经验由深度论坛用户(zhang12345shun)分享，<a rel="nofollow" class="external text" href="https://bbs.deepin.org/forum.php?mod=viewthread&amp;tid=36225">原文地址</a></p>
<h3><span class="mw-headline" id=".E6.AD.A3.E6.96.87">正文</span></h3>
<h3><span class="mw-headline" id="SUN_JDK.EF.BC.88.E7.8E.B0.E5.B7.B2.E6.94.B9.E5.90.8DOracle_JDK.EF.BC.89">SUN JDK（现已改名Oracle JDK）</span></h3>
<p>1.下载Sun版JDK压缩包（.tar.gz），选择其中的32/64位Linux版本。</p>
<p>2.将其解压缩：</p>
<p><code>sudo tar -zxvf ~/Downloads/jdk-8u45-linux-i586.tar.gz -C /usr/lib</code> </p>
<p>其中参数-C后面的路径是解压缩的目标路径。</p>
<p>3.根据官网的说法：</p>
<blockquote>
<p>Starting with version 8u40, the JDK installation is integrated with the alternatives framework and after installation, the alternatives framework is updated to reflect the binaries from the recently installed JDK. Java commands such as java, javac, javadoc, and javap can be invoked from the command line.  </p>
</blockquote>
<p>所以：</p>
<pre><code>sudo update-alternatives --install /usr/bin/java java  /usr/lib/jdk1.8.0_66/bin/java 1000 
sudo update-alternatives --install /usr/bin/javac javac  /usr/lib/jdk1.8.0_66/bin/javac 1000</code></pre>
<p>现在可以验证一下JDK安装是否已成功 </p>
<p><code>java -version</code></p>
<h3><span class="mw-headline" id="tomact_.E5.AE.89.E8.A3.85.E5.92.8C.E4.BD.BF.E7.94.A8">tomact 安装和使用</span></h3>
<p>1.下载并解压缩到部署位置(8.0.30)</p>
<p>2.配置环境变量</p>
<p><code>startup.sh-----&gt;catalina.sh-----&gt;setclassspath.shJAVA_HOME=/usr/lib/jdk1.8.0_66JRE_HOME=$JAVA_HOME/jre</code></p>
<ul>
<li>备注：这里的配置可以不写（如果jdk是8u40及以后版本） </li>
</ul>
<p>3.启动tomcat： </p>
<p><code>sudo ./bin/startup.sh</code></p>
<p>4.关闭tomcat： </p>
<p><code>sudo ./bin/shutdown.sh</code></p>
<p>5.最后，验证tomcat关闭是否成功：</p>
<p>在浏览器中输入：<a rel="nofollow" class="external free" href="http://localhost:8080/">http://localhost:8080/</a></p>
<h3><span class="mw-headline" id="MYSQL.E5.AE.89.E8.A3.85.E5.92.8C.E4.BD.BF.E7.94.A8">MYSQL安装和使用</span></h3>
<p>1.下载并解压缩 </p>
<p><code>sudo tar -xzvf mysql-6.0.11-alpha-linux-x86_64-glibc23.tar.gz -C destdir</code></p>
<p>2.新增用户mysql和组mysql </p>
<pre><code>sudo groupadd mysql 
sudo useradd -g mysql mysql</code></pre>
<p>3.创建链接 </p>
<pre><code>cd /usr/local 
sudo ln -s /opt/mysql-6.0.11-alpha-linux-x86_64-glibc23/ mysql</code></pre>
<p>4.改变mysql文件夹own group </p>
<pre><code>sudo chown -R mysql . 
sudo chgrp -R mysql .</code></pre>
<p>5.执行初始化脚本 </p>
<p><code>scripts/mysql_install_db –user=mysql</code></p>
<p>6.改变文件夹权限 </p>
<pre><code>chown -R root . 
chown -R mysql data</code></pre>
<p>7.配置mysql环境 </p>
<p>使用自带的配置文件复制到/etc 目录下比如：</p>
<p><code>cp support-files/my-medium.cnf /etc/my.cnf</code></p>
<p>根据内存不同使用不同的配置文件。一般建议使用 </p>
<p><strong> my-larger.cnf </strong> </p>
<ul>
<li>说明：会占用系统内存512M，运行主要的进行。</li>
</ul>
<p><strong> my-medium.cnf </strong> </p>
<ul>
<li>说明：mysql平时只占用系统内存在【32M～64M】之间，或者和其他程序一起工作时比如 web server .占用内存不会超过128M </li>
</ul>
<p><strong> my-small.cnf </strong> </p>
<ul>
<li>说明：只占用系统的很小内存（&lt;=64M）,只运行重要的守护进程。不会占用太多的资源 </li>
</ul>
<p>8.启动服务 </p>
<pre><code>bin/mysqld_safe –user=mysql &amp; //启动服务 
bin/mysqladmin -u root password ‘new_password’ //初始化root密码</code></pre>
<p>9.开机自启动 </p>
<p>复制服务脚本&nbsp;: <code>cp support-files/mysql.server /etc/init.d/mysql</code></p>
<p>取消自启动:<code>sudo update-rc.d -f mysql.server remove</code></p>
<p>把 /usr/local/mysql/bin/mysql 命令加到用户命令中 </p>
<p><code>sudo ln -s /usr/local/mysql/bin/mysql /usr/local/bin/mysql</code></p>
<p>现在就直接可以使用 mysql 命令了 </p>
<p><code>mysql -u root -p</code></p>
<h3><span class="mw-headline" id="Eclipse_.E5.AE.89.E8.A3.85.E4.BD.BF.E7.94.A8">Eclipse 安装使用</span></h3>
<p>1.安装JDK8，具体过程参考上面
2.下载 Eclipse 最新版http://www.eclipse.org/downloads/ </p>
<p>解压 Eclipse:</p>
<p><code>sudo tar -zxvf ~/Downloads/eclipse-*.tar.gz</code></p>
<p>3.创建 Eclipse 快捷方式 </p>
<p>在终端中执行如下命令 </p>
<p><code>sudo gedit /usr/share/applications/eclipse.desktop</code></p>
<p>粘贴并保存如下内容 </p>
<pre><code>[Desktop Entry] 
Type=Application 
Name=Eclipse 
Comment=Eclipse Integrated Development Environment 
Icon=eclipse 
Exec=/opt/eclipse/eclipse 
Terminal=false 
Categories=Development;IDE;Java; </code></pre>
<p>至此，我们就将最新版本的 Eclipse 安装完成</p>
<h3><span class="mw-headline" id="MAVEN.E5.AE.89.E8.A3.85">MAVEN安装</span></h3>
<p>1.下载并加压包到安装位置 exp:/usr/local/</p>
<p>2.配置命令连接符</p>
<p><code>sudo update-alternatives --install /usr/bin/mvn mvn /opt/apache-maven-3.3.9/bin/mvn 1000</code></p>
<p>3.配置默认jdk版本和默认编译级别在目录conf/setting.xml中配置</p>
<pre><code>&lt;profile&gt;
    &lt;id&gt;jdk-1.8&lt;/id&gt;
    &lt;activation&gt;
        &lt;activeByDefault&gt;true&lt;/activeByDefault&gt;
        &lt;jdk&gt;1.8&lt;/jdk&gt;
    &lt;/activation&gt;
    &lt;properties&gt;      
        &lt;maven.compiler.source&gt;1.8&lt;/maven.compiler.source&gt;
        &lt;maven.compiler.target&gt;1.8&lt;/maven.compiler.target&gt;            
        &lt;maven.compiler.compilerVersion&gt;1.8&lt;/maven.compiler.compilerVersion&gt;
    &lt;/properties&gt;
&lt;/profile&gt;</code></pre>

<!-- 
NewPP limit report
Cached time: 20190903123746
Cache expiry: 86400
Dynamic content: false
CPU time usage: 0.008 seconds
Real time usage: 0.009 seconds
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

<!-- Saved in parser cache with key mediawiki:pcache:idhash:471-0!*!*!!zh-cn!*!* and timestamp 20190903123746 and revision id 1689
 -->
</div>                </div>
            </section>