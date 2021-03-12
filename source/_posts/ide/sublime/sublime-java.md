---
title: 'sublime text 配置java开发环境'
date:       2019-10-18
tags:
	- ide
	- solution
	- sublime
---

<ul>
<li>把SublimeText当作一个轻量级的编译工具来用还是不错的，可是当我下载好并且写了一个HelloWord的Java程序之后，它居然只编译不运行！那么我们就来解决这个问题</li>
<li>注意：本教程针对的是Windows平台，Mac OS我已经试过了，并不行。</li>
</ul>

<h2 id="变化"><a name="t1"></a>变化</h2>

<ul>
<li>原本网上是有一些关于sublime text 2的教程的，可是Sublime Text 3 和2 有些区别，主要是原来的一些配置文件都被压缩成一个文件了。下面我们就来看看如何让Java程序在Sublime Text中编译和运行。</li>
</ul>



<h2 id="准备"><a name="t2"></a>准备</h2>

<ul>
<li>如果你已经配置好了JDK并且安装好了Sublime Text 3 ，那么就可以继续看下去了，否则，你应该先去配置环境和安装软件。</li>
</ul>



<h2 id="教程"><a name="t3"></a>教程</h2>

<ol>
<li>首先找到Sublime Text 3 安装目录下的<code>Java.sublime-package</code>文件。我的这个文件是在<code>C:\Program Files\Sublime Text 3\Packages</code></li>
<li>使用WinRAR或者其他解压软件打开上一步中说的文件</li>
<li>找到<code>JavaC.sublime-build</code>文件并且使用Sublime Text 3 打开，修改内容为下文给出的内容</li>
<li>然后保存，WinRAR会提示是否保存修改的文件到压缩文件，当然选是</li>
</ol>



<h2 id="javacsublime-build"><a name="t4"></a>JavaC.sublime-build</h2>

```python
{
    "cmd": ["javac", "$file_name", "&&", "java", "$file_base_name"], 
    "working_dir": "${project_path:${folder}}", 
    "selector": "source.java", 
    "shell": true, 
    "encoding":"utf-8" 
}
```

<h2 id="然后然我们来看看结果如何"><a name="t5"></a>然后然我们来看看结果如何</h2>

<p><img src="/img/posts/ide/sublime_java.png" alt="sublime_java" title=""> <br>
It Works！！！</p>                                  