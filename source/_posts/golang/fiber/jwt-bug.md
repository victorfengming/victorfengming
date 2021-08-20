---
title: "如何绕过dgrijalva/jwt go中的cve-2020-26160漏洞"
cover: "/img/lynk/62.jpg"
date:       2021-08-21
subtitle: "An Express inspired web framework"
tags:
    - Golang
    - Web
    - Fiber
---




# 如何绕过dgrijalva/jwt go中的cve-2020-26160漏洞


如何绕过dgrijalva/jwt go中的cve-2020-26160漏洞？

```golang
go jwt jwt-go
```

由于存在一个高级漏洞，Gitlab管道中无法传递容器安全状态。此漏洞为jwt-go，安装的版本为v3.2.0+incompatible。错误标题如下：jwt-go: access restriction bypass vulnerability-->avd.aquasec.com/nvd/cve-2020-26160。相关回购协议的Go版本为1.16.3。如何修复此漏洞？


CVE-2020-26160漏洞是由于dgrijalva/jwt-go错误地将JWTaud字段建模为string，而基于JWT规范，它应该是字符串的一部分。

在一般情况下，“aud”值是case-sensitive字符串的数组

你自己不能绕过它，因为它是库中的一个bug：`https://github.com/dgrijalva/jwt-go/issues/428`

切换到官方社区分支golang-jwt/jwt，其v3.2.1修复了漏洞：`https://github.com/golang-jwt/jwt/releases/tag/v3.2.1`

导入路径更改：有关更新代码的提示，请参见MIGRATION_GUIDE.md，将导入路径从`github.com/dgrijalva/jwt-go`更改为`github.com/golang-jwt/jwt`
修复了VerifyAudience（#12）中字符串和[]字符串之间的类型混淆问题。这修复了CVE-2020-26160


原文连接: https://www.5axxw.com/questions/content/o849sj




文档地址: https://docs.gofiber.io/


# helloworld

```go
package main

import "github.com/gofiber/fiber/v2"

func main() {
	app := fiber.New()

	app.Get("/", func(c *fiber.Ctx) error {
		return c.SendString("Hello, World!")
	})

	app.Listen(":3000")
}
```

# 其他案例

- [fiber-demo](https://gitee.com/victorfengming/fiber-demo/)