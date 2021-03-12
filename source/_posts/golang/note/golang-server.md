---
title: "Golang web编程服务端 客户端爬虫"
cover: "/img/lynk/88.jpg"
date:       2020-04-03
subtitle: "Golang并发编程案例"
tags:
	- Golang
	- base
---








### 服务端

```golang
package main

import (
	"fmt"
	"net/http"
)

// w 用于给客户端回复数据
// request ,读取客户端发送的数据
func HandConn(w http.ResponseWriter, r *http.Request) {
	w.Write([]byte("hello go net server"))
	// 给客户端回复数据
	fmt.Println(r)
	fmt.Println("r.Method",r.Method)
	fmt.Println("r.Body",r.Body)
	fmt.Println("r.Header",r.Header)
	fmt.Println("r.Url",r.URL)
}



func main()  {
	// 注册处理函数,用户连接,自动调用指定的处理函数
	http.HandleFunc("/",HandConn)
	// 监听绑定
	http.ListenAndServe(":8000",nil)
}


```


### 客户端


#### 普通版爬虫
```golang
package main

import (
	"fmt"
	"net/http"
	"os"
	"strconv"
)
func doWork(start, end int) {
	ori_url := "https://tieba.baidu.com/f?kw=%E7%A9%BF%E8%B6%8A%E7%81%AB%E7%BA%BF&ie=utf-8&pn="
	for i := start; i<= end ; i++ {
		url := ori_url+strconv.Itoa((i-1)*50)
		result, err := doSpider(url)
		if err != nil {
			fmt.Println("doSpider error = ",err)
			continue
		}
		/*把内容写入到文件*/
		//以这个i为文件名
		fileName := strconv.Itoa(i) + ".html"
		f, err1 := os.Create(fileName)
		if err1 != nil {
			fmt.Println("os.Create err1 = ",err1)
			continue
		}
		// 写内容
		f.WriteString(result)
		//关闭文件
		f.Close()
	}
}
func doSpider(url string) (result string, err error) {
	fmt.Println("当前准备爬取>>>>",url)
	resp, err := http.Get(url)
	if err != nil {
		fmt.Println("http.Get = ",err)
		return
	}

	defer resp.Body.Close()

	//fmt.Println("status = ",resp.Status)
	//fmt.Println("status = ",resp.StatusCode)
	//fmt.Println("status = ",resp.Header)
	//fmt.Println("status = ",resp.Body)

	/*读取网页body内容*/
	buf := make([]byte, 4*1024)

	for{
		n, err := resp.Body.Read(buf)
		if n == 0 {
			fmt.Println("read err = ", err)
			break
		}
		result += string(buf[:n])

	}
	return
}

func main() {

	var start, end int
	fmt.Println("请输入start页码(>1):")
	fmt.Scan(&start)
	fmt.Println("请输入end页码:")
	fmt.Scan(&end)
	doWork(start,end)
}

```

#### 并发爬虫
```golang
package main

import (
	"fmt"
	"net/http"
	"os"
	"strconv"
)

func spiderPage(i int, page chan<- int) {
	fmt.Println("正在爬第",i,"个网页>>>>>")
	ori_url := "https://tieba.baidu.com/f?kw=%E7%A9%BF%E8%B6%8A%E7%81%AB%E7%BA%BF&ie=utf-8&pn="
	url := ori_url + strconv.Itoa((i-1)*50)
	result, err := doSpider(url)
	if err != nil {
		fmt.Println("doSpider error = ", err)
		return
	}
	/*把内容写入到文件*/
	//以这个i为文件名
	fileName := strconv.Itoa(i) + ".html"
	f, err1 := os.Create(fileName)
	if err1 != nil {
		fmt.Println("os.Create err1 = ", err1)
		return
	}
	// 写内容
	f.WriteString(result)
	//关闭文件
	f.Close()

	page <- i
}

func doWork(start, end int) {
	page := make(chan int)
	for i := start; i <= end; i++ {
		go spiderPage(i,page)
	}
	for i := start; i <= end; i++ {
		fmt.Println("第%d个页面爬取完成",<-page)
	}
}
func doSpider(url string) (result string, err error) {
	fmt.Println("当前准备爬取>>>>", url)
	resp, err := http.Get(url)
	if err != nil {
		fmt.Println("http.Get = ", err)
		return
	}

	defer resp.Body.Close()

	//fmt.Println("status = ",resp.Status)
	//fmt.Println("status = ",resp.StatusCode)
	//fmt.Println("status = ",resp.Header)
	//fmt.Println("status = ",resp.Body)

	/*读取网页body内容*/
	buf := make([]byte, 4*1024)

	for {
		n, err := resp.Body.Read(buf)
		if n == 0 {
			fmt.Println("read err = ", err)
			break
		}
		result += string(buf[:n])

	}
	return
}

func main() {

	var start, end int
	fmt.Println("请输入start页码(>1):")
	fmt.Scan(&start)
	fmt.Println("请输入end页码:")
	fmt.Scan(&end)
	doWork(start, end)
}

```