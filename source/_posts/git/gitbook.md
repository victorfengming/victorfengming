---
title: "Gitbook安装问题"
cover: "/img/lynk/84.jpg"
date:       2021-02-04
subtitle: "问题解决"
tags:
	- gitbook
---

安装gitbook ,由于原来的 安装环境中的文件没有删除干净,导致一直安装不上,

只需要将对应的文件删除了即可

现在解决就

```shell script
E:\Projects\IdeaProjects\gitbook\other_gitbook>
E:\Projects\IdeaProjects\gitbook\other_gitbook>npm install -g gitbook-cli
npm WARN rollback Rolling back is-fullwidth-code-point@2.0.0 failed (this is probably harmless): EPERM: operation not permitted, lstat 'C:\Users\Administrator\AppData\Roaming\npm\node_modules\gitbo
ok-cli\node_modules\npm\node_modules\update-notifier\node_modules\boxen\node_modules\string-width\node_modules'
npm WARN rollback Rolling back strip-ansi@4.0.0 failed (this is probably harmless): EPERM: operation not permitted, lstat 'C:\Users\Administrator\AppData\Roaming\npm\node_modules\gitbook-cli\node_m
odules\npm\node_modules\update-notifier\node_modules\boxen\node_modules\string-width\node_modules'
npm WARN rollback Rolling back number-is-nan@1.0.1 failed (this is probably harmless): EPERM: operation not permitted, lstat 'C:\Users\Administrator\AppData\Roaming\npm\node_modules\gitbook-cli\nod
e_modules\npm\node_modules\update-notifier\node_modules\boxen\node_modules\widest-line\node_modules\string-width\node_modules\is-fullwidth-code-point\node_modules'
npm WARN rollback Rolling back copy-concurrently@1.0.3 failed (this is probably harmless): EPERM: operation not permitted, lstat 'C:\Users\Administrator\AppData\Roaming\npm\node_modules\gitbook-cli
\node_modules\npm\node_modules\move-concurrently\node_modules'
npm WARN rollback Rolling back has-ansi@2.0.0 failed (this is probably harmless): EPERM: operation not permitted, scandir 'C:\Users\Administrator\AppData\Roaming\npm\node_modules\gitbook-cli\node_m
odules\npm\node_modules\update-notifier\node_modules\chalk\node_modules'
npm WARN rollback Rolling back defaults@1.0.3 failed (this is probably harmless): EPERM: operation not permitted, lstat 'C:\Users\Administrator\AppData\Roaming\npm\node_modules\gitbook-cli\node_mod
ules\npm\node_modules\columnify\node_modules\wcwidth\node_modules'
npm WARN rollback Rolling back registry-url@3.1.0 failed (this is probably harmless): EPERM: operation not permitted, scandir 'C:\Users\Administrator\AppData\Roaming\npm\node_modules\gitbook-cli\no
de_modules\npm\node_modules\update-notifier\node_modules\latest-version\node_modules\package-json\node_modules'
npm WARN rollback Rolling back asn1@0.2.3 failed (this is probably harmless): EPERM: operation not permitted, scandir 'C:\Users\Administrator\AppData\Roaming\npm\node_modules\gitbook-cli\node_modul
es\npmi\node_modules\npm\node_modules\request\node_modules\http-signature\node_modules\sshpk\node_modules'
npm WARN rollback Rolling back http-signature@1.1.1 failed (this is probably harmless): EPERM: operation not permitted, scandir 'C:\Users\Administrator\AppData\Roaming\npm\node_modules\gitbook-cli\
node_modules\npmi\node_modules\npm\node_modules\request\node_modules'
npm ERR! code EEXIST
npm ERR! path C:\Users\Administrator\AppData\Roaming\npm\node_modules\gitbook-cli\bin\gitbook.js
npm ERR! dest C:\Users\Administrator\AppData\Roaming\npm\gitbook
npm ERR! EEXIST: file already exists, cmd shim 'C:\Users\Administrator\AppData\Roaming\npm\node_modules\gitbook-cli\bin\gitbook.js' -> 'C:\Users\Administrator\AppData\Roaming\npm\gitbook'
npm ERR! File exists: C:\Users\Administrator\AppData\Roaming\npm\gitbook
npm ERR! Remove the existing file and try again, or run npm
npm ERR! with --force to overwrite files recklessly.

npm ERR! A complete log of this run can be found in:
npm ERR!     C:\Users\Administrator\AppData\Roaming\npm-cache\_logs\2021-02-04T13_02_46_864Z-debug.log

E:\Projects\IdeaProjects\gitbook\other_gitbook>npm install -g gitbook-cli
C:\Users\Administrator\AppData\Roaming\npm\gitbook -> C:\Users\Administrator\AppData\Roaming\npm\node_modules\gitbook-cli\bin\gitbook.js
+ gitbook-cli@2.3.2
added 578 packages from 672 contributors in 16.351s

```

### 第二个问题

```shell script
E:\Projects\IdeaProjects\gitbook\other_gitbook>gitbook -V
CLI version: 2.3.2
Installing GitBook 3.2.3
C:\Users\Administrator\AppData\Roaming\npm\node_modules\gitbook-cli\node_modules\npm\node_modules\graceful-fs\polyfills.js:287
      if (cb) cb.apply(this, arguments)
                 ^

TypeError: cb.apply is not a function
    at C:\Users\Administrator\AppData\Roaming\npm\node_modules\gitbook-cli\node_modules\npm\node_modules\graceful-fs\polyfills.js:287:18
    at FSReqCallback.oncomplete (fs.js:169:5)


```


这行代码就是检查的,没鸡儿用

```javascript

function statFix (orig) {
  if (!orig) return orig
  // Older versions of Node erroneously returned signed integers for
  // uid + gid.
  return function (target, cb) {
    return orig.call(fs, target, function (er, stats) {
      if (!stats) return cb.apply(this, arguments)
      if (stats.uid < 0) stats.uid += 0x100000000
      if (stats.gid < 0) stats.gid += 0x100000000
      // if (cb) cb.apply(this, arguments)
      // 直接就给他注释掉,完美!perfect 
    })
  }
}

```

__注意__



这里不能直接注释 掉if (cb) cb.apply(this, arguments)

需要注释掉62-64行

```javascript
  // fs.stat = statFix(fs.stat)
  // fs.fstat = statFix(fs.fstat)
  // fs.lstat = statFix(fs.lstat)
```

看完这些commit的记录

物是人非

19 20 21年的提交都在这里

刻出了时光的痕迹


