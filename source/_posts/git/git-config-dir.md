---
title: "Git仓库.git文件夹目录介绍"
date:       2019-10-17
tags:
	- Git
	- solution
---

<div id="content_views" class="markdown_views prism-github-gist">
                    <!-- flowchart 箭头图标 勿删 -->
                    <svg xmlns="http://www.w3.org/2000/svg" style="display: none;">
                        <path stroke-linecap="round" d="M5,0 0,2.5 5,5z" id="raphael-marker-block" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);"></path>
                    </svg>
                                            <h2><a name="t0"></a><a id="_0"></a>说明</h2>
<blockquote>
<h3><a name="t1"></a><a id="git__1"></a>以下皆为.git/ 目录下的文件</h3>
</blockquote>
<h3><a name="t2"></a><a id="1__ORIG_HEAD_2"></a>1  ORIG_HEAD</h3>
<blockquote>
<h4><a id="__3"></a>远程仓库 当前引用</h4>
</blockquote>
<h4><a id="git__5"></a>在git本地仓库根目录 运行:</h4>
<pre class="prettyprint"><code class="has-numbering" onclick="mdcp.copyCode(event)" style="position: unset;">cat .git/ORIG_HEAD
<div class="hljs-button {2}" data-title="复制"></div></code><ul class="pre-numbering" style=""><li style="color: rgb(153, 153, 153);">1</li></ul></pre>
<h4><a id="_10"></a>显示</h4>
<pre class="prettyprint"><code class="has-numbering" onclick="mdcp.copyCode(event)" style="position: unset;">88e6fb86f5317bdfd2e8a78899334e9f0ba16987

<div class="hljs-button {2}" data-title="复制"></div></code><ul class="pre-numbering" style=""><li style="color: rgb(153, 153, 153);">1</li><li style="color: rgb(153, 153, 153);">2</li></ul></pre>
<h4><a id="_16"></a>如图：</h4>
<p><img src="https://img-blog.csdn.net/2018100411103066?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3Nvbmd5dWVxdWFu/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70" alt="在这里插入图片描述"></p>
<h3><a name="t3"></a><a id="2_HEAD_18"></a>2 HEAD</h3>
<blockquote>
<h4><a id="__19"></a>本地仓库 当前引用</h4>
</blockquote>
<pre class="prettyprint"><code class="has-numbering" onclick="mdcp.copyCode(event)" style="position: unset;"> 文件内容：refs/heads/&lt;branchName&gt;
<div class="hljs-button {2}" data-title="复制"></div></code><ul class="pre-numbering" style=""><li style="color: rgb(153, 153, 153);">1</li></ul></pre>
<h4><a id="git__24"></a>在git本地仓库根目录 运行:</h4>
<pre class="prettyprint"><code class="has-numbering" onclick="mdcp.copyCode(event)" style="position: unset;">cat .git/HEAD
<div class="hljs-button {2}" data-title="复制"></div></code><ul class="pre-numbering" style=""><li style="color: rgb(153, 153, 153);">1</li></ul></pre>
<h4><a id="_31"></a>显示</h4>
<pre class="prettyprint"><code class="has-numbering" onclick="mdcp.copyCode(event)" style="position: unset;">ref: refs/heads/master

<div class="hljs-button {2}" data-title="复制"></div></code><ul class="pre-numbering" style=""><li style="color: rgb(153, 153, 153);">1</li><li style="color: rgb(153, 153, 153);">2</li></ul></pre>
<h3><a name="t4"></a><a id="3_refsheadsbranchName_38"></a>3 refs/heads/branchName</h3>
<blockquote>
<h4><a id="__40"></a>本地仓库 当前分支</h4>
</blockquote>
<h4><a id="_41"></a></h4>
<h4><a id="git__45"></a>在git本地仓库根目录 运行:</h4>
<pre class="prettyprint"><code class="has-numbering" onclick="mdcp.copyCode(event)" style="position: unset;">cat .git/refs/heads/master
<div class="hljs-button {2}" data-title="复制"></div></code><ul class="pre-numbering" style=""><li style="color: rgb(153, 153, 153);">1</li></ul></pre>
<h4><a id="_50"></a>显示</h4>
<pre class="prettyprint"><code class="has-numbering" onclick="mdcp.copyCode(event)" style="position: unset;">3396b04ee5343498d8c2f457d14d3aee36239c6f

<div class="hljs-button {2}" data-title="复制"></div></code><ul class="pre-numbering" style=""><li style="color: rgb(153, 153, 153);">1</li><li style="color: rgb(153, 153, 153);">2</li></ul></pre>
<blockquote>
<h4><a id="_commitId_57"></a>这是 当前分支最后一次commitId</h4>
</blockquote>
<h3><a name="t5"></a><a id="2__3__59"></a>2 和 3 的关系如图:</h3>
<p><img src="https://img-blog.csdn.net/20181004111137755?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3Nvbmd5dWVxdWFu/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70" alt="在这里插入图片描述"></p>
<h3><a name="t6"></a><a id="4_refsremotesrepertoryNameHEAD_62"></a>4 refs/remotes/repertoryName/HEAD</h3>
<blockquote>
<h4><a id="_63"></a>远程仓库当前分支</h4>
</blockquote>
<h4><a id="git__64"></a>在git本地仓库根目录 运行:</h4>
<pre class="prettyprint"><code class="has-numbering" onclick="mdcp.copyCode(event)" style="position: unset;">cat .git/refs/remotes/origin/HEAD
<div class="hljs-button {2}" data-title="复制"></div></code><ul class="pre-numbering" style=""><li style="color: rgb(153, 153, 153);">1</li></ul></pre>
<h4><a id="_69"></a>显示</h4>
<pre class="prettyprint"><code class="has-numbering" onclick="mdcp.copyCode(event)" style="position: unset;">ref: refs/remotes/origin/master

<div class="hljs-button {2}" data-title="复制"></div></code><ul class="pre-numbering" style=""><li style="color: rgb(153, 153, 153);">1</li><li style="color: rgb(153, 153, 153);">2</li></ul></pre>
<h3><a name="t7"></a><a id="5_refsremotesrepertoryNameremoteBranchName_76"></a>5 refs/remotes/repertoryName/remoteBranchName</h3>
<blockquote>
<h4><a id="commit_77"></a>远程仓库对应分支最后一次commit</h4>
</blockquote>
<h4><a id="git__78"></a>在git本地仓库根目录 运行:</h4>
<pre class="prettyprint"><code class="has-numbering" onclick="mdcp.copyCode(event)" style="position: unset;">cat .git/refs/remotes/origin/master
<div class="hljs-button {2}" data-title="复制"></div></code><ul class="pre-numbering" style=""><li style="color: rgb(153, 153, 153);">1</li></ul></pre>
<h4><a id="_83"></a>显示</h4>
<pre class="prettyprint"><code class="has-numbering" onclick="mdcp.copyCode(event)" style="position: unset;">581ba1436ebaa54a7f5d0f1db8cc4da0ca72127e

<div class="hljs-button {2}" data-title="复制"></div></code><ul class="pre-numbering" style=""><li style="color: rgb(153, 153, 153);">1</li><li style="color: rgb(153, 153, 153);">2</li></ul></pre>
<blockquote>
<h4><a id="commitId_89"></a>这是远程仓库当前分支最后一次commitId</h4>
</blockquote>
<h3><a name="t8"></a><a id="4__5__91"></a>4 和 5 的关系如图:</h3>
<p><img src="https://img-blog.csdn.net/20181004111234450?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3Nvbmd5dWVxdWFu/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70" alt="在这里插入图片描述"></p>
<h3><a name="t9"></a><a id="6_logsrefsheadsbranchName_95"></a>6 logs/refs/heads/branchName</h3>
<blockquote>
<h4><a id="_96"></a>本地仓库对应分支所有操作</h4>
</blockquote>
<h4><a id="git__98"></a>在git本地仓库根目录 运行:</h4>
<pre class="prettyprint"><code class="has-numbering" onclick="mdcp.copyCode(event)" style="position: unset;">cat .git/logs/refs/heads/master 

<div class="hljs-button {2}" data-title="复制"></div></code><ul class="pre-numbering" style=""><li style="color: rgb(153, 153, 153);">1</li><li style="color: rgb(153, 153, 153);">2</li></ul></pre>
<h4><a id="_105"></a>显示</h4>
<pre class="prettyprint"><code class="has-numbering" onclick="mdcp.copyCode(event)" style="position: unset;">0000000000000000000000000000000000000000 88e6fb86f5317bdfd2e8a78899334e9f0ba16987 author &lt;author@youxiang.com&gt; 1537330001 +0800  clone: from https://github.com/google/guava.git

88e6fb86f5317bdfd2e8a78899334e9f0ba16987 581ba1436ebaa54a7f5d0f1db8cc4da0ca72127e author &lt;author@youxiang.com&gt; 1538568357 +0800   pull: Fast-forward
<div class="hljs-button {2}" data-title="复制"></div></code><ul class="pre-numbering" style=""><li style="color: rgb(153, 153, 153);">1</li><li style="color: rgb(153, 153, 153);">2</li><li style="color: rgb(153, 153, 153);">3</li></ul></pre>
<blockquote>
<h4><a id="master_112"></a>本地master分支的两次操作</h4>
<h4><a id="1_clone__113"></a>1 clone 项目</h4>
</blockquote>
<pre class="prettyprint"><code class="has-numbering" onclick="mdcp.copyCode(event)" style="position: unset;">commitId(0000000000000000000000000000000000000000) ——&gt; commitId(88e6fb86f5317bdfd2e8a78899334e9f0ba16987)
<div class="hljs-button {2}" data-title="复制"></div></code><ul class="pre-numbering" style=""><li style="color: rgb(153, 153, 153);">1</li></ul></pre>
<blockquote>
<h4><a id="2_git_pull_Fastforward_119"></a>2 git pull: Fast-forward</h4>
</blockquote>
<pre class="prettyprint"><code class="has-numbering" onclick="mdcp.copyCode(event)" style="position: unset;">commitId(88e6fb86f5317bdfd2e8a78899334e9f0ba16987) ——&gt; commitId(581ba1436ebaa54a7f5d0f1db8cc4da0ca72127e)
<div class="hljs-button {2}" data-title="复制"></div></code><ul class="pre-numbering" style=""><li style="color: rgb(153, 153, 153);">1</li></ul></pre>
<h3><a name="t10"></a><a id="7_logsrefsheadsrepertoryNamebranchName_123"></a>7 logs/refs/heads/repertoryName/branchName</h3>
<blockquote>
<h4><a id="_124"></a>远程仓库对应分支所有操作</h4>
</blockquote>
<h4><a id="git__126"></a>在git本地仓库根目录 运行:</h4>
<pre class="prettyprint"><code class="has-numbering" onclick="mdcp.copyCode(event)" style="position: unset;">cat .git/logs/refs/remotes/origin/master
<div class="hljs-button {2}" data-title="复制"></div></code><ul class="pre-numbering" style=""><li style="color: rgb(153, 153, 153);">1</li></ul></pre>
<h4><a id="_132"></a>显示</h4>
<pre class="prettyprint"><code class="has-numbering" onclick="mdcp.copyCode(event)" style="position: unset;">88e6fb86f5317bdfd2e8a78899334e9f0ba16987 581ba1436ebaa54a7f5d0f1db8cc4da0ca72127e songyuequan &lt;songyuequangit@163.com&gt; 1538568357 +0800  pull: fast-forward
<div class="hljs-button {2}" data-title="复制"></div></code><ul class="pre-numbering" style=""><li style="color: rgb(153, 153, 153);">1</li></ul></pre>
<blockquote>
<h4><a id="_137"></a>同上</h4>
</blockquote>
<h3><a name="t11"></a><a id="8_refstagstagName_139"></a>8 refs/tags/tagName</h3>
<blockquote>
<h4><a id="tagcommitID_140"></a>文件内容:tag所在的commitID</h4>
</blockquote>
<h4><a id="git__141"></a>在git本地仓库根目录 运行:</h4>
<pre class="prettyprint"><code class="has-numbering" onclick="mdcp.copyCode(event)" style="position: unset;">cat  .git/refs/tags/Release1.0 
<div class="hljs-button {2}" data-title="复制"></div></code><ul class="pre-numbering" style=""><li style="color: rgb(153, 153, 153);">1</li></ul></pre>
<h4><a id="_147"></a>显示</h4>
<pre class="prettyprint"><code class="has-numbering" onclick="mdcp.copyCode(event)" style="position: unset;">72014f48f489e1e43519212de1bd9f78c3755a4c
<div class="hljs-button {2}" data-title="复制"></div></code><ul class="pre-numbering" style=""><li style="color: rgb(153, 153, 153);">1</li></ul></pre>
<h3><a name="t12"></a><a id="9_packedrefs_154"></a>9 packed-refs</h3>
<blockquote>
<h4><a id="clone_155"></a>clone仓库时所有的引用</h4>
</blockquote>
<h3><a name="t13"></a><a id="10_COMMIT_EDITMSG_157"></a>10 COMMIT_EDITMSG</h3>
<blockquote>
<h4><a id="_158"></a>本地最后一个提交的信息</h4>
</blockquote>
<h3><a name="t14"></a><a id="11_objects_160"></a>11 objects目录</h3>
<blockquote>
<h4><a id="_161"></a>所有文件对象</h4>
</blockquote>
<p>具体详情请看 这篇翻译文章</p>
<p><a href="https://blog.csdn.net/songyuequan/article/details/85862415" rel="nofollow" data-token="28a1aaa367aa941bd1bba7db61d52256">https://blog.csdn.net/songyuequan/article/details/85862415</a></p>
<h3><a name="t15"></a><a id="12__info_169"></a>12  info</h3>
<p><mark>待研究</mark></p>
<h3><a name="t16"></a><a id="13_index_172"></a>13 index</h3>
<p><a href="https://blog.csdn.net/s646575997/article/details/52143586" rel="nofollow" data-token="caeb42407afef3a7ab4480aa399bd736">Git暂存区原理</a></p>
<h3><a name="t17"></a><a id="14_hooks_175"></a>14 hooks</h3>
<p><mark>shell脚本</mark></p>

                                    </div>