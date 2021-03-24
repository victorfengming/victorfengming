---
title: "PHP MySQL 连接数据库"  
cover: "/img/lynk/74.jpg"
date:       2019-10-04
tags:
	- database
	- mysql
	- php
---

<div>
<h2>连接到一个 MySQL 数据库</h2>

<p>在您能够访问并处理数据库中的数据之前，您必须创建到达数据库的连接。</p>

<p>在 PHP 中，这个任务通过 mysql_connect() 函数完成。</p>

<h3>语法</h3>
<pre>mysql_connect(servername,username,password);</pre>

<table class="dataintable">
<tbody><tr>
<th>参数</th>
<th>描述</th>
</tr>

<tr>
<td>servername</td>
<td>可选。规定要连接的服务器。默认是 "localhost:3306"。</td>
</tr>

<tr>
<td>username</td>
<td>可选。规定登录所使用的用户名。默认值是拥有服务器进程的用户的名称。</td>
</tr>

<tr>
<td>password</td>
<td>可选。规定登录所用的密码。默认是 ""。</td>
</tr>
</tbody></table>

<p class="note"><span>注释：</span>虽然还存在其他的参数，但上面列出了最重要的参数。请访问 W3School 提供的 <a href="/php/php_ref_mysql.asp" title="PHP MySQL 函数">PHP MySQL 参考手册</a>，获得更多的细节信息。</p>

<h3>例子</h3>
<p>在下面的例子中，我们在一个变量中 ($con) 存放了在脚本中供稍后使用的连接。如果连接失败，将执行 "die" 部分：</p>

<pre>&lt;?php
$con = mysql_connect("localhost","peter","abc123");
if (!$con)
  {
  die('Could not connect: ' . mysql_error());
  }

// some code

?&gt;</pre>
</div>

<div>
<h2>关闭连接</h2>

<p>脚本一结束，就会关闭连接。如需提前关闭连接，请使用 mysql_close() 函数。</p>

<pre>&lt;?php
$con = mysql_connect("localhost","peter","abc123");
if (!$con)
  {
  die('Could not connect: ' . mysql_error());
  }

// some code

mysql_close($con);
?&gt;</pre>
</div>

### 相关推荐

[PHP MySQL 连接数据库](https://victorfengming.gitee.io/blog/php-mysql-connect-database/)

[PHP MySQL Insert Into](https://victorfengming.gitee.io/blog/php-mysql-insert/)