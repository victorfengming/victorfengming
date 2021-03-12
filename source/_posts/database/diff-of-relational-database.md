---
title: "关于关系型数据库和非关系型数据库的区别浅析"
date:       2019-09-26
tags:
	- database
	- basis
	- nosql
---

<div class="post">
            <h1 class="postTitle">
                
<a id="cb_post_title_url" class="postTitle2" href="https://www.cnblogs.com/wuyepeng/p/9744393.html">原文链接</a>

            </h1>
            <div class="clear"></div>
            <div class="postBody">
                
<div id="cnblogs_post_body" class="blogpost-body ">
    <pre class="best-text mb-10">1.关系型数据库通过外键关联来建立表与表之间的关系，<br>2.非关系型数据库通常指数据以对象的形式存储在数据库中，而对象之间的关系通过每个对象自身的属性来决定</pre>
<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 比如 有一个学生的数据：</p>
<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 姓名：张三，性别：男，学号：12345，班级：二年级一班</p>
<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 还有一个班级的数据：</p>
<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 班级：二年级一班，班主任：李四</p>
<p>&nbsp;关系型数据库中，我们创建学生表和班级表来存这两条数据，并且学生表中的班级存储的是班级表中的主键。</p>
<p>非关系型数据库中，我们创建两个对象，一个是学生对象，一个是班级对象，用代码表示如下：</p>
<div class="cnblogs_Highlighter sh-gutter">
<div><div id="highlighter_214897" class="syntaxhighlighter  cpp"><div class="toolbar"><span><a href="#" class="toolbar_item command_help help">?</a></span></div><table border="0" cellpadding="0" cellspacing="0"><tbody><tr><td class="gutter"><div class="line number1 index0 alt2">1</div><div class="line number2 index1 alt1">2</div><div class="line number3 index2 alt2">3</div><div class="line number4 index3 alt1">4</div><div class="line number5 index4 alt2">5</div><div class="line number6 index5 alt1">6</div><div class="line number7 index6 alt2">7</div><div class="line number8 index7 alt1">8</div><div class="line number9 index8 alt2">9</div><div class="line number10 index9 alt1">10</div><div class="line number11 index10 alt2">11</div><div class="line number12 index11 alt1">12</div></td><td class="code"><div class="container"><div class="line number1 index0 alt2"><code class="cpp keyword bold">class</code> <code class="cpp plain">Student {</code></div><div class="line number2 index1 alt1"><code class="cpp spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="cpp plain">String id;</code></div><div class="line number3 index2 alt2"><code class="cpp spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="cpp plain">String name;</code></div><div class="line number4 index3 alt1"><code class="cpp spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="cpp plain">String sex;</code></div><div class="line number5 index4 alt2"><code class="cpp spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="cpp plain">String number;</code></div><div class="line number6 index5 alt1"><code class="cpp spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="cpp plain">String classid;</code></div><div class="line number7 index6 alt2"><code class="cpp plain">}</code></div><div class="line number8 index7 alt1"><code class="cpp keyword bold">class</code> <code class="cpp plain">Grade {</code></div><div class="line number9 index8 alt2"><code class="cpp spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="cpp plain">String id;</code></div><div class="line number10 index9 alt1"><code class="cpp spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="cpp plain">String name;</code></div><div class="line number11 index10 alt2"><code class="cpp spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="cpp plain">String teacher;</code></div><div class="line number12 index11 alt1"><code class="cpp plain">}</code></div></div></td></tr></tbody></table></div></div>
</div>
<p>　　</p>
<p>通过设置Student类的classid等于Grade类的id来建立这种关系；</p>
<p>&nbsp;</p>
<p>非关系型数据库中，我们查询一条数据，结果出来一个数组，关系型数据库中，查询一条数据结果是一个对象。</p>
<p>&nbsp;</p>
<table border="1" cellspacing="1" cellpadding="1">
<tbody>
<tr>
<td>数据库<br>类型</td>
<td>特性</td>
<td>优点</td>
<td>缺点</td>

</tr>
<tr>
<td>关系型数据库<br>SQLite、Oracle、mysql</td>
<td>1、关系型数据库，是指采用了关系模型来组织<br>数据的数据库；<br>2、关系型数据库的最大特点就是事务的一致性；<br>3、简单来说，关系模型指的就是二维表格模型，<br>而一个关系型数据库就是由二维表及其之间的联系所组成的一个数据组织。</td>
<td>1、容易理解：二维表结构是非常贴近逻辑世界一个概念，关系模型相对网状、层次等其他模型来说更容易理解；<br>2、使用方便：通用的SQL语言使得操作关系型数据库非常方便；<br>3、易于维护：丰富的完整性(实体完整性、参照完整性和用户定义的完整性)大大减低了数据冗余和数据不一致的概率；<br>4、支持SQL，可用于复杂的查询。</td>
<td>1、为了维护一致性所付出的巨大代价就是其读写性能比较差；<br>2、固定的表结构；<br>3、高并发读写需求；<br>4、海量数据的高效率读写；</td>

</tr>
<tr>
<td>非关系型数据库<br>MongoDb、redis、HBase</td>
<td>1、使用键值对存储数据；<br>2、分布式；<br>3、一般不支持ACID特性；<br>4、非关系型数据库严格上不是一种数据库，应该是一种数据结构化存储方法的集合。</td>
<td>1、无需经过sql层的解析，读写性能很高；<br>2、基于键值对，数据没有耦合性，容易扩展；<br>3、存储数据的格式：nosql的存储格式是key,value形式、文档形式、图片形式等等，文档形式、图片形式等等，而关系型数据库则只支持基础类型。</td>
<td>1、不提供sql支持，学习和使用成本较高；<br>2、无事务处理，附加功能bi和报表等支持也不好；</td>

</tr>

</tbody>

</table>
<p>&nbsp;</p>
<p>注1：数据库事务必须具备ACID特性，ACID是Atomic原子性，Consistency一致性，Isolation隔离性，Durability持久性。</p>
<p>&nbsp;</p>
<p>注2：数据的持久存储，尤其是海量数据的持久存储，还是需要一种关系数据库。</p>
