---
title: "node+socket+jq 实现简易聊天室"
cover: "/img/lynk/73.jpg"
date:       2019-09-03
tags:
	- node
	- web
	- server
	- solution
---












直接上代码

### 前台部分（client.html)
```html
<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport"
          content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <script src="http://libs.baidu.com/jquery/2.0.0/jquery.min.js"></script>
<!--    导入socket.io-->
<script type="text/javascript" src="http://wulv5.com/js/socket.io.min.js"></script>
    <title>Document</title>
</head>
<body>

<div id="main">
    <div id="title">
        花里胡哨的聊天室
    </div>
    <input type="text" id="shuru">
    <button id="btn">send it</button>
    <div id="record"></div>
</div>

<style>

*{
margin: 0;
padding: 0;
font-size: 100%;
}

#main{
    width: 800px;
    margin: 0 auto;
}

#title{
    width: 700px;
    font-size: 50px;
    color: deeppink;
    margin: 0 auto;
}

#shuru{
    position: relative;
    width: 500px;
    height: 50px;
    margin: 0 auto;
    font-size: 45px;
    border-radius: 15px;
    border: 2px solid lightsalmon;

}

#btn{
    height: 55px;
    font-size: 30px;
    background-color: greenyellow;
    margin: auto auto;
    border-radius: 15px;
    text-align: left;
    border: 2px solid lightsalmon;
}

.son{

    border: 1px solid lightsalmon;
    font-size: 30px;
    background-color: blueviolet;
    color: #ffffff;
    border-radius: 15px;
    width: 600px;

}
</style>

<script>

    // 链接聊天室的io服务器
    var socket = io.connect('/');
    // 监听点击事件
    $('#btn').click(function () {
        socket.send($('#shuru').val());
        $('#shuru').val('');
    });
    // 输出服务端返回的信息
    socket.on('message', function (mes) {
        content = '<div class="son">' + '&nbsp;&nbsp;' +mes + "<br>"+'</div>';
        $('#record').append(content);
    })

</script>
</body>
</html>
```


### 后台部分(server.js)
```JavaScript
var http = require('http');

var fs = require('fs');

var ws = require('socket.io');

var server = http.createServer(function () {
    var html = fs.readFileSync('./client.html');
    res.end(html);
}).listen(1998);

var io = ws(server);

io.on('connection',function (socket) {
    socket.on('message',function (obj) {
        io.emit('message', obj)
    })
})
```

### 运行
`node server.js`
### 访问
在本机的ip地址中访问本地服务器即可  
`http://127.0.0.1:1998/`

![chatroom](/img/posts/node/chatroom.png)