---
title: "Python数据分析"
date:       2019-10-02
subtitle: "Web APIs交互和数据库交互"
tags:
	- Python
	- solution
---

<script>
window.location.href='https://blog.csdn.net/sdu_hao/article/details/101751560';
</script>

目录

1. Web APIs交互

2. 数据库交互

3. 总结


1. Web APIs交互
许多网站都有一些通过JSON或其他格式提供数据的公共API。通过Python访 问这些API的办法有不少。一个简单易用的办法(推荐)是requests包 (http://docs.python-requests.org)。

为了搜索最新的30个GitHub上的pandas主题，我们可以发一个HTTP GET请 求，使用requests扩展库: