---
title: "啥是猴子补丁"
date:       2019-11-28
subtitle: "属性在运行时的动态替换"
tags:
	- Python
	- solution
	- interview
---


### Python猴子补丁
推荐阅读：[python自定义对象转json串](https://www.jianshu.com/p/f1060b22aab8)

<blockquote>
    <p>属性在运行时的动态替换，叫做猴子补丁（Monkey Patch）。</p>
</blockquote>
<h1>为什么叫猴子补丁</h1>
<p>属性的运行时替换和猴子也没什么关系，关于猴子补丁的由来网上查到两种说法：</p>
<blockquote>
    <p>1，这个词原来为Guerrilla Patch，杂牌军、游击队，说明这部分不是原装的，在英文里guerilla发音和gorllia(猩猩)相似，再后来就写了monkey(猴子)。<br>
        2，还有一种解释是说由于这种方式将原来的代码弄乱了(messing with it)，在英文里叫monkeying about(顽皮的)，所以叫做Monkey Patch。</p>
</blockquote>
<p>猴子补丁的叫法有些莫名其妙，只要和“模块运行时替换的功能”对应就行了。</p>
<h1>猴子补丁的用法</h1>
<h2>1，运行时动态替换模块的方法</h2>
<p>stackoverflow上有两个比较热的例子，</p>
<blockquote>
    <p>consider a class that has a method get_data. This method does an external lookup (on a database or web
        API, for example), and various other methods in the class call it. However, in a unit test, you don't
        want to depend on the external data source - so you dynamically replace the get_data method with a stub
        that returns some fixed data.<br>
        假设一个类有一个方法get_data。这个方法做一些外部查询（如查询数据库或者Web
        API等），类里面的很多其他方法都调用了它。然而，在一个单元测试中，你不想依赖外部数据源。所以你用哑方法态替换了这个get_data方法，哑方法只返回一些测试数据。</p>
</blockquote>
<p>另一个例子引用了，Zope wiki上对Monkey Patch解释：</p>
<pre class="line-numbers  language-python"><code class="  language-python"><span
        class="token keyword">from</span> SomeOtherProduct<span
        class="token punctuation">.</span>SomeModule <span class="token keyword">import</span> SomeClass

<span class="token keyword">def</span> <span class="token function">speak</span><span class="token punctuation">(</span>self<span
            class="token punctuation">)</span><span class="token punctuation">:</span>
    <span class="token keyword">return</span> <span class="token string">"ook ook eee eee eee!"</span>

SomeClass<span class="token punctuation">.</span>speak <span class="token operator">=</span> speak
<span aria-hidden="true"
      class="line-numbers-rows"><span></span><span></span><span></span><span></span><span></span><span></span></span></code><button
        class="VJbwyy" type="button" aria-label="复制代码"><i aria-label="icon: copy" class="anticon anticon-copy"><svg
        viewBox="64 64 896 896" focusable="false" class="" data-icon="copy" width="1em" height="1em"
        fill="currentColor" aria-hidden="true"><path
        d="M832 64H296c-4.4 0-8 3.6-8 8v56c0 4.4 3.6 8 8 8h496v688c0 4.4 3.6 8 8 8h56c4.4 0 8-3.6 8-8V96c0-17.7-14.3-32-32-32zM704 192H192c-17.7 0-32 14.3-32 32v530.7c0 8.5 3.4 16.6 9.4 22.6l173.3 173.3c2.2 2.2 4.7 4 7.4 5.5v1.9h4.2c3.5 1.3 7.2 2 11 2H704c17.7 0 32-14.3 32-32V224c0-17.7-14.3-32-32-32zM350 856.2L263.9 770H350v86.2zM664 888H414V746c0-22.1-17.9-40-40-40H232V264h432v624z"></path></svg></i></button></pre>
<p>还有一个比较实用的例子，很多代码用到 import json，后来发现ujson性能更高，如果觉得把每个文件的import json 改成 import ujson as
    json成本较高，或者说想测试一下用ujson替换json是否符合预期，只需要在入口加上：</p>
<pre class="line-numbers  language-python"><code class="  language-python"><span
        class="token keyword">import</span> json
<span class="token keyword">import</span> ujson

<span class="token keyword">def</span> <span class="token function">monkey_patch_json</span><span
            class="token punctuation">(</span><span class="token punctuation">)</span><span
            class="token punctuation">:</span>
    json<span class="token punctuation">.</span>__name__ <span class="token operator">=</span> <span
            class="token string">'ujson'</span>
    json<span class="token punctuation">.</span>dumps <span class="token operator">=</span> ujson<span
            class="token punctuation">.</span>dumps
    json<span class="token punctuation">.</span>loads <span class="token operator">=</span> ujson<span
            class="token punctuation">.</span>loads

monkey_patch_json<span class="token punctuation">(</span><span class="token punctuation">)</span>
<span aria-hidden="true"
      class="line-numbers-rows"><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span></span></code><button
        class="VJbwyy" type="button" aria-label="复制代码"><i aria-label="icon: copy" class="anticon anticon-copy"><svg
        viewBox="64 64 896 896" focusable="false" class="" data-icon="copy" width="1em" height="1em"
        fill="currentColor" aria-hidden="true"><path
        d="M832 64H296c-4.4 0-8 3.6-8 8v56c0 4.4 3.6 8 8 8h496v688c0 4.4 3.6 8 8 8h56c4.4 0 8-3.6 8-8V96c0-17.7-14.3-32-32-32zM704 192H192c-17.7 0-32 14.3-32 32v530.7c0 8.5 3.4 16.6 9.4 22.6l173.3 173.3c2.2 2.2 4.7 4 7.4 5.5v1.9h4.2c3.5 1.3 7.2 2 11 2H704c17.7 0 32-14.3 32-32V224c0-17.7-14.3-32-32-32zM350 856.2L263.9 770H350v86.2zM664 888H414V746c0-22.1-17.9-40-40-40H232V264h432v624z"></path></svg></i></button></pre>
<h2>2，运行时动态增加模块的方法</h2>
<p>这种场景也比较多，比如我们引用团队通用库里的一个模块，又想丰富模块的功能，除了继承之外也可以考虑用Monkey Patch。<br>
    个人感觉Monkey Patch带了便利的同时也有搞乱源代码优雅的风险。</p>
<h1>参考：</h1>
<blockquote>
    <p><a href="https://link.jianshu.com?t=http://stackoverflow.com/questions/5626193/what-is-a-monkey-patch"
          target="_blank"
          rel="nofollow">http://stackoverflow.com/questions/5626193/what-is-a-monkey-patch</a><br>
        <a href="https://www.jianshu.com/p/f1060b22aab8"
           target="_blank">http://www.jianshu.com/p/f1060b22aab8</a><br>
        <a href="https://link.jianshu.com?t=http://blog.csdn.net/handsomekang/article/details/40297775"
           target="_blank" rel="nofollow">http://blog.csdn.net/handsomekang/article/details/40297775</a></p>
</blockquote>