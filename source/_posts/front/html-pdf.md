---
title: '如何直接在网页中显示PDF文件'
date:       2019-10-19
tags:
	- web
	- html
	- solution
---


版权声明：本文为CSDN博主「北方的刀郎」的原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接及本声明。

原文链接：https://blog.csdn.net/forest_fire/article/details/50944069

博客分类： web开发
 
### 1、
```html
<embed width="800" height="600" src="test_pdf.pdf"> </embed> 
```
通过的浏览器：360、Firefox、IE、Chrome 
### 2、

```html
<object classid="clsid:CA8A9780-280D-11CF-A24D-444553540000" width="800" height="600" border="0"> 

<param name="SRC" value="test_pdf.pdf"> 

</object> 
```

### 下面这个完整点： 

```html
<object classid="clsid:CA8A9780-280D-11CF-A24D-444553540000" width="100%" height="100%" border="0"><!--IE--> 
      <param name="_Version" value="65539"> 
      <param name="_ExtentX" value="20108"> 
      <param name="_ExtentY" value="10866"> 
      <param name="_StockProps" value="0"> 
      <param name="SRC" value="testing_pdf.pdf"> 
<embed src="testing_pdf.pdf" width="100%" height="800" href="testing_pdf.pdf"></embed><!--FF--> 
</object> 
```

通过的浏览器：360、IE 

未通过的浏览器：Firefox、Chrome 

3、
```html
<iframe src="test_pdf.pdf" width="800" height="600"></iframe> 
```

通过的浏览器：360、Firefox、IE、Chrome 

4、用浏览器直接访问http://127.0.0.1/test_pdf.pdf (其实这个不算是在网页内吧) 

通过的浏览器：360、Firefox、IE、Chrome 

以上四种方式均在WinXP下。（之前有碰到过上传的功能在Win7下失效的情况，故在此说明一下OS）


--------------------------------------------------------
今天有一需求，要在网页中显示pdf，于是立马开始搜索解决方案，无意中发现一个非常好的解决方法，详见http://blogs.adobe.com/pdfdevjunkie/web_designers_guide。

其实就光看这个网站也足够了，http://www.pdfobject.com/。



记录一下主要代码：

pdfobject.js 下载:http://pan.baidu.com/s/1kTJTiqr     http://pan.baidu.com/s/1kTJTiqr

```html
<script type="text/javascript" src="scripts/pdfobject/pdfobject.js"></script>
<script type="text/javascript"> 
window.onload = function (){
    var success = new PDFObject({ url: "pdf/CGVET22-08-2011V2P.pdf" ,pdfOpenParams: { scrollbars: '0', toolbar: '0', statusbar: '0'}}).embed("pdf1");
};
</script> 
 
<div id="pdf1" style="width:700px; height:600px;">It appears you don't have Adobe Reader or PDF support in this web browser. <a href="~/pdf/CGVET22-08-2011V2P.pdf">Click here to download the PDF</a></div>
```