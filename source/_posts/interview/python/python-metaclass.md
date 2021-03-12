---
title: "python中什么是元类metaclass？"
date:       2019-12-01
subtitle: "万物皆对象"
tags:
	- Python
	- solution
	- interview
---





<blockquote>
    <p>原文地址：<a
            href="https://link.jianshu.com?t=http://stackoverflow.com/questions/100003/what-is-a-metaclass-in-python/6581949#6581949"
            target="_blank" rel="nofollow">what is metaclass in Python?</a><br>
        此文为原译，如需转载，请联系作者<br>
        我的简书地址：<a href="https://www.jianshu.com/users/69ba0aedbe3c/latest_articles" target="_blank">:nummy</a></p>
</blockquote>
<h3>类即对象</h3>
<p>在理解元类之前，需要先掌握Python中的类，Python中类的概念与SmallTalk中类的概念相似。<br>
    在大多数语言中，类是用来描述如何创建对象的代码段，这在Python中也是成立的：</p>
<pre class="line-numbers  language-python"><code class="python  language-python"><span
        class="token operator">&gt;&gt;</span><span
        class="token operator">&gt;</span> <span class="token keyword">class</span> <span class="token class-name">ObjectCreator</span><span
        class="token punctuation">(</span><span class="token builtin">object</span><span
        class="token punctuation">)</span><span class="token punctuation">:</span>
<span class="token punctuation">.</span><span class="token punctuation">.</span><span class="token punctuation">.</span>       <span
            class="token keyword">pass</span>
<span class="token punctuation">.</span><span class="token punctuation">.</span><span class="token punctuation">.</span> 

<span class="token operator">&gt;&gt;</span><span class="token operator">&gt;</span> my_object <span
            class="token operator">=</span> ObjectCreator<span class="token punctuation">(</span><span
            class="token punctuation">)</span>
<span class="token operator">&gt;&gt;</span><span class="token operator">&gt;</span> <span
            class="token keyword">print</span><span class="token punctuation">(</span>my_object<span
            class="token punctuation">)</span>
<span class="token operator">&lt;</span>__main__<span class="token punctuation">.</span>ObjectCreator <span
            class="token builtin">object</span> at <span class="token number">0x8974f2c</span><span
            class="token operator">&gt;</span>
<span aria-hidden="true"
      class="line-numbers-rows"><span></span><span></span><span></span><span></span><span></span><span></span><span></span></span></code><button
        class="VJbwyy" type="button" aria-label="复制代码"><i aria-label="icon: copy" class="anticon anticon-copy"><svg
        viewBox="64 64 896 896" focusable="false" class="" data-icon="copy" width="1em" height="1em"
        fill="currentColor" aria-hidden="true"><path
        d="M832 64H296c-4.4 0-8 3.6-8 8v56c0 4.4 3.6 8 8 8h496v688c0 4.4 3.6 8 8 8h56c4.4 0 8-3.6 8-8V96c0-17.7-14.3-32-32-32zM704 192H192c-17.7 0-32 14.3-32 32v530.7c0 8.5 3.4 16.6 9.4 22.6l173.3 173.3c2.2 2.2 4.7 4 7.4 5.5v1.9h4.2c3.5 1.3 7.2 2 11 2H704c17.7 0 32-14.3 32-32V224c0-17.7-14.3-32-32-32zM350 856.2L263.9 770H350v86.2zM664 888H414V746c0-22.1-17.9-40-40-40H232V264h432v624z"></path></svg></i></button></pre>
<p>
    Python中，类其实也是对象。当我们使用关键字<strong>class</strong>的时候，Python会执行这段代码，然后生成一个对象。下面的代码在内存中创建一个对象<code>ObjectCreator</code>:
</p>
<pre class="line-numbers  language-python"><code class="python  language-python"><span
        class="token operator">&gt;&gt;</span><span
        class="token operator">&gt;</span> <span class="token keyword">class</span> <span class="token class-name">ObjectCreator</span><span
        class="token punctuation">(</span><span class="token builtin">object</span><span
        class="token punctuation">)</span><span class="token punctuation">:</span>
<span class="token punctuation">.</span><span class="token punctuation">.</span><span class="token punctuation">.</span>       <span
            class="token keyword">pass</span>
<span class="token punctuation">.</span><span class="token punctuation">.</span><span class="token punctuation">.</span> 
<span aria-hidden="true" class="line-numbers-rows"><span></span><span></span><span></span></span></code><button
        class="VJbwyy" type="button" aria-label="复制代码"><i aria-label="icon: copy" class="anticon anticon-copy"><svg
        viewBox="64 64 896 896" focusable="false" class="" data-icon="copy" width="1em" height="1em"
        fill="currentColor" aria-hidden="true"><path
        d="M832 64H296c-4.4 0-8 3.6-8 8v56c0 4.4 3.6 8 8 8h496v688c0 4.4 3.6 8 8 8h56c4.4 0 8-3.6 8-8V96c0-17.7-14.3-32-32-32zM704 192H192c-17.7 0-32 14.3-32 32v530.7c0 8.5 3.4 16.6 9.4 22.6l173.3 173.3c2.2 2.2 4.7 4 7.4 5.5v1.9h4.2c3.5 1.3 7.2 2 11 2H704c17.7 0 32-14.3 32-32V224c0-17.7-14.3-32-32-32zM350 856.2L263.9 770H350v86.2zM664 888H414V746c0-22.1-17.9-40-40-40H232V264h432v624z"></path></svg></i></button></pre>
<p><strong>当一个对象具有创建对象的能力时，就称该对象为类。</strong></p>
<p>所以类本质上还是一个对象，因此它具有以下属性：</p>
<ul>
    <li>可以将它赋值给其它变量</li>
    <li>可以对它进行复制</li>
    <li>可以给它添加属性</li>
    <li>可以将它传递给函数作为参数</li>
</ul>
<p>例如：</p>
<pre class="line-numbers  language-python"><code class="python  language-python"><span
        class="token operator">&gt;&gt;</span><span
        class="token operator">&gt;</span> <span class="token keyword">print</span><span
        class="token punctuation">(</span>ObjectCreator<span class="token punctuation">)</span> <span
        class="token comment"># you can print a class because it's an object</span>
<span class="token operator">&lt;</span><span class="token keyword">class</span> <span class="token string">'__main__.ObjectCreator'</span><span
            class="token operator">&gt;</span>
<span class="token operator">&gt;&gt;</span><span class="token operator">&gt;</span> <span
            class="token keyword">def</span> <span class="token function">echo</span><span
            class="token punctuation">(</span>o<span class="token punctuation">)</span><span
            class="token punctuation">:</span>
<span class="token punctuation">.</span><span class="token punctuation">.</span><span class="token punctuation">.</span>       <span
            class="token keyword">print</span><span class="token punctuation">(</span>o<span
            class="token punctuation">)</span>
<span class="token punctuation">.</span><span class="token punctuation">.</span><span class="token punctuation">.</span> 
<span class="token operator">&gt;&gt;</span><span class="token operator">&gt;</span> echo<span
            class="token punctuation">(</span>ObjectCreator<span class="token punctuation">)</span> <span
            class="token comment"># you can pass a class as a parameter</span>
<span class="token operator">&lt;</span><span class="token keyword">class</span> <span class="token string">'__main__.ObjectCreator'</span><span
            class="token operator">&gt;</span>
<span class="token operator">&gt;&gt;</span><span class="token operator">&gt;</span> <span
            class="token keyword">print</span><span class="token punctuation">(</span><span class="token builtin">hasattr</span><span
            class="token punctuation">(</span>ObjectCreator<span class="token punctuation">,</span> <span
            class="token string">'new_attribute'</span><span class="token punctuation">)</span><span
            class="token punctuation">)</span>
<span class="token boolean">False</span>
<span class="token operator">&gt;&gt;</span><span class="token operator">&gt;</span> ObjectCreator<span
            class="token punctuation">.</span>new_attribute <span class="token operator">=</span> <span
            class="token string">'foo'</span> <span class="token comment"># you can add attributes to a class</span>
<span class="token operator">&gt;&gt;</span><span class="token operator">&gt;</span> <span
            class="token keyword">print</span><span class="token punctuation">(</span><span class="token builtin">hasattr</span><span
            class="token punctuation">(</span>ObjectCreator<span class="token punctuation">,</span> <span
            class="token string">'new_attribute'</span><span class="token punctuation">)</span><span
            class="token punctuation">)</span>
<span class="token boolean">True</span>
<span class="token operator">&gt;&gt;</span><span class="token operator">&gt;</span> <span
            class="token keyword">print</span><span class="token punctuation">(</span>ObjectCreator<span
            class="token punctuation">.</span>new_attribute<span class="token punctuation">)</span>
foo
<span class="token operator">&gt;&gt;</span><span class="token operator">&gt;</span> ObjectCreatorMirror <span
            class="token operator">=</span> ObjectCreator <span class="token comment"># you can assign a class to a variable</span>
<span class="token operator">&gt;&gt;</span><span class="token operator">&gt;</span> <span
            class="token keyword">print</span><span class="token punctuation">(</span>ObjectCreatorMirror<span
            class="token punctuation">.</span>new_attribute<span class="token punctuation">)</span>
foo
<span class="token operator">&gt;&gt;</span><span class="token operator">&gt;</span> <span
            class="token keyword">print</span><span class="token punctuation">(</span>ObjectCreatorMirror<span
            class="token punctuation">(</span><span class="token punctuation">)</span><span
            class="token punctuation">)</span>
<span class="token operator">&lt;</span>__main__<span class="token punctuation">.</span>ObjectCreator <span
            class="token builtin">object</span> at <span class="token number">0x8997b4c</span><span
            class="token operator">&gt;</span>
<span aria-hidden="true"
      class="line-numbers-rows"><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span></span></code><button
        class="VJbwyy" type="button" aria-label="复制代码"><i aria-label="icon: copy" class="anticon anticon-copy"><svg
        viewBox="64 64 896 896" focusable="false" class="" data-icon="copy" width="1em" height="1em"
        fill="currentColor" aria-hidden="true"><path
        d="M832 64H296c-4.4 0-8 3.6-8 8v56c0 4.4 3.6 8 8 8h496v688c0 4.4 3.6 8 8 8h56c4.4 0 8-3.6 8-8V96c0-17.7-14.3-32-32-32zM704 192H192c-17.7 0-32 14.3-32 32v530.7c0 8.5 3.4 16.6 9.4 22.6l173.3 173.3c2.2 2.2 4.7 4 7.4 5.5v1.9h4.2c3.5 1.3 7.2 2 11 2H704c17.7 0 32-14.3 32-32V224c0-17.7-14.3-32-32-32zM350 856.2L263.9 770H350v86.2zM664 888H414V746c0-22.1-17.9-40-40-40H232V264h432v624z"></path></svg></i></button></pre>
<h3>动态创建类</h3>
<p>既然类就是对象，那我们就可以像创建其他对象一样动态创建类。<br>
    首先，在函数中使用class创建一个类：</p>
<pre class="line-numbers  language-python"><code class="python  language-python"><span
        class="token operator">&gt;&gt;</span><span
        class="token operator">&gt;</span> <span class="token keyword">def</span> <span class="token function">choose_class</span><span
        class="token punctuation">(</span>name<span class="token punctuation">)</span><span
        class="token punctuation">:</span>
<span class="token punctuation">.</span><span class="token punctuation">.</span><span class="token punctuation">.</span>     <span
            class="token keyword">if</span> name <span class="token operator">==</span> <span
            class="token string">'foo'</span><span
            class="token punctuation">:</span>
<span class="token punctuation">.</span><span class="token punctuation">.</span><span class="token punctuation">.</span>         <span
            class="token keyword">class</span> <span class="token class-name">Foo</span><span
            class="token punctuation">(</span><span class="token builtin">object</span><span
            class="token punctuation">)</span><span class="token punctuation">:</span>
<span class="token punctuation">.</span><span class="token punctuation">.</span><span class="token punctuation">.</span>             <span
            class="token keyword">pass</span>
<span class="token punctuation">.</span><span class="token punctuation">.</span><span class="token punctuation">.</span>         <span
            class="token keyword">return</span> Foo <span
            class="token comment"># return the class, not an instance</span>
<span class="token punctuation">.</span><span class="token punctuation">.</span><span class="token punctuation">.</span>     <span
            class="token keyword">else</span><span class="token punctuation">:</span>
<span class="token punctuation">.</span><span class="token punctuation">.</span><span class="token punctuation">.</span>         <span
            class="token keyword">class</span> <span class="token class-name">Bar</span><span
            class="token punctuation">(</span><span class="token builtin">object</span><span
            class="token punctuation">)</span><span class="token punctuation">:</span>
<span class="token punctuation">.</span><span class="token punctuation">.</span><span class="token punctuation">.</span>             <span
            class="token keyword">pass</span>
<span class="token punctuation">.</span><span class="token punctuation">.</span><span class="token punctuation">.</span>         <span
            class="token keyword">return</span> Bar
<span class="token punctuation">.</span><span class="token punctuation">.</span><span class="token punctuation">.</span>     
<span class="token operator">&gt;&gt;</span><span class="token operator">&gt;</span> MyClass <span
            class="token operator">=</span> choose_class<span class="token punctuation">(</span><span
            class="token string">'foo'</span><span class="token punctuation">)</span> 
<span class="token operator">&gt;&gt;</span><span class="token operator">&gt;</span> <span
            class="token keyword">print</span><span class="token punctuation">(</span>MyClass<span
            class="token punctuation">)</span> <span class="token comment"># the function returns a class, not an instance</span>
<span class="token operator">&lt;</span><span class="token keyword">class</span> <span class="token string">'__main__.Foo'</span><span
            class="token operator">&gt;</span>
<span class="token operator">&gt;&gt;</span><span class="token operator">&gt;</span> <span
            class="token keyword">print</span><span class="token punctuation">(</span>MyClass<span
            class="token punctuation">(</span><span class="token punctuation">)</span><span
            class="token punctuation">)</span> <span
            class="token comment"># you can create an object from this class</span>
<span class="token operator">&lt;</span>__main__<span class="token punctuation">.</span>Foo <span class="token builtin">object</span> at <span
            class="token number">0x89c6d4c</span><span class="token operator">&gt;</span>
<span aria-hidden="true"
      class="line-numbers-rows"><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span></span></code><button
        class="VJbwyy" type="button" aria-label="复制代码"><i aria-label="icon: copy" class="anticon anticon-copy"><svg
        viewBox="64 64 896 896" focusable="false" class="" data-icon="copy" width="1em" height="1em"
        fill="currentColor" aria-hidden="true"><path
        d="M832 64H296c-4.4 0-8 3.6-8 8v56c0 4.4 3.6 8 8 8h496v688c0 4.4 3.6 8 8 8h56c4.4 0 8-3.6 8-8V96c0-17.7-14.3-32-32-32zM704 192H192c-17.7 0-32 14.3-32 32v530.7c0 8.5 3.4 16.6 9.4 22.6l173.3 173.3c2.2 2.2 4.7 4 7.4 5.5v1.9h4.2c3.5 1.3 7.2 2 11 2H704c17.7 0 32-14.3 32-32V224c0-17.7-14.3-32-32-32zM350 856.2L263.9 770H350v86.2zM664 888H414V746c0-22.1-17.9-40-40-40H232V264h432v624z"></path></svg></i></button></pre>
<p>但是上面的例子也称不上是完全动态的创建类，因为我们还需要在其中编写整个类的代码。<br>
    既然类就是对象，那么它们肯定是通过某个东西来创建的。当使用<strong>class</strong>关键字的时候，Python会自动创建类，Python也提供了方法让我们手动来创建类。</p>
<p>还记得<strong>type()</strong>函数吗？这个函数可以获取对象的类型。</p>
<pre class="line-numbers  language-python"><code class="python  language-python"><span
        class="token operator">&gt;&gt;</span><span
        class="token operator">&gt;</span> <span class="token keyword">print</span><span
        class="token punctuation">(</span><span class="token builtin">type</span><span
        class="token punctuation">(</span><span class="token number">1</span><span
        class="token punctuation">)</span><span class="token punctuation">)</span>
<span class="token operator">&lt;</span><span class="token builtin">type</span> <span
            class="token string">'int'</span><span class="token operator">&gt;</span>
<span class="token operator">&gt;&gt;</span><span class="token operator">&gt;</span> <span
            class="token keyword">print</span><span class="token punctuation">(</span><span
            class="token builtin">type</span><span
            class="token punctuation">(</span><span class="token string">"1"</span><span
            class="token punctuation">)</span><span class="token punctuation">)</span>
<span class="token operator">&lt;</span><span class="token builtin">type</span> <span
            class="token string">'str'</span><span class="token operator">&gt;</span>
<span class="token operator">&gt;&gt;</span><span class="token operator">&gt;</span> <span
            class="token keyword">print</span><span class="token punctuation">(</span><span
            class="token builtin">type</span><span
            class="token punctuation">(</span>ObjectCreator<span class="token punctuation">)</span><span
            class="token punctuation">)</span>
<span class="token operator">&lt;</span><span class="token builtin">type</span> <span class="token string">'type'</span><span
            class="token operator">&gt;</span>
<span class="token operator">&gt;&gt;</span><span class="token operator">&gt;</span> <span
            class="token keyword">print</span><span class="token punctuation">(</span><span
            class="token builtin">type</span><span
            class="token punctuation">(</span>ObjectCreator<span class="token punctuation">(</span><span
            class="token punctuation">)</span><span class="token punctuation">)</span><span
            class="token punctuation">)</span>
<span class="token operator">&lt;</span><span class="token keyword">class</span> <span class="token string">'__main__.ObjectCreator'</span><span
            class="token operator">&gt;</span>
<span aria-hidden="true"
      class="line-numbers-rows"><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span></span></code><button
        class="VJbwyy" type="button" aria-label="复制代码"><i aria-label="icon: copy" class="anticon anticon-copy"><svg
        viewBox="64 64 896 896" focusable="false" class="" data-icon="copy" width="1em" height="1em"
        fill="currentColor" aria-hidden="true"><path
        d="M832 64H296c-4.4 0-8 3.6-8 8v56c0 4.4 3.6 8 8 8h496v688c0 4.4 3.6 8 8 8h56c4.4 0 8-3.6 8-8V96c0-17.7-14.3-32-32-32zM704 192H192c-17.7 0-32 14.3-32 32v530.7c0 8.5 3.4 16.6 9.4 22.6l173.3 173.3c2.2 2.2 4.7 4 7.4 5.5v1.9h4.2c3.5 1.3 7.2 2 11 2H704c17.7 0 32-14.3 32-32V224c0-17.7-14.3-32-32-32zM350 856.2L263.9 770H350v86.2zM664 888H414V746c0-22.1-17.9-40-40-40H232V264h432v624z"></path></svg></i></button></pre>
<p><strong>type</strong>还有另外一个功能，那就是创建类。<strong>type</strong>使用类的相关描述作为参数，然后返回一个类。<br>
    <strong>type</strong>创建类的语法如下：</p>
<pre class="line-numbers  language-bash"><code class="  language-bash">type(类名,基类元组(可以为空，用于继承), 包含属性或函数的字典)
<span aria-hidden="true" class="line-numbers-rows"><span></span></span></code><button class="VJbwyy" type="button"
                                                                                      aria-label="复制代码"><i
        aria-label="icon: copy" class="anticon anticon-copy"><svg viewBox="64 64 896 896" focusable="false" class=""
                                                                  data-icon="copy" width="1em" height="1em"
                                                                  fill="currentColor" aria-hidden="true"><path
        d="M832 64H296c-4.4 0-8 3.6-8 8v56c0 4.4 3.6 8 8 8h496v688c0 4.4 3.6 8 8 8h56c4.4 0 8-3.6 8-8V96c0-17.7-14.3-32-32-32zM704 192H192c-17.7 0-32 14.3-32 32v530.7c0 8.5 3.4 16.6 9.4 22.6l173.3 173.3c2.2 2.2 4.7 4 7.4 5.5v1.9h4.2c3.5 1.3 7.2 2 11 2H704c17.7 0 32-14.3 32-32V224c0-17.7-14.3-32-32-32zM350 856.2L263.9 770H350v86.2zM664 888H414V746c0-22.1-17.9-40-40-40H232V264h432v624z"></path></svg></i></button></pre>
<p>例如：</p>
<pre class="line-numbers  language-python"><code class="python  language-python"><span
        class="token operator">&gt;&gt;</span><span
        class="token operator">&gt;</span> <span class="token keyword">class</span> <span class="token class-name">MyShinyClass</span><span
        class="token punctuation">(</span><span class="token builtin">object</span><span
        class="token punctuation">)</span><span class="token punctuation">:</span>
<span class="token punctuation">.</span><span class="token punctuation">.</span><span class="token punctuation">.</span>       <span
            class="token keyword">pass</span>
<span aria-hidden="true" class="line-numbers-rows"><span></span><span></span></span></code><button class="VJbwyy"
                                                                                                   type="button"
                                                                                                   aria-label="复制代码"><i
        aria-label="icon: copy" class="anticon anticon-copy"><svg viewBox="64 64 896 896" focusable="false" class=""
                                                                  data-icon="copy" width="1em" height="1em"
                                                                  fill="currentColor" aria-hidden="true"><path
        d="M832 64H296c-4.4 0-8 3.6-8 8v56c0 4.4 3.6 8 8 8h496v688c0 4.4 3.6 8 8 8h56c4.4 0 8-3.6 8-8V96c0-17.7-14.3-32-32-32zM704 192H192c-17.7 0-32 14.3-32 32v530.7c0 8.5 3.4 16.6 9.4 22.6l173.3 173.3c2.2 2.2 4.7 4 7.4 5.5v1.9h4.2c3.5 1.3 7.2 2 11 2H704c17.7 0 32-14.3 32-32V224c0-17.7-14.3-32-32-32zM350 856.2L263.9 770H350v86.2zM664 888H414V746c0-22.1-17.9-40-40-40H232V264h432v624z"></path></svg></i></button></pre>
<p>上面的类可以使用下面的方法手动创建：</p>
<pre class="line-numbers  language-python"><code class="python  language-python"><span
        class="token operator">&gt;&gt;</span><span
        class="token operator">&gt;</span> MyShinyClass <span class="token operator">=</span> <span
        class="token builtin">type</span><span class="token punctuation">(</span><span class="token string">'MyShinyClass'</span><span
        class="token punctuation">,</span> <span class="token punctuation">(</span><span
        class="token punctuation">)</span><span class="token punctuation">,</span> <span
        class="token punctuation">{</span><span class="token punctuation">}</span><span
        class="token punctuation">)</span> <span class="token comment"># returns a class object</span>
<span class="token operator">&gt;&gt;</span><span class="token operator">&gt;</span> <span
            class="token keyword">print</span><span class="token punctuation">(</span>MyShinyClass<span
            class="token punctuation">)</span>
<span class="token operator">&lt;</span><span class="token keyword">class</span> <span class="token string">'__main__.MyShinyClass'</span><span
            class="token operator">&gt;</span>
<span class="token operator">&gt;&gt;</span><span class="token operator">&gt;</span> <span
            class="token keyword">print</span><span class="token punctuation">(</span>MyShinyClass<span
            class="token punctuation">(</span><span class="token punctuation">)</span><span
            class="token punctuation">)</span> <span
            class="token comment"># create an instance with the class</span>
<span class="token operator">&lt;</span>__main__<span class="token punctuation">.</span>MyShinyClass <span
            class="token builtin">object</span> at <span class="token number">0x8997cec</span><span
            class="token operator">&gt;</span>
<span aria-hidden="true"
      class="line-numbers-rows"><span></span><span></span><span></span><span></span><span></span></span></code><button
        class="VJbwyy" type="button" aria-label="复制代码"><i aria-label="icon: copy" class="anticon anticon-copy"><svg
        viewBox="64 64 896 896" focusable="false" class="" data-icon="copy" width="1em" height="1em"
        fill="currentColor" aria-hidden="true"><path
        d="M832 64H296c-4.4 0-8 3.6-8 8v56c0 4.4 3.6 8 8 8h496v688c0 4.4 3.6 8 8 8h56c4.4 0 8-3.6 8-8V96c0-17.7-14.3-32-32-32zM704 192H192c-17.7 0-32 14.3-32 32v530.7c0 8.5 3.4 16.6 9.4 22.6l173.3 173.3c2.2 2.2 4.7 4 7.4 5.5v1.9h4.2c3.5 1.3 7.2 2 11 2H704c17.7 0 32-14.3 32-32V224c0-17.7-14.3-32-32-32zM350 856.2L263.9 770H350v86.2zM664 888H414V746c0-22.1-17.9-40-40-40H232V264h432v624z"></path></svg></i></button></pre>
<p><strong>type</strong>也接收一个字典参数来定义类中的属性：</p>
<pre class="line-numbers  language-python"><code class="python  language-python"><span
        class="token operator">&gt;&gt;</span><span
        class="token operator">&gt;</span> <span class="token keyword">class</span> <span
        class="token class-name">Foo</span><span
        class="token punctuation">(</span><span class="token builtin">object</span><span
        class="token punctuation">)</span><span class="token punctuation">:</span>
<span class="token punctuation">.</span><span class="token punctuation">.</span><span class="token punctuation">.</span>       bar <span
            class="token operator">=</span> <span class="token boolean">True</span>
<span aria-hidden="true" class="line-numbers-rows"><span></span><span></span></span></code><button class="VJbwyy"
                                                                                                   type="button"
                                                                                                   aria-label="复制代码"><i
        aria-label="icon: copy" class="anticon anticon-copy"><svg viewBox="64 64 896 896" focusable="false" class=""
                                                                  data-icon="copy" width="1em" height="1em"
                                                                  fill="currentColor" aria-hidden="true"><path
        d="M832 64H296c-4.4 0-8 3.6-8 8v56c0 4.4 3.6 8 8 8h496v688c0 4.4 3.6 8 8 8h56c4.4 0 8-3.6 8-8V96c0-17.7-14.3-32-32-32zM704 192H192c-17.7 0-32 14.3-32 32v530.7c0 8.5 3.4 16.6 9.4 22.6l173.3 173.3c2.2 2.2 4.7 4 7.4 5.5v1.9h4.2c3.5 1.3 7.2 2 11 2H704c17.7 0 32-14.3 32-32V224c0-17.7-14.3-32-32-32zM350 856.2L263.9 770H350v86.2zM664 888H414V746c0-22.1-17.9-40-40-40H232V264h432v624z"></path></svg></i></button></pre>
<p>等价于</p>
<pre class="line-numbers  language-python"><code class="python  language-python"><span
        class="token operator">&gt;&gt;</span><span
        class="token operator">&gt;</span> Foo <span class="token operator">=</span> <span
        class="token builtin">type</span><span
        class="token punctuation">(</span><span class="token string">'Foo'</span><span
        class="token punctuation">,</span> <span class="token punctuation">(</span><span
        class="token punctuation">)</span><span class="token punctuation">,</span> <span
        class="token punctuation">{</span><span class="token string">'bar'</span><span
        class="token punctuation">:</span><span class="token boolean">True</span><span
        class="token punctuation">}</span><span class="token punctuation">)</span>
<span aria-hidden="true" class="line-numbers-rows"><span></span></span></code><button class="VJbwyy" type="button"
                                                                                      aria-label="复制代码"><i
        aria-label="icon: copy" class="anticon anticon-copy"><svg viewBox="64 64 896 896" focusable="false" class=""
                                                                  data-icon="copy" width="1em" height="1em"
                                                                  fill="currentColor" aria-hidden="true"><path
        d="M832 64H296c-4.4 0-8 3.6-8 8v56c0 4.4 3.6 8 8 8h496v688c0 4.4 3.6 8 8 8h56c4.4 0 8-3.6 8-8V96c0-17.7-14.3-32-32-32zM704 192H192c-17.7 0-32 14.3-32 32v530.7c0 8.5 3.4 16.6 9.4 22.6l173.3 173.3c2.2 2.2 4.7 4 7.4 5.5v1.9h4.2c3.5 1.3 7.2 2 11 2H704c17.7 0 32-14.3 32-32V224c0-17.7-14.3-32-32-32zM350 856.2L263.9 770H350v86.2zM664 888H414V746c0-22.1-17.9-40-40-40H232V264h432v624z"></path></svg></i></button></pre>
<p>通过<code>type</code>创建的类使用方式跟普通类一样：</p>
<pre class="line-numbers  language-python"><code class="python  language-python"><span
        class="token operator">&gt;&gt;</span><span
        class="token operator">&gt;</span> <span class="token keyword">print</span><span
        class="token punctuation">(</span>Foo<span class="token punctuation">)</span>
<span class="token operator">&lt;</span><span class="token keyword">class</span> <span class="token string">'__main__.Foo'</span><span
            class="token operator">&gt;</span>
<span class="token operator">&gt;&gt;</span><span class="token operator">&gt;</span> <span
            class="token keyword">print</span><span class="token punctuation">(</span>Foo<span
            class="token punctuation">.</span>bar<span class="token punctuation">)</span>
<span class="token boolean">True</span>
<span class="token operator">&gt;&gt;</span><span class="token operator">&gt;</span> f <span
            class="token operator">=</span> Foo<span class="token punctuation">(</span><span
            class="token punctuation">)</span>
<span class="token operator">&gt;&gt;</span><span class="token operator">&gt;</span> <span
            class="token keyword">print</span><span class="token punctuation">(</span>f<span
            class="token punctuation">)</span>
<span class="token operator">&lt;</span>__main__<span class="token punctuation">.</span>Foo <span class="token builtin">object</span> at <span
            class="token number">0x8a9b84c</span><span class="token operator">&gt;</span>
<span class="token operator">&gt;&gt;</span><span class="token operator">&gt;</span> <span
            class="token keyword">print</span><span class="token punctuation">(</span>f<span
            class="token punctuation">.</span>bar<span class="token punctuation">)</span>
<span class="token boolean">True</span>
<span aria-hidden="true"
      class="line-numbers-rows"><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span></span></code><button
        class="VJbwyy" type="button" aria-label="复制代码"><i aria-label="icon: copy" class="anticon anticon-copy"><svg
        viewBox="64 64 896 896" focusable="false" class="" data-icon="copy" width="1em" height="1em"
        fill="currentColor" aria-hidden="true"><path
        d="M832 64H296c-4.4 0-8 3.6-8 8v56c0 4.4 3.6 8 8 8h496v688c0 4.4 3.6 8 8 8h56c4.4 0 8-3.6 8-8V96c0-17.7-14.3-32-32-32zM704 192H192c-17.7 0-32 14.3-32 32v530.7c0 8.5 3.4 16.6 9.4 22.6l173.3 173.3c2.2 2.2 4.7 4 7.4 5.5v1.9h4.2c3.5 1.3 7.2 2 11 2H704c17.7 0 32-14.3 32-32V224c0-17.7-14.3-32-32-32zM350 856.2L263.9 770H350v86.2zM664 888H414V746c0-22.1-17.9-40-40-40H232V264h432v624z"></path></svg></i></button></pre>
<p>当然也可以继承：</p>
<pre class="line-numbers  language-python"><code class="python  language-python"><span
        class="token operator">&gt;&gt;</span><span
        class="token operator">&gt;</span>   <span class="token keyword">class</span> <span
        class="token class-name">FooChild</span><span class="token punctuation">(</span>Foo<span
        class="token punctuation">)</span><span class="token punctuation">:</span>
<span class="token punctuation">.</span><span class="token punctuation">.</span><span class="token punctuation">.</span>         <span
            class="token keyword">pass</span>
<span aria-hidden="true" class="line-numbers-rows"><span></span><span></span></span></code><button class="VJbwyy"
                                                                                                   type="button"
                                                                                                   aria-label="复制代码"><i
        aria-label="icon: copy" class="anticon anticon-copy"><svg viewBox="64 64 896 896" focusable="false" class=""
                                                                  data-icon="copy" width="1em" height="1em"
                                                                  fill="currentColor" aria-hidden="true"><path
        d="M832 64H296c-4.4 0-8 3.6-8 8v56c0 4.4 3.6 8 8 8h496v688c0 4.4 3.6 8 8 8h56c4.4 0 8-3.6 8-8V96c0-17.7-14.3-32-32-32zM704 192H192c-17.7 0-32 14.3-32 32v530.7c0 8.5 3.4 16.6 9.4 22.6l173.3 173.3c2.2 2.2 4.7 4 7.4 5.5v1.9h4.2c3.5 1.3 7.2 2 11 2H704c17.7 0 32-14.3 32-32V224c0-17.7-14.3-32-32-32zM350 856.2L263.9 770H350v86.2zM664 888H414V746c0-22.1-17.9-40-40-40H232V264h432v624z"></path></svg></i></button></pre>
<p>等价于：</p>
<pre class="line-numbers  language-python"><code class="python  language-python"><span
        class="token operator">&gt;&gt;</span><span
        class="token operator">&gt;</span> FooChild <span class="token operator">=</span> <span
        class="token builtin">type</span><span class="token punctuation">(</span><span
        class="token string">'FooChild'</span><span
        class="token punctuation">,</span> <span class="token punctuation">(</span>Foo<span
        class="token punctuation">,</span><span class="token punctuation">)</span><span
        class="token punctuation">,</span> <span class="token punctuation">{</span><span
        class="token punctuation">}</span><span class="token punctuation">)</span>
<span class="token operator">&gt;&gt;</span><span class="token operator">&gt;</span> <span
            class="token keyword">print</span><span class="token punctuation">(</span>FooChild<span
            class="token punctuation">)</span>
<span class="token operator">&lt;</span><span class="token keyword">class</span> <span class="token string">'__main__.FooChild'</span><span
            class="token operator">&gt;</span>
<span class="token operator">&gt;&gt;</span><span class="token operator">&gt;</span> <span
            class="token keyword">print</span><span class="token punctuation">(</span>FooChild<span
            class="token punctuation">.</span>bar<span class="token punctuation">)</span> <span
            class="token comment"># bar is inherited from Foo</span>
<span class="token boolean">True</span>
<span aria-hidden="true"
      class="line-numbers-rows"><span></span><span></span><span></span><span></span><span></span></span></code><button
        class="VJbwyy" type="button" aria-label="复制代码"><i aria-label="icon: copy" class="anticon anticon-copy"><svg
        viewBox="64 64 896 896" focusable="false" class="" data-icon="copy" width="1em" height="1em"
        fill="currentColor" aria-hidden="true"><path
        d="M832 64H296c-4.4 0-8 3.6-8 8v56c0 4.4 3.6 8 8 8h496v688c0 4.4 3.6 8 8 8h56c4.4 0 8-3.6 8-8V96c0-17.7-14.3-32-32-32zM704 192H192c-17.7 0-32 14.3-32 32v530.7c0 8.5 3.4 16.6 9.4 22.6l173.3 173.3c2.2 2.2 4.7 4 7.4 5.5v1.9h4.2c3.5 1.3 7.2 2 11 2H704c17.7 0 32-14.3 32-32V224c0-17.7-14.3-32-32-32zM350 856.2L263.9 770H350v86.2zM664 888H414V746c0-22.1-17.9-40-40-40H232V264h432v624z"></path></svg></i></button></pre>
<p>最后，我们可能还想给类添加方法，可以先定义一个函数，然后将它以属性的方式赋予给类。</p>
<pre class="line-numbers  language-python"><code class="python  language-python"><span
        class="token operator">&gt;&gt;</span><span
        class="token operator">&gt;</span> <span class="token keyword">def</span> <span
        class="token function">echo_bar</span><span
        class="token punctuation">(</span>self<span class="token punctuation">)</span><span
        class="token punctuation">:</span>
<span class="token punctuation">.</span><span class="token punctuation">.</span><span class="token punctuation">.</span>       <span
            class="token keyword">print</span><span class="token punctuation">(</span>self<span
            class="token punctuation">.</span>bar<span class="token punctuation">)</span>
<span class="token punctuation">.</span><span class="token punctuation">.</span><span class="token punctuation">.</span> 
<span class="token operator">&gt;&gt;</span><span class="token operator">&gt;</span> FooChild <span
            class="token operator">=</span> <span class="token builtin">type</span><span
            class="token punctuation">(</span><span class="token string">'FooChild'</span><span
            class="token punctuation">,</span> <span class="token punctuation">(</span>Foo<span
            class="token punctuation">,</span><span class="token punctuation">)</span><span
            class="token punctuation">,</span> <span class="token punctuation">{</span><span class="token string">'echo_bar'</span><span
            class="token punctuation">:</span> echo_bar<span class="token punctuation">}</span><span
            class="token punctuation">)</span>
<span class="token operator">&gt;&gt;</span><span class="token operator">&gt;</span> <span
            class="token builtin">hasattr</span><span class="token punctuation">(</span>Foo<span
            class="token punctuation">,</span> <span class="token string">'echo_bar'</span><span
            class="token punctuation">)</span>
<span class="token boolean">False</span>
<span class="token operator">&gt;&gt;</span><span class="token operator">&gt;</span> <span
            class="token builtin">hasattr</span><span class="token punctuation">(</span>FooChild<span
            class="token punctuation">,</span> <span class="token string">'echo_bar'</span><span
            class="token punctuation">)</span>
<span class="token boolean">True</span>
<span class="token operator">&gt;&gt;</span><span class="token operator">&gt;</span> my_foo <span
            class="token operator">=</span> FooChild<span class="token punctuation">(</span><span
            class="token punctuation">)</span>
<span class="token operator">&gt;&gt;</span><span class="token operator">&gt;</span> my_foo<span
            class="token punctuation">.</span>echo_bar<span class="token punctuation">(</span><span
            class="token punctuation">)</span>
<span class="token boolean">True</span>
<span aria-hidden="true"
      class="line-numbers-rows"><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span></span></code><button
        class="VJbwyy" type="button" aria-label="复制代码"><i aria-label="icon: copy" class="anticon anticon-copy"><svg
        viewBox="64 64 896 896" focusable="false" class="" data-icon="copy" width="1em" height="1em"
        fill="currentColor" aria-hidden="true"><path
        d="M832 64H296c-4.4 0-8 3.6-8 8v56c0 4.4 3.6 8 8 8h496v688c0 4.4 3.6 8 8 8h56c4.4 0 8-3.6 8-8V96c0-17.7-14.3-32-32-32zM704 192H192c-17.7 0-32 14.3-32 32v530.7c0 8.5 3.4 16.6 9.4 22.6l173.3 173.3c2.2 2.2 4.7 4 7.4 5.5v1.9h4.2c3.5 1.3 7.2 2 11 2H704c17.7 0 32-14.3 32-32V224c0-17.7-14.3-32-32-32zM350 856.2L263.9 770H350v86.2zM664 888H414V746c0-22.1-17.9-40-40-40H232V264h432v624z"></path></svg></i></button></pre>
<p>而且，我们还可以在动态创建类之后，给类添加更多的方法和属性：</p>
<pre class="line-numbers  language-python"><code class="python  language-python"><span
        class="token operator">&gt;&gt;</span><span
        class="token operator">&gt;</span> <span class="token keyword">def</span> <span class="token function">echo_bar_more</span><span
        class="token punctuation">(</span>self<span class="token punctuation">)</span><span
        class="token punctuation">:</span>
<span class="token punctuation">.</span><span class="token punctuation">.</span><span class="token punctuation">.</span>       <span
            class="token keyword">print</span><span class="token punctuation">(</span><span class="token string">'yet another method'</span><span
            class="token punctuation">)</span>
<span class="token punctuation">.</span><span class="token punctuation">.</span><span class="token punctuation">.</span> 
<span class="token operator">&gt;&gt;</span><span class="token operator">&gt;</span> FooChild<span
            class="token punctuation">.</span>echo_bar_more <span class="token operator">=</span> echo_bar_more
<span class="token operator">&gt;&gt;</span><span class="token operator">&gt;</span> <span
            class="token builtin">hasattr</span><span class="token punctuation">(</span>FooChild<span
            class="token punctuation">,</span> <span class="token string">'echo_bar_more'</span><span
            class="token punctuation">)</span>
<span class="token boolean">True</span>
<span aria-hidden="true"
      class="line-numbers-rows"><span></span><span></span><span></span><span></span><span></span><span></span></span></code><button
        class="VJbwyy" type="button" aria-label="复制代码"><i aria-label="icon: copy" class="anticon anticon-copy"><svg
        viewBox="64 64 896 896" focusable="false" class="" data-icon="copy" width="1em" height="1em"
        fill="currentColor" aria-hidden="true"><path
        d="M832 64H296c-4.4 0-8 3.6-8 8v56c0 4.4 3.6 8 8 8h496v688c0 4.4 3.6 8 8 8h56c4.4 0 8-3.6 8-8V96c0-17.7-14.3-32-32-32zM704 192H192c-17.7 0-32 14.3-32 32v530.7c0 8.5 3.4 16.6 9.4 22.6l173.3 173.3c2.2 2.2 4.7 4 7.4 5.5v1.9h4.2c3.5 1.3 7.2 2 11 2H704c17.7 0 32-14.3 32-32V224c0-17.7-14.3-32-32-32zM350 856.2L263.9 770H350v86.2zM664 888H414V746c0-22.1-17.9-40-40-40H232V264h432v624z"></path></svg></i></button></pre>
<h3>什么是元类？</h3>
<p>通常，我们定义类来创建对象，但是现在我们知道类也是对象。那么是通过什么来创建类呢？答案就是元类。你可以想象关系如下：</p>
<pre class="line-numbers  language-python"><code class="python  language-python">MyClass <span
        class="token operator">=</span> MetaClass<span class="token punctuation">(</span><span
        class="token punctuation">)</span>
MyObject <span class="token operator">=</span> MyClass<span class="token punctuation">(</span><span
            class="token punctuation">)</span>
<span aria-hidden="true" class="line-numbers-rows"><span></span><span></span></span></code><button class="VJbwyy"
                                                                                                   type="button"
                                                                                                   aria-label="复制代码"><i
        aria-label="icon: copy" class="anticon anticon-copy"><svg viewBox="64 64 896 896" focusable="false" class=""
                                                                  data-icon="copy" width="1em" height="1em"
                                                                  fill="currentColor" aria-hidden="true"><path
        d="M832 64H296c-4.4 0-8 3.6-8 8v56c0 4.4 3.6 8 8 8h496v688c0 4.4 3.6 8 8 8h56c4.4 0 8-3.6 8-8V96c0-17.7-14.3-32-32-32zM704 192H192c-17.7 0-32 14.3-32 32v530.7c0 8.5 3.4 16.6 9.4 22.6l173.3 173.3c2.2 2.2 4.7 4 7.4 5.5v1.9h4.2c3.5 1.3 7.2 2 11 2H704c17.7 0 32-14.3 32-32V224c0-17.7-14.3-32-32-32zM350 856.2L263.9 770H350v86.2zM664 888H414V746c0-22.1-17.9-40-40-40H232V264h432v624z"></path></svg></i></button></pre>
<p>你已经知道使用<code>type</code>可以创建类：</p>
<pre class="line-numbers  language-python"><code class="python  language-python">MyClass <span
        class="token operator">=</span> <span class="token builtin">type</span><span
        class="token punctuation">(</span><span class="token string">'MyClass'</span><span
        class="token punctuation">,</span> <span class="token punctuation">(</span><span
        class="token punctuation">)</span><span class="token punctuation">,</span> <span
        class="token punctuation">{</span><span class="token punctuation">}</span><span
        class="token punctuation">)</span>
<span aria-hidden="true" class="line-numbers-rows"><span></span></span></code><button class="VJbwyy" type="button"
                                                                                      aria-label="复制代码"><i
        aria-label="icon: copy" class="anticon anticon-copy"><svg viewBox="64 64 896 896" focusable="false" class=""
                                                                  data-icon="copy" width="1em" height="1em"
                                                                  fill="currentColor" aria-hidden="true"><path
        d="M832 64H296c-4.4 0-8 3.6-8 8v56c0 4.4 3.6 8 8 8h496v688c0 4.4 3.6 8 8 8h56c4.4 0 8-3.6 8-8V96c0-17.7-14.3-32-32-32zM704 192H192c-17.7 0-32 14.3-32 32v530.7c0 8.5 3.4 16.6 9.4 22.6l173.3 173.3c2.2 2.2 4.7 4 7.4 5.5v1.9h4.2c3.5 1.3 7.2 2 11 2H704c17.7 0 32-14.3 32-32V224c0-17.7-14.3-32-32-32zM350 856.2L263.9 770H350v86.2zM664 888H414V746c0-22.1-17.9-40-40-40H232V264h432v624z"></path></svg></i></button></pre>
<p>那是因为<strong>type</strong>函数实际上就是一个元类，Python使用<strong>type</strong>作为元类来创建所有的类。<br>
    通过检查<strong><strong>class</strong></strong>属性，我们可以知道，其实Python中任何数据类型都是对象，包括整型、字符串、函数以及类，它们都是对象。它们都是从类中创建的。</p>
<pre class="line-numbers  language-python"><code class="python  language-python"><span
        class="token operator">&gt;&gt;</span><span
        class="token operator">&gt;</span> age <span class="token operator">=</span> <span
        class="token number">35</span>
<span class="token operator">&gt;&gt;</span><span class="token operator">&gt;</span> age<span class="token punctuation">.</span>__class__
<span class="token operator">&lt;</span><span class="token builtin">type</span> <span
            class="token string">'int'</span><span class="token operator">&gt;</span>
<span class="token operator">&gt;&gt;</span><span class="token operator">&gt;</span> name <span
            class="token operator">=</span> <span class="token string">'bob'</span>
<span class="token operator">&gt;&gt;</span><span class="token operator">&gt;</span> name<span
            class="token punctuation">.</span>__class__
<span class="token operator">&lt;</span><span class="token builtin">type</span> <span
            class="token string">'str'</span><span class="token operator">&gt;</span>
<span class="token operator">&gt;&gt;</span><span class="token operator">&gt;</span> <span
            class="token keyword">def</span> <span class="token function">foo</span><span
            class="token punctuation">(</span><span
            class="token punctuation">)</span><span class="token punctuation">:</span> <span
            class="token keyword">pass</span>
<span class="token operator">&gt;&gt;</span><span class="token operator">&gt;</span> foo<span class="token punctuation">.</span>__class__
<span class="token operator">&lt;</span><span class="token builtin">type</span> <span
            class="token string">'function'</span><span class="token operator">&gt;</span>
<span class="token operator">&gt;&gt;</span><span class="token operator">&gt;</span> <span
            class="token keyword">class</span> <span class="token class-name">Bar</span><span
            class="token punctuation">(</span><span class="token builtin">object</span><span
            class="token punctuation">)</span><span class="token punctuation">:</span> <span
            class="token keyword">pass</span>
<span class="token operator">&gt;&gt;</span><span class="token operator">&gt;</span> b <span
            class="token operator">=</span> Bar<span class="token punctuation">(</span><span
            class="token punctuation">)</span>
<span class="token operator">&gt;&gt;</span><span class="token operator">&gt;</span> b<span
            class="token punctuation">.</span>__class__
<span class="token operator">&lt;</span><span class="token keyword">class</span> <span class="token string">'__main__.Bar'</span><span
            class="token operator">&gt;</span>
<span aria-hidden="true"
      class="line-numbers-rows"><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span></span></code><button
        class="VJbwyy" type="button" aria-label="复制代码"><i aria-label="icon: copy" class="anticon anticon-copy"><svg
        viewBox="64 64 896 896" focusable="false" class="" data-icon="copy" width="1em" height="1em"
        fill="currentColor" aria-hidden="true"><path
        d="M832 64H296c-4.4 0-8 3.6-8 8v56c0 4.4 3.6 8 8 8h496v688c0 4.4 3.6 8 8 8h56c4.4 0 8-3.6 8-8V96c0-17.7-14.3-32-32-32zM704 192H192c-17.7 0-32 14.3-32 32v530.7c0 8.5 3.4 16.6 9.4 22.6l173.3 173.3c2.2 2.2 4.7 4 7.4 5.5v1.9h4.2c3.5 1.3 7.2 2 11 2H704c17.7 0 32-14.3 32-32V224c0-17.7-14.3-32-32-32zM350 856.2L263.9 770H350v86.2zM664 888H414V746c0-22.1-17.9-40-40-40H232V264h432v624z"></path></svg></i></button></pre>
<p>那么<code>__class__</code>的<code>__class__</code>是什么呢？</p>
<pre class="line-numbers  language-python"><code class="python  language-python"><span
        class="token operator">&gt;&gt;</span><span
        class="token operator">&gt;</span> age<span class="token punctuation">.</span>__class__<span
        class="token punctuation">.</span>__class__
<span class="token operator">&lt;</span><span class="token builtin">type</span> <span class="token string">'type'</span><span
            class="token operator">&gt;</span>
<span class="token operator">&gt;&gt;</span><span class="token operator">&gt;</span> name<span
            class="token punctuation">.</span>__class__<span class="token punctuation">.</span>__class__
<span class="token operator">&lt;</span><span class="token builtin">type</span> <span class="token string">'type'</span><span
            class="token operator">&gt;</span>
<span class="token operator">&gt;&gt;</span><span class="token operator">&gt;</span> foo<span class="token punctuation">.</span>__class__<span
            class="token punctuation">.</span>__class__
<span class="token operator">&lt;</span><span class="token builtin">type</span> <span class="token string">'type'</span><span
            class="token operator">&gt;</span>
<span class="token operator">&gt;&gt;</span><span class="token operator">&gt;</span> b<span
            class="token punctuation">.</span>__class__<span class="token punctuation">.</span>__class__
<span class="token operator">&lt;</span><span class="token builtin">type</span> <span class="token string">'type'</span><span
            class="token operator">&gt;</span>
<span aria-hidden="true"
      class="line-numbers-rows"><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span></span></code><button
        class="VJbwyy" type="button" aria-label="复制代码"><i aria-label="icon: copy" class="anticon anticon-copy"><svg
        viewBox="64 64 896 896" focusable="false" class="" data-icon="copy" width="1em" height="1em"
        fill="currentColor" aria-hidden="true"><path
        d="M832 64H296c-4.4 0-8 3.6-8 8v56c0 4.4 3.6 8 8 8h496v688c0 4.4 3.6 8 8 8h56c4.4 0 8-3.6 8-8V96c0-17.7-14.3-32-32-32zM704 192H192c-17.7 0-32 14.3-32 32v530.7c0 8.5 3.4 16.6 9.4 22.6l173.3 173.3c2.2 2.2 4.7 4 7.4 5.5v1.9h4.2c3.5 1.3 7.2 2 11 2H704c17.7 0 32-14.3 32-32V224c0-17.7-14.3-32-32-32zM350 856.2L263.9 770H350v86.2zM664 888H414V746c0-22.1-17.9-40-40-40H232V264h432v624z"></path></svg></i></button></pre>
<p>所以类其实就是通过元类来创建的，你可以将元类称之为类工厂。<br>
    <strong>type</strong>是内置的元类，Python默认使用它来创建类。当然，我们也可以定义属于我们自己的元类。</p>
<h3>
    <strong><strong>metaclass</strong></strong>属性</h3>
<p>当我们创建类的时候，可以给它添加<strong><strong>metaclass</strong></strong>属性:</p>
<pre class="line-numbers  language-kotlin"><code class="  language-kotlin"><span
        class="token keyword">class</span> <span
        class="token function">Foo</span><span class="token punctuation">(</span><span
        class="token keyword">object</span><span class="token punctuation">)</span><span
        class="token operator">:</span>
  __metaclass__ <span class="token operator">=</span> something<span class="token operator">..</span><span
            class="token punctuation">.</span>
  <span class="token punctuation">[</span><span class="token operator">..</span><span class="token punctuation">.</span><span
            class="token punctuation">]</span>
<span aria-hidden="true" class="line-numbers-rows"><span></span><span></span><span></span></span></code><button
        class="VJbwyy" type="button" aria-label="复制代码"><i aria-label="icon: copy" class="anticon anticon-copy"><svg
        viewBox="64 64 896 896" focusable="false" class="" data-icon="copy" width="1em" height="1em"
        fill="currentColor" aria-hidden="true"><path
        d="M832 64H296c-4.4 0-8 3.6-8 8v56c0 4.4 3.6 8 8 8h496v688c0 4.4 3.6 8 8 8h56c4.4 0 8-3.6 8-8V96c0-17.7-14.3-32-32-32zM704 192H192c-17.7 0-32 14.3-32 32v530.7c0 8.5 3.4 16.6 9.4 22.6l173.3 173.3c2.2 2.2 4.7 4 7.4 5.5v1.9h4.2c3.5 1.3 7.2 2 11 2H704c17.7 0 32-14.3 32-32V224c0-17.7-14.3-32-32-32zM350 856.2L263.9 770H350v86.2zM664 888H414V746c0-22.1-17.9-40-40-40H232V264h432v624z"></path></svg></i></button></pre>
<p>如果我们定义了<strong><strong>metaclass</strong></strong>属性，Python就会使用这个元类来创建类Foo。<br>
    注意，编译器首先读取<code>class Foo(object)</code>，这时并不会在内存中创建Foo类。Python会继续查找类定义中的<code>__meatclass__</code>，如果找到了，就使用它来创建类Foo，如果没有找到，就使用<strong>type</strong>来创建类。<br>
    所以对于以下代码：</p>
<pre class="line-numbers  language-python"><code class="python  language-python"><span
        class="token keyword">class</span> <span class="token class-name">Foo</span><span
        class="token punctuation">(</span>Bar<span
        class="token punctuation">)</span><span class="token punctuation">:</span>
  <span class="token keyword">pass</span>
<span aria-hidden="true" class="line-numbers-rows"><span></span><span></span></span></code><button class="VJbwyy"
                                                                                                   type="button"
                                                                                                   aria-label="复制代码"><i
        aria-label="icon: copy" class="anticon anticon-copy"><svg viewBox="64 64 896 896" focusable="false" class=""
                                                                  data-icon="copy" width="1em" height="1em"
                                                                  fill="currentColor" aria-hidden="true"><path
        d="M832 64H296c-4.4 0-8 3.6-8 8v56c0 4.4 3.6 8 8 8h496v688c0 4.4 3.6 8 8 8h56c4.4 0 8-3.6 8-8V96c0-17.7-14.3-32-32-32zM704 192H192c-17.7 0-32 14.3-32 32v530.7c0 8.5 3.4 16.6 9.4 22.6l173.3 173.3c2.2 2.2 4.7 4 7.4 5.5v1.9h4.2c3.5 1.3 7.2 2 11 2H704c17.7 0 32-14.3 32-32V224c0-17.7-14.3-32-32-32zM350 856.2L263.9 770H350v86.2zM664 888H414V746c0-22.1-17.9-40-40-40H232V264h432v624z"></path></svg></i></button></pre>
<p>Python工作流程如下：</p>
<ul>
    <li>首先检查<code>Foo</code>中是否具有属性<code>__metaclass__</code>？</li>
</ul>
<ul>
    <li>如果找到，就使用<code>__metaclass__</code>定义的元类在内存中创建一个类对象。</li>
</ul>
<ul>
    <li>如果在类定义中没有找到这个属性，就在模块级别中进行查找。</li>
</ul>
<ul>
    <li>如果还是没有找到，就会使用父类Bar中的元类来创建类。</li>
</ul>
<p>注意：类中的<code>__metaclass__</code>属性不会被子类继承，但是父类中的<code>__class__</code>会被继承。</p>
<h3>自定义元类</h3>
<p>元类的主要作用是在创建类的时候自动改变类。<br>
    例如，想要实现模块中所有的类属性都是大写格式。可以定义模块级别的<code>__metaclass__</code>来实现。<br>
    这样模块中所有的类都是通过这个元类来创建的。</p>
<pre class="line-numbers  language-python"><code class="python  language-python"><span
        class="token keyword">def</span> <span class="token function">upper_attr</span><span
        class="token punctuation">(</span>future_class_name<span class="token punctuation">,</span> future_class_parents<span
        class="token punctuation">,</span> future_class_attr<span class="token punctuation">)</span><span
        class="token punctuation">:</span>
  <span class="token triple-quoted-string string">"""
    返回一个类，该类的所有属性名的都为大写
  """</span>
  <span class="token comment"># 将不是__开头的属性名转为大写字母</span>
  uppercase_attr <span class="token operator">=</span> <span class="token punctuation">{</span><span
            class="token punctuation">}</span>
  <span class="token keyword">for</span> name<span class="token punctuation">,</span> val <span
            class="token keyword">in</span> future_class_attr<span class="token punctuation">.</span>items<span
            class="token punctuation">(</span><span class="token punctuation">)</span><span
            class="token punctuation">:</span>
      <span class="token keyword">if</span> <span class="token keyword">not</span> name<span
            class="token punctuation">.</span>startswith<span class="token punctuation">(</span><span
            class="token string">'__'</span><span class="token punctuation">)</span><span
            class="token punctuation">:</span>
          uppercase_attr<span class="token punctuation">[</span>name<span class="token punctuation">.</span>upper<span
            class="token punctuation">(</span><span class="token punctuation">)</span><span
            class="token punctuation">]</span> <span class="token operator">=</span> val
      <span class="token keyword">else</span><span class="token punctuation">:</span>
          uppercase_attr<span class="token punctuation">[</span>name<span class="token punctuation">]</span> <span
            class="token operator">=</span> val
  <span class="token comment"># 使用type创建类</span>
  <span class="token keyword">return</span> <span class="token builtin">type</span><span
            class="token punctuation">(</span>future_class_name<span class="token punctuation">,</span> future_class_parents<span
            class="token punctuation">,</span> uppercase_attr<span class="token punctuation">)</span>

__metaclass__ <span class="token operator">=</span> upper_attr <span
            class="token comment"># 定义模块级别的元类，这样模块中所有类都会使用该元类创建</span>

<span class="token keyword">class</span> <span class="token class-name">Foo</span><span
            class="token punctuation">(</span><span class="token punctuation">)</span><span
            class="token punctuation">:</span> 
  <span class="token comment"># 注意，新式类不支持模块级别的元类，但是可以在类中定义__metaclass__</span>
  bar <span class="token operator">=</span> <span class="token string">'bip'</span>

<span class="token keyword">print</span><span class="token punctuation">(</span><span
            class="token builtin">hasattr</span><span class="token punctuation">(</span>Foo<span
            class="token punctuation">,</span> <span class="token string">'bar'</span><span
            class="token punctuation">)</span><span class="token punctuation">)</span>
<span class="token comment"># 输出: False</span>
<span class="token keyword">print</span><span class="token punctuation">(</span><span
            class="token builtin">hasattr</span><span class="token punctuation">(</span>Foo<span
            class="token punctuation">,</span> <span class="token string">'BAR'</span><span
            class="token punctuation">)</span><span class="token punctuation">)</span>
<span class="token comment"># 输出: True</span>

f <span class="token operator">=</span> Foo<span class="token punctuation">(</span><span
            class="token punctuation">)</span>
<span class="token keyword">print</span><span class="token punctuation">(</span>f<span
            class="token punctuation">.</span>BAR<span class="token punctuation">)</span>
<span class="token comment"># Out: 'bip'</span>
<span aria-hidden="true"
      class="line-numbers-rows"><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span></span></code><button
        class="VJbwyy" type="button" aria-label="复制代码"><i aria-label="icon: copy" class="anticon anticon-copy"><svg
        viewBox="64 64 896 896" focusable="false" class="" data-icon="copy" width="1em" height="1em"
        fill="currentColor" aria-hidden="true"><path
        d="M832 64H296c-4.4 0-8 3.6-8 8v56c0 4.4 3.6 8 8 8h496v688c0 4.4 3.6 8 8 8h56c4.4 0 8-3.6 8-8V96c0-17.7-14.3-32-32-32zM704 192H192c-17.7 0-32 14.3-32 32v530.7c0 8.5 3.4 16.6 9.4 22.6l173.3 173.3c2.2 2.2 4.7 4 7.4 5.5v1.9h4.2c3.5 1.3 7.2 2 11 2H704c17.7 0 32-14.3 32-32V224c0-17.7-14.3-32-32-32zM350 856.2L263.9 770H350v86.2zM664 888H414V746c0-22.1-17.9-40-40-40H232V264h432v624z"></path></svg></i></button></pre>
<p>也可以将<code>metaclass</code>定义为一个真正的类:</p>
<pre class="line-numbers  language-python"><code class="python  language-python"><span class="token comment"># 记住type还是一个类，所以可以继承它</span>
<span class="token keyword">class</span> <span class="token class-name">UpperAttrMetaclass</span><span
            class="token punctuation">(</span><span class="token builtin">type</span><span
            class="token punctuation">)</span><span class="token punctuation">:</span> 
    <span class="token comment"># __new__ 会在__init__之前调用，它会创建并返回一个实例</span>
    <span class="token comment"># 而__init__仅用于初始化，进行一些参数的配置 </span>
    <span class="token keyword">def</span> <span class="token function">__new__</span><span
            class="token punctuation">(</span>upperattr_metaclass<span class="token punctuation">,</span> future_class_name<span
            class="token punctuation">,</span> 
                future_class_parents<span class="token punctuation">,</span> future_class_attr<span
            class="token punctuation">)</span><span class="token punctuation">:</span>
        uppercase_attr <span class="token operator">=</span> <span class="token punctuation">{</span><span
            class="token punctuation">}</span>
        <span class="token keyword">for</span> name<span class="token punctuation">,</span> val <span
            class="token keyword">in</span> future_class_attr<span class="token punctuation">.</span>items<span
            class="token punctuation">(</span><span class="token punctuation">)</span><span
            class="token punctuation">:</span>
            <span class="token keyword">if</span> <span class="token keyword">not</span> name<span
            class="token punctuation">.</span>startswith<span class="token punctuation">(</span><span
            class="token string">'__'</span><span class="token punctuation">)</span><span
            class="token punctuation">:</span>
                uppercase_attr<span class="token punctuation">[</span>name<span
            class="token punctuation">.</span>upper<span class="token punctuation">(</span><span
            class="token punctuation">)</span><span class="token punctuation">]</span> <span
            class="token operator">=</span> val
            <span class="token keyword">else</span><span class="token punctuation">:</span>
                uppercase_attr<span class="token punctuation">[</span>name<span class="token punctuation">]</span> <span
            class="token operator">=</span> val

        <span class="token keyword">return</span> <span class="token builtin">type</span><span
            class="token punctuation">(</span>future_class_name<span class="token punctuation">,</span> future_class_parents<span
            class="token punctuation">,</span> uppercase_attr<span class="token punctuation">)</span>
<span aria-hidden="true"
      class="line-numbers-rows"><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span></span></code><button
        class="VJbwyy" type="button" aria-label="复制代码"><i aria-label="icon: copy" class="anticon anticon-copy"><svg
        viewBox="64 64 896 896" focusable="false" class="" data-icon="copy" width="1em" height="1em"
        fill="currentColor" aria-hidden="true"><path
        d="M832 64H296c-4.4 0-8 3.6-8 8v56c0 4.4 3.6 8 8 8h496v688c0 4.4 3.6 8 8 8h56c4.4 0 8-3.6 8-8V96c0-17.7-14.3-32-32-32zM704 192H192c-17.7 0-32 14.3-32 32v530.7c0 8.5 3.4 16.6 9.4 22.6l173.3 173.3c2.2 2.2 4.7 4 7.4 5.5v1.9h4.2c3.5 1.3 7.2 2 11 2H704c17.7 0 32-14.3 32-32V224c0-17.7-14.3-32-32-32zM350 856.2L263.9 770H350v86.2zM664 888H414V746c0-22.1-17.9-40-40-40H232V264h432v624z"></path></svg></i></button></pre>
<p>但是上面的做法并不符合OOP的思想，因为它直接调用了<strong>type</strong>方法，实际上可以调用<strong>type</strong>的<code>__new__</code>方法。</p>
<pre class="line-numbers  language-python"><code class="python  language-python"><span
        class="token keyword">class</span> <span class="token class-name">UpperAttrMetaclass</span><span
        class="token punctuation">(</span><span class="token builtin">type</span><span
        class="token punctuation">)</span><span class="token punctuation">:</span> 
    <span class="token keyword">def</span> <span class="token function">__new__</span><span
            class="token punctuation">(</span>upperattr_metaclass<span class="token punctuation">,</span> future_class_name<span
            class="token punctuation">,</span> 
                future_class_parents<span class="token punctuation">,</span> future_class_attr<span
            class="token punctuation">)</span><span class="token punctuation">:</span>
        uppercase_attr <span class="token operator">=</span> <span class="token punctuation">{</span><span
            class="token punctuation">}</span>
        <span class="token keyword">for</span> name<span class="token punctuation">,</span> val <span
            class="token keyword">in</span> future_class_attr<span class="token punctuation">.</span>items<span
            class="token punctuation">(</span><span class="token punctuation">)</span><span
            class="token punctuation">:</span>
            <span class="token keyword">if</span> <span class="token keyword">not</span> name<span
            class="token punctuation">.</span>startswith<span class="token punctuation">(</span><span
            class="token string">'__'</span><span class="token punctuation">)</span><span
            class="token punctuation">:</span>
                uppercase_attr<span class="token punctuation">[</span>name<span
            class="token punctuation">.</span>upper<span class="token punctuation">(</span><span
            class="token punctuation">)</span><span class="token punctuation">]</span> <span
            class="token operator">=</span> val
            <span class="token keyword">else</span><span class="token punctuation">:</span>
                uppercase_attr<span class="token punctuation">[</span>name<span class="token punctuation">]</span> <span
            class="token operator">=</span> val
        <span class="token comment"># 调用type.__new__方法 </span>
        <span class="token keyword">return</span> <span class="token builtin">type</span><span
            class="token punctuation">.</span>__new__<span
            class="token punctuation">(</span>upperattr_metaclass<span class="token punctuation">,</span> future_class_name<span
            class="token punctuation">,</span> 
                            future_class_parents<span class="token punctuation">,</span> uppercase_attr<span
            class="token punctuation">)</span>
<span aria-hidden="true"
      class="line-numbers-rows"><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span></span></code><button
        class="VJbwyy" type="button" aria-label="复制代码"><i aria-label="icon: copy" class="anticon anticon-copy"><svg
        viewBox="64 64 896 896" focusable="false" class="" data-icon="copy" width="1em" height="1em"
        fill="currentColor" aria-hidden="true"><path
        d="M832 64H296c-4.4 0-8 3.6-8 8v56c0 4.4 3.6 8 8 8h496v688c0 4.4 3.6 8 8 8h56c4.4 0 8-3.6 8-8V96c0-17.7-14.3-32-32-32zM704 192H192c-17.7 0-32 14.3-32 32v530.7c0 8.5 3.4 16.6 9.4 22.6l173.3 173.3c2.2 2.2 4.7 4 7.4 5.5v1.9h4.2c3.5 1.3 7.2 2 11 2H704c17.7 0 32-14.3 32-32V224c0-17.7-14.3-32-32-32zM350 856.2L263.9 770H350v86.2zM664 888H414V746c0-22.1-17.9-40-40-40H232V264h432v624z"></path></svg></i></button></pre>
<p>你可能注意到参数<code>upperattr_metaclass</code>, 它代表要实例化的类。当然，我这里取这么个复杂的名字主要是为了明确它的含义。但是，就像<code>self</code>参数一样，所有参数都有其习惯性命名。所以生产环境下的<code>metaclass</code>定义如下：
</p>
<pre class="line-numbers  language-python"><code class="python  language-python"><span
        class="token keyword">class</span> <span class="token class-name">UpperAttrMetaclass</span><span
        class="token punctuation">(</span><span class="token builtin">type</span><span
        class="token punctuation">)</span><span class="token punctuation">:</span> 
    <span class="token keyword">def</span> <span class="token function">__new__</span><span
            class="token punctuation">(</span>cls<span class="token punctuation">,</span> clsname<span
            class="token punctuation">,</span> bases<span class="token punctuation">,</span> dct<span
            class="token punctuation">)</span><span class="token punctuation">:</span>
        uppercase_attr <span class="token operator">=</span> <span class="token punctuation">{</span><span
            class="token punctuation">}</span>
        <span class="token keyword">for</span> name<span class="token punctuation">,</span> val <span
            class="token keyword">in</span> dct<span class="token punctuation">.</span>items<span
            class="token punctuation">(</span><span class="token punctuation">)</span><span
            class="token punctuation">:</span>
            <span class="token keyword">if</span> <span class="token keyword">not</span> name<span
            class="token punctuation">.</span>startswith<span class="token punctuation">(</span><span
            class="token string">'__'</span><span class="token punctuation">)</span><span
            class="token punctuation">:</span>
                uppercase_attr<span class="token punctuation">[</span>name<span
            class="token punctuation">.</span>upper<span class="token punctuation">(</span><span
            class="token punctuation">)</span><span class="token punctuation">]</span> <span
            class="token operator">=</span> val
            <span class="token keyword">else</span><span class="token punctuation">:</span>
                uppercase_attr<span class="token punctuation">[</span>name<span class="token punctuation">]</span> <span
            class="token operator">=</span> val
        <span class="token keyword">return</span> <span class="token builtin">type</span><span
            class="token punctuation">.</span>__new__<span class="token punctuation">(</span>cls<span
            class="token punctuation">,</span> clsname<span class="token punctuation">,</span> bases<span
            class="token punctuation">,</span> uppercase_attr<span class="token punctuation">)</span>
<span aria-hidden="true"
      class="line-numbers-rows"><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span></span></code><button
        class="VJbwyy" type="button" aria-label="复制代码"><i aria-label="icon: copy" class="anticon anticon-copy"><svg
        viewBox="64 64 896 896" focusable="false" class="" data-icon="copy" width="1em" height="1em"
        fill="currentColor" aria-hidden="true"><path
        d="M832 64H296c-4.4 0-8 3.6-8 8v56c0 4.4 3.6 8 8 8h496v688c0 4.4 3.6 8 8 8h56c4.4 0 8-3.6 8-8V96c0-17.7-14.3-32-32-32zM704 192H192c-17.7 0-32 14.3-32 32v530.7c0 8.5 3.4 16.6 9.4 22.6l173.3 173.3c2.2 2.2 4.7 4 7.4 5.5v1.9h4.2c3.5 1.3 7.2 2 11 2H704c17.7 0 32-14.3 32-32V224c0-17.7-14.3-32-32-32zM350 856.2L263.9 770H350v86.2zM664 888H414V746c0-22.1-17.9-40-40-40H232V264h432v624z"></path></svg></i></button></pre>
<p>更好的方式是使用<code>super</code>方法，以便减轻这种继承关系。</p>
<pre class="line-numbers  language-python"><code class="python  language-python"><span
        class="token keyword">class</span> <span class="token class-name">UpperAttrMetaclass</span><span
        class="token punctuation">(</span><span class="token builtin">type</span><span
        class="token punctuation">)</span><span class="token punctuation">:</span> 
    <span class="token keyword">def</span> <span class="token function">__new__</span><span
            class="token punctuation">(</span>cls<span class="token punctuation">,</span> clsname<span
            class="token punctuation">,</span> bases<span class="token punctuation">,</span> dct<span
            class="token punctuation">)</span><span class="token punctuation">:</span>
        uppercase_attr <span class="token operator">=</span> <span class="token punctuation">{</span><span
            class="token punctuation">}</span>
        <span class="token keyword">for</span> name<span class="token punctuation">,</span> val <span
            class="token keyword">in</span> dct<span class="token punctuation">.</span>items<span
            class="token punctuation">(</span><span class="token punctuation">)</span><span
            class="token punctuation">:</span>
            <span class="token keyword">if</span> <span class="token keyword">not</span> name<span
            class="token punctuation">.</span>startswith<span class="token punctuation">(</span><span
            class="token string">'__'</span><span class="token punctuation">)</span><span
            class="token punctuation">:</span>
                uppercase_attr<span class="token punctuation">[</span>name<span
            class="token punctuation">.</span>upper<span class="token punctuation">(</span><span
            class="token punctuation">)</span><span class="token punctuation">]</span> <span
            class="token operator">=</span> val
            <span class="token keyword">else</span><span class="token punctuation">:</span>
                uppercase_attr<span class="token punctuation">[</span>name<span class="token punctuation">]</span> <span
            class="token operator">=</span> val

        <span class="token keyword">return</span> <span class="token builtin">super</span><span
            class="token punctuation">(</span>UpperAttrMetaclass<span class="token punctuation">,</span> cls<span
            class="token punctuation">)</span><span class="token punctuation">.</span>__new__<span
            class="token punctuation">(</span>cls<span class="token punctuation">,</span> clsname<span
            class="token punctuation">,</span> bases<span class="token punctuation">,</span> uppercase_attr<span
            class="token punctuation">)</span>
<span aria-hidden="true"
      class="line-numbers-rows"><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span></span></code><button
        class="VJbwyy" type="button" aria-label="复制代码"><i aria-label="icon: copy" class="anticon anticon-copy"><svg
        viewBox="64 64 896 896" focusable="false" class="" data-icon="copy" width="1em" height="1em"
        fill="currentColor" aria-hidden="true"><path
        d="M832 64H296c-4.4 0-8 3.6-8 8v56c0 4.4 3.6 8 8 8h496v688c0 4.4 3.6 8 8 8h56c4.4 0 8-3.6 8-8V96c0-17.7-14.3-32-32-32zM704 192H192c-17.7 0-32 14.3-32 32v530.7c0 8.5 3.4 16.6 9.4 22.6l173.3 173.3c2.2 2.2 4.7 4 7.4 5.5v1.9h4.2c3.5 1.3 7.2 2 11 2H704c17.7 0 32-14.3 32-32V224c0-17.7-14.3-32-32-32zM350 856.2L263.9 770H350v86.2zM664 888H414V746c0-22.1-17.9-40-40-40H232V264h432v624z"></path></svg></i></button></pre>
<p>元类实际上做了以下三方面的工作：</p>
<ul>
    <li>干涉创建类的过程</li>
    <li>修改类</li>
    <li>返回修改之后的类</li>
</ul>
<h3>为什么使用类而不是函数来定义元类？</h3>
<p>理由如下：</p>
<ul>
    <li>目的更明确，当你阅读<code>UpperAttrMetaclass(type)</code>的时候，你知道它用来做什么。</li>
    <li>可以使用面向对象编程，元类可以继承自其它元类，还可以覆盖父类方法。</li>
    <li>可以更好的组织代码结构。元类通常用于处理比较复杂的情况。</li>
    <li>可以为<code>__new__</code>、<code>__init__</code>和<code>__call__</code>编写钩子，为后续开发者提供便利。</li>
</ul>
<h3>为什么使用元类？</h3>
<p>现在，终极问题来了，为什么要使用元类这种模糊且容易出错的功能？<br>
    一般情况下，我们并不会使用元类，99%的开发者并不会用到元类，所以一般不用考虑这个问题。<br>
    元类主用用于创建API，一个典型的例子就是Django的ORM。<br>
    它让我们可以这样定义一个类：</p>
<pre class="line-numbers  language-python"><code class="python  language-python"><span
        class="token keyword">class</span> <span class="token class-name">Person</span><span
        class="token punctuation">(</span>models<span class="token punctuation">.</span>Model<span
        class="token punctuation">)</span><span class="token punctuation">:</span>
  name <span class="token operator">=</span> models<span class="token punctuation">.</span>CharField<span
            class="token punctuation">(</span>max_length<span class="token operator">=</span><span
            class="token number">30</span><span class="token punctuation">)</span>
  age <span class="token operator">=</span> models<span class="token punctuation">.</span>IntegerField<span
            class="token punctuation">(</span><span class="token punctuation">)</span>
<span aria-hidden="true" class="line-numbers-rows"><span></span><span></span><span></span></span></code><button
        class="VJbwyy" type="button" aria-label="复制代码"><i aria-label="icon: copy" class="anticon anticon-copy"><svg
        viewBox="64 64 896 896" focusable="false" class="" data-icon="copy" width="1em" height="1em"
        fill="currentColor" aria-hidden="true"><path
        d="M832 64H296c-4.4 0-8 3.6-8 8v56c0 4.4 3.6 8 8 8h496v688c0 4.4 3.6 8 8 8h56c4.4 0 8-3.6 8-8V96c0-17.7-14.3-32-32-32zM704 192H192c-17.7 0-32 14.3-32 32v530.7c0 8.5 3.4 16.6 9.4 22.6l173.3 173.3c2.2 2.2 4.7 4 7.4 5.5v1.9h4.2c3.5 1.3 7.2 2 11 2H704c17.7 0 32-14.3 32-32V224c0-17.7-14.3-32-32-32zM350 856.2L263.9 770H350v86.2zM664 888H414V746c0-22.1-17.9-40-40-40H232V264h432v624z"></path></svg></i></button></pre>
<p>运行下面的代码：</p>
<pre class="line-numbers  language-python"><code class="python  language-python">guy <span
        class="token operator">=</span> Person<span class="token punctuation">(</span>name<span
        class="token operator">=</span><span class="token string">'bob'</span><span
        class="token punctuation">,</span> age<span class="token operator">=</span><span
        class="token string">'35'</span><span class="token punctuation">)</span>
<span class="token keyword">print</span><span class="token punctuation">(</span>guy<span
            class="token punctuation">.</span>age<span class="token punctuation">)</span>
<span aria-hidden="true" class="line-numbers-rows"><span></span><span></span></span></code><button class="VJbwyy"
                                                                                                   type="button"
                                                                                                   aria-label="复制代码"><i
        aria-label="icon: copy" class="anticon anticon-copy"><svg viewBox="64 64 896 896" focusable="false" class=""
                                                                  data-icon="copy" width="1em" height="1em"
                                                                  fill="currentColor" aria-hidden="true"><path
        d="M832 64H296c-4.4 0-8 3.6-8 8v56c0 4.4 3.6 8 8 8h496v688c0 4.4 3.6 8 8 8h56c4.4 0 8-3.6 8-8V96c0-17.7-14.3-32-32-32zM704 192H192c-17.7 0-32 14.3-32 32v530.7c0 8.5 3.4 16.6 9.4 22.6l173.3 173.3c2.2 2.2 4.7 4 7.4 5.5v1.9h4.2c3.5 1.3 7.2 2 11 2H704c17.7 0 32-14.3 32-32V224c0-17.7-14.3-32-32-32zM350 856.2L263.9 770H350v86.2zM664 888H414V746c0-22.1-17.9-40-40-40H232V264h432v624z"></path></svg></i></button></pre>
<p>
    返回的结果是<code>int</code>类型而不是<code>IntegerField</code>对象。这是因为<code>models.Model</code>使用了元类，它会将Python中定义的字段转换成数据库中的字段。<br>
    通过使用元类，Django将复杂的接口转换成简单的接口。</p>
<h3>总结</h3>
<p>首先，我们知道了类其实就是可以创建实例的对象。而类又是通过元类来创建的。</p>
<pre class="line-numbers  language-python"><code class="python  language-python"><span
        class="token operator">&gt;&gt;</span><span
        class="token operator">&gt;</span> <span class="token keyword">class</span> <span
        class="token class-name">Foo</span><span
        class="token punctuation">(</span><span class="token builtin">object</span><span
        class="token punctuation">)</span><span class="token punctuation">:</span> <span
        class="token keyword">pass</span>
<span class="token operator">&gt;&gt;</span><span class="token operator">&gt;</span> <span
            class="token builtin">id</span><span class="token punctuation">(</span>Foo<span
            class="token punctuation">)</span>
<span class="token number">142630324</span>
<span aria-hidden="true" class="line-numbers-rows"><span></span><span></span><span></span></span></code><button
        class="VJbwyy" type="button" aria-label="复制代码"><i aria-label="icon: copy" class="anticon anticon-copy"><svg
        viewBox="64 64 896 896" focusable="false" class="" data-icon="copy" width="1em" height="1em"
        fill="currentColor" aria-hidden="true"><path
        d="M832 64H296c-4.4 0-8 3.6-8 8v56c0 4.4 3.6 8 8 8h496v688c0 4.4 3.6 8 8 8h56c4.4 0 8-3.6 8-8V96c0-17.7-14.3-32-32-32zM704 192H192c-17.7 0-32 14.3-32 32v530.7c0 8.5 3.4 16.6 9.4 22.6l173.3 173.3c2.2 2.2 4.7 4 7.4 5.5v1.9h4.2c3.5 1.3 7.2 2 11 2H704c17.7 0 32-14.3 32-32V224c0-17.7-14.3-32-32-32zM350 856.2L263.9 770H350v86.2zM664 888H414V746c0-22.1-17.9-40-40-40H232V264h432v624z"></path></svg></i></button></pre>
<p>Python中所有数据类型都是对象，它们要么是类的实例要么是元类的实例。<br>
    除了<strong>type</strong>，它实际上是自身的元类。这一点没法在Python中重现，因为它是在编译阶段实现的。</p>
<p>其次， 元类都是复杂的，对于一般的类是用不着的。可以使用以下两种技巧修改类：</p>
<ul>
    <li>monkey patch</li>
    <li>类修饰器</li>
</ul>
<p>当你需要修改类的时候，99%的情况下可以使用元类。但是99%的情况下，你根本不需要修改一个类。</p>