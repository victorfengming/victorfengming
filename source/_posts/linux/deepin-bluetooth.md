---
title: "关于deepin系统不能识别蓝牙设备问题的完美解决方案"
cover: "/img/lynk/44.jpg"
date:       2019-08-29
tags:
	- Linux
	- deepin
---


### 为Deepin Linux启用蓝牙支持

自从安装了Deepin Linux，并采用自己编译的内核后，笔者的ThinkPad X200笔记本体验可谓是上升了一个非常重要的层次。后来有一天，笔者想用蓝牙耳机听音乐，然而在使用过程中发现，这台笔记本虽然自带蓝牙，屏幕下的蓝牙指示灯一直点亮着，系统中却看不到与蓝牙有关的设置选项。
出现这样的问题，多半就是因为系统中对蓝牙的支持没有启用，主要包括系统组件和内核两个层面。下面把我的经验总结如下。

### 安装蓝牙组件
默认地，Deepin并没有在系统中装上蓝牙组件，须用户手动安装。在终端中运行：
```
sudo apt install bluetooth blueman
```
其中，`bluetooth`是Linux蓝牙的核心组件，而`blueman`则是基于GTK+的一个全功能蓝牙管理器。把它们一齐装上，即可为Deepin启用全面的蓝牙支持。

### 配置内核
笔者本以为安装了蓝牙组件后，蓝牙功能就能正常使用（因为之前在解决WLAN问题时，WLAN驱动未配置的情况下无线网卡灯是不会亮的，然而蓝牙灯始终会常亮），但是当打开蓝牙管理器时，竟然报错，提示蓝牙服务未启动。这不得不让我想到，内核中的蓝牙支持是否没有启用。
果不其然。在内核源码目录下运行`make menuconfig`，打开内核配置界面，依次对内核进行以下配置。

### 1、启用蓝牙支持
内核中的蓝牙选项位于【Network Settings】 --> 【Bluetooth subsystem support】。先选中【Bluetooth subsystem support】，然后按”Y“，勾选它。

![lanya](bluetooth.jpg)
<center>启用蓝牙支持</center>

### 2、启用特定类型蓝牙设备协议支持
【Bluetooth subsystem support】中有子菜单，按回车进入，如下所示：


![lanya2](bluetooth2.jpg)

其中有几个选项，控制特定类型蓝牙设备协议的支持，一般全部启用。它们包括：



|项目|说明|
|---|---|
|RFCOMM protocol support|RFCOMM串口协议，用于设备通信、拨号网络等|
|BNET protocol support|BNEP（Bluetooth Network Encapsulation Protocol，蓝牙网络封装协议），用于蓝牙组建网络，蓝牙上网与组蓝牙个人区域网时需要|
|HIDP protocol support|人体学输入设备，用于连接蓝牙输入设备，如键盘、鼠标|

### 3、启用蓝牙适配器驱动
最为重要的一步，就是将蓝牙适配器驱动编译入内核当中。进入最下方子菜单【Bluetooth device drivers】，如下所示：


![lanya3](bluetooth3.jpg)

菜单中根据接口和特定型号设备，列出了相应的支持选项，有些选项在勾选后还会展开新的选项。典型的接口有USB、SDIO、UART，按需要勾选。
笔者X200笔记本的蓝牙适配器是Broadcom BCM2045B，走的是USB通道，因此先勾选【HCI USB driver】，随后会在该项下面出现三个新的选项，再进一步勾选【Broadcom protocol support】。不过，在得知适配器信息之前，笔者拿捏蓝牙适配器可能也走了UART通道，所以也将【HCI UART driver】勾上，再进一步勾选下面的【Intel AG6XX protocol support】。但实际使用时发现，X200的蓝牙适配器的确走的是USB而非UART。若不能确定自己的蓝牙适配器类型，可以一并选上，也不占用太多空间。

### 4、重新编译内核
上述配置完成后，按左右方向键选择”Save“，保存内核配置，然后选”Exit“退出。使用下面的命令重新编译内核并安装：

```
sudo make -j2
sudo make modules_install
sudo make install
```
重启后，蓝牙功能即被激活。  
### 使用体验
在内核中启用蓝牙支持，并在系统中安装蓝牙组件后，Deepin发生了翻天覆地的变化。Deepin下蓝牙的体验非常出色。  
Blueman管理器默认开机启动，会在托盘区域出现一个蓝牙图标，在其中可以很方便地管理蓝牙设备。  
在Blueman管理器中可以搜索到各种蓝牙设备，包括各种手机、电脑，以及笔者的蓝牙耳机。与蓝牙耳机配对后，Deepin即刻将声音通过蓝牙进行播放，无需再进行进一步的配置，尤其方便。此外，Blueman还有其他有趣的玩法，比如文件传输、浏览设备文件，其中对设备文件的浏览功能与当年的MTK功能机类似。

![lanya4](bluetooth4.jpg)

以X200为代表的ThinkPad早期机型有一项设计非常出彩，就是它屏幕下的灯条，系统运行状态一目了然。其中正包括了蓝牙指示灯，当有数据传输时（如正使用蓝牙音频），指示灯会闪烁，如此就能知道蓝牙设备是否正常工作。可谓匠心。

### 总结

要想让使用Deepin的笔记本支持蓝牙，需要做两项工作:  

- 安装蓝牙组件  
- 启用内核的蓝牙支持  

由此，Deepin下设备的价值就能被进一步挖掘，体验自会更上一层楼。  

作者：爱拼安小匠  
链接：https://www.jianshu.com/p/e5b3f501c953  
来源：简书  
简书著作权归作者所有，任何形式的转载都请联系作者获得授权并注明出处。  


