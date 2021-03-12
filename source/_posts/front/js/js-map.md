---
title: 'JavaScript中的map数据类型'
cover: "/img/lynk/23.jpg"
date:       2020-04-04
tags:
	- JavaScript
	- web
	- basis
---

## Map

　Map是一组键值对的结构，具有极快的查找速度。

### Map的定义
```js
//空map设值key-value
var m = new Map();
m.set("XiaoMing",99);
m.set("XiaoHong",66);
//构造参数传key-value
var m = new Map([['XiaoMing', 99], ['XiaoHong', 66]]);
```

### Map中的方法
```js
var a = ['A', 'B', 'C'];
var s = new Set(['A', 'B', 'C']);
var m = new Map([[1, 'x'], [2, 'y'], [3, 'z']]);
for (var x of a) { // 遍历Array
    alert(x);
}
for (var x of s) { // 遍历Set
    alert(x);
}
for (var x of m) { // 遍历Map
    alert(x[0] + '=' + x[1]);
}
```

### 更好的遍历：forEach

　forEach是iterable内置的方法，它接收一个函数，每次迭代就自动回调该函数。
```js
var a = ['A', 'B', 'C'];
a.forEach(function (element, index, array) {
    // element: 指向当前元素的值
    // index: 指向当前索引
    // array: 指向Array对象本身
    alert(element);
});
```

Set与Array类似，但Set没有索引，因此回调函数的前两个参数都是元素本身：

```js
var s = new Set(['A', 'B', 'C']);
s.forEach(function (element, sameElement, set) {
    alert(element);
});
```

Map的回调函数参数依次为value、key和map本身：
```js
var m = new Map([[1, 'x'], [2, 'y'], [3, 'z']]);
m.forEach(function (value, key, map) {
    alert(value);
});
```