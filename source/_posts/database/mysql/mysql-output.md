---
title: "MySQL 数据库导出导入操作"
cover: "/img/lynk/96.jpg"
date:       2020-01-14
subtitle: "让你的数据不再丢失"
tags:
	- basis
	- mysql
	- database
---

<div id="content_views" class="markdown_views">
    <!-- flowchart 箭头图标 勿删 -->
    <svg xmlns="http://www.w3.org/2000/svg" style="display: none;">
        <path stroke-linecap="round" d="M5,0 0,2.5 5,5z" id="raphael-marker-block"
              style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);"></path>
    </svg>
    <p>有时需要将 MySQL 数据库中的数据导入到其它的数据库中，这里以从 Ubuntu 系统的 MySQL 数据库导出 zabbix 这个数据库到 Windows 系统中的MySQL 为例。</p>

    <h2 id="导出数据库"><a name="t0"></a><a name="t0"></a>导出数据库</h2>

    <p>导出数据其实非常方便，比如将 MySQL 中的 zabbix 这个数据库导出到当前文件夹，首先切换到 root 用户，然后再切换到 Document
        这个目录，这样就可以直接将数据库导出到这个目录了，当然，指定特定目录也是可以的，接着执行</p>


    <pre class="prettyprint" name="code"><code class="hljs lasso has-numbering" onclick="mdcp.copyCode(event)"
                                               style="position: unset;">mysqldump <span
            class="hljs-attribute">-uroot</span> <span class="hljs-attribute">-ppassword</span> zabbix<span
            class="hljs-subst">&gt;</span>zabbix<span class="hljs-built_in">.</span>sql<div class="hljs-button {2}"
                                                                                            data-title="复制"></div></code><ul
            class="pre-numbering" style=""><li style="color: rgb(153, 153, 153);">1</li></ul></pre>

    <p><code>-p</code>后是自己 MySQL 数据库密码，如果<code>&gt;</code>后不指定目录，则导出到当前文件夹内。</p>


    <h2 id="导入数据库"><a name="t1"></a><a name="t1"></a>导入数据库</h2>

    <p>导入到 windows 系统数据库也很简单，可以使用客户端导入，这里使用命令行的形式导入，首先使用 <code>WIN + R</code>快捷键调出“运行”窗口，然后输入<code>cmd</code>打开命令行终端，依次执行如下命令
    </p>

    <ul>
        <li>登陆数据库</li>
    </ul>

    <pre class="prettyprint" name="code"><code class="hljs lasso has-numbering" onclick="mdcp.copyCode(event)"
                                               style="position: unset;"><span class="hljs-subst">&gt;</span>mysql <span
            class="hljs-attribute">-uroot</span> <span class="hljs-attribute">-ppassword</span><div
            class="hljs-button {2}" data-title="复制"></div></code><ul class="pre-numbering" style=""><li
            style="color: rgb(153, 153, 153);">1</li></ul></pre>

    <ul>
        <li>创建数据库</li>
    </ul>


    <pre class="prettyprint" name="code"><code class="hljs oxygene has-numbering" onclick="mdcp.copyCode(event)"
                                               style="position: unset;">&gt;<span class="hljs-keyword">CREATE</span> DATABASE zabbix;<div
            class="hljs-button {2}" data-title="复制"></div></code><ul class="pre-numbering" style=""><li
            style="color: rgb(153, 153, 153);">1</li></ul></pre>

    <ul>
        <li>导入数据</li>
    </ul>


    <pre class="prettyprint" name="code"><code class="hljs tex has-numbering" onclick="mdcp.copyCode(event)"
                                               style="position: unset;">&gt;use zabbix;
&gt;set names utf8;
&gt;source <span class="hljs-command">\Users</span><span class="hljs-command">\Erik</span><span class="hljs-command">\Desktop</span><span
                class="hljs-command">\zabbix</span>.sql<div class="hljs-button {2}" data-title="复制"></div></code><ul
            class="pre-numbering" style=""><li style="color: rgb(153, 153, 153);">1</li><li
            style="color: rgb(153, 153, 153);">2</li><li style="color: rgb(153, 153, 153);">3</li></ul></pre>

    <p>这里<code>\Users\Erik\Desktop\</code>是<code>zabbix.sql</code>的存放路径。</p>

    <p>这样就将数据导入到 Windows 系统的 MySQL 数据库中了。</p>

    <h2 id="参考资料"><a name="t2"></a><a name="t2"></a>参考资料</h2>

    <p>Mysql导入导出数据库以及数据表：<a href="https://my.oschina.net/linuxphp/blog/693650" rel="nofollow">https://my.oschina.net/linuxphp/blog/693650</a>
    </p></div>