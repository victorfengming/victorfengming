---
title: "对python中变量值交换的一些思考"
cover: "/img/lynk/69.jpg"
date:       2019-12-01
subtitle: "哪种方式性能更好"
tags:
	- Python
	- solution
	- interview
---




本文转载自:https://www.jianshu.com/p/0a80f376c7f3

<p>简书不维护了，欢迎关注我的知乎：<a
        href="https://links.jianshu.com/go?to=https%3A%2F%2Fwww.zhihu.com%2Fpeople%2Fxue-jian-27%2Factivities"
        target="_blank" rel="nofollow">波罗学的个人主页</a></p>
<p>知乎地址：<a href="https://links.jianshu.com/go?to=https%3A%2F%2Fzhuanlan.zhihu.com%2Fp%2F58691979" target="_blank"
           rel="nofollow">https://zhuanlan.zhihu.com/p/58691979</a></p>
<p>在编程中，一旦提到变量值的交换，脑海中最先浮现的做法就是引入一个临时变量作为媒介来做，来看看具体的实现。</p>
<h2>解决方案</h2>
<p>先假设有两个变量x、y，如下：</p>
<pre class="line-numbers  language-python"><code class="python  language-python">x <span
        class="token operator">=</span> <span class="token number">10</span>
y <span class="token operator">=</span> <span class="token number">20</span>
<span aria-hidden="true" class="line-numbers-rows"><span></span><span></span></span></code><button class="VJbwyy"
                                                                                                   type="button"
                                                                                                   aria-label="复制代码"><i
        aria-label="icon: copy" class="anticon anticon-copy"><svg viewBox="64 64 896 896" focusable="false" class=""
                                                                  data-icon="copy" width="1em" height="1em"
                                                                  fill="currentColor" aria-hidden="true"><path
        d="M832 64H296c-4.4 0-8 3.6-8 8v56c0 4.4 3.6 8 8 8h496v688c0 4.4 3.6 8 8 8h56c4.4 0 8-3.6 8-8V96c0-17.7-14.3-32-32-32zM704 192H192c-17.7 0-32 14.3-32 32v530.7c0 8.5 3.4 16.6 9.4 22.6l173.3 173.3c2.2 2.2 4.7 4 7.4 5.5v1.9h4.2c3.5 1.3 7.2 2 11 2H704c17.7 0 32-14.3 32-32V224c0-17.7-14.3-32-32-32zM350 856.2L263.9 770H350v86.2zM664 888H414V746c0-22.1-17.9-40-40-40H232V264h432v624z"></path></svg></i></button></pre>
<p><strong>常见方案</strong>，定义一个临时变量作为媒介，实现变量值的交换。实现如下：</p>
<pre class="line-numbers  language-python"><code class="python  language-python">t <span
        class="token operator">=</span> x
x <span class="token operator">=</span> y
y <span class="token operator">=</span> t
<span aria-hidden="true" class="line-numbers-rows"><span></span><span></span><span></span></span></code><button
        class="VJbwyy" type="button" aria-label="复制代码"><i aria-label="icon: copy" class="anticon anticon-copy"><svg
        viewBox="64 64 896 896" focusable="false" class="" data-icon="copy" width="1em" height="1em"
        fill="currentColor" aria-hidden="true"><path
        d="M832 64H296c-4.4 0-8 3.6-8 8v56c0 4.4 3.6 8 8 8h496v688c0 4.4 3.6 8 8 8h56c4.4 0 8-3.6 8-8V96c0-17.7-14.3-32-32-32zM704 192H192c-17.7 0-32 14.3-32 32v530.7c0 8.5 3.4 16.6 9.4 22.6l173.3 173.3c2.2 2.2 4.7 4 7.4 5.5v1.9h4.2c3.5 1.3 7.2 2 11 2H704c17.7 0 32-14.3 32-32V224c0-17.7-14.3-32-32-32zM350 856.2L263.9 770H350v86.2zM664 888H414V746c0-22.1-17.9-40-40-40H232V264h432v624z"></path></svg></i></button></pre>
<p><strong>pythonic</strong>，对于这种需求其实python为我们提供了一种更方便的解决方案。</p>
<pre class="line-numbers  language-python"><code class="python  language-python">x<span
        class="token punctuation">,</span> y <span class="token operator">=</span> y<span
        class="token punctuation">,</span> x
<span aria-hidden="true" class="line-numbers-rows"><span></span></span></code><button class="VJbwyy" type="button"
                                                                                      aria-label="复制代码"><i
        aria-label="icon: copy" class="anticon anticon-copy"><svg viewBox="64 64 896 896" focusable="false" class=""
                                                                  data-icon="copy" width="1em" height="1em"
                                                                  fill="currentColor" aria-hidden="true"><path
        d="M832 64H296c-4.4 0-8 3.6-8 8v56c0 4.4 3.6 8 8 8h496v688c0 4.4 3.6 8 8 8h56c4.4 0 8-3.6 8-8V96c0-17.7-14.3-32-32-32zM704 192H192c-17.7 0-32 14.3-32 32v530.7c0 8.5 3.4 16.6 9.4 22.6l173.3 173.3c2.2 2.2 4.7 4 7.4 5.5v1.9h4.2c3.5 1.3 7.2 2 11 2H704c17.7 0 32-14.3 32-32V224c0-17.7-14.3-32-32-32zM350 856.2L263.9 770H350v86.2zM664 888H414V746c0-22.1-17.9-40-40-40H232V264h432v624z"></path></svg></i></button></pre>
<p>从代码上就可以直观的理解此处的意图，即实现x与y变量值的交换。</p>
<p>到这里都非常容易理解，但是接下来我们需要思考一下：此写法性能如何？为什么可以如此便捷地就是实现了变量值交换？</p>
<h2>性能比较</h2>
<p>虽然写法简洁方便，但是是否已损耗性能为代价呢？定义两个函数：</p>
<pre class="line-numbers  language-python"><code class="python  language-python"><span
        class="token keyword">def</span> <span class="token function">swap1</span><span
        class="token punctuation">(</span><span class="token punctuation">)</span><span
        class="token punctuation">:</span>
    x <span class="token operator">=</span> <span class="token number">1</span>
    y <span class="token operator">=</span> <span class="token number">2</span>
    t <span class="token operator">=</span> x 
    x <span class="token operator">=</span> y
    y <span class="token operator">=</span> t

<span class="token keyword">def</span> <span class="token function">swap2</span><span class="token punctuation">(</span><span
            class="token punctuation">)</span><span class="token punctuation">:</span>
    x <span class="token operator">=</span> <span class="token number">1</span>
    y <span class="token operator">=</span> <span class="token number">2</span>
    x<span class="token punctuation">,</span> y <span class="token operator">=</span> y<span
            class="token punctuation">,</span> x
<span aria-hidden="true"
      class="line-numbers-rows"><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span></span></code><button
        class="VJbwyy" type="button" aria-label="复制代码"><i aria-label="icon: copy" class="anticon anticon-copy"><svg
        viewBox="64 64 896 896" focusable="false" class="" data-icon="copy" width="1em" height="1em"
        fill="currentColor" aria-hidden="true"><path
        d="M832 64H296c-4.4 0-8 3.6-8 8v56c0 4.4 3.6 8 8 8h496v688c0 4.4 3.6 8 8 8h56c4.4 0 8-3.6 8-8V96c0-17.7-14.3-32-32-32zM704 192H192c-17.7 0-32 14.3-32 32v530.7c0 8.5 3.4 16.6 9.4 22.6l173.3 173.3c2.2 2.2 4.7 4 7.4 5.5v1.9h4.2c3.5 1.3 7.2 2 11 2H704c17.7 0 32-14.3 32-32V224c0-17.7-14.3-32-32-32zM350 856.2L263.9 770H350v86.2zM664 888H414V746c0-22.1-17.9-40-40-40H232V264h432v624z"></path></svg></i></button></pre>
<p>为了更好的看出性能差异，循环调用分别调用两函数100次（需要在ipython中执行）：</p>
<p>swap1耗时38µs</p>
<pre class="line-numbers  language-python"><code class="python  language-python"><span
        class="token operator">%</span>time a <span class="token operator">=</span> <span
        class="token punctuation">[</span>swap1<span
        class="token punctuation">(</span><span class="token punctuation">)</span> <span
        class="token keyword">for</span> _ <span class="token keyword">in</span> <span
        class="token builtin">range</span><span class="token punctuation">(</span><span
        class="token number">100</span><span class="token punctuation">)</span><span
        class="token punctuation">]</span>
<span aria-hidden="true" class="line-numbers-rows"><span></span></span></code><button class="VJbwyy" type="button"
                                                                                      aria-label="复制代码"><i
        aria-label="icon: copy" class="anticon anticon-copy"><svg viewBox="64 64 896 896" focusable="false" class=""
                                                                  data-icon="copy" width="1em" height="1em"
                                                                  fill="currentColor" aria-hidden="true"><path
        d="M832 64H296c-4.4 0-8 3.6-8 8v56c0 4.4 3.6 8 8 8h496v688c0 4.4 3.6 8 8 8h56c4.4 0 8-3.6 8-8V96c0-17.7-14.3-32-32-32zM704 192H192c-17.7 0-32 14.3-32 32v530.7c0 8.5 3.4 16.6 9.4 22.6l173.3 173.3c2.2 2.2 4.7 4 7.4 5.5v1.9h4.2c3.5 1.3 7.2 2 11 2H704c17.7 0 32-14.3 32-32V224c0-17.7-14.3-32-32-32zM350 856.2L263.9 770H350v86.2zM664 888H414V746c0-22.1-17.9-40-40-40H232V264h432v624z"></path></svg></i></button></pre>
<p>结果如下：</p>
<pre class="line-numbers  language-bash"><code class="  language-bash">CPU times: user 31 µs, sys: 7 µs, total: 38 µs
Wall time: 67 µs
<span aria-hidden="true" class="line-numbers-rows"><span></span><span></span></span></code><button class="VJbwyy"
                                                                                                   type="button"
                                                                                                   aria-label="复制代码"><i
        aria-label="icon: copy" class="anticon anticon-copy"><svg viewBox="64 64 896 896" focusable="false" class=""
                                                                  data-icon="copy" width="1em" height="1em"
                                                                  fill="currentColor" aria-hidden="true"><path
        d="M832 64H296c-4.4 0-8 3.6-8 8v56c0 4.4 3.6 8 8 8h496v688c0 4.4 3.6 8 8 8h56c4.4 0 8-3.6 8-8V96c0-17.7-14.3-32-32-32zM704 192H192c-17.7 0-32 14.3-32 32v530.7c0 8.5 3.4 16.6 9.4 22.6l173.3 173.3c2.2 2.2 4.7 4 7.4 5.5v1.9h4.2c3.5 1.3 7.2 2 11 2H704c17.7 0 32-14.3 32-32V224c0-17.7-14.3-32-32-32zM350 856.2L263.9 770H350v86.2zM664 888H414V746c0-22.1-17.9-40-40-40H232V264h432v624z"></path></svg></i></button></pre>
<p>swap2耗时18µs</p>
<pre class="line-numbers  language-python"><code class="python  language-python"> <span
        class="token operator">%</span>time a <span class="token operator">=</span> <span
        class="token punctuation">[</span>swap2<span
        class="token punctuation">(</span><span class="token punctuation">)</span> <span
        class="token keyword">for</span> _ <span class="token keyword">in</span> <span
        class="token builtin">range</span><span class="token punctuation">(</span><span
        class="token number">100</span><span class="token punctuation">)</span><span
        class="token punctuation">]</span>
<span aria-hidden="true" class="line-numbers-rows"><span></span></span></code><button class="VJbwyy" type="button"
                                                                                      aria-label="复制代码"><i
        aria-label="icon: copy" class="anticon anticon-copy"><svg viewBox="64 64 896 896" focusable="false" class=""
                                                                  data-icon="copy" width="1em" height="1em"
                                                                  fill="currentColor" aria-hidden="true"><path
        d="M832 64H296c-4.4 0-8 3.6-8 8v56c0 4.4 3.6 8 8 8h496v688c0 4.4 3.6 8 8 8h56c4.4 0 8-3.6 8-8V96c0-17.7-14.3-32-32-32zM704 192H192c-17.7 0-32 14.3-32 32v530.7c0 8.5 3.4 16.6 9.4 22.6l173.3 173.3c2.2 2.2 4.7 4 7.4 5.5v1.9h4.2c3.5 1.3 7.2 2 11 2H704c17.7 0 32-14.3 32-32V224c0-17.7-14.3-32-32-32zM350 856.2L263.9 770H350v86.2zM664 888H414V746c0-22.1-17.9-40-40-40H232V264h432v624z"></path></svg></i></button></pre>
<p>结果如下：</p>
<pre class="line-numbers  language-bash"><code class="  language-bash">CPU times: user 18 µs, sys: 0 ns, total: 18 µs
Wall time: 21 µs
<span aria-hidden="true" class="line-numbers-rows"><span></span><span></span></span></code><button class="VJbwyy"
                                                                                                   type="button"
                                                                                                   aria-label="复制代码"><i
        aria-label="icon: copy" class="anticon anticon-copy"><svg viewBox="64 64 896 896" focusable="false" class=""
                                                                  data-icon="copy" width="1em" height="1em"
                                                                  fill="currentColor" aria-hidden="true"><path
        d="M832 64H296c-4.4 0-8 3.6-8 8v56c0 4.4 3.6 8 8 8h496v688c0 4.4 3.6 8 8 8h56c4.4 0 8-3.6 8-8V96c0-17.7-14.3-32-32-32zM704 192H192c-17.7 0-32 14.3-32 32v530.7c0 8.5 3.4 16.6 9.4 22.6l173.3 173.3c2.2 2.2 4.7 4 7.4 5.5v1.9h4.2c3.5 1.3 7.2 2 11 2H704c17.7 0 32-14.3 32-32V224c0-17.7-14.3-32-32-32zM350 856.2L263.9 770H350v86.2zM664 888H414V746c0-22.1-17.9-40-40-40H232V264h432v624z"></path></svg></i></button></pre>
<p>可以看出pythonic的写法比简单粗暴的引入新的辅助变量要快很多。写法如此简洁而且性能高，何乐而不为呢。</p>
<p>补充：这有一篇文章 <a href="https://links.jianshu.com/go?to=https%3A%2F%2Fzhuanlan.zhihu.com%2Fp%2F35095687"
                target="_blank" rel="nofollow">python面试值交换变量值</a> 从底层解释了两种方式性能上差异的原因。</p>
<h2>多些思考</h2>
<p>那么下面再思考一个问题：为什么python可以用这种写法来赋值呢？</p>
<p>看一些赋值运算符右边的表达式，即 y, x，这实际在python中称为<strong>元组</strong>的数据结构。我们可以看到赋值表达式左边是 x, y，那么为什么元组可以直接赋值给 x,y 呢？</p>
<p>此处利用了python的一个特性，即任何序列（或可迭代的对象）都可以通过简单的赋值操作分解为单独的变量。我们再来看一个例子：</p>
<pre class="line-numbers  language-python"><code class="python  language-python">name<span
        class="token punctuation">,</span> age<span class="token punctuation">,</span> mobile <span
        class="token operator">=</span> <span class="token string">'polo'</span><span
        class="token punctuation">,</span> <span class="token number">30</span><span
        class="token punctuation">,</span> <span class="token string">'15312210823'</span>
<span aria-hidden="true" class="line-numbers-rows"><span></span></span></code><button class="VJbwyy" type="button"
                                                                                      aria-label="复制代码"><i
        aria-label="icon: copy" class="anticon anticon-copy"><svg viewBox="64 64 896 896" focusable="false" class=""
                                                                  data-icon="copy" width="1em" height="1em"
                                                                  fill="currentColor" aria-hidden="true"><path
        d="M832 64H296c-4.4 0-8 3.6-8 8v56c0 4.4 3.6 8 8 8h496v688c0 4.4 3.6 8 8 8h56c4.4 0 8-3.6 8-8V96c0-17.7-14.3-32-32-32zM704 192H192c-17.7 0-32 14.3-32 32v530.7c0 8.5 3.4 16.6 9.4 22.6l173.3 173.3c2.2 2.2 4.7 4 7.4 5.5v1.9h4.2c3.5 1.3 7.2 2 11 2H704c17.7 0 32-14.3 32-32V224c0-17.7-14.3-32-32-32zM350 856.2L263.9 770H350v86.2zM664 888H414V746c0-22.1-17.9-40-40-40H232V264h432v624z"></path></svg></i></button></pre>
<p>执行以上代码便可将name赋值为polo，age赋值为30，phone赋值为15312210823。</p>
<h2>延伸扩展</h2>
<p>除了以上这种简单序列的拆解，python同样支持其他更复杂的场景，下面来看看多层嵌套变量的分解，例子最直观：</p>
<pre class="line-numbers  language-python"><code class="python  language-python">school_name<span
        class="token punctuation">,</span> <span class="token punctuation">(</span>student_name<span
        class="token punctuation">,</span> stduent_age<span class="token punctuation">,</span> stduent_sex<span
        class="token punctuation">)</span> <span class="token operator">=</span> <span
        class="token string">'致远中学'</span><span class="token punctuation">,</span> <span
        class="token punctuation">(</span><span class="token string">'polo'</span><span
        class="token punctuation">,</span> <span class="token number">18</span><span
        class="token punctuation">,</span> <span class="token string">'M'</span><span
        class="token punctuation">)</span>
<span aria-hidden="true" class="line-numbers-rows"><span></span></span></code><button class="VJbwyy" type="button"
                                                                                      aria-label="复制代码"><i
        aria-label="icon: copy" class="anticon anticon-copy"><svg viewBox="64 64 896 896" focusable="false" class=""
                                                                  data-icon="copy" width="1em" height="1em"
                                                                  fill="currentColor" aria-hidden="true"><path
        d="M832 64H296c-4.4 0-8 3.6-8 8v56c0 4.4 3.6 8 8 8h496v688c0 4.4 3.6 8 8 8h56c4.4 0 8-3.6 8-8V96c0-17.7-14.3-32-32-32zM704 192H192c-17.7 0-32 14.3-32 32v530.7c0 8.5 3.4 16.6 9.4 22.6l173.3 173.3c2.2 2.2 4.7 4 7.4 5.5v1.9h4.2c3.5 1.3 7.2 2 11 2H704c17.7 0 32-14.3 32-32V224c0-17.7-14.3-32-32-32zM350 856.2L263.9 770H350v86.2zM664 888H414V746c0-22.1-17.9-40-40-40H232V264h432v624z"></path></svg></i></button></pre>
<p>也可以支持不定长序列的灵活分解，比如现在有一个班级已排序的学生成绩列表，如下：</p>
<pre class="line-numbers  language-python"><code class="python  language-python">scores <span
        class="token operator">=</span> <span class="token punctuation">[</span><span
        class="token number">21</span><span
        class="token punctuation">,</span> <span class="token number">34</span><span
        class="token punctuation">,</span> <span class="token number">36</span><span
        class="token punctuation">,</span> <span class="token number">56</span><span
        class="token punctuation">,</span> <span class="token number">60</span><span
        class="token punctuation">,</span> <span class="token number">75</span><span
        class="token punctuation">,</span> <span class="token number">76</span><span
        class="token punctuation">,</span> <span class="token number">81</span><span
        class="token punctuation">,</span> <span class="token number">83</span><span
        class="token punctuation">,</span> <span class="token number">86</span><span
        class="token punctuation">,</span> <span class="token number">86</span><span
        class="token punctuation">,</span> <span class="token number">89</span><span
        class="token punctuation">,</span> <span class="token number">90</span><span
        class="token punctuation">,</span> <span class="token number">95</span><span
        class="token punctuation">,</span> <span class="token number">98</span><span
        class="token punctuation">,</span> <span class="token number">99</span><span
        class="token punctuation">]</span>
<span aria-hidden="true" class="line-numbers-rows"><span></span></span></code><button class="VJbwyy" type="button"
                                                                                      aria-label="复制代码"><i
        aria-label="icon: copy" class="anticon anticon-copy"><svg viewBox="64 64 896 896" focusable="false" class=""
                                                                  data-icon="copy" width="1em" height="1em"
                                                                  fill="currentColor" aria-hidden="true"><path
        d="M832 64H296c-4.4 0-8 3.6-8 8v56c0 4.4 3.6 8 8 8h496v688c0 4.4 3.6 8 8 8h56c4.4 0 8-3.6 8-8V96c0-17.7-14.3-32-32-32zM704 192H192c-17.7 0-32 14.3-32 32v530.7c0 8.5 3.4 16.6 9.4 22.6l173.3 173.3c2.2 2.2 4.7 4 7.4 5.5v1.9h4.2c3.5 1.3 7.2 2 11 2H704c17.7 0 32-14.3 32-32V224c0-17.7-14.3-32-32-32zM350 856.2L263.9 770H350v86.2zM664 888H414V746c0-22.1-17.9-40-40-40H232V264h432v624z"></path></svg></i></button></pre>
<p>我们的目标获取成绩最大、最小和其他学生的成绩列表，直接通过序列的分解便可快速得到需要的数据：</p>
<pre class="line-numbers  language-python"><code class="python  language-python">min_score<span
        class="token punctuation">,</span> <span class="token operator">*</span>other_scores<span
        class="token punctuation">,</span> max_score <span class="token operator">=</span> scores
<span aria-hidden="true" class="line-numbers-rows"><span></span></span></code><button class="VJbwyy" type="button"
                                                                                      aria-label="复制代码"><i
        aria-label="icon: copy" class="anticon anticon-copy"><svg viewBox="64 64 896 896" focusable="false" class=""
                                                                  data-icon="copy" width="1em" height="1em"
                                                                  fill="currentColor" aria-hidden="true"><path
        d="M832 64H296c-4.4 0-8 3.6-8 8v56c0 4.4 3.6 8 8 8h496v688c0 4.4 3.6 8 8 8h56c4.4 0 8-3.6 8-8V96c0-17.7-14.3-32-32-32zM704 192H192c-17.7 0-32 14.3-32 32v530.7c0 8.5 3.4 16.6 9.4 22.6l173.3 173.3c2.2 2.2 4.7 4 7.4 5.5v1.9h4.2c3.5 1.3 7.2 2 11 2H704c17.7 0 32-14.3 32-32V224c0-17.7-14.3-32-32-32zM350 856.2L263.9 770H350v86.2zM664 888H414V746c0-22.1-17.9-40-40-40H232V264h432v624z"></path></svg></i></button></pre>
<p>这里引入了一种新的写法，*表达式变量 轻松分解出中间的可迭代对象并赋值给other_scores，同时将开头和结束的对象分别赋值给min_score和max_score。</p>
<p>看到这里感觉序列分解似乎有点类似于正则表达式的模式匹配。</p>
<h2>总结</h2>
<p>虽然只是小小的变量值的交换，但本质也是由需求和语言自身特性决定的。学会一些必要的技巧，将会帮助我们写出更高质量的代码。</p>