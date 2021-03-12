---
title: '宇宙最强编辑器系列:Jetbrains介绍'
date:       2019-09-26
tags:
	- ide
	- solution
	
---

<div class="markdown-body">
            <!-- 欢迎成为极客学院WIKI作者 -->
                        <!-- 授权极客学院转载 -->
                <p class="author"><a href="https://github.com/judasn" class="reprint-name right-top-img" data-name="点击授权商" target="_blank">Judas.n</a> · 更新于 2018-11-28 11:00:42</p>
                        <!-- 内容 -->
            <h1>介绍</h1>
<h2 id="d58a3ddd14ef6536f4a5e42603ae05db">本系列教程介绍</h2>
<p>本系列教程从 IntelliJ IDEA 的安装、卸载、软件设置、项目配置等各个方面进行讲解。通过本系列教程的学习，也希望你能爱上 IntelliJ IDEA，爱上它的体贴。同时学完本系列教程对于你学习 JetBrains 公司下的其他产品也有好处，其他产品包括：</p>
<blockquote>
<ul>
<li><a rel="nofollow" href="http://www.jetbrains.com/phpstorm/"  title="PhpStorm 主要用于开发 PHP">PhpStorm</a> 主要用于开发 PHP</li>
<li><a rel="nofollow" href="http://www.jetbrains.com/ruby/"  title="RubyMine 主要用于开发 Ruby">RubyMine</a> 主要用于开发 Ruby</li>
<li><a rel="nofollow" href="http://www.jetbrains.com/pycharm/"  title="PyCharm 主要用于开发 Python">PyCharm</a> 主要用于开发 Python</li>
<li><a rel="nofollow" href="http://www.jetbrains.com/objc/"  title="AppCode 主要用于开发 Objective-C">AppCode</a> 主要用于开发 Objective-C / Swift</li>
<li><a rel="nofollow" href="http://www.jetbrains.com/clion/"  title="CLion 主要用于开发 C/C++">CLion</a> 主要用于开发 C / C++</li>
<li><a rel="nofollow" href="http://www.jetbrains.com/webstorm/"  title="WebStorm 主要用于开发 JavaScript 等前端技术">WebStorm</a> 主要用于开发 JavaScript、HTML5、CSS3 等前端技术</li>
<li><a rel="nofollow" href="http://www.jetbrains.com/dbe/"  title="DataGrip 主要用于开发 SQL">DataGrip</a> 主要用于开发 SQL</li>
<li><a rel="nofollow" href="http://developer.android.com/tools/studio/"  title="Android Studio 主要用于开发 Android">Android Studio</a> 主要用于开发 Android（Google 基于 IntelliJ IDEA 社区版进行迭代所以也姑且算上）</li>
</ul>
</blockquote>
<h2 id="9f5872dbd7bc043f919cbcd1ba189103">IntelliJ IDEA 介绍</h2>
<blockquote>
<ul>
<li>IntelliJ IDEA 官网：<a rel="nofollow" href="https://www.jetbrains.com/idea/" >https://www.jetbrains.com/idea/</a></li>
</ul>
</blockquote>
<p>IntelliJ IDEA 在 2015 年 06 月官网主页是这样介绍自己的：</p>
<blockquote>
<p>Excel at enterprise, mobile and web development with Java, Scala and Groovy, with all the latest modern technologies and frameworks available out of the box.</p>
</blockquote>
<p>简明翻译：IntelliJ IDEA 主要用于支持 Java、Scala、Groovy 等语言的开发工具，同时具备支持目前主流的技术和框架，擅长于企业应用、移动应用和 Web 应用的开发。</p>
<p>IntelliJ IDEA 对自己的定义是很清晰的，对于新人来讲可能还不太理解，可能还会有误会，认为它博而不精，但是对于老用户来讲应该是非常认可上面这句话的。通过下面功能表格，新人对于 IntelliJ IDEA 所具备的功能会有一个新的认识。</p>
<p>如果用一句话来形容 IntelliJ IDEA，我会说：<strong>IntelliJ IDEA 是目前所有 IDE 中最具备沉浸式的 JVM IDE，没有之一</strong>。 </p>
<h2 id="d1a66d0e4565515013c548a757c046d3">IntelliJ IDEA 主要功能介绍</h2>
<blockquote>
<ul>
<li>语言支持上：</li>
</ul>
</blockquote>
<table>
<thead>
<tr>
<th style="text-align: left;">安装插件后支持</th>
<th style="text-align: left;">SQL类</th>
<th style="text-align: left;">基本JVM</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;">PHP</td>
<td style="text-align: left;">PostgreSQL</td>
<td style="text-align: left;">Java</td>
</tr>
<tr>
<td style="text-align: left;">Python</td>
<td style="text-align: left;">MySQL</td>
<td style="text-align: left;">Groovy</td>
</tr>
<tr>
<td style="text-align: left;">Ruby</td>
<td style="text-align: left;">Oracle</td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">Scala</td>
<td style="text-align: left;">SQL Server</td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">Kotlin</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">Clojure</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
</tbody>
</table>
<blockquote>
<ul>
<li>其他支持：</li>
</ul>
</blockquote>
<table>
<thead>
<tr>
<th style="text-align: left;">支持的框架</th>
<th style="text-align: left;">额外支持的语言代码提示</th>
<th style="text-align: left;">支持的容器</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;">Spring MVC</td>
<td style="text-align: left;">HTML5</td>
<td style="text-align: left;">Tomcat</td>
</tr>
<tr>
<td style="text-align: left;">GWT</td>
<td style="text-align: left;">CSS3</td>
<td style="text-align: left;">TomEE</td>
</tr>
<tr>
<td style="text-align: left;">Vaadin</td>
<td style="text-align: left;">SASS</td>
<td style="text-align: left;">WebLogic</td>
</tr>
<tr>
<td style="text-align: left;">Play</td>
<td style="text-align: left;">LESS</td>
<td style="text-align: left;">JBoss</td>
</tr>
<tr>
<td style="text-align: left;">Grails</td>
<td style="text-align: left;">JavaScript</td>
<td style="text-align: left;">Jetty</td>
</tr>
<tr>
<td style="text-align: left;">Web Services</td>
<td style="text-align: left;">CoffeeScript</td>
<td style="text-align: left;">WebSphere</td>
</tr>
<tr>
<td style="text-align: left;">JSF</td>
<td style="text-align: left;">Node.js</td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">Struts</td>
<td style="text-align: left;">ActionScript</td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">Hibernate</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">Flex</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
</tbody>
</table>
<p>上面特性只是 IntelliJ IDEA 的冰山一角，而且这个还不是 IntelliJ IDEA 最重要的地方，IntelliJ IDEA 最重要的特性就是人性化、智能，后面学习你会慢慢接触到。</p>
<h2 id="31366c9276e6126c25c0490d9cfef87f">更多官方学习信息</h2>
<blockquote>
<ul>
<li>IntelliJ IDEA 主要特性介绍 1：<a rel="nofollow" href="https://www.jetbrains.com/idea/features/" >https://www.jetbrains.com/idea/features/</a></li>
<li>IntelliJ IDEA 主要特性介绍 2：<a rel="nofollow" href="https://www.jetbrains.com/idea/features/editions_comparison_matrix.html" >https://www.jetbrains.com/idea/features/editions_comparison_matrix.html</a></li>
<li>官方快速入门：<a rel="nofollow" href="http://confluence.jetbrains.com/display/IntelliJIDEA/Quick+Start" >http://confluence.jetbrains.com/display/IntelliJIDEA/Quick+Start</a></li>
<li>官方在线帮助文档：<a rel="nofollow" href="http://www.jetbrains.com/idea/webhelp/getting-help.html" >http://www.jetbrains.com/idea/webhelp/getting-help.html</a></li>
<li>官方 wiki：<a rel="nofollow" href="http://wiki.jetbrains.net/intellij" >http://wiki.jetbrains.net/intellij</a></li>
</ul>
</blockquote>
<h2 id="0ce963d1052f0ba1689eed01429a26af">更多官方资讯跟踪途径</h2>
<blockquote>
<ul>
<li>官方博客：<a rel="nofollow" href="http://blog.jetbrains.com/idea/" >http://blog.jetbrains.com/idea/</a></li>
<li>IntelliJ IDEA 官方 community：<a rel="nofollow" href="https://intellij-support.jetbrains.com/hc/en-us/community/topics" >https://intellij-support.jetbrains.com/hc/en-us/community/topics</a></li>
<li>IntelliJ IDEA 官方 issue：<a rel="nofollow" href="https://youtrack.jetbrains.com/issues/IDEA" >https://youtrack.jetbrains.com/issues/IDEA</a></li>
<li>YouTube：<a rel="nofollow" href="https://www.youtube.com/user/intellijideavideo" >https://www.youtube.com/user/intellijideavideo</a></li>
<li>Twitter：<a rel="nofollow" href="https://twitter.com/IntelliJIDEA" >https://twitter.com/IntelliJIDEA</a></li>
<li>Facebook：<a rel="nofollow" href="https://www.facebook.com/IntelliJIDEA" >https://www.facebook.com/IntelliJIDEA</a></li>
<li>JetBrains 新浪微博：<a rel="nofollow" href="http://www.weibo.com/u/3220313942" >http://www.weibo.com/u/3220313942</a></li>
<li>JetBrains Google+：<a rel="nofollow" href="https://plus.google.com/+jetbrains" >https://plus.google.com/+jetbrains</a></li>
<li>IntelliJ IDEA Google+：<a rel="nofollow" href="https://plus.google.com/+intellijidea" >https://plus.google.com/+intellijidea</a></li>
</ul>
</blockquote>
        </div>