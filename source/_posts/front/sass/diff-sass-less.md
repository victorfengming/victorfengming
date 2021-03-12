---
title: '关于Sass和less的奇妙故事'
date:       2019-09-23
tags:
	- web
	- solution
	- sass
---

<article class="_2rhmJa"><div class="image-package">
<img src="http://img0.imgtn.bdimg.com/it/u=861104756,4244471114&amp;fm=26&amp;gp=0.jpg" data-original-src="http://img0.imgtn.bdimg.com/it/u=861104756,4244471114&amp;fm=26&amp;gp=0.jpg" data-image-index="0" style="cursor: zoom-in;"><div class="image-caption"></div>
</div>
<h3>起步</h3>
<p>首先sass和less都是css的预编译处理语言，他们引入了mixins，参数，嵌套规则，运算，颜色，名字空间，作用域，JavaScript赋值等 加快了css开发效率,当然这两者都可以配合gulp和grunt等前端构建工具使用</p>
<p>sass和less主要区别:在于实现方式 less是基于JavaScript的在客户端处理 所以安装的时候用npm，sass是基于ruby所以在服务器处理。</p>
<p>很多开发者不会选择LESS因为JavaScript引擎需要额外的时间来处理代码然后输出修改过的CSS到浏览器。关于这个有很多种方式，我选择的是只在开发环节使用LESS。一旦我完成了开发，我就复制然后粘贴LESS输出的到一个压缩器，然后到一个单独的CSS文件来替代LESS文件。另一个选择是使用LESS.app来编译和压缩你的LESS文件。两个选择都将最小化你的样式输出，从而避免由于用户的浏览器不支持JavaScript而可能引起的任何问题。尽管这不大可能，但终归是有可能的</p>
<h3>LESS详细</h3>
<p>首先扩展文件名的格式是 xxx.less</p>
<p>在此推荐大家在练习环节可以用</p>
<pre class="line-numbers  language-xml"><code class="  language-xml"><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>script</span> <span class="token attr-name">src</span><span class="token attr-value"><span class="token punctuation">=</span><span class="token punctuation">"</span>less.js<span class="token punctuation">"</span></span><span class="token attr-name">...</span><span class="token punctuation">&gt;</span></span> 这种方式编译less
<span aria-hidden="true" class="line-numbers-rows"><span></span></span></code></pre>
<p>但在实际项目中 还是用命令行的 lessc xxx.less&gt;xxx.css 方式然后引入编译后的css文件 这样减少在运行时上面出现的问题</p>
<pre class="line-numbers  language-cpp"><code class="  language-cpp">//安装less
npm install -g less
<span aria-hidden="true" class="line-numbers-rows"><span></span><span></span></span></code></pre>
<h5>变量</h5>
<pre class="line-numbers  language-java"><code class="  language-java">@变量名<span class="token operator">:</span>值
<span class="token annotation punctuation">@width</span>：<span class="token number">100</span>px<span class="token punctuation">;</span>
<span class="token punctuation">.</span>box<span class="token punctuation">{</span>
    width<span class="token operator">:</span><span class="token annotation punctuation">@width</span><span class="token punctuation">;</span>
<span class="token punctuation">}</span>
<span aria-hidden="true" class="line-numbers-rows"><span></span><span></span><span></span><span></span><span></span></span></code></pre>
<h5>混合</h5>
<pre class="line-numbers  language-java"><code class="  language-java">定义classa 然后可以将classa引入到classb中
<span class="token punctuation">.</span><span class="token function">classa</span><span class="token punctuation">(</span>a<span class="token punctuation">)</span><span class="token punctuation">{</span>
    width<span class="token operator">:</span><span class="token annotation punctuation">@width</span><span class="token punctuation">;</span>
<span class="token punctuation">}</span>

<span class="token punctuation">.</span>classb<span class="token punctuation">{</span>
    <span class="token punctuation">.</span><span class="token function">classa</span><span class="token punctuation">(</span>a<span class="token punctuation">)</span><span class="token punctuation">;</span>
<span class="token punctuation">}</span>
<span aria-hidden="true" class="line-numbers-rows"><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span></span></code></pre>
<h5>嵌套规则</h5>
<pre class="line-numbers  language-undefined"><code class="  language-undefined">父级{
    子集
}
<span aria-hidden="true" class="line-numbers-rows"><span></span><span></span><span></span></span></code></pre>
<h5>函数和运算</h5>
<pre class="line-numbers  language-ruby"><code class="  language-ruby">可以将值计算
<span class="token variable">@the</span><span class="token operator">-</span>border<span class="token punctuation">:</span> <span class="token number">1</span>px<span class="token punctuation">;</span>
<span class="token variable">@base</span><span class="token operator">-</span>color<span class="token punctuation">:</span> <span class="token comment">#111;</span>
<span class="token variable">@red</span><span class="token punctuation">:</span>        <span class="token comment">#842210;</span>

<span class="token comment">#header {</span>
  color<span class="token punctuation">:</span> <span class="token variable">@base</span><span class="token operator">-</span>color <span class="token operator">*</span> <span class="token number">3</span><span class="token punctuation">;</span>
  border<span class="token operator">-</span>left<span class="token punctuation">:</span> <span class="token variable">@the</span><span class="token operator">-</span>border<span class="token punctuation">;</span>
  border<span class="token operator">-</span>right<span class="token punctuation">:</span> <span class="token variable">@the</span><span class="token operator">-</span>border <span class="token operator">*</span> <span class="token number">2</span><span class="token punctuation">;</span>
<span class="token punctuation">}</span>
<span class="token comment">#footer { </span>
  color<span class="token punctuation">:</span> <span class="token variable">@base</span><span class="token operator">-</span>color <span class="token operator">+</span> <span class="token comment">#003300;</span>
  border<span class="token operator">-</span>color<span class="token punctuation">:</span> desaturate<span class="token punctuation">(</span><span class="token variable">@red</span><span class="token punctuation">,</span> <span class="token number">10</span><span class="token operator">%</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
<span class="token punctuation">}</span>
<span aria-hidden="true" class="line-numbers-rows"><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span></span></code></pre>
<h3>SASS详细</h3>
<p>首件扩展文件名的格式是 xxx.scss 或者是 xxx.sass</p>
<p>使用方法: sass xxx.scss xxx.css</p>
<h5>编译风格：</h5>
<pre class="line-numbers  language-undefined"><code class="  language-undefined">nested:嵌套缩进的css代码，默认
expanded:没有缩紧的,扩展的css代码
campact:简介格式的css代码
compressed:压缩后的css代码(生产环境)
<span aria-hidden="true" class="line-numbers-rows"><span></span><span></span><span></span><span></span></span></code></pre>
<p>使用的时候　sass --style compressed xxx.sass xxx.css</p>
<h5>监听目录</h5>
<pre class="line-numbers  language-cpp"><code class="  language-cpp">sass --watch xxx.scss:xxx.css //监听文件
sass --watch scsspath:csspath //监听文件夹
<span aria-hidden="true" class="line-numbers-rows"><span></span><span></span></span></code></pre>
<h5>变量</h5>
<pre class="line-numbers  language-ruby"><code class="  language-ruby">$变量名<span class="token punctuation">:</span>值
<span class="token variable">$width</span>：<span class="token number">100</span>px<span class="token punctuation">;</span>

<span class="token punctuation">.</span>box<span class="token punctuation">{</span>
    width<span class="token punctuation">:</span><span class="token variable">$width</span><span class="token punctuation">;</span>
<span class="token punctuation">}</span>

如果变量包含字符串则写在 <span class="token comment">#{}之中</span>
<span class="token variable">$c</span><span class="token symbol">:color</span><span class="token punctuation">;</span>

<span class="token punctuation">.</span>box<span class="token punctuation">{</span>
    border<span class="token operator">-</span><span class="token comment">#{$c}:red;</span>
<span class="token punctuation">}</span>
<span aria-hidden="true" class="line-numbers-rows"><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span></span></code></pre>
<h5>嵌套计算</h5>
<p>less和sass嵌套相同，计算同理</p>
<h5>继承</h5>
<p>同less混合相同 定义classa 然后再classb可饮用classa值</p>
<pre class="line-numbers  language-java"><code class="  language-java"><span class="token comment">//使用方法 定义classa </span>
<span class="token punctuation">.</span>classb<span class="token punctuation">{</span>
    <span class="token annotation punctuation">@extend</span> <span class="token punctuation">.</span>classa
<span class="token punctuation">}</span>
<span aria-hidden="true" class="line-numbers-rows"><span></span><span></span><span></span><span></span></span></code></pre>
<h5>Mixin</h5>
<p>即重用代码块</p>
<pre class="line-numbers  language-cpp"><code class="  language-cpp">//使用方法先用@mixin命令定义一个代码块
@mixin left(参数1，参数2){
    float:left;
    margin-left:10px;
}
//使用@include调用刚刚定义的代码块
.box{
    @inclidu left(参数1，参数2);
}
<span aria-hidden="true" class="line-numbers-rows"><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span></span></code></pre>
<h5>颜色函数 lighten(颜色，百分比)</h5>
<h5>插入文件</h5>
<pre class="line-numbers  language-cpp"><code class="  language-cpp">@import命令插入外部文件 .scss和css都可
<span aria-hidden="true" class="line-numbers-rows"><span></span></span></code></pre>
<h5>条件语句</h5>
<pre class="line-numbers  language-bash"><code class="  language-bash">//@if 可以用来判断 @else 则是配套

.box{
    @if 1+1&gt;1 {width:100px;}@else {
        width:200px;
    }
}
<span aria-hidden="true" class="line-numbers-rows"><span></span><span></span><span></span><span></span><span></span><span></span><span></span></span></code></pre>
<h5>循环语句</h5>
<pre class="line-numbers  language-bash"><code class="  language-bash">//@for @while @each

@for $i from 1 to 10{
    border-#{$i}{
        border:#{$i}px solid red;
    }
}

//@while
$i:6;
@while $i&gt;0{
    .item-#{$i}{
        width:2em*$i;
    }
    $i:$i-2;
}

//@each
    @each $member in a, b, c, d {
　　　　.#{$member} {
　　　　　　background-image: url("/image/#{$member}.jpg");
　　　　}
　　}
<span aria-hidden="true" class="line-numbers-rows"><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span></span></code></pre>
<h5>自定义函数</h5>
<pre class="line-numbers  language-css"><code class="  language-css"><span class="token atrule"><span class="token rule">@function</span> <span class="token function">name</span><span class="token punctuation">(</span>$n<span class="token punctuation">)</span></span><span class="token punctuation">{</span>
    <span class="token atrule"><span class="token rule">@return</span> $n*2<span class="token punctuation">;</span></span>
<span class="token punctuation">}</span>

<span class="token selector">.box</span><span class="token punctuation">{</span>
    <span class="token property">width</span><span class="token punctuation">:</span><span class="token function">name</span><span class="token punctuation">(</span>value<span class="token punctuation">)</span><span class="token punctuation">;</span>
<span class="token punctuation">}</span>
<span aria-hidden="true" class="line-numbers-rows"><span></span><span></span><span></span><span></span><span></span><span></span><span></span></span></code></pre>
<h3>总结</h3>
<p>总体来说sass和less都有各自的好处，这要根据每个开发者的习惯和爱好来使用，都可提高开发效率，当然还有stylus等工具，因为目前未使用过所以不做评判，个人比较倾向sass，至于比较，两者都有其优缺点，如果你开发环境中并没有ruby 并且你不想安装ruby 你就可以使用less，如果你觉得sass的语法你更倾向并且你安装了ruby 你就可以使用sass。总之工具不重要，码出一手好代码才是真理。</p>
</article>