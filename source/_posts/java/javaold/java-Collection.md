---
title: 'Java中Collection类数据'
cover: "/img/lynk/89.jpg"
date:       2019-10-20
subtitle: '增删改查'
tags:
	- Java
	- basis
---


## Collection集合

### 概述

#### 集合和数组可不一样:

- 数组的长度的固定的,集合可以随时增删改查
- 数组的数据类型的相同的基本数据类型,而集合存储的是不同类型的对象

#### 集合的分类
集合按照其存储结构可以分为两大类，分别是单列集合`java.util.Collection`和双列集合`java.util.Map`

#### Collection单列集合
* **Collection**：单列集合类的根接口，用于存储一系列符合某种规则的元素，它有两个重要的子接口，分别是`java.util.List`和`java.util.Set`。

其中，`List`的特点是元素有序、元素可重复。

`Set`的特点是元素无序，而且不可重复。

`List`接口的主要实现类有`java.util.ArrayList`和`java.util.LinkedList`，

`Set`接口的主要实现类有`java.util.HashSet`和`java.util.TreeSet`。

#### Collection 常用功能

Collection是所有单列集合的父接口，因此在Collection中定义了单列集合(List和Set)通用的一些方法，这些方法可用于操作所有的单列集合。方法如下：

* `public boolean add(E e)`：  把给定的对象添加到当前集合中。
* `public void clear()` :清空集合中所有的元素。
* `public boolean remove(E e)`: 把给定的对象在当前集合中删除。
* `public boolean contains(E e)`: 判断当前集合中是否包含给定的对象。
* `public boolean isEmpty()`: 判断当前集合是否为空。
* `public int size()`: 返回集合中元素的个数。
* `public Object[] toArray()`: 把集合中的元素，存储到数组中。

## list
### list集合
```java
List作为Collection集合的子接口，不但继承了Collection接口中的全部方法，而且还增加了一些根据元素索引来操
作集合的特有方法，如下：
public void add(int index, E element) : 将指定的元素，添加到该集合中的指定位置上。
public E get(int index) :返回集合中指定位置的元素。
public E remove(int index) : 移除列表中指定位置的元素, 返回的是被移除的元素。
public E set(int index, E element) :用指定元素替换集合中指定位置的元素,返回值的更新前的元素。
```
### ArrayList集合
```java
实际开发中对一个集合元素的添加与删除经常涉及到首尾操作，而LinkedList提供了大量首尾操作的方法。这些方
法我们作为了解即可：
public void addFirst(E e) :将指定元素插入此列表的开头。
public void addLast(E e) :将指定元素添加到此列表的结尾。
public E getFirst() :返回此列表的第一个元素。
public E getLast() :返回此列表的最后一个元素。
public E removeFirst() :移除并返回此列表的第一个元素。
public E removeLast() :移除并返回此列表的最后一个元素。
public E pop() :从此列表所表示的堆栈处弹出一个元素。
public void push(E e) :将元素推入此列表所表示的堆栈。
public boolean isEmpty() ：如果列表不包含元素，则返回true
```

