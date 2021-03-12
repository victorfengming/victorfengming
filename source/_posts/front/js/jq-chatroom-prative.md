---
title: '慕课网轮播图100%还原'
date:       2019-09-05
tags:
	- JavaScript
	- web
	- solution
---












### 骨架
```html
<!DOCTYPE html>
<html>
<head>
    <title></title>
    <script src="http://libs.baidu.com/jquery/2.0.0/jquery.min.js"></script>
</head>

<body>
<div id="main">
    <img src="./img/1.png">
    <img src="./img/2.png">
    <img src="./img/3.png">
    <img src="./img/4.png">
    <img src="./img/5.png">
    <img src="./img/6.png">
</div>
<div>
    <a href="javascript:;"><div id="leftside" class="side"></div></a>
    <a href="javascript:;"><div id="rightside" class="side"></div></a>

    <ul id="ul">
        <li class='lili' name="1">&nbsp;</li>
        <li class='lili' name="2">&nbsp;</li>
        <li class='lili' name="3">&nbsp;</li>
        <li class='lili' name="4">&nbsp;</li>
        <li class='lili' name="5">&nbsp;</li>
        <li class='lili' name="6">&nbsp;</li>
    </ul>

    <div id="test">

    </div>
</div>

</body>
</html>
```
### 样式
```
<style type="text/css">
    img{
        position: absolute;
        width: 936px;
        height: 316px;
    }

    .side{
        font-size: 25px;
        position: absolute;
        color: rgba(255, 255, 255, 0.6);
        width: 36px;
        height: 60px;

    }

    .side:hover{
        background-color: rgba(7, 17, 27, 0.6);
        border-radius: 3px;

    }

    .side:only-child{
        height: 60px;

    }

    #leftside{

        left: 10px;
        top: 140px;

    }

    #rightside{

        left: 906px;
        top: 140px;
    }

    ul{
        list-style-type: none;
        position: absolute;
        left: 775px;
        top: 270px;
    }

    li{
        /*position: ;*/
        float: left;
        text-align: center;
        cursor: pointer;
        width: 18px;
        height: 20px;
    }

    .yuan{
        width: 20px;
        height: 20px;
    }

    #test{
        width: 20px;
        height: 20px;
        top: 100px;
        left: 100px;
        background-color: red;
    }
</style>
```

### 脚本
```
<script>
    var n = 0;
    function update_img(n) {
        // 隐藏全部
        $("#main").children().hide();
        //显示当前
        $('#main').children().eq(n).fadeIn();
        // 更新变量
    }

    //更改函数
    function change(){
        // 设置次数
        n = n>=6?0:n;
        update_img(n);
        n++;
    }

    timer1 = setInterval(change, 1500);

    // 监听鼠标进入,清除定时器
    $('#main').mouseenter(function () {
        clearInterval(timer1)
    });
    // 监听鼠标离开,开启定时器
    $('#main').mouseleave(function () {
        // 实在整不出来,假装实现了
        // window.location.reload();
        timer1 = setInterval(change, 1500);
    });

    // 监听鼠标点击事件
    $('#rightside').click(function () {
        n = n>=6?0:n;
        update_img(n);
        n++;
    });

    // 监听鼠标点击事件
    $('#leftside').click(function () {
        n = n<=-1?6:n;
        update_img(n);
        n--;
    });


    for(var i=0; i<6; i++){
        $('#ul').children().eq(i).click(function () {
        console.log(this);
        m = this.getAttribute("name");
        console.log(m);
        update_img(m-1);
    })
    }

</script>
```