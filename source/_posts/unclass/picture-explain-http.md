---
title: "图解HTTP"
cover: "/img/lynk/33.jpg"
date:       2019-09-01
tags:
	- web
	- server
---

版权声明：本文为CSDN博主「极客学伟」的原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/qxuewei/article/details/100108137

<div id="content_views" class="markdown_views prism-atom-one-dark">
                    <!-- flowchart 箭头图标 勿删 -->
                    <svg xmlns="http://www.w3.org/2000/svg" style="display: none;">
                        <path stroke-linecap="round" d="M5,0 0,2.5 5,5z" id="raphael-marker-block" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);"></path>
                    </svg>
                                            <h1><a name="t0"></a><a id="HTTP_0"></a>《图解HTTP》读书笔记</h1>
<h2><a name="t1"></a><a id="Web_2"></a>第一章：了解Web及网路基础</h2>
<h3><a name="t2"></a><a id="TCPIP_4"></a>TCP/IP协议</h3>
<p>把互联网想关联的协议集合起来总称为TCP/IP协议<br>
TCP/IP 协议族按层次分为：应用层，传输层，网络层，数据链路层</p>
<h4><a id="_8"></a>应用层</h4>
<p>决定了向用户提供应用服务时通信的活动。<br>
TCP/IP 协议族内预存了各类通用的应用服务，比如：<strong>FTP</strong> 和 <strong>DNS</strong> 服务就是其中两类<br>
<strong>HTTP 协议也处于该层</strong></p>
<h4><a id="_13"></a>传输层</h4>
<p>传输层对上层应用层，提供处于网络连接中的两台计算机之间的数据传输。<br>
在传输层有两个性质不同的协议：<strong>TCP</strong>（Transmission Control Protocol，传输控制协议）和 <strong>UDP</strong>（User Data Protocol，用户数据报协议）</p>
<h4><a id="_17"></a>网路层（又名网络互联层）</h4>
<p>网路层用来处理网络上流动的数据包。数据包是网络传输的最小数据单位，该层规定了通过怎样的路径（所谓的传输路线）到达对方的计算机，并把数据包传送给对方。与对方计算机之间通过多台计算机或网络设备进行传输时，网络层所起的作用就是在众多的选项内选择一条传输路线。</p>
<h4><a id="_20"></a>链路层（又名数据链路层，网络接口层）</h4>
<p>用来处理连接网络的硬件部分。包括操作系统、硬件的设备驱动、NIC（Network Interface Card，网络适配器，即网卡），及光纤等物理可见部分，硬件上的范畴均在链路层的作用范围之内。</p>
<h3><a name="t3"></a><a id="TCPIP__23"></a>TCP/IP 通信传输流</h3>
<p><img src="https://imgconvert.csdnimg.cn/aHR0cDovL2Jsb2cuaW1hZ2Uuamt4dWV3ZWkuY29tL213ZWIvMjAxOS4wOC4yNy5YbmlwMjAxOS0wOC0xNV8wOC0xMC01OS5qcGc?x-oss-process=image/format,png" alt="Xnip2019-08-15_08-10-59"></p>
<p>利用TCP/IP 协议族进行通信时，会通过分层顺序与对方进行通信，发送端从应用层往下走，接收端则从应用层往上走。<br>
发送端在层与层之间传输数据时，没经过一层时必定会被打上一个该层所属的首部信息，反之，接收端在层与层之间传输数据时，每经过一层时会把对应的首部消去。- 这种把数据信息包装起来的做法称为封装。</p>
<h3><a name="t4"></a><a id="_TCP__30"></a>确保可靠性的 TCP 协议</h3>
<p>按层次分，TCP位于传输层，提供可靠的字节流服务（字节流：为了方便传输，将大块数据分割成以报文段为单位的数据包进行管理）。<br>
<strong>TCP 协议为了更容易传送大数据才把数据分割，而且 TCP 协议能够确认数据最终是否送达到对方。</strong></p>
<h4><a id="_34"></a>如何确保数据能到达目标？</h4>
<p>TCP 协议采用了三次握手策略。用TCP协议把数据包送出去以后，TCP不会对传送后的情况置之不理，它一定会向对方确认是否成功送达，握手过程使用了TCP的标志：SYN（synchronize）和 ACK（acknowledgement）。<br>
发送端首先先发送一个带SYN标志的数据包给对方，接收端收到后，回传一个带有 SYN/ACK 标志的数据包以示传达确认信息，最后，发送端再回传一个带 ACK 标志的数据包，代表握手结束。若捂手过程中在某个阶段莫名中断，TCP协议会在此以相同的顺序发送相同的数据包</p>
<p><img src="https://imgconvert.csdnimg.cn/aHR0cDovL2Jsb2cuaW1hZ2Uuamt4dWV3ZWkuY29tL213ZWIvMjAxOS4wOC4yNy5YbmlwMjAxOS0wOC0xNV8xMy00OS0zNC5qcGc?x-oss-process=image/format,png" alt="Xnip2019-08-15_13-49-34"></p>
<h3><a name="t5"></a><a id="_DNS__41"></a>负责域名解析的 DNS 服务</h3>
<p>DNS（Domain Name System）服务是和HTTP协议一样位于应用层的协议，它提供域名到IP地址之间的解析服务。</p>
<p>浏览一个网址的全过程：</p>
<p><img src="https://imgconvert.csdnimg.cn/aHR0cDovL2Jsb2cuaW1hZ2Uuamt4dWV3ZWkuY29tL213ZWIvMjAxOS4wOC4yNy5YbmlwMjAxOS0wOC0xNl8wNy0wMy0yMi5qcGc?x-oss-process=image/format,png" alt="Xnip2019-08-16_07-03-22"></p>
<h3><a name="t6"></a><a id="URLUniform_Resource_Locator__URI_48"></a>URL（Uniform Resource Locator，统一资源定位符） 和 URI（统一资源标示符）</h3>
<p>URL 是访问web页面需要输入的网页地址<br>
URI 是由某个协议方案表示的资源的定位标示符，协议方案是指访问资源所使用的协议类型名称</p>
<p>URI 用字符串标识某一互联网资源，而URL表示资源的地点（互联网上所处的位置），可见 URL 是 URI 的子集。</p>
<h2><a name="t7"></a><a id="HTTP_54"></a>第二章：简单的HTTP协议</h2>
<p>HTTP请求报文由：请求方法、请求URI、协议版本、可选的请求首部字段和内容实体 构成<br>
<img src="https://imgconvert.csdnimg.cn/aHR0cDovL2Jsb2cuaW1hZ2Uuamt4dWV3ZWkuY29tL213ZWIvMjAxOS4wOC4yNy5YbmlwMjAxOS0wOC0xNl8wNy0yNC0yOC5qcGc?x-oss-process=image/format,png" alt="Xnip2019-08-16_07-24-28"></p>
<h3><a name="t8"></a><a id="HTTP__59"></a>HTTP 是一种不保存状态，即无状态协议。</h3>
<p>HTTP 协议自身不对请求和响应之间的通信状态进行保存。目的是为了更快的处理大量事务，确保协议的可伸缩性。<br>
后来有一些场景需要保存客户端的状态，比如登录状态，于是引入了 Cookie 技术。有了 Cookie 再用HTTP协议通信，就可以管理状态了。</p>
<h3><a name="t9"></a><a id="HTTP_63"></a>告知服务器意图的HTTP方法</h3>
<ul>
<li>GET : 获取</li>
<li>POST: 传输实体主体</li>
<li>PUT : 传输文件</li>
<li>HEAD: 获得报文首部</li>
<li>DELETE: 删除文件</li>
<li>OPTIONS: 询问支持的方法</li>
<li>TRACE：追踪路径</li>
<li>CONNECT：要求用隧道协议连接代理</li>
</ul>
<h3><a name="t10"></a><a id="_73"></a>持久连接节省通信量</h3>
<p>HTTP 初始版本，每进行一次HTTP通信就要断开一次TCP连接，当年数据小没问题，但随着HTTP的普及，HTTP所传输的内容愈来愈多，每次请求都会造成无谓的TCP连接建立和断开，增加通信量的开销。</p>
<p>为解决上述TCP连接的问题，HTTP/1.1 和 一部分 HTTP/1.0 相处了持久连接的方法，特点是：只要任意一端没有明确的提出断开连接，则保持TCP连接状态。</p>
<h4><a id="_78"></a>管线化</h4>
<p>持久连接使得多数请求以管线化（pipelining）方式发送成为可能，以前发送请求后需等待并受到响应，才能发送下一个请求。管线化技术出现后，不用等待响应亦可直接发送下一个请求。这样就能做到同时并行发送多个请求。而不需要一个接一个地等待响应了。</p>
<h2><a name="t11"></a><a id="HTTPHTTP_81"></a>第三章：HTTP报文内的HTTP信息</h2>
<p>请求报文和响应报文的首部内容由以下数据组成：</p>
<ul>
<li>
<p>请求行<br>
包含用于请求的方法，请求 URI 和 HTTP 版本</p>
</li>
<li>
<p>状态行<br>
包含响应结果的状态码，原因短语和HTTP版本</p>
</li>
<li>
<p>首部字段<br>
包含请求和响应的各种条件和属性的各类首部<br>
一般有四种首部：通用首部，请求首部，响应首部和实体首部</p>
</li>
<li>
<p>其他<br>
可能包含HTTP的RFC 里未定义的首部（Cookie等）</p>
</li>
</ul>
<h3><a name="t12"></a><a id="_97"></a>编码提升传输速率</h3>
<h4><a id="_99"></a>报文</h4>
<p>是HTTP通信中的基本单位，由8位字节流组成，通过 HTTP 通信传输</p>
<h4><a id="_102"></a>实体</h4>
<p>作为请求或响应的有效载荷数据（补充项）被传输，其内容由实体首部和实体主体组成</p>
<p>HTTP 报文的主体用于传输请求或响应的实体主体。通常，报文主体等于实体主体。只有当传输中进行编码操作时，实体主体的内容发生变化，才导致它和报文主体产生差异。</p>
<h2><a name="t13"></a><a id="HTTP_107"></a>第四章：返回结果的HTTP状态码</h2>
<h3><a name="t14"></a><a id="_109"></a>状态码的类别</h3>

<div class="table-box"><table>
<thead>
<tr>
<th align="center"></th>
<th align="center">类别</th>
<th align="center">原因短语</th>
</tr>
</thead>
<tbody>
<tr>
<td align="center">1xx</td>
<td align="center">Infomational（信息性状态码）</td>
<td align="center">接收的请求正常处理</td>
</tr>
<tr>
<td align="center">2xx</td>
<td align="center">Success（成功状态码）</td>
<td align="center">请求正常处理完毕</td>
</tr>
<tr>
<td align="center">3xx</td>
<td align="center">Redirection（重定向状态码）</td>
<td align="center">需要进行附加操作以完成请求</td>
</tr>
<tr>
<td align="center">4xx</td>
<td align="center">Client Error（客户端状态错误码）</td>
<td align="center">服务器无法处理请求</td>
</tr>
<tr>
<td align="center">5xx</td>
<td align="center">Server Error（服务器状态码）</td>
<td align="center">服务器处理请求出错</td>
</tr>
</tbody>
</table></div><h3><a name="t15"></a><a id="_119"></a>常见错误码</h3>
<h4><a id="2xx___121"></a>2xx - 成功</h4>
<ul>
<li>200 OK  ： 请求被正常处理。</li>
<li>204 No Content ： 请求成功但返回的响应报文中不含实体的主体部分，一般只需要从客户端往服务器发送信息，而对客户端不需要发送新信息内容的情况下使用。</li>
<li>206 Partial Content : 客户端进行了范围请求，服务器成功执行了这部分GET请求，响应报文中包含由 Content-Range 指定范围的实体内容</li>
</ul>
<h4><a id="3xx___126"></a>3xx - 重定向</h4>
<ul>
<li>301 Moved Permanently ： 永久性重定向，该状态码表示请求的资源已被分配了新的URI，以后应使用资源现在所指的URI。</li>
<li>302 Found ： 临时性重定向，表示请求的资源已被分配了新的URI，希望用户本次能使用新的URI访问</li>
<li>303 See Other ： 表示由于请求对应的资源存在着另一个URI，应使用GET方法定向获取请求的资源。</li>
<li>304 Not Modified : 表示客户端发送附带条件的请求时，服务端允许请求访问资源，但未满足条件的情况。</li>
<li>307 Temporary Redirect : 临时重定向</li>
</ul>
<h4><a id="4xx___133"></a>4xx - 客户端错误</h4>
<ul>
<li>400 Bad Request : 请求报文中存在语法错误，当错误发生时，需修改请求的内容后再次发送请求。</li>
<li>401 Unauthorized ： 表示发送的请求需要有同感HTTP认证的认证信息。</li>
<li>403 Forbidden ： 表明对请求资源的访问被服务器拒绝了。例如未获取到文件系统的访问权限</li>
<li>404 Not Found ： 表明服务器上无法找到请求的资源。</li>
</ul>
<h4><a id="5xx___139"></a>5xx - 服务器错误</h4>
<ul>
<li>500 Internal Server Error ： 服务器端在执行请求时发生了错误。</li>
<li>503 Service Unavailable ：表明服务器暂时处于超负载或正在进行停机去维护，现在无法处理请求。</li>
</ul>
<h2><a name="t16"></a><a id="_HTTP__Web__143"></a>第五章：与 HTTP 协作的 Web 服务器</h2>
<p>一台 Web 服务器可搭建多个独立域名的 Web 网站，也可作为通信路径上的中转服务器提升传输速率</p>
<h4><a id="_146"></a>代理</h4>
<p>代理是一种由转发功能的应用程序，扮演了位于服务器和客户端中间人的角色，接收由客户端发送的请求并转发给服务器，同时也接收服务器返回的响应并转发给客户端<br>
分缓存代理（缓存从源服务器获取的数据）和透明代理（对请求不做任何加工）</p>
<h4><a id="_150"></a>网关</h4>
<p>网关是转发其他服务器通信数据的服务器，接收从客户端发送来的请求时，它像自己拥有资源的源服务器一样对请求进行处理。<br>
工作机制和代理类似，而网关能够使通信线路上的服务器提供非HTTP协议服务。利用网关能够提高通信的安全性，因为可以在客户端与网关之间的通信线路上加密以确保连接的安全。</p>
<h4><a id="_154"></a>隧道</h4>
<p>隧道是在相隔甚远的客户端和服务器两者之间进行中转，并保持双方通信连接的应用程序。<br>
可按要求建立一条与其他服务器的通信线路，届时使用 SSL 等加密手段进行通信。隧道的目的是确保客户端与服务器进行安全的通信。</p>
<h2><a name="t17"></a><a id="HTTP_158"></a>第六章：HTTP首部</h2>
<p>HTTP 协议的请求和响应报文中必含HTTP首部，首部内容为客户端和服务器分别处理请求和响应提供所需要的信息。</p>
<h4><a id="_161"></a>请求报文</h4>
<p>HTTP请求报文由：方法，URI，HTTP版本，HTTP首部字段等部分构成。</p>
<h4><a id="_164"></a>响应报文</h4>
<p>HTTP响应报文由：HTTP版本，状态码（数字和原因短语），HTTP首部字段等3部分构成。</p>
<h3><a name="t18"></a><a id="HTTP_167"></a>HTTP首部字段</h3>
<p>首部字段由首部字段名和字段值构成，中间用冒号 ：分割。<br>
例如HTTP首部中以 Content-Type 这个字段来表示报文主体的对象类型。</p>
<h4><a id="_171"></a>通用首部字段</h4>
<p><img src="https://imgconvert.csdnimg.cn/aHR0cDovL2Jsb2cuaW1hZ2Uuamt4dWV3ZWkuY29tL213ZWIvMjAxOS4wOC4yNy5YbmlwMjAxOS0wOC0xOF8xMC01My0wNy5qcGc?x-oss-process=image/format,png" alt="Xnip2019-08-18_10-53-07"></p>
<h4><a id="_174"></a>请求首部字段</h4>
<p><img src="https://imgconvert.csdnimg.cn/aHR0cDovL2Jsb2cuaW1hZ2Uuamt4dWV3ZWkuY29tL213ZWIvMjAxOS4wOC4yNy5YbmlwMjAxOS0wOC0xOF8xMC01Ni01NC5qcGc?x-oss-process=image/format,png" alt="Xnip2019-08-18_10-56-54"></p>
<h4><a id="_178"></a>响应首部字段</h4>
<p><img src="https://imgconvert.csdnimg.cn/aHR0cDovL2Jsb2cuaW1hZ2Uuamt4dWV3ZWkuY29tL213ZWIvMjAxOS4wOC4yNy5YbmlwMjAxOS0wOC0xOF8xMS0wNy00Ni5qcGc?x-oss-process=image/format,png" alt="Xnip2019-08-18_11-07-46"></p>
<h4><a id="_181"></a>实体首部字段</h4>
<p><img src="https://imgconvert.csdnimg.cn/aHR0cDovL2Jsb2cuaW1hZ2Uuamt4dWV3ZWkuY29tL213ZWIvMjAxOS4wOC4yNy5YbmlwMjAxOS0wOC0xOF8xMS0wOC0yNy5qcGc?x-oss-process=image/format,png" alt="Xnip2019-08-18_11-08-27"></p>
<h6><a id="_HTTP__184"></a>其他首部字段： HTTP 首部字段是可以自行扩展的</h6>
<h2><a name="t19"></a><a id="WebHTTPS_186"></a>第七章：确保Web安全的HTTPS</h2>
<h3><a name="t20"></a><a id="HTTP__188"></a>HTTP 的缺点</h3>
<ul>
<li>通信使用明文（不加密），内容可能会被窃听</li>
<li>不验证通信方的身份，因此有可能遭遇伪装</li>
<li>无法证明报文的完整性，所以有可能已遭篡改</li>
</ul>
<p>####加密处理防止被窃听</p>
<h5><a id="_194"></a>通信的加密</h5>
<p>HTTP 协议中没有加密机制，但可以通过和SSL（Secure Socket Layer，安全套接层）或 TLS（Transport Layer Security，安全传输层协议）的组合使用，加密HTTP的通信内容。</p>
<p>用SSL建立安全通信线路之后，就可以在这条线路上进行HTTP通信的。与SSL组合使用的HTTP被称为 HTTPS（HTTP Secure，超文本传输安全协议）</p>
<h5><a id="_199"></a>内容的加密</h5>
<p>通过使用证书，以证明通信方就是意料中的服务器。</p>
<h3><a name="t21"></a><a id="HTTP__HTTPS_203"></a>HTTP+加密+认证+完整性保护 = HTTPS</h3>
<p>通常，HTTP直接和TCP通信，当使用 SSL 时，则演变成先和 SSL 通信，再由SSL 和 TCP 通信了。</p>
<p>SSL 是独立于HTTP的协议，所以不光是HTTP协议，其他运行在应用层的SMTP和Telnet等协议均可配合SSL协议使用。可以说 SSL 是当今世界上应用最为广泛的网络安全技术。</p>
<p>HTTPS 采用共享密钥加密和公开密钥加密两者并用的混合加密机制。</p>
<p>使用SSL速度不可避免的会变慢：1.通信慢 2.大量消耗CPU和内存等资源，导致处理速度变慢。</p>
<h2><a name="t22"></a><a id="_212"></a>第八章：确认访问用户身份的认证</h2>
<p>认证的几种常见方式：</p>
<ul>
<li>密码：只有本人才会知道的字符串信息</li>
<li>动态令牌：仅限本人持有的设备内显示的一次性密码</li>
<li>数字证书：仅限本人（终端）持有的信息</li>
<li>生物认证：指纹和虹膜等本人的生理信息</li>
<li>IC卡等：仅限本人持有的信息</li>
</ul>
<p>HTTP/1.1 使用的认证方式：</p>
<ol>
<li>BASIC认证（基本认证）</li>
<li>DIGEST认证（摘要认证）</li>
<li>SSL客户端认证</li>
<li>FormBase认证（基于表单认证）</li>
</ol>
<h2><a name="t23"></a><a id="HTTP_226"></a>第九章：基于HTTP的功能追加协议</h2>
<p>使用HTTP协议存在如下瓶颈：</p>
<ul>
<li>一条连接上只可发送一个请求</li>
<li>请求只能从客户端开始，客户端不可以接收除响应以外的指令</li>
<li>请求/响应首部未经压缩就发送。首部信息越多延迟越大</li>
<li>发送冗长的首部，每次互相发送相同的首部造成的浪费较多</li>
<li>可任意选择数据压缩格式。非强制压缩发送</li>
</ul>
<h4><a id="Ajax__234"></a>Ajax 的解决方法</h4>
<p>Ajax（Asynchronous JavaScript and XML, 异步JavaScript与XML技术） 是一种有效利用JavaScript 和 DOM（Document Object Model） 的操作，以达到局部Web页面替换加载的异步通信手段。由于它只更新一部分界面，响应中传输的数据量会因此而减少。</p>
<h4><a id="Comet__237"></a>Comet 的解决方法</h4>
<p>通常，服务端接收到请求，在处理完毕后就会立即返回响应，但为了实现推送功能，Comet会先将响应置于挂起状态，当服务端有内容更新时，再返回该响应。因此，服务端一旦有更新，就可以立即反馈给客户端。</p>
<h4><a id="SPDY__240"></a>SPDY 的目标</h4>
<p>SPDY 没有完全改写HTTP协议，而是再TCP/IP的应用层与传输层之间通过新加会话层的形式运作。同时，考虑到安全性问题，SDPY规定通信中使用SSL。</p>
<p><img src="https://imgconvert.csdnimg.cn/aHR0cDovL2Jsb2cuaW1hZ2Uuamt4dWV3ZWkuY29tL213ZWIvMjAxOS4wOC4yNy5YbmlwMjAxOS0wOC0yMl8wOC01NC0xNy5qcGc?x-oss-process=image/format,png" alt="Xnip2019-08-22_08-54-17"></p>
<p>SDPY的设计图示</p>
<p>使用 SDPY后，HTTP协议额外获得以下功能：</p>
<h5><a id="_248"></a>多路复用流</h5>
<p>通过单一的TCP连接，可以无限制处理多个HTTP请求。所有请求的处理都在一条TCP连接上完成，因此TCP处理效率得到提高</p>
<h5><a id="_251"></a>赋予请求优先级</h5>
<h5><a id="HTTP_252"></a>压缩HTTP首部</h5>
<h5><a id="_253"></a>推送功能</h5>
<h5><a id="_254"></a>服务器提示功能</h5>
<p>服务器可以主动提示客户端请求所需的资源。</p>
<h4><a id="WebSocket_257"></a>WebSocket</h4>
<p>Web 浏览器与 Web 服务器之间全双工通信标准。一旦Web服务器与客户端之间建立起 WebSocket 协议的通信连接，之后所有的通信都依赖这个专用协议进行，通信过程中可互相发送JSON，XML，HTML或图片等任意格式的数据。</p>
<p>WebSocket 通信的主要特点：</p>
<ul>
<li>推送功能</li>
<li>减少通信量</li>
</ul>
<h2><a name="t24"></a><a id="Web_264"></a>第十章：构建Web内容的技术</h2>
<h3><a name="t25"></a><a id="HTML_HyperText_Markup_Language_266"></a>HTML （HyperText Markup Language，超文本标记语言）。</h3>
<p>CSS（Cascading Style Sheets，层叠样式表），可以指定如何展现HTML内的各种元素，属于样式表标准之一。</p>
<h3><a name="t26"></a><a id="HTMLDynamic_HTML_269"></a>动态HTML（Dynamic HTML）</h3>
<p>通过调用客户端脚本语言JavaScript，实现对HTML的Web页面的动态改造。利用 DOM（Document Object Model，文档对象模型）可指定欲发生动态变化的HTML元素。</p>
<h3><a name="t27"></a><a id="Web_272"></a>Web应用</h3>
<h3><a name="t28"></a><a id="_274"></a>数据发布的格式及语言·</h3>
<ul>
<li>XML</li>
<li>RSS</li>
<li>JSON</li>
</ul>
<h2><a name="t29"></a><a id="Web_279"></a>第十一章：Web的攻击技术</h2>
<p>HTTP 不具备必要的安全功能</p>
<h4><a id="SQL_283"></a>SQL注入攻击</h4>
<p>对Web应用使用的数据库，通过运行非法的SQL而产生的攻击。</p>
<h4><a id="HTTP_286"></a>HTTP首部注入攻击</h4>
<p>攻击者通过在响应首部字段内插入换行，添加任意响应首部或主体的一种攻击。</p>
<ul>
<li>设置任何Cookie信息</li>
<li>重定向至任意URL</li>
<li>显示任意的主体（HTTP响应截断攻击）</li>
</ul>
<h4><a id="_293"></a>目标遍历攻击</h4>
<p>对本无意公开的文件目录通过非法截断其目录路径后，达成访问目的的一种攻击。</p>
<h4><a id="_296"></a>因设置或设计上的缺陷引发的安全漏洞</h4>
<h4><a id="_298"></a>密码破解</h4>
<p>算出密码，突破认证</p>
<h4><a id="DoS_301"></a>DoS攻击</h4>
<p>一种让运行中的服务呈停止状态的攻击。</p>
<ul>
<li>集中利用访问请求造成资源过载，资源用尽的同时，实际上服务也就呈停止状态</li>
<li>通过攻击安全漏洞使服务停止</li>
</ul>
<p>单纯来讲就是发生大量合法请求，服务器很难分辨何为正常请求，何为攻击请求，因此很难防止DoS攻击。<br>
多态计算机发起的DoS攻击成为 DDoS攻击（Distributed Denial of Service attack）。</p>

                                    </div>