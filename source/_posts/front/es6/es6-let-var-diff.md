---
title: 'ES6中let和var的区别'
cover: "/img/lynk/37.jpg"
date:       2019-09-16
tags:
	- web
	- html
	- solution
---













[原文链接](https://www.jianshu.com/p/759f120910e8)

<section class="ouvJEz">
    <article class="_2rhmJa"><p>let是在ES6中新引入的关键字，用来改进var带来的各种问题。<br>
let和var相比，大致有下面几个方面的不同：</p>
<ul>
<li>作用域<br>
通过let定义的变量，作用域是在定义它的块级代码以及其中包括的子块中，并且无法在全局作用域添加变量。<br>
通过var定义的变量，作用域为包括它的函数作用域或者全局作用域。</li>
</ul>
<pre class="line-numbers  language-jsx"><code class="  language-jsx"><span class="token keyword">function</span> <span class="token function">varTest</span><span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
  <span class="token keyword">var</span> x <span class="token operator">=</span> <span class="token number">1</span><span class="token punctuation">;</span>
  <span class="token keyword">if</span> <span class="token punctuation">(</span><span class="token boolean">true</span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
    <span class="token keyword">var</span> x <span class="token operator">=</span> <span class="token number">2</span><span class="token punctuation">;</span>  <span class="token comment">// same variable!</span>
    console<span class="token punctuation">.</span><span class="token function">log</span><span class="token punctuation">(</span>x<span class="token punctuation">)</span><span class="token punctuation">;</span>  <span class="token comment">// 2</span>
  <span class="token punctuation">}</span>
  console<span class="token punctuation">.</span><span class="token function">log</span><span class="token punctuation">(</span>x<span class="token punctuation">)</span><span class="token punctuation">;</span>  <span class="token comment">// 2</span>
<span class="token punctuation">}</span>

<span class="token keyword">function</span> <span class="token function">letTest</span><span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
  <span class="token keyword">let</span> x <span class="token operator">=</span> <span class="token number">1</span><span class="token punctuation">;</span>
  <span class="token keyword">if</span> <span class="token punctuation">(</span><span class="token boolean">true</span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
    <span class="token keyword">let</span> x <span class="token operator">=</span> <span class="token number">2</span><span class="token punctuation">;</span>  <span class="token comment">// different variable</span>
    console<span class="token punctuation">.</span><span class="token function">log</span><span class="token punctuation">(</span>x<span class="token punctuation">)</span><span class="token punctuation">;</span>  <span class="token comment">// 2</span>
  <span class="token punctuation">}</span>
  console<span class="token punctuation">.</span><span class="token function">log</span><span class="token punctuation">(</span>x<span class="token punctuation">)</span><span class="token punctuation">;</span>  <span class="token comment">// 1</span>
<span class="token punctuation">}</span>
<span class="token comment">// let 无法在全局作用域中定义变量</span>
<span class="token keyword">var</span> x <span class="token operator">=</span> <span class="token string">'global'</span><span class="token punctuation">;</span>
<span class="token keyword">let</span> y <span class="token operator">=</span> <span class="token string">'global'</span><span class="token punctuation">;</span>
console<span class="token punctuation">.</span><span class="token function">log</span><span class="token punctuation">(</span><span class="token keyword">this</span><span class="token punctuation">.</span>x<span class="token punctuation">)</span><span class="token punctuation">;</span> <span class="token comment">// "global"</span>
console<span class="token punctuation">.</span><span class="token function">log</span><span class="token punctuation">(</span><span class="token keyword">this</span><span class="token punctuation">.</span>y<span class="token punctuation">)</span><span class="token punctuation">;</span> <span class="token comment">// undefined</span>
<span aria-hidden="true" class="line-numbers-rows"><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span></span></code></pre>
<p>let的block scope的特性，可以用来实现class的私有成员。在let之前，一般是通过闭包的特性实现的。代码如下：</p>
<pre class="line-numbers  language-jsx"><code class="  language-jsx"><span class="token keyword">var</span> Thing <span class="token operator">=</span> <span class="token punctuation">{</span><span class="token punctuation">}</span>
<span class="token comment">// block scope</span>
<span class="token punctuation">{</span>
  <span class="token keyword">let</span> counter <span class="token operator">=</span> <span class="token number">1</span>
  <span class="token function-variable function">Thing</span> <span class="token operator">=</span> <span class="token keyword">function</span> <span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
    <span class="token keyword">this</span><span class="token punctuation">.</span>name <span class="token operator">=</span> <span class="token string">'something'</span>  <span class="token comment">// 创建公共成员</span>
  <span class="token punctuation">}</span>
  <span class="token class-name">Thing</span><span class="token punctuation">.</span>prototype<span class="token punctuation">.</span><span class="token function-variable function">showPublic</span> <span class="token operator">=</span> <span class="token keyword">function</span> <span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
    <span class="token keyword">return</span> <span class="token keyword">this</span><span class="token punctuation">.</span>name
  <span class="token punctuation">}</span>
  <span class="token class-name">Thing</span><span class="token punctuation">.</span>prototype<span class="token punctuation">.</span><span class="token function-variable function">showPrivate</span> <span class="token operator">=</span> <span class="token keyword">function</span> <span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token punctuation">{</span>  <span class="token comment">// counter变为了私有成员，只能通过showPrivate进行访问</span>
    counter <span class="token operator">++</span>
    <span class="token keyword">return</span> counter
  <span class="token punctuation">}</span>
<span class="token punctuation">}</span>
<span class="token keyword">var</span> thing <span class="token operator">=</span> <span class="token keyword">new</span> <span class="token class-name">Thing</span><span class="token punctuation">(</span><span class="token punctuation">)</span>
console<span class="token punctuation">.</span><span class="token function">log</span><span class="token punctuation">(</span>thing<span class="token punctuation">.</span>name<span class="token punctuation">)</span>  <span class="token comment">// something</span>
console<span class="token punctuation">.</span><span class="token function">log</span><span class="token punctuation">(</span>thing<span class="token punctuation">.</span><span class="token function">showPublic</span><span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token punctuation">)</span>  <span class="token comment">// something</span>
thing<span class="token punctuation">.</span>name <span class="token operator">=</span> <span class="token string">'otherthing'</span>
console<span class="token punctuation">.</span><span class="token function">log</span><span class="token punctuation">(</span>thing<span class="token punctuation">.</span><span class="token function">showPublic</span><span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token punctuation">)</span>  <span class="token comment">// otherthing</span>
console<span class="token punctuation">.</span><span class="token function">log</span><span class="token punctuation">(</span>thing<span class="token punctuation">.</span><span class="token function">showPrivate</span><span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token punctuation">)</span> <span class="token comment">// 2</span>
console<span class="token punctuation">.</span><span class="token function">log</span><span class="token punctuation">(</span>thing<span class="token punctuation">)</span>  <span class="token comment">// Thing {name: "otherthing"}</span>
<span aria-hidden="true" class="line-numbers-rows"><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span></span></code></pre>
<p>我们可以和之前使用闭包的方法进行比较下：</p>
<pre class="line-numbers  language-jsx"><code class="  language-jsx"><span class="token keyword">var</span> Thing <span class="token operator">=</span> <span class="token punctuation">(</span><span class="token keyword">function</span><span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
  <span class="token keyword">var</span> counter <span class="token operator">=</span> <span class="token number">1</span><span class="token punctuation">;</span>
  <span class="token keyword">return</span> <span class="token punctuation">{</span>
    name<span class="token punctuation">:</span> <span class="token string">'something'</span><span class="token punctuation">,</span>
    <span class="token function-variable function">showPublic</span><span class="token punctuation">:</span> <span class="token keyword">function</span> <span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
      <span class="token keyword">return</span> <span class="token keyword">this</span><span class="token punctuation">.</span>name
    <span class="token punctuation">}</span><span class="token punctuation">,</span>
    <span class="token function-variable function">showPrivate</span><span class="token punctuation">:</span> <span class="token keyword">function</span> <span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
      counter<span class="token operator">++</span>
      <span class="token keyword">return</span> counter
    <span class="token punctuation">}</span>
  <span class="token punctuation">}</span>   
<span class="token punctuation">}</span><span class="token punctuation">)</span><span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token punctuation">;</span>

<span class="token keyword">var</span> thing <span class="token operator">=</span> Thing
console<span class="token punctuation">.</span><span class="token function">log</span><span class="token punctuation">(</span>thing<span class="token punctuation">.</span>name<span class="token punctuation">)</span>  <span class="token comment">// something</span>
console<span class="token punctuation">.</span><span class="token function">log</span><span class="token punctuation">(</span>thing<span class="token punctuation">.</span><span class="token function">showPublic</span><span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token punctuation">)</span>  <span class="token comment">// something</span>
thing<span class="token punctuation">.</span>name <span class="token operator">=</span> <span class="token string">'otherthing'</span>
console<span class="token punctuation">.</span><span class="token function">log</span><span class="token punctuation">(</span>thing<span class="token punctuation">.</span><span class="token function">showPublic</span><span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token punctuation">)</span>  <span class="token comment">// otherthing</span>
console<span class="token punctuation">.</span><span class="token function">log</span><span class="token punctuation">(</span>thing<span class="token punctuation">.</span><span class="token function">showPrivate</span><span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token punctuation">)</span> <span class="token comment">// 2</span>
console<span class="token punctuation">.</span><span class="token function">log</span><span class="token punctuation">(</span>thing<span class="token punctuation">)</span>  <span class="token comment">// Thing {name: "otherthing"}</span>
<span aria-hidden="true" class="line-numbers-rows"><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span></span></code></pre>
<p>两个的差异，在于一个使用了property，通过new创建新对象。一个是直接返回一个对象。后面要重新看下原型链的问题，再对其总结下。</p>
<ul>
<li>重复声明<br>
通过let定义的变量，在同一个作用域内，不可以重复声明。<br>
通过var定义的变量，在同一个作用域内，重复声明，在生成执行上下文的时候，会无视后面的声明。</li>
</ul>
<pre class="line-numbers  language-jsx"><code class="  language-jsx"><span class="token comment">// 报错</span>
<span class="token punctuation">(</span><span class="token keyword">function</span> <span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
  <span class="token keyword">let</span> a <span class="token operator">=</span> <span class="token number">10</span><span class="token punctuation">;</span>
  <span class="token keyword">var</span> a <span class="token operator">=</span> <span class="token number">1</span><span class="token punctuation">;</span>
  console<span class="token punctuation">.</span><span class="token function">log</span><span class="token punctuation">(</span>a<span class="token punctuation">)</span>
<span class="token punctuation">}</span><span class="token punctuation">)</span><span class="token punctuation">(</span><span class="token punctuation">)</span>
<span class="token comment">// 报错</span>
<span class="token punctuation">(</span><span class="token keyword">function</span> <span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
  <span class="token keyword">let</span> a <span class="token operator">=</span> <span class="token number">10</span><span class="token punctuation">;</span>
  <span class="token keyword">let</span> a <span class="token operator">=</span> <span class="token number">1</span><span class="token punctuation">;</span>
  console<span class="token punctuation">.</span><span class="token function">log</span><span class="token punctuation">(</span>a<span class="token punctuation">)</span>
<span class="token punctuation">}</span><span class="token punctuation">)</span><span class="token punctuation">(</span><span class="token punctuation">)</span>
<span class="token comment">// 报错</span>
<span class="token punctuation">(</span><span class="token keyword">function</span> <span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
  <span class="token keyword">var</span> a <span class="token operator">=</span> <span class="token number">10</span><span class="token punctuation">;</span>
  <span class="token keyword">var</span> a <span class="token operator">=</span> <span class="token number">1</span><span class="token punctuation">;</span>
  console<span class="token punctuation">.</span><span class="token function">log</span><span class="token punctuation">(</span>a<span class="token punctuation">)</span> <span class="token comment">// 1</span>
<span class="token punctuation">}</span><span class="token punctuation">)</span><span class="token punctuation">(</span><span class="token punctuation">)</span>
<span aria-hidden="true" class="line-numbers-rows"><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span></span></code></pre>
<p>需要注意，当在switch-case语句中，如果case语句没有使用{}包括，则视为同一个作用域。</p>
<ul>
<li>临时死区引起的提升等问题<br>
我们知道在代码执行之前，会先扫描所有域内的var声明的变量，将其先进行初始化为undefined，然后再执行代码，也就是所谓的“提升”现象。<br>
但对于let声明的变量而言，则有所不同。在代码执行之前的扫描，同样也会对let变量进行“提升”，但并没有将其置为undefined。let定义的变量虽然经历了提升，但在没有执行到初始化它的代码前，该变量并没有被初始化，如果此时访问的话，会被置为<a href="https://developer.mozilla.org/en-US/docs/JavaScript/Reference/Global_Objects/ReferenceError" target="_blank" rel="nofollow">ReferenceError</a>错误。从代码块开始到执行到let变量初始化完毕这段时间，let变量已经被声明，但不可访问。这段时间被成为临时死区。下面是几个典型的展示临时死区问题的代码：</li>
</ul>
<pre class="line-numbers  language-jsx"><code class="  language-jsx"><span class="token comment">// let变量的作用域为function scope</span>
<span class="token keyword">function</span> <span class="token function">do_something</span><span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
  console<span class="token punctuation">.</span><span class="token function">log</span><span class="token punctuation">(</span>bar<span class="token punctuation">)</span><span class="token punctuation">;</span> <span class="token comment">// undefined</span>
  console<span class="token punctuation">.</span><span class="token function">log</span><span class="token punctuation">(</span>foo<span class="token punctuation">)</span><span class="token punctuation">;</span> <span class="token comment">// ReferenceError</span>
  <span class="token keyword">var</span> bar <span class="token operator">=</span> <span class="token number">1</span><span class="token punctuation">;</span>
  <span class="token keyword">let</span> foo <span class="token operator">=</span> <span class="token number">2</span><span class="token punctuation">;</span>
<span class="token punctuation">}</span>
<span class="token comment">// let变量的作用域为整段代码，</span>
<span class="token comment">// prints out 'undefined'</span>
console<span class="token punctuation">.</span><span class="token function">log</span><span class="token punctuation">(</span><span class="token keyword">typeof</span> undeclaredVariable<span class="token punctuation">)</span><span class="token punctuation">;</span>  <span class="token comment">// typeof对于未声明的变量返回undefined</span>
<span class="token comment">// results in a 'ReferenceError'</span>
console<span class="token punctuation">.</span><span class="token function">log</span><span class="token punctuation">(</span><span class="token keyword">typeof</span> i<span class="token punctuation">)</span><span class="token punctuation">;</span>
<span class="token keyword">let</span> i <span class="token operator">=</span> <span class="token number">10</span><span class="token punctuation">;</span>
<span class="token comment">// let 变量为block scope，在初始化时使用，依然会视为临时死区，只有在初始化执行完后才可以使用</span>
<span class="token keyword">function</span> <span class="token function">test</span><span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token punctuation">{</span>
   <span class="token keyword">var</span> foo <span class="token operator">=</span> <span class="token number">33</span><span class="token punctuation">;</span>
   <span class="token keyword">if</span> <span class="token punctuation">(</span><span class="token boolean">true</span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
      <span class="token keyword">let</span> foo <span class="token operator">=</span> <span class="token punctuation">(</span>foo <span class="token operator">+</span> <span class="token number">55</span><span class="token punctuation">)</span><span class="token punctuation">;</span> <span class="token comment">// ReferenceError</span>
   <span class="token punctuation">}</span>
<span class="token punctuation">}</span>
<span class="token function">test</span><span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
<span class="token comment">// let 变量在for的block scope内进行了声明，n.a对应的是在本地作用域中的let变量n。在未初始化前，通过n.a进行了访问了n，因此报错</span>
<span class="token keyword">function</span> <span class="token function">go</span><span class="token punctuation">(</span><span class="token parameter">n</span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
  <span class="token comment">// n here is defined!</span>
  console<span class="token punctuation">.</span><span class="token function">log</span><span class="token punctuation">(</span>n<span class="token punctuation">)</span><span class="token punctuation">;</span> <span class="token comment">// Object {a: [1,2,3]}</span>

  <span class="token keyword">for</span> <span class="token punctuation">(</span><span class="token keyword">let</span> n <span class="token keyword">of</span> n<span class="token punctuation">.</span>a<span class="token punctuation">)</span> <span class="token punctuation">{</span> <span class="token comment">// ReferenceError</span>
    console<span class="token punctuation">.</span><span class="token function">log</span><span class="token punctuation">(</span>n<span class="token punctuation">)</span><span class="token punctuation">;</span>
  <span class="token punctuation">}</span>
<span class="token punctuation">}</span>

<span class="token function">go</span><span class="token punctuation">(</span><span class="token punctuation">{</span>a<span class="token punctuation">:</span> <span class="token punctuation">[</span><span class="token number">1</span><span class="token punctuation">,</span> <span class="token number">2</span><span class="token punctuation">,</span> <span class="token number">3</span><span class="token punctuation">]</span><span class="token punctuation">}</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
<span aria-hidden="true" class="line-numbers-rows"><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span></span></code></pre>
<p>Tip：需要注意的是，和<code>let</code>一起引入的<code>const</code>同样拥有“临时死区”的特性，也一样无法重复声明。</p>
</article>
</section>