---
title: "MySQL分页查询方法及优化"
cover: "/img/lynk/41.jpg"
date:       2019-10-09
tags:
	- database
	- mysql
	- solution
---

<div class="content-intro view-box "><p>当数据库的数据量很大时，一次性查询结果就会变得很慢，为了提高查询效率，我们可以使用MySQL的分页查询功能。本文就为大家带来MySQL分页查询方法及优化。
    <br>
</p><p><br></p><p><b>推荐阅读：</b></p><p><a href="https://www.w3cschool.cn/mysql21minutes/" target="_blank">21分钟MySQL入门教程</a></p><p><a href="https://www.w3cschool.cn/mysql/" target="_blank">MySQL完整教程</a></p><p><br></p>
<p><b>分页查询方法：</b><br></p>
<p>在MySQL中，分页查询一般都是使用limit子句实现，limit子句声明如下：</p><pre lang="sql" style="max-width: 100%;"><code class="sql hljs"><span class="hljs-keyword">SELECT</span> * <span class="hljs-keyword">FROM</span> <span class="hljs-keyword">table</span> <span class="hljs-keyword">LIMIT</span> [<span class="hljs-keyword">offset</span>,] <span class="hljs-keyword">rows</span> | <span class="hljs-keyword">rows</span> <span class="hljs-keyword">OFFSET</span> <span class="hljs-keyword">offset</span></code></pre>
<p>LIMIT子句可以被用于指定&nbsp;SELECT&nbsp;语句返回的记录数。需注意以下几点：</p>
<p>1、第一个参数指定第一个返回记录行的偏移量</p>
<p>2、第二个参数指定返回记录行的最大数目</p>
<p>3、如果只给定一个参数：它表示返回最大的记录行数目</p>
<p>4、第二个参数为&nbsp;-1&nbsp;表示检索从某一个偏移量到记录集的结束所有的记录行</p>
<p>5、初始记录行的偏移量是0(而不是&nbsp;1)</p>
<p>
    <br>
</p>
<p>下面是一个应用实例：</p><pre lang="sql" style="max-width: 100%;"><code class="sql hljs"><span class="hljs-keyword">select</span> * <span class="hljs-keyword">from</span> orders_history <span class="hljs-keyword">where</span> <span class="hljs-keyword">type</span>=<span class="hljs-number">8</span> <span class="hljs-keyword">limit</span> <span class="hljs-number">1000</span>,<span class="hljs-number">10</span>;</code></pre>
<p>该条语句将会从表&nbsp;orders_history&nbsp;中查询第1000条数据之后的10条数据，也就是第1001条到第1010条数据。</p>
<p>数据表中的记录默认使用主键（一般为id）排序，上面的结果相当于：</p><pre lang="sql" style="max-width: 100%;"><code class="sql hljs"><span class="hljs-keyword">select</span> * <span class="hljs-keyword">from</span> orders_history <span class="hljs-keyword">where</span> <span class="hljs-keyword">type</span>=<span class="hljs-number">8</span> <span class="hljs-keyword">order</span> <span class="hljs-keyword">by</span> <span class="hljs-keyword">id</span> <span class="hljs-keyword">limit</span> <span class="hljs-number">10000</span>,<span class="hljs-number">10</span>;</code></pre>
<p>三次查询时间分别为：</p>
<p>3040&nbsp;ms</p>
<p>3063&nbsp;ms</p>
<p>3018&nbsp;ms</p>
<p>针对这种查询方式，下面测试查询记录量对时间的影响：</p><pre lang="sql" style="max-width: 100%;"><code class="sql hljs"><span class="hljs-keyword">select</span> * <span class="hljs-keyword">from</span> orders_history <span class="hljs-keyword">where</span> <span class="hljs-keyword">type</span>=<span class="hljs-number">8</span> <span class="hljs-keyword">limit</span> <span class="hljs-number">10000</span>,<span class="hljs-number">1</span>;
<span class="hljs-keyword">select</span> * <span class="hljs-keyword">from</span> orders_history <span class="hljs-keyword">where</span> <span class="hljs-keyword">type</span>=<span class="hljs-number">8</span> <span class="hljs-keyword">limit</span> <span class="hljs-number">10000</span>,<span class="hljs-number">10</span>;
<span class="hljs-keyword">select</span> * <span class="hljs-keyword">from</span> orders_history <span class="hljs-keyword">where</span> <span class="hljs-keyword">type</span>=<span class="hljs-number">8</span> <span class="hljs-keyword">limit</span> <span class="hljs-number">10000</span>,<span class="hljs-number">100</span>;
<span class="hljs-keyword">select</span> * <span class="hljs-keyword">from</span> orders_history <span class="hljs-keyword">where</span> <span class="hljs-keyword">type</span>=<span class="hljs-number">8</span> <span class="hljs-keyword">limit</span> <span class="hljs-number">10000</span>,<span class="hljs-number">1000</span>;
<span class="hljs-keyword">select</span> * <span class="hljs-keyword">from</span> orders_history <span class="hljs-keyword">where</span> <span class="hljs-keyword">type</span>=<span class="hljs-number">8</span> <span class="hljs-keyword">limit</span> <span class="hljs-number">10000</span>,<span class="hljs-number">10000</span>;</code></pre>
<p>三次查询时间如下：</p>
<p>查询1条记录：3072ms&nbsp;3092ms&nbsp;3002ms</p>
<p>查询10条记录：3081ms&nbsp;3077ms&nbsp;3032ms</p>
<p>查询100条记录：3118ms&nbsp;3200ms&nbsp;3128ms</p>
<p>查询1000条记录：3412ms&nbsp;3468ms&nbsp;3394ms</p>
<p>查询10000条记录：3749ms&nbsp;3802ms&nbsp;3696ms</p>
<p>另外我还做了十来次查询，从查询时间来看，基本可以确定，在查询记录量低于100时，查询时间基本没有差距，随着查询记录量越来越大，所花费的时间也会越来越多。</p>
<p>
    <br>
</p>
<p>针对查询偏移量的测试：</p><pre lang="sql" style="max-width: 100%;"><code class="sql hljs"><span class="hljs-keyword">select</span> * <span class="hljs-keyword">from</span> orders_history <span class="hljs-keyword">where</span> <span class="hljs-keyword">type</span>=<span class="hljs-number">8</span> <span class="hljs-keyword">limit</span> <span class="hljs-number">100</span>,<span class="hljs-number">100</span>;
<span class="hljs-keyword">select</span> * <span class="hljs-keyword">from</span> orders_history <span class="hljs-keyword">where</span> <span class="hljs-keyword">type</span>=<span class="hljs-number">8</span> <span class="hljs-keyword">limit</span> <span class="hljs-number">1000</span>,<span class="hljs-number">100</span>;
<span class="hljs-keyword">select</span> * <span class="hljs-keyword">from</span> orders_history <span class="hljs-keyword">where</span> <span class="hljs-keyword">type</span>=<span class="hljs-number">8</span> <span class="hljs-keyword">limit</span> <span class="hljs-number">10000</span>,<span class="hljs-number">100</span>;
<span class="hljs-keyword">select</span> * <span class="hljs-keyword">from</span> orders_history <span class="hljs-keyword">where</span> <span class="hljs-keyword">type</span>=<span class="hljs-number">8</span> <span class="hljs-keyword">limit</span> <span class="hljs-number">100000</span>,<span class="hljs-number">100</span>;
<span class="hljs-keyword">select</span> * <span class="hljs-keyword">from</span> orders_history <span class="hljs-keyword">where</span> <span class="hljs-keyword">type</span>=<span class="hljs-number">8</span> <span class="hljs-keyword">limit</span> <span class="hljs-number">1000000</span>,<span class="hljs-number">100</span>;</code></pre>
<p>三次查询时间如下：</p>
<p>查询100偏移：25ms&nbsp;24ms&nbsp;24ms</p>
<p>查询1000偏移：78ms&nbsp;76ms&nbsp;77ms</p>
<p>查询10000偏移：3092ms&nbsp;3212ms&nbsp;3128ms</p>
<p>查询100000偏移：3878ms&nbsp;3812ms&nbsp;3798ms</p>
<p>查询1000000偏移：14608ms&nbsp;14062ms&nbsp;14700ms</p>
<p>随着查询偏移的增大，尤其查询偏移大于10万以后，查询时间急剧增加。</p>
<p>这种分页查询方式会从数据库第一条记录开始扫描，所以越往后，查询速度越慢，而且查询的数据越多，也会拖慢总查询速度。</p>
<p>
    <br>
</p>
<p><b>使用子查询优化
</b>
</p>
<p>这种方式先定位偏移位置的&nbsp;id，然后往后查询，这种方式适用于&nbsp;id&nbsp;递增的情况。</p><pre lang="sql" style="max-width: 100%;"><code class="sql hljs"><span class="hljs-keyword">select</span> * <span class="hljs-keyword">from</span> orders_history <span class="hljs-keyword">where</span> <span class="hljs-keyword">type</span>=<span class="hljs-number">8</span> <span class="hljs-keyword">limit</span> <span class="hljs-number">100000</span>,<span class="hljs-number">1</span>;

<span class="hljs-keyword">select</span> <span class="hljs-keyword">id</span> <span class="hljs-keyword">from</span> orders_history <span class="hljs-keyword">where</span> <span class="hljs-keyword">type</span>=<span class="hljs-number">8</span> <span class="hljs-keyword">limit</span> <span class="hljs-number">100000</span>,<span class="hljs-number">1</span>;

<span class="hljs-keyword">select</span> * <span class="hljs-keyword">from</span> orders_history <span class="hljs-keyword">where</span> <span class="hljs-keyword">type</span>=<span class="hljs-number">8</span> <span class="hljs-keyword">and</span> 
<span class="hljs-keyword">id</span>&gt;=(<span class="hljs-keyword">select</span> <span class="hljs-keyword">id</span> <span class="hljs-keyword">from</span> orders_history <span class="hljs-keyword">where</span> <span class="hljs-keyword">type</span>=<span class="hljs-number">8</span> <span class="hljs-keyword">limit</span> <span class="hljs-number">100000</span>,<span class="hljs-number">1</span>) 
<span class="hljs-keyword">limit</span> <span class="hljs-number">100</span>;

<span class="hljs-keyword">select</span> * <span class="hljs-keyword">from</span> orders_history <span class="hljs-keyword">where</span> <span class="hljs-keyword">type</span>=<span class="hljs-number">8</span> <span class="hljs-keyword">limit</span> <span class="hljs-number">100000</span>,<span class="hljs-number">100</span>;</code></pre>
<p>4条语句的查询时间如下：</p>
<p>第1条语句：3674ms</p>
<p>第2条语句：1315ms</p>
<p>第3条语句：1327ms</p>
<p>第4条语句：3710ms</p>
<p>针对上面的查询需要注意：</p>
<p>1、比较第1条语句和第2条语句：使用&nbsp;select&nbsp;id&nbsp;代替&nbsp;select&nbsp;*&nbsp;速度增加了3倍</p>
<p>2、比较第2条语句和第3条语句：速度相差几十毫秒</p>
<p>3、比较第3条语句和第4条语句：得益于&nbsp;select&nbsp;id&nbsp;速度增加，第3条语句查询速度增加了3倍</p>
<p>这种方式相较于原始一般的查询方法，将会增快数倍。</p>
<p>
    <br>
</p>
<p><b>使用&nbsp;id&nbsp;限定优化
</b>
</p>
<p>这种方式假设数据表的id是连续递增的，则我们根据查询的页数和查询的记录数可以算出查询的id的范围，可以使用&nbsp;id&nbsp;between&nbsp;and&nbsp;来查询：</p><pre lang="sql" style="max-width: 100%;"><code class="sql hljs"><span class="hljs-keyword">select</span> * <span class="hljs-keyword">from</span> orders_history <span class="hljs-keyword">where</span> <span class="hljs-keyword">type</span>=<span class="hljs-number">2</span> 
<span class="hljs-keyword">and</span> <span class="hljs-keyword">id</span> <span class="hljs-keyword">between</span> <span class="hljs-number">1000000</span> <span class="hljs-keyword">and</span> <span class="hljs-number">1000100</span> <span class="hljs-keyword">limit</span> <span class="hljs-number">100</span>;</code></pre>
<p>查询时间：15ms&nbsp;12ms&nbsp;9ms</p>
<p>这种查询方式能够极大地优化查询速度，基本能够在几十毫秒之内完成。限制是只能使用于明确知道id的情况，不过一般建立表的时候，都会添加基本的id字段，这为分页查询带来很多便利。</p>
<p>还可以有另外一种写法：</p><pre lang="sql" style="max-width: 100%;"><code class="sql hljs"><span class="hljs-keyword">select</span> * <span class="hljs-keyword">from</span> orders_history <span class="hljs-keyword">where</span> <span class="hljs-keyword">id</span> &gt;= <span class="hljs-number">1000001</span> <span class="hljs-keyword">limit</span> <span class="hljs-number">100</span>;</code></pre>
<p>当然还可以使用&nbsp;in&nbsp;的方式来进行查询，这种方式经常用在多表关联的时候进行查询，使用其他表查询的id集合，来进行查询：</p><pre lang="sql" style="max-width: 100%;"><code class="sql hljs"><span class="hljs-keyword">select</span> * <span class="hljs-keyword">from</span> orders_history <span class="hljs-keyword">where</span> <span class="hljs-keyword">id</span> <span class="hljs-keyword">in</span>
(<span class="hljs-keyword">select</span> order_id <span class="hljs-keyword">from</span> trade_2 <span class="hljs-keyword">where</span> goods = <span class="hljs-string">'pen'</span>)
<span class="hljs-keyword">limit</span> <span class="hljs-number">100</span>;</code></pre>
<p>这种&nbsp;in&nbsp;查询的方式要注意：某些&nbsp;mysql&nbsp;版本不支持在&nbsp;in&nbsp;子句中使用&nbsp;limit。</p>
<p>
    <br>
</p>
<p><b>关于数据表的id说明
</b>
</p>
<p>一般情况下，在数据库中建立表的时候，每一张表强制添加&nbsp;id&nbsp;递增字段，这样更方便我们查询数据。</p>
<p>如果数据量很大，比如像订单这类，一般会推荐进行分库分表。这个时候 id 就不建议作为唯一标识了，而应该使用分布式的高并发唯一&nbsp;id&nbsp;生成器来生成，并在数据表中使用另外的字段来存储这个唯一标识。</p>
<p>首先使用范围查询定位&nbsp;id&nbsp;（或者索引），然后再使用索引进行定位数据，即先&nbsp;select&nbsp;id，然后在&nbsp;select&nbsp;*；这样查询的速度将会提升好几倍。</p><p><br></p>
<p>原文地址：<a rel="nofollow" href="http://uusama.com/458.html" target="_blank" style="background-color: rgb(255, 255, 255);">http://uusama.com/458.html</a>
</p><p><br></p></div>