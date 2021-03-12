---
title: "MySQL ERROR 1698 (28000) 错误"  
date:       2019-10-05
tags:
	- database
	- mysql
	- solution
---

<div id="cnblogs_post_body" class="blogpost-body ">
    <h3>之前MySQL服务端本机上使用密码登陆root账号是没有问题的，但是今天不知道是因为动了哪里，登陆失败并有这个错误代码：</h3>
<div class="cnblogs_code">
<pre>~$ mysql -u root -<span style="color: #000000;">p
Enter password: 
ERROR </span><span style="color: #800080;">1698</span> (<span style="color: #800080;">28000</span>): Access denied <span style="color: #0000ff;">for</span> user <span style="color: #800000;">'</span><span style="color: #800000;">root</span><span style="color: #800000;">'</span>@<span style="color: #800000;">'</span><span style="color: #800000;">localhost</span><span style="color: #800000;">'</span></pre>
</div>
<p>&nbsp;&nbsp;</p>
<h3>解决步骤：</h3>
<p>停止mysql服务</p>
<div class="cnblogs_code">
<pre>~$ <span style="color: #0000ff;">sudo</span> service mysql stop</pre>
</div>
<p>&nbsp;</p>
<p>以安全模式启动MySQL</p>
<div class="cnblogs_code">
<pre>~$ <span style="color: #0000ff;">sudo</span> mysqld_safe --skip-grant-tables &amp;</pre>
</div>
<p>&nbsp;</p>
<h3>MySQL启动之后就可以不用密码登陆了</h3>
<div class="cnblogs_code">
<pre>~$ mysql -<span style="color: #000000;">u root
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection </span><span style="color: #0000ff;">id</span> is <span style="color: #800080;">2</span><span style="color: #000000;">
Server version: </span><span style="color: #800080;">5.7</span>.<span style="color: #800080;">10</span> MySQL Community Server (GPL)</pre>
</div>
<p>&nbsp;</p>
<p>查看一下user表，错误的起因就是在这里， root的plugin被修改成了auth_socket，用密码登陆的plugin应该是mysql_native_password。</p>
<div class="cnblogs_code"><div class="cnblogs_code_toolbar"><span class="cnblogs_code_copy"><a href="javascript:void(0);" onclick="copyCnblogsCode(this)" title="复制代码"><img src="//common.cnblogs.com/img/copycode.gif" alt="复制代码"></a></span></div>
<pre>mysql<span style="color: #808080;">&gt;</span> <span style="color: #0000ff;">select</span> <span style="color: #ff00ff;">user</span>, plugin <span style="color: #0000ff;">from</span> mysql.<span style="color: #ff00ff;">user</span><span style="color: #000000;">;
</span><span style="color: #808080;">+</span><span style="color: #008080;">--</span><span style="color: #008080;">---------+-----------------------+</span>
<span style="color: #808080;">|</span> <span style="color: #ff00ff;">user</span>      <span style="color: #808080;">|</span> plugin                <span style="color: #808080;">|</span>
<span style="color: #808080;">+</span><span style="color: #008080;">--</span><span style="color: #008080;">---------+-----------------------+</span>
<span style="color: #808080;">|</span> root      <span style="color: #808080;">|</span> auth_socket           <span style="color: #808080;">|</span>
<span style="color: #808080;">|</span> mysql.sys <span style="color: #808080;">|</span> mysql_native_password <span style="color: #808080;">|</span>
<span style="color: #808080;">|</span> dev       <span style="color: #808080;">|</span> mysql_native_password <span style="color: #808080;">|</span>
<span style="color: #808080;">+</span><span style="color: #008080;">--</span><span style="color: #008080;">---------+-----------------------+</span>
<span style="color: #800000; font-weight: bold;">3</span> rows <span style="color: #808080;">in</span> <span style="color: #0000ff;">set</span> (<span style="color: #800000; font-weight: bold;">0.01</span> sec)</pre>
<div class="cnblogs_code_toolbar"><span class="cnblogs_code_copy"><a href="javascript:void(0);" onclick="copyCnblogsCode(this)" title="复制代码"><img src="//common.cnblogs.com/img/copycode.gif" alt="复制代码"></a></span></div></div>
<p>&nbsp;</p>
<p>关于auth_socket，在官方有说明：&nbsp;<a href="https://dev.mysql.com/doc/mysql-security-excerpt/5.5/en/socket-authentication-plugin.html" target="_blank">https://dev.mysql.com/doc/mysql-security-excerpt/5.5/en/socket-authentication-plugin.html</a>&nbsp;，反正现在暂时不用它， 那就把这里改了。</p>
<div class="cnblogs_code"><div class="cnblogs_code_toolbar"><span class="cnblogs_code_copy"><a href="javascript:void(0);" onclick="copyCnblogsCode(this)" title="复制代码"><img src="//common.cnblogs.com/img/copycode.gif" alt="复制代码"></a></span></div>
<pre>mysql<span style="color: #808080;">&gt;</span> <span style="color: #0000ff;">update</span> mysql.<span style="color: #ff00ff;">user</span> <span style="color: #0000ff;">set</span> authentication_string<span style="color: #808080;">=</span>PASSWORD(<span style="color: #ff0000;">'</span><span style="color: #ff0000;">newPwd</span><span style="color: #ff0000;">'</span>), plugin<span style="color: #808080;">=</span><span style="color: #ff0000;">'</span><span style="color: #ff0000;">mysql_native_password</span><span style="color: #ff0000;">'</span> <span style="color: #0000ff;">where</span> <span style="color: #ff00ff;">user</span><span style="color: #808080;">=</span><span style="color: #ff0000;">'</span><span style="color: #ff0000;">root</span><span style="color: #ff0000;">'</span><span style="color: #000000;">;
Query OK, </span><span style="color: #800000; font-weight: bold;">1</span> row affected, <span style="color: #800000; font-weight: bold;">1</span> warning (<span style="color: #800000; font-weight: bold;">0.00</span><span style="color: #000000;"> sec)
Rows matched: </span><span style="color: #800000; font-weight: bold;">1</span>  Changed: <span style="color: #800000; font-weight: bold;">1</span>  Warnings: <span style="color: #800000; font-weight: bold;">1</span><span style="color: #000000;">

mysql</span><span style="color: #808080;">&gt;</span> flush <span style="color: #0000ff;">privileges</span><span style="color: #000000;">;
Query OK, </span><span style="color: #800000; font-weight: bold;">0</span> rows affected (<span style="color: #800000; font-weight: bold;">0.00</span> sec)</pre>
<div class="cnblogs_code_toolbar"><span class="cnblogs_code_copy"><a href="javascript:void(0);" onclick="copyCnblogsCode(this)" title="复制代码"><img src="//common.cnblogs.com/img/copycode.gif" alt="复制代码"></a></span></div></div>
<p>&nbsp;</p>
<h3>重启服务，问题就解决了</h3>
<div class="cnblogs_code"><div class="cnblogs_code_toolbar"><span class="cnblogs_code_copy"><a href="javascript:void(0);" onclick="copyCnblogsCode(this)" title="复制代码"><img src="//common.cnblogs.com/img/copycode.gif" alt="复制代码"></a></span></div>
<pre>~$ <span style="color: #0000ff;">sudo</span><span style="color: #000000;"> service mysql stop
...
 </span>* MySQL Community Server <span style="color: #800080;">5.7</span>.<span style="color: #800080;">10</span><span style="color: #000000;"> is stopped
</span>~$ <span style="color: #0000ff;">sudo</span><span style="color: #000000;"> service mysql start
..
 </span>* MySQL Community Server <span style="color: #800080;">5.7</span>.<span style="color: #800080;">10</span><span style="color: #000000;"> is started
</span>~$ mysql -u root -<span style="color: #000000;">p
Enter password: 
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection </span><span style="color: #0000ff;">id</span> is <span style="color: #800080;">2</span><span style="color: #000000;">
Server version: </span><span style="color: #800080;">5.7</span>.<span style="color: #800080;">10</span> MySQL Community Server (GPL)</pre>
<div class="cnblogs_code_toolbar"><span class="cnblogs_code_copy"><a href="javascript:void(0);" onclick="copyCnblogsCode(this)" title="复制代码"><img src="//common.cnblogs.com/img/copycode.gif" alt="复制代码"></a></span></div></div>
<p>&nbsp;</p>
<p>　　　　</p>
</div>