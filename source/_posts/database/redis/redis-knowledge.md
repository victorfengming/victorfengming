---
title: "关于redis，学会这8点就够了"
cover: "/img/lynk/89.jpg"
date:       2019-09-28
tags:
	- Linux
	- deepin
	- database
	- redis
	- nosql
---
  
<div class="htmledit_views" id="content_views">
                                            <p style="margin-left:10px;"><strong>1，redis是什么</strong></p>

<p style="margin-left:10px;"><a href="https://www.huaweicloud.com/product/dcs.html?wx" rel="nofollow" data-token="f27424da9cfb05f20ea8d00dc1ead38b">redis</a>是一种支持Key-Value等多种数据结构的存储系统。可用于缓存，事件发布或订阅，高速队列等场景。该数据库使用ANSI C语言编写，支持网络，提供字符串，哈希，列表，队列，集合结构直接存取，基于内存，可持久化。</p>

<p style="margin-left:10px;">&nbsp;</p>

<p style="margin-left:10px;"><strong>2，支持的语言</strong></p>

<p style="margin-left:10px;"><img alt="" class="has" height="105" src="https://img-blog.csdnimg.cn/20181224163405267" width="553"></p>

<p style="margin-left:10px;">&nbsp;</p>

<p style="margin-left:10px;"><strong>3，redis的应用场景有哪些</strong></p>

<p style="margin-left:10px;">1，会话缓存（最常用）<br>
2，消息队列，<br>
比如支付3，活动排行榜或计数<br>
4，发布，订阅消息（消息通知）<br>
5，商品列表，评论列表等</p>

<p style="margin-left:10px;">&nbsp;</p>

<p style="margin-left:10px;"><strong>4，redis数据类型</strong><br><strong><u><a href="https://www.huaweicloud.com/product/dcs.html?wx" rel="nofollow" data-token="f27424da9cfb05f20ea8d00dc1ead38b"><span style="color:#f33b45;">Redis</span></a></u></strong>一共支持五种数据类：string（字符串），hash（哈希），list（列表），set（集合）和zset（sorted set有序集合）。</p>

<p style="margin-left:10px;">（1）字符串（字符串）<br>
它是redis的最基本的数据类型，一个键对应一个值，需要注意是一个键值最大存储512MB。</p>

<p style="margin-left:10px;"><img alt="" class="has" height="225" src="https://img-blog.csdnimg.cn/20181224163405288" width="554"></p>

<p style="margin-left:10px;">（2）hash（哈希）<br>
redis hash是一个键值对的集合，是一个string类型的field和value的映射表，适合用于存储对象</p>

<p style="margin-left:10px;"><img alt="" class="has" height="244" src="https://img-blog.csdnimg.cn/20181224163405306" width="644"></p>

<p style="margin-left:10px;">（3）表（列表）<br>
是redis的简单的字符串列表，它按插入顺序排序</p>

<p style="margin-left:10px;"><img alt="" class="has" height="227" src="https://img-blog.csdnimg.cn/20181224163405324" width="637"></p>

<p style="margin-left:10px;">（4）组（集合）<br>
是字符串类型的无序集合，也不可重复</p>

<p style="margin-left:10px;"><img alt="" class="has" height="499" src="https://img-blog.csdnimg.cn/20181224163405342" width="634"></p>

<p style="margin-left:10px;">（5）zset（sorted set有序集合）<br>
是string类型的有序集合，也不可重复<br>
有序集合中的每个元素都需要指定一个分数，根据分数对元素进行升序排序，如果多个元素有相同的分数，则以字典序进行升序排序，sorted set因此非常适合实现排名</p>

<p style="margin-left:10px;"><img alt="" class="has" height="671" src="https://img-blog.csdnimg.cn/20181224163405363" width="626"></p>

<p style="margin-left:10px;">&nbsp;</p>

<p style="margin-left:10px;"><strong>5，redis的服务相关的命令</strong></p>

<p style="margin-left:10px;"><img alt="" class="has" height="478" src="https://img-blog.csdnimg.cn/20181224163405380" width="628"></p>

<p style="margin-left:10px;">slect＃选择数据库（数据库编号0-15）<br>
退出＃退出连接<br>
信息＃获得服务的信息与统计<br>
monitor＃实时监控<br>
config get＃获得服务配置<br>
flushdb＃删除当前选择的数据库中的key<br>
flushall＃删除所有数据库中的键</p>

<p style="margin-left:10px;">&nbsp;</p>

<p style="margin-left:10px;"><strong>6，redis的发布与订阅</strong></p>

<p style="margin-left:10px;">redis的发布与订阅（发布/订阅）是它的一种消息通信模式，一方发送信息，一方接收信息。<br>
下图是三个客户端同时订阅同一个频道</p>

<p style="margin-left:10px;"><img alt="" class="has" height="198" src="https://img-blog.csdnimg.cn/20181224163405400" width="319"></p>

<p style="margin-left:10px;">下图是有新信息发送给频道1时，就会将消息发送给订阅它的三个客户端<br><img alt="" class="has" height="285" src="https://img-blog.csdnimg.cn/20181224163405417" width="315"></p>

<p style="margin-left:10px;">&nbsp;</p>

<p style="margin-left:10px;">&nbsp;</p>

<p style="margin-left:10px;"><strong>7，redis的持久化</strong></p>

<p style="margin-left:10px;">redis持久有两种方式：快照（快照），仅附加文件（AOF）</p>

<p style="margin-left:10px;">快照（快照）</p>

<p style="margin-left:10px;">1，将存储在内存的数据以快照的方式写入二进制文件中，如默认dump.rdb中<br>
2，保存900 1&nbsp;</p>

<p style="margin-left:10px;">＃900秒内如果超过1个Key被修改，则启动快照保存<br>
3，保存300 10&nbsp;</p>

<p style="margin-left:10px;">＃300秒内如果超过10个Key被修改，则启动快照保存<br>
4，保存60 10000&nbsp;</p>

<p style="margin-left:10px;">＃60秒内如果超过10000个重点被修改，则启动快照保存<br>
&nbsp;</p>

<p style="margin-left:10px;">仅附加文件（AOF）</p>

<p style="margin-left:10px;">1，使用AOF持久时，服务会将每个收到的写命令通过写函数追加到文件中（appendonly.aof）<br>
2，AOF持久化存储方式参数说明<br>
&nbsp; &nbsp;&nbsp;appendonly yes &nbsp;</p>

<p style="margin-left:10px;">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;＃开启AOF持久化存储方式&nbsp;<br>
&nbsp; &nbsp; appendfsync always&nbsp;</p>

<p style="margin-left:10px;">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;＃收到写命令后就立即写入磁盘，效率最差，效果最好<br>
&nbsp; &nbsp; appendfsync everysec</p>

<p style="margin-left:10px;">&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;&nbsp;＃每秒写入磁盘一次，效率与效果居中<br>
&nbsp; &nbsp; appendfsync no&nbsp;</p>

<p style="margin-left:10px;">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;＃完全依赖操作系统，效率最佳，效果没法保证</p>

<p style="margin-left:10px;">&nbsp;</p>

<p style="margin-left:10px;"><strong>8，redis的性能测试</strong></p>

<p style="margin-left:10px;">自带相关测试工具</p>

<p style="margin-left:10px;"><img alt="" class="has" height="779" src="https://img-blog.csdnimg.cn/20181224163405438" width="570"></p>

<p style="margin-left:10px;">实际测试同时执行100万的请求</p>

<p style="margin-left:10px;"><img alt="" class="has" height="299" src="https://img-blog.csdnimg.cn/20181224163405456" width="632"></p>

<p style="margin-left:10px;">&nbsp;</p>

<p style="margin-left:10px;">【本文由<strong><a href="https://www.huaweicloud.com/product/dcs.html?wx" rel="nofollow" data-token="f27424da9cfb05f20ea8d00dc1ead38b">中间件小哥</a></strong>收集整理自“民工哥的Linux的运维”】</p>
                                    </div>