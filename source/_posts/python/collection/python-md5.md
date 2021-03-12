---
title: "Python之MD5加密"
cover: "/img/lynk/56.jpg"
date:       2019-01-13
subtitle: "带你玩转各种加密"
tags:
	- Python
	- background
	- solution
---


<article class="baidu_pl">
    <!--python安装手册开始-->
    <!--python安装手册结束-->
    <!--####专栏广告位图文切换开始-->
    <!--####专栏广告位图文切换结束-->
    <div id="article_content" class="article_content clearfix">
        <link rel="stylesheet" href="https://csdnimg.cn/release/phoenix/template/css/ck_htmledit_views-833878f763.css">
        <div id="content_views" class="markdown_views">
            <!-- flowchart 箭头图标 勿删 -->
            <svg xmlns="http://www.w3.org/2000/svg" style="display: none;">
                <path stroke-linecap="round" d="M5,0 0,2.5 5,5z" id="raphael-marker-block"
                      style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);"></path>
            </svg>
            <blockquote>
                <p><strong>Python 3下MD5加密</strong></p>
            </blockquote>

            <pre class="prettyprint" name="code"><code class="hljs vala has-numbering" onclick="mdcp.copyCode(event)"
                                                       style="position: unset;">
                <span class="hljs-preprocessor"># 由于MD5模块在python3中被移除</span>
                <span class="hljs-preprocessor"># 在python3中使用hashlib模块进行md5操作</span>

import hashlib

<span class="hljs-preprocessor"># 待加密信息</span>
str = <span class="hljs-string">'this is a md5 test.'</span>

<span class="hljs-preprocessor"># 创建md5对象</span>
hl = hashlib.md5()

<span class="hljs-preprocessor"># Tips</span>
<span class="hljs-preprocessor"># 此处必须声明encode</span>
<span class="hljs-preprocessor"># 若写法为hl.update(str)  报错为： Unicode-objects must be encoded before hashing</span>
hl.update(str.encode(encoding=<span class="hljs-string">'utf-8'</span>))

print(<span class="hljs-string">'MD5加密前为 ：'</span> + str)
print(<span class="hljs-string">'MD5加密后为 ：'</span> + hl.hexdigest())<div class="hljs-button {2}" data-title="复制"></div></code><ul
                    class="pre-numbering" style=""><li style="color: rgb(153, 153, 153);">1</li><li
                    style="color: rgb(153, 153, 153);">2</li><li style="color: rgb(153, 153, 153);">3</li><li
                    style="color: rgb(153, 153, 153);">4</li><li style="color: rgb(153, 153, 153);">5</li><li
                    style="color: rgb(153, 153, 153);">6</li><li style="color: rgb(153, 153, 153);">7</li><li
                    style="color: rgb(153, 153, 153);">8</li><li style="color: rgb(153, 153, 153);">9</li><li
                    style="color: rgb(153, 153, 153);">10</li><li style="color: rgb(153, 153, 153);">11</li><li
                    style="color: rgb(153, 153, 153);">12</li><li style="color: rgb(153, 153, 153);">13</li><li
                    style="color: rgb(153, 153, 153);">14</li><li style="color: rgb(153, 153, 153);">15</li><li
                    style="color: rgb(153, 153, 153);">16</li><li style="color: rgb(153, 153, 153);">17</li><li
                    style="color: rgb(153, 153, 153);">18</li></ul></pre>

            <blockquote>
                <p><strong>运行结果</strong></p>
            </blockquote>

            <p>
                <img src="https://img-blog.csdn.net/20170704143346220?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcXFfODc4Nzk5NTc5/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast"
                     alt="这里写图片描述" title=""></p>

            <blockquote>
                <p><strong>封装Python3下MD5加密</strong></p>
            </blockquote>

            <pre class="prettyprint" name="code"><code class="hljs python has-numbering" onclick="mdcp.copyCode(event)"
                                                       style="position: unset;">
<span class="hljs-comment"># 生成MD5</span>
<span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">genearteMD5</span><span
        class="hljs-params">(str)</span>:</span>
    <span class="hljs-comment"># 创建md5对象</span>
    hl = hashlib.md5()

    <span class="hljs-comment"># Tips</span>
    <span class="hljs-comment"># 此处必须声明encode</span>
    <span class="hljs-comment"># 否则报错为：hl.update(str)    Unicode-objects must be encoded before hashing</span>
    hl.update(str.encode(encoding=<span class="hljs-string">'utf-8'</span>))

    print(<span class="hljs-string">'MD5加密前为 ：'</span> + str)
    print(<span class="hljs-string">'MD5加密后为 ：'</span> + hl.hexdigest())<div class="hljs-button {2}"
                                                                             data-title="复制"></div></code><ul
                    class="pre-numbering" style=""><li style="color: rgb(153, 153, 153);">1</li><li
                    style="color: rgb(153, 153, 153);">2</li><li style="color: rgb(153, 153, 153);">3</li><li
                    style="color: rgb(153, 153, 153);">4</li><li style="color: rgb(153, 153, 153);">5</li><li
                    style="color: rgb(153, 153, 153);">6</li><li style="color: rgb(153, 153, 153);">7</li><li
                    style="color: rgb(153, 153, 153);">8</li><li style="color: rgb(153, 153, 153);">9</li><li
                    style="color: rgb(153, 153, 153);">10</li><li style="color: rgb(153, 153, 153);">11</li><li
                    style="color: rgb(153, 153, 153);">12</li><li style="color: rgb(153, 153, 153);">13</li></ul></pre>

            <blockquote>
                <p><strong>Python2版本中带有MD5模块生成MD5 如下</strong></p>
            </blockquote>

            <pre class="prettyprint" name="code"><code class="hljs coffeescript has-numbering"
                                                       onclick="mdcp.copyCode(event)" style="position: unset;"><span
                    class="hljs-reserved">import</span> md5

src = <span class="hljs-string">'this is a md5 test.'</span>
m1 = md5.<span class="hljs-keyword">new</span>()
m1.update(src.encode(encoding=<span class="hljs-string">'utf-8'</span>))
<span class="hljs-built_in">print</span>(m1.hexdigest())
<div class="hljs-button {2}" data-title="复制"></div></code><ul class="pre-numbering" style=""><li
                    style="color: rgb(153, 153, 153);">1</li><li style="color: rgb(153, 153, 153);">2</li><li
                    style="color: rgb(153, 153, 153);">3</li><li style="color: rgb(153, 153, 153);">4</li><li
                    style="color: rgb(153, 153, 153);">5</li><li style="color: rgb(153, 153, 153);">6</li><li
                    style="color: rgb(153, 153, 153);">7</li></ul></pre>
        </div>
        <link href="https://csdnimg.cn/release/phoenix/mdeditor/markdown_views-b6c3c6d139.css" rel="stylesheet">
        
</article>