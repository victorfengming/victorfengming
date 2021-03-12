---
title: "Vue指令大全"
date:       2019-09-15
tags:
	- web
	- vue
	- basis
---


  <section class="ouvJEz">
   <h1 class="_1RuRku">Vue指令大全</h1>
   <div class="rEsl9f">
    <div class="s-dsoj">
     <span class="_3tCVn5"><i aria-label="ic-diamond" class="anticon">
       <svg width="1em" height="1em" fill="currentColor" aria-hidden="true" focusable="false" class="">
        <use xlink:href="#ic-diamond"></use>
       </svg></i><span>2</span></span>
     <time datetime="2018-06-06T04:49:13.000Z">2018.06.06 12:49:13</time>
     <span>字数 1222</span>
     <span>阅读 28624</span>
    </div>
   </div>
   <article class="_2rhmJa">
    <p><h3>1. v-text</h3><br /> v-text主要用来更新textContent，可以等同于JS的text属性。</p> 
    <pre class="line-numbers  language-xml"><code class="  language-xml"><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>span</span> <span class="token attr-name">v-text</span><span class="token attr-value"><span class="token punctuation">=</span><span class="token punctuation">&quot;</span>msg<span class="token punctuation">&quot;</span></span><span class="token punctuation">&gt;</span></span><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>span</span><span class="token punctuation">&gt;</span></span>
<span aria-hidden="true" class="line-numbers-rows"><span></span></span></code></pre> 
    <p>这两者等价：</p> 
    <pre class="line-numbers  language-xml"><code class="  language-xml"><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>span</span><span class="token punctuation">&gt;</span></span>{{msg}}<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>span</span><span class="token punctuation">&gt;</span></span>
<span aria-hidden="true" class="line-numbers-rows"><span></span></span></code></pre> 
    <hr /> 
    <p><h3>2. v-html</h3><br /> 双大括号的方式会将数据解释为纯文本，而非HTML。为了输出真正的HTML，可以用v-html指令。它等同于JS的innerHtml属性。</p> 
    <pre class="line-numbers  language-xml"><code class="  language-xml"><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>div</span> <span class="token attr-name">v-html</span><span class="token attr-value"><span class="token punctuation">=</span><span class="token punctuation">&quot;</span>rawHtml<span class="token punctuation">&quot;</span></span><span class="token punctuation">&gt;</span></span><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>div</span><span class="token punctuation">&gt;</span></span>
<span aria-hidden="true" class="line-numbers-rows"><span></span></span></code></pre> 
    <p>这个div的内容将会替换成属性值rawHtml，直接作为HTML进行渲染。</p> 
    <hr /> 
    <p><h3>3. v-pre</h3><br /> v-pre主要用来跳过这个元素和它的子元素编译过程。可以用来显示原始的Mustache标签。跳过大量没有指令的节点加快编译。</p> 
    <pre class="line-numbers  language-jsx"><code class="  language-jsx"><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>div</span> <span class="token attr-name">id</span><span class="token attr-value"><span class="token punctuation">=</span><span class="token punctuation">&quot;</span>app<span class="token punctuation">&quot;</span></span><span class="token punctuation">&gt;</span></span><span class="token plain-text">
    </span><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>span</span> <span class="token attr-name">v-pre</span><span class="token punctuation">&gt;</span></span><span class="token punctuation">{</span><span class="token punctuation">{</span>message<span class="token punctuation">}</span><span class="token punctuation">}</span><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>span</span><span class="token punctuation">&gt;</span></span><span class="token plain-text">  //这条语句不进行编译
    </span><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>span</span><span class="token punctuation">&gt;</span></span><span class="token punctuation">{</span><span class="token punctuation">{</span>message<span class="token punctuation">}</span><span class="token punctuation">}</span><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>span</span><span class="token punctuation">&gt;</span></span><span class="token plain-text">
</span><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>div</span><span class="token punctuation">&gt;</span></span>
<span aria-hidden="true" class="line-numbers-rows"><span></span><span></span><span></span><span></span></span></code></pre> 
    <p>最终仅显示第二个span的内容</p> 
    <hr /> 
    <p><h3>4. v-cloak</h3><br /> 这个指令是用来保持在元素上直到关联实例结束时进行编译。</p> 
    <pre class="line-numbers  language-xml"><code class="  language-xml"><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>div</span> <span class="token attr-name">id</span><span class="token attr-value"><span class="token punctuation">=</span><span class="token punctuation">&quot;</span>app<span class="token punctuation">&quot;</span></span> <span class="token attr-name">v-cloak</span><span class="token punctuation">&gt;</span></span>
    <span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>div</span><span class="token punctuation">&gt;</span></span>
        {{message}}
    <span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>div</span><span class="token punctuation">&gt;</span></span>
<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>div</span><span class="token punctuation">&gt;</span></span>
<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>script</span> <span class="token attr-name">type</span><span class="token attr-value"><span class="token punctuation">=</span><span class="token punctuation">&quot;</span>text/javascript<span class="token punctuation">&quot;</span></span><span class="token punctuation">&gt;</span></span>
    new Vue({
      el:'#app',
      data:{
        message:'hello world'
      }
    })
<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>script</span><span class="token punctuation">&gt;</span></span>
<span aria-hidden="true" class="line-numbers-rows"><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span></span></code></pre> 
    <p>在页面加载时会闪烁，先显示:</p> 
    <pre class="line-numbers  language-xml"><code class="  language-xml"><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>div</span><span class="token punctuation">&gt;</span></span>
    {{message}}
<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>div</span><span class="token punctuation">&gt;</span></span>
<span aria-hidden="true" class="line-numbers-rows"><span></span><span></span><span></span></span></code></pre> 
    <p>然后才会编译为：</p> 
    <pre class="line-numbers  language-xml"><code class="  language-xml"><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>div</span><span class="token punctuation">&gt;</span></span>
    hello world!
<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>div</span><span class="token punctuation">&gt;</span></span>
<span aria-hidden="true" class="line-numbers-rows"><span></span><span></span><span></span></span></code></pre> 
    <hr /> 
    <p><h3>5. v-once</h3><br /> v-once关联的实例，只会渲染一次。之后的重新渲染，实例极其所有的子节点将被视为静态内容跳过，这可以用于优化更新性能。</p> 
    <pre class="line-numbers  language-xml"><code class="  language-xml"><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>span</span> <span class="token attr-name">v-once</span><span class="token punctuation">&gt;</span></span>This will never change:{{msg}}<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>span</span><span class="token punctuation">&gt;</span></span>  //单个元素
<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>div</span> <span class="token attr-name">v-once</span><span class="token punctuation">&gt;</span></span>//有子元素
    <span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>h1</span><span class="token punctuation">&gt;</span></span>comment<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>h1</span><span class="token punctuation">&gt;</span></span>
    <span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>p</span><span class="token punctuation">&gt;</span></span>{{msg}}<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>p</span><span class="token punctuation">&gt;</span></span>
<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>div</span><span class="token punctuation">&gt;</span></span>
<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>my-component</span> <span class="token attr-name"><span class="token namespace">v-once:</span>comment</span><span class="token attr-value"><span class="token punctuation">=</span><span class="token punctuation">&quot;</span>msg<span class="token punctuation">&quot;</span></span><span class="token punctuation">&gt;</span></span><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>my-component</span><span class="token punctuation">&gt;</span></span>  //组件
<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>ul</span><span class="token punctuation">&gt;</span></span>
    <span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>li</span> <span class="token attr-name">v-for</span><span class="token attr-value"><span class="token punctuation">=</span><span class="token punctuation">&quot;</span>i in list<span class="token punctuation">&quot;</span></span><span class="token punctuation">&gt;</span></span>{{i}}<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>li</span><span class="token punctuation">&gt;</span></span>
<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>ul</span><span class="token punctuation">&gt;</span></span>
<span aria-hidden="true" class="line-numbers-rows"><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span></span></code></pre> 
    <p>上面的例子中，msg,list即使产生改变，也不会重新渲染。</p> 
    <hr /> 
    <p><h3>6. v-if</h3><br /> v-if可以实现条件渲染，Vue会根据表达式的值的真假条件来渲染元素。</p> 
    <pre class="line-numbers  language-xml"><code class="  language-xml"><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>a</span> <span class="token attr-name">v-if</span><span class="token attr-value"><span class="token punctuation">=</span><span class="token punctuation">&quot;</span>ok<span class="token punctuation">&quot;</span></span><span class="token punctuation">&gt;</span></span>yes<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>a</span><span class="token punctuation">&gt;</span></span>
<span aria-hidden="true" class="line-numbers-rows"><span></span></span></code></pre> 
    <p>如果属性值ok为true，则显示。否则，不会渲染这个元素。</p> 
    <hr /> 
    <p><h3>7. v-else</h3><br /> v-else是搭配v-if使用的，它必须紧跟在v-if或者v-else-if后面，否则不起作用。</p> 
    <pre class="line-numbers  language-xml"><code class="  language-xml"><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>a</span> <span class="token attr-name">v-if</span><span class="token attr-value"><span class="token punctuation">=</span><span class="token punctuation">&quot;</span>ok<span class="token punctuation">&quot;</span></span><span class="token punctuation">&gt;</span></span>yes<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>a</span><span class="token punctuation">&gt;</span></span>
<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>a</span> <span class="token attr-name">v-else</span><span class="token punctuation">&gt;</span></span>No<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>a</span><span class="token punctuation">&gt;</span></span>
<span aria-hidden="true" class="line-numbers-rows"><span></span><span></span></span></code></pre> 
    <hr /> 
    <p><h3>8. v-else-if</h3><br /> v-else-if充当v-if的else-if块，可以链式的使用多次。可以更加方便的实现switch语句。</p> 
    <pre class="line-numbers  language-xml"><code class="  language-xml"><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>div</span> <span class="token attr-name">v-if</span><span class="token attr-value"><span class="token punctuation">=</span><span class="token punctuation">&quot;</span>type==='A'<span class="token punctuation">&quot;</span></span><span class="token punctuation">&gt;</span></span>
    A
<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>div</span><span class="token punctuation">&gt;</span></span>
<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>div</span> <span class="token attr-name">v-if</span><span class="token attr-value"><span class="token punctuation">=</span><span class="token punctuation">&quot;</span>type==='B'<span class="token punctuation">&quot;</span></span><span class="token punctuation">&gt;</span></span>
    B
<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>div</span><span class="token punctuation">&gt;</span></span>
<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>div</span> <span class="token attr-name">v-if</span><span class="token attr-value"><span class="token punctuation">=</span><span class="token punctuation">&quot;</span>type==='C'<span class="token punctuation">&quot;</span></span><span class="token punctuation">&gt;</span></span>
    C
<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>div</span><span class="token punctuation">&gt;</span></span>
<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>div</span> <span class="token attr-name">v-else</span><span class="token punctuation">&gt;</span></span>
    Not A,B,C
<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>div</span><span class="token punctuation">&gt;</span></span>
<span aria-hidden="true" class="line-numbers-rows"><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span></span></code></pre> 
    <hr /> 
    <p><h3>9. v-show</h3><br /></p> 
    <pre class="line-numbers  language-xml"><code class="  language-xml"><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>h1</span> <span class="token attr-name">v-show</span><span class="token attr-value"><span class="token punctuation">=</span><span class="token punctuation">&quot;</span>ok<span class="token punctuation">&quot;</span></span><span class="token punctuation">&gt;</span></span>hello world<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>h1</span><span class="token punctuation">&gt;</span></span>
<span aria-hidden="true" class="line-numbers-rows"><span></span></span></code></pre> 
    <p>也是用于根据条件展示元素。和v-if不同的是，如果v-if的值是false，则这个元素被销毁，不在dom中。但是v-show的元素会始终被渲染并保存在dom中，它只是简单的切换css的dispaly属性。</p> 
    <blockquote> 
     <p>注意：v-if有更高的切换开销<br /> v-show有更高的初始渲染开销。<br /> 因此，如果要非常频繁的切换，则使用v-show较好；如果在运行时条件不太可能改变，则v-if较好</p> 
    </blockquote> 
    <hr /> 
    <p><h3>10. v-for</h3><br /> 用v-for指令根据遍历数组来进行渲染<br /> 有下面两种遍历形式</p> 
    <pre class="line-numbers  language-jsx"><code class="  language-jsx"><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>div</span> <span class="token attr-name">v-for</span><span class="token attr-value"><span class="token punctuation">=</span><span class="token punctuation">&quot;</span>(item,index) in items<span class="token punctuation">&quot;</span></span><span class="token punctuation">&gt;</span></span><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>div</span><span class="token punctuation">&gt;</span></span>   <span class="token comment">//使用in，index是一个可选参数，表示当前项的索引</span>
<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>div</span> <span class="token attr-name">v-for</span><span class="token attr-value"><span class="token punctuation">=</span><span class="token punctuation">&quot;</span>item of items<span class="token punctuation">&quot;</span></span><span class="token punctuation">&gt;</span></span><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>div</span><span class="token punctuation">&gt;</span></span>   <span class="token comment">//使用of</span>
<span aria-hidden="true" class="line-numbers-rows"><span></span><span></span></span></code></pre> 
    <p>下面是一个例子，并且在v-for中，拥有对父作用域属性的完全访问权限。</p> 
    <pre class="line-numbers  language-xml"><code class="  language-xml"><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>ul</span> <span class="token attr-name">id</span><span class="token attr-value"><span class="token punctuation">=</span><span class="token punctuation">&quot;</span>app<span class="token punctuation">&quot;</span></span><span class="token punctuation">&gt;</span></span>
    <span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>li</span> <span class="token attr-name">v-for</span><span class="token attr-value"><span class="token punctuation">=</span><span class="token punctuation">&quot;</span>item in items<span class="token punctuation">&quot;</span></span><span class="token punctuation">&gt;</span></span>
        {{parent}}-{{item.text}}
    <span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>li</span><span class="token punctuation">&gt;</span></span>
<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>ul</span><span class="token punctuation">&gt;</span></span>
<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>script</span> <span class="token attr-name">type</span><span class="token attr-value"><span class="token punctuation">=</span><span class="token punctuation">&quot;</span>text/javascript<span class="token punctuation">&quot;</span></span><span class="token punctuation">&gt;</span></span>
    var example = new Vue({
      el:'#app',
      data:{
        parent:'父作用域'
        items:[
          {text:'文本1'},
          {text:'文本2'}
        ]
      }
    })
<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>script</span><span class="token punctuation">&gt;</span></span>
<span aria-hidden="true" class="line-numbers-rows"><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span></span></code></pre> 
    <p>会被渲染为：</p> 
    <pre class="line-numbers  language-xml"><code class="  language-xml"><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>ul</span> <span class="token attr-name">id</span><span class="token attr-value"><span class="token punctuation">=</span><span class="token punctuation">&quot;</span>app<span class="token punctuation">&quot;</span></span><span class="token punctuation">&gt;</span></span>
    <span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>li</span><span class="token punctuation">&gt;</span></span>父作用域-文本1<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>li</span><span class="token punctuation">&gt;</span></span>
    <span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>li</span><span class="token punctuation">&gt;</span></span>父作用域-文本2<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>li</span><span class="token punctuation">&gt;</span></span>
<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>ul</span><span class="token punctuation">&gt;</span></span>
<span aria-hidden="true" class="line-numbers-rows"><span></span><span></span><span></span><span></span></span></code></pre> 
    <blockquote> 
     <p><strong>注意：当v-for和v-if同处于一个节点时，v-for的优先级比v-if更高。这意味着v-if将运行在每个v-for循环中</strong></p> 
    </blockquote> 
    <hr /> 
    <p><h3>11. v-bind</h3><br /> v-bind用来<strong>动态的绑定一个或者多个特性</strong>。没有参数时，可以绑定到一个包含键值对的对象。常用于动态绑定class和style。以及href等。<br /> 简写为一个冒号【 <strong>：</strong>】</p> 
    <p><strong>&lt;1&gt;对象语法</strong>：</p> 
    <pre class="line-numbers  language-jsx"><code class="  language-jsx"><span class="token comment">//进行类切换的例子</span>
<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>div</span> <span class="token attr-name">id</span><span class="token attr-value"><span class="token punctuation">=</span><span class="token punctuation">&quot;</span>app<span class="token punctuation">&quot;</span></span><span class="token punctuation">&gt;</span></span><span class="token plain-text">
    &lt;!--当data里面定义的isActive等于true时，is-active这个类才会被添加起作用--&gt;
    &lt;!--当data里面定义的hasError等于true时，text-danger这个类才会被添加起作用--&gt;
    </span><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>div</span> <span class="token attr-name">:class</span><span class="token attr-value"><span class="token punctuation">=</span><span class="token punctuation">&quot;</span>{'is-active':isActive, 'text-danger':hasError}<span class="token punctuation">&quot;</span></span><span class="token punctuation">&gt;</span></span><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>div</span><span class="token punctuation">&gt;</span></span><span class="token plain-text">
</span><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>div</span><span class="token punctuation">&gt;</span></span>
<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>script</span><span class="token punctuation">&gt;</span></span><span class="token plain-text">
    var app = new Vue({
        el: '#app',
        data: {
            isActive: true,  
            hasError: false
        }
    })
</span><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>script</span><span class="token punctuation">&gt;</span></span>
<span aria-hidden="true" class="line-numbers-rows"><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span></span></code></pre> 
    <p>渲染结果：</p> 
    <pre class="line-numbers  language-xml"><code class="  language-xml"><span class="token comment">&lt;!--因为hasError: false，所以text-danger不被渲染--&gt;</span>
<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>div</span> <span class="token attr-name">class</span> <span class="token attr-value"><span class="token punctuation">=</span> <span class="token punctuation">&quot;</span>is-active<span class="token punctuation">&quot;</span></span><span class="token punctuation">&gt;</span></span><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>div</span><span class="token punctuation">&gt;</span></span>
<span aria-hidden="true" class="line-numbers-rows"><span></span><span></span></span></code></pre> 
    <p><strong>&lt;2&gt;数组语法</strong></p> 
    <pre class="line-numbers  language-xml"><code class="  language-xml"><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>div</span> <span class="token attr-name">id</span><span class="token attr-value"><span class="token punctuation">=</span><span class="token punctuation">&quot;</span>app<span class="token punctuation">&quot;</span></span><span class="token punctuation">&gt;</span></span>
    <span class="token comment">&lt;!--数组语法：errorClass在data对应的类一定会添加--&gt;</span>
    <span class="token comment">&lt;!--is-active是对象语法，根据activeClass对应的取值决定是否添加--&gt;</span>
    <span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>p</span> <span class="token attr-name">:class</span><span class="token attr-value"><span class="token punctuation">=</span><span class="token punctuation">&quot;</span>[{'is-active':activeClass},errorClass]<span class="token punctuation">&quot;</span></span><span class="token punctuation">&gt;</span></span>12345<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>p</span><span class="token punctuation">&gt;</span></span>
<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>div</span><span class="token punctuation">&gt;</span></span>
<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>script</span><span class="token punctuation">&gt;</span></span>
    var app = new Vue({
        el: '#app',
        data: {
            activeClass: false,
            errorClass: 'text-danger'
        }
    })
<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>script</span><span class="token punctuation">&gt;</span></span>
<span aria-hidden="true" class="line-numbers-rows"><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span></span></code></pre> 
    <p>渲染结果：</p> 
    <pre class="line-numbers  language-xml"><code class="  language-xml"><span class="token comment">&lt;!--因为activeClass: false，所以is-active不被渲染--&gt;</span>
<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>p</span> <span class="token attr-name">class</span> <span class="token attr-value"><span class="token punctuation">=</span> <span class="token punctuation">&quot;</span>text-danger<span class="token punctuation">&quot;</span></span><span class="token punctuation">&gt;</span></span><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>p</span><span class="token punctuation">&gt;</span></span>
<span aria-hidden="true" class="line-numbers-rows"><span></span><span></span></span></code></pre> 
    <p><strong>&lt;3&gt;直接绑定数据对象</strong></p> 
    <pre class="line-numbers  language-xml"><code class="  language-xml"><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>div</span> <span class="token attr-name">id</span><span class="token attr-value"><span class="token punctuation">=</span><span class="token punctuation">&quot;</span>app<span class="token punctuation">&quot;</span></span><span class="token punctuation">&gt;</span></span>
    <span class="token comment">&lt;!--在vue实例的data中定义了classObject对象，这个对象里面是所有类名及其真值--&gt;</span>
    <span class="token comment">&lt;!--当里面的类的值是true时会被渲染--&gt;</span>
    <span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>div</span> <span class="token attr-name">:class</span><span class="token attr-value"><span class="token punctuation">=</span><span class="token punctuation">&quot;</span>classObject<span class="token punctuation">&quot;</span></span><span class="token punctuation">&gt;</span></span>12345<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>div</span><span class="token punctuation">&gt;</span></span>
<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>div</span><span class="token punctuation">&gt;</span></span>
<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>script</span><span class="token punctuation">&gt;</span></span>
    var app = new Vue({
        el: '#app',
        data: {
            classObject:{
                'is-active': false,
                'text-danger':true
            }           
        }
    })
<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>script</span><span class="token punctuation">&gt;</span></span>
<span aria-hidden="true" class="line-numbers-rows"><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span></span></code></pre> 
    <p>渲染结果：</p> 
    <pre class="line-numbers  language-xml"><code class="  language-xml"><span class="token comment">&lt;!--因为'is-active': false，所以is-active不被渲染--&gt;</span>
<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>div</span> <span class="token attr-name">class</span> <span class="token attr-value"><span class="token punctuation">=</span> <span class="token punctuation">&quot;</span>text-danger<span class="token punctuation">&quot;</span></span><span class="token punctuation">&gt;</span></span><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>div</span><span class="token punctuation">&gt;</span></span>
<span aria-hidden="true" class="line-numbers-rows"><span></span><span></span></span></code></pre> 
    <hr /> 
    <p><h3>12. v-model</h3><br /> 这个指令用于在表单上创建<strong>双向数据绑定</strong>。<br /> v-model会忽略所有表单元素的value、checked、selected特性的初始值。因为它选择Vue实例数据做为具体的值。</p> 
    <pre class="line-numbers  language-xml"><code class="  language-xml"><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>div</span> <span class="token attr-name">id</span><span class="token attr-value"><span class="token punctuation">=</span><span class="token punctuation">&quot;</span>app<span class="token punctuation">&quot;</span></span><span class="token punctuation">&gt;</span></span>
    <span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>input</span> <span class="token attr-name">v-model</span><span class="token attr-value"><span class="token punctuation">=</span><span class="token punctuation">&quot;</span>somebody<span class="token punctuation">&quot;</span></span><span class="token punctuation">&gt;</span></span>
    <span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>p</span><span class="token punctuation">&gt;</span></span>hello {{somebody}}<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>p</span><span class="token punctuation">&gt;</span></span>
<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>div</span><span class="token punctuation">&gt;</span></span>
<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>script</span><span class="token punctuation">&gt;</span></span>
    var app = new Vue({
        el: '#app',
        data: {
            somebody:'小明'
        }
    })
<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>script</span><span class="token punctuation">&gt;</span></span>
<span aria-hidden="true" class="line-numbers-rows"><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span></span></code></pre> 
    <p>这个例子中直接在浏览器input中输入别的名字，下面的p的内容会直接跟着变。这就是双向数据绑定。</p> 
    <p><strong>v-model修饰符</strong><br /> <strong>&lt;1&gt; .lazy</strong><br /> 默认情况下，v-model同步输入框的值和数据。可以通过这个修饰符，转变为在change事件再同步。</p> 
    <pre class="line-numbers  language-xml"><code class="  language-xml"><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>input</span> <span class="token attr-name">v-model.lazy</span><span class="token attr-value"><span class="token punctuation">=</span><span class="token punctuation">&quot;</span>msg<span class="token punctuation">&quot;</span></span><span class="token punctuation">&gt;</span></span>
<span aria-hidden="true" class="line-numbers-rows"><span></span></span></code></pre> 
    <p><strong>&lt;2&gt; .number</strong><br /> 自动将用户的输入值转化为数值类型</p> 
    <pre class="line-numbers  language-xml"><code class="  language-xml"><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>input</span> <span class="token attr-name">v-model.number</span><span class="token attr-value"><span class="token punctuation">=</span><span class="token punctuation">&quot;</span>msg<span class="token punctuation">&quot;</span></span><span class="token punctuation">&gt;</span></span>
<span aria-hidden="true" class="line-numbers-rows"><span></span></span></code></pre> 
    <p><strong>&lt;3&gt; .trim</strong><br /> 自动过滤用户输入的首尾空格</p> 
    <pre class="line-numbers  language-xml"><code class="  language-xml"><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>input</span> <span class="token attr-name">v-model.trim</span><span class="token attr-value"><span class="token punctuation">=</span><span class="token punctuation">&quot;</span>msg<span class="token punctuation">&quot;</span></span><span class="token punctuation">&gt;</span></span>
<span aria-hidden="true" class="line-numbers-rows"><span></span></span></code></pre> 
    <hr /> 
    <p><h3>13. v-on</h3><br /> v-on主要用来监听dom事件，以便执行一些代码块。表达式可以是一个方法名。<br /> 简写为：【 <strong>@</strong> 】</p> 
    <pre class="line-numbers  language-xml"><code class="  language-xml"><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>div</span> <span class="token attr-name">id</span><span class="token attr-value"><span class="token punctuation">=</span><span class="token punctuation">&quot;</span>app<span class="token punctuation">&quot;</span></span><span class="token punctuation">&gt;</span></span>
    <span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>button</span> <span class="token attr-name">@click</span><span class="token attr-value"><span class="token punctuation">=</span><span class="token punctuation">&quot;</span>consoleLog<span class="token punctuation">&quot;</span></span><span class="token punctuation">&gt;</span></span><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>button</span><span class="token punctuation">&gt;</span></span>
<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>div</span><span class="token punctuation">&gt;</span></span>
<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>script</span><span class="token punctuation">&gt;</span></span>
    var app = new Vue({
        el: '#app',
        methods:{
            consoleLog:function (event) {
                console.log(1)
            }
        }
    })
<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>script</span><span class="token punctuation">&gt;</span></span>
<span aria-hidden="true" class="line-numbers-rows"><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span></span></code></pre> 
    <p><strong>事件修饰符</strong></p> 
    <ul> 
     <li> <code>.stop</code> 阻止事件继续传播</li> 
     <li> <code>.prevent</code> 事件不再重载页面</li> 
     <li> <code>.capture</code> 使用事件捕获模式,即元素自身触发的事件先在此处处理，然后才交由内部元素进行处理</li> 
     <li> <code>.self</code> 只当在 event.target 是当前元素自身时触发处理函数</li> 
     <li> <code>.once</code> 事件将只会触发一次</li> 
     <li> <code>.passive</code> 告诉浏览器你不想阻止事件的默认行为</li> 
    </ul> 
    <pre class="line-numbers  language-xml"><code class="  language-xml"><span class="token comment">&lt;!-- 阻止单击事件继续传播 --&gt;</span>
<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>a</span> <span class="token attr-name"><span class="token namespace">v-on:</span>click.stop</span><span class="token attr-value"><span class="token punctuation">=</span><span class="token punctuation">&quot;</span>doThis<span class="token punctuation">&quot;</span></span><span class="token punctuation">&gt;</span></span><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>a</span><span class="token punctuation">&gt;</span></span>

<span class="token comment">&lt;!-- 提交事件不再重载页面 --&gt;</span>
<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>form</span> <span class="token attr-name"><span class="token namespace">v-on:</span>submit.prevent</span><span class="token attr-value"><span class="token punctuation">=</span><span class="token punctuation">&quot;</span>onSubmit<span class="token punctuation">&quot;</span></span><span class="token punctuation">&gt;</span></span><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>form</span><span class="token punctuation">&gt;</span></span>

<span class="token comment">&lt;!-- 修饰符可以串联 --&gt;</span>
<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>a</span> <span class="token attr-name"><span class="token namespace">v-on:</span>click.stop.prevent</span><span class="token attr-value"><span class="token punctuation">=</span><span class="token punctuation">&quot;</span>doThat<span class="token punctuation">&quot;</span></span><span class="token punctuation">&gt;</span></span><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>a</span><span class="token punctuation">&gt;</span></span>

<span class="token comment">&lt;!-- 只有修饰符 --&gt;</span>
<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>form</span> <span class="token attr-name"><span class="token namespace">v-on:</span>submit.prevent</span><span class="token punctuation">&gt;</span></span><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>form</span><span class="token punctuation">&gt;</span></span>

<span class="token comment">&lt;!-- 添加事件监听器时使用事件捕获模式 --&gt;</span>
<span class="token comment">&lt;!-- 即元素自身触发的事件先在此处处理，然后才交由内部元素进行处理 --&gt;</span>
<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>div</span> <span class="token attr-name"><span class="token namespace">v-on:</span>click.capture</span><span class="token attr-value"><span class="token punctuation">=</span><span class="token punctuation">&quot;</span>doThis<span class="token punctuation">&quot;</span></span><span class="token punctuation">&gt;</span></span>...<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>div</span><span class="token punctuation">&gt;</span></span>

<span class="token comment">&lt;!-- 只当在 event.target 是当前元素自身时触发处理函数 --&gt;</span>
<span class="token comment">&lt;!-- 即事件不是从内部元素触发的 --&gt;</span>
<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>div</span> <span class="token attr-name"><span class="token namespace">v-on:</span>click.self</span><span class="token attr-value"><span class="token punctuation">=</span><span class="token punctuation">&quot;</span>doThat<span class="token punctuation">&quot;</span></span><span class="token punctuation">&gt;</span></span>...<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>div</span><span class="token punctuation">&gt;</span></span>

<span class="token comment">&lt;!-- 点击事件将只会触发一次 --&gt;</span>
<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>a</span> <span class="token attr-name"><span class="token namespace">v-on:</span>click.once</span><span class="token attr-value"><span class="token punctuation">=</span><span class="token punctuation">&quot;</span>doThis<span class="token punctuation">&quot;</span></span><span class="token punctuation">&gt;</span></span><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>a</span><span class="token punctuation">&gt;</span></span>

<span class="token comment">&lt;!-- 滚动事件的默认行为 (即滚动行为) 将会立即触发 --&gt;</span>
<span class="token comment">&lt;!-- 而不会等待 `onScroll` 完成  --&gt;</span>
<span class="token comment">&lt;!-- 这其中包含 `event.preventDefault()` 的情况 --&gt;</span>
<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>div</span> <span class="token attr-name"><span class="token namespace">v-on:</span>scroll.passive</span><span class="token attr-value"><span class="token punctuation">=</span><span class="token punctuation">&quot;</span>onScroll<span class="token punctuation">&quot;</span></span><span class="token punctuation">&gt;</span></span>...<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>div</span><span class="token punctuation">&gt;</span></span>
<span aria-hidden="true" class="line-numbers-rows"><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span></span></code></pre> 
    <blockquote> 
     <p>使用修饰符时，顺序很重要；相应的代码会以同样的顺序产生。因此，用<code>v-on:click.prevent.self</code>会<strong>阻止所有的点击</strong>，而 <code>v-on:click.self.prevent</code> 只会阻止对元素自身的点击。</p> 
    </blockquote> 
   </article>
   
  </section>
