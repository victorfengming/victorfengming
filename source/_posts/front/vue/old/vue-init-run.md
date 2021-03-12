---
title: "初始化vue项目并启动"
cover: "/img/lynk/17.jpg"
date:       2019-09-17
tags:
	- web
	- vue
	- basis
---

### 初始化vue项目
项目起名为`vue-playlist`
```JavaScript
victor@asus:~/WebstormProjects/vuejs/vue_demo2$ vue init webpack vue-playlist
```
确认项目名字,这里我们直接就一个回车,默认的名字不用改
```
? Project name vue-playlist
```
下面是添加对于项目的描述
```
? Project description Vue基础知识
```
作者的信息,默认就行了,直接就一个回车
```
? Author fengming <victorfm@163.com>
```
```
? Vue build standalone
```
下面的对于我们新手来说暂时不需要,直接就一个no就行了哦 
```
? Install vue-router? No
? Use ESLint to lint your code? No
? Set up unit tests No
? Setup e2e tests with Nightwatch? No
```
这里问我们是否运行npm来创建项目
```
? Should we run `npm install` for you after the project has been created? (recommended) np
m

   vue-cli · Generated "vue-playlist".

```
下面在安装项目所需要的依赖
```
# Installing project dependencies ...
# ========================

npm WARN deprecated extract-text-webpack-plugin@3.0.2: Deprecated. Please use https://github.com/webpack-contrib/mini-css-extract-plugin
npm WARN deprecated browserslist@2.11.3: Browserslist 2 could fail on reading Browserslist >3.0 config used in other tools.
npm WARN deprecated bfj-node4@5.3.1: Switch to the `bfj` package for fixes and new features!
npm WARN deprecated flatten@1.0.2: I wrote this module a very long time ago; you should use something else.
npm WARN deprecated browserslist@1.7.7: Browserslist 2 could fail on reading Browserslist >3.0 config used in other tools.

> core-js@2.6.9 postinstall /home/victor/WebstormProjects/vuejs/vue_demo2/vue-playlist/node_modules/core-js
> node scripts/postinstall || echo "ignore"

Thank you for using core-js ( https://github.com/zloirock/core-js ) for polyfilling JavaScript standard library!

The project needs your help! Please consider supporting of core-js on Open Collective or Patreon: 
> https://opencollective.com/core-js 
> https://www.patreon.com/zloirock 

Also, the author of core-js ( https://github.com/zloirock ) is looking for a good job -)


> uglifyjs-webpack-plugin@0.4.6 postinstall /home/victor/WebstormProjects/vuejs/vue_demo2/vue-playlist/node_modules/webpack/node_modules/uglifyjs-webpack-plugin
> node lib/post_install.js

npm notice created a lockfile as package-lock.json. You should commit this file.
npm WARN ajv-keywords@3.4.1 requires a peer of ajv@^6.9.1 but none is installed. You must install peer dependencies yourself.
npm WARN optional SKIPPING OPTIONAL DEPENDENCY: fsevents@1.2.9 (node_modules/fsevents):
npm WARN notsup SKIPPING OPTIONAL DEPENDENCY: Unsupported platform for fsevents@1.2.9: wanted {"os":"darwin","arch":"any"} (current: {"os":"linux","arch":"x64"})

added 1215 packages from 670 contributors and audited 11812 packages in 156.77s
found 10 vulnerabilities (6 moderate, 4 high)
  run `npm audit fix` to fix them, or `npm audit` for details
```
到这里项目初始化成功
```
# Project initialization finished!
# ========================
```
需要我们进入项目目录,使用npm来启动项目
```
To get started:

  cd vue-playlist
  npm run dev
  
Documentation can be found at https://vuejs-templates.github.io/webpack
```
进入项目文件夹中后,执行启动命令`npm run dev`
```js
victor@asus:~/WebstormProjects/vuejs/vue_demo2/vue-playlist$ npm run dev

> vue-playlist@1.0.0 dev /home/victor/WebstormProjects/vuejs/vue_demo2/vue-playlist
> webpack-dev-server --inline --progress --config build/webpack.dev.conf.js

 12% building modules 20/29 modules 9 active ...js/vue_demo2/vue-playlist/src/App.vue{ parser: "babylon" } is deprecated; we now treat it as { parser: "babel" }.
 95% emitting                                                                        

 DONE  Compiled successfully in 8720ms                                            16:34:56

 I  Your application is running here: http://localhost:8080
 
```
到这里即可在本地服务器访问你的项目了
```
地址为:http://localhost:8080
```
![vuehelloworld](/img/posts/vue/vuejs4.png)


