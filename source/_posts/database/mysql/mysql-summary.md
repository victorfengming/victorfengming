---
title: "可能是全网最好的MySQL重要知识点/面试题总结"
cover: "/img/lynk/17.jpg"
date:       2019-09-01
tags:
	- basis
	- mysql
	- Index
	- database
	- summer
---


版权声明：本文为CSDN博主「SnailClimb在csdn」的原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接及本声明。  
原文链接：https://blog.csdn.net/qq_34337272/article/details/94201189

<div id="content_views" class="markdown_views prism-atom-one-dark">
                    <!-- flowchart 箭头图标 勿删 -->
                    <svg xmlns="http://www.w3.org/2000/svg" style="display: none;">
                        <path stroke-linecap="round" d="M5,0 0,2.5 5,5z" id="raphael-marker-block" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);"></path>
                    </svg>
                                            <p>标题有点标题党的意思，看了文章之后希望大家不会有这个想法，绝对干货！！！这篇花文章是我花了几天时间对之前总结的MySQL知识点做了完善后的产物，这篇文章可以用来回顾MySQL基础知识以及备战MySQL常见面试问题。</p>
<p>文末有公众号二维码，欢迎关注获取笔主最新更新文章，并可免费获取笔主总结的《Java面试突击》以及Java工程师必备学习资源。<br>
</p><div class="toc"><h3><a name="t0"></a>文章目录</h3><ul><ul><li><a href="#MySQL_5" rel="nofollow" data-token="40f92f4c395320b95165ff7419966844" target="_self">什么是MySQL?</a></li><li><a href="#_9" rel="nofollow" data-token="da3976286948212b046fd1454e9505c7" target="_self">事务相关</a></li><ul><li><a href="#_11" rel="nofollow" data-token="6eedfa365683009f30709e58b02529ca" target="_self">什么是事务?</a></li><li><a href="#ACID_17" rel="nofollow" data-token="1d3b4631599c2a8d6945f9ef55ba48fc" target="_self">事物的四大特性(ACID)介绍一下?</a></li><li><a href="#_26" rel="nofollow" data-token="dd70d5fc37a7006c10eedb36c8608607" target="_self">并发事务带来哪些问题?</a></li><li><a href="#MySQL_43" rel="nofollow" data-token="c4ee63869f46dd85b8b19a58d5488f4c" target="_self">事务隔离级别有哪些?MySQL的默认隔离级别是?</a></li></ul><li><a href="#_78" rel="nofollow" data-token="e0efcb894cd0cc2a776527642e54fefe" target="_self">索引相关</a></li><ul><li><a href="#_82" rel="nofollow" data-token="4971367271f313697ecd711231f4ecce" target="_self">为什么索引能提高查询速度</a></li><li><a href="#_120" rel="nofollow" data-token="681b102127025ebe08f6f2332c464b5c" target="_self">什么是最左前缀原则？</a></li><li><a href="#_134" rel="nofollow" data-token="a2bf0951e9f32e22be131562b928c787" target="_self">注意避免冗余索引</a></li><li><a href="#Mysql_140" rel="nofollow" data-token="43fa1c9ea287fbb83c87428c2b2b997e" target="_self">Mysql如何为表字段添加索引？</a></li></ul><li><a href="#_172" rel="nofollow" data-token="56e6eee47e91124d5cef7d916eda63a9" target="_self">存储引擎</a></li><ul><ul><li><a href="#_174" rel="nofollow" data-token="c556d9ac67c1e709871aa09b74dfcb4f" target="_self">一些常用命令</a></li><li><a href="#MyISAMInnoDB_202" rel="nofollow" data-token="ffbf31d34d62d21d3d5e8f0d60f3a5d0" target="_self">MyISAM和InnoDB区别</a></li></ul></ul><li><a href="#_222" rel="nofollow" data-token="e2023e04dcfea6e6084f3a8acb489fa6" target="_self">乐观锁与悲观锁的区别</a></li><ul><li><a href="#_224" rel="nofollow" data-token="578abff404671cc2ae1580eada81d5b9" target="_self">悲观锁</a></li><li><a href="#_228" rel="nofollow" data-token="27b96ea87a0fb0428b6a3e329789dad9" target="_self">乐观锁</a></li><li><a href="#_232" rel="nofollow" data-token="758c35b5e169d54c4237cbcac8682809" target="_self">两种锁的使用场景</a></li><li><a href="#_236" rel="nofollow" data-token="e03ede430b787aa17be759734fa661ed" target="_self">乐观锁常见的两种实现方式</a></li><ul><li><a href="#1__240" rel="nofollow" data-token="79155e924b39a26e92b8ec2b6ffd3d2c" target="_self">1. 版本号机制</a></li><li><a href="#2_CAS_253" rel="nofollow" data-token="1d9e472ef7aedd4113ae3a35a15de159" target="_self">2. CAS算法</a></li></ul><li><a href="#_265" rel="nofollow" data-token="71c6dc92bcf4f9fcc038e9bd9d1e29c2" target="_self">乐观锁的缺点</a></li><ul><li><a href="#1_ABA__269" rel="nofollow" data-token="97ff6679f265f6646e7296222a0b962d" target="_self">1 ABA 问题</a></li><li><a href="#2__275" rel="nofollow" data-token="e6711d56acd4e92d45293001c577a772" target="_self">2 循环时间长开销大</a></li><li><a href="#3__279" rel="nofollow" data-token="babf0f6b1b7e38a2bd7d6bfa231ac9ed" target="_self">3 只能保证一个共享变量的原子操作</a></li></ul></ul><li><a href="#InnoDB_283" rel="nofollow" data-token="e6d68a3c95aa5f64b14044941785368a" target="_self">锁机制与InnoDB锁算法</a></li><li><a href="#_311" rel="nofollow" data-token="eb6d5e9afde70f0264abf0a9b23cd75a" target="_self">大表优化</a></li><ul><li><a href="#1__315" rel="nofollow" data-token="e5dc256deec892d343abf0e1e49adf42" target="_self">1. 限定数据的范围</a></li><li><a href="#2__319" rel="nofollow" data-token="43b1e023f7666326175aaa57b900158f" target="_self">2. 读/写分离</a></li><li><a href="#3__323" rel="nofollow" data-token="7d0ab07ace8865f32741e2614b676e12" target="_self">3. 垂直分区</a></li><li><a href="#4__333" rel="nofollow" data-token="e0b7d7e9cc38f49c5ef2b089e951c3f1" target="_self">4. 水平分区</a></li></ul><li><a href="#SQLMySQL_352" rel="nofollow" data-token="a88c6903220ee69f9988933786a53c2f" target="_self">一条SQL语句在MySQL中如何执行的</a></li><li><a href="#MySQL_356" rel="nofollow" data-token="0f0f71e71150711534b9795b5ea1ec25" target="_self">MySQL高性能优化规范建议</a></li><li><a href="#SQL_360" rel="nofollow" data-token="c429962db2751e65313bf8b5742a37c4" target="_self">一条SQL语句执行得很慢的原因有哪些？</a></li><li><a href="#_MySQL__364" rel="nofollow" data-token="71a53a90acb5d646282f24d29a509b07" target="_self">一千行 MySQL 学习笔记</a></li><li><a href="#_368" rel="nofollow" data-token="df6d4e7608e3b7e60a1b34892820d3f6" target="_self">公众号</a></li></ul></ul></div><p></p>
<h2><a name="t1"></a><a id="MySQL_5"></a>什么是MySQL?</h2>
<p>MySQL 是一种关系型数据库，在Java企业级开发中非常常用，因为 MySQL 是开源免费的，并且方便扩展。阿里巴巴数据库系统也大量用到了 MySQL，因此它的稳定性是有保障的。MySQL是开放源代码的，因此任何人都可以在 GPL(General Public License) 的许可下下载并根据个性化的需要对其进行修改。MySQL的默认端口号是<strong>3306</strong>。</p>
<h2><a name="t2"></a><a id="_9"></a>事务相关</h2>
<h3><a name="t3"></a><a id="_11"></a>什么是事务?</h3>
<p><strong>事务是逻辑上的一组操作，要么都执行，要么都不执行。</strong></p>
<p>事务最经典也经常被拿出来说例子就是转账了。假如小明要给小红转账1000元，这个转账会涉及到两个关键操作就是：将小明的余额减少1000元，将小红的余额增加1000元。万一在这两个操作之间突然出现错误比如银行系统崩溃，导致小明余额减少而小红的余额没有增加，这样就不对了。事务就是保证这两个关键操作要么都成功，要么都要失败。</p>
<h3><a name="t4"></a><a id="ACID_17"></a>事物的四大特性(ACID)介绍一下?</h3>
<p><img src="https://my-blog-to-use.oss-cn-beijing.aliyuncs.com/2019-6/%E4%BA%8B%E5%8A%A1%E7%89%B9%E6%80%A7.png" alt="事物的特性"></p>
<ol>
<li><strong>原子性：</strong> 事务是最小的执行单位，不允许分割。事务的原子性确保动作要么全部完成，要么完全不起作用；</li>
<li><strong>一致性：</strong> 执行事务前后，数据保持一致，多个事务对同一个数据读取的结果是相同的；</li>
<li><strong>隔离性：</strong> 并发访问数据库时，一个用户的事务不被其他事务所干扰，各并发事务之间数据库是独立的；</li>
<li><strong>持久性：</strong> 一个事务被提交之后。它对数据库中数据的改变是持久的，即使数据库发生故障也不应该对其有任何影响。</li>
</ol>
<h3><a name="t5"></a><a id="_26"></a>并发事务带来哪些问题?</h3>
<p>在典型的应用程序中，多个事务并发运行，经常会操作相同的数据来完成各自的任务（多个用户对统一数据进行操作）。并发虽然是必须的，但可能会导致以下的问题。</p>
<ul>
<li><strong>脏读（Dirty read）:</strong> 当一个事务正在访问数据并且对数据进行了修改，而这种修改还没有提交到数据库中，这时另外一个事务也访问了这个数据，然后使用了这个数据。因为这个数据是还没有提交的数据，那么另外一个事务读到的这个数据是“脏数据”，依据“脏数据”所做的操作可能是不正确的。</li>
<li><strong>丢失修改（Lost to modify）:</strong> 指在一个事务读取一个数据时，另外一个事务也访问了该数据，那么在第一个事务中修改了这个数据后，第二个事务也修改了这个数据。这样第一个事务内的修改结果就被丢失，因此称为丢失修改。  例如：事务1读取某表中的数据A=20，事务2也读取A=20，事务1修改A=A-1，事务2也修改A=A-1，最终结果A=19，事务1的修改被丢失。</li>
<li><strong>不可重复读（Unrepeatableread）:</strong> 指在一个事务内多次读同一数据。在这个事务还没有结束时，另一个事务也访问该数据。那么，在第一个事务中的两次读数据之间，由于第二个事务的修改导致第一个事务两次读取的数据可能不太一样。这就发生了在一个事务内两次读到的数据是不一样的情况，因此称为不可重复读。</li>
<li><strong>幻读（Phantom read）:</strong> 幻读与不可重复读类似。它发生在一个事务（T1）读取了几行数据，接着另一个并发事务（T2）插入了一些数据时。在随后的查询中，第一个事务（T1）就会发现多了一些原本不存在的记录，就好像发生了幻觉一样，所以称为幻读。</li>
</ul>
<p><strong>不可重复度和幻读区别：</strong></p>
<p>不可重复读的重点是修改，幻读的重点在于新增或者删除。</p>
<p>例1（同样的条件, 你读取过的数据, 再次读取出来发现值不一样了 ）：事务1中的A先生读取自己的工资为     1000的操作还没完成，事务2中的B先生就修改了A的工资为2000，导        致A再读自己的工资时工资变为  2000；这就是不可重复读。</p>
<p>例2（同样的条件, 第1次和第2次读出来的记录数不一样 ）：假某工资单表中工资大于3000的有4人，事务1读取了所有工资大于3000的人，共查到4条记录，这时事务2 又插入了一条工资大于3000的记录，事务1再次读取时查到的记录就变为了5条，这样就导致了幻读。</p>
<h3><a name="t6"></a><a id="MySQL_43"></a>事务隔离级别有哪些?MySQL的默认隔离级别是?</h3>
<p><strong>SQL 标准定义了四个隔离级别：</strong></p>
<ul>
<li><strong>READ-UNCOMMITTED(读取未提交)：</strong> 最低的隔离级别，允许读取尚未提交的数据变更，<strong>可能会导致脏读、幻读或不可重复读</strong>。</li>
<li><strong>READ-COMMITTED(读取已提交)：</strong> 允许读取并发事务已经提交的数据，<strong>可以阻止脏读，但是幻读或不可重复读仍有可能发生</strong>。</li>
<li><strong>REPEATABLE-READ(可重复读)：</strong>  对同一字段的多次读取结果都是一致的，除非数据是被本身事务自己所修改，<strong>可以阻止脏读和不可重复读，但幻读仍有可能发生</strong>。</li>
<li><strong>SERIALIZABLE(可串行化)：</strong> 最高的隔离级别，完全服从ACID的隔离级别。所有的事务依次逐个执行，这样事务之间就完全不可能产生干扰，也就是说，<strong>该级别可以防止脏读、不可重复读以及幻读</strong>。</li>
</ul>
<hr>

<div class="table-box"><table>
<thead>
<tr>
<th align="center">隔离级别</th>
<th align="center">脏读</th>
<th align="center">不可重复读</th>
<th align="center">幻影读</th>
</tr>
</thead>
<tbody>
<tr>
<td align="center">READ-UNCOMMITTED</td>
<td align="center">√</td>
<td align="center">√</td>
<td align="center">√</td>
</tr>
<tr>
<td align="center">READ-COMMITTED</td>
<td align="center">×</td>
<td align="center">√</td>
<td align="center">√</td>
</tr>
<tr>
<td align="center">REPEATABLE-READ</td>
<td align="center">×</td>
<td align="center">×</td>
<td align="center">√</td>
</tr>
<tr>
<td align="center">SERIALIZABLE</td>
<td align="center">×</td>
<td align="center">×</td>
<td align="center">×</td>
</tr>
</tbody>
</table></div><p>MySQL InnoDB 存储引擎的默认支持的隔离级别是 <strong>REPEATABLE-READ（可重读）</strong>。我们可以通过<code>SELECT @@tx_isolation;</code>命令来查看</p>
<pre class="prettyprint"><code class="prism language-sql has-numbering" onclick="mdcp.copyCode(event)" style="position: unset;">mysql<span class="token operator">&gt;</span> <span class="token keyword">SELECT</span> @<span class="token variable">@tx_isolation</span><span class="token punctuation">;</span>
<span class="token operator">+</span><span class="token comment">-----------------+</span>
<span class="token operator">|</span> @<span class="token variable">@tx_isolation</span>  <span class="token operator">|</span>
<span class="token operator">+</span><span class="token comment">-----------------+</span>
<span class="token operator">|</span> <span class="token keyword">REPEATABLE</span><span class="token operator">-</span><span class="token keyword">READ</span> <span class="token operator">|</span>
<span class="token operator">+</span><span class="token comment">-----------------+</span>
<div class="hljs-button {2}" data-title="复制"></div></code><ul class="pre-numbering" style=""><li style="color: rgb(153, 153, 153);">1</li><li style="color: rgb(153, 153, 153);">2</li><li style="color: rgb(153, 153, 153);">3</li><li style="color: rgb(153, 153, 153);">4</li><li style="color: rgb(153, 153, 153);">5</li><li style="color: rgb(153, 153, 153);">6</li></ul></pre>
<p>这里需要注意的是：与 SQL 标准不同的地方在于InnoDB 存储引擎在 **REPEATABLE-READ（可重读）<strong>事务隔离级别下使用的是Next-Key Lock 锁算法，因此可以避免幻读的产生，这与其他数据库系统(如 SQL Server)是不同的。所以说InnoDB 存储引擎的默认支持的隔离级别是 <strong>REPEATABLE-READ（可重读）</strong> 已经可以完全保证事务的隔离性要求，即达到了 SQL标准的</strong>SERIALIZABLE(可串行化)**隔离级别。</p>
<p>因为隔离级别越低，事务请求的锁越少，所以大部分数据库系统的隔离级别都是<strong>READ-COMMITTED(读取提交内容):</strong>，但是你要知道的是InnoDB 存储引擎默认使用 **REPEATABLE-READ（可重读）**并不会有任何性能损失。</p>
<p>InnoDB 存储引擎在 <strong>分布式事务</strong> 的情况下一般会用到**SERIALIZABLE(可串行化)**隔离级别。</p>
<h2><a name="t7"></a><a id="_78"></a>索引相关</h2>
<p><img src="http://my-blog-to-use.oss-cn-beijing.aliyuncs.com/18-10-2/70973487.jpg" alt="[思维导图-索引篇]"></p>
<h3><a name="t8"></a><a id="_82"></a>为什么索引能提高查询速度</h3>
<blockquote>
<p>以下内容整理自： 地址： <a href="https://juejin.im/post/5b55b842f265da0f9e589e79" rel="nofollow" data-token="32914170fb1af2eb6f6fd6508c0bb699">https://juejin.im/post/5b55b842f265da0f9e589e79</a> 作者 ：Java3y</p>
</blockquote>
<p><strong>先从 MySQL 的基本存储结构说起</strong></p>
<p>MySQL的基本存储结构是页(记录都存在页里边)：</p>
<p><img src="http://my-blog-to-use.oss-cn-beijing.aliyuncs.com/18-10-2/28559421.jpg" alt="MySQL的基本存储结构是页"></p>
<p><img src="http://my-blog-to-use.oss-cn-beijing.aliyuncs.com/18-10-2/82053134.jpg" alt=""></p>
<ul>
<li><strong>各个数据页可以组成一个双向链表</strong></li>
<li><strong>每个数据页中的记录又可以组成一个单向链表</strong>
<ul>
<li>每个数据页都会为存储在它里边儿的记录生成一个页目录，在通过主键查找某条记录的时候可以在页目录中使用二分法快速定位到对应的槽，然后再遍历该槽对应分组中的记录即可快速找到指定的记录</li>
<li>以其他列(非主键)作为搜索条件：只能从最小记录开始依次遍历单链表中的每条记录。</li>
</ul>
</li>
</ul>
<p>所以说，如果我们写select * from user where indexname = 'xxx’这样没有进行任何优化的sql语句，默认会这样做：</p>
<ol>
<li><strong>定位到记录所在的页：需要遍历双向链表，找到所在的页</strong></li>
<li><strong>从所在的页内中查找相应的记录：由于不是根据主键查询，只能遍历所在页的单链表了</strong></li>
</ol>
<p>很明显，在数据量很大的情况下这样查找会很慢！这样的时间复杂度为O（n）。</p>
<p><strong>索引做了些什么可以让我们查询加快速度呢？其实就是将无序的数据变成有序(相对)：</strong></p>
<p><img src="http://my-blog-to-use.oss-cn-beijing.aliyuncs.com/18-10-2/5373082.jpg" alt=""></p>
<p>要找到id为8的记录简要步骤：</p>
<p><img src="http://my-blog-to-use.oss-cn-beijing.aliyuncs.com/18-10-2/89338047.jpg" alt=""></p>
<p>很明显的是：没有用索引我们是需要遍历双向链表来定位对应的页，现在通过 <strong>“目录”</strong> 就可以很快地定位到对应的页上了！（二分查找，时间复杂度近似为O(logn)）</p>
<p>其实底层结构就是B+树，B+树作为树的一种实现，能够让我们很快地查找出对应的记录。</p>
<blockquote>
<p>以下内容整理自：《Java工程师修炼之道》</p>
</blockquote>
<h3><a name="t9"></a><a id="_120"></a>什么是最左前缀原则？</h3>
<p>MySQL中的索引可以以一定顺序引用多列，这种索引叫作联合索引。如User表的name和city加联合索引就是(name,city)，而最左前缀原则指的是，如果查询的时候查询条件精确匹配索引的左边连续一列或几列，则此列就可以被用到。如下：</p>
<pre class="prettyprint"><code class="prism language-sql has-numbering" onclick="mdcp.copyCode(event)" style="position: unset;"><span class="token keyword">select</span> <span class="token operator">*</span> <span class="token keyword">from</span> <span class="token keyword">user</span> <span class="token keyword">where</span> name<span class="token operator">=</span>xx <span class="token operator">and</span> city<span class="token operator">=</span>xx <span class="token punctuation">;</span> ／／可以命中索引
<span class="token keyword">select</span> <span class="token operator">*</span> <span class="token keyword">from</span> <span class="token keyword">user</span> <span class="token keyword">where</span> name<span class="token operator">=</span>xx <span class="token punctuation">;</span> <span class="token comment">// 可以命中索引</span>
<span class="token keyword">select</span> <span class="token operator">*</span> <span class="token keyword">from</span> <span class="token keyword">user</span> <span class="token keyword">where</span> city<span class="token operator">=</span>xx <span class="token punctuation">;</span> <span class="token comment">// 无法命中索引            </span>
<div class="hljs-button {2}" data-title="复制"></div></code><ul class="pre-numbering" style=""><li style="color: rgb(153, 153, 153);">1</li><li style="color: rgb(153, 153, 153);">2</li><li style="color: rgb(153, 153, 153);">3</li></ul></pre>
<p>这里需要注意的是，查询的时候如果两个条件都用上了，但是顺序不同，如 <code>city= xx and name ＝xx</code>，那么现在的查询引擎会自动优化为匹配联合索引的顺序，这样是能够命中索引的。</p>
<p>由于最左前缀原则，在创建联合索引时，索引字段的顺序需要考虑字段值去重之后的个数，较多的放前面。ORDER BY子句也遵循此规则。</p>
<h3><a name="t10"></a><a id="_134"></a>注意避免冗余索引</h3>
<p>冗余索引指的是索引的功能相同，能够命中就肯定能命中 ，那么 就是冗余索引如（name,city ）和（name ）这两个索引就是冗余索引，能够命中后者的查询肯定是能够命中前者的 在大多数情况下，都应该尽量扩展已有的索引而不是创建新索引。</p>
<p>MySQLS.7 版本后，可以通过查询 sys 库的 <code>schema_redundant_indexes</code> 表来查看冗余索引</p>
<h3><a name="t11"></a><a id="Mysql_140"></a>Mysql如何为表字段添加索引？</h3>
<p>1.添加PRIMARY KEY（主键索引）</p>
<pre class="prettyprint"><code class="prism language-sql has-numbering" onclick="mdcp.copyCode(event)" style="position: unset;"><span class="token keyword">ALTER</span> <span class="token keyword">TABLE</span> <span class="token punctuation">`</span>table_name<span class="token punctuation">`</span> <span class="token keyword">ADD</span> <span class="token keyword">PRIMARY</span> <span class="token keyword">KEY</span> <span class="token punctuation">(</span> <span class="token punctuation">`</span><span class="token keyword">column</span><span class="token punctuation">`</span> <span class="token punctuation">)</span> 
<div class="hljs-button {2}" data-title="复制"></div></code><ul class="pre-numbering" style=""><li style="color: rgb(153, 153, 153);">1</li></ul></pre>
<p>2.添加UNIQUE(唯一索引)</p>
<pre class="prettyprint"><code class="prism language-sql has-numbering" onclick="mdcp.copyCode(event)" style="position: unset;"><span class="token keyword">ALTER</span> <span class="token keyword">TABLE</span> <span class="token punctuation">`</span>table_name<span class="token punctuation">`</span> <span class="token keyword">ADD</span> <span class="token keyword">UNIQUE</span> <span class="token punctuation">(</span> <span class="token punctuation">`</span><span class="token keyword">column</span><span class="token punctuation">`</span> <span class="token punctuation">)</span> 
<div class="hljs-button {2}" data-title="复制"></div></code><ul class="pre-numbering" style=""><li style="color: rgb(153, 153, 153);">1</li></ul></pre>
<p>3.添加INDEX(普通索引)</p>
<pre class="prettyprint"><code class="prism language-sql has-numbering" onclick="mdcp.copyCode(event)" style="position: unset;"><span class="token keyword">ALTER</span> <span class="token keyword">TABLE</span> <span class="token punctuation">`</span>table_name<span class="token punctuation">`</span> <span class="token keyword">ADD</span> <span class="token keyword">INDEX</span> index_name <span class="token punctuation">(</span> <span class="token punctuation">`</span><span class="token keyword">column</span><span class="token punctuation">`</span> <span class="token punctuation">)</span>
<div class="hljs-button {2}" data-title="复制"></div></code><ul class="pre-numbering" style=""><li style="color: rgb(153, 153, 153);">1</li></ul></pre>
<p>4.添加FULLTEXT(全文索引)</p>
<pre class="prettyprint"><code class="prism language-sql has-numbering" onclick="mdcp.copyCode(event)" style="position: unset;"><span class="token keyword">ALTER</span> <span class="token keyword">TABLE</span> <span class="token punctuation">`</span>table_name<span class="token punctuation">`</span> <span class="token keyword">ADD</span> FULLTEXT <span class="token punctuation">(</span> <span class="token punctuation">`</span><span class="token keyword">column</span><span class="token punctuation">`</span><span class="token punctuation">)</span> 
<div class="hljs-button {2}" data-title="复制"></div></code><ul class="pre-numbering" style=""><li style="color: rgb(153, 153, 153);">1</li></ul></pre>
<p>5.添加多列索引</p>
<pre class="prettyprint"><code class="prism language-sql has-numbering" onclick="mdcp.copyCode(event)" style="position: unset;"><span class="token keyword">ALTER</span> <span class="token keyword">TABLE</span> <span class="token punctuation">`</span>table_name<span class="token punctuation">`</span> <span class="token keyword">ADD</span> <span class="token keyword">INDEX</span> index_name <span class="token punctuation">(</span> <span class="token punctuation">`</span>column1<span class="token punctuation">`</span><span class="token punctuation">,</span> <span class="token punctuation">`</span>column2<span class="token punctuation">`</span><span class="token punctuation">,</span> <span class="token punctuation">`</span>column3<span class="token punctuation">`</span> <span class="token punctuation">)</span>
<div class="hljs-button {2}" data-title="复制"></div></code><ul class="pre-numbering" style=""><li style="color: rgb(153, 153, 153);">1</li></ul></pre>
<h2><a name="t12"></a><a id="_172"></a>存储引擎</h2>
<h4><a id="_174"></a>一些常用命令</h4>
<p><strong>查看MySQL提供的所有存储引擎</strong></p>
<pre class="prettyprint"><code class="prism language-sql has-numbering" onclick="mdcp.copyCode(event)" style="position: unset;">mysql<span class="token operator">&gt;</span> <span class="token keyword">show</span> engines<span class="token punctuation">;</span>
<div class="hljs-button {2}" data-title="复制"></div></code><ul class="pre-numbering" style=""><li style="color: rgb(153, 153, 153);">1</li></ul></pre>
<p><img src="https://my-blog-to-use.oss-cn-beijing.aliyuncs.com/2019-6/mysql-engines.png" alt="查看MySQL提供的所有存储引擎"></p>
<p>从上图我们可以查看出 MySQL 当前默认的存储引擎是InnoDB,并且在5.7版本所有的存储引擎中只有 InnoDB 是事务性存储引擎，也就是说只有 InnoDB 支持事务。</p>
<p><strong>查看MySQL当前默认的存储引擎</strong></p>
<p>我们也可以通过下面的命令查看默认的存储引擎。</p>
<pre class="prettyprint"><code class="prism language-sql has-numbering" onclick="mdcp.copyCode(event)" style="position: unset;">mysql<span class="token operator">&gt;</span> <span class="token keyword">show</span> variables <span class="token operator">like</span> <span class="token string">'%storage_engine%'</span><span class="token punctuation">;</span>
<div class="hljs-button {2}" data-title="复制"></div></code><ul class="pre-numbering" style=""><li style="color: rgb(153, 153, 153);">1</li></ul></pre>
<p><strong>查看表的存储引擎</strong></p>
<pre class="prettyprint"><code class="prism language-sql has-numbering" onclick="mdcp.copyCode(event)" style="position: unset;"><span class="token keyword">show</span> <span class="token keyword">table</span> <span class="token keyword">status</span> <span class="token operator">like</span> <span class="token string">"table_name"</span> <span class="token punctuation">;</span>
<div class="hljs-button {2}" data-title="复制"></div></code><ul class="pre-numbering" style=""><li style="color: rgb(153, 153, 153);">1</li></ul></pre>
<p><img src="https://my-blog-to-use.oss-cn-beijing.aliyuncs.com/2019-6/%E6%9F%A5%E7%9C%8B%E8%A1%A8%E7%9A%84%E5%AD%98%E5%82%A8%E5%BC%95%E6%93%8E.png" alt="查看表的存储引擎"></p>
<h4><a id="MyISAMInnoDB_202"></a>MyISAM和InnoDB区别</h4>
<p>MyISAM是MySQL的默认数据库引擎（5.5版之前）。虽然性能极佳，而且提供了大量的特性，包括全文索引、压缩、空间函数等，但MyISAM不支持事务和行级锁，而且最大的缺陷就是崩溃后无法安全恢复。不过，5.5版本之后，MySQL引入了InnoDB（事务性数据库引擎），MySQL 5.5版本后默认的存储引擎为InnoDB。</p>
<p>大多数时候我们使用的都是 InnoDB 存储引擎，但是在某些情况下使用 MyISAM 也是合适的比如读密集的情况下。（如果你不介意 MyISAM 崩溃回复问题的话）。</p>
<p><strong>两者的对比：</strong></p>
<ol>
<li><strong>是否支持行级锁</strong> : MyISAM 只有表级锁(table-level locking)，而InnoDB 支持行级锁(row-level locking)和表级锁,默认为行级锁。</li>
<li><strong>是否支持事务和崩溃后的安全恢复： MyISAM</strong> 强调的是性能，每次查询具有原子性,其执行数度比InnoDB类型更快，但是不提供事务支持。但是<strong>InnoDB</strong> 提供事务支持事务，外部键等高级数据库功能。 具有事务(commit)、回滚(rollback)和崩溃修复能力(crash recovery capabilities)的事务安全(transaction-safe (ACID compliant))型表。</li>
<li><strong>是否支持外键：</strong> MyISAM不支持，而InnoDB支持。</li>
<li><strong>是否支持MVCC</strong> ：仅 InnoDB 支持。应对高并发事务, MVCC比单纯的加锁更高效;MVCC只在 <code>READ COMMITTED</code> 和 <code>REPEATABLE READ</code> 两个隔离级别下工作;MVCC可以使用 乐观(optimistic)锁 和 悲观(pessimistic)锁来实现;各数据库中MVCC实现并不统一。推荐阅读：<a href="https://segmentfault.com/a/1190000012650596" rel="nofollow" data-token="50ce0a801445dfff3ec3a26420bffdfa">MySQL-InnoDB-MVCC多版本并发控制</a></li>
<li>…</li>
</ol>
<p>《MySQL高性能》上面有一句话这样写到:</p>
<blockquote>
<p>不要轻易相信“MyISAM比InnoDB快”之类的经验之谈，这个结论往往不是绝对的。在很多我们已知场景中，InnoDB的速度都可以让MyISAM望尘莫及，尤其是用到了聚簇索引，或者需要访问的数据都可以放入内存的应用。</p>
</blockquote>
<p>一般情况下我们选择 InnoDB 都是没有问题的，但是某事情况下你并不在乎可扩展能力和并发能力，也不需要事务支持，也不在乎崩溃后的安全恢复问题的话，选择MyISAM也是一个不错的选择。但是一般情况下，我们都是需要考虑到这些问题的。</p>
<h2><a name="t13"></a><a id="_222"></a>乐观锁与悲观锁的区别</h2>
<h3><a name="t14"></a><a id="_224"></a>悲观锁</h3>
<p>总是假设最坏的情况，每次去拿数据的时候都认为别人会修改，所以每次在拿数据的时候都会上锁，这样别人想拿这个数据就会阻塞直到它拿到锁（<strong>共享资源每次只给一个线程使用，其它线程阻塞，用完后再把资源转让给其它线程</strong>）。传统的关系型数据库里边就用到了很多这种锁机制，比如行锁，表锁等，读锁，写锁等，都是在做操作之前先上锁。Java中<code>synchronized</code>和<code>ReentrantLock</code>等独占锁就是悲观锁思想的实现。</p>
<h3><a name="t15"></a><a id="_228"></a>乐观锁</h3>
<p>总是假设最好的情况，每次去拿数据的时候都认为别人不会修改，所以不会上锁，但是在更新的时候会判断一下在此期间别人有没有去更新这个数据，可以使用版本号机制和CAS算法实现。<strong>乐观锁适用于多读的应用类型，这样可以提高吞吐量</strong>，像数据库提供的类似于<strong>write_condition机制</strong>，其实都是提供的乐观锁。在Java中<code>java.util.concurrent.atomic</code>包下面的原子变量类就是使用了乐观锁的一种实现方式<strong>CAS</strong>实现的。</p>
<h3><a name="t16"></a><a id="_232"></a>两种锁的使用场景</h3>
<p>从上面对两种锁的介绍，我们知道两种锁各有优缺点，不可认为一种好于另一种，像<strong>乐观锁适用于写比较少的情况下（多读场景）</strong>，即冲突真的很少发生的时候，这样可以省去了锁的开销，加大了系统的整个吞吐量。但如果是多写的情况，一般会经常产生冲突，这就会导致上层应用会不断的进行retry，这样反倒是降低了性能，所以<strong>一般多写的场景下用悲观锁就比较合适。</strong></p>
<h3><a name="t17"></a><a id="_236"></a>乐观锁常见的两种实现方式</h3>
<blockquote>
<p><strong>乐观锁一般会使用版本号机制或CAS算法实现。</strong></p>
</blockquote>
<h4><a id="1__240"></a>1. 版本号机制</h4>
<p>一般是在数据表中加上一个数据版本号version字段，表示数据被修改的次数，当数据被修改时，version值会加一。当线程A要更新数据值时，在读取数据的同时也会读取version值，在提交更新时，若刚才读取到的version值为当前数据库中的version值相等时才更新，否则重试更新操作，直到更新成功。</p>
<p><strong>举一个简单的例子：</strong> 假设数据库中帐户信息表中有一个 version 字段，当前值为 1 ；而当前帐户余额字段（ balance ）为 $100 。</p>
<ol>
<li>操作员 A 此时将其读出（ version=1 ），并从其帐户余额中扣除 $50（ $100-$50 ）。</li>
<li>在操作员 A 操作的过程中，操作员B 也读入此用户信息（ version=1 ），并从其帐户余额中扣除 $20 （ $100-$20 ）。</li>
<li>操作员 A 完成了修改工作，将数据版本号加一（ version=2 ），连同帐户扣除后余额（ balance=$50 ），提交至数据库更新，此时由于提交数据版本大于数据库记录当前版本，数据被更新，数据库记录 version 更新为 2 。</li>
<li>操作员 B 完成了操作，也将版本号加一（ version=2 ）试图向数据库提交数据（ balance=$80 ），但此时比对数据库记录版本时发现，操作员 B 提交的数据版本号为 2 ，数据库记录当前版本也为 2 ，不满足 “ 提交版本必须大于记录当前版本才能执行更新 “ 的乐观锁策略，因此，操作员 B 的提交被驳回。</li>
</ol>
<p>这样，就避免了操作员 B 用基于 version=1 的旧数据修改的结果覆盖操作员A 的操作结果的可能。</p>
<h4><a id="2_CAS_253"></a>2. CAS算法</h4>
<p>即<strong>compare and swap（比较与交换）</strong>，是一种有名的<strong>无锁算法</strong>。无锁编程，即不使用锁的情况下实现多线程之间的变量同步，也就是在没有线程被阻塞的情况下实现变量的同步，所以也叫非阻塞同步（Non-blocking Synchronization）。<strong>CAS算法</strong>涉及到三个操作数</p>
<ul>
<li>需要读写的内存值 V</li>
<li>进行比较的值 A</li>
<li>拟写入的新值 B</li>
</ul>
<p>当且仅当 V 的值等于 A时，CAS通过原子方式用新值B来更新V的值，否则不会执行任何操作（比较和替换是一个原子操作）。一般情况下是一个<strong>自旋操作</strong>，即<strong>不断的重试</strong>。</p>
<p>关于自旋锁，大家可以看一下这篇文章，非常不错：<a href="https://blog.csdn.net/qq_34337272/article/details/81252853" rel="nofollow" data-token="c9644a0b8eaa9d0e9f771488f10e5568">《 面试必备之深入理解自旋锁》</a></p>
<h3><a name="t18"></a><a id="_265"></a>乐观锁的缺点</h3>
<blockquote>
<p>ABA 问题是乐观锁一个常见的问题</p>
</blockquote>
<h4><a id="1_ABA__269"></a>1 ABA 问题</h4>
<p>如果一个变量V初次读取的时候是A值，并且在准备赋值的时候检查到它仍然是A值，那我们就能说明它的值没有被其他线程修改过了吗？很明显是不能的，因为在这段时间它的值可能被改为其他值，然后又改回A，那CAS操作就会误认为它从来没有被修改过。这个问题被称为CAS操作的 <strong>"ABA"问题。</strong></p>
<p>JDK 1.5 以后的 <code>AtomicStampedReference 类</code>就提供了此种能力，其中的 <code>compareAndSet 方法</code>就是首先检查当前引用是否等于预期引用，并且当前标志是否等于预期标志，如果全部相等，则以原子方式将该引用和该标志的值设置为给定的更新值。</p>
<h4><a id="2__275"></a>2 循环时间长开销大</h4>
<p><strong>自旋CAS（也就是不成功就一直循环执行直到成功）如果长时间不成功，会给CPU带来非常大的执行开销。</strong> 如果JVM能支持处理器提供的pause指令那么效率会有一定的提升，pause指令有两个作用，第一它可以延迟流水线执行指令（de-pipeline）,使CPU不会消耗过多的执行资源，延迟的时间取决于具体实现的版本，在一些处理器上延迟时间是零。第二它可以避免在退出循环的时候因内存顺序冲突（memory order violation）而引起CPU流水线被清空（CPU pipeline flush），从而提高CPU的执行效率。</p>
<h4><a id="3__279"></a>3 只能保证一个共享变量的原子操作</h4>
<p>CAS 只对单个共享变量有效，当操作涉及跨多个共享变量时 CAS 无效。但是从 JDK 1.5开始，提供了<code>AtomicReference类</code>来保证引用对象之间的原子性，你可以把多个变量放在一个对象里来进行 CAS 操作.所以我们可以使用锁或者利用<code>AtomicReference类</code>把多个共享变量合并成一个共享变量来操作。</p>
<h2><a name="t19"></a><a id="InnoDB_283"></a>锁机制与InnoDB锁算法</h2>
<p><strong>MyISAM和InnoDB存储引擎使用的锁：</strong></p>
<ul>
<li>MyISAM 采用表级锁(table-level locking)。</li>
<li>InnoDB 支持行级锁(row-level locking)和表级锁,默认为行级锁</li>
</ul>
<p><strong>表级锁和行级锁对比：</strong></p>
<ul>
<li><strong>表级锁：</strong> Mysql中锁定 <strong>粒度最大</strong> 的一种锁，对当前操作的整张表加锁，实现简单，资源消耗也比较少，加锁快，不会出现死锁。其锁定粒度最大，触发锁冲突的概率最高，并发度最低，MyISAM和 InnoDB引擎都支持表级锁。</li>
<li><strong>行级锁：</strong> Mysql中锁定 <strong>粒度最小</strong> 的一种锁，只针对当前操作的行进行加锁。 行级锁能大大减少数据库操作的冲突。其加锁粒度最小，并发度高，但加锁的开销也最大，加锁慢，会出现死锁。</li>
</ul>
<p>详细内容可以参考： <a href="https://blog.csdn.net/qq_34337272/article/details/80611486" rel="nofollow" data-token="a1a93671f741eb9cc824a7075cae9340">Mysql锁机制简单了解一下</a></p>
<p><strong>InnoDB存储引擎的锁的算法有三种：</strong></p>
<ul>
<li>Record lock：单个行记录上的锁</li>
<li>Gap lock：间隙锁，锁定一个范围，不包括记录本身</li>
<li>Next-key lock：record+gap 锁定一个范围，包含记录本身</li>
</ul>
<p><strong>相关知识点：</strong></p>
<ol>
<li>innodb对于行的查询使用next-key lock</li>
<li>Next-locking keying为了解决Phantom Problem幻读问题</li>
<li>当查询的索引含有唯一属性时，将next-key lock降级为record key</li>
<li>Gap锁设计的目的是为了阻止多个事务将记录插入到同一范围内，而这会导致幻读问题的产生</li>
<li>有两种方式显式关闭gap锁：（除了外键约束和唯一性检查外，其余情况仅使用record lock） A. 将事务隔离级别设置为RC B. 将参数innodb_locks_unsafe_for_binlog设置为1</li>
</ol>
<h2><a name="t20"></a><a id="_311"></a>大表优化</h2>
<p>当MySQL单表记录数过大时，数据库的CRUD性能会明显下降，一些常见的优化措施如下：</p>
<h3><a name="t21"></a><a id="1__315"></a>1. 限定数据的范围</h3>
<p>务必禁止不带任何限制数据范围条件的查询语句。比如：我们当用户在查询订单历史的时候，我们可以控制在一个月的范围内；</p>
<h3><a name="t22"></a><a id="2__319"></a>2. 读/写分离</h3>
<p>经典的数据库拆分方案，主库负责写，从库负责读；</p>
<h3><a name="t23"></a><a id="3__323"></a>3. 垂直分区</h3>
<p><strong>根据数据库里面数据表的相关性进行拆分。</strong> 例如，用户表中既有用户的登录信息又有用户的基本信息，可以将用户表拆分成两个单独的表，甚至放到单独的库做分库。</p>
<p><strong>简单来说垂直拆分是指数据表列的拆分，把一张列比较多的表拆分为多张表。</strong> 如下图所示，这样来说大家应该就更容易理解了。<br>
<img src="https://my-blog-to-use.oss-cn-beijing.aliyuncs.com/2019-6/%E6%95%B0%E6%8D%AE%E5%BA%93%E5%9E%82%E7%9B%B4%E5%88%86%E5%8C%BA.png" alt="数据库垂直分区"></p>
<ul>
<li><strong>垂直拆分的优点：</strong> 可以使得列数据变小，在查询时减少读取的Block数，减少I/O次数。此外，垂直分区可以简化表的结构，易于维护。</li>
<li><strong>垂直拆分的缺点：</strong> 主键会出现冗余，需要管理冗余列，并会引起Join操作，可以通过在应用层进行Join来解决。此外，垂直分区会让事务变得更加复杂；</li>
</ul>
<h3><a name="t24"></a><a id="4__333"></a>4. 水平分区</h3>
<p><strong>保持数据表结构不变，通过某种策略存储数据分片。这样每一片数据分散到不同的表或者库中，达到了分布式的目的。 水平拆分可以支撑非常大的数据量。</strong></p>
<p>水平拆分是指数据表行的拆分，表的行数超过200万行时，就会变慢，这时可以把一张的表的数据拆成多张表来存放。举个例子：我们可以将用户信息表拆分成多个用户信息表，这样就可以避免单一表数据量过大对性能造成影响。</p>
<p><img src="https://my-blog-to-use.oss-cn-beijing.aliyuncs.com/2019-6/%E6%95%B0%E6%8D%AE%E5%BA%93%E6%B0%B4%E5%B9%B3%E6%8B%86%E5%88%86.png" alt="数据库水平拆分"></p>
<p>水平拆分可以支持非常大的数据量。需要注意的一点是：分表仅仅是解决了单一表数据过大的问题，但由于表的数据还是在同一台机器上，其实对于提升MySQL并发能力没有什么意义，所以 <strong>水平拆分最好分库</strong> 。</p>
<p>水平拆分能够 <strong>支持非常大的数据量存储，应用端改造也少</strong>，但 <strong>分片事务难以解决</strong>  ，跨节点Join性能较差，逻辑复杂。《Java工程师修炼之道》的作者推荐 <strong>尽量不要对数据进行分片，因为拆分会带来逻辑、部署、运维的各种复杂度</strong> ，一般的数据表在优化得当的情况下支撑千万以下的数据量是没有太大问题的。如果实在要分片，尽量选择客户端分片架构，这样可以减少一次和中间件的网络I/O。</p>
<p><strong>下面补充一下数据库分片的两种常见方案：</strong></p>
<ul>
<li><strong>客户端代理：</strong>  <strong>分片逻辑在应用端，封装在jar包中，通过修改或者封装JDBC层来实现。</strong> 当当网的 <strong>Sharding-JDBC</strong> 、阿里的TDDL是两种比较常用的实现。</li>
<li><strong>中间件代理：</strong> <strong>在应用和数据中间加了一个代理层。分片逻辑统一维护在中间件服务中。</strong> 我们现在谈的 <strong>Mycat</strong> 、360的Atlas、网易的DDB等等都是这种架构的实现。</li>
</ul>
<p>详细内容可以参考： <a href="https://segmentfault.com/a/1190000006158186" rel="nofollow" data-token="b3c8fc3b11074e2bd3f8951e470ce231">MySQL大表优化方案</a></p>
<h2><a name="t25"></a><a id="SQLMySQL_352"></a>一条SQL语句在MySQL中如何执行的</h2>
<p><a href="https://mp.weixin.qq.com/s?__biz=Mzg2OTA0Njk0OA==&amp;mid=2247485097&amp;idx=1&amp;sn=84c89da477b1338bdf3e9fcd65514ac1&amp;chksm=cea24962f9d5c074d8d3ff1ab04ee8f0d6486e3d015cfd783503685986485c11738ccb542ba7&amp;token=79317275&amp;lang=zh_CN#rd" rel="nofollow" data-token="91fc57e9e13f9a665f16076402cd1988">一条SQL语句在MySQL中如何执行的</a></p>
<h2><a name="t26"></a><a id="MySQL_356"></a>MySQL高性能优化规范建议</h2>
<p><a href="https://mp.weixin.qq.com/s?__biz=Mzg2OTA0Njk0OA==&amp;mid=2247485117&amp;idx=1&amp;sn=92361755b7c3de488b415ec4c5f46d73&amp;chksm=cea24976f9d5c060babe50c3747616cce63df5d50947903a262704988143c2eeb4069ae45420&amp;token=79317275&amp;lang=zh_CN#rd" rel="nofollow" data-token="27894dd2b90062d7cd10e664f254967c">MySQL高性能优化规范建议</a></p>
<h2><a name="t27"></a><a id="SQL_360"></a>一条SQL语句执行得很慢的原因有哪些？</h2>
<p><a href="https://mp.weixin.qq.com/s?__biz=Mzg2OTA0Njk0OA==&amp;mid=2247485185&amp;idx=1&amp;sn=66ef08b4ab6af5757792223a83fc0d45&amp;chksm=cea248caf9d5c1dc72ec8a281ec16aa3ec3e8066dbb252e27362438a26c33fbe842b0e0adf47&amp;token=79317275&amp;lang=zh_CN#rd" rel="nofollow" data-token="912cb4d535c6579f100a435506c6f844">腾讯面试：一条SQL语句执行得很慢的原因有哪些？—不看后悔系列</a></p>
<h2><a name="t28"></a><a id="_MySQL__364"></a>一千行 MySQL 学习笔记</h2>
<p><a href="https://mp.weixin.qq.com/s?__biz=Mzg2OTA0Njk0OA==&amp;mid=2247485025&amp;idx=1&amp;sn=1f4e19fc77af28f6795feff6ce7465b9&amp;chksm=cea249aaf9d5c0bc89a421c0759d27af3f55797a5fcff0111308307eff54fc4321c45ceb97ad&amp;token=283141110&amp;lang=zh_CN#rd" rel="nofollow" data-token="10094e726d13a618aceaa58982290d92">一千行 MySQL 学习笔记</a></p>
<h2><a name="t29"></a><a id="_368"></a>公众号</h2>
<p>如果大家想要实时关注我更新的文章以及分享的干货的话，可以关注我的公众号。</p>
<p><strong>《Java面试突击》:</strong> 由本文档衍生的专为面试而生的《Java面试突击》V2.0 PDF 版本<a href="#%E5%85%AC%E4%BC%97%E5%8F%B7" rel="nofollow" data-token="5175ed40ae48aa3e98c4c7d55fab81a2" target="_self">公众号</a>后台回复 <strong>“Java面试突击”</strong> 即可免费领取！</p>
<p><strong>Java工程师必备学习资源:</strong> 一些Java工程师常用学习资源公众号后台回复关键字 <strong>“1”</strong> 即可免费无套路获取。</p>
<p><img src="https://my-blog-to-use.oss-cn-beijing.aliyuncs.com/2019-6/167598cd2e17b8ec.png" alt="我的公众号"></p>

                                    </div>