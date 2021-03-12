---
title: "Golang学习笔记02"
date:       2020-02-25
subtitle: "Go 中的变量"
tags:
	- Golang
	- base
---









变量: variable   
概念: 一小块内存,用于存储数据,在程序运行过程中数值可以改变  
使用:  
    step1: 变量的声明,也叫定义  
    step2: 变量的访问,赋值和取值  
go的特性:  
    静态语言:强类型语言  
    go, Java, c++, c#  
    动态语言:弱类型语言

# 变量的定义
```go
package main

import "fmt"

func main(){
	
	// 第一种:定义变量,然后进行赋值
	var num1 int
	num1 = 30
	fmt.Printf("num1d 数值是: %d\n",num1)
	/*
	在go中如果变量不被调用是不能运行成功的
	*/
	//  写在一行中
	var num2 int = 15
	fmt.Printf("num2是:>>>>>>>>>%d\n",num2)
	/*第二种 类型的判断*/
	var name = "王二狗"
	fmt.Printf("类型是:%T,namme是:>>>>>>>>>%s\n",name,name)
	// 第三种,剪短定义,也叫简短声明
	sum := 100
	fmt.Println(sum)

	// 多个变量同时定义
	var a,b,c int
	a = 1
	b = 2
	c = 3
	fmt.Println(a,b,c)

	var m, n int = 100, 200
	fmt.Println(m,n)

	var n1,f1,s1 = 100,3.14,"GOGOGOG"
	fmt.Println(n1,f1,s1)

	var(
		studentName = "李小花"
		age = 18
		sex = "女"
	)
	fmt.Println("学生姓名:%s, 年龄:%d,性别:%s\n",studentName,age,sex)

}

```

## 注意事项:
- 变量必须先定义才能使用
- go语言是静态语言,要求变量的类型和赋值的类型必须一致
- 变量名不能冲突.*(同一个作用域内不能冲突)
- 简短定义方式,左边的变量名至少有一个是新的
- 剪短定义方式, 不能定义全局变量
- 变量的零值.也叫做默认值
- 变量定义了就要使用,否则无法通过编译

如果在相同的代码块中,我们不可以再次对于相同名称的变量使用初始化声明,
例如:

a := 20 

就是不被允许的,编译器会提示错误  
no new variables on left side of :=

但是 a = 20 是可以的,因为这是给相同的变量赋予一个新的值.

如果你再定义变量a之前使用它,则会得到编译错误undefinded:a.  
如果你声明了一个局部变量却没有在相同的代码块中使用他,同样会得到

# 基本语法-常量
## 常量的使用
### 常量的声明
常量是一个简单值的标识符,在程序运行时,不会被修改的量.
const identifier [type] = value
```
显示类型定义: const b string = "abc
隐示类型定义: const b = "abc
```
## 注意: 
- 在变量定义好后需要进行调用才行,而这里常量不需要
2020-02-25-golang-note2.md
## 枚举类型
使用常量组作为枚举类型,一组相关数值的数据.
****

# go语言的数据类型
## 1. 基本数据类型
- 布尔类型：bool
    - 取值：true
    - 取值：false
- 数值类型：
    - 整数：
    - 浮点：生活中的小数
    - 复数：complex，
- 字符串：string
## 2. 复合数据类型
array， slice， map， function， pointer， struct， interface， channel。。。





- go语言出自名门正派,在go语言中可以看见C语言,Java甚至python的影子.

- go通过协程(微线程)来实现更高性能的异步并发处理




























