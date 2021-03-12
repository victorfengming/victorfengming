---
title: 'Sass、LESS 和 Stylus区别总结'
cover: "/img/lynk/62.jpg"
date:       2019-09-23
tags:
	- web
	- solution
	- sass
	- summer
---

<div id="content_views" class="markdown_views">
                    <!-- flowchart 箭头图标 勿删 -->
                    <svg xmlns="http://www.w3.org/2000/svg" style="display: none;">
                        <path stroke-linecap="round" d="M5,0 0,2.5 5,5z" id="raphael-marker-block" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);"></path>
                    </svg>
                                            <p>CSS 预处理器技术已经非常的成熟了，而且也涌现出了越来越多的 CSS 的预处理器框架。本文便总结下 Sass、Less CSS、Stylus这三个预处理器的区别和各自的基本语法。</p>



<h2 id="1什么是-css-预处理器"><a name="t0"></a>1.什么是 CSS 预处理器</h2>

<p>CSS 预处理器是一种语言用来为 CSS 增加一些编程的的特性，无需考虑浏览器的兼容性问题，例如你可以在 CSS 中使用变量、简单的程序逻辑、函数等等在编程语言中的一些基本技巧，可以让CSS 更见简洁，适应性更强，代码更直观等诸多好处。</p>



<h2 id="2基本语法区别"><a name="t1"></a>2.基本语法区别:</h2>

<p>在使用 CSS 预处理器之前最重要的是理解语法，幸运的是基本上大多数预处理器的语法跟 CSS 都差不多。</p>

<p>首先 Sass 和 Less 都使用的是标准的 CSS 语法，因此如果可以很方便的将已有的 CSS 代码转为预处理器代码，默认 Sass 使用 .sass 扩展名，而 Less 使用 .less 扩展名。</p>



<pre class="prettyprint" name="code"><code class="hljs css has-numbering" onclick="mdcp.signin(event)" style="position: unset;"><span class="hljs-comment">/* style.scss or style.less */</span>
<span class="hljs-tag">h1</span> <span class="hljs-rules">{
  <span class="hljs-rule"><span class="hljs-attribute">color</span>:<span class="hljs-value"> <span class="hljs-hexcolor">#0982C1</span></span></span>;
<span class="hljs-rule">}</span></span><div class="hljs-button signin" data-title="登录后复制"></div></code><ul class="pre-numbering" style=""><li style="color: rgb(153, 153, 153);">1</li><li style="color: rgb(153, 153, 153);">2</li><li style="color: rgb(153, 153, 153);">3</li><li style="color: rgb(153, 153, 153);">4</li></ul></pre>

<p>这是一个再普通不过的，不过 Sass 同时也支持老的语法，就是不包含花括号和分号的方式：</p>



<pre class="prettyprint" name="code"><code class="hljs rsl has-numbering" onclick="mdcp.signin(event)" style="position: unset;"><span class="hljs-comment">/* style.sass */</span>
h1
  <span class="hljs-keyword">color</span>: <span class="hljs-preprocessor">#0982c1</span><div class="hljs-button signin" data-title="登录后复制"></div></code><ul class="pre-numbering" style=""><li style="color: rgb(153, 153, 153);">1</li><li style="color: rgb(153, 153, 153);">2</li><li style="color: rgb(153, 153, 153);">3</li></ul></pre>

<p>而 Stylus 支持的语法要更多样性一点，它默认使用 .styl 的文件扩展名，下面是 Stylus 支持的语法：</p>



<pre class="prettyprint" name="code"><code class="hljs css has-numbering" onclick="mdcp.signin(event)" style="position: unset;"><span class="hljs-comment">/* style.styl */</span>
<span class="hljs-tag">h1</span> <span class="hljs-rules">{
  <span class="hljs-rule"><span class="hljs-attribute">color</span>:<span class="hljs-value"> <span class="hljs-hexcolor">#0982C1</span></span></span>;
<span class="hljs-rule">}</span></span>

<span class="hljs-comment">/* omit brackets */</span>
<span class="hljs-tag">h1</span>
  <span class="hljs-tag">color</span>: <span class="hljs-id">#0982C1</span>;

<span class="hljs-comment">/* omit colons and semi-colons */</span>
<span class="hljs-tag">h1</span>
  <span class="hljs-tag">color</span> <span class="hljs-id">#0982C1</span><div class="hljs-button signin" data-title="登录后复制"></div></code><ul class="pre-numbering" style=""><li style="color: rgb(153, 153, 153);">1</li><li style="color: rgb(153, 153, 153);">2</li><li style="color: rgb(153, 153, 153);">3</li><li style="color: rgb(153, 153, 153);">4</li><li style="color: rgb(153, 153, 153);">5</li><li style="color: rgb(153, 153, 153);">6</li><li style="color: rgb(153, 153, 153);">7</li><li style="color: rgb(153, 153, 153);">8</li><li style="color: rgb(153, 153, 153);">9</li><li style="color: rgb(153, 153, 153);">10</li><li style="color: rgb(153, 153, 153);">11</li><li style="color: rgb(153, 153, 153);">12</li></ul></pre>

<p>可以在同一个样式单中使用不同的变量，例如下面的写法也不会报错：</p>



<pre class="prettyprint" name="code"><code class="hljs rsl has-numbering" onclick="mdcp.signin(event)" style="position: unset;">h1 {
  <span class="hljs-keyword">color</span> <span class="hljs-preprocessor">#0982c1</span>
}
h2
  font-size: <span class="hljs-number">1.2</span>em<div class="hljs-button signin" data-title="登录后复制"></div></code><ul class="pre-numbering" style=""><li style="color: rgb(153, 153, 153);">1</li><li style="color: rgb(153, 153, 153);">2</li><li style="color: rgb(153, 153, 153);">3</li><li style="color: rgb(153, 153, 153);">4</li><li style="color: rgb(153, 153, 153);">5</li></ul></pre>



<h2 id="3变量"><a name="t2"></a>3.变量</h2>

<p><strong>1. sass：</strong></p>

<p>Sass让人们受益的一个重要特性就是它为css引入了变量。你可以把反复使用的css属性值 定义成变量，然后通过变量名来引用它们，而无需重复书写这一属性值。</p>

<pre class="prettyprint"><code class="has-numbering" onclick="mdcp.signin(event)" style="position: unset;">     sass变量必须是以$开头的，然后变量和值之间使用冒号（：）隔开，和css属性是一样的，例如：
<div class="hljs-button signin" data-title="登录后复制"></div></code><ul class="pre-numbering" style=""><li style="color: rgb(153, 153, 153);">1</li></ul></pre>

<pre class="prettyprint" name="code"><code class="hljs css has-numbering" onclick="mdcp.signin(event)" style="position: unset;">$<span class="hljs-tag">maincolor</span> : <span class="hljs-id">#092873</span>;
$<span class="hljs-tag">siteWidth</span> : 1024<span class="hljs-tag">px</span>;
$<span class="hljs-tag">borderStyle</span> : <span class="hljs-tag">dotted</span>;
<span class="hljs-tag">body</span> <span class="hljs-rules">{
  <span class="hljs-rule"><span class="hljs-attribute">color</span>:<span class="hljs-value"> $maincolor</span></span>;
  <span class="hljs-rule"><span class="hljs-attribute">border</span>:<span class="hljs-value"> <span class="hljs-number">1</span>px $borderStyle $mainColor</span></span>;
  <span class="hljs-rule"><span class="hljs-attribute">max-width</span>:<span class="hljs-value"> $siteWidth</span></span>;
<span class="hljs-rule">}</span></span><div class="hljs-button signin" data-title="登录后复制"></div></code><ul class="pre-numbering" style=""><li style="color: rgb(153, 153, 153);">1</li><li style="color: rgb(153, 153, 153);">2</li><li style="color: rgb(153, 153, 153);">3</li><li style="color: rgb(153, 153, 153);">4</li><li style="color: rgb(153, 153, 153);">5</li><li style="color: rgb(153, 153, 153);">6</li><li style="color: rgb(153, 153, 153);">7</li><li style="color: rgb(153, 153, 153);">8</li></ul></pre>

<p><strong>2.less css ：</strong></p>

<p>在less文件中，当一个值需要反复使用时，可以通过@符号定义变量。已经被赋值的变量以及其他的常量（如像素、颜色等）都可以参与运算。</p>

<pre class="prettyprint"><code class="has-numbering" onclick="mdcp.signin(event)" style="position: unset;"> Less css中变量都是用@开头的，其余与sass都是一样的，例如：
<div class="hljs-button signin" data-title="登录后复制"></div></code><ul class="pre-numbering" style=""><li style="color: rgb(153, 153, 153);">1</li></ul></pre>

<pre class="prettyprint" name="code"><code class="hljs css has-numbering" onclick="mdcp.signin(event)" style="position: unset;"><span class="hljs-at_rule">@<span class="hljs-keyword">maincolor</span> : #<span class="hljs-number">092873</span></span>;
<span class="hljs-at_rule">@<span class="hljs-keyword">siteWidth</span> : <span class="hljs-number">1024</span>px</span>;
<span class="hljs-at_rule">@<span class="hljs-keyword">borderStyle</span> : dotted</span>;
<span class="hljs-tag">body</span> <span class="hljs-rules">{
  <span class="hljs-rule"><span class="hljs-attribute">color</span>:<span class="hljs-value"> @maincolor</span></span>;
  <span class="hljs-rule"><span class="hljs-attribute">border</span>:<span class="hljs-value"> <span class="hljs-number">1</span>px @borderStyle @mainColor</span></span>;
  <span class="hljs-rule"><span class="hljs-attribute">max-width</span>:<span class="hljs-value"> @siteWidth</span></span>;
<span class="hljs-rule">}</span></span><div class="hljs-button signin" data-title="登录后复制"></div></code><ul class="pre-numbering" style=""><li style="color: rgb(153, 153, 153);">1</li><li style="color: rgb(153, 153, 153);">2</li><li style="color: rgb(153, 153, 153);">3</li><li style="color: rgb(153, 153, 153);">4</li><li style="color: rgb(153, 153, 153);">5</li><li style="color: rgb(153, 153, 153);">6</li><li style="color: rgb(153, 153, 153);">7</li><li style="color: rgb(153, 153, 153);">8</li></ul></pre>

<p><strong>3.stylus：</strong></p>

<pre class="prettyprint"><code class="has-numbering" onclick="mdcp.signin(event)" style="position: unset;"> stylus对变量是没有任何设定的，可以是以$开头，或者任何的字符，而且与变量之间可以用冒号，空格隔开，
 但是在stylus中不能用@开头，例如：    
<div class="hljs-button signin" data-title="登录后复制"></div></code><ul class="pre-numbering" style=""><li style="color: rgb(153, 153, 153);">1</li><li style="color: rgb(153, 153, 153);">2</li></ul></pre>

<pre class="prettyprint" name="code"><code class="hljs rsl has-numbering" onclick="mdcp.signin(event)" style="position: unset;">maincolor = <span class="hljs-preprocessor">#092873</span>
siteWidth = <span class="hljs-number">1024</span>px
borderStyle = dotted
body 
  <span class="hljs-keyword">color</span> maincolor
  border <span class="hljs-number">1</span>px borderStyle mainColor
  <span class="hljs-built_in">max</span>-width siteWidth<div class="hljs-button signin" data-title="登录后复制"></div></code><ul class="pre-numbering" style=""><li style="color: rgb(153, 153, 153);">1</li><li style="color: rgb(153, 153, 153);">2</li><li style="color: rgb(153, 153, 153);">3</li><li style="color: rgb(153, 153, 153);">4</li><li style="color: rgb(153, 153, 153);">5</li><li style="color: rgb(153, 153, 153);">6</li><li style="color: rgb(153, 153, 153);">7</li></ul></pre>

<p>以上三种写法都如同一下这种css：</p>

<pre class="prettyprint" name="code"><code class="hljs css has-numbering" onclick="mdcp.signin(event)" style="position: unset;"><span class="hljs-tag">body</span> <span class="hljs-rules">{
  <span class="hljs-rule"><span class="hljs-attribute">color</span>:<span class="hljs-value"> <span class="hljs-hexcolor">#092873</span></span></span>;
  <span class="hljs-rule"><span class="hljs-attribute">border</span>:<span class="hljs-value"> <span class="hljs-number">1</span>px dotted <span class="hljs-hexcolor">#092873</span></span></span>;
  <span class="hljs-rule"><span class="hljs-attribute">max-width</span>:<span class="hljs-value"> <span class="hljs-number">1024</span>px</span></span>;
<span class="hljs-rule">}</span></span><div class="hljs-button signin" data-title="登录后复制"></div></code><ul class="pre-numbering" style=""><li style="color: rgb(153, 153, 153);">1</li><li style="color: rgb(153, 153, 153);">2</li><li style="color: rgb(153, 153, 153);">3</li><li style="color: rgb(153, 153, 153);">4</li><li style="color: rgb(153, 153, 153);">5</li></ul></pre>

<p>这样做的好处也是显而易见的，在修改多处相同颜色的时候，这时就只需要修改变量值即可。</p>

<h2 id="4嵌套"><a name="t3"></a>4.嵌套</h2>

<p>如果我们需要在CSS中相同的 parent 引用多个元素，这将是非常乏味的，你需要一遍又一遍地写 parent。例如：</p>



<pre class="prettyprint" name="code"><code class="hljs css has-numbering" onclick="mdcp.signin(event)" style="position: unset;"><span class="hljs-tag">div</span> <span class="hljs-rules">{
  <span class="hljs-rule"><span class="hljs-attribute">margin</span>:<span class="hljs-value"> <span class="hljs-number">10</span>px</span></span>;
<span class="hljs-rule">}</span></span>
<span class="hljs-tag">div</span> <span class="hljs-tag">nav</span> <span class="hljs-rules">{
  <span class="hljs-rule"><span class="hljs-attribute">height</span>:<span class="hljs-value"> <span class="hljs-number">25</span>px</span></span>;
<span class="hljs-rule">}</span></span>
<span class="hljs-tag">div</span> <span class="hljs-tag">nav</span> <span class="hljs-tag">a</span> <span class="hljs-rules">{
  <span class="hljs-rule"><span class="hljs-attribute">color</span>:<span class="hljs-value"> <span class="hljs-hexcolor">#0982C1</span></span></span>;
<span class="hljs-rule">}</span></span>
<span class="hljs-tag">div</span> <span class="hljs-tag">nav</span> <span class="hljs-tag">a</span><span class="hljs-pseudo">:hover</span> <span class="hljs-rules">{
  <span class="hljs-rule"><span class="hljs-attribute">text-decoration</span>:<span class="hljs-value"> underline</span></span>;
<span class="hljs-rule">}</span></span><div class="hljs-button signin" data-title="登录后复制"></div></code><ul class="pre-numbering" style=""><li style="color: rgb(153, 153, 153);">1</li><li style="color: rgb(153, 153, 153);">2</li><li style="color: rgb(153, 153, 153);">3</li><li style="color: rgb(153, 153, 153);">4</li><li style="color: rgb(153, 153, 153);">5</li><li style="color: rgb(153, 153, 153);">6</li><li style="color: rgb(153, 153, 153);">7</li><li style="color: rgb(153, 153, 153);">8</li><li style="color: rgb(153, 153, 153);">9</li><li style="color: rgb(153, 153, 153);">10</li><li style="color: rgb(153, 153, 153);">11</li><li style="color: rgb(153, 153, 153);">12</li></ul></pre>

<p>如果用 CSS 预处理器，就可以少写很多单词，而且父子节点关系一目了然，并且sass，Less，stylus都支持下面这样的写法，且都是相同的：</p>



<pre class="prettyprint" name="code"><code class="hljs scss has-numbering" onclick="mdcp.signin(event)" style="position: unset;"><span class="hljs-comment">//scss style //----------------------------------- </span>
<span class="hljs-tag">nav</span> { 
    <span class="hljs-tag">ul</span> { 
       <span class="hljs-attribute">margin</span><span class="hljs-value">: <span class="hljs-number">0</span>;</span> 
       <span class="hljs-attribute">padding</span><span class="hljs-value">: <span class="hljs-number">0</span>;</span> 
    } 
    <span class="hljs-tag">li</span> { 
       <span class="hljs-attribute">display</span><span class="hljs-value">: inline-block;</span> 
    } 
    <span class="hljs-tag">a</span> { 
       <span class="hljs-attribute">display</span><span class="hljs-value">: block;</span> 
       <span class="hljs-attribute">padding</span><span class="hljs-value">: <span class="hljs-number">6</span>px <span class="hljs-number">12</span>px;</span> 
       <span class="hljs-attribute">text-decoration</span><span class="hljs-value">: none;</span> 
    } 
}
<span class="hljs-comment">//css style //----------------------------------- </span>
<span class="hljs-tag">nav</span> <span class="hljs-tag">ul</span> { 
    <span class="hljs-attribute">margin</span><span class="hljs-value">: <span class="hljs-number">0</span>;</span> 
    <span class="hljs-attribute">padding</span><span class="hljs-value">: <span class="hljs-number">0</span>;</span> 
    <span class="hljs-attribute">list-style</span><span class="hljs-value">: none;</span> 
} 
<span class="hljs-tag">nav</span> <span class="hljs-tag">li</span> { 
    <span class="hljs-attribute">display</span><span class="hljs-value">: inline-block;</span> 
} 
<span class="hljs-tag">nav</span> <span class="hljs-tag">a</span> { 
    <span class="hljs-attribute">display</span><span class="hljs-value">: block;</span> 
    <span class="hljs-attribute">padding</span><span class="hljs-value">: <span class="hljs-number">6</span>px <span class="hljs-number">12</span>px;</span> 
    <span class="hljs-attribute">text-decoration</span><span class="hljs-value">: none;</span> 
}<div class="hljs-button signin" data-title="登录后复制"></div></code><ul class="pre-numbering" style=""><li style="color: rgb(153, 153, 153);">1</li><li style="color: rgb(153, 153, 153);">2</li><li style="color: rgb(153, 153, 153);">3</li><li style="color: rgb(153, 153, 153);">4</li><li style="color: rgb(153, 153, 153);">5</li><li style="color: rgb(153, 153, 153);">6</li><li style="color: rgb(153, 153, 153);">7</li><li style="color: rgb(153, 153, 153);">8</li><li style="color: rgb(153, 153, 153);">9</li><li style="color: rgb(153, 153, 153);">10</li><li style="color: rgb(153, 153, 153);">11</li><li style="color: rgb(153, 153, 153);">12</li><li style="color: rgb(153, 153, 153);">13</li><li style="color: rgb(153, 153, 153);">14</li><li style="color: rgb(153, 153, 153);">15</li><li style="color: rgb(153, 153, 153);">16</li><li style="color: rgb(153, 153, 153);">17</li><li style="color: rgb(153, 153, 153);">18</li><li style="color: rgb(153, 153, 153);">19</li><li style="color: rgb(153, 153, 153);">20</li><li style="color: rgb(153, 153, 153);">21</li><li style="color: rgb(153, 153, 153);">22</li><li style="color: rgb(153, 153, 153);">23</li><li style="color: rgb(153, 153, 153);">24</li><li style="color: rgb(153, 153, 153);">25</li><li style="color: rgb(153, 153, 153);">26</li><li style="color: rgb(153, 153, 153);">27</li><li style="color: rgb(153, 153, 153);">28</li><li style="color: rgb(153, 153, 153);">29</li></ul></pre>

<p>这样做是非常方便的，也很直观。</p>

<h2 id="5运算符"><a name="t4"></a>5.运算符</h2>

<p>在 CSS 预处理器中还是可以进行样式的计算如下：</p>

<pre class="prettyprint" name="code"><code class="hljs css has-numbering" onclick="mdcp.signin(event)" style="position: unset;"><span class="hljs-tag">body</span> <span class="hljs-rules">{
  <span class="hljs-rule"><span class="hljs-attribute">margin</span>:<span class="hljs-value"> (<span class="hljs-number">14</span>px/<span class="hljs-number">2</span>)</span></span>;
  <span class="hljs-rule"><span class="hljs-attribute">top</span>:<span class="hljs-value"> <span class="hljs-number">50</span>px + <span class="hljs-number">100</span>px</span></span>;
  <span class="hljs-rule"><span class="hljs-attribute">right</span>:<span class="hljs-value"> <span class="hljs-number">80</span> * <span class="hljs-number">10</span>%</span></span>;
<span class="hljs-rule">}</span></span><div class="hljs-button signin" data-title="登录后复制"></div></code><ul class="pre-numbering" style=""><li style="color: rgb(153, 153, 153);">1</li><li style="color: rgb(153, 153, 153);">2</li><li style="color: rgb(153, 153, 153);">3</li><li style="color: rgb(153, 153, 153);">4</li><li style="color: rgb(153, 153, 153);">5</li></ul></pre>

<p>在sass，Less与stylus中都是可以这样做的。</p>

<h2 id="6颜色函数"><a name="t5"></a>6.颜色函数</h2>

<p>CSS 预处理器一般都会内置一些颜色处理函数用来对颜色值进行处理，例如加亮、变暗、颜色梯度等。</p>

<p><strong>1.sass的颜色处理函数：</strong></p>

<pre class="prettyprint" name="code"><code class="hljs mel has-numbering" onclick="mdcp.signin(event)" style="position: unset;">lighten(<span class="hljs-variable">$color</span>, <span class="hljs-number">10</span><span class="hljs-variable">%)</span>; 
darken(<span class="hljs-variable">$color</span>, <span class="hljs-number">10</span><span class="hljs-variable">%)</span>;  
saturate(<span class="hljs-variable">$color</span>, <span class="hljs-number">10</span><span class="hljs-variable">%)</span>;   
desaturate(<span class="hljs-variable">$color</span>, <span class="hljs-number">10</span><span class="hljs-variable">%)</span>;
grayscale(<span class="hljs-variable">$color</span>);  
complement(<span class="hljs-variable">$color</span>); 
invert(<span class="hljs-variable">$color</span>); 
mix(<span class="hljs-variable">$color1</span>, <span class="hljs-variable">$color2</span>, <span class="hljs-number">50</span><span class="hljs-variable">%)</span>; <div class="hljs-button signin" data-title="登录后复制"></div></code><ul class="pre-numbering" style=""><li style="color: rgb(153, 153, 153);">1</li><li style="color: rgb(153, 153, 153);">2</li><li style="color: rgb(153, 153, 153);">3</li><li style="color: rgb(153, 153, 153);">4</li><li style="color: rgb(153, 153, 153);">5</li><li style="color: rgb(153, 153, 153);">6</li><li style="color: rgb(153, 153, 153);">7</li><li style="color: rgb(153, 153, 153);">8</li></ul></pre>

<p>实例如下：</p>

<pre class="prettyprint" name="code"><code class="hljs css has-numbering" onclick="mdcp.signin(event)" style="position: unset;">$<span class="hljs-tag">color</span>: <span class="hljs-id">#0982C1</span>;
<span class="hljs-tag">h1</span> <span class="hljs-rules">{
  <span class="hljs-rule"><span class="hljs-attribute">background</span>:<span class="hljs-value"> $color</span></span>;
  <span class="hljs-rule"><span class="hljs-attribute">border</span>:<span class="hljs-value"> <span class="hljs-number">3</span>px solid <span class="hljs-function">darken($color, <span class="hljs-number">50</span>%)</span></span></span>;
<span class="hljs-rule">}</span></span><div class="hljs-button signin" data-title="登录后复制"></div></code><ul class="pre-numbering" style=""><li style="color: rgb(153, 153, 153);">1</li><li style="color: rgb(153, 153, 153);">2</li><li style="color: rgb(153, 153, 153);">3</li><li style="color: rgb(153, 153, 153);">4</li><li style="color: rgb(153, 153, 153);">5</li></ul></pre>

<p><strong>2.Less css颜色处理函数：</strong></p>

<pre class="prettyprint" name="code"><code class="hljs css has-numbering" onclick="mdcp.signin(event)" style="position: unset;"><span class="hljs-tag">lighten</span>(<span class="hljs-at_rule">@<span class="hljs-keyword">color,</span> <span class="hljs-number">10</span>%)</span>; 
<span class="hljs-tag">darken</span>(<span class="hljs-at_rule">@<span class="hljs-keyword">color,</span> <span class="hljs-number">10</span>%)</span>;  
<span class="hljs-tag">saturate</span>(<span class="hljs-at_rule">@<span class="hljs-keyword">color,</span> <span class="hljs-number">10</span>%)</span>;  
<span class="hljs-tag">desaturate</span>(<span class="hljs-at_rule">@<span class="hljs-keyword">color,</span> <span class="hljs-number">10</span>%)</span>; 
<span class="hljs-tag">spin</span>(<span class="hljs-at_rule">@<span class="hljs-keyword">color,</span> <span class="hljs-number">10</span>)</span>; 
<span class="hljs-tag">spin</span>(<span class="hljs-at_rule">@<span class="hljs-keyword">color,</span> -<span class="hljs-number">10</span>)</span>; 
<span class="hljs-tag">mix</span>(<span class="hljs-at_rule">@<span class="hljs-keyword">color1,</span> @color2)</span>;<div class="hljs-button signin" data-title="登录后复制"></div></code><ul class="pre-numbering" style=""><li style="color: rgb(153, 153, 153);">1</li><li style="color: rgb(153, 153, 153);">2</li><li style="color: rgb(153, 153, 153);">3</li><li style="color: rgb(153, 153, 153);">4</li><li style="color: rgb(153, 153, 153);">5</li><li style="color: rgb(153, 153, 153);">6</li><li style="color: rgb(153, 153, 153);">7</li></ul></pre>

<p>示例如下：</p>

<pre class="prettyprint" name="code"><code class="hljs css has-numbering" onclick="mdcp.signin(event)" style="position: unset;"><span class="hljs-at_rule">@<span class="hljs-keyword">color:</span> #<span class="hljs-number">0982</span>C1</span>;
<span class="hljs-tag">h1</span> <span class="hljs-rules">{
  <span class="hljs-rule"><span class="hljs-attribute">background</span>:<span class="hljs-value"> @color</span></span>;
  <span class="hljs-rule"><span class="hljs-attribute">border</span>:<span class="hljs-value"> <span class="hljs-number">3</span>px solid <span class="hljs-function">darken(@color, <span class="hljs-number">50</span>%)</span></span></span>;
<span class="hljs-rule">}</span></span><div class="hljs-button signin" data-title="登录后复制"></div></code><ul class="pre-numbering" style=""><li style="color: rgb(153, 153, 153);">1</li><li style="color: rgb(153, 153, 153);">2</li><li style="color: rgb(153, 153, 153);">3</li><li style="color: rgb(153, 153, 153);">4</li><li style="color: rgb(153, 153, 153);">5</li></ul></pre>

<p><strong>3.Stylus颜色处理函数：</strong></p>

<pre class="prettyprint" name="code"><code class="hljs mel has-numbering" onclick="mdcp.signin(event)" style="position: unset;">lighten(<span class="hljs-keyword">color</span>, <span class="hljs-number">10</span><span class="hljs-variable">%)</span>; 
darken(<span class="hljs-keyword">color</span>, <span class="hljs-number">10</span><span class="hljs-variable">%)</span>;  
saturate(<span class="hljs-keyword">color</span>, <span class="hljs-number">10</span><span class="hljs-variable">%)</span>;  
desaturate(<span class="hljs-keyword">color</span>, <span class="hljs-number">10</span><span class="hljs-variable">%)</span>; <div class="hljs-button signin" data-title="登录后复制"></div></code><ul class="pre-numbering" style=""><li style="color: rgb(153, 153, 153);">1</li><li style="color: rgb(153, 153, 153);">2</li><li style="color: rgb(153, 153, 153);">3</li><li style="color: rgb(153, 153, 153);">4</li></ul></pre>

<p>示例如下;</p>

<pre class="prettyprint" name="code"><code class="hljs rsl has-numbering" onclick="mdcp.signin(event)" style="position: unset;"><span class="hljs-keyword">color</span> = <span class="hljs-preprocessor">#0982C1 </span>
h1
  background <span class="hljs-keyword">color</span>
  border <span class="hljs-number">3</span>px solid darken(<span class="hljs-keyword">color</span>, <span class="hljs-number">50</span>%)<div class="hljs-button signin" data-title="登录后复制"></div></code><ul class="pre-numbering" style=""><li style="color: rgb(153, 153, 153);">1</li><li style="color: rgb(153, 153, 153);">2</li><li style="color: rgb(153, 153, 153);">3</li><li style="color: rgb(153, 153, 153);">4</li></ul></pre>

<h2 id="7导入-import"><a name="t6"></a>7.导入 (Import)</h2>

<p>很多 CSS 开发者对导入的做法都不太感冒，因为它需要多次的 HTTP 请求。但是在 CSS 预处理器中的导入操作则不同，它只是在语义上包含了不同的文件，但最终结果是一个单一的 CSS 文件，如果你是通过 @ import “file.css”; 导入 CSS 文件，那效果跟普通的 CSS 导入一样。</p>

<p><strong>注意：</strong>导入文件中定义的混入、变量等信息也将会被引入到主样式文件中，因此需要避免它们互相冲突。 <br>
例如： <br>
1.css:</p>

<pre class="prettyprint" name="code"><code class="hljs scss has-numbering" onclick="mdcp.signin(event)" style="position: unset;"><span class="hljs-comment">//1.css</span>
<span class="hljs-comment">/* file.{type} */</span>
<span class="hljs-tag">body</span> {
  <span class="hljs-attribute">background</span><span class="hljs-value">: <span class="hljs-hexcolor">#000</span>;</span>
}<div class="hljs-button signin" data-title="登录后复制"></div></code><ul class="pre-numbering" style=""><li style="color: rgb(153, 153, 153);">1</li><li style="color: rgb(153, 153, 153);">2</li><li style="color: rgb(153, 153, 153);">3</li><li style="color: rgb(153, 153, 153);">4</li><li style="color: rgb(153, 153, 153);">5</li></ul></pre>

<p>2.XXX:</p>



<pre class="prettyprint" name="code"><code class="hljs css has-numbering" onclick="mdcp.signin(event)" style="position: unset;"><span class="hljs-at_rule">@ import <span class="hljs-string">"1.css"</span></span>;
<span class="hljs-at_rule">@ import <span class="hljs-string">"file.{type}"</span></span>;

<span class="hljs-tag">p</span> <span class="hljs-rules">{
  <span class="hljs-rule"><span class="hljs-attribute">background</span>:<span class="hljs-value"> <span class="hljs-hexcolor">#092873</span></span></span>;
<span class="hljs-rule">}</span></span><div class="hljs-button signin" data-title="登录后复制"></div></code><ul class="pre-numbering" style=""><li style="color: rgb(153, 153, 153);">1</li><li style="color: rgb(153, 153, 153);">2</li><li style="color: rgb(153, 153, 153);">3</li><li style="color: rgb(153, 153, 153);">4</li><li style="color: rgb(153, 153, 153);">5</li><li style="color: rgb(153, 153, 153);">6</li></ul></pre>

<p>最终生成的 CSS：</p>

<pre class="prettyprint" name="code"><code class="hljs css has-numbering" onclick="mdcp.signin(event)" style="position: unset;"><span class="hljs-at_rule">@ import <span class="hljs-string">"1.css"</span></span>;
<span class="hljs-tag">body</span> <span class="hljs-rules">{
  <span class="hljs-rule"><span class="hljs-attribute">background</span>:<span class="hljs-value"> <span class="hljs-hexcolor">#000</span></span></span>;
<span class="hljs-rule">}</span></span>
<span class="hljs-tag">p</span> <span class="hljs-rules">{
  <span class="hljs-rule"><span class="hljs-attribute">background</span>:<span class="hljs-value"> <span class="hljs-hexcolor">#092873</span></span></span>;
<span class="hljs-rule">}</span></span><div class="hljs-button signin" data-title="登录后复制"></div></code><ul class="pre-numbering" style=""><li style="color: rgb(153, 153, 153);">1</li><li style="color: rgb(153, 153, 153);">2</li><li style="color: rgb(153, 153, 153);">3</li><li style="color: rgb(153, 153, 153);">4</li><li style="color: rgb(153, 153, 153);">5</li><li style="color: rgb(153, 153, 153);">6</li><li style="color: rgb(153, 153, 153);">7</li></ul></pre>

<h2 id="8继承"><a name="t7"></a>8.继承</h2>

<p>当我们需要为多个元素定义相同样式的时候，我们可以考虑使用继承的做法.</p>

<p><strong>1.sass：</strong> <br>
sass可通过@extend来实现代码组合声明，使代码更加优越简洁。</p>



<pre class="prettyprint" name="code"><code class="hljs scss has-numbering" onclick="mdcp.signin(event)" style="position: unset;"><span class="hljs-class">.message</span> {
  <span class="hljs-attribute">border</span><span class="hljs-value">: <span class="hljs-number">1</span>px solid <span class="hljs-hexcolor">#ccc</span>;</span>
  <span class="hljs-attribute">padding</span><span class="hljs-value">: <span class="hljs-number">10</span>px;</span>
  <span class="hljs-attribute">color</span><span class="hljs-value">: <span class="hljs-hexcolor">#333</span>;</span>
}
<span class="hljs-class">.success</span> {
  <span class="hljs-at_rule">@<span class="hljs-keyword">extend</span><span class="hljs-preprocessor"> .message</span>;</span>
  <span class="hljs-attribute">border-color</span><span class="hljs-value">: green;</span>
}
<span class="hljs-class">.error</span> {
  <span class="hljs-at_rule">@<span class="hljs-keyword">extend</span><span class="hljs-preprocessor"> .message</span>;</span>
  <span class="hljs-attribute">border-color</span><span class="hljs-value">: red;</span>
}
<span class="hljs-class">.warning</span> {
  <span class="hljs-at_rule">@<span class="hljs-keyword">extend</span><span class="hljs-preprocessor"> .message</span>;</span>
  <span class="hljs-attribute">border-color</span><span class="hljs-value">: yellow;</span>
}<div class="hljs-button signin" data-title="登录后复制"></div></code><ul class="pre-numbering" style=""><li style="color: rgb(153, 153, 153);">1</li><li style="color: rgb(153, 153, 153);">2</li><li style="color: rgb(153, 153, 153);">3</li><li style="color: rgb(153, 153, 153);">4</li><li style="color: rgb(153, 153, 153);">5</li><li style="color: rgb(153, 153, 153);">6</li><li style="color: rgb(153, 153, 153);">7</li><li style="color: rgb(153, 153, 153);">8</li><li style="color: rgb(153, 153, 153);">9</li><li style="color: rgb(153, 153, 153);">10</li><li style="color: rgb(153, 153, 153);">11</li><li style="color: rgb(153, 153, 153);">12</li><li style="color: rgb(153, 153, 153);">13</li><li style="color: rgb(153, 153, 153);">14</li><li style="color: rgb(153, 153, 153);">15</li><li style="color: rgb(153, 153, 153);">16</li><li style="color: rgb(153, 153, 153);">17</li></ul></pre>

<p><strong>2.Less css：</strong></p>

<p>但是在这方面 Less 表现的稍微弱一些，更像是混入写法：</p>

<pre class="prettyprint" name="code"><code class="hljs scss has-numbering" onclick="mdcp.signin(event)" style="position: unset;"><span class="hljs-class">.message</span> {
  <span class="hljs-attribute">border</span><span class="hljs-value">: <span class="hljs-number">1</span>px solid <span class="hljs-hexcolor">#ccc</span>;</span>
  <span class="hljs-attribute">padding</span><span class="hljs-value">: <span class="hljs-number">10</span>px;</span>
  <span class="hljs-attribute">color</span><span class="hljs-value">: <span class="hljs-hexcolor">#333</span>;</span>
}
<span class="hljs-class">.success</span> {
  <span class="hljs-class">.message</span>;
  <span class="hljs-attribute">border-color</span><span class="hljs-value">: green;</span>
}
<span class="hljs-class">.error</span> {
  <span class="hljs-class">.message</span>;
  <span class="hljs-attribute">border-color</span><span class="hljs-value">: red;</span>
}
<span class="hljs-class">.warning</span> {
  <span class="hljs-class">.message</span>;
  <span class="hljs-attribute">border-color</span><span class="hljs-value">: yellow;</span>
}<div class="hljs-button signin" data-title="登录后复制"></div></code><ul class="pre-numbering" style=""><li style="color: rgb(153, 153, 153);">1</li><li style="color: rgb(153, 153, 153);">2</li><li style="color: rgb(153, 153, 153);">3</li><li style="color: rgb(153, 153, 153);">4</li><li style="color: rgb(153, 153, 153);">5</li><li style="color: rgb(153, 153, 153);">6</li><li style="color: rgb(153, 153, 153);">7</li><li style="color: rgb(153, 153, 153);">8</li><li style="color: rgb(153, 153, 153);">9</li><li style="color: rgb(153, 153, 153);">10</li><li style="color: rgb(153, 153, 153);">11</li><li style="color: rgb(153, 153, 153);">12</li><li style="color: rgb(153, 153, 153);">13</li><li style="color: rgb(153, 153, 153);">14</li><li style="color: rgb(153, 153, 153);">15</li><li style="color: rgb(153, 153, 153);">16</li><li style="color: rgb(153, 153, 153);">17</li></ul></pre>

<p>上面两种写法其最终呈现的css样式都如下：</p>

<pre class="prettyprint" name="code"><code class="hljs css has-numbering" onclick="mdcp.signin(event)" style="position: unset;"><span class="hljs-class">.message</span>, <span class="hljs-class">.success</span>, <span class="hljs-class">.error</span>, <span class="hljs-class">.warning</span> <span class="hljs-rules">{
  <span class="hljs-rule"><span class="hljs-attribute">border</span>:<span class="hljs-value"> <span class="hljs-number">1</span>px solid <span class="hljs-hexcolor">#cccccc</span></span></span>;
  <span class="hljs-rule"><span class="hljs-attribute">padding</span>:<span class="hljs-value"> <span class="hljs-number">10</span>px</span></span>;
  <span class="hljs-rule"><span class="hljs-attribute">color</span>:<span class="hljs-value"> <span class="hljs-hexcolor">#333</span></span></span>;
<span class="hljs-rule">}</span></span>
<span class="hljs-class">.success</span> <span class="hljs-rules">{
  <span class="hljs-rule"><span class="hljs-attribute">border-color</span>:<span class="hljs-value"> green</span></span>;
<span class="hljs-rule">}</span></span>
<span class="hljs-class">.error</span> <span class="hljs-rules">{
  <span class="hljs-rule"><span class="hljs-attribute">border-color</span>:<span class="hljs-value"> red</span></span>;
<span class="hljs-rule">}</span></span>
<span class="hljs-class">.warning</span> <span class="hljs-rules">{
  <span class="hljs-rule"><span class="hljs-attribute">border-color</span>:<span class="hljs-value"> yellow</span></span>;
<span class="hljs-rule">}</span></span><div class="hljs-button signin" data-title="登录后复制"></div></code><ul class="pre-numbering" style=""><li style="color: rgb(153, 153, 153);">1</li><li style="color: rgb(153, 153, 153);">2</li><li style="color: rgb(153, 153, 153);">3</li><li style="color: rgb(153, 153, 153);">4</li><li style="color: rgb(153, 153, 153);">5</li><li style="color: rgb(153, 153, 153);">6</li><li style="color: rgb(153, 153, 153);">7</li><li style="color: rgb(153, 153, 153);">8</li><li style="color: rgb(153, 153, 153);">9</li><li style="color: rgb(153, 153, 153);">10</li><li style="color: rgb(153, 153, 153);">11</li><li style="color: rgb(153, 153, 153);">12</li><li style="color: rgb(153, 153, 153);">13</li><li style="color: rgb(153, 153, 153);">14</li></ul></pre>

<p>.message的样式将会被插入到相应的你想要继承的选择器中，但需要注意的是优先级的问题。</p>

<h2 id="9mixins混入"><a name="t8"></a>9.Mixins（混入）</h2>

<p>Mixins 有点像是函数或者是宏，当某段 CSS 经常需要在多个元素中使用时，可以为这些共用的 CSS 定义一个 Mixin，然后只需要在需要引用这些 CSS 地方调用该 Mixin 即可。</p>

<p><strong>1.Sass 的混入语法：</strong></p>

<p>sass中可用mixin定义一些代码片段，且可传参数，方便日后根据需求调用。比如说处理css3浏览器前缀：</p>

<pre class="prettyprint" name="code"><code class="hljs scss has-numbering" onclick="mdcp.signin(event)" style="position: unset;"><span class="hljs-at_rule">@<span class="hljs-keyword">mixin</span><span class="hljs-preprocessor"> error</span>($borderWidth:<span class="hljs-preprocessor"> 2px</span>) {</span>
  <span class="hljs-attribute">border</span><span class="hljs-value">: $borderWidth solid <span class="hljs-hexcolor">#F00</span>;</span>
  <span class="hljs-attribute">color</span><span class="hljs-value">: <span class="hljs-hexcolor">#F00</span>;</span>
}
<span class="hljs-class">.generic-error</span> {
  <span class="hljs-attribute">padding</span><span class="hljs-value">: <span class="hljs-number">20</span>px;</span>
  <span class="hljs-attribute">margin</span><span class="hljs-value">: <span class="hljs-number">4</span>px;</span>
  <span class="hljs-at_rule">@<span class="hljs-preprocessor"> include</span><span class="hljs-preprocessor"> error</span>();</span> <span class="hljs-comment">//这里调用默认 border: 2px solid #F00;</span>
}
<span class="hljs-class">.login-error</span> {
  <span class="hljs-attribute">left</span><span class="hljs-value">: <span class="hljs-number">12</span>px;</span>
  <span class="hljs-attribute">position</span><span class="hljs-value">: absolute;</span>
  <span class="hljs-attribute">top</span><span class="hljs-value">: <span class="hljs-number">20</span>px;</span>
  <span class="hljs-at_rule">@<span class="hljs-preprocessor"> include</span><span class="hljs-preprocessor"> error</span>(<span class="hljs-number">5</span>px);</span> <span class="hljs-comment">//这里调用 border:5px solid #F00;</span>
}<div class="hljs-button signin" data-title="登录后复制"></div></code><ul class="pre-numbering" style=""><li style="color: rgb(153, 153, 153);">1</li><li style="color: rgb(153, 153, 153);">2</li><li style="color: rgb(153, 153, 153);">3</li><li style="color: rgb(153, 153, 153);">4</li><li style="color: rgb(153, 153, 153);">5</li><li style="color: rgb(153, 153, 153);">6</li><li style="color: rgb(153, 153, 153);">7</li><li style="color: rgb(153, 153, 153);">8</li><li style="color: rgb(153, 153, 153);">9</li><li style="color: rgb(153, 153, 153);">10</li><li style="color: rgb(153, 153, 153);">11</li><li style="color: rgb(153, 153, 153);">12</li><li style="color: rgb(153, 153, 153);">13</li><li style="color: rgb(153, 153, 153);">14</li><li style="color: rgb(153, 153, 153);">15</li></ul></pre>

<p><strong>2.Less CSS 的混入语法：</strong> <br>
less也支持带参数的混合以及有默认参数值的混合，如下面的例子所示：</p>



<pre class="prettyprint" name="code"><code class="hljs scss has-numbering" onclick="mdcp.signin(event)" style="position: unset;"><span class="hljs-class">.error</span>(<span class="hljs-at_rule">@borderWidth:<span class="hljs-preprocessor"> 2px</span>) {</span>
  <span class="hljs-attribute">border</span><span class="hljs-value">: @borderWidth solid <span class="hljs-hexcolor">#F00</span>;</span>
  <span class="hljs-attribute">color</span><span class="hljs-value">: <span class="hljs-hexcolor">#F00</span>;</span>
}
<span class="hljs-class">.generic-error</span> {
  <span class="hljs-attribute">padding</span><span class="hljs-value">: <span class="hljs-number">20</span>px;</span>
  <span class="hljs-attribute">margin</span><span class="hljs-value">: <span class="hljs-number">4</span>px;</span>
  <span class="hljs-class">.error</span>(); <span class="hljs-comment">//这里调用默认 border: 2px solid #F00;</span>
}
<span class="hljs-class">.login-error</span> {
  <span class="hljs-attribute">left</span><span class="hljs-value">: <span class="hljs-number">12</span>px;</span>
  <span class="hljs-attribute">position</span><span class="hljs-value">: absolute;</span>
  <span class="hljs-attribute">top</span><span class="hljs-value">: <span class="hljs-number">20</span>px;</span>
  <span class="hljs-class">.error</span>(5px); <span class="hljs-comment">//这里调用 border:5px solid #F00;</span>
}<div class="hljs-button signin" data-title="登录后复制"></div></code><ul class="pre-numbering" style=""><li style="color: rgb(153, 153, 153);">1</li><li style="color: rgb(153, 153, 153);">2</li><li style="color: rgb(153, 153, 153);">3</li><li style="color: rgb(153, 153, 153);">4</li><li style="color: rgb(153, 153, 153);">5</li><li style="color: rgb(153, 153, 153);">6</li><li style="color: rgb(153, 153, 153);">7</li><li style="color: rgb(153, 153, 153);">8</li><li style="color: rgb(153, 153, 153);">9</li><li style="color: rgb(153, 153, 153);">10</li><li style="color: rgb(153, 153, 153);">11</li><li style="color: rgb(153, 153, 153);">12</li><li style="color: rgb(153, 153, 153);">13</li><li style="color: rgb(153, 153, 153);">14</li><li style="color: rgb(153, 153, 153);">15</li></ul></pre>

<p><strong>3.Stylus 的混入语法：</strong></p>



<pre class="prettyprint" name="code"><code class="hljs scss has-numbering" onclick="mdcp.signin(event)" style="position: unset;"><span class="hljs-function">error(borderWidth= <span class="hljs-number">2</span>px)</span> {
  <span class="hljs-attribute">border</span><span class="hljs-value">: borderWidth solid <span class="hljs-hexcolor">#F00</span>;</span>
  <span class="hljs-attribute">color</span><span class="hljs-value">: <span class="hljs-hexcolor">#F00</span>;</span>
}
<span class="hljs-class">.generic-error</span> {
  <span class="hljs-attribute">padding</span><span class="hljs-value">: <span class="hljs-number">20</span>px;</span>
  <span class="hljs-attribute">margin</span><span class="hljs-value">: <span class="hljs-number">4</span>px;</span>
  <span class="hljs-function">error()</span>; 
}
<span class="hljs-class">.login-error</span> {
  <span class="hljs-attribute">left</span><span class="hljs-value">: <span class="hljs-number">12</span>px;</span>
  <span class="hljs-attribute">position</span><span class="hljs-value">: absolute;</span>
  <span class="hljs-attribute">top</span><span class="hljs-value">: <span class="hljs-number">20</span>px;</span>
  <span class="hljs-function">error(<span class="hljs-number">5</span>px)</span>; 
}<div class="hljs-button signin" data-title="登录后复制"></div></code><ul class="pre-numbering" style=""><li style="color: rgb(153, 153, 153);">1</li><li style="color: rgb(153, 153, 153);">2</li><li style="color: rgb(153, 153, 153);">3</li><li style="color: rgb(153, 153, 153);">4</li><li style="color: rgb(153, 153, 153);">5</li><li style="color: rgb(153, 153, 153);">6</li><li style="color: rgb(153, 153, 153);">7</li><li style="color: rgb(153, 153, 153);">8</li><li style="color: rgb(153, 153, 153);">9</li><li style="color: rgb(153, 153, 153);">10</li><li style="color: rgb(153, 153, 153);">11</li><li style="color: rgb(153, 153, 153);">12</li><li style="color: rgb(153, 153, 153);">13</li><li style="color: rgb(153, 153, 153);">14</li><li style="color: rgb(153, 153, 153);">15</li></ul></pre>

<p>他们最终呈现的效果都如下：</p>

<pre class="prettyprint" name="code"><code class="hljs css has-numbering" onclick="mdcp.signin(event)" style="position: unset;"><span class="hljs-class">.generic-error</span> <span class="hljs-rules">{
  <span class="hljs-rule"><span class="hljs-attribute">padding</span>:<span class="hljs-value"> <span class="hljs-number">20</span>px</span></span>;
  <span class="hljs-rule"><span class="hljs-attribute">margin</span>:<span class="hljs-value"> <span class="hljs-number">4</span>px</span></span>;
  <span class="hljs-rule"><span class="hljs-attribute">border</span>:<span class="hljs-value"> <span class="hljs-number">2</span>px solid <span class="hljs-hexcolor">#f00</span></span></span>;
  <span class="hljs-rule"><span class="hljs-attribute">color</span>:<span class="hljs-value"> <span class="hljs-hexcolor">#f00</span></span></span>;
<span class="hljs-rule">}</span></span>
<span class="hljs-class">.login-error</span> <span class="hljs-rules">{
  <span class="hljs-rule"><span class="hljs-attribute">left</span>:<span class="hljs-value"> <span class="hljs-number">12</span>px</span></span>;
  <span class="hljs-rule"><span class="hljs-attribute">position</span>:<span class="hljs-value"> absolute</span></span>;
  <span class="hljs-rule"><span class="hljs-attribute">top</span>:<span class="hljs-value"> <span class="hljs-number">20</span>px</span></span>;
  <span class="hljs-rule"><span class="hljs-attribute">border</span>:<span class="hljs-value"> <span class="hljs-number">5</span>px solid <span class="hljs-hexcolor">#f00</span></span></span>;
  <span class="hljs-rule"><span class="hljs-attribute">color</span>:<span class="hljs-value"> <span class="hljs-hexcolor">#f00</span></span></span>;
<span class="hljs-rule">}</span></span><div class="hljs-button signin" data-title="登录后复制"></div></code><ul class="pre-numbering" style=""><li style="color: rgb(153, 153, 153);">1</li><li style="color: rgb(153, 153, 153);">2</li><li style="color: rgb(153, 153, 153);">3</li><li style="color: rgb(153, 153, 153);">4</li><li style="color: rgb(153, 153, 153);">5</li><li style="color: rgb(153, 153, 153);">6</li><li style="color: rgb(153, 153, 153);">7</li><li style="color: rgb(153, 153, 153);">8</li><li style="color: rgb(153, 153, 153);">9</li><li style="color: rgb(153, 153, 153);">10</li><li style="color: rgb(153, 153, 153);">11</li><li style="color: rgb(153, 153, 153);">12</li><li style="color: rgb(153, 153, 153);">13</li></ul></pre>

<h2 id="103d文本"><a name="t9"></a>10.3D文本</h2>

<p>要生成具有 3D 效果的文本可以使用 text-shadows ，唯一的问题就是当要修改颜色的时候就非常的麻烦，而通过 mixin 和颜色函数可以很轻松的实现：</p>

<p><strong>1.sass：</strong></p>



<pre class="prettyprint" name="code"><code class="hljs mel has-numbering" onclick="mdcp.signin(event)" style="position: unset;"><span class="hljs-variable">@mixin</span> text3d(<span class="hljs-variable">$color</span>) {
  <span class="hljs-keyword">color</span>: <span class="hljs-variable">$color</span>;
  <span class="hljs-keyword">text</span>-shadow: <span class="hljs-number">1</span>px <span class="hljs-number">1</span>px <span class="hljs-number">0</span>px darken(<span class="hljs-variable">$color</span>, <span class="hljs-number">5</span><span class="hljs-variable">%)</span>,
               <span class="hljs-number">2</span>px <span class="hljs-number">2</span>px <span class="hljs-number">0</span>px darken(<span class="hljs-variable">$color</span>, <span class="hljs-number">10</span><span class="hljs-variable">%)</span>,
               <span class="hljs-number">3</span>px <span class="hljs-number">3</span>px <span class="hljs-number">0</span>px darken(<span class="hljs-variable">$color</span>, <span class="hljs-number">15</span><span class="hljs-variable">%)</span>,
               <span class="hljs-number">4</span>px <span class="hljs-number">4</span>px <span class="hljs-number">0</span>px darken(<span class="hljs-variable">$color</span>, <span class="hljs-number">20</span><span class="hljs-variable">%)</span>,
               <span class="hljs-number">4</span>px <span class="hljs-number">4</span>px <span class="hljs-number">2</span>px #<span class="hljs-number">000</span>;
}

h1 {
  font-<span class="hljs-keyword">size</span>: <span class="hljs-number">32</span>pt;
  @ include text3d(#<span class="hljs-number">0982</span>c1);
}<div class="hljs-button signin" data-title="登录后复制"></div></code><ul class="pre-numbering" style=""><li style="color: rgb(153, 153, 153);">1</li><li style="color: rgb(153, 153, 153);">2</li><li style="color: rgb(153, 153, 153);">3</li><li style="color: rgb(153, 153, 153);">4</li><li style="color: rgb(153, 153, 153);">5</li><li style="color: rgb(153, 153, 153);">6</li><li style="color: rgb(153, 153, 153);">7</li><li style="color: rgb(153, 153, 153);">8</li><li style="color: rgb(153, 153, 153);">9</li><li style="color: rgb(153, 153, 153);">10</li><li style="color: rgb(153, 153, 153);">11</li><li style="color: rgb(153, 153, 153);">12</li><li style="color: rgb(153, 153, 153);">13</li></ul></pre>

<p><strong>2.Less CSS：</strong></p>



<pre class="prettyprint" name="code"><code class="hljs mel has-numbering" onclick="mdcp.signin(event)" style="position: unset;">.text3d(<span class="hljs-variable">@color</span>) {
  <span class="hljs-keyword">color</span>: <span class="hljs-variable">@color</span>;
  <span class="hljs-keyword">text</span>-shadow: <span class="hljs-number">1</span>px <span class="hljs-number">1</span>px <span class="hljs-number">0</span>px darken(<span class="hljs-variable">@color</span>, <span class="hljs-number">5</span><span class="hljs-variable">%)</span>,
               <span class="hljs-number">2</span>px <span class="hljs-number">2</span>px <span class="hljs-number">0</span>px darken(<span class="hljs-variable">@color</span>, <span class="hljs-number">10</span><span class="hljs-variable">%)</span>,
               <span class="hljs-number">3</span>px <span class="hljs-number">3</span>px <span class="hljs-number">0</span>px darken(<span class="hljs-variable">@color</span>, <span class="hljs-number">15</span><span class="hljs-variable">%)</span>,
               <span class="hljs-number">4</span>px <span class="hljs-number">4</span>px <span class="hljs-number">0</span>px darken(<span class="hljs-variable">@color</span>, <span class="hljs-number">20</span><span class="hljs-variable">%)</span>,
               <span class="hljs-number">4</span>px <span class="hljs-number">4</span>px <span class="hljs-number">2</span>px #<span class="hljs-number">000</span>;
}

span {
  font-<span class="hljs-keyword">size</span>: <span class="hljs-number">32</span>pt;
  .text3d(#<span class="hljs-number">0982</span>c1);
}<div class="hljs-button signin" data-title="登录后复制"></div></code><ul class="pre-numbering" style=""><li style="color: rgb(153, 153, 153);">1</li><li style="color: rgb(153, 153, 153);">2</li><li style="color: rgb(153, 153, 153);">3</li><li style="color: rgb(153, 153, 153);">4</li><li style="color: rgb(153, 153, 153);">5</li><li style="color: rgb(153, 153, 153);">6</li><li style="color: rgb(153, 153, 153);">7</li><li style="color: rgb(153, 153, 153);">8</li><li style="color: rgb(153, 153, 153);">9</li><li style="color: rgb(153, 153, 153);">10</li><li style="color: rgb(153, 153, 153);">11</li><li style="color: rgb(153, 153, 153);">12</li><li style="color: rgb(153, 153, 153);">13</li></ul></pre>

<p><strong>3.Stylus：</strong></p>



<pre class="prettyprint" name="code"><code class="hljs mel has-numbering" onclick="mdcp.signin(event)" style="position: unset;">text3d(<span class="hljs-keyword">color</span>)
  <span class="hljs-keyword">color</span>: <span class="hljs-keyword">color</span>
  <span class="hljs-keyword">text</span>-shadow: <span class="hljs-number">1</span>px <span class="hljs-number">1</span>px <span class="hljs-number">0</span>px darken(<span class="hljs-keyword">color</span>, <span class="hljs-number">5</span><span class="hljs-variable">%)</span>, 
               <span class="hljs-number">2</span>px <span class="hljs-number">2</span>px <span class="hljs-number">0</span>px darken(<span class="hljs-keyword">color</span>, <span class="hljs-number">10</span><span class="hljs-variable">%)</span>, 
               <span class="hljs-number">3</span>px <span class="hljs-number">3</span>px <span class="hljs-number">0</span>px darken(<span class="hljs-keyword">color</span>, <span class="hljs-number">15</span><span class="hljs-variable">%)</span>, 
               <span class="hljs-number">4</span>px <span class="hljs-number">4</span>px <span class="hljs-number">0</span>px darken(<span class="hljs-keyword">color</span>, <span class="hljs-number">20</span><span class="hljs-variable">%)</span>, 
               <span class="hljs-number">4</span>px <span class="hljs-number">4</span>px <span class="hljs-number">2</span>px #<span class="hljs-number">000</span>
span
  font-<span class="hljs-keyword">size</span>: <span class="hljs-number">32</span>pt
  text3d(#<span class="hljs-number">0982</span>c1)<div class="hljs-button signin" data-title="登录后复制"></div></code><ul class="pre-numbering" style=""><li style="color: rgb(153, 153, 153);">1</li><li style="color: rgb(153, 153, 153);">2</li><li style="color: rgb(153, 153, 153);">3</li><li style="color: rgb(153, 153, 153);">4</li><li style="color: rgb(153, 153, 153);">5</li><li style="color: rgb(153, 153, 153);">6</li><li style="color: rgb(153, 153, 153);">7</li><li style="color: rgb(153, 153, 153);">8</li><li style="color: rgb(153, 153, 153);">9</li><li style="color: rgb(153, 153, 153);">10</li></ul></pre>

<p>其生成的css最终的效果如下：</p>

<pre class="prettyprint" name="code"><code class="hljs css has-numbering" onclick="mdcp.signin(event)" style="position: unset;"><span class="hljs-tag">span</span> <span class="hljs-rules">{
  <span class="hljs-rule"><span class="hljs-attribute">font-size</span>:<span class="hljs-value"> <span class="hljs-number">32</span>pt</span></span>;
  <span class="hljs-rule"><span class="hljs-attribute">color</span>:<span class="hljs-value"> <span class="hljs-hexcolor">#0982c1</span></span></span>;
  <span class="hljs-rule"><span class="hljs-attribute">text-shadow</span>:<span class="hljs-value"> <span class="hljs-number">1</span>px <span class="hljs-number">1</span>px <span class="hljs-number">0</span>px <span class="hljs-hexcolor">#097bb7</span>,
               <span class="hljs-number">2</span>px <span class="hljs-number">2</span>px <span class="hljs-number">0</span>px <span class="hljs-hexcolor">#0875ae</span>,
               <span class="hljs-number">3</span>px <span class="hljs-number">3</span>px <span class="hljs-number">0</span>px <span class="hljs-hexcolor">#086fa4</span>,
               <span class="hljs-number">4</span>px <span class="hljs-number">4</span>px <span class="hljs-number">0</span>px <span class="hljs-hexcolor">#07689a</span>,
               <span class="hljs-number">4</span>px <span class="hljs-number">4</span>px <span class="hljs-number">2</span>px <span class="hljs-hexcolor">#000</span></span></span>;
<span class="hljs-rule">}</span></span><div class="hljs-button signin" data-title="登录后复制"></div></code><ul class="pre-numbering" style=""><li style="color: rgb(153, 153, 153);">1</li><li style="color: rgb(153, 153, 153);">2</li><li style="color: rgb(153, 153, 153);">3</li><li style="color: rgb(153, 153, 153);">4</li><li style="color: rgb(153, 153, 153);">5</li><li style="color: rgb(153, 153, 153);">6</li><li style="color: rgb(153, 153, 153);">7</li><li style="color: rgb(153, 153, 153);">8</li><li style="color: rgb(153, 153, 153);">9</li></ul></pre>

<h2 id="11列-columns"><a name="t10"></a>11.列 (Columns)</h2>

<p>使用数值操作和变量可以很方便的实现适应屏幕大小的布局处理。 <br>
<strong>1.Sass：</strong></p>



<pre class="prettyprint" name="code"><code class="hljs css has-numbering" onclick="mdcp.signin(event)" style="position: unset;">$<span class="hljs-tag">siteWidth</span>: 1024<span class="hljs-tag">px</span>;
$<span class="hljs-tag">gutterWidth</span>: 20<span class="hljs-tag">px</span>;
$<span class="hljs-tag">sidebarWidth</span>: 300<span class="hljs-tag">px</span>;
<span class="hljs-tag">body</span> <span class="hljs-rules">{
  <span class="hljs-rule"><span class="hljs-attribute">margin</span>:<span class="hljs-value"> <span class="hljs-number">0</span> auto</span></span>;
  <span class="hljs-rule"><span class="hljs-attribute">width</span>:<span class="hljs-value"> $siteWidth</span></span>;
<span class="hljs-rule">}</span></span>
<span class="hljs-class">.content</span> <span class="hljs-rules">{
  <span class="hljs-rule"><span class="hljs-attribute">float</span>:<span class="hljs-value"> left</span></span>;
  <span class="hljs-rule"><span class="hljs-attribute">width</span>:<span class="hljs-value"> $siteWidth - ($sidebarWidth+$gutterWidth)</span></span>;
<span class="hljs-rule">}</span></span>
<span class="hljs-class">.sidebar</span> <span class="hljs-rules">{
  <span class="hljs-rule"><span class="hljs-attribute">float</span>:<span class="hljs-value"> left</span></span>;
  <span class="hljs-rule"><span class="hljs-attribute">margin-left</span>:<span class="hljs-value"> $gutterWidth</span></span>;
  <span class="hljs-rule"><span class="hljs-attribute">width</span>:<span class="hljs-value"> $sidebarWidth</span></span>;
<span class="hljs-rule">}</span></span><div class="hljs-button signin" data-title="登录后复制"></div></code><ul class="pre-numbering" style=""><li style="color: rgb(153, 153, 153);">1</li><li style="color: rgb(153, 153, 153);">2</li><li style="color: rgb(153, 153, 153);">3</li><li style="color: rgb(153, 153, 153);">4</li><li style="color: rgb(153, 153, 153);">5</li><li style="color: rgb(153, 153, 153);">6</li><li style="color: rgb(153, 153, 153);">7</li><li style="color: rgb(153, 153, 153);">8</li><li style="color: rgb(153, 153, 153);">9</li><li style="color: rgb(153, 153, 153);">10</li><li style="color: rgb(153, 153, 153);">11</li><li style="color: rgb(153, 153, 153);">12</li><li style="color: rgb(153, 153, 153);">13</li><li style="color: rgb(153, 153, 153);">14</li><li style="color: rgb(153, 153, 153);">15</li><li style="color: rgb(153, 153, 153);">16</li></ul></pre>

<p>2.Less CSS：</p>



<pre class="prettyprint" name="code"><code class="hljs css has-numbering" onclick="mdcp.signin(event)" style="position: unset;"><span class="hljs-at_rule">@<span class="hljs-keyword">siteWidth:</span> <span class="hljs-number">1024</span>px</span>;
<span class="hljs-at_rule">@<span class="hljs-keyword">gutterWidth:</span> <span class="hljs-number">20</span>px</span>;
<span class="hljs-at_rule">@<span class="hljs-keyword">sidebarWidth:</span> <span class="hljs-number">300</span>px</span>;

<span class="hljs-tag">body</span> <span class="hljs-rules">{
  <span class="hljs-rule"><span class="hljs-attribute">margin</span>:<span class="hljs-value"> <span class="hljs-number">0</span> auto</span></span>;
  <span class="hljs-rule"><span class="hljs-attribute">width</span>:<span class="hljs-value"> @siteWidth</span></span>;
<span class="hljs-rule">}</span></span>
<span class="hljs-class">.content</span> <span class="hljs-rules">{
  <span class="hljs-rule"><span class="hljs-attribute">float</span>:<span class="hljs-value"> left</span></span>;
  <span class="hljs-rule"><span class="hljs-attribute">width</span>:<span class="hljs-value"> @siteWidth - (@sidebarWidth+@gutterWidth)</span></span>;
<span class="hljs-rule">}</span></span>
<span class="hljs-class">.sidebar</span> <span class="hljs-rules">{
  <span class="hljs-rule"><span class="hljs-attribute">float</span>:<span class="hljs-value"> left</span></span>;
  <span class="hljs-rule"><span class="hljs-attribute">margin-left</span>:<span class="hljs-value"> @gutterWidth</span></span>;
  <span class="hljs-rule"><span class="hljs-attribute">width</span>:<span class="hljs-value"> @sidebarWidth</span></span>;
<span class="hljs-rule">}</span></span><div class="hljs-button signin" data-title="登录后复制"></div></code><ul class="pre-numbering" style=""><li style="color: rgb(153, 153, 153);">1</li><li style="color: rgb(153, 153, 153);">2</li><li style="color: rgb(153, 153, 153);">3</li><li style="color: rgb(153, 153, 153);">4</li><li style="color: rgb(153, 153, 153);">5</li><li style="color: rgb(153, 153, 153);">6</li><li style="color: rgb(153, 153, 153);">7</li><li style="color: rgb(153, 153, 153);">8</li><li style="color: rgb(153, 153, 153);">9</li><li style="color: rgb(153, 153, 153);">10</li><li style="color: rgb(153, 153, 153);">11</li><li style="color: rgb(153, 153, 153);">12</li><li style="color: rgb(153, 153, 153);">13</li><li style="color: rgb(153, 153, 153);">14</li><li style="color: rgb(153, 153, 153);">15</li><li style="color: rgb(153, 153, 153);">16</li><li style="color: rgb(153, 153, 153);">17</li></ul></pre>

<p><strong>3.Stylus：</strong></p>



<pre class="prettyprint" name="code"><code class="hljs d has-numbering" onclick="mdcp.signin(event)" style="position: unset;">siteWidth = <span class="hljs-number">1024</span>px;
gutterWidth = <span class="hljs-number">20</span>px;
sidebarWidth = <span class="hljs-number">300</span>px;

<span class="hljs-keyword">body</span> {
  margin: <span class="hljs-number">0</span> <span class="hljs-keyword">auto</span>;
  width: siteWidth;
}
.content {
  <span class="hljs-built_in">float</span>: left;
  width: siteWidth - (sidebarWidth+gutterWidth);
}
.sidebar {
  <span class="hljs-built_in">float</span>: left;
  margin-left: gutterWidth;
  width: sidebarWidth;
}<div class="hljs-button signin" data-title="登录后复制"></div></code><ul class="pre-numbering" style=""><li style="color: rgb(153, 153, 153);">1</li><li style="color: rgb(153, 153, 153);">2</li><li style="color: rgb(153, 153, 153);">3</li><li style="color: rgb(153, 153, 153);">4</li><li style="color: rgb(153, 153, 153);">5</li><li style="color: rgb(153, 153, 153);">6</li><li style="color: rgb(153, 153, 153);">7</li><li style="color: rgb(153, 153, 153);">8</li><li style="color: rgb(153, 153, 153);">9</li><li style="color: rgb(153, 153, 153);">10</li><li style="color: rgb(153, 153, 153);">11</li><li style="color: rgb(153, 153, 153);">12</li><li style="color: rgb(153, 153, 153);">13</li><li style="color: rgb(153, 153, 153);">14</li><li style="color: rgb(153, 153, 153);">15</li><li style="color: rgb(153, 153, 153);">16</li><li style="color: rgb(153, 153, 153);">17</li></ul></pre>

<p>其最终生成的css效果如下：</p>



<pre class="prettyprint" name="code"><code class="hljs css has-numbering" onclick="mdcp.signin(event)" style="position: unset;"><span class="hljs-tag">body</span> <span class="hljs-rules">{
  <span class="hljs-rule"><span class="hljs-attribute">margin</span>:<span class="hljs-value"> <span class="hljs-number">0</span> auto</span></span>;
  <span class="hljs-rule"><span class="hljs-attribute">width</span>:<span class="hljs-value"> <span class="hljs-number">1024</span>px</span></span>;
<span class="hljs-rule">}</span></span>
<span class="hljs-class">.content</span> <span class="hljs-rules">{
  <span class="hljs-rule"><span class="hljs-attribute">float</span>:<span class="hljs-value"> left</span></span>;
  <span class="hljs-rule"><span class="hljs-attribute">width</span>:<span class="hljs-value"> <span class="hljs-number">704</span>px</span></span>;
<span class="hljs-rule">}</span></span>
<span class="hljs-class">.sidebar</span> <span class="hljs-rules">{
  <span class="hljs-rule"><span class="hljs-attribute">float</span>:<span class="hljs-value"> left</span></span>;
  <span class="hljs-rule"><span class="hljs-attribute">margin-left</span>:<span class="hljs-value"> <span class="hljs-number">20</span>px</span></span>;
  <span class="hljs-rule"><span class="hljs-attribute">width</span>:<span class="hljs-value"> <span class="hljs-number">300</span>px</span></span>;
<span class="hljs-rule">}</span></span><div class="hljs-button signin" data-title="登录后复制"></div></code><ul class="pre-numbering" style=""><li style="color: rgb(153, 153, 153);">1</li><li style="color: rgb(153, 153, 153);">2</li><li style="color: rgb(153, 153, 153);">3</li><li style="color: rgb(153, 153, 153);">4</li><li style="color: rgb(153, 153, 153);">5</li><li style="color: rgb(153, 153, 153);">6</li><li style="color: rgb(153, 153, 153);">7</li><li style="color: rgb(153, 153, 153);">8</li><li style="color: rgb(153, 153, 153);">9</li><li style="color: rgb(153, 153, 153);">10</li><li style="color: rgb(153, 153, 153);">11</li><li style="color: rgb(153, 153, 153);">12</li><li style="color: rgb(153, 153, 153);">13</li></ul></pre>

<h2 id="12高级语法"><a name="t11"></a>12.高级语法</h2>

<p>1.在sass中，还支持条件语句：</p>

<pre class="prettyprint"><code class="has-numbering" onclick="mdcp.signin(event)" style="position: unset;">    @if可一个条件单独使用，也可以和@else结合多条件使用
<div class="hljs-button signin" data-title="登录后复制"></div></code><ul class="pre-numbering" style=""><li style="color: rgb(153, 153, 153);">1</li></ul></pre>

<p>代码如下：</p>

<pre class="prettyprint" name="code"><code class="hljs scss has-numbering" onclick="mdcp.signin(event)" style="position: unset;">$lte7<span class="hljs-value">: true;</span>
$type<span class="hljs-value">: monster;</span>
<span class="hljs-class">.ib</span>{
    <span class="hljs-attribute">display</span><span class="hljs-value">:inline-block;</span>
    <span class="hljs-at_rule">@<span class="hljs-keyword">if</span> $lte7 {</span>
        *<span class="hljs-attribute">display</span><span class="hljs-value">:inline;</span>
        *zoom<span class="hljs-value">:<span class="hljs-number">1</span>;</span>
    }
}
<span class="hljs-tag">p</span> {
  <span class="hljs-at_rule">@<span class="hljs-keyword">if</span> $type ==<span class="hljs-preprocessor"> ocean</span> {</span>
    <span class="hljs-attribute">color</span><span class="hljs-value">: blue;</span>
  } <span class="hljs-at_rule">@<span class="hljs-keyword">else</span><span class="hljs-preprocessor"> if</span> $type ==<span class="hljs-preprocessor"> matador</span> {</span>
    <span class="hljs-attribute">color</span><span class="hljs-value">: red;</span>
  } <span class="hljs-at_rule">@<span class="hljs-keyword">else</span><span class="hljs-preprocessor"> if</span> $type ==<span class="hljs-preprocessor"> monster</span> {</span>
    <span class="hljs-attribute">color</span><span class="hljs-value">: green;</span>
  } <span class="hljs-at_rule">@<span class="hljs-keyword">else</span> {</span>
    <span class="hljs-attribute">color</span><span class="hljs-value">: black;</span>
  }
}<div class="hljs-button signin" data-title="登录后复制"></div></code><ul class="pre-numbering" style=""><li style="color: rgb(153, 153, 153);">1</li><li style="color: rgb(153, 153, 153);">2</li><li style="color: rgb(153, 153, 153);">3</li><li style="color: rgb(153, 153, 153);">4</li><li style="color: rgb(153, 153, 153);">5</li><li style="color: rgb(153, 153, 153);">6</li><li style="color: rgb(153, 153, 153);">7</li><li style="color: rgb(153, 153, 153);">8</li><li style="color: rgb(153, 153, 153);">9</li><li style="color: rgb(153, 153, 153);">10</li><li style="color: rgb(153, 153, 153);">11</li><li style="color: rgb(153, 153, 153);">12</li><li style="color: rgb(153, 153, 153);">13</li><li style="color: rgb(153, 153, 153);">14</li><li style="color: rgb(153, 153, 153);">15</li><li style="color: rgb(153, 153, 153);">16</li><li style="color: rgb(153, 153, 153);">17</li><li style="color: rgb(153, 153, 153);">18</li><li style="color: rgb(153, 153, 153);">19</li><li style="color: rgb(153, 153, 153);">20</li></ul></pre>

<p>其最终的css代码如下：</p>



<pre class="prettyprint" name="code"><code class="hljs css has-numbering" onclick="mdcp.signin(event)" style="position: unset;"><span class="hljs-class">.ib</span><span class="hljs-rules">{
    <span class="hljs-rule"><span class="hljs-attribute">display</span>:<span class="hljs-value">inline-block</span></span>;
    <span class="hljs-rule">*<span class="hljs-attribute">display</span>:<span class="hljs-value">inline</span></span>;
    <span class="hljs-rule">*<span class="hljs-attribute">zoom</span>:<span class="hljs-value"><span class="hljs-number">1</span></span></span>;
<span class="hljs-rule">}</span></span>
<span class="hljs-tag">p</span> <span class="hljs-rules">{
  <span class="hljs-rule"><span class="hljs-attribute">color</span>:<span class="hljs-value"> green</span></span>; 
<span class="hljs-rule">}</span></span><div class="hljs-button signin" data-title="登录后复制"></div></code><ul class="pre-numbering" style=""><li style="color: rgb(153, 153, 153);">1</li><li style="color: rgb(153, 153, 153);">2</li><li style="color: rgb(153, 153, 153);">3</li><li style="color: rgb(153, 153, 153);">4</li><li style="color: rgb(153, 153, 153);">5</li><li style="color: rgb(153, 153, 153);">6</li><li style="color: rgb(153, 153, 153);">7</li><li style="color: rgb(153, 153, 153);">8</li></ul></pre>

<p>2.除却条件语句，sass还支持for循环：</p>

<p>for循环有两种形式，分别为：</p>



<pre class="prettyprint" name="code"><code class="hljs livecodeserver has-numbering" onclick="mdcp.signin(event)" style="position: unset;"><span class="hljs-number">1.</span>@<span class="hljs-keyword">for</span> $var <span class="hljs-built_in">from</span> &lt;start&gt; through &lt;<span class="hljs-function"><span class="hljs-keyword">end</span>&gt;</span>
<span class="hljs-number">2.</span>@<span class="hljs-keyword">for</span> $var <span class="hljs-built_in">from</span> &lt;start&gt; <span class="hljs-built_in">to</span> &lt;<span class="hljs-function"><span class="hljs-keyword">end</span>&gt;。</span><div class="hljs-button signin" data-title="登录后复制"></div></code><ul class="pre-numbering" style=""><li style="color: rgb(153, 153, 153);">1</li><li style="color: rgb(153, 153, 153);">2</li></ul></pre>

<p>其中$i表示变量，start表示起始值，end表示结束值，这两个的区别是关键字through表示包括end这个数，而to则不包括end这个数。</p>

<pre class="prettyprint" name="code"><code class="hljs haml has-numbering" onclick="mdcp.signin(event)" style="position: unset;">@for $i from 1 to 10 {
  .border-#{<span class="ruby"><span class="hljs-variable">$i</span>}</span> {
    border: #{<span class="ruby"><span class="hljs-variable">$i</span>}</span>px solid blue;
  }
}<div class="hljs-button signin" data-title="登录后复制"></div></code><ul class="pre-numbering" style=""><li style="color: rgb(153, 153, 153);">1</li><li style="color: rgb(153, 153, 153);">2</li><li style="color: rgb(153, 153, 153);">3</li><li style="color: rgb(153, 153, 153);">4</li><li style="color: rgb(153, 153, 153);">5</li></ul></pre>

<p>同时也支持while循环：</p>

<pre class="prettyprint" name="code"><code class="hljs mel has-numbering" onclick="mdcp.signin(event)" style="position: unset;"><span class="hljs-variable">$i</span>: <span class="hljs-number">6</span>;
<span class="hljs-variable">@while</span> <span class="hljs-variable">$i</span> &gt; <span class="hljs-number">0</span> {
  .item-#{<span class="hljs-variable">$i</span>} { width: <span class="hljs-number">2</span>em * <span class="hljs-variable">$i</span>; }
  <span class="hljs-variable">$i</span>: <span class="hljs-variable">$i</span> - <span class="hljs-number">2</span>;
}<div class="hljs-button signin" data-title="登录后复制"></div></code><ul class="pre-numbering" style=""><li style="color: rgb(153, 153, 153);">1</li><li style="color: rgb(153, 153, 153);">2</li><li style="color: rgb(153, 153, 153);">3</li><li style="color: rgb(153, 153, 153);">4</li><li style="color: rgb(153, 153, 153);">5</li></ul></pre>

<p>最后，同时支持each命令，作用与for类似：</p>



<pre class="prettyprint" name="code"><code class="hljs ruby has-numbering" onclick="mdcp.signin(event)" style="position: unset;"><span class="hljs-variable">$animal</span>-<span class="hljs-symbol">list:</span> puma, sea-slug, egret, salamander;
<span class="hljs-variable">@each</span> <span class="hljs-variable">$animal</span> <span class="hljs-keyword">in</span> <span class="hljs-variable">$animal</span>-list {
  .<span class="hljs-comment">#{$animal}-icon {</span>
    background-<span class="hljs-symbol">image:</span> url(<span class="hljs-string">'/img/<span class="hljs-subst">#{<span class="hljs-variable">$animal</span>}</span>.png'</span>);
  }
}<div class="hljs-button signin" data-title="登录后复制"></div></code><ul class="pre-numbering" style=""><li style="color: rgb(153, 153, 153);">1</li><li style="color: rgb(153, 153, 153);">2</li><li style="color: rgb(153, 153, 153);">3</li><li style="color: rgb(153, 153, 153);">4</li><li style="color: rgb(153, 153, 153);">5</li><li style="color: rgb(153, 153, 153);">6</li></ul></pre>

<p>其css最终效果如下：</p>



<pre class="prettyprint" name="code"><code class="hljs css has-numbering" onclick="mdcp.signin(event)" style="position: unset;"><span class="hljs-class">.puma-icon</span> <span class="hljs-rules">{
  <span class="hljs-rule"><span class="hljs-attribute">background-image</span>:<span class="hljs-value"> <span class="hljs-function">url(<span class="hljs-string">'/img/puma.png'</span>)</span></span></span>; 
<span class="hljs-rule">}</span></span>
<span class="hljs-class">.sea-slug-icon</span> <span class="hljs-rules">{
  <span class="hljs-rule"><span class="hljs-attribute">background-image</span>:<span class="hljs-value"> <span class="hljs-function">url(<span class="hljs-string">'/img/sea-slug.png'</span>)</span></span></span>; 
<span class="hljs-rule">}</span></span>
<span class="hljs-class">.egret-icon</span> <span class="hljs-rules">{
  <span class="hljs-rule"><span class="hljs-attribute">background-image</span>:<span class="hljs-value"> <span class="hljs-function">url(<span class="hljs-string">'/img/egret.png'</span>)</span></span></span>; 
<span class="hljs-rule">}</span></span>
<span class="hljs-class">.salamander-icon</span> <span class="hljs-rules">{
  <span class="hljs-rule"><span class="hljs-attribute">background-image</span>:<span class="hljs-value"> <span class="hljs-function">url(<span class="hljs-string">'/img/salamander.png'</span>)</span></span></span>; 
<span class="hljs-rule">}</span></span><div class="hljs-button signin" data-title="登录后复制"></div></code><ul class="pre-numbering" style=""><li style="color: rgb(153, 153, 153);">1</li><li style="color: rgb(153, 153, 153);">2</li><li style="color: rgb(153, 153, 153);">3</li><li style="color: rgb(153, 153, 153);">4</li><li style="color: rgb(153, 153, 153);">5</li><li style="color: rgb(153, 153, 153);">6</li><li style="color: rgb(153, 153, 153);">7</li><li style="color: rgb(153, 153, 153);">8</li><li style="color: rgb(153, 153, 153);">9</li><li style="color: rgb(153, 153, 153);">10</li><li style="color: rgb(153, 153, 153);">11</li><li style="color: rgb(153, 153, 153);">12</li></ul></pre>

<p>以上就是sass，Less css与stylus的最显著的区别。</p>                                    </div>