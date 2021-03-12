---
title: '前端框架之webpack介绍'
date:       2019-09-21
tags:
	- web
	- html
	- basis
---
  
### 概念  
本质上，webpack 是一个现代 JavaScript 应用程序的静态模块打包器(module bundler)。当 webpack 处理应用程序时，它会递归地构建一个依赖关系图(dependency graph)，其中包含应用程序需要的每个模块，然后将所有这些模块打包成一个或多个 bundle。  
  
  
### 模块(modules)  
在模块化编程中，开发者将程序分解成离散功能块`(discrete chunks of functionality)`，并称之为模块。  
  
每个模块具有比完整程序更小的接触面，使得校验、调试、测试轻而易举。 精心编写的模块提供了可靠的抽象和封装界限，使得应用程序中每个模块都具有条理清楚的设计和明确的目的。  
  
Node.js 从最一开始就支持模块化编程。然而，在 web，模块化的支持正缓慢到来。在 web 存在多种支持 JavaScript 模块化的工具，这些工具各有优势和限制。webpack 基于从这些系统获得的经验教训，并将模块的概念应用于项目中的任何文件。  
  
### 什么是 webpack 模块  
对比 Node.js 模块，webpack 模块能够以各种方式表达它们的依赖关系，几个例子如下：  
  
ES2015 import 语句  
CommonJS require() 语句  
AMD define 和 require 语句  
css/sass/less 文件中的 @import 语句。  
样式`(url(...))`或 HTML 文件`(<img src=...>)`中的图片链接`(image url)`  
  
