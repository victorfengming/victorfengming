---
title: "正则表达式、xpath和Beautifulsoup的分析和总结"
cover: "/img/lynk/61.jpg"
date:       2018-11-17
tags:
	- Python
	- solution
	- spider
	- regex
	- summer
---

### 概述
1.正则表达式是进行内容匹配，将符合要求的内容全部获取；xpath()能将字符串转化为标签，它会检测字符串内容是否为标签，但是不能检
测出内容是否为真的标签；Beautifulsoup是Python的一个第三方库，它的作用和 xpath 作用一样，都是用来解析html数据的相比之下，
xpath的速度会快一点，因为xpath底层是用c来实现的

2.三者语法不同，正则表达式使用元字符，将所有获得内容与匹配条件进行匹配，而xpath和bs4将获取的解析后的源码进行按条件筛选，筛选
出想要的标签即根据标签属性来找到指定的标签，之后对标签进行对应内容获取。

### Beautifulsoup4
bs4是一种对性能的要求,时间的限制相对较弱的一种爬取方式.

bs4爬取数据
```python
# 四种种安装方式
pip install beautifulsoup4
easy_install beautifulsoup4
# 下载tar.gz包 pip setup.py install
# 拷贝别人的bs4文件夹,知己复制到site-pakages/目录下即可

# 从程序中引入bs4
from bs4 import BeautifulSoup

# 从网页文件中直接加载
soup = BeautifulSoup(open("index.html"), "lxml")

print(soup)

```

### 作为爬虫工具对比

||re|	xpath|	bs4|
|---|---|---|---|
|安装|	内置|	第三方	|第三方|
|语法|	正则|	路径匹配|	面向对象|
|使用|	困难|	较困难	|简单|
|性能|	最高|	适中	|最低|