---
title: 'sublime Text 正则替换'
date:       2019-09-12
tags:
	- web
	- html
	- solution
	- sublime
---

[原文链接](https://cloud.tencent.com/developer/article/1342450)


<div class="c-markdown J-articleContent"><p>我遇到一个文章，需要把所有的 (数字)  换为 [数字]</p><p>于是我使用 Sublime Text的替换</p><p>首先，我们需要打开正则使用“Alt+R” 或打开“Ctrl+h”选择正则。</p><p>然后我们开始输入正则，“ ((\d+) ” 我们需要拿出的是数字，所有在数字加“()”。于是在替换写“[$1]”，其中$0就是所有的，$1就是第一个括号。</p><p>如何使用正则可以去看<a data-from="10680" href="http://lindexi.oschina.io/lindexi/post/%E6%AD%A3%E5%88%99%E8%A1%A8%E8%BE%BE%E5%BC%8F30%E5%88%86%E9%92%9F%E5%85%A5%E9%97%A8%E6%95%99%E7%A8%8B/" target="_blank" rel="nofollow noopener noreferrer">正则表达入门</a>。</p><p>Sumlime 还可以创建代码行，做法也很简单。</p><p>点击 Tools   New Snippet</p><figure><div class="image-block"><span><img src="https://ask.qcloudimg.com/http-save/yehe-2759138/w41nf9yxc1.jpeg?imageView2/2/w/1620" class="" style="cursor: zoom-in;"></span></div></figure><pre class="prism-token token  language-javascript"><span class="token operator">&lt;</span> snippet<span class="token operator">&gt;</span>
    <span class="token operator">&lt;</span> content<span class="token operator">&gt;</span><span class="token operator">&lt;</span><span class="token operator">!</span><span class="token punctuation">[</span>CDATA<span class="token punctuation">[</span>
Hello<span class="token punctuation">,</span> $<span class="token punctuation">{</span><span class="token number">1</span><span class="token punctuation">:</span><span class="token keyword">this</span><span class="token punctuation">}</span> is a $<span class="token punctuation">{</span><span class="token number">2</span><span class="token punctuation">:</span>snippet<span class="token punctuation">}</span><span class="token punctuation">.</span>
<span class="token punctuation">]</span><span class="token punctuation">]</span><span class="token operator">&gt;</span><span class="token operator">&lt;</span> <span class="token operator">/</span>content<span class="token operator">&gt;</span>
    <span class="token operator">&lt;</span><span class="token operator">!</span><span class="token operator">--</span> Optional<span class="token punctuation">:</span> Set a tabTrigger to define how to trigger the snippet <span class="token operator">--</span><span class="token operator">&gt;</span>
    <span class="token operator">&lt;</span><span class="token operator">!</span><span class="token operator">--</span> <span class="token operator">&lt;</span>tabTrigger<span class="token operator">&gt;</span>hello<span class="token operator">&lt;</span><span class="token operator">/</span>tabTrigger<span class="token operator">&gt;</span> <span class="token operator">--</span><span class="token operator">&gt;</span>
    <span class="token operator">&lt;</span><span class="token operator">!</span><span class="token operator">--</span> Optional<span class="token punctuation">:</span> Set a scope to limit where the snippet will trigger <span class="token operator">--</span><span class="token operator">&gt;</span>
    <span class="token operator">&lt;</span><span class="token operator">!</span><span class="token operator">--</span> <span class="token operator">&lt;</span>scope<span class="token operator">&gt;</span>source<span class="token punctuation">.</span>python<span class="token operator">&lt;</span><span class="token operator">/</span>scope<span class="token operator">&gt;</span> <span class="token operator">--</span><span class="token operator">&gt;</span>
<span class="token operator">&lt;</span> <span class="token operator">/</span>snippet<span class="token operator">&gt;</span></pre><p>content 是我们按下快捷键的内容，$ {1:this} 就是第一个输入内容，其中，默认写This，所有的{1}都代换你输入的第一个。$2就是第二个。</p><p>我们需要设置快捷键。</p><p><code>&lt;tabTrigger&gt;hello&lt;/tabTrigger&gt;</code></p><p>就是按下 hello，按下 tab 就会使用代码段。</p><p>写好，我们保存在<code>C:\Users\&lt;Use&gt;\AppData\Roaming\Sublime Text 2\Packages\User</code> 后缀<code>.sublime-snippet</code></p><p>我们有时打开中文会乱码，我们可以 ctrl+shift+p</p><p>输入 Package  control:install 安装 CovertToUTF8</p><figure><hr></figure></div>

