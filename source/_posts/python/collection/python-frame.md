---
title: "Python 四大主流 Web 编程框架"
cover: "/img/lynk/5.jpg"
date:       2019-01-12
tags:
	- Python
	- background
	- solution
---

<br>
目前Python的网络编程框架已经多达几十个，逐个学习它们显然不现实。但这些框架在系统架构和运行环境中有很多共通之处，本文带领读者学习基于Python网络框架开发的常用知识,及目前的4种主流Python网络框架：Django、Tornado、Flask、Twisted。

<p>网络框架及MVC架构<br>所谓网络框架是指这样的一组Python包，它能够使开发者专注于网站应用业务逻辑的开发，而无须处理网络应用底层的协议、线程、进程等方面。这样能大大提高开发者的工作效率，同时提高网络应用程序的质量。
</p>
<p>
    在目前Python语言的几十个开发框架中，几乎所有的全栈网络框架都强制或引导开发者使用MVC架构开发Web应用。所谓全栈网络框架，是指除了封装网络和线程操作，还提供HTTP栈、数据库读写管理、HTML模板引擎等一系列功能的网络框架。本文重点讲解的Django、Tornado和Flask是全栈网络框架的典型标杆；而Twisted更专注于网络底层的高性能封装而不提供HTML模板引擎等界面功能，所以不能称之为全栈框架。</p>
<p>MVC（Model-View-Controller）模式最早由Trygve
    Reenskaug在1978年提出，在20世纪80年代是程序语言Smalltalk的一种内部架构。后来MVC被其他语言所借鉴，成为了软件工程中的一种软件架构模式。MVC把Web应用系统分为3个基本部分。</p>
<p>
    模型（Model）：用于封装与应用程序的业务逻辑相关的数据及对数据的处理方法，是Web应用程序中用于处理应用程序的数据逻辑的部分，Model只提供功能性的接口，通过这些接口可以获取Model的所有功能。Model不依赖于View和Controller，它们可以在任何时候调用Model访问数据。有些Model还提供了事件通知机制，为在其上注册过的View或Controller提供实时的数据更新。</p>
<p>视图（View）：负责数据的显示和呈现，View是对用户的直接输出。MVC中的一个Model通常为多个View提供服务。为了获取Model的实时更新数据，View应该尽早地注册到Model中。</p>
<p>
    控制器（Controller）：负责从用户端收集用户的输入，可以看成提供View的反向功能。当用户的输入导致View发生变化时，这种变化必须是通过Model反映给View的。在MVC架构下，Controller一般不能与View直接通信，这样提高了业务数据的一致性，即以Model作为数据中心。</p>
<p>这3个基本部分互相分离，使得在改进和升级界面及用户交互流程时，不需要重写业务逻辑及数据访问代码。MVC架构如图1所示。</p>
<p>MVC架构图</p>
<p>注意：MVC在除Python外的其他语言中也有广泛应用，例如VC++的MFC、Java的Structs及Spring、C#的.NET开发框架，读者应该有深刻的体会。<br>4种Python网络框架：Django、Tornado、Flask、Twisted
</p>
<p>接下来学习当今主流的4种Python网络框架。</p>
<p>企业级开发框架——Django<br>Django于2003年诞生于美国堪萨斯（Kansas）州，最初用来制作在线新闻Web站点，于2005年加入了BSD许可证家族，成为开源网络框架。Django根据比利时的爵士音乐家Django
    Reinhardt命名，作者这样命名Django意味着Django能优雅地演奏（开发）功能丰富的乐曲（Web应用）。</p>
<p>
    它是当前Python世界里最负盛名且最成熟的网络框架。最初用来制作在线新闻的Web站点，目前已发展为应用最广泛的Python网络框架。Django的各模块之间结合得比较紧密，所以在功能强大的同时又是一个相对封闭的系统，但是其健全的在线文档及开发社区，使开发者在遇到问题时能找到解决方法。</p>
<p>Django框架的特点<br>相对于Python的其他Web框架，Django的功能是最完整的，Django定义了服务发布、路由映射、模板编程、数据处理的一整套功能。这也意味着Django模块之间紧密耦合，开发者需要学习Django自己定义的这一整套技术。Django的主要特点如下。
</p>
<p>完善的文档：经过10多年的发展和完善，Django有广泛的应用和完善的在线文档，开发者遇到问题时可以搜索在线文档寻求解决方案。<br>集成数据访问组件：Django的Model层自带数据库ORM组件，使开发者无须学习其他数据库访问技术（dbi、SQLAlchemy等）。<br>强大的URL映射技术：Django使用正则表达式管理URL映射，因此给开发者带来了极高的灵活性。<br>后台管理系统自动生成：开发者只需通过简单的几行配置和代码就可以实现完整的后台数据管理Web控制台。<br>错误信息非常完整：在开发调试过程中如果出现运行异常，则Django可以提供非常完整的错误信息帮助开发者定位问题，比如缺少xxx组件的配置引用等，这样可以使开发者马上改正错误。
</p>
<p>Django的组成结构</p>
<p>Django是遵循MVC架构的Web开发框架，其主要由以下几部分组成。</p>
<p>管理工具（Management）：一套内置的创建站点、迁移数据、维护静态文件的命令工具。<br>模型（Model）：提供数据访问接口和模块，包括数据字段、元数据、数据关系等的定义及操作。<br>视图（View）：Django的视图层封装了HTTP
    Request和Response的一系列操作和数据流，其主要功能包括URL映射机制、绑定模板等。<br>模板（Template）：是一套Django自己的页面渲染模板语言，用若干内置的tags和filters定义页面的生成方式。<br>表单（Form）：通过内置的数据类型和控件生成HTML表单。<br>管理站（Admin）：通过声明需要管理的Model，快速生成后台数据管理网站。
</p>
<p>高并发处理框架——Tornado<br>Tornado是使用Python编写的一个强大的可扩展的Web服务器。它在处理高网络流量时表现得足够强健，却在创建和编写时有着足够的轻量级，并能够被用在大量的应用和工具中。Tornado作为FriendFeed网站的基础框架，于2009年9月10日发布，目前已经获得了很多社区的支持，并且在一系列不同的场合中得到应用。除FriendFeed和Facebook外，还有很多公司在生产上转向Tornado，包括Quora、Turntable.fm、Bit.ly、Hipmunk及MyYearbook等。
</p>
<p>相对于其他Python网络框架，Tornado有如下特点。</p>
<p>完备的Web框架：与Django、Flask等一样，Tornado也提供了URL路由映射、Request上下文、基于模板的页面渲染技术等开发Web应用的必备工具。<br>是一个高效的网络库，性能与Twisted、Gevent等底层Python框架相媲美：提供了异步I/O支持、超时事件处理。这使得Tornado除了可以作为Web应用服务器框架，还可以用来做爬虫应用、物联网关、游戏服务器等后台应用。<br>提供高效HTTPClient：除了服务器端框架，Tornado还提供了基于异步框架的HTTP客户端。<br>提供高效的内部HTTP服务器：虽然其他Python网络框架（Django、Flask）也提供了内部HTTP服务器，但它们的HTTP服务器由于性能原因只能用于测试环境。而Tornado的HTTP服务器与Tornado异步调用紧密结合，可以直接用于生产环境。<br>完备的WebSocket支持：WebSocket是HTML5的一种新标准，实现了浏览器与服务器之间的双向实时通信。<br>因为Tornado的上述特点，Tornado常被用作大型站点的接口服务框架，而不像Django那样着眼于建立完整的大型网站，所以本章着重讲解Tornado的异步及协程编程、身份认证框架、独特的非WSGI部署方式。
</p>
<p>支持快速建站的框架——Flask<br>Flask是Python
    Web框架族里比较年轻的一个，于2010年出现，这使得它吸收了其他框架的优点，并且把自己的主要领域定义在了微小项目上。同时，它是可扩展的，Flask让开发者自己选择用什么数据库插件存储他们的数据。很多功能简单但性能卓越的网站就是基于Flask框架而搭建的，比如<a
            href="https://yq.aliyun.com/go/articleRenderRedirect?url=http%3A%2F%2Fhttpbin.org%2F"
            target="_blank" data-url="http://httpbin.org/">http://httpbin.org/</a>就是一个功能简单但性能强大的HTTP测试项目。Flask是一个面向简单需求和小型应用的微框架。
</p>
<p>相对于其他Python语言的Web框架而言，Flask的特点可以归结如下。</p>
<p>内置开发服务器和调试器<br>网络程序调试是在将编制好的网站投入实际运行前，用手工或编译程序等方法进行测试，修正语法错误和逻辑错误的过程。有经验的开发者都知道，这是保证网站系统能够正式应用的必要步骤。<br>Flask
    自带的开发服务器使开发者在调试程序时无须再安装其他任何网络服务器，比如Tomcat、JBoss、Apache等。Flask默认处于调试状态，使得运行中的任何错误会同时向两个目标发送信息：一个是Python
    Console，即启动Python程序的控制台；另一个是HTTP客户端，即Flask开发服务器将调试信息传递给了客户端。<br>与Python单元测试功能无缝衔接<br>单元测试是对最小软件开发单元的测试，其重点测试程序的内部结构，主要采用白盒测试方法，由开发人员负责。单元测试的主要目标是保证函数在给定的输入状态下，能够得到预想的输出，在不符合要求时能够提醒开发人员进行检查。<br>Flask提供了一个与Python自带的单元测试框架unitest无缝衔接的测试接口，即Flask对象的test_client()函数。通过test_client()函数，测试程序可以模拟进行HTTP访问的客户端来调用Flask路由处理函数，并且获取函数的输出来进行自定义的验证。<br>使用Jinja2模板<br>将HTML页面与后台应用程序联系起来一直是网站程序框架的一个重要目标。Flask通过使用Jinja2模板技术解决了这个问题。Jinja2是一个非常灵活的HTML模板技术，它是从Django模板发展而来的，但是比Django模板使用起来更加自由且更加高效。Jinja2模板使用配制的语义系统，提供灵活的模板继承技术，自动抗击XSS跨站攻击并且易于调试。<br>完全兼容WSGI
    1.0标准<br>WSGI（Web Server Gateway
    Interface）具有很强的伸缩性且能运行于多线程或多进程环境下，因为Python线程全局锁的存在，使得WSGI的这个特性至关重要。WSGI已经是Python界的一个主要标准，各种大型网路服务器对其都有良好的支持。WSGI位于Web应用程序与Web服务器之间，与WSGI完全兼容使得Flask能够配置到各种大型网络服务器中。<br>基于Unicode编码<br>Flask是完全基于Unicode的。这对制作非纯ASCII字符集的网站来说非常方便。HTTP本身是基于字节的，也就是说任何编码格式都可以在HTTP中传输。但是，HTTP要求在HTTP
    Head中显式地声明在本次传输中所应用的编码格式。在默认情况下，Flask会自动添加一个UTF-8编码格式的HTTP Head，使程序员无须担心编码的问题。</p>
<p>底层自定义协议网络框架——Twisted</p>
<p>以上讲到的3个Python
    Web框架都是围绕着应用层HTTP展开的，而Twisted是一个例外。Twisted是一个用Python语言编写的事件驱动的网络框架，对于追求服务器程序性能的应用，Twisted框架是一个很好的选择。</p>
<p>
    Twisted是一个有着10多年历史的开源事件驱动框架。Twisted支持很多种协议，包括传输层的UDP、TCP、TLS，以及应用层的HTTP、FTP等。对于所有这些协议，Twisted提供了客户端和服务器方面的开发工具。</p>
<p>Twisted框架的历史悠久，其主要发行版本都以Python 2为基础，最新的版本为基于Python 2.7的Twisted-15.4.0。Twisted社区正在开发基于Python
    3的版本，但目前为止尚没有基于Python 3的Twisted稳定发行版。</p>
<p>Twisted是一个高性能的编程框架。在不同的操作系统平台上，Twisted利用不同的底层技术实现了高效能通信。在Windows中，Twisted的实现基于I/O完成端口（IOCP，Input/Output
    Completion
    Port）技术，它保证了底层高效地将I/O事件通知给框架及应用程序；在Linux中，Twisted的实现基于epoll技术，epoll是Linux下多路复用I/O接口select/poll的增强版本，它能显著提高程序在大量并发连接中只有少量活跃的情况下的系统CPU利用率。<br>在开发方法上，Twisted引导程序员使用异步编程模型。Twisted提供了丰富的Defer、Threading等特性来支持异步编程。<br>原文地址<a
            href="https://yq.aliyun.com/go/articleRenderRedirect?url=https%3A%2F%2Fwww.cnblogs.com%2Fan-wen%2Fp%2F11330834.html"
            target="_blank" data-url="https://www.cnblogs.com/an-wen/p/11330834.html">https://www.cnblogs.com/an-wen/p/11330834.html</a>
</p>
