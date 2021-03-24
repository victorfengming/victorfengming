---
title: "nodejs中的npm介绍"
cover: "/img/lynk/73.jpg"
date:       2019-08-27
tags:
	- node
	- background
	- server
	- basis
---












[nodejs安装](https://victorfengming.gitee.io/blog/nodejs-install/)后，还需要安装npm，本文中小编会带大家安装它  
### NPM是什么？
NPM是随同NodeJS一起安装的包管理工具，能解决NodeJS代码部署上的很多问题，常见的使用场景有以下几种：

- 允许用户从NPM服务器下载别人编写的第三方包到本地使用。
- 允许用户从NPM服务器下载并安装别人编写的命令行程序到本地使用。
- 允许用户将自己编写的包或命令行程序上传到NPM服务器供别人使用。 

由于新版的nodejs已经集成了npm，所以之前npm也一并安装好了。同样可以通过输入
"npm -v"
来测试是否成功安装。命令如下，出现版本提示表示安装成功:  
```
$ npm -v
2.3.0 
```
如果你安装的是旧版本的 npm，可以很容易得通过 npm 命令来升级，命令如下：
```
$ sudo npm install npm -g
/usr/local/bin/npm -> /usr/local/lib/node_modules/npm/bin/npm-cli.js
npm@2.14.2 /usr/local/lib/node_modules/npm
```
如果是 Window 系统使用以下命令即可： 
`npm install npm -g`  

### 全局安装与本地安装
npm 的包安装分为本地安装（local）、全局安装（global）两种，从敲的命令行来看，差别只是有没有-g而已，比如
```
npm install express          # 本地安装
npm install express -g   # 全局安装
```
如果出现以下错误：
`npm err! Error: connect ECONNREFUSED 127.0.0.1:8087 `  
解决办法为：
`$ npm config set proxy null`  

#### 本地安装
1. 将安装包放在 ./node_modules 下（运行 npm 命令时所在的目录），如果没有 node_modules 目录，会在当前执行 npm 命令的目录下生成 node_modules 目录。
2. 可以通过 require() 来引入本地安装的包。

#### 全局安装
1. 将安装包放在 /usr/local 下或者你 node 的安装目录。
2. 可以直接在命令行里使用。


如果你希望具备两者功能，则需要在两个地方安装它或使用 npm link。

### NPM 应用
NPM建立了一个NodeJS生态圈，NodeJS开发者和用户可以在里边互通有无。以下介绍NPM应用的三种场景：

#### 下载第三方包
我们可以使用以下命令来下载第三方包。
```
$ npm install argv
...
argv@0.0.2 node_modules\argv
```
下载好之后，argv包就放在了工程目录下的node_modules目录中，因此在代码中只需要通过require('argv')的方式就好，无需指定第三方包路径。

以上命令默认下载最新版第三方包，如果想要下载指定版本的话，可以在包名后边加上@<version>，例如通过以下命令可下载0.0.1版的argv。
```
$ npm install argv@0.0.1
...
argv@0.0.1 node_modules\argv
```
NPM对package.json的字段做了扩展，允许在其中申明第三方包依赖。因此，上边例子中的package.json可以改写如下：
```
{
    "name": "node-echo",
    "main": "./lib/echo.js",
    "dependencies": {
        "argv": "0.0.2"
    }
}    
```

这样处理后，在工程目录下就可以使用npm install命令批量安装第三方包了。

更重要的是，当以后node-echo也上传到了NPM服务器，别人下载这个包时，NPM会根据包中申明的第三方包依赖自动下载进一步依赖的第三方包。

例如，使用npm install node-echo命令时，NPM会自动创建以下目录结构。


```
- project/
    - node_modules/
        - node-echo/
            - node_modules/
                + argv/
            ...
    ...

```    
如此一来，用户只需关心自己直接使用的第三方包，不需要自己去解决所有包的依赖关系。

##### 安装命令行程序
从NPM服务上下载安装一个命令行程序的方法与第三方包类似。

例如上例中的node-echo提供了命令行使用方式，只要node-echo自己配置好了相关的package.json字段，对于用户而言，只需要使用以下命令安装程序。

`$ npm install node-echo -g`
参数中的-g表示全局安装，因此node-echo会默认安装到以下位置，并且NPM会自动创建好Linux系统下需要的软链文件或Windows系统下需要的.cmd文件。
```
- /usr/local/               # Linux系统下
    - lib/node_modules/
        + node-echo/
        ...
    - bin/
        node-echo
        ...
    ...

- %APPDATA%\npm\            # Windows系统下
    - node_modules\
        + node-echo\
        ...
    node-echo.cmd
    ...
```    
##### 发布代码
第一次使用NPM发布代码前需要注册一个账号。终端下运行npm adduser，之后按照提示做即可。

账号注册完成后，接着我们需要编辑package.json文件，加入NPM必需的字段。接着上边node-echo的例子，package.json里必要的字段如下。
```
{
    "name": "node-echo",           # 包名，在NPM服务器上须要保持唯一
    "version": "1.0.0",            # 当前版本号
    "dependencies": {              # 第三方包依赖，需要指定包名和版本号
        "argv": "0.0.2"
      },
    "main": "./lib/echo.js",       # 入口模块位置
    "bin" : {
        "node-echo": "./bin/node-echo"      # 命令行程序名和主模块位置
    }
}
```
之后，我们就可以在package.json所在目录下运行npm publish发布代码了。

### 版本号
使用NPM下载和发布代码时都会接触到版本号。NPM使用语义版本号来管理代码，这里简单介绍一下。

语义版本号分为X.Y.Z三位，分别代表主版本号、次版本号和补丁版本号。当代码变更时，版本号按以下原则更新。

如果只是修复bug，需要更新Z位。
如果是新增了功能，但是向下兼容，需要更新Y位。
如果有大变动，向下不兼容，需要更新X位。
版本号有了这个保证后，在申明第三方包依赖时，除了可依赖于一个固定版本号外，还可依赖于某个范围的版本号。例如"argv": "0.0.x"表示依赖于0.0.x系列的最新版argv。

NPM支持的所有版本号范围指定方式可以查看[官方文档](https://npmjs.org/doc/files/package.json.html#dependencies) 。


