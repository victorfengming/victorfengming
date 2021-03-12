---
title: "Golang学习笔记01"
date:       2020-04-02
subtitle: "Golang"
tags:
	- Golang
	- base
---








在go语言的main()函数外面是不能记性语句的执行的,只能写一些定义的语句

```go
package main

import (
    "fmt"
)

/*if 变体 这个num 这能够在 if else 中使用 ,作用范围固定了*/
func main() {
    if num := 10; num % 2 == 0 { //checks if number is even
        fmt.Println(num,"is even")
    }  else {
        fmt.Println(num,"is odd")
    }
}
```

```golang
package main

import "fmt"


/*go 中的复制是深拷贝,不存在引用传递的问题*/

func main() {
    a := [...]string{"USA", "China", "India", "Germany", "France"}
    b := a // a copy of a is assigned to b
    b[0] = "Singapore"
    fmt.Println("a is ", a)
    fmt.Println("b is ", b)
}
```

map集合就像python中的字典  
delete(map, key) 函数用于删除集合的元素, 参数为 map 和其对应的 key。删除函数不返回任何值。

取值,并且判断是否存在

```golang
package main

import (
    "fmt"
)

func main() {
    m := make(map[string]int)
    m["a"] = 1
    x, ok := m["b"]
    fmt.Println(x, ok)
    x, ok = m["a"]
    fmt.Println(x, ok)
}
```

go中的map是引用类型,如果赋值到其他变量后,会同步更改值

go中的结构体,就像Java中的工厂类

结构体的匿名字段就类似类的继承



接口,结构体,方法
```golang
package main

import "fmt"

/*定义接口*/
type myInterface interface {
	add()
	remove()
}
type MyS struct {
}
func (MyS) add(){
	fmt.Println("MyS增加")
}

func (MyS) remove(){
	fmt.Println("mys删除")
}

func main() {
	/*
	*/
	var myf myInterface
	myf = new(MyS)
	myf.add()
	myf.remove()
}

```

在go中
接口进行实例化,然后这个变量能够存储一个结构体的实例化对象,并且这个结构体有对应的实现的方法,这个方法之前在这个接口中声明过,然后就成了

虽然method的名字一模一样，但是如果接收者不一样，那么method就不一样

method里面可以访问接收者的字段

调用method通过.访问，就像struct里面访问字段一样


type是go语法里的重要而且常用的关键字，type绝不只是对应于C/C++中的typedef。搞清楚type的使用，就容易理解go语言中的核心概念struct、interface、函数等的使用