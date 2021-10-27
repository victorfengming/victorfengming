---
title: "MySQL极客时间45讲"
cover: "/img/lynk/7.jpg"
date:       2021-04-15
author:       "victor"
tags:
	- database
	- mysql
---






# 01.基础架构：一条SQL查询语句是如何执行的?



# 02.日志系统：一条SQL更新语句是如何执行的?



# 03.事务隔离：为什么你改了我还看不见?



# 04.深入浅出索引_上_



# 05.深入浅出索引_下_



# 06.全局锁和表锁 ：给表加个字段怎么有这么多阻碍?



# 07.行锁功过：怎么减少行锁对性能的影响?



# 08.事务到底是隔离的还是不隔离的?



# 09.普通索引和唯一索引_应该怎么选择?

普通索引: 

唯一索引: 



普通索引在进行新增的时候不需要进行 重复的判断,而唯一索引需要

在查询的时候,唯一索引只需要查询到对应的值(从B+Tree的根节点一路下来)

如果是普通索引,在一个inooDB的一个页中,恰巧这条记录是本页的最后一条,则又需要进行一次IO来判断下一个inooDB页的第一个值等不等与要查询的值,但是对于inooDB来说,这种一页1000个索引的数据量,这个可能性会被CPU的速度认为忽略不计





# 10.MySQL为什么有时候会选错索引?



# 11.怎么给字符串字段加索引?



# 12.为什么我的MySQL会_抖_一下?



# 13.为什么表数据删掉一半_表文件大小不变?



# 14.count(×)这么慢_我该怎么办?



# 15.答疑文章_一_：日志和索引相关问题



# 16._order by_是怎么工作的?



# 17.如何正确地显示随机消息?



# 18.为什么这些SQL语句逻辑相同性能却差异巨大?



# 18.为什么这些SQL语句逻辑相同_性能却差异巨大?



# 19.为什么我只查一行的语句也执行这么慢?



# 19.为什么我只查一行的语句_也执行这么慢?



# 20.幻读是什么幻读有什么问题?



# 21.为什么我只改一行的语句锁这么多?



# 22.MySQL有哪些_饮鸩止渴_提高性能的方法?



# 23.MySQL是怎么保证数据不丢的?



# 24.MySQL是怎么保证主备一致的?



# 25.MySQL是怎么保证高可用的?



# 26.备库为什么会延迟好几个小时?



# 27.主库出问题了从库怎么办?



# 28.读写分离有哪些坑?



# 29.如何判断一个数据库是不是出问题了?



# 30.答疑文章_二_：用动态的观点看加锁



# 31.误删数据后除了跑路还能怎么办?



# 32.为什么还有kill不掉的语句?



# 33.我查这么多数据会不会把数据库内存打爆?



# 34.到底可不可以使用join?



# 35.join语句怎么优化?



# 36.为什么临时表可以重名?



# 37.什么时候会使用内部临时表?



# 38.都说InnoDB好那还要不要使用Memory引擎?



# 39.自增主键为什么不是连续的?



# 40.insert语句的锁为什么这么多?



# 41.怎么最快地复制一张表?



# 42.grant之后要跟着flush privileges吗?



# 43.要不要使用分区表?



# 44.答疑文章_三_：说一说这些好问题



# 45.自增id用完怎么办?



# 



查询的参数 只需要传 plan_number (表示第几种方案的航班计划)

**返回的数据如下**

```json


{
  "data": {
    "1": {
      "66e804df98eb4fc58c8f55970fea3aa5": {
        "plan": {
          "plan_id": "66e804df98eb4fc58c8f55970fea3aa5",
          "plan_number": "1",
          "plan_name": "第一计划",
          "effect_status": "0",
          "begin_time": "2021-10-21T11:23:37Z",
          "end_time": "2021-11-22T11:23:37Z",
          "update_time": "2021-10-22T16:09:31.346704Z"
        },
        "task": {
          "3": [
            {
              "task_id": "3505e9b90d75445cb5e5d4a820718c23",
              "plan_id": "66e804df98eb4fc58c8f55970fea3aa5",
              "week_number": "3",
              "executedate": "2021-09-14",
              "airway": "",
              "flightno": "KN5519",
```


- 第一级的数字(key)"1"表示 10个计划中的第一个
- 第二级的数字(key)"66e804df98eb4fc58c8f55970fea3aa5"
- "66e804df98eb4fc58c8f55970fea3aa5"下的plan里是计划信息
- task下的(key) "3" 表示 每周的星期数(星期一:1,星期二:2,,星期三:3...)
-  "3"下面是航班模板的数组,里面的结构和航班信息是一样的(多了task_id,plan_id,week_number)