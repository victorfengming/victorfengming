---
title: "redis笔记02"
date:       2020-02-07
subtitle: "redis数据类型操作"
tags:
	- Linux
	- database
	- redis
	- nosql
---
  
  
  



* content
{:toc}



## String类型数据的扩展操作
解决方案
- 设置数据具有指定的生命周期
```redis
setex key seconds value
psetex key milliseconds value
```

redis控制数据的生命周期,通过数据是否失效控制业务行为,适用于所有具有时效性限定控制的操作

## String类型数据操作的注意事项
- 数据操作不成功的反馈与数据正常操作之间的差异
    - 表示运行结果是否成功
        - (integer)0 -> false 失败
        - (integer)1 -> true 成功
    - 表示运行结果值
        - (integer)3 -> 3   3个
        - (integer)1 -> 1   1个
- 数据未获取到
    (nil) 等同于 null
- 数据最大存储量
    - 512MB 没有必要来探讨上限问题
- 数值计算最大范围(Java中的long的最大值)
    - 9223372036854775807
    
# 目录
- 数据类型介绍
- string
- hash
- list
- set
- sorted_set
- 数据类型实践案例

## hash类型
存储的困惑
对象类数据的存储如果具有较频繁的更新需求操作会显得比较笨重

- 新的存储需求:对一系列的数据进行编组,方便管理,典型应用存储对象信息
- 需要的存储结构:一个存储空间保存多个键值对数据
- hash类型:底层使用哈希表结构实现数据存储
### hash存储结构优化
- 如果field数量较少,存储结构优化为类数组结构
- 如果field数量较多,存储结构使用hashMap结构



















