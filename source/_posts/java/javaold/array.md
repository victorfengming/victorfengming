---
title: 'java,python,php 中的数组简识'
date:       2019-10-13
tags:
	- Java
	- basis
	- Python
	- php
---


### python 列表，元素，字典
数组三种模式:列表(list),元组(tuple),字典(dict)，均支持遍历，也支持迭代

```python
demo1 = ['a','b','c','d']           # 列表
demo2 = ('a','b','c','d')           # 元组
demo3 = {"name":"kurt","age":18,"sex",1} # 字典

# for循环遍历列表/元组里面的数据
for item in demo1:
    print item

# for循环遍历列表/元组里面的索引
for key in xrange(0, len(demo1)):
    print key, demo1[key]

# for循环遍历字典的数据

# key
for key in demo3:
    print key

# value
for value in demo3.values():
    print value

# key&values
for item in demo3.items():
    print item # tuple

# python的iteritems,iterkeys,itervalues。作用相似，返回的是一个迭代器。迭代器可以用next来输出
rs = demo1.iteritems()
print rs.next()
print rs.next()
```

### php数组
php数组支持一维数组和多维数组的混搭。数组的value可以是任意类型。

```php

// 关联数组。需要指定key。
$arr1 = array(
    "name"=>"kurt",
    "age" =>18,
    "sex" =>1
);
// 索引数组，key会自动以0开始。
$arr2 = [ 12, 34,2,41,5 ]; // 简写数组

// 多维数组
$arr3 = [
    'http'  => ['nginx','apache','iis'],
    'cache' => ['redis','memcache'],
    'database' => ['mysql','orecal','DB2','mssql'],
    'remark' => '多维数组下面的value是相对独立'
]

// 遍历
foreach ($arr1 as $k=>$v)
{
        echo $k,$v ; // key && value
}
```

### java数组
数组中可以存放任意类型的数据，但是同一个数组存放的元素必须一致。
```
# 声明并创建可以存3个整数的数组
int[] arr0 = new int[3] ; 
# 先声明后创建可以存3个整数数组
int[] arr1; 
arr1=new int[3]; 

# 数组赋值。初始化数组的时候会赋值为0.
arr0[0] = 'a';
arr0[1] = 'b';
arr0[2] = 'c';
# arr0[3] = 'd'; # 报错，超出索引

# 数组静态初始化。。
int[] arr2 = new int[]{1,2,3,4}; # 声明并初始化并复制
int[] arr3 = {1,2,3,4}; # 声明后直接复制

# for循环遍历数组
for (int i = 0; i <arr0.length ; i++) 
{
    System.out.print(arr0[i]);
}
```
