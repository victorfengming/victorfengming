---
title: "Python中@classmethod 和@staticmethod用法和区别"
cover: "/img/lynk/47.jpg"
date:       2019-11-28
subtitle: "装饰器的高级用法"
tags:
	- Python
	- solution
	- interview
	- decorator
---


<p><code>@classsmethod</code>
    类装饰器：当用此装饰器定义方法时，将类而不是类的实例作为第一个参数，这意味着可以在此方法中直接使用类的属性，而不是特定的实例的属性，因此不必进行硬编码。
</p>
<p><code>@staticmethod</code> 静态装饰器：当用此装饰器定义方法时，不会传递类或实例作为它的参数，这意味着可以在类中放置一个函数。静态方法就是普通的函数，只是碰巧在类的定义体中，而不是在模块层定义。
</p>
<blockquote>
    <p>在《流畅的Python》中，作者对这两个装饰器的评价：classmethod 装饰器非常有用，但是我从未见过不得不用 staticmethod
        的情况。如果想定义不需要与类交互的函数，那么在模块中定义就好了。有时，函数虽然从不处理类，但是函数的功能与类紧密相关，因此想把它放在近处。即便如此，在同一模块中的类前面或后面定义函数也就行了。</p>
</blockquote>
<pre class="line-numbers  language-python"><code class="python  language-python"><span
        class="token keyword">class</span> <span class="token class-name">Date</span><span
        class="token punctuation">(</span><span class="token builtin">object</span><span
        class="token punctuation">)</span><span class="token punctuation">:</span>

    <span class="token keyword">def</span> <span class="token function">__init__</span><span
            class="token punctuation">(</span>self<span class="token punctuation">,</span> day<span
            class="token operator">=</span><span class="token number">0</span><span
            class="token punctuation">,</span> month<span class="token operator">=</span><span
            class="token number">0</span><span
            class="token punctuation">,</span> year<span class="token operator">=</span><span
            class="token number">0</span><span class="token punctuation">)</span><span
            class="token punctuation">:</span>
        self<span class="token punctuation">.</span>day <span class="token operator">=</span> day
        self<span class="token punctuation">.</span>month <span class="token operator">=</span> month
        self<span class="token punctuation">.</span>year <span class="token operator">=</span> year

    @<span class="token builtin">classmethod</span>
    <span class="token keyword">def</span> <span class="token function">from_string</span><span
            class="token punctuation">(</span>cls<span class="token punctuation">,</span> date_as_string<span
            class="token punctuation">)</span><span class="token punctuation">:</span>
        day<span class="token punctuation">,</span> month<span class="token punctuation">,</span> year <span
            class="token operator">=</span> <span class="token builtin">map</span><span
            class="token punctuation">(</span><span class="token builtin">int</span><span
            class="token punctuation">,</span> date_as_string<span
            class="token punctuation">.</span>split<span class="token punctuation">(</span><span
            class="token string">'-'</span><span class="token punctuation">)</span><span
            class="token punctuation">)</span>
        date1 <span class="token operator">=</span> cls<span class="token punctuation">(</span>day<span
            class="token punctuation">,</span> month<span class="token punctuation">,</span> year<span
            class="token punctuation">)</span>
        <span class="token keyword">return</span> date1

    @<span class="token builtin">staticmethod</span>
    <span class="token keyword">def</span> <span class="token function">is_date_valid</span><span
            class="token punctuation">(</span>date_as_string<span class="token punctuation">)</span><span
            class="token punctuation">:</span>
        day<span class="token punctuation">,</span> month<span class="token punctuation">,</span> year <span
            class="token operator">=</span> <span class="token builtin">map</span><span
            class="token punctuation">(</span><span class="token builtin">int</span><span
            class="token punctuation">,</span> date_as_string<span
            class="token punctuation">.</span>split<span class="token punctuation">(</span><span
            class="token string">'-'</span><span class="token punctuation">)</span><span
            class="token punctuation">)</span>
        <span class="token keyword">return</span> day <span class="token operator">&lt;=</span> <span
            class="token number">31</span> <span class="token keyword">and</span> month <span
            class="token operator">&lt;=</span> <span class="token number">12</span> <span
            class="token keyword">and</span> year <span class="token operator">&lt;=</span> <span
            class="token number">3999</span>

date2 <span class="token operator">=</span> Date<span class="token punctuation">.</span>from_string<span
            class="token punctuation">(</span><span class="token string">'11-09-2012'</span><span
            class="token punctuation">)</span>
is_date <span class="token operator">=</span> Date<span class="token punctuation">.</span>is_date_valid<span
            class="token punctuation">(</span><span class="token string">'11-09-2012'</span><span
            class="token punctuation">)</span>
<span aria-hidden="true"
      class="line-numbers-rows"><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span></span></code><button
        class="VJbwyy" type="button" aria-label="复制代码"><i aria-label="icon: copy" class="anticon anticon-copy"><svg
        viewBox="64 64 896 896" focusable="false" class="" data-icon="copy" width="1em" height="1em"
        fill="currentColor" aria-hidden="true"><path
        d="M832 64H296c-4.4 0-8 3.6-8 8v56c0 4.4 3.6 8 8 8h496v688c0 4.4 3.6 8 8 8h56c4.4 0 8-3.6 8-8V96c0-17.7-14.3-32-32-32zM704 192H192c-17.7 0-32 14.3-32 32v530.7c0 8.5 3.4 16.6 9.4 22.6l173.3 173.3c2.2 2.2 4.7 4 7.4 5.5v1.9h4.2c3.5 1.3 7.2 2 11 2H704c17.7 0 32-14.3 32-32V224c0-17.7-14.3-32-32-32zM350 856.2L263.9 770H350v86.2zM664 888H414V746c0-22.1-17.9-40-40-40H232V264h432v624z"></path></svg></i></button></pre>
<p>使用静态方法写基类，注意静态方法使用了实例的硬编码。</p>
<pre class="line-numbers  language-python"><code class="python  language-python"><span
        class="token keyword">class</span> <span class="token class-name">Date</span><span
        class="token punctuation">:</span>
  <span class="token keyword">def</span> <span class="token function">__init__</span><span
            class="token punctuation">(</span>self<span class="token punctuation">,</span> month<span
            class="token punctuation">,</span> day<span class="token punctuation">,</span> year<span
            class="token punctuation">)</span><span class="token punctuation">:</span>
    self<span class="token punctuation">.</span>month <span class="token operator">=</span> month
    self<span class="token punctuation">.</span>day   <span class="token operator">=</span> day
    self<span class="token punctuation">.</span>year  <span class="token operator">=</span> year

  <span class="token keyword">def</span> <span class="token function">display</span><span
            class="token punctuation">(</span>self<span class="token punctuation">)</span><span
            class="token punctuation">:</span>
    <span class="token keyword">return</span> <span class="token string">"{0}-{1}-{2}"</span><span
            class="token punctuation">.</span><span class="token builtin">format</span><span
            class="token punctuation">(</span>self<span class="token punctuation">.</span>month<span
            class="token punctuation">,</span> self<span class="token punctuation">.</span>day<span
            class="token punctuation">,</span> self<span class="token punctuation">.</span>year<span
            class="token punctuation">)</span>

  @<span class="token builtin">staticmethod</span>
  <span class="token keyword">def</span> <span class="token function">millenium</span><span
            class="token punctuation">(</span>month<span class="token punctuation">,</span> day<span
            class="token punctuation">)</span><span class="token punctuation">:</span>
    <span class="token keyword">return</span> Date<span class="token punctuation">(</span>month<span
            class="token punctuation">,</span> day<span class="token punctuation">,</span> <span
            class="token number">2000</span><span class="token punctuation">)</span>

new_year <span class="token operator">=</span> Date<span class="token punctuation">(</span><span
            class="token number">1</span><span class="token punctuation">,</span> <span
            class="token number">1</span><span class="token punctuation">,</span> <span
            class="token number">2013</span><span class="token punctuation">)</span>               <span
            class="token comment"># Creates a new Date object</span>
millenium_new_year <span class="token operator">=</span> Date<span class="token punctuation">.</span>millenium<span
            class="token punctuation">(</span><span class="token number">1</span><span
            class="token punctuation">,</span> <span class="token number">1</span><span
            class="token punctuation">)</span> <span class="token comment"># also creates a Date object. </span>

<span class="token comment"># Proof:</span>
new_year<span class="token punctuation">.</span>display<span class="token punctuation">(</span><span
            class="token punctuation">)</span>           <span class="token comment"># "1-1-2013"</span>
millenium_new_year<span class="token punctuation">.</span>display<span class="token punctuation">(</span><span
            class="token punctuation">)</span> <span class="token comment"># "1-1-2000"</span>

<span class="token builtin">isinstance</span><span class="token punctuation">(</span>new_year<span
            class="token punctuation">,</span> Date<span class="token punctuation">)</span> <span
            class="token comment"># True</span>
<span class="token builtin">isinstance</span><span class="token punctuation">(</span>millenium_new_year<span
            class="token punctuation">,</span> Date<span class="token punctuation">)</span> <span
            class="token comment"># True</span>
<span aria-hidden="true"
      class="line-numbers-rows"><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span></span></code><button
        class="VJbwyy" type="button" aria-label="复制代码"><i aria-label="icon: copy" class="anticon anticon-copy"><svg
        viewBox="64 64 896 896" focusable="false" class="" data-icon="copy" width="1em" height="1em"
        fill="currentColor" aria-hidden="true"><path
        d="M832 64H296c-4.4 0-8 3.6-8 8v56c0 4.4 3.6 8 8 8h496v688c0 4.4 3.6 8 8 8h56c4.4 0 8-3.6 8-8V96c0-17.7-14.3-32-32-32zM704 192H192c-17.7 0-32 14.3-32 32v530.7c0 8.5 3.4 16.6 9.4 22.6l173.3 173.3c2.2 2.2 4.7 4 7.4 5.5v1.9h4.2c3.5 1.3 7.2 2 11 2H704c17.7 0 32-14.3 32-32V224c0-17.7-14.3-32-32-32zM350 856.2L263.9 770H350v86.2zM664 888H414V746c0-22.1-17.9-40-40-40H232V264h432v624z"></path></svg></i></button></pre>
<p>继承之后，millenium方法就用不了了。</p>
<pre class="line-numbers  language-python"><code class="python  language-python"><span
        class="token keyword">class</span> <span class="token class-name">DateTime</span><span
        class="token punctuation">(</span>Date<span class="token punctuation">)</span><span
        class="token punctuation">:</span>
  <span class="token keyword">def</span> <span class="token function">display</span><span
            class="token punctuation">(</span>self<span class="token punctuation">)</span><span
            class="token punctuation">:</span>
      <span class="token keyword">return</span> <span class="token string">"{0}-{1}-{2} - 00:00:00PM"</span><span
            class="token punctuation">.</span><span class="token builtin">format</span><span
            class="token punctuation">(</span>self<span class="token punctuation">.</span>month<span
            class="token punctuation">,</span> self<span class="token punctuation">.</span>day<span
            class="token punctuation">,</span> self<span class="token punctuation">.</span>year<span
            class="token punctuation">)</span>

datetime1 <span class="token operator">=</span> DateTime<span class="token punctuation">(</span><span
            class="token number">10</span><span class="token punctuation">,</span> <span
            class="token number">10</span><span class="token punctuation">,</span> <span
            class="token number">1990</span><span class="token punctuation">)</span>
datetime2 <span class="token operator">=</span> DateTime<span class="token punctuation">.</span>millenium<span
            class="token punctuation">(</span><span class="token number">10</span><span
            class="token punctuation">,</span> <span class="token number">10</span><span
            class="token punctuation">)</span>

<span class="token builtin">isinstance</span><span class="token punctuation">(</span>datetime1<span
            class="token punctuation">,</span> DateTime<span class="token punctuation">)</span> <span
            class="token comment"># True</span>
<span class="token builtin">isinstance</span><span class="token punctuation">(</span>datetime2<span
            class="token punctuation">,</span> DateTime<span class="token punctuation">)</span> <span
            class="token comment"># False</span>

datetime1<span class="token punctuation">.</span>display<span class="token punctuation">(</span><span
            class="token punctuation">)</span> <span
            class="token comment"># returns "10-10-1990 - 00:00:00PM"</span>
datetime2<span class="token punctuation">.</span>display<span class="token punctuation">(</span><span
            class="token punctuation">)</span> <span class="token comment"># returns "10-10-2000" because it's not a DateTime object but a Date object.</span>
<span aria-hidden="true"
      class="line-numbers-rows"><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span></span></code><button
        class="VJbwyy" type="button" aria-label="复制代码"><i aria-label="icon: copy" class="anticon anticon-copy"><svg
        viewBox="64 64 896 896" focusable="false" class="" data-icon="copy" width="1em" height="1em"
        fill="currentColor" aria-hidden="true"><path
        d="M832 64H296c-4.4 0-8 3.6-8 8v56c0 4.4 3.6 8 8 8h496v688c0 4.4 3.6 8 8 8h56c4.4 0 8-3.6 8-8V96c0-17.7-14.3-32-32-32zM704 192H192c-17.7 0-32 14.3-32 32v530.7c0 8.5 3.4 16.6 9.4 22.6l173.3 173.3c2.2 2.2 4.7 4 7.4 5.5v1.9h4.2c3.5 1.3 7.2 2 11 2H704c17.7 0 32-14.3 32-32V224c0-17.7-14.3-32-32-32zM350 856.2L263.9 770H350v86.2zM664 888H414V746c0-22.1-17.9-40-40-40H232V264h432v624z"></path></svg></i></button></pre>
<p>改成类方法，</p>
<pre class="line-numbers  language-python"><code class="python  language-python"><span
        class="token decorator annotation punctuation">@classmethod</span>
<span class="token keyword">def</span> <span class="token function">millenium</span><span
            class="token punctuation">(</span>cls<span class="token punctuation">,</span> month<span
            class="token punctuation">,</span> day<span class="token punctuation">)</span><span
            class="token punctuation">:</span>
    <span class="token keyword">return</span> cls<span class="token punctuation">(</span>month<span
            class="token punctuation">,</span> day<span class="token punctuation">,</span> <span
            class="token number">2000</span><span class="token punctuation">)</span>
<span aria-hidden="true" class="line-numbers-rows"><span></span><span></span><span></span></span></code><button
        class="VJbwyy" type="button" aria-label="复制代码"><i aria-label="icon: copy" class="anticon anticon-copy"><svg
        viewBox="64 64 896 896" focusable="false" class="" data-icon="copy" width="1em" height="1em"
        fill="currentColor" aria-hidden="true"><path
        d="M832 64H296c-4.4 0-8 3.6-8 8v56c0 4.4 3.6 8 8 8h496v688c0 4.4 3.6 8 8 8h56c4.4 0 8-3.6 8-8V96c0-17.7-14.3-32-32-32zM704 192H192c-17.7 0-32 14.3-32 32v530.7c0 8.5 3.4 16.6 9.4 22.6l173.3 173.3c2.2 2.2 4.7 4 7.4 5.5v1.9h4.2c3.5 1.3 7.2 2 11 2H704c17.7 0 32-14.3 32-32V224c0-17.7-14.3-32-32-32zM350 856.2L263.9 770H350v86.2zM664 888H414V746c0-22.1-17.9-40-40-40H232V264h432v624z"></path></svg></i></button></pre>
<p>就正确了</p>
<pre class="line-numbers  language-python"><code class="python  language-python">datetime1 <span
        class="token operator">=</span> DateTime<span class="token punctuation">(</span><span
        class="token number">10</span><span
        class="token punctuation">,</span> <span class="token number">10</span><span
        class="token punctuation">,</span> <span class="token number">1990</span><span
        class="token punctuation">)</span>
datetime2 <span class="token operator">=</span> DateTime<span class="token punctuation">.</span>millenium<span
            class="token punctuation">(</span><span class="token number">10</span><span
            class="token punctuation">,</span> <span class="token number">10</span><span
            class="token punctuation">)</span>

<span class="token builtin">isinstance</span><span class="token punctuation">(</span>datetime1<span
            class="token punctuation">,</span> DateTime<span class="token punctuation">)</span> <span
            class="token comment"># True</span>
<span class="token builtin">isinstance</span><span class="token punctuation">(</span>datetime2<span
            class="token punctuation">,</span> DateTime<span class="token punctuation">)</span> <span
            class="token comment"># True</span>

datetime1<span class="token punctuation">.</span>display<span class="token punctuation">(</span><span
            class="token punctuation">)</span> <span class="token comment"># "10-10-1990 - 00:00:00PM"</span>
datetime2<span class="token punctuation">.</span>display<span class="token punctuation">(</span><span
            class="token punctuation">)</span> <span class="token comment"># "10-10-2000 - 00:00:00PM"</span>
<span aria-hidden="true"
      class="line-numbers-rows"><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span></span></code><button
        class="VJbwyy" type="button" aria-label="复制代码"><i aria-label="icon: copy" class="anticon anticon-copy"><svg
        viewBox="64 64 896 896" focusable="false" class="" data-icon="copy" width="1em" height="1em"
        fill="currentColor" aria-hidden="true"><path
        d="M832 64H296c-4.4 0-8 3.6-8 8v56c0 4.4 3.6 8 8 8h496v688c0 4.4 3.6 8 8 8h56c4.4 0 8-3.6 8-8V96c0-17.7-14.3-32-32-32zM704 192H192c-17.7 0-32 14.3-32 32v530.7c0 8.5 3.4 16.6 9.4 22.6l173.3 173.3c2.2 2.2 4.7 4 7.4 5.5v1.9h4.2c3.5 1.3 7.2 2 11 2H704c17.7 0 32-14.3 32-32V224c0-17.7-14.3-32-32-32zM350 856.2L263.9 770H350v86.2zM664 888H414V746c0-22.1-17.9-40-40-40H232V264h432v624z"></path></svg></i></button></pre>
<p>代码来自下面的链接，答的很赞：<br>
    <a href="https://stackoverflow.com/questions/12179271/meaning-of-classmethod-and-staticmethod-for-beginner/"
       target="_blank" rel="nofollow">https://stackoverflow.com/questions/12179271/meaning-of-classmethod-and-staticmethod-for-beginner/</a>
</p>
