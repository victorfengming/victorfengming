---
title: "Cmder使用"
date:       2020-03-04
subtitle: "Windows下非常好用的终端模拟器"
tags:
	- base
	- cmder
---









原文链接:https://www.jianshu.com/p/552b7f0bb18c



<p>Cmder是Windows下非常好用的终端模拟器， 常用于替换windows自带的终端。它可以在不同的标签页中同时连接不同的底层Shell，包括cmd、PowerShell、Bash和WSL，并提供相关增强功能和更加便捷的操作方式，这也正是它被大家称作为Windows下的神器的原因。</p>
<div class="image-package">
<div class="image-container" style="max-width: 700px; max-height: 424px; background-color: transparent;">
<div class="image-container-fill" style="padding-bottom: 43.0%;"></div>
<div class="image-view" data-width="986" data-height="424">


<img data-original-src="https://upload-images.jianshu.io/upload_images/7667789-cbf8041249833a04.png" data-original-width="986" data-original-height="424" data-original-format="image/png" data-original-filesize="59056" data-image-index="0" style="cursor: zoom-in;" class="" src="https://upload-images.jianshu.io/upload_images/7667789-cbf8041249833a04.png?imageMogr2/auto-orient/strip|imageView2/2/w/986/format/webp"></div>
</div>
<div class="image-caption">Cmder展示图片</div>
</div>
<p>正如Cmder官网所说，我们应该将Cmder看作一个软件包，而非单个软件，它包含了：</p>
<ul>
<li>控制台模拟器：<a href="https://links.jianshu.com/go?to=https%3A%2F%2Fconemu.github.io%2F" target="_blank">Conemu</a> （它是Cmder的基础）</li>
<li>Cmd.exe增强功能：<a href="https://links.jianshu.com/go?to=https%3A%2F%2Fmridgers.github.io%2Fclink%2F" target="_blank">clink</a>  （通过clink进一步增强cmd shell）</li>
<li>Unix tools on windows：<a href="https://links.jianshu.com/go?to=https%3A%2F%2Fgitforwindows.org%2F" target="_blank">git for windows</a>
</li>
</ul>
<blockquote>
<p>本文属于我的Cmder系列文章中的第一篇：《Cmder入门配置》</p>
</blockquote>
<h2>安装</h2>
<p><strong>安装方式一：</strong>在官网<a href="https://links.jianshu.com/go?to=http%3A%2F%2Fcmder.net%2F" target="_blank">Cmder</a>下载cmder压缩包，解压即可。这里<strong>注意</strong>解压路径不能位于需要管理员访问权限的地方，<strong>建议</strong>放在D盘并且确保路径中没有空格。</p>
<ul>
<li>
<p>将cmder添加到文件夹<strong>右键菜单</strong>（即添加Cmder here）：</p>
<p>以管理员权限打开 PowerShell；切换到 cmder 的解压路径；执行 <code>.\cmder.exe /REGISTER ALL</code>，即可添加，取消注册则执行 <code>.\cmder.exe /UNREGISTER ALL</code></p>
</li>
<li><p>为cmder创建桌面快捷方式。</p></li>
</ul>
<blockquote>
<p>如果你有自己的可执行程序，那么你可以考虑将他们放入 <code>%cmder_root%\bin</code> 目录，再将 <code>%cmder_root%\bin</code> 目录添加到 PATH 环境变量。</p>
<p>这里将上文的 <code>%cmder_root%</code> 修改为 <code>cmder.exe</code>所在路径，或者你可以考虑新建一个<code>%cmder_root%</code> 系统变量，或者将其也添加到PATH中（随意就好）。</p>
</blockquote>
<p><strong>安装方式二：</strong> 通过 scoop 安装（推荐）</p>
<div class="_2Uzcx_"><button class="VJbwyy" type="button" aria-label="复制代码"><i aria-label="icon: copy" class="anticon anticon-copy"><svg viewBox="64 64 896 896" focusable="false" class="" data-icon="copy" width="1em" height="1em" fill="currentColor" aria-hidden="true"><path d="M832 64H296c-4.4 0-8 3.6-8 8v56c0 4.4 3.6 8 8 8h496v688c0 4.4 3.6 8 8 8h56c4.4 0 8-3.6 8-8V96c0-17.7-14.3-32-32-32zM704 192H192c-17.7 0-32 14.3-32 32v530.7c0 8.5 3.4 16.6 9.4 22.6l173.3 173.3c2.2 2.2 4.7 4 7.4 5.5v1.9h4.2c3.5 1.3 7.2 2 11 2H704c17.7 0 32-14.3 32-32V224c0-17.7-14.3-32-32-32zM350 856.2L263.9 770H350v86.2zM664 888H414V746c0-22.1-17.9-40-40-40H232V264h432v624z"></path></svg></i></button><pre class="line-numbers  language-shell"><code class="shell  language-shell"># 安装完整版（自带git-for-windows）
scoop install cmder-full
# 安装mini版，不带git，安装后如果想使用bash则还需做一些配置,可见我的系列文章
scoop install cmder
<span aria-hidden="true" class="line-numbers-rows"><span></span><span></span><span></span><span></span></span></code></pre></div>
<blockquote>
<p>scoop的安装和使用可参考我的相关文章：<a href="https://links.jianshu.com/go?to=https%3A%2F%2Fwww.thisfaner.com%2Fposts%2Fdevops%2Fwindows%2Fscoop%25E5%258C%2585%25E7%25AE%25A1%25E7%2590%2586%25E5%25B7%25A5%25E5%2585%25B7%2F" target="_blank">Scoop包管理工具 – 就是这个范儿</a></p>
</blockquote>
<h2>常用操作</h2>
<h3>中文配置</h3>
<p>进入seting界面：点击Cmder窗口左上角的图标 或者 右下角的 <code>三</code>图标，然后选择 <code>setting</code></p>
<p>设置中文界面： 选择<code>General-&gt;Interface language -&gt; zh:简体中文</code></p>
<div class="image-package">
<div class="image-container" style="max-width: 700px; max-height: 244px;">
<div class="image-container-fill" style="padding-bottom: 31.979999999999997%;"></div>
<div class="image-view" data-width="763" data-height="244"><img data-original-src="https://upload-images.jianshu.io/upload_images/7667789-2dd1e8d59ee5908b.png" data-original-width="763" data-original-height="244" data-original-format="image/png" data-original-filesize="13776" data-image-index="1" style="cursor: zoom-in;" class="image-loading"></div>
</div>
<div class="image-caption">cmder01.png</div>
</div>
<h3>粘贴复制</h3>
<p>复制：只需选中一段文字那么该段文字就会被复制到剪贴板</p>
<p>粘贴：直接<code>鼠标右键</code>即可粘贴，或者使用 <code>Ctrl + v</code> 进行粘贴.</p>
<h3>设置为默认终端</h3>
<p>setting 👉 集成 👉 默认项目 👉 强制使用ConEmu作为控制台应用程序的默认终端`</p>
<p>如果允许某些程序出现错误，需要关闭此选项。</p>
<h3>cmd模式和bash模式</h3>
<p>新手可能会经常在cmd模式下输入bash相关的命令格式，导致相关错误；所以注意一下你当前在哪个模式。</p>
<p>比如在初次使用时，可能会出现切换不了路径的情况，这是因为你还没意识到自己在哪个模式下：</p>
<p>如果是用默认的<code>bash</code>, 可以直接 <code>cd /d/myworkstation</code> 这样跨盘切换。</p>
<p>如果用的是<code>cmd</code>模式, 需要先输入 <code>d:</code>来切换到d盘。</p>
<h3>配置cmder以下拉方式划出</h3>
<p>设置 👉 通用 👉 Quake 风格 👉</p>
<ul>
<li>勾选 Quake式向下滑动</li>
<li>勾选 失去焦点时自动隐藏</li>
<li>修改 动画时间 为 <code>150</code>
</li>
</ul>
<p>然后在 “通用” 设置处，设置 最小化和恢复 （Minimize/Restore hotkey ）时所使用的快捷键，默认为  <code>Ctrl + `</code></p>
<blockquote>
<p>如果你同时使用VS Code会发现 <code>Ctrl + `</code>快捷键在VS Code中是打开终端的默认快捷键；为避免冲突，我个人是选择将 cmder 的该快捷键修改为：  <code>Win + `</code></p>
</blockquote>
<h2>alias别名机制</h2>
<p><strong>Cmder增加了alias功能：</strong> 它让你用短短的指令执行一些常见但指令超长又难以记忆的语法；</p>
<p>在控制台输入<code>alias</code>可以查看现有别名。</p>
<p>并且它有分别应用于 cmd，bash和PowerShell的 别名 。</p>
<p><strong>1. cmd aliases：</strong></p>
<p>在<code>%CMDER_ROOT%\config\user-aliases.cmd</code>中添加 cmd aliases，它<strong>仅用于 cmd 命令</strong></p>
<p>示例：</p>
<div class="_2Uzcx_"><button class="VJbwyy" type="button" aria-label="复制代码"><i aria-label="icon: copy" class="anticon anticon-copy"><svg viewBox="64 64 896 896" focusable="false" class="" data-icon="copy" width="1em" height="1em" fill="currentColor" aria-hidden="true"><path d="M832 64H296c-4.4 0-8 3.6-8 8v56c0 4.4 3.6 8 8 8h496v688c0 4.4 3.6 8 8 8h56c4.4 0 8-3.6 8-8V96c0-17.7-14.3-32-32-32zM704 192H192c-17.7 0-32 14.3-32 32v530.7c0 8.5 3.4 16.6 9.4 22.6l173.3 173.3c2.2 2.2 4.7 4 7.4 5.5v1.9h4.2c3.5 1.3 7.2 2 11 2H704c17.7 0 32-14.3 32-32V224c0-17.7-14.3-32-32-32zM350 856.2L263.9 770H350v86.2zM664 888H414V746c0-22.1-17.9-40-40-40H232V264h432v624z"></path></svg></i></button><pre class="line-numbers  language-cmd"><code class="cmd  language-cmd">ls=ls --show-control-chars -F --color $*
pwd=cd
clear=cls
<span aria-hidden="true" class="line-numbers-rows"><span></span><span></span><span></span></span></code></pre></div>
<blockquote>
<p>具体配置可参考：<a href="https://links.jianshu.com/go?to=https%3A%2F%2Fgithub.com%2Fcmderdev%2Fcmder%2Fblob%2Fmaster%2FREADME.md%23cmdercmdexe-aliases" target="_blank">cmder/README.md </a></p>
</blockquote>
<p><strong>2. Bash/Mintty aliases：</strong></p>
<p>对于bash，其配置文件的加载顺序是：</p>
<div class="_2Uzcx_"><button class="VJbwyy" type="button" aria-label="复制代码"><i aria-label="icon: copy" class="anticon anticon-copy"><svg viewBox="64 64 896 896" focusable="false" class="" data-icon="copy" width="1em" height="1em" fill="currentColor" aria-hidden="true"><path d="M832 64H296c-4.4 0-8 3.6-8 8v56c0 4.4 3.6 8 8 8h496v688c0 4.4 3.6 8 8 8h56c4.4 0 8-3.6 8-8V96c0-17.7-14.3-32-32-32zM704 192H192c-17.7 0-32 14.3-32 32v530.7c0 8.5 3.4 16.6 9.4 22.6l173.3 173.3c2.2 2.2 4.7 4 7.4 5.5v1.9h4.2c3.5 1.3 7.2 2 11 2H704c17.7 0 32-14.3 32-32V224c0-17.7-14.3-32-32-32zM350 856.2L263.9 770H350v86.2zM664 888H414V746c0-22.1-17.9-40-40-40H232V264h432v624z"></path></svg></i></button><pre class="line-numbers  language-bash"><code class="  language-bash">$CMDER_ROOT/config/profile.d/*.sh
$CMDER_ROOT/config/user-profile.sh
$HOME/.bashrc
<span aria-hidden="true" class="line-numbers-rows"><span></span><span></span><span></span></span></code></pre></div>
<p>所以我们可以在上面的文件中添加 alias 即可。</p>
<p>几个示例：</p>
<div class="_2Uzcx_"><button class="VJbwyy" type="button" aria-label="复制代码"><i aria-label="icon: copy" class="anticon anticon-copy"><svg viewBox="64 64 896 896" focusable="false" class="" data-icon="copy" width="1em" height="1em" fill="currentColor" aria-hidden="true"><path d="M832 64H296c-4.4 0-8 3.6-8 8v56c0 4.4 3.6 8 8 8h496v688c0 4.4 3.6 8 8 8h56c4.4 0 8-3.6 8-8V96c0-17.7-14.3-32-32-32zM704 192H192c-17.7 0-32 14.3-32 32v530.7c0 8.5 3.4 16.6 9.4 22.6l173.3 173.3c2.2 2.2 4.7 4 7.4 5.5v1.9h4.2c3.5 1.3 7.2 2 11 2H704c17.7 0 32-14.3 32-32V224c0-17.7-14.3-32-32-32zM350 856.2L263.9 770H350v86.2zM664 888H414V746c0-22.1-17.9-40-40-40H232V264h432v624z"></path></svg></i></button><pre class="line-numbers  language-shell"><code class="shell  language-shell">alias l.='ls -d .* --color=tty'
alias ll='ls -l --color=tty'
alias ls='ls --color=tty'
<span aria-hidden="true" class="line-numbers-rows"><span></span><span></span><span></span></span></code></pre></div>
<p>由于 Git for Windows 会自动创建 <code>~/.bash_profile</code>，而对此cmder会提示有冲突，此时可以创建一个<code>~/.profile</code>并在该文件中添加别名。（这里 <code>~</code>表示<code>$HOME</code>）</p>
<p><strong>3.PowerShell aliases：</strong></p>
<p>直接使用PowerShell 的 <code>alias</code>命令添加或在下面的文件中添加：</p>
<div class="_2Uzcx_"><button class="VJbwyy" type="button" aria-label="复制代码"><i aria-label="icon: copy" class="anticon anticon-copy"><svg viewBox="64 64 896 896" focusable="false" class="" data-icon="copy" width="1em" height="1em" fill="currentColor" aria-hidden="true"><path d="M832 64H296c-4.4 0-8 3.6-8 8v56c0 4.4 3.6 8 8 8h496v688c0 4.4 3.6 8 8 8h56c4.4 0 8-3.6 8-8V96c0-17.7-14.3-32-32-32zM704 192H192c-17.7 0-32 14.3-32 32v530.7c0 8.5 3.4 16.6 9.4 22.6l173.3 173.3c2.2 2.2 4.7 4 7.4 5.5v1.9h4.2c3.5 1.3 7.2 2 11 2H704c17.7 0 32-14.3 32-32V224c0-17.7-14.3-32-32-32zM350 856.2L263.9 770H350v86.2zM664 888H414V746c0-22.1-17.9-40-40-40H232V264h432v624z"></path></svg></i></button><pre class="line-numbers  language-dart"><code class="  language-dart"><span class="token string">'$ENV:CMDER_ROOT\config\profile.d\*.ps1'</span>
<span class="token string">'$ENV:CMDER_ROOT\config\user-profile.ps1'</span>
<span aria-hidden="true" class="line-numbers-rows"><span></span><span></span></span></code></pre></div>
<p>这里<code>$ENV:CMDER_ROOT</code> 指 cmder 的安装目录。</p>
<h2>Cmder启动选项</h2>
<div class="image-package">
<div class="image-container" style="max-width: 700px; max-height: 303px;">
<div class="image-container-fill" style="padding-bottom: 39.82%;"></div>
<div class="image-view" data-width="761" data-height="303"><img data-original-src="https://upload-images.jianshu.io/upload_images/7667789-b643de5f075b918d.png" data-original-width="761" data-original-height="303" data-original-format="image/png" data-original-filesize="13314" data-image-index="2" style="cursor: zoom-in;" class="image-loading"></div>
</div>
<div class="image-caption">cmder02.png</div>
</div>
<p>相关介绍</p>
<ul>
<li>
<p>在 启动（Startup）处设置 cmder 启动时需要执行的任务</p>
<p>默认选择的启动项是 <code>{cmd::Cmder}</code> 这个命名任务，我们可以更改成其它的命令任务或者直接切换到其它的启动项。</p>
<p>当选中某个命名任务时，下面的  "选中的任务内容" 下会显示该任务执行的具体内容</p>
</li>
<li><p>我们也可以在 <code>启动 -&gt; 任务</code>（<code>startup -&gt; tasks</code>）处更改和添加命名任务。</p></li>
</ul>
<blockquote>
<p>这里<code>cmd::Cmder</code>前面的cmd标明它是cmd模式，我们可以看到还有 bash 和 PowerShell等模式</p>
</blockquote>
<h3>自定义启动目录</h3>
<p>下面就来克隆现有的<code>{cmd::Cmder}</code>添加一个设置自定义的启动目录的任务(Task)：</p>
<div class="image-package">
<div class="image-container" style="max-width: 700px; max-height: 510px;">
<div class="image-container-fill" style="padding-bottom: 66.84%;"></div>
<div class="image-view" data-width="763" data-height="510"><img data-original-src="https://upload-images.jianshu.io/upload_images/7667789-dea640daf3733022.png" data-original-width="763" data-original-height="510" data-original-format="image/png" data-original-filesize="56937" data-image-index="3" style="cursor: zoom-in;" class="image-loading"></div>
</div>
<div class="image-caption">cmder03.png</div>
</div>
<p>设置启动目录</p>
<div class="image-package">
<div class="image-container" style="max-width: 700px; max-height: 508px;">
<div class="image-container-fill" style="padding-bottom: 66.75%;"></div>
<div class="image-view" data-width="761" data-height="508"><img data-original-src="https://upload-images.jianshu.io/upload_images/7667789-ba0fcc97010f0e25.png" data-original-width="761" data-original-height="508" data-original-format="image/png" data-original-filesize="35096" data-image-index="4" style="cursor: zoom-in;" class="image-loading"></div>
</div>
<div class="image-caption">cmder04.png</div>
</div>
<ul>
<li>任务参数：下面来看 “Task parameters”命令参数，阅读实例可知参数 <code>/icon</code>指定<strong>图标</strong>位置，<code>/dir</code> 指定启动目录，所以我们可以添加下面的参数：<code>/icon "%CMDER_ROOT%\icons\cmder.ico" /dir "C:\Users\Fan"</code>
</li>
<li>记得在 <code>startup</code> 的“ Specified named task” 处选择 <code>cmd::diy1</code>
</li>
<li>保存设置，退出，重新打开 cmder 查看效果</li>
</ul>
<h3>为任务添加快捷键</h3>
<p>在上图中我们可以发现还可以为每个任务设置 <code>热键</code> ，下面是我个人的热键设置：</p>
<ul>
<li>打开一个 cmd 任务标签页：<code>Alt+c</code>
</li>
<li>打开一个PowerShell 任务标签页：<code>Alt+p</code>
</li>
<li>打开一个 bash 任务标签页：<code>Alt+b</code>
</li>
<li>打开一个 WSL 任务标签页：<code>Alt+l</code>
</li>
</ul>
<h2>Cmder连接Linux子系统（WSL）</h2>
<p>Windows Subsystem for Linux（简称WSL）。</p>
<p>ConEmu（包括基于 ConEmu 修改的 cmder） 等终端模拟器也已经适配了 WSL 环境。</p>
<p>连接方式：</p>
<ul>
<li>添加一个标签页时（点击右下角的 ➕），选择 <code>WSL --&gt; bash</code>
</li>
<li>或直接将启动任务指定为 <code>{WSL::bash}</code>
</li>
</ul>
<p>Windows系统的分区全部挂载于Linux子系统的 <code>/mnt</code> 目录</p>
<div class="_2Uzcx_"><button class="VJbwyy" type="button" aria-label="复制代码"><i aria-label="icon: copy" class="anticon anticon-copy"><svg viewBox="64 64 896 896" focusable="false" class="" data-icon="copy" width="1em" height="1em" fill="currentColor" aria-hidden="true"><path d="M832 64H296c-4.4 0-8 3.6-8 8v56c0 4.4 3.6 8 8 8h496v688c0 4.4 3.6 8 8 8h56c4.4 0 8-3.6 8-8V96c0-17.7-14.3-32-32-32zM704 192H192c-17.7 0-32 14.3-32 32v530.7c0 8.5 3.4 16.6 9.4 22.6l173.3 173.3c2.2 2.2 4.7 4 7.4 5.5v1.9h4.2c3.5 1.3 7.2 2 11 2H704c17.7 0 32-14.3 32-32V224c0-17.7-14.3-32-32-32zM350 856.2L263.9 770H350v86.2zM664 888H414V746c0-22.1-17.9-40-40-40H232V264h432v624z"></path></svg></i></button><pre class="line-numbers  language-shell"><code class="shell  language-shell">$ ls /mnt
c  d  e  f  g
<span aria-hidden="true" class="line-numbers-rows"><span></span><span></span></span></code></pre></div>
<p>这表示可用<code>/mnt/c</code> 来访问 C: 盘；这里还可以进行一些调整（例如创建从<code>/c</code>到的符号链接<code>/mnt/c</code>）</p>
<p>也可以在<strong>Linux子系统中</strong>设置如下别名以便于切换：</p>
<div class="_2Uzcx_"><button class="VJbwyy" type="button" aria-label="复制代码"><i aria-label="icon: copy" class="anticon anticon-copy"><svg viewBox="64 64 896 896" focusable="false" class="" data-icon="copy" width="1em" height="1em" fill="currentColor" aria-hidden="true"><path d="M832 64H296c-4.4 0-8 3.6-8 8v56c0 4.4 3.6 8 8 8h496v688c0 4.4 3.6 8 8 8h56c4.4 0 8-3.6 8-8V96c0-17.7-14.3-32-32-32zM704 192H192c-17.7 0-32 14.3-32 32v530.7c0 8.5 3.4 16.6 9.4 22.6l173.3 173.3c2.2 2.2 4.7 4 7.4 5.5v1.9h4.2c3.5 1.3 7.2 2 11 2H704c17.7 0 32-14.3 32-32V224c0-17.7-14.3-32-32-32zM350 856.2L263.9 770H350v86.2zM664 888H414V746c0-22.1-17.9-40-40-40H232V264h432v624z"></path></svg></i></button><pre class="line-numbers  language-bash"><code class="bash  language-bash"># ~/.bashrc 
alias cdc='cd /mnt/c/'
alias cdd='cd /mnt/d/'
alias cde='cd /mnt/e/'
<span aria-hidden="true" class="line-numbers-rows"><span></span><span></span><span></span><span></span></span></code></pre></div>
<h2>其它问题</h2>
<h3>中文乱码</h3>
<p>在 <code>Startup -&gt; Environment</code> 中添加下面的语句：</p>
<div class="_2Uzcx_"><button class="VJbwyy" type="button" aria-label="复制代码"><i aria-label="icon: copy" class="anticon anticon-copy"><svg viewBox="64 64 896 896" focusable="false" class="" data-icon="copy" width="1em" height="1em" fill="currentColor" aria-hidden="true"><path d="M832 64H296c-4.4 0-8 3.6-8 8v56c0 4.4 3.6 8 8 8h496v688c0 4.4 3.6 8 8 8h56c4.4 0 8-3.6 8-8V96c0-17.7-14.3-32-32-32zM704 192H192c-17.7 0-32 14.3-32 32v530.7c0 8.5 3.4 16.6 9.4 22.6l173.3 173.3c2.2 2.2 4.7 4 7.4 5.5v1.9h4.2c3.5 1.3 7.2 2 11 2H704c17.7 0 32-14.3 32-32V224c0-17.7-14.3-32-32-32zM350 856.2L263.9 770H350v86.2zM664 888H414V746c0-22.1-17.9-40-40-40H232V264h432v624z"></path></svg></i></button><pre class="line-numbers  language-bash"><code class="  language-bash">set LANG=zh_CN.UTF-8
<span aria-hidden="true" class="line-numbers-rows"><span></span></span></code></pre></div>
<blockquote>
<p>如果没有出现乱码，则可以不添加。</p>
<p>如果打开的文本文件的编码方式不是 utf-8 那么在cmder中查看时会乱码，这种情况需要转换该文件的编码方式为 utf-8</p>
</blockquote>
<div class="image-package">
<div class="image-container" style="max-width: 700px; max-height: 243px;">
<div class="image-container-fill" style="padding-bottom: 31.929999999999996%;"></div>
<div class="image-view" data-width="761" data-height="243"><img data-original-src="https://upload-images.jianshu.io/upload_images/7667789-a3c4e6f00d7bdd85.png" data-original-width="761" data-original-height="243" data-original-format="image/png" data-original-filesize="27962" data-image-index="5" style="cursor: zoom-in;" class="image-loading"></div>
</div>
<div class="image-caption">cmder05.png</div>
</div>
<h3>查看git log时乱码</h3>
<p>这一般是git的配置问题，执行下面的命令，来配置git log的输出</p>
<div class="_2Uzcx_"><button class="VJbwyy" type="button" aria-label="复制代码"><i aria-label="icon: copy" class="anticon anticon-copy"><svg viewBox="64 64 896 896" focusable="false" class="" data-icon="copy" width="1em" height="1em" fill="currentColor" aria-hidden="true"><path d="M832 64H296c-4.4 0-8 3.6-8 8v56c0 4.4 3.6 8 8 8h496v688c0 4.4 3.6 8 8 8h56c4.4 0 8-3.6 8-8V96c0-17.7-14.3-32-32-32zM704 192H192c-17.7 0-32 14.3-32 32v530.7c0 8.5 3.4 16.6 9.4 22.6l173.3 173.3c2.2 2.2 4.7 4 7.4 5.5v1.9h4.2c3.5 1.3 7.2 2 11 2H704c17.7 0 32-14.3 32-32V224c0-17.7-14.3-32-32-32zM350 856.2L263.9 770H350v86.2zM664 888H414V746c0-22.1-17.9-40-40-40H232V264h432v624z"></path></svg></i></button><pre class="line-numbers  language-csharp"><code class="  language-csharp">git config <span class="token operator">--</span><span class="token keyword">global</span> i18n<span class="token punctuation">.</span>logoutputencoding utf<span class="token operator">-</span><span class="token number">8</span>
<span aria-hidden="true" class="line-numbers-rows"><span></span></span></code></pre></div>
<blockquote>
<p>或者在 .gitconfig 文件中配置</p>
<p>更多git乱码问题见： <a href="https://links.jianshu.com/go?to=https%3A%2F%2Fblog.csdn.net%2Fguiying123456%2Farticle%2Fdetails%2F62881400" target="_blank">cmder中文乱码 </a></p>
</blockquote>
<h3>ssh agent</h3>
<p>每次想要向远程git仓库推送更新时，都需要先启动ssh代理，再加载(使用ssh-add)私钥，否则就报错而感到很烦。那么可以参考下面的解决方法：</p>
<p><strong>cmd 模式中：</strong></p>
<p>官方文档中有说在 cmd 模式中如何处理 ssh agent的相关问题：</p>
<p>To start the vendored SSH agent simply call <code>start-ssh-agent</code>, which is in the <code>vendor/git-for-windows/cmd</code> folder.</p>
<p>If you want to run SSH agent on startup, include the line <code>@call "%GIT_INSTALL_ROOT%/cmd/start-ssh-agent.cmd"</code> in <code>%CMDER_ROOT%/config/user-profile.cmd</code> (usually just uncomment it).</p>
<p><strong>bash模式中：</strong></p>
<p>官方文档中没有说如何在bash模式中处理ssh-agent的问题，但我们可以这样解决。</p>
<p>在<code>$HOME/.bashrc</code>或<code>$HOME/.profilec</code>文件中添加如下内容：</p>
<div class="_2Uzcx_"><button class="VJbwyy" type="button" aria-label="复制代码"><i aria-label="icon: copy" class="anticon anticon-copy"><svg viewBox="64 64 896 896" focusable="false" class="" data-icon="copy" width="1em" height="1em" fill="currentColor" aria-hidden="true"><path d="M832 64H296c-4.4 0-8 3.6-8 8v56c0 4.4 3.6 8 8 8h496v688c0 4.4 3.6 8 8 8h56c4.4 0 8-3.6 8-8V96c0-17.7-14.3-32-32-32zM704 192H192c-17.7 0-32 14.3-32 32v530.7c0 8.5 3.4 16.6 9.4 22.6l173.3 173.3c2.2 2.2 4.7 4 7.4 5.5v1.9h4.2c3.5 1.3 7.2 2 11 2H704c17.7 0 32-14.3 32-32V224c0-17.7-14.3-32-32-32zM350 856.2L263.9 770H350v86.2zM664 888H414V746c0-22.1-17.9-40-40-40H232V264h432v624z"></path></svg></i></button><pre class="line-numbers  language-shell"><code class="shell  language-shell"># 启动一个 ssh-agent 进程 
eval "$(ssh-agent -s)"
# 这里同时添加了两个私钥
ssh-add "C:/Users/Fan/.ssh/one_rsa" "C:/Users/Fan/.ssh/two_id_rsa"
# 清除上面命令的输出内容
clear
<span aria-hidden="true" class="line-numbers-rows"><span></span><span></span><span></span><span></span><span></span><span></span></span></code></pre></div>
<blockquote>
<p>更多 ssh-agent 介绍可参考: <a href="https://www.jianshu.com/p/8e88d4b11dec" target="_blank">SSH相关命令 </a>中的ssh-agent部分</p>
<p>或者查看：<a href="https://links.jianshu.com/go?to=https%3A%2F%2Fdev.to%2Fqm3ster%2Fsetting-up-gitsshgpg-on-windows-5c85" target="_blank">Setting up git+ssh+gpg on Windows</a></p>
</blockquote>
<h2>补充</h2>
<p>点击右下角的锁（🔒 :lock: ）即可锁定视窗 ，可以让窗口无法再输入内容。</p>
<h3>正确退出</h3>
<p>我们一直是习惯于直接点击右上角的 × 来关闭程序，但是正确的退出方法应该是在cmder中输入 <code>exit</code> 来进行退出，只有这样退出历史记录才会保留，你在下次打开cmder时才可向上翻看上次历史。</p>
<h3>Cmder系列文章</h3>
<p>下面是我的系列文章</p>
<ul>
<li><a href="https://links.jianshu.com/go?to=https%3A%2F%2Fwww.thisfaner.com%2Fposts%2Ftools%2Fcmder%2F" target="_blank">Cmder入门配置 – 就是这个范儿</a></li>
<li><a href="https://links.jianshu.com/go?to=https%3A%2F%2Fwww.thisfaner.com%2Fposts%2Ftools%2Fcmder%25E8%25BF%259B%25E9%2598%25B6%25E9%2585%258D%25E7%25BD%25AE%2F" target="_blank">Cmder进阶配置 – 就是这个范儿</a></li>
<li><a href="https://links.jianshu.com/go?to=https%3A%2F%2Fwww.thisfaner.com%2Fposts%2Ftools%2F%25E6%25B7%25B1%25E5%25BA%25A6%25E5%25AE%259A%25E5%2588%25B6cmder%2F" target="_blank">深度定制Cmder – 就是这个范儿</a></li>
<li><a href="https://links.jianshu.com/go?to=https%3A%2F%2Fwww.thisfaner.com%2Fposts%2Fdevops%2Fwindows%2Fpowershell%25E4%25B8%25BB%25E9%25A2%2598%25E8%25AE%25BE%25E7%25BD%25AE%2F" target="_blank">PowerShell主题设置 – 就是这个范儿</a></li>
<li><a href="https://links.jianshu.com/go?to=https%3A%2F%2Fwww.thisfaner.com%2Fposts%2Ftools%2Fpowerlevel9kzsh%25E4%25B8%258B%25E6%259C%2580%25E6%25A3%2592%25E7%259A%2584powerline%25E4%25B8%25BB%25E9%25A2%2598%2F" target="_blank">Powerlevel9k：zsh下最棒的Powerline主题 – 就是这个范儿</a></li>
</ul>
<p>如果想要将Cmder对应的任务标签页配置为如下效果，则可参考该系列文章：</p>
<ul>
<li>
<p></p>
<p></p>
在Cmd下的效果：<div class="image-package">
<div class="image-container" style="max-width: 700px; max-height: 424px;">
<div class="image-container-fill" style="padding-bottom: 43.0%;"></div>
<div class="image-view" data-width="986" data-height="424"><img data-original-src="https://upload-images.jianshu.io/upload_images/7667789-1a6ed28bd6b97073.png" data-original-width="986" data-original-height="424" data-original-format="image/png" data-original-filesize="30427" data-image-index="6" style="cursor: zoom-in;" class="image-loading"></div>
</div>
<div class="image-caption">cmder-cmd-20191215162952.png</div>
</div>
</li>
<li>
<p></p>
<p></p>
PowerShell下不同主题的效果：<div class="image-package">
<div class="image-container" style="max-width: 700px; max-height: 328px;">
<div class="image-container-fill" style="padding-bottom: 44.81%;"></div>
<div class="image-view" data-width="732" data-height="328"><img data-original-src="https://upload-images.jianshu.io/upload_images/7667789-1c39094b99509f9c.png" data-original-width="732" data-original-height="328" data-original-format="image/png" data-original-filesize="53308" data-image-index="7" style="cursor: zoom-in;" class="image-loading"></div>
</div>
<div class="image-caption">powershell-theme01.png</div>
</div>
</li>
<li>
<p></p>
<p></p>
WSL bash下的效果：<div class="image-package">
<div class="image-container" style="max-width: 700px; max-height: 424px;">
<div class="image-container-fill" style="padding-bottom: 43.0%;"></div>
<div class="image-view" data-width="986" data-height="424"><img data-original-src="https://upload-images.jianshu.io/upload_images/7667789-0d3b2d8b9dbeecdf.png" data-original-width="986" data-original-height="424" data-original-format="image/png" data-original-filesize="59056" data-image-index="8" style="cursor: zoom-in;" class="image-loading"></div>
</div>
<div class="image-caption">cmder-zsh-p9k-20191215153654.png</div>
</div>
</li>
</ul>
<h3>参考</h3>
<p>官方文档：</p>
<ul>
<li>Readme：<a href="https://links.jianshu.com/go?to=https%3A%2F%2Fgithub.com%2Fcmderdev%2Fcmder%2Fblob%2Fmaster%2FREADME.md" target="_blank">cmder/README.md at master · cmderdev/cmder</a>
</li>
<li>wiki：<a href="https://links.jianshu.com/go?to=https%3A%2F%2Fgithub.com%2Fcmderdev%2Fcmder%2Fwiki" target="_blank">Home · cmderdev/cmder Wiki</a>
</li>
</ul>
