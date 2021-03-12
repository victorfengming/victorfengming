---
title: "Oracle基础知识总结"
date:       2019-09-28
tags:
	- Linux
	- deepin
	- database
	- oracle
	- summer
---
  
 







原文链接: https://blog.csdn.net/qq_39876666/article/details/82764040

 
## ORACLE 基础
### ORACLE 数据库具有以下特点：
- 支持多用户、大事务量的事务处理
- 数据安全性和完整性控制
- 支持分布式数据处理
- 可移植性

### ORACLE 体系结构
- 数据库
- 实例
- 数据文件(dbf)
- 表空间
    - 用户
    
![实力示意图](https://img-blog.csdn.net/2018091818142275?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM5ODc2NjY2/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

### 创建表空间

```
create tablespace waterboss
datafile 'c:\waterboss.dbf'
size 100m
autoextend on
next 10m

waterboss 为表空间名称
datafile 用于设置物理文件名称
size 用于设置表空间的初始大小
autoextend on 用于设置自动增长，如果存储量超过初始大小，则开始自动扩容
next 用于设置扩容的空间大小
```


### 创建用户

```
create user wateruser
identified by itcast
default tablespace waterboss

wateruser 为创建的用户名
identified by 用于设置用户的密码
default tablesapce 用于指定默认表空间名称
```

### 用户赋权

```
grant dba to wateruser
```

### 表的创建、修改与删除
#### 创建表

```
CREATE TABLE 表名称(
字段名 类型(长度) primary key,
字段名 类型(长度),
.......
);
```

    
#### 数据类型：

- 字符型
    0. CHAR : 固定长度的字符类型，最多存储 2000 个字节
    0. VARCHAR2 :可变长度的字符类型，最多存储 4000 个字节
    0. LONG : 大文本类型。最大可以存储 2 个 G

- 数值型
    0. NUMBER : 数值类型
    0. 例如：NUMBER(5) 最大可以存的数为 99999
    0. NUMBER(5,2) 最大可以存的数为 999.99
    
- 日期型
    0. DATE：日期时间型，精确到秒
    0. TIMESTAMP：精确到秒的小数点后 9 位
    
- 二进制型（大数据类型）
    0. CLOB : 存储字符,最大可以存 4 个 G
    0. BLOB：存储图像、声音、视频等二进制数据,最多可以存 4 个 G
    
    
#### 修改表



- 增加字段


```
ALTER TABLE 表名称 ADD(列名 1 类型 [DEFAULT 默认值]，列名 1 类型 [DEFAULT 默认值]…)
```


- 修改字段


```
ALTER TABLE 表名称 MODIFY(列名 1 类型 [DEFAULT 默认值]，列名 1 类型 [DEFAULT 默认值]…)
```



- 修改字段名


```
ALTER TABLE 表名称 RENAME COLUMN 原列名 TO 新列名
```



- 删除字段名

```
ALTER TABLE T_OWNERS DROP COLUMN REMARK
```


#### 删除表

```
drop table 表名称
```


### 数据增删改
- INSERT INTO 表名[(列名 1，列名 2，…)]VALUES(值 1，值2，…)
- UPDATE 表名 SET 列名 1=值 1，列名 2=值 2，…WHERE 修改条件；
- DELETE FROM 表名 WHERE 删除条件;
- TRUNCATE TABLE 表名称 ---- 删除表

#### 比较 truncat 与 delete 实现数据删除？
0. delete 删除的数据可以 rollback
0. delete 删除可能产生碎片，并且不释放空间
0. truncate 是先摧毁表结构，再重构表结构


#### JDBC 连接 ORACLE



```java
//加载驱动
static{
	try {
		Class.forName("oracle.jdbc.driver.OracleDriver");	Class.forName("oracle.jdbc.driver.OracleDriver");
	} catch (ClassNotFoundException e) {
		e.printStackTrace();	e.printStackTrace();
	}
}


// 获取数据库连接
public static java.sql.Connection getConnection() throwsSQLException{
    return java.sql.DriverManager.getConnection("jdbc:oracle:thin:@192.168.80.10:1521:orcl","wateruser", "itcast");
}
```



##### JDBC 驱动为：


```
oracle.jdbc.OracleDriver
```

##### 连接字符串( 瘦连接 )：


```
jdbc:oracle:thin:@虚拟机的 IP:1521:orcl
```


### 数据导出与导入

#### 整库导出与导入

- 整库导出命令

    `exp system/itcast full=y 或者 exp system/itcast file=文件名 full=y`

- 整库导入命令

    `imp system/itcast full=y or imp system/itcast full=y file=water.dm`
    
#### 按用户导出与导入
- 按用户导出

    `exp system/itcast owner=wateruser file=wateruser.dmp`

- 按用户导入

    `imp system/itcast file=wateruser.dmp fromuser=wateruser`
    
#### 按表导出与导入
- 按表导出 

    `exp wateruser/itcast file=a.dmp tables=t_account,a_area`
- 按表导入 
    
    `imp wateruser/itcast file=a.dmp tables=t_account,a_are`
    
    
### ORACLE 查询
#### 单表查询
##### 简单条件查询
- 精确查询 select * from T_OWNERS where watermeter=‘30408’
- 模糊查询 select * from t_owners where name like ‘%刘%’
- and 运算符 select * from t_owners where name like ‘%刘%’ and housenumber like ‘%5%’
- or 运算符 select * from t_owners where name like ‘%刘%’ or housenumber like ‘%5%’
- and 与 or 运算符混合使用
 
    select * from t_owners where (name like ‘%刘%’ or housenumber like ‘%5%’) and addressid=3
- 范围查询 select * from T_ACCOUNT where usenum>=10000 and usenum<=20000
- 空值查询 select * from T_PRICETABLE t where maxnum is null


##### 去掉重复记录

`select distinct addressid from T_OWNERS`

##### 排序查询

- 升序排序 `select * from T_ACCOUNT order by usenum`
- 降序排序 `select * from T_ACCOUNT order by usenum desc`


##### 基于伪列的查询
- ROWID 具体某一行数据的物理地址 select rowID,t.* from T_AREA t
- ROWNUM 每一行的行号,查询后才会标注 select rownum,t.* from T_OWNERTYPE t


##### 聚合统计
- 聚合函数
```
sum* select sum(usenum) from t_account where year=‘2012’

avg* select avg(usenum) from T_ACCOUNT where year=‘2012’

max* select max(usenum) from T_ACCOUNT where year=‘2012’

select* min(usenum) from T_ACCOUNT where year=‘2012’

count* select count(*) from T_OWNERS t where ownertypeid=1
```
- 分组聚合 `Group by* select areaid,sum(money) from t_account group by areaid`
- 分组后条件查询 `having* select areaid,sum(money) from t_account group by areaid having sum(money)>169000`


