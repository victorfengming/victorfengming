---
title: "python生成requirements.txt的两种方法"
date:       2019-01-15
subtitle: "带你玩转虚拟环境"
tags:
	- Python
	- background
	- solution
---




<div id="content">
    <p>python项目如何在另一个环境上重新构建项目所需要的运行环境依赖包？</p>
    <p>使用的时候边记载是个很麻烦的事情，总会出现遗漏的包的问题，这个时候手动安装也很麻烦，不能确定代码报错的需要安装的包是什么版本。这些问题，requirements.txt都可以解决！</p>
    <p>生成requirements.txt，有两种方式：</p>
    <p>第一种 适用于 <strong>单虚拟环境的情况：</strong> ：</p>
    <div class="jb51code">
        <div>
            <div id="highlighter_464138" class="syntaxhighlighter  py">
                <div class="toolbar"><span><a href="#" class="toolbar_item command_help help">?</a></span></div>
                <table border="0" cellpadding="0" cellspacing="0">
                    <tbody>
                    <tr>
                        <td class="gutter">
                            <div class="line number1 index0 alt2">1</div>
                        </td>
                        <td class="code">
                            <div class="container">
                                <div class="line number1 index0 alt2"><code class="py plain">pip freeze &gt;
                                    requirements.txt</code></div>
                            </div>
                        </td>
                    </tr>
                    </tbody>
                </table>
            </div>
        </div>
    </div>
    <p>为什么只适用于单虚拟环境？因为这种方式，会将环境中的依赖包全都加入，如果使用的全局环境，则下载的所有包都会在里面，不管是不时当前项目依赖的，如下图</p>
    <p style="text-align: center"><img alt="" src="//files.jb51.net/file_images/article/201909/2019091810141718.png">
    </p>
    <p>当然这种情况并不是我们想要的，当我们使用的是全局环境时，可以使用第二种方法。</p>
    <p>第二种 <strong>(推荐)</strong> 使用 <code>pipreqs</code> ，github地址为： https://github.com/bndr/pipreqs</p>
    <div class="jb51code">
        <div>
            <div id="highlighter_117559" class="syntaxhighlighter  py">
                <div class="toolbar"><span><a href="#" class="toolbar_item command_help help">?</a></span></div>
                <table border="0" cellpadding="0" cellspacing="0">
                    <tbody>
                    <tr>
                        <td class="gutter">
                            <div class="line number1 index0 alt2">1</div>
                            <div class="line number2 index1 alt1">2</div>
                            <div class="line number3 index2 alt2">3</div>
                            <div class="line number4 index3 alt1">4</div>
                        </td>
                        <td class="code">
                            <div class="container">
                                <div class="line number1 index0 alt2"><code class="py comments"># 安装</code></div>
                                <div class="line number2 index1 alt1"><code class="py plain">pip install pipreqs</code>
                                </div>
                                <div class="line number3 index2 alt2"><code class="py comments"># 在当前目录生成</code></div>
                                <div class="line number4 index3 alt1"><code class="py plain">pipreqs . </code><code
                                        class="py keyword">-</code><code class="py keyword">-</code><code
                                        class="py plain">encoding</code><code class="py keyword">=</code><code
                                        class="py plain">utf8 </code><code class="py keyword">-</code><code
                                        class="py keyword">-</code><code class="py plain">force</code></div>
                            </div>
                        </td>
                    </tr>
                    </tbody>
                </table>
            </div>
        </div>
    </div>
    <p>注意 <code>--encoding=utf8</code> 为使用utf8编码，不然可能会报UnicodeDecodeError: 'gbk' codec can't decode byte 0xae in
        position 406: illegal multibyte sequence 的错误。</p>
    <p><code>--force</code> 强制执行，当 生成目录下的requirements.txt存在时覆盖。</p>
    <p>当当当，可以看见我依赖的只有这些啦</p>
    <p style="text-align: center"><img alt="" src="//files.jb51.net/file_images/article/201909/2019091810141719.png">
    </p>
    <p>使用requirements.txt安装依赖的方式：</p>
    <div class="jb51code">
        <div>
            <div id="highlighter_474262" class="syntaxhighlighter  py">
                <div class="toolbar"><span><a href="#" class="toolbar_item command_help help">?</a></span></div>
                <table border="0" cellpadding="0" cellspacing="0">
                    <tbody>
                    <tr>
                        <td class="gutter">
                            <div class="line number1 index0 alt2">1</div>
                        </td>
                        <td class="code">
                            <div class="container">
                                <div class="line number1 index0 alt2"><code class="py plain">pip install </code><code
                                        class="py keyword">-</code><code class="py plain">r requirements.txt</code>
                                </div>
                            </div>
                        </td>
                    </tr>
                    </tbody>
                </table>
            </div>
        </div>
    </div>



    <p>原文链接：https://segmentfault.com/a/1190000020411620</p>

</div>