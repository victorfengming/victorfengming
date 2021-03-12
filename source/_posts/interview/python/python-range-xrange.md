---
title: "python range() 和xrange()的区别"
date:       2019-11-28
tags:
	- Python
	- background
	- interview
---


<div id="cnblogs_post_body" class="blogpost-body ">
    <div class="cnblogs_Highlighter sh-gutter">
        <div>
            <div id="highlighter_834530" class="syntaxhighlighter  bash">
                <div class="toolbar"><span><a href="#" class="toolbar_item command_help help">?</a></span></div>
                <table border="0" cellpadding="0" cellspacing="0">
                    <tbody>
                    <tr>
                        <td class="gutter">
                            <div class="line number1 index0 alt2">1</div>
                            <div class="line number2 index1 alt1">2</div>
                            <div class="line number3 index2 alt2">3</div>
                            <div class="line number4 index3 alt1">4</div>
                            <div class="line number5 index4 alt2">5</div>
                            <div class="line number6 index5 alt1">6</div>
                            <div class="line number7 index6 alt2">7</div>
                            <div class="line number8 index7 alt1">8</div>
                            <div class="line number9 index8 alt2">9</div>
                            <div class="line number10 index9 alt1">10</div>
                            <div class="line number11 index10 alt2">11</div>
                            <div class="line number12 index11 alt1">12</div>
                        </td>
                        <td class="code">
                            <div class="container">
                                <div class="line number1 index0 alt2"><code class="bash plain">Help on
                                    built-</code><code class="bash keyword">in</code> <code class="bash keyword">function</code>
                                    <code class="bash plain">range </code><code class="bash keyword">in</code> <code
                                            class="bash plain">module __builtin__:</code></div>
                                <div class="line number2 index1 alt1">&nbsp;</div>
                                <div class="line number3 index2 alt2"><code class="bash plain">range(...)</code></div>
                                <div class="line number4 index3 alt1"><code
                                        class="bash spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="bash plain">range(stop)
                                    -&gt; list of integers</code></div>
                                <div class="line number5 index4 alt2"><code
                                        class="bash spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="bash plain">range(start,
                                    stop[, step]) -&gt; list of integers</code></div>
                                <div class="line number6 index5 alt1"><code
                                        class="bash spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code>&nbsp;
                                </div>
                                <div class="line number7 index6 alt2"><code
                                        class="bash spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="bash plain">Return
                                    a list containing an arithmetic progression of integers.</code></div>
                                <div class="line number8 index7 alt1"><code
                                        class="bash spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="bash plain">range(i,
                                    j) returns [i, i+1, i+2, ..., j-1]; start (!) defaults to 0.</code></div>
                                <div class="line number9 index8 alt2"><code
                                        class="bash spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="bash plain">When
                                    step is given, it specifies the increment (or decrement).</code></div>
                                <div class="line number10 index9 alt1"><code class="bash spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code
                                        class="bash plain">For example, range(4) returns [0, 1, 2, 3].&nbsp; The end
                                    point is omitted!</code></div>
                                <div class="line number11 index10 alt2"><code class="bash spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code
                                        class="bash plain">These are exactly the valid indices </code><code
                                        class="bash keyword">for</code> <code class="bash plain">a list of 4
                                    elements.</code></div>
                                <div class="line number12 index11 alt1"><code class="bash plain">(END)</code></div>
                            </div>
                        </td>
                    </tr>
                    </tbody>
                </table>
            </div>
        </div>
    </div>
    <p>以上是range函数的说明，三个参数，分别代表开始，结束位置和步长。</p>
    <p>使用方法如下：</p>
    <div class="cnblogs_Highlighter sh-gutter">
        <div>
            <div id="highlighter_356591" class="syntaxhighlighter  python">
                <div class="toolbar"><span><a href="#" class="toolbar_item command_help help">?</a></span></div>
                <table border="0" cellpadding="0" cellspacing="0">
                    <tbody>
                    <tr>
                        <td class="gutter">
                            <div class="line number1 index0 alt2">1</div>
                            <div class="line number2 index1 alt1">2</div>
                            <div class="line number3 index2 alt2">3</div>
                            <div class="line number4 index3 alt1">4</div>
                            <div class="line number5 index4 alt2">5</div>
                            <div class="line number6 index5 alt1">6</div>
                            <div class="line number7 index6 alt2">7</div>
                            <div class="line number8 index7 alt1">8</div>
                            <div class="line number9 index8 alt2">9</div>
                            <div class="line number10 index9 alt1">10</div>
                            <div class="line number11 index10 alt2">11</div>
                            <div class="line number12 index11 alt1">12</div>
                            <div class="line number13 index12 alt2">13</div>
                            <div class="line number14 index13 alt1">14</div>
                            <div class="line number15 index14 alt2">15</div>
                            <div class="line number16 index15 alt1">16</div>
                            <div class="line number17 index16 alt2">17</div>
                            <div class="line number18 index17 alt1">18</div>
                            <div class="line number19 index18 alt2">19</div>
                            <div class="line number20 index19 alt1">20</div>
                            <div class="line number21 index20 alt2">21</div>
                            <div class="line number22 index21 alt1">22</div>
                            <div class="line number23 index22 alt2">23</div>
                            <div class="line number24 index23 alt1">24</div>
                            <div class="line number25 index24 alt2">25</div>
                        </td>
                        <td class="code">
                            <div class="container">
                                <div class="line number1 index0 alt2"><code class="python plain">In [</code><code
                                        class="python value">2</code><code class="python plain">]: </code><code
                                        class="python functions">range</code><code class="python plain">(</code><code
                                        class="python value">10</code><code class="python plain">)</code></div>
                                <div class="line number2 index1 alt1"><code class="python plain">Out[</code><code
                                        class="python value">2</code><code class="python plain">]: [</code><code
                                        class="python value">0</code><code class="python plain">, </code><code
                                        class="python value">1</code><code class="python plain">, </code><code
                                        class="python value">2</code><code class="python plain">, </code><code
                                        class="python value">3</code><code class="python plain">, </code><code
                                        class="python value">4</code><code class="python plain">, </code><code
                                        class="python value">5</code><code class="python plain">, </code><code
                                        class="python value">6</code><code class="python plain">, </code><code
                                        class="python value">7</code><code class="python plain">, </code><code
                                        class="python value">8</code><code class="python plain">, </code><code
                                        class="python value">9</code><code class="python plain">]</code></div>
                                <div class="line number3 index2 alt2">&nbsp;</div>
                                <div class="line number4 index3 alt1"><code class="python plain">In [</code><code
                                        class="python value">3</code><code class="python plain">]: </code><code
                                        class="python functions">range</code><code class="python plain">(</code><code
                                        class="python value">1</code><code class="python plain">, </code><code
                                        class="python value">10</code><code class="python plain">)</code></div>
                                <div class="line number5 index4 alt2"><code class="python plain">Out[</code><code
                                        class="python value">3</code><code class="python plain">]: [</code><code
                                        class="python value">1</code><code class="python plain">, </code><code
                                        class="python value">2</code><code class="python plain">, </code><code
                                        class="python value">3</code><code class="python plain">, </code><code
                                        class="python value">4</code><code class="python plain">, </code><code
                                        class="python value">5</code><code class="python plain">, </code><code
                                        class="python value">6</code><code class="python plain">, </code><code
                                        class="python value">7</code><code class="python plain">, </code><code
                                        class="python value">8</code><code class="python plain">, </code><code
                                        class="python value">9</code><code class="python plain">]</code></div>
                                <div class="line number6 index5 alt1">&nbsp;</div>
                                <div class="line number7 index6 alt2"><code class="python plain">In [</code><code
                                        class="python value">4</code><code class="python plain">]: </code><code
                                        class="python functions">range</code><code class="python plain">(</code><code
                                        class="python value">1</code><code class="python plain">, </code><code
                                        class="python value">10</code><code class="python plain">, </code><code
                                        class="python value">2</code><code class="python plain">)</code></div>
                                <div class="line number8 index7 alt1"><code class="python plain">Out[</code><code
                                        class="python value">4</code><code class="python plain">]: [</code><code
                                        class="python value">1</code><code class="python plain">, </code><code
                                        class="python value">3</code><code class="python plain">, </code><code
                                        class="python value">5</code><code class="python plain">, </code><code
                                        class="python value">7</code><code class="python plain">, </code><code
                                        class="python value">9</code><code class="python plain">]</code></div>
                                <div class="line number9 index8 alt2">&nbsp;</div>
                                <div class="line number10 index9 alt1"><code class="python plain">In [</code><code
                                        class="python value">5</code><code class="python plain">]: </code><code
                                        class="python functions">type</code><code class="python plain">(</code><code
                                        class="python functions">range</code><code class="python plain">(</code><code
                                        class="python value">1</code><code class="python plain">, </code><code
                                        class="python value">3</code><code class="python plain">))</code></div>
                                <div class="line number11 index10 alt2"><code class="python plain">Out[</code><code
                                        class="python value">5</code><code class="python plain">]: </code><code
                                        class="python functions">list</code></div>
                                <div class="line number12 index11 alt1">&nbsp;</div>
                                <div class="line number13 index12 alt2"><code class="python plain">In [</code><code
                                        class="python value">6</code><code class="python plain">]: </code><code
                                        class="python keyword">for</code> <code class="python plain">i </code><code
                                        class="python keyword">in</code> <code
                                        class="python functions">range</code><code class="python plain">(</code><code
                                        class="python value">10</code><code class="python plain">):</code></div>
                                <div class="line number14 index13 alt1"><code
                                        class="python spaces">&nbsp;&nbsp;&nbsp;</code><code class="python plain">...:&nbsp;&nbsp;&nbsp;&nbsp; </code><code
                                        class="python functions">print</code> <code class="python plain">i</code></div>
                                <div class="line number15 index14 alt2"><code
                                        class="python spaces">&nbsp;&nbsp;&nbsp;</code><code class="python plain">...:&nbsp;&nbsp;&nbsp;&nbsp; </code>
                                </div>
                                <div class="line number16 index15 alt1"><code class="python value">0</code></div>
                                <div class="line number17 index16 alt2"><code class="python value">1</code></div>
                                <div class="line number18 index17 alt1"><code class="python value">2</code></div>
                                <div class="line number19 index18 alt2"><code class="python value">3</code></div>
                                <div class="line number20 index19 alt1"><code class="python value">4</code></div>
                                <div class="line number21 index20 alt2"><code class="python value">5</code></div>
                                <div class="line number22 index21 alt1"><code class="python value">6</code></div>
                                <div class="line number23 index22 alt2"><code class="python value">7</code></div>
                                <div class="line number24 index23 alt1"><code class="python value">8</code></div>
                                <div class="line number25 index24 alt2"><code class="python value">9</code></div>
                            </div>
                        </td>
                    </tr>
                    </tbody>
                </table>
            </div>
        </div>
    </div>
    <p>　　</p>
    <p>而xrange（）说明如下：</p>
    <div class="cnblogs_Highlighter sh-gutter">
        <div>
            <div id="highlighter_795700" class="syntaxhighlighter  bash">
                <div class="toolbar"><span><a href="#" class="toolbar_item command_help help">?</a></span></div>
                <table border="0" cellpadding="0" cellspacing="0">
                    <tbody>
                    <tr>
                        <td class="gutter">
                            <div class="line number1 index0 alt2">1</div>
                            <div class="line number2 index1 alt1">2</div>
                            <div class="line number3 index2 alt2">3</div>
                            <div class="line number4 index3 alt1">4</div>
                            <div class="line number5 index4 alt2">5</div>
                            <div class="line number6 index5 alt1">6</div>
                            <div class="line number7 index6 alt2">7</div>
                            <div class="line number8 index7 alt1">8</div>
                            <div class="line number9 index8 alt2">9</div>
                            <div class="line number10 index9 alt1">10</div>
                            <div class="line number11 index10 alt2">11</div>
                            <div class="line number12 index11 alt1">12</div>
                            <div class="line number13 index12 alt2">13</div>
                            <div class="line number14 index13 alt1">14</div>
                            <div class="line number15 index14 alt2">15</div>
                            <div class="line number16 index15 alt1">16</div>
                            <div class="line number17 index16 alt2">17</div>
                            <div class="line number18 index17 alt1">18</div>
                            <div class="line number19 index18 alt2">19</div>
                            <div class="line number20 index19 alt1">20</div>
                            <div class="line number21 index20 alt2">21</div>
                            <div class="line number22 index21 alt1">22</div>
                            <div class="line number23 index22 alt2">23</div>
                            <div class="line number24 index23 alt1">24</div>
                            <div class="line number25 index24 alt2">25</div>
                            <div class="line number26 index25 alt1">26</div>
                            <div class="line number27 index26 alt2">27</div>
                            <div class="line number28 index27 alt1">28</div>
                            <div class="line number29 index28 alt2">29</div>
                            <div class="line number30 index29 alt1">30</div>
                            <div class="line number31 index30 alt2">31</div>
                            <div class="line number32 index31 alt1">32</div>
                            <div class="line number33 index32 alt2">33</div>
                            <div class="line number34 index33 alt1">34</div>
                            <div class="line number35 index34 alt2">35</div>
                            <div class="line number36 index35 alt1">36</div>
                            <div class="line number37 index36 alt2">37</div>
                            <div class="line number38 index37 alt1">38</div>
                        </td>
                        <td class="code">
                            <div class="container">
                                <div class="line number1 index0 alt2"><code class="bash plain">Help on class
                                    xrange </code><code class="bash keyword">in</code> <code class="bash plain">module
                                    __builtin__:</code></div>
                                <div class="line number2 index1 alt1">&nbsp;</div>
                                <div class="line number3 index2 alt2"><code class="bash plain">class
                                    xrange(object)</code></div>
                                <div class="line number4 index3 alt1"><code class="bash spaces">&nbsp;</code><code
                                        class="bash plain">|&nbsp; xrange(stop) -&gt; xrange object</code></div>
                                <div class="line number5 index4 alt2"><code class="bash spaces">&nbsp;</code><code
                                        class="bash plain">|&nbsp; xrange(start, stop[, step]) -&gt; xrange
                                    object</code></div>
                                <div class="line number6 index5 alt1"><code class="bash spaces">&nbsp;</code><code
                                        class="bash plain">|&nbsp; </code></div>
                                <div class="line number7 index6 alt2"><code class="bash spaces">&nbsp;</code><code
                                        class="bash plain">|&nbsp; Like range(), but instead of returning a list,
                                    returns an object that</code></div>
                                <div class="line number8 index7 alt1"><code class="bash spaces">&nbsp;</code><code
                                        class="bash plain">|&nbsp; generates the numbers </code><code
                                        class="bash keyword">in</code> <code class="bash plain">the range on demand.&nbsp;
                                    For looping, this is </code></div>
                                <div class="line number9 index8 alt2"><code class="bash spaces">&nbsp;</code><code
                                        class="bash plain">|&nbsp; slightly faster than range() and </code><code
                                        class="bash functions">more</code> <code class="bash plain">memory
                                    efficient.</code></div>
                                <div class="line number10 index9 alt1"><code class="bash spaces">&nbsp;</code><code
                                        class="bash plain">|&nbsp; </code></div>
                                <div class="line number11 index10 alt2"><code class="bash spaces">&nbsp;</code><code
                                        class="bash plain">|&nbsp; Methods defined here:</code></div>
                                <div class="line number12 index11 alt1"><code class="bash spaces">&nbsp;</code><code
                                        class="bash plain">|&nbsp; </code></div>
                                <div class="line number13 index12 alt2"><code class="bash spaces">&nbsp;</code><code
                                        class="bash plain">|&nbsp; __getattribute__(...)</code></div>
                                <div class="line number14 index13 alt1"><code class="bash spaces">&nbsp;</code><code
                                        class="bash plain">|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                                    x.__getattribute__(</code><code class="bash string">'name'</code><code
                                        class="bash plain">) &lt;==&gt; x.name</code></div>
                                <div class="line number15 index14 alt2"><code class="bash spaces">&nbsp;</code><code
                                        class="bash plain">|&nbsp; </code></div>
                                <div class="line number16 index15 alt1"><code class="bash spaces">&nbsp;</code><code
                                        class="bash plain">|&nbsp; __getitem__(...)</code></div>
                                <div class="line number17 index16 alt2"><code class="bash spaces">&nbsp;</code><code
                                        class="bash plain">|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; x.__getitem__(y) &lt;==&gt;
                                    x[y]</code></div>
                                <div class="line number18 index17 alt1"><code class="bash spaces">&nbsp;</code><code
                                        class="bash plain">|&nbsp; </code></div>
                                <div class="line number19 index18 alt2"><code class="bash spaces">&nbsp;</code><code
                                        class="bash plain">|&nbsp; __iter__(...)</code></div>
                                <div class="line number20 index19 alt1"><code class="bash spaces">&nbsp;</code><code
                                        class="bash plain">|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; x.__iter__() &lt;==&gt;
                                    iter(x)</code></div>
                                <div class="line number21 index20 alt2"><code class="bash spaces">&nbsp;</code><code
                                        class="bash plain">|&nbsp; </code></div>
                                <div class="line number22 index21 alt1"><code class="bash spaces">&nbsp;</code><code
                                        class="bash plain">|&nbsp; __len__(...)</code></div>
                                <div class="line number23 index22 alt2"><code class="bash spaces">&nbsp;</code><code
                                        class="bash plain">|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; x.__len__() &lt;==&gt;
                                    len(x)</code></div>
                                <div class="line number24 index23 alt1"><code class="bash spaces">&nbsp;</code><code
                                        class="bash plain">|&nbsp; </code></div>
                                <div class="line number25 index24 alt2"><code class="bash spaces">&nbsp;</code><code
                                        class="bash plain">|&nbsp; __reduce__(...)</code></div>
                                <div class="line number26 index25 alt1"><code class="bash spaces">&nbsp;</code><code
                                        class="bash plain">|&nbsp; </code></div>
                                <div class="line number27 index26 alt2"><code class="bash spaces">&nbsp;</code><code
                                        class="bash plain">|&nbsp; __repr__(...)</code></div>
                                <div class="line number28 index27 alt1"><code class="bash spaces">&nbsp;</code><code
                                        class="bash plain">|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; x.__repr__() &lt;==&gt;
                                    repr(x)</code></div>
                                <div class="line number29 index28 alt2"><code class="bash spaces">&nbsp;</code><code
                                        class="bash plain">|&nbsp; </code></div>
                                <div class="line number30 index29 alt1"><code class="bash spaces">&nbsp;</code><code
                                        class="bash plain">|&nbsp; __reversed__(...)</code></div>
                                <div class="line number31 index30 alt2"><code class="bash spaces">&nbsp;</code><code
                                        class="bash plain">|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Returns a reverse
                                    iterator.</code></div>
                                <div class="line number32 index31 alt1"><code class="bash spaces">&nbsp;</code><code
                                        class="bash plain">|&nbsp; </code></div>
                                <div class="line number33 index32 alt2"><code class="bash spaces">&nbsp;</code><code
                                        class="bash plain">|&nbsp;
                                    ----------------------------------------------------------------------</code></div>
                                <div class="line number34 index33 alt1"><code class="bash spaces">&nbsp;</code><code
                                        class="bash plain">|&nbsp; Data and other attributes defined here:</code></div>
                                <div class="line number35 index34 alt2"><code class="bash spaces">&nbsp;</code><code
                                        class="bash plain">|&nbsp; </code></div>
                                <div class="line number36 index35 alt1"><code class="bash spaces">&nbsp;</code><code
                                        class="bash plain">|&nbsp; __new__ = &lt;built-</code><code
                                        class="bash keyword">in</code> <code class="bash plain">method __new__
                                    of </code><code class="bash functions">type</code> <code class="bash plain">object&gt;</code>
                                </div>
                                <div class="line number37 index36 alt2"><code class="bash spaces">&nbsp;</code><code
                                        class="bash plain">|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; T.__new__(S, ...) -&gt; a new
                                    object with </code><code class="bash functions">type</code> <code
                                        class="bash plain">S, a subtype of T</code></div>
                                <div class="line number38 index37 alt1"><code class="bash plain">(END)</code></div>
                            </div>
                        </td>
                    </tr>
                    </tbody>
                </table>
            </div>
        </div>
    </div>
    <p>说明了两者的区别是xrange返回的是一个可迭代的对象，range返回的则是一个列表. 同时效率更高，更快。</p>
    <p>原因是实现的时候使用了yield（唔，源码没看见，具体对比可以看一下http://ju.outofmemory.cn/entry/122781），</p>
    <p>因此更节省内存，规模越大区别更明显.</p>
    <p>关于可迭代对象的定义见：https://eastlakeside.gitbooks.io/interpy-zh/content/Generators/Iterable.html</p>
    <p>即，只要定义了可以返回一个迭代器的__iter__方法，或者__getitem__那么就是可迭代对象。</p>
    <p>&nbsp;</p>
    <p>xrange使用方法如下：</p>
    <div class="cnblogs_Highlighter sh-gutter">
        <div>
            <div id="highlighter_575244" class="syntaxhighlighter  python">
                <div class="toolbar"><span><a href="#" class="toolbar_item command_help help">?</a></span></div>
                <table border="0" cellpadding="0" cellspacing="0">
                    <tbody>
                    <tr>
                        <td class="gutter">
                            <div class="line number1 index0 alt2">1</div>
                            <div class="line number2 index1 alt1">2</div>
                            <div class="line number3 index2 alt2">3</div>
                            <div class="line number4 index3 alt1">4</div>
                            <div class="line number5 index4 alt2">5</div>
                            <div class="line number6 index5 alt1">6</div>
                            <div class="line number7 index6 alt2">7</div>
                            <div class="line number8 index7 alt1">8</div>
                            <div class="line number9 index8 alt2">9</div>
                            <div class="line number10 index9 alt1">10</div>
                        </td>
                        <td class="code">
                            <div class="container">
                                <div class="line number1 index0 alt2"><code class="python plain">In [</code><code
                                        class="python value">13</code><code class="python plain">]: </code><code
                                        class="python functions">list</code><code class="python plain">(</code><code
                                        class="python functions">xrange</code><code class="python plain">(</code><code
                                        class="python value">3</code><code class="python plain">))</code></div>
                                <div class="line number2 index1 alt1"><code class="python plain">Out[</code><code
                                        class="python value">13</code><code class="python plain">]: [</code><code
                                        class="python value">0</code><code class="python plain">, </code><code
                                        class="python value">1</code><code class="python plain">, </code><code
                                        class="python value">2</code><code class="python plain">]</code></div>
                                <div class="line number3 index2 alt2">&nbsp;</div>
                                <div class="line number4 index3 alt1"><code class="python plain">In [</code><code
                                        class="python value">14</code><code class="python plain">]: a </code><code
                                        class="python keyword">=</code> <code
                                        class="python functions">xrange</code><code class="python plain">(</code><code
                                        class="python value">3</code><code class="python plain">)</code></div>
                                <div class="line number5 index4 alt2">&nbsp;</div>
                                <div class="line number6 index5 alt1"><code class="python plain">In [</code><code
                                        class="python value">15</code><code class="python plain">]: a.__iter__</code>
                                </div>
                                <div class="line number7 index6 alt2"><code class="python plain">Out[</code><code
                                        class="python value">15</code><code class="python plain">]:
                                    &lt;method</code><code class="python keyword">-</code><code class="python plain">wrapper </code><code
                                        class="python string">'__iter__'</code> <code
                                        class="python plain">of </code><code class="python functions">xrange</code>
                                    <code class="python functions">object</code> <code
                                            class="python plain">at </code><code
                                            class="python value">0x7f415be1bdc8</code><code
                                            class="python plain">&gt;</code></div>
                                <div class="line number8 index7 alt1">&nbsp;</div>
                                <div class="line number9 index8 alt2"><code class="python plain">In [</code><code
                                        class="python value">16</code><code class="python plain">]: a.__iter__()</code>
                                </div>
                                <div class="line number10 index9 alt1"><code class="python plain">Out[</code><code
                                        class="python value">16</code><code class="python plain">]: &lt;rangeiterator
                                    at </code><code class="python value">0x7f415aa27210</code><code
                                        class="python plain">&gt;</code></div>
                            </div>
                        </td>
                    </tr>
                    </tbody>
                </table>
            </div>
        </div>
    </div>
    <p>　　</p>
    <p>　</p>
    <p>　　</p>
</div>