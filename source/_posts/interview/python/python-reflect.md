---
title: "python3中的反射详解"
date:       2019-11-28
subtitle: "Java中是支持python3中的反射详解的。在高级的Python中当然也是支持"
tags:
	- Python
	- solution
	- interview
---


<p>相信很多人和我一样第一次听到<code>反射</code>这个词语是特别陌生的，再次之前我最熟悉的还是c语言，但是在c语言中并没有反射这种机制。<br>
    c++中原生并不支持反射机制，但是Java中是支持的。在高级的Python中当然也是支持的。</p>
<h1>什么是反射？</h1>
<p>说到反射，我并不想用很多专业晦涩难懂的词语，因为也不是很懂害怕出错，如果那里有错还请指正。</p>
<p>相信我们是经常使用浏览器的，在使用浏览器的时候最重要的也不就是输入网址了，在浏览器的地址栏中输入对应的网址，对应的网站也就会有反应，并给你返回对应的网页。首相我们要知道，我们输入到浏览器地址栏的<code>url</code>是一个字符串，这个字符串的<code>url</code>到web服务器上后是怎么找到对应的代码函数并执行后给我们返回内容的。
</p>
<p>比如：现在我们有这样一个需求，已知有三个函数<code>fun1</code>, <code>fun2</code>, <code>fun3</code>这三个函数，我们都找到如果我们想调用其中某个函数的时候，我们就只有在代码中写好，比如我写了一个这样的代码来实现这个功能：
</p>
<p>首先在文件项目下创建两个文件：<code>test.py</code>, <code>s.py</code>这两个python文件</p>
<div class="image-package">
    <div class="image-container" style="max-width: 700px; max-height: 414px; background-color: transparent;">
        <div class="image-container-fill" style="padding-bottom: 37.3%;"></div>
        <div class="image-view" data-width="1110" data-height="414"><img
                data-original-src="//upload-images.jianshu.io/upload_images/13859457-3c31dd82c446cc0e.png"
                data-original-width="1110" data-original-height="414" data-original-format="image/png"
                data-original-filesize="72108" class="" data-image-index="0" style="cursor: zoom-in;"
                src="//upload-images.jianshu.io/upload_images/13859457-3c31dd82c446cc0e.png?imageMogr2/auto-orient/strip|imageView2/2/w/1110/format/webp">
        </div>
    </div>
    <div class="image-caption"></div>
</div>
<p><code>s.py</code>,代码如下：</p>
<pre class="line-numbers  language-python"><code class="  language-python"><span
        class="token keyword">def</span> <span class="token function">fun2</span><span
        class="token punctuation">(</span><span class="token punctuation">)</span><span
        class="token punctuation">:</span>
    <span class="token keyword">return</span> <span class="token string">"fun2"</span>


<span class="token keyword">def</span> <span class="token function">fun1</span><span
            class="token punctuation">(</span><span class="token punctuation">)</span><span
            class="token punctuation">:</span>
    <span class="token keyword">return</span> <span class="token string">'fun1'</span>


<span class="token keyword">def</span> <span class="token function">fun3</span><span
            class="token punctuation">(</span><span class="token punctuation">)</span><span
            class="token punctuation">:</span>
    <span class="token keyword">return</span> <span class="token string">'fun3'</span>
<span aria-hidden="true"
      class="line-numbers-rows"><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span></span></code><button
        class="VJbwyy" type="button" aria-label="复制代码"><i aria-label="icon: copy" class="anticon anticon-copy"><svg
        viewBox="64 64 896 896" focusable="false" class="" data-icon="copy" width="1em" height="1em"
        fill="currentColor" aria-hidden="true"><path
        d="M832 64H296c-4.4 0-8 3.6-8 8v56c0 4.4 3.6 8 8 8h496v688c0 4.4 3.6 8 8 8h56c4.4 0 8-3.6 8-8V96c0-17.7-14.3-32-32-32zM704 192H192c-17.7 0-32 14.3-32 32v530.7c0 8.5 3.4 16.6 9.4 22.6l173.3 173.3c2.2 2.2 4.7 4 7.4 5.5v1.9h4.2c3.5 1.3 7.2 2 11 2H704c17.7 0 32-14.3 32-32V224c0-17.7-14.3-32-32-32zM350 856.2L263.9 770H350v86.2zM664 888H414V746c0-22.1-17.9-40-40-40H232V264h432v624z"></path></svg></i></button></pre>
<p><code>test.py</code>，代码如下：</p>
<pre class="line-numbers  language-python"><code class="  language-python"><span class="token keyword">import</span> s  <span
        class="token comment">#导入s.py文件。</span>

call_str <span class="token operator">=</span> <span class="token builtin">input</span><span
            class="token punctuation">(</span><span
            class="token string">"input which function you want to call :"</span><span
            class="token punctuation">)</span>

<span class="token keyword">if</span> call_str <span class="token operator">==</span> <span
            class="token string">'fun1'</span><span class="token punctuation">:</span>
    <span class="token keyword">print</span><span class="token punctuation">(</span>s<span
            class="token punctuation">.</span>fun1<span class="token punctuation">(</span><span
            class="token punctuation">)</span><span class="token punctuation">)</span>
<span class="token keyword">elif</span> call_str <span class="token operator">==</span> <span class="token string">'fun2'</span><span
            class="token punctuation">:</span>
    <span class="token keyword">print</span><span class="token punctuation">(</span>s<span
            class="token punctuation">.</span>fun2<span class="token punctuation">(</span><span
            class="token punctuation">)</span><span class="token punctuation">)</span>
<span class="token keyword">elif</span> call_str <span class="token operator">==</span> <span class="token string">'fun3'</span><span
            class="token punctuation">:</span>
    <span class="token keyword">print</span><span class="token punctuation">(</span>s<span
            class="token punctuation">.</span>fun3<span class="token punctuation">(</span><span
            class="token punctuation">)</span><span class="token punctuation">)</span>
<span class="token keyword">else</span><span class="token punctuation">:</span>
    <span class="token keyword">print</span><span class="token punctuation">(</span><span class="token string">"404 not Found"</span><span
            class="token punctuation">)</span>
<span aria-hidden="true"
      class="line-numbers-rows"><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span></span></code><button
        class="VJbwyy" type="button" aria-label="复制代码"><i aria-label="icon: copy" class="anticon anticon-copy"><svg
        viewBox="64 64 896 896" focusable="false" class="" data-icon="copy" width="1em" height="1em"
        fill="currentColor" aria-hidden="true"><path
        d="M832 64H296c-4.4 0-8 3.6-8 8v56c0 4.4 3.6 8 8 8h496v688c0 4.4 3.6 8 8 8h56c4.4 0 8-3.6 8-8V96c0-17.7-14.3-32-32-32zM704 192H192c-17.7 0-32 14.3-32 32v530.7c0 8.5 3.4 16.6 9.4 22.6l173.3 173.3c2.2 2.2 4.7 4 7.4 5.5v1.9h4.2c3.5 1.3 7.2 2 11 2H704c17.7 0 32-14.3 32-32V224c0-17.7-14.3-32-32-32zM350 856.2L263.9 770H350v86.2zM664 888H414V746c0-22.1-17.9-40-40-40H232V264h432v624z"></path></svg></i></button></pre>
<p>
    运行文件<code>test.py</code>后输入对应的函数名就可以调用相应的函数了。如果在<code>s.py</code>文件中，有上千个函数呢！岂不是我想像以上方式调用的时候得写上千个判断语句，这样是不是太麻烦了。<br>
    所以python给我们提供了强大的反射机制，这个反射机制是通过<code>字符串返回映射到代码中的一种机制</code>。<br>
    这便是反射的意思了，如果你还不是很明白还可以继续百度，参考其他的写的文章了。</p>
<h1>python怎样使用反射</h1>
<p>首先，python给我嗯提供了四个关于反射的四个内置函数分别是：</p>
<ol>
    <li><code>getattr</code></li>
    <li><code>setattr</code></li>
    <li><code>delattr</code></li>
    <li><code>hasattr</code></li>
</ol>
<p>下面我们简单的学习下这四个函数的有关用法：<br>
    在上面我是用if判断语句来实现函数的调用，这里我使用<code>getattr</code>的方法来调用，在<code>test.py</code>中增加代码如下：</p>
<pre class="line-numbers  language-python"><code class="  language-python"><span class="token keyword">import</span> s

call_str <span class="token operator">=</span> <span class="token builtin">input</span><span
            class="token punctuation">(</span><span
            class="token string">"input which function you want to call :"</span><span
            class="token punctuation">)</span>

<span class="token keyword">if</span> call_str <span class="token operator">==</span> <span
            class="token string">'fun1'</span><span class="token punctuation">:</span>
    <span class="token keyword">print</span><span class="token punctuation">(</span>s<span
            class="token punctuation">.</span>fun1<span class="token punctuation">(</span><span
            class="token punctuation">)</span><span class="token punctuation">)</span>
<span class="token keyword">elif</span> call_str <span class="token operator">==</span> <span class="token string">'fun2'</span><span
            class="token punctuation">:</span>
    <span class="token keyword">print</span><span class="token punctuation">(</span>s<span
            class="token punctuation">.</span>fun2<span class="token punctuation">(</span><span
            class="token punctuation">)</span><span class="token punctuation">)</span>
<span class="token keyword">elif</span> call_str <span class="token operator">==</span> <span class="token string">'fun3'</span><span
            class="token punctuation">:</span>
    <span class="token keyword">print</span><span class="token punctuation">(</span>s<span
            class="token punctuation">.</span>fun3<span class="token punctuation">(</span><span
            class="token punctuation">)</span><span class="token punctuation">)</span>
<span class="token keyword">else</span><span class="token punctuation">:</span>
    <span class="token keyword">print</span><span class="token punctuation">(</span><span class="token string">"404 not Found"</span><span
            class="token punctuation">)</span>

obj <span class="token operator">=</span> <span class="token builtin">getattr</span><span
            class="token punctuation">(</span>s<span class="token punctuation">,</span> call_str<span
            class="token punctuation">)</span> <span class="token comment"># 其中的s是值的带入的s文件，s也可以换为其他的你想倒入的模块等</span>
<span class="token keyword">print</span><span class="token punctuation">(</span>obj<span
            class="token punctuation">(</span><span class="token punctuation">)</span><span
            class="token punctuation">)</span>
<span aria-hidden="true"
      class="line-numbers-rows"><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span></span></code><button
        class="VJbwyy" type="button" aria-label="复制代码"><i aria-label="icon: copy" class="anticon anticon-copy"><svg
        viewBox="64 64 896 896" focusable="false" class="" data-icon="copy" width="1em" height="1em"
        fill="currentColor" aria-hidden="true"><path
        d="M832 64H296c-4.4 0-8 3.6-8 8v56c0 4.4 3.6 8 8 8h496v688c0 4.4 3.6 8 8 8h56c4.4 0 8-3.6 8-8V96c0-17.7-14.3-32-32-32zM704 192H192c-17.7 0-32 14.3-32 32v530.7c0 8.5 3.4 16.6 9.4 22.6l173.3 173.3c2.2 2.2 4.7 4 7.4 5.5v1.9h4.2c3.5 1.3 7.2 2 11 2H704c17.7 0 32-14.3 32-32V224c0-17.7-14.3-32-32-32zM350 856.2L263.9 770H350v86.2zM664 888H414V746c0-22.1-17.9-40-40-40H232V264h432v624z"></path></svg></i></button></pre>
<p>运行后我们输入 <code>fun1</code>, <code>fun2</code>, <code>fun3</code>都没有问题，但是当我们乱输入一个字符串的时候<code>getattr</code>内置函数就报如下的错误：<br>
    <code>module 's' has no attribute 'asf'</code></p>
<p>怎么解决这个问题呢？我们就可以使用<code>hasattr</code>这一个内置函数了：</p>
<pre class="line-numbers  language-python"><code class="  language-python"><span class="token keyword">import</span> s

call_str <span class="token operator">=</span> <span class="token builtin">input</span><span
            class="token punctuation">(</span><span
            class="token string">"input which function you want to call :"</span><span
            class="token punctuation">)</span>

<span class="token keyword">if</span> call_str <span class="token operator">==</span> <span
            class="token string">'fun1'</span><span class="token punctuation">:</span>
    <span class="token keyword">print</span><span class="token punctuation">(</span>s<span
            class="token punctuation">.</span>fun1<span class="token punctuation">(</span><span
            class="token punctuation">)</span><span class="token punctuation">)</span>
<span class="token keyword">elif</span> call_str <span class="token operator">==</span> <span class="token string">'fun2'</span><span
            class="token punctuation">:</span>
    <span class="token keyword">print</span><span class="token punctuation">(</span>s<span
            class="token punctuation">.</span>fun2<span class="token punctuation">(</span><span
            class="token punctuation">)</span><span class="token punctuation">)</span>
<span class="token keyword">elif</span> call_str <span class="token operator">==</span> <span class="token string">'fun3'</span><span
            class="token punctuation">:</span>
    <span class="token keyword">print</span><span class="token punctuation">(</span>s<span
            class="token punctuation">.</span>fun3<span class="token punctuation">(</span><span
            class="token punctuation">)</span><span class="token punctuation">)</span>
<span class="token keyword">else</span><span class="token punctuation">:</span>
    <span class="token keyword">print</span><span class="token punctuation">(</span><span class="token string">"404 not Found"</span><span
            class="token punctuation">)</span>

    
<span class="token keyword">if</span> <span class="token builtin">hasattr</span><span class="token punctuation">(</span>s<span
            class="token punctuation">,</span> call_str<span class="token punctuation">)</span><span
            class="token punctuation">:</span>    <span class="token comment"># 判断是否存在函数 call_str，这样处理就不会报错了。</span>
    obj <span class="token operator">=</span> <span class="token builtin">getattr</span><span class="token punctuation">(</span>s<span
            class="token punctuation">,</span> call_str<span class="token punctuation">)</span>
    <span class="token keyword">print</span><span class="token punctuation">(</span>obj<span
            class="token punctuation">(</span><span class="token punctuation">)</span><span
            class="token punctuation">)</span>
<span class="token keyword">else</span><span class="token punctuation">:</span>
    <span class="token keyword">print</span><span class="token punctuation">(</span><span class="token string">"404 not Found"</span><span
            class="token punctuation">)</span>
<span aria-hidden="true"
      class="line-numbers-rows"><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span></span></code><button
        class="VJbwyy" type="button" aria-label="复制代码"><i aria-label="icon: copy" class="anticon anticon-copy"><svg
        viewBox="64 64 896 896" focusable="false" class="" data-icon="copy" width="1em" height="1em"
        fill="currentColor" aria-hidden="true"><path
        d="M832 64H296c-4.4 0-8 3.6-8 8v56c0 4.4 3.6 8 8 8h496v688c0 4.4 3.6 8 8 8h56c4.4 0 8-3.6 8-8V96c0-17.7-14.3-32-32-32zM704 192H192c-17.7 0-32 14.3-32 32v530.7c0 8.5 3.4 16.6 9.4 22.6l173.3 173.3c2.2 2.2 4.7 4 7.4 5.5v1.9h4.2c3.5 1.3 7.2 2 11 2H704c17.7 0 32-14.3 32-32V224c0-17.7-14.3-32-32-32zM350 856.2L263.9 770H350v86.2zM664 888H414V746c0-22.1-17.9-40-40-40H232V264h432v624z"></path></svg></i></button></pre>
<p>当然<code>setattr</code>和<code>delattr</code>,也分别是设置和删除功能。<br>
    如果你对面对对象比较熟悉的话，你就能很容易的理解到了，这里的四个函数也是可以分别对对象进行操作的。</p>
    

原文链接:https://www.jianshu.com/p/f6d82f6226cf
推荐参考:https://www.jianshu.com/p/1fcea924e71f