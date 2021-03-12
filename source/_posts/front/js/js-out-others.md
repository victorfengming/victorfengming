---
title: 'JS中的排他思想'
date:       2019-09-06
tags:
	- JavaScript
	- web
	- solution
---

<div class="content">本篇文章给大家分享了关于JS的排他思想的一点内容，有兴趣的朋友看一下<p></p><p>今天学习的JS中，要实现tba栏切换效果，运用了排他思想。</p><p><span class="img-wrap"><img src="https://img.php.cn/upload/article/000/153/291/edb090b1ed271d41d9711e85fc710063-0.png"></span></p><p>用户点击button时，不但button的背景颜色会改变，而且下面的内容也会随之改变。</p><p><span class="img-wrap"><img src="https://img.php.cn/upload/article/000/153/291/5c3ee46132e9f02d23ff1e8ad4ca4680-1.png"></span></p><p>首先要实现button的改变，用for循环遍历每个button，对所有的button进行初始化，使其类名为空；然后跳出循环，对当前被点击的button赋予一个类。</p><p><span class="img-wrap"><img src="https://img.php.cn/upload/article/000/153/291/5c3ee46132e9f02d23ff1e8ad4ca4680-2.png"></span></p><p>而对于下面每个盒子随着button的不同而改变，首先得先得到每个button的序号，对每个进行匹配，使之互相对应。</p><p><span class="img-wrap"><img src="https://img.php.cn/upload/article/000/153/291/df174f38274120d26cfbf0ccda10f945-3.png"></span></p><p>以上就是JS的排他思想的详细内容，更多请关注php中文网其它相关文章！</p><div class="share layui-clear bdsharebuttonbox bdshare-button-style0-16" data-bd-bind="1567767708992"><li><a href="javascript:;" data-cmd="weixin" class="wechat"><i class="layui-icon"></i>微信</a></li><li><a href="javascript:;" data-cmd="more" class="share-btn"><i class="layui-icon"></i>分享</a></li></div><img src="/static/img/article_wechat.jpg?1" style="margin-top: 30px;" alt="php中文网最新课程二维码"><div class="tags layui-clear"><li>相关标签：<a href="/search?word=javascript" target="_blank">javascript</a> <a href="/search?word=思想" target="_blank">思想</a> <a href="/search?word=排他" target="_blank">排他</a></li><li class="line">本文原创发布php中文网，转载请注明出处，感谢您的尊重！</li></div><div class="page layui-clear"><ul><li>上一篇：<a href="/js-tutorial-390900.html">ajax和jsonp跨域详解（附代码）</a></li><li>下一篇：<a href="/js-tutorial-390902.html">怎样用Ajax异步检查用户名有无重复</a></li></ul></div></div>
