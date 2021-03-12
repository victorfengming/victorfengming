---
title: "PEP8 Python 编码规范"
date:       2019-11-28
subtitle: "遵循规范才能写出优美的代码"
tags:
	- Python
	- background
	- interview
	- standard
---


<div id="article_content" class="article_content clearfix">
    <div id="content_views" class="markdown_views">

        <h1 id="1-pep8"><a name="t0"></a>1. PEP8</h1>

        <p><strong>什么是PEP</strong> <br>
            PEP是 Python Enhancement Proposal 的缩写，翻译过来就是 Python增强建议书 。 <br>
            <strong>PEP8</strong> <br>
            译者：本文基于 2013-08-02 最后修改的 PEP8 版本翻译，若要查看英文原文，请参考<a href="http://www.python.org/dev/peps/pep-0008/"
                                                              rel="nofollow">PEP8</a></p>

        <p>许多项目都有一套专有的编码风格指南，当冲突发生时，应以项目编码规范为优先。 <br>
            当以下情况发生时，也是忽略某个风格指南的好理由：</p>

        <ul>
            <li>当遵守指南会降低代码可读性，甚至对于那些依循 PEP 去阅读代码的人也是这样时。</li>
            <li>当遵守指南会与其他部分的代码风格背离时 — 当然也许这是一个修正某些混乱代码的机会。</li>
            <li>当那些并没有遵循指南的旧代码已无法修改时。</li>
            <li>当你的代码需要与旧版本的 Python 保持兼容，而旧版本的 Python 不支持指南中提到的特性时。</li>
        </ul>


        <h1 id="2-代码布局"><a name="t1"></a>2. 代码布局</h1>
        <h2 id="21-缩进"><a name="t2"></a>2.1 缩进</h2>

        <p>每次缩进使用 4 个空格。</p>

        <p>续行应该与被圆括号、方括号、花括号包裹起来的其他元素对齐，或者使用悬挂式缩进。当使用悬挂式缩进时，应该遵循这些注意事项：第一行不能有参数，应该使用进一步的缩进来将续行与其他行区分开。</p>

        <p>符合本约定的代码：</p>

        <pre class="prettyprint" name="code"><code class="hljs python has-numbering" onclick="mdcp.copyCode(event)"
                                                   style="position: unset;"><span class="hljs-comment"># Aligned with opening delimiter</span>
foo = long_function_name(var_one, var_two,
                 var_three, var_four)

<span class="hljs-comment"># More indentation included to distinguish this from the rest.</span>
<span class="hljs-function"><span class="hljs-keyword">def</span> <span
        class="hljs-title">long_function_name</span><span class="hljs-params">(
var_one, var_two, var_three,
var_four)</span>:</span>
print(var_one)<div class="hljs-button {2}" data-title="复制"></div></code><ul class="pre-numbering" style=""><li
                style="color: rgb(153, 153, 153);">1</li><li style="color: rgb(153, 153, 153);">2</li><li
                style="color: rgb(153, 153, 153);">3</li><li style="color: rgb(153, 153, 153);">4</li><li
                style="color: rgb(153, 153, 153);">5</li><li style="color: rgb(153, 153, 153);">6</li><li
                style="color: rgb(153, 153, 153);">7</li><li style="color: rgb(153, 153, 153);">8</li><li
                style="color: rgb(153, 153, 153);">9</li></ul></pre>

        <p>不符合本约定的代码：</p>

        <pre class="prettyprint" name="code"><code class="hljs python has-numbering" onclick="mdcp.copyCode(event)"
                                                   style="position: unset;"><span class="hljs-comment"># Arguments on first line forbidden when not using vertical alignment</span>
foo = long_function_name(var_one, var_two,
var_three, var_four)

<span class="hljs-comment"># Further indentation required as indentation is not distinguishable</span>
<span class="hljs-function"><span class="hljs-keyword">def</span> <span
        class="hljs-title">long_function_name</span><span class="hljs-params">(
var_one, var_two, var_three,
var_four)</span>:</span>
print(var_one)<div class="hljs-button {2}" data-title="复制"></div></code><ul class="pre-numbering" style=""><li
                style="color: rgb(153, 153, 153);">1</li><li style="color: rgb(153, 153, 153);">2</li><li
                style="color: rgb(153, 153, 153);">3</li><li style="color: rgb(153, 153, 153);">4</li><li
                style="color: rgb(153, 153, 153);">5</li><li style="color: rgb(153, 153, 153);">6</li><li
                style="color: rgb(153, 153, 153);">7</li><li style="color: rgb(153, 153, 153);">8</li><li
                style="color: rgb(153, 153, 153);">9</li></ul></pre>

        <p>可选的符合约定的代码：</p>

        <pre class="prettyprint" name="code"><code class="hljs vala has-numbering" onclick="mdcp.copyCode(event)"
                                                   style="position: unset;"><span class="hljs-preprocessor"># Extra indentation is not necessary.</span>
foo = long_function_name(
var_one, var_two,
var_three, var_four)<div class="hljs-button {2}" data-title="复制"></div></code><ul class="pre-numbering" style=""><li
                style="color: rgb(153, 153, 153);">1</li><li style="color: rgb(153, 153, 153);">2</li><li
                style="color: rgb(153, 153, 153);">3</li><li style="color: rgb(153, 153, 153);">4</li></ul></pre>

        <p>结尾的括号另起一行，如下所示：</p>


        <pre class="prettyprint" name="code"><code class="hljs livecodeserver has-numbering"
                                                   onclick="mdcp.copyCode(event)" style="position: unset;">my_list = [
<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>,
<span class="hljs-number">4</span>, <span class="hljs-number">5</span>, <span class="hljs-number">6</span>,
]
<span class="hljs-built_in">result</span> = some_function_that_takes_arguments(
<span class="hljs-string">'a'</span>, <span class="hljs-string">'b'</span>, <span class="hljs-string">'c'</span>,
<span class="hljs-string">'d'</span>, <span class="hljs-string">'e'</span>, <span class="hljs-string">'f'</span>,
)<div class="hljs-button {2}" data-title="复制"></div></code><ul class="pre-numbering" style=""><li
                style="color: rgb(153, 153, 153);">1</li><li style="color: rgb(153, 153, 153);">2</li><li
                style="color: rgb(153, 153, 153);">3</li><li style="color: rgb(153, 153, 153);">4</li><li
                style="color: rgb(153, 153, 153);">5</li><li style="color: rgb(153, 153, 153);">6</li><li
                style="color: rgb(153, 153, 153);">7</li><li style="color: rgb(153, 153, 153);">8</li></ul></pre>

        <p>or</p>


        <pre class="prettyprint" name="code"><code class="hljs livecodeserver has-numbering"
                                                   onclick="mdcp.copyCode(event)" style="position: unset;">my_list = [
<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>,
<span class="hljs-number">4</span>, <span class="hljs-number">5</span>, <span class="hljs-number">6</span>,
]
<span class="hljs-built_in">result</span> = some_function_that_takes_arguments(
<span class="hljs-string">'a'</span>, <span class="hljs-string">'b'</span>, <span class="hljs-string">'c'</span>,
<span class="hljs-string">'d'</span>, <span class="hljs-string">'e'</span>, <span class="hljs-string">'f'</span>,
)<div class="hljs-button {2}" data-title="复制"></div></code><ul class="pre-numbering" style=""><li
                style="color: rgb(153, 153, 153);">1</li><li style="color: rgb(153, 153, 153);">2</li><li
                style="color: rgb(153, 153, 153);">3</li><li style="color: rgb(153, 153, 153);">4</li><li
                style="color: rgb(153, 153, 153);">5</li><li style="color: rgb(153, 153, 153);">6</li><li
                style="color: rgb(153, 153, 153);">7</li><li style="color: rgb(153, 153, 153);">8</li></ul></pre>


        <h2 id="22-制表符"><a name="t3"></a>2.2 制表符</h2>

        <p>不使用Tap，更不能混合使用Tap和空格</p>

        <blockquote>
            <p>Python 3 不支持空格缩进与制表符缩进混用。 <br>
                Python 2 中的混用缩进代码也应该被转换为统一使用空格。 <br>
                当使用 -t 选项来调用 Python 2 命令行工具时，运行混用缩进的代码会报出警告，当使用 -tt 选项时，运行混用缩进的代码会报出错误。强力建议使用这两个选项。</p>
        </blockquote>


        <h2 id="23-单行最大长度"><a name="t4"></a>2.3 单行最大长度</h2>

        <p>每行最大长度79，换行可以使用反斜杠，最好使用圆括号。 <br>
            文档字符串、注释等最大行宽72 <br>
            换行点要在操作符的后边敲回车。 <br>
            确保使用适当的行续缩进。在二元操作符两端，换行的推荐位置是在操作符之后，而不是操作符之前。</p>

        <pre class="prettyprint" name="code"><code class="hljs python has-numbering" onclick="mdcp.copyCode(event)"
                                                   style="position: unset;"><span class="hljs-class"><span
                class="hljs-keyword">class</span> <span class="hljs-title">Rectangle</span><span class="hljs-params">(Blob)</span>:</span>

<span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">__init__</span><span
        class="hljs-params">(self, width, height,
         color=<span class="hljs-string">'black'</span>, emphasis=None, highlight=<span
            class="hljs-number">0</span>)</span>:</span>
<span class="hljs-keyword">if</span> (width == <span class="hljs-number">0</span> <span
                    class="hljs-keyword">and</span> height == <span class="hljs-number">0</span> <span
                    class="hljs-keyword">and</span>
        color == <span class="hljs-string">'red'</span> <span class="hljs-keyword">and</span> emphasis == <span
                    class="hljs-string">'strong'</span> <span class="hljs-keyword">or</span>
        highlight &gt; <span class="hljs-number">100</span>):
    <span class="hljs-keyword">raise</span> ValueError(<span class="hljs-string">"sorry, you lose"</span>)
<span class="hljs-keyword">if</span> width == <span class="hljs-number">0</span> <span
                    class="hljs-keyword">and</span> height == <span class="hljs-number">0</span> <span
                    class="hljs-keyword">and</span> (color == <span class="hljs-string">'red'</span> <span
                    class="hljs-keyword">or</span>
                                   emphasis <span class="hljs-keyword">is</span> <span
                    class="hljs-keyword">None</span>):
    <span class="hljs-keyword">raise</span> ValueError(<span
                    class="hljs-string">"I don't think so -- values are %s, %s"</span> %
                     (width, height))
Blob.__init__(self, width, height,
              color, emphasis, highlight)<div class="hljs-button {2}" data-title="复制"></div></code><ul
                class="pre-numbering" style=""><li style="color: rgb(153, 153, 153);">1</li><li
                style="color: rgb(153, 153, 153);">2</li><li style="color: rgb(153, 153, 153);">3</li><li
                style="color: rgb(153, 153, 153);">4</li><li style="color: rgb(153, 153, 153);">5</li><li
                style="color: rgb(153, 153, 153);">6</li><li style="color: rgb(153, 153, 153);">7</li><li
                style="color: rgb(153, 153, 153);">8</li><li style="color: rgb(153, 153, 153);">9</li><li
                style="color: rgb(153, 153, 153);">10</li><li style="color: rgb(153, 153, 153);">11</li><li
                style="color: rgb(153, 153, 153);">12</li><li style="color: rgb(153, 153, 153);">13</li><li
                style="color: rgb(153, 153, 153);">14</li></ul></pre>


        <h2 id="24-空白行"><a name="t5"></a>2.4 空白行</h2>

        <p>使用两个空白行来分隔顶级函数定义、类定义。 <br>
            使用单个空白行来分隔类内的方法定义。 <br>
            额外的空白行可以被（尽量少的）用来分隔几组相关的函数。在一堆相关的单行代码之间，空白行应该被省略。 <br>
            在函数中（尽量少的）使用空白行来区分逻辑代码块。</p>


        <h2 id="25-文档编排"><a name="t6"></a>2.5 文档编排</h2>

        <p><strong>（1）模块内容的顺序</strong> <br>
            模块说明和docstring—import—globals&amp;constants—其他定义。其中import部分，又按标准、三方和自己编写顺序依次排放，之间空一行。 <br>
            <strong>（2）不要在一句import中多个库，比如import os, sys不推荐。</strong></p>

        <pre class="prettyprint" name="code"><code class="hljs python has-numbering" onclick="mdcp.copyCode(event)"
                                                   style="position: unset;"><span
                class="hljs-comment">#符合约定的代码：     </span>
<span class="hljs-keyword">import</span> os
<span class="hljs-keyword">import</span> sys

<span class="hljs-keyword">from</span> subprocess <span class="hljs-keyword">import</span> Popen, PIPE

<span class="hljs-comment">#不符合本约定的代码：  </span>
<span class="hljs-keyword">import</span> os,sys<div class="hljs-button {2}" data-title="复制"></div></code><ul
                class="pre-numbering" style=""><li style="color: rgb(153, 153, 153);">1</li><li
                style="color: rgb(153, 153, 153);">2</li><li style="color: rgb(153, 153, 153);">3</li><li
                style="color: rgb(153, 153, 153);">4</li><li style="color: rgb(153, 153, 153);">5</li><li
                style="color: rgb(153, 153, 153);">6</li><li style="color: rgb(153, 153, 153);">7</li><li
                style="color: rgb(153, 153, 153);">8</li></ul></pre>

        <p><strong>（3）如果采用from XX import XX引用库，可以省略‘module.’，都是可能出现命名冲突，这时就要采用import XX。</strong> <br>
            <strong>（4）多条 Import 语句总应该遵循这样的顺序书写：</strong></p>

        <ul>
            <li>标准库的导入</li>
            <li>相关第三方库导入</li>
            <li>本地应用/库的相关导入</li>
        </ul>

        <p><strong>（5）当在某个包含类的模块中导入类时，这样的书写方式是合理的：</strong></p>


        <pre class="prettyprint" name="code"><code class="hljs python has-numbering" onclick="mdcp.copyCode(event)"
                                                   style="position: unset;"><span class="hljs-keyword">from</span> myclass <span
                class="hljs-keyword">import</span> MyClass
<span class="hljs-keyword">from</span> foo.bar.yourclass <span class="hljs-keyword">import</span> YourClass<div
                    class="hljs-button {2}" data-title="复制"></div></code><ul class="pre-numbering" style=""><li
                style="color: rgb(153, 153, 153);">1</li><li style="color: rgb(153, 153, 153);">2</li></ul></pre>

        <p>但如果这样的书写方式引起类名冲突，则请这样书写：</p>


        <pre class="prettyprint" name="code"><code class="hljs java has-numbering" onclick="mdcp.copyCode(event)"
                                                   style="position: unset;"><span class="hljs-keyword">import</span> myclass
<span class="hljs-keyword">import</span> foo.bar.yourclass<div class="hljs-button {2}" data-title="复制"></div></code><ul
                class="pre-numbering" style=""><li style="color: rgb(153, 153, 153);">1</li><li
                style="color: rgb(153, 153, 153);">2</li></ul></pre>

        <p>并使用 “myclass.MyClass” 和 “foo.bar.yourclass.YourClass” 来对其进行引用。</p>

        <h1 id="3-空格的使用"><a name="t7"></a>3. 空格的使用</h1>

        <p>总体原则，避免不必要的空格。 <br>
            （1）各种右括号前不要加空格。</p>


        <pre class="prettyprint" name="code"><code class="hljs css has-numbering" onclick="mdcp.copyCode(event)"
                                                   style="position: unset;">#符合约定的代码
<span class="hljs-tag">spam</span>(<span class="hljs-tag">ham</span><span class="hljs-attr_selector">[1]</span>, <span
                    class="hljs-rules">{<span class="hljs-rule"><span class="hljs-attribute">eggs</span>:<span
                    class="hljs-value"> <span class="hljs-number">2</span></span></span></span>})
#不符合约定的代码
<span class="hljs-tag">spam</span>( <span class="hljs-tag">ham</span><span
                    class="hljs-attr_selector">[ 1 ]</span>, <span class="hljs-rules">{ <span class="hljs-rule"><span
                    class="hljs-attribute">eggs</span>:<span class="hljs-value"> <span
                    class="hljs-number">2</span> </span></span></span>} )<div class="hljs-button {2}"
                                                                              data-title="复制"></div></code><ul
                class="pre-numbering" style=""><li style="color: rgb(153, 153, 153);">1</li><li
                style="color: rgb(153, 153, 153);">2</li><li style="color: rgb(153, 153, 153);">3</li><li
                style="color: rgb(153, 153, 153);">4</li></ul></pre>

        <p>（2）逗号、冒号、分号前不要加空格。</p>


        <pre class="prettyprint" name="code"><code class="hljs php has-numbering" onclick="mdcp.copyCode(event)"
                                                   style="position: unset;"><span class="hljs-comment">#符合约定的代码</span>
<span class="hljs-keyword">if</span> x == <span class="hljs-number">4</span>: <span class="hljs-keyword">print</span> x, y; x, y = y, x
<span class="hljs-comment">#不符合约定的代码</span>
<span class="hljs-keyword">if</span> x == <span class="hljs-number">4</span> : <span class="hljs-keyword">print</span> x , y ; x , y = y , x<div
                    class="hljs-button {2}" data-title="复制"></div></code><ul class="pre-numbering" style=""><li
                style="color: rgb(153, 153, 153);">1</li><li style="color: rgb(153, 153, 153);">2</li><li
                style="color: rgb(153, 153, 153);">3</li><li style="color: rgb(153, 153, 153);">4</li></ul></pre>

        <p>（3）函数的左括号前不要加空格。如Func(1)。</p>


        <pre class="prettyprint" name="code"><code class="hljs vala has-numbering" onclick="mdcp.copyCode(event)"
                                                   style="position: unset;"><span
                class="hljs-preprocessor">#符合约定代码</span>
spam(<span class="hljs-number">1</span>)
<span class="hljs-preprocessor">#不符合约定的代码</span>
spam (<span class="hljs-number">1</span>)<div class="hljs-button {2}" data-title="复制"></div></code><ul
                class="pre-numbering" style=""><li style="color: rgb(153, 153, 153);">1</li><li
                style="color: rgb(153, 153, 153);">2</li><li style="color: rgb(153, 153, 153);">3</li><li
                style="color: rgb(153, 153, 153);">4</li></ul></pre>

        <p>（4）序列的左括号前不要加空格。如list[2]。</p>


        <pre class="prettyprint" name="code"><code class="hljs php has-numbering" onclick="mdcp.copyCode(event)"
                                                   style="position: unset;"><span class="hljs-comment">#符合约定的代码</span>
dict[<span class="hljs-string">'key'</span>] = <span class="hljs-keyword">list</span>[index]
<span class="hljs-comment">#不符合约定的代码</span>
dict [<span class="hljs-string">'key'</span>] = <span class="hljs-keyword">list</span> [index]<div
                    class="hljs-button {2}" data-title="复制"></div></code><ul class="pre-numbering" style=""><li
                style="color: rgb(153, 153, 153);">1</li><li style="color: rgb(153, 153, 153);">2</li><li
                style="color: rgb(153, 153, 153);">3</li><li style="color: rgb(153, 153, 153);">4</li></ul></pre>

        <p>（5） 操作符左右各加一个空格，不要为了对齐增加空格。</p>


        <pre class="prettyprint" name="code"><code class="hljs makefile has-numbering" onclick="mdcp.copyCode(event)"
                                                   style="position: unset;"><span class="hljs-comment">#符合约定的代码</span>
<span class="hljs-constant">x</span> = 1
<span class="hljs-constant">y</span> = 2
<span class="hljs-constant">long_variable</span> = 3
<span class="hljs-comment">#不符合约定的代码</span>
<span class="hljs-constant">x</span>             = 1
<span class="hljs-constant">y</span>             = 2
<span class="hljs-constant">long_variable</span> = 3<div class="hljs-button {2}" data-title="复制"></div></code><ul
                class="pre-numbering" style=""><li style="color: rgb(153, 153, 153);">1</li><li
                style="color: rgb(153, 153, 153);">2</li><li style="color: rgb(153, 153, 153);">3</li><li
                style="color: rgb(153, 153, 153);">4</li><li style="color: rgb(153, 153, 153);">5</li><li
                style="color: rgb(153, 153, 153);">6</li><li style="color: rgb(153, 153, 153);">7</li><li
                style="color: rgb(153, 153, 153);">8</li></ul></pre>

        <p>（6） 函数默认参数使用的赋值符左右省略空格。</p>


        <pre class="prettyprint" name="code"><code class="hljs python has-numbering" onclick="mdcp.copyCode(event)"
                                                   style="position: unset;"><span class="hljs-comment">#符合约定的代码</span>
<span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">complex</span><span
        class="hljs-params">(real, imag=<span class="hljs-number">0.0</span>)</span>:</span>
<span class="hljs-keyword">return</span> magic(r=real, i=imag)
<span class="hljs-comment">#不符合约定的代码</span>
<span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">complex</span><span
        class="hljs-params">(real, imag = <span class="hljs-number">0.0</span>)</span>:</span>
<span class="hljs-keyword">return</span> magic(r = real, i = imag)<div class="hljs-button {2}"
                                                                       data-title="复制"></div></code><ul
                class="pre-numbering" style=""><li style="color: rgb(153, 153, 153);">1</li><li
                style="color: rgb(153, 153, 153);">2</li><li style="color: rgb(153, 153, 153);">3</li><li
                style="color: rgb(153, 153, 153);">4</li><li style="color: rgb(153, 153, 153);">5</li><li
                style="color: rgb(153, 153, 153);">6</li></ul></pre>

        <p>（7） 不要将多句语句写在同一行，尽管使用‘；’允许。 <br>
            （8） if/for/while语句中，即使执行语句只有一句，也必须另起一行。</p>

        <h1 id="4-注释"><a name="t8"></a>4. 注释</h1>

        <p><strong>总体原则，错误的注释不如没有注释。所以当一段代码发生变化时，第一件事就是要修改注释！</strong> <br>
            注释必须使用英文，最好是完整的句子，首字母大写，句后要有结束符，结束符后跟两个空格，开始下一句。如果是短语，可以省略结束符。 <br>
            <strong>（1）块注释</strong> <br>
            在一段代码前增加的注释。在‘#’后加一空格。段落之间以只有‘#’的行间隔。比如：</p>

        <pre class="prettyprint" name="code"><code class="hljs vala has-numbering" onclick="mdcp.copyCode(event)"
                                                   style="position: unset;"><span class="hljs-preprocessor"># Description : Module config.</span>
<span class="hljs-preprocessor"># </span>
<span class="hljs-preprocessor"># Input : None</span>
<span class="hljs-preprocessor">#</span>
<span class="hljs-preprocessor"># Output : None</span><div class="hljs-button {2}" data-title="复制"></div></code><ul
                class="pre-numbering" style=""><li style="color: rgb(153, 153, 153);">1</li><li
                style="color: rgb(153, 153, 153);">2</li><li style="color: rgb(153, 153, 153);">3</li><li
                style="color: rgb(153, 153, 153);">4</li><li style="color: rgb(153, 153, 153);">5</li></ul></pre>

        <p><strong>（2）行注释</strong> <br>
            在一句代码后加注释。比如：</p>

        <pre class="prettyprint" name="code"><code class="hljs bash has-numbering" onclick="mdcp.copyCode(event)"
                                                   style="position: unset;">x = x + <span class="hljs-number">1</span>           <span
                class="hljs-comment"># Increment x</span><div class="hljs-button {2}" data-title="复制"></div></code><ul
                class="pre-numbering" style=""><li style="color: rgb(153, 153, 153);">1</li></ul></pre>

        <p>但是这种方式尽量少使用。 <br>
            <strong>（3）避免无谓的注释。</strong></p>

        <h1 id="5-文档描述"><a name="t9"></a>5. 文档描述</h1>

        <p>（1）为所有的共有模块、函数、类、方法写docstrings；非共有的没有必要，但是可以写注释（在def的下一行）。 <br>
            （2）如果docstring要换行，参考如下例子,详见<a href="http://www.python.org/dev/peps/pep-0257/" rel="nofollow">PEP 257</a></p>

        <pre class="prettyprint" name="code"><code class="hljs python has-numbering" onclick="mdcp.copyCode(event)"
                                                   style="position: unset;"><span class="hljs-string">"""Return a foobang

Optional plotz says to frobnicate the bizbaz first.

"""</span><div class="hljs-button {2}" data-title="复制"></div></code><ul class="pre-numbering" style=""><li
                style="color: rgb(153, 153, 153);">1</li><li style="color: rgb(153, 153, 153);">2</li><li
                style="color: rgb(153, 153, 153);">3</li><li style="color: rgb(153, 153, 153);">4</li><li
                style="color: rgb(153, 153, 153);">5</li></ul></pre>


        <h1 id="6-命名规范"><a name="t10"></a>6. 命名规范</h1>

        <p><strong>总体原则，新编代码必须按下面命名风格进行，现有库的编码尽量保持风格。</strong></p>

        <blockquote>
            <p>1 尽量单独使用小写字母‘l’，大写字母‘O’等容易混淆的字母。 <br>
                2 模块命名尽量短小，使用全部小写的方式，可以使用下划线。 <br>
                3 包命名尽量短小，使用全部小写的方式，不可以使用下划线。 <br>
                4 类的命名使用CapWords的方式，模块内部使用的类采用_CapWords的方式。 <br>
                5 异常命名使用CapWords+Error后缀的方式。 <br>
                6 全局变量尽量只在模块内有效，类似C语言中的static。实现方法有两种，一是<strong>all</strong>机制;二是前缀一个下划线。 <br>
                7 函数命名使用全部小写的方式，可以使用下划线。 <br>
                8 常量命名使用全部大写的方式，可以使用下划线。 <br>
                9 类的属性（方法和变量）命名使用全部小写的方式，可以使用下划线。 <br>
                9 类的属性有3种作用域public、non-public和subclass API，可以理解成C++中的public、private、protected，non-public属性前，前缀一条下划线。
                <br>
                11 类的属性若与关键字名字冲突，后缀一下划线，尽量不要使用缩略等其他方式。 <br>
                12 为避免与子类属性命名冲突，在类的一些属性前，前缀两条下划线。比如：类Foo中声明__a,访问时，只能通过Foo._Foo__a，避免歧义。如果子类也叫Foo，那就无能为力了。 <br>
                13 类的方法第一个参数必须是self，而静态方法第一个参数必须是cls。</p>
        </blockquote>

        <p><strong>（1）变量</strong></p>

        <p>常量 : 大写加下划线</p>


        <pre class="prettyprint" name="code"><code class="hljs  has-numbering" onclick="mdcp.copyCode(event)"
                                                   style="position: unset;">USER_CONSTANT<div class="hljs-button {2}"
                                                                                              data-title="复制"></div></code><ul
                class="pre-numbering" style=""><li style="color: rgb(153, 153, 153);">1</li></ul></pre>

        <p>对于不会发生改变的全局变量，使用大写加下划线。</p>

        <p>私有变量 : 小写和一个前导下划线</p>


        <pre class="prettyprint" name="code"><code class="hljs  has-numbering" onclick="mdcp.copyCode(event)"
                                                   style="position: unset;">_private_value<div class="hljs-button {2}"
                                                                                               data-title="复制"></div></code><ul
                class="pre-numbering" style=""><li style="color: rgb(153, 153, 153);">1</li></ul></pre>

        <p>Python 中不存在私有变量一说，若是遇到需要保护的变量，使用小写和一个前导下划线。但这只是程序员之间的一个约定，用于警告说明这是一个私有变量，外部类不要去访问它。但实际上，外部类还是可以访问到这个变量。</p>

        <p>内置变量 : 小写，两个前导下划线和两个后置下划线</p>


        <pre class="prettyprint" name="code"><code class="hljs markdown has-numbering" onclick="mdcp.copyCode(event)"
                                                   style="position: unset;"><span class="hljs-strong">__class__</span><div
                class="hljs-button {2}" data-title="复制"></div></code><ul class="pre-numbering" style=""><li
                style="color: rgb(153, 153, 153);">1</li></ul></pre>

        <p>两个前导下划线会导致变量在解释期间被更名。这是为了避免内置变量和其他变量产生冲突。用户定义的变量要严格避免这种风格。以免导致混乱。</p>

        <p><strong>（2）函数和方法</strong></p>

        <p>总体而言应该使用，小写和下划线。但有些比较老的库使用的是混合大小写，即首单词小写，之后每个单词第一个字母大写，其余小写。但现在，小写和下划线已成为规范。</p>

        <p>私有方法 ： 小写和一个前导下划线</p>

        <pre class="prettyprint" name="code"><code class="hljs python has-numbering" onclick="mdcp.copyCode(event)"
                                                   style="position: unset;"><span class="hljs-function"><span
                class="hljs-keyword">def</span> <span class="hljs-title">_secrete</span><span
                class="hljs-params">(self)</span>:</span>
<span class="hljs-keyword">print</span> <span class="hljs-string">"don't test me."</span><div
                    class="hljs-button {2}" data-title="复制"></div></code><ul class="pre-numbering" style=""><li
                style="color: rgb(153, 153, 153);">1</li><li style="color: rgb(153, 153, 153);">2</li></ul></pre>

        <p>这里和私有变量一样，并不是真正的私有访问权限。同时也应该注意一般函数不要使用两个前导下划线(当遇到两个前导下划线时，Python 的名称改编特性将发挥作用)。特殊函数后面会提及。</p>

        <p>特殊方法 ： 小写和两个前导下划线，两个后置下划线</p>


        <pre class="prettyprint" name="code"><code class="hljs python has-numbering" onclick="mdcp.copyCode(event)"
                                                   style="position: unset;"><span class="hljs-function"><span
                class="hljs-keyword">def</span> <span class="hljs-title">__add__</span><span class="hljs-params">(self, other)</span>:</span>
<span class="hljs-keyword">return</span> int.__add__(other)<div class="hljs-button {2}"
                                                                data-title="复制"></div></code><ul
                class="pre-numbering" style=""><li style="color: rgb(153, 153, 153);">1</li><li
                style="color: rgb(153, 153, 153);">2</li></ul></pre>

        <p>这种风格只应用于特殊函数，比如操作符重载等。</p>

        <p>函数参数 : 小写和下划线，缺省值等号两边无空格</p>


        <pre class="prettyprint" name="code"><code class="hljs python has-numbering" onclick="mdcp.copyCode(event)"
                                                   style="position: unset;"><span class="hljs-function"><span
                class="hljs-keyword">def</span> <span class="hljs-title">connect</span><span class="hljs-params">(self, user=None)</span>:</span>
self._user = user<div class="hljs-button {2}" data-title="复制"></div></code><ul class="pre-numbering" style=""><li
                style="color: rgb(153, 153, 153);">1</li><li style="color: rgb(153, 153, 153);">2</li></ul></pre>

        <p><strong>（3）类</strong></p>

        <p>类总是使用驼峰格式命名，即所有单词首字母大写其余字母小写。类名应该简明，精确，并足以从中理解类所完成的工作。常见的一个方法是使用表示其类型或者特性的后缀，例如: <br>
            SQLEngine <br>
            MimeTypes</p>

        <p>对于基类而言，可以使用一个 Base 或者 Abstract 前缀</p>


        <pre class="prettyprint" name="code"><code class="hljs python has-numbering" onclick="mdcp.copyCode(event)"
                                                   style="position: unset;">BaseCookie
AbstractGroup
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">UserProfile</span><span
        class="hljs-params">(object)</span>:</span>
<span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">__init__</span><span
        class="hljs-params">(self, profile)</span>:</span>
<span class="hljs-keyword">return</span> self._profile = profile

<span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">profile</span><span
        class="hljs-params">(self)</span>:</span>
<span class="hljs-keyword">return</span> self._profile<div class="hljs-button {2}" data-title="复制"></div></code><ul
                class="pre-numbering" style=""><li style="color: rgb(153, 153, 153);">1</li><li
                style="color: rgb(153, 153, 153);">2</li><li style="color: rgb(153, 153, 153);">3</li><li
                style="color: rgb(153, 153, 153);">4</li><li style="color: rgb(153, 153, 153);">5</li><li
                style="color: rgb(153, 153, 153);">6</li><li style="color: rgb(153, 153, 153);">7</li><li
                style="color: rgb(153, 153, 153);">8</li></ul></pre>

        <h1 id="7-编码建议"><a name="t11"></a>7. 编码建议</h1>

        <p>1 编码中考虑到其他python实现的效率等问题，比如运算符‘+’在CPython（Python）中效率很高，都是Jython中却非常低，所以应该采用.join()的方式。 <br>
            2 尽可能使用‘is’‘is not’取代‘==’，比如if x is not None 要优于if x。 <br>
            3 使用基于类的异常，每个模块或包都有自己的异常类，此异常类继承自Exception。 <br>
            4 异常中不要使用裸露的except，except后跟具体的exceptions。 <br>
            5 异常中try的代码尽可能少。比如：</p>

        <pre class="prettyprint" name="code"><code class="hljs cs has-numbering" onclick="mdcp.copyCode(event)"
                                                   style="position: unset;"><span class="hljs-keyword">try</span>:
<span class="hljs-keyword">value</span> = collection[key]
except KeyError:
<span class="hljs-keyword">return</span> key_not_found(key)
<span class="hljs-keyword">else</span>:
<span class="hljs-keyword">return</span> handle_value(<span class="hljs-keyword">value</span>)<div
                    class="hljs-button {2}" data-title="复制"></div></code><ul class="pre-numbering" style=""><li
                style="color: rgb(153, 153, 153);">1</li><li style="color: rgb(153, 153, 153);">2</li><li
                style="color: rgb(153, 153, 153);">3</li><li style="color: rgb(153, 153, 153);">4</li><li
                style="color: rgb(153, 153, 153);">5</li><li style="color: rgb(153, 153, 153);">6</li></ul></pre>

        <p>要优于</p>


        <pre class="prettyprint" name="code"><code class="hljs vala has-numbering" onclick="mdcp.copyCode(event)"
                                                   style="position: unset;"><span class="hljs-keyword">try</span>:
<span class="hljs-preprocessor"># Too broad!</span>
<span class="hljs-keyword">return</span> handle_value(collection[key])
except KeyError:
<span class="hljs-preprocessor"># Will also catch KeyError raised by handle_value()</span>
<span class="hljs-keyword">return</span> key_not_found(key)<div class="hljs-button {2}" data-title="复制"></div></code><ul
                class="pre-numbering" style=""><li style="color: rgb(153, 153, 153);">1</li><li
                style="color: rgb(153, 153, 153);">2</li><li style="color: rgb(153, 153, 153);">3</li><li
                style="color: rgb(153, 153, 153);">4</li><li style="color: rgb(153, 153, 153);">5</li><li
                style="color: rgb(153, 153, 153);">6</li></ul></pre>

        <p>6 使用startswith() and endswith()代替切片进行序列前缀或后缀的检查。比如：</p>


        <pre class="prettyprint" name="code"><code class="hljs bash has-numbering" onclick="mdcp.copyCode(event)"
                                                   style="position: unset;"> <span class="hljs-keyword">if</span> foo.startswith(<span
                class="hljs-string">'bar'</span>):<div class="hljs-button {2}" data-title="复制"></div></code><ul
                class="pre-numbering" style=""><li style="color: rgb(153, 153, 153);">1</li></ul></pre>

        <p>优于</p>


        <pre class="prettyprint" name="code"><code class="hljs bash has-numbering" onclick="mdcp.copyCode(event)"
                                                   style="position: unset;"> <span
                class="hljs-keyword">if</span> foo[:<span class="hljs-number">3</span>] == <span class="hljs-string">'bar'</span>:<div
                class="hljs-button {2}" data-title="复制"></div></code><ul class="pre-numbering" style=""><li
                style="color: rgb(153, 153, 153);">1</li></ul></pre>

        <p>7 使用isinstance()比较对象的类型。比如</p>


        <pre class="prettyprint" name="code"><code class="hljs cs has-numbering" onclick="mdcp.copyCode(event)"
                                                   style="position: unset;"><span class="hljs-keyword">if</span> isinstance(obj, <span
                class="hljs-keyword">int</span>): <div class="hljs-button {2}" data-title="复制"></div></code><ul
                class="pre-numbering" style=""><li style="color: rgb(153, 153, 153);">1</li></ul></pre>

        <p>优于</p>


        <pre class="prettyprint" name="code"><code class="hljs haskell has-numbering" onclick="mdcp.copyCode(event)"
                                                   style="position: unset;"> <span class="hljs-keyword">if</span> <span
                class="hljs-typedef"><span class="hljs-keyword">type</span><span class="hljs-container">(<span
                class="hljs-title">obj</span>)</span> is <span class="hljs-keyword">type</span><span
                class="hljs-container">(1)</span>:</span><div class="hljs-button {2}" data-title="复制"></div></code><ul
                class="pre-numbering" style=""><li style="color: rgb(153, 153, 153);">1</li></ul></pre>

        <p>8 判断序列空或不空，有如下规则</p>


        <pre class="prettyprint" name="code"><code class="hljs ruby has-numbering" onclick="mdcp.copyCode(event)"
                                                   style="position: unset;"><span class="hljs-keyword">if</span> <span
                class="hljs-keyword">not</span> <span class="hljs-symbol">seq:</span>
<span class="hljs-keyword">if</span> <span class="hljs-symbol">seq:</span><div class="hljs-button {2}"
                                                                               data-title="复制"></div></code><ul
                class="pre-numbering" style=""><li style="color: rgb(153, 153, 153);">1</li><li
                style="color: rgb(153, 153, 153);">2</li></ul></pre>

        <p>优于</p>


        <pre class="prettyprint" name="code"><code class="hljs livecodeserver has-numbering"
                                                   onclick="mdcp.copyCode(event)" style="position: unset;"><span
                class="hljs-keyword">if</span> <span class="hljs-built_in">len</span>(seq)
<span class="hljs-keyword">if</span> <span class="hljs-operator">not</span> <span class="hljs-built_in">len</span>(seq)<div
                    class="hljs-button {2}" data-title="复制"></div></code><ul class="pre-numbering" style=""><li
                style="color: rgb(153, 153, 153);">1</li><li style="color: rgb(153, 153, 153);">2</li></ul></pre>

        <p>9 字符串不要以空格收尾。 <br>
            10 二进制数据判断使用 if boolvalue的方式。</p>


        <h1 id="8-参考文献"><a name="t12"></a>8. 参考文献</h1>

        <p>[1] PEP8中文翻译 <a href="http://wiki.hiaero.net/doku.php?id=python:pep8" rel="nofollow">http://wiki.hiaero.net/doku.php?id=python:pep8</a>
            <br>
            [2] PEP8 Python 编码规范整理 <a href="https://www.douban.com/note/134971609/" rel="nofollow">https://www.douban.com/note/134971609/</a>
            <br>
            [3] Python 代码风格 和 PEP8 <a href="http://www.blogjava.net/lincode/archive/2011/02/02/343859.html"
                                      rel="nofollow">http://www.blogjava.net/lincode/archive/2011/02/02/343859.html</a>
        </p></div>
    <link href="https://csdnimg.cn/release/phoenix/mdeditor/markdown_views-b6c3c6d139.css" rel="stylesheet">
</div>