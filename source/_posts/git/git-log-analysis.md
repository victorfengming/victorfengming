---
title: "git log解析"
cover: "/img/lynk/96.jpg"
date:       2019-09-06
subtitle: "打log随心所欲！"
tags:
	- Git
	- solution
---

<div id="cnblogs_post_body" class="blogpost-body ">
    <p><!--?xml version="1.0" encoding="UTF-8" standalone="no"?--></p>
<div>git log命令非常强大而好用，在复杂系统的版本管理中扮演着重要的角色，但默认的git log命令显示出的东西实在太丑，不好好打扮一下根本没法见人，打扮好了用alias命令拍个照片，就正式出道了！</div>
<div>&nbsp;</div>
<div>下面先详细而系统地介绍git log的所有配置知识（用我一向简洁清晰的表述方式），熟悉了这些东西，你就可以自由配置自己美丽的git log了～</div>
<div>最后上个干货，直接给一个我打扮好的alias配置，懒人直接跳到最后吧 ！</div>
<div>&nbsp;</div>
<div>（转载请注明：博客园-阁刚广志，地址：http://www.cnblogs.com/bellkosmos/p/5923439.html&nbsp;）</div>
<div>&nbsp;</div>
<div><!--?xml version="1.0" encoding="UTF-8" standalone="no"?-->
<div>git log用于查询版本的历史，命令形式如下：</div>
<div>
<div class="cnblogs_code">
<pre>git log [&lt;options&gt;] [&lt;since&gt;..&lt;until&gt;] [[--] &lt;path&gt;...]</pre>
</div>
<p>&nbsp;</p>
</div>
<div>这条命令有很多参数选项</div>
<div>一、不带参数</div>
<ol>
<li>如果不带任何参数，它会列出所有历史记录，最近的排在最上方，显示提交对象的哈希值，作者、提交日期、和提交说明</li>
<li>如果记录过多，则按Page Up、Page Down、↓、↑来控制显示</li>
<li>按q退出历史记录列表</li>
</ol>
<div>&nbsp;</div>
<div>二、显示参数</div>
<ol>
<li>-p：按补丁显示每个更新间的差异，比下一条- -stat命令信息更全</li>
<li>--stat：显示每次更新的修改文件的统计信息，每个提交都列出了修改过的文件，以及其中添加和移除的行数，并在最后列出所有增减行数小计</li>
<li>--shortstat：只显示--stat中最后的行数添加修改删除统计</li>
<li>--name-only：尽在已修改的提交信息后显示文件清单</li>
<li>--name-status：显示新增、修改和删除的文件清单</li>
<li>--abbrev-commit：仅显示SHA-1的前几个字符，而非所有的40个字符</li>
<li>--relative-date：使用较短的相对时间显示（例如："two weeks ago"）</li>
<li>--graph：显示ASCII图形表示的分支合并历史</li>
<li>—pretty＝：使用其他格式显示历史提交信息，可选项有：oneline,short,medium,full,fuller,email,raw以及format:&lt;string&gt;,默认为medium，如：<ol>
<li><strong>--pretty=oneline：</strong>一行显示，只显示哈希值和提交说明（--online本身也可以作为单独的属性）</li>
<li><strong>--pretty=format:” "：</strong>控制显示的记录格式，如：<ol>
<li>%H&nbsp; 提交对象（commit）的完整哈希字串</li>
<li>%h&nbsp; 提交对象的简短哈希字串</li>
<li>%T&nbsp; 树对象（tree）的完整哈希字串</li>
<li>%t&nbsp; 树对象的简短哈希字串</li>
<li>%P&nbsp; 父对象（parent）的完整哈希字串</li>
<li>%p&nbsp; 父对象的简短哈希字串</li>
<li>%an 作者（author）的名字</li>
<li>%ae 作者的电子邮件地址</li>
<li>%ad 作者修订日期（可以用 -date= 选项定制格式）</li>
<li>%ar 作者修订日期，按多久以前的方式显示</li>
<li>%cn 提交者(committer)的名字<ol>
<li>作者和提交者的区别不知道是啥？</li>
<li>作者与提交者的关系：作者是程序的修改者，提交者是代码提交人（自己的修改不提交是怎么能让别人拉下来再提交的？）</li>
<li>其实作者指的是实际作出修改的人，提交者指的是最后将此工作成果提交到仓库的人。所以，当你为某个项目发布补丁，然后某个核心成员将你的补丁并入项目时，你就是作者，而那个核心成员就是提交者（soga）</li>
</ol></li>
<li>%ce 提交者的电子邮件地址</li>
<li>%cd 提交日期（可以用 -date= 选项定制格式）</li>
<li>%cr 提交日期，按多久以前的方式显示</li>
<li>%s&nbsp; 提交说明</li>
</ol></li>
<li>带颜色的<strong>--pretty=format:” "</strong>，这个另外写出来分析<ol>
<li>以这句为例：%Cred%h%Creset -%C(yellow)%d%Cblue %s %Cgreen(%cd) %C(bold blue)&lt;%an&gt;</li>
<li>它的效果是：<!--?xml version="1.0" encoding="UTF-8" standalone="no"?-->&nbsp;<!--?xml version="1.0" encoding="UTF-8" standalone="no"?-->&nbsp;<!--?xml version="1.0" encoding="UTF-8" standalone="no"?-->&nbsp;<img src="https://images2015.cnblogs.com/blog/748759/201609/748759-20160930121017813-427458411.png" alt="">
<p>&nbsp;</p>
</li>
<li>先断句：［%Cred%h］［%Creset &nbsp; -］［%C(yellow)%d ］［%Cblue%s］［%Cgreen(%cd)］［%C(bold blue)&lt;%an&gt;］</li>
<li>然后就是很明显能得到的规律了<ol>
<li>一个颜色＋一个内容</li>
<li>颜色以％C开头，后边接几种颜色，还可以设置字体，如果要设置字体的话，要一块加个括号<ol>
<li>能设置的颜色值包括：reset（默认的灰色），normal, black, red, green, yellow, blue, magenta, cyan, white.</li>
<li>字体属性则有bold, dim, ul, blink, reverse. &nbsp;</li>
</ol></li>
<li>内容可以是占位元字符，也可以是直接显示的普通字符</li>
</ol></li>
</ol></li>
</ol></li>
<li>--date= (relative|local|default|iso|rfc|short|raw)：定制后边如果出现%ad或%cd时的日期格式<ol>
<li>有几个默认选项<ol>
<li>--date=relative：shows dates relative to the current time, e.g. "2 hours ago".</li>
<li>--date=local：shows timestamps in user’s local timezone.</li>
<li>--date=iso (or --date=iso8601)：shows timestamps in ISO 8601 format.</li>
<li>--date=rfc (or --date=rfc2822)：shows timestamps in RFC 2822 format,often found in E-mail messages.</li>
<li>--date=short：shows only date but not time, in YYYY-MM-DD format.这个挺好用</li>
<li>--date=raw：shows the date in the internal raw git format %s %z format.</li>
<li>--date=default：shows timestamps in the original timezone&nbsp;(either committer’s or author’s).</li>
</ol></li>
<li>也可以自定义格式（需要git版本2.6.0以上），比如--date=format:'%Y-%m-%d %H:%M:%S' 会格式化成：2016-01-13 11:32:13，其他的格式化占位符如下：<ol>
<li>%a：Abbreviated weekday name</li>
<li>%A：Full weekday name</li>
<li>%b：Abbreviated month name</li>
<li>%B：Full month name</li>
<li>%c：Date and time representation appropriate for locale</li>
<li>%d：Day of month as decimal number (01 – 31)</li>
<li>%H： Hour in 24-hour format (00 – 23)</li>
<li>%I：Hour in 12-hour format (01 – 12)</li>
<li>%j：Day of year as decimal number (001 – 366)</li>
<li>%m：Month as decimal number (01 – 12)</li>
<li>%M：Minute as decimal number (00 – 59)</li>
<li>%p：Current locale's A.M./P.M. indicator for 12-hour clock</li>
<li>%S：Second as decimal number (00 – 59)</li>
<li>%U：Week of year as decimal number, with Sunday as first day of week (00 – 53)</li>
<li>%w：Weekday as decimal number (0 – 6; Sunday is 0)</li>
<li>%W：Week of year as decimal number, with Monday as first day of week (00 – 53)</li>
<li>%x：Date representation for current locale</li>
<li>%X：Time representation for current locale</li>
<li>%y：Year without century, as decimal number (00 – 99)</li>
<li>%Y：Year with century, as decimal number</li>
<li>%z, %Z：Either the time-zone name or time zone abbreviation, depending on registry settings; no characters if time zone is unknown</li>
<li>%%：Percent sign</li>
</ol></li>
</ol></li>
</ol>
<div>&nbsp;</div>
<div>三、筛选参数：</div>
<ol>
<li>按数量<ol>
<li>-n：显示前n条log</li>
</ol></li>
<li>按日期<ol>
<li>--after=<ol>
<li>比如git log --after="2014-7-1”，显示2014年7月1号之后的commit(包含7月1号)</li>
<li>后边的日期还可以用相对时间表示，比如"1 week ago"和”yesterday"，比如git log --after="yesterday"</li>
<li>这里的格式可以是什么？</li>
</ol></li>
<li>--before=<ol>
<li>同上</li>
<li>另外这两条命令可以同时使用表示时间段，比如git log --after="2014-7-1" --before="2014-7-4"</li>
<li>另外--since --until和 --after --before是一个意思，都可以用</li>
</ol></li>
</ol></li>
<li>按作者<ol>
<li>--author=<ol>
<li>比如git log --author=“John"，显示John贡献的commit</li>
<li>注意：作者名不需要精确匹配，只需要包含就行了</li>
<li>而且：可以使用正则表达式，比如git log --author="John\|Mary”，搜索Marry和John贡献的commit</li>
<li>而且：这个--author不仅包含名还包含email, 所以你可以用这个搜索email</li>
</ol></li>
</ol></li>
<li>按commit描述<ol>
<li>--grep=<ol>
<li>比如：git log --grep="JRA-224"</li>
<li>而且：可以传入-i用来忽略大小写</li>
<li>注意：如果想同时使用--grep和--author，必须在附加一个--all-match参数</li>
</ol></li>
</ol></li>
<li>按文件<ol>
<li>- -（空格）或［没有］<ol>
<li>有时你可能只对某个文件的修改感兴趣, 你只想查看跟某个文件相关的历史信息, 你只需要插入你感兴趣文件的路径［对，是路径，所以经常是不太好用］就可以了</li>
<li>比如：git log -- foo.py bar.py ，只返回和foo.py或bar.py相关的commit</li>
<li>这里的--是告诉Git后面的参数是文件路径而不是branch的名字. 如果后面的文件路径不会和某个branch产生混淆, 你可以省略- -，比如git log foo.py&nbsp;</li>
<li>另外，后边的路径还支持正则，比如：git log&nbsp; *install.md 是，指定项目路径下的所有以install.md结尾的文件的提交历史</li>
<li>另外，文件名应该放到参数的最后位置，通常在前面加上--并用空格隔开表示是文件</li>
<li>另外，git log file/ 查看file文件夹下所有文件的提交记录</li>
</ol></li>
</ol></li>
<li>按分支<ol>
<li>- -<ol>
<li>--branchName branchName为任意一个分支名字，查看某个分支上的提交记录</li>
<li>需要放到参数中的最后位置处</li>
<li>如果分支名与文件名相同，系统会提示错 误，可通过--选项来指定给定的参数是分支名还是文件名<ol>
<li>比如：在当前分支中有一个名为v1的文件，同时还存在一个名为v1的分支</li>
<li>git log v1 -- 此时的v1代表的是分支名字（－－后边是空的）</li>
<li>git log -- v1 此时的v1代表的是名为v1的文件</li>
<li>git log v1 －－ v1 代表v1分支下的v1文件</li>
</ol></li>
</ol></li>
</ol></li>
<li>按内容<ol>
<li>-S"&lt;string&gt;"、-G"&lt;string&gt;"<ol>
<li>有时你想搜索和新增或删除某行代码相关的commit. 可以使用这条命令</li>
<li>假设你想知道Hello, World!这句话是什么时候加入到项目里去的，可以用：git log -S"Hello,World!"</li>
<li>另外：如果你想使用正则表达式去匹配而不是字符串, 那么你可以使用-G代替-S.</li>
<li>这是一个非常有用的debug工具, 使用他你可以定位所有跟某行代码相关的commit. 甚至可以查看某行是什么时候被copy的, 什么时候移到另外一个文件中去的</li>
<li>注：-S后没有"="，与查询内容之间也没有空格符</li>
</ol></li>
</ol></li>
<li>按范围<ol>
<li>git log &lt;since&gt;..&lt;until&gt;<ol>
<li>这个命令可以查看某个范围的commit</li>
<li>这个命令非常有用当你使用branch做为range参数的时候. 能很方便的显示2个branch之间的不同</li>
<li>比如：git log master..feature，master..feature这个range包含了在feature有而在master没有的所有commit，同样，如果是feature..master包含所有master有但是feature没有的commit</li>
<li>另外，如果是三个点，表示或的意思：git log master...test 查询master或test分支中的提交记录</li>
</ol></li>
</ol></li>
<li>过滤掉merge commit<ol>
<li>--no-merges<ol>
<li>默认情况下git log会输出merge commit.&nbsp; 你可以通过--no-merges标记来过滤掉merge commit，git log --no-merges</li>
<li>另外，如果你只对merge commit感兴趣可以使用—merges，git log --merges</li>
</ol></li>
</ol></li>
<li>按标签tag<ol>
<li>git log v1.0<ol>
<li>直接这样是查询标签之前的commit</li>
<li>加两个点git log v1.0.. 查询从v1.0以后的提交历史记录(不包含v1.0)</li>
</ol></li>
</ol></li>
<li>按commit<ol>
<li>git log commit ：查询commit之前的记录，包含commit</li>
<li>git log commit1 commit2：查询commit1与commit2之间的记录，包括commit1和commit2</li>
<li>git log commit1..commit2：同上，但是不包括commit1<ol>
<li>其中，commit可以是提交哈希值的简写模式，也可以使用HEAD代替<ol>
<li>HEAD代表最后一次提交，HEAD^为最后一个提交的父提交，等同于HEAD～1</li>
<li>HEAD～2代表倒数第二次提交</li>
</ol></li>
</ol></li>
</ol></li>
</ol>
<div>&nbsp;</div>
</div>
<div>最后干货，你会喜欢的~</div>
<div>下面第一条的效果是这样：</div>
<div><img src="https://images2015.cnblogs.com/blog/748759/201702/748759-20170221115250304-122758740.png" alt="">
<p>&nbsp;</p>
</div>
<div>
<div class="cnblogs_code"><div class="cnblogs_code_toolbar"><span class="cnblogs_code_copy"><a href="javascript:void(0);" onclick="copyCnblogsCode(this)" title="复制代码"><img src="//common.cnblogs.com/img/copycode.gif" alt="复制代码"></a></span></div>
<pre>git config --global alias.lm  "log --no-merges --color --date=format:'%Y-%m-%d %H:%M:%S' --author='你的名字！自己修改！' --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Cblue %s %Cgreen(%cd) %C(bold blue)&lt;%an&gt;%Creset' --abbrev-commit"<br><br><span style="color: #000000;">
git config </span>--global alias.lms  "log --no-merges --color --stat --date=format:'%Y-%m-%d %H:%M:%S' --author='你的名字！自己修改！' --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Cblue %s %Cgreen(%cd) %C(bold blue)&lt;%an&gt;%Creset' --abbrev-commit"<br><br><span style="color: #000000;">
git config </span>--global alias.ls "log --no-merges --color --graph --date=format:'%Y-%m-%d %H:%M:%S' --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Cblue %s %Cgreen(%cd) %C(bold blue)&lt;%an&gt;%Creset' --abbrev-commit"<br><br><span style="color: #000000;">
git config </span>--global alias.lss "log --no-merges --color --stat --graph --date=format:'%Y-%m-%d %H:%M:%S' --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Cblue %s %Cgreen(%cd) %C(bold blue)&lt;%an&gt;%Creset' --abbrev-commit"</pre>
<div class="cnblogs_code_toolbar"><span class="cnblogs_code_copy"><a href="javascript:void(0);" onclick="copyCnblogsCode(this)" title="复制代码"><img src="//common.cnblogs.com/img/copycode.gif" alt="复制代码"></a></span></div></div>
<p>&nbsp;</p>
</div>
<div>参考资料：</div>
<div><!--?xml version="1.0" encoding="UTF-8" standalone="no"?-->
<div><a href="http://www.cnblogs.com/irocker/p/advanced-git-log.html">http://www.cnblogs.com/irocker/p/advanced-git-log.html</a></div>
<div><a href="http://stackoverflow.com/questions/7853332/git-log-date-formats">http://stackoverflow.com/questions/7853332/git-log-date-formats</a></div>
<div><a href="https://git-scm.com/docs/git-log">https://git-scm.com/docs/git-log</a></div>
</div>
<div>&nbsp;</div>
<div>&nbsp;</div>
</div>



