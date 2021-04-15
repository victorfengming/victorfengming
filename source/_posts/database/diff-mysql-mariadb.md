---
title: "MariaDB mysql 比较区别选择"  
cover: "/img/lynk/86.jpg"
date:       2019-10-03
tags:
	- Linux
	- database
	- mysql
---

 MariaDB
 数据库管理系统是
 MySQL
 的一个分支

 
 

 开发这个分支的原因之一是：
 甲骨文公司
 收购了MySQL后，有将MySQL
 闭源
 的潜在风险，因此社区采用分支的方式来避开这个风险。

 
 

 MariaDB的目的是完全兼容MySQL，包括
 API
 和命令行，使之能轻松成为MySQL的代替品。在存储引擎方面，10.0.9版起使用
 XtraDB
 （名称代号为
 Aria
 ）来代替MySQL的
 InnoDB
 。

 
 

 MariaDB直到5.5版本，均依照MySQL的版本。因此，使用MariaDB5.5的人会从MySQL 5.5中了解到MariaDB的所有功能。

 从2012年11月12日起发布的10.0.0版开始，不再依照MySQL的版号。10.0.x版以5.5版为基础，加上移植自MySQL 5.6版的功能和自行开发的新功能。

 
 

 MySQL分支的选择：Percona还是MariaDB

 
 

 PostgreSQL一直被当作MySQL的直接竞争对手

 
 

 
 

 MyISAM没有提供事务支持，而InnoDB提供了事务支持。

 XtraDB 是 InnoDB 存储引擎的增强版

 
 

 谷歌和维基都选择了mariaDB

 
 

 MariaDB是MySQL创始人搞的

 
 

 
 

 PostgreSQL 与 MySQL 相比，优势何在？

 不少人应该遇到过 MySQL 里需要 utf8mb4 才能显示 emoji 的坑, Pg 就没这个坑

 https://www.zhihu.com/question/20010554

 
 

 https://db-engines.com/en/system/MariaDB%3BPostgreSQL

 http://www.infoq.com/cn/news/2013/12/mysql-vs-postgresql


原文链接：https://blog.csdn.net/elesos/article/details/73804680

