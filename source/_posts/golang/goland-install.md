---
title: "Goland安装"
cover: "/img/lynk/64.jpg"
date:       2020-02-26
subtitle: "工欲善其事必先利其器"
tags:
	- Golang
	- base
	- Goland
---








# ⼀、安装Goland开发⼯具
## （⼀）、介绍
Goland是由JetBrains公司旨在为go开发者提供的⼀个符合⼈体⼯程学的新
的商业IDE。这个IDE整合了IntelliJ平台的有关go语⾔的编码辅助功能和⼯具集成
特点。它具有以下特点：
- 编码辅助功能
- 符合⼈体⼯程学的设计
- ⼯具的集成
- IntelliJ插件⽣态系统

## （⼆）、下载及安装
1、官⽹下载地址：https://www.jetbrains.com/go/download/。下载完成后，在
本地执⾏解压，安装。

2、安装过程
点击“next”按钮，选择要安装的路径，然后点击“next”，会出现安装选项。
Goland安装和配置
根据你⾃⼰电脑的型号，选择合适的版本后点击“next”按钮。接着保持默认的程
序启动⽬录，点击“install”进⾏安装。整个安装过程很快，⼏乎⼀路next到底。
## （三）、使⽤Goland
1、打开Goland⼯具
2、创建项⽬：
# ⼆、第⼀个程序：HelloWorld
##（⼀）、编写第⼀个程序
1、打开编辑器创建⼀个新的helloworld.go⽂件，并输⼊以下内容：
```go
package main
import "fmt"
func main() {
 /* 输出 */
 fmt.Println("Hello, World!")
}
```

2、执⾏go程序  
执⾏go程序由⼏种⽅式

⽅式⼀：使⽤go run命令
- step1：使⽤快捷键win+R，输⼊cmd打开命令⾏提示符
- step2：进⼊helloworld.go所在的⽬录
- step3：输⼊go run helloworld.go命令并观察运⾏结果。

⽅式⼆：使⽤go build命令
- step1：使⽤快捷键win+R，输⼊cmd打开命令⾏提示符
- step2：进⼊helloworld.go所在的⽬录
- step3：输⼊go build helloworld.go命令进⾏编译，产⽣同名的
helloworld.exe⽂件
- step4：输⼊helloworld.exe，执⾏
 
⽅式三：使⽤ go playground
- step1：打开⼀下⽹址https://play.golang.org/

# 三、Goland常⽤快捷键
##（⼀）、⽂件相关快捷键：
1. CTRL+E，打开最近浏览过的⽂件。
2. CTRL+SHIFT+E，打开最近更改的⽂件。
3. CTRL+N，可以快速打开struct结构体。
4. CTRL+SHIFT+N，可以快速打开⽂件。
##（⼆）、代码格式化：
1. CTRL+ALT+T，可以把代码包在⼀个块内，例如if{…}else{…}。
2. CTRL+ALT+L，格式化代码。
3. CTRL+空格，代码提示。
4. CTRL+/，单⾏注释。CTRL+SHIFT+/，进⾏多⾏注释。
5. CTRL+B，快速打开光标处的结构体或⽅法（跳转到定义处）。
6. CTRL+“+/-”，可以将当前⽅法进⾏展开或折叠。
##（三）、查找和定位
1. CTRL+R，替换⽂本。
2. CTRL+F，查找⽂本。
3. CTRL+SHIFT+F，进⾏全局查找。
4. CTRL+G，快速定位到某⾏。
## （四）、代码编辑
1. ALT+Q，可以看到当前⽅法的声明。
2. SHIFT+ENTER，可以向下插⼊新⾏，即使光标在当前⾏的中间。
3. CTRL+Backspace，按单词进⾏删除或删除光标所在⾏。
4. CTRL+X，剪切当前光标所在⾏。
5. CTRL+D，复制当前光标所在⾏。
6. ALT+SHIFT+UP/DOWN，可以将光标所在⾏的代码上下移动。
7. CTRL+SHIFT+U，可以将选中内容进⾏⼤⼩写转化。