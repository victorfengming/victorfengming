---
title: "了解FastAPI结构"
date:       2020-03-05
subtitle: "python的api框架"
tags:
	- base
	- FastAPI
---


原文链接:https://www.jianshu.com/p/94710ed35b92

<h2>一、编写一个简单的FastAPI程序</h2>
<p>最简单的FastAPI文件可能如下：</p>
<div class="_2Uzcx_"><button class="VJbwyy" type="button" aria-label="复制代码"><i aria-label="icon: copy" class="anticon anticon-copy"><svg viewBox="64 64 896 896" focusable="false" class="" data-icon="copy" width="1em" height="1em" fill="currentColor" aria-hidden="true"><path d="M832 64H296c-4.4 0-8 3.6-8 8v56c0 4.4 3.6 8 8 8h496v688c0 4.4 3.6 8 8 8h56c4.4 0 8-3.6 8-8V96c0-17.7-14.3-32-32-32zM704 192H192c-17.7 0-32 14.3-32 32v530.7c0 8.5 3.4 16.6 9.4 22.6l173.3 173.3c2.2 2.2 4.7 4 7.4 5.5v1.9h4.2c3.5 1.3 7.2 2 11 2H704c17.7 0 32-14.3 32-32V224c0-17.7-14.3-32-32-32zM350 856.2L263.9 770H350v86.2zM664 888H414V746c0-22.1-17.9-40-40-40H232V264h432v624z"></path></svg></i></button><pre class="line-numbers  language-python"><code class="  language-python"><span class="token keyword">from</span> fastapi <span class="token keyword">import</span> FastAPI

app <span class="token operator">=</span> FastAPI<span class="token punctuation">(</span><span class="token punctuation">)</span>

@app<span class="token punctuation">.</span>get<span class="token punctuation">(</span><span class="token string">"/"</span><span class="token punctuation">)</span>
<span class="token keyword">async</span> <span class="token keyword">def</span> <span class="token function">root</span><span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token punctuation">:</span>
    <span class="token keyword">return</span> <span class="token punctuation">{</span><span class="token string">"message"</span><span class="token punctuation">:</span> <span class="token string">"Hello World"</span><span class="token punctuation">}</span>
<span aria-hidden="true" class="line-numbers-rows"><span></span><span></span><span></span><span></span><span></span><span></span><span></span></span></code></pre></div>
<p>将上面代码块复制到 <code>main.py</code>.</p>
<p>启动服务：</p>
<div class="_2Uzcx_"><button class="VJbwyy" type="button" aria-label="复制代码"><i aria-label="icon: copy" class="anticon anticon-copy"><svg viewBox="64 64 896 896" focusable="false" class="" data-icon="copy" width="1em" height="1em" fill="currentColor" aria-hidden="true"><path d="M832 64H296c-4.4 0-8 3.6-8 8v56c0 4.4 3.6 8 8 8h496v688c0 4.4 3.6 8 8 8h56c4.4 0 8-3.6 8-8V96c0-17.7-14.3-32-32-32zM704 192H192c-17.7 0-32 14.3-32 32v530.7c0 8.5 3.4 16.6 9.4 22.6l173.3 173.3c2.2 2.2 4.7 4 7.4 5.5v1.9h4.2c3.5 1.3 7.2 2 11 2H704c17.7 0 32-14.3 32-32V224c0-17.7-14.3-32-32-32zM350 856.2L263.9 770H350v86.2zM664 888H414V746c0-22.1-17.9-40-40-40H232V264h432v624z"></path></svg></i></button><pre class="line-numbers  language-css"><code class="  language-css">uvicorn <span class="token property">main</span><span class="token punctuation">:</span>app --reload
<span aria-hidden="true" class="line-numbers-rows"><span></span></span></code></pre></div>
<p><strong>注意：</strong></p>
<p><code>uvicorn main:app</code> 命令指:</p>
<ul>
<li>
<code>main</code>: <code>main.py</code> 文件(也可理解为Python模块).</li>
<li>
<code>app</code>: <code>main.py</code> 中<code>app = FastAPI()</code>语句创建的app对象.</li>
<li>
<code>--reload</code>: 在代码改变后重启服务器，只能在开发的时候使用</li>
</ul>
<p>你将会看到如下的输出：</p>
<div class="_2Uzcx_"><button class="VJbwyy" type="button" aria-label="复制代码"><i aria-label="icon: copy" class="anticon anticon-copy"><svg viewBox="64 64 896 896" focusable="false" class="" data-icon="copy" width="1em" height="1em" fill="currentColor" aria-hidden="true"><path d="M832 64H296c-4.4 0-8 3.6-8 8v56c0 4.4 3.6 8 8 8h496v688c0 4.4 3.6 8 8 8h56c4.4 0 8-3.6 8-8V96c0-17.7-14.3-32-32-32zM704 192H192c-17.7 0-32 14.3-32 32v530.7c0 8.5 3.4 16.6 9.4 22.6l173.3 173.3c2.2 2.2 4.7 4 7.4 5.5v1.9h4.2c3.5 1.3 7.2 2 11 2H704c17.7 0 32-14.3 32-32V224c0-17.7-14.3-32-32-32zM350 856.2L263.9 770H350v86.2zM664 888H414V746c0-22.1-17.9-40-40-40H232V264h432v624z"></path></svg></i></button><pre class="line-numbers  language-csharp"><code class="  language-csharp">INFO<span class="token punctuation">:</span> <span class="token class-name">Started</span> reloader process <span class="token punctuation">[</span><span class="token number">17961</span><span class="token punctuation">]</span>
INFO<span class="token punctuation">:</span> <span class="token class-name">Started</span> server process <span class="token punctuation">[</span><span class="token number">17962</span><span class="token punctuation">]</span>
INFO<span class="token punctuation">:</span> <span class="token class-name">Waiting</span> <span class="token keyword">for</span> application startup<span class="token punctuation">.</span>
INFO<span class="token punctuation">:</span> <span class="token class-name">Uvicorn</span> running on http<span class="token punctuation">:</span><span class="token operator">/</span><span class="token operator">/</span><span class="token number">127.0</span><span class="token number">.0</span><span class="token number">.1</span><span class="token punctuation">:</span><span class="token number">8000</span> <span class="token punctuation">(</span><span class="token class-name">Press</span> CTRL<span class="token operator">+</span><span class="token class-name">C</span> to quit<span class="token punctuation">)</span> <span class="token operator">&lt;</span><span class="token operator">/</span>pre<span class="token operator">&gt;</span>
<span aria-hidden="true" class="line-numbers-rows"><span></span><span></span><span></span><span></span></span></code></pre></div>
<p>最后一句表明你的app服务在本地的URL地址。</p>
<h2>二、检查</h2>
<p>打开你的浏览器，输入 <a href="https://links.jianshu.com/go?to=http%3A%2F%2F127.0.0.1%3A8000%2F" target="_blank">http://127.0.0.1:8000</a>.</p>
<p>你将会看见JSON响应：</p>
<div class="_2Uzcx_"><button class="VJbwyy" type="button" aria-label="复制代码"><i aria-label="icon: copy" class="anticon anticon-copy"><svg viewBox="64 64 896 896" focusable="false" class="" data-icon="copy" width="1em" height="1em" fill="currentColor" aria-hidden="true"><path d="M832 64H296c-4.4 0-8 3.6-8 8v56c0 4.4 3.6 8 8 8h496v688c0 4.4 3.6 8 8 8h56c4.4 0 8-3.6 8-8V96c0-17.7-14.3-32-32-32zM704 192H192c-17.7 0-32 14.3-32 32v530.7c0 8.5 3.4 16.6 9.4 22.6l173.3 173.3c2.2 2.2 4.7 4 7.4 5.5v1.9h4.2c3.5 1.3 7.2 2 11 2H704c17.7 0 32-14.3 32-32V224c0-17.7-14.3-32-32-32zM350 856.2L263.9 770H350v86.2zM664 888H414V746c0-22.1-17.9-40-40-40H232V264h432v624z"></path></svg></i></button><pre class="line-numbers  language-json"><code class="  language-json"><span class="token punctuation">{</span><span class="token property">"hello"</span><span class="token operator">:</span> <span class="token string">"world"</span><span class="token punctuation">}</span>
<span aria-hidden="true" class="line-numbers-rows"><span></span></span></code></pre></div>
<h2>三、API交互文档</h2>
<p>现在转到 <a href="https://links.jianshu.com/go?to=http%3A%2F%2F127.0.0.1%3A8000%2Fdocs" target="_blank">http://127.0.0.1:8000/docs</a>.</p>
<p>你将会看到自动生成的API交互文档(由 <a href="https://links.jianshu.com/go?to=https%3A%2F%2Fgithub.com%2Fswagger-api%2Fswagger-ui" target="_blank">Swagger UI</a>提供):<br>
</p><div class="image-package">
<div class="image-container" style="max-width: 700px; max-height: 788px; background-color: transparent;">
<div class="image-container-fill" style="padding-bottom: 112.5%;"></div>
<div class="image-view" data-width="960" data-height="1080"><img data-original-src="//upload-images.jianshu.io/upload_images/12745724-93152ffa97ca22b2.png" data-original-width="960" data-original-height="1080" data-original-format="image/png" data-original-filesize="94592" data-image-index="0" style="cursor: zoom-in;" class="" src="//upload-images.jianshu.io/upload_images/12745724-93152ffa97ca22b2.png?imageMogr2/auto-orient/strip|imageView2/2/w/960/format/webp"></div>
</div>
<div class="image-caption"></div>
</div><p></p>
<h2>四、可选的API文档</h2>
<p>现在，转到 <a href="https://links.jianshu.com/go?to=http%3A%2F%2F127.0.0.1%3A8000%2Fredoc" target="_blank">http://127.0.0.1:8000/redoc</a>.</p>
<p>你将会看到自动生成的可选的API文档(由(provided by <a href="https://links.jianshu.com/go?to=https%3A%2F%2Fgithub.com%2FRebilly%2FReDoc" target="_blank">ReDoc</a>提供):</p>
<div class="image-package">
<div class="image-container" style="max-width: 700px; max-height: 788px; background-color: transparent;">
<div class="image-container-fill" style="padding-bottom: 112.5%;"></div>
<div class="image-view" data-width="960" data-height="1080"><img data-original-src="//upload-images.jianshu.io/upload_images/12745724-48422ef751879020.png" data-original-width="960" data-original-height="1080" data-original-format="image/png" data-original-filesize="68468" data-image-index="1" style="cursor: zoom-in;" class="" src="//upload-images.jianshu.io/upload_images/12745724-48422ef751879020.png?imageMogr2/auto-orient/strip|imageView2/2/w/960/format/webp"></div>
</div>
<div class="image-caption">ReDoc</div>
</div>
<h2>五、OpenAPI</h2>
<p><strong>FastAPI</strong>使用用于定义API的OpenAPI标准为您的所有API生成“模式”。</p>
<h4>1. "模式"</h4>
<p>模式”是事物的定义或描述。 不是实现它的代码，只是抽象描述。</p>
<h4>2. API "模式"</h4>
<p>在这种情况下，OpenAPI是规定如何定义API模式的规范。</p>
<p>此OpenAPI架构将包括您的API路径，以及路径中包含的可能参数等。</p>
<h4>3. 数据 "模式"</h4>
<p>术语“模式”也可能表示某些数据的形状，例如JSON内容。</p>
<p>在这种情况下，这将意味着JSON属性及其具有的数据类型，等等。</p>
<h4>4. OpenAPI 和 JSON 模式</h4>
<ul>
<li>
<strong>OpenAPI</strong> ：为你的API定义API模式. 并且这个模式包含了API传输数据的定义和API接收数据的定义。</li>
<li>
<strong>JSON 模式</strong>, the standard for JSON data schemas.</li>
</ul>
<h4>5. 检查</h4>
<p>如果你对原生的OpenAPI是什么样子感兴趣，它只是一个自动生成的JSON，其中包含所有API的描述。</p>
<p>你可以直接转到: <a href="https://links.jianshu.com/go?to=http%3A%2F%2F127.0.0.1%3A8000%2Fopenapi.json" target="_blank">http://127.0.0.1:8000/openapi.json</a>.</p>
<p>它将会展示可能是这样开头的JSON：</p>
<div class="_2Uzcx_"><button class="VJbwyy" type="button" aria-label="复制代码"><i aria-label="icon: copy" class="anticon anticon-copy"><svg viewBox="64 64 896 896" focusable="false" class="" data-icon="copy" width="1em" height="1em" fill="currentColor" aria-hidden="true"><path d="M832 64H296c-4.4 0-8 3.6-8 8v56c0 4.4 3.6 8 8 8h496v688c0 4.4 3.6 8 8 8h56c4.4 0 8-3.6 8-8V96c0-17.7-14.3-32-32-32zM704 192H192c-17.7 0-32 14.3-32 32v530.7c0 8.5 3.4 16.6 9.4 22.6l173.3 173.3c2.2 2.2 4.7 4 7.4 5.5v1.9h4.2c3.5 1.3 7.2 2 11 2H704c17.7 0 32-14.3 32-32V224c0-17.7-14.3-32-32-32zM350 856.2L263.9 770H350v86.2zM664 888H414V746c0-22.1-17.9-40-40-40H232V264h432v624z"></path></svg></i></button><pre class="line-numbers  language-bash"><code class="  language-bash">{
    "openapi": "3.0.2",
    "info": {
        "title": "Fast API",
        "version": "0.1.0"
    },
    "paths": {
        "/items/": {
            "get": {
                "responses": {
                    "200": {
                        "description": "Successful Response",
                        "content": {
                            "application/json": {

...
<span aria-hidden="true" class="line-numbers-rows"><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span></span></code></pre></div>
<h4>6. 做什么的？</h4>
<p>此OpenAPI架构是为所包括的2个交互式文档系统提供支持的。</p>
<p>并且有数十种替代方案，全部基于OpenAPI。 您可以轻松地将这些替代方案中的任何一种添加到使用** FastAPI **构建的应用程序中。</p>
<p>您还可以使用它为与您的API通信的客户端自动生成代码。 例如，前端，移动或物联网应用程序。</p>
<h2>六、概括</h2>
<h3>Step 1: import <code>FastAPI</code>
</h3>
<div class="_2Uzcx_"><button class="VJbwyy" type="button" aria-label="复制代码"><i aria-label="icon: copy" class="anticon anticon-copy"><svg viewBox="64 64 896 896" focusable="false" class="" data-icon="copy" width="1em" height="1em" fill="currentColor" aria-hidden="true"><path d="M832 64H296c-4.4 0-8 3.6-8 8v56c0 4.4 3.6 8 8 8h496v688c0 4.4 3.6 8 8 8h56c4.4 0 8-3.6 8-8V96c0-17.7-14.3-32-32-32zM704 192H192c-17.7 0-32 14.3-32 32v530.7c0 8.5 3.4 16.6 9.4 22.6l173.3 173.3c2.2 2.2 4.7 4 7.4 5.5v1.9h4.2c3.5 1.3 7.2 2 11 2H704c17.7 0 32-14.3 32-32V224c0-17.7-14.3-32-32-32zM350 856.2L263.9 770H350v86.2zM664 888H414V746c0-22.1-17.9-40-40-40H232V264h432v624z"></path></svg></i></button><pre class="line-numbers  language-python"><code class="  language-python"><span class="token keyword">from</span> fastapi <span class="token keyword">import</span> FastAPI 
app <span class="token operator">=</span> FastAPI<span class="token punctuation">(</span><span class="token punctuation">)</span>

@app<span class="token punctuation">.</span>get<span class="token punctuation">(</span><span class="token string">"/"</span><span class="token punctuation">)</span>
<span class="token keyword">async</span> <span class="token keyword">def</span> <span class="token function">root</span><span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token punctuation">:</span>
    <span class="token keyword">return</span> <span class="token punctuation">{</span><span class="token string">"message"</span><span class="token punctuation">:</span> <span class="token string">"Hello World"</span><span class="token punctuation">}</span>
<span aria-hidden="true" class="line-numbers-rows"><span></span><span></span><span></span><span></span><span></span><span></span></span></code></pre></div>
<p><code>FastAPI</code> 是为您的API提供所有功能的一个Python类。</p>
<blockquote>
<p><strong>技术细节</strong></p>
<ul>
<li>FastAPI是直接从Starlette继承的类。</li>
</ul>
<p>您也可以将所有Starlette功能与FastAPI一起使用.</p>
</blockquote>
<h3>Step 2: 创建一个 <code>FastAPI</code> 实例</h3>
<div class="_2Uzcx_"><button class="VJbwyy" type="button" aria-label="复制代码"><i aria-label="icon: copy" class="anticon anticon-copy"><svg viewBox="64 64 896 896" focusable="false" class="" data-icon="copy" width="1em" height="1em" fill="currentColor" aria-hidden="true"><path d="M832 64H296c-4.4 0-8 3.6-8 8v56c0 4.4 3.6 8 8 8h496v688c0 4.4 3.6 8 8 8h56c4.4 0 8-3.6 8-8V96c0-17.7-14.3-32-32-32zM704 192H192c-17.7 0-32 14.3-32 32v530.7c0 8.5 3.4 16.6 9.4 22.6l173.3 173.3c2.2 2.2 4.7 4 7.4 5.5v1.9h4.2c3.5 1.3 7.2 2 11 2H704c17.7 0 32-14.3 32-32V224c0-17.7-14.3-32-32-32zM350 856.2L263.9 770H350v86.2zM664 888H414V746c0-22.1-17.9-40-40-40H232V264h432v624z"></path></svg></i></button><pre class="line-numbers  language-python"><code class="  language-python">app <span class="token operator">=</span> FastAPI<span class="token punctuation">(</span><span class="token punctuation">)</span> 

@app<span class="token punctuation">.</span>get<span class="token punctuation">(</span><span class="token string">"/"</span><span class="token punctuation">)</span>
<span class="token keyword">async</span> <span class="token keyword">def</span> <span class="token function">root</span><span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token punctuation">:</span>
    <span class="token keyword">return</span> <span class="token punctuation">{</span><span class="token string">"message"</span><span class="token punctuation">:</span> <span class="token string">"Hello World"</span><span class="token punctuation">}</span>
<span aria-hidden="true" class="line-numbers-rows"><span></span><span></span><span></span><span></span><span></span></span></code></pre></div>
<p>上面代码中<code>app</code> 变量就是<code>FastAPI</code>的一个实例.</p>
<p>这将是创建所有API的主要交互点。</p>
<p>该app与uvicorn在命令中引用的同一个app：</p>
<div class="_2Uzcx_"><button class="VJbwyy" type="button" aria-label="复制代码"><i aria-label="icon: copy" class="anticon anticon-copy"><svg viewBox="64 64 896 896" focusable="false" class="" data-icon="copy" width="1em" height="1em" fill="currentColor" aria-hidden="true"><path d="M832 64H296c-4.4 0-8 3.6-8 8v56c0 4.4 3.6 8 8 8h496v688c0 4.4 3.6 8 8 8h56c4.4 0 8-3.6 8-8V96c0-17.7-14.3-32-32-32zM704 192H192c-17.7 0-32 14.3-32 32v530.7c0 8.5 3.4 16.6 9.4 22.6l173.3 173.3c2.2 2.2 4.7 4 7.4 5.5v1.9h4.2c3.5 1.3 7.2 2 11 2H704c17.7 0 32-14.3 32-32V224c0-17.7-14.3-32-32-32zM350 856.2L263.9 770H350v86.2zM664 888H414V746c0-22.1-17.9-40-40-40H232V264h432v624z"></path></svg></i></button><pre class="line-numbers  language-css"><code class="  language-css">uvicorn <span class="token property">main</span><span class="token punctuation">:</span>app --reload
<span aria-hidden="true" class="line-numbers-rows"><span></span></span></code></pre></div>
<p>如果你创建的app像这样：</p>
<div class="_2Uzcx_"><button class="VJbwyy" type="button" aria-label="复制代码"><i aria-label="icon: copy" class="anticon anticon-copy"><svg viewBox="64 64 896 896" focusable="false" class="" data-icon="copy" width="1em" height="1em" fill="currentColor" aria-hidden="true"><path d="M832 64H296c-4.4 0-8 3.6-8 8v56c0 4.4 3.6 8 8 8h496v688c0 4.4 3.6 8 8 8h56c4.4 0 8-3.6 8-8V96c0-17.7-14.3-32-32-32zM704 192H192c-17.7 0-32 14.3-32 32v530.7c0 8.5 3.4 16.6 9.4 22.6l173.3 173.3c2.2 2.2 4.7 4 7.4 5.5v1.9h4.2c3.5 1.3 7.2 2 11 2H704c17.7 0 32-14.3 32-32V224c0-17.7-14.3-32-32-32zM350 856.2L263.9 770H350v86.2zM664 888H414V746c0-22.1-17.9-40-40-40H232V264h432v624z"></path></svg></i></button><pre class="line-numbers  language-python"><code class="  language-python">my_awesome_api <span class="token operator">=</span> FastAPI<span class="token punctuation">(</span><span class="token punctuation">)</span> 

@my_awesome_api<span class="token punctuation">.</span>get<span class="token punctuation">(</span><span class="token string">"/"</span><span class="token punctuation">)</span>
<span class="token keyword">async</span> <span class="token keyword">def</span> <span class="token function">root</span><span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token punctuation">:</span>
    <span class="token keyword">return</span> <span class="token punctuation">{</span><span class="token string">"message"</span><span class="token punctuation">:</span> <span class="token string">"Hello World"</span><span class="token punctuation">}</span>
<span aria-hidden="true" class="line-numbers-rows"><span></span><span></span><span></span><span></span><span></span></span></code></pre></div>
<p>将上段代码保存到 <code>main.py</code>, 然后你可以这样启动 <code>uvicorn</code> :</p>
<div class="_2Uzcx_"><button class="VJbwyy" type="button" aria-label="复制代码"><i aria-label="icon: copy" class="anticon anticon-copy"><svg viewBox="64 64 896 896" focusable="false" class="" data-icon="copy" width="1em" height="1em" fill="currentColor" aria-hidden="true"><path d="M832 64H296c-4.4 0-8 3.6-8 8v56c0 4.4 3.6 8 8 8h496v688c0 4.4 3.6 8 8 8h56c4.4 0 8-3.6 8-8V96c0-17.7-14.3-32-32-32zM704 192H192c-17.7 0-32 14.3-32 32v530.7c0 8.5 3.4 16.6 9.4 22.6l173.3 173.3c2.2 2.2 4.7 4 7.4 5.5v1.9h4.2c3.5 1.3 7.2 2 11 2H704c17.7 0 32-14.3 32-32V224c0-17.7-14.3-32-32-32zM350 856.2L263.9 770H350v86.2zM664 888H414V746c0-22.1-17.9-40-40-40H232V264h432v624z"></path></svg></i></button><pre class="line-numbers  language-css"><code class="  language-css">uvicorn <span class="token property">main</span><span class="token punctuation">:</span>my_awesome_api --reload
<span aria-hidden="true" class="line-numbers-rows"><span></span></span></code></pre></div>
<h3>Step 3: 创建一个path 操作</h3>
<h4>Path</h4>
<p>这里的“路径”是指URL的最后一部分，从第一个<code>/</code>开始。</p>
<p>因此，在一个URL中：</p>
<div class="_2Uzcx_"><button class="VJbwyy" type="button" aria-label="复制代码"><i aria-label="icon: copy" class="anticon anticon-copy"><svg viewBox="64 64 896 896" focusable="false" class="" data-icon="copy" width="1em" height="1em" fill="currentColor" aria-hidden="true"><path d="M832 64H296c-4.4 0-8 3.6-8 8v56c0 4.4 3.6 8 8 8h496v688c0 4.4 3.6 8 8 8h56c4.4 0 8-3.6 8-8V96c0-17.7-14.3-32-32-32zM704 192H192c-17.7 0-32 14.3-32 32v530.7c0 8.5 3.4 16.6 9.4 22.6l173.3 173.3c2.2 2.2 4.7 4 7.4 5.5v1.9h4.2c3.5 1.3 7.2 2 11 2H704c17.7 0 32-14.3 32-32V224c0-17.7-14.3-32-32-32zM350 856.2L263.9 770H350v86.2zM664 888H414V746c0-22.1-17.9-40-40-40H232V264h432v624z"></path></svg></i></button><pre class="line-numbers  language-cpp"><code class="  language-cpp">https<span class="token operator">:</span><span class="token operator">/</span><span class="token operator">/</span>example<span class="token punctuation">.</span>com<span class="token operator">/</span>items<span class="token operator">/</span>foo
<span aria-hidden="true" class="line-numbers-rows"><span></span></span></code></pre></div>
<p>路径可能是:</p>
<div class="_2Uzcx_"><button class="VJbwyy" type="button" aria-label="复制代码"><i aria-label="icon: copy" class="anticon anticon-copy"><svg viewBox="64 64 896 896" focusable="false" class="" data-icon="copy" width="1em" height="1em" fill="currentColor" aria-hidden="true"><path d="M832 64H296c-4.4 0-8 3.6-8 8v56c0 4.4 3.6 8 8 8h496v688c0 4.4 3.6 8 8 8h56c4.4 0 8-3.6 8-8V96c0-17.7-14.3-32-32-32zM704 192H192c-17.7 0-32 14.3-32 32v530.7c0 8.5 3.4 16.6 9.4 22.6l173.3 173.3c2.2 2.2 4.7 4 7.4 5.5v1.9h4.2c3.5 1.3 7.2 2 11 2H704c17.7 0 32-14.3 32-32V224c0-17.7-14.3-32-32-32zM350 856.2L263.9 770H350v86.2zM664 888H414V746c0-22.1-17.9-40-40-40H232V264h432v624z"></path></svg></i></button><pre class="line-numbers  language-undefined"><code class="  language-undefined">/items/foo
<span aria-hidden="true" class="line-numbers-rows"><span></span></span></code></pre></div>
<blockquote>
<p>“路径”通常也称为“端点”或“路由”。</p>
</blockquote>
<p>构建API时，“路径”是分离“关注点”和“资源”的主要方法。</p>
<h4>Operation</h4>
<p>"Operation" 这里指 HTTP 方法：</p>
<p>比如:</p>
<ul>
<li><code>POST</code></li>
<li><code>GET</code></li>
<li><code>PUT</code></li>
<li><code>DELETE</code></li>
</ul>
<p>...还有更少见的一些方法:</p>
<ul>
<li><code>OPTIONS</code></li>
<li><code>HEAD</code></li>
<li><code>PATCH</code></li>
<li><code>TRACE</code></li>
</ul>
<p>在HTTP协议中，你可以使用任意方法访问一个路径</p>
<hr>
<p>构建API时，通常使用这些特定的HTTP方法来执行特定的操作。</p>
<p>通常你会用到:</p>
<ul>
<li>
<code>POST</code>: 创建数据.</li>
<li>
<code>GET</code>: 读取数据.</li>
<li>
<code>PUT</code>: 更新数据.</li>
<li>
<code>DELETE</code>: 删除数据.</li>
</ul>
<p>因此，在OpenAPI中，每个HTTP方法都称为<code>方法</code>。</p>
<p>在以后的内容中，我们也把它称为方法。</p>
<h4>定义URL路由</h4>
<div class="_2Uzcx_"><button class="VJbwyy" type="button" aria-label="复制代码"><i aria-label="icon: copy" class="anticon anticon-copy"><svg viewBox="64 64 896 896" focusable="false" class="" data-icon="copy" width="1em" height="1em" fill="currentColor" aria-hidden="true"><path d="M832 64H296c-4.4 0-8 3.6-8 8v56c0 4.4 3.6 8 8 8h496v688c0 4.4 3.6 8 8 8h56c4.4 0 8-3.6 8-8V96c0-17.7-14.3-32-32-32zM704 192H192c-17.7 0-32 14.3-32 32v530.7c0 8.5 3.4 16.6 9.4 22.6l173.3 173.3c2.2 2.2 4.7 4 7.4 5.5v1.9h4.2c3.5 1.3 7.2 2 11 2H704c17.7 0 32-14.3 32-32V224c0-17.7-14.3-32-32-32zM350 856.2L263.9 770H350v86.2zM664 888H414V746c0-22.1-17.9-40-40-40H232V264h432v624z"></path></svg></i></button><pre class="line-numbers  language-dart"><code class="  language-dart">from fastapi <span class="token keyword">import</span> FastAPI

app <span class="token operator">=</span> <span class="token function">FastAPI</span><span class="token punctuation">(</span><span class="token punctuation">)</span>

<span class="token metadata symbol">@app</span><span class="token punctuation">.</span><span class="token keyword">get</span><span class="token punctuation">(</span><span class="token string">"/"</span><span class="token punctuation">)</span> <span class="token keyword">async</span> def <span class="token function">root</span><span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token punctuation">:</span>
    <span class="token keyword">return</span> <span class="token punctuation">{</span><span class="token string">"message"</span><span class="token punctuation">:</span> <span class="token string">"Hello World"</span><span class="token punctuation">}</span>
<span aria-hidden="true" class="line-numbers-rows"><span></span><span></span><span></span><span></span><span></span><span></span></span></code></pre></div>
<p><code>@app.get("/")</code>指明 <strong>FastAPI</strong> 下面的函数负责处理收到的请求：</p>
<ul>
<li>路径 <code>/</code>
</li>
<li>使用<code>get</code> 方法</li>
</ul>
<p>Python中 <code>@something</code> 语法被称为<code>装饰器</code>.</p>
<p>将这个装饰器放在函数的上方，就像一个漂亮的装饰帽(我猜想这也是这个属于名称的来源).</p>
<p>一个"装饰器"使用下方的函数，并对其进行处理.</p>
<p>在我们的例子中，这个装饰器告诉<strong>FastAPI</strong>，下方视图函数将会响应<strong>路径</strong><code>/</code>中的<strong>方法</strong><code>get</code>.</p>
<p>这就是<strong>路由操作装饰器</strong>.</p>
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
<li><code>@app.trace()</code></li>
</ul>
<h4>建议</h4>
<p>你可以使用任意的HTTP方法.</p>
<p><strong>FastAPI</strong>不强制任何特定函数。</p>
<p>此处提供的信息，仅供参考，并非必需。</p>
<p>例如，当使用 GraphQL , 你通常会只执行<code>post</code>方法</p>
<h3>Step 4: 定义<strong>路径操作函数</strong>
</h3>
<p>这是我们的 "<strong>路径操作函数</strong>":</p>
<ul>
<li>
<strong>路径</strong>:  <code>/</code>.</li>
<li>
<strong>操作</strong>:  <code>get</code>.</li>
<li>
<strong>函数</strong>: <code>@app.get("/")</code>下方的函数.</li>
</ul>
<div class="_2Uzcx_"><button class="VJbwyy" type="button" aria-label="复制代码"><i aria-label="icon: copy" class="anticon anticon-copy"><svg viewBox="64 64 896 896" focusable="false" class="" data-icon="copy" width="1em" height="1em" fill="currentColor" aria-hidden="true"><path d="M832 64H296c-4.4 0-8 3.6-8 8v56c0 4.4 3.6 8 8 8h496v688c0 4.4 3.6 8 8 8h56c4.4 0 8-3.6 8-8V96c0-17.7-14.3-32-32-32zM704 192H192c-17.7 0-32 14.3-32 32v530.7c0 8.5 3.4 16.6 9.4 22.6l173.3 173.3c2.2 2.2 4.7 4 7.4 5.5v1.9h4.2c3.5 1.3 7.2 2 11 2H704c17.7 0 32-14.3 32-32V224c0-17.7-14.3-32-32-32zM350 856.2L263.9 770H350v86.2zM664 888H414V746c0-22.1-17.9-40-40-40H232V264h432v624z"></path></svg></i></button><pre class="line-numbers  language-python"><code class="  language-python"><span class="token keyword">from</span> fastapi <span class="token keyword">import</span> FastAPI

app <span class="token operator">=</span> FastAPI<span class="token punctuation">(</span><span class="token punctuation">)</span>

@app<span class="token punctuation">.</span>get<span class="token punctuation">(</span><span class="token string">"/"</span><span class="token punctuation">)</span>
<span class="token keyword">async</span> <span class="token keyword">def</span> <span class="token function">root</span><span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token punctuation">:</span>
    <span class="token keyword">return</span> <span class="token punctuation">{</span><span class="token string">"message"</span><span class="token punctuation">:</span> <span class="token string">"Hello World"</span><span class="token punctuation">}</span>
<span aria-hidden="true" class="line-numbers-rows"><span></span><span></span><span></span><span></span><span></span><span></span><span></span></span></code></pre></div>
<p>这是Python函数。</p>
<p>这个函数将会被 <strong>FastAPI</strong> 调用只要有 <code>GET</code>请求到URL "<code>/</code>".</p>
<p>在这个例子中，使用的是 <code>async</code> 函数。</p>
<hr>
<p>你也可以定义普通的函数而不是<code>async def</code>:</p>
<div class="_2Uzcx_"><button class="VJbwyy" type="button" aria-label="复制代码"><i aria-label="icon: copy" class="anticon anticon-copy"><svg viewBox="64 64 896 896" focusable="false" class="" data-icon="copy" width="1em" height="1em" fill="currentColor" aria-hidden="true"><path d="M832 64H296c-4.4 0-8 3.6-8 8v56c0 4.4 3.6 8 8 8h496v688c0 4.4 3.6 8 8 8h56c4.4 0 8-3.6 8-8V96c0-17.7-14.3-32-32-32zM704 192H192c-17.7 0-32 14.3-32 32v530.7c0 8.5 3.4 16.6 9.4 22.6l173.3 173.3c2.2 2.2 4.7 4 7.4 5.5v1.9h4.2c3.5 1.3 7.2 2 11 2H704c17.7 0 32-14.3 32-32V224c0-17.7-14.3-32-32-32zM350 856.2L263.9 770H350v86.2zM664 888H414V746c0-22.1-17.9-40-40-40H232V264h432v624z"></path></svg></i></button><pre class="line-numbers  language-python"><code class="  language-python"><span class="token keyword">from</span> fastapi <span class="token keyword">import</span> FastAPI

app <span class="token operator">=</span> FastAPI<span class="token punctuation">(</span><span class="token punctuation">)</span>

@app<span class="token punctuation">.</span>get<span class="token punctuation">(</span><span class="token string">"/"</span><span class="token punctuation">)</span>
<span class="token keyword">def</span> <span class="token function">root</span><span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token punctuation">:</span>
    <span class="token keyword">return</span> <span class="token punctuation">{</span><span class="token string">"message"</span><span class="token punctuation">:</span> <span class="token string">"Hello World"</span><span class="token punctuation">}</span>
<span aria-hidden="true" class="line-numbers-rows"><span></span><span></span><span></span><span></span><span></span><span></span><span></span></span></code></pre></div>
<h4>注释</h4>
<p>如果你不了解其中的区别，可以查看<em>"In a hurry?"</em> 章节关于 <a href="https://links.jianshu.com/go?to=https%3A%2F%2Ffastapi.tiangolo.com%2Fasync%2F%23in-a-hurry" target="_blank"><code>async</code> and <code>await</code> in the docs</a>.</p>
<h3>Step 5: 返回内容</h3>
<div class="_2Uzcx_"><button class="VJbwyy" type="button" aria-label="复制代码"><i aria-label="icon: copy" class="anticon anticon-copy"><svg viewBox="64 64 896 896" focusable="false" class="" data-icon="copy" width="1em" height="1em" fill="currentColor" aria-hidden="true"><path d="M832 64H296c-4.4 0-8 3.6-8 8v56c0 4.4 3.6 8 8 8h496v688c0 4.4 3.6 8 8 8h56c4.4 0 8-3.6 8-8V96c0-17.7-14.3-32-32-32zM704 192H192c-17.7 0-32 14.3-32 32v530.7c0 8.5 3.4 16.6 9.4 22.6l173.3 173.3c2.2 2.2 4.7 4 7.4 5.5v1.9h4.2c3.5 1.3 7.2 2 11 2H704c17.7 0 32-14.3 32-32V224c0-17.7-14.3-32-32-32zM350 856.2L263.9 770H350v86.2zM664 888H414V746c0-22.1-17.9-40-40-40H232V264h432v624z"></path></svg></i></button><pre class="line-numbers  language-python"><code class="  language-python"><span class="token keyword">from</span> fastapi <span class="token keyword">import</span> FastAPI

app <span class="token operator">=</span> FastAPI<span class="token punctuation">(</span><span class="token punctuation">)</span>

@app<span class="token punctuation">.</span>get<span class="token punctuation">(</span><span class="token string">"/"</span><span class="token punctuation">)</span>
<span class="token keyword">async</span> <span class="token keyword">def</span> <span class="token function">root</span><span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token punctuation">:</span>
 <span class="token keyword">return</span> <span class="token punctuation">{</span><span class="token string">"message"</span><span class="token punctuation">:</span> <span class="token string">"Hello World"</span><span class="token punctuation">}</span>
<span aria-hidden="true" class="line-numbers-rows"><span></span><span></span><span></span><span></span><span></span><span></span><span></span></span></code></pre></div>
<h4>可返回的类型</h4>
<blockquote>
<p>你可以返回一个<code>dict</code>, <code>list</code>，单独的值，比如<code>str</code>, <code>int</code>等</p>
<p>你也可以返回 <strong>Pydantic模型</strong>，在稍后的章节中会看到更多。</p>
</blockquote>
<p>在<strong>FastAPI</strong>中，许多其他的对象和模型都会被自动转换为JSON(包括ORM等)。</p>
<p>试着使用最适合您的方法，很有可能他们已经支持了。</p>
<h2>七、总结</h2>
<ul>
<li>Import <code>FastAPI</code>.</li>
<li>创建一个  <code>app</code> 实例.</li>
<li>编写一个 <strong>路径操作装饰器</strong> (比如<code>@app.get("/")</code>).</li>
<li>编写一个<strong>路径操作函数</strong> (比如上方的 <code>def root(): ...</code> ).</li>
<li>运行开发服务器(比如<code>uvicorn main:app --reload</code>).</li>
</ul>