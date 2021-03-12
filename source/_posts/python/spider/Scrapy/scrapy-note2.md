---
title: "Scrapy笔记02"
date:       2019-11-21
tags:
	- Python
	- solution
	- basis
	- spider
---
  
  











### 项目结构
>1. Scrapy Engine:提供并发的支持-已经实现好的
>2. Scheduler(调度器): 存储以及调度(URL+函数) = Request - 已经实现好的,不需要修改
>3. Downloader(下载器):爬虫第三部,通过request下载返回值(HTML,JSON),RESPONSE - 已经实现好的
>4. Spiders(蜘蛛):爬虫第四步,获取到了Response之后,需要定位具体信息 - 需要自己实现的
>5. Item Pipeline(项目管道):存储或者是继续处理具体信息 - 需要自己实现的  


新建一个Scrapy的项目

爬虫的重点在分析网页上面,而不是在写程序上面

### 后续内容
- post请求怎么办
- 如何使用image pipeline
- 如何添加headers相关信息
- 如何添加代理
- 全网爬虫如何建立
- 各种中间件的内容
- 分布式爬虫的原理以及案例

### scrapy数据流
>1. spiders 中需要有start_urls或者start_requests,生成初始的requests,发送给Engine处理
>2. 将Request放到sheduler中存储
>3. 当并发处理有空闲的时候,Engine就会到sheduler中获取一个request,当欧昂将
>4. 将获取到的request放到Downloader中下载,会经过Downloader Middleware
>5. 通过request下载内容,之后,会生成一个response的内容 将response的内容返还给Engine
>6. Engine将Response返还给Spiders,在Spiders中定位具体的信息,会经过中间件,Spider Middleware
>7. 返回的过程中会生成两类数据,其一是items,其二是requests(第7个requests会经过中间件,而第一个requests不会经过中间件)
>8. 如果返回值是ITEMS, 那么我们将它放入ITEM Pipeline 如果返回的是Request,将它加入到Scheduler中共
>9. 循环三到八不,知道scheduler中没有request为止

### 中间件有什么用处?