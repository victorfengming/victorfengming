---
title: "linux中的技巧和快捷键总结"
date:       2019-08-27
subtitle: "Linux面试宝典"
tags:
	- Linux
	- basis
	- server
---


<section class="" mpa-from-tpl="t">
    <section mpa-from-tpl="t">
        <section class="" style="" powered-by="xiumi.us" mpa-from-tpl="t">
            <section style="margin: 10px 0% 8px;" mpa-from-tpl="t">
                <section
                        style="display: inline-block;width: 100%;vertical-align: top;border-left: 3px solid rgb(160, 160, 160);border-bottom-left-radius: 0px;padding-left: 8px;background-color: rgb(250, 250, 250);"
                        mpa-from-tpl="t">
                    <section class="" powered-by="xiumi.us" mpa-from-tpl="t">
                        <section style="" mpa-from-tpl="t">
                            <section style="color: rgb(123, 123, 123);" mpa-from-tpl="t"><p><span
                                    style="font-size: 14px;"></span></p></section>
                        </section>
                    </section>
                </section>
            </section>
        </section>
    </section>
</section>
<h2 style="color: inherit;line-height: inherit;margin-bottom: 1.5em;font-weight: bold;font-size: 1.4em;margin-top: 5px;">
    <span style="font-size: inherit;color: inherit;line-height: inherit;">前言</span><br></h2>
<p style="font-size: inherit;color: inherit;line-height: inherit;margin-top: 1.5em;margin-bottom: 1.5em;">
    linux中的一些小技巧可以大大提高你的工作效率，本文就细数那些提高效率或者简单却有效的linux技巧。</p>
<h2 style="color: inherit;line-height: inherit;margin-top: 1.5em;margin-bottom: 1.5em;font-weight: bold;font-size: 1.4em;">
    <span style="font-size: inherit;color: inherit;line-height: inherit;">命令编辑及光标移动</span></h2>
<p style="font-size: inherit;color: inherit;line-height: inherit;margin-top: 1.5em;margin-bottom: 1.5em;">
    这里有很多快捷键可以帮我们修正自己的命令。接下来使用光标二字代替光标的位置。</p><h4
        style="color: inherit;line-height: inherit;margin-top: 1.5em;margin-bottom: 1.5em;font-weight: bold;font-size: 1.2em;">
    <span style="font-size: inherit;color: inherit;line-height: inherit;">删除从开头到光标处的命令文本</span></h4>
<p style="font-size: inherit;color: inherit;line-height: inherit;margin-top: 1.5em;margin-bottom: 1.5em;">ctrl +
    u，例如：</p>
<pre style="font-size: inherit;color: inherit;line-height: inherit;"><code class=""
                                                                           style="margin-right: 2px;margin-left: 2px;line-height: 18px;font-size: 14px;letter-spacing: 0px;font-family: Consolas, Inconsolata, Courier, monospace;border-radius: 0px;color: rgb(169, 183, 198);background: rgb(40, 43, 46);padding: 0.5em;display: block !important;word-wrap: normal !important;word-break: normal !important;overflow: auto !important;"><span
        class=""
        style="font-size: inherit;line-height: inherit;color: rgb(238, 220, 112);word-wrap: inherit !important;word-break: inherit !important;">$ cd</span>&nbsp;/proc/tty;<span
        class=""
        style="font-size: inherit;line-height: inherit;color: rgb(238, 220, 112);word-wrap: inherit !important;word-break: inherit !important;">ls</span>&nbsp;-al光标<br></code></pre>
<p style="font-size: inherit;color: inherit;line-height: inherit;margin-top: 1.5em;margin-bottom: 1.5em;">如果此时使用ctrl
    + u快捷键，那么该条命令都会被清除，而不需要长按backspace键。</p><h4
        style="color: inherit;line-height: inherit;margin-top: 1.5em;margin-bottom: 1.5em;font-weight: bold;font-size: 1.2em;">
    <span style="font-size: inherit;color: inherit;line-height: inherit;">删除从光标到结尾处的命令文本</span></h4>
<p style="font-size: inherit;color: inherit;line-height: inherit;margin-top: 1.5em;margin-bottom: 1.5em;">
    ctrl+k，例如：</p>
<pre style="font-size: inherit;color: inherit;line-height: inherit;"><code class=""
                                                                           style="margin-right: 2px;margin-left: 2px;line-height: 18px;font-size: 14px;letter-spacing: 0px;font-family: Consolas, Inconsolata, Courier, monospace;border-radius: 0px;color: rgb(169, 183, 198);background: rgb(40, 43, 46);padding: 0.5em;display: block !important;word-wrap: normal !important;word-break: normal !important;overflow: auto !important;"><span
        class=""
        style="font-size: inherit;line-height: inherit;color: rgb(238, 220, 112);word-wrap: inherit !important;word-break: inherit !important;">$ cd</span>&nbsp;/proc/tty光标;<span
        class=""
        style="font-size: inherit;line-height: inherit;color: rgb(238, 220, 112);word-wrap: inherit !important;word-break: inherit !important;">ls</span>&nbsp;-al<br></code></pre>
<p style="font-size: inherit;color: inherit;line-height: inherit;margin-top: 1.5em;margin-bottom: 1.5em;">如果此时使用ctrl
    + k快捷键，那么从光标开始处到结尾的命令文本将会被删除。</p>
<p style="font-size: inherit;color: inherit;line-height: inherit;margin-top: 1.5em;margin-bottom: 1.5em;">
    还有其他的操作，不再举例，例如：</p>
<ul style="" class="list-paddingleft-2">
    <li><p><span style="font-size: inherit;color: inherit;line-height: inherit;">ctrl + a:光标移动到命令开头</span></p></li>
    <li><p><span style="font-size: inherit;color: inherit;line-height: inherit;">ctrl + e：光标移动到命令结尾</span></p></li>
    <li><p><span style="font-size: inherit;color: inherit;line-height: inherit;">alt &nbsp;f:光标向前移动一个单词</span></p>
    </li>
    <li><p><span style="font-size: inherit;color: inherit;line-height: inherit;">alt &nbsp;b：光标向前移动一个单词</span></p>
    </li>
    <li><p><span style="font-size: inherit;color: inherit;line-height: inherit;">ctrl w：删除一个词（以空格隔开的字符串）</span></p>
    </li>
</ul>
<h2 style="color: inherit;line-height: inherit;margin-top: 1.5em;margin-bottom: 1.5em;font-weight: bold;font-size: 1.4em;">
    <span style="font-size: inherit;color: inherit;line-height: inherit;">历史命令快速执行</span></h2>
<p style="font-size: inherit;color: inherit;line-height: inherit;margin-top: 1.5em;margin-bottom: 1.5em;">
    我们都知道history记录了执行的历史命令，而使用!＋历史命令前的数字，可快速执行历史命令。另外，还可以使用ctrl+r搜索执行过的命令。</p>
<h2 style="color: inherit;line-height: inherit;margin-top: 1.5em;margin-bottom: 1.5em;font-weight: bold;font-size: 1.4em;">
    <span style="font-size: inherit;color: inherit;line-height: inherit;">部分历史命令查看</span></h2>
<p style="font-size: inherit;color: inherit;line-height: inherit;margin-top: 1.5em;margin-bottom: 1.5em;">
    history会显示大量的历史命令，而fs -l只会显示部分。</p>
<h2 style="color: inherit;line-height: inherit;margin-top: 1.5em;margin-bottom: 1.5em;font-weight: bold;font-size: 1.4em;">
    <span style="font-size: inherit;color: inherit;line-height: inherit;">实时查看日志</span></h2>
<pre style="font-size: inherit;color: inherit;line-height: inherit;"><code class=""
                                                                           style="margin-right: 2px;margin-left: 2px;line-height: 18px;font-size: 14px;letter-spacing: 0px;font-family: Consolas, Inconsolata, Courier, monospace;border-radius: 0px;color: rgb(169, 183, 198);background: rgb(40, 43, 46);padding: 0.5em;display: block !important;word-wrap: normal !important;word-break: normal !important;overflow: auto !important;">$&nbsp;tail&nbsp;-f&nbsp;filename.<span
        class=""
        style="font-size: inherit;line-height: inherit;color: rgb(248, 35, 117);word-wrap: inherit !important;word-break: inherit !important;">log</span><br></code></pre>
<p style="font-size: inherit;color: inherit;line-height: inherit;margin-top: 1.5em;margin-bottom: 1.5em;">tail -f
    加文件名，可以实时显示日志文件内容。当然，使用less命令查看文件内容，并且使用shift+f键，也可达到类似的效果。</p>
<h2 style="color: inherit;line-height: inherit;margin-top: 1.5em;margin-bottom: 1.5em;font-weight: bold;font-size: 1.4em;">
    <span style="font-size: inherit;color: inherit;line-height: inherit;">磁盘或内存情况查看</span></h2><h4
        style="color: inherit;line-height: inherit;margin-top: 1.5em;margin-bottom: 1.5em;font-weight: bold;font-size: 1.2em;">
    <span style="font-size: inherit;color: inherit;line-height: inherit;">怎么知道当前磁盘是否满了呢？</span></h4>
<pre style="font-size: inherit;color: inherit;line-height: inherit;"><code class=""
                                                                           style="margin-right: 2px;margin-left: 2px;line-height: 18px;font-size: 14px;letter-spacing: 0px;font-family: Consolas, Inconsolata, Courier, monospace;border-radius: 0px;color: rgb(169, 183, 198);background: rgb(40, 43, 46);padding: 0.5em;display: block !important;word-wrap: normal !important;word-break: normal !important;overflow: auto !important;">$&nbsp;df&nbsp;-h<br>/dev/sda14&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span
        class=""
        style="font-size: inherit;line-height: inherit;color: rgb(174, 135, 250);word-wrap: inherit !important;word-break: inherit !important;">4.6</span>G&nbsp;&nbsp;&nbsp;<span
        class=""
        style="font-size: inherit;line-height: inherit;color: rgb(174, 135, 250);word-wrap: inherit !important;word-break: inherit !important;">10</span>M&nbsp;&nbsp;<span
        class=""
        style="font-size: inherit;line-height: inherit;color: rgb(174, 135, 250);word-wrap: inherit !important;word-break: inherit !important;">4.4</span>G&nbsp;&nbsp;&nbsp;<span
        class=""
        style="font-size: inherit;line-height: inherit;color: rgb(174, 135, 250);word-wrap: inherit !important;word-break: inherit !important;">1</span>%&nbsp;/tmp<br>/dev/sda11&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span
        class=""
        style="font-size: inherit;line-height: inherit;color: rgb(174, 135, 250);word-wrap: inherit !important;word-break: inherit !important;">454</span>M&nbsp;&nbsp;<span
        class=""
        style="font-size: inherit;line-height: inherit;color: rgb(174, 135, 250);word-wrap: inherit !important;word-break: inherit !important;">366</span>M&nbsp;&nbsp;&nbsp;<span
        class=""
        style="font-size: inherit;line-height: inherit;color: rgb(174, 135, 250);word-wrap: inherit !important;word-break: inherit !important;">61</span>M&nbsp;&nbsp;<span
        class=""
        style="font-size: inherit;line-height: inherit;color: rgb(174, 135, 250);word-wrap: inherit !important;word-break: inherit !important;">86</span>%&nbsp;/boot<br>/dev/sda15&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span
        class=""
        style="font-size: inherit;line-height: inherit;color: rgb(174, 135, 250);word-wrap: inherit !important;word-break: inherit !important;">55</span>G&nbsp;&nbsp;&nbsp;<span
        class=""
        style="font-size: inherit;line-height: inherit;color: rgb(174, 135, 250);word-wrap: inherit !important;word-break: inherit !important;">18</span>G&nbsp;&nbsp;&nbsp;<span
        class=""
        style="font-size: inherit;line-height: inherit;color: rgb(174, 135, 250);word-wrap: inherit !important;word-break: inherit !important;">35</span>G&nbsp;&nbsp;<span
        class=""
        style="font-size: inherit;line-height: inherit;color: rgb(174, 135, 250);word-wrap: inherit !important;word-break: inherit !important;">35</span>%&nbsp;/home<br>/dev/sda1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span
        class=""
        style="font-size: inherit;line-height: inherit;color: rgb(174, 135, 250);word-wrap: inherit !important;word-break: inherit !important;">256</span>M&nbsp;&nbsp;&nbsp;<span
        class=""
        style="font-size: inherit;line-height: inherit;color: rgb(174, 135, 250);word-wrap: inherit !important;word-break: inherit !important;">31</span>M&nbsp;&nbsp;<span
        class=""
        style="font-size: inherit;line-height: inherit;color: rgb(174, 135, 250);word-wrap: inherit !important;word-break: inherit !important;">226</span>M&nbsp;&nbsp;<span
        class=""
        style="font-size: inherit;line-height: inherit;color: rgb(174, 135, 250);word-wrap: inherit !important;word-break: inherit !important;">12</span>%&nbsp;/boot/efi<br>tmpfs&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span
        class=""
        style="font-size: inherit;line-height: inherit;color: rgb(174, 135, 250);word-wrap: inherit !important;word-break: inherit !important;">786</span>M&nbsp;&nbsp;&nbsp;<span
        class=""
        style="font-size: inherit;line-height: inherit;color: rgb(174, 135, 250);word-wrap: inherit !important;word-break: inherit !important;">64</span>K&nbsp;&nbsp;<span
        class=""
        style="font-size: inherit;line-height: inherit;color: rgb(174, 135, 250);word-wrap: inherit !important;word-break: inherit !important;">786</span>M&nbsp;&nbsp;&nbsp;<span
        class=""
        style="font-size: inherit;line-height: inherit;color: rgb(174, 135, 250);word-wrap: inherit !important;word-break: inherit !important;">1</span>%&nbsp;/run/user/<span
        class=""
        style="font-size: inherit;line-height: inherit;color: rgb(174, 135, 250);word-wrap: inherit !important;word-break: inherit !important;">1000</span><br></code></pre>
<p style="font-size: inherit;color: inherit;line-height: inherit;margin-top: 1.5em;margin-bottom: 1.5em;">
    使用df命令可以快速查看各挂载路径磁盘占用情况。</p><h4
        style="color: inherit;line-height: inherit;margin-top: 1.5em;margin-bottom: 1.5em;font-weight: bold;font-size: 1.2em;">
    <span style="font-size: inherit;color: inherit;line-height: inherit;">当前目录各个子目录占用空间大小</span></h4>
<p style="font-size: inherit;color: inherit;line-height: inherit;margin-top: 1.5em;margin-bottom: 1.5em;">
    如果你已经知道home目录占用空间较大了，你想知道home目录下各个目录占用情况：</p>
<pre style="font-size: inherit;color: inherit;line-height: inherit;"><code class=""
                                                                           style="margin-right: 2px;margin-left: 2px;line-height: 18px;font-size: 14px;letter-spacing: 0px;font-family: Consolas, Inconsolata, Courier, monospace;border-radius: 0px;color: rgb(169, 183, 198);background: rgb(40, 43, 46);padding: 0.5em;display: block !important;word-wrap: normal !important;word-break: normal !important;overflow: auto !important;">$&nbsp;du&nbsp;-h&nbsp;–-max-depth=<span
        class=""
        style="font-size: inherit;line-height: inherit;color: rgb(174, 135, 250);word-wrap: inherit !important;word-break: inherit !important;">1</span>&nbsp;/home(或者-d&nbsp;<span
        class=""
        style="font-size: inherit;line-height: inherit;color: rgb(174, 135, 250);word-wrap: inherit !important;word-break: inherit !important;">1</span>)<br><span
        class=""
        style="font-size: inherit;line-height: inherit;color: rgb(174, 135, 250);word-wrap: inherit !important;word-break: inherit !important;">18</span>G&nbsp;&nbsp;&nbsp;&nbsp;/home/hyb<br><span
        class=""
        style="font-size: inherit;line-height: inherit;color: rgb(174, 135, 250);word-wrap: inherit !important;word-break: inherit !important;">16</span>K&nbsp;&nbsp;&nbsp;&nbsp;/home/lost+found<br><span
        class=""
        style="font-size: inherit;line-height: inherit;color: rgb(174, 135, 250);word-wrap: inherit !important;word-break: inherit !important;">18</span>G&nbsp;&nbsp;&nbsp;&nbsp;<span
        class=""
        style="font-size: inherit;color: inherit;line-height: inherit;word-wrap: inherit !important;word-break: inherit !important;">/home/</span><br></code></pre>
<p style="font-size: inherit;color: inherit;line-height: inherit;margin-top: 1.5em;margin-bottom: 1.5em;">
    这里指定了目录深度，否则的话，它会递归统计子目录占用空间大小，可自行尝试。</p><h4
        style="color: inherit;line-height: inherit;margin-top: 1.5em;margin-bottom: 1.5em;font-weight: bold;font-size: 1.2em;">
    <span style="font-size: inherit;color: inherit;line-height: inherit;">当前内存使用情况</span></h4>
<pre style="font-size: inherit;color: inherit;line-height: inherit;"><code class=""
                                                                           style="margin-right: 2px;margin-left: 2px;line-height: 18px;font-size: 14px;letter-spacing: 0px;font-family: Consolas, Inconsolata, Courier, monospace;border-radius: 0px;color: rgb(169, 183, 198);background: rgb(40, 43, 46);padding: 0.5em;display: block !important;word-wrap: normal !important;word-break: normal !important;overflow: auto !important;">$&nbsp;<span
        class=""
        style="font-size: inherit;line-height: inherit;color: rgb(248, 35, 117);word-wrap: inherit !important;word-break: inherit !important;">free</span>&nbsp;-h<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;total&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;used&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span
        class=""
        style="font-size: inherit;line-height: inherit;color: rgb(248, 35, 117);word-wrap: inherit !important;word-break: inherit !important;">free</span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;shared&nbsp;&nbsp;buff/cache&nbsp;&nbsp;&nbsp;available<br>Mem:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span
        class=""
        style="font-size: inherit;line-height: inherit;color: rgb(174, 135, 250);word-wrap: inherit !important;word-break: inherit !important;">7.7</span>G&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span
        class=""
        style="font-size: inherit;line-height: inherit;color: rgb(174, 135, 250);word-wrap: inherit !important;word-break: inherit !important;">3.5</span>G&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span
        class=""
        style="font-size: inherit;line-height: inherit;color: rgb(174, 135, 250);word-wrap: inherit !important;word-break: inherit !important;">452</span>M&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span
        class=""
        style="font-size: inherit;line-height: inherit;color: rgb(174, 135, 250);word-wrap: inherit !important;word-break: inherit !important;">345</span>M&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span
        class=""
        style="font-size: inherit;line-height: inherit;color: rgb(174, 135, 250);word-wrap: inherit !important;word-break: inherit !important;">3.7</span>G&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span
        class=""
        style="font-size: inherit;line-height: inherit;color: rgb(174, 135, 250);word-wrap: inherit !important;word-break: inherit !important;">3.5</span>G<br>Swap:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span
        class=""
        style="font-size: inherit;line-height: inherit;color: rgb(174, 135, 250);word-wrap: inherit !important;word-break: inherit !important;">7.6</span>G&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span
        class=""
        style="font-size: inherit;line-height: inherit;color: rgb(174, 135, 250);word-wrap: inherit !important;word-break: inherit !important;">0B</span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span
        class=""
        style="font-size: inherit;line-height: inherit;color: rgb(174, 135, 250);word-wrap: inherit !important;word-break: inherit !important;">7.6</span>G<br></code></pre>
<p style="font-size: inherit;color: inherit;line-height: inherit;margin-top: 1.5em;margin-bottom: 1.5em;">
    通过free的结果，很容易看到当前总共内存多少，剩余可用内存多少等等。</p><h4
        style="color: inherit;line-height: inherit;margin-top: 1.5em;margin-bottom: 1.5em;font-weight: bold;font-size: 1.2em;">
    <span style="font-size: inherit;color: inherit;line-height: inherit;">使用-h参数</span></h4>
<p style="font-size: inherit;color: inherit;line-height: inherit;margin-top: 1.5em;margin-bottom: 1.5em;">
    不知道你是否注意到，我们在前面几个命令中，都使用了-h参数，它的作用是使得结果以人类可读的方式呈现，所以我们看到它呈现的单位是G,M等，如果不使用-h参数，可以自己尝试一下会是什么样的结果呈现。</p>
<h2 style="color: inherit;line-height: inherit;margin-top: 1.5em;margin-bottom: 1.5em;font-weight: bold;font-size: 1.4em;">
    <span style="font-size: inherit;color: inherit;line-height: inherit;">根据名称查找进程id</span></h2>
<p style="font-size: inherit;color: inherit;line-height: inherit;margin-top: 1.5em;margin-bottom: 1.5em;">
    想快速直接查找进程id，可以使用：</p>
<pre style="font-size: inherit;color: inherit;line-height: inherit;"><code class=""
                                                                           style="margin-right: 2px;margin-left: 2px;line-height: 18px;font-size: 14px;letter-spacing: 0px;font-family: Consolas, Inconsolata, Courier, monospace;border-radius: 0px;color: rgb(169, 183, 198);background: rgb(40, 43, 46);padding: 0.5em;display: block !important;word-wrap: normal !important;word-break: normal !important;overflow: auto !important;">$&nbsp;pgrep&nbsp;hello<br><span
        class=""
        style="font-size: inherit;line-height: inherit;color: rgb(174, 135, 250);word-wrap: inherit !important;word-break: inherit !important;">22692</span><br></code></pre>
<p style="font-size: inherit;color: inherit;line-height: inherit;margin-top: 1.5em;margin-bottom: 1.5em;">或者：</p>
<pre style="font-size: inherit;color: inherit;line-height: inherit;"><code class=""
                                                                           style="margin-right: 2px;margin-left: 2px;line-height: 18px;font-size: 14px;letter-spacing: 0px;font-family: Consolas, Inconsolata, Courier, monospace;border-radius: 0px;color: rgb(169, 183, 198);background: rgb(40, 43, 46);padding: 0.5em;display: block !important;word-wrap: normal !important;word-break: normal !important;overflow: auto !important;">$&nbsp;pidof&nbsp;hello<br><span
        class=""
        style="font-size: inherit;line-height: inherit;color: rgb(174, 135, 250);word-wrap: inherit !important;word-break: inherit !important;">22692</span><br></code></pre>
<p style="font-size: inherit;color: inherit;line-height: inherit;margin-top: 1.5em;margin-bottom: 1.5em;">
    其中，hello是进程名称。</p>
<h2 style="color: inherit;line-height: inherit;margin-top: 1.5em;margin-bottom: 1.5em;font-weight: bold;font-size: 1.4em;">
    <span style="font-size: inherit;color: inherit;line-height: inherit;">根据名称杀死进程</span></h2>
<p style="font-size: inherit;color: inherit;line-height: inherit;margin-top: 1.5em;margin-bottom: 1.5em;">
    一般我们可以使用kill　-9 pid方式杀死一个进程，但是这样就需要先找到这个进程的进程id，实际上我们也可以直接根据名称杀死进程，例如：</p>
<pre style="font-size: inherit;color: inherit;line-height: inherit;"><code class=""
                                                                           style="margin-right: 2px;margin-left: 2px;line-height: 18px;font-size: 14px;letter-spacing: 0px;font-family: Consolas, Inconsolata, Courier, monospace;border-radius: 0px;color: rgb(169, 183, 198);background: rgb(40, 43, 46);padding: 0.5em;display: block !important;word-wrap: normal !important;word-break: normal !important;overflow: auto !important;">$&nbsp;killall&nbsp;hello<br></code></pre>
<p style="font-size: inherit;color: inherit;line-height: inherit;margin-top: 1.5em;margin-bottom: 1.5em;">或者：</p>
<pre style="font-size: inherit;color: inherit;line-height: inherit;"><code class=""
                                                                           style="margin-right: 2px;margin-left: 2px;line-height: 18px;font-size: 14px;letter-spacing: 0px;font-family: Consolas, Inconsolata, Courier, monospace;border-radius: 0px;color: rgb(169, 183, 198);background: rgb(40, 43, 46);padding: 0.5em;display: block !important;word-wrap: normal !important;word-break: normal !important;overflow: auto !important;"><span
        class=""
        style="font-size: inherit;line-height: inherit;color: rgb(238, 220, 112);word-wrap: inherit !important;word-break: inherit !important;">$ pkill</span>&nbsp;hello<br></code></pre>
<h2 style="color: inherit;line-height: inherit;margin-top: 1.5em;margin-bottom: 1.5em;font-weight: bold;font-size: 1.4em;">
    <span style="font-size: inherit;color: inherit;line-height: inherit;">查看进程运行时间</span></h2>
<p style="font-size: inherit;color: inherit;line-height: inherit;margin-top: 1.5em;margin-bottom: 1.5em;">
    可以使用下面的命令查看进程已运行时间：</p>
<pre style="font-size: inherit;color: inherit;line-height: inherit;"><code class=""
                                                                           style="margin-right: 2px;margin-left: 2px;line-height: 18px;font-size: 14px;letter-spacing: 0px;font-family: Consolas, Inconsolata, Courier, monospace;border-radius: 0px;color: rgb(169, 183, 198);background: rgb(40, 43, 46);padding: 0.5em;display: block !important;word-wrap: normal !important;word-break: normal !important;overflow: auto !important;">$&nbsp;ps&nbsp;-p&nbsp;<span
        class=""
        style="font-size: inherit;line-height: inherit;color: rgb(174, 135, 250);word-wrap: inherit !important;word-break: inherit !important;">24525</span>&nbsp;-o&nbsp;lstart,etime&nbsp;<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;STARTED&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ELAPSED<br>Sat&nbsp;Mar&nbsp;<span
        class=""
        style="font-size: inherit;line-height: inherit;color: rgb(174, 135, 250);word-wrap: inherit !important;word-break: inherit !important;">23</span>&nbsp;<span
        class=""
        style="font-size: inherit;line-height: inherit;color: rgb(174, 135, 250);word-wrap: inherit !important;word-break: inherit !important;">20</span>:<span
        class=""
        style="font-size: inherit;line-height: inherit;color: rgb(174, 135, 250);word-wrap: inherit !important;word-break: inherit !important;">52</span>:<span
        class=""
        style="font-size: inherit;line-height: inherit;color: rgb(174, 135, 250);word-wrap: inherit !important;word-break: inherit !important;">08</span>&nbsp;<span
        class=""
        style="font-size: inherit;line-height: inherit;color: rgb(174, 135, 250);word-wrap: inherit !important;word-break: inherit !important;">2019</span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span
        class=""
        style="font-size: inherit;line-height: inherit;color: rgb(174, 135, 250);word-wrap: inherit !important;word-break: inherit !important;">02</span>:<span
        class=""
        style="font-size: inherit;line-height: inherit;color: rgb(174, 135, 250);word-wrap: inherit !important;word-break: inherit !important;">45</span><br></code></pre>
<p style="font-size: inherit;color: inherit;line-height: inherit;margin-top: 1.5em;margin-bottom: 1.5em;">
    其中24525是你要查看进程的进程id。</p>
<h2 style="color: inherit;line-height: inherit;margin-top: 1.5em;margin-bottom: 1.5em;font-weight: bold;font-size: 1.4em;">
    <span style="font-size: inherit;color: inherit;line-height: inherit;">快速目录切换</span></h2>
<ul style="" class="list-paddingleft-2">
    <li><p><span style="font-size: inherit;color: inherit;line-height: inherit;">cd -　回到上一个目录</span></p></li>
    <li><p><span style="font-size: inherit;color: inherit;line-height: inherit;">cd &nbsp;回到用户家目录</span></p></li>
</ul>
<h2 style="color: inherit;line-height: inherit;margin-top: 1.5em;margin-bottom: 1.5em;font-weight: bold;font-size: 1.4em;">
    <span style="font-size: inherit;color: inherit;line-height: inherit;">多条命令执行</span></h2>
<p style="font-size: inherit;color: inherit;line-height: inherit;margin-top: 1.5em;margin-bottom: 1.5em;">
    我们知道使用分号隔开可以执行多条命令，例如：</p>
<pre style="font-size: inherit;color: inherit;line-height: inherit;"><code class=""
                                                                           style="margin-right: 2px;margin-left: 2px;line-height: 18px;font-size: 14px;letter-spacing: 0px;font-family: Consolas, Inconsolata, Courier, monospace;border-radius: 0px;color: rgb(169, 183, 198);background: rgb(40, 43, 46);padding: 0.5em;display: block !important;word-wrap: normal !important;word-break: normal !important;overflow: auto !important;"><span
        class=""
        style="font-size: inherit;line-height: inherit;color: rgb(91, 218, 237);word-wrap: inherit !important;word-break: inherit !important;">$</span><span
        class=""
        style="font-size: inherit;color: inherit;line-height: inherit;word-wrap: inherit !important;word-break: inherit !important;">&nbsp;<span
        class=""
        style="font-size: inherit;line-height: inherit;color: rgb(248, 35, 117);word-wrap: inherit !important;word-break: inherit !important;">cd</span>&nbsp;/temp/<span
        class=""
        style="font-size: inherit;line-height: inherit;color: rgb(248, 35, 117);word-wrap: inherit !important;word-break: inherit !important;">log</span>/;rm&nbsp;-rf&nbsp;*</span><br></code></pre>
<p style="font-size: inherit;color: inherit;line-height: inherit;margin-top: 1.5em;margin-bottom: 1.5em;">
    但是如果当前目录是/目录，并且/temp/log目录不存在，那么就会发生激动人心的一幕：</p>
<pre style="font-size: inherit;color: inherit;line-height: inherit;"><code class=""
                                                                           style="margin-right: 2px;margin-left: 2px;line-height: 18px;font-size: 14px;letter-spacing: 0px;font-family: Consolas, Inconsolata, Courier, monospace;border-radius: 0px;color: rgb(169, 183, 198);background: rgb(40, 43, 46);padding: 0.5em;display: block !important;word-wrap: normal !important;word-break: normal !important;overflow: auto !important;">bash:&nbsp;<span
        class=""
        style="font-size: inherit;line-height: inherit;color: rgb(248, 35, 117);word-wrap: inherit !important;word-break: inherit !important;">cd</span>:&nbsp;/temp/<span
        class=""
        style="font-size: inherit;line-height: inherit;color: rgb(248, 35, 117);word-wrap: inherit !important;word-break: inherit !important;">log</span>:&nbsp;No&nbsp;such&nbsp;file&nbsp;or&nbsp;directory<br>（突然陷入沉默）<br></code></pre>
<p style="font-size: inherit;color: inherit;line-height: inherit;margin-top: 1.5em;margin-bottom: 1.5em;">
    因为;可以执行多条命令，但是不会因为前一条命令失败，而导致后面的不会执行，因此，cd执行失败后，仍然会继续执行rm -rf *，由于处于/目录下，结果可想而知。<br>所以你还以为这种事故是对rf -rf
    *的力量一无所知的情况下产生的吗？</p>
<p style="font-size: inherit;color: inherit;line-height: inherit;margin-top: 1.5em;margin-bottom: 1.5em;">
    如果解决呢？很简单，使用&amp;&amp;，例如:</p>
<pre style="font-size: inherit;color: inherit;line-height: inherit;"><code class=""
                                                                           style="margin-right: 2px;margin-left: 2px;line-height: 18px;font-size: 14px;letter-spacing: 0px;font-family: Consolas, Inconsolata, Courier, monospace;border-radius: 0px;color: rgb(169, 183, 198);background: rgb(40, 43, 46);padding: 0.5em;display: block !important;word-wrap: normal !important;word-break: normal !important;overflow: auto !important;"><span
        class=""
        style="font-size: inherit;line-height: inherit;color: rgb(91, 218, 237);word-wrap: inherit !important;word-break: inherit !important;">$</span><span
        class=""
        style="font-size: inherit;color: inherit;line-height: inherit;word-wrap: inherit !important;word-break: inherit !important;">&nbsp;<span
        class=""
        style="font-size: inherit;line-height: inherit;color: rgb(248, 35, 117);word-wrap: inherit !important;word-break: inherit !important;">cd</span>&nbsp;/temp/<span
        class=""
        style="font-size: inherit;line-height: inherit;color: rgb(248, 35, 117);word-wrap: inherit !important;word-break: inherit !important;">log</span>/&amp;&amp;rm&nbsp;-rf&nbsp;*</span><br></code></pre>
<p style="font-size: inherit;color: inherit;line-height: inherit;margin-top: 1.5em;margin-bottom: 1.5em;">
    这样就会确保前一条命令执行成功，才会执行后面一条。</p>
<h2 style="color: inherit;line-height: inherit;margin-top: 1.5em;margin-bottom: 1.5em;font-weight: bold;font-size: 1.4em;">
    <span style="font-size: inherit;color: inherit;line-height: inherit;">查看压缩日志文件</span></h2>
<p style="font-size: inherit;color: inherit;line-height: inherit;margin-top: 1.5em;margin-bottom: 1.5em;">
    有时候日志文件是压缩的，那么能不能偷懒一下，不解压查看呢？当然可以啦。<br>例如：</p>
<pre style="font-size: inherit;color: inherit;line-height: inherit;"><code class=""
                                                                           style="margin-right: 2px;margin-left: 2px;line-height: 18px;font-size: 14px;letter-spacing: 0px;font-family: Consolas, Inconsolata, Courier, monospace;border-radius: 0px;color: rgb(169, 183, 198);background: rgb(40, 43, 46);padding: 0.5em;display: block !important;word-wrap: normal !important;word-break: normal !important;overflow: auto !important;">$&nbsp;zcat&nbsp;test.gz<br><span
        class=""
        style="font-size: inherit;line-height: inherit;color: rgb(248, 35, 117);word-wrap: inherit !important;word-break: inherit !important;">test</span>&nbsp;<span
        class=""
        style="font-size: inherit;line-height: inherit;color: rgb(248, 35, 117);word-wrap: inherit !important;word-break: inherit !important;">log</span><br></code></pre>
<p style="font-size: inherit;color: inherit;line-height: inherit;margin-top: 1.5em;margin-bottom: 1.5em;">或者：</p>
<pre style="font-size: inherit;color: inherit;line-height: inherit;"><code class=""
                                                                           style="margin-right: 2px;margin-left: 2px;line-height: 18px;font-size: 14px;letter-spacing: 0px;font-family: Consolas, Inconsolata, Courier, monospace;border-radius: 0px;color: rgb(169, 183, 198);background: rgb(40, 43, 46);padding: 0.5em;display: block !important;word-wrap: normal !important;word-break: normal !important;overflow: auto !important;">$&nbsp;zless&nbsp;test.gz<br><span
        class=""
        style="font-size: inherit;line-height: inherit;color: rgb(248, 35, 117);word-wrap: inherit !important;word-break: inherit !important;">test</span>&nbsp;<span
        class=""
        style="font-size: inherit;line-height: inherit;color: rgb(248, 35, 117);word-wrap: inherit !important;word-break: inherit !important;">log</span></code></pre>
<h2 style="color: inherit;line-height: inherit;margin-top: 1.5em;margin-bottom: 1.5em;font-weight: bold;font-size: 1.4em;">
    <span style="font-size: inherit;color: inherit;line-height: inherit;">清空文件内容</span></h2>
<p style="font-size: inherit;color: inherit;line-height: inherit;margin-top: 1.5em;margin-bottom: 1.5em;">
    比如有一个大文件，你想快速删除，或者不想删除，但是想清空内容：</p>
<pre style="font-size: inherit;color: inherit;line-height: inherit;"><code class=""
                                                                           style="margin-right: 2px;margin-left: 2px;line-height: 18px;font-size: 14px;letter-spacing: 0px;font-family: Consolas, Inconsolata, Courier, monospace;border-radius: 0px;color: rgb(169, 183, 198);background: rgb(40, 43, 46);padding: 0.5em;display: block !important;word-wrap: normal !important;word-break: normal !important;overflow: auto !important;"><span
        class=""
        style="font-size: inherit;line-height: inherit;color: rgb(91, 218, 237);word-wrap: inherit !important;word-break: inherit !important;">&gt;</span><span
        class=""
        style="font-size: inherit;color: inherit;line-height: inherit;word-wrap: inherit !important;word-break: inherit !important;">filename</span><br></code></pre>
<h2 style="color: inherit;line-height: inherit;margin-top: 1.5em;margin-bottom: 1.5em;font-weight: bold;font-size: 1.4em;">
    <span style="font-size: inherit;color: inherit;line-height: inherit;">将日志同时记录文件并打印到控制台</span></h2>
<p style="font-size: inherit;color: inherit;line-height: inherit;margin-top: 1.5em;margin-bottom: 1.5em;">
    在执行shell脚本，常常会将日志重定向，但是这样的话，控制台就没有打印了，如何使得既能记录日志文件，又能将日志输出到控制台呢？</p>
<pre style="font-size: inherit;color: inherit;line-height: inherit;"><code class=""
                                                                           style="margin-right: 2px;margin-left: 2px;line-height: 18px;font-size: 14px;letter-spacing: 0px;font-family: Consolas, Inconsolata, Courier, monospace;border-radius: 0px;color: rgb(169, 183, 198);background: rgb(40, 43, 46);padding: 0.5em;display: block !important;word-wrap: normal !important;word-break: normal !important;overflow: auto !important;">$&nbsp;./test.sh&nbsp;|tee&nbsp;test.<span
        class=""
        style="font-size: inherit;line-height: inherit;color: rgb(248, 35, 117);word-wrap: inherit !important;word-break: inherit !important;">log</span><br></code></pre>
<h2 style="color: inherit;line-height: inherit;margin-top: 1.5em;margin-bottom: 1.5em;font-weight: bold;font-size: 1.4em;">
    <span style="font-size: inherit;color: inherit;line-height: inherit;">终止并恢复进程执行</span></h2>
<p style="font-size: inherit;color: inherit;line-height: inherit;margin-top: 1.5em;margin-bottom: 1.5em;">我们使用ctrl+z
    暂停一个进程的执行，也可以使用fg恢复执行。例如我们使用</p>
<pre style="font-size: inherit;color: inherit;line-height: inherit;"><code class=""
                                                                           style="margin-right: 2px;margin-left: 2px;line-height: 18px;font-size: 14px;letter-spacing: 0px;font-family: Consolas, Inconsolata, Courier, monospace;border-radius: 0px;color: rgb(169, 183, 198);background: rgb(40, 43, 46);padding: 0.5em;display: block !important;word-wrap: normal !important;word-break: normal !important;overflow: auto !important;">$&nbsp;cat&nbsp;filename<br></code></pre>
<p style="font-size: inherit;color: inherit;line-height: inherit;margin-top: 1.5em;margin-bottom: 1.5em;">
    当我们发现文件内容可能很多时，使用ctrl+z暂停程序，而如果又想要从刚才的地方继续执行，则只需要使用fg命令即可恢复执行。或者使用bg使得进程继续在后台执行。</p>
<h2 style="color: inherit;line-height: inherit;margin-top: 1.5em;margin-bottom: 1.5em;font-weight: bold;font-size: 1.4em;">
    <span style="font-size: inherit;color: inherit;line-height: inherit;">计算程序运行时间</span></h2>
<p style="font-size: inherit;color: inherit;line-height: inherit;margin-top: 1.5em;margin-bottom: 1.5em;">
    我们可能会进程写一些小程序，并且想要知道它的运行时间，实际上我们可以很好的利用time命令帮我们计算，例如：</p>
<pre style="font-size: inherit;color: inherit;line-height: inherit;"><code class=""
                                                                           style="margin-right: 2px;margin-left: 2px;line-height: 18px;font-size: 14px;letter-spacing: 0px;font-family: Consolas, Inconsolata, Courier, monospace;border-radius: 0px;color: rgb(169, 183, 198);background: rgb(40, 43, 46);padding: 0.5em;display: block !important;word-wrap: normal !important;word-break: normal !important;overflow: auto !important;">$&nbsp;time&nbsp;./fibo&nbsp;<span
        class=""
        style="font-size: inherit;line-height: inherit;color: rgb(174, 135, 250);word-wrap: inherit !important;word-break: inherit !important;">30</span><br>the&nbsp;<span
        class=""
        style="font-size: inherit;line-height: inherit;color: rgb(174, 135, 250);word-wrap: inherit !important;word-break: inherit !important;">30</span>&nbsp;result&nbsp;is&nbsp;<span
        class=""
        style="font-size: inherit;line-height: inherit;color: rgb(174, 135, 250);word-wrap: inherit !important;word-break: inherit !important;">832040</span><br><br><span
        class=""
        style="font-size: inherit;line-height: inherit;color: rgb(248, 35, 117);word-wrap: inherit !important;word-break: inherit !important;">real</span>&nbsp;&nbsp;&nbsp;&nbsp;<span
        class=""
        style="font-size: inherit;line-height: inherit;color: rgb(174, 135, 250);word-wrap: inherit !important;word-break: inherit !important;">0</span>m0<span
        class=""
        style="font-size: inherit;line-height: inherit;color: rgb(174, 135, 250);word-wrap: inherit !important;word-break: inherit !important;">.088s</span><br>user&nbsp;&nbsp;&nbsp;&nbsp;<span
        class=""
        style="font-size: inherit;line-height: inherit;color: rgb(174, 135, 250);word-wrap: inherit !important;word-break: inherit !important;">0</span>m0<span
        class=""
        style="font-size: inherit;line-height: inherit;color: rgb(174, 135, 250);word-wrap: inherit !important;word-break: inherit !important;">.084s</span><br>sys&nbsp;&nbsp;&nbsp;&nbsp;<span
        class=""
        style="font-size: inherit;line-height: inherit;color: rgb(174, 135, 250);word-wrap: inherit !important;word-break: inherit !important;">0</span>m0<span
        class=""
        style="font-size: inherit;line-height: inherit;color: rgb(174, 135, 250);word-wrap: inherit !important;word-break: inherit !important;">.004s</span><br></code></pre>
<p style="font-size: inherit;color: inherit;line-height: inherit;margin-top: 1.5em;margin-bottom: 1.5em;">
    它会显示系统时间，用户时间以及实际使用的总时间。</p>
<h2 style="color: inherit;line-height: inherit;margin-top: 1.5em;margin-bottom: 1.5em;font-weight: bold;font-size: 1.4em;">
    <span style="font-size: inherit;color: inherit;line-height: inherit;">查看内存占用前10的进程</span></h2>
<pre style="font-size: inherit;color: inherit;line-height: inherit;"><code class=""
                                                                           style="margin-right: 2px;margin-left: 2px;line-height: 18px;font-size: 14px;letter-spacing: 0px;font-family: Consolas, Inconsolata, Courier, monospace;border-radius: 0px;color: rgb(169, 183, 198);background: rgb(40, 43, 46);padding: 0.5em;display: block !important;word-wrap: normal !important;word-break: normal !important;overflow: auto !important;"><span
        class=""
        style="font-size: inherit;line-height: inherit;color: rgb(238, 220, 112);word-wrap: inherit !important;word-break: inherit !important;">$ ps</span>&nbsp;-aux|sort&nbsp;-k4nr&nbsp;|head&nbsp;-n&nbsp;<span
        class=""
        style="font-size: inherit;line-height: inherit;color: rgb(174, 135, 250);word-wrap: inherit !important;word-break: inherit !important;">10</span><br></code></pre>
<p style="font-size: inherit;color: inherit;line-height: inherit;margin-top: 1.5em;margin-bottom: 1.5em;">
    这里综合使用了ps，sort，head命令。</p>
<h2 style="color: inherit;line-height: inherit;margin-top: 1.5em;margin-bottom: 1.5em;font-weight: bold;font-size: 1.4em;">
    <span style="font-size: inherit;color: inherit;line-height: inherit;">快速查找你需要的命令</span></h2>
<p style="font-size: inherit;color: inherit;line-height: inherit;margin-top: 1.5em;margin-bottom: 1.5em;">
    我们都知道man可以查看命令的帮助手册，但是如果我们想要某个功能却不知道使用哪个命令呢？别着急，还是可以使用man：</p>
<pre style="font-size: inherit;color: inherit;line-height: inherit;"><code class=""
                                                                           style="margin-right: 2px;margin-left: 2px;line-height: 18px;font-size: 14px;letter-spacing: 0px;font-family: Consolas, Inconsolata, Courier, monospace;border-radius: 0px;color: rgb(169, 183, 198);background: rgb(40, 43, 46);padding: 0.5em;display: block !important;word-wrap: normal !important;word-break: normal !important;overflow: auto !important;">$&nbsp;man&nbsp;-k&nbsp;<span
        class=""
        style="font-size: inherit;line-height: inherit;color: rgb(238, 220, 112);word-wrap: inherit !important;word-break: inherit !important;">"copy&nbsp;files"</span><br>cp&nbsp;(<span
        class=""
        style="font-size: inherit;line-height: inherit;color: rgb(174, 135, 250);word-wrap: inherit !important;word-break: inherit !important;">1</span>)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;copy&nbsp;files&nbsp;<span
        class=""
        style="font-size: inherit;line-height: inherit;color: rgb(248, 35, 117);word-wrap: inherit !important;word-break: inherit !important;">and</span>&nbsp;directories<br>cpio&nbsp;(<span
        class=""
        style="font-size: inherit;line-height: inherit;color: rgb(174, 135, 250);word-wrap: inherit !important;word-break: inherit !important;">1</span>)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;copy&nbsp;files&nbsp;<span
        class=""
        style="font-size: inherit;line-height: inherit;color: rgb(248, 35, 117);word-wrap: inherit !important;word-break: inherit !important;">to</span>&nbsp;<span
        class=""
        style="font-size: inherit;line-height: inherit;color: rgb(248, 35, 117);word-wrap: inherit !important;word-break: inherit !important;">and</span>&nbsp;<span
        class=""
        style="font-size: inherit;line-height: inherit;color: rgb(248, 35, 117);word-wrap: inherit !important;word-break: inherit !important;">from</span>&nbsp;archives<br>git-checkout-index&nbsp;(<span
        class=""
        style="font-size: inherit;line-height: inherit;color: rgb(174, 135, 250);word-wrap: inherit !important;word-break: inherit !important;">1</span>)&nbsp;-&nbsp;Copy&nbsp;files&nbsp;<span
        class=""
        style="font-size: inherit;line-height: inherit;color: rgb(248, 35, 117);word-wrap: inherit !important;word-break: inherit !important;">from</span>&nbsp;the&nbsp;index&nbsp;<span
        class=""
        style="font-size: inherit;line-height: inherit;color: rgb(248, 35, 117);word-wrap: inherit !important;word-break: inherit !important;">to</span>&nbsp;the&nbsp;working&nbsp;tree<br>gvfs-copy&nbsp;(<span
        class=""
        style="font-size: inherit;line-height: inherit;color: rgb(174, 135, 250);word-wrap: inherit !important;word-break: inherit !important;">1</span>)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;Copy&nbsp;files<br>gvfs-move&nbsp;(<span
        class=""
        style="font-size: inherit;line-height: inherit;color: rgb(174, 135, 250);word-wrap: inherit !important;word-break: inherit !important;">1</span>)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;Copy&nbsp;files<br>install&nbsp;(<span
        class=""
        style="font-size: inherit;line-height: inherit;color: rgb(174, 135, 250);word-wrap: inherit !important;word-break: inherit !important;">1</span>)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;copy&nbsp;files&nbsp;<span
        class=""
        style="font-size: inherit;line-height: inherit;color: rgb(248, 35, 117);word-wrap: inherit !important;word-break: inherit !important;">and</span>&nbsp;<span
        class=""
        style="font-size: inherit;line-height: inherit;color: rgb(248, 35, 117);word-wrap: inherit !important;word-break: inherit !important;">set</span>&nbsp;attributes<br></code></pre>
<p style="font-size: inherit;color: inherit;line-height: inherit;margin-top: 1.5em;margin-bottom: 1.5em;">
    使用-k参数，使得与copy files相关的帮助手册都显示出来了。</p>
<h2 style="color: inherit;line-height: inherit;margin-top: 1.5em;margin-bottom: 1.5em;font-weight: bold;font-size: 1.4em;">
    <span style="font-size: inherit;color: inherit;line-height: inherit;">命令行下的复制粘贴</span></h2>
<p style="font-size: inherit;color: inherit;line-height: inherit;margin-top: 1.5em;margin-bottom: 1.5em;">
    我们知道，在命令行下，复制不能再是ctrl + c了，因为它表示终止当前进程，而控制台下的复制粘贴需要使用下面的快捷键：</p>
<ul style="" class="list-paddingleft-2">
    <li><p><span style="font-size: inherit;color: inherit;line-height: inherit;">ctrl + &nbsp;insert</span></p></li>
    <li><p><span style="font-size: inherit;color: inherit;line-height: inherit;">shift + insert</span></p></li>
</ul>
<h2 style="color: inherit;line-height: inherit;margin-top: 1.5em;margin-bottom: 1.5em;font-weight: bold;font-size: 1.4em;">
    <span style="font-size: inherit;color: inherit;line-height: inherit;">搜索包含某个字符串的文件</span></h2>
<p style="font-size: inherit;color: inherit;line-height: inherit;margin-top: 1.5em;margin-bottom: 1.5em;">
    例如，要在当前目录下查找包含test字符串的文件：</p>
<pre style="font-size: inherit;color: inherit;line-height: inherit;"><code class=""
                                                                           style="margin-right: 2px;margin-left: 2px;line-height: 18px;font-size: 14px;letter-spacing: 0px;font-family: Consolas, Inconsolata, Courier, monospace;border-radius: 0px;color: rgb(169, 183, 198);background: rgb(40, 43, 46);padding: 0.5em;display: block !important;word-wrap: normal !important;word-break: normal !important;overflow: auto !important;">$&nbsp;grep&nbsp;-rn&nbsp;<span
        class=""
        style="font-size: inherit;line-height: inherit;color: rgb(238, 220, 112);word-wrap: inherit !important;word-break: inherit !important;">"test"</span><br>test2.<span
        class=""
        style="font-size: inherit;line-height: inherit;color: rgb(174, 135, 250);word-wrap: inherit !important;word-break: inherit !important;">txt:</span><span
        class=""
        style="font-size: inherit;line-height: inherit;color: rgb(174, 135, 250);word-wrap: inherit !important;word-break: inherit !important;">1</span><span
        class=""
        style="font-size: inherit;line-height: inherit;color: rgb(174, 135, 250);word-wrap: inherit !important;word-break: inherit !important;">:test</span><br></code></pre>
<p style="font-size: inherit;color: inherit;line-height: inherit;margin-top: 1.5em;margin-bottom: 1.5em;">
    它便可以找到该字符串在哪个文件的第几行。</p>
<h2 style="color: inherit;line-height: inherit;margin-top: 1.5em;margin-bottom: 1.5em;font-weight: bold;font-size: 1.4em;">
    <span style="font-size: inherit;color: inherit;line-height: inherit;">屏幕冻结</span></h2>
<p style="font-size: inherit;color: inherit;line-height: inherit;margin-top: 1.5em;margin-bottom: 1.5em;">
    程序运行时，终端可能输出大量的日志，你想简单查看一下，又不想记录日志文件，此时可以使用ctrl+s键，冻结屏幕，使得日志不再继续输出，而如果想要恢复，可使用ctrl+q退出冻结。</p>
<h2 style="color: inherit;line-height: inherit;margin-top: 1.5em;margin-bottom: 1.5em;font-weight: bold;font-size: 1.4em;">
    <span style="font-size: inherit;color: inherit;line-height: inherit;">无编辑器情况下编辑文本文件</span></h2>
<p style="font-size: inherit;color: inherit;line-height: inherit;margin-top: 1.5em;margin-bottom: 1.5em;">
    如果在某些系统上连基本的vi编辑器都没有，那么可以使用下面的方式进行编辑内容：</p>
<pre style="font-size: inherit;color: inherit;line-height: inherit;"><code class=""
                                                                           style="margin-right: 2px;margin-left: 2px;line-height: 18px;font-size: 14px;letter-spacing: 0px;font-family: Consolas, Inconsolata, Courier, monospace;border-radius: 0px;color: rgb(169, 183, 198);background: rgb(40, 43, 46);padding: 0.5em;display: block !important;word-wrap: normal !important;word-break: normal !important;overflow: auto !important;">$&nbsp;cat&nbsp;&gt;file.txt<br>some&nbsp;words<br>(ctrl+d)<br></code></pre>
<p style="font-size: inherit;color: inherit;line-height: inherit;margin-top: 1.5em;margin-bottom: 1.5em;">
    编辑完成后，ctrl+d即可保存。</p>
<h2 style="color: inherit;line-height: inherit;margin-top: 1.5em;margin-bottom: 1.5em;font-weight: bold;font-size: 1.4em;">
    <span style="font-size: inherit;color: inherit;line-height: inherit;">查看elf文件</span></h2><h4
        style="color: inherit;line-height: inherit;margin-top: 1.5em;margin-bottom: 1.5em;font-weight: bold;font-size: 1.2em;">
    <span style="font-size: inherit;color: inherit;line-height: inherit;">查看elf文件头信息</span></h4>
<p style="font-size: inherit;color: inherit;line-height: inherit;margin-top: 1.5em;margin-bottom: 1.5em;">例如：</p>
<pre style="font-size: inherit;color: inherit;line-height: inherit;"><code class=""
                                                                           style="margin-right: 2px;margin-left: 2px;line-height: 18px;font-size: 14px;letter-spacing: 0px;font-family: Consolas, Inconsolata, Courier, monospace;border-radius: 0px;color: rgb(169, 183, 198);background: rgb(40, 43, 46);padding: 0.5em;display: block !important;word-wrap: normal !important;word-break: normal !important;overflow: auto !important;">$&nbsp;readelf&nbsp;-h&nbsp;filename<br></code></pre>
<p style="font-size: inherit;color: inherit;line-height: inherit;margin-top: 1.5em;margin-bottom: 1.5em;">
    我们在显示结果中，可以看到运行的平台，elf文件类型，大小端情况等。</p><h4
        style="color: inherit;line-height: inherit;margin-top: 1.5em;margin-bottom: 1.5em;font-weight: bold;font-size: 1.2em;">
    <span style="font-size: inherit;color: inherit;line-height: inherit;">查看库中是否包含某个接口</span></h4>
<pre style="font-size: inherit;color: inherit;line-height: inherit;"><code class=""
                                                                           style="margin-right: 2px;margin-left: 2px;line-height: 18px;font-size: 14px;letter-spacing: 0px;font-family: Consolas, Inconsolata, Courier, monospace;border-radius: 0px;color: rgb(169, 183, 198);background: rgb(40, 43, 46);padding: 0.5em;display: block !important;word-wrap: normal !important;word-break: normal !important;overflow: auto !important;">$ nm&nbsp;filename&nbsp;|grep&nbsp;<span
        class=""
        style="font-size: inherit;color: inherit;line-height: inherit;word-wrap: inherit !important;word-break: inherit !important;"><span
        class=""
        style="font-size: inherit;line-height: inherit;color: rgb(248, 35, 117);word-wrap: inherit !important;word-break: inherit !important;">interface</span></span><br></code></pre>
<p style="font-size: inherit;color: inherit;line-height: inherit;margin-top: 1.5em;margin-bottom: 1.5em;">
    这里是从文件filename中查看是否包含interface接口，前提是该文件包含符号表。<br></p>
<h2 style="color: inherit;line-height: inherit;margin-top: 1.5em;margin-bottom: 1.5em;font-weight: bold;font-size: 1.4em;">
    <span style="font-size: inherit;color: inherit;line-height: inherit;">总结</span></h2>
<p style="font-size: inherit;color: inherit;line-height: inherit;margin-top: 1.5em;margin-bottom: 1.5em;">
    本文所提到的内容建议自己上机操作，体验效果。本文总结了一些常用的linux小技巧，你还有哪些linux小技巧？欢迎留言分享。</p>
<section class="" mpa-from-tpl="t"><p><br></p>
    <section class="" mpa-from-tpl="t" style="color: rgb(51, 51, 51);font-size: 17px;text-align: justify;">

<p style="clear: both;min-height: 1em;"><br mpa-from-tpl="t"></p></section>

