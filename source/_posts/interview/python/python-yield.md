---
title: "Python中的yield详解"
date:       2019-11-22
tags:
	- Python
	- background
	- interview
---










阅读别人的python源码时碰到了这个yield这个关键字，各种搜索终于搞懂了，在此做一下总结：

1. 通常的for...in...循环中，in后面是一个数组，这个数组就是一个可迭代对象，类似的还有链表，字符串，文件。它可以是mylist = [1, 2, 3]，也可以是mylist = [x*x for x in range(3)]。
它的缺陷是所有数据都在内存中，如果有海量数据的话将会非常耗内存。
2. 生成器是可以迭代的，但只可以读取它一次。因为用的时候才生成。比如 mygenerator = (x*x for x in range(3))，注意这里用到了()，它就不是数组，而上面的例子是[]。
3. 我理解的生成器(generator)能够迭代的关键是它有一个next()方法，工作原理就是通过重复调用next()方法，直到捕获一个异常。可以用上面的mygenerator测试。
4. 带有 yield 的函数不再是一个普通函数，而是一个生成器generator，可用于迭代，工作原理同上。
5. yield 是一个类似 return 的关键字，迭代一次遇到yield时就返回yield后面(右边)的值。重点是：下一次迭代时，从上一次迭代遇到的yield后面的代码(下一行)开始执行。
6. 简要理解：yield就是 return 返回一个值，并且记住这个返回的位置，下次迭代就从这个位置后(下一行)开始。
7. 带有yield的函数不仅仅只用于for循环中，而且可用于某个函数的参数，只要这个函数的参数允许迭代参数。比如array.extend函数，它的原型是array.extend(iterable)。
8. send(msg)与next()的区别在于send可以传递参数给yield表达式，这时传递的参数会作为yield表达式的值，而yield的参数是返回给调用者的值。——换句话说，就是send可以强行修改上一个yield表达式值。比如函数中有一个yield赋值，a = yield 5，第一次迭代到这里会返回5，a还没有赋值。第二次迭代时，使用.send(10)，那么，就是强行修改yield 5表达式的值为10，本来是5的，那么a=10
9. send(msg)与next()都有返回值，它们的返回值是当前迭代遇到yield时，yield后面表达式的值，其实就是当前迭代中yield后面的参数。
10. 第一次调用时必须先next()或send(None)，否则会报错，send后之所以为None是因为这时候没有上一个yield(根据第8条)。可以认为，next()等同于send(None)。
### 代码示例1

```python
#encoding:UTF-8  
def yield_test(n):  
    for i in range(n):  
        yield call(i)  
        print("i=",i)  
    #做一些其它的事情      
    print("do something.")      
    print("end.")  
  
def call(i):  
    return i*2  
  
#使用for循环  
for i in yield_test(5):  
    print(i,",")  
```

##### 结果是：

```shell
>>>   
0 ,  
i= 0  
2 ,  
i= 1  
4 ,  
i= 2  
6 ,  
i= 3  
8 ,  
i= 4  
do something.  
end.  
>>> 
```

理解的关键在于：下次迭代时，代码从yield的下一跳语句开始执行。

### 代码示例2：
```python
def node._get_child_candidates(self, distance, min_dist, max_dist):
    if self._leftchild and distance - max_dist < self._median:
        yield self._leftchild
    if self._rightchild and distance + max_dist >= self._median:
        yield self._rightchild
```
与前面不同的是，这个函数中没有for循环，但它依然可以用于迭代。
node._get_child_candidates函数中有yield，所以它变成了一个迭代器，可以用于迭代。

执行第一次迭代时（其实就是调用next()方法），如果有左节点并且距离满足要求，会执行第一个yield，这时会返回self._leftchild并完成第一个迭代。

执行第二次迭代时，从第一个yield后面开始，如果有右节点并且距离满足要求，会执行第二个yield，这时会返回self._rightchild并完成第一个迭代。

执行第三次迭代时，第二个yield后再无代码，捕获异常，退出迭代。

##### 调用过程：
```python
result, candidates = list(), [self]
while candidates:
    node = candidates.pop()
    distance = node._get_dist(obj)
    if distance <= max_dist and distance >= min_dist:
        result.extend(node._values)
    candidates.extend(node._get_child_candidates(distance, min_dist, max_dist))
return result
```
上面的node._get_child_candidates(self, distance, min_dist, max_dist)是放在extend()函数中作为参数的，为什么可以这么用，就因为extend函数的参数不仅仅支持array，只要它是一个迭代器就可以。它的原型是array.extend(iterable)。



作者：千若逸  
链接：https://www.jianshu.com/p/d09778f4e055  
来源：简书  
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。  