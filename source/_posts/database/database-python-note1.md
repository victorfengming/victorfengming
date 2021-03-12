---
title: "python操作数据库笔记1"
cover: "/img/lynk/62.jpg"
date:       2019-12-18
tags:
	- database
	- mysql
	- base
	- redis
	- mongodb
---


## 起步
### 分关系型数据库
#### 分类 
- 文档型
- key-value型
- 列式数据库
- 图形数据库

```json
{
  "name": "张三",
  "age": 20,
  "sex": "男",
},
{
  "name": "李四",
  "age": 18,
  "sex": "nv",
},
```
#### 文档类型
|举例| CouchDB,MongoDB|
|---|---|
|典型应用场景|Web应用(与key-vlaue类似,value是结构化的,不同的是数据库能够了解value的内容|
|数据模型|key-value对应的键值对,value为结构化数据|
|强项|查找速度快,可扩展性强,更容易进行分布式扩展|
|弱项|功能相对局限|
#### key-value型
|举例| Redis,Voldemort,Oracle DBD|
|---|---|
|典型应用场景|内容缓存,主要用于处理大量数据的高访问负载,也用于一些日志系统等|
|数据模型|key指向value的键值对,通常用hash table来实现|
|强项|查找速度快|
|弱项|数据无结构化,通常只被当做字符串或者二进制数据|

#### 列式数据库
|举例| Cassandra,HBase,Riak|
|---|---|
|典型应用场景|分布式的文件系统|
|数据模型|以列簇式存储,将同一列数据存在一起|
|强项|查找速度快,可扩展性强,更容易进行分布式扩展|
|弱项|功能相对局限|

#### 图形数据库
|举例|Neo4J,InfoGrid,Infinite Graph|
|---|---|
|典型应用场景|社交网络,推荐系统等,专注于构建关系图谱图结构|
|数据模型|图结构|
|强项|利用图结构相关算法,比如最短路径寻址,N度关系查找等|
|弱项|很多时候需要对整个图做计算才能得出需要的信息,而且这种结构不太好做分布式的集群方案|


#### MYSQL 事务处理主要有两种方法：
1、用 BEGIN, ROLLBACK, COMMIT来实现

BEGIN 开始一个事务  
ROLLBACK 事务回滚  
COMMIT 事务确认  
2、直接用 SET 来改变 MySQL 的自动提交模式:  

SET AUTOCOMMIT=0 禁止自动提交  
SET AUTOCOMMIT=1 开启自动提交  
