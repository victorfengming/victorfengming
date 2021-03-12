---
title: "什么是wsgi？"
cover: "/img/lynk/48.jpg"
date:       2019-12-02
subtitle: "Web服务器网关接口"
tags:
	- Python
	- solution
	- web
	- django
---


本文转自:https://www.jianshu.com/p/c66d3adeaaed

<p>WSGI的全称是<em>Web Server Gateway Interface</em>，翻译过来就是<em>Web服务器网关接口</em>。具体的来说，<strong>WSGI是一个规范，定义了Web服务器如何与Python应用程序进行交互，使得使用Python写的Web应用程序可以和Web服务器对接起来</strong>。WSGI一开始是在<a
        href="https://www.python.org/dev/peps/pep-0333/" target="_blank" rel="nofollow">PEP-0333</a>中定义的，最新版本是在Python的<a
        href="https://www.python.org/dev/peps/pep-3333/" target="_blank" rel="nofollow">PEP-3333</a>定义的。</p>
<h1>WSGI是什么</h1>
<p>WSGI的全称是<em>Web Server Gateway Interface</em>，翻译过来就是<em>Web服务器网关接口</em>。具体的来说，<strong>WSGI是一个规范，定义了Web服务器如何与Python应用程序进行交互，使得使用Python写的Web应用程序可以和Web服务器对接起来</strong>。WSGI一开始是在<a
        href="https://www.python.org/dev/peps/pep-0333/" target="_blank" rel="nofollow">PEP-0333</a>中定义的，最新版本是在Python的<a
        href="https://www.python.org/dev/peps/pep-3333/" target="_blank" rel="nofollow">PEP-3333</a>定义的。</p>
<p>对于初学者来说，上面那段就是废话，说了跟没说一样。本文的主要内容就是说清楚，WSGI到底是如何工作的。</p>
<h2>为什么需要WSGI这个规范</h2>
<p>在Web部署的方案上，有一个方案是目前应用最广泛的：</p>
<ul>
    <li><p>首先，部署一个Web服务器专门用来处理HTTP协议层面相关的事情，比如如何在一个物理机上提供多个不同的Web服务（单IP多域名，单IP多端口等）这种事情。</p></li>
    <li><p>然后，部署一个用各种语言编写（Java, PHP, Python,
        Ruby等）的应用程序，这个应用程序会从Web服务器上接收客户端的请求，处理完成后，再返回响应给Web服务器，最后由Web服务器返回给客户端。</p></li>
</ul>
<p>
    那么，要采用这种方案，Web服务器和应用程序之间就要知道如何进行交互。为了定义Web服务器和应用程序之间的交互过程，就形成了很多不同的规范。这种规范里最早的一个是CGI][3，1993年开发的。后来又出现了很多这样的规范。比如改进CGI性能的FasgCGI，Java专用的Servlet规范，还有Python专用的WSGI规范等。提出这些规范的目的就是为了定义统一的标准，提升程序的可移植性。在WSGI规范的最开始的PEP-333中一开始就描述了为什么需要WSGI规范。</p>
<h1>WSGI如何工作</h1>
<p>从上文可以知道，WSGI相当于是Web服务器和Python应用程序之间的桥梁。那么这个桥梁是如何工作的呢？首先，我们明确桥梁的作用，WSGI存在的目的有两个：</p>
<ol>
    <li><p>让Web服务器知道如何调用Python应用程序，并且把用户的请求告诉应用程序。</p></li>
    <li><p>让Python应用程序知道用户的具体请求是什么，以及如何返回结果给Web服务器。</p></li>
</ol>
<h2>WSGI中的角色</h2>
<p>
    在WSGI中定义了两个角色，Web服务器端称为<strong>server</strong>或者<strong>gateway</strong>，应用程序端称为<strong>application</strong>或者<strong>framework</strong>（因为WSGI的应用程序端的规范一般都是由具体的框架来实现的）。我们下面统一使用server和application这两个术语。
</p>
<p>server端会先收到用户的请求，然后会根据规范的要求调用application端，如下图所示：</p>
<p>[图片上传失败...(image-1bd5a9-1541121120404)]</p>
<p>调用的结果会被封装成HTTP响应后再发送给客户端。</p>
<h2>server如何调用application</h2>
<p>首先，每个application的入口只有一个，也就是所有的客户端请求都同一个入口进入到应用程序。</p>
<p>
    接下来，server端需要知道去哪里找application的入口。这个需要在server端指定一个Python模块，也就是Python应用中的一个文件，并且这个模块中需要包含一个名称为<strong>application</strong>的可调用对象（函数和类都可以），这个<strong>application</strong>对象就是这个应用程序的唯一入口了。WSGI还定义了<strong>application</strong>对象的形式：
</p>
<pre class="line-numbers  language-python"><code class="  language-python"><span
        class="token keyword">def</span> <span class="token function">simple_app</span><span
        class="token punctuation">(</span>environ<span class="token punctuation">,</span> start_response<span
        class="token punctuation">)</span><span class="token punctuation">:</span>
      <span class="token keyword">pass</span>
<span aria-hidden="true" class="line-numbers-rows"><span></span><span></span></span></code><button class="VJbwyy"
                                                                                                   type="button"
                                                                                                   aria-label="复制代码"><i
        aria-label="icon: copy" class="anticon anticon-copy"><svg viewBox="64 64 896 896" focusable="false" class=""
                                                                  data-icon="copy" width="1em" height="1em"
                                                                  fill="currentColor" aria-hidden="true"><path
        d="M832 64H296c-4.4 0-8 3.6-8 8v56c0 4.4 3.6 8 8 8h496v688c0 4.4 3.6 8 8 8h56c4.4 0 8-3.6 8-8V96c0-17.7-14.3-32-32-32zM704 192H192c-17.7 0-32 14.3-32 32v530.7c0 8.5 3.4 16.6 9.4 22.6l173.3 173.3c2.2 2.2 4.7 4 7.4 5.5v1.9h4.2c3.5 1.3 7.2 2 11 2H704c17.7 0 32-14.3 32-32V224c0-17.7-14.3-32-32-32zM350 856.2L263.9 770H350v86.2zM664 888H414V746c0-22.1-17.9-40-40-40H232V264h432v624z"></path></svg></i></button></pre>
<p>上面代码中的<code>environ</code>和<code>start_response</code>就是server端调用<strong>application</strong>对象时传递的两个参数。</p>
<p>
    我们来看具体的例子。假设我们的应用程序的入口文件是<code>/var/www/index.py</code>，那么我们就需要在server端配置好这个路径（如何配置取决于server端的实现），然后在<code>index.py</code>中的代码如下所示：
</p>
<p>使用标准库（这个只是demo）</p>
<pre class="line-numbers  language-swift"><code class="  language-swift"><span class="token keyword">import</span> wsgiref

application <span class="token operator">=</span> wsgiref<span class="token punctuation">.</span>simple_server<span
            class="token punctuation">.</span>demo_app
<span aria-hidden="true" class="line-numbers-rows"><span></span><span></span><span></span></span></code><button
        class="VJbwyy" type="button" aria-label="复制代码"><i aria-label="icon: copy" class="anticon anticon-copy"><svg
        viewBox="64 64 896 896" focusable="false" class="" data-icon="copy" width="1em" height="1em"
        fill="currentColor" aria-hidden="true"><path
        d="M832 64H296c-4.4 0-8 3.6-8 8v56c0 4.4 3.6 8 8 8h496v688c0 4.4 3.6 8 8 8h56c4.4 0 8-3.6 8-8V96c0-17.7-14.3-32-32-32zM704 192H192c-17.7 0-32 14.3-32 32v530.7c0 8.5 3.4 16.6 9.4 22.6l173.3 173.3c2.2 2.2 4.7 4 7.4 5.5v1.9h4.2c3.5 1.3 7.2 2 11 2H704c17.7 0 32-14.3 32-32V224c0-17.7-14.3-32-32-32zM350 856.2L263.9 770H350v86.2zM664 888H414V746c0-22.1-17.9-40-40-40H232V264h432v624z"></path></svg></i></button></pre>
<p>使用web.py框架</p>
<pre class="line-numbers  language-python"><code class="  language-python"><span class="token keyword">import</span> web

urls <span class="token operator">=</span> <span class="token punctuation">(</span>
    <span class="token string">'/.*'</span><span class="token punctuation">,</span> <span
            class="token string">'hello'</span><span class="token punctuation">,</span>
<span class="token punctuation">)</span>

<span class="token keyword">class</span> <span class="token class-name">hello</span><span
            class="token punctuation">(</span><span class="token builtin">object</span><span
            class="token punctuation">)</span><span class="token punctuation">:</span>
    <span class="token keyword">def</span> <span class="token function">GET</span><span
            class="token punctuation">(</span>self<span class="token punctuation">)</span><span
            class="token punctuation">:</span>
        <span class="token keyword">return</span> <span class="token string">"Hello, world."</span>

application <span class="token operator">=</span> web<span class="token punctuation">.</span>application<span
            class="token punctuation">(</span>urls<span class="token punctuation">,</span> <span
            class="token builtin">globals</span><span class="token punctuation">(</span><span
            class="token punctuation">)</span><span class="token punctuation">)</span><span
            class="token punctuation">.</span>wsgifunc<span class="token punctuation">(</span><span
            class="token punctuation">)</span>
<span aria-hidden="true"
      class="line-numbers-rows"><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span></span></code><button
        class="VJbwyy" type="button" aria-label="复制代码"><i aria-label="icon: copy" class="anticon anticon-copy"><svg
        viewBox="64 64 896 896" focusable="false" class="" data-icon="copy" width="1em" height="1em"
        fill="currentColor" aria-hidden="true"><path
        d="M832 64H296c-4.4 0-8 3.6-8 8v56c0 4.4 3.6 8 8 8h496v688c0 4.4 3.6 8 8 8h56c4.4 0 8-3.6 8-8V96c0-17.7-14.3-32-32-32zM704 192H192c-17.7 0-32 14.3-32 32v530.7c0 8.5 3.4 16.6 9.4 22.6l173.3 173.3c2.2 2.2 4.7 4 7.4 5.5v1.9h4.2c3.5 1.3 7.2 2 11 2H704c17.7 0 32-14.3 32-32V224c0-17.7-14.3-32-32-32zM350 856.2L263.9 770H350v86.2zM664 888H414V746c0-22.1-17.9-40-40-40H232V264h432v624z"></path></svg></i></button></pre>
<p>你可以看到，文件中都需要有一个<strong>application</strong>对象，server端会找到这个文件，然后调用这个对象。所以支持WSGI的Python框架最终都会有这么一个application对象，不过框架的使用者不需要关心这个application对象内部是如何工作的，只需要关心路由定义、请求处理等具体的业务逻辑。
</p>
<p>因为application对象是唯一的入口，所以不管客户端请求的路径和数据是什么，server都是调用这个application对象，具体的客户端请求的处理有application对象完成。</p>
<h2>application对象需要做什么</h2>
<p>上面已经提到了，application对象需要是一个可调用对象，而且其定义需要满足如下形式：</p>
<pre class="line-numbers  language-python"><code class="  language-python"><span
        class="token keyword">def</span> <span class="token function">simple_app</span><span
        class="token punctuation">(</span>environ<span class="token punctuation">,</span> start_response<span
        class="token punctuation">)</span><span class="token punctuation">:</span>
      <span class="token keyword">pass</span>
<span aria-hidden="true" class="line-numbers-rows"><span></span><span></span></span></code><button class="VJbwyy"
                                                                                                   type="button"
                                                                                                   aria-label="复制代码"><i
        aria-label="icon: copy" class="anticon anticon-copy"><svg viewBox="64 64 896 896" focusable="false" class=""
                                                                  data-icon="copy" width="1em" height="1em"
                                                                  fill="currentColor" aria-hidden="true"><path
        d="M832 64H296c-4.4 0-8 3.6-8 8v56c0 4.4 3.6 8 8 8h496v688c0 4.4 3.6 8 8 8h56c4.4 0 8-3.6 8-8V96c0-17.7-14.3-32-32-32zM704 192H192c-17.7 0-32 14.3-32 32v530.7c0 8.5 3.4 16.6 9.4 22.6l173.3 173.3c2.2 2.2 4.7 4 7.4 5.5v1.9h4.2c3.5 1.3 7.2 2 11 2H704c17.7 0 32-14.3 32-32V224c0-17.7-14.3-32-32-32zM350 856.2L263.9 770H350v86.2zM664 888H414V746c0-22.1-17.9-40-40-40H232V264h432v624z"></path></svg></i></button></pre>
<p>
    当server按照WSGI的规范调用了application之后，application就可以开始处理客户端的请求了，处理请求之后，application对象需要返回处理结果给server端。处理请求和返回结果这两个事情，都和server调用application对象时传递的两个参数有关。</p>
<h3>environ参数</h3>
<p>
    environ参数是一个Python的字典，里面存放了所有和客户端相关的信息，这样application对象就能知道客户端请求的资源是什么，请求中带了什么数据等。environ字典包含了一些CGI规范要求的数据，以及WSGI规范新增的数据，还可能包含一些操作系统的环境变量以及Web服务器相关的环境变量。我们来看一些environ中常用的成员：</p>
<p>首先是CGI规范中要求的变量：</p>
<ul>
    <li><p><strong>REQUEST_METHOD</strong>： 请求方法，是个字符串，'GET', 'POST'等</p></li>
    <li><p><strong>SCRIPT_NAME</strong>： HTTP请求的path中的用于查找到application对象的部分，比如Web服务器可以根据path的一部分来决定请求由哪个virtual
        host处理</p></li>
    <li><p><strong>PATH_INFO</strong>： HTTP请求的path中剩余的部分，也就是application要处理的部分</p></li>
    <li><p><strong>QUERY_STRING</strong>： HTTP请求中的查询字符串，URL中<strong>?</strong>后面的内容</p></li>
    <li><p><strong>CONTENT_TYPE</strong>： HTTP headers中的content-type内容</p></li>
    <li><p><strong>CONTENT_LENGTH</strong>： HTTP headers中的content-length内容</p></li>
    <li><p><strong>SERVER_NAME</strong>和<strong>SERVER_PORT</strong>： 服务器名和端口，这两个值和前面的SCRIPT_NAME,
        PATH_INFO拼起来可以得到完整的URL路径</p></li>
    <li><p><strong>SERVER_PROTOCOL</strong>： HTTP协议版本，HTTP/1.0或者HTTP/1.1</p></li>
    <li><p><strong>HTTP_</strong>： 和HTTP请求中的headers对应。</p></li>
</ul>
<p>WSGI规范中还要求environ包含下列成员：</p>
<ul>
    <li><p><strong>wsgi.version</strong>：表示WSGI版本，一个元组(1, 0)，表示版本1.0</p></li>
    <li><p><strong>wsgi.url_scheme</strong>：http或者https</p></li>
    <li><p><strong>wsgi.input</strong>：一个类文件的输入流，application可以通过这个获取HTTP request body</p></li>
    <li><p><strong>wsgi.errors</strong>：一个输出流，当应用程序出错时，可以将错误信息写入这里</p></li>
    <li><p><strong>wsgi.multithread</strong>：当application对象可能被多个线程同时调用时，这个值需要为True</p></li>
    <li><p><strong>wsgi.multiprocess</strong>：当application对象可能被多个进程同时调用时，这个值需要为True</p></li>
    <li><p><strong>wsgi.run_once</strong>：当server期望application对象在进程的生命周期内只被调用一次时，该值为True</p></li>
</ul>
<p>上面列出的这些内容已经包括了客户端请求的所有数据，足够application对象处理客户端请求了。</p>
<h3>start_resposne参数</h3>
<p>start_response是一个可调用对象，接收两个必选参数和一个可选参数：</p>
<ul>
    <li><p><strong>status</strong>: 一个字符串，表示HTTP响应状态字符串</p></li>
    <li><p><strong>response_headers</strong>: 一个列表，包含有如下形式的元组：(header_name, header_value)，用来表示HTTP响应的headers</p>
    </li>
    <li><p><strong>exc_info</strong>（可选）: 用于出错时，server需要返回给浏览器的信息</p></li>
</ul>
<p>
    当application对象根据environ参数的内容执行完业务逻辑后，就需要返回结果给server端。我们知道HTTP的响应需要包含status，headers和body，所以在application对象将body作为返回值return之前，需要先调用<code>start_response()</code>，将status和headers的内容返回给server，这同时也是告诉server，application对象要开始返回body了。
</p>
<h3>application对象的返回值</h3>
<p>
    application对象的返回值用于为HTTP响应提供body，如果没有body，那么可以返回None。如果有body的化，那么需要返回一个可迭代的对象。server端通过遍历这个可迭代对象可以获得body的全部内容。</p>
<h3>application demo</h3>
<p>PEP-3333中有一个application的实现demo，我把它再简化之后如下：</p>
<pre class="line-numbers  language-python"><code class="  language-python"><span
        class="token keyword">def</span> <span class="token function">simple_app</span><span
        class="token punctuation">(</span>environ<span class="token punctuation">,</span> start_response<span
        class="token punctuation">)</span><span class="token punctuation">:</span>
      status <span class="token operator">=</span> <span class="token string">'200 OK'</span>
      response_headers <span class="token operator">=</span> <span class="token punctuation">[</span><span
            class="token punctuation">(</span><span class="token string">'Content-type'</span><span
            class="token punctuation">,</span> <span class="token string">'text/plain'</span><span
            class="token punctuation">)</span><span class="token punctuation">]</span>
      start_response<span class="token punctuation">(</span>status<span class="token punctuation">,</span> response_headers<span
            class="token punctuation">)</span>
      <span class="token keyword">return</span> <span class="token punctuation">[</span><span class="token string">'hello, world'</span><span
            class="token punctuation">]</span>
<span aria-hidden="true"
      class="line-numbers-rows"><span></span><span></span><span></span><span></span><span></span></span></code><button
        class="VJbwyy" type="button" aria-label="复制代码"><i aria-label="icon: copy" class="anticon anticon-copy"><svg
        viewBox="64 64 896 896" focusable="false" class="" data-icon="copy" width="1em" height="1em"
        fill="currentColor" aria-hidden="true"><path
        d="M832 64H296c-4.4 0-8 3.6-8 8v56c0 4.4 3.6 8 8 8h496v688c0 4.4 3.6 8 8 8h56c4.4 0 8-3.6 8-8V96c0-17.7-14.3-32-32-32zM704 192H192c-17.7 0-32 14.3-32 32v530.7c0 8.5 3.4 16.6 9.4 22.6l173.3 173.3c2.2 2.2 4.7 4 7.4 5.5v1.9h4.2c3.5 1.3 7.2 2 11 2H704c17.7 0 32-14.3 32-32V224c0-17.7-14.3-32-32-32zM350 856.2L263.9 770H350v86.2zM664 888H414V746c0-22.1-17.9-40-40-40H232V264h432v624z"></path></svg></i></button></pre>
<p>可以将这段代码和前面的说明对照起来理解。</p>
<h2>再谈server如何调用application</h2>
<p>
    前面已经知道server如何定位到application的入口了，也知道了application的入口的形式以及application对象内部需要完成的工作。那么，我们还需要再说一下，<code>environ</code>和<code>start_response()</code>是需要在server端的生成和定义的，其中关于<code>start_response()</code>的部分在规范中也有明确的要求。这部分内容太长了，不适合放在本文中，有兴趣的读者可以去看下PEP-3333，里面有一段server端的demo实现。
</p>
<h1>WSGI中间件</h1>
<p><strong>WSGI Middleware</strong>（中间件）也是WSGI规范的一部分。上一章我们已经说明了WSGI的两个角色：server和application。那么middleware是一种运行在server和application中间的应用（一般都是Python应用）。middleware同时具备server和application角色，对于server来说，它是一个application；对于application来说，它是一个server。middleware并不修改server端和application端的规范，只是同时实现了这两个角色的功能而已。
</p>
<p>我们可以通过下图来说明middleware是如何工作的：</p>
<div class="image-package">
    <div class="image-container" style="max-width: 700px; max-height: 632px;">
        <div class="image-container-fill" style="padding-bottom: 87.9%;"></div>
        <div class="image-view" data-width="719" data-height="632"><img
                data-original-src="//upload-images.jianshu.io/upload_images/12899159-c08bb71a5e61b087.png"
                data-original-width="719" data-original-height="632" data-original-format="image/png"
                data-original-filesize="55852" class="image-loading" data-image-index="0" style="cursor: zoom-in;">
        </div>
    </div>
    <div class="image-caption">755097673-55c76463de432_articlex.png</div>
</div>
<p>上图中最上面的三个彩色框表示角色，中间的白色框表示操作，操作的发生顺序按照1 ~ 5进行了排序，我们直接对着上图来说明middleware是如何工作的：</p>
<ol>
    <li><p>Server收到客户端的HTTP请求后，生成了<code>environ_s</code>，并且已经定义了<code>start_response_s</code>。</p></li>
    <li><p>Server调用Middleware的application对象，传递的参数是<code>environ_s</code>和<code>start_response_s</code>。</p></li>
    <li><p>Middleware会根据<code>environ</code>执行业务逻辑，生成<code>environ_m</code>，并且已经定义了<code>start_response_m</code>。
    </p></li>
    <li><p>Middleware决定调用Application的application对象，传递参数是<code>environ_m</code>和<code>start_response_m</code>。Application的application对象处理完成后，会调用<code>start_response_m</code>并且返回结果给Middleware，存放在<code>result_m</code>中。
    </p></li>
    <li><p>Middleware处理<code>result_m</code>，然后生成<code>result_s</code>，接着调用<code>start_response_s</code>，并返回结果<code>result_s</code>给Server端。Server端获取到result_s后就可以发送结果给客户端了。
    </p></li>
</ol>
<p>从上面的流程可以看出middleware应用的几个特点：</p>
<ol>
    <li><p>Server认为middleware是一个application。</p></li>
    <li><p>Application认为middleware是一个server。</p></li>
    <li><p>Middleware可以有多层。</p></li>
</ol>
<p>因为Middleware能过处理所有经过的request和response，所以要做什么都可以，没有限制。比如可以检查request是否有非法内容，检查response是否有非法内容，为request加上特定的HTTP
    header等，这些都是可以的。</p>
<h1>WSGI的实现和部署</h1>
<p>要使用WSGI，需要分别实现server角色和application角色。</p>
<p>Application端的实现一般是由Python的各种框架来实现的，比如Django, web.py等，一般开发者不需要关心WSGI的实现，框架会会提供接口让开发者获取HTTP请求的内容以及发送HTTP响应。</p>
<p>
    Server端的实现会比较复杂一点，这个主要是因为软件架构的原因。一般常用的Web服务器，如Apache和nginx，都不会内置WSGI的支持，而是通过扩展来完成。比如Apache服务器，会通过扩展模块mod_wsgi来支持WSGI。Apache和mod_wsgi之间通过程序内部接口传递信息，mod_wsgi会实现WSGI的server端、进程管理以及对application的调用。Nginx上一般是用proxy的方式，用nginx的协议将请求封装好，发送给应用服务器，比如uWSGI，应用服务器会实现WSGI的服务端、进程管理以及对application的调用。</p>