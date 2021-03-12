---
title: "PHP MySQL Insert Into"  
date:       2019-10-04
tags:
	- database
	- mysql
	- php
---

<div id="maincontent">

<div id="intro">
<p><strong>INSERT INTO 语句用于向数据库表中插入新记录。</strong></p>
</div>

<div>
<h2>向数据库表插入数据</h2>

<p>INSERT INTO 语句用于向数据库表添加新记录。</p>

<h3>语法</h3>
<pre>INSERT INTO table_name
VALUES (value1, value2,....)</pre>

<p>您还可以规定希望在其中插入数据的列：</p>

<pre>INSERT INTO table_name (column1, column2,...)
VALUES (value1, value2,....)</pre>

<p class="note"><span>注释：</span>SQL 语句对大小写不敏感。INSERT INTO 与 insert into 相同。</p>

<p>为了让 PHP 执行该语句，我们必须使用 mysql_query() 函数。该函数用于向 MySQL 连接发送查询或命令。</p>

<h3>例子</h3>
<p>在前面的章节，我们创建了一个名为 "Persons" 的表，有三个列："Firstname", "Lastname" 以及 "Age"。我们将在本例中使用同样的表。下面的例子向 "Persons" 表添加了两个新记录：</p>

<pre>&lt;?php
$con = mysql_connect("localhost","peter","abc123");
if (!$con)
  {
  die('Could not connect: ' . mysql_error());
  }

mysql_select_db("my_db", $con);

mysql_query("INSERT INTO Persons (FirstName, LastName, Age) 
VALUES ('Peter', 'Griffin', '35')");

mysql_query("INSERT INTO Persons (FirstName, LastName, Age) 
VALUES ('Glenn', 'Quagmire', '33')");

mysql_close($con);
?&gt;</pre>
</div>

<div>
<h2>把来自表单的数据插入数据库</h2>

<p>现在，我们创建一个 HTML 表单，这个表单可把新记录插入 "Persons" 表。</p>

<p>这是这个 HTML 表单：</p>

<pre>&lt;html&gt;
&lt;body&gt;

&lt;form action="insert.php" method="post"&gt;
Firstname: &lt;input type="text" name="firstname" /&gt;
Lastname: &lt;input type="text" name="lastname" /&gt;
Age: &lt;input type="text" name="age" /&gt;
&lt;input type="submit" /&gt;
&lt;/form&gt;

&lt;/body&gt;
&lt;/html&gt;</pre>

<p>当用户点击上例中 HTML 表单中的提交按钮时，表单数据被发送到 "insert.php"。"insert.php" 文件连接数据库，并通过 $_POST 变量从表单取回值。然后，mysql_query() 函数执行 INSERT INTO 语句，一条新的记录会添加到数据库表中。</p>

<p>下面是 "insert.php" 页面的代码：</p>

<pre>&lt;?php
$con = mysql_connect("localhost","peter","abc123");
if (!$con)
  {
  die('Could not connect: ' . mysql_error());
  }

mysql_select_db("my_db", $con);

$sql="INSERT INTO Persons (FirstName, LastName, Age)
VALUES
('$_POST[firstname]','$_POST[lastname]','$_POST[age]')";

if (!mysql_query($sql,$con))
  {
  die('Error: ' . mysql_error());
  }
echo "1 record added";

mysql_close($con)
?&gt;</pre>
</div>

<div id="bpn">
<ul class="prenext">
<li class="pre"><a href="/php/php_mysql_create.asp" title="PHP MySQL 创建数据库和表">MySQL Create</a></li>
<li class="next"><a href="/php/php_mysql_select.asp" title="PHP MySQL Select">MySQL Select</a></li>
</ul>
</div>
</div>

### 相关推荐

[PHP MySQL 连接数据库](https://victorfengming.gitee.io/2019/10/04/php-mysql-connect-database/)

[PHP MySQL 创建数据库和表](https://victorfengming.gitee.io/2019/10/04/php-mysql-createtables/)