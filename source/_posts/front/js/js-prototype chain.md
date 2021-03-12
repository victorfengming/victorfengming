---
title: 'js 原型链的理解'
date:       2019-09-11
tags:
	- JavaScript
	- web
	- basis
---

<div class="project-body">
<div class="portlet-title pro-title" style="width: 1220px;">
<div class="set-btn-group font-settings pull-left">
<a href="javascript:;" class="expand-collapse-trigger" title="折叠/展开"><i class="icon-th-list"></i></a>
<a href="javascript:;" class="toggle-dropdown" title="视觉主题设置"><i class="icon-font"></i></a>
<div class="set-dropdown-menu docblur" style="display:none;">
<div class="dropdown-caret">
<span class="caret-outer"></span>
<span class="caret-inner"></span>
</div>
<div class="buttons font-opt">
<button class="button size font-reduce" font="reduce" title="缩小字体">A</button>
<button class="button size font-enlarge" font="enlarge" title="放大字体">A</button>
</div>
<div class="buttons bg-color">
<button class="button theme" color="color-theme-white" title="默认模式">默认</button>
<button class="button theme" color="color-theme-sepia" title="护眼模式">护眼</button>
<button class="button theme" color="color-theme-night" title="夜间模式">夜间</button>
</div>
</div>
</div>
<div class="kn-btn-group pull-right">            
<span id="content-head-viewcount" class="viewcount-btn"><i class="icon-eye-open"></i> <span>阅读(67243)</span></span>
<a id="knstar" href="javascript:;" onclick="isstar()" data-type="star"><i class="icon-bookmark-empty"></i> <span>书签</span></a>
<a class="btn-thumbs-up" href="javascript:;" onclick="islike()"><i class="icon-thumbs-up"></i> <span id="likestatus">赞</span>(<span id="likecount">6</span>)</a>
<a href="javascript:;" title="分享" class="share-btn  popup_more bdsharebuttonbox bdshare-button-style0-16" data-cmd="more" data-bd-bind="1568202163307"><i class="icon-share"></i> 分享</a>
<a href="/edit/javascript/javascript-5isn2lax" rel="nofollow"><i class="icon-edit"></i> <span>我要纠错</span></a>
</div>
</div>
<div id="pro-mian-header">
<div class="content-top">
<h1>JavaScript 原型链的理解</h1>
</div>
<div class="kn-infomation">
由&nbsp;<span>alexbro</span>&nbsp;创建，Loen 最后一次修改&nbsp;<span>2018-02-24</span>    
</div>          
</div>          
<div class="content-bg">
<div class="content-intro view-box "><p>看这样一段代码：</p><pre lang="javascript" style="max-width: 100%;"><code class="javascript hljs"><span class="hljs-keyword">var</span> Person = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>{ };
<span class="hljs-keyword">var</span> p = <span class="hljs-keyword">new</span> Person();</code></pre><p>我们来看看这个 new 究竟做了什么？</p><blockquote><p>我们把 new 的过程拆分成以下三步：</p><p>1. var p={}; 也就是说，初始化一个对象p。</p><p>2. p.__proto__=Person.prototype;</p><p>3. Person.call(p);也就是说构造p，也可以称之为初始化p。</p></blockquote><p>我们来证明一下：</p><pre lang="javascript" style="max-width: 100%;" showdemo="1"><code class="javascript hljs"><span class="hljs-keyword">var</span> Person = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>{ };
<span class="hljs-keyword">var</span> p = <span class="hljs-keyword">new</span> Person();
alert(p.__proto__ === Person.prototype); <span class="hljs-comment">// true</span>
</code></pre><p>这段代码会返回 true。说明我们步骤2是正确的。</p><p><br></p><p>那么__proto__是什么？</p><blockquote><p>每个对象都会在其内部初始化一个属性，就是 __proto__，当我们访问一个对象的属性 时，如果这个对象内部不存在这个属性，那么他就会去__proto__里找这个属性，这个__proto__又会有自己的__proto__，于是就这样 一直找下去，也就是我们平时所说的原型链的概念。</p></blockquote><p>按照标准，__proto__是不对外公开的，也就是说是个私有属性，但是 Firefox 的引擎将他暴露了出来成为了一个共有的属性，我们可以对外访问和设置。</p><p>我们看一下下面这些代码：</p><pre lang="javascript" style="max-width: 100%;" showdemo="1"><code class="javascript hljs"><span class="hljs-keyword">var</span> Person = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>{ };
&nbsp;&nbsp;&nbsp;&nbsp;Person.prototype.Say = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>{
&nbsp;&nbsp;&nbsp;&nbsp;alert(<span class="hljs-string">"Person say"</span>);
}
<span class="hljs-keyword">var</span> p = <span class="hljs-keyword">new</span> Person();
p.Say();</code></pre><p>我们看下为什么 p 可以访问 Person 的 Say。</p><p>首先var p=new Person()；</p><p>可以得出 p.__proto__=Person.prototype。那么当我们调用 p.Say() 时，首先 p 中没有 Say 这个属性， 于是，他就需要到他的 __proto__ 中去找，也就是 Person.prototype，而我们在上面定义了 Person.prototype.Say = function(){}; 于是，就找到了这个方法。</p><p>好，接下来，让我们看个更复杂的。</p><p><br></p><p>我们来做这样的推导：</p><p>var p=new Programmer()可以得出p.__proto__=Programmer.prototype;</p><p>而在上面我们指定了Programmer.prototype=new Person();我们来这样拆分，var p1=new Person();Programmer.prototype=p1;那么:</p><p>p1.__proto__=Person.prototype;</p><p>Programmer.prototype.__proto__=Person.prototype;</p><p>由根据上面得到p.__proto__=Programmer.prototype。可以得到p.__proto__.__proto__=Person.prototype。</p><p>好，算清楚了之后我们来看上面的结果,p.Say()。由于p没有Say这个属性，于是去p.__proto__，也就是 Programmer.prototype，也就是p1中去找，由于p1中也没有Say，那就去p.__proto__.__proto__，也就是 Person.prototype中去找，于是就找到了alert(“Person say”)的方法。</p><p>其余的也都是同样的道理。</p><p>这也就是原型链的实现原理。</p><p>最后，其实prototype只是一个假象，他在实现原型链中只是起到了一个辅助作用，换句话说，他只是在new的时候有着一定的价值，而原型链的本质，其实在于__proto__！</p><p><br></p></div>
<div style="clear:both"></div>
</div>
<!--控制本地字体主题样式-->
<script type="text/javascript">
var tempFontsize = $.cookie("fontsize");
if (tempFontsize != undefined) {
$("#pro-mian").addClass(tempFontsize);
}
</script>
<!--我要赞赏-->
<div class="project-sq"><div class="project-sq-info"><span>您的支持将鼓励我们做得更好</span></div><ul class="project-sq-avatar"></ul><div class="project-sq-btnarea"><a href="javascript:;">赞赏支持</a></div></div>
<!--我要赞赏结束-->
<!--我要评价-->
<div id="evaluate-box"><span id="evaluates">以上内容是否对您有帮助：</span><span class="star_score"><span title="1分"></span><span title="2分"></span><span title="3分"></span><span title="4分"></span><span title="5分"></span></span></div>
<!--评价结束-->
<div class="content-links">
<div class="previous-link">← <a href="/javascript/javascript-expression.html" title="上一篇：javascript正则表达式知识拓展总结">javascript正则表达式知识拓展总结</a></div>
</div>
<!--练习、出题、写笔记-->
<div class="project-operation">
<div class="pull-right">
<a href="javascript:;" class="op-btn note-btn" onclick="openNote()"><i class="icon-pencil"></i>写笔记</a>
</div>
</div>
<!--横版广告放置-->
<div class="abox-item">    <div class="abox-content">    </div></div> 
<!-- 笔记列表 -->
<div class="notelist-box" style="display:none">
<div class="notelist-head" onclick="openNoteList(this)">
<span class="notelist-title">精选笔记</span>
<i class="icon-circle-arrow-up"></i>
</div>
<div class="notelist-content" id="notelist_content" style="display: none;">
</div>
</div>
<!--相关推荐|wiki推荐-->
<div class="maylike">
<h2 class="project-maylike-info">您可能还喜欢：</h2>
<ul class="project-maylike-ul">
<li><a href="/javascript/javascript-t64x2ksc.html" title="JavaScript JSON.stringify()">JavaScript JSON.stringify()</a></li>
<li><a href="/javascript/js-typeof.html" title="JavaScript typeof, null, 和 undefined">JavaScript typeof, null, 和 undefined</a></li>
</ul>
</div>
<!--相关推荐|wiki推荐 结束-->
</div>