---
title: "Golang语言写99乘法表"
date:       2020-02-28
subtitle: "双重for循环"
tags:
	- Golang
	- base
---





* content
{:toc}



### 1. 标准写法:
```golang
for 表达式1;表达式2;表达式3{
    循环体
}
```

### 2. 同时省略表达式1和表达式3
```golang
for 表达式2{
    循环体
}
// 相当于while(条件)
```

### 3. 同时省略3个表达式
```golang
for{
    循环体
}
// 相当于while(true)
// 注意:当for循环中,省略了表达式2,就相当于直接作用在了true上
```
### 4. 其他写法
for循环中同时省略几个表达式都可以..
- 省略表达式1:变量的初始定义要在外面
- 省略表达式2:循环永远成立->>>死循环
- 省略表达式3:变量的更新需要写着循环体里面,否则还是死循环

## 99乘法表程序
```golang
package main

import "fmt"

/*
循环语句
for 表达式1；表达式2；表达式3{
	循环体
}
*/
func main() {
	for i := 1; i < 10; i++ {
		for j := 1; j<i+1; j++{
			fmt.Print(i,"*",j,"=",i*j)
			fmt.Print("\t")
		}
		fmt.Println()
	}
}

```