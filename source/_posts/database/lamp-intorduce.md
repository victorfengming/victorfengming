---
title: "关于LAMP架构的简单介绍"
date:       2019-09-26
tags:
	- Linux
	- deepin
	- php
	- database
	- mysql
---

<div class="htmledit_views" id="content_views">
                                            <p><img alt="" class="has" height="258" src="https://img-blog.csdnimg.cn/20181119082239314.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3NqMzQ5NzgxNDc4,size_16,color_FFFFFF,t_70" width="657"></p>

<p><span style="color:#3399ea;"><strong>一、LAMP架构介绍</strong></span></p>

<p><strong>&nbsp;&nbsp;&nbsp;</strong>现如今打开浏览器，搜索LAMP关键词，出现大量的关于LAMP的介绍，包括LAMP的一键脚本、LAMP的yum安装、LAMP的编译安装，但是对于一个非开发或非专业人员有可能根据网络参考资源实现LAMP的搭建并成功运行各种服务，也有部分人员完全照搬某些博客知识进行搭建，最后以失败告终，因此抱怨互联网资源不够成熟，其实根本原因并非如此，主要原因如下：</p>

<ul><li>
    <p>初学者对LAMP架构原理不熟悉</p>
    </li>
    <li>
    <p>初学者实验时所用系统和软件版本和某些博客资源并不相同</p>
    </li>
</ul><p>因此导致大量初学者以失败告终,其实只有了解并掌握LAMP的工作原理才能轻松的搭建成功，其次参数的配置都是次要因素，因为互联网上拥有大量的参考资料供查询，下面将逐一介绍</p>

<p><span style="color:#f33b45;"><strong>&nbsp;&nbsp;&nbsp;</strong>L：很显然L代表Linux系统，但此L需注意系统的版本号，如Centos6.9或Centos7.3；</span></p>

<p><span style="color:#f33b45;">&nbsp;&nbsp; A：表示apache，在传统行业中，多数采用Apache服务器，因此也很有必要了解学习Apache；</span></p>

<p><span style="color:#f33b45;">&nbsp;&nbsp; M：表示数据库，多数采用mysql或mariadb，作为专业的数据库工程师需经多年的历练；</span></p>

<p><span style="color:#f33b45;">&nbsp;&nbsp; P：表示PHP、python、perl等等编程语言。</span></p>

<p>&nbsp;&nbsp; 在这里注意讲解Linux+apache+mariadb+PHP组合的架构，架构图如下：</p>

<p><img alt="" class="has" height="398" src="https://img-blog.csdnimg.cn/20181119082310315.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3NqMzQ5NzgxNDc4,size_16,color_FFFFFF,t_70" width="558"></p>

<p>根据上图中访问数据流可知，处理一次动态页面请求，服务器主要经历：<strong>Apache处理请求——通过CGI接口访问PHP的的应用程序——PHP应用程序调用PHP解释器执行PHP代码——PHP程序访问调用数据库——最后给客户做反馈。</strong></p>

<p>故在LAMP的环境机构中，apache、mariadb和php的主要功能分别如下。</p>

<p><img alt="" class="has" height="456" src="https://img-blog.csdnimg.cn/20181119083215117.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3NqMzQ5NzgxNDc4,size_16,color_FFFFFF,t_70" width="769"></p>

<p>&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:#f33b45;"><strong>apache</strong></span>主要实现如下功能：</p>

<p>&nbsp;&nbsp;&nbsp; 第一：处理http的请求、构建响应报文等自身服务；</p>

<p>&nbsp;&nbsp;&nbsp; 第二：配置让Apache支持PHP程序的响应（通过PHP模块或FPM）；</p>

<p>&nbsp;&nbsp;&nbsp; 第三：配置Apache具体处理php程序的方法，如通过反向代理将php程序交给fcgi处理。</p>

<p>&nbsp;&nbsp;&nbsp;<span style="color:#f33b45;">&nbsp;<strong>mariadb</strong></span>主要实现如下功能：</p>

<p>&nbsp;&nbsp;&nbsp;&nbsp;第一：提供PHP程序对数据的存储；</p>

<p>&nbsp;&nbsp;&nbsp;&nbsp;第二：提供PHP程序对数据的读取(通常情况下从性能的角度考虑，尽量实现数据库的读写分离)。</p>

<p>&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:#f33b45;"><strong>php</strong></span>主要实现如下功能：</p>

<p>&nbsp;&nbsp;&nbsp;&nbsp;第一：提供apache的访问接口，即CGI或Fast CGI(FPM);</p>

<p>&nbsp;&nbsp;&nbsp;&nbsp;第二：提供PHP程序的解释器；</p>

<p>&nbsp;&nbsp;&nbsp;&nbsp;第三：提供mairadb数据库的连接函数的基本环境。</p>

<p>&nbsp;&nbsp;&nbsp;&nbsp;由此可知，要实现LAMP在配置每一个服务时，安装功能需求进行配置，即可实现LAMP的架构，当然apache、mariadb和php服务都可配置为独立服务，安装在不同服务器之上。</p>                                    </div>