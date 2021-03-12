---
title: 'IDEA自动生成序列化ID'
date:       2019-10-30
tags:
	- ide
	- solution
	- idea
	
---

idea是十分智能的Java集成开发环境

而我们在用实体类继承 java.io.Serializable后，需要设置序列化ID。

java的序列化机制是通过在运行时判断类的serialVersionUID来验证版本一致性的。在进行反序列化时，JVM会把传来的字节流中的serialVersionUID与本地实体类中的serialVersionUID进行比较，如果相同则认为是一致的，便可以进行反序列化，否则就会报序列化版本不一致的异常。

而IDEA，默认是不支持自动生成序列化ID的（我使用的是IDEA2019版本）。

今天小编就交大家如何自定义设置自动生成序列化

### 1、安装 serialVersionUID 插件：

若你的IDEA已安装，则跳过此步骤；

若未安装，参考 [IDEA插件安装](http://blog.csdn.net/qq_21033663/article/details/78477309)，搜索插件时使用关键词“serialVersionUID ”

### 2、设置你的IDEA为检查序列化ID

![](/img/posts/ide/idea_serializable_UID.png)

### 3、重启IDEA
有的版本可以不重启,比如小编使用的
IntelliJ IDEA 2019.2.3 (Ultimate Edition)

就不需要重新启动,设置好后点击确定即可

这个可以根据实际情况而定
### 4、在需要自动生成序列化ID的类中使用快捷键:Alt+Insert
![](/img/posts/ide/idea_generate.png)

### 本文参考
[岳阳-丁's blog](https://1978413822.github.io/)的[IDEA加序列化](https://1978413822.github.io/2019/10/29/2019-10-29-idea%E4%B8%AD%E5%8A%A0%E5%BA%8F%E5%88%97%E5%8C%96/)

### 相关推荐
[在idea中使用git管理你的项目](https://victorfengming.gitee.io/2019/10/14/git-idea/)

[关于宇宙最强Java编辑器:IntelliJ IDEA](https://victorfengming.gitee.io/2019/09/26/jetbrains-idea-introduce/)

[在IDEA中调试代码](https://victorfengming.gitee.io/2019/10/21/jetbrains-idea-debug/)