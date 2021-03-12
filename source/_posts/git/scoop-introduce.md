---
title: "Scoop简识"
date:       2020-03-04
subtitle: "Windows下常用的包管理工具"
tags:
	- base
	- cmder
---








本文转载自:[Scoop包管理工具](https://www.thisfaner.com/posts/devops/windows/scoop%E5%8C%85%E7%AE%A1%E7%90%86%E5%B7%A5%E5%85%B7/#scoop%E5%B8%B8%E7%94%A8%E5%91%BD%E4%BB%A4)

      
<h2 id="scoop-包管理工具介绍">Scoop 包管理工具介绍<span class="anchor hide" data-clipboard-text="https://www.thisfaner.com/posts/devops/windows/scoop%25E5%258C%2585%25E7%25AE%25A1%25E7%2590%2586%25E5%25B7%25A5%25E5%2585%25B7/#scoop-包管理工具介绍" aria-label="null" style="position: relative;"><span style="font-size: 1rem; position: absolute; top: 50%; transform: translateY(-50%); right: -2rem;">🔗</span></span></h2>
<p>Windows下常用的包管理工具有：</p>
<ul>
<li>Scoop</li>
<li>Chocolatey</li>
</ul>
<p>由于Scoop更容易配置（相比于Chocolatey），这里选择 Scoop</p>
<p>使用Scoop安装最佳的应用程序通常称为“便携式”应用程序：即在解压缩时独立运行的压缩程序文件，不存在更改注册表或将文件放在程序目录之外的副作用。</p>
<p>对于像 VirtualBox、Docker for Windows 这些需要高权限的软件还是会用安装包在用户界面下自定义安装。</p>
<p><strong>对比Scoop和Chocolatey：</strong></p>
<p>Chocolatey 能更加全面地包办绝大多数的软件安装，适应重度需求；而 Scoop 则更加简单利落，容易自定义软件包，适应中低需求。</p>
<p>Chocolatey 的安装脚本默认要求管理员权限安装，同时非管理员安装默认路径是&nbsp;<code>C:\ProgramData\chocoportable</code>，这对于非高权限用户来说不太友好（比如没有管理员权限的工作机安装会比较折腾），而 Scoop 默认仅需普通用户权限，安装路径是&nbsp;<code>%USERPROFILE%\scoop</code>&nbsp;则显得比较清新，不过这都是<strong>可以根据需求修改</strong>的了。</p>
<p>Scoop更专注于开源的命令行开发人员工具 。</p>
<p>Github页面： <a href="https://github.com/lukesampson/scoop" title="lukesampson/scoop: A command-line installer for Windows.">scoop: A command-line installer for Windows.</a></p>
<h2 id="scoop安装配置">Scoop安装配置<span class="anchor hide" data-clipboard-text="https://www.thisfaner.com/posts/devops/windows/scoop%25E5%258C%2585%25E7%25AE%25A1%25E7%2590%2586%25E5%25B7%25A5%25E5%2585%25B7/#scoop安装配置" style="position: relative;"><span style="font-size: 1rem; position: absolute; top: 50%; transform: translateY(-50%); right: -2rem;">🔗</span></span></h2>
<p>默认设置已配置为用户级别<strong>安装的程序</strong>和Scoop本身都位于 <code>C:\Users\&lt;user&gt;\scoop </code></p>
<p>全局安装的程序（所有用户可用）（<code>--global</code>）位于<code>C\ProgramData\scoop</code>中。可以通过环境变量更改这些设置 。</p>
<p>所以安装时先通过配置环境变量来配置其安装路径；然后在PowerShell运行命令下载。</p>
<p><strong>Install Scoop to a Custom Directory</strong></p>
<div data-lang="Code" class="language-code"><pre><code>[environment]::setEnvironmentVariable('SCOOP','D:\Scoop','User')
$env:SCOOP='D:\Scoop'
iex (new-object net.webclient).downloadstring('https://get.scoop.sh')
</code></pre><span class="copy-to-clipboard" title="Copy to clipboard"></span></div><blockquote>
<p>相当于在用户变量中设置  <code>SCOOP=D:\Scoop</code></p>
<p>具体安装方法见其Github</p>
</blockquote>
<p><strong>Configure Scoop to install global programs to a Custom Directory</strong>（可选，建议不改）</p>
<div data-lang="Code" class="language-code"><pre><code>[environment]::setEnvironmentVariable('SCOOP_GLOBAL','D:\Scoop\GlobalScoopApps','Machine')
$env:SCOOP_GLOBAL='D:\Scoop\GlobalScoopApps'
</code></pre><span class="copy-to-clipboard" title="Copy to clipboard"></span></div><blockquote>
<p>相当于在系统变量中设置： <code>SCOOP_GLOBAL=D:\Scoop\GlobalScoopApps</code>；默认是在  <code>C:\ProgramData\scoop</code>，感觉不应该更改。</p>
</blockquote>
<p>为什么需要全局安装呢？我想应该 对于那些 要求管理员权限的程序需要安装在全局</p>
<p><a href="https://github.com/lukesampson/scoop/wiki/Global-Installs">Global Installs / scoop Wiki</a> ，像字体等需要给所有用户使用，所以需要使用全局安装。</p>
<div class="highlight"><div class="chroma">
<table class="lntable"><tbody><tr><td class="lntd">
<div data-lang="Code" class="language-code"><pre class="chroma"><code><span class="lnt">1
</span><span class="lnt">2
</span><span class="lnt">3
</span><span class="lnt">4
</span><span class="lnt">5
</span><span class="lnt">6
</span></code></pre><span class="copy-to-clipboard" title="Copy to clipboard"></span></div></td>
<td class="lntd">
<pre class="chroma"><code class="language-powershell" data-lang="powershell"><span class="c"># 初次安装也可选择安装下面这些，其中sudo要先进行本地安装</span>
<span class="n">scoop</span> <span class="n">install</span> <span class="n">sudo</span>
<span class="c"># 下面是全局安装的示例：个人感觉这几个软件还是直接进行本地安装更好</span>
<span class="n">sudo</span> <span class="n">scoop</span> <span class="n">install</span> <span class="n">7zip</span> <span class="n">git</span> <span class="n">openssh</span> <span class="p">-</span><span class="n">-global</span>
<span class="c"># 更新同样需要sudo 和 -g</span>
<span class="n">sudo</span> <span class="n">scoop</span> <span class="n">update</span> <span class="n">7zip</span> <span class="n">-g</span>
</code></pre><span class="copy-to-clipboard" title="Copy to clipboard"></span></td></tr></tbody></table>
</div>
</div><p><strong>Multi-connection downloads with aria2</strong></p>
<p>scoop可通过aria2来进行多任务下载：</p>
<div class="highlight"><div class="chroma">
<table class="lntable"><tbody><tr><td class="lntd">
<div data-lang="Code" class="language-code"><pre class="chroma"><code><span class="lnt">1
</span></code></pre><span class="copy-to-clipboard" title="Copy to clipboard"></span></div></td>
<td class="lntd">
<pre class="chroma"><code class="language-shell" data-lang="shell">scoop install aria2
</code></pre><span class="copy-to-clipboard" title="Copy to clipboard"></span></td></tr></tbody></table>
</div>
</div><h2 id="scoop常用命令">Scoop常用命令<span class="anchor hide" data-clipboard-text="https://www.thisfaner.com/posts/devops/windows/scoop%25E5%258C%2585%25E7%25AE%25A1%25E7%2590%2586%25E5%25B7%25A5%25E5%2585%25B7/#scoop常用命令" style="position: relative;"><span style="font-size: 1rem; position: absolute; top: 50%; transform: translateY(-50%); right: -2rem;">🔗</span></span></h2>
<div class="highlight"><div class="chroma">
<table class="lntable"><tbody><tr><td class="lntd">
<div data-lang="Code" class="language-code"><pre class="chroma"><code><span class="lnt"> 1
</span><span class="lnt"> 2
</span><span class="lnt"> 3
</span><span class="lnt"> 4
</span><span class="lnt"> 5
</span><span class="lnt"> 6
</span><span class="lnt"> 7
</span><span class="lnt"> 8
</span><span class="lnt"> 9
</span><span class="lnt">10
</span><span class="lnt">11
</span><span class="lnt">12
</span><span class="lnt">13
</span></code></pre><span class="copy-to-clipboard" title="Copy to clipboard"></span></div></td>
<td class="lntd">
<pre class="chroma"><code class="language-shell" data-lang="shell">scoop <span class="nb">help</span> <span class="c1">#查看帮助</span>
scoop <span class="nb">help</span> &lt;某个命令&gt; <span class="c1"># 具体查看某个命令的帮助</span>
scoop install <span class="c1">#安装 APP</span>
scoop uninstall <span class="c1">#卸载 APP</span>
scoop list <span class="c1">#列出已安装的 APP</span>
scoop search <span class="c1">#搜索 APP</span>
scoop update <span class="c1">#更新 Scoop 自身</span>
scoop update appName1 appName2 <span class="c1"># 更新某些app</span>
scoop update *  <span class="c1"># 更新所有 app （前提是需要在apps目录下操作）</span>
scoop status <span class="c1"># 检查哪些软件有更新</span>
scoop bucket known <span class="c1">#通过此命令列出已知所有 bucket（软件源）</span>
scoop bucket add bucketName <span class="c1">#添加某个 bucket</span>
scoop cache rm &lt;app&gt; <span class="c1"># 移除某个app的缓存</span>
</code></pre><span class="copy-to-clipboard" title="Copy to clipboard"></span></td></tr></tbody></table>
</div>
</div><ul>
<li>
<p><strong>对于GUI程序</strong>，scoop会自动为其在开始菜单中添加快捷方式 ，路径： <code>C:\Users\Fan Dean\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Scoop Apps</code></p>
</li>
<li>
<p><strong>对于命令行程序</strong>，scoop会自动在 scoop应用安装路径下的 shims 文件夹下为其添加对应的exe程序，而shims文件夹是被添加到 PATH 变量中，所以可以直接在命令行中运行刚安装的程序。</p>
</li>
</ul>
<p><strong>安装 curl 、grep</strong></p>
<div data-lang="Code" class="language-code"><pre><code>scoop install curl grep
</code></pre><span class="copy-to-clipboard" title="Copy to clipboard"></span></div><p>我们发现，下载的过程中自动下载了依赖7-zip。 在安装方面，它利用了7zip去解压安装包/压缩包，因此它对绿色软件有天生的友好属性。 。不仅如此，<strong>下载之后的内容会自动将加入到（Path）环境变量中</strong>。十分方便。大家都可以自己尝试为一些免安装软件建立软件源（需要安装的软件比较复杂，需要一定门槛）</p>
<blockquote>
<p>Scoop 是一个强大的工具，有着极大的可玩性、设计与实现理念，包括但不限于 <code>shim</code> 的软链接理念、利用 <code>persist</code> 存储<strong>用户数据</strong>等等，如果你感兴趣，请直接参考 <a href="https://github.com/lukesampson/scoop/wiki">Scoop 官方的 Wiki</a>。</p>
</blockquote>
<h2 id="添加软件源bucket">添加软件源Bucket<span class="anchor hide" data-clipboard-text="https://www.thisfaner.com/posts/devops/windows/scoop%25E5%258C%2585%25E7%25AE%25A1%25E7%2590%2586%25E5%25B7%25A5%25E5%2585%25B7/#添加软件源bucket" style="position: relative;"><span style="font-size: 1rem; position: absolute; top: 50%; transform: translateY(-50%); right: -2rem;">🔗</span></span></h2>
<p>Scoop说自己的软件源为Bucket，也可以称其为软件源或仓库。</p>
<p>参考：</p>
<ul>
<li><a href="https://github.com/lukesampson/scoop/wiki/Buckets#creating-your-own-bucket" title="Buckets · lukesampson/scoop Wiki">Buckets · lukesampson/scoop Wiki</a></li>
</ul>
<div data-lang="Code" class="language-code"><pre><code># bucket的用法
scoop bucket add|list|known|rm [&lt;args&gt;]
</code></pre><span class="copy-to-clipboard" title="Copy to clipboard"></span></div><p>一个添加第三方bucket的示例：</p>
<div data-lang="Code" class="language-code"><pre><code>scoop bucket add dorado https://github.com/h404bi/dorado
</code></pre><span class="copy-to-clipboard" title="Copy to clipboard"></span></div><p>明确指定安装此软件源中的的程序</p>
<div data-lang="Code" class="language-code"><pre><code>scoop install dorado/&lt;app_name&gt;
# 下面是dorado中特有的软件，测试其是否添加成功
scoop search trash
</code></pre><span class="copy-to-clipboard" title="Copy to clipboard"></span></div><p>推荐的Bucket：</p>
<ul>
<li><code>extras</code>：Scoop 官方维护的一个仓库，涵盖了大部分因为种种原因不能被收录进主仓库的常用软件。地址：<a href="https://github.com/lukesampson/scoop-extras/tree/master/bucket">lukesampson/scoop-extras</a></li>
<li><code>nirsoft</code>：是一个 NirSoft 开发的小工具的安装合集。NirSoft 制作了大量的（dozens and dozens）小工具，包括系统工具、网络工具、密码恢复等等，孜孜不倦、持续更新。
<ul>
<li>Bucket 地址：<a href="https://github.com/kodybrown/scoop-nirsoft">kodybrown/scoop-nirsoft</a></li>
<li>NirSoft 官网地址：<a href="https://www.nirsoft.net/">NirSoft</a></li>
</ul>
</li>
<li>dorado（对中文支持更好）<a href="https://github.com/h404bi/dorado">h404bi/dorado: 🐟 A bucket of Scoop, for h404bi</a></li>
<li>ash258：<a href="https://github.com/Ash258/scoop-Ash258">Ash258/scoop-Ash258: Personal bucket with wide variety of applications of all kind.</a></li>
<li>java：</li>
<li>nerd-fonts ：包含各种字体</li>
</ul>
<div class="highlight"><div class="chroma">
<table class="lntable"><tbody><tr><td class="lntd">
<div data-lang="Code" class="language-code"><pre class="chroma"><code><span class="lnt">1
</span><span class="lnt">2
</span><span class="lnt">3
</span><span class="lnt">4
</span><span class="lnt">5
</span><span class="lnt">6
</span><span class="lnt">7
</span><span class="lnt">8
</span><span class="lnt">9
</span></code></pre><span class="copy-to-clipboard" title="Copy to clipboard"></span></div></td>
<td class="lntd">
<pre class="chroma"><code class="language-shell" data-lang="shell"><span class="c1"># 先添加bucket</span>
scoop bucket add extras
scoop bucket add nirsoft
scoop bucket add dorado https://github.com/h404bi/dorado
scoop bucket add Ash258 <span class="s1">'https://github.com/Ash258/Scoop-Ash258.git'</span>
scoop bucket add nerd-fonts
<span class="c1"># 对于开发人员，可添加</span>
scoop bucket add java
scoop bucket add versions
</code></pre><span class="copy-to-clipboard" title="Copy to clipboard"></span></td></tr></tbody></table>
</div>
</div><h2 id="bucket更新时遇到问题">bucket更新时遇到问题<span class="anchor hide" data-clipboard-text="https://www.thisfaner.com/posts/devops/windows/scoop%25E5%258C%2585%25E7%25AE%25A1%25E7%2590%2586%25E5%25B7%25A5%25E5%2585%25B7/#bucket更新时遇到问题" style="position: relative;"><span style="font-size: 1rem; position: absolute; top: 50%; transform: translateY(-50%); right: -2rem;">🔗</span></span></h2>
<p>由于extras bucket更新时遇到问题，我将其删除后再添加提示成功，但是它却把 main bucket及默认的bucket给删除了。通过"scoop status"检查状态时出现"These app manifests have been removed"并且下面列出了已被移除的软件名单。<strong>那么如何将 main bucket重新添加进来？</strong></p>
<div class="highlight"><div class="chroma">
<table class="lntable"><tbody><tr><td class="lntd">
<div data-lang="Code" class="language-code"><pre class="chroma"><code><span class="lnt"> 1
</span><span class="lnt"> 2
</span><span class="lnt"> 3
</span><span class="lnt"> 4
</span><span class="lnt"> 5
</span><span class="lnt"> 6
</span><span class="lnt"> 7
</span><span class="lnt"> 8
</span><span class="lnt"> 9
</span><span class="lnt">10
</span><span class="lnt">11
</span><span class="lnt">12
</span><span class="lnt">13
</span><span class="lnt">14
</span><span class="lnt">15
</span><span class="lnt">16
</span><span class="lnt">17
</span></code></pre><span class="copy-to-clipboard" title="Copy to clipboard"></span></div></td>
<td class="lntd">
<pre class="chroma"><code class="language-shell" data-lang="shell">scoop <span class="nb">help</span> bucket
scoop bucket known <span class="c1">#通过此命令列出已知所有 bucket</span>

$ scoop bucket known <span class="c1"># 示列</span>
main
extras
versions
nightlies
nirsoft
php
nerd-fonts
nonportable
java
games
jetbrains

scoop bucket add main <span class="c1">#添加 main bucket</span>
</code></pre><span class="copy-to-clipboard" title="Copy to clipboard"></span></td></tr></tbody></table>
</div>
</div><h2 id="网络问题安装失败">网络问题安装失败<span class="anchor hide" data-clipboard-text="https://www.thisfaner.com/posts/devops/windows/scoop%25E5%258C%2585%25E7%25AE%25A1%25E7%2590%2586%25E5%25B7%25A5%25E5%2585%25B7/#网络问题安装失败" style="position: relative;"><span style="font-size: 1rem; position: absolute; top: 50%; transform: translateY(-50%); right: -2rem;">🔗</span></span></h2>
<p>比如安装irfanview一直失败，查看信息</p>
<div class="highlight"><div class="chroma">
<table class="lntable"><tbody><tr><td class="lntd">
<div data-lang="Code" class="language-code"><pre class="chroma"><code><span class="lnt">1
</span><span class="lnt">2
</span></code></pre><span class="copy-to-clipboard" title="Copy to clipboard"></span></div></td>
<td class="lntd">
<pre class="chroma"><code class="language-shell" data-lang="shell">ERROR Download failed! <span class="o">(</span>Error 1<span class="o">)</span> An unknown error occurred
ERROR https://www.irfanview.info/files/iview453_x64.zip
</code></pre><span class="copy-to-clipboard" title="Copy to clipboard"></span></td></tr></tbody></table>
</div>
</div><p>看另一个示例：</p>
<div class="highlight"><div class="chroma">
<table class="lntable"><tbody><tr><td class="lntd">
<div data-lang="Code" class="language-code"><pre class="chroma"><code><span class="lnt">1
</span></code></pre><span class="copy-to-clipboard" title="Copy to clipboard"></span></div></td>
<td class="lntd">
<pre class="chroma"><code class="language-shell" data-lang="shell">scoop install mediainfo
</code></pre><span class="copy-to-clipboard" title="Copy to clipboard"></span></td></tr></tbody></table>
</div>
</div><p>也是下载不下来，从输出信息中可以看到如下内容</p>
<div data-lang="Code" class="language-code"><pre><code>ERROR Download failed! (Error 1) An unknown error occurred
ERROR https://mediaarea.net/download/binary/mediainfo/19.09/MediaInfo_CLI_19.09_Windows_x64.zip
    referer=https://mediaarea.net/download/binary/mediainfo/19.09/
    dir=D:\Scoop\Applications\cache
    out=mediainfo#19.09#https_mediaarea.net_download_binary_mediainfo_19.09_MediaInfo_CLI_19.09_Windows_x64.zip

ERROR &amp; 'D:\Scoop\Applications\apps\aria2\current\aria2c.exe' --input-file='D:\Scoop\Applications\cache\mediainfo.txt'
</code></pre><span class="copy-to-clipboard" title="Copy to clipboard"></span></div><p>我们可以发现文件的下载路径和下载后的文件名称，这里 <code>out=</code> 后面的压缩包就是下载后文件的名称，(也可以在 mediainfo.txt 中找到)</p>
<p>然后我们可以尝试在浏览器下载该程序，再更改文件名放入 sxoop 的 cache 目录，最后再次运行 scoop install mediainfo 即可安装。</p>
<hr>
<blockquote>
<p>下面的内容只是个人的一些记录，还有待补充和完善</p>
</blockquote>
<h2 id="已安装软件列表">已安装软件列表<span class="anchor hide" data-clipboard-text="https://www.thisfaner.com/posts/devops/windows/scoop%25E5%258C%2585%25E7%25AE%25A1%25E7%2590%2586%25E5%25B7%25A5%25E5%2585%25B7/#已安装软件列表" style="position: relative;"><span style="font-size: 1rem; position: absolute; top: 50%; transform: translateY(-50%); right: -2rem;">🔗</span></span></h2>
<p>添加额外的extras bucket：</p>
<div class="highlight"><div class="chroma">
<table class="lntable"><tbody><tr><td class="lntd">
<div data-lang="Code" class="language-code"><pre class="chroma"><code><span class="lnt">1
</span></code></pre><span class="copy-to-clipboard" title="Copy to clipboard"></span></div></td>
<td class="lntd">
<pre class="chroma"><code class="language-shell" data-lang="shell">scoop bucket add extras
</code></pre><span class="copy-to-clipboard" title="Copy to clipboard"></span></td></tr></tbody></table>
</div>
</div><p>离线文档查看 zeal ：可集成到 idea 等</p>
<div class="highlight"><div class="chroma">
<table class="lntable"><tbody><tr><td class="lntd">
<div data-lang="Code" class="language-code"><pre class="chroma"><code><span class="lnt">1
</span></code></pre><span class="copy-to-clipboard" title="Copy to clipboard"></span></div></td>
<td class="lntd">
<pre class="chroma"><code class="language-shell" data-lang="shell">λ scoop install zeal
</code></pre><span class="copy-to-clipboard" title="Copy to clipboard"></span></td></tr></tbody></table>
</div>
</div><p><strong>视频播放器 mpv</strong></p>
<div class="highlight"><div class="chroma">
<table class="lntable"><tbody><tr><td class="lntd">
<div data-lang="Code" class="language-code"><pre class="chroma"><code><span class="lnt">1
</span></code></pre><span class="copy-to-clipboard" title="Copy to clipboard"></span></div></td>
<td class="lntd">
<pre class="chroma"><code class="language-shell" data-lang="shell">λ scoop install mpv
</code></pre><span class="copy-to-clipboard" title="Copy to clipboard"></span></td></tr></tbody></table>
</div>
</div><p><strong>文件同步工具 syncthing</strong>，在GitHub上超级火爆</p>
<div class="highlight"><div class="chroma">
<table class="lntable"><tbody><tr><td class="lntd">
<div data-lang="Code" class="language-code"><pre class="chroma"><code><span class="lnt">1
</span></code></pre><span class="copy-to-clipboard" title="Copy to clipboard"></span></div></td>
<td class="lntd">
<pre class="chroma"><code class="language-shell" data-lang="shell">λ scoop install syncthing
</code></pre><span class="copy-to-clipboard" title="Copy to clipboard"></span></td></tr></tbody></table>
</div>
</div><p><strong>ImageMagick 看图软件</strong>可以安装其替代品 GraphicsMagick</p>
<p>SVN</p>
<div data-lang="Code" class="language-code"><pre><code>scoop install sliksvn
scoop install xx-net
</code></pre><span class="copy-to-clipboard" title="Copy to clipboard"></span></div><p><strong>idea-ultimate：</strong></p>
<div data-lang="Code" class="language-code"><pre><code>scoop install idea-ultimate
</code></pre><span class="copy-to-clipboard" title="Copy to clipboard"></span></div><div data-lang="Code" class="language-code"><pre><code>scoop install sumatrapdf
</code></pre><span class="copy-to-clipboard" title="Copy to clipboard"></span></div><h2 id="推荐的软件">推荐的软件<span class="anchor hide" data-clipboard-text="https://www.thisfaner.com/posts/devops/windows/scoop%25E5%258C%2585%25E7%25AE%25A1%25E7%2590%2586%25E5%25B7%25A5%25E5%2585%25B7/#推荐的软件" style="position: relative;"><span style="font-size: 1rem; position: absolute; top: 50%; transform: translateY(-50%); right: -2rem;">🔗</span></span></h2>
<blockquote>
<p>这里记录了Github上各种bucket，<a href="https://github.com/rasa/scoop-directory">rasa/scoop-directory: A directory of buckets for the scoop package manager for Windows</a> 相当于Scoop的第三方软件源。</p>
</blockquote>
<p>新机安装顺序：</p>
<ul>
<li>可选：Google官网下载Chrome下载器</li>
<li>先安装 scoop，将其配置好；再为scoop添加下面几个软件源：extras、dorado（对中文支持更好）、ash258、java</li>
<li>通过scoop安装cmder（或者安装WindowsTerminal）、RunAny（第一次使用scoop安装其他程序时就会自动安装7z）</li>
<li>通过scoop安装必要软件</li>
</ul>
<p>按安装方式进行分类</p>
<p>下载exe安装包安装：</p>
<ul>
<li>
<p>Firefox：使用scoop下载的话会出现无法更改语言和添加插件；使用PortableApp下载速度又贼慢</p>
<p>Firefox最新版本下载：根据此处（<a href="https://ftp.mozilla.org/pub/firefox/releases/latest/README.txt">latest Firefox release</a>）说明，拼出下面的下载地址（Win64，简体中文）</p>
<div data-lang="Code" class="language-code"><pre><code>https://download.mozilla.org/?product=firefox-latest&amp;os=win64&amp;lang=zh-CN
</code></pre><span class="copy-to-clipboard" title="Copy to clipboard"></span></div></li>
<li>
<p>Chrome浏览器：直接在官网下载（是一个安装器），通过安装器安装的Chrome在之后更新时无需翻墙</p>
</li>
</ul>
<p>通过压缩包安装：</p>
<ul>
<li><a href="https://www.iplaysoft.com/runany.html">RunAny - 开源免费“一劳永逸”的热键快速启动工具 </a> 非常不错的工具，它的快捷键是`，如果要在文件中输入它，需要先按 “win”键。</li>
<li>ZoomIt：用作教鞭。通过Scoop无法安装它。ZoomIt是由微软工作人员开发的 <a href="https://docs.microsoft.com/en-us/sysinternals/downloads/">Sysinternals Utilities</a> 系列中的一个，我们也可以选择通过scoop安装所有工具</li>
</ul>
<p>通过Scoop安装：</p>
<ul>
<li>Cmder：Windows下替代cmd的终端</li>
<li>各种可在命令行使用的开发相关的程序</li>
<li>geekuninstaller：著名的卸载工具，能够完全清理卸载残留</li>
<li>vscode-portable ：VS code 在scoop中已经有绿色版</li>
<li>qbittorrent：BT下载软件</li>
<li>notepadplusplus：替代默认记事本的程序</li>
<li>7-zip：</li>
<li>uGet：简洁无广告的下载工具（Linux上可用）</li>
</ul>
