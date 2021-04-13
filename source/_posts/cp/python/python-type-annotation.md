---
title: "​Python3新特性：类型注解"
cover: "/img/lynk/46.jpg"
date:       2019-11-28
subtitle: "让你的代码具有灵魂"
tags:
	- Python
	- solution
	- interview
---


<div class="RichText ztext Post-RichText">
    <p>前几天有同学问到，这个写法是什么意思：</p>
    <div class="highlight"><pre><code class="language-python3"><span class="k">def</span> <span
            class="nf">add</span><span class="p">(</span><span class="n">x</span><span class="p">:</span><span
            class="nb">int</span><span class="p">,</span> <span class="n">y</span><span class="p">:</span><span
            class="nb">int</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">int</span><span
            class="p">:</span>
    <span class="k">return</span> <span class="n">x</span> <span class="o">+</span> <span
                class="n">y</span></code></pre>
    </div>
    <p>我们知道 Python 是一种动态语言，变量以及函数的参数是<b>不区分类型</b>。因此我们定义函数只需要这样写就可以了：</p>
    <div class="highlight"><pre><code class="language-python3"><span class="k">def</span> <span
            class="nf">add</span><span class="p">(</span><span class="n">x</span><span class="p">,</span> <span
            class="n">y</span><span class="p">):</span>
    <span class="k">return</span> <span class="n">x</span> <span class="o">+</span> <span
                class="n">y</span></code></pre>
    </div>
    <p>这样的好处是有极大的灵活性，但坏处就是对于别人代码，无法一眼判断出参数的类型，IDE 也无法给出正确的提示。</p>
    <p>于是 Python 3 提供了一个新的特性：<br><b>函数注解</b></p>
    <p>也就是文章开头的这个例子：</p>
    <div class="highlight"><pre><code class="language-python3"><span class="k">def</span> <span
            class="nf">add</span><span class="p">(</span><span class="n">x</span><span class="p">:</span><span
            class="nb">int</span><span class="p">,</span> <span class="n">y</span><span class="p">:</span><span
            class="nb">int</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">int</span><span
            class="p">:</span>
    <span class="k">return</span> <span class="n">x</span> <span class="o">+</span> <span
                class="n">y</span></code></pre>
    </div>
    <p>用 <code>: 类型</code> 的形式指定函数的<b>参数类型</b>，用 <code>-&gt; 类型</code> 的形式指定函数的<b>返回值</b>类型。</p>
    <p>然后特别要强调的是，Python 解释器<b>并不会</b>因为这些注解而提供额外的校验，没有任何的类型检查工作。也就是说，这些类型注解加不加，对你的代码来说<b>没有任何影响</b>：</p>
    <figure data-size="normal">
        <noscript><img src="https://pic4.zhimg.com/v2-9b87d43afdc941929c428b03865037c3_b.jpg" data-caption=""
                       data-size="normal" data-rawwidth="1064" data-rawheight="530"
                       class="origin_image zh-lightbox-thumb" width="1064"
                       data-original="https://pic4.zhimg.com/v2-9b87d43afdc941929c428b03865037c3_r.jpg"/></noscript>
        <img src="https://pic4.zhimg.com/80/v2-9b87d43afdc941929c428b03865037c3_hd.jpg" data-caption=""
             data-size="normal" data-rawwidth="1064" data-rawheight="530" class="origin_image zh-lightbox-thumb lazy"
             width="1064" data-original="https://pic4.zhimg.com/v2-9b87d43afdc941929c428b03865037c3_r.jpg"
             data-actualsrc="https://pic4.zhimg.com/v2-9b87d43afdc941929c428b03865037c3_b.jpg" data-lazy-status="ok">
    </figure>
    <p>输出：</p>
    <figure data-size="normal">
        <noscript><img src="https://pic4.zhimg.com/v2-f00b176bddec7e1d242e3c0e13f30f33_b.jpg" data-caption=""
                       data-size="normal" data-rawwidth="486" data-rawheight="202"
                       class="origin_image zh-lightbox-thumb" width="486"
                       data-original="https://pic4.zhimg.com/v2-f00b176bddec7e1d242e3c0e13f30f33_r.jpg"/></noscript>
        <img src="https://pic4.zhimg.com/80/v2-f00b176bddec7e1d242e3c0e13f30f33_hd.jpg" data-caption=""
             data-size="normal" data-rawwidth="486" data-rawheight="202" class="origin_image zh-lightbox-thumb lazy"
             width="486" data-original="https://pic4.zhimg.com/v2-f00b176bddec7e1d242e3c0e13f30f33_r.jpg"
             data-actualsrc="https://pic4.zhimg.com/v2-f00b176bddec7e1d242e3c0e13f30f33_b.jpg" data-lazy-status="ok">
    </figure>
    <p>但这么做的好处是：</p>
    <ol>
        <li>让别的程序员看得更明白</li>
        <li>让 IDE 了解类型，从而提供更准确的代码提示、补全和语法检查（包括类型检查，可以看到 str 和 float 类型的参数被高亮提示）</li>
    </ol>
    <figure data-size="normal">
        <noscript><img src="https://pic2.zhimg.com/v2-057629e3d59552c856dba7341882ea55_b.jpg" data-caption=""
                       data-size="normal" data-rawwidth="1080" data-rawheight="631"
                       class="origin_image zh-lightbox-thumb" width="1080"
                       data-original="https://pic2.zhimg.com/v2-057629e3d59552c856dba7341882ea55_r.jpg"/></noscript>
        <img src="https://pic2.zhimg.com/80/v2-057629e3d59552c856dba7341882ea55_hd.jpg" data-caption=""
             data-size="normal" data-rawwidth="1080" data-rawheight="631" class="origin_image zh-lightbox-thumb lazy"
             width="1080" data-original="https://pic2.zhimg.com/v2-057629e3d59552c856dba7341882ea55_r.jpg"
             data-actualsrc="https://pic2.zhimg.com/v2-057629e3d59552c856dba7341882ea55_b.jpg" data-lazy-status="ok">
    </figure>
    <p>在函数的 <code>__annotations__</code> 属性中会有你设定的注解：</p>
    <figure data-size="normal">
        <noscript><img src="https://pic1.zhimg.com/v2-9a9f55559930501472752996a3b772a4_b.jpg" data-caption=""
                       data-size="normal" data-rawwidth="1004" data-rawheight="306"
                       class="origin_image zh-lightbox-thumb" width="1004"
                       data-original="https://pic1.zhimg.com/v2-9a9f55559930501472752996a3b772a4_r.jpg"/></noscript>
        <img src="https://pic1.zhimg.com/80/v2-9a9f55559930501472752996a3b772a4_hd.jpg" data-caption=""
             data-size="normal" data-rawwidth="1004" data-rawheight="306" class="origin_image zh-lightbox-thumb lazy"
             width="1004" data-original="https://pic1.zhimg.com/v2-9a9f55559930501472752996a3b772a4_r.jpg"
             data-actualsrc="https://pic1.zhimg.com/v2-9a9f55559930501472752996a3b772a4_b.jpg" data-lazy-status="ok">
    </figure>
    <p>输出：</p>
    <figure data-size="normal">
        <noscript><img src="https://pic4.zhimg.com/v2-35506981e2c4f0e021b4b0902e36441b_b.jpg" data-caption=""
                       data-size="normal" data-rawwidth="1080" data-rawheight="57"
                       class="origin_image zh-lightbox-thumb" width="1080"
                       data-original="https://pic4.zhimg.com/v2-35506981e2c4f0e021b4b0902e36441b_r.jpg"/></noscript>
        <img src="https://pic4.zhimg.com/80/v2-35506981e2c4f0e021b4b0902e36441b_hd.jpg" data-caption=""
             data-size="normal" data-rawwidth="1080" data-rawheight="57" class="origin_image zh-lightbox-thumb lazy"
             width="1080" data-original="https://pic4.zhimg.com/v2-35506981e2c4f0e021b4b0902e36441b_r.jpg"
             data-actualsrc="https://pic4.zhimg.com/v2-35506981e2c4f0e021b4b0902e36441b_b.jpg" data-lazy-status="ok">
    </figure>
    <p>在 Python 3.6 中，又引入了对<b>变量类型</b>进行注解的方法：</p>
    <div class="highlight"><pre><code class="language-python3"><span class="n">a</span><span class="p">:</span> <span
            class="nb">int</span> <span class="o">=</span> <span class="mi">123</span>
<span class="n">b</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s1">'hello'</span></code></pre>
    </div>
    <p>更进一步，如果你需要指明一个全部由整数组成的列表：</p>
    <div class="highlight"><pre><code class="language-python3"><span class="kn">from</span> <span
            class="nn">typing</span> <span class="k">import</span> <span class="n">List</span>
<span class="n">l</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span
                class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="p">[</span><span
                class="mi">1</span><span class="p">,</span> <span class="mi">2</span><span class="p">,</span> <span
                class="mi">3</span><span class="p">]</span></code></pre>
    </div>
    <p>但同样，这些仅仅是“<b>注解</b>”，不会对代码产生任何影响。</p>
    <p>不过，你可以通过 <b>mypy</b> 库来检验最终代码是否符合注解。</p>
    <p>安装 mypy：</p>
    <div class="highlight">
        <pre><code class="language-bash">pip install mypy</code></pre>
    </div>
    <p>执行代码：</p>
    <div class="highlight">
        <pre><code class="language-bash">mypy test.py</code></pre>
    </div>
    <p>如果类型都符合，则不会有任何输出，否则就会给出类似输出：</p>
    <figure data-size="normal">
        <noscript><img src="https://pic4.zhimg.com/v2-57b0ba00b7e95b092ae6fd6acc50eb37_b.jpg" data-caption=""
                       data-size="normal" data-rawwidth="1076" data-rawheight="58"
                       class="origin_image zh-lightbox-thumb" width="1076"
                       data-original="https://pic4.zhimg.com/v2-57b0ba00b7e95b092ae6fd6acc50eb37_r.jpg"/></noscript>
        <img src="https://pic4.zhimg.com/80/v2-57b0ba00b7e95b092ae6fd6acc50eb37_hd.jpg" data-caption=""
             data-size="normal" data-rawwidth="1076" data-rawheight="58" class="origin_image zh-lightbox-thumb lazy"
             width="1076" data-original="https://pic4.zhimg.com/v2-57b0ba00b7e95b092ae6fd6acc50eb37_r.jpg"
             data-actualsrc="https://pic4.zhimg.com/v2-57b0ba00b7e95b092ae6fd6acc50eb37_b.jpg" data-lazy-status="ok">
    </figure>
    <p>这些新特性也许你并不会在代码中使用，不过当你在别人的代码中看到时，请按照对方的约定进行赋值或调用。</p>
    <p>当然，也不排除 Python 以后的版本把类型检查做到解释器里，谁知道呢。</p>
</div>