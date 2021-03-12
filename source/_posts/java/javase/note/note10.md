---
title: "Java笔记10-Map集合"
date:       2019-10-22
tags:
	- Java
	
---








### Map集合

Map集合就是python中的dict

### Map集合的定义(声明)
Map<key的泛型, 值的泛型> 变量名 = new HashMap<key的泛型, 值的泛型>();

例如
```java
Map<Integer, String> m1 = new HashMap<Integer, String>();
```
### 增加和修改操作
```java
Object.put(new key, new value);
// 如果没有就是增加,有就是修改
// 返回值为原来的那个value的值,没有就返回null
```

### 查找操作
```java
Object.get(Object key)
// 如果不存在,返回null

```

### 判断存在操作

判断建存在
```java
Object.containsKey(1)
// 返回布尔类型
```

判断值存在
```java
Object.containsValue("one")
// 返回布尔类型
```
