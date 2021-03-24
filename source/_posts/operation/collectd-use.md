---
title: "collectd+graphite使用"
date: 2021-03-24 19:46:24
cover: "/img/lynk/27.jpg"
tags:
---

## collectd和graphite是用来做什么的

- collectd: 是一个守护(daemon)进程，用来收集系统性能和提供各种存储方式来存储不同值的机制。比如基本的系统性能的收集（CPU、memory、process等）
- graphite：是一个企业级的监控工具，可以在廉价机硬件上运行；Graphite仅是一个画图工具，不主动地收集数据，而是将接收到的数据以图形的方式展现出来。

 这里结合collectd和graphite，collectd用于收集数据，graphite以图表的形式显示数据 

### collect安装

- 安装collectd-5.5.0.tar.gz，这个是目前最新版本，对java等支持非常好
- 在root@10.175.180.180这台机：
  - 安装包在/tmp目录下，将其解压安装
  - 安装完在/etc目录下有份collectd.conf配置文件，在其中配置需要的即可
  - 启动命令：service collectd restart/start

 install process: 

1. Install prereqs

```
yum -y install libcurl libcurl-devel rrdtool rrdtool-devel rrdtool-prel libgcrypt-devel gcc make gcc-c++
```

2.  Get Collectd, untar it, make it and install 

```bash
wget http://collectd.org/files/collectd-5.5.0.tar.gz

tar zxvf collectd-5.5.0.tar.gz

cd collectd-5.5.0

./configure --prefix=/usr --sysconfdir=/etc --localstatedir=/var --libdir=/usr/lib --mandir=/usr/share/man --enable-all-plugins

make

make install
```

   

3. Copy the default init.d script 

```bash
cp /tmp/collectd-5.4.0/contrib/redhat/init.d-collectd /etc/init.d/collectd
```

   

4.  Set the correct permissions 

```bash
chmod +x /etc/init.d/collectd
```

   

5. Start the deamon

```
service collectd start
```

 Note:If cannot tar the `collectd-5.5.0.tar.gz`, you should upload it. 

### graphite安装

这里不介绍graphite的安装，本人没有安装graphite，在配置的Linux上已经安装好了graphite，就不误导大家了。推荐大家浏览

 http://my.oschina.net/fufangchun/blog/232895?p=1 

 这里有详细的原理、安装等说明 

### collectd.conf基本配置

```bash
###########################################################
##############################################################################
# Global                                                                     #
#----------------------------------------------------------------------------#
# Global settings for the daemon.                                            #
##############################################################################

Hostname    "localhost"
#FQDNLookup   true
#BaseDir     "/var/lib/collectd"
#PIDFile     "/var/run/collectd.pid"
#PluginDir   "/usr/lib/collectd"
#TypesDB     "/usr/share/collectd/types.db"
```

```bash
#----------------------------------------------------------------------------#
# Interval at which to query values. This may be overwritten on a per-plugin #
# base by using the 'Interval' option of the LoadPlugin block:               #
#   <LoadPlugin foo>                                                         #
#       Interval 60                                                          #
#   </LoadPlugin>                                                            #
#----------------------------------------------------------------------------#

<LoadPlugin write_graphite>
  Interval 5
</LoadPlugin>

Interval     10
Timeout      2
ReadThreads  5
WriteThreads 5
```

```bash
##############################################################################
# Logging                                                                    #
#----------------------------------------------------------------------------#
# Plugins which provide logging functions should be loaded first, so log     #
# messages generated when loading or configuring other plugins can be        #
# accessed.                                                                  #
##############################################################################

LoadPlugin syslog
LoadPlugin logfile

<Plugin logfile>
LogLevel info
File STDOUT
Timestamp true
PrintSeverity false
</Plugin>

<Plugin syslog>
LogLevel info
</Plugin>
```

```bash
##############################################################################
# LoadPlugin section                                                         #
#----------------------------------------------------------------------------#
# Lines beginning with a single `#' belong to plugins which have been built  #
# but are disabled by default.                                               #
#                                                                            #
# Lines begnning with `##' belong to plugins which have not been built due   #
# to missing dependencies or because they have been deactivated explicitly.  #
##############################################################################

LoadPlugin cpu
LoadPlugin interface
LoadPlugin memory
LoadPlugin processes
LoadPlugin users
LoadPlugin disk
LoadPlugin java
LoadPlugin write_graphite
```



```bash
##############################################################################
# Plugin configuration                                                       #
#----------------------------------------------------------------------------#
# In this section configuration stubs for each plugin are provided. A desc-  #
# ription of those options is available in the collectd.conf(5) manual page. #
##############################################################################

<Plugin disk>
        Disk "/^[vhs]d[a-f][0-9]?$/"
        IgnoreSelected false
</Plugin>

<Plugin interface>
        Interface "eth0"
        IgnoreSelected false
</Plugin>

<Plugin  write_graphite>
    <Node "graphing">
        Host "localhost"
        Port "2003"
        Protocol "tcp"
        LogSendErrors true
        Prefix "collectd."
        StoreRates true
        AlwaysAppendDS false
        EscapeCharacter "_"
    </Node>
</Plugin>
```

### graphite显示的结果

 ![这里写图片描述](20160113172857144) 