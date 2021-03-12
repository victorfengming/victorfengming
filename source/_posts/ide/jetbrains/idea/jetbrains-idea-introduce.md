---
title: '宇宙最强Java编辑器'
cover: "/img/lynk/97.jpg"
date:       2019-09-26
subtitle: 'IntelliJ IDEA 介绍'
tags:
	- ide
	- solution
	- idea
	
---

<div id="article_content" class="article_content clearfix">
                                    <link rel="stylesheet" href="https://csdnimg.cn/release/phoenix/template/css/ck_htmledit_views-3019150162.css">
                                        <link rel="stylesheet" href="https://csdnimg.cn/release/phoenix/template/css/ck_htmledit_views-3019150162.css">
                <div class="htmledit_views" id="content_views">
                                            <h1><a name="t0"></a><strong>前言：IntelliJ IDEA</strong></h1>

<p>如果说IntelliJ IDEA是一款现代化智能开发工具的话，Eclipse则称得上是<code>石器时代</code>的东西了。其实笔者也是一枚从Eclipse转IDEA的探索者，随着近期的不断开发实践和调试，逐步体会到这款智能IDE带来的巨大开发便利，在强大的插件功能支持下，诸如对Git和Maven的支持简直让人停不下来，各种代码提示，包括JS更是手到擒来，最终不得不被这款神奇的IDE所折服。为了让身边更多的小伙伴参与进来，决定写下这篇文章，与君共享。(*^_^*)</p>

<p>高级传送门：<a href="https://link.jianshu.com/?t=https%3A%2F%2Fwww.jetbrains.com%2Fidea%2Fdownload%2F%23section%3Dwindows" rel="nofollow" data-token="a10d260e3f5f408735a67237789d53d3">IntelliJ IDEA 官网下载 - Ultimate 终极版</a></p>

<p>激活方法： 安装完成后 选择License&nbsp; 输入 http://intellij.mandroid.cn</p>

<h1><a name="t1"></a><a name="t1"></a><strong>正文：IntelliJ IDEA 使用教程</strong></h1>

<h3><a name="t2"></a><a name="t2"></a><strong>1. IDEA VS Eclipse 核心术语比较</strong></h3>

<p><strong>&nbsp; &nbsp; 由下图可见：</strong>两者最大的转变就在于工作空间概念的转变，并且在IDEA当中，Project和&nbsp; Module是作为两个不同的概念，对项目结构是重要意义的，这也恰恰是许多IDEA初学者觉得困扰的地方。</p>

<p><img alt="" class="has" src="https://upload-images.jianshu.io/upload_images/8069210-1f60e92b9a8d5559.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/648"></p>

<h4><a name="t3"></a><a name="t3"></a>&nbsp; &nbsp; 1.1 为什么要取消工作空间？</h4>

<p>&nbsp; &nbsp; &nbsp; &nbsp; 答：&nbsp;<strong>简单来说，IDEA不需要设置工作空间，因为每一个Project都具备一个工作空间！！<u>对于每一个IDEA的项目工程（Project）而言，它的每一个子模块（Module）都可以使用独立的JDK和MAVEN</u></strong><u>。</u>这对于传统项目迈向新项目的重构添加了极大的便利性，这种多元化的灵活性正是Eclipse所缺失的，因为开始Eclipse在初次使用时已经绑死了工作空间。</p>

<p>&nbsp; &nbsp; 1.2 此外，很多新手都会问，为什么IDEA里面的子工程要称为Module ？</p>

<p>&nbsp; &nbsp; &nbsp; &nbsp; 答：其实就是模块化的概念，作为聚合工程亦或普通的根目录，它称之为Project，而下面的子工程称为模块，每一个子模块之间可以相关联，也可以没有任何关联。</p>

<h3><a name="t4"></a><a name="t4"></a><strong>2. 当前项目配置VS 默认配置&nbsp;&nbsp;</strong></h3>

<p>&nbsp; &nbsp; 2.1 为什么有了当前项目配置，还需要默认配置呢？</p>

<p><strong>&nbsp; &nbsp; 答：<u>因为IDEA没有工作空间的概念，所以每个新项目（Project）都需要设置自己的JDK和MAVEN等相关配置，</u></strong>这样虽然提高了灵活性，但是却要为每个新项目都要重新配置，这显然不符合我们的预期。在这个背景下，<u><strong>默认配置给予当前项目配置提供了Default选项</strong></u>，问题自然就迎刃而解了。</p>

<p>&nbsp; &nbsp; 2.2 初始化步骤</p>

<p>&nbsp; &nbsp; &nbsp; 打开默认配置：顶部导航栏 -&gt; File -&gt; Other Settings -&gt; Default Settings /ProjectStructs&nbsp;</p>

<p>&nbsp; &nbsp; &nbsp; 打开当前配置：顶部导航栏 -&gt; File -&gt; Settings / ProjectStructs</p>

<p><strong>&nbsp; &nbsp; &nbsp;示例图：</strong></p>

<p><img alt="" class="has" src="https://upload-images.jianshu.io/upload_images/8069210-ac73a71f4046699e.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/494"></p>

<p>如果当前项目想覆盖默认配置，直接在Settins/Project Structure设置即可。</p>

<blockquote>
<p>=============================================</p>

<p>接下来，来看看IDEA如何快速搭建Java开发环境！！</p>

<p>=============================================</p>
</blockquote>

<h3><a name="t5"></a><a name="t5"></a>3. 全局JDK（默认配置）</h3>

<p>&nbsp; 具体步骤：顶部工具栏&nbsp; File -&gt;Other Settins -&gt; Default Project Structure -&gt; SDKs -&gt; JDK</p>

<p>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; 示例： 根据下图步骤设置JDK目录，最后点击OK保存。</p>

<p><img alt="" class="has" src="https://upload-images.jianshu.io/upload_images/8069210-fa02a9132d9aaee2.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/683"></p>

<p>PS：同理，当前项目在Project Structure可为工程和各模块设置喜欢的JDK版本。</p>

<h3><a name="t6"></a><a name="t6"></a>4. 全局Maven（默认配置）</h3>

<p>具体步骤：顶部工具栏&nbsp; File -&gt;Other Settings -&gt; Default Settings -&gt; Build &amp; Tools -&gt; Maven</p>

<p>&nbsp; &nbsp; &nbsp; 示例： 理论上只要配置了Maven主目录即可，实际开发推荐采用User Settins file .</p>

<p><img alt="" class="has" src="https://upload-images.jianshu.io/upload_images/8069210-c847845f860324be.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/700"></p>

<p>PS:为了方便查阅,推荐在Settings配置好本地仓库. 例如D:\mvnrepository</p>

<h3><a name="t7"></a><a name="t7"></a>5. 版本控制Git/Svn （默认配置）</h3>

<p>具体步骤：顶部工具栏&nbsp; File -&gt;Other Settings -&gt; Default Settings -&gt; Version Control -&gt; Git</p>

<p>&nbsp; &nbsp; &nbsp; 示例： IDEA默认集成了对Git/Svn的支持&nbsp; 直接设置执行程序，右边Test提示成功即可。</p>

<p>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; 部分小伙伴反馈说无法找到svn.exe，解决方法：重装SVN，配置项重新选择command line client tools 即可。</p>

<p><img alt="" class="has" src="https://upload-images.jianshu.io/upload_images/8069210-9bbaa622cf3daeed.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/700"></p>

<p>PS: IDEA内置的Git插件灰常好用，尤其是解决冲突性的代码。另外Git客户端推荐SourceTree。</p>

<h3><a name="t8"></a><a name="t8"></a>6. 自动导包和智能移除 （默认配置）</h3>

<p>具体步骤：顶部工具栏&nbsp; File -&gt;Other Settings -&gt; Default Settings -&gt; Auto Import</p>

<p>&nbsp; &nbsp; &nbsp; 说明：&nbsp;<strong>在网上看到很多人在提问IDEA为什么不能优化导包而Eclipse可以，</strong></p>

<p><strong>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; 所以特意抽出来跟大家分享IDEA如何优化导包。</strong></p>

<p><img alt="" class="has" src="https://upload-images.jianshu.io/upload_images/8069210-d66b1318a29ab251.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/700"></p>

<h3><a name="t9"></a><a name="t9"></a>&nbsp; 7. Tomcat Server（当前项目配置）&nbsp;</h3>

<p>很多小伙伴刚开始都找不到Tomcat的配置，其实很简单，Tomcat或者Jetty这些都是部署的容器，自然会联想到Deployment ，打开部署配置，可以看到应用服务器的配置。</p>

<p>配置Tomcat方法： File -&gt; Settings -&gt; Deployment -&gt; Application Servers -&gt; Tomcat Server&nbsp;&nbsp;</p>

<p>具体配置方法，如下图：</p>

<p><img alt="" class="has" src="https://upload-images.jianshu.io/upload_images/8069210-4d628299a415e63d.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/700"></p>

<h2><a name="t10"></a><a name="t10"></a>IDEA 必备小技能&nbsp;</h2>

<p>为了提升开发效率，撸主贴心为大家准备以下实用指数五颗星的小技巧：</p>

<h3><a name="t11"></a><a name="t11"></a>8. 自动编译</h3>

<p>具体步骤：顶部工具栏&nbsp; File -&gt;Other Settings -&gt; Default Settings -&gt; Auto Import</p>

<p>说明：开启自动编译之后，结合Ctrl+Shift+F9 会有热更新效果。</p>

<p><img alt="" class="has" src="https://upload-images.jianshu.io/upload_images/8069210-e10620f9da31fe9c.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/700"></p>

<h4><a name="t12"></a><a name="t12"></a>自动编译（Runtime）</h4>

<p>具体步骤： 敲击 Ctrl + Shift + Alt + /&nbsp; 然后进入Registry ，找到compiler.automake.allow.when.app.running ，然后勾选上。</p>

<p><img alt="" class="has" src="https://upload-images.jianshu.io/upload_images/8069210-0734034dd7995cf4.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/371"></p>

<p><img alt="" class="has" src="https://upload-images.jianshu.io/upload_images/8069210-3a4d633c2c0496f5.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/700"></p>

<h3><a name="t13"></a><a name="t13"></a>9. 取消大小写敏感</h3>

<p>具体步骤：</p>

<p>File | Settings | Editor | General | Code Completion Case | Sensitive Completion = None</p>

<p>取消大小敏感，在编写代码的时候，代码的自动提示将更加全面和丰富。</p>

<p><img alt="" class="has" src="https://upload-images.jianshu.io/upload_images/8069210-60b6ee65a7b778a0.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/700"></p>

<h3><a name="t14"></a><a name="t14"></a>10. 调整字体类型和字体大小</h3>

<p>默认的白色背景和细小的字体会影响大家的编码体验，这里特意提供了调整代码窗的快捷配置。打开配置，搜索Font，然后再Font可以调整字体类型，Size可以调整字体大小</p>

<h3><a name="t15"></a><a name="t15"></a>10. 将快捷键设置为跟Eclipse一样</h3>

<p>很多人可能并不习惯IDEA的快捷键，为了方便，这里我们将快捷键设置为跟 Eclipse一样。</p>

<p>具体步骤: File -&gt; Settings -&gt; Keymap - &gt; 选择Eclipse .</p>

<p><img alt="" class="has" src="https://upload-images.jianshu.io/upload_images/8069210-de1b7cb998e21a2d.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/700"></p>

<p>从Eclipse转过来的小伙伴 可以放心使用</p>

<h3><a name="t16"></a><a name="t16"></a>11. 打开常用工具栏</h3>

<p>具体步骤：顶部导航栏 - View -&gt; 勾选 Toolbar &amp; Tool Buttons</p>

<p>如下图所示：</p>

<p><img alt="" class="has" src="https://upload-images.jianshu.io/upload_images/8069210-575c85658a9b06fd.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/534"></p>

<h3><a name="t17"></a><a name="t17"></a>12. 打开Maven神器（强烈推荐！）</h3>

<p>具体步骤：右侧直接点击 Maven Project 管理插件 ，记得先打开常用工具栏，详见8.3。</p>

<p>如下图所示： 还在Eclipse使用Update命令苦苦挣扎的童鞋，请火速尝试此款插件，能给你带来前所未有的愉快感！！</p>

<p><img alt="" class="has" src="https://upload-images.jianshu.io/upload_images/8069210-c6aca3ce3f7cb954.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/429"></p>

<h3><a name="t19"></a><a name="t19"></a>13. 懒人必备快捷键</h3>

<p>&nbsp;</p>

<p><strong>1. 按【鼠标中键】快速打开智能提示，取代alt+enter 。</strong></p>

<p>File-&gt;Settings-&gt; Keymap-&gt; 搜索 Show Intention Actions -&gt; 添加快捷键为鼠标中键。</p>

<p><strong>2. 按【F2】快速修改文件名，告别双手操作。</strong></p>

<p>File-&gt;Settings-&gt; Keymap-&gt; 搜索 Rename -&gt; 将快捷键设置为F2 。</p>

<p><strong>3. 按【F3】直接打开文件所在目录，浏览一步到位。</strong></p>

<p>File-&gt;Settings-&gt; Keymap-&gt; 搜索 Show In Explorer -&gt; 将快捷键设置为F3 。</p>

<p><strong>4. 按【Ctrl+右键】直接打开实现类，方便开发查询。</strong></p>

<p>File-&gt;Settings-&gt; Keymap-&gt; 搜索 implementation-&gt;&nbsp; Add Mouse Shortcut 将快捷键设置为Ctrl+ 鼠标右键。</p>

<p>&nbsp;</p>

<h3><a name="t20"></a><a name="t20"></a><strong>14. 重度强迫症患者</strong></h3>

<p><strong>1.取消大小写敏感，让自动完成更齐全！&nbsp;&nbsp;</strong></p>

<p>File | Settings | Editor | General | Code Completion Case | Sensitive Completion = None。</p>

<p><strong>2.自动隐藏注释，让源码阅读更为清爽！&nbsp;</strong></p>

<p>File -&gt; Settings -&gt; Editor -&gt; General -&gt; Code Folding -&gt;&nbsp; Documentation comments 勾选。</p>

<p>如何想快速一键打开全部注释，则单击鼠标右键，选择Folding -&gt; Expand Doc comments 。</p>

<p><strong>3. Maven自动下载源码包，告别反编译，直接上源码注释！！</strong></p>

<p>File | Settings | Build, Execution, Deployment | Build Tools | Maven | Importing</p>

<p>将Automatically Download&nbsp; 的 Source 勾上。</p>

<p>&nbsp;</p>

<h3><a name="t21"></a><a name="t21"></a>15. IDEA十问十答</h3>

<p>&nbsp; &nbsp;&nbsp;<strong>（1）如何打开本地工程/已存在的工程？</strong></p>

<p>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;答：点击File -&gt; Open 打开 工程文件夹即可，注意先配置好JDK、Maven等基础配置。</p>

<p><strong>&nbsp; &nbsp;（2）IDEA如何删除项目工程？</strong></p>

<p>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; 答：问这个问题的Coder真的好可爱啊哈哈，很肯定的回答你，不需要删，</p>

<p>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; 点击File-&gt; Close Project 即可快速关闭当前项目； 示例：</p>

<p>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;什么？你还是想要干掉整个目录？那也阔以，右键Show In Explorer ，删掉文件夹&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;即可。不过笔者建议还是直接Close关掉就好啦，万一以后用得上呢，你说呢？</p>

<p><img alt="" class="has" src="https://upload-images.jianshu.io/upload_images/8069210-8fa3622b2e764134.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/274"></p>

<p><strong>&nbsp; &nbsp;（3）如何在单个窗口打开多个Maven工程啊？</strong></p>

<p>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; 答：随便新建一个文件夹，然后将工程都扔进去，使用IDEA打开这个文件夹。</p>

<p><strong>&nbsp; &nbsp;（4）如何为当前项目工程添加多个模块啊？</strong></p>

<p>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;答： 对着工程右键 -&gt; 选择New -&gt; Module -&gt; 通常选择Spring Initializr&nbsp; ，如图：</p>

<p><img alt="" class="has" src="https://upload-images.jianshu.io/upload_images/8069210-64822a874d368f32.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/563"></p>

<p>新增模块</p>

<p><img alt="" class="has" src="https://upload-images.jianshu.io/upload_images/8069210-b1aa086b58e093c5.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/304"></p>

<p>多模块工程</p>                                    </div>
                    </div>