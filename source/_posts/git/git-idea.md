---
title: "在idea中使用git管理你的项目"
date:       2019-10-14
tags:
	- Git
	- solution
	- idea
---












### 起步
idea是十分智能的Java集成开发环境

而我们在用idea写项目的时候经常遇到版本控制的问题,而git工具如果你只会在终端中的git命令来进行控制,可能会使得效率低下

今天小编就教大家在idea中使用git

### 首先创建一个项目

![开启](/img/posts/git/idea_git/1.png)
点击create new projects
![创建项目](/img/posts/git/idea_git/2.png)
这里选择默认的就可以,关于jdk的安装可以参考[ubuntu系统下Java环境JDK的安装](https://victorfengming.gitee.io/2019/09/04/ubuntu-install-jdk/)和[Deepin下java开发环境部署](https://victorfengming.gitee.io/2019/09/04/deepin-install-jdk/)

![创建项目2](/img/posts/git/idea_git/3.png)

这里是询问我们需不需要从模板创建项目,直接点击next即可

![创建项目](/img/posts/git/idea_git/4.png)

这里填写项目的名称和位置

填完后,点击finish即可

### 在idea中登录你的github

刚刚创建的Java项目是这样的
![创建项目](/img/posts/git/idea_git/5.png)

我们需要点击设置
![setting](/img/posts/git/idea_git/6.png)

在设置中搜索git
![git](/img/posts/git/idea_git/7.png)

选择git下面的github
![git](/img/posts/git/idea_git/8.png)

在右边点击`+`号
![github](/img/posts/git/idea_git/9.png)

输入你的github的账号和密码
![github](/img/posts/git/idea_git/10.png)

这里可以勾选ssh协议,关于ssh的配置可以参考:[git生成SSH并提交](https://victorfengming.gitee.io/2019/08/19/github-generate-ssh/)

配置好后
点击OK即可

**注意**:
登录github之后
项目中文件的颜色将会变为`褐色`

### 创建一个github仓库,并将项目交给git来管理

点击菜单栏的VCS->Import into Version Control->Create Git Repository

![交给git管理](/img/posts/git/idea_git/11.png)

这里我们选中项目文件夹即可

![仓库](/img/posts/git/idea_git/12.png)


### 新建一个类,测试运行

![仓库](/img/posts/git/idea_git/13.png)
创建好了一个空类

![仓库](/img/posts/git/idea_git/14.png)
写一个简单的helloworld代码

![仓库](/img/posts/git/idea_git/15.png)

运行一下,测试效果
![仓库](/img/posts/git/idea_git/16.png)

运行成功
### 添加到本地(add)
注意上面的文件名称为`红色`的

然后我们在项目文件夹上面右键->选择Git->add

![仓库](/img/posts/git/idea_git/17.png)

add 之后

项目中文件的颜色将会变为`绿色`

![仓库](/img/posts/git/idea_git/18.png)

### 提交的本地仓库(commit)

我们在项目文件夹上面右键->选择Git->Commit Directory

![仓库](/img/posts/git/idea_git/19.png)

这里填写一些我们关于这此提交的说明或注释
![仓库](/img/posts/git/idea_git/20.png)

commit之后
项目中文件的颜色将会变为`白色`
![仓库](/img/posts/git/idea_git/21.png)

### 推本地存储库到远程仓库(push)

首先我们需要在github中创建一个存储库

关于git可以参考:[git个人整理总结](https://victorfengming.gitee.io/2019/08/21/progit-min/),关于github使用,可以参考:[GitHub使用教程](https://blog.csdn.net/nyist327/article/details/38900721)

![仓库](/img/posts/git/idea_git/23.png)
repository创建好后,复制远程仓库的地址,这里我们使用的是SSH协议(当然你也可以使用HTTPS的协议)

关于ssh的配置可以参考:[git生成SSH并提交](https://victorfengming.gitee.io/2019/08/19/github-generate-ssh/)

![仓库](/img/posts/git/idea_git/24.png)

然后我们回到idea中

在项目文件夹上面右键->选择Git->Repository->Push (或者按快捷键Ctrl+shift+K)

![打开push](/img/posts/git/idea_git/25.png)

在弹出的窗口中点击define remote
![remote](/img/posts/git/idea_git/26.png)

这里我们需要填写名称和远程仓库的地址
直接将刚才复制好的远程仓库的地址粘贴进来即可
![ssh地址](/img/posts/git/idea_git/27.png)

点击OK稍等片刻
![配置remote](/img/posts/git/idea_git/28.png)

右面会出现刚刚commit后的本地仓库中的文件列表
![push文件列表](/img/posts/git/idea_git/29.png)

点击Push即可推到远程仓库中
![状态栏](/img/posts/git/idea_git/30.png)
在idea下面的状况栏中可以查看进度,和分支的一些详细信息

回到github中,刷新你的存储库的页面,会发现刚才push的文件已经存到你的远程仓库中了

![远程仓库](/img/posts/git/idea_git/31.png)

### 克隆远程的git项目到本地(clone)

先在github中复制你的远程仓库地址(这里使用sh协议)

![状态栏](/img/posts/git/idea_git/32.png)

然后回到idea中

点击菜单栏中 VCS -> check from version control-> Git

![状态栏](/img/posts/git/idea_git/33.png)

将你的url粘贴进去
![状态栏](/img/posts/git/idea_git/34.png)

点击Test进行测试连接,如果现实connection successful 即为连接成功
![状态栏](/img/posts/git/idea_git/35.png)

然后点击clone 即可克隆到本地

![状态栏](/img/posts/git/idea_git/36.png)
这里克隆成功后会询问你要不要在idea中打开它

这里我们选择取消即可,然后重新打开刚刚克隆的项目即可

### 拉取远程的git项目到本地(pull)
如果你想要push你的修改,但是这是其他人也对项目进行了修改,这就有可能会导致merge失败,所以在你push前,需要先pull拉去最新的版本,再进行push你的提交

进入idea中

在项目文件夹上面右键->选择Git->Repository->Pull 

![状态栏](/img/posts/git/idea_git/37.png)

这里点击pull即可拉取远程仓库的最新修改
![状态栏](/img/posts/git/idea_git/38.png)

这样,在你下一次push 的时候,就可以选择哪个分支来处理版本之间的冲突了



