---
title: "mysql修改密码方法"
date:       2019-10-09
tags:
	- database
	- mysql
	- solution
---

<div class="content-intro view-box "><p>在windows系统中，<a href="https://www.w3cschool.cn/mysql/" target="_blank">mysql</a>修改密码的方法还是比较多的。本文就为大家介绍四种MySQL修改root密码的方法。</p><p><br></p><p><b>方法一：用SET&nbsp;PASSWORD命令修改
</b></p><p>首先登陆mysql，一般命令格式为：mysql&gt;&nbsp;set&nbsp;password&nbsp;for&nbsp;用户名@localhost&nbsp;=&nbsp;password('新密码');&nbsp;
</p><p>例子：
</p><pre lang="sql" style="max-width: 100%;"><code class="sql hljs">mysql&gt; <span class="hljs-keyword">set</span> <span class="hljs-keyword">password</span> <span class="hljs-keyword">for</span> root@localhost = <span class="hljs-keyword">password</span>(<span class="hljs-string">'123'</span>); </code></pre><p><br></p><p><b>方法二：用mysqladmin修改
</b></p><p>格式：mysqladmin&nbsp;-u用户名&nbsp;-p旧密码&nbsp;password&nbsp;新密码&nbsp;
</p><p>例子：
</p><pre lang="sql" style="max-width: 100%;"><code class="sql hljs">mysqladmin -uroot -p123456 password 123 </code></pre><p>这个命令就是讲uroot这个用户的密码由p123456改成了123
</p><p><br></p><p><b>方法三：用UPDATE直接编辑user表&nbsp;
</b></p><p>首先登陆mysql
</p><pre lang="sql" style="max-width: 100%;"><code class="sql hljs">mysql&gt; <span class="hljs-keyword">use</span> mysql; 
mysql&gt; <span class="hljs-keyword">update</span> <span class="hljs-keyword">user</span> <span class="hljs-keyword">set</span> <span class="hljs-keyword">password</span>=<span class="hljs-keyword">password</span>(<span class="hljs-string">'123'</span>) <span class="hljs-keyword">where</span> <span class="hljs-keyword">user</span>=<span class="hljs-string">'root'</span> <span class="hljs-keyword">and</span> host=<span class="hljs-string">'localhost'</span>; 
mysql&gt; <span class="hljs-keyword">flush</span> <span class="hljs-keyword">privileges</span>; </code></pre><p>以上的代码是将root的密码更改为123
</p><p><br></p><p>以上三种方法都是在记得旧密码的情况下，如果用户忘记了密码，那么该怎么办呢？
</p><p><br></p><p><b>方法四：忘记旧密码的修改方法
</b></p><p>1.&nbsp;关闭正在运行的MySQL服务。&nbsp;
</p><p>2.&nbsp;打开DOS窗口，转到mysql\bin目录。&nbsp;
</p><p>3.&nbsp;输入mysqld--skip-grant-tables回车。--skip-grant-tables这个指令是让用户再次启动MySQL服务的时候，可以直接跳过权限表认证。&nbsp;
</p><p>4.&nbsp;再开一个DOS窗口（因为刚才那个DOS窗口已经不能动了），然后转到mysql\bin目录。&nbsp;
</p><p>5.&nbsp;输入mysql回车，如果成功，将出现MySQL提示符&nbsp;&gt;。&nbsp;
</p><p>6.&nbsp;连接权限数据库：&nbsp;use&nbsp;mysql;&nbsp;。&nbsp;
</p><p>6.&nbsp;改密码：update&nbsp;user&nbsp;set&nbsp;password=password("123")&nbsp;where&nbsp;user="root";（别忘了最后加分号）&nbsp;。&nbsp;
</p><p>7.&nbsp;刷新权限（必须步骤）：flush&nbsp;privileges;　。&nbsp;
</p><p>8.&nbsp;退出&nbsp;quit。&nbsp;
</p><p>9.&nbsp;注销系统，再进入，使用用户名root和刚才设置的新密码123登录。&nbsp;
</p></div>