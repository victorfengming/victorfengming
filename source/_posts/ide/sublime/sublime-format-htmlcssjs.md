---
title: 'sublime一键格式化'
cover: "/img/lynk/23.jpg"
date:       2019-09-17
subtitle: 'html/css/js'
tags:
	- ide
	- solution
	- sublime
---

<div class="htmledit_views" id="content_views">
    <p>1.使用快捷键ctrl+shift+p调出控制台，输入install package，然后输入<span>html-css-js prettify</span>，进行下载</p><p>2.下载完成后，在preference打开package settings，会出现如下内容：</p><p><img src="https://img-blog.csdn.net/20180427160941871?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl8zNjg5MjEwNg==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70" alt=""></p><p><span>html-css-js prettify</span>安装成功。</p><p>3.具体的快捷键在preference &gt; package setting &gt; html/css/js prettify &gt; keyboard-shortcuts-default中</p><p><img src="https://img-blog.csdn.net/20180427161403345?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl8zNjg5MjEwNg==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70" alt=""><br></p><p><br></p><p><strong><span style="color:#000000;">注意：容易出现的错误！</span></strong></p><p>博主第一次使用时，按下ctrl + shift +h并没有奏效，发现这插件依赖node.js，所以要下载node.js（下载node.js不要等级太低）</p><p>node.js下载地址：http://nodejs.cn/download/</p><p>下载后使用cmd，进入下载的目录，使用node.exe --version</p><p><img src="https://img-blog.csdn.net/20180427161958508?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl8zNjg5MjEwNg==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70" alt=""></p><p>这样node.js就安装成功了！</p><p>然后在sublime中的preference &gt; package setting &gt; html/css/js prettify &gt; plugin-options-default中修改</p><p><img src="https://img-blog.csdn.net/20180427162321946?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl8zNjg5MjEwNg==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70" alt=""></p><p>红标处改为node的安装地址</p><p>再次使用ctrl + shift + h就可以格式化html/css/js了</p><p>ps:</p><p>&nbsp;&nbsp;&nbsp; 可能会有热键冲突，本人使用搜狗输入法，使用ctrl + shift + h就是换搜狗输入法的皮肤，要切换在电脑自带的输入法下的英文才可以使用！<br></p>                                    </div>