---
title: "Python中的docstring"
cover: "/img/lynk/86.jpg"
date:       2019-11-28
subtitle: "养成写文档的好习惯"
tags:
	- Python
	- solution
	- interview
---

<div style="line-height:28px;word-wrap:break-word">
    <h1 style="color:#903;line-height:36px;margin-bottom:4px">使用Python的docstring</h1>
    <p style="color:#aaa">
        2017年8月25日<span> / </span>11,653次阅读<br><a style="color:#903" target="_blank"
                                                  href="https://www.maixj.net/tag/py">Python</a></p>

    <div>
        <div id="wz"><p>程序员一直以来都有一个烦恼，他们只想写代码，不想写文档。他们说：代码就表达了我的思想和灵魂。</p>
            <p>小公司相对随意一些，可以先写代码调试，但是最后老板害怕程序员离职造成“青黄不接”，还是会要求补上文档。大公司要求更高，要先写文档，评审通过，然后再开始编码。有的程序员整天都在写文档，苦不堪言。</p>
            <p>Python提出了一个方案，叫docstring，来试图解决这个问题。即编写代码，同时也能写出文档，保持代码和文档的一致。</p>
            <p>
                Python提出的这个方案其实并不新鲜，docstring说白了就是一堆代码中的注释。任何编程语言都有注释的好不好！！不过，Python的docstring可以通过help函数直接输出一份有格式的文档，这个就厉害了。代码写完，注释写完，一个help调用，就有文档看了。</p>
            <p>&nbsp;</p>
            <p><strong>docstring可以写在三个地方：模块或包，对象，函数。</strong></p>
            <p>（以下示例使用著名的requests包）</p>
            <p>&nbsp;</p>
            <p>对于模块，docstring就是在模块文件的最前面，如下示例：</p>
            <pre><code class="python hljs"><span class="hljs-comment"># -*- coding: utf-8 -*-</span>

<span class="hljs-string">"""
requests.api
~~~~~~~~~~~~

This module implements the Requests API.

:copyright: (c) 2012 by Kenneth Reitz.
:license: Apache2, see LICENSE for more details.
"""</span>

<span class="hljs-keyword">from</span> . <span class="hljs-keyword">import</span> sessions</code></pre>
            <p><span style="color: #ff0000;"><strong>docstring使用三个双引号（”），triple double quote for docstring，这是PEP0257里的约定。</strong></span>
            </p>
            <p>&nbsp;</p>
            <p>对于包，docstring就是在package的__init__.py这个文件的任何语句的前面（<strong>docstring的前面还可以有#注释</strong>），如下示例：</p>
            <pre><code class="python hljs"><span class="hljs-comment"># -*- coding: utf-8 -*-</span>

<span class="hljs-comment">#   __</span>
<span class="hljs-comment">#  /__)  _  _     _   _ _/   _</span>
<span class="hljs-comment"># / (   (- (/ (/ (- _)  /  _)</span>
<span class="hljs-comment">#          /</span>

<span class="hljs-string">"""
Requests HTTP Library
~~~~~~~~~~~~~~~~~~~~~

Requests is an HTTP library, written in Python, for human beings. Basic GET
usage:

   &gt;&gt;&gt; import requests
   &gt;&gt;&gt; r = requests.get('https://www.python.org')
   &gt;&gt;&gt; r.status_code
   200
   &gt;&gt;&gt; 'Python is a programming language' in r.content
   True

<span class="hljs-meta">... </span>or POST:

   &gt;&gt;&gt; payload = dict(key1='value1', key2='value2')
   &gt;&gt;&gt; r = requests.post('http://httpbin.org/post', data=payload)
   &gt;&gt;&gt; print(r.text)
   {
     ...
     "form": {
       "key2": "value2",
       "key1": "value1"
     },
     ...
   }

The other HTTP methods are supported - see `requests.api`. Full documentation
is at &lt;http://python-requests.org&gt;.

:copyright: (c) 2017 by Kenneth Reitz.
:license: Apache 2.0, see LICENSE for more details.
"""</span>

<span class="hljs-keyword">import</span> urllib3</code></pre>
            <p>&nbsp;</p>
            <p>对于函数，docstring就是在函数定义的最前面，如下示例：</p>
            <pre><code class="python hljs"><span class="hljs-function"><span class="hljs-keyword">def</span> <span
                    class="hljs-title">get</span><span class="hljs-params">(url, params=None, **kwargs)</span>:</span>
    <span class="hljs-string">r"""Sends a GET request.

    :param url: URL for the new :class:`Request` object.
    :param params: (optional) Dictionary or bytes to be sent in the query string for the :class:`Request`.
    :param \*\*kwargs: Optional arguments that ``request`` takes.
    :return: :class:`Response &lt;Response&gt;` object
    :rtype: requests.Response
    """</span>

    kwargs.setdefault(<span class="hljs-string">'allow_redirects'</span>, <span class="hljs-keyword">True</span>)
    <span class="hljs-keyword">return</span> request(<span class="hljs-string">'get'</span>, url, params=params, **kwargs)</code></pre>
            <p><strong>注意上例的三个双引号前有个r，r是raw的意思，表示这个字符串里面的\就是它自己，不是用来转意的。</strong></p>
            <p>&nbsp;</p>
            <p>对于对象定义，docstring就是在class定义的最前面，如下示例：</p>
            <pre><code class="python hljs"><span class="hljs-class"><span class="hljs-keyword">class</span> <span
                    class="hljs-title">Timeout</span><span class="hljs-params">(RequestException)</span>:</span>
    <span class="hljs-string">"""The request timed out.

    Catching this error will catch both
    :exc:`~requests.exceptions.ConnectTimeout` and
    :exc:`~requests.exceptions.ReadTimeout` errors.
    """</span>


<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">ConnectTimeout</span><span
        class="hljs-params">(ConnectionError, Timeout)</span>:</span>
    <span class="hljs-string">"""The request timed out while trying to connect to the remote server.

    Requests that produced this error are safe to retry.
    """</span>
</code></pre>
            <p>&nbsp;</p>
            <p>还有一种单行docstring的写法，如下：</p>
            <pre><code class="python hljs"><span class="hljs-function"><span class="hljs-keyword">def</span> <span
                    class="hljs-title">getStartLink</span><span class="hljs-params">()</span>:</span>
    <span class="hljs-string">"""get start link"""</span>
    startLink = str()

    <span class="hljs-comment"># get start link value</span>
    <span class="hljs-keyword">if</span> __name__ == <span class="hljs-string">"__main__"</span>:</code></pre>
            <p>&nbsp;</p>
            <p>Python builtin的help函数主要是在交互模式下使用，在交互模式下，使用help，就能够看到文档中的这些被称为docstring的注释，被一种良好的格式显示出来。</p>
            <p>在调整代码的时候，维护注释，维护docstring，进而保持代码和文档（help函数的输出）一致，麦新杰认为是一种简化的思想。docstring不是强制的，如果不写，help函数的输出就是空空的。</p>
            <p>下面是help(requests)的输出：</p>
            <pre><code class="python hljs">&gt;&gt;&gt;
<span class="hljs-meta">&gt;&gt;&gt; </span><span class="hljs-keyword">import</span> requests
<span class="hljs-meta">&gt;&gt;&gt; </span>help(requests)
Help on package requests:

NAME
    requests

DESCRIPTION
    Requests HTTP Library
    ~~~~~~~~~~~~~~~~~~~~~

    Requests <span class="hljs-keyword">is</span> an HTTP library, written <span class="hljs-keyword">in</span> Python, <span
                        class="hljs-keyword">for</span> human beings. Basic GET
    usage:

       &gt;&gt;&gt; <span class="hljs-keyword">import</span> requests
       &gt;&gt;&gt; r = requests.get(<span class="hljs-string">'https://www.python.org'</span>)
       &gt;&gt;&gt; r.status_code
       <span class="hljs-number">200</span>
       &gt;&gt;&gt; <span class="hljs-string">'Python is a programming language'</span> <span
                        class="hljs-keyword">in</span> r.content
       <span class="hljs-keyword">True</span>

    ... <span class="hljs-keyword">or</span> POST:

       &gt;&gt;&gt; payload = dict(key1=<span class="hljs-string">'value1'</span>, key2=<span class="hljs-string">'value2'</span>)
       &gt;&gt;&gt; r = requests.post(<span class="hljs-string">'http://httpbin.org/post'</span>, data=payload)
       &gt;&gt;&gt; print(r.text)
       {
         ...
         <span class="hljs-string">"form"</span>: {
           <span class="hljs-string">"key2"</span>: <span class="hljs-string">"value2"</span>,
           <span class="hljs-string">"key1"</span>: <span class="hljs-string">"value1"</span>
         },
         ...
       }

    The other HTTP methods are supported - see `requests.api`. Full documentatio
n
    <span class="hljs-keyword">is</span> at &lt;http://python-requests.org&gt;.

    :copyright: (c) <span class="hljs-number">2017</span> by Kenneth Reitz.
    :license: Apache <span class="hljs-number">2.0</span>, see LICENSE <span class="hljs-keyword">for</span> more details.

PACKAGE CONTENTS
    __version__
    _internal_utils
    adapters
    api
    auth</code></pre>
            <p>看description部分，这就是写requests包的__init__.py文档中的docstring。</p>
            <p>而且还可以看出，help函数不仅输出docstring，还有一些其它的格式化的输出信息，非常handy呀。</p>
            <p>&nbsp;</p>
            <p>专业的Python docstring文档，请参考<a href="https://www.python.org/dev/peps/pep-0257/" target="_blank"
                                           rel="noopener">PEP257</a></p>
            <p>您可能要先看一下：<a href="https://www.maixj.net/ict/python-pep-13746" target="_blank"
                           rel="noopener">什么是PEP文档？</a></p>
            <p>&nbsp;</p>
            <p>Python这种语言简单易学，有个原因就是它将一些复杂的事情简化了，比如非强制的docstring，比如强制缩进。</p>
        </div>
    </div>
</div>