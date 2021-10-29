---
title: "python爬取妹子图"
cover: "/img/lynk/51.jpg"
date:       2019-09-23
subtitle: "tkinter下载界面"
tags:
	- Python
	- solution
	- spider
	- tkinter
---









### 环境准备

1. python的安装

利用python爬虫爬取图片，首先要进行安装python

可以参考:[window下python的安装与版本检测](https://victorfengming.gitee.io/blog/python-install-window/)
2. IDE的安装

PyCharm 是一种 Python IDE，带有一整套可以帮助用户在使用 Python 语言开发时提高其效率的工具，比如调试、语法高亮、Project 管理、代码跳转、智能提示、自动完成、单元测试、版本控制。此外，该 IDE 提供了一些高级功能，以用于支持 Django 框架下的专业 Web 开发。其中免费的[社区版（点击即下载）](https://www.jetbrains.com/pycharm/download/download-thanks.html?platform=windows&code=PCC&utm_source=so&utm_source=so)已经能够满足我们的需求，它的安装可以参考:[PyCharm的安装以及破解](https://victorfengming.gitee.io/blog/pycharm-install/),关于它的使用可以参考[Pycharm使用秘籍](https://www.luffycity.com/free/39)
3. requests的安装  
这里我们在终端中用pip安装  
`pip install requests`

如果出现pip没有找到或者不是系统命令,可以参考[python如何安装pip](https://blog.csdn.net/qq_40223983/article/details/96832040)

### 爬虫简介

爬虫是什么？

爬虫爬取的过程从本质上说就是在模拟 HTTP 请求，记住这句话，这就是我们后面经常需要做的事情。一般用户获取网络数据的方式有两种：

- a. 浏览器提交 HTTP 请求--->下载网页代码--->解析成页面。
- b. 模拟浏览器发送请求（获取网页代码）->提取有用的数据->存放于数据库或文件中。

爬虫就是在做第二种事情，大致过程如下:

i. 通过 HTTP 库向目标站点发起请求，即发送一个 Request，请求可以包含额外的 headers 等信息，等待服务器的响应

ii. 如果服务器正常响应，会得到一个 Response，Response 的内容便是所要获取的页面内容，类型可能有 HTML、JSON、二进制文件（如图片、视频等类型）。

iii. 得到的内容可能是 HTML，可以用正则表达式、网页解析库进行解析。可能是 JSON，可以直接转成 JOSN 对象进行解析，可能是二进制数据，可以保存或者进一步处理

iv. 保存形式多样，可以保存成文本，也可以保存至数据库，或者保存成特定格式的文件。
许多读者可能不知道上面具体在做什么，那么接下来我们通过浏览器抓包分析上面的过程，笔者推荐使用 Chrome，对开发者很友好，后续我们会经常使用到，Chrome 下载，如果下载速度较慢，建议使用国内 Chrome 镜像下载安装。

### 利用python抓取网络图片的步骤：

1. 根据给定的网址获取网页源代码

2. 利用正则表达式把源代码中的图片地址过滤出来

3. 根据过滤出来的图片地址下载网络图片

### 爬虫部分(源码)

```python
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by victor

import requests
import re
import os
from urllib import request
import time
'''
妹子图网站反扒手段 ,限制方位来源,需在headers中加入 Referer 跳转来源
urlretrieve 无法加入请求头headers
我们使用bytes直接下载图片
同时需注意限制访问时间间隔,访问频次过快,服务器进制访问

#### 注意图片下载地址是.jpg格式,我们下午使用链接不正确所以可以下载但无法打开

'''
def ori_video(meizi_url):
    headers = {
        'Referer': 'https://www.mzitu.com',
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36'
    }
    # print(meizi_url)
    meizi_html = requests.get(meizi_url,headers = headers).text
    end_url = re.findall("<span>(\d+?)</span></a><a href='https://www.mzitu.com/\d*?/2'><span>下一页&raquo",meizi_html)
    name_id = re.search('<h2 class="main-title">(.*?)</h2>',meizi_html).group(1)
    name = re.sub('!','',name_id)
    print(end_url)
    end_url = int(end_url[0])

    for x in range(1,end_url):
        newurl = meizi_url + '/' + str(x)

        # print(name)
        newurl = meizi_url + '/' +  str(x)
        # print(newurl)
        html = requests.get(newurl,headers = headers).text
        end_re = re.findall(r'<div class="main-image"><p><a href=".+?" ><img src="(.*?)"',html)
        print(end_re[0])

        headers = {
            'Referer': 'https://www.mzitu.com',
            'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36'
        }
        # urlretrieve(end_re[0],path+'/'+ str(x)) 不能加请求头
        req = request.Request(end_re[0],headers = headers)
        response = request.urlopen(req)
        fname = end_re[0].split('/')[-1]
        print('正在下载: ',fname)

        if name not in os.listdir():
            os.mkdir(name)
        with open(name + '/' + fname, 'wb') as f:
            f.write(response.read())
        ''' 反反爬  设置时间间隔 防止服务器封锁IP或禁止访问'''
        time.sleep(1)


# 下载一页的内容
def page_one():
    url = 'https://www.mzitu.com/'
    headers = {
        'Referer': 'https://www.mzitu.com',
        'user-agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36'
    }
    html = requests.get(url,headers = headers).text
    # print(html)
    ret = re.findall('<li><a href="(.*?)" target="_blank"><img class=',html)
    print(ret)
    # for meizi_url in ret:
    meizi_url = 'https://www.mzitu.com/166998'
    ori_video(meizi_url)


# 调用
page_one()
```


### 带有图形界面部分(源码)
```python
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by victor

# 本模块的功能:<带有图形界面的妹子图爬虫程序>
'''
加入了顶部颜色的更改,实现了排它思想
下载按钮在下载中的按钮颜色更改
加上了 一个顶部的转台信息栏
加入了多线程功能,解决了在下载过程中图形界面卡顿问题
TODO 显示预览图
'''
# 导包
from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askdirectory
from requests import get
from re import findall
from re import search
from re import sub
from os import listdir
from os import mkdir
from os import path
from urllib.request import Request
from urllib.request import urlopen
from time import sleep
from threading import Thread


class Tk_gui():

    def __init__(self):
        '''
        初始化魔术方法
        用于设置界面的初始状态
        '''
        # 创建tkinter窗口
        self.root = Tk()
        # 设置窗口的标题
        self.root.title('一起来看美女')
        # 设置窗口的长和宽,最大值和最小值设置相同,用户不可调整窗口大小
        self.root.minsize(780, 370)
        self.root.maxsize(780, 570)


        # 初始化
        self.curr_page = 1
        self.page_max = self.get_page_max()
        # 初始化主要url
        self.curr_url = 'https://www.mzitu.com/'
        self.tit_list = s.page_one(self.curr_url)

        # 调用主要逻辑执行函数
        self.main_logic()

    def thread_it(self, func, *args):
        '''
        将函数打包进线程
        :param func:
        :param args:
        :return:
        '''
        # 创建
        t = Thread(target=func, args=args)
        # 守护 !!!
        t.setDaemon(True)
        # 启动
        t.start()
        # 阻塞--卡死界面！
        # t.join()

    def get_save_path(self):

        path_ = askdirectory()
        Tk_gui.path.set(path_)

    def get_page_max(self):
        return 50

    def main_logic(self):
        '''
        主业务逻辑
        :return:
        '''
        # 顶部信息栏
        topp = Frame()
        topp.grid(row=0, column=0)
        # 内容栏
        self.cont = Frame()
        self.cont.grid(row=1, column=0)
        # 输入选项操作
        self.indo = Frame()
        self.indo.grid(row=0, column=1, rowspan=2)

        # 状态栏
        self.stat = Frame()
        self.stat.grid(row=2, column=0)

        self.top_menu(topp)
        self.stat_info()
        self.main_content(self.get_num_list())

        self.get_title_list('https://www.mzitu.com')

        # 加入主消息循环
        self.root.mainloop()

    def download(self):
        '''
        正式下载图片
        :return:
        '''
        self.btn5['background'] = 'pink'
        para = self.search()
        s.ori_video(para[0], para[1], para[2])

    def search(self):
        '''
        搜索预加载页面中的图片个数
        :return:
        '''
        # print("下载url:")
        index = int(self.number_chosen.get()) - 1
        # print('index:%d'%index)
        url = tit_list[0][index]
        para = s.pre_download(url)
        self.detail_info["text"] = "本页有" + str(para[0]) + "张图"
        return para

    def get_title_list(self, url):
        '''
        获取标题列表内容
        :param url:
        :return:
        '''
        global tit_list
        tit_list = s.page_one(url)
        self.info["text"] = "\n".join(tit_list[1])

    def get_num_list(self):
        '''
        获取数值列表
        :return:
        '''
        num = []
        for i in range(1, 25):
            num.append(str(i))
        num_str = "\n".join(num)
        return num_str

    def set_top_bg(self,id):
        '''

        :param id: id 是按钮摆放的位置,int类型的
        :return:
        '''
        # 还原现场
        for i in self.button_list:
            i['background'] = 'skyblue'

        self.button_list[id-1]['background'] = 'pink'
        # for i in
        #     if curr == i:
        #         i['bg']=='gray'
        #     else:
        #         i['bg']==''
        pass

    def update_page_url(self, option, reg_url):
        if option:
            if option == 2:
                print('下一页')
                if self.curr_page < self.page_max:
                    self.curr_page += 1
            elif option == 1:
                print('上一页')
                if self.curr_page > 1:
                    self.curr_page -= 1
            elif option == 3:
                self.curr_page = int(self.page_chosen.get())
        if reg_url:
            # TODO 设置更新按钮的背景颜色
            # 调用set_button_color
            # 重置页面数
            self.curr_page = 1
            self.curr_url = reg_url
        if self.curr_page == 1:
            url = self.curr_url
        else:
            url = self.curr_url + 'page/' + str(self.curr_page) + '/'
        print(self.curr_page)
        self.page_info['text'] = '当前页数:' + str(self.curr_page)
        self.get_title_list(url)

    def top_menu(self, topp):
        '''
        用于绘制顶部菜单
        :param topp:
        :return:
        '''
        self.button_list = []
        # 菜单栏
        url_list = {
            '推荐': 'https://www.mzitu.com/',
            '性感': 'https://www.mzitu.com/xinggan/',
            '日本': 'https://www.mzitu.com/japan/',
            '台湾': 'https://www.mzitu.com/taiwan/',
            '清纯': 'https://www.mzitu.com/mm/'
        }
        # update_page_url函数是用来更新页面的内容以及后面要下载的url的
        menu = Button(topp, text='', font=("Arial", 12), width=1)
        menu.grid(row=0, column=0)

        def put_button(key, col):
            '''
            用于画出按钮组件
            :param contain:按钮显示的文本内容
            :param key: 命令执行的函数选择的键
            :param col: 按钮放置的列数
            :return:
            '''
            # self.curr_button = StringVar()
            # TODO 怎么解决一个command 执行两个函数的问题
            # 这里用is机制的占了个位置,让两个函数都执行,随便返回点啥,我都不要,哈哈哈哈哈
            # 之前尝试过用函数的参数传递,但是有点不太好管理
            # 后来用的+号,程序报错,虽然界面中看不出来,但是我还是有点强迫症的让他不报错
            self.menu = Button(topp, text=key, font=("Arial", 12), width=7,\
            command=lambda: self.update_page_url(option=0, reg_url=url_list[key]) is \
                            self.set_top_bg(col))

            self.menu.grid(row=0, column=col)
            self.button_list.append(self.menu)
            for i in self.button_list:
                i['background'] = 'skyblue'
            self.button_list[0]['background'] = 'pink'
            # if key == self.curr_button:
            #     menu['background'] = 'gray'

        i = 1
        for contain in url_list.keys():
            put_button(contain, i)
            i += 1
        #

        # 前进和后退,进行页数的更改
        # option为标记位,0为不改变

        # 顶部的显示当前页数的lable
        # 定义成类属性,以便于在Spider类中更改其值
        self.page_info = Label(topp, text='', justify="left", \
                               font=("Arial", 12), width=10)
        self.page_info.grid(row=0, column=6)

        self.page_info["text"] = '当前页数:1'

    def main_content(self, num_str):
        '''
        主要内容界面,包括数字列表的显示,标题列表的显示以及右边输入框和下载按钮部分
        :param num_str:数字列表显示内容
        :return:
        '''

        # 左边的序号栏
        one = Label(self.cont, text=num_str, font=("Arial", 12),relief='ridge')
        one.grid(row=1, column=0)
        # 中间的主要信息栏
        '''
        relief(可选值为：flat(默认),sunken,raised,groove,ridge)，borderwidth(边框的宽度，单位是像素，默认根据系统而定，一般是1或2像素)
        '''
        self.info = Label(self.cont, text='info', justify="left", \
                          font=("Arial", 12), width=49,relief='ridge')
        self.info.grid(row=1, column=1, columnspan=6)
        # 右边的选择栏
        # 上面的提升lable
        ttk.Label(self.indo, text="\n\n\n选择一个", font=("Arial", 12)).grid(column=0, row=4, columnspan=2)
        # 添加一个标签，并将其列设置为1，行设置为0
        # 中间的下拉框
        number = StringVar()
        # 这里直接定义成为类的属性,以便于其他方法中直接获取其选择的页数
        self.number_chosen = ttk.Combobox(self.indo, width=12, textvariable=number)
        self.number_chosen['values'] = tuple(range(1, 25))  # 设置下拉列表的值
        self.number_chosen.grid(column=0, row=5, columnspan=2)  # 设置其在界面中出现的位置 column代表列 row 代表行
        self.number_chosen.current(0)  # 设置下拉列表默认显示的值，0为 numberChosen['values'] 的下标值

        # 由于进行了类的封装,所以不需要借用列表的穿透性了
        # 直接定义一个类的成员属性即可传递到类中的任何位置
        # 这里实时更新当前选中的数字内容,以便于按下下载按钮时能够定位到准确的页面
        # TODO 可以优化到其他位置,减少功能模块之间的耦合性
        # self.user_choose_num = self.number_chosen.get()

        # 点击查询按钮
        btn4 = Button(self.indo, text="查询图片个数", font=("Arial", 12),background = 'gray', command=lambda: self.thread_it(self.search))
        btn4.grid(column=0, row=6, columnspan=2)

        # 外加的详细信息栏
        # 这里直接定义成为类的属性,以便于其他方法中直接修改其内容
        self.detail_info = Label(self.indo, text='', justify="left", \
                                 font=("Arial", 12), width=10)
        self.detail_info.grid(row=7, column=0, columnspan=2)
        # 点击下载的按钮
        self.btn5 = Button(self.indo, text="下载此页图片", font=("Arial", 12),background = 'gray', command=lambda: self.thread_it(self.download))
        self.btn5.grid(column=0, row=12, columnspan=2)

        # 外加的详细下载信息栏
        # 定义成类属性,以便于在Spider类中更改其值
        Tk_gui.terminal_info = Label(self.stat, text='', justify="left", \
                                     font=("Arial", 12))
        Tk_gui.terminal_info.grid(row=0, column=0)

        Tk_gui.terminal_info["text"] = ''

        menu = Button(self.indo, text=" 上一页", font=("Arial", 12), background='gray',
                      command=lambda: self.thread_it(lambda: self.update_page_url(option=1, reg_url='')))
        menu.grid(row=0, column=0)

        menu = Button(self.indo, text="下一页 ", font=("Arial", 12), background='gray',
                      command=lambda: self.thread_it(lambda: self.update_page_url(option=2, reg_url='')))
        menu.grid(row=0, column=1)

        # 添加一个标签，并将其列设置为1，行设置为0
        # 中间的下拉框
        page = StringVar()
        # 这里直接定义成为类的属性,以便于其他方法中直接获取其选择的页数
        self.page_chosen = ttk.Combobox(self.indo, width=12, textvariable=page)
        self.page_chosen['values'] = tuple(range(1, self.page_max + 1))  # 设置下拉列表的值
        # 设置其在界面中出现的位置 column代表列 row 代表行
        self.page_chosen.grid(row=2, column=0, columnspan=2)
        # 设置下拉列表默认显示的值，0为 numberChosen['values'] 的下标值
        self.page_chosen.current(0)

        menu = Button(self.indo, text=" 跳转到此页 ", font=("Arial", 12),background = 'gray',
                      command=lambda: self.update_page_url(option=3, reg_url=''))
        menu.grid(row=3, column=0, columnspan=2)

        # 用于指定下载路径
        Tk_gui.path = StringVar()
        #
        Label(self.indo, text="目标路径:", font=("Arial", 12)). \
            grid(row=9, column=0, columnspan=2)
        Entry(self.indo, textvariable=self.path, width=15). \
            grid(row=10, column=0, columnspan=2)
        Button(self.indo, text="更改下载路径", font=("Arial", 12), background='gray', command=self.get_save_path). \
            grid(row=11, column=0, columnspan=2)

        # 初始化保存路径
        Tk_gui.path.set(path.dirname(__file__))

    def stat_info(self):
        # 外加的详细下载信息栏
        # 定义成类属性,以便于在Spider类中更改其值
        Tk_gui.stat_info = Label(self.stat, text='', justify="left", \
                                     font=("Arial", 12))
        Tk_gui.stat_info.grid(row=0, column=0)

        Tk_gui.stat_info["text"] = ''


class Spider():

    def pre_download(self, meizi_url):
        self.headers = {
            'Referer': 'https://www.mzitu.com',
            'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36'
        }
        # print(self.meizi_url)
        meizi_html = get(meizi_url, headers=self.headers).text
        end_url = findall("<span>(\d+?)</span></a><a href='https://www.mzitu.com/\d*?/2'><span>下一页&raquo", meizi_html)
        name_id = search('<h2 class="main-title">(.*?)</h2>', meizi_html).group(1)
        name = sub('!', '', name_id)
        print("本页的总数:")
        end_url = int(end_url[0])
        print(end_url)
        return end_url, name, meizi_url

    def ori_video(self, end_url, name, meizi_url):
        # 获取用户选择的路径
        choose_dir = Tk_gui.path.get()
        # print('选择的路径：', choose_dir)
        # 判断文件夹是否存在
        # print('lsitdir', listdir(choose_dir))
        # name = choose_dir + '/' + name

        curr_dir = choose_dir + '/' + name
        for x in range(1, end_url + 1):
            # 更新详情信息的内容
            Tk_gui.terminal_info["text"] = \
                '正在下载图片...\t' + '当前进度:' + str(x) + ' / ' + str(end_url)

            if name not in listdir(choose_dir):
                mkdir(curr_dir)
                Tk_gui.terminal_info["text"] = '创建文件夹:'+ curr_dir
            self.single(x, name, meizi_url, curr_dir)
        Tk_gui.terminal_info["text"] = '图片下载完成,成功保存到'+curr_dir[0:25]+'...'

    def single(self, x, name, meizi_url, curr_dir):
        newurl = meizi_url + '/' + str(x)

        html = get(newurl, headers=self.headers).text
        end_re = findall(r'<div class="main-image"><p><a href=".+?" ><img src="(.*?)"', html)
        print(end_re[0])

        # urlretrieve(end_re[0],path+'/'+ str(x)) 不能加请求头
        req = Request(end_re[0], headers=self.headers)
        response = urlopen(req)
        fname = end_re[0].split('/')[-1]
        print('正在下载: ', fname)

        # 文件夹名字前面加上所选择的路径

        with open(curr_dir + '/' + fname, 'wb') as f:
            f.write(response.read())
        ''' 反反爬  设置时间间隔 防止服务器封锁IP或禁止访问'''
        # sleep(1)

    def page_one(self, url):
        '''
        # 下载一页的内容
        :param url:
        :return:
        '''
        # url = 'https://www.mzitu.com/'
        # url = 'https://www.mzitu.com/page/2/'
        headers = {
            'Referer': 'https://www.mzitu.com',
            'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36'
        }
        html = get(url, headers=headers).text
        # print(html)
        ret = findall('<li><a href="(.*?)" target="_blank"><img class=', html)
        tit = findall("<li><a.*?alt=\'(.*?)\'", html)
        return ret, tit

# 实例化对象
s = Spider()
t = Tk_gui()
```

### 相关阅读
[python爬取梨视频](https://blog.csdn.net/qq_40223983/article/details/96857832)

[python爬取有道翻译](https://blog.csdn.net/qq_40223983/article/details/96310326)


### 维护

> mzitu网站加了一个类导致原来的正则不正确
>
>修复如下

```python
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by victor

# 本模块的功能:<带有图形界面的妹子图爬虫程序>
'''
加入了顶部颜色的更改,实现了排它思想
下载按钮在下载中的按钮颜色更改
加上了 一个顶部的转台信息栏
加入了多线程功能,解决了在下载过程中图形界面卡顿问题
TODO 显示预览图
'''
# 导包
from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askdirectory
from requests import get
from re import findall
from re import search
from re import sub
from os import listdir
from os import mkdir
from os import path
from urllib.request import Request
from urllib.request import urlopen
from time import sleep
from threading import Thread


class Tk_gui():

    def __init__(self):
        '''
        初始化魔术方法
        用于设置界面的初始状态
        '''
        # 创建tkinter窗口
        self.root = Tk()
        # 设置窗口的标题
        self.root.title('一起来看美女')
        # 设置窗口的长和宽,最大值和最小值设置相同,用户不可调整窗口大小
        self.root.minsize(780, 370)
        self.root.maxsize(780, 570)

        # 初始化
        self.curr_page = 1
        self.page_max = self.get_page_max()
        # 初始化主要url
        self.curr_url = 'https://www.mzitu.com/'
        self.tit_list = s.page_one(self.curr_url)

        # 调用主要逻辑执行函数
        self.main_logic()

    def thread_it(self, func, *args):
        '''
        将函数打包进线程
        :param func:
        :param args:
        :return:
        '''
        # 创建
        t = Thread(target=func, args=args)
        # 守护 !!!
        t.setDaemon(True)
        # 启动
        t.start()
        # 阻塞--卡死界面！
        # t.join()

    def get_save_path(self):

        path_ = askdirectory()
        Tk_gui.path.set(path_)

    def get_page_max(self):
        return 50

    def main_logic(self):
        '''
        主业务逻辑
        :return:
        '''
        # 顶部信息栏
        topp = Frame()
        topp.grid(row=0, column=0)
        # 内容栏
        self.cont = Frame()
        self.cont.grid(row=1, column=0)
        # 输入选项操作
        self.indo = Frame()
        self.indo.grid(row=0, column=1, rowspan=2)

        # 状态栏
        self.stat = Frame()
        self.stat.grid(row=2, column=0)

        self.top_menu(topp)
        self.stat_info()
        self.main_content(self.get_num_list())

        self.get_title_list('https://www.mzitu.com')

        # 加入主消息循环
        self.root.mainloop()

    def download(self):
        '''
        正式下载图片
        :return:
        '''
        self.btn5['background'] = 'pink'
        para = self.search()
        s.ori_video(para[0], para[1], para[2])

    def search(self):
        '''
        搜索预加载页面中的图片个数
        :return:
        '''
        # print("下载url:")
        index = int(self.number_chosen.get()) - 1
        # print('index:%d'%index)
        url = tit_list[0][index]
        para = s.pre_download(url)
        self.detail_info["text"] = "本页有" + str(para[0]) + "张图"
        return para

    def get_title_list(self, url):
        '''
        获取标题列表内容
        :param url:
        :return:
        '''
        global tit_list
        tit_list = s.page_one(url)
        self.info["text"] = "\n".join(tit_list[1])

    def get_num_list(self):
        '''
        获取数值列表
        :return:
        '''
        num = []
        for i in range(1, 25):
            num.append(str(i))
        num_str = "\n".join(num)
        return num_str

    def set_top_bg(self, id):
        '''

        :param id: id 是按钮摆放的位置,int类型的
        :return:
        '''
        # 还原现场
        for i in self.button_list:
            i['background'] = 'skyblue'

        self.button_list[id - 1]['background'] = 'pink'
        # for i in
        #     if curr == i:
        #         i['bg']=='gray'
        #     else:
        #         i['bg']==''
        pass

    def update_page_url(self, option, reg_url):
        if option:
            if option == 2:
                print('下一页')
                if self.curr_page < self.page_max:
                    self.curr_page += 1
            elif option == 1:
                print('上一页')
                if self.curr_page > 1:
                    self.curr_page -= 1
            elif option == 3:
                self.curr_page = int(self.page_chosen.get())
        if reg_url:
            # TODO 设置更新按钮的背景颜色
            # 调用set_button_color
            # 重置页面数
            self.curr_page = 1
            self.curr_url = reg_url
        if self.curr_page == 1:
            url = self.curr_url
        else:
            url = self.curr_url + 'page/' + str(self.curr_page) + '/'
        print(self.curr_page)
        self.page_info['text'] = '当前页数:' + str(self.curr_page)
        self.get_title_list(url)

    def top_menu(self, topp):
        '''
        用于绘制顶部菜单
        :param topp:
        :return:
        '''
        self.button_list = []
        # 菜单栏
        url_list = {
            '推荐': 'https://www.mzitu.com/',
            '性感': 'https://www.mzitu.com/xinggan/',
            '日本': 'https://www.mzitu.com/japan/',
            '台湾': 'https://www.mzitu.com/taiwan/',
            '清纯': 'https://www.mzitu.com/mm/'
        }
        # update_page_url函数是用来更新页面的内容以及后面要下载的url的
        menu = Button(topp, text='', font=("Arial", 12), width=1)
        menu.grid(row=0, column=0)

        def put_button(key, col):
            '''
            用于画出按钮组件
            :param contain:按钮显示的文本内容
            :param key: 命令执行的函数选择的键
            :param col: 按钮放置的列数
            :return:
            '''
            # self.curr_button = StringVar()
            # TODO 怎么解决一个command 执行两个函数的问题
            # 这里用is机制的占了个位置,让两个函数都执行,随便返回点啥,我都不要,哈哈哈哈哈
            # 之前尝试过用函数的参数传递,但是有点不太好管理
            # 后来用的+号,程序报错,虽然界面中看不出来,但是我还是有点强迫症的让他不报错
            self.menu = Button(topp, text=key, font=("Arial", 12), width=7, \
                               command=lambda: self.update_page_url(option=0, reg_url=url_list[key]) is \
                                               self.set_top_bg(col))

            self.menu.grid(row=0, column=col)
            self.button_list.append(self.menu)
            for i in self.button_list:
                i['background'] = 'skyblue'
            self.button_list[0]['background'] = 'pink'
            # if key == self.curr_button:
            #     menu['background'] = 'gray'

        i = 1
        for contain in url_list.keys():
            put_button(contain, i)
            i += 1
        #

        # 前进和后退,进行页数的更改
        # option为标记位,0为不改变

        # 顶部的显示当前页数的lable
        # 定义成类属性,以便于在Spider类中更改其值
        self.page_info = Label(topp, text='', justify="left", \
                               font=("Arial", 12), width=10)
        self.page_info.grid(row=0, column=6)

        self.page_info["text"] = '当前页数:1'

    def main_content(self, num_str):
        '''
        主要内容界面,包括数字列表的显示,标题列表的显示以及右边输入框和下载按钮部分
        :param num_str:数字列表显示内容
        :return:
        '''

        # 左边的序号栏
        one = Label(self.cont, text=num_str, font=("Arial", 12), relief='ridge')
        one.grid(row=1, column=0)
        # 中间的主要信息栏
        '''
        relief(可选值为：flat(默认),sunken,raised,groove,ridge)，borderwidth(边框的宽度，单位是像素，默认根据系统而定，一般是1或2像素)
        '''
        self.info = Label(self.cont, text='info', justify="left", \
                          font=("Arial", 12), width=49, relief='ridge')
        self.info.grid(row=1, column=1, columnspan=6)
        # 右边的选择栏
        # 上面的提升lable
        ttk.Label(self.indo, text="\n\n\n选择一个", font=("Arial", 12)).grid(column=0, row=4, columnspan=2)
        # 添加一个标签，并将其列设置为1，行设置为0
        # 中间的下拉框
        number = StringVar()
        # 这里直接定义成为类的属性,以便于其他方法中直接获取其选择的页数
        self.number_chosen = ttk.Combobox(self.indo, width=12, textvariable=number)
        self.number_chosen['values'] = tuple(range(1, 25))  # 设置下拉列表的值
        self.number_chosen.grid(column=0, row=5, columnspan=2)  # 设置其在界面中出现的位置 column代表列 row 代表行
        self.number_chosen.current(0)  # 设置下拉列表默认显示的值，0为 numberChosen['values'] 的下标值

        # 由于进行了类的封装,所以不需要借用列表的穿透性了
        # 直接定义一个类的成员属性即可传递到类中的任何位置
        # 这里实时更新当前选中的数字内容,以便于按下下载按钮时能够定位到准确的页面
        # TODO 可以优化到其他位置,减少功能模块之间的耦合性
        # self.user_choose_num = self.number_chosen.get()

        # 点击查询按钮
        btn4 = Button(self.indo, text="查询图片个数", font=("Arial", 12), background='gray',
                      command=lambda: self.thread_it(self.search))
        btn4.grid(column=0, row=6, columnspan=2)

        # 外加的详细信息栏
        # 这里直接定义成为类的属性,以便于其他方法中直接修改其内容
        self.detail_info = Label(self.indo, text='', justify="left", \
                                 font=("Arial", 12), width=10)
        self.detail_info.grid(row=7, column=0, columnspan=2)
        # 点击下载的按钮
        self.btn5 = Button(self.indo, text="下载此页图片", font=("Arial", 12), background='gray',
                           command=lambda: self.thread_it(self.download))
        self.btn5.grid(column=0, row=12, columnspan=2)

        # 外加的详细下载信息栏
        # 定义成类属性,以便于在Spider类中更改其值
        Tk_gui.terminal_info = Label(self.stat, text='', justify="left", \
                                     font=("Arial", 12))
        Tk_gui.terminal_info.grid(row=0, column=0)

        Tk_gui.terminal_info["text"] = ''

        menu = Button(self.indo, text=" 上一页", font=("Arial", 12), background='gray',
                      command=lambda: self.thread_it(lambda: self.update_page_url(option=1, reg_url='')))
        menu.grid(row=0, column=0)

        menu = Button(self.indo, text="下一页 ", font=("Arial", 12), background='gray',
                      command=lambda: self.thread_it(lambda: self.update_page_url(option=2, reg_url='')))
        menu.grid(row=0, column=1)

        # 添加一个标签，并将其列设置为1，行设置为0
        # 中间的下拉框
        page = StringVar()
        # 这里直接定义成为类的属性,以便于其他方法中直接获取其选择的页数
        self.page_chosen = ttk.Combobox(self.indo, width=12, textvariable=page)
        self.page_chosen['values'] = tuple(range(1, self.page_max + 1))  # 设置下拉列表的值
        # 设置其在界面中出现的位置 column代表列 row 代表行
        self.page_chosen.grid(row=2, column=0, columnspan=2)
        # 设置下拉列表默认显示的值，0为 numberChosen['values'] 的下标值
        self.page_chosen.current(0)

        menu = Button(self.indo, text=" 跳转到此页 ", font=("Arial", 12), background='gray',
                      command=lambda: self.update_page_url(option=3, reg_url=''))
        menu.grid(row=3, column=0, columnspan=2)

        # 用于指定下载路径
        Tk_gui.path = StringVar()
        #
        Label(self.indo, text="目标路径:", font=("Arial", 12)). \
            grid(row=9, column=0, columnspan=2)
        Entry(self.indo, textvariable=self.path, width=15). \
            grid(row=10, column=0, columnspan=2)
        Button(self.indo, text="更改下载路径", font=("Arial", 12), background='gray', command=self.get_save_path). \
            grid(row=11, column=0, columnspan=2)

        # 初始化保存路径
        Tk_gui.path.set(path.dirname(__file__))

    def stat_info(self):
        # 外加的详细下载信息栏
        # 定义成类属性,以便于在Spider类中更改其值
        Tk_gui.stat_info = Label(self.stat, text='', justify="left", \
                                 font=("Arial", 12))
        Tk_gui.stat_info.grid(row=0, column=0)

        Tk_gui.stat_info["text"] = ''


class Spider():

    def pre_download(self, meizi_url):
        self.headers = {
            'Referer': 'https://www.mzitu.com',
            'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36'
        }
        # print(self.meizi_url)
        meizi_html = get(meizi_url, headers=self.headers).text
        end_url = findall("<span>(\d+?)</span></a><a href='https://www.mzitu.com/\d*?/2'><span>下一页&raquo", meizi_html)
        name_id = search('<h2 class="main-title">(.*?)</h2>', meizi_html).group(1)
        name = sub('!', '', name_id)
        print("本页的总数:")
        end_url = int(end_url[0])
        print(end_url)
        return end_url, name, meizi_url

    def ori_video(self, end_url, name, meizi_url):
        # 获取用户选择的路径
        choose_dir = Tk_gui.path.get()
        # print('选择的路径：', choose_dir)
        # 判断文件夹是否存在
        # print('lsitdir', listdir(choose_dir))
        # name = choose_dir + '/' + name

        curr_dir = choose_dir + '/' + name
        for x in range(1, end_url + 1):
            # 更新详情信息的内容
            Tk_gui.terminal_info["text"] = \
                '正在下载图片...\t' + '当前进度:' + str(x) + ' / ' + str(end_url)

            if name not in listdir(choose_dir):
                mkdir(curr_dir)
                Tk_gui.terminal_info["text"] = '创建文件夹:' + curr_dir
            self.single(x, name, meizi_url, curr_dir)
        Tk_gui.terminal_info["text"] = '图片下载完成,成功保存到' + curr_dir[0:25] + '...'

    def single(self, x, name, meizi_url, curr_dir):
        newurl = meizi_url + '/' + str(x)

        html = get(newurl, headers=self.headers).text
        print(html)
        end_re = findall(r'<div class="main-image"><p><a href=".+?" ><img class="blur" src="(.*?)"', html)
        print("end_re>>>",end_re)

        # urlretrieve(end_re[0],path+'/'+ str(x)) 不能加请求头
        req = Request(end_re[0], headers=self.headers)
        response = urlopen(req)
        fname = end_re[0].split('/')[-1]
        print('正在下载: ', fname)

        # 文件夹名字前面加上所选择的路径

        with open(curr_dir + '/' + fname, 'wb') as f:
            f.write(response.read())
        ''' 反反爬  设置时间间隔 防止服务器封锁IP或禁止访问'''
        # sleep(1)

    def page_one(self, url):
        '''
        # 下载一页的内容
        :param url:
        :return:
        '''
        # url = 'https://www.mzitu.com/'
        # url = 'https://www.mzitu.com/page/2/'
        headers = {
            'Referer': 'https://www.mzitu.com',
            'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36'
        }
        html = get(url, headers=headers).text
        # print(html)
        ret = findall('<li><a href="(.*?)" target="_blank"><img class=', html)
        tit = findall("<li><a.*?alt=\'(.*?)\'", html)
        return ret, tit


# 实例化对象
s = Spider()
t = Tk_gui()
```

## 打包exe
> 可以用pyinstaller 打包成exe ,这样就可以脱离python环境运行了
>


## 图片展示
![](QQ截图20210312233035.png)
### 日志中可以显示当前进度
![](QQ截图20210312232813.png)
### 你会看着文件夹中图片变多
![](QQ截图20210312233012.png)
![](QQ截图20210312233229.png)

### 还可以选择翻页

![](QQ截图20210312233253.png)


## 源
exe下载路径: [meizi_spider.exe](https://gitee.com/victorfengming/python_projects/blob/master/meizi_spider/meizi_spider7.1.exe)