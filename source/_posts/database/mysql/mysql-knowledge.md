---
title: "MySql数据库知识学习笔记------索引，优化，事务"
date:       2019-09-28
tags:
	- Linux
	- deepin
	- database
	- mysql
---
  
<div id="article_content" class="article_content clearfix">
                                                <div class="article-copyright">
                <span class="creativecommons">
                <a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/">
                    </a>
            <span>
                版权声明：本文为博主原创文章，遵循<a href="http://creativecommons.org/licenses/by-sa/4.0/" target="_blank" rel="noopener"> CC 4.0 BY-SA </a>版权协议，转载请附上原文出处链接和本声明。            </span>
               <div class="article-source-link2222">
                    本文链接：<a href="https://blog.csdn.net/bupttulongming/article/details/101466955">https://blog.csdn.net/bupttulongming/article/details/101466955</a>
                </div>
            </span>
                    </div>
                                                    <link rel="stylesheet" href="https://csdnimg.cn/release/phoenix/template/css/ck_htmledit_views-3019150162.css">
                                        <div id="content_views" class="markdown_views prism-atom-one-dark">
                    <!-- flowchart 箭头图标 勿删 -->
                    <svg xmlns="http://www.w3.org/2000/svg" style="display: none;">
                        <path stroke-linecap="round" d="M5,0 0,2.5 5,5z" id="raphael-marker-block" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);"></path>
                    </svg>
                                            <p><strong>一.事务是什么，事务的四大特性？</strong></p>
<p><img src="https://img-blog.csdnimg.cn/2019092619334088.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2J1cHR0dWxvbmdtaW5n,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述"></p>
<p><strong>二.并发事务带来的问题</strong></p>
<ul>
<li><strong>脏读（Dirty read）</strong>: 当一个事务正在访问数据并且对数据进行了修改，而这种修改还没有提交到数据库中，这时另外一个事务也访问了这个数据，然后使用了这个数据。因为这个数据是还没有提交的数据，那么另外一个事务读到的这个数据是“脏数据”，依据“脏数据”所做的操作可能是不正确的。</li>
<li><strong>不可重复读（Unrepeatableread）</strong>: 指在一个事务内多次读同一数据。在这个事务还没有结束时，另一个事务也访问该数据。那么，在第一个事务中的两次读数据之间，由于第二个事务的修改导致第一个事务两次读取的数据可能不太一样。这就发生了在一个事务内两次读到的数据是不一样的情况，因此称为不可重复读。</li>
<li><strong>幻读（Phantom read）</strong>: 幻读与不可重复读类似。它发生在一个事务（T1）读取了几行数据，接着另一个并发事务（T2）插入了一些数据时。在随后的查询中，第一个事务（T1）就会发现多了一些原本不存在的记录，就好像发生了幻觉一样，所以称为幻读。<br>
<em><strong>不可重复读和幻读的区别是，一个是多次读同一条数据，发现数据的值不一样了；一个是读取数据时，数据本身并未变化，而是记录的数目变多了。</strong></em></li>
</ul>
<p><strong>三.事务的四个隔离级别</strong></p>
<ol>
<li><strong>READ-UNCOMMITTED(读取未提交)</strong>： 最低的隔离级别，允许读取尚未提交的数据变更，可能会导致脏读、幻读或不可重复读。</li>
<li><strong>READ-COMMITTED(读取已提交)</strong>： 允许读取并发事务已经提交的数据，可以阻止脏读，但是幻读或不可重复读仍有可能发生。</li>
<li><strong>REPEATABLE-READ(可重复读)</strong>： 对同一字段的多次读取结果都是一致的，除非数据是被本身事务自己所修改，可以阻止脏读和不可重复读，但幻读仍有可能发生。</li>
<li><strong>SERIALIZABLE(可串行化)</strong>： 最高的隔离级别，完全服从ACID的隔离级别。所有的事务依次逐个执行，这样事务之间就完全不可能产生干扰，也就是说，该级别可以防止脏读、不可重复读以及幻读</li>
</ol>
<p><img src="https://img-blog.csdnimg.cn/20190926193705742.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2J1cHR0dWxvbmdtaW5n,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述"><br>
MYSQL的默认隔离级别是可重复读</p>
<p><strong>四.MySql数据库底层是B+树</strong></p>
<p><strong>五.乐观锁&amp;悲观锁</strong></p>
<ul>
<li><strong>悲观锁</strong>：总是假设最坏的情况，每次去拿数据的时候都认为别人会修改，所以每次在拿数据的时候都会上锁，这样别人想拿这个数据就会阻塞直到它拿到锁（共享资源每次只给一个线程使用，其它线程阻塞，用完后再把资源转让给其它线程）。Java中synchronized和ReentrantLock等独占锁就是悲观锁思想的实现。</li>
<li><strong>乐观锁</strong>：总是假设最好的情况，每次去拿数据的时候都认为别人不会修改，所以不会上锁，但是在更新的时候会判断一下在此期间别人有没有去更新这个数据，可以使用版本号机制和CAS算法实现。<strong>乐观锁适用于多读的应用类型</strong>，这样可以提高吞吐量，像数据库提供的类似于write_condition机制，其实都是提供的乐观锁。在Java中java.util.concurrent.atomic包下面的原子变量类就是使用了乐观锁的一种实现方式CAS实现的。</li>
</ul>
<p><strong>像乐观锁适用于写比较少的情况下（多读场景），即冲突真的很少发生的时候，这样可以省去了锁的开销，加大了系统的整个吞吐量。但如果是多写的情况，一般会经常产生冲突，这就会导致上层应用会不断的进行retry，这样反倒是降低了性能，所以一般多写的场景下用悲观锁就比较合适。</strong><br>
<br></p>
<p><strong>六.乐观锁的实现方式</strong></p>
<ul>
<li>
<p><strong>版本号机制</strong>：一般是在数据表中加上一个数据版本号version字段，表示数据被修改的次数，当数据被修改时，version值会加一。当线程A要更新数据值时，在读取数据的同时也会读取version值，在提交更新时，若刚才读取到的version值为当前数据库中的version值相等时才更新，否则重试更新操作，直到更新成功。</p>
</li>
<li>
<p><strong>CAS</strong>：compare and swap（比较与交换），是一种无锁算法。无锁编程，即不使用锁的情况下实现多线程之间的变量同步，也就是在没有线程被阻塞的情况下实现变量的同步，所以也叫非阻塞同步（Non-blocking Synchronization）。CAS算法涉及到三个操作数：</p>
<ul>
<li>需要读写的内存 V</li>
<li>进行比较的值A</li>
<li>新值B<br>
<strong>当且仅当 V 的值等于 A时，CAS通过原子方式用新值B来更新V的值，否则不会执行任何操作（比较和替换是一个原子操作）。一般情况下是一个自旋操作，即不断的重试。</strong></li>
</ul>
</li>
</ul>
<p><strong>七.自旋锁</strong><br>
是指当一个线程在获取锁的时候，如果锁已经被其它线程获取，那么该线程将循环等待，然后不断的判断锁是否能够被成功获取，直到获取到锁才会退出循环。</p>
<p><strong>八.MyISAM和InnoDB存储引擎使用的锁：</strong></p>
<ul>
<li>MyISAM 采用表级锁(table-level locking)</li>
<li>InnoDB 支持行级锁(row-level locking)和表级锁,默认为行级锁</li>
</ul>
<p><strong>表级锁：Mysql中锁定粒度最大 的一种锁，对当前操作的整张表加锁，实现简单，资源消耗也比较少，加锁快，不会出现死锁。其锁定粒度最大，触发锁冲突的概率最高，并发度最低，MyISAM和 InnoDB引擎都支持表级锁。</strong><br>
<strong>行级锁： Mysql中锁定 粒度最小 的一种锁，只针对当前操作的行进行加锁。 行级锁能大大减少数据库操作的冲突。其加锁粒度最小，并发度高，但加锁的开销也最大，加锁慢，会出现死锁。</strong></p>
<p><strong>九.大表优化</strong></p>
<p>常见的优化措施：</p>
<ol>
<li><strong>限定数据的范围</strong>：务必禁止不带任何限制数据范围条件的查询语句。比如：我们当用户在查询订单历史的时候，我们可以控制在一个月的范围内；</li>
<li><strong>读/写分离</strong>：经典的数据库拆分方案，主库负责写，从库负责读；</li>
<li><strong>垂直分区</strong>：根据数据库里面数据表的相关性进行拆分。 例如，用户表中既有用户的登录信息又有用户的基本信息，可以将用户表拆分成两个单独的表，甚至放到单独的库做分库。</li>
<li><strong>垂直拆分的优点缺点</strong>：优点：可以使得列数据变小，在查询时减少读取的Block数，减少I/O次数。此外，垂直分区可以简化表的结构，易于维护。<strong>缺点：主键会出现冗余</strong>，需要管理冗余列，并会引起Join操作，可以通过在应用层进行Join来解决。此外，垂直分区会让事务变得更加复杂；</li>
<li><strong>水平分区</strong>：保持数据表结构不变，通过某种策略存储数据分片。这样每一片数据分散到不同的表或者库中，达到了分布式的目的。 水平拆分可以支撑非常大的数据量。**水平拆分可以支持非常大的数据量。需要注意的一点是：分表仅仅是解决了单一表数据过大的问题，但由于表的数据还是在同一台机器上，其实对于提升MySQL并发能力没有什么意义，所以 水平拆分最好分库 **</li>
<li>水平拆分能够 支持非常大的数据量存储，应用端改造也少，但 分片事务难以解决 ，跨节点Join性能较差，逻辑复杂。《Java工程师修炼之道》的作者推荐 尽量不要对数据进行分片，因为拆分会带来逻辑、部署、运维的各种复杂度 ，一般的数据表在优化得当的情况下支撑千万以下的数据量是没有太大问题的。如果实在要分片，尽量选择客户端分片架构，这样可以减少一次和中间件的网络I/O。</li>
</ol>
<p><strong>十.SQL查询优化</strong></p>
<ul>
<li>可通过开启慢查询日志查找出较慢的SQL.</li>
<li>不做列运算: SELECT id WHERE age+1=10 ,任何对列的操作都将导致全表扫描.它包括数据库教程函数,计算表达式等等,查询时尽量将操作移至等号右边. —&gt;age=10-1</li>
<li>SQL语句尽可能简单:一条SQL只能在一个cpu进行运算;大语句拆分成小语句,减少锁时间;一条大SQL可以堵死整个库.</li>
<li>不用 SELECT *.</li>
<li>少用 JOIN.</li>
<li>避免 %xxx式查询.</li>
<li>不用函数和触发器,在应用程序实现.</li>
<li>尽量避免在WHERE 子句中使用!= &lt;&gt;操作,否则将导致引擎放弃索引使用全表扫描.</li>
</ul>

                                    </div>
                <link href="https://csdnimg.cn/release/phoenix/mdeditor/markdown_views-095d4a0b23.css" rel="stylesheet">
                    </div>