---
title: "面试必问的`Redis`,你掌握多少？"
cover: "/img/lynk/17.jpg"
date:       2021-03-23
tags:
	- Linux
	- database
	- Redis
	- nosql
---
  
  
## 概述


`Redis` 是速度非常快的非关系型（NoSQL）内存键值数据库，可以存储键和五种不同类型的值之间的映射。

键的类型只能为字符串，值支持五种数据类型：字符串、列表、集合、散列表、有序集合。

`Redis` 支持很多特性，例如将内存中的数据持久化到硬盘中，使用复制来扩展读性能，使用分片来扩展写性能。



## 1、`Redis`支持多种类型的数据结构
1）.string：最基本的数据类型，二进制安全的字符串，最大512M。
2）.list：按照添加顺序保持顺序的字符串列表。
3）.set：无序的字符串集合，不存在重复的元素。
4）.sorted set：已排序的字符串集合。
5）.hash：key-value对的一种集合。

![图片](640.webp)

**具体操作，看这篇文章：**[**[基础\] PHP操作Redis，多操作几次你就会了**](http://mp.weixin.qq.com/s?__biz=MzIxMDA0OTcxNA==&mid=2654262356&idx=2&sn=99e16c11be6abe9ba7a45fed2141415d&chksm=8caafb89bbdd729f8c1cfb5d6ae0650dc47e741e3538f10e29e09fdb454ca27f94b2fedba8ce&scene=21#wechat_redirect)



## 2 使用`Redis`的优势？
**速度快**，因为数据存在内存中，类似于HashMap，HashMap的优势就是查找和操作的时间复杂度都是O(1)

**支持丰富数据类型**，支持string，list，set，sorted set，hash

**支持事务**，操作都是原子性，所谓的原子性就是对数据的更改要么全部执行，要么全部不执行

**丰富的特性**：可用于缓存，消息，按key设置过期时间，过期后将会自动删除



## 3 `Redis`单点吞吐量
单点TPS达到8万/秒，QPS达到10万/秒，补充下TPS和QPS的概念

QPS: 应用系统每秒钟最大能接受的用户访问量
每秒钟处理完请求的次数，注意这里是处理完，具体是指发出请求到服务器处理完成功返回结果。可以理解在server中有个counter，每处理一个请求加1，1秒后counter=QPS。

TPS： 每秒钟最大能处理的请求数
每秒钟处理完的事务次数，一个应用系统1s能完成多少事务处理，一个事务在分布式处理中，可能会对应多个请求，对于衡量单个接口服务的处理能力，用QPS比较合理。



## 4 `Redis`相比memcached有哪些优势？
1.memcached所有的值均是简单的字符串，`Redis`作为其替代者，支持更为丰富的数据类型
2.`Redis`的速度比memcached快很多
3.`Redis`可以持久化其数据
4.`Redis`支持数据的备份，即master-slave模式的数据备份。



## 5 `Redis`有哪几种数据淘汰策略？
在`Redis`中，允许用户设置最大使用内存大小server.maxmemory，当`Redis` 内存数据集大小上升到一定大小的时候，就会施行数据淘汰策略。

1.volatile-lru:从已设置过期的数据集中挑选最近最少使用的淘汰
2.volatile-ttr:从已设置过期的数据集中挑选将要过期的数据淘汰
3.volatile-random:从已设置过期的数据集中任意挑选数据淘汰
4.allkeys-lru:从数据集中挑选最近最少使用的数据淘汰
5.allkeys-random:从数据集中任意挑选数据淘汰
6.noenviction:禁止淘汰数据，`Redis`淘汰数据时还会同步到aof

作为内存数据库，出于对性能和内存消耗的考虑，`Redis` 的淘汰算法实际实现上并非针对所有 key，而是抽样一小部分并且从中选出被淘汰的 key。

使用 `Redis` 缓存数据时，为了提高缓存命中率，需要保证缓存数据都是热点数据。可以将内存最大使用量设置为热点数据占用的内存量，然后启用 allkeys-lru 淘汰策略，将最近最少使用的数据淘汰。

`Redis` 4.0 引入了 volatile-lfu 和 allkeys-lfu 淘汰策略，LFU 策略通过统计访问频率，将访问频率最少的键值对淘汰。



## 6 `Redis`提供了哪几种持久化方式？
1）RDB持久化方式能够在指定的时间间隔能对你的数据进行快照存储。
2）AOF持久化方式记录每次对服务器写的操作,当服务器重启的时候会重新执行这些命令来恢复原始的数据,AOF命令以`Redis`协议追加保存每次写的操作到文件末尾。

`Redis`还能对AOF文件进行后台重写,使得AOF文件的体积不至于过大。
如果你只希望你的数据在服务器运行的时候存在,你也可以不使用任何持久化方式。

你也可以同时开启两种持久化方式, 在这种情况下, 当`Redis`重启的时候会优先载入AOF文件来恢复原始的数据,因为在通常情况下AOF文件保存的数据集要比RDB文件保存的数据集要完整。



## 7 如何选择合适的持久化方式？

`Redis`主要提供了两种持久化机制：RDB和AOF

**RDB：**默认开启，会按照配置的指定时间将内存中的数据快照到磁盘中，创建一个dump.rdb文件，`Redis`启动时再恢复到内存中。

`Redis`会单独创建fork()一个子进程，将当前父进程的数据库数据复制到子进程的内存中，然后由子进程写入到临时文件中，持久化的过程结束了，再用这个临时文件替换上次的快照文件，然后子进程退出，内存释放。

需要注意的是，每次快照持久化都会将主进程的数据库数据复制一遍，导致内存开销加倍，若此时内存不足，则会阻塞服务器运行，直到复制结束释放内存；

都会将内存数据完整写入磁盘一次，所以如果数据量大的话，而且写操作频繁，必然会引起大量的磁盘I/O操作，严重影响性能，并且最后一次持久化后的数据可能会丢失；

**AOF：**以日志的形式记录每个写操作（读操作不记录），只需追加文件但不可以改写文件，`Redis`启动时会根据日志从头到尾全部执行一遍以完成数据的恢复工作。包括flushDB也会执行。

主要有两种方式触发：有写操作就写、每秒定时写（也会丢数据）。

因为AOF采用追加的方式，所以文件会越来越大，针对这个问题，新增了重写机制，就是当日志文件大到一定程度的时候，会fork出一条新进程来遍历进程内存中的数据，每条记录对应一条set语句，写到临时文件中，然后再替换到旧的日志文件（类似rdb的操作方式）。默认触发是当aof文件大小是上次重写后大小的一倍且文件大于64M时触发。

当两种方式同时开启时，**数据恢复`Redis`会优先选择AOF恢复**。一般情况下，只要使用默认开启的RDB即可，因为相对于AOF，RDB便于进行数据库备份，并且恢复数据集的速度也要快很多。

开启持久化缓存机制，对性能会有一定的影响，特别是当设置的内存满了的时候，更是下降到几百reqs/s。所以如果只是用来做缓存的话，可以关掉持久化。



## 8 `Redis`的事务**

一个事务包含了多个命令，服务器在执行事务期间，不会改去执行其它客户端的命令请求。

事务中的多个命令被一次性发送给服务器，而不是一条一条发送，这种方式被称为流水线，它可以减少客户端与服务器之间的网络通信次数从而提升性能。

`Redis` 最简单的事务实现方式是使用 MULTI 和 EXEC 命令将事务操作包围起来。



## 9 `Redis`集群之间是如何复制的？

通过使用 slaveof host port 命令来让一个服务器成为另一个服务器的从服务器。

一个从服务器只能有一个主服务器，并且不支持主主复制。



### **连接过程**

主服务器创建快照文件，发送给从服务器，并在发送期间使用缓冲区记录执行的写命令。快照文件发送完毕之后，开始向从服务器发送存储在缓冲区中的写命令；



从服务器丢弃所有旧数据，载入主服务器发来的快照文件，之后从服务器开始接受主服务器发来的写命令；

主服务器每执行一次写命令，就向从服务器发送相同的写命令。



### **主从链**

随着负载不断上升，主服务器可能无法很快地更新所有从服务器，或者重新连接和重新同步从服务器将导致系统超载。



为了解决这个问题，可以创建一个中间层来分担主服务器的复制工作。中间层的服务器是最上层服务器的从服务器，又是最下层服务器的主服务器。





## 10 `Redis`如何做内存优化？
尽可能使用散列表（hashes），散列表（是说散列表里面存储的数少）使用的内存非常小，所以你应该尽可能的将你的数据模型抽象到一个散列表里面。



比如你的web系统中有一个用户对象，不要为这个用户的名称，姓氏，邮箱，密码设置单独的key,而是应该把这个用户的所有信息存储到一张散列表里面.





## 11 `Redis`回收进程如何工作的？
一个客户端运行了新的命令，添加了新的数据。

Redi检查内存使用情况，如果大于maxmemory的限制, 则根据设定好的策略进行回收。





## 12 使用过`Redis`分布式锁么，它是什么回事？

先拿setnx来争抢锁，抢到之后，再用expire给锁加一个过期时间防止锁忘记了释放。



这时候对方会告诉你说你回答得不错，然后接着问如果在setnx之后执行expire之前进程意外crash或者要重启维护了，那会怎么样？



这时候你要给予惊讶的反馈：唉，是喔，这个锁就永远得不到释放了。紧接着你需要抓一抓自己得脑袋，故作思考片刻，好像接下来的结果是你主动思考出来的。



然后回答：我记得set指令有非常复杂的参数，这个应该是可以同时把setnx和expire合成一条指令来用的！对方这时会显露笑容，心里开始默念：嗯，这小子还不错。





## 13 `Redis`里面有1亿个key，其中有10w个key是以某个固定的已知的前缀开头的，如何将它们全部找出来？

使用keys指令可以扫出指定模式的key列表。

对方接着追问：如果这个`Redis`正在给线上的业务提供服务，那使用keys指令会有什么问题？



这个时候你要回答`Redis`关键的一个特性：`Redis`的单线程的。keys指令会导致线程阻塞一段时间，线上服务会停顿，直到指令执行完毕，服务才能恢复。



这个时候可以使用scan指令，scan指令可以无阻塞的提取出指定模式的key列表，但是会有一定的重复概率，在客户端做一次去重就可以了，但是整体所花费的时间会比直接用keys指令长。





## 14 使用过`Redis`做异步队列么，你是怎么用的？

一般使用list结构作为队列，rpush生产消息，lpop消费消息。当lpop没有消息的时候，要适当sleep一会再重试。



**如果对方追问可不可以不用sleep呢？**list还有个指令叫blpop，在没有消息的时候，它会阻塞住直到消息到来。



**如果对方追问能不能生产一次消费多次呢？**使用pub/sub主题订阅者模式，可以实现1:N的消息队列。



**如果对方追问pub/sub有什么缺点？**在消费者下线的情况下，生产的消息会丢失，得使用专业的消息队列如Rabbitmq等。



**如果对方追问`Redis`如何实现延时队列？**我估计现在你很想把面试官一棒打死。如果你手上有一根棒球棍的话，怎么问的这么详细。但是你很克制，然后神态自若的回答道：使用sortedset，拿时间戳作为score，消息内容作为key调用zadd来生产消息，消费者用zrangebyscore指令获取N秒之前的数据轮询进行处理。





## 15 如果有大量的key需要设置同一时间过期，一般需要注意什么？

如果大量的key过期时间设置的过于集中，到过期的那个时间点，`Redis`可能会出现短暂的卡顿现象。一般需要在时间上加一个随机值，使得过期时间分散一些。





## 16 `Redis`的同步机制了解么？

**从从同步。**第一次同步时，主节点做一次bgsave，并同时将后续修改操作记录到内存buffer，待完成后将rdb文件全量同步到复制节点，复制节点接受完成后将rdb镜像加载到内存。



加载完成后，再通知主节点将期间修改的操作记录同步到复制节点进行重放就完成了同步过程。





## 17 Reids哈希冲突，如何解决？

### 1.线性探测法：

如果hash函数计算得出的存储位置一杯占用，那么将继续向后寻找空间的位置进行存放

缺点：hash一旦冲突，将会增加查询的时间复杂度，由原来的O(1)转化成O(n)，hash冲出越多，效率越低



随着hash表越来越满，哈希冲的概率就越大，所以的哈希表都有一个衡量因子，即加载因子（loadfactor = 0.75）



公式： 以占有的hash位置 / 总的hash位置 > loadfactor O(1)



### 2.链地址法(拉链法)：

把哈希冲突冲突的元素都放在一个链表中，但是链表的长度不能太长，越长效率越慢



时刻关注哈希表的loadfactor加载因子，如果查过及时进行扩容操作，扩容后原来表的hash数据，需要重新hash



如图：

![图片](640-1616417574130.webp)


 **文章来自：https://blog.csdn.net/weixin_36380516/article/details/107171865**

***\*以上是本文的全部内容，希望对大家的学习有帮助，觉得有用，有需要就支持一下吧\****