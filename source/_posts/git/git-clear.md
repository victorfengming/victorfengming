---
title: "删除github上的commit历史记录"
date:       2019-10-17
tags:
	- Git
	- solution
---












### 起步
今天小编发现了git克隆下来的远程库特别大:

经过查询之后发现是每次推送之后都会留下记录缓存，这样很多没用的记录就会占用多余的空间，别人克隆的时候也会多耗费时间，今天我查到了一个清除无用记录的方法。

```cmd

# 克隆你的远程仓库
git clone git@github.com:victorfengming/victorfengming.github.io.git

# 进入你的本地库
cd victorfengming.github.io

# 新建并切换到一个分支
git checkout –orphan latest_branch

# 选中全部文件
git add -A

# 提交
git commit -am “Reinitialize”

# 删除原分支
git branch -D master

# 将本分支改为原分支名
git branch -m master

# 推送到远程分支
git push -f origin master
```

现在你再去GitHub上去看提交分支的记录，会发现只有一次提交了

可以删除本地库重新将远程库克隆下来，这次就没有那些多余的提交记录了！