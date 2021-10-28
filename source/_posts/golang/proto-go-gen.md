---
title: "proto安装&go-proto编写"
date:       2021-10-28 
cover: "/img/lynk/5.jpg"
date: 2018-12-21 
tags: XDH
---

## proto 安装

https://hub.fastgit.org/protocolbuffers/protobuf/releases/tag/v3.13.0

下载对应版本

解压

把解压目录/bin 加入path变量中

使之生效

## proto-go 安装

```go
package main

import (
	"fmt"

	_ "github.com/golang/protobuf/protoc-gen-go"
	_ "github.com/grpc-ecosystem/grpc-gateway/v2/protoc-gen-grpc-gateway"
	_ "github.com/grpc-ecosystem/grpc-gateway/v2/protoc-gen-openapiv2"
	_ "google.golang.org/grpc/cmd/protoc-gen-go-grpc"
)

func main() {
	fmt.Println("hello")
}

```

```shell
go mod tidy
```

保证正确安装protobuf，已经在$GOPATH\bin目录下生成了protoc-gen-go.exe二进制文件。

把这个二进制文件剪切复制到$DOROOT\bin目录下即可：

---

## 编写 proto文件

```proto
syntax = "proto3";
package coolcar;
option go_package="server/proto/gen/go;trippb";

message Trip{
    string start = 1;   // 第一个字段是 start
    string end = 2;     // 第二个字段是 end
    int64 duration_sec = 3; // duration in second
    int64 fee_cent = 4;
}
```

```shell
PS E:\Projects\GolandProjects\go-camp\mooc\code\coolcar\server\proto> pwd

Path
----
E:\Projects\GolandProjects\go-camp\mooc\code\coolcar\server\proto


PS E:\Projects\GolandProjects\go-camp\mooc\code\coolcar\server\proto> ls


    Directory: E:\Projects\GolandProjects\go-camp\mooc\code\coolcar\server\proto


Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
d-----        2021/10/28     16:29                gen
-a----        2021/10/28     16:27            285 trip.proto


PS E:\Projects\GolandProjects\go-camp\mooc\code\coolcar\server\proto>
```

```shell
protoc -I=E:\Projects\GolandProjects\go-camp\mooc\code\coolcar\server\proto --go_out=paths=source_relative:gen/go trip.proto
```


## reference

https://blog.csdn.net/ckx178/article/details/90721241


