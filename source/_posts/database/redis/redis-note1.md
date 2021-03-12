---
title: "redis笔记01"
cover: "/img/lynk/80.jpg"
date:       2019-12-18
subtitle: "redis简介"
tags:
	- Linux
	- deepin
	- database
	- redis
	- nosql
---
  
  
  








## 起步
### redis简介
redis是完全开源免费的,遵守[BSD协议](https://baike.baidu.com/item/BSD%E5%8D%8F%E8%AE%AE),是一个高性能的key-value数据库.

#### redis与其他key-value缓存产品有一下三个特点:
- redis支持数据的持久化,可以将内存中的数据保持在磁盘中,重启的时候可以再次加载进行使用
- redis不仅仅支持简单的key-value类型的数据,同时还提供list,set,zset,hash等数据结构的存储.
- redis支持数据的备份,及master-slave模式的数据备份
### redis优势
- 性能极高-Redis能读的速度是110000次/s,写的速度是81000次/s.
- 丰富的数据类型-Redis支持二进制案例的Strings,List,Hashes,Sets及Ordered Sets数据类型操作
- 原子-redis的所有操作都是原子性的,同时redis还支持对几个操作全并后的[原子性](https://blog.csdn.net/qq_30243515/article/details/82557535)执行(原子性即为一个操作的完整性,要不就全不操作,要不就操作成功)
- 丰富的特性- Redis还支持[publish / subscribe](https://jingyan.baidu.com/article/54b6b9c0a6dbdd2d583b4716.html) ,[通知](https://www.cnblogs.com/tangxuliang/p/10659439.html) ,[key过期](https://www.cnblogs.com/duhuo/p/6323499.html)的等等特性.

### Redis与其他key-value存储有什么不同?
- Redis有着更为复杂的数据类型,不用于其他key-value类型的数据库方案,他这个类型更加的透明对于程序员来说,无需进行额外的抽象
- Redis虽然说的运行在内存中,但是也是可以进行持久化存储到硬盘中的,这要根据这个数据量进行权衡.这样相比在硬盘中的复杂的数据类型,内存操作显得更加的直接,简单,这样redis可以做更加复杂的一些操作.同时,在磁盘的格式方面,他们是以一个紧凑的追加方式产生的,因为他们不需要进行随机的访问.














