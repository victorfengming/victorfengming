---
title: 'c3p0-config.xml文件简单说明与备忘'
cover: "/img/lynk/8.jpg"
date:       2019-11-09
tags:
	- Java
	- basis
	- JDBC
---
  
  

  



```xml
<?xml version="1.0" encoding="UTF-8"?>
<c3p0-config>
    <named-config name="mysql">
        <!-- 配置数据库用户名 -->
        <property name="user">root</property>
        <!-- 配置数据库密码 -->
        <property name="password"></property>
        <!-- 配置数据库链接地址 -->
        <property name="jdbcUrl">jdbc:mysql://localhost:3306/cdcol?useUnicode=true&amp;characterEncoding=UTF-8</property>
        <!-- 配置数据库驱动 -->
        <property name="driverClass">com.mysql.jdbc.Driver</property>
        <!-- 数据库连接池一次性向数据库要多少个连接对象 -->
        <property name="acquireIncrement">20</property>
        <!-- 初始化连接数 -->
        <property name="initialPoolSize">10</property>
        <!-- 最小连接数 -->
        <property name="minPoolSize">5</property>
        <!--连接池中保留的最大连接数。Default: 15 -->
        <property name="maxPoolSize">30</property>
        <!--JDBC的标准参数，用以控制数据源内加载的PreparedStatements数量。但由于预缓存的statements 属于单个connection而不是整个连接池。所以设置这个参数需要考虑到多方面的因素。如果maxStatements与maxStatementsPerConnection均为0，则缓存被关闭。Default:0 -->
        <property name="maxStatements">0</property>
        <!--maxStatementsPerConnection定义了连接池内单个连接所拥有的最大缓存statements数。Default: 0 -->
        <property name="maxStatementsPerConnection">0</property>
        <!--c3p0是异步操作的，缓慢的JDBC操作通过帮助进程完成。扩展这些操作可以有效的提升性能 通过多线程实现多个操作同时被执行。Default:3 -->
        <property name="numHelperThreads">3</property>
        <!--用户修改系统配置参数执行前最多等待300秒。Default: 300 -->
        <property name="propertyCycle">3</property>
        <!-- 获取连接超时设置 默认是一直等待单位毫秒 -->
        <property name="checkoutTimeout">1000</property>
        <!--每多少秒检查所有连接池中的空闲连接。Default: 0 -->
        <property name="idleConnectionTestPeriod">3</property>
        <!--最大空闲时间,多少秒内未使用则连接被丢弃。若为0则永不丢弃。Default: 0 -->
        <property name="maxIdleTime">10</property>
        <!--配置连接的生存时间，超过这个时间的连接将由连接池自动断开丢弃掉。当然正在使用的连接不会马上断开，而是等待它close再断开。配置为0的时候则不会对连接的生存时间进行限制。 -->
        <property name="maxIdleTimeExcessConnections">5</property>
        <!--两次连接中间隔时间，单位毫秒。Default: 1000 -->
        <property name="acquireRetryDelay">1000</property>
        <!--c3p0将建一张名为Test的空表，并使用其自带的查询语句进行测试。如果定义了这个参数那么属性preferredTestQuery将被忽略。你不能在这张Test表上进行任何操作，它将只供c3p0测试使用。Default: null -->
        <property name="automaticTestTable">Test</property>
        <!-- 获取connnection时测试是否有效 -->
        <property name="testConnectionOnCheckin">true</property>
    </named-config>
</c3p0-config>
```

注释:以上为c3p0-config.xml文件。一般放在项目scr资源文件下。lib导包需要两个c3p0-0.x.x.jar和依赖包mchange-commons-java-0.X.x.jar