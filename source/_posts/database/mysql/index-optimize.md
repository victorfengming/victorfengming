---
title: "MySQL的索引与优化"
cover: "/img/lynk/37.jpg"
date:       2021-04-15
author:       "victor"
tags:
	- database
	- mysql
---

## 写在前面:
### TO KNOW
- MySQL索引定义
- MySQL索引结构
- MySQL索引优势



写在前面:索引对查询的速度有着至关重要的影响,理解索引也是进行数据库性能调优的起点.考虑如下情况,假设数据库中一个表有10^6条记录,DBMS的页面大小为4K,并存储100条记录.如果没有索引,查询将对整个表进行扫描,最坏的情况下,如果所有数据页,需要读取10^4个页面,如果这10^4个页面在磁盘上下随机分布,需要需要进行10^4次I/O,假设磁盘每次I/O时间为10ms(忽略数据传输时间),则总共需要100s(但实际上要好很多很多).如果对之建立B-Tree索引,则只需要进行log100(10^6)=3次页面读取,最坏情况下耗时30ms.这就是索引带来的效果,很多时候,当你的应用程序进行SQL查询速度很慢时,应该想想是否可以建索引.进入正题:

## 索引与优化

### 1. 选择索引的数据类型

MySQL支持很多数据类型,选择合适的数据类型存储数据对性能有很大影响.

通常来说,可以遵循以下一些指导原则:

- **越小的数据类型通常更好**:越小的数据类型通常在磁盘,内存和CPU缓存中都需要更少的空间,处理起来更快.
- **简单的数据类型更好**:整形数据比起字符,处理开销更小,因为字符串的比较更复杂. 在MySQL中,应该用内置的日期和时间数据类型,而不是用字符串来存储时间;以及用整型数据类型存储IP地址.
- **尽量避免NULL:**应该指定列为NOT NULL,除非你想存储NULL.在MySQL中,含有空值的列很难进行查询优化,因为他们使得索引,索引的统计信息以及比较运算更加复杂.你应该用0,一个特除的值或者一个空串代替空值.

#### 选择标识符

选择合适的标识符是非常重要的.选择时不仅应该考虑存储类型,而且应该考虑MySQL是怎样进行运算和比较的.一旦选定数据类型,应该保证所有相关的表都使用相同的数据类型.

- 整型: 通常是作为标识符的最好选择,因为可以更快的处理,而且可以设置为AUTO_INCREMENT.
- 字符串: 尽量避免使用字符串作为标识符,它们消耗更好的空间,处理起来也较慢.而且,通常来说,字符串都是随机的,所以他们在索引中的位置也是随机的,这会导致页面分裂,随机访问磁盘,聚簇索引分裂(对于使用聚簇索引的存储引擎).


### 2. 索引的入口

对于任何[DBMS](https://blog.csdn.net/gengkui9897/article/details/89294936),索引都是进行优化的最主要的因素.对于少量的数据,没有合适的索引影响不是很大,但是,当随着数据量的增加,性能会急剧下降.

如果对多列进行索引(组合索引),列的顺序非常重要,MySQL仅能对索引最左边的前缀进行有效的查找.例如:

假设存在组合索引it1c1c2(c1,c2)，查询语句select * from t1 where c1=1 and c2=2能够使用该索引。查询语句select * from t1 where c1=1也能够使用该索引。但是，查询语句select * from t1 where c2=2不能够使用该索引，因为没有组合索引的引导列，即，要想使用c2列进行查找，必需出现c1等于某值。

#### 索引的类型
索引是在存储引擎中实现的,而不是在服务器层中实现的.所以,每种存储引擎的索引类型都不一定完全相同,并不是所有的存储引擎都支持所有的索引类型.

##### B-Tree 索引

[B-Tree(balance Tree)](https://victorfengming.gitee.io/data_algorithm/135_%E6%A0%91_%E5%B9%B3%E8%A1%A1%E4%BA%8C%E5%8F%89%E6%A0%91_AVL%E6%A0%91_%E4%BB%8B%E7%BB%8D.html)


 
 





