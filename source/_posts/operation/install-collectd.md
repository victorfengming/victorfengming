---
title: 如何安装和配置“Collectd”和“Collectd-Web”以监控Linux中的服务器资源
date: 2021-03-24 19:46:24
cover: "/img/lynk/77.jpg"
tags:
---

![img](workbench.jpg) 



## 如何安装和配置“Collectd”和“Collectd-Web”以监控Linux中的服务器资源

本教程将介绍在RHEL / CentOS / Fedora和基于Ubuntu / Debian的系统上的Collectd和Collectd-web界面的安装过程，

分类:[监控工具](https://www.howtoing.com/category/monitoring-tools)[开发工具](https://www.howtoing.com/category/developer-kits)

 *2015-06-30 00:00:00*

**Collectd的Web**是基于RRDtool的**（R** ound- **- [R** **obinÐatabase** **工具），**它解释和图形输出，通过在Linux系统上**Collectd**服务收集的数据的Web前端监控工具。

**Collectd**服务需要在默认情况下可用插件的巨大集合到其默认的配置文件，其中一些被默认情况下，已激活，一旦你已经安装了软件包。

**Collectd卷材CGI**脚本它解释，并生成图形html页面统计数据可以由**Apache CGI**网关以最小的Apache Web服务器侧需要配置简单地执行。

然而，随着生成的统计图形Web界面可以，还可以通过自带预装与主**Git**仓库被**Python**脚本**CGIHTTPServer**提供的独立的Web服务器执行。

本教程将介绍**Collectd**服务和**Collectd-Web**界面**RHEL / CentOS的/ Fedora**和**Ubuntu / Debian的**基于系统的需要的，以便运行服务，并启用**Collectd**服务插件做的最小配置的安装过程。

请通过**collectd**系列的以下文章。

**第1部分** ： **安装和配置“Collectd'和'Collectd的Web”监视Linux的资源**

**第2部分** ： [监控Linux的资源与Collectd的Web和Apache CGI](https://www.howtoing.com/monitor-linux-server-resources-with-collectd-web-and-apache-cgi/)

**第3部分** ： [配置Collectd作为中央监控服务器的客户端](https://www.howtoing.com/configure-collectd-as-central-monitoring-server-for-clients/)

### 第1步： - 安装Collectd服务

**1.**基本上**，Collectd**守护任务是收集和存储数据的统计，它运行在系统上。 该**Collectd**包可以下载并安装由发出以下命令的默认基于Debian发行库：

##### 在Ubuntu / Debian

```
# apt-get install collectd			[On Debian based Systems]
```

[![在Ubuntu上安装Collectd](Install-Collectd-on-Ubuntu-568x450.png)](https://www.howtoing.com/wp-content/uploads/2015/04/Install-Collectd-on-Ubuntu-568x450.png)

在Debian / Ubuntu上安装Collectd

##### 在RHEL / CentOS 6.x / 5.x上

像**CentOS的/ Fedora的**旧的基于**RedHat**系统**中** ，你首先需要[启用EPEL软件库](https://www.howtoing.com/how-to-enable-epel-repository-for-rhel-centos-6-5/)系统下，那么你就可以能够从EPEL软件库安装**collectd**包。

```
# yum install collectd
```

##### 在RHEL / CentOS 7.x上

在最新版本的RHEL / CentOS 7.x上，您可以从默认yum repo安装和启用epel存储库，如下所示。

```
# yum install epel-release
# yum install collectd
```

[![在CentOS上安装Collectd](Install-Collectd-on-CentOS-620x344.png)](https://www.howtoing.com/wp-content/uploads/2015/04/Install-Collectd-on-CentOS-620x344.png)

在CentOS / RHEL / Fedora上安装Collectd

**注意：**对于Fedora用户，无需启用任何第三方的仓库，简单yum来获得默认的yum仓库的collectd包。

**2.**一旦软件包安装在系统上，以启动该服务运行以下命令。

```
# service collectd start			[On Debian based Systems]
# service collectd start                        [On RHEL/CentOS 6.x/5.x Systems]
# systemctl start collectd.service              [On RHEL/CentOS 7.x Systems]
```

### 第2步：安装Collectd-Web和依赖关系

**3.**开始导入**Collectd的Web** Git仓库之前，首先需要保证**的Git**软件包及以下所需的相关计算机上安装：

```
----------------- On Debian / Ubuntu systems -----------------
# apt-get install git
# apt-get install librrds-perl libjson-perl libhtml-parser-perl
```

[![在Ubuntu上安装Git](Install-Git-on-Ubuntu-620x242.png)](https://www.howtoing.com/wp-content/uploads/2015/04/Install-Git-on-Ubuntu-620x242.png)

在Debian / Ubuntu上安装Git

```
----------------- On RedHat/CentOS/Fedora based systems -----------------
# yum install git
# yum install rrdtool rrdtool-devel rrdtool-perl perl-HTML-Parser perl-JSON
```

[![在CentOS上安装Git](Install-Git-on-CentOS-620x344.png)](https://www.howtoing.com/wp-content/uploads/2015/04/Install-Git-on-CentOS-620x344.png)

安装Git和依赖关系

### 第3步：导入Collectd-Web Git存储库并修改独立的Python服务器

**4.**在下一步选择和更改目录从Linux树层次结构要导入Git项目（可以使用系统路径`/usr/local/`路径），然后运行下面的命令来克隆**Collectd的Web** git仓库：

```
# cd /usr/local/
# git clone https://github.com/httpdss/collectd-web.git
```

[![Git Clone Collectd-Web](Clone-Collectd-Web-620x344.png)](https://www.howtoing.com/wp-content/uploads/2015/04/Clone-Collectd-Web-620x344.png)

Git Clone Collectd-Web

**5.**一旦Git仓库导入到系统中，继续前进，进入**collectd-web**目录**，**并以确定的Python服务器脚本（列出其内容`runserver.py` ），这将在下一步进行修改。 此外，添加执行权限下列CGI脚本： `graphdefs.cgi` 。

```
# cd collectd-web/
# ls
# chmod +x cgi-bin/graphdefs.cgi
```

[![设置执行权限](Set-Execute-Permission-620x344.png)](https://www.howtoing.com/wp-content/uploads/2015/04/Set-Execute-Permission-620x344.png)

设置执行权限

**6.** **Collectd的Web**独立的Python服务器脚本默认配置来运行和约束只在**环回地址（127.0.0.1）。**

为了从远程浏览器访问**Collectd的Web**界面，您需要编辑`runserver.py`脚本并更改**127.0.1.1 IP**地址为**0.0.0.0，**以绑定所有网络接口IP地址。



如果要仅在特定接口上绑定，则使用该接口IP地址（不建议使用此选项，以防您的网络接口地址由DHCP服务器动态分配）。 使用下面的截图作为最后如何摘录`runserver.py`脚本应该是这样的：

```
# nano runserver.py
```

[![配置Collect-Web](Configure-Collect-web-620x361.png)](https://www.howtoing.com/wp-content/uploads/2015/04/Configure-Collect-web-620x361.png)

配置Collect-web

如果你想使用其他网络端口超过**8888，**修改端口变量的值。

### 第4步：运行Python CGI独立服务器并浏览Collectd-web界面

**7.**当你修改了独立的Python脚本，服务器IP地址绑定，继续前进并发出以下命令来启动服务器在后台：

```
# ./runserver.py &
```

可选，作为一种替代方法，您可以调用Python解释器启动服务器：

```
# python runserver.py &
```

[![启动Collect-Web服务器](Start-Collect-Web-620x344.png)](https://www.howtoing.com/wp-content/uploads/2015/04/Start-Collect-Web-620x344.png)

启动Collect-Web服务器