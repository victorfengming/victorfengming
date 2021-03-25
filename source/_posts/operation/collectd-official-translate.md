---
title: collectd官方教程翻译
date: 2021-03-25 15:55:17
cover: "/img/lynk/11.jpg"
author: "victor"
tags:
    - collectd
---



[官方文档地址](https://collectd.org/wiki/index.php/First_steps)



## 1.下载官方压缩包

1. 你可以通过,[官方地址](https://collectd.org/download.shtml) 下载

2. 也可以通过命令下载

```bash
cd /tmp/
wget http://collectd.org/files/collectd-x.y.z.tar.bz2
tar jxf collectd-x.y.z.tar.bz2
cd collectd-x.y.z
```


## 2.现在用常规配置来配置源文件

```bash
./configure 
```

完成`configure`脚本后，它会显示它找到(和没有找到)的库的摘要，以及哪些插件已经启用。

默认情况下，满足依赖关系的所有插件都是启用的。如果您想使用的插件缺失，请安装所需的开发包并再次运行`configure`。

最后但并非最不重要的:编译并安装程序。默认情况下，它将安装到`/opt/collectd`。如果您更喜欢另一个目录，可以使用`——prefix`选项调用configure脚本。

```bash
make all install
cd /opt/collectd/
```

## 配置

配置文件在`/etc/collectd.conf`中。`</prefix>`手册页[collectd.conf](http://collectd.org/documentation/manpages/collectd.conf.5.shtml)。打开文件并特别注意`LoadPlugin`行。

```bash
vim etc/collectd.conf
```