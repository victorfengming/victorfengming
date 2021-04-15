---
title: "python爬取梨视频"
cover: "/img/lynk/76.jpg"
date:       2019-09-23
tags:
	- Python
	- solution
	- spider
	- regex
---



## python爬虫程序,下载梨视频到本地
## 环境搭建
关于python的介绍可以参考:python简介

python安装参考:Python安装以及版本检测

pycharm安装可以参考:PyCharm的安装和破解

pip安装参考:添加链接描述

request安装:`pip install request`

urllib安装:`pip install urllib`


## 需求分析
梨视频首页

## 具体实现
通过两次请求

## 源代码

```python
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by xiaoming

# 本模块的功能:<>
from urllib.request import *
from requests import *
from re import *
from os import *
from random import *
# makedirs('视频')
titlep = []
def single_page(url,name,video_num):
    if path.exists(name):
        pass
    else:
        makedirs(name)

    response = get(url)

    response = response.text

    rep = findall('categoryem.*?href=\"video(.*?)\"',response,S)
    # print(rep)
    j = 0
    for i in rep:
        j += 1
        i = 'https://www.pearvideo.com/video' + i
        ori_video_url = one_video(i)
        print('正在下载第',j,'个视频...')
        suiji = random()
        full_name = name+'/' + titlep[0] + '.mp4'
        # full_name = name+'/' + str(suiji)[2:] + '.mp4'
        urlretrieve(ori_video_url, full_name)
        print('成功保存视频: ',full_name)
        if j == video_num:
            break
'''
当你的才华还撑不起你的野心时,那你就应该静下心来学习
当你的能力还驾驭不了你的目标时,那就应该沉下心来历练
'''
def one_video(url):
    '''
    梨视频网站,传递一个单个视频页面,返回一个视频的原始地址
    :param url:
    :return:
    '''
    response = get(url)

    response = response.text

    # print(response)

    rep = findall(r'https://video.pearvideo.com/mp4/(.*?)mp4', response, S)

    titlee = findall(r'class="video-tt".*?>(.*?)</h1>', response, S)
    for i in titlee:
        titlep.clear()
        titlep.append(i)
    print(titlep)
    # print(rep)

    for i in rep:
        i = 'https://video.pearvideo.com/mp4/' + i + 'mp4'
        print(i)
        return i


def main():
    mulu = {
        '新知':'10',
        '社会':'1',
        '世界':'2',
        '体育':'9',
        '生活':'5',
        '科技':'8',
        '娱乐':'4',
        '财富':'3',
        '汽车':'31',
        '美食':'6',
        '音乐':'59',
    }
    # 新知 社会 世界 体育 生活 科技 娱乐 财富 汽车 美食 音乐 拍客
    url = 'https://www.pearvideo.com/category_'

    for i in mulu:
        print(i,end=" ")
    print()
    choice = input("请选择需要的视频类型:")
    num = mulu[choice]
    url = url + num

    video_num = int(input("请输入要下载视频的数量:"))
    single_page(url,choice,video_num)


main()

```