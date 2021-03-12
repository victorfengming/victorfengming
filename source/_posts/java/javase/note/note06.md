---
title: "Java笔记06-Map集合"
date:       2019-10-20
tags:
	- Java
	
---


* content
{:toc}





# Map集合

### 学习目标

- 能够说出Map集合特点
- 使用Map集合添加方法保存数据
- 使用”键找值”的方式遍历Map集合
- 使用”键值对”的方式遍历Map集合
- 能够使用HashMap存储自定义键值对的数据
- 能够使用HashMap编写斗地主洗牌发牌案例

### Map集合概述
啥也不用说,Map集合就相当于python中的字典

Java提供了专门的集合类用来存放这种对象关系的对象，即 java.util.Map 接口。


说白了就是键值对儿的形式存的数据

### Map接口中的常用方法
Map接口中定义了很多方法，常用的如下：

- public V put(K key, V value) : 把指定的键与指定的值添加到Map集合中。
- public V remove(Object key) : 把指定的键 所对应的键值对元素 在Map集合中删除，返回被删除元素的
值。
- public V get(Object key) 根据指定的键，在Map集合中获取对应的值。
- public Set<K> keySet() : 获取Map集合中所有的键，存储到Set集合中。
- public Set<Map.Entry<K,V>> entrySet() : 获取到Map集合中所有的键值对对象的集合(Set集合)。


### Map接口的方法演示
```java
public class Demo01 {

    public static void main(String[] args) {
//创建 map对象
        HashMap<String, String> map = new HashMap<String, String>();
//添加元素到集合
        map.put("黄晓明", "杨颖");
        map.put("黄晓明", "杨颖2");
        map.put("文章", "马伊琍");
        map.put("邓超", "孙俪");
        System.out.println(map);
//String remove(String key)
        System.out.println(map.remove("邓超"));
        System.out.println(map);
// 想要查看 黄晓明的媳妇 是谁
        System.out.println(map.get("黄晓明"));
        System.out.println(map.get("邓超"));
    }
}
```
运行结果:
```cmd
{邓超=孙俪, 文章=马伊琍, 黄晓明=杨颖}
孙俪
{文章=马伊琍, 黄晓明=杨颖}
杨颖
null
```