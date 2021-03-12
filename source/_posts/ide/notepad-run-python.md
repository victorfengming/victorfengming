---
title: "Notepad++运行python"
cover: "/img/lynk/6.jpg"
date:       2019-08-16
tags:
	- Python
---



### 关于使用notepad运行python程序

 1. 首先要确保python解释器已经安装成功,查看方法,windows可以在命令提示符中查看,通过按下win+R键,调出运行窗口,在输入框中输入cmd回车,然后在命令行中输入python,若出现版本信息,例如`Python 3.6.1 (v3.6.1:69c0db5, Mar 21 2017, 18:41:36) [MSC v.1900 64 bit (AMD64)] on win32 Type "help", "copyright", "credits" or "license" for more information.`则安装成功,若出现`'python' 不是内部或外部命令，也不是可运行的程序`,则需要配置环境变量,详情参考[如何配置python的环境变量](https://blog.csdn.net/taowuhua0505/article/details/80435374)
 2. 在在notepad++中，按F5，或者菜单栏点击 "运行－＞运行" (默认快捷键是 F5 )，在弹出的对话框中，输入`cmd /k python "$(FULL_CURRENT_PATH)"& PAUSE & EXIT`

<div align="center">
    <img src="/img/posts/technology/20190712173112386notepad1.png" >  
</div>


 3. 点击 "保存"，就可以给这条命令设置一个快捷键并起一个名字，比如 "run_python"。以后运行直接按自定义的快捷键就妥了。


 <div align="center">
    <img src="/img/posts/technology/20190712173148840notepad2.png" >  
</div>



