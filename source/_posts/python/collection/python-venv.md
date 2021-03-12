---
title: "python虚拟环境--virtualenv"
date:       2019-01-14
subtitle: "带你玩转虚拟环境"
tags:
	- Python
	- background
	- solution
---



<div class="post">
    <h1 class="postTitle">

        <a id="cb_post_title_url" class="postTitle2" href="https://www.cnblogs.com/technologylife/p/6635631.html">python虚拟环境--virtualenv</a>

    </h1>
    <div class="clear"></div>
    <div class="postBody">

        <div id="cnblogs_post_body" class="blogpost-body ">
            <p><span style="font-size: 14px;">　　<span style="font-size: 15px;">virtualenv&nbsp;是一个创建隔绝的Python环境的工具。virtualenv创建一个包含所有必要的可执行文件的文件夹，用来使用Python工程所需的包。</span></span>
            </p>
            <h3>　　安装</h3>
            <div class="cnblogs_code">
                <pre><span
                        style="font-family: 黑体; font-size: 14px;"><strong>pip install virtualenv</strong></span></pre>
            </div>
            <h3>　　基本使用</h3>
            <ol class="arabic simple">
                <li>为一个工程创建一个虚拟环境：</li>
            </ol>
            <div class="highlight-console">
                <div class="highlight">
                    <div class="cnblogs_code">
<pre><span style="color: #000000;"><strong><span style="font-size: 14px; font-family: 'Microsoft YaHei';">$ cd my_project_dir
$ virtualenv venv　</span></strong>　<strong>#venv为虚拟环境目录名，目录名自定义</strong></span></pre>
                    </div>
                </div>
            </div>
            <p><code class="docutils literal"><span class="pre">　　virtualenv&nbsp;<span
                    class="pre">venv</span></span></code>&nbsp;将会在当前的目录中创建一个文件夹，包含了Python可执行文件，以及&nbsp;<code
                    class="docutils literal">pip</code>&nbsp;库的一份拷贝，这样就能安装其他包了。虚拟环境的名字（此例中是&nbsp;<code
                    class="docutils literal">venv</code>&nbsp;）可以是任意的；若省略名字将会把文件均放在当前目录。</p>
            <p>　　在任何你运行命令的目录中，这会创建Python的拷贝，并将之放在叫做&nbsp;<code class="file docutils literal">venv</code>&nbsp;的文件中。</p>
            <p>　　你可以选择使用一个Python解释器：</p>
            <div class="cnblogs_code">
                <pre><span style="font-size: 14px; font-family: 'Microsoft YaHei';"><strong>$ virtualenv -p /usr/bin/python2.7 venv</strong></span>　　　　<strong># -p参数指定Python解释器程序路径</strong></pre>
            </div>
            <p>　　这将会使用&nbsp;<code class="file docutils literal">/usr/bin/python2.7</code>&nbsp;中的Python解释器。</p>
            <p>&nbsp;</p>
            <ol class="arabic simple" start="2">
                <li>要开始使用虚拟环境，其需要被激活：</li>
            </ol>
            <div class="cnblogs_code">
                <pre><strong><span style="font-size: 14px; font-family: 'Microsoft YaHei';">$ source venv/bin/activate　　　</span></strong></pre>
            </div>
            <p><code class="docutils literal"><span class="pre"><span class="pre">从现在起，任何你使用pip安装的包将会放在&nbsp;<span
                    class="pre">venv</span></span></span></code>&nbsp;文件夹中，与全局安装的Python隔绝开。</p>
            <p>像平常一样安装包，比如：</p>
            <div class="highlight-console">
                <div class="highlight">
<pre><span class="gp">$ pip install requests
</span></pre>
                </div>
            </div>
            <ol class="arabic simple" start="3">
                <li>如果你在虚拟环境中暂时完成了工作，则可以停用它：</li>
            </ol>
            <div class="highlight-console">
                <div class="highlight">
                    <div class="cnblogs_code">
                        <pre><strong><span style="font-size: 15px;">$ . venv/bin/deactivate</span></strong></pre>
                    </div>
                </div>
            </div>
            <p>这将会回到系统默认的Python解释器，包括已安装的库也会回到默认的。</p>
            <p>要删除一个虚拟环境，只需删除它的文件夹。（执行&nbsp;<code class="docutils literal"><span class="pre">rm&nbsp;<span class="pre">-rf&nbsp;<span
                    class="pre">venv</span></span></span></code>&nbsp;）。</p>
            <p>这里virtualenv 有些不便，因为virtual的启动、停止脚本都在特定文件夹，可能一段时间后，你可能会有很多个虚拟环境散落在系统各处，你可能忘记它们的名字或者位置。</p>
            <h2>virtualenvwrapper</h2>
            <p>　　鉴于virtualenv不便于对虚拟环境集中管理，所以推荐直接使用virtualenvwrapper。&nbsp;virtualenvwrapper提供了一系列命令使得和虚拟环境工作变得便利。它把你所有的虚拟环境都放在一个地方。</p>
            <p>　　安装virtualenvwrapper(确保virtualenv已安装)</p>
            <div class="cnblogs_code">
                <pre>pip install virtualenvwrapper<br>pip install virtualenvwrapper-win　　#Windows使用该命令</pre>
            </div>
            <p>　　安装完成后，在~/.bashrc写入以下内容</p>
            <div class="cnblogs_code">
                <pre>export WORKON_HOME=~/<span>Envs<br></span><span>source </span>/usr/local/bin/virtualenvwrapper.sh　　</pre>
            </div>
            <p>　　第一行：v<span style="font-size: 14px;">irtualenvwrapper存放虚拟环境目录</span></p>
            <p><em style="font-family: 'Courier New'; font-size: 12px; line-height: 1.5;"><span
                    style="font-size: 14px;">　</span></em><span style="font-size: 14px;">　第二行：</span>virtrualenvwrapper会安装到python的bin目录下，所以该路径是python安装目录下bin/virtualenvwrapper.sh
            </p>
            <div class="cnblogs_code">
                <pre>source ~/.bashrc　　　　#读入配置文件，立即生效</pre>
            </div>
            <p>　</p>
            <p>　virtualenvwrapper基本使用</p>
            <p>1.创建虚拟环境　<strong>mkvirtualenv</strong></p>
            <div class="cnblogs_code">
                <pre>mkvirtualenv venv　　　</pre>
            </div>
            <p>　　这样会在WORKON_HOME变量指定的目录下新建名为venv的虚拟环境。</p>
            <p>　　若想指定python版本，可通过"--python"指定python解释器</p>
            <div class="cnblogs_code">
                <pre>mkvirtualenv --python=/usr/local/python3.<span
                        style="color: #800080;">5.3</span>/bin/python venv</pre>
            </div>
            <p>2. 基本命令&nbsp;　</p>
            <p><strong>　　</strong>查看当前的虚拟环境目录</p>
            <div class="cnblogs_code">
<pre>[root@localhost ~<span style="color: #000000;">]# workon
py2
py3</span></pre>
            </div>
            <p>　　切换到虚拟环境</p>
            <div class="cnblogs_code">
<pre>[root@localhost ~<span style="color: #000000;">]# workon py3
(py3) [root@localhost </span>~]# </pre>
            </div>
            <p>　　退出虚拟环境</p>
            <div class="cnblogs_code">
<pre>(py3) [root@localhost ~<span style="color: #000000;">]# deactivate
[root@localhost </span>~]# </pre>
            </div>
            <p>　　删除虚拟环境</p>
            <div class="cnblogs_code">
                <pre>rmvirtualenv venv</pre>
            </div>
            <p>&nbsp;</p>
            <p>&nbsp;</p>
            <p>本文参考链接：http://pythonguidecn.readthedocs.io/zh/latest/dev/virtualenvs.html</p>
            <p>&nbsp;</p>
        </div>
    </div>

</div>