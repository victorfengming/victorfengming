---
title: "在ubuntu下安装mysql数据库"
cover: "/img/lynk/62.jpg"
date:       2019-10-09
tags:
	- database
	- mysql
	- solution
	- ubuntu
---

<div class="content-intro view-box "><p>Ubuntu是一个比较流行的Linux操作系统，不仅简单易用，而且和Windows相容性非常好。那么在ubuntu下如何安装mysql数据库呢？<br></p><p>在Ubuntu上安装mysql数据库，一般分为两种方法，分别是使用Ubuntu&nbsp;Software&nbsp;Center或者apt命令来安装，而且过程都相对比较简单。
</p><p><br></p><p><b>1、使用Ubuntu&nbsp;Software&nbsp;Center安装
</b></p><p>打开Ubuntu&nbsp;Software&nbsp;Center，在右上角的搜索框查询mysql，然后选定MySQL&nbsp;Server，点击安装即可。
</p><p><br></p><p><b>2、使用apt命令安装
</b></p><p>打开终端执行&nbsp;”sudo&nbsp;apt-get&nbsp;install&nbsp;mysql-server“&nbsp;即可。
</p><p><br></p><p><b>MySQL初始配置
</b></p><p>在成功安装mysql后，可以直接使用root账户登录，注意这个账户是默认没有密码的。因此为了数据库的安全，需要第一时间给root用户设置密码。
</p><pre lang="sql" style="max-width: 100%;"><code class="sql hljs">mysql&gt; <span class="hljs-keyword">GRANT</span> ALL <span class="hljs-keyword">PRIVILEGES</span> <span class="hljs-keyword">ON</span> *.* <span class="hljs-keyword">TO</span> root@localhost <span class="hljs-keyword">IDENTIFIED</span> <span class="hljs-keyword">BY</span> <span class="hljs-string">"&lt;password&gt;"</span>;</code></pre><p>将以上命令中的&lt;password&gt;替换为你要设定的密码即可。设置密码后，如果再以root用户登录就需要输入密码了，如：
</p><pre lang="sql" style="max-width: 100%;"><code class="sql hljs">$ mysql -u rootERROR 1045 (28000): Access denied for user 'root'@'localhost' (using password: NO)$ mysql -u root -pEnter password: Welcome to the MySQL monitor.  Commands <span class="hljs-keyword">end</span> <span class="hljs-keyword">with</span> ; or \g.Your MySQL connection id is 75Server version: 5.5.34-0ubuntu0.13.10.1 (Ubuntu)Copyright (c) 2000, 2013, Oracle and/or its affiliates. All rights reserved.Oracle is a registered trademark of Oracle Corporation and/or itsaffiliates. Other names may be trademarks of their respectiveowners.Type '<span class="hljs-keyword">help</span>;' or '\h' for help. <span class="hljs-keyword">Type</span> <span class="hljs-string">'\c'</span> <span class="hljs-keyword">to</span> <span class="hljs-keyword">clear</span> the <span class="hljs-keyword">current</span> <span class="hljs-keyword">input</span> statement.mysql&gt; </code></pre><p><br></p><p><b>建立数据库独立用户
</b></p><p>root用户拥有数据库的所有操作权限，因此不能轻易给别人用。在一个MySQL实例中，我们可以创建多个数据库，而这些数据库可能会分属不同的项目，那么每个数据库的操作角色也就不一样。对此，我们可以针对不同的数据库，去指定用户进行访问。
</p><pre lang="sql" style="max-width: 100%;"><code class="sql hljs">首先使用root角色创建一个数据库mysql&gt; <span class="hljs-keyword">create</span> <span class="hljs-keyword">database</span> db_web_monitor然后将这个数据库授予一个叫xavier的用户使用mysql&gt; <span class="hljs-keyword">GRANT</span> ALL <span class="hljs-keyword">PRIVILEGES</span> <span class="hljs-keyword">ON</span> db_web_monitor.* <span class="hljs-keyword">TO</span> xavier@localhost <span class="hljs-keyword">IDENTIFIED</span> <span class="hljs-keyword">BY</span> <span class="hljs-string">"xavier"</span>;</code></pre><p>这样就可以使用xavier用户，密码为xavier在本机登录MySQL操作db_web_monitor数据库了。
</p><pre lang="sql" style="max-width: 100%;"><code class="sql hljs">$ mysql -u xavierERROR 1045 (28000): Access denied for user 'xavier'@'localhost' (using password: NO)$ mysql -u xavier -pEnter password: Welcome to the MySQL monitor.  Commands <span class="hljs-keyword">end</span> <span class="hljs-keyword">with</span> ; or \g.Your MySQL connection id is 77Server version: 5.5.34-0ubuntu0.13.10.1 (Ubuntu)Copyright (c) 2000, 2013, Oracle and/or its affiliates. All rights reserved.Oracle is a registered trademark of Oracle Corporation and/or itsaffiliates. Other names may be trademarks of their respectiveowners.Type '<span class="hljs-keyword">help</span>;' or '\h' for help. <span class="hljs-keyword">Type</span> <span class="hljs-string">'\c'</span> <span class="hljs-keyword">to</span> <span class="hljs-keyword">clear</span> the <span class="hljs-keyword">current</span> <span class="hljs-keyword">input</span> statement.mysql&gt; <span class="hljs-keyword">show</span> <span class="hljs-keyword">databases</span>;+<span class="hljs-comment">--------------------+| Database           |+--------------------+| information_schema || db_web_monitor     || test               |+--------------------+3 rows in set (0.00 sec)mysql&gt; </span></code></pre><p><b>开放远程登录权限
</b></p><p>1.&nbsp;首先修改MySQL的配置文件，允许监听远程登录。
</p><pre lang="sql" style="max-width: 100%;"><code class="sql hljs">$ sudo vi /etc/mysql/my.cnf找到bind-address所在行 45 # Instead of skip-networking the default is now to listen only on 46 # localhost which is more compatible and is not less secure. 47 bind-address        = 127.0.0.1将 bind-address值修改为本机IP即可。注意注释说明，如果是较老版本的MySQL，此处就应该是skip-networking，直接将其注释即可。</code></pre><p>2.&nbsp;授予用户远程登录权限。
</p><pre lang="sql" style="max-width: 100%;"><code class="sql hljs">mysql&gt;<span class="hljs-keyword">GRANT</span> ALL <span class="hljs-keyword">PRIVILEGES</span> <span class="hljs-keyword">ON</span> db_web_monitor.* <span class="hljs-keyword">TO</span> xavier@<span class="hljs-string">"%"</span> <span class="hljs-keyword">IDENTIFIED</span> <span class="hljs-keyword">BY</span> <span class="hljs-string">"xavier"</span>;</code></pre><p>如此这般，xavier用户就可以在任意主机通过IP访问到本机MySQL，对db_web_monitor数据库进行操作了</p><p><br></p><p><b>推荐阅读：</b></p><p><a href="https://www.w3cschool.cn/ubuntu/" target="_blank">Ubuntu官方帮助文档</a><br></p><p><a href="https://www.w3cschool.cn/mysql/" target="_blank">MySQL教程</a></p><p><br></p></div>

