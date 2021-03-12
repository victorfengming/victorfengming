---
title: Python脚本实现爬取哔哩哔哩壁纸
date: 2021-03-12 21:25:09
tags:
---


```python


"""
爬虫

爬取 哔哩哔哩中 的领克壁纸



"""
import re

import requests

def main():

    url = "https://www.bilibili.com/read/cv8222028"

    meizi_html = requests.get(url).text

    # print(meizi_html)
    patt = "data-src=\"//i0.hdslb.com/bfs/article/(.*?.\w\wg)\" width"
    src_list = re.findall(patt,meizi_html)

    # src = src_list.group(0)

    i = 0
    for src in src_list:
        i+=1
        image_url = "http://i0.hdslb.com/bfs/article/"+src
        download(image_url,"./lynk/",str(i)+image_url[-4:])
        print(src)

def download(image_url,dir_path,file_name):
    r = requests.get(image_url)
    with open(dir_path+file_name, 'wb') as f:
        f.write(r.content)
# 测试可用
# download("http://i0.hdslb.com/bfs/article/1fff23a7966b36b1ccb13c6203006969fedaf3b5.jpg","./","demo01.jpg")


main()

```

>在第一次获取到页面,最好先保存一下HTML,免得被封掉
>


