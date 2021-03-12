---
title: "python爬取有道詞典"
date:       2018-09-23
tags:
	- Python
	- solution
	- spider
	- regex
---



# python爬虫爬取有道翻译教程
## 编写环境
**为了宝宝们能够正确读懂本教程,在正式开始前,宝宝们需要搭建的环境如下:**
 1. 连接互联网的win10电脑,(win7也可以)
 2. Google浏览器(版本无要求)
 3. Python(版本3就可以了),如果没有安装的小伙伴可以参考[python安装以及版本检测](https://blog.csdn.net/qq_40223983/article/details/95655470)
 4. requests库(版本没啥要求),没有安装的小伙伴可以参考[python request库安装](https://blog.csdn.net/IT__LS/article/details/77801743)

## 需求分析
我们本次要爬取的网页是:[有道翻译](http://fanyi.youdao.com/)
![在这里插入图片描述](20190717151250306.png)
这时,按下F12键,调出Google浏览器的开发者工具
![在这里插入图片描述](20190717151618520.png)
现在里面没有内容,别慌,点击NetWork选项卡后,再次点击翻译按钮
![在这里插入图片描述](201907171516579.png)
这时,宝宝们会发现下面多了几条网络请求,我们点击第一个请求
![在这里插入图片描述](20190717152014646.png)
在右边有三个点的按钮,可以切换开发者工具的显示状态,我们点击第一个,让它单独分出一页显示出来,以便于观察
![在这里插入图片描述](20190717152217512.png)
在Headers选项卡中,可以查看这次请求的URL、headers参数
![在这里插入图片描述](2019071715235350.png)
往下面翻,还有data的参数值
![在这里插入图片描述](20190717152420267.png)
我们点击Response来查看这次请求的响应,也就是服务器给我们返回的结果,经过和网页中翻译内容的比较,可以确定,这个数据就是我们需要爬取的内容.
![在这里插入图片描述](20190717152633170.png)
经过我们的多次改变翻译内容,比较请求信息,我们可以发现:

在data中有三个数据是加密的变量,其中i为我们输入要翻译的字符串,而salt、sign和ts是加密的变值.所以我们猜测这个值是由JavaScript生成的,这里我们可以在页面中右键->查看网页源代码
通过Ctrl+F搜索js,找到js文件
![在这里插入图片描述](20190717153513681.png)
通过向下继续搜索,我们发现了三个以js结尾的文件
![在这里插入图片描述](20190717153733970.png)
依次点击进入后进行搜索,最终确为
http://shared.ydstatic.com/fanyi/newweb/v1.0.18/scripts/newweb/fanyi.min.js
是进行加密的JavaScript文件
![在这里插入图片描述](20190717153844373.png)
我们将这个JavaScript文件,按下Ctrl+A全选,Ctrl+C进行复制,但是这个代码是压缩格式,不利于我们的阅读
这里小编给给大家提供了一个js格式化的网站[在线代码格式化](http://tool.oschina.net/codeformat/js/)
粘贴进来后,即可复制格式化好的代码
![在这里插入图片描述](20190717154346596.png)
下面在PyCharm中新建一个js文件,将格式化好的js代码粘贴进来,PyCharm的安装可以参考[PyCharm的安装以及破解](https://blog.csdn.net/qq_40223983/article/details/95736859)

将代码粘贴进来后,按下Ctrl+F可以在代码中进行搜索,输入salt,逐个查看比对
![在这里插入图片描述](20190717160045237.png)
但是通过我们的观察,浏览器中的data参数,版本是2.1
![在这里插入图片描述](20190717160252257.png)
说明我们找的不对,继续向下搜索,只到查找到version : 2.1,这里的salt即为data中的参数
![在这里插入图片描述](20190717160404599.png)
我们发现salt、sign和ts都的r的属性,下面我们搜索一下r是如何定义的
通过搜索,我们找到了这里
![在这里插入图片描述](20190717161152255.png)
根据代码可以看出:
```
r = "" + (new Date).getTime()
```
所以ts就是当前的时间戳(这里要注意:JavaScript中的时间是以毫秒为单位的,所以在下面我们生成的时候注意单位的换算)

```
i = r + parseInt(10 * Math.random(), 10);
```
salt即为r加上一个在0-10之间的随机数

```
sign: n.md5("fanyideskweb" + e + i + "97_3(jkMYg@T[KZQmqjTK")
```
sign为对两个字符串加上e和i拼接的md5加密
其中i即为salt
![在这里插入图片描述](20190717162135404.png)
而e经过上面的代码,我们可以确定为输入的字符串
到这里我们就将需要的加密字符确定好了

## 实战代码
在PyCharm中新建一个项目,建立一个py文件
在正式写代码之前,我们可以在程序前加上
```
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by 秋叶夏风
```

第一行 指出python解释器位置,不知道的小伙伴可以参考[#!/usr/bin/python 作用](https://www.cnblogs.com/mqxs/p/7728404.html)
第二行 # -*- coding:utf-8 -*-的意思时指点该程序使用的utf-8编码,这个utf-8编码是干啥的呢？可以参考[-*- coding: utf-8 -*-的作用](https://bbs.csdn.net/topics/390476205)
(づ￣ 3￣)づ皮一下，很开心。
第三行不是必须要写的，可以省略。。。。



导入requests模块,代码如下

```
import requests
```
将Request URL复制过来

```
url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
```
将要翻译的字符输入进来

```
e = input('please input:')
```
下面构建请求需要的data
首先要构建的是ts,导入python中的时间模块

```
import time
```
生成当前的时间戳

```
sjc = time.time()
```
转换类型和进制

```
ts = str(int(sjc*1000))
```
下面构建salt
导入random模块,
```
import random
```
生成随机数并转换类型和进制
```
salt = ts + str(int(random.random()*10))
```
接下来是构建sign,需要用到python中的hashlib库来进行md5的加密,代码如下
导入模块
```
import hashlib
```
拼接字符串

```
con = "fanyideskweb" + e + salt + "97_3(jkMYg@T[KZQmqjTK"
```
md5加密

```
sign = hashlib.md5(con.encode(encoding='UTF-8')).hexdigest()
```

复制data中的内容
![在这里插入图片描述](20190717164028790.png)
在PyCharm中粘贴后按下Ctrl+R可以进行替换,需要勾选Regex(正则表达式匹配模式)
![在这里插入图片描述](20190717164247442.png)
匹配的正则表达式代码如下:
```
^(.*): (.*)
    '$1':'$2',
```
匹配好后,将i、salt、sign和ts替换成前面生成的变量

```
data = {
    'i': e,
    'from': 'AUTO',
    'to': 'AUTO',
    'smartresult': 'dict',
    'client': 'fanyideskweb',
    'salt': salt,
    'sign': sign,
    'ts': ts,
    'bv': '9c4fffad2fb69d08cd130e408e0f8108',
    'doctype': 'json',
    'version': '2.1',
    'keyfrom': 'fanyi.web',
    'action': 'FY_BY_REALTlME'
}
```
构建headers,这里给出了三个必要的参数,不确定的小伙伴可以将请求头中的Request Headers全部复制过来也行

```
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
    'Referer': 'http://fanyi.youdao.com/',
    'Cookie': 'OUTFOX_SEARCH_USER_ID=-1154806696@10.168.8.76; OUTFOX_SEARCH_USER_ID_NCOO=1227534676.2988937; JSESSIONID=aaa7LDLdy4Wbh9ECJb_Vw; ___rl__test__cookies=1563334957868'
}
```
发出请求
```
res = requests.post(url,data=data,headers=header).text
```
用正则进行匹配翻译的内容
导入re模块
```
import re
```
开始匹配
```
rep = re.findall('"tgt":"(.*?)"',res,re.S)[0]
```
输出匹配的内容

```
print(rep)
```
经过封装,完整代码如下

```
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by  秋叶夏风

def get_data(e):
    '''
    构建data数据函数
    :param e: 输入要翻译的内容
    :return: 字典类型的data数据
    '''
    import time
    sjc = time.time()
    ts = str(int(sjc * 1000))
    import random
    salt = ts + str(int(random.random() * 10))
    import hashlib
    con = "fanyideskweb" + e + salt + "97_3(jkMYg@T[KZQmqjTK"
    sign = hashlib.md5(con.encode(encoding='UTF-8')).hexdigest()

    data = {
        'i': e,
        'from': 'AUTO',
        'to': 'AUTO',
        'smartresult': 'dict',
        'client': 'fanyideskweb',
        'salt': salt,
        'sign': sign,
        'ts': ts,
        'bv': '9c4fffad2fb69d08cd130e408e0f8108',
        'doctype': 'json',
        'version': '2.1',
        'keyfrom': 'fanyi.web',
        'action': 'FY_BY_REALTlME'
    }
    return data

def get_para(e):
    '''
    获取需要的参数
    :param e: 输入字符串
    :return:
    '''
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/\
                       537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
        'Cookie': 'OUTFOX_SEARCH_USER_ID=-1154806696@10.168.8.76; \
                   OUTFOX_SEARCH_USER_ID_NCOO=1227534676.2988937; \
                   JSESSIONID=aaa7LDLdy4Wbh9ECJb_Vw; ___rl__test__cookies=1563334957868',
        'Referer': 'http://fanyi.youdao.com/'
    }
    return get_data(e),header

def search(res):
    '''
    用于匹配响应的结果
    :param res:
    :return:
    '''
    import re
    model = '"tgt":"(.*?)"'
    rep = re.findall(model, res, re.S)
    rep = rep[0]
    return rep

def main():
    import requests
    url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
    e = input('please input:')
    data = get_para(e)[0]
    header = get_para(e)[1]
    response = requests.post(url,data=data,headers=header).text
    result = search(response)
    print(result)
if __name__ == '__main__':
    while True:
        main()
```