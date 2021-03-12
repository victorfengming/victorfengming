---
title: 'js、jq获取当前鼠标位置'
date:       2019-09-10
tags:
	- JavaScript
	- web
	- jQuery
---












### 使用jQuery获取

```html
<html>
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=gb2312"/>
    <title>javascript获得鼠标位置</title>
    <script src="js/jquery.min.js"></script>
</head>
<body id="testDiv">

</body>
<script type="text/javascript">
    $('#testDiv').mousemove(function (e) {
        var xx = e.originalEvent.x || e.originalEvent.layerX || 0;
        var yy = e.originalEvent.y || e.originalEvent.layerY || 0;
        $(this).text(xx + '---' + yy);
        //var d = document.getElementById("div");获取某div在当前窗口的位置
        //var dx = xx - p.getBoundingClientRect().left;
        //var dy = yy - p.getBoundingClientRect().top;
        //$(this).text(dx + '---' + dy);鼠标在该div内位置
    });
</script>
</body>
```

### 使用JavaScript获取
```html
<html>
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=gb2312"/>
    <title>javascript获得鼠标位置</title>
</head>
<body>
鼠标X轴:
<input id=xxx type=text>
鼠标Y轴:
<input id=yyy type=text>
</body>
<script>
    function mouseMove(ev) {
        Ev = ev || window.event;
        var mousePos = mouseCoords(ev);
        document.getElementById("xxx").value = mousePos.x;
        document.getElementById("yyy").value = mousePos.y;
    }
    function mouseCoords(ev) {
        if (ev.pageX || ev.pageY) {
            return {x: ev.pageX, y: ev.pageY};
        }
        return {
            x: ev.clientX + document.body.scrollLeft - document.body.clientLeft,
            y: ev.clientY + document.body.scrollTop - document.body.clientTop
        };
    }
    document.onmousemove = mouseMove;
</script>
</html>
```


