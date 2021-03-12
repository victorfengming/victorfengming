---
title: "解决VSCode报错"
date:       2020-03-04
subtitle: "因为在此系统上禁止运行脚本"
tags:
	- solution
	- ide
---




很多小伙伴在使用VSCODE自带的terminal的时候会报出"系统禁止脚本运行的错误",

小编找了下原因，是因为PowerShell执行策略的问题。

解决方法：

1. 以管理员身份运行vscode;
2. 执行：get-ExecutionPolicy，显示Restricted，表示状态是禁止的;
3. 执行：set-ExecutionPolicy RemoteSigned;
4. 这时再执行get-ExecutionPolicy，就显示RemoteSigned;

之后就不再有问题。