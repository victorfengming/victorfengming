---
title: "Xadmin添加用户小组件出错"
date:       2020-01-16
subtitle: "render() got an unexpected keyword argument 'renderer"
tags:
	- Python
	- background
	- solution
---


<p>环境：</p>
<p>Python 3.5.6</p>
<p>Django 2.1</p>
<p>Xadmin</p>
<p>&nbsp;</p>
<p>原因：</p>
<p>render函数在django2.1上有变化</p>
<p>&nbsp;</p>
<p>解决方案：</p>
<p>1.在Python终端输入命令help('xadmin') 查看xadmin安装位置 得到如下输出</p>
<div class="cnblogs_code">
<pre><span style="color: #000000;">FILE
    </span>/root/anaconda3/envs/learndjango/lib/python3.<span style="color: #800080;">5</span>/site-packages/xadmin/__init__.py</pre>
</div>
<p>2.进入xadmin安装路径，编辑xadmin/views/dashboard.py</p>
<div class="cnblogs_code">
<pre> 36     <span style="color: #008000;">#</span><span style="color: #008000;">render() got an unexpected keyword argument 'renderer'</span>
 37     <span style="color: #008000;">#</span><span style="color: #008000;">修改bug, 添加renderer</span>
 38     <span style="color: #008000;">#</span><span style="color: #008000;">by prism 2018/10/4</span>
 39     <span style="color: #0000ff;">def</span> render(self, name, value, attrs=None, renderer=None):</pre>
</div>
<p>&nbsp;</p>
