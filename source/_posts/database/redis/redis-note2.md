---
title: "redis笔记02"
date:       2019-12-18
subtitle: "redis安装以及配置"
tags:
	- Linux
	- deepin
	- database
	- redis
	- nosql
---
  
  
  








## Redis 安装
### Window 下安装
下载地址：https://github.com/dmajkic/redis/downloads。

下载到的Redis支持32bit和64bit。根据自己实际情况选择，将64bit的内容cp到自定义盘符安装目录取名redis。 如 C:\redis

打开一个cmd窗口 使用cd命令切换目录到 C:\redis 运行 redis-server.exe redis.conf 。（如果下载的是Redis-x64-3.2.100版本，是运行 redis-server.exe redis.windows.conf）

如果想方便的话，可以把redis的路径加到系统的环境变量里，这样就省得再输路径了，后面的那个redis.conf可以省略，如果省略，会启用默认的。


这时候另启一个cmd窗口，原来的不要关闭，不然就无法访问服务端了。

切换到redis目录下运行 redis-cli.exe -h 127.0.0.1 -p 6379 。

设置键值对 set myKey abc

取出键值对 get myKey

### Ubuntu 下安装
在 Ubuntu 系统安装 Redi 可以使用以下命令:

```shell
$sudo apt-get update
$sudo apt-get install redis-server
```
启动 Redis

```
$redis-server
```

查看 redis 是否启动？

```
$redis-cli
```

以上命令将打开以下终端：
```
redis 127.0.0.1:6379>
```

127.0.0.1 是本机 IP ，6379 是 redis 服务端口。现在我们输入 PING 命令。

```
redis 127.0.0.1:6379> ping
PONG
```
以上说明我们已经成功安装了redis。

## Redis 配置

Redis 的配置文件位于 Redis 安装目录下，文件名为 redis.conf。

你可以通过 CONFIG 命令查看或设置配置项。
### 语法
Redis CONFIG 命令格式如下：

```
redis 127.0.0.1:6379> CONFIG GET CONFIG_SETTING_NAME
```
### 实例

```
redis 127.0.0.1:6379> CONFIG GET loglevel

1) "loglevel"
2) "notice"
```

使用 * 号获取所有配置项：

```
redis 127.0.0.1:6379> CONFIG GET *
 1) "dir"
 2) "C:\\Users\\Administrator"
 3) "dbfilename"
 4) "dump.rdb"
 5) "requirepass"
 6) (nil)
 7) "masterauth"
 8) (nil)
 9) "maxmemory"
10) "0"
11) "maxmemory-policy"
12) "volatile-lru"
13) "maxmemory-samples"
14) "3"
15) "timeout"
16) "0"
17) "appendonly"
18) "no"
19) "no-appendfsync-on-rewrite"
20) "no"
21) "appendfsync"
22) "everysec"
23) "save"
24) "3600 1 300 100 60 10000"
25) "auto-aof-rewrite-percentage"
26) "100"
27) "auto-aof-rewrite-min-size"
28) "1048576"
29) "slave-serve-stale-data"
30) "yes"
31) "hash-max-zipmap-entries"
32) "512"
33) "hash-max-zipmap-value"
34) "64"
35) "list-max-ziplist-entries"
36) "512"
37) "list-max-ziplist-value"
38) "64"
39) "set-max-intset-entries"
40) "512"
41) "zset-max-ziplist-entries"
42) "128"
43) "zset-max-ziplist-value"
44) "64"
45) "slowlog-log-slower-than"
46) "10000"
47) "slowlog-max-len"
48) "64"
49) "loglevel"
50) "verbose"
```

### 编辑配置
你可以通过修改 redis.conf 文件或使用 CONFIG set 命令来修改配置。

### 语法
`CONFIG SET` 命令基本语法：

```
redis 127.0.0.1:6379> CONFIG SET CONFIG_SETTING_NAME NEW_CONFIG_VALUE
```

### 实例

```
redis 127.0.0.1:6379> CONFIG SET loglevel "notice"
OK
redis 127.0.0.1:6379> CONFIG GET loglevel

1) "loglevel"
2) "notice"
```

### 参数说明
参数说明
redis.conf 配置项说明如下：

1. Redis默认不是以守护进程的方式运行，可以通过该配置项修改，使用yes启用守护进程

    `daemonize no`

2. 当Redis以守护进程方式运行时，Redis默认会把pid写入/var/run/redis.pid文件，可以通过pidfile指定

   ` pidfile /var/run/redis.pid`

3. 指定Redis监听端口，默认端口为6379，作者在自己的一篇博文中解释了为什么选用6379作为默认端口，因为6379在手机按键上MERZ对应的号码，而MERZ取自意大利歌女Alessia Merz的名字

    `port 6379`

4. 绑定的主机地址

    `bind 127.0.0.1`

5. 当 客户端闲置多长时间后关闭连接，如果指定为0，表示关闭该功能

    `timeout 300`

6. 指定日志记录级别，Redis总共支持四个级别：debug、verbose、notice、warning，默认为verbose

    `loglevel verbose`

7. 日志记录方式，默认为标准输出，如果配置Redis为守护进程方式运行，而这里又配置为日志记录方式为标准输出，则日志将会发送给/dev/null

    `logfile stdout`

8. 设置数据库的数量，默认数据库为0，可以使用SELECT <dbid>命令在连接上指定数据库id

    `databases 16`

9. 指定在多长时间内，有多少次更新操作，就将数据同步到数据文件，可以多个条件配合

   ` save <seconds> <changes>`

    Redis默认配置文件中提供了三个条件：

    `save 900 1`

    `save 300 10`

    `save 60 10000`

    分别表示900秒（15分钟）内有1个更改，300秒（5分钟）内有10个更改以及60秒内有10000个更改。

 

10. 指定存储至本地数据库时是否压缩数据，默认为yes，Redis采用LZF压缩，如果为了节省CPU时间，可以关闭该选项，但会导致数据库文件变的巨大

    `rdbcompression yes`

11. 指定本地数据库文件名，默认值为dump.rdb

    `dbfilename dump.rdb`

12. 指定本地数据库存放目录

    `dir ./`

13. 设置当本机为slav服务时，设置master服务的IP地址及端口，在Redis启动时，它会自动从master进行数据同步

    `slaveof <masterip> <masterport>`

14. 当master服务设置了密码保护时，slav服务连接master的密码

    `masterauth <master-password>`

15. 设置Redis连接密码，如果配置了连接密码，客户端在连接Redis时需要通过AUTH <password>命令提供密码，默认关闭

    `requirepass foobared`

16. 设置同一时间最大客户端连接数，默认无限制，Redis可以同时打开的客户端连接数为Redis进程可以打开的最大文件描述符数，如果设置 maxclients 0，表示不作限制。当客户端连接数到达限制时，Redis会关闭新的连接并向客户端返回max number of clients reached错误信息

    `maxclients 128`

17. 指定Redis最大内存限制，Redis在启动时会把数据加载到内存中，达到最大内存后，Redis会先尝试清除已到期或即将到期的Key，当此方法处理 后，仍然到达最大内存设置，将无法再进行写入操作，但仍然可以进行读取操作。Redis新的vm机制，会把Key存放内存，Value会存放在swap区

    `maxmemory <bytes>`

18. 指定是否在每次更新操作后进行日志记录，Redis在默认情况下是异步的把数据写入磁盘，如果不开启，可能会在断电时导致一段时间内的数据丢失。因为 redis本身同步数据文件是按上面save条件来同步的，所以有的数据会在一段时间内只存在于内存中。默认为no

    `appendonly no`

19. 指定更新日志文件名，默认为appendonly.aof

     `appendfilename appendonly.aof`

20. 指定更新日志条件，共有3个可选值：
    no：表示等操作系统进行数据缓存同步到磁盘（快）
    always：表示每次更新操作后手动调用fsync()将数据写到磁盘（慢，安全）
    everysec：表示每秒同步一次（折衷，默认值）

    `appendfsync everysec`

 

21. 指定是否启用虚拟内存机制，默认值为no，简单的介绍一下，VM机制将数据分页存放，由Redis将访问量较少的页即冷数据swap到磁盘上，访问多的页面由磁盘自动换出到内存中（在后面的文章我会仔细分析Redis的VM机制）

     `vm-enabled no`

22. 虚拟内存文件路径，默认值为/tmp/redis.swap，不可多个Redis实例共享

    ` vm-swap-file /tmp/redis.swap`

23. 将所有大于vm-max-memory的数据存入虚拟内存,无论vm-max-memory设置多小,所有索引数据都是内存存储的(Redis的索引数据 就是keys),也就是说,当vm-max-memory设置为0的时候,其实是所有value都存在于磁盘。默认值为0

     `vm-max-memory 0`

24. Redis swap文件分成了很多的page，一个对象可以保存在多个page上面，但一个page上不能被多个对象共享，vm-page-size是要根据存储的 数据大小来设定的，作者建议如果存储很多小对象，page大小最好设置为32或者64bytes；如果存储很大大对象，则可以使用更大的page，如果不 确定，就使用默认值

     `vm-page-size 32`

25. 设置swap文件中的page数量，由于页表（一种表示页面空闲或使用的bitmap）是在放在内存中的，，在磁盘上每8个pages将消耗1byte的内存。

     `vm-pages 134217728`

26. 设置访问swap文件的线程数,最好不要超过机器的核数,如果设置为0,那么所有对swap文件的操作都是串行的，可能会造成比较长时间的延迟。默认值为4

     `vm-max-threads 4`

27. 设置在向客户端应答时，是否把较小的包合并为一个包发送，默认为开启

    `glueoutputbuf yes`

28. 指定在超过一定的数量或者最大的元素超过某一临界值时，采用一种特殊的哈希算法

    `hash-max-zipmap-entries 6`4

    `hash-max-zipmap-value 51`2

29. 指定是否激活重置哈希，默认为开启（后面在介绍Redis的哈希算法时具体介绍）

    `activerehashing yes`

30. 指定包含其它的配置文件，可以在同一主机上多个Redis实例之间使用同一份配置文件，而同时各个实例又拥有自己的特定配置文件

    `include /path/to/local.conf`