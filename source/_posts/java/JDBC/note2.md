---
title: 'JDBC笔记02'
cover: "/img/lynk/63.jpg"
date:       2019-11-09
subtitle: '数据库连接池 Spring JDBC'  
tags:
	- Java
	- basis
	- JDBC
---
  
  
* content  
{:toc}  
  
  
  
  



# 今日内容
1. 数据库连接池
2. Spring JDBC : JDBC Template

## 数据库连接池
### 概念:
其实就是一个容器(集合),存放数据库连接的容器

当系统初始化好后,容器被创建,容器中会申请一些连接对象,当用户来访问数据库时,从容器中获取连接对象,用户访问完之后,会将连接对象归还给容器

### 好处:
- 节约资源
- 用户访问高效

### 实现
1. 标准接口:DataSource javax.sql包下的
    - 方法:
        - 获取连接:getConnection()
        - 归还连接:Connection.close(). 如果连接对象Connection是从连接池中获取的,那么调用方法,则不会再关闭连接了.而是归还连接
2. 一般我们不去实现它,有数据库厂商来实现
    1. C3P0: 数据库连接池技术
    2. Druid: 数据库连接池实现技术,由阿里巴巴提供的(这玩意十分的高效,性能好,全球最好的数据库连接池技术!nb吧)        

### C3P0:数据库连接池技术
#### 步骤:
1. 导入jar包(两个) 
c3p0-0.9.5.2.jar 
mchange-commons-java-0.1.12.jar
不要忘记导入数据库的驱动jar包
2. 定义配置文件:
    - 名称:-c3p0.properties 或者 c3p0-config.xml
    - 路径:直接将文件放在src目录下即可.
3. 创建核心对象 数据库连接池对象 ComboPooledDataSource
4. 获取连接:getConnection
### Druid :数据库连接池实现技术,有阿里巴巴提供的
#### 步骤:
1. 导入jar包 fruid-1.9.9.jar
2. 定义配置文件:
    - 是properties形式的
    - 可以叫任意名称,可以放在任意目录下
3. 加载配置文件.properties
4. 获取数据库连接池对象:通过工厂来获取DruidDataSourceFactory
5. 获取连接:getConnection    


## Spring JDBC
### Spring 框架对JDBC的简单封装
提供了一个JDBCTemplate对象简化JDBC的开发
步骤:
    1. 导入jar包
    2. 创建JdbcTemplate对象,依赖于数据源DataSource
        - JdbcTemplate template = new JdbcTemplate(ds);
    3. 调用JdbcTemplate的方法来完成CRUD的操作
        - update():执行DML语句.增删改语句
        - queryForMap(): 查询结果将结果集封装为map集合
            - 将列明作为key,将值作为value 将这条记录封装为一个map集合
            - 注意:这个方法查询的结果集长度只能是1
        - queryForList(): 查询结果将结果集封装为list集合
            - 注意:将每一条记录封装为一个Map集合,再讲Map集合装载到List集合中
        - query(): 查询结果,将结果封装为JavaBean对象
            - query的参数:RowMapper,一般我们使用BeanPropertyRowMapper实现类.
            - 以完成数据到JavaBean的自动封装
            - `new BeanPropertyRowMapper<类型>(类型.class)`
        - queryForObject:查询结果,将结果封装为对象
            - 一般用于聚合函数的查询
    4. 练习:
        - 需求:
            1. 修改1号数据的 salary 为 10000
            2. 添加一条记录
            3. 删除刚才添加的记录
            4. 查询id为1的记号,将其封装为Map集合
            5. 查询所有记录,将其封装为List
            6. 查询所有记录,将其封装为Emp对象的List集合
            7. 查询总记录数
            
        
        