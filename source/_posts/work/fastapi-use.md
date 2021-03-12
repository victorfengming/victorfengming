---
title: "FastAPI框架使用"
cover: "/img/lynk/26.jpg"
date:       2020-03-05
subtitle: "快速的构建出一套高性能的api服务"
tags:
	- base
	- FastAPI
---


原文链接:https://www.cnblogs.com/neo98/p/12250730.html

<div class="post">
    <h1 class="postTitle">

        <a id="cb_post_title_url" class="postTitle2" href="https://www.cnblogs.com/neo98/p/12250730.html">FastAPI框架快速构建高性能的api服务</a>

    </h1>
    <div class="clear"></div>
    <div class="postBody">

        <div id="cnblogs_post_body" class="blogpost-body ">
            <p><a href="https://cloud.tencent.com/developer/article/1431448">https://cloud.tencent.com/developer/article/1431448</a>
            </p>
            <p>&nbsp;</p>
            <p>使用FastAPI可以非常快速的构建出一套高性能的api服务。下面通过实战演示一下：</p>
            <blockquote>
                <p>fastapi目前仅支持python 3.6+以上版本。</p>
            </blockquote>
            <h4 id="%E4%B8%80%E3%80%81%E5%AE%89%E8%A3%85fastapi%E5%92%8Cuvicorn"><strong>一、安装fastapi和uvicorn</strong>
            </h4>
            <pre class="prism-token token  language-javascript">pip install fastapi
pip install uvicorn</pre>
            <h4 id="%E4%BA%8C%E3%80%81%E6%96%B0%E5%BB%BA%E4%B8%80%E4%B8%AAmain.py%E6%96%87%E4%BB%B6%EF%BC%8C%E7%BC%96%E5%86%99%E5%A6%82%E4%B8%8B%E4%BB%A3%E7%A0%81">
                <strong>二、新建一个main.py文件，编写如下代码</strong></h4>
            <pre class="prism-token token  language-javascript"><span class="token keyword">from fastapi <span
                    class="token keyword">import FastAPI

app <span class="token operator">= <span class="token function">FastAPI<span class="token punctuation">(<span
                        class="token punctuation">)

@app<span class="token punctuation">.<span class="token keyword">get<span class="token punctuation">(<span
                            class="token string">"/"<span class="token punctuation">)
def <span class="token function">read_root<span class="token punctuation">(<span class="token punctuation">)<span
                                class="token punctuation">:
    <span class="token keyword">return <span class="token punctuation">{<span class="token string">"Hello"<span
            class="token punctuation">: <span class="token string">"World"<span class="token punctuation">}

@app<span class="token punctuation">.<span class="token keyword">get<span class="token punctuation">(<span
                class="token string">"/items/{item_id}"<span class="token punctuation">)
def <span class="token function">read_item<span class="token punctuation">(item_id<span
                    class="token punctuation">: int<span class="token punctuation">, q<span class="token punctuation">: str <span
                    class="token operator">= None<span class="token punctuation">)<span class="token punctuation">:
    <span class="token keyword">return <span class="token punctuation">{<span class="token string">"item_id"<span
            class="token punctuation">: item_id<span class="token punctuation">, <span class="token string">"q"<span
            class="token punctuation">: q<span
            class="token punctuation">}</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></pre>
            <h4 id="%E4%B8%89%E3%80%81%E8%BF%90%E8%A1%8C%E6%8E%A5%E5%8F%A3%E6%9C%8D%E5%8A%A1"><strong>三、运行接口服务</strong>
            </h4>
            <p>在命令行，执行下面的命令</p>
            <pre class="prism-token token  language-javascript">uvicorn main<span class="token punctuation">:app <span
                    class="token operator">--reload</span></span></pre>
            <h4 id="%E5%9B%9B%E3%80%81%E8%AF%B7%E6%B1%82%E6%8E%A5%E5%8F%A3"><strong>四、请求接口</strong></h4>
            <p>运行成功后在浏览器打开http://127.0.0.1:8000 ,你将在一个JSON格式响应结果：</p>
            <pre class="prism-token token  language-javascript"><span class="token punctuation">{<span
                    class="token string">'hello'<span class="token punctuation">:<span class="token string">'world'<span
                    class="token punctuation">}</span></span></span></span></span></pre>
            <p>再次在浏览器打开http://127.0.0.1:8000/items/5?q=somequery，你将在一个如下JSON格式响应结果：</p>
            <pre class="prism-token token  language-javascript"><span class="token punctuation">{<span
                    class="token string">'item_id'<span class="token punctuation">:<span class="token number">5<span
                    class="token punctuation">,<span class="token string">'q'<span class="token punctuation">:<span
                    class="token string">'somequery'<span class="token punctuation">}</span></span></span></span></span></span></span></span></span></pre>
            <h4 id="%E4%BA%94%E3%80%81%E5%8F%AF%E8%A7%86%E5%8C%96API%E6%96%87%E6%A1%A3"><strong>五、可视化API文档</strong></h4>
            <p>现在在浏览器中打开http://127.0.0.1:8000/docs,你会看到一个可以交互的api文档</p>
            <p>&nbsp;</p>
            <p>&nbsp;</p>
            <div>
                <div>
                    <p>你也可以其他方法的装饰器:</p>
                    <ul>
                        <li><code>@app.post()</code></li>
                        <li><code>@app.put()</code></li>
                        <li><code>@app.delete()</code></li>
                    </ul>
                    <p>还有一些比较少见的方法的装饰器:</p>
                    <ul>
                        <li><code>@app.options()</code></li>
                        <li><code>@app.head()</code></li>
                        <li><code>@app.patch()</code></li>
                        <li><code>@app.trace(</code></li>
                    </ul>
                </div>
                <br><br>
                <h4>建议</h4>
                <p>你可以使用任意的HTTP方法.</p>
                <p>FastAPI不强制任何特定函数。</p>
                <p>此处提供的信息，仅供参考，并非必需。</p>
                <p>例如，当使用 GraphQL , 你通常会只执行<code>post</code>方法</p>
                <p>&nbsp;</p>
                <div>
                    <div>
                        <h4>总结</h4>
                        <ul>
                            <li>Import <code>FastAPI</code>.</li>
                            <li>创建一个 <code>app</code> 实例.</li>
                            <li>编写一个 <strong>路径操作装饰器</strong> (比如<code>@app.get("/")</code>).</li>
                            <li>编写一个<strong>路径操作函数</strong> (比如上方的 <code>def root(): ...</code> ).</li>
                            <li>运行开发服务器(比如<code>uvicorn main:app --reload</code>).</li>

                        </ul>

                    </div>

                </div>

            </div>
            
    </div>
</div>