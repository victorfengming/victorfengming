---
title: "MySQL中交集和差集"
cover: "/img/lynk/82.jpg"
date:       2019-10-09
tags:
	- database
	- mysql
	- solution
---

<div class="content-intro view-box "><p>在MySQL中，只支持Union(并集)集合运算，而对于交集Intersect和差集Except并不支持。那么如何才能在MySQL中实现交集和差集呢？
    <br>
</p><p><br></p>
<p>一般在MySQL中，我们可以通过in和not&nbsp;in来间接实现交集和差集，当然也有一定局限性，面对少量数据还可以，但数据量大了效率就会变得很低。</p>
<p>创建table1</p><pre lang="sql" style="max-width: 100%;"><code class="sql hljs"><span class="hljs-comment">/*DDL 信息*/</span><span class="hljs-comment">------------  </span>
  
<span class="hljs-keyword">CREATE</span> <span class="hljs-keyword">TABLE</span> <span class="hljs-string">`t1`</span> (  
  <span class="hljs-string">`id`</span> <span class="hljs-built_in">int</span>(<span class="hljs-number">11</span>) <span class="hljs-keyword">NOT</span> <span class="hljs-literal">NULL</span>,  
  <span class="hljs-string">`name`</span> <span class="hljs-built_in">varchar</span>(<span class="hljs-number">20</span>) <span class="hljs-keyword">DEFAULT</span> <span class="hljs-literal">NULL</span>,  
  <span class="hljs-string">`age`</span> <span class="hljs-built_in">int</span>(<span class="hljs-number">11</span>) <span class="hljs-keyword">DEFAULT</span> <span class="hljs-literal">NULL</span>,  
  PRIMARY <span class="hljs-keyword">KEY</span> (<span class="hljs-string">`id`</span>)  
) <span class="hljs-keyword">ENGINE</span>=<span class="hljs-keyword">InnoDB</span> <span class="hljs-keyword">DEFAULT</span> <span class="hljs-keyword">CHARSET</span>=utf8  </code></pre>
<p>创建table2</p><pre lang="sql" style="max-width: 100%;"><code class="sql hljs"><span class="hljs-comment">/*DDL 信息*/</span><span class="hljs-comment">------------  </span>
  
<span class="hljs-keyword">CREATE</span> <span class="hljs-keyword">TABLE</span> <span class="hljs-string">`t2`</span> (  
  <span class="hljs-string">`id`</span> <span class="hljs-built_in">int</span>(<span class="hljs-number">11</span>) <span class="hljs-keyword">NOT</span> <span class="hljs-literal">NULL</span>,  
  <span class="hljs-string">`name`</span> <span class="hljs-built_in">varchar</span>(<span class="hljs-number">20</span>) <span class="hljs-keyword">DEFAULT</span> <span class="hljs-literal">NULL</span>,  
  <span class="hljs-string">`age`</span> <span class="hljs-built_in">int</span>(<span class="hljs-number">11</span>) <span class="hljs-keyword">DEFAULT</span> <span class="hljs-literal">NULL</span>,  
  PRIMARY <span class="hljs-keyword">KEY</span> (<span class="hljs-string">`id`</span>)  
) <span class="hljs-keyword">ENGINE</span>=<span class="hljs-keyword">InnoDB</span> <span class="hljs-keyword">DEFAULT</span> <span class="hljs-keyword">CHARSET</span>=utf8  </code></pre>
<p>插入</p><pre lang="sql" style="max-width: 100%;"><code class="sql hljs"><span class="hljs-keyword">INSERT</span> <span class="hljs-keyword">INTO</span> t1 <span class="hljs-keyword">VALUES</span>(<span class="hljs-number">1</span>,<span class="hljs-string">'小王'</span>,<span class="hljs-number">10</span>);  
<span class="hljs-keyword">INSERT</span> <span class="hljs-keyword">INTO</span> t1 <span class="hljs-keyword">VALUES</span>(<span class="hljs-number">2</span>,<span class="hljs-string">'小宋'</span>,<span class="hljs-number">20</span>);  
<span class="hljs-keyword">INSERT</span> <span class="hljs-keyword">INTO</span> t1 <span class="hljs-keyword">VALUES</span>(<span class="hljs-number">3</span>,<span class="hljs-string">'小白'</span>,<span class="hljs-number">30</span>);  
<span class="hljs-keyword">INSERT</span> <span class="hljs-keyword">INTO</span> t1 <span class="hljs-keyword">VALUES</span>(<span class="hljs-number">4</span>,<span class="hljs-string">'hello'</span>,<span class="hljs-number">40</span>);  
  
  
<span class="hljs-keyword">INSERT</span> <span class="hljs-keyword">INTO</span> t2 <span class="hljs-keyword">VALUES</span>(<span class="hljs-number">1</span>,<span class="hljs-string">'小王'</span>,<span class="hljs-number">10</span>);  
<span class="hljs-keyword">INSERT</span> <span class="hljs-keyword">INTO</span> t2 <span class="hljs-keyword">VALUES</span>(<span class="hljs-number">2</span>,<span class="hljs-string">'小宋'</span>,<span class="hljs-number">22</span>);  
<span class="hljs-keyword">INSERT</span> <span class="hljs-keyword">INTO</span> t2 <span class="hljs-keyword">VALUES</span>(<span class="hljs-number">3</span>,<span class="hljs-string">'小肖'</span>,<span class="hljs-number">31</span>);  
<span class="hljs-keyword">INSERT</span> <span class="hljs-keyword">INTO</span> t2 <span class="hljs-keyword">VALUES</span>(<span class="hljs-number">4</span>,<span class="hljs-string">'hello'</span>,<span class="hljs-number">40</span>);  
</code></pre><pre lang="sql" style="max-width: 100%;"><code class="sql hljs"><span class="hljs-keyword">SELECT</span> t1.* <span class="hljs-keyword">FROM</span> t1   
  
<span class="hljs-keyword">id</span>  <span class="hljs-keyword">name</span>    age  
<span class="hljs-number">1</span>   小王      <span class="hljs-number">10</span>  
<span class="hljs-number">2</span>   小宋      <span class="hljs-number">20</span>  
<span class="hljs-number">3</span>   小白      <span class="hljs-number">30</span>  
<span class="hljs-number">4</span>   hello   <span class="hljs-number">40</span>  </code></pre><pre lang="sql" style="max-width: 100%;"><code class="sql hljs"><span class="hljs-keyword">SELECT</span> t2.* <span class="hljs-keyword">FROM</span> t2   
  
<span class="hljs-keyword">id</span>  <span class="hljs-keyword">name</span>    age  
<span class="hljs-number">1</span>   小王  <span class="hljs-number">10</span>  
<span class="hljs-number">2</span>   小宋  <span class="hljs-number">22</span>  
<span class="hljs-number">3</span>   小肖  <span class="hljs-number">31</span>  
<span class="hljs-number">4</span>   hello   <span class="hljs-number">40</span>  </code></pre>
<p>使用not&nbsp;in&nbsp;求差集，但效率低</p><pre lang="sql" style="max-width: 100%;"><code class="sql hljs"><span class="hljs-keyword">SELECT</span> t1.* <span class="hljs-keyword">FROM</span> t1   
<span class="hljs-keyword">WHERE</span>   
<span class="hljs-keyword">name</span> <span class="hljs-keyword">NOT</span> <span class="hljs-keyword">IN</span>  
(<span class="hljs-keyword">SELECT</span> <span class="hljs-keyword">name</span> <span class="hljs-keyword">FROM</span> t2)  
  
<span class="hljs-keyword">id</span>  <span class="hljs-keyword">name</span>    age  
<span class="hljs-number">3</span>   小白      <span class="hljs-number">30</span>  </code></pre><pre lang="sql" style="max-width: 100%;"><code class="sql hljs"><span class="hljs-keyword">SELECT</span> t1.id, t1.name, t1.age  
<span class="hljs-keyword">FROM</span> t1   
<span class="hljs-keyword">LEFT</span> <span class="hljs-keyword">JOIN</span> t2   
<span class="hljs-keyword">ON</span> t1.id = t2.id  
<span class="hljs-keyword">WHERE</span> t1.name != t2.name  
  
   <span class="hljs-keyword">OR</span> t1.age != t2.age;  
  
  
id  name    age  
2   小宋      20  
3   小白      30  </code></pre>
<p>求交集，此时只有id&nbsp;name&nbsp;age&nbsp;所有都一样才是符合要求的。</p><pre lang="sql" style="max-width: 100%;"><code class="sql hljs"><span class="hljs-keyword">SELECT</span>  <span class="hljs-keyword">id</span>,  <span class="hljs-keyword">NAME</span>,  age, <span class="hljs-keyword">COUNT</span>(*)  
    <span class="hljs-keyword">FROM</span> (<span class="hljs-keyword">SELECT</span> <span class="hljs-keyword">id</span>, <span class="hljs-keyword">NAME</span>, age  
        <span class="hljs-keyword">FROM</span> t1  
          
        <span class="hljs-keyword">UNION</span> ALL  
          
        <span class="hljs-keyword">SELECT</span> <span class="hljs-keyword">id</span>, <span class="hljs-keyword">NAME</span>, age  
        <span class="hljs-keyword">FROM</span> t2  
        ) a  
    <span class="hljs-keyword">GROUP</span> <span class="hljs-keyword">BY</span> <span class="hljs-keyword">id</span>, <span class="hljs-keyword">NAME</span>, age  
    <span class="hljs-keyword">HAVING</span> <span class="hljs-keyword">COUNT</span>(*) &gt; <span class="hljs-number">1</span>  
      
    <span class="hljs-keyword">id</span>  <span class="hljs-keyword">NAME</span>    age <span class="hljs-keyword">COUNT</span>(*)  
    <span class="hljs-number">1</span>   小王      <span class="hljs-number">10</span>  <span class="hljs-number">2</span>  
    <span class="hljs-number">4</span>   hello   <span class="hljs-number">40</span>  <span class="hljs-number">2</span>  </code></pre>
<p><b><br></b>
</p>
<p><b>union&nbsp;all和union的区别
</b>
</p>
<p>UNION和UNION&nbsp;ALL的功能都是将两个结果集合并为一个，但是这两个关键字不管从使用还是效率上来说，都是有一定区别的。</p><p>使用上：</p>
<p>1、对重复结果的处理：UNION在进行表链接后会筛选掉重复的记录，而Union&nbsp;All则不会去除重复记录。</p>
<p>2、对排序的处理：Union将会按照字段的顺序进行排序；UNION&nbsp;ALL只是将两个结果合并后就返回，并不会进行排序处理。</p><p>效率上：</p>
<p>从效率上说，UNION&nbsp;ALL的处理效率要比UNION高很多，所以，如果可以确认合并的两个结果集中，且不包含重复数据和不需要进行排序的话，推荐使用UNION&nbsp;ALL。</p>
<p>
    <br>
</p><p><b>相关阅读：</b></p><p><a href="https://www.w3cschool.cn/mysql_migration/" target="_blank">不同场景下&nbsp;MySQL&nbsp;的迁移方案</a></p><p><a href="https://www.w3cschool.cn/hjikt5/" target="_blank">MySQL&nbsp;FAQ系列整理</a></p><p><br></p>
<p>原文地址：<a rel="nofollow" href="https://blog.csdn.net/mine_song/article/details/70184072" target="_blank">https://blog.csdn.net/mine_song/article/details/70184072</a>
</p>
<p>
    <br>
</p></div>