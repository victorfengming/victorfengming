---
title: "图片格式详解:PNG、JPEG、GIF、SVG"
date:       2019-09-13
tags:
	- web
	- basis
---

<section class="ouvJEz"><h1 class="_1RuRku">PNG、JPEG、GIF、SVG应该用哪个？</h1><div class="rEsl9f"><div class="s-dsoj"><span class="_3tCVn5"><i aria-label="ic-diamond" class="anticon"><svg width="1em" height="1em" fill="currentColor" aria-hidden="true" focusable="false" class=""><use xlink:href="#ic-diamond"></use></svg></i><span>0.674</span></span><time datetime="2016-10-13T13:49:27.000Z">2016.10.13 21:49:27</time><span>字数 1790</span><span>阅读 11501</span></div></div><article class="_2rhmJa"><h3>Beginning</h3>
<p>当我们构建网站或者开发App的时候，应当怎样选择使用图片的类型呢？<br>
是简单的全部使用一种类型还是根据业务情形选择不同的图片类型呢？<br>
每种类型的图片类型又有怎样的优点和缺点呢？</p>
<h3>Concepts</h3>
<p>图片呈现效果的异同跟以下两个因素有关：</p>
<p>首先，压缩分两派：<strong>无损压缩</strong>和<strong>有损压缩</strong>。</p>
<ul>
<li>
<strong>无损压缩</strong> ：能够使图片占用的存储空间变小，而且不会损害图片的质量。</li>
<li>
<strong>有损压缩</strong>：相对<strong>无损压缩</strong>会压缩的更狠一点，但是不可避免的会对图片质量产生损害。如果有损压缩的次数多了的话，那么图片的质量也会越来越差。</li>
</ul>
<p>其次也有不同的色彩深度（色彩模式）：<strong>索引色彩</strong>和<strong>直接色彩</strong>。</p>
<ul>
<li>
<strong>索引色彩</strong> ：这个模式下图片仅可以存储有限数量的颜色种类（通常是2^8即256种）。</li>
<li>
<strong>直接色彩</strong>：这个模式下你可以存储成千上万种颜色值，所以相对而言采用这种模式的图片会显得色彩更加丰富饱满和艳丽。</li>
</ul>
<p>接下来会通过这两个维度对常见的几种图片类型来进行分析和比较，总结它们的优缺点和适用场景。</p>
<h3>BMP - 无损压缩、索引色彩模式、直接色彩模式</h3>
<p>这是较早出现的一种图片格式。它是无损的但是压缩比例着实很低，BMP格式的图片通常会占用较大的存储空间。它拥有两种色彩模式，但是由于占用存储空间如此之大，几乎没有人会去使用这种格式。<br>
擅长：真的没有，BMP格式真的没有任何优点，大家还是尽量不要用这种格式的图片。</p>
<h3>GIF - 无损压缩、直接色彩模式</h3>
<p>GIF使用了更好的无损压缩算法，所以你可以压缩图片的大小但是不会丢失任何数据，文件大小也比BMP小得多。但是只可以使用索引色彩模式。这意味着大多数情况下最多只可以有256种颜色显示在图片里。颜色种类貌似真的好少，确实。GIF图片可以动并且拥有透明度（<code>透明或不透明，并没有alpha通道</code>）。<br>
擅长：logo，线条，或其他需要尺寸尽可能小的简单图像。</p>
<h3>JPEG - 有损压缩、直接色彩模式</h3>
<p>JPEG是一种偏向平衡性的格式，它会舍弃掉人眼根本无法感知的颜色信息，以使文件尽可能小并且细节不丢失。因此，它是一种有损格式。它颜色丰富并且很适合那些允许轻微失真的像素色彩丰富的图片（如相片）。但是有损压缩意味着不适合logo和线图，因为不仅看起来模糊还比GIF占用的文件大小大。<br>
擅长：相片，渐变图像。</p>
<h3>PNG-8 - 无损压缩、索引色彩模式</h3>
<p>PNG是一种较新的格式，并且PNG-8（PNG的索引模式版本）是GIF格式很好的替代。可是也有一些缺点：首先不能像GIF一样能动，其次对一些老旧的浏览器（如IE6）会有不兼容的问题。<br>
擅长：PNG-8相对于GIF来讲有对alpha透明通道的支持。</p>
<h3>PNG-24 - 无损压缩、直接色彩模式</h3>
<p>PNG-24对无损压缩和直接色彩模式结合的很好（就像JPEG一样色彩丰富），在这方面和BMP很相似，但是PNG的压缩比率远强过BMP，所以文件大小也更小。不幸的是PNG-24仍然会比JPEG，GIF，PNG-8占用更多的存储空间，所以如果你对文件大小很在意的话，还是要考虑是否要选择以上的一种。</p>
<p>尽管PNG-24压缩比率较高而且还有丰富的色彩，但它不是为了来取代JPEG的，因为一个照片保存为PNG-24格式的话会比JPEG至少大5倍，但是图片显示质量却几乎没有提升。（如果你唯一考虑的因素就是图片质量的话，你还是可以使用这个格式的）<br>
PNG-24和PNG-8一样也支持alpha透明通道。</p>
<h3>SVG -无损压缩、矢量模式</h3>
<p>SVG正变得越来越热门，它不同于以上所有的文件类型，因为它是一个矢量文件格式。这就是说它实际上是由线条和曲线，而不是像素组成的。当你放大一个矢量图像时，你仍然看到一条曲线或一条线。当你放大一个由像素构成的图像时，你会看到像素。<br>
例如：</p>
<br>
<div class="image-package">
<div class="image-container" style="max-width: 640px; max-height: 352px; background-color: transparent;">
<div class="image-container-fill" style="padding-bottom: 55.00000000000001%;"></div>

</div>
<div class="image-caption"></div>
</div><br>
<div class="image-package">
<div class="image-container" style="max-width: 640px; max-height: 352px; background-color: transparent;">
<div class="image-container-fill" style="padding-bottom: 55.00000000000001%;"></div>
<div class="image-view" data-width="640" data-height="352"><img data-original-src="//upload-images.jianshu.io/upload_images/174711-b2a169cc588490f6.png" data-original-width="640" data-original-height="352" data-original-format="image/png" data-original-filesize="18743" data-image-index="1" class="" style="cursor: zoom-in;" src="//upload-images.jianshu.io/upload_images/174711-b2a169cc588490f6.png?imageMogr2/auto-orient/strip|imageView2/2/w/640/format/webp"></div>
</div>
<div class="image-caption"></div>
</div>
<p>这意味着，对于小logo和图标和来说，SVG是很理想的，因为无论是Retina屏幕或在其他低清晰度的屏幕上它的形状都是一样的。这也意味着一个小的SVG logo可以放大但不失真，如果是像素构成的图片格式的话就需要设计多套图片，可以参考Android中的xxxdpi。<br>
SVG文件的大小通常是极小的，即使它们看起来的样子真的很大。然而，值得注意的是，SVG文件的大小也取决于要展示图形的复杂度。而且SVG在渲染的时候需要比像素图更多的计算能力，这也就意味着性能的损耗。如果你的logo是特别复杂的，它可能会很耗费性能，甚至文件大小也非常大。所以尽可能简化你的矢量形状的复杂度是很重要也很有必要的。<br>
此外，SVG文件是用XML编写的，因此可以在文本编辑器中打开和编辑。这意味着它展示的效果在运行时是可以改变的。例如，你可以使用JavaScript来改变对一个网站的SVG图标的颜色。所以，对于简单的平面形状，像logo或图形，使用svg是坠好的。<br>
另外Android现在对SVG的支持也算是比较成熟了，微信团队貌似现在所有的图片资源都替换成SVG了。</p>
<h3>Summary</h3>
<p>所以这么一个小小的问题也有这么多值得挖掘的知识点。作为一个合格的工程师，任何一个细节都不可以放过，因为<code>They just make it better</code>.</p>
</article><div></div><div class="_1kCBjS"><div class="_18vaTa"><div class="_3BUZPB"><div class="_2Bo4Th" role="button" tabindex="-1" aria-label="给文章点赞"><i aria-label="ic-like" class="anticon"><svg width="1em" height="1em" fill="currentColor" aria-hidden="true" focusable="false" class=""><use xlink:href="#ic-like"></use></svg></i></div><span class="_1LOh_5" role="button" tabindex="-1" aria-label="查看点赞列表">16人点赞<i aria-label="icon: right" class="anticon anticon-right"><svg viewBox="64 64 896 896" focusable="false" class="" data-icon="right" width="1em" height="1em" fill="currentColor" aria-hidden="true"><path d="M765.7 486.8L314.9 134.7A7.97 7.97 0 0 0 302 141v77.3c0 4.9 2.3 9.6 6.1 12.6l360 281.1-360 281.1c-3.9 3-6.1 7.7-6.1 12.6V883c0 6.7 7.7 10.4 12.9 6.3l450.8-352.1a31.96 31.96 0 0 0 0-50.4z"></path></svg></i></span></div><div class="_3BUZPB"><div class="_2Bo4Th" role="button" tabindex="-1"><i aria-label="ic-dislike" class="anticon"><svg width="1em" height="1em" fill="currentColor" aria-hidden="true" focusable="false" class=""><use xlink:href="#ic-dislike"></use></svg></i></div></div></div><div class="_18vaTa"><a class="_3BUZPB _1x1ok9 _1OhGeD" href="/nb/359801" target="_blank" rel="noopener noreferrer"><i aria-label="ic-notebook" class="anticon"><svg width="1em" height="1em" fill="currentColor" aria-hidden="true" focusable="false" class=""><use xlink:href="#ic-notebook"></use></svg></i><span>日记本</span></a><div class="_3BUZPB ant-dropdown-trigger"><div class="_2Bo4Th"><i aria-label="ic-others" class="anticon"><svg width="1em" height="1em" fill="currentColor" aria-hidden="true" focusable="false" class=""><use xlink:href="#ic-others"></use></svg></i></div></div></div></div><div class="_19DgIp" style="margin-top:24px;margin-bottom:24px"></div><div class="_3W59v5"><div class="Uz-vZq"><div class="VwEQ52"><a class="_1OhGeD" href="/u/9b40ae19f574" target="_blank" rel="noopener noreferrer"><img class="_3nYIo3" src="//upload.jianshu.io/users/upload_avatars/174711/4a2fedd6424e?imageMogr2/auto-orient/strip|imageView2/1/w/120/h/120/format/webp" alt="  "></a><div class="_2lfNuF"><div class="Cqpr1X" title="lchad"><a class="_1OhGeD" href="/u/9b40ae19f574" target="_blank" rel="noopener noreferrer">lchad</a></div><div class="_2qBui4"><span>拥有1钻 (约0.35元)</span></div></div><button data-locale="zh-CN" type="button" class="_1OyPqC _3Mi9q9"><span>关注</span></button></div><div class="VwEQ52 _13lIbp"><div class="_2lfNuF"><div class="Cqpr1X">"小礼物走一走，来简书关注我"</div></div><button type="button" class="_1OyPqC _3Mi9q9"><span>赞赏</span></button></div></div></div></section>

