---
title: "redis笔记04"
date:       2019-12-18
subtitle: "redis高级部分"
tags:
	- Linux
	- deepin
	- database
	- redis
	- nosql
---
  
  
  



* content
{:toc}


## Redis 数据备份与恢复
Redis SAVE 命令用于创建当前数据库的备份。

### 语法
redis Save 命令基本语法如下：

```
redis 127.0.0.1:6379> SAVE 
```

### 实例

```
redis 127.0.0.1:6379> SAVE 
OK
```

该命令将在 redis 安装目录中创建`dump.rdb`文件。

### 恢复数据
如果需要恢复数据，只需将备份文件 (dump.rdb) 移动到 redis 安装目录并启动服务即可。获取 redis 目录可以使用 CONFIG 命令，如下所示：
```
redis 127.0.0.1:6379> CONFIG GET dir
1) "dir"
2) "/usr/local/redis/bin"
```

以上命令 CONFIG GET dir 输出的 redis 安装目录为 /usr/local/redis/bin。

### Bgsave
创建 redis 备份文件也可以使用命令 BGSAVE，该命令在后台执行。

### 实例

```
127.0.0.1:6379> BGSAVE
Background saving started
```

## Redis 安全
我们可以通过 redis 的配置文件设置密码参数，这样客户端连接到 redis 服务就需要密码验证，这样可以让你的 redis 服务更安全。

### 实例
我们可以通过以下命令查看是否设置了密码验证：

```
127.0.0.1:6379> CONFIG get requirepass

1) "requirepass"
2) ""
```
默认情况下 requirepass 参数是空的，这就意味着你无需通过密码验证就可以连接到 redis 服务。

你可以通过以下命令来修改该参数：

```
127.0.0.1:6379> CONFIG set requirepass "w3cschool.cn"
OK
127.0.0.1:6379> CONFIG get requirepass
1) "requirepass"
2) "w3cschool.cn"
```

设置密码后，客户端连接 redis 服务就需要密码验证，否则无法执行命令。

### 语法
AUTH 命令基本语法格式如下：

```
127.0.0.1:6379> AUTH password
```

### 实例

```
127.0.0.1:6379> AUTH "w3cschool.cn"
OK
127.0.0.1:6379> SET mykey "Test value"
OK
127.0.0.1:6379> GET mykey
"Test value"
```


## Redis 客户端连接
Redis 通过监听一个 TCP 端口或者 Unix socket 的方式来接收来自客户端的连接，当一个连接建立后，Redis 内部会进行以下一些操作：

- 首先，客户端 socket 会被设置为非阻塞模式，因为 Redis 在网络事件处理上采用的是非阻塞多路复用模型。
- 然后为这个 socket 设置 TCP_NODELAY 属性，禁用 Nagle 算法
- 然后创建一个可读的文件事件用于监听这个客户端 socket 的数据发送

## redis管道技术
redis管道技术可以在服务端未响应时,客户端可以继续想服务端发送请求,并最终一次性读取所有服务端的响应

### 实例
查看redis管道,只需要启动redis实例并输入以下命令:

```
$(echo -en "PING\r\n SET w3ckey redis\r\nGET w3ckey\r\nINCR visitor\r\nINCR visitor\r\nINCR visitor\r\n"; sleep 10) | nc localhost 6379

+PONG
+OK
redis
:1
:2
:3
```
以上实例中我们通过使用PING命令查看redis服务是否可用,之后我们设置了w3ckey的值尾redis.然后我们获取w3ckey的值并使得visitor自增3次.
在返回的结果中我们可以看到这些命令一次性向redis服务提交,并最终一次性读取所有服务端的响应

### 管道技术的优势
管道技术最显著的优势是提高了redis服务的性能
### 一些测试数据
在下面的测试中,我们将使用redis的Ruby客户端,支持管道技术特性,测试管道技术对速度的提升效果

从处于局域网中的Mac OS X系统上执行上面这个简单脚本的数据表明，开启了管道操作后，往返时延已经被改善得相当低了。

```
without pipelining 1.185238 seconds 
with pipelining 0.250783 seconds
```

如你所见，开启管道后，我们的速度效率提升了5倍。

## redis 分区
分区是分割数据到多个redis实例的处理过程,因此每个实例只保存key的一个子集.

### 分区的优势
- 通过利用多台计算机内存的和值,允许我们构造跟大的数据库
- 通过多核和多台计算机,允许我们扩展计算能力;通过多台计算机和网络适配器,扩展网络带宽

### 分区的不足
redis的一些特性在分区方面表现的不是很好:
- 涉及多个key的操作通常是不被支持的.举例来说,当两个set映射到不同的redis实例时,你就补鞥呢对这两个set执行交集操作.
- 涉及多个key和redis事务不能使用
- 当使用分区时,数据处理较为复杂,比如你需要处理多个rdb/aof文件,并且从多个主机备份持久化文件
- 增加或者删除容量也比较复杂.redis集群大多数支持在运行时增加,删除节点的透明数据平衡的能力,但是类似于客户端分区,代理等其他系统则不支持这项特性.然而,一种叫做presharding的技术对此是有帮助的.

### 分区类型
redis 有两种类型的分区.假设有4个redis实例,R0,R1,R2,R3 和类似user:1,user:2这样的表示用户的多个key,对既定的key有多种不同方式来选择这个key存放在哪个实例中,也就是说,有不同的系统来映射某个key到某个redis服务

### 范围分区
最简单的分区方式是安范围分区,就是映射一定范围的对象到特定的redis实例
比如,id从0到10000的用户会保存到实例R0,ID从10001到 20000的用户会保存到R1，以此类推。

这种方式是可行的，并且在实际中使用，不足就是要有一个区间范围到实例的映射表。这个表要被管理，同时还需要各 种对象的映射表，通常对Redis来说并非是好的方法。

### 哈希分区
另外一种分区方法是hash分区。这对任何key都适用，也无需是object_name:这种形式，像下面描述的一样简单：

- 用一个hash函数将key转换为一个数字，比如使用crc32 hash函数。对key foobar执行crc32(foobar)会输出类似93024922的整数。
- 对这个整数取模，将其转化为0-3之间的数字，就可以将这个整数映射到4个Redis实例中的一个了。93024922 % 4 = 2，就是说key foobar应该被存到R2实例中。注意：取模操作是取除的余数，通常在多种编程语言中用%操作符实现。













































