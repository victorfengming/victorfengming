---
title: 'SublimeText3输入法问题'
cover: "/img/lynk/93.jpg"
date:       2019-10-16
subtitle: '关于SublimeText3输入法候选窗口不能跟随光标位置的解决方案'
tags:
	- ide
	- solution
	- sublime
---


### 方案1
很多新手朋友使用sublime,它是一个开源免费和轻量级的编辑器

但是在使用的过程中,可能会遇到SublimeText3默认不支持输入法跟随光标，这在输入中文的时候看起来不方便。

今天小编就教大家解决这个问题


进入`SublimeText3`在上面菜单栏里`Perferences`点击`PackageControl`，这样就会自动安装一个可支持插件的终端窗口。

安装完毕之后，按快捷键`ctrl+shift+p`会弹出终端窗口，输入`install package`（下方会有提示）。

然后输入`imesupport`安装这个插件，安装完毕后，重启`Sublime`

如果上述方案仍然不能解决,请读下文
### 方案2

<div class="htmledit_views" id="content_views">
                                            <p>我们使用Sublime时有个Bug就是输入文字时，输入法的框不会跟随光标。</p>

<p><img alt="" class="has" height="55" src="https://img-blog.csdnimg.cn/20190220142828949.png" width="633"></p>

<p>我们需要手动添加一个包 就能解决这个问题</p>

<p>第一步：下载<strong>IMESupport </strong>插件</p>

<p><strong>Github传送门</strong>：<a href="https://github.com/zcodes/IMESupport" rel="nofollow" data-token="0dce66f1378bbdf8a96f5c646cf34dce">https://github.com/zcodes/IMESupport</a>&nbsp;</p>

<p>如果你是用下载，下载后解压，注意双层文件夹的问题（两个同名文件夹，去掉外面的一个）。</p>

<p>第二步：<strong>放到package包下</strong>，这里必须手动添加依赖，不然不会生效</p>

<p><img alt="" class="has" src="/img/posts/ide/sublime_packagecontrol.png"></p>
<p><img alt="" class="has" src="/img/posts/ide/sublime_packagecontrol2.png"></p>

<p>图中第一个是用package control安装的 没用。</p>                                    </div>
