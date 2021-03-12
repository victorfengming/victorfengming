---
title: "redis笔记03"
date:       2019-12-18
subtitle: "redis数据类型"
tags:
	- Linux
	- deepin
	- database
	- redis
	- nosql
---
  
  
  



* content
{:toc}




## Redis数据类型
### Redis 数据类型
redis支持种数据类型 : 
- string(字符串)
- hash(哈希)
- list(列表)
- set(集合)
- zset(sorted set:有序集合)


### String（字符串）
string是redis最基本的类型，你可以理解成与[Memcached](https://www.runoob.com/memcached/memcached-tutorial.html)一模一样的类型，一个key对应一个value。

string类型是二进制安全的。意思是redis的string可以包含任何数据。比如jpg图片或者序列化的对象 。

string类型是Redis最基本的数据类型，一个键最大能存储512MB。

### 实例

```
redis 127.0.0.1:6379> set name "victor"
OK
redis 127.0.0.1:6379> get name
"victor"
```

在以上实例中我们使用了 Redis 的 SET 和 GET 命令。键为 name，对应的值为"victor"

注意：一个键最大能存储512MB。


### Hash（哈希）
Redis hash 是一个键值对集合。

Redis hash是一个string类型的field和value的映射表，hash特别适合用于存储对象。

### 实例

```
redis 127.0.0.1:6379> hmset user:1 username victor password 123456 points 200
OK
redis 127.0.0.1:6379> hgetall user:1
1) "username"
2) "victor"
3) "password"
4) "123456"
5) "points"
6) "200"
```
以上实例中 hash 数据类型存储了包含用户脚本信息的用户对象。实例中我们使用了 Redis HMSET, HGETALL 命令，user:1 为键值。

每个 hash 可以存储 2^32 - 1 键值对（40多亿）。
### List（列表）
Redis 列表是简单的字符串列表，按照插入顺序排序。你可以添加一个元素到列表的头部（左边）或者尾部（右边）。
### 实例

```
redis 127.0.0.1:6379> lpush mylist python
(integer) 1
redis 127.0.0.1:6379> lpush mylist java
(integer) 2
redis 127.0.0.1:6379> lpush mylist php
(integer) 3
redis 127.0.0.1:6379> lpush mylist node
(integer) 4
redis 127.0.0.1:6379> lrange mylist 0 11
1) "node"
2) "php"
3) "java"
4) "python"
redis 127.0.0.1:6379>
```
列表最多可存储 232 - 1 元素 (4294967295, 每个列表可存储40多亿)。
### Set（集合）
Redis的Set是string类型的无序集合。

集合是通过哈希表实现的，所以添加，删除，查找的复杂度都是O(1)。
### sadd 命令
添加一个string元素到,key对应的set集合中，成功返回1,如果元素以及在集合中返回0,key对应的set不存在返回错误。

```
sadd key member
```

### 实例

```
redis 127.0.0.1:6379> sadd list1 ttk
(integer) 1
redis 127.0.0.1:6379> sadd list1 victor
(integer) 1
redis 127.0.0.1:6379> sadd list1 nineberg
(integer) 1
redis 127.0.0.1:6379> sadd list1 mengya
(integer) 1
redis 127.0.0.1:6379> sadd list1 yupeng
(integer) 1
redis 127.0.0.1:6379> sadd list1 chenzan
(integer) 1
redis 127.0.0.1:6379> smembers list1
1) "mengya"
2) "nineberg"
3) "ttk"
4) "chenzan"
5) "victor"
6) "yupeng"
redis 127.0.0.1:6379> sadd list1 yupeng
(integer) 0
redis 127.0.0.1:6379> smembers list1 yupeng
(error) ERR wrong number of arguments for 'smembers' command
redis 127.0.0.1:6379> smembers list1
1) "nineberg"
2) "ttk"
3) "chenzan"
4) "victor"
5) "yupeng"
6) "mengya"
redis 127.0.0.1:6379>
```

注意：以上实例中 rabitmq 添加了两次，但根据集合内元素的唯一性，第二次插入的元素将被忽略。

集合中最大的成员数为 232 - 1 (4294967295, 每个集合可存储40多亿个成员)。

### zset(sorted set：有序集合)
Redis zset 和 set 一样也是string类型元素的集合,且不允许重复的成员。
不同的是每个元素都会关联一个double类型的分数。redis正是通过分数来为集合中的成员进行从小到大的排序。

zset的成员是唯一的,但分数(score)却可以重复。
### zadd 命令
添加元素到集合，元素在集合中存在则更新对应score

```
zadd key score member 
```
### 实力

```
redis 127.0.0.1:6379> zadd list2 0 node
(integer) 1
redis 127.0.0.1:6379> zadd list2 0 html
(integer) 1
redis 127.0.0.1:6379> zadd list2 0 css
(integer) 1
redis 127.0.0.1:6379> zadd list2 0 js
(integer) 1
redis 127.0.0.1:6379> zadd list2 0 js
(integer) 0
redis 127.0.0.1:6379> zrengebyscore list2 0 1000
(error) ERR unknown command 'zrengebyscore'
redis 127.0.0.1:6379> zrangebyscore list2 0 1000
1) "css"
2) "html"
3) "js"
4) "node"
redis 127.0.0.1:6379>
```