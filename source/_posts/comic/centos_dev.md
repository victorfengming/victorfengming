---
title: 'Centos部署前端命令汇总'
cover: "/img/lynk/72.jpg"
date:       2021-11-03
tags:
  - node
  - node
  - git
  - linux
  - system
---


## 宝塔

### 安装

```shell
yum install -y wget && wget -O install.sh http://download.bt.cn/install/install_6.0.sh && sh install.sh
# ref https://www.bt.cn/bbs/thread-19376-1-1.html
```

### 卸载

```shell
wget http://download.bt.cn/install/bt-uninstall.sh
sh bt-uninstall.sh
```

## git

```
yum install -y git
```

## 创建用户

```shell
adduser work
# 设置密码
passwd work
# ref : https://blog.csdn.net/nieji3057/article/details/79421874
```

## nodejs

```
repo: https://nodejs.org/dist/latest-v16.x/
```

```shell
tar -xzvf node-v16.13.0-xxx
```



2、通过ftp工具上传到linux服务，解压安装包

```
tar -xvf node-v10.16.0-linux-x64.tar.xz
```

3、移动并改名文件夹（不改名也行）

```
cd /usr/local/
mv /var/ftp/pub/node-v10.16.0-linux-64 . //后面的.表示移动到当前目录
mv node-v10.16.0.0-linux-64/ nodejs
```



4、让npm和node命令全局生效

方式一：环境变量方式（这种方式似乎只对登录用户有效？）

1）、加入环境变量，在 /etc/profile 文件末尾增加配置

```
vi /etc/profileexport PATH=$PATH:/usr/local/nodejs/bin
```

2）、执行命令使配置文件生效

```
source /etc/profile
```

方式二：软链接方式（推荐）

```
ln -s /usr/local/nodejs/bin/npm /usr/local/bin/
ln -s /usr/local/nodejs/bin/node /usr/local/bin/
```

5、查看nodejs是否安装成功

```
node -vnpm -v
```





>
> ref : https://www.cnblogs.com/zhi-leaf/p/10979629.html
>




## nvm

### 安装Node.js版本管理工具nvm

```
curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.33.11/install.sh | bash
```

或者

```
wget -qO- https://raw.githubusercontent.com/creationix/nvm/v0.33.11/install.sh | bash
```

还可以用下面这种方法

```
git clone git://github.com/creationix/nvm.git ~/nvm
```

### 验证安装

```shell
command -v nvm
```

### 配置

设置nvm自动运行

```
echo "source ~/nvm/nvm.sh" >> ~/.bashrc
source ~/.bashrc
```

### 使用

查询Node.js版本

```
nvm list-remote
```

安装Node.js版本

```
nvm install v16.11.1
```

切换Node.js版本

```
nvm use v7.6.0
```

升级npm

```
npm -g install npm@5.7.1
```

> ref : https://www.cnblogs.com/ycyzharry/p/10186251.html

### 换源

当前nvm在github上的最新版本是0.33.8，首先运行：

```
curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.33.8/install.sh | bash
```

待到安装完成提示用户设置环境变量的时候，修改`.bash_profile`，在末尾加入：

```shell
echo "export NVM_NODEJS_ORG_MIRROR=http://npm.taobao.org/mirrors/node" >> ~/.bash_profile
echo "export NVM_DIR=\"$HOME/.nvm\"" >> ~/.bash_profile
echo "[ -s \"$NVM_DIR/nvm.sh\" ] && \. \"$NVM_DIR/nvm.sh\"" >> ~/.bash_profile
echo "[ -s \"$NVM_DIR/bash_completion\" ] && \. \"$NVM_DIR/bash_completion\"" >> ~/.bash_profile
```



随后使配置生效，运行

```
cd ~
source .bash_profile
```

当前，使配置生效的方法还有直接退出终端，新开一个终端的方法。
运行：

```
nvm ls
nvm ls-remote
```

就可以分别查看本地已经安装的版


> ref : https://blog.csdn.net/caoshiying/article/details/79580261

### npm换源

```
npm config set registry https://registry.npm.taobao.org
```
// 配置后可通过下面方式来验证是否成功
 ```
npm config get registry
 
// 或npm info express
 ```

> ref: https://www.jianshu.com/p/0deb70e6f395

## ssh

```shell
cd ~
ll -a
cd /home/work

# 测试一下
ping 49.233.107.254
scp -r -v /home/work/a play@49.223.107.254:/home/play/

# 实际的
scp -r /home/work/.ssh play@49.223.107.254:/home/play/

```



### 改.ssh权限

```shell
cd ~
# 查看
ll -a
# 改权限
chmod 600  /home/play/.ssh/*
```



## 拉代码

```shell
git clone git@github.com:moderateReact/moderate-react-template.git
```

