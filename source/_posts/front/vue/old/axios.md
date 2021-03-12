---
title: "axios浅析"
date:       2019-12-12
tags:
	- JavaScript
	- web
	- vue
	- axios
---





原文链接:https://www.jianshu.com/p/df464b26ae58

<article class="_2rhmJa">
    <h2>一、安装</h2>
    <p>1、 利用npm安装<code>npm install axios --save</code><br>
        2、 利用bower安装<code>bower install axios --save</code><br>
        3、 直接利用cdn引入<code>&lt;script src="https://unpkg.com/axios/dist/axios.min.js"&gt;&lt;/script&gt;</code></p>
    <h2>二、例子</h2>
    <p>1、 发送一个<code>GET</code>请求</p>
    <div class="_2Uzcx_">
        <button class="VJbwyy" type="button" aria-label="复制代码"><i aria-label="icon: copy"
                                                                  class="anticon anticon-copy">
            <svg viewBox="64 64 896 896" focusable="false" class="" data-icon="copy" width="1em" height="1em"
                 fill="currentColor" aria-hidden="true">
                <path d="M832 64H296c-4.4 0-8 3.6-8 8v56c0 4.4 3.6 8 8 8h496v688c0 4.4 3.6 8 8 8h56c4.4 0 8-3.6 8-8V96c0-17.7-14.3-32-32-32zM704 192H192c-17.7 0-32 14.3-32 32v530.7c0 8.5 3.4 16.6 9.4 22.6l173.3 173.3c2.2 2.2 4.7 4 7.4 5.5v1.9h4.2c3.5 1.3 7.2 2 11 2H704c17.7 0 32-14.3 32-32V224c0-17.7-14.3-32-32-32zM350 856.2L263.9 770H350v86.2zM664 888H414V746c0-22.1-17.9-40-40-40H232V264h432v624z"></path>
            </svg>
        </i></button>
        <pre class="line-numbers  language-jsx"><code class="  language-jsx"><span
                class="token comment">//通过给定的ID来发送请求</span>
axios<span class="token punctuation">.</span><span class="token function">get</span><span
                    class="token punctuation">(</span><span class="token string">'/user?ID=12345'</span><span
                    class="token punctuation">)</span>
  <span class="token punctuation">.</span><span class="token function">then</span><span
                    class="token punctuation">(</span><span class="token keyword">function</span><span
                    class="token punctuation">(</span><span class="token parameter">response</span><span
                    class="token punctuation">)</span><span class="token punctuation">{</span>
    console<span class="token punctuation">.</span><span class="token function">log</span><span
                    class="token punctuation">(</span>response<span class="token punctuation">)</span><span
                    class="token punctuation">;</span>
  <span class="token punctuation">}</span><span class="token punctuation">)</span>
  <span class="token punctuation">.</span><span class="token function">catch</span><span
                    class="token punctuation">(</span><span class="token keyword">function</span><span
                    class="token punctuation">(</span><span class="token parameter">err</span><span
                    class="token punctuation">)</span><span class="token punctuation">{</span>
    console<span class="token punctuation">.</span><span class="token function">log</span><span
                    class="token punctuation">(</span>err<span class="token punctuation">)</span><span
                    class="token punctuation">;</span>
  <span class="token punctuation">}</span><span class="token punctuation">)</span><span
                    class="token punctuation">;</span>
<span class="token comment">//以上请求也可以通过这种方式来发送</span>
axios<span class="token punctuation">.</span><span class="token function">get</span><span
                    class="token punctuation">(</span><span class="token string">'/user'</span><span
                    class="token punctuation">,</span><span class="token punctuation">{</span>
  params<span class="token punctuation">:</span><span class="token punctuation">{</span>
    <span class="token constant">ID</span><span class="token punctuation">:</span><span
                    class="token number">12345</span>
  <span class="token punctuation">}</span>
<span class="token punctuation">}</span><span class="token punctuation">)</span>
<span class="token punctuation">.</span><span class="token function">then</span><span class="token punctuation">(</span><span
                    class="token keyword">function</span><span class="token punctuation">(</span><span
                    class="token parameter">response</span><span class="token punctuation">)</span><span
                    class="token punctuation">{</span>
  console<span class="token punctuation">.</span><span class="token function">log</span><span class="token punctuation">(</span>response<span
                    class="token punctuation">)</span><span class="token punctuation">;</span>
<span class="token punctuation">}</span><span class="token punctuation">)</span>
<span class="token punctuation">.</span><span class="token function">catch</span><span
                    class="token punctuation">(</span><span class="token keyword">function</span><span
                    class="token punctuation">(</span><span class="token parameter">err</span><span
                    class="token punctuation">)</span><span class="token punctuation">{</span>
  console<span class="token punctuation">.</span><span class="token function">log</span><span class="token punctuation">(</span>err<span
                    class="token punctuation">)</span><span class="token punctuation">;</span>
<span class="token punctuation">}</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
<span aria-hidden="true"
      class="line-numbers-rows"><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span></span></code></pre>
    </div>
    <p>2、 发送一个<code>POST</code>请求</p>
    <div class="_2Uzcx_">
        <button class="VJbwyy" type="button" aria-label="复制代码"><i aria-label="icon: copy"
                                                                  class="anticon anticon-copy">
            <svg viewBox="64 64 896 896" focusable="false" class="" data-icon="copy" width="1em" height="1em"
                 fill="currentColor" aria-hidden="true">
                <path d="M832 64H296c-4.4 0-8 3.6-8 8v56c0 4.4 3.6 8 8 8h496v688c0 4.4 3.6 8 8 8h56c4.4 0 8-3.6 8-8V96c0-17.7-14.3-32-32-32zM704 192H192c-17.7 0-32 14.3-32 32v530.7c0 8.5 3.4 16.6 9.4 22.6l173.3 173.3c2.2 2.2 4.7 4 7.4 5.5v1.9h4.2c3.5 1.3 7.2 2 11 2H704c17.7 0 32-14.3 32-32V224c0-17.7-14.3-32-32-32zM350 856.2L263.9 770H350v86.2zM664 888H414V746c0-22.1-17.9-40-40-40H232V264h432v624z"></path>
            </svg>
        </i></button>
        <pre class="line-numbers  language-jsx"><code class="  language-jsx">axios<span
                class="token punctuation">.</span><span class="token function">post</span><span
                class="token punctuation">(</span><span class="token string">'/user'</span><span
                class="token punctuation">,</span><span class="token punctuation">{</span>
  firstName<span class="token punctuation">:</span><span class="token string">'Fred'</span><span
                    class="token punctuation">,</span>
  lastName<span class="token punctuation">:</span><span class="token string">'Flintstone'</span>
<span class="token punctuation">}</span><span class="token punctuation">)</span>
<span class="token punctuation">.</span><span class="token function">then</span><span class="token punctuation">(</span><span
                    class="token keyword">function</span><span class="token punctuation">(</span><span
                    class="token parameter">res</span><span class="token punctuation">)</span><span
                    class="token punctuation">{</span>
  console<span class="token punctuation">.</span><span class="token function">log</span><span class="token punctuation">(</span>res<span
                    class="token punctuation">)</span><span class="token punctuation">;</span>
<span class="token punctuation">}</span><span class="token punctuation">)</span>
<span class="token punctuation">.</span><span class="token function">catch</span><span
                    class="token punctuation">(</span><span class="token keyword">function</span><span
                    class="token punctuation">(</span><span class="token parameter">err</span><span
                    class="token punctuation">)</span><span class="token punctuation">{</span>
  console<span class="token punctuation">.</span><span class="token function">log</span><span class="token punctuation">(</span>err<span
                    class="token punctuation">)</span><span class="token punctuation">;</span>
<span class="token punctuation">}</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
<span aria-hidden="true"
      class="line-numbers-rows"><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span></span></code></pre>
    </div>
    <p>3、 一次性并发多个请求</p>
    <div class="_2Uzcx_">
        <button class="VJbwyy" type="button" aria-label="复制代码"><i aria-label="icon: copy"
                                                                  class="anticon anticon-copy">
            <svg viewBox="64 64 896 896" focusable="false" class="" data-icon="copy" width="1em" height="1em"
                 fill="currentColor" aria-hidden="true">
                <path d="M832 64H296c-4.4 0-8 3.6-8 8v56c0 4.4 3.6 8 8 8h496v688c0 4.4 3.6 8 8 8h56c4.4 0 8-3.6 8-8V96c0-17.7-14.3-32-32-32zM704 192H192c-17.7 0-32 14.3-32 32v530.7c0 8.5 3.4 16.6 9.4 22.6l173.3 173.3c2.2 2.2 4.7 4 7.4 5.5v1.9h4.2c3.5 1.3 7.2 2 11 2H704c17.7 0 32-14.3 32-32V224c0-17.7-14.3-32-32-32zM350 856.2L263.9 770H350v86.2zM664 888H414V746c0-22.1-17.9-40-40-40H232V264h432v624z"></path>
            </svg>
        </i></button>
        <pre class="line-numbers  language-jsx"><code class="  language-jsx"><span
                class="token keyword">function</span> <span class="token function">getUserAccount</span><span
                class="token punctuation">(</span><span class="token punctuation">)</span><span
                class="token punctuation">{</span>
  <span class="token keyword">return</span> axios<span class="token punctuation">.</span><span class="token function">get</span><span
                    class="token punctuation">(</span><span class="token string">'/user/12345'</span><span
                    class="token punctuation">)</span><span class="token punctuation">;</span>
<span class="token punctuation">}</span>
<span class="token keyword">function</span> <span class="token function">getUserPermissions</span><span
                    class="token punctuation">(</span><span class="token punctuation">)</span><span
                    class="token punctuation">{</span>
  <span class="token keyword">return</span> axios<span class="token punctuation">.</span><span class="token function">get</span><span
                    class="token punctuation">(</span><span
                    class="token string">'/user/12345/permissions'</span><span
                    class="token punctuation">)</span><span class="token punctuation">;</span>
<span class="token punctuation">}</span>
axios<span class="token punctuation">.</span><span class="token function">all</span><span
                    class="token punctuation">(</span><span class="token punctuation">[</span><span
                    class="token function">getUserAccount</span><span class="token punctuation">(</span><span
                    class="token punctuation">)</span><span class="token punctuation">,</span><span
                    class="token function">getUserPermissions</span><span class="token punctuation">(</span><span
                    class="token punctuation">)</span><span class="token punctuation">]</span><span
                    class="token punctuation">)</span>
  <span class="token punctuation">.</span><span class="token function">then</span><span
                    class="token punctuation">(</span>axios<span class="token punctuation">.</span><span
                    class="token function">spread</span><span class="token punctuation">(</span><span
                    class="token keyword">function</span><span class="token punctuation">(</span><span
                    class="token parameter">acct<span class="token punctuation">,</span>perms</span><span
                    class="token punctuation">)</span><span class="token punctuation">{</span>
    <span class="token comment">//当这两个请求都完成的时候会触发这个函数，两个参数分别代表返回的结果</span>
  <span class="token punctuation">}</span><span class="token punctuation">)</span><span
                    class="token punctuation">)</span>
<span aria-hidden="true"
      class="line-numbers-rows"><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span></span></code></pre>
    </div>
    <h2>三、axios的API</h2>
    <h4>（一） axios可以通过配置（<code>config</code>）来发送请求</h4>
    <p>1、 <code>axios(config)</code></p>
    <div class="_2Uzcx_">
        <button class="VJbwyy" type="button" aria-label="复制代码"><i aria-label="icon: copy"
                                                                  class="anticon anticon-copy">
            <svg viewBox="64 64 896 896" focusable="false" class="" data-icon="copy" width="1em" height="1em"
                 fill="currentColor" aria-hidden="true">
                <path d="M832 64H296c-4.4 0-8 3.6-8 8v56c0 4.4 3.6 8 8 8h496v688c0 4.4 3.6 8 8 8h56c4.4 0 8-3.6 8-8V96c0-17.7-14.3-32-32-32zM704 192H192c-17.7 0-32 14.3-32 32v530.7c0 8.5 3.4 16.6 9.4 22.6l173.3 173.3c2.2 2.2 4.7 4 7.4 5.5v1.9h4.2c3.5 1.3 7.2 2 11 2H704c17.7 0 32-14.3 32-32V224c0-17.7-14.3-32-32-32zM350 856.2L263.9 770H350v86.2zM664 888H414V746c0-22.1-17.9-40-40-40H232V264h432v624z"></path>
            </svg>
        </i></button>
        <pre class="line-numbers  language-kotlin"><code class="  language-kotlin"><span class="token comment">//发送一个`POST`请求</span>
<span class="token function">axios</span><span class="token punctuation">(</span><span
                    class="token punctuation">{</span>
    method<span class="token operator">:</span><span class="token string">"POST"</span><span
                    class="token punctuation">,</span>
    url<span class="token operator">:</span><span class="token string">'/user/12345'</span><span
                    class="token punctuation">,</span>
    <span class="token keyword">data</span><span class="token operator">:</span><span class="token punctuation">{</span>
        firstName<span class="token operator">:</span><span class="token string">"Fred"</span><span
                    class="token punctuation">,</span>
        lastName<span class="token operator">:</span><span class="token string">"Flintstone"</span>
    <span class="token punctuation">}</span>
<span class="token punctuation">}</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
<span aria-hidden="true"
      class="line-numbers-rows"><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span></span></code></pre>
    </div>
    <p>2、 <code>axios(url[,config])</code></p>
    <div class="_2Uzcx_">
        <button class="VJbwyy" type="button" aria-label="复制代码"><i aria-label="icon: copy"
                                                                  class="anticon anticon-copy">
            <svg viewBox="64 64 896 896" focusable="false" class="" data-icon="copy" width="1em" height="1em"
                 fill="currentColor" aria-hidden="true">
                <path d="M832 64H296c-4.4 0-8 3.6-8 8v56c0 4.4 3.6 8 8 8h496v688c0 4.4 3.6 8 8 8h56c4.4 0 8-3.6 8-8V96c0-17.7-14.3-32-32-32zM704 192H192c-17.7 0-32 14.3-32 32v530.7c0 8.5 3.4 16.6 9.4 22.6l173.3 173.3c2.2 2.2 4.7 4 7.4 5.5v1.9h4.2c3.5 1.3 7.2 2 11 2H704c17.7 0 32-14.3 32-32V224c0-17.7-14.3-32-32-32zM350 856.2L263.9 770H350v86.2zM664 888H414V746c0-22.1-17.9-40-40-40H232V264h432v624z"></path>
            </svg>
        </i></button>
        <pre class="line-numbers  language-csharp"><code class="  language-csharp"><span class="token comment">//发送一个`GET`请求（默认的请求方式）</span>
<span class="token function">axios</span><span class="token punctuation">(</span><span class="token string">'/user/12345'</span><span
                    class="token punctuation">)</span><span class="token punctuation">;</span>
<span aria-hidden="true" class="line-numbers-rows"><span></span><span></span></span></code></pre>
    </div>
    <h4>（二）、 请求方式的别名，这里对所有已经支持的请求方式都提供了方便的别名</h4>
    <div class="_2Uzcx_">
        <button class="VJbwyy" type="button" aria-label="复制代码"><i aria-label="icon: copy"
                                                                  class="anticon anticon-copy">
            <svg viewBox="64 64 896 896" focusable="false" class="" data-icon="copy" width="1em" height="1em"
                 fill="currentColor" aria-hidden="true">
                <path d="M832 64H296c-4.4 0-8 3.6-8 8v56c0 4.4 3.6 8 8 8h496v688c0 4.4 3.6 8 8 8h56c4.4 0 8-3.6 8-8V96c0-17.7-14.3-32-32-32zM704 192H192c-17.7 0-32 14.3-32 32v530.7c0 8.5 3.4 16.6 9.4 22.6l173.3 173.3c2.2 2.2 4.7 4 7.4 5.5v1.9h4.2c3.5 1.3 7.2 2 11 2H704c17.7 0 32-14.3 32-32V224c0-17.7-14.3-32-32-32zM350 856.2L263.9 770H350v86.2zM664 888H414V746c0-22.1-17.9-40-40-40H232V264h432v624z"></path>
            </svg>
        </i></button>
        <pre class="line-numbers  language-css"><code class="  language-css">axios.<span
                class="token function">request</span><span
                class="token punctuation">(</span>config<span class="token punctuation">)</span><span
                class="token punctuation">;</span>

axios.<span class="token function">get</span><span class="token punctuation">(</span>url[<span
                    class="token punctuation">,</span>config]<span class="token punctuation">)</span><span
                    class="token punctuation">;</span>

axios.<span class="token function">delete</span><span class="token punctuation">(</span>url[<span
                    class="token punctuation">,</span>config]<span class="token punctuation">)</span><span
                    class="token punctuation">;</span>

axios.<span class="token function">head</span><span class="token punctuation">(</span>url[<span
                    class="token punctuation">,</span>config]<span class="token punctuation">)</span><span
                    class="token punctuation">;</span>

axios.<span class="token function">post</span><span class="token punctuation">(</span>url[<span
                    class="token punctuation">,</span>data[<span class="token punctuation">,</span>config]]<span
                    class="token punctuation">)</span><span class="token punctuation">;</span>

axios.<span class="token function">put</span><span class="token punctuation">(</span>url[<span
                    class="token punctuation">,</span>data[<span class="token punctuation">,</span>config]]<span
                    class="token punctuation">)</span>

axios.<span class="token function">patch</span><span class="token punctuation">(</span>url[<span
                    class="token punctuation">,</span>data[<span class="token punctuation">,</span>config]]<span
                    class="token punctuation">)</span>
<span aria-hidden="true"
      class="line-numbers-rows"><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span></span></code></pre>
    </div>
    <ul>
        <li>注意：当我们在使用别名方法的时候，<code>url,method,data</code>这几个参数不需要在配置中声明</li>
    </ul>
    <h4>（三）、 并发请求（concurrency）,即是帮助处理并发请求的辅助函数</h4>
    <div class="_2Uzcx_">
        <button class="VJbwyy" type="button" aria-label="复制代码"><i aria-label="icon: copy"
                                                                  class="anticon anticon-copy">
            <svg viewBox="64 64 896 896" focusable="false" class="" data-icon="copy" width="1em" height="1em"
                 fill="currentColor" aria-hidden="true">
                <path d="M832 64H296c-4.4 0-8 3.6-8 8v56c0 4.4 3.6 8 8 8h496v688c0 4.4 3.6 8 8 8h56c4.4 0 8-3.6 8-8V96c0-17.7-14.3-32-32-32zM704 192H192c-17.7 0-32 14.3-32 32v530.7c0 8.5 3.4 16.6 9.4 22.6l173.3 173.3c2.2 2.2 4.7 4 7.4 5.5v1.9h4.2c3.5 1.3 7.2 2 11 2H704c17.7 0 32-14.3 32-32V224c0-17.7-14.3-32-32-32zM350 856.2L263.9 770H350v86.2zM664 888H414V746c0-22.1-17.9-40-40-40H232V264h432v624z"></path>
            </svg>
        </i></button>
        <pre class="line-numbers  language-cpp"><code class="  language-cpp"><span class="token comment">//iterable是一个可以迭代的参数如数组等</span>
axios<span class="token punctuation">.</span><span class="token function">all</span><span
                    class="token punctuation">(</span>iterable<span class="token punctuation">)</span>
<span class="token comment">//callback要等到所有请求都完成才会执行</span>
axios<span class="token punctuation">.</span><span class="token function">spread</span><span
                    class="token punctuation">(</span>callback<span class="token punctuation">)</span>
<span aria-hidden="true"
      class="line-numbers-rows"><span></span><span></span><span></span><span></span></span></code></pre>
    </div>
    <h4>（四）、创建一个<code>axios</code>实例，并且可以自定义其配置</h4>
    <p>1、 <code>axios.create([config])</code></p>
    <div class="_2Uzcx_">
        <button class="VJbwyy" type="button" aria-label="复制代码"><i aria-label="icon: copy"
                                                                  class="anticon anticon-copy">
            <svg viewBox="64 64 896 896" focusable="false" class="" data-icon="copy" width="1em" height="1em"
                 fill="currentColor" aria-hidden="true">
                <path d="M832 64H296c-4.4 0-8 3.6-8 8v56c0 4.4 3.6 8 8 8h496v688c0 4.4 3.6 8 8 8h56c4.4 0 8-3.6 8-8V96c0-17.7-14.3-32-32-32zM704 192H192c-17.7 0-32 14.3-32 32v530.7c0 8.5 3.4 16.6 9.4 22.6l173.3 173.3c2.2 2.2 4.7 4 7.4 5.5v1.9h4.2c3.5 1.3 7.2 2 11 2H704c17.7 0 32-14.3 32-32V224c0-17.7-14.3-32-32-32zM350 856.2L263.9 770H350v86.2zM664 888H414V746c0-22.1-17.9-40-40-40H232V264h432v624z"></path>
            </svg>
        </i></button>
        <pre class="line-numbers  language-csharp"><code class="  language-csharp"><span
                class="token keyword">var</span> instance <span class="token operator">=</span> axios<span
                class="token punctuation">.</span><span class="token function">create</span><span
                class="token punctuation">(</span><span class="token punctuation">{</span>
  baseURL<span class="token punctuation">:</span><span class="token string">"https://some-domain.com/api/"</span><span
                    class="token punctuation">,</span>
  timeout<span class="token punctuation">:</span><span class="token number">1000</span><span
                    class="token punctuation">,</span>
  headers<span class="token punctuation">:</span> <span class="token punctuation">{</span><span class="token string">'X-Custom-Header'</span><span
                    class="token punctuation">:</span><span class="token string">'foobar'</span><span
                    class="token punctuation">}</span>
<span class="token punctuation">}</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
<span aria-hidden="true"
      class="line-numbers-rows"><span></span><span></span><span></span><span></span><span></span></span></code></pre>
    </div>
    <p>2、 实例的方法</p>
    <ul>
        <li>一下是实例方法，注意已经定义的配置将和利用create创建的实例的配置合并</li>
    </ul>
    <div class="_2Uzcx_">
        <button class="VJbwyy" type="button" aria-label="复制代码"><i aria-label="icon: copy"
                                                                  class="anticon anticon-copy">
            <svg viewBox="64 64 896 896" focusable="false" class="" data-icon="copy" width="1em" height="1em"
                 fill="currentColor" aria-hidden="true">
                <path d="M832 64H296c-4.4 0-8 3.6-8 8v56c0 4.4 3.6 8 8 8h496v688c0 4.4 3.6 8 8 8h56c4.4 0 8-3.6 8-8V96c0-17.7-14.3-32-32-32zM704 192H192c-17.7 0-32 14.3-32 32v530.7c0 8.5 3.4 16.6 9.4 22.6l173.3 173.3c2.2 2.2 4.7 4 7.4 5.5v1.9h4.2c3.5 1.3 7.2 2 11 2H704c17.7 0 32-14.3 32-32V224c0-17.7-14.3-32-32-32zM350 856.2L263.9 770H350v86.2zM664 888H414V746c0-22.1-17.9-40-40-40H232V264h432v624z"></path>
            </svg>
        </i></button>
        <pre class="line-numbers  language-css"><code class="  language-css">axios#<span
                class="token function">request</span><span
                class="token punctuation">(</span>config<span class="token punctuation">)</span>

axios#<span class="token function">get</span><span class="token punctuation">(</span>url[<span
                    class="token punctuation">,</span>config]<span class="token punctuation">)</span>

axios#<span class="token function">delete</span><span class="token punctuation">(</span>url[<span
                    class="token punctuation">,</span>config]<span class="token punctuation">)</span>

axios#<span class="token function">head</span><span class="token punctuation">(</span>url[<span
                    class="token punctuation">,</span>config]<span class="token punctuation">)</span>

axios#<span class="token function">post</span><span class="token punctuation">(</span>url[<span
                    class="token punctuation">,</span>data[<span class="token punctuation">,</span>config]]<span
                    class="token punctuation">)</span>

axios#<span class="token function">put</span><span class="token punctuation">(</span>url[<span
                    class="token punctuation">,</span>data[<span class="token punctuation">,</span>config]]<span
                    class="token punctuation">)</span>

axios#<span class="token function">patch</span><span class="token punctuation">(</span>url[<span
                    class="token punctuation">,</span>data[<span class="token punctuation">,</span>config]]<span
                    class="token punctuation">)</span>
<span aria-hidden="true"
      class="line-numbers-rows"><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span></span></code></pre>
    </div>
    <h2>四、请求的配置（request config）</h2>
    <ul>
        <li>以下就是请求的配置选项，只有<code>url</code>选项是必须的，如果<code>method</code>选项未定义，那么它默认是以<code>GET</code>的方式发出请求</li>
    </ul>
    <div class="_2Uzcx_">
        <button class="VJbwyy" type="button" aria-label="复制代码"><i aria-label="icon: copy"
                                                                  class="anticon anticon-copy">
            <svg viewBox="64 64 896 896" focusable="false" class="" data-icon="copy" width="1em" height="1em"
                 fill="currentColor" aria-hidden="true">
                <path d="M832 64H296c-4.4 0-8 3.6-8 8v56c0 4.4 3.6 8 8 8h496v688c0 4.4 3.6 8 8 8h56c4.4 0 8-3.6 8-8V96c0-17.7-14.3-32-32-32zM704 192H192c-17.7 0-32 14.3-32 32v530.7c0 8.5 3.4 16.6 9.4 22.6l173.3 173.3c2.2 2.2 4.7 4 7.4 5.5v1.9h4.2c3.5 1.3 7.2 2 11 2H704c17.7 0 32-14.3 32-32V224c0-17.7-14.3-32-32-32zM350 856.2L263.9 770H350v86.2zM664 888H414V746c0-22.1-17.9-40-40-40H232V264h432v624z"></path>
            </svg>
        </i></button>
        <pre class="line-numbers  language-jsx"><code class="  language-jsx"><span
                class="token punctuation">{</span>
  <span class="token comment">//`url`是请求的服务器地址</span>
  url<span class="token punctuation">:</span><span class="token string">'/user'</span><span
                    class="token punctuation">,</span>
  <span class="token comment">//`method`是请求资源的方式</span>
  method<span class="token punctuation">:</span><span class="token string">'get'</span><span class="token comment">//default</span>
  <span class="token comment">//如果`url`不是绝对地址，那么`baseURL`将会加到`url`的前面</span>
  <span class="token comment">//当`url`是相对地址的时候，设置`baseURL`会非常的方便</span>
  baseURL<span class="token punctuation">:</span><span class="token string">'https://some-domain.com/api/'</span><span
                    class="token punctuation">,</span>
  <span class="token comment">//`transformRequest`选项允许我们在请求发送到服务器之前对请求的数据做出一些改动</span>
  <span class="token comment">//该选项只适用于以下请求方式：`put/post/patch`</span>
  <span class="token comment">//数组里面的最后一个函数必须返回一个字符串、-一个`ArrayBuffer`或者`Stream`</span>
  transformRequest<span class="token punctuation">:</span><span class="token punctuation">[</span><span
                    class="token keyword">function</span><span class="token punctuation">(</span><span
                    class="token parameter">data</span><span class="token punctuation">)</span><span
                    class="token punctuation">{</span>
    <span class="token comment">//在这里根据自己的需求改变数据</span>
    <span class="token keyword">return</span> data<span class="token punctuation">;</span>
  <span class="token punctuation">}</span><span class="token punctuation">]</span><span
                    class="token punctuation">,</span>
  <span class="token comment">//`transformResponse`选项允许我们在数据传送到`then/catch`方法之前对数据进行改动</span>
  transformResponse<span class="token punctuation">:</span><span class="token punctuation">[</span><span
                    class="token keyword">function</span><span class="token punctuation">(</span><span
                    class="token parameter">data</span><span class="token punctuation">)</span><span
                    class="token punctuation">{</span>
    <span class="token comment">//在这里根据自己的需求改变数据</span>
    <span class="token keyword">return</span> data<span class="token punctuation">;</span>
  <span class="token punctuation">}</span><span class="token punctuation">]</span><span
                    class="token punctuation">,</span>
  <span class="token comment">//`headers`选项是需要被发送的自定义请求头信息</span>
  headers<span class="token punctuation">:</span> <span class="token punctuation">{</span><span class="token string">'X-Requested-With'</span><span
                    class="token punctuation">:</span><span class="token string">'XMLHttpRequest'</span><span
                    class="token punctuation">}</span><span class="token punctuation">,</span>
  <span class="token comment">//`params`选项是要随请求一起发送的请求参数----一般链接在URL后面</span>
  <span class="token comment">//他的类型必须是一个纯对象或者是URLSearchParams对象</span>
  params<span class="token punctuation">:</span> <span class="token punctuation">{</span>
    <span class="token constant">ID</span><span class="token punctuation">:</span><span
                    class="token number">12345</span>
  <span class="token punctuation">}</span><span class="token punctuation">,</span>
  <span class="token comment">//`paramsSerializer`是一个可选的函数，起作用是让参数（params）序列化</span>
  <span class="token comment">//例如(https://www.npmjs.com/package/qs,http://api.jquery.com/jquery.param)</span>
  <span class="token function-variable function">paramsSerializer</span><span class="token punctuation">:</span> <span
                    class="token keyword">function</span><span class="token punctuation">(</span><span
                    class="token parameter">params</span><span class="token punctuation">)</span><span
                    class="token punctuation">{</span>
    <span class="token keyword">return</span> Qs<span class="token punctuation">.</span><span class="token function">stringify</span><span
                    class="token punctuation">(</span>params<span class="token punctuation">,</span><span
                    class="token punctuation">{</span>arrayFormat<span class="token punctuation">:</span><span
                    class="token string">'brackets'</span><span class="token punctuation">}</span><span
                    class="token punctuation">)</span>
  <span class="token punctuation">}</span><span class="token punctuation">,</span>
  <span class="token comment">//`data`选项是作为一个请求体而需要被发送的数据</span>
  <span class="token comment">//该选项只适用于方法：`put/post/patch`</span>
  <span class="token comment">//当没有设置`transformRequest`选项时dada必须是以下几种类型之一</span>
  <span class="token comment">//string/plain/object/ArrayBuffer/ArrayBufferView/URLSearchParams</span>
  <span class="token comment">//仅仅浏览器：FormData/File/Bold</span>
  <span class="token comment">//仅node:Stream</span>
  data <span class="token punctuation">{</span>
    firstName<span class="token punctuation">:</span><span class="token string">"Fred"</span>
  <span class="token punctuation">}</span><span class="token punctuation">,</span>
  <span class="token comment">//`timeout`选项定义了请求发出的延迟毫秒数</span>
  <span class="token comment">//如果请求花费的时间超过延迟的时间，那么请求会被终止</span>

  timeout<span class="token punctuation">:</span><span class="token number">1000</span><span
                    class="token punctuation">,</span>
  <span class="token comment">//`withCredentails`选项表明了是否是跨域请求</span>
  
  withCredentials<span class="token punctuation">:</span><span class="token boolean">false</span><span
                    class="token punctuation">,</span><span class="token comment">//default</span>
  <span class="token comment">//`adapter`适配器选项允许自定义处理请求，这会使得测试变得方便</span>
  <span class="token comment">//返回一个promise,并提供验证返回</span>
  <span class="token function-variable function">adapter</span><span class="token punctuation">:</span> <span
                    class="token keyword">function</span><span class="token punctuation">(</span><span
                    class="token parameter">config</span><span class="token punctuation">)</span><span
                    class="token punctuation">{</span>
    <span class="token comment">/*..........*/</span>
  <span class="token punctuation">}</span><span class="token punctuation">,</span>
  <span class="token comment">//`auth`表明HTTP基础的认证应该被使用，并提供证书</span>
  <span class="token comment">//这会设置一个authorization头（header）,并覆盖你在header设置的Authorization头信息</span>
  auth<span class="token punctuation">:</span> <span class="token punctuation">{</span>
    username<span class="token punctuation">:</span><span class="token string">"zhangsan"</span><span
                    class="token punctuation">,</span>
    password<span class="token punctuation">:</span> <span class="token string">"s00sdkf"</span>
  <span class="token punctuation">}</span><span class="token punctuation">,</span>
  <span class="token comment">//返回数据的格式</span>
  <span class="token comment">//其可选项是arraybuffer,blob,document,json,text,stream</span>
  responseType<span class="token punctuation">:</span><span class="token string">'json'</span><span
                    class="token punctuation">,</span><span class="token comment">//default</span>
  <span class="token comment">//</span>
  xsrfCookieName<span class="token punctuation">:</span> <span class="token string">'XSRF-TOKEN'</span><span
                    class="token punctuation">,</span><span class="token comment">//default</span>
  xsrfHeaderName<span class="token punctuation">:</span><span class="token string">'X-XSRF-TOKEN'</span><span
                    class="token punctuation">,</span><span class="token comment">//default</span>
  <span class="token comment">//`onUploadProgress`上传进度事件</span>
  <span class="token function-variable function">onUploadProgress</span><span class="token punctuation">:</span><span
                    class="token keyword">function</span><span class="token punctuation">(</span><span
                    class="token parameter">progressEvent</span><span class="token punctuation">)</span><span
                    class="token punctuation">{</span>
    <span class="token comment">//下载进度的事件</span>
<span class="token function-variable function">onDownloadProgress</span><span class="token punctuation">:</span><span
                    class="token keyword">function</span><span class="token punctuation">(</span><span
                    class="token parameter">progressEvent</span><span class="token punctuation">)</span><span
                    class="token punctuation">{</span>
<span class="token punctuation">}</span>
  <span class="token punctuation">}</span><span class="token punctuation">,</span>
  <span class="token comment">//相应内容的最大值</span>
  maxContentLength<span class="token punctuation">:</span><span class="token number">2000</span><span
                    class="token punctuation">,</span>
  <span class="token comment">//`validateStatus`定义了是否根据http相应状态码，来resolve或者reject promise</span>
  <span class="token comment">//如果`validateStatus`返回true(或者设置为`null`或者`undefined`),那么promise的状态将会是resolved,否则其状态就是rejected</span>
  <span class="token function-variable function">validateStatus</span><span class="token punctuation">:</span><span
                    class="token keyword">function</span><span class="token punctuation">(</span><span
                    class="token parameter">status</span><span class="token punctuation">)</span><span
                    class="token punctuation">{</span>
    <span class="token keyword">return</span> status <span class="token operator">&gt;=</span> <span
                    class="token number">200</span> <span class="token operator">&amp;&amp;</span> status <span
                    class="token operator">&lt;</span><span class="token number">300</span><span
                    class="token punctuation">;</span><span class="token comment">//default</span>
  <span class="token punctuation">}</span><span class="token punctuation">,</span>
  <span class="token comment">//`maxRedirects`定义了在nodejs中重定向的最大数量</span>
  maxRedirects<span class="token punctuation">:</span> <span class="token number">5</span><span
                    class="token punctuation">,</span><span class="token comment">//default</span>
  <span class="token comment">//`httpAgent/httpsAgent`定义了当发送http/https请求要用到的自定义代理</span>
  <span class="token comment">//keeyAlive在选项中没有被默认激活</span>
  httpAgent<span class="token punctuation">:</span> <span class="token keyword">new</span> <span
                    class="token class-name">http<span class="token punctuation">.</span>Agent</span><span
                    class="token punctuation">(</span><span class="token punctuation">{</span>keeyAlive<span
                    class="token punctuation">:</span><span class="token boolean">true</span><span
                    class="token punctuation">}</span><span class="token punctuation">)</span><span
                    class="token punctuation">,</span>
  httpsAgent<span class="token punctuation">:</span> <span class="token keyword">new</span> <span
                    class="token class-name">https<span class="token punctuation">.</span>Agent</span><span
                    class="token punctuation">(</span><span class="token punctuation">{</span>keeyAlive<span
                    class="token punctuation">:</span><span class="token boolean">true</span><span
                    class="token punctuation">}</span><span class="token punctuation">)</span><span
                    class="token punctuation">,</span>
  <span class="token comment">//proxy定义了主机名字和端口号，</span>
  <span class="token comment">//`auth`表明http基本认证应该与proxy代理链接，并提供证书</span>
  <span class="token comment">//这将会设置一个`Proxy-Authorization` header,并且会覆盖掉已经存在的`Proxy-Authorization`  header</span>
  proxy<span class="token punctuation">:</span> <span class="token punctuation">{</span>
    host<span class="token punctuation">:</span><span class="token string">'127.0.0.1'</span><span
                    class="token punctuation">,</span>
    port<span class="token punctuation">:</span> <span class="token number">9000</span><span
                    class="token punctuation">,</span>
    auth<span class="token punctuation">:</span> <span class="token punctuation">{</span>
      username<span class="token punctuation">:</span><span class="token string">'skda'</span><span
                    class="token punctuation">,</span>
      password<span class="token punctuation">:</span><span class="token string">'radsd'</span>
    <span class="token punctuation">}</span>
  <span class="token punctuation">}</span><span class="token punctuation">,</span>
  <span class="token comment">//`cancelToken`定义了一个用于取消请求的cancel token</span>
  <span class="token comment">//详见cancelation部分</span>
  cancelToken<span class="token punctuation">:</span> <span class="token keyword">new</span> <span
                    class="token class-name">cancelToken</span><span class="token punctuation">(</span><span
                    class="token keyword">function</span><span class="token punctuation">(</span><span
                    class="token parameter">cancel</span><span class="token punctuation">)</span><span
                    class="token punctuation">{</span>

  <span class="token punctuation">}</span><span class="token punctuation">)</span>
<span class="token punctuation">}</span>
<span aria-hidden="true"
      class="line-numbers-rows"><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span></span></code></pre>
    </div>
    <h2>五、请求返回的内容</h2>
    <div class="_2Uzcx_">
        <button class="VJbwyy" type="button" aria-label="复制代码"><i aria-label="icon: copy"
                                                                  class="anticon anticon-copy">
            <svg viewBox="64 64 896 896" focusable="false" class="" data-icon="copy" width="1em" height="1em"
                 fill="currentColor" aria-hidden="true">
                <path d="M832 64H296c-4.4 0-8 3.6-8 8v56c0 4.4 3.6 8 8 8h496v688c0 4.4 3.6 8 8 8h56c4.4 0 8-3.6 8-8V96c0-17.7-14.3-32-32-32zM704 192H192c-17.7 0-32 14.3-32 32v530.7c0 8.5 3.4 16.6 9.4 22.6l173.3 173.3c2.2 2.2 4.7 4 7.4 5.5v1.9h4.2c3.5 1.3 7.2 2 11 2H704c17.7 0 32-14.3 32-32V224c0-17.7-14.3-32-32-32zM350 856.2L263.9 770H350v86.2zM664 888H414V746c0-22.1-17.9-40-40-40H232V264h432v624z"></path>
            </svg>
        </i></button>
        <pre class="line-numbers  language-kotlin"><code class="  language-kotlin"><span
                class="token punctuation">{</span>

  <span class="token keyword">data</span><span class="token operator">:</span><span
                    class="token punctuation">{</span><span class="token punctuation">}</span><span
                    class="token punctuation">,</span>
  status<span class="token operator">:</span><span class="token number">200</span><span
                    class="token punctuation">,</span>
  <span class="token comment">//从服务器返回的http状态文本</span>
  statusText<span class="token operator">:</span><span class="token string">'OK'</span><span
                    class="token punctuation">,</span>
  <span class="token comment">//响应头信息</span>
  headers<span class="token operator">:</span> <span class="token punctuation">{</span><span
                    class="token punctuation">}</span><span class="token punctuation">,</span>
  <span class="token comment">//`config`是在请求的时候的一些配置信息</span>
  config<span class="token operator">:</span> <span class="token punctuation">{</span><span
                    class="token punctuation">}</span>
<span class="token punctuation">}</span>
<span aria-hidden="true"
      class="line-numbers-rows"><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span></span></code></pre>
    </div>
    <ul>
        <li>你可以这样来获取响应信息</li>
    </ul>
    <div class="_2Uzcx_">
        <button class="VJbwyy" type="button" aria-label="复制代码"><i aria-label="icon: copy"
                                                                  class="anticon anticon-copy">
            <svg viewBox="64 64 896 896" focusable="false" class="" data-icon="copy" width="1em" height="1em"
                 fill="currentColor" aria-hidden="true">
                <path d="M832 64H296c-4.4 0-8 3.6-8 8v56c0 4.4 3.6 8 8 8h496v688c0 4.4 3.6 8 8 8h56c4.4 0 8-3.6 8-8V96c0-17.7-14.3-32-32-32zM704 192H192c-17.7 0-32 14.3-32 32v530.7c0 8.5 3.4 16.6 9.4 22.6l173.3 173.3c2.2 2.2 4.7 4 7.4 5.5v1.9h4.2c3.5 1.3 7.2 2 11 2H704c17.7 0 32-14.3 32-32V224c0-17.7-14.3-32-32-32zM350 856.2L263.9 770H350v86.2zM664 888H414V746c0-22.1-17.9-40-40-40H232V264h432v624z"></path>
            </svg>
        </i></button>
        <pre class="line-numbers  language-jsx"><code class="  language-jsx">axios<span
                class="token punctuation">.</span><span class="token function">get</span><span
                class="token punctuation">(</span><span class="token string">'/user/12345'</span><span
                class="token punctuation">)</span>
  <span class="token punctuation">.</span><span class="token function">then</span><span
                    class="token punctuation">(</span><span class="token keyword">function</span><span
                    class="token punctuation">(</span><span class="token parameter">res</span><span
                    class="token punctuation">)</span><span class="token punctuation">{</span>
    console<span class="token punctuation">.</span><span class="token function">log</span><span
                    class="token punctuation">(</span>res<span class="token punctuation">.</span>data<span
                    class="token punctuation">)</span><span class="token punctuation">;</span>
    console<span class="token punctuation">.</span><span class="token function">log</span><span
                    class="token punctuation">(</span>res<span class="token punctuation">.</span>status<span
                    class="token punctuation">)</span><span class="token punctuation">;</span>
    console<span class="token punctuation">.</span><span class="token function">log</span><span
                    class="token punctuation">(</span>res<span class="token punctuation">.</span>statusText<span
                    class="token punctuation">)</span><span class="token punctuation">;</span>
    console<span class="token punctuation">.</span><span class="token function">log</span><span
                    class="token punctuation">(</span>res<span class="token punctuation">.</span>headers<span
                    class="token punctuation">)</span><span class="token punctuation">;</span>
    console<span class="token punctuation">.</span><span class="token function">log</span><span
                    class="token punctuation">(</span>res<span class="token punctuation">.</span>config<span
                    class="token punctuation">)</span><span class="token punctuation">;</span>
  <span class="token punctuation">}</span><span class="token punctuation">)</span>
<span aria-hidden="true"
      class="line-numbers-rows"><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span></span></code></pre>
    </div>
    <h2>六、默认配置</h2>
    <ul>
        <li>你可以设置默认配置，对所有请求都有效</li>
    </ul>
    <p>1、 全局默认配置</p>
    <div class="_2Uzcx_">
        <button class="VJbwyy" type="button" aria-label="复制代码"><i aria-label="icon: copy"
                                                                  class="anticon anticon-copy">
            <svg viewBox="64 64 896 896" focusable="false" class="" data-icon="copy" width="1em" height="1em"
                 fill="currentColor" aria-hidden="true">
                <path d="M832 64H296c-4.4 0-8 3.6-8 8v56c0 4.4 3.6 8 8 8h496v688c0 4.4 3.6 8 8 8h56c4.4 0 8-3.6 8-8V96c0-17.7-14.3-32-32-32zM704 192H192c-17.7 0-32 14.3-32 32v530.7c0 8.5 3.4 16.6 9.4 22.6l173.3 173.3c2.2 2.2 4.7 4 7.4 5.5v1.9h4.2c3.5 1.3 7.2 2 11 2H704c17.7 0 32-14.3 32-32V224c0-17.7-14.3-32-32-32zM350 856.2L263.9 770H350v86.2zM664 888H414V746c0-22.1-17.9-40-40-40H232V264h432v624z"></path>
            </svg>
        </i></button>
        <pre class="line-numbers  language-rust"><code class="  language-rust">axios<span
                class="token punctuation">.</span>defaults<span
                class="token punctuation">.</span>baseURL <span class="token operator">=</span> <span
                class="token lifetime-annotation symbol">'http://api.exmple.com</span><span
                class="token lifetime-annotation symbol">';</span>
axios<span class="token punctuation">.</span>defaults<span class="token punctuation">.</span>headers<span
                    class="token punctuation">.</span>common<span class="token punctuation">[</span><span
                    class="token lifetime-annotation symbol">'Authorization</span><span
                    class="token lifetime-annotation symbol">']</span> <span
                    class="token operator">=</span> AUTH_TOKEN<span
                    class="token punctuation">;</span>
axios<span class="token punctuation">.</span>defaults<span class="token punctuation">.</span>headers<span
                    class="token punctuation">.</span>post<span class="token punctuation">[</span><span
                    class="token lifetime-annotation symbol">'content-Type</span><span
                    class="token lifetime-annotation symbol">']</span> <span class="token operator">=</span> <span
                    class="token lifetime-annotation symbol">'appliction/x-www-form-urlencoded</span><span
                    class="token lifetime-annotation symbol">';</span>
<span aria-hidden="true" class="line-numbers-rows"><span></span><span></span><span></span></span></code></pre>
    </div>
    <p>2、 自定义的实例默认设置</p>
    <div class="_2Uzcx_">
        <button class="VJbwyy" type="button" aria-label="复制代码"><i aria-label="icon: copy"
                                                                  class="anticon anticon-copy">
            <svg viewBox="64 64 896 896" focusable="false" class="" data-icon="copy" width="1em" height="1em"
                 fill="currentColor" aria-hidden="true">
                <path d="M832 64H296c-4.4 0-8 3.6-8 8v56c0 4.4 3.6 8 8 8h496v688c0 4.4 3.6 8 8 8h56c4.4 0 8-3.6 8-8V96c0-17.7-14.3-32-32-32zM704 192H192c-17.7 0-32 14.3-32 32v530.7c0 8.5 3.4 16.6 9.4 22.6l173.3 173.3c2.2 2.2 4.7 4 7.4 5.5v1.9h4.2c3.5 1.3 7.2 2 11 2H704c17.7 0 32-14.3 32-32V224c0-17.7-14.3-32-32-32zM350 856.2L263.9 770H350v86.2zM664 888H414V746c0-22.1-17.9-40-40-40H232V264h432v624z"></path>
            </svg>
        </i></button>
        <pre class="line-numbers  language-csharp"><code class="  language-csharp"><span class="token comment">//当创建实例的时候配置默认配置</span>
<span class="token keyword">var</span> instance <span class="token operator">=</span> axios<span
                    class="token punctuation">.</span><span class="token function">create</span><span
                    class="token punctuation">(</span><span class="token punctuation">{</span>
    baseURL<span class="token punctuation">:</span> <span class="token string">'https://api.example.com'</span>
<span class="token punctuation">}</span><span class="token punctuation">)</span><span class="token punctuation">;</span>

<span class="token comment">//当实例创建时候修改配置</span>
instance<span class="token punctuation">.</span>defaults<span class="token punctuation">.</span>headers<span
                    class="token punctuation">.</span>common<span class="token punctuation">[</span><span
                    class="token string">"Authorization"</span><span class="token punctuation">]</span> <span
                    class="token operator">=</span> AUTH_TOKEN<span class="token punctuation">;</span>
<span aria-hidden="true"
      class="line-numbers-rows"><span></span><span></span><span></span><span></span><span></span><span></span><span></span></span></code></pre>
    </div>
    <p>3、 配置中的有优先级</p>
    <ul>
        <li>config配置将会以优先级别来合并，顺序是lib/defauts.js中的默认配置，然后是实例中的默认配置，最后是请求中的config参数的配置，越往后等级越高，后面的会覆盖前面的例子。</li>
    </ul>
    <div class="_2Uzcx_">
        <button class="VJbwyy" type="button" aria-label="复制代码"><i aria-label="icon: copy"
                                                                  class="anticon anticon-copy">
            <svg viewBox="64 64 896 896" focusable="false" class="" data-icon="copy" width="1em" height="1em"
                 fill="currentColor" aria-hidden="true">
                <path d="M832 64H296c-4.4 0-8 3.6-8 8v56c0 4.4 3.6 8 8 8h496v688c0 4.4 3.6 8 8 8h56c4.4 0 8-3.6 8-8V96c0-17.7-14.3-32-32-32zM704 192H192c-17.7 0-32 14.3-32 32v530.7c0 8.5 3.4 16.6 9.4 22.6l173.3 173.3c2.2 2.2 4.7 4 7.4 5.5v1.9h4.2c3.5 1.3 7.2 2 11 2H704c17.7 0 32-14.3 32-32V224c0-17.7-14.3-32-32-32zM350 856.2L263.9 770H350v86.2zM664 888H414V746c0-22.1-17.9-40-40-40H232V264h432v624z"></path>
            </svg>
        </i></button>
        <pre class="line-numbers  language-csharp"><code class="  language-csharp"><span class="token comment">//创建一个实例的时候会使用libray目录中的默认配置</span>
<span class="token comment">//在这里timeout配置的值为0，来自于libray的默认值</span>
<span class="token keyword">var</span> instance <span class="token operator">=</span> axios<span
                    class="token punctuation">.</span><span class="token function">create</span><span
                    class="token punctuation">(</span><span class="token punctuation">)</span><span
                    class="token punctuation">;</span>
<span class="token comment">//回覆盖掉library的默认值</span>
<span class="token comment">//现在所有的请求都要等2.5S之后才会发出</span>
instance<span class="token punctuation">.</span>defaults<span class="token punctuation">.</span>timeout <span
                    class="token operator">=</span> <span class="token number">2500</span><span
                    class="token punctuation">;</span>
<span class="token comment">//这里的timeout回覆盖之前的2.5S变成5s</span>
instance<span class="token punctuation">.</span><span class="token keyword">get</span><span
                    class="token punctuation">(</span><span class="token string">'/longRequest'</span><span
                    class="token punctuation">,</span><span class="token punctuation">{</span>
  timeout<span class="token punctuation">:</span> <span class="token number">5000</span>
<span class="token punctuation">}</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
<span aria-hidden="true"
      class="line-numbers-rows"><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span></span></code></pre>
    </div>
    <h2>七、拦截器</h2>
    <ul>
        <li>你可以在请求、响应在到达<code>then/catch</code>之前拦截他们</li>
    </ul>
    <div class="_2Uzcx_">
        <button class="VJbwyy" type="button" aria-label="复制代码"><i aria-label="icon: copy"
                                                                  class="anticon anticon-copy">
            <svg viewBox="64 64 896 896" focusable="false" class="" data-icon="copy" width="1em" height="1em"
                 fill="currentColor" aria-hidden="true">
                <path d="M832 64H296c-4.4 0-8 3.6-8 8v56c0 4.4 3.6 8 8 8h496v688c0 4.4 3.6 8 8 8h56c4.4 0 8-3.6 8-8V96c0-17.7-14.3-32-32-32zM704 192H192c-17.7 0-32 14.3-32 32v530.7c0 8.5 3.4 16.6 9.4 22.6l173.3 173.3c2.2 2.2 4.7 4 7.4 5.5v1.9h4.2c3.5 1.3 7.2 2 11 2H704c17.7 0 32-14.3 32-32V224c0-17.7-14.3-32-32-32zM350 856.2L263.9 770H350v86.2zM664 888H414V746c0-22.1-17.9-40-40-40H232V264h432v624z"></path>
            </svg>
        </i></button>
        <pre class="line-numbers  language-jsx"><code class="  language-jsx"><span
                class="token comment">//添加一个请求拦截器</span>
axios<span class="token punctuation">.</span>interceptors<span class="token punctuation">.</span>request<span
                    class="token punctuation">.</span><span class="token function">use</span><span
                    class="token punctuation">(</span><span class="token keyword">function</span><span
                    class="token punctuation">(</span><span class="token parameter">config</span><span
                    class="token punctuation">)</span><span class="token punctuation">{</span>
  <span class="token comment">//在请求发出之前进行一些操作</span>
  <span class="token keyword">return</span> config<span class="token punctuation">;</span>
<span class="token punctuation">}</span><span class="token punctuation">,</span><span
                    class="token keyword">function</span><span class="token punctuation">(</span><span
                    class="token parameter">err</span><span class="token punctuation">)</span><span
                    class="token punctuation">{</span>
  <span class="token comment">//Do something with request error</span>
  <span class="token keyword">return</span> Promise<span class="token punctuation">.</span><span class="token function">reject</span><span
                    class="token punctuation">(</span>error<span class="token punctuation">)</span><span
                    class="token punctuation">;</span>
<span class="token punctuation">}</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
<span class="token comment">//添加一个响应拦截器</span>
axios<span class="token punctuation">.</span>interceptors<span class="token punctuation">.</span>response<span
                    class="token punctuation">.</span><span class="token function">use</span><span
                    class="token punctuation">(</span><span class="token keyword">function</span><span
                    class="token punctuation">(</span><span class="token parameter">res</span><span
                    class="token punctuation">)</span><span class="token punctuation">{</span>
  <span class="token comment">//在这里对返回的数据进行处理</span>
  <span class="token keyword">return</span> res<span class="token punctuation">;</span>
<span class="token punctuation">}</span><span class="token punctuation">,</span><span
                    class="token keyword">function</span><span class="token punctuation">(</span><span
                    class="token parameter">err</span><span class="token punctuation">)</span><span
                    class="token punctuation">{</span>
  <span class="token comment">//Do something with response error</span>
  <span class="token keyword">return</span> Promise<span class="token punctuation">.</span><span class="token function">reject</span><span
                    class="token punctuation">(</span>error<span class="token punctuation">)</span><span
                    class="token punctuation">;</span>
<span class="token punctuation">}</span><span class="token punctuation">)</span>


<span aria-hidden="true"
      class="line-numbers-rows"><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span></span></code></pre>
    </div>
    <p>2、取消拦截器</p>
    <div class="_2Uzcx_">
        <button class="VJbwyy" type="button" aria-label="复制代码"><i aria-label="icon: copy"
                                                                  class="anticon anticon-copy">
            <svg viewBox="64 64 896 896" focusable="false" class="" data-icon="copy" width="1em" height="1em"
                 fill="currentColor" aria-hidden="true">
                <path d="M832 64H296c-4.4 0-8 3.6-8 8v56c0 4.4 3.6 8 8 8h496v688c0 4.4 3.6 8 8 8h56c4.4 0 8-3.6 8-8V96c0-17.7-14.3-32-32-32zM704 192H192c-17.7 0-32 14.3-32 32v530.7c0 8.5 3.4 16.6 9.4 22.6l173.3 173.3c2.2 2.2 4.7 4 7.4 5.5v1.9h4.2c3.5 1.3 7.2 2 11 2H704c17.7 0 32-14.3 32-32V224c0-17.7-14.3-32-32-32zM350 856.2L263.9 770H350v86.2zM664 888H414V746c0-22.1-17.9-40-40-40H232V264h432v624z"></path>
            </svg>
        </i></button>
        <pre class="line-numbers  language-jsx"><code class="  language-jsx"><span class="token keyword">var</span> myInterceptor <span
                class="token operator">=</span> axios<span class="token punctuation">.</span>interceptor<span
                class="token punctuation">.</span>request<span class="token punctuation">.</span><span
                class="token function">use</span><span class="token punctuation">(</span><span
                class="token keyword">function</span><span class="token punctuation">(</span><span
                class="token punctuation">)</span><span class="token punctuation">{</span><span
                class="token comment">/*....*/</span><span class="token punctuation">}</span><span
                class="token punctuation">)</span><span class="token punctuation">;</span>
axios<span class="token punctuation">.</span>interceptors<span class="token punctuation">.</span>request<span
                    class="token punctuation">.</span><span class="token function">eject</span><span
                    class="token punctuation">(</span>myInterceptor<span class="token punctuation">)</span><span
                    class="token punctuation">;</span>
<span aria-hidden="true" class="line-numbers-rows"><span></span><span></span></span></code></pre>
    </div>
    <p>3、 给自定义的axios实例添加拦截器</p>
    <div class="_2Uzcx_">
        <button class="VJbwyy" type="button" aria-label="复制代码"><i aria-label="icon: copy"
                                                                  class="anticon anticon-copy">
            <svg viewBox="64 64 896 896" focusable="false" class="" data-icon="copy" width="1em" height="1em"
                 fill="currentColor" aria-hidden="true">
                <path d="M832 64H296c-4.4 0-8 3.6-8 8v56c0 4.4 3.6 8 8 8h496v688c0 4.4 3.6 8 8 8h56c4.4 0 8-3.6 8-8V96c0-17.7-14.3-32-32-32zM704 192H192c-17.7 0-32 14.3-32 32v530.7c0 8.5 3.4 16.6 9.4 22.6l173.3 173.3c2.2 2.2 4.7 4 7.4 5.5v1.9h4.2c3.5 1.3 7.2 2 11 2H704c17.7 0 32-14.3 32-32V224c0-17.7-14.3-32-32-32zM350 856.2L263.9 770H350v86.2zM664 888H414V746c0-22.1-17.9-40-40-40H232V264h432v624z"></path>
            </svg>
        </i></button>
        <pre class="line-numbers  language-jsx"><code class="  language-jsx"><span class="token keyword">var</span> instance <span
                class="token operator">=</span> axios<span class="token punctuation">.</span><span
                class="token function">create</span><span class="token punctuation">(</span><span
                class="token punctuation">)</span><span class="token punctuation">;</span>
instance<span class="token punctuation">.</span>interceptors<span class="token punctuation">.</span>request<span
                    class="token punctuation">.</span><span class="token function">use</span><span
                    class="token punctuation">(</span><span class="token keyword">function</span><span
                    class="token punctuation">(</span><span class="token punctuation">)</span><span
                    class="token punctuation">{</span><span class="token punctuation">}</span><span
                    class="token punctuation">)</span>
<span aria-hidden="true" class="line-numbers-rows"><span></span><span></span></span></code></pre>
    </div>
    <h2>八、错误处理</h2>
    <div class="_2Uzcx_">
        <button class="VJbwyy" type="button" aria-label="复制代码"><i aria-label="icon: copy"
                                                                  class="anticon anticon-copy">
            <svg viewBox="64 64 896 896" focusable="false" class="" data-icon="copy" width="1em" height="1em"
                 fill="currentColor" aria-hidden="true">
                <path d="M832 64H296c-4.4 0-8 3.6-8 8v56c0 4.4 3.6 8 8 8h496v688c0 4.4 3.6 8 8 8h56c4.4 0 8-3.6 8-8V96c0-17.7-14.3-32-32-32zM704 192H192c-17.7 0-32 14.3-32 32v530.7c0 8.5 3.4 16.6 9.4 22.6l173.3 173.3c2.2 2.2 4.7 4 7.4 5.5v1.9h4.2c3.5 1.3 7.2 2 11 2H704c17.7 0 32-14.3 32-32V224c0-17.7-14.3-32-32-32zM350 856.2L263.9 770H350v86.2zM664 888H414V746c0-22.1-17.9-40-40-40H232V264h432v624z"></path>
            </svg>
        </i></button>
        <pre class="line-numbers  language-jsx"><code class="  language-jsx">axios<span
                class="token punctuation">.</span><span class="token function">get</span><span
                class="token punctuation">(</span><span class="token string">'/user/12345'</span><span
                class="token punctuation">)</span>
  <span class="token punctuation">.</span><span class="token function">catch</span><span
                    class="token punctuation">(</span><span class="token keyword">function</span><span
                    class="token punctuation">(</span><span class="token parameter">error</span><span
                    class="token punctuation">)</span><span class="token punctuation">{</span>
    <span class="token keyword">if</span><span class="token punctuation">(</span>error<span
                    class="token punctuation">.</span>response<span class="token punctuation">)</span><span
                    class="token punctuation">{</span>
      <span class="token comment">//请求已经发出，但是服务器响应返回的状态吗不在2xx的范围内</span>
      console<span class="token punctuation">.</span><span class="token function">log</span><span
                    class="token punctuation">(</span>error<span class="token punctuation">.</span>response<span
                    class="token punctuation">.</span>data<span class="token punctuation">)</span><span
                    class="token punctuation">;</span>
      console<span class="token punctuation">.</span><span class="token function">log</span><span
                    class="token punctuation">(</span>error<span class="token punctuation">.</span>response<span
                    class="token punctuation">.</span>status<span class="token punctuation">)</span><span
                    class="token punctuation">;</span>
      console<span class="token punctuation">.</span><span class="token function">log</span><span
                    class="token punctuation">(</span>error<span class="token punctuation">.</span>response<span
                    class="token punctuation">.</span>header<span class="token punctuation">)</span><span
                    class="token punctuation">;</span>
    <span class="token punctuation">}</span><span class="token keyword">else</span> <span
                    class="token punctuation">{</span>
      <span class="token comment">//一些错误是在设置请求的时候触发</span>
      console<span class="token punctuation">.</span><span class="token function">log</span><span
                    class="token punctuation">(</span><span class="token string">'Error'</span><span
                    class="token punctuation">,</span>error<span class="token punctuation">.</span>message<span
                    class="token punctuation">)</span><span class="token punctuation">;</span>
    <span class="token punctuation">}</span>
    console<span class="token punctuation">.</span><span class="token function">log</span><span
                    class="token punctuation">(</span>error<span class="token punctuation">.</span>config<span
                    class="token punctuation">)</span><span class="token punctuation">;</span>
  <span class="token punctuation">}</span><span class="token punctuation">)</span><span
                    class="token punctuation">;</span>
<span aria-hidden="true"
      class="line-numbers-rows"><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span></span></code></pre>
    </div>
    <h2>九、取消</h2>
    <ul>
        <li>你可以通过一个<code>cancel token</code>来取消一个请求</li>
    </ul>
    <ol>
        <li>你可以通过<code>CancelToken.source</code>工厂函数来创建一个<code>cancel token</code>
        </li>
    </ol>
    <div class="_2Uzcx_">
        <button class="VJbwyy" type="button" aria-label="复制代码"><i aria-label="icon: copy"
                                                                  class="anticon anticon-copy">
            <svg viewBox="64 64 896 896" focusable="false" class="" data-icon="copy" width="1em" height="1em"
                 fill="currentColor" aria-hidden="true">
                <path d="M832 64H296c-4.4 0-8 3.6-8 8v56c0 4.4 3.6 8 8 8h496v688c0 4.4 3.6 8 8 8h56c4.4 0 8-3.6 8-8V96c0-17.7-14.3-32-32-32zM704 192H192c-17.7 0-32 14.3-32 32v530.7c0 8.5 3.4 16.6 9.4 22.6l173.3 173.3c2.2 2.2 4.7 4 7.4 5.5v1.9h4.2c3.5 1.3 7.2 2 11 2H704c17.7 0 32-14.3 32-32V224c0-17.7-14.3-32-32-32zM350 856.2L263.9 770H350v86.2zM664 888H414V746c0-22.1-17.9-40-40-40H232V264h432v624z"></path>
            </svg>
        </i></button>
        <pre class="line-numbers  language-jsx"><code class="  language-jsx"><span class="token keyword">var</span> CancelToken <span
                class="token operator">=</span> axios<span class="token punctuation">.</span>CancelToken<span
                class="token punctuation">;</span>
<span class="token keyword">var</span> source <span class="token operator">=</span> CancelToken<span
                    class="token punctuation">.</span><span class="token function">source</span><span
                    class="token punctuation">(</span><span class="token punctuation">)</span><span
                    class="token punctuation">;</span>

axios<span class="token punctuation">.</span><span class="token function">get</span><span
                    class="token punctuation">(</span><span class="token string">'/user/12345'</span><span
                    class="token punctuation">,</span><span class="token punctuation">{</span>
  cancelToken<span class="token punctuation">:</span> source<span class="token punctuation">.</span>token
<span class="token punctuation">}</span><span class="token punctuation">)</span><span class="token punctuation">.</span><span
                    class="token function">catch</span><span class="token punctuation">(</span><span
                    class="token keyword">function</span><span class="token punctuation">(</span><span
                    class="token parameter">thrown</span><span class="token punctuation">)</span><span
                    class="token punctuation">{</span>
  <span class="token keyword">if</span><span class="token punctuation">(</span>axios<span
                    class="token punctuation">.</span><span class="token function">isCancel</span><span
                    class="token punctuation">(</span>thrown<span class="token punctuation">)</span><span
                    class="token punctuation">)</span><span class="token punctuation">{</span>
    console<span class="token punctuation">.</span><span class="token function">log</span><span
                    class="token punctuation">(</span><span class="token string">'Request canceled'</span><span
                    class="token punctuation">,</span>thrown<span class="token punctuation">.</span>message<span
                    class="token punctuation">)</span><span class="token punctuation">;</span>
  <span class="token punctuation">}</span><span class="token keyword">else</span> <span
                    class="token punctuation">{</span>
    <span class="token comment">//handle error</span>
  <span class="token punctuation">}</span>
<span class="token punctuation">}</span><span class="token punctuation">)</span><span class="token punctuation">;</span>

<span class="token comment">//取消请求（信息的参数可以设置的）</span>
source<span class="token punctuation">.</span><span class="token function">cance</span><span
                    class="token punctuation">(</span><span class="token string">"操作被用户取消"</span><span
                    class="token punctuation">)</span><span class="token punctuation">;</span>

<span aria-hidden="true"
      class="line-numbers-rows"><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span></span></code></pre>
    </div>
    <ol start="2">
        <li>你可以给cancelToken构造函数传递一个executor function来创建一个cancel token:</li>
    </ol>
    <div class="_2Uzcx_">
        <button class="VJbwyy" type="button" aria-label="复制代码"><i aria-label="icon: copy"
                                                                  class="anticon anticon-copy">
            <svg viewBox="64 64 896 896" focusable="false" class="" data-icon="copy" width="1em" height="1em"
                 fill="currentColor" aria-hidden="true">
                <path d="M832 64H296c-4.4 0-8 3.6-8 8v56c0 4.4 3.6 8 8 8h496v688c0 4.4 3.6 8 8 8h56c4.4 0 8-3.6 8-8V96c0-17.7-14.3-32-32-32zM704 192H192c-17.7 0-32 14.3-32 32v530.7c0 8.5 3.4 16.6 9.4 22.6l173.3 173.3c2.2 2.2 4.7 4 7.4 5.5v1.9h4.2c3.5 1.3 7.2 2 11 2H704c17.7 0 32-14.3 32-32V224c0-17.7-14.3-32-32-32zM350 856.2L263.9 770H350v86.2zM664 888H414V746c0-22.1-17.9-40-40-40H232V264h432v624z"></path>
            </svg>
        </i></button>
        <pre class="line-numbers  language-jsx"><code class="  language-jsx"><span class="token keyword">var</span> cancelToken <span
                class="token operator">=</span> axios<span class="token punctuation">.</span>CancelToken<span
                class="token punctuation">;</span>
<span class="token keyword">var</span> cance<span class="token punctuation">;</span>
axios<span class="token punctuation">.</span><span class="token function">get</span><span
                    class="token punctuation">(</span><span class="token string">'/user/12345'</span><span
                    class="token punctuation">,</span><span class="token punctuation">{</span>
  cancelToken<span class="token punctuation">:</span> <span class="token keyword">new</span> <span
                    class="token class-name">CancelToken</span><span class="token punctuation">(</span><span
                    class="token keyword">function</span><span class="token punctuation">(</span><span
                    class="token parameter">c</span><span class="token punctuation">)</span><span
                    class="token punctuation">{</span>
    <span class="token comment">//这个executor函数接受一个cancel function作为参数</span>
    cancel <span class="token operator">=</span> c<span class="token punctuation">;</span>
  <span class="token punctuation">}</span><span class="token punctuation">)</span>
<span class="token punctuation">}</span><span class="token punctuation">)</span>
<span class="token comment">//取消请求</span>
<span class="token function">cancel</span><span class="token punctuation">(</span><span
                    class="token punctuation">)</span><span class="token punctuation">;</span>
<span aria-hidden="true"
      class="line-numbers-rows"><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span></span></code></pre>
    </div>
</article>
<div></div>
<div class="_1kCBjS">
    <div class="_18vaTa">
        <div class="_3BUZPB">
            <div class="_2Bo4Th" role="button" tabindex="-1" aria-label="给文章点赞"><i aria-label="ic-like"
                                                                                   class="anticon">
                <svg width="1em" height="1em" fill="currentColor" aria-hidden="true" focusable="false" class="">
                    <use xlink:href="#ic-like"></use>
                </svg>
            </i></div>
            <span class="_1LOh_5" role="button" tabindex="-1" aria-label="查看点赞列表">267人点赞<i aria-label="icon: right"
                                                                                           class="anticon anticon-right"><svg viewBox="64 64 896 896" focusable="false" class="" data-icon="right" width="1em" height="1em"
                    fill="currentColor" aria-hidden="true"><path
                    d="M765.7 486.8L314.9 134.7A7.97 7.97 0 0 0 302 141v77.3c0 4.9 2.3 9.6 6.1 12.6l360 281.1-360 281.1c-3.9 3-6.1 7.7-6.1 12.6V883c0 6.7 7.7 10.4 12.9 6.3l450.8-352.1a31.96 31.96 0 0 0 0-50.4z"></path></svg></i></span>
        </div>
        <div class="_3BUZPB">
            <div class="_2Bo4Th" role="button" tabindex="-1"><i aria-label="ic-dislike" class="anticon">
                <svg width="1em" height="1em" fill="currentColor" aria-hidden="true" focusable="false" class="">
                    <use xlink:href="#ic-dislike"></use>
                </svg>
            </i></div>
        </div>
    </div>
    <div class="_18vaTa"><a class="_3BUZPB _1x1ok9 _1OhGeD" href="/nb/10418276" target="_blank"
                            rel="noopener noreferrer"><i aria-label="ic-notebook" class="anticon">
        <svg width="1em" height="1em" fill="currentColor" aria-hidden="true" focusable="false" class="">
            <use xlink:href="#ic-notebook"></use>
        </svg>
    </i><span>通信</span></a>
        <div class="_3BUZPB ant-dropdown-trigger">
            <div class="_2Bo4Th"><i aria-label="ic-others" class="anticon">
                <svg width="1em" height="1em" fill="currentColor" aria-hidden="true" focusable="false" class="">
                    <use xlink:href="#ic-others"></use>
                </svg>
            </i></div>
        </div>
    </div>
</div>
<div class="_19DgIp" style="margin-top:24px;margin-bottom:24px"></div>
<div class="_13lIbp">
    <div class="_191KSt">"小礼物走一走，来简书关注我"</div>
    <button type="button" class="_1OyPqC _3Mi9q9 _2WY0RL _1YbC5u"><span>赞赏支持</span></button>
    <span class="_3zdmIj">还没有人赞赏，支持一下</span></div>
<div class="d0hShY"><a class="_1OhGeD" href="/u/cc401bccfdf8" target="_blank" rel="noopener noreferrer"><img
        class="_27NmgV"
        src="https://upload.jianshu.io/users/upload_avatars/4499098/a839bb46-6e73-4404-b544-09f0dcd902e2?imageMogr2/auto-orient/strip|imageView2/1/w/100/h/100/format/webp"
        alt="  "></a>
    <div class="Uz-vZq">
        <div class="Cqpr1X"><a class="HC3FFO _1OhGeD" href="/u/cc401bccfdf8" title="FunnySeeker" target="_blank"
                               rel="noopener noreferrer">FunnySeeker</a><span class="_2WEj6j" title=""></span></div>
        <div class="lJvI3S"><span>总资产3 (约0.35元)</span><span>共写了693字</span><span>获得273个赞</span><span>共175个粉丝</span>
        </div>
    </div>
    <button data-locale="zh-CN" type="button" class="_1OyPqC _3Mi9q9"><span>关注</span></button>
</div>
