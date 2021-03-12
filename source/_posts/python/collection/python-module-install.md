---
title: "python相关模块安装 "
date:       2019-11-03
subtitle: "国内镜像地址 "
tags:
	- Python
	- solution
	- basis
---

<div class="post">
            <h1 class="postTitle">
                
<a id="cb_post_title_url" class="postTitle2" href="https://www.cnblogs.com/hellojesson/p/6431398.html">python 相关模块安装 国内镜像地址</a>

            </h1>
            <div class="clear"></div>
            <div class="postBody">
                
<div id="cnblogs_post_body" class="blogpost-body ">
    <p>python 相关模块安装 国内镜像地址</p>
<p>pipy国内镜像目前有：</p>
<p>http://pypi.douban.com/ &nbsp;豆瓣</p>
<p>http://pypi.hustunique.com/ &nbsp;华中理工大学</p>
<p>http://pypi.sdutlinux.org/ &nbsp;山东理工大学</p>
<p>http://pypi.mirrors.ustc.edu.cn/ &nbsp;中国科学技术大学</p>
<p>https://pypi.tuna.tsinghua.edu.cn/ 清华大学</p>
<p>对于pip这种在线安装的方式来说，很方便，但网络不稳定的话很要命。使用国内镜像相对好一些，</p>
<p>&nbsp;</p>
<p>如果想手动指定源，可以在pip后面跟-i 来指定源，比如用豆瓣的源来安装web.py框架：</p>
<p>pip install web.py -i http://pypi.douban.com/simple</p>
<p>注意后面要有/simple目录！！！</p>
<p>&nbsp;</p>
<p>要配制成默认的话，需要创建或修改配置文件（linux的文件在~/.pip/pip.conf，windows在%HOMEPATH%\pip\pip.ini），修改内容为：</p>
<p>code:</p>
<p>[global]</p>
<p>index-url = http://pypi.douban.com/simple</p>
<p>&nbsp;</p>
<p>推荐使用清华大学的源，速度快(依个人情况而定！)：</p>
<p>pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple django</p>
<p>pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple pillow</p>
<p>pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple paramiko</p>
<p>pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple cryptography==1.5.2</p>
<p>pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple django-session-security==2.4.0</p>
<p>pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple djangorestframework==3.5.3</p>
<p>pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple paramiko==2.0.2</p>
<p>pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple pycparser==2.16</p>
<p>pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple PyMySQL==0.7.9</p>
<p>&nbsp;</p>
<p>++++++++++++++++++++++++++++++++++++++++++++++++++++++</p>
<p>Python开发 常用模块安装</p>
<p>包括Python，eclipse，jdk，pydev，pip，setuptools，beautifulsoup，pyyaml，nltk，mysqldb的下载安装配置。<br>*************************************************<br>python<br>下载：<br>python-2.7.6.amd64.msi<br><a href="http://www.python.org/" rel="external" target="_blank">http://www.python.org/</a><br>Python 2.7.6 released<br>Python 2.7.6 is now available.<br><a href="http://www.python.org/" rel="external" target="_blank">http://www.python.org/</a>download/releases/2.7.6/<br>Windows X86-64 MSI Installer (2.7.6) [1] (sig)<br><br>安装<br>配置：<br>我的电脑-&gt;属性-&gt;高级-&gt;环境变量-&gt;系统变量中的PATH增加:C:\Python27;<br>验证：<br>在桌面建立一个文件pt.py，内容为print 'hello python'<br>在cmd中输入命令python C:\Users\***\Desktop\pt.py<br>***为电脑用户名。<br><br>C:\Users\***&gt;python C:\Users\***\Desktop\pt.py<br>hello python<br>C:\Users\***&gt;<br><br>*************************************************<br>Eclipse：<br>eclipse-java-indigo-SR2-win32-x86_64.zip<br><a href="http://www.eclipse.org/downloads/" rel="external" target="_blank">http://www.eclipse.org/downloads/</a><br>Older Versions<br><a href="http://wiki.eclipse.org/Older_Versions_Of_Eclipse" rel="external" target="_blank">http://wiki.eclipse.org/Older_Versions_Of_Eclipse</a><br>Eclipse Indigo SR2 Packages (v 3.7.2)<br><a href="http://www.eclipse.org/downloads/" rel="external" target="_blank">http://www.eclipse.org/downloads/</a>packages/release/indigo/sr2<br>Eclipse IDE for Java Developers, (128 MB)<br>Downloaded 1,226,421 TimesDetails Windows 32-bit&nbsp;&nbsp;64-bit&nbsp;<br><a href="http://www.eclipse.org/downloads/" rel="external" target="_blank">http://www.eclipse.org/downloads/</a>download.php?file=/technology/epp/downloads/release/indigo/SR2/eclipse-java-indigo-SR2-win32-x86_64.zip<br>Download eclipse-java-indigo-SR2-win32-x86_64.zip from:<br><br>*************************************************<br>jdk：<br>jdk-7u45-windows-x64.exe<br><a href="http://www.oracle.com/technetwork/java/javase/downloads/index.html" rel="external" target="_blank">http://www.oracle.com/technetwork/java/javase/downloads/index.html</a><br>Windows x64 125.31 MB&nbsp;&nbsp;&nbsp;&nbsp; jdk-7u45-windows-x64.exe<br><a href="http://www.oracle.com/technetwork/java/javase/downloads/jdk7-downloads-1880260.html" rel="external" target="_blank">http://www.oracle.com/technetwork/java/javase/downloads/jdk7-downloads-1880260.html</a><br><br>*************************************************<br>pydev<br>为了在Eclipse中进行python工程的开发。<br><a href="http://sourceforge.net/projects/pydev/files/" rel="external" target="_blank">http://sourceforge.net/projects/pydev/files/</a><br>PyDev for Eclipse<br>Looking for the latest version? Download PyDev 3.2.0.zip (8.2 MB)<br>版本一直在更新中，几天前是3.1.0.zip<br>下载完，解压缩，将features和plugins文件夹中的内容分别复制到eclipse的features和plugins文件夹下。<br>重复则替换。<br>具体方法见windows xp，32位，环境下，Eclipse+python平台搭建<br><a href="http://blog.sina.com.cn/s/blog_8af1069601019uaw.html" rel="external" target="_blank">http://blog.sina.com.cn/s/blog_8af1069601019uaw.html</a><br>“安装python插件”，打开eclipse先来配置preference-》PyDev-》Interpreter-Python-》New python的执行exe文件的目录<br><br>*************************************************<br>pip<br><a href="https://pypi.python.org/pypi/pip" rel="external" target="_blank">https://pypi.python.org/pypi/pip</a><br>Download<br>pip-1.4.1.tar.gz<br>A tool for installing and managing Python packages.<br>解压缩，在cmd中进入到pip-1.4.1目录，执行 python setup.py install<br>报错：<br>ImportError: No module named setuptools<br>所以，需要先安装setuptools<br><br>*************************************************<br>setuptools<br><a href="https://pypi.python.org/pypi/setuptools/" rel="external" target="_blank">https://pypi.python.org/pypi/setuptools/</a><br>setuptools 2.0.2<br>点击右侧Downloads按钮，跳至Downloads<br>Scroll to the very bottom of the page to find the links.<br>需要到页面底部去找链接下载。<br>File Type Py Version Uploaded on Size<br>setuptools-2.0.2-py2.py3-none-any.whl (md5)&nbsp;&nbsp;Python Wheel&nbsp;&nbsp;3.4 2013-12-29 527KB<br>setuptools-2.0.2.tar.gz (md5)&nbsp;&nbsp;Source&nbsp;&nbsp;2013-12-29 765KB<br>下载setuptools-2.0.2.tar.gz (md5)<br>解压缩<br>在cmd中进入到setuptools-2.0.2目录，执行 python setup.py install<br>成功标志：<br>Installed c:\python27\lib\site-packages\setuptools-2.0.2-py2.7.egg<br>Processing dependencies for setuptools==2.0.2<br>Finished processing dependencies for setuptools==2.0.2<br>继续安装pip<br><br>*************************************************<br>pip<br>在cmd中进入到pip-1.4.1目录，执行 python setup.py install<br>成功标记：<br>Installed c:\python27\lib\site-packages\pip-1.4.1-py2.7.egg<br>Processing dependencies for pip==1.4.1<br>Finished processing dependencies for pip==1.4.1<br>添加到系统环境变量Path：C:\Python27\Scripts;<br>在cmd测试，输入pip，输出：<br>C:\Users\***&gt;pip<br>Usage:<br>&nbsp;&nbsp;pip [options]<br>Commands:<br>&nbsp;&nbsp;install&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Install packages.<br>&nbsp;&nbsp;uninstall&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Uninstall packages.<br>&nbsp;&nbsp;freeze&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Output installed packages in requirements format.<br>&nbsp;&nbsp;list&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;List installed packages.<br>&nbsp;&nbsp;show&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Show information about installed packages.<br>&nbsp;&nbsp;search&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Search PyPI for packages.<br>&nbsp;&nbsp;wheel&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Build wheels from your requirements.<br>&nbsp;&nbsp;zip&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Zip individual packages.<br>&nbsp;&nbsp;unzip&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Unzip individual packages.<br>&nbsp;&nbsp;bundle&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Create pybundles.<br>&nbsp;&nbsp;help&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Show help for commands.<br><br>*************************************************<br>BeautifulSoup<br>可以利用pip进行安装：<br>在cmd中敲入命令查找BeautifulSoup：<br>C:\Users\***&gt;pip search BeautifulSoup<br>BeautifulSoup&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - HTML/XML parser for quick-turnaround applications<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;like screen-scraping.<br>pynliner&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- Python CSS-to-inline-styles conversion tool for<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;HTML using BeautifulSoup and cssutils<br>Detextile&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - Convert HTML to Textile syntax using<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;BeautifulSoup.<br>TreeSoup&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- BeautifulSoup-like wrapper around ElementTree.<br>beautifulscraper&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- Python web-scraping library that wraps urllib2 and<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;BeautifulSoup.<br>ElementSoup&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - ElementTree wrapper for BeautifulSoup HTML parser<br>beautifulsoup4&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- Screen-scraping library<br>collective.soupstrainer&nbsp;&nbsp; - Clean up HTML using BeautifulSoup and filter<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rules.<br>在cmd中敲入命令安装BeautifulSoup<br>C:\Users\***&gt;pip install BeautifulSoup<br>Downloading/unpacking BeautifulSoup<br>&nbsp;&nbsp;Downloading BeautifulSoup-3.2.1.tar.gz<br>&nbsp;&nbsp;Running setup.py egg_info for package BeautifulSoup<br>Installing collected packages: BeautifulSoup<br>&nbsp;&nbsp;Running setup.py install for BeautifulSoup<br>Successfully installed BeautifulSoup<br>Cleaning up...<br>还可参见：安装Beautiful Soup<br><a href="http://blog.sina.com.cn/s/blog_8af1069601019vr2.html" rel="external" target="_blank">http://blog.sina.com.cn/s/blog_8af1069601019vr2.html</a><br><br>*************************************************<br>PyYAML&nbsp;<br>可以利用pip进行安装<br>C:\Users\***&gt;pip search pyyaml<br>PyYAML&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- YAML parser and emitter for Python<br>pyaml&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - PyYAML-based module to produce pretty and readable<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;YAML-serialized data<br>yamly&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - pyyaml wrapper<br>enhancedyaml&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- It makes it more convenient to use PyYAML.<br>C:\Users\***&gt;pip install PyYAML<br>Downloading/unpacking PyYAML<br>&nbsp;&nbsp;Downloading PyYAML-3.10.tar.gz (241kB): 241kB downloaded<br>&nbsp;&nbsp;Running setup.py egg_info for package PyYAML<br>Installing collected packages: PyYAML<br>&nbsp;&nbsp;Running setup.py install for PyYAML<br>&nbsp;&nbsp;&nbsp;&nbsp;checking if libyaml is compilable<br>&nbsp;&nbsp;&nbsp;&nbsp;Unable to find vcvarsall.bat<br>&nbsp;&nbsp;&nbsp;&nbsp;skipping build_ext<br>Successfully installed PyYAML<br>Cleaning up...<br><br>*************************************************<br>nltk<br><a href="https://pypi.python.org/pypi/nltk/" rel="external" target="_blank">https://pypi.python.org/pypi/nltk/</a><br>nltk 2.0.4<br>File Type Py Version Uploaded on Size<br>nltk-2.0.4.tar.gz (md5)&nbsp;&nbsp;Source&nbsp;&nbsp;2012-11-07 933KB<br>nltk-2.0.4.win32.exe (md5)&nbsp;&nbsp;MS Windows installer&nbsp;&nbsp;2.5 2012-11-07 1MB<br>nltk-2.0.4.zip (md5)&nbsp;&nbsp;Source&nbsp;&nbsp;2012-11-07 1MB<br>下载nltk-2.0.4.tar.gz<br>解压缩，在cmd中进入到nltk-2.0.4目录，执行 python setup.py install<br>成功标志：<br>Installed c:\python27\lib\site-packages\nltk-2.0.4-py2.7.egg<br>Processing dependencies for nltk==2.0.4<br>Searching for PyYAML==3.10<br>Best match: PyYAML 3.10<br>Adding PyYAML 3.10 to easy-install.pth file<br>Using c:\python27\lib\site-packages<br>Finished processing dependencies for nltk==2.0.4<br>打开python Idle：<br>输入import nltk<br>输入nltk.download()<br>出现一个NLTK Downloader对话框，修改Download Diretory（E盘或其他盘符下）。点击all开始下载。<br>下载慢还可以到NLTK Corpora&nbsp;<a href="http://nltk.org/nltk_data/" rel="external" target="_blank">http://nltk.org/nltk_data/</a>手工下载缺失的，然后放到Download Diretory，zip别删。<br>重装系统后nltk_data文件夹可以保留，避免重复下载。<br><br>*************************************************<br>mysqldb<br><a href="http://www.lfd.uci.edu/~gohlke/pythonlibs/" rel="external" target="_blank">http://www.lfd.uci.edu/~gohlke/pythonlibs/</a>#mysql-python<br>MySQL-python-1.2.4.win-amd64-py2.7.exe<br>直接双击安装。<br>成功验证：<br>py文件：<br>import MySQLdb<br>connection = MySQLdb.connect(host="127.0.0.1",user="root",passwd="root",db="dbtest")<br>cursor = connection.cursor()<br>cursor.execute( "Select id,content FROM tabletest&nbsp;&nbsp;")<br>print "Rows selected:", cursor.rowcount<br>运行结果输出dbtest数据库中tabletest表的行数。&nbsp;</p>
<p>&nbsp;</p>
</div>
<div id="MySignature"></div>
<div class="clear"></div>
<div id="blog_post_info_block">


    <div id="blog_post_info">
<div id="green_channel">
        <a href="javascript:void(0);" id="green_channel_digg" onclick="DiggIt(6431398,cb_blogId,1);green_channel_success(this,'谢谢推荐！');">好文要顶</a>
        <a id="green_channel_follow" onclick="follow('2449c41d-c738-e311-8d02-90b11c0b17d6');" href="javascript:void(0);">关注我</a>
    <a id="green_channel_favorite" onclick="AddToWz(cb_entryId);return false;" href="javascript:void(0);">收藏该文</a>
    <a id="green_channel_weibo" href="javascript:void(0);" title="分享至新浪微博" onclick="ShareToTsina()"><img src="https://common.cnblogs.com/img/icon_weibo_24.png" alt=""></a>
    <a id="green_channel_wechat" href="javascript:void(0);" title="分享至微信" onclick="shareOnWechat()"><img src="https://common.cnblogs.com/img/wechat.png" alt=""></a>
</div>
<div id="author_profile">
    <div id="author_profile_info" class="author_profile_info">
            <a href="https://home.cnblogs.com/u/hellojesson/" target="_blank"><img src="https://pic.cnblogs.com/face/575577/20150707101005.png" class="author_avatar" alt=""></a>
        <div id="author_profile_detail" class="author_profile_info">
            <a href="https://home.cnblogs.com/u/hellojesson/">hello-Jesson</a><br>
            <a href="https://home.cnblogs.com/u/hellojesson/followees/">关注 - 22</a><br>
            <a href="https://home.cnblogs.com/u/hellojesson/followers/">粉丝 - 32</a>
        </div>
    </div>
    <div class="clear"></div>
    <div id="author_profile_honor"></div>
    <div id="author_profile_follow">
                <a href="javascript:void(0);" onclick="follow('2449c41d-c738-e311-8d02-90b11c0b17d6');return false;">+加关注</a>
    </div>
</div>
<div id="div_digg">
    <div class="diggit" onclick="votePost(6431398,'Digg')">
        <span class="diggnum" id="digg_count">0</span>
    </div>
    <div class="buryit" onclick="votePost(6431398,'Bury')">
        <span class="burynum" id="bury_count">0</span>
    </div>
    <div class="clear"></div>
    <div class="diggword" id="digg_tips">
    </div>
</div>

<script type="text/javascript">
    currentDiggType = 0;
</script></div>
    <div class="clear"></div>
    <div id="post_next_prev">

    <a href="https://www.cnblogs.com/hellojesson/p/6429024.html" class="p_n_p_prefix">« </a> 上一篇：    <a href="https://www.cnblogs.com/hellojesson/p/6429024.html" title="发布于 2017-02-22 15:02">Celery启动Django项目：Client sent AUTH, but no password is set 错误处理</a>
    <br>
    <a href="https://www.cnblogs.com/hellojesson/p/6432149.html" class="p_n_p_prefix">» </a> 下一篇：    <a href="https://www.cnblogs.com/hellojesson/p/6432149.html" title="发布于 2017-02-23 10:09">数据库默认端口</a>

</div>
</div>
            </div>
            <div class="postDesc">posted @ 
<span id="post-date">2017-02-22 22:43</span>&nbsp;<a href="https://www.cnblogs.com/hellojesson/">hello-Jesson</a> 阅读(<span id="post_view_count">7283</span>) 评论(<span id="post_comment_count">0</span>) <a href="https://i.cnblogs.com/EditPosts.aspx?postid=6431398" rel="nofollow"> 编辑</a> <a href="javascript:void(0)" onclick="AddToWz(6431398); return false;">收藏</a>
</div>
        </div>