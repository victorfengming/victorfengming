---
title: "PHP MySQL 创建数据库和表"  
date:       2019-10-04
tags:
	- database
	- mysql
	- php
---

<div id="maincontent">

<div id="intro">
<p><strong>数据库存有一个或多个表。</strong></p>
</div>

<div>
<h2>创建数据库</h2>

<p>CREATE DATABASE 语句用于在 MySQL 中创建数据库。</p>

<h3>语法</h3>
<pre>CREATE DATABASE database_name</pre>

<p>为了让 PHP 执行上面的语句，我们必须使用 mysql_query() 函数。此函数用于向 MySQL 连接发送查询或命令。</p>

<h3>例子</h3>
<p>在下面的例子中，我们创建了一个名为 "my_db" 的数据库：</p>

<pre>&lt;?php
$con = mysql_connect("localhost","peter","abc123");
if (!$con)
  {
  die('Could not connect: ' . mysql_error());
  }

if (mysql_query("CREATE DATABASE my_db",$con))
  {
  echo "Database created";
  }
else
  {
  echo "Error creating database: " . mysql_error();
  }

mysql_close($con);
?&gt;</pre>
</div>

<div>
<h2>创建表</h2>

<p>CREATE TABLE 用于在 MySQL 中创建数据库表。</p>

<h3>语法</h3>
<pre>CREATE TABLE table_name
(
column_name1 data_type,
column_name2 data_type,
column_name3 data_type,
.......
)</pre>

<p>为了执行此命令，我必须向 mysql_query() 函数添加 CREATE TABLE 语句。</p>

<h3>例子</h3>
<p>下面的例子展示了如何创建一个名为 "Persons" 的表，此表有三列。列名是 "FirstName", "LastName" 以及 "Age"：</p>

<pre>&lt;?php
$con = mysql_connect("localhost","peter","abc123");
if (!$con)
  {
  die('Could not connect: ' . mysql_error());
  }

// Create database
if (mysql_query("CREATE DATABASE my_db",$con))
  {
  echo "Database created";
  }
else
  {
  echo "Error creating database: " . mysql_error();
  }

// Create table in my_db database
mysql_select_db("my_db", $con);
$sql = "CREATE TABLE Persons&nbsp;
(
FirstName varchar(15),
LastName varchar(15),
Age int
)";
mysql_query($sql,$con);

mysql_close($con);
?&gt;</pre>

<p class="important"><span>重要事项：</span>在创建表之前，必须首先选择数据库。通过 mysql_select_db() 函数选取数据库。</p>

<p class="note"><span>注释：</span>当您创建 varchar 类型的数据库字段时，必须规定该字段的最大长度，例如：varchar(15)。</p>
</div>

<div>
<h2>MySQL 数据类型</h2>

<p>下面的可使用的各种 MySQL 数据类型：</p>

<table class="dataintable">
<tbody><tr>
<th style="width:40%">数值类型</th>
<th>描述</th>
</tr>

<tr>
<td>
<ul>
<li>int(size)</li>
<li>smallint(size)</li>
<li>tinyint(size)</li>
<li>mediumint(size)</li>
<li>bigint(size)</li>
</ul>
</td>
<td>仅支持整数。在 size 参数中规定数字的最大值。</td>
</tr>

<tr>
<td>
<ul>
<li>decimal(size,d)</li>
<li>double(size,d)</li>
<li>float(size,d)</li>
</ul>
</td>
<td>
<p>支持带有小数的数字。</p>
<p>在 size 参数中规定数字的最大值。在 d 参数中规定小数点右侧的数字的最大值。</p>
</td>
</tr>
</tbody></table>

<table class="dataintable">
<tbody><tr>
<th style="width:40%">文本数据类型</th>
<th>描述</th>
</tr>

<tr>
<td>char(size)</td>
<td>
<p>支持固定长度的字符串。（可包含字母、数字以及特殊符号）。</p>
<p>在 size 参数中规定固定长度。</p>
</td>
</tr>

<tr>
<td>varchar(size)</td>
<td>
<p>支持可变长度的字符串。（可包含字母、数字以及特殊符号）。</p>
<p>在 size 参数中规定最大长度。</p>
</td>
</tr>

<tr>
<td>tinytext</td>
<td>支持可变长度的字符串，最大长度是 255 个字符。</td>
</tr>

<tr>
<td>
<ul>
<li>text</li>
<li>blob</li>
</ul>
</td>
<td>支持可变长度的字符串，最大长度是 65535 个字符。</td>
</tr>

<tr>
<td>
<ul>
<li>mediumtext</li>
<li>mediumblob</li>
</ul>
</td>
<td>支持可变长度的字符串，最大长度是 16777215 个字符。</td>
</tr>

<tr>
<td>
<ul>
<li>longtext</li>
<li>longblob</li>
</ul>
</td>
<td>支持可变长度的字符串，最大长度是 4294967295 个字符。</td>
</tr>
</tbody></table>

<table class="dataintable">
<tbody><tr>
<th style="width:40%">日期数据类型</th>
<th>描述</th>
</tr>

<tr>
<td>
<ul>
<li>date(yyyy-mm-dd)</li>
<li>datetime(yyyy-mm-dd hh:mm:ss)</li>
<li>timestamp(yyyymmddhhmmss)</li>
<li>time(hh:mm:ss)</li>
</ul>
</td>
<td>支持日期或时间</td>
</tr>
</tbody></table>

<table class="dataintable">
<tbody><tr>
<th style="width:40%">杂项数据类型</th>
<th>描述</th>
</tr>

<tr>
<td>enum(value1,value2,ect)</td>
<td>ENUM 是 ENUMERATED 列表的缩写。可以在括号中存放最多 65535 个值。</td>
</tr>

<tr>
<td>set</td>
<td>SET 与 ENUM 相似。但是，SET 可拥有最多 64 个列表项目，并可存放不止一个 choice</td>
</tr>
</tbody></table>
</div>

<div>
<h2>主键和自动递增字段</h2>

<p>每个表都应有一个主键字段。</p>

<p>主键用于对表中的行进行唯一标识。每个主键值在表中必须是唯一的。此外，主键字段不能为空，这是由于数据库引擎需要一个值来对记录进行定位。</p>

<p>主键字段永远要被编入索引。这条规则没有例外。你必须对主键字段进行索引，这样数据库引擎才能快速定位给予该键值的行。</p>

<p>下面的例子把 personID 字段设置为主键字段。主键字段通常是 ID 号，且通常使用 AUTO_INCREMENT 设置。AUTO_INCREMENT 会在新记录被添加时逐一增加该字段的值。要确保主键字段不为空，我们必须向该字段添加 NOT NULL 设置。</p>

<h3>例子</h3>
<pre>$sql = "CREATE TABLE Persons&nbsp;
(
personID int NOT NULL AUTO_INCREMENT, 
PRIMARY KEY(personID),
FirstName varchar(15),
LastName varchar(15),
Age int
)";

mysql_query($sql,$con);</pre>
</div>

<div id="bpn">
<ul class="prenext">
<li class="pre"><a href="/php/php_mysql_connect.asp" title="PHP MySQL 连接数据库">MySQL Connect</a></li>
<li class="next"><a href="/php/php_mysql_insert.asp" title="PHP MySQL Insert Into">MySQL Insert</a></li>
</ul>
</div>

</div>

### 相关推荐

[PHP MySQL 连接数据库](https://victorfengming.gitee.io/2019/10/04/php-mysql-connect-database/)

[PHP MySQL Insert Into](https://victorfengming.gitee.io/2019/10/04/php-mysql-insert/)
