---
title: 'JS中的定时器'
date:       2019-08-29
tags:
	- JavaScript
	- web
	- basis
---














### js定时器的制作  
在javascritp中，有两个关于定时器的专用函数，分别为：
```
1.倒计定时器：timename=setTimeout("function();",delaytime);  
2.循环定时器：timename=setInterval("function();",delaytime);
```

第一个参数“function()”是定时器触发时要执行的动作，可以是一个函数，也可以是几个函数，函数间用“；”隔开即可。比如要弹出两个警告窗口，便可将“function();”换成  
“alert('第一个警告窗口!');alert('第二个警告窗口!');”；而第二个参数“delaytime”则是间隔的时间，以毫秒为单位，即填写“5000”，就表示5秒钟。
　　

倒计时定时器是在指定时间到达后触发事件，而循环定时器就是在间隔时间到来时反复触发事件，两者的区别在于：前者只是作用一次，而后者则不停地作用。  


比如你打开一个页面后，想间隔几秒自动跳转到另一个页面，则你就需要采用倒计定时器“setTimeout("function();",delaytime)” ，而如果想将某一句话设置成一个一个字的出现，
则需要用到循环定时器“setInterval("function();",delaytime)” 。

获取表单的焦点，则用到document.activeElement.id。利用if来判断document.activeElement.id和表单的ID是否相同。
比如：if ("mid" == document.activeElement.id) {alert();},"mid"便是表单对应的ID。



定时器：
用以指定在一段特定的时间后执行某段程序。

JS中定时执行,setTimeout和setInterval的区别,以及l解除方法

```
setTimeout(Expression,DelayTime),在DelayTime过后,将执行一次Expression,setTimeout 运用在延迟一段时间，再进行某项操作。
setTimeout("function",time) 设置一个超时对象

setInterval(expression,delayTime),每个DelayTime,都将执行Expression.常常可用于刷新表达式.
setInterval("function",time) 设置一个超时对象

SetInterval为自动重复，setTimeout不会重复。

clearTimeout(对象) 清除已设置的setTimeout对象
clearInterval(对象) 清除已设置的setInterval对象
```


##略举两例。

### 例1.表单触发或加载时，逐字输出字符串

代码如下:
```html
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=gb2312" />
<title>无标题文档</title>
<script language="JavaScript" type="text/javascript">
var str = "这个是测试用的范例文字";
var seq = 0;
var second=1000; //间隔时间1秒钟
function scroll() {
msg = str.substring(0, seq+1);
document.getElementByIdx_x_x('word').innerHTML = msg;
seq++;
if (seq >= str.length) seq = 0;
}
</script>
</head>
<body onload="setInterval('scroll()',second)">
<div id="word"></div><br/><br/>
</body>
</html>
```
 
### 例2.当焦点在输入框的时候，定时检查输入框信息，焦点不在时不执行检查动作。

代码如下:
```html
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=gb2312" />
<title>无标题文档</title>
<script language="JavaScript" type="text/javascript">
var second=5000; //间隔时间5秒钟
var c=0;
function scroll() {
c++;
if ("b" == document.activeElement.id) {
var str="定时检查第<b> "+c+" </b>次<br/>";
if(document.getElementByIdx_x_x('b').value!=""){
str+="输入框当前内容为当前内容为<br/><b> "+document.getElementByIdx_x_x('b').value+"</b>";
}
document.getElementByIdx_x_x('word').innerHTML = str;
}
}
</script>
</head>
<body>
<textarea id="b" name="b" style="height:100px; width:300px;" onfocus="setInterval('scroll()',second)"></textarea><br/><br/>
<div id="word"></div><br/><br/>
</body>
</html>
```

### 例3.下面这个是最简单的例子，定时器时间到达后弹出警告窗口。

代码如下:
```html
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=gb2312" />
<script language="javascript">
function count() {
document.getElementByIdx_x_x('m').innerHTML="计时已经开始！";
setTimeout("alert('十秒钟到！')",10000)
}
</script>
<body>
<div id="m"></div>
<input TYPE="button" value=" 计时开始" onclick="count()">
</body>
</html>
```

### 例4:倒计时定时跳转

代码如下:
```
<html>
<head>
  <base href="<%=basePath%>">
  <title>My JSP 'ds04.jsp' starting page</title>
  <span id="tiao">3</span>
  <a href="javascript:countDown"> </a>秒后自动跳转……
  <meta http-equiv=refresh content=3;url= '/ds02.jsp'/>
  <!--脚本开始-->
  <script language="javascript" type="">
function countDown(secs){
 tiao.innerText=secs;
 if(--secs>0)
  setTimeout("countDown("+secs+")",1000);
 }
 countDown(3);
 </script>
  <!--脚本结束-->
 </head>
 </html>
```

### 例6:
代码如下:
```
<head> 
    <meta http-equiv="refresh" content="2;url='b.html'"> 
</head> 
```

### 例7:

代码如下:
```
<script language="javascript" type="text/javascript">
 setTimeout("window.location.href='b.html'", 2000);
 //下面两个都可以用
 //setTimeout("javascript:location.href='b.html'", 2000);
 //setTimeout("window.location='b.html'", 2000);
</script>
```

### 例8:

代码如下:
```
<span id="totalSecond">2</span>
<script language="javascript" type="text/javascript">
 var second = document.getElementByIdx_x('totalSecond').innerHTML;
 if(isNaN(second)){
  //……不是数字的处理方法
 }else{
  setInterval(function(){
   document.getElementByIdx_x('totalSecond').innerHTML = --second;
   if (second <= 0) {
    window.location = 'b.html';
   }
  }, 1000);
 } 
</script>
```

### js定时器(执行一次、重复执行)

分享一段js代码，有关js定时器的小例子，分为执行一次的定时器与重复执行的定时器。供初学的朋友参考。


### 1，只执行一次的定时器

代码如下:
```html
<script>  
//定时器 异步运行  
function hello(){  
    alert("hello");  
}  
//使用方法名字执行方法  
var t1 = window.setTimeout(hello,1000);  
var t2 = window.setTimeout("hello()",3000);//使用字符串执行方法  
window.clearTimeout(t1);//去掉定时器  
</script>
```

### 2，重复执行的定时器

代码如下:
```html
<script>  
function hello(){  
    alert("hello");  
}  
//重复执行某个方法  
var t1 = window.setInterval(hello,1000);  
var t2 = window.setInterval("hello()",3000);  
//去掉定时器的方法  
window.clearInterval(t1);  
</script>
```
备注：

如果在一个页面中有两个方法，都是在页面加载完成之后执行的，实际却未能按先后顺序执行，可以参照如下方法解决：
可以在onload方法中添加一个定时器，设置一个定时器，“延迟”一段时间之后再运行，即可认为区分页面加载运行方法的先后顺序。



代码如下:
```
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
    <title>Untitled Page</title>
    <script language="javascript" type="text/javascript">
    var YC = new Object();
    function beginYC()
    {
        var secondsYC = document.getElementById("txtYCSeconds").value;
        try
        { 
            YC = setTimeout("alert('延迟"+secondsYC+"秒成功')",secondsYC*1000);
        }
        catch(e)
        {
            alert("请输入正确的秒数。");
        }
    }
    function overYC()
    {
        clearTimeout(YC);
        YC=null;
        alert("终止延迟成功。");
    }

/**************************↓↓↓↓定时器的使用↓↓↓↓********************************/

    var timerDS = new Object();
    var timerDDS = new Object();
    function beginDS()
    {
        sn.innerHTML = "0";
        timerDS = setInterval("addOne()",parseInt(document.getElementById("txtIntervalSeconds").value,10)*1000);
    }
    function goonDS()
    {
        timerDS = setInterval("addOne()",parseInt(document.getElementById("txtIntervalSeconds").value,10)*1000);
    }
    function overDS()
    {
        clearInterval(timerDS);
        timerDS=null;
    }
    function delayDS()
    {
        overDS();
        timerDDS = setTimeout("goonDS()",document.getElementById("txtDDSSeconds").value*1000);
    }
    function addOne()
    {
        if(sn.innerHTML=="10")
        {
            overDS();
            alert("恭喜你，已成功达到10秒");
            return;
        }
        sn.innerHTML=parseInt(sn.innerHTML,10)+1;
    }

    </script>

</head>
<body>
    <form id="form1" runat="server">
    <div>
        延迟器的使用：</div>
    <div>
     <label id="Label2" title="延迟秒数："></label>
        <input type="text" id="txtYCSeconds" value="3" />
        <input type="button" id="btnBYC" onclick="javascript:beginYC()" value="开始延迟" />
        <input type="button" id="btnOYC" onclick="javascript:overYC()" value="终止延迟" />
        <input type="button" id="Button1" onclick="javascript:alert('good monrning');" value="普通弹窗" />
    </div>
    <br />
    <div>
        定时器的使用：</div>
    <div>
    <div id="sn">0</div>
    <label id="Label1" title="定时间隔秒数："></label>
        <input type="text" id="txtIntervalSeconds" value="1" />
        <input type="button" id="btnBDS" onclick="javascript:beginDS()" value="启动定时" />
        <input type="button" id="btnODS" onclick="javascript:overDS()" value="终止定时" />
        <input type="button" id="btnGDS" onclick="javascript:goonDS()" value="继续定时" />

        <label id="ds" title="延迟秒数："></label>
        <input type="text" id="txtDDSSeconds" value="5" />
        <input type="button" id="btnDDS" onclick="javascript:delayDS()" value="延迟定时" />

        </div>
    </form>
</body>
</html>
```
