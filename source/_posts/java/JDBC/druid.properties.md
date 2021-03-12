---
title: 'druid.properties文件的配置'
date:       2019-11-10
tags:
	- Java
	- basis
	- JDBC
---
  
  

```properties
# druid.properties文件的配置
driverClassName=com.mysql.jdbc.Driver
url=jdbc:mysql://127.0.0.1:3306/plan
username=root
password=
# 初始化连接数量
initialSize=5
# 最大连接数
maxActive=10
# 最大超时时间
maxWait=3000
```