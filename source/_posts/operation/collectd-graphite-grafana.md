---
title: collectd+Graphite+Grafana搭建网络质量监控系统
date: 2021-03-24 15:55:17
cover: "/img/lynk/92.jpg"
tags:
    - collectd
    - graphite
    - grpfana
---



这是一篇发表已超过三年的旧文，文中的信息可能已经有所发展或是发生改变。

前段时间[入手一台 Gen8 服务器](https://wzyboy.im/post/1070.html)，主要用来做网络存储。光做网络存储显然太浪费了，感谢 ESXi，一机多用很方便。本文介绍如何在家庭服务器上搭建简单好用的网络质量监控系统。

## 一、选材

说到网络质量监控，大部分人会想到著名的 [SmokePing](http://oss.oetiker.ch/smokeping/)。SmokePing 的确是经典工具，但未免老旧，配置也略复杂。本文使用 [collectd](https://collectd.org/) 作为收集工具，[Graphite](http://graphite.readthedocs.org/) 作为存储工具，[Grafana](http://docs.grafana.org/) 作为展示工具。这些工具符合「专做一件事情并把这件事情做好」的 Unix 哲学，配置灵活、功能强大。

整体结构是这样的：

![asciiflow-collectd-graphite-grafana-2](asciiflow-collectd-graphite-grafana-2.png)

## 二、收集：collectd

正如其名字所暗示的那样，collectd 是一个收集系统各项指标的进程。它自带很多插件，也可以通过自定义插件和数据类型的方式增加更多的收集项。网络质量监控主要用到其中的 [ping 插件](https://collectd.org/wiki/index.php/Plugin:Ping)，该插件依赖 [Liboping](http://noping.cc/) 这个库。这两个项目在主流 GNU/Linux 发行版中都有打包。

使用你最喜爱的包管理器安装 collectd 和 liboping 之后，使用你最喜爱的编辑器打开 `/etc/collectd.conf` 文件。这是一个带有详尽注释的超长配置文件，要让 ping 插件工作，以下是一份示例配置：

```
Hostname "your-hostname"
FQDNLookup false

LoadPlugin ping
LoadPlugin write_graphite

<Plugin ping>
  Host "8.8.8.8"
  Host "8.8.4.4"
  Interval 1.0
  Timeout 0.9
</Plugin>

<Plugin write_graphite>
  <Node "localhost">
    Host "localhost"
    Port "2003"
    Protocol "tcp"
    LogSendErrors true
  </Node>
</Plugin>
```

意义很明确，声明自己的主机名（用于上报数据），加载 ping 和 write_graphite 插件，然后配置这两个插件。

ping 插件的配置项中，Host 用于添加需要被监控的目标，一行一个，`Interval` 和 `Timeout` 则分别指定多久 ping 一次，以及多久没收到回包认为是超时。如有特殊需求，还可以指定 `SourceAddress`, `Device` 等参数指定从哪个网络设备发出 ICMP 包。注意，这里 `Interval` 不是指多久上报一次，而是指多久 ping 一次，上报的话还是按全局的来（默认 10 秒），上报时的数据是这段时间 RTT 的算术平均数。

write_graphite 插件的配置项中，填写 carbon-cache.py 监听的地址和端口。本例中跑 collectd 的机器同时也跑了 carbon-cache.py，因此填 localhost 即可。如果它们不在同一台机器上（比如 collectd 跑在路由器上，carbon-cache.py 跑在配置更高的设备上），则需要填写相应的地址。

collectd 发出去的数据是很简单的 TCP 消息，如：

```
foo.bar.baz 123 1458372405
```

以空格分隔，第一段是指标名字，第二段是数值，第三段是时间戳。

改好配置之后保存。因为现在 carbon-cache.py 还没有运行，因此还不能启动 collectd。

## 三、接收、存储和查询：carbon-cache.py 和 graphite-api

Graphite 是一个较大项目，它的主要组件有：

- [Carbon](https://github.com/graphite-project/carbon)。包括 carbon-cache.py, carbon-relay.py 等，用于接收数据点；
- [Whisper](https://github.com/graphite-project/whisper)。数据点存储格式，Carbon 用它把数据点写入磁盘；
- Graphite Web。基于 Django 的网页应用，既提供查询数据点的 API，也提供一个展示用的网页。

由于 Graphite Web 较为臃肿而功能比较弱，因此这里不使用它，而是使用 [Graphite-API](https://github.com/brutasse/graphite-api) 这个第三方项目提供查询 API，用漂亮的 Grafana 提供展示页面。

Carbon 可以直接从 PyPI 安装，注意它只支持 Legacy Python。它是纯 Python 的，没有其他依赖，使用 `pip2 install carbon` 即可轻松安装。

Carbon 使用 Whisper 存储数据点，这一格式的文件大小是预分配的，并且是固定的。旧的数据可以设置自动降低精度，非常旧的数据可以设置丢弃。在 `storage-schemas.conf` 中可以这么设置：

```
[ping]
pattern = \.ping\.
retentions = 10s:1d,1m:30d,5m:180d,30m:1y

[default]
pattern = .*
retentions = 1m:1d,5m:30d,30m:180d,1h:1y
```

其中 pattern 匹配指标的名字，retentions 指定这个指标应该保留多久。以 `[default]` 为例，这个指标的数据，1 分钟精度的会保留 1 天，之后自动降为 5 分钟精度，保留 30 天，之后自动降为 30 分钟精度，保留 180 天，之后自动降为 1 小时精度，保留 1 年。而对于 `[ping]` 一节的数据，我希望能更精确一些，因此 1 天内的数据是 10 秒精度的。这样的设置可以使不同的指标按需自动降低精度以节省存储空间，既能查到近期的高精度数据，也能反观远期的大致趋势。

注意这些政策仅对新创建的 `.wsp` 文件有效，已有的文件的存储策略需要通过 whisper-resize.py 进行更改。
Graphite-API 因为带有非 Python 的图形库依赖，编译安装时较为麻烦。Ubuntu / Debian 用户可以用官方提供的 [.deb](https://github.com/brutasse/graphite-api/releases) 安装。Arch Linux 用户可以使用我打包的 [aur/graphite-api](https://aur.archlinux.org/packages/graphite-api/) 安装。

安装之后打开 `graphite-api.yaml` 文件。根据安装方式的不同，Carbon 和 Graphite-API 的存储路径、配置文件路径会有一些差别，请按照自己的情况将 whisper – directories 一节的路径填写正确。

另外推荐配置 carbonlink，查询那些在 carbon-cache.py 内存中还未写入磁盘的数据。最终我使用的 `graphite-api.yaml` 内容如下：

```
finders:
  - graphite_api.finders.whisper.WhisperFinder
whisper:
  directories:
    - /var/lib/carbon/whisper
carbon:
  hosts:
    - 127.0.0.1:7002
  timeout: 1
  retry_delay: 15
  carbon_prefix: carbon
  replication_factor: 1
```

配置完成后，可以启动 carbon-cache.py 和 graphite-api。上节配置的 collectd 也可以启动了。

## 四、展示：grafana-server

Grafana 是一个功能强大的图表绘制服务器，支持 Graphite, InfluxDB, OpenTSDB 等多种后端，支持多种图表绘制，几乎无外部依赖。

Grafana 由 Go 和 Node.js 写成，编译结果是一个单文件 Go 程序和一堆 HTML + CSS + JavaScript。官方提供了 [.deb](http://docs.grafana.org/installation/debian/) 和 [.rpm](http://docs.grafana.org/installation/rpm/) 可供安装。我在 Arch Linux 上安装的时候，本来直接用的 aur/grafana，后来发现 go get 和 npm install 的过程简直蛋疼，于是将官方提供的 [.tar.gz](http://grafana.org/download/) 二进制包做了一份 [aur/grafana-bin](https://aur.archlinux.org/packages/grafana-bin/)，直接装这个就省力多了。

安装之后启动服务，在浏览器中打开 :3000 端口，即可用 admin / admin 登录。在 `grafana.ini` 中也可以开启匿名登录。

登录后需要先添加数据源（data source），将 graphite-api 的地址和端口（默认是 8888）填写进去即可。

然后便可以开始画图了，通过简单的网页操作即可添加各种不同类型的图表，也可以方便地选用 Graphite 内置的各种函数。Grafana 的具体操作可以从[官方文档](http://docs.grafana.org/guides/gettingstarted/)了解到，这里不再赘述。

以下是我用 Grafana 绘制的网络质量监控的页面，其中用到 [Templating](http://docs.grafana.org/reference/templating/)、[Singlestat Panel](http://docs.grafana.org/reference/singlestat/) 等功能：

![](grafana-dashboard-network-fullscreen-20160319-2-blurred.png)


请原谅那一段 100% 丢包率的部分，是我的一台 VPS 所在的机房出了问题……

## 五、监控更多的指标

collectd 还可以做[很多事情](https://collectd.org/wiki/index.php/Table_of_Plugins)，只用它的 ping 插件太大材小用了。玩熟了 ping 插件之后，我又用它监控了局域网内各机器（自己的笔记本、Gen8 上运行的其他虚拟机等）的 CPU、内存、磁盘、网络等其他指标。collectd 的客户端也是移植性很强，我甚至在 Raspberry Pi 上也部署了一下。Windows 机器的话，则可以安装 [SSC Serv](https://collectd.org/wiki/index.php/SSC_Serv)，这是一个协议兼容的 collectd agent，免费版本有五分钟上报一次的限制，基本够用了。


by wzyboy on 2016-03-21