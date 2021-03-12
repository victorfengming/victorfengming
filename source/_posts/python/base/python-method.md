---
title: "Python中的魔术方法"
cover: "/img/lynk/35.jpg"
date:       2018-08-29
tags:
	- Python
	- background
---












### 魔术方法
<hr>
<blockquote>
<p>&#x9B54;&#x672F;&#x65B9;&#x6CD5;&#x5C31;&#x662F;&#x4E00;&#x4E2A;&#x7C7B;/&#x5BF9;&#x8C61;&#x4E2D;&#x7684;&#x65B9;&#x6CD5;&#xFF0C;&#x548C;&#x666E;&#x901A;&#x65B9;&#x6CD5;&#x552F;&#x4E00;&#x7684;&#x4E0D;&#x540C;&#x65F6;&#xFF0C;&#x666E;&#x901A;&#x65B9;&#x6CD5;&#x9700;&#x8981;&#x8C03;&#x7528;&#xFF01;&#x800C;&#x9B54;&#x672F;&#x65B9;&#x6CD5;&#x662F;&#x5728;&#x7279;&#x5B9A;&#x65F6;&#x523B;&#x81EA;&#x52A8;&#x89E6;&#x53D1;&#x3002;</p>
</blockquote>
<h4 id="1init">1.__init__</h4>
<pre><code>&#x521D;&#x59CB;&#x5316;&#x9B54;&#x672F;&#x65B9;&#x6CD5;
&#x89E6;&#x53D1;&#x65F6;&#x673A;&#xFF1A;&#x521D;&#x59CB;&#x5316;&#x5BF9;&#x8C61;&#x65F6;&#x89E6;&#x53D1;&#xFF08;&#x4E0D;&#x662F;&#x5B9E;&#x4F8B;&#x5316;&#x89E6;&#x53D1;&#xFF0C;&#x4F46;&#x662F;&#x548C;&#x5B9E;&#x4F8B;&#x5316;&#x5728;&#x4E00;&#x4E2A;&#x64CD;&#x4F5C;&#x4E2D;&#xFF09;
&#x53C2;&#x6570;&#xFF1A;&#x81F3;&#x5C11;&#x6709;&#x4E00;&#x4E2A;self&#xFF0C;&#x63A5;&#x6536;&#x5BF9;&#x8C61;
&#x8FD4;&#x56DE;&#x503C;&#xFF1A;&#x65E0;
&#x4F5C;&#x7528;&#xFF1A;&#x521D;&#x59CB;&#x5316;&#x5BF9;&#x8C61;&#x7684;&#x6210;&#x5458;
&#x6CE8;&#x610F;&#xFF1A;&#x4F7F;&#x7528;&#x8BE5;&#x65B9;&#x5F0F;&#x521D;&#x59CB;&#x5316;&#x7684;&#x6210;&#x5458;&#x90FD;&#x662F;&#x76F4;&#x63A5;&#x5199;&#x5165;&#x5BF9;&#x8C61;&#x5F53;&#x4E2D;&#xFF0C;&#x7C7B;&#x4E2D;&#x65E0;&#x6CD5;&#x5177;&#x6709;
</code></pre><h4 id="2new">2.__new__</h4>
<pre><code>&#x5B9E;&#x4F8B;&#x5316;&#x9B54;&#x672F;&#x65B9;&#x6CD5;
&#x89E6;&#x53D1;&#x65F6;&#x673A;&#xFF1A; &#x5728;&#x5B9E;&#x4F8B;&#x5316;&#x5BF9;&#x65F6;&#x89E6;&#x53D1;
&#x53C2;&#x6570;&#xFF1A;&#x81F3;&#x5C11;&#x4E00;&#x4E2A;cls &#x63A5;&#x6536;&#x5F53;&#x524D;&#x7C7B;
&#x8FD4;&#x56DE;&#x503C;&#xFF1A;&#x5FC5;&#x987B;&#x8FD4;&#x56DE;&#x4E00;&#x4E2A;&#x5BF9;&#x8C61;&#x5B9E;&#x4F8B;
&#x4F5C;&#x7528;&#xFF1A;&#x5B9E;&#x4F8B;&#x5316;&#x5BF9;&#x8C61;
&#x6CE8;&#x610F;&#xFF1A;&#x5B9E;&#x4F8B;&#x5316;&#x5BF9;&#x8C61;&#x662F;Object&#x7C7B;&#x5E95;&#x5C42;&#x5B9E;&#x73B0;&#xFF0C;&#x5176;&#x4ED6;&#x7C7B;&#x7EE7;&#x627F;&#x4E86;Object&#x7684;__new__&#x624D;&#x80FD;&#x591F;&#x5B9E;&#x73B0;&#x5B9E;&#x4F8B;&#x5316;&#x5BF9;&#x8C61;&#x3002;
&#x6CA1;&#x4E8B;&#x522B;&#x78B0;&#x8FD9;&#x4E2A;&#x9B54;&#x672F;&#x65B9;&#x6CD5;&#xFF0C;&#x5148;&#x89E6;&#x53D1;__new__&#x624D;&#x4F1A;&#x89E6;&#x53D1;__init__ 
</code></pre><h4 id="3del">3.__del__</h4>
<pre><code>&#x6790;&#x6784;&#x9B54;&#x672F;&#x65B9;&#x6CD5;
&#x89E6;&#x53D1;&#x65F6;&#x673A;&#xFF1A;&#x5F53;&#x5BF9;&#x8C61;&#x6CA1;&#x6709;&#x7528;&#xFF08;&#x6CA1;&#x6709;&#x4EFB;&#x4F55;&#x53D8;&#x91CF;&#x5F15;&#x7528;&#xFF09;&#x7684;&#x65F6;&#x5019;&#x88AB;&#x89E6;&#x53D1;
&#x53C2;&#x6570;&#xFF1A;&#x4E00;&#x4E2A;self &#x7ED3;&#x5A5A;&#x641C;&#x5BF9;&#x8C61;
&#x8FD4;&#x56DE;&#x503C;&#xFF1A;&#x65E0;
&#x4F5C;&#x7528;&#xFF1A;&#x4F7F;&#x7528;&#x5B8C;&#x5BF9;&#x8C61;&#x662F;&#x56DE;&#x6536;&#x8D44;&#x6E90;
&#x6CE8;&#x610F;&#xFF1A;del&#x4E0D;&#x4E00;&#x5B9A;&#x4F1A;&#x89E6;&#x53D1;&#x5F53;&#x524D;&#x65B9;&#x6CD5;&#xFF0C;&#x53EA;&#x6709;&#x5F53;&#x524D;&#x5BF9;&#x8C61;&#x6CA1;&#x6709;&#x4EFB;&#x4F55;&#x53D8;&#x91CF;&#x63A5;&#x6536;&#x65F6;&#x624D;&#x4F1A;&#x89E6;&#x53D1;
</code></pre><h4 id="4call">4.__call__</h4>
<pre><code>&#x8C03;&#x7528;&#x5BF9;&#x8C61;&#x7684;&#x9B54;&#x672F;&#x65B9;&#x6CD5;
&#x89E6;&#x53D1;&#x65F6;&#x673A;:&#x5C06;&#x5BF9;&#x8C61;&#x5F53;&#x4F5C;&#x51FD;&#x6570;&#x8C03;&#x7528;&#x65F6;&#x89E6;&#x53D1; &#x5BF9;&#x8C61;()
&#x53C2;&#x6570;:&#x81F3;&#x5C11;&#x4E00;&#x4E2A;self&#x63A5;&#x6536;&#x5BF9;&#x8C61;&#xFF0C;&#x5176;&#x4F59;&#x6839;&#x636E;&#x8C03;&#x7528;&#x65F6;&#x53C2;&#x6570;&#x51B3;&#x5B9A;
&#x8FD4;&#x56DE;&#x503C;&#xFF1A;&#x6839;&#x636E;&#x60C5;&#x51B5;&#x800C;&#x5B9A;
&#x4F5C;&#x7528;&#xFF1A;&#x53EF;&#x4EE5;&#x5C06;&#x590D;&#x6742;&#x7684;&#x6B65;&#x9AA4;&#x8FDB;&#x884C;&#x5408;&#x5E76;&#x64CD;&#x4F5C;&#xFF0C;&#x51CF;&#x5C11;&#x8C03;&#x7528;&#x7684;&#x6B65;&#x9AA4;&#xFF0C;&#x65B9;&#x4FBF;&#x4F7F;&#x7528;
&#x6CE8;&#x610F;&#xFF1A;&#x65E0;
</code></pre><h4 id="5len">5.__len__</h4>
<pre><code>&#x89E6;&#x53D1;&#x65F6;&#x673A;&#xFF1A;&#x4F7F;&#x7528;len(&#x5BF9;&#x8C61;) &#x7684;&#x65F6;&#x5019;&#x89E6;&#x53D1;
&#x53C2;&#x6570;&#xFF1A;&#x4E00;&#x4E2A;&#x53C2;&#x6570;self
&#x8FD4;&#x56DE;&#x503C;&#xFF1A;&#x5FC5;&#x987B;&#x662F;&#x4E00;&#x4E2A;&#x6574;&#x578B;
&#x4F5C;&#x7528;&#xFF1A;&#x53EF;&#x4EE5;&#x8BBE;&#x7F6E;&#x4E3A;&#x68C0;&#x6D4B;&#x5BF9;&#x8C61;&#x6210;&#x5458;&#x4E2A;&#x6570;&#xFF0C;&#x4F46;&#x662F;&#x4E5F;&#x53EF;&#x4EE5;&#x8FDB;&#x884C;&#x5176;&#x4ED6;&#x4EFB;&#x610F;&#x64CD;&#x4F5C;
&#x6CE8;&#x610F;&#xFF1A;&#x8FD4;&#x56DE;&#x503C;&#x5FC5;&#x987B;&#x5FC5;&#x987B;&#x662F;&#x6574;&#x6570;&#xFF0C;&#x5426;&#x5219;&#x8BED;&#x6CD5;&#x62A5;&#x9519;&#xFF0C;&#x53E6;&#x5916;&#x8BE5;&#x8981;&#x6C42;&#x662F;&#x683C;&#x5F0F;&#x8981;&#x6C42;&#x3002;
</code></pre><h4 id="6str">6.__str__</h4>
<pre><code>&#x89E6;&#x53D1;&#x65F6;&#x673A;:&#x4F7F;&#x7528;print(&#x5BF9;&#x8C61;)&#x6216;&#x8005;str(&#x5BF9;&#x8C61;)&#x7684;&#x65F6;&#x5019;&#x89E6;&#x53D1;
&#x53C2;&#x6570;&#xFF1A;&#x4E00;&#x4E2A;self&#x63A5;&#x6536;&#x5BF9;&#x8C61;
&#x8FD4;&#x56DE;&#x503C;&#xFF1A;&#x5FC5;&#x987B;&#x662F;&#x5B57;&#x7B26;&#x4E32;&#x7C7B;&#x578B;
&#x4F5C;&#x7528;&#xFF1A;print&#xFF08;&#x5BF9;&#x8C61;&#x65F6;&#xFF09;&#x8FDB;&#x884C;&#x64CD;&#x4F5C;&#xFF0C;&#x5F97;&#x5230;&#x5B57;&#x7B26;&#x4E32;&#xFF0C;&#x901A;&#x5E38;&#x7528;&#x4E8E;&#x5FEB;&#x6377;&#x64CD;&#x4F5C;
&#x6CE8;&#x610F;&#xFF1A;&#x65E0;
</code></pre><h4 id="7repr">7.__repr__</h4>
<pre><code>&#x89E6;&#x53D1;&#x65F6;&#x673A;:&#x5728;&#x4F7F;&#x7528;repr(&#x5BF9;&#x8C61;)&#x7684;&#x65F6;&#x5019;&#x89E6;&#x53D1;
&#x53C2;&#x6570;&#xFF1A;&#x4E00;&#x4E2A;self&#x63A5;&#x6536;&#x5BF9;&#x8C61;
&#x8FD4;&#x56DE;&#x503C;&#xFF1A;&#x5FC5;&#x987B;&#x662F;&#x5B57;&#x7B26;&#x4E32;
&#x4F5C;&#x7528;&#xFF1A;&#x5C06;&#x5BF9;&#x8C61;&#x8F6C;&#x4F7F;&#x7528;repr&#x5316;&#x4E3A;&#x5B57;&#x7B26;&#x4E32;&#x65F6;&#x4F7F;&#x7528;&#xFF0C;&#x4E5F;&#x53EF;&#x4EE5;&#x7528;&#x4E8E;&#x5FEB;&#x6377;&#x64CD;&#x4F5C;
</code></pre><blockquote>
<p>repr&#x51FD;&#x6570;&#x548C;str&#x51FD;&#x6570;&#x5904;&#x7406;&#x5B57;&#x7B26;&#x4E32;&#x53EA;&#x6709;&#x4E00;&#x4E2A;&#x533A;&#x522B;&#xFF1A;</p>
<p>str&#x7684;&#x7ED3;&#x679C; &#x5B57;&#x7B26;&#x4E32;&#x672C;&#x8EAB; &#xFF08;&#x7ED3;&#x679C;&#x53EF;&#x4EE5;&#x88AB;eval&#x6267;&#x884C;&#xFF09;</p>
<p>&#x5982;&#xFF1A;x = &apos;&#x65E0;&#x56FE;&#x8A00;Diao&apos; str() -&gt;&#x65E0;&#x56FE;&#x8A00;Diao</p>
<p>rerpr&#x7684;&#x7ED3;&#x679C; &#x5B57;&#x7B26;&#x4E32;&#x5B9A;&#x4E49;&#x7ED3;&#x6784; &#xFF08;eavl&#x4E0D;&#x4F1A;&#x6267;&#x884C;repr&#x7ED3;&#x679C;&#xFF09;</p>
<p>&#x5982;&#xFF1A;x = &apos;&#x65E0;&#x56FE;&#x8A00;Diao&apos; repr() -&gt;&apos;&#x65E0;&#x56FE;&#x8A00;Diao&apos;</p>
<p>&#x5907;&#x6CE8;: &#x5728;&#x7C7B;&#x4E2D;&#x901A;&#x5E38;&#x60C5;&#x51B5;&#x4E0B;__str__&#x548C;__repr__ &#x8BBE;&#x7F6E;&#x76F8;&#x540C;&#x5373;&#x53EF;</p>
<p><strong>eval()</strong> </p>
<p>&#x51FD;&#x6570; &#x5C06;&#x5B57;&#x7B26;&#x4E32;&#x5F53;&#x4F5C;python&#x4EE3;&#x7801;&#x6267;&#x884C;</p>
<p>&#x683C;&#x5F0F;&#xFF1A;eval(&#x5B57;&#x7B26;&#x4E32;)</p>
<p>&#x8FD4;&#x56DE;&#x503C;&#xFF1A;&#x53EF;&#x4EE5;&#x6709;&#x8FD4;&#x56DE;&#x503C;</p>
</blockquote>
<h4 id="8bool">8.__bool__</h4>
<pre><code>&#x89E6;&#x53D1;&#x65F6;&#x673A;: &#x4F7F;&#x7528;bool(&#x5BF9;&#x8C61;)&#x7684;&#x65F6;&#x5019;&#x89E6;&#x53D1;
&#x53C2;&#x6570;&#xFF1A;&#x4E00;&#x4E2A;self&#x63A5;&#x6536;&#x5BF9;&#x8C61;
&#x8FD4;&#x56DE;&#x503C;&#xFF1A;&#x5FC5;&#x987B;&#x662F;&#x5E03;&#x5C14;&#x503C;
&#x4F5C;&#x7528;&#xFF1A;&#x6839;&#x636E;&#x5B9E;&#x9645;&#x60C5;&#x51B5;&#x51B3;&#x5B9A;&#xFF0C;&#x53EF;&#x4EE5;&#x4F5C;&#x4E3A;&#x5FEB;&#x6377;&#x65B9;&#x5F0F;&#x4F7F;&#x7528;
&#x6CE8;&#x610F;:&#x4EC5;&#x9002;&#x5408;&#x4E8E;&#x8FD4;&#x56DE;&#x5E03;&#x5C14;&#x503C;&#x7684;&#x64CD;&#x4F5C;
</code></pre><h4 id="9format">9.__format__</h4>
<pre><code>&#x89E6;&#x53D1;&#x65F6;&#x673A;&#xFF1A;&#x4F7F;&#x7528;&#x5B57;&#x7B26;&#x4E32;.format(&#x5BF9;&#x8C61;)&#x65F6;&#x5019;&#x89E6;&#x53D1;
&#x53C2;&#x6570;&#xFF1A;&#x4E00;&#x4E2A;self&#x63A5;&#x6536;&#x5BF9;&#x8C61;&#xFF0C;&#x4E00;&#x4E2A;&#x53C2;&#x6570;&#x63A5;&#x6536;format&#x7684;{}&#x4E2D;&#x7684;&#x683C;&#x5F0F;&#xFF0C;&#x4F8B;&#x5982;:&gt;5
&#x8FD4;&#x56DE;&#x503C;:&#x5FC5;&#x987B;&#x662F;&#x5B57;&#x7B26;&#x4E32;
&#x4F5C;&#x7528;&#xFF1A;&#x8BBE;&#x7F6E;&#x5BF9;&#x8C61;&#x53EF;&#x4EE5;&#x4F5C;&#x4E3A;format&#x7684;&#x53C2;&#x6570;&#xFF0C;&#x5E76;&#x4E14;&#x81EA;&#x5B9A;&#x4E49;&#x5BF9;&#x8C61;&#x683C;&#x5F0F;&#x5316;&#x7684;&#x89C4;&#x5219;
&#x6CE8;&#x610F;&#xFF1A;&#x65E0;
</code></pre><h1 id="&#x63CF;&#x8FF0;&#x7B26;&#x76F8;&#x5173;&#x7684;&#x9B54;&#x672F;&#x65B9;&#x6CD5;">&#x63CF;&#x8FF0;&#x7B26;&#x76F8;&#x5173;&#x7684;&#x9B54;&#x672F;&#x65B9;&#x6CD5;</h1>
<hr>
<h4 id="1get">1.__get__()</h4>
<pre><code>&#x89E6;&#x53D1;&#x65F6;&#x673A;&#xFF1A;&#x5728;&#x83B7;&#x53D6;&#x6307;&#x5B9A;&#x63CF;&#x8FF0;&#x7B26;&#x64CD;&#x4F5C;&#x7684;&#x6210;&#x5458;&#x5C5E;&#x6027;&#x7684;&#x503C;&#x7684;&#x65F6;&#x5019;&#x89E6;&#x53D1;
&#x53C2;&#x6570;&#xFF1A;1&#x63CF;&#x8FF0;&#x7B26;&#x5BF9;&#x8C61;&#x672C;&#x8EAB;&#xFF0C;2&#x63CF;&#x8FF0;&#x7B26;&#x63CF;&#x8FF0;&#x7684;&#x5C5E;&#x6027;&#x6240;&#x5728;&#x7684;&#x5BF9;&#x8C61;&#xFF0C;&#x63CF;&#x8FF0;&#x7B26;&#x63CF;&#x8FF0;&#x7684;&#x5BF9;&#x8C61;&#x7684;&#x7C7B;
&#x8FD4;&#x56DE;&#x503C;&#xFF1A;&#x5FC5;&#x987B;&#x6709;&#xFF0C;&#x4E0D;&#x7136;&#x65E0;&#x6CD5;&#x83B7;&#x53D6;&#x76F8;&#x5E94;&#x5C5E;&#x6027;&#x503C;
&#x6CE8;&#x610F;&#xFF1A;&#x4EC5;&#x5728;&#x63CF;&#x8FF0;&#x7B26;&#x4E2D;&#x4F7F;&#x7528;
</code></pre><h4 id="2set">2.__set__()</h4>
<pre><code>&#x89E6;&#x53D1;&#x65F6;&#x673A;&#xFF1A;&#x5728;&#x8BBE;&#x7F6E;&#x6216;&#x8005;&#x6DFB;&#x52A0;&#x6307;&#x5B9A;&#x63CF;&#x8FF0;&#x7B26;&#x64CD;&#x4F5C;&#x7684;&#x6210;&#x5458;&#x5C5E;&#x6027;&#x7684;&#x65F6;&#x5019;&#x89E6;&#x53D1;
&#x53C2;&#x6570;&#xFF1A;1&#x63CF;&#x8FF0;&#x7B26;&#x5BF9;&#x8C61;&#x672C;&#x8EAB;&#xFF0C;2&#x63CF;&#x8FF0;&#x7B26;&#x63CF;&#x8FF0;&#x7684;&#x5C5E;&#x6027;&#x6240;&#x5728;&#x7684;&#x5BF9;&#x8C61;,3&#x8981;&#x8BBE;&#x7F6E;&#x7684;&#x503C;
&#x8FD4;&#x56DE;&#x503C;&#xFF1A;&#x65E0;
&#x6CE8;&#x610F;&#xFF1A;&#x4EC5;&#x5728;&#x63CF;&#x8FF0;&#x7B26;&#x4E2D;&#x4F7F;&#x7528;
</code></pre><h4 id="3delete">3.__delete__()</h4>
<pre><code>&#x89E6;&#x53D1;&#x65F6;&#x673A;&#xFF1A;&#x5728;&#x5220;&#x9664;&#x6307;&#x5B9A;&#x63CF;&#x8FF0;&#x7B26;&#x64CD;&#x4F5C;&#x7684;&#x6210;&#x5458;&#x5C5E;&#x6027;&#x7684;&#x65F6;&#x5019;&#x89E6;&#x53D1;
&#x53C2;&#x6570;&#xFF1A;1&#x63CF;&#x8FF0;&#x7B26;&#x5BF9;&#x8C61;&#x672C;&#x8EAB;&#xFF0C;2&#x63CF;&#x8FF0;&#x7B26;&#x63CF;&#x8FF0;&#x7684;&#x5C5E;&#x6027;&#x6240;&#x5728;&#x7684;&#x5BF9;&#x8C61;
&#x8FD4;&#x56DE;&#x503C;&#xFF1A;&#x65E0;
&#x6CE8;&#x610F;&#xFF1A;&#x4EC5;&#x5728;&#x63CF;&#x8FF0;&#x7B26;&#x4E2D;&#x4F7F;&#x7528;
</code></pre><h1 id="&#x4E0E;&#x5C5E;&#x6027;&#x64CD;&#x4F5C;&#x76F8;&#x5173;&#x7684;&#x9B54;&#x672F;&#x65B9;&#x6CD5;">&#x4E0E;&#x5C5E;&#x6027;&#x64CD;&#x4F5C;&#x76F8;&#x5173;&#x7684;&#x9B54;&#x672F;&#x65B9;&#x6CD5;</h1>
<hr>
<h4 id="1getattr&#xFF08;&#xFF09;">1.__getattr__&#xFF08;&#xFF09;</h4>
<pre><code>&#x89E6;&#x53D1;&#x65F6;&#x673A;&#xFF1A;&#x83B7;&#x53D6;&#x4E0D;&#x5B58;&#x5728;&#x7684;&#x5BF9;&#x8C61;&#x6210;&#x5458;&#x65F6;&#x89E6;&#x53D1;
&#x53C2;&#x6570;&#xFF1A;1&#x63A5;&#x6536;&#x5F53;&#x524D;&#x5BF9;&#x8C61;&#x7684;self&#xFF0C;&#x4E00;&#x4E2A;&#x662F;&#x83B7;&#x53D6;&#x6210;&#x5458;&#x540D;&#x79F0;&#x7684;&#x5B57;&#x7B26;&#x4E32;
&#x8FD4;&#x56DE;&#x503C;&#xFF1A;&#x5FC5;&#x987B;&#x6709;&#x503C;
&#x4F5C;&#x7528;:&#x4E3A;&#x8BBF;&#x95EE;&#x4E0D;&#x5B58;&#x5728;&#x7684;&#x5C5E;&#x6027;&#x8BBE;&#x7F6E;&#x503C;
&#x6CE8;&#x610F;&#xFF1A;getattribute&#x65E0;&#x8BBA;&#x4F55;&#x65F6;&#x90FD;&#x4F1A;&#x5728;getattr&#x4E4B;&#x524D;&#x89E6;&#x53D1;&#xFF0C;&#x89E6;&#x53D1;&#x4E86;getattribute&#x5C31;&#x4E0D;&#x4F1A;&#x5728;&#x89E6;&#x53D1;getattr&#x4E86;
</code></pre><h4 id="2setattr&#xFF08;&#xFF09;">2.__setattr__&#xFF08;&#xFF09;</h4>
<pre><code>&#x89E6;&#x53D1;&#x65F6;&#x673A;:&#x8BBE;&#x7F6E;&#x5BF9;&#x8C61;&#x6210;&#x5458;&#x503C;&#x7684;&#x65F6;&#x5019;&#x89E6;&#x53D1;
&#x53C2;&#x6570;:1&#x4E2A;&#x5F53;&#x524D;&#x5BF9;&#x8C61;&#x7684;self,&#x4E00;&#x4E2A;&#x662F;&#x8981;&#x8BBE;&#x7F6E;&#x7684;&#x6210;&#x5458;&#x540D;&#x79F0;&#x5B57;&#x7B26;&#x4E32;,&#x4E00;&#x4E2A;&#x662F;&#x8981;&#x8BBE;&#x7F6E;&#x7684;&#x503C;
&#x8FD4;&#x56DE;&#x503C;:&#x65E0; &#x8FC7;&#x7A0B;&#x64CD;&#x4F5C;
&#x4F5C;&#x7528;:&#x63A5;&#x7BA1;&#x8BBE;&#x7F6E;&#x64CD;&#x4F5C;,&#x53EF;&#x4EE5;&#x5728;&#x8BBE;&#x7F6E;&#x524D;&#x4E4B;&#x524D;&#x8FDB;&#x884C;&#x5224;&#x65AD;&#x9A8C;&#x8BC1;&#x7B49;&#x884C;&#x4E3A;
&#x6CE8;&#x610F;:&#x5728;&#x5F53;&#x524D;&#x65B9;&#x6CD5;&#x4E2D;&#x65E0;&#x6CD5;&#x4F7F;&#x7528;&#x6210;&#x5458;=&#x503C;&#x7684;&#x65B9;&#x5F0F;&#x76F4;&#x63A5;&#x8BBE;&#x7F6E;&#x6210;&#x5458;&#xFF0C;&#x5426;&#x5219;&#x4F1A;&#x65E0;&#x9650;&#x9012;&#x5F52;&#xFF0C;&#x5FC5;&#x987B;&#x501F;&#x52A9;object&#x7684;&#x8BBE;&#x7F6E;&#x65B9;&#x6CD5;&#x6765;&#x5B8C;&#x6210;

object.__setattr__&#xFF08;&#x53C2;&#x6570;1&#xFF0C;&#x53C2;&#x6570;2&#xFF0C;&#x53C2;&#x6570;3&#xFF09;
</code></pre><h4 id="3deleteattr&#xFF08;&#xFF09;">3.__delattr__&#xFF08;&#xFF09;</h4>
<pre><code>&#x89E6;&#x53D1;&#x65F6;&#x673A;&#xFF1A;&#x5220;&#x9664;&#x5BF9;&#x8C61;&#x6210;&#x5458;&#x65F6;&#x89E6;&#x53D1;
&#x53C2;&#x6570;&#xFF1A;&#x4E00;&#x4E2A;&#x5F53;&#x524D;&#x5BF9;&#x8C61;&#x7684;self
&#x8FD4;&#x56DE;&#x503C;&#xFF1A;&#x65E0;
&#x4F5C;&#x7528;:&#x53EF;&#x4EE5;&#x5728;&#x5220;&#x9664;&#x6210;&#x5458;&#x65F6;&#x8FDB;&#x884C;&#x9A8C;&#x8BC1;&#x3002;
</code></pre><h4 id="4getattribute&#xFF08;&#xFF09;">4.__getattribute__&#xFF08;&#xFF09;</h4>
<pre><code>&#x89E6;&#x53D1;&#x65F6;&#x673A;&#xFF1A;&#x4F7F;&#x7528;&#x5BF9;&#x8C61;&#x6210;&#x5458;&#x65F6;&#x89E6;&#x53D1;&#xFF0C;&#x65E0;&#x8BBA;&#x6210;&#x5458;&#x662F;&#x5426;&#x5B58;&#x5728;
&#x53C2;&#x6570;&#xFF1A;1&#x4E2A;&#x63A5;&#x6536;&#x5F53;&#x524D;&#x5BF9;&#x8C61;self&#xFF0C;&#x4E00;&#x4E2A;&#x662F;&#x83B7;&#x53D6;&#x7684;&#x6210;&#x5458;&#x7684;&#x540D;&#x79F0;&#x5B57;&#x7B26;&#x4E32;
&#x8FD4;&#x56DE;&#x503C;&#xFF1A;&#x5FC5;&#x987B;&#x6709;
&#x4F5C;&#x7528;&#xFF1A;&#x5728;&#x5177;&#x6709;&#x5C01;&#x88C5;&#x64CD;&#x4F5C;&#xFF08;&#x79C1;&#x6709;&#x5316;&#x65F6;&#xFF09;&#xFF0C;&#x4E3A;&#x7A0B;&#x5E8F;&#x5F00;&#x90E8;&#x5206;&#x8BBF;&#x95EE;&#x6743;&#x9650;&#x4F7F;&#x7528;
</code></pre><h4 id="5dir&#xFF08;&#xFF09;">5.__dir__&#xFF08;&#xFF09;</h4>
<pre><code>&#x89E6;&#x53D1;&#x65F6;&#x673A;&#xFF1A;dir&#xFF08;&#x5BF9;&#x8C61;&#xFF09;&#x7684;&#x65F6;&#x5019;&#x89E6;&#x53D1;
&#x53C2;&#x6570;:1&#x4E2A;&#x63A5;&#x6536;&#x5F53;&#x524D;&#x5BF9;&#x8C61;self
&#x8FD4;&#x56DE;&#x503C;&#xFF1A;&#x5FC5;&#x987B;&#x4E3A;&#x5E8F;&#x5217;&#x7C7B;&#x578B;&#xFF08;&#x5217;&#x8868;&#xFF0C;&#x5143;&#x7EC4;&#xFF0C;&#x96C6;&#x5408;&#x7B49;&#xFF0C;&#xFF09;
&#x4F5C;&#x7528;&#xFF1A;&#x53EF;&#x4EE5;&#x81EA;&#x5B9A;&#x4E49;&#x6210;&#x5458;&#x5217;&#x8868;&#x7684;&#x8FD4;&#x56DE;&#x503C;
</code></pre><h1 id="&#x8FD0;&#x7B97;&#x76F8;&#x5173;&#x9B54;&#x672F;&#x65B9;&#x6CD5;&#x4E0A;&#x5E1D;&#x6A21;&#x5F0F;">&#x8FD0;&#x7B97;&#x76F8;&#x5173;&#x9B54;&#x672F;&#x65B9;&#x6CD5;(&#x4E0A;&#x5E1D;&#x6A21;&#x5F0F;)</h1>
<hr>
<h2 id="&#x6BD4;&#x8F83;&#x8FD0;&#x7B97;&#x76F8;&#x5173;&#x9B54;&#x672F;&#x65B9;&#x6CD5;">&#x6BD4;&#x8F83;&#x8FD0;&#x7B97;&#x76F8;&#x5173;&#x9B54;&#x672F;&#x65B9;&#x6CD5;</h2>
<hr>
<h4 id="1lt">1.__lt__()</h4>
<pre><code>&#x683C;&#x5F0F;&#xFF1A;
    def __lt__(self,other):
    return &#x6570;&#x636E;

&#x7279;&#x5F81;&#xFF1A;
    &#x89E6;&#x53D1;&#x65F6;&#x673A;&#xFF1A;&#x8FDB;&#x884C;&#x5C0F;&#x4E8E;&#x5224;&#x65AD;&#x65F6;&#x81EA;&#x52A8;&#x89E6;&#x53D1;
    &#x53C2;&#x6570;&#xFF1A;2&#x4E2A;&#x53C2;&#x6570;&#x7B2C;&#x4E00;&#x4E2A;&#x662F;self&#xFF0C;&#x7B2C;&#x4E8C;&#x4E2A;&#x5224;&#x65AD;&#x7684;&#x7B2C;&#x4E8C;&#x4E2A;&#x5BF9;&#x8C61;
    &#x8FD4;&#x56DE;&#x503C;&#xFF1A;&#x8FD4;&#x56DE;&#x503C;&#x53EF;&#x4EE5;&#x4EFB;&#x610F;&#x7C7B;&#x578B;&#xFF0C;&#x63A8;&#x8350;&#x5E03;&#x5C14;&#x503C;
    &#x4F5C;&#x7528;&#xFF1A;&#x5B9A;&#x4E49;&#x5C0F;&#x4E8E;&#x53F7;&#x7684;&#x884C;&#x4E3A;&#xFF1A;x &lt; y &#x8C03;&#x7528; x.lt(y)
</code></pre><h4 id="2le">2.__le__()</h4>
<pre><code>&#x683C;&#x5F0F;&#xFF1A;
    def __le__(self):
    return str

&#x7279;&#x5F81;&#xFF1A;
    &#x89E6;&#x53D1;&#x65F6;&#x673A;&#xFF1A;&#x8FDB;&#x884C;&#x5C0F;&#x4E8E;&#x7B49;&#x4E8E;&#x5224;&#x65AD;&#x65F6;&#x81EA;&#x52A8;&#x89E6;&#x53D1;
    &#x53C2;&#x6570;&#xFF1A;2&#x4E2A;&#x53C2;&#x6570;&#x7B2C;&#x4E00;&#x4E2A;&#x662F;self&#xFF0C;&#x7B2C;&#x4E8C;&#x4E2A;&#x5224;&#x65AD;&#x7684;&#x7B2C;&#x4E8C;&#x4E2A;&#x5BF9;&#x8C61;
    &#x8FD4;&#x56DE;&#x503C;&#xFF1A;&#x8FD4;&#x56DE;&#x503C;&#x53EF;&#x4EE5;&#x4EFB;&#x610F;&#x7C7B;&#x578B;&#xFF0C;&#x63A8;&#x8350;&#x5E03;&#x5C14;&#x503C;
    &#x4F5C;&#x7528;&#xFF1A;&#x5B9A;&#x4E49;&#x5C0F;&#x4E8E;&#x7B49;&#x4E8E;&#x53F7;&#x7684;&#x884C;&#x4E3A;&#xFF1A;x &lt;= y &#x8C03;&#x7528; x.le(y)
</code></pre><h4 id="3gt">3.__gt__()</h4>
<pre><code>&#x683C;&#x5F0F;&#xFF1A;
    def __gt__(self):
    return str

&#x7279;&#x5F81;&#xFF1A;
    &#x89E6;&#x53D1;&#x65F6;&#x673A;&#xFF1A;&#x8FDB;&#x884C;&#x5927;&#x4E8E;&#x5224;&#x65AD;&#x65F6;&#x81EA;&#x52A8;&#x89E6;&#x53D1;
    &#x53C2;&#x6570;&#xFF1A;2&#x4E2A;&#x53C2;&#x6570;&#x7B2C;&#x4E00;&#x4E2A;&#x662F;self&#xFF0C;&#x7B2C;&#x4E8C;&#x4E2A;&#x5224;&#x65AD;&#x7684;&#x7B2C;&#x4E8C;&#x4E2A;&#x5BF9;&#x8C61;
    &#x8FD4;&#x56DE;&#x503C;&#xFF1A;&#x8FD4;&#x56DE;&#x503C;&#x53EF;&#x4EE5;&#x4EFB;&#x610F;&#x7C7B;&#x578B;&#xFF0C;&#x63A8;&#x8350;&#x5E03;&#x5C14;&#x503C;
    &#x4F5C;&#x7528;&#xFF1A;&#x5B9A;&#x4E49;&#x5927;&#x4E8E;&#x53F7;&#x7684;&#x884C;&#x4E3A;&#xFF1A;x &gt; y &#x8C03;&#x7528; x.gt(y)
</code></pre><h4 id="4ge">4.__ge__()</h4>
<pre><code>&#x683C;&#x5F0F;&#xFF1A;
    def __ge__(self):
    return str

&#x7279;&#x5F81;&#xFF1A;
    &#x89E6;&#x53D1;&#x65F6;&#x673A;&#xFF1A;&#x8FDB;&#x884C;&#x5927;&#x4E8E;&#x7B49;&#x4E8E;&#x5224;&#x65AD;&#x65F6;&#x81EA;&#x52A8;&#x89E6;&#x53D1;
    &#x53C2;&#x6570;&#xFF1A;2&#x4E2A;&#x53C2;&#x6570;&#x7B2C;&#x4E00;&#x4E2A;&#x662F;self&#xFF0C;&#x7B2C;&#x4E8C;&#x4E2A;&#x5224;&#x65AD;&#x7684;&#x7B2C;&#x4E8C;&#x4E2A;&#x5BF9;&#x8C61;
    &#x8FD4;&#x56DE;&#x503C;&#xFF1A;&#x8FD4;&#x56DE;&#x503C;&#x53EF;&#x4EE5;&#x4EFB;&#x610F;&#x7C7B;&#x578B;&#xFF0C;&#x63A8;&#x8350;&#x5E03;&#x5C14;&#x503C;
    &#x4F5C;&#x7528;&#xFF1A;&#x5B9A;&#x4E49;&#x5927;&#x4E8E;&#x7B49;&#x4E8E;&#x53F7;&#x7684;&#x884C;&#x4E3A;&#xFF1A;x &gt;= y &#x8C03;&#x7528; x.ge(y)
</code></pre><h4 id="5eq">5.__eq__()</h4>
<pre><code>&#x683C;&#x5F0F;&#xFF1A;
    def __eq__(self):
    return str

&#x7279;&#x5F81;&#xFF1A;
    &#x89E6;&#x53D1;&#x65F6;&#x673A;&#xFF1A;&#x8FDB;&#x884C;&#x7B49;&#x4E8E;&#x5224;&#x65AD;&#x65F6;&#x81EA;&#x52A8;&#x89E6;&#x53D1;
    &#x53C2;&#x6570;&#xFF1A;2&#x4E2A;&#x53C2;&#x6570;&#x7B2C;&#x4E00;&#x4E2A;&#x662F;self&#xFF0C;&#x7B2C;&#x4E8C;&#x4E2A;&#x5224;&#x65AD;&#x7684;&#x7B2C;&#x4E8C;&#x4E2A;&#x5BF9;&#x8C61;
    &#x8FD4;&#x56DE;&#x503C;&#xFF1A;&#x8FD4;&#x56DE;&#x503C;&#x53EF;&#x4EE5;&#x4EFB;&#x610F;&#x7C7B;&#x578B;&#xFF0C;&#x63A8;&#x8350;&#x5E03;&#x5C14;&#x503C;
    &#x4F5C;&#x7528;&#xFF1A;&#x5B9A;&#x4E49;&#x5927;&#x4E8E;&#x7B49;&#x4E8E;&#x53F7;&#x7684;&#x884C;&#x4E3A;&#xFF1A;x == y &#x8C03;&#x7528; x.eq(y)
</code></pre><h4 id="6ne">6.__ne__()</h4>
<pre><code>&#x683C;&#x5F0F;&#xFF1A;
    def __ne__(self):
    return str

&#x7279;&#x5F81;&#xFF1A;
    &#x89E6;&#x53D1;&#x65F6;&#x673A;&#xFF1A;&#x8FDB;&#x884C;&#x4E0D;&#x7B49;&#x4E8E;&#x5224;&#x65AD;&#x65F6;&#x81EA;&#x52A8;&#x89E6;&#x53D1;
    &#x53C2;&#x6570;&#xFF1A;2&#x4E2A;&#x53C2;&#x6570;&#x7B2C;&#x4E00;&#x4E2A;&#x662F;self&#xFF0C;&#x7B2C;&#x4E8C;&#x4E2A;&#x5224;&#x65AD;&#x7684;&#x7B2C;&#x4E8C;&#x4E2A;&#x5BF9;&#x8C61;
    &#x8FD4;&#x56DE;&#x503C;&#xFF1A;&#x8FD4;&#x56DE;&#x503C;&#x53EF;&#x4EE5;&#x4EFB;&#x610F;&#x7C7B;&#x578B;&#xFF0C;&#x63A8;&#x8350;&#x5E03;&#x5C14;&#x503C;
    &#x4F5C;&#x7528;&#xFF1A;&#x5B9A;&#x4E49;&#x4E0D;&#x7B49;&#x53F7;&#x7684;&#x884C;&#x4E3A;&#xFF1A;x != y &#x8C03;&#x7528; x.ne(y)
</code></pre><h2 id="&#x7B97;&#x672F;&#x8FD0;&#x7B97;&#x76F8;&#x5173;&#x9B54;&#x672F;&#x65B9;&#x6CD5;">&#x7B97;&#x672F;&#x8FD0;&#x7B97;&#x76F8;&#x5173;&#x9B54;&#x672F;&#x65B9;&#x6CD5;</h2>
<hr>
<pre><code>__add__(self, other)           &#x5B9A;&#x4E49;&#x52A0;&#x6CD5;&#x7684;&#x884C;&#x4E3A;&#xFF1A;+
__sub__(self, other)           &#x5B9A;&#x4E49;&#x51CF;&#x6CD5;&#x7684;&#x884C;&#x4E3A;&#xFF1A;-
__mul__(self, other)           &#x5B9A;&#x4E49;&#x4E58;&#x6CD5;&#x7684;&#x884C;&#x4E3A;&#xFF1A;
__truediv__(self, other)       &#x5B9A;&#x4E49;&#x771F;&#x9664;&#x6CD5;&#x7684;&#x884C;&#x4E3A;&#xFF1A;/
__floordiv__(self, other)      &#x5B9A;&#x4E49;&#x6574;&#x6570;&#x9664;&#x6CD5;&#x7684;&#x884C;&#x4E3A;&#xFF1A;//
__mod__(self, other)           &#x5B9A;&#x4E49;&#x53D6;&#x6A21;&#x7B97;&#x6CD5;&#x7684;&#x884C;&#x4E3A;&#xFF1A;%
__divmod__(self, other)        &#x5B9A;&#x4E49;&#x5F53;&#x88AB; divmod() &#x8C03;&#x7528;&#x65F6;&#x7684;&#x884C;&#x4E3A;
__pow__(self, other[, modulo]) &#x5B9A;&#x4E49;&#x5F53;&#x88AB; power() &#x8C03;&#x7528;&#x6216; ** &#x8FD0;&#x7B97;&#x65F6;&#x7684;&#x884C;&#x4E3A;
__lshift__(self, other)        &#x5B9A;&#x4E49;&#x6309;&#x4F4D;&#x5DE6;&#x79FB;&#x4F4D;&#x7684;&#x884C;&#x4E3A;&#xFF1A;&lt;&lt;
__rshift__(self, other)        &#x5B9A;&#x4E49;&#x6309;&#x4F4D;&#x53F3;&#x79FB;&#x4F4D;&#x7684;&#x884C;&#x4E3A;&#xFF1A;&gt;&gt;
__and__(self, other)           &#x5B9A;&#x4E49;&#x6309;&#x4F4D;&#x4E0E;&#x64CD;&#x4F5C;&#x7684;&#x884C;&#x4E3A;&#xFF1A;&amp;
__xor__(self, other)           &#x5B9A;&#x4E49;&#x6309;&#x4F4D;&#x5F02;&#x6216;&#x64CD;&#x4F5C;&#x7684;&#x884C;&#x4E3A;&#xFF1A;^
__or__(self, other)            &#x5B9A;&#x4E49;&#x6309;&#x4F4D;&#x6216;&#x64CD;&#x4F5C;&#x7684;&#x884C;&#x4E3A;&#xFF1A;|
</code></pre><h2 id="&#x53CD;&#x8FD0;&#x7B97;&#x76F8;&#x5173;&#x9B54;&#x672F;&#x65B9;&#x6CD5;">&#x53CD;&#x8FD0;&#x7B97;&#x76F8;&#x5173;&#x9B54;&#x672F;&#x65B9;&#x6CD5;</h2>
<hr>
<pre><code>__radd__(self, other)      &#x4E0E;&#x4E0A;&#x65B9;&#x76F8;&#x540C;&#xFF0C;&#x5F53;&#x5DE6;&#x64CD;&#x4F5C;&#x6570;&#x4E0D;&#x652F;&#x6301;&#x76F8;&#x5E94;&#x7684;&#x64CD;&#x4F5C;&#x65F6;&#x88AB;&#x8C03;&#x7528;
__rsub__(self, other)      &#x4E0E;&#x4E0A;&#x65B9;&#x76F8;&#x540C;&#xFF0C;&#x5F53;&#x5DE6;&#x64CD;&#x4F5C;&#x6570;&#x4E0D;&#x652F;&#x6301;&#x76F8;&#x5E94;&#x7684;&#x64CD;&#x4F5C;&#x65F6;&#x88AB;&#x8C03;&#x7528;
__rmul__(self, other)      &#x4E0E;&#x4E0A;&#x65B9;&#x76F8;&#x540C;&#xFF0C;&#x5F53;&#x5DE6;&#x64CD;&#x4F5C;&#x6570;&#x4E0D;&#x652F;&#x6301;&#x76F8;&#x5E94;&#x7684;&#x64CD;&#x4F5C;&#x65F6;&#x88AB;&#x8C03;&#x7528;
__rtruediv__(self, other)  &#x4E0E;&#x4E0A;&#x65B9;&#x76F8;&#x540C;&#xFF0C;&#x5F53;&#x5DE6;&#x64CD;&#x4F5C;&#x6570;&#x4E0D;&#x652F;&#x6301;&#x76F8;&#x5E94;&#x7684;&#x64CD;&#x4F5C;&#x65F6;&#x88AB;&#x8C03;&#x7528;
__rfloordiv__(self, other) &#x4E0E;&#x4E0A;&#x65B9;&#x76F8;&#x540C;&#xFF0C;&#x5F53;&#x5DE6;&#x64CD;&#x4F5C;&#x6570;&#x4E0D;&#x652F;&#x6301;&#x76F8;&#x5E94;&#x7684;&#x64CD;&#x4F5C;&#x65F6;&#x88AB;&#x8C03;&#x7528;
__rmod__(self, other)      &#x4E0E;&#x4E0A;&#x65B9;&#x76F8;&#x540C;&#xFF0C;&#x5F53;&#x5DE6;&#x64CD;&#x4F5C;&#x6570;&#x4E0D;&#x652F;&#x6301;&#x76F8;&#x5E94;&#x7684;&#x64CD;&#x4F5C;&#x65F6;&#x88AB;&#x8C03;&#x7528;
__rdivmod__(self, other)   &#x4E0E;&#x4E0A;&#x65B9;&#x76F8;&#x540C;&#xFF0C;&#x5F53;&#x5DE6;&#x64CD;&#x4F5C;&#x6570;&#x4E0D;&#x652F;&#x6301;&#x76F8;&#x5E94;&#x7684;&#x64CD;&#x4F5C;&#x65F6;&#x88AB;&#x8C03;&#x7528;
__rpow__(self, other)      &#x4E0E;&#x4E0A;&#x65B9;&#x76F8;&#x540C;&#xFF0C;&#x5F53;&#x5DE6;&#x64CD;&#x4F5C;&#x6570;&#x4E0D;&#x652F;&#x6301;&#x76F8;&#x5E94;&#x7684;&#x64CD;&#x4F5C;&#x65F6;&#x88AB;&#x8C03;&#x7528;
__rlshift__(self, other)   &#x4E0E;&#x4E0A;&#x65B9;&#x76F8;&#x540C;&#xFF0C;&#x5F53;&#x5DE6;&#x64CD;&#x4F5C;&#x6570;&#x4E0D;&#x652F;&#x6301;&#x76F8;&#x5E94;&#x7684;&#x64CD;&#x4F5C;&#x65F6;&#x88AB;&#x8C03;&#x7528;
__rrshift__(self, other)   &#x4E0E;&#x4E0A;&#x65B9;&#x76F8;&#x540C;&#xFF0C;&#x5F53;&#x5DE6;&#x64CD;&#x4F5C;&#x6570;&#x4E0D;&#x652F;&#x6301;&#x76F8;&#x5E94;&#x7684;&#x64CD;&#x4F5C;&#x65F6;&#x88AB;&#x8C03;&#x7528;
__rand__(self, other)      &#x4E0E;&#x4E0A;&#x65B9;&#x76F8;&#x540C;&#xFF0C;&#x5F53;&#x5DE6;&#x64CD;&#x4F5C;&#x6570;&#x4E0D;&#x652F;&#x6301;&#x76F8;&#x5E94;&#x7684;&#x64CD;&#x4F5C;&#x65F6;&#x88AB;&#x8C03;&#x7528;
__rxor__(self, other)      &#x4E0E;&#x4E0A;&#x65B9;&#x76F8;&#x540C;&#xFF0C;&#x5F53;&#x5DE6;&#x64CD;&#x4F5C;&#x6570;&#x4E0D;&#x652F;&#x6301;&#x76F8;&#x5E94;&#x7684;&#x64CD;&#x4F5C;&#x65F6;&#x88AB;&#x8C03;&#x7528;
__ror__(self, other)       &#x4E0E;&#x4E0A;&#x65B9;&#x76F8;&#x540C;&#xFF0C;&#x5F53;&#x5DE6;&#x64CD;&#x4F5C;&#x6570;&#x4E0D;&#x652F;&#x6301;&#x76F8;&#x5E94;&#x7684;&#x64CD;&#x4F5C;&#x65F6;&#x88AB;&#x8C03;&#x7528;
</code></pre><h2 id="&#x8D4B;&#x503C;&#x8FD0;&#x7B97;&#x76F8;&#x5173;&#x9B54;&#x672F;&#x65B9;&#x6CD5;">&#x8D4B;&#x503C;&#x8FD0;&#x7B97;&#x76F8;&#x5173;&#x9B54;&#x672F;&#x65B9;&#x6CD5;</h2>
<hr>
<pre><code>__iadd__(self, other)             &#x5B9A;&#x4E49;&#x8D4B;&#x503C;&#x52A0;&#x6CD5;&#x7684;&#x884C;&#x4E3A;&#xFF1A;+=
__isub__(self, other)             &#x5B9A;&#x4E49;&#x8D4B;&#x503C;&#x51CF;&#x6CD5;&#x7684;&#x884C;&#x4E3A;&#xFF1A;-=
__imul__(self, other)             &#x5B9A;&#x4E49;&#x8D4B;&#x503C;&#x4E58;&#x6CD5;&#x7684;&#x884C;&#x4E3A;&#xFF1A;=
__itruediv__(self, other)         &#x5B9A;&#x4E49;&#x8D4B;&#x503C;&#x771F;&#x9664;&#x6CD5;&#x7684;&#x884C;&#x4E3A;&#xFF1A;/=
__ifloordiv__(self, other)        &#x5B9A;&#x4E49;&#x8D4B;&#x503C;&#x6574;&#x6570;&#x9664;&#x6CD5;&#x7684;&#x884C;&#x4E3A;&#xFF1A;//=
__imod__(self, other)             &#x5B9A;&#x4E49;&#x8D4B;&#x503C;&#x53D6;&#x6A21;&#x7B97;&#x6CD5;&#x7684;&#x884C;&#x4E3A;&#xFF1A;%=
__ipow__(self, other[, modulo])   &#x5B9A;&#x4E49;&#x8D4B;&#x503C;&#x5E42;&#x8FD0;&#x7B97;&#x7684;&#x884C;&#x4E3A;&#xFF1A;**=
__ilshift__(self, other)          &#x5B9A;&#x4E49;&#x8D4B;&#x503C;&#x6309;&#x4F4D;&#x5DE6;&#x79FB;&#x4F4D;&#x7684;&#x884C;&#x4E3A;&#xFF1A;&lt;&lt;=
__irshift__(self, other)          &#x5B9A;&#x4E49;&#x8D4B;&#x503C;&#x6309;&#x4F4D;&#x53F3;&#x79FB;&#x4F4D;&#x7684;&#x884C;&#x4E3A;&#xFF1A;&gt;&gt;=
__iand__(self, other)             &#x5B9A;&#x4E49;&#x8D4B;&#x503C;&#x6309;&#x4F4D;&#x4E0E;&#x64CD;&#x4F5C;&#x7684;&#x884C;&#x4E3A;&#xFF1A;&amp;=
__ixor__(self, other)             &#x5B9A;&#x4E49;&#x8D4B;&#x503C;&#x6309;&#x4F4D;&#x5F02;&#x6216;&#x64CD;&#x4F5C;&#x7684;&#x884C;&#x4E3A;&#xFF1A;^=
__ior__(self, other)              &#x5B9A;&#x4E49;&#x8D4B;&#x503C;&#x6309;&#x4F4D;&#x6216;&#x64CD;&#x4F5C;&#x7684;&#x884C;&#x4E3A;&#xFF1A;|=
</code></pre><h2 id="&#x4E00;&#x5143;&#x8FD0;&#x7B97;&#x76F8;&#x5173;&#x9B54;&#x672F;&#x65B9;&#x6CD5;">&#x4E00;&#x5143;&#x8FD0;&#x7B97;&#x76F8;&#x5173;&#x9B54;&#x672F;&#x65B9;&#x6CD5;</h2>
<hr>
<pre><code>__pos__(self)      &#x5B9A;&#x4E49;&#x6B63;&#x53F7;&#x7684;&#x884C;&#x4E3A;&#xFF1A;+x
__neg__(self)      &#x5B9A;&#x4E49;&#x8D1F;&#x53F7;&#x7684;&#x884C;&#x4E3A;&#xFF1A;-x
__abs__(self)      &#x5B9A;&#x4E49;&#x5F53;&#x88AB; abs() &#x8C03;&#x7528;&#x65F6;&#x7684;&#x884C;&#x4E3A;
__invert__(self)   &#x5B9A;&#x4E49;&#x6309;&#x4F4D;&#x6C42;&#x53CD;&#x7684;&#x884C;&#x4E3A;&#xFF1A;~x
</code></pre><h2 id="&#x7C7B;&#x578B;&#x8F6C;&#x6362;&#x76F8;&#x5173;&#x9B54;&#x672F;&#x65B9;&#x6CD5;-jiang">&#x7C7B;&#x578B;&#x8F6C;&#x6362;&#x76F8;&#x5173;&#x9B54;&#x672F;&#x65B9;&#x6CD5; JIANG</h2>
<hr>
<pre><code>__complex__(self)      &#x5B9A;&#x4E49;&#x5F53;&#x88AB; complex() &#x8C03;&#x7528;&#x65F6;&#x7684;&#x884C;&#x4E3A;&#xFF08;&#x9700;&#x8981;&#x8FD4;&#x56DE;&#x6070;&#x5F53;&#x7684;&#x503C;&#xFF09;
__int__(self)          &#x5B9A;&#x4E49;&#x5F53;&#x88AB; int() &#x8C03;&#x7528;&#x65F6;&#x7684;&#x884C;&#x4E3A;&#xFF08;&#x9700;&#x8981;&#x8FD4;&#x56DE;&#x6070;&#x5F53;&#x7684;&#x503C;&#xFF09;
__float__(self)        &#x5B9A;&#x4E49;&#x5F53;&#x88AB; float() &#x8C03;&#x7528;&#x65F6;&#x7684;&#x884C;&#x4E3A;&#xFF08;&#x9700;&#x8981;&#x8FD4;&#x56DE;&#x6070;&#x5F53;&#x7684;&#x503C;&#xFF09;
__round__(self[, n])   &#x5B9A;&#x4E49;&#x5F53;&#x88AB; round() &#x8C03;&#x7528;&#x65F6;&#x7684;&#x884C;&#x4E3A;&#xFF08;&#x9700;&#x8981;&#x8FD4;&#x56DE;&#x6070;&#x5F53;&#x7684;&#x503C;&#xFF09;
__index(self)__        1. &#x5F53;&#x5BF9;&#x8C61;&#x662F;&#x88AB;&#x5E94;&#x7528;&#x5728;&#x5207;&#x7247;&#x8868;&#x8FBE;&#x5F0F;&#x4E2D;&#x65F6;&#xFF0C;&#x5B9E;&#x73B0;&#x6574;&#x5F62;&#x5F3A;&#x5236;&#x8F6C;&#x6362;
                       2. &#x5982;&#x679C;&#x4F60;&#x5B9A;&#x4E49;&#x4E86;&#x4E00;&#x4E2A;&#x53EF;&#x80FD;&#x5728;&#x5207;&#x7247;&#x65F6;&#x7528;&#x5230;&#x7684;&#x5B9A;&#x5236;&#x7684;&#x6570;&#x503C;&#x578B;,&#x4F60;&#x5E94;&#x8BE5;&#x5B9A;&#x4E49; index
                       3. &#x5982;&#x679C; index &#x88AB;&#x5B9A;&#x4E49;&#xFF0C;&#x5219; int &#x4E5F;&#x9700;&#x8981;&#x88AB;&#x5B9A;&#x4E49;&#xFF0C;&#x4E14;&#x8FD4;&#x56DE;&#x76F8;&#x540C;&#x7684;&#x503C;
</code></pre><h2 id="&#x4E0A;&#x4E0B;&#x6587;&#x7BA1;&#x7406;&#x76F8;&#x5173;&#x9B54;&#x672F;&#x65B9;&#x6CD5;">&#x4E0A;&#x4E0B;&#x6587;&#x7BA1;&#x7406;&#x76F8;&#x5173;&#x9B54;&#x672F;&#x65B9;&#x6CD5;</h2>
<hr>
<p><strong>__enter__()</strong> &#x548C; <strong>__exit__()</strong></p>
<pre><code>enter(self)
    1. &#x5B9A;&#x4E49;&#x5F53;&#x4F7F;&#x7528; with &#x8BED;&#x53E5;&#x65F6;&#x7684;&#x521D;&#x59CB;&#x5316;&#x884C;&#x4E3A;
    2. enter &#x7684;&#x8FD4;&#x56DE;&#x503C;&#x88AB; with &#x8BED;&#x53E5;&#x7684;&#x76EE;&#x6807;&#x6216;&#x8005; as &#x540E;&#x7684;&#x540D;&#x5B57;&#x7ED1;&#x5B9A;

exit(self, exctype, excvalue, traceback)
    1. &#x5B9A;&#x4E49;&#x5F53;&#x4E00;&#x4E2A;&#x4EE3;&#x7801;&#x5757;&#x88AB;&#x6267;&#x884C;&#x6216;&#x8005;&#x7EC8;&#x6B62;&#x540E;&#x4E0A;&#x4E0B;&#x6587;&#x7BA1;&#x7406;&#x5668;&#x5E94;&#x8BE5;&#x505A;&#x4EC0;&#x4E48;
    2. &#x4E00;&#x822C;&#x88AB;&#x7528;&#x6765;&#x5904;&#x7406;&#x5F02;&#x5E38;&#xFF0C;&#x6E05;&#x9664;&#x5DE5;&#x4F5C;&#x6216;&#x8005;&#x505A;&#x4E00;&#x4E9B;&#x4EE3;&#x7801;&#x5757;&#x6267;&#x884C;&#x5B8C;&#x6BD5;&#x4E4B;&#x540E;&#x7684;&#x65E5;&#x5E38;&#x5DE5;&#x4F5C;
</code></pre><h2 id="&#x5BB9;&#x5668;&#x7C7B;&#x578B;&#x76F8;&#x5173;&#x9B54;&#x672F;&#x65B9;&#x6CD5;">&#x5BB9;&#x5668;&#x7C7B;&#x578B;&#x76F8;&#x5173;&#x9B54;&#x672F;&#x65B9;&#x6CD5;</h2>
<hr>
<pre><code>__len__(self)                  &#x5B9A;&#x4E49;&#x5F53;&#x88AB; len() &#x8C03;&#x7528;&#x65F6;&#x7684;&#x884C;&#x4E3A;&#xFF08;&#x8FD4;&#x56DE;&#x5BB9;&#x5668;&#x4E2D;&#x5143;&#x7D20;&#x7684;&#x4E2A;&#x6570;&#xFF09;
__getitem__(self, key)         &#x5B9A;&#x4E49;&#x83B7;&#x53D6;&#x5BB9;&#x5668;&#x4E2D;&#x6307;&#x5B9A;&#x5143;&#x7D20;&#x7684;&#x884C;&#x4E3A;&#xFF0C;&#x76F8;&#x5F53;&#x4E8E; self[key]
__setitem__(self, key, value)  &#x5B9A;&#x4E49;&#x8BBE;&#x7F6E;&#x5BB9;&#x5668;&#x4E2D;&#x6307;&#x5B9A;&#x5143;&#x7D20;&#x7684;&#x884C;&#x4E3A;&#xFF0C;&#x76F8;&#x5F53;&#x4E8E; self[key] = value
__delitem__(self, key)         &#x5B9A;&#x4E49;&#x5220;&#x9664;&#x5BB9;&#x5668;&#x4E2D;&#x6307;&#x5B9A;&#x5143;&#x7D20;&#x7684;&#x884C;&#x4E3A;&#xFF0C;&#x76F8;&#x5F53;&#x4E8E; del self[key]
__iter__(self)                 &#x5B9A;&#x4E49;&#x5F53;&#x8FED;&#x4EE3;&#x5BB9;&#x5668;&#x4E2D;&#x7684;&#x5143;&#x7D20;&#x7684;&#x884C;&#x4E3A;
__reversed__(self)             &#x5B9A;&#x4E49;&#x5F53;&#x88AB; reversed() &#x8C03;&#x7528;&#x65F6;&#x7684;&#x884C;&#x4E3A;
__contains__(self, item)       &#x5B9A;&#x4E49;&#x5F53;&#x4F7F;&#x7528;&#x6210;&#x5458;&#x6D4B;&#x8BD5;&#x8FD0;&#x7B97;&#x7B26;&#xFF08;in &#x6216; not in&#xFF09;&#x65F6;&#x7684;&#x884C;&#x4E3A;
</code></pre>
                    
                    