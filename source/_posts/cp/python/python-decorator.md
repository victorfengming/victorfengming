---
title: "Python中的装饰器:Decorator"
cover: "/img/lynk/55.jpg"
date:       2019-11-28
subtitle: "别样的方式实现面向切面编程"
tags:
	- Python
	- solution
	- interview
	- decorator
---




<article class="_2rhmJa"><h2>理解Python装饰器(Decorator)</h2>
    <p>Python装饰器看起来类似Java中的注解，然鹅和注解并不相同，不过同样能够实现面向切面编程。</p>
    <p>想要理解Python中的装饰器，不得不先理解闭包（closure）这一概念。</p>
    <h3>闭包</h3>
    <p>看看维基百科中的解释：</p>
    <blockquote>
        <p>在计算机科学中，闭包（英语：Closure），又称词法闭包（Lexical Closure）或函数闭包（function
            closures），是引用了自由变量的函数。这个被引用的自由变量将和这个函数一同存在，即使已经离开了创造它的环境也不例外。</p>
    </blockquote>
    <p>官方的解释总是不说人话，but--talk is cheap，show me the code:</p>
    <pre class="line-numbers  language-python"><code class="  language-python"><span class="token comment"># print_msg是外围函数</span>
<span class="token keyword">def</span> <span class="token function">print_msg</span><span
                class="token punctuation">(</span><span class="token punctuation">)</span><span
                class="token punctuation">:</span>
    msg <span class="token operator">=</span> <span class="token string">"I'm closure"</span>

    <span class="token comment"># printer是嵌套函数</span>
    <span class="token keyword">def</span> <span class="token function">printer</span><span
                class="token punctuation">(</span><span class="token punctuation">)</span><span
                class="token punctuation">:</span>
        <span class="token keyword">print</span><span class="token punctuation">(</span>msg<span
                class="token punctuation">)</span>

    <span class="token keyword">return</span> printer


<span class="token comment"># 这里获得的就是一个闭包</span>
closure <span class="token operator">=</span> print_msg<span class="token punctuation">(</span><span
                class="token punctuation">)</span>
<span class="token comment"># 输出 I'm closure</span>
closure<span class="token punctuation">(</span><span class="token punctuation">)</span>
<span aria-hidden="true"
      class="line-numbers-rows"><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span></span></code><button
            class="VJbwyy" type="button" aria-label="复制代码"><i aria-label="icon: copy" class="anticon anticon-copy"><svg
            viewBox="64 64 896 896" focusable="false" class="" data-icon="copy" width="1em" height="1em"
            fill="currentColor" aria-hidden="true"><path
            d="M832 64H296c-4.4 0-8 3.6-8 8v56c0 4.4 3.6 8 8 8h496v688c0 4.4 3.6 8 8 8h56c4.4 0 8-3.6 8-8V96c0-17.7-14.3-32-32-32zM704 192H192c-17.7 0-32 14.3-32 32v530.7c0 8.5 3.4 16.6 9.4 22.6l173.3 173.3c2.2 2.2 4.7 4 7.4 5.5v1.9h4.2c3.5 1.3 7.2 2 11 2H704c17.7 0 32-14.3 32-32V224c0-17.7-14.3-32-32-32zM350 856.2L263.9 770H350v86.2zM664 888H414V746c0-22.1-17.9-40-40-40H232V264h432v624z"></path></svg></i></button></pre>
    <p><code>msg</code>是一个局部变量，在<code>print_msg</code>函数执行之后应该就不会存在了。但是嵌套函数引用了这个变量，将这个局部变量封闭在了嵌套函数中，这样就形成了一个闭包。</p>
    <p>结合这个例子再看维基百科的解释，就清晰明了多了。闭包就是引用了自有变量的函数，这个函数保存了执行的上下文，可以脱离原本的作用域独立存在。</p>
    <p>下面来看看Python中的装饰器。</p>
    <h3>装饰器</h3>
    <p>一个普通的装饰器一般是这样：</p>
    <pre class="line-numbers  language-python"><code class="  language-python"><span class="token keyword">import</span> functools


<span class="token keyword">def</span> <span class="token function">log</span><span class="token punctuation">(</span>func<span
                class="token punctuation">)</span><span class="token punctuation">:</span>
    @functools<span class="token punctuation">.</span>wraps<span class="token punctuation">(</span>func<span
                class="token punctuation">)</span>
    <span class="token keyword">def</span> <span class="token function">wrapper</span><span
                class="token punctuation">(</span><span class="token operator">*</span>args<span
                class="token punctuation">,</span> <span class="token operator">**</span>kwargs<span
                class="token punctuation">)</span><span class="token punctuation">:</span>
        <span class="token keyword">print</span><span class="token punctuation">(</span><span class="token string">'call %s():'</span> <span
                class="token operator">%</span> func<span class="token punctuation">.</span>__name__<span
                class="token punctuation">)</span>
        <span class="token keyword">print</span><span class="token punctuation">(</span><span class="token string">'args = {}'</span><span
                class="token punctuation">.</span><span class="token builtin">format</span><span
                class="token punctuation">(</span><span class="token operator">*</span>args<span
                class="token punctuation">)</span><span class="token punctuation">)</span>
        <span class="token keyword">return</span> func<span class="token punctuation">(</span><span
                class="token operator">*</span>args<span class="token punctuation">,</span> <span
                class="token operator">**</span>kwargs<span class="token punctuation">)</span>

    <span class="token keyword">return</span> wrapper
<span aria-hidden="true"
      class="line-numbers-rows"><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span></span></code><button
            class="VJbwyy" type="button" aria-label="复制代码"><i aria-label="icon: copy" class="anticon anticon-copy"><svg
            viewBox="64 64 896 896" focusable="false" class="" data-icon="copy" width="1em" height="1em"
            fill="currentColor" aria-hidden="true"><path
            d="M832 64H296c-4.4 0-8 3.6-8 8v56c0 4.4 3.6 8 8 8h496v688c0 4.4 3.6 8 8 8h56c4.4 0 8-3.6 8-8V96c0-17.7-14.3-32-32-32zM704 192H192c-17.7 0-32 14.3-32 32v530.7c0 8.5 3.4 16.6 9.4 22.6l173.3 173.3c2.2 2.2 4.7 4 7.4 5.5v1.9h4.2c3.5 1.3 7.2 2 11 2H704c17.7 0 32-14.3 32-32V224c0-17.7-14.3-32-32-32zM350 856.2L263.9 770H350v86.2zM664 888H414V746c0-22.1-17.9-40-40-40H232V264h432v624z"></path></svg></i></button></pre>
    <p>这样就定义了一个打印出方法名及其参数的装饰器。</p>
    <p>调用之：</p>
    <pre class="line-numbers  language-python"><code class="  language-python"><span
            class="token decorator annotation punctuation">@log</span>
<span class="token keyword">def</span> <span class="token function">test</span><span class="token punctuation">(</span>p<span
                class="token punctuation">)</span><span class="token punctuation">:</span>
    <span class="token keyword">print</span><span class="token punctuation">(</span>test<span class="token punctuation">.</span>__name__ <span
                class="token operator">+</span> <span class="token string">" param: "</span> <span
                class="token operator">+</span> p<span class="token punctuation">)</span>
    
test<span class="token punctuation">(</span><span class="token string">"I'm a param"</span><span
                class="token punctuation">)</span>
<span aria-hidden="true"
      class="line-numbers-rows"><span></span><span></span><span></span><span></span><span></span></span></code><button
            class="VJbwyy" type="button" aria-label="复制代码"><i aria-label="icon: copy" class="anticon anticon-copy"><svg
            viewBox="64 64 896 896" focusable="false" class="" data-icon="copy" width="1em" height="1em"
            fill="currentColor" aria-hidden="true"><path
            d="M832 64H296c-4.4 0-8 3.6-8 8v56c0 4.4 3.6 8 8 8h496v688c0 4.4 3.6 8 8 8h56c4.4 0 8-3.6 8-8V96c0-17.7-14.3-32-32-32zM704 192H192c-17.7 0-32 14.3-32 32v530.7c0 8.5 3.4 16.6 9.4 22.6l173.3 173.3c2.2 2.2 4.7 4 7.4 5.5v1.9h4.2c3.5 1.3 7.2 2 11 2H704c17.7 0 32-14.3 32-32V224c0-17.7-14.3-32-32-32zM350 856.2L263.9 770H350v86.2zM664 888H414V746c0-22.1-17.9-40-40-40H232V264h432v624z"></path></svg></i></button></pre>
    <p>输出：</p>
    <pre class="line-numbers  language-bash"><code class="  language-bash">call test():
args = I'm a param
test param: I'm a param
<span aria-hidden="true" class="line-numbers-rows"><span></span><span></span><span></span></span></code><button
            class="VJbwyy" type="button" aria-label="复制代码"><i aria-label="icon: copy" class="anticon anticon-copy"><svg
            viewBox="64 64 896 896" focusable="false" class="" data-icon="copy" width="1em" height="1em"
            fill="currentColor" aria-hidden="true"><path
            d="M832 64H296c-4.4 0-8 3.6-8 8v56c0 4.4 3.6 8 8 8h496v688c0 4.4 3.6 8 8 8h56c4.4 0 8-3.6 8-8V96c0-17.7-14.3-32-32-32zM704 192H192c-17.7 0-32 14.3-32 32v530.7c0 8.5 3.4 16.6 9.4 22.6l173.3 173.3c2.2 2.2 4.7 4 7.4 5.5v1.9h4.2c3.5 1.3 7.2 2 11 2H704c17.7 0 32-14.3 32-32V224c0-17.7-14.3-32-32-32zM350 856.2L263.9 770H350v86.2zM664 888H414V746c0-22.1-17.9-40-40-40H232V264h432v624z"></path></svg></i></button></pre>
    <p>装饰器在使用时，用了<code>@</code>语法，让人有些困扰。其实，装饰器只是个方法，与下面的调用方式没有区别：</p>
    <pre class="line-numbers  language-bash"><code class="  language-bash">def test(p):
    print(test.__name__ + " param: " + p)

wrapper = log(test)
wrapper("I'm a param")
<span aria-hidden="true"
      class="line-numbers-rows"><span></span><span></span><span></span><span></span><span></span></span></code><button
            class="VJbwyy" type="button" aria-label="复制代码"><i aria-label="icon: copy" class="anticon anticon-copy"><svg
            viewBox="64 64 896 896" focusable="false" class="" data-icon="copy" width="1em" height="1em"
            fill="currentColor" aria-hidden="true"><path
            d="M832 64H296c-4.4 0-8 3.6-8 8v56c0 4.4 3.6 8 8 8h496v688c0 4.4 3.6 8 8 8h56c4.4 0 8-3.6 8-8V96c0-17.7-14.3-32-32-32zM704 192H192c-17.7 0-32 14.3-32 32v530.7c0 8.5 3.4 16.6 9.4 22.6l173.3 173.3c2.2 2.2 4.7 4 7.4 5.5v1.9h4.2c3.5 1.3 7.2 2 11 2H704c17.7 0 32-14.3 32-32V224c0-17.7-14.3-32-32-32zM350 856.2L263.9 770H350v86.2zM664 888H414V746c0-22.1-17.9-40-40-40H232V264h432v624z"></path></svg></i></button></pre>
    <p><code>@</code>语法只是将函数传入装饰器函数，并无神奇之处。</p>
    <p>值得注意的是<code>@functools.wraps(func)</code>，这是python提供的装饰器。它能把原函数的元信息拷贝到装饰器里面的 func 函数中。函数的元信息包括docstring、<strong>name</strong>、参数列表等等。可以尝试去除<code>@functools.wraps(func)</code>，你会发现<code>test.__name__</code>的输出变成了wrapper。
    </p>
    <h3>带参数的装饰器</h3>
    <p>装饰器允许传入参数，一个携带了参数的装饰器将有三层函数，如下所示：</p>
    <pre class="line-numbers  language-python"><code class="  language-python"><span class="token keyword">import</span> functools

<span class="token keyword">def</span> <span class="token function">log_with_param</span><span
                class="token punctuation">(</span>text<span class="token punctuation">)</span><span
                class="token punctuation">:</span>
    <span class="token keyword">def</span> <span class="token function">decorator</span><span class="token punctuation">(</span>func<span
                class="token punctuation">)</span><span class="token punctuation">:</span>
        @functools<span class="token punctuation">.</span>wraps<span class="token punctuation">(</span>func<span
                class="token punctuation">)</span>
        <span class="token keyword">def</span> <span class="token function">wrapper</span><span
                class="token punctuation">(</span><span class="token operator">*</span>args<span
                class="token punctuation">,</span> <span class="token operator">**</span>kwargs<span
                class="token punctuation">)</span><span class="token punctuation">:</span>
            <span class="token keyword">print</span><span class="token punctuation">(</span><span class="token string">'call %s():'</span> <span
                class="token operator">%</span> func<span class="token punctuation">.</span>__name__<span
                class="token punctuation">)</span>
            <span class="token keyword">print</span><span class="token punctuation">(</span><span class="token string">'args = {}'</span><span
                class="token punctuation">.</span><span class="token builtin">format</span><span
                class="token punctuation">(</span><span class="token operator">*</span>args<span
                class="token punctuation">)</span><span class="token punctuation">)</span>
            <span class="token keyword">print</span><span class="token punctuation">(</span><span class="token string">'log_param = {}'</span><span
                class="token punctuation">.</span><span class="token builtin">format</span><span
                class="token punctuation">(</span>text<span class="token punctuation">)</span><span
                class="token punctuation">)</span>
            <span class="token keyword">return</span> func<span class="token punctuation">(</span><span
                class="token operator">*</span>args<span class="token punctuation">,</span> <span
                class="token operator">**</span>kwargs<span class="token punctuation">)</span>

        <span class="token keyword">return</span> wrapper

    <span class="token keyword">return</span> decorator
    
@log_with_param<span class="token punctuation">(</span><span class="token string">"param"</span><span
                class="token punctuation">)</span>
<span class="token keyword">def</span> <span class="token function">test_with_param</span><span
                class="token punctuation">(</span>p<span class="token punctuation">)</span><span
                class="token punctuation">:</span>
    <span class="token keyword">print</span><span class="token punctuation">(</span>test_with_param<span
                class="token punctuation">.</span>__name__<span class="token punctuation">)</span>
<span aria-hidden="true"
      class="line-numbers-rows"><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span></span></code><button
            class="VJbwyy" type="button" aria-label="复制代码"><i aria-label="icon: copy" class="anticon anticon-copy"><svg
            viewBox="64 64 896 896" focusable="false" class="" data-icon="copy" width="1em" height="1em"
            fill="currentColor" aria-hidden="true"><path
            d="M832 64H296c-4.4 0-8 3.6-8 8v56c0 4.4 3.6 8 8 8h496v688c0 4.4 3.6 8 8 8h56c4.4 0 8-3.6 8-8V96c0-17.7-14.3-32-32-32zM704 192H192c-17.7 0-32 14.3-32 32v530.7c0 8.5 3.4 16.6 9.4 22.6l173.3 173.3c2.2 2.2 4.7 4 7.4 5.5v1.9h4.2c3.5 1.3 7.2 2 11 2H704c17.7 0 32-14.3 32-32V224c0-17.7-14.3-32-32-32zM350 856.2L263.9 770H350v86.2zM664 888H414V746c0-22.1-17.9-40-40-40H232V264h432v624z"></path></svg></i></button></pre>
    <p>看到这个代码是不是又有些疑问，内层的decorator函数的参数func是怎么传进去的？和上面一般的装饰器不大一样啊。</p>
    <p>其实道理是一样的，将其<code>@</code>语法去除，恢复函数调用的形式一看就明白了：</p>
    <pre class="line-numbers  language-bash"><code class="  language-bash"># 传入装饰器的参数，并接收返回的decorator函数
decorator = log_with_param("param")
# 传入test_with_param函数
wrapper = decorator(test_with_param)
# 调用装饰器函数
wrapper("I'm a param")
<span aria-hidden="true"
      class="line-numbers-rows"><span></span><span></span><span></span><span></span><span></span><span></span></span></code><button
            class="VJbwyy" type="button" aria-label="复制代码"><i aria-label="icon: copy" class="anticon anticon-copy"><svg
            viewBox="64 64 896 896" focusable="false" class="" data-icon="copy" width="1em" height="1em"
            fill="currentColor" aria-hidden="true"><path
            d="M832 64H296c-4.4 0-8 3.6-8 8v56c0 4.4 3.6 8 8 8h496v688c0 4.4 3.6 8 8 8h56c4.4 0 8-3.6 8-8V96c0-17.7-14.3-32-32-32zM704 192H192c-17.7 0-32 14.3-32 32v530.7c0 8.5 3.4 16.6 9.4 22.6l173.3 173.3c2.2 2.2 4.7 4 7.4 5.5v1.9h4.2c3.5 1.3 7.2 2 11 2H704c17.7 0 32-14.3 32-32V224c0-17.7-14.3-32-32-32zM350 856.2L263.9 770H350v86.2zM664 888H414V746c0-22.1-17.9-40-40-40H232V264h432v624z"></path></svg></i></button></pre>
    <p>输出结果与正常使用装饰器相同：</p>
    <pre class="line-numbers  language-rust"><code class="  language-rust">call <span class="token function">test_with_param</span><span
            class="token punctuation">(</span><span class="token punctuation">)</span><span
            class="token punctuation">:</span>
args <span class="token operator">=</span> I<span class="token lifetime-annotation symbol">'m</span> a param
log_param <span class="token operator">=</span> param
test_with_param
<span aria-hidden="true" class="line-numbers-rows"><span></span><span></span><span></span><span></span></span></code><button
            class="VJbwyy" type="button" aria-label="复制代码"><i aria-label="icon: copy" class="anticon anticon-copy"><svg
            viewBox="64 64 896 896" focusable="false" class="" data-icon="copy" width="1em" height="1em"
            fill="currentColor" aria-hidden="true"><path
            d="M832 64H296c-4.4 0-8 3.6-8 8v56c0 4.4 3.6 8 8 8h496v688c0 4.4 3.6 8 8 8h56c4.4 0 8-3.6 8-8V96c0-17.7-14.3-32-32-32zM704 192H192c-17.7 0-32 14.3-32 32v530.7c0 8.5 3.4 16.6 9.4 22.6l173.3 173.3c2.2 2.2 4.7 4 7.4 5.5v1.9h4.2c3.5 1.3 7.2 2 11 2H704c17.7 0 32-14.3 32-32V224c0-17.7-14.3-32-32-32zM350 856.2L263.9 770H350v86.2zM664 888H414V746c0-22.1-17.9-40-40-40H232V264h432v624z"></path></svg></i></button></pre>
    <p>至此，装饰器这个有点费解的特性也没什么神秘了。</p>
    <p>装饰器这一语法体现了Python中函数是第一公民，函数是对象、是变量，可以作为参数、可以是返回值，非常的灵活与强大。</p>
    <p>Python中引入了很多函数式编程的特性，需要好好学习与体会。</p>
</article>