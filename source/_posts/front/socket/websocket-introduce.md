---
title: "websocket初识"
date:       2019-08-30
tags:
	- socket
	- web
	- basis
---

### websocket的基本概念
websocket协议是基于TCP的一种新的网络协议。它实现了浏览器与服务器（full-duplex）通信-允许服务区主动发送信息给客户端。

websocket是一种持久协议，http是非持久协议

现在很多网站都有实施推送的需求，比如聊天，客服咨询等

早期没有websocket时，通过ajax轮询

websocket是一种网络协议，允许客户端和服务端全双工的进行网络通信。服务器可以给客户端发消息，客户端也可以给服务端发消息。

这种方式十分节省性能  
要是ajax轮循，http的握手过程是十分耗性能的

### 在H5中，如何使用websocket


###　websocket事件


|事件|事件处理程序|描述|
|---|---|---|
|open|Socket.onopen|连接建立时触发|
|message|Socket.onmessage|客户端接受服务端数据时触发|
|error|Socket.onerror|通信发生错误时触发|
|close|Socket.onclose|连接关闭时触发|