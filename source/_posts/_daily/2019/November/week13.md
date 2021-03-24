---  
title: "第十三周日报"   
date:       2019-11-04
cover: "/img/lynk/23.jpg"
subtitle: "day83、84、85、86、87、88、89"   
tags: XDH    
---  









# day83-使用Django的第1天   

### 充实的一天
使用国内镜像源安装模块速度飞起->[python 相关模块安装 国内镜像地址](https://victorfengming.gitee.io/victorfengming_old/2019/11/03/python-module-install/)
### 每日新词

ginx 是一款轻量级的 Web 服务器/反向代理服务器及电子邮件（IMAP/POP3）代理服务器，其特点是占有内存少，并发能力强

### 当天小结

今天做了两个实验

SOPC设计与验证-Hello实验
SOPC设计与验证-定时器实验

pycharm还是不会用啊,比如数据库工具的使用,版本控制,文件/代码结构的预览功能,它的强大有待你的发现? 加油!!!

又发现了一个快捷commit的地方,又傻了直接 `ctrl+k` 就行了,完美,唉那不用add么,好像是不用了

[毕业论文___基于python的博客设计与开发.doc 22页](https://max.book118.com/html/2017/0120/85586597.shtm)

window远程登录厉害了! 直接登录你的服务器,管理项目

---  
title: "第84天日报"  
date:       2019-11-04
cover: "/img/lynk/23.jpg"
subtitle: "写javaSE阶段项目(兄弟连考试系统)的第1天"  
tags: XDH    
---  

### 充实的一天

### 当天小结

- 我这一套组合拳下来,打的你都找不到鼠标了
```
ctrl+k  ->  ctrl+alt+k  -> ctrl+enter
ctrl+k  -> ctrl+enter -> ctrl+shift+k -> ctrl+enter  
```
简直完美,还要什么python自动推啊!!!

-   java中一个文件是一个class,

    python中一个文件是一个module

    所以导致相对路径的根目录不一样

    是`大瑕疵`吧!

- 环境变量就是没啥用,我直接在IDE中配置好就OK

- IDEA快捷键->`alt+F7` 查找方法调用处

- IDEA快捷键->`ALT+J` 相当于sublime中的`ctrl+D`

来自于[IntelliJ IDEA 超实用使用技巧分享](https://blog.csdn.net/weixin_38405253/article/details/102583954?utm_source=app)


# 第85天日报-写javaSE阶段项目(兄弟连考试系统)的第2天

### 充实的一天
今天写这个一期项目进展还可以,之前学那个pyqt5什么鬼玩意,浪费我时间!
### 当天小结

学生管理的增删改查完事儿了,下一步就是试题管理的增删改查了

### 每日分享->idea 自定义设置

### 内存显示以及性能优化
Preferences-->Appearance & Behavior-->Appearance，右侧勾选Window Options下面的Show memory indicator即可

安装目录中的bin文件夹->idea64.exe.vmoptions-> 前两行 最大内存 最小内存 16GB 建议 把idea的最大内存设置2048m，最小内存1024m

### 区分大小写 
Editor->General->Code Completion->取消Match case前的勾选

### 软换行

### 自定义折叠代码区域功能
(用啥包裹代码块)
### 更改变量名
方式1 查找替换
方式2 alt+j
方式3 s+F6
### 字体快速缩放
Editor->General->Mouse->Change font size(Zoom)with Ctrl+Mouse Wheel
### 显示调用处
A+F7
### 跳转定义位置
C+b
### 自动导包
  Editor->General->Auto Import 
    add 自动优化导入的包

### 去除没用的包    

C+A+o
Editor->General->Auto Import->Optimize
    
### 类结构

### TODO

### 并行运行or重新运行
配置运行方式 edit configurations
### 统计代码量
statistic插件
### IDEA中调试代码
https://victorfengming.gitee.io/ide/jetbrains/idea/jetbrains-idea-debug
### 强行假装git    
本地文件的历史记录
项目右键->Local History ->Show Hisory
Put Label
### IDEA使用git
https://blog.csdn.net/qq_40223983/article/details/102543484

https://victorfengming.gitee.io/git/git-idea


#第86天日报-写javaSE阶段项目(兄弟连考试系统)的第3天


### 充实的一天
今天写的学员的登录以及学员的考试和成绩查询

这个项目就这样吧,要完善有的是功能等着你来整,就不写了吧!

javaSE部分,笔记记得乱码七糟,还是看[ttk](https://ttk1907.gitee.io/)的[JavaSE阶段总结](https://ttk1907.gitee.io/2019/11/01/xiongdihui-javaSE-note-conclusion-%E5%89%AF%E6%9C%AC/)吧!

其实我也写笔记了的:
- [Java笔记01-数组相关](https://victorfengming.gitee.io/java/javase/note/note01/)
- [Java笔记02-OOP](https://victorfengming.gitee.io/java/javase/note/note02/)
- [Java笔记03-Constructor & Override](https://victorfengming.gitee.io/java/javase/note/note03/)
- [Java笔记04-核心类库](https://victorfengming.gitee.io/java/javase/note/note04/)
- [Java笔记05-Collection、泛型、迭代器](https://victorfengming.gitee.io/java/javase/note/note05/)
- [Java笔记06-Map集合详解](https://victorfengming.gitee.io/java/javase/note/note06/)
- [Java笔记07-List、Set、数据结构、Collections](https://victorfengming.gitee.io/java/javase/note/note07/)
- [Java笔记08-Map详解](https://victorfengming.gitee.io/java/javase/note/note08/)
- [Java笔记09-继承、super、this、抽象类](https://victorfengming.gitee.io/java/javase/note/note09/)
- [Java笔记10-Map集合简识](https://victorfengming.gitee.io/java/javase/note/note10/)
- [Java笔记11-异常、线程](https://victorfengming.gitee.io/java/javase/note/note11/)
- [Java笔记12-函数式接口](https://victorfengming.gitee.io/java/javase/note/note12/)
- [Java笔记13-兄弟连在线考试系统](https://victorfengming.gitee.io/java/javase/note/note13/)

### 每日新发现
ttk乱按我键盘出现了这个:
[idea官方帮助](https://www.jetbrains.com/help/idea/2019.2/getting-started.html?utm_campaign=IU&utm_content=2019.2&utm_medium=link&utm_source=product)

# 第87天日报-"学习JDBC的第1天


### 充实的一天
今天开始学习的JDBC,能够进行对于mysql数据库的简单的增删改查操作了
### 每日新发现
markdown的在线编辑网站:
https://www.zybuluo.com/mdeditor

客户端下载:https://www.zybuluo.com/cmd/


# 第88天日报-学习JDBC的第2天  



### 充实的一天
今天继续学习的JDBC
更加高级的增删改查操作,防止sql注入,连接池技术...
### 每日新发现
c3p0所有版本的jar包下载地址:
https://mvnrepository.com/artifact/com.mchange/c3p0

# 第89天日报-学习JDBC的第3天

### 充实的一天
Druid 驱动配置,看完了JDBC的课

//TODO 有一个关于QQ的数据库操作练习的作业,暂时还没做


### 每日新发现
[Druid_jar包及配置文件(druid-1.0.9.jar、druid-1.0.9-javadoc.jar、druid-1.0.9-sources.jar)](https://blog.csdn.net/qq_36050720/article/details/100097024)

[Spring Transaction » 5.0.0.RELEASE](https://mvnrepository.com/artifact/org.springframework/spring-tx/5.0.0.RELEASE)

IDEA查看参数parameter -> `ctrl+P`

[一个大牛的github博客](https://zhiyuancs.github.io/)

[换了他的博客主题](https://github.com/ppoffice/hexo-theme-icarus)