---
title: "ansible简介"
date:       2020-04-21
subtitle: "一款简单的运维自动化工具"
tags:
	- base
---
  











#ansible
Ansible是一款简单的运维自动化工具，只需要使用ssh协议连接就可以来进行系统管理，自动化执行命令，部署等任务。

### Ansible的特点
##### 1、ansible不需要单独安装客户端，也不需要启动任何服务
##### 2、ansible是python中的一套完整的自动化执行任务模块
##### 3、ansible playbook 采用yaml配置，对于自动化任务执行过一目了然

### Ansible组成结构

##### Ansible
是Ansible的命令工具，核心执行工具；一次性或临时执行的操作都是通过该命令执行。
##### Playbook
任务剧本（又称任务集），编排定义Ansible任务集的配置文件，由Ansible顺序依次执行，yaml格式。
##### Inventory
Ansible管理主机的清单，默认是/etc/ansible/hosts文件。
##### Modules
Ansible执行命令的功能模块，Ansible2.3版本为止，共有1039个模块。还可以自定义模块。
##### Plugins
插件，模块功能的补充，常有连接类型插件，循环插件，变量插件，过滤插件，插件功能用的较少。
#####API
提供给第三方程序调用的应用程序编程接口。

### 安装ansible
```
yum -y install ansible	 # 使用yum源安装ansible
ansible --version		# 查看ansible版本
```
#### ansible的一般使用
```
cd /etc/ansible			#进入ansible目录下
vim hosts			    #修改hosts文件，添加主机组
		[组名]	     #主机分组的的组名
 		IP或者主机名	   #被管理主机名	
 
ssh-keygen		#创建ssh	进行ssh免密连接
    （有提示直接根据提示回车或者yes）
    
ssh-copy-id 服务器名(或者用户名@地址)  #给控制服务器复制 ssh秘钥
```

#### 常用命令参数
```
ansible -h
Usage: ansible <host-group> [options]
-a MODULE_ARGS   #模块参数
-C, --check     #检查语法
-f FORKS        #并发
--list-hosts    #列出主机列表
-m MODULE_NAME  #模块名字
-o              #使用精简的输出
```

```
ansible all --list-hosts		#列出所有主机

ansible all -m ping  / ansible 组名 -m ping -k	Ping所有主机

ansible <文件名> -m copy -a 'src=/本地路径 dest=/目标路径'		#将本机的/etc/passwd 复制到远程机子文件 /tmp/passwd
```

#### Ansible Ad-hoc模式常用模块
```
ping模块、 raw模块、yum模块、apt模块、copy模块、user模块与group模块、、fetch模块、file模块、command 模块和shell
```
命令相关模块：command shell
	ansible默认的模块,执行命令，注意：shell中的"<", ">", "|", ";", "&","$"等特殊字符不能在command模块中使用，如果需要使用，则用shell模块
	shel模块l专门用来执行shell命令的模块，和command模块一样，参数基本一样，
```	
ansible-doc -s shell	# 查看模块参数
```
文件相关的模块：file copy
	用于对文件的处理，创建，删除，权限控制等
```

 [root@ansible ~]# ansible-doc -s file	 # 查看模块参数
 path     #要管理的文件路径
   state：
       directory  #创建目录，如果目标不存在则创建目录及其子目录
       touch      #创建文件，如果文件存在，则修改文件 属性
       absent     #删除文件或目录
       mode       #设置文件或目录权限
       owner      #设置文件或目录属主信息
       group      #设置文件或目录属组信息
       
  
  # 创建目录
 [root@ansible ~]# ansible 192.168.1.31 -m file -a 'path=/tmp/test1 state=directory'
 
 # 创建文件
 [root@ansible ~]# ansible 192.168.1.31 -m file -a 'path=/tmp/test2 state=touch'
 
 # 删除文件
 [root@ansible ~]# ansible 192.168.1.31 -m file -a 'path=/tmp/test2 state=absent'
 
 # 创建文件时同时设置权限等信息
[root@ansible ~]# ansible 192.168.1.31 -m file -a 'path=/tmp/test4 state=directory mode=775 owner=root group=root'
```
```
Linux 将访问文件的用户分为 3 类，分别是文件的所有者，所属组（也就是文件所属的群组）以及其他人。
最常见的文件权限有 3 种，即对文件的读（用 r 表示）、 写（用 w 表示）、 执行（用 x 表示，针对可执行文件或目录）权限。
		ower     group    other

		r w x    r w x    r w x

		4 2 1    4 2 1    4 2 1 
对于目录来说，常用来设定目录的权限其实只有 0（---）、5（r-x）、7（rwx）这 3 种。

777 三组都有读写执行权限;  755 所有者读写执行权限  所属组读执行权限  其他人读执行权限
```
#### copy 用于管理端复制文件到远程主机，并可以设置权限，属组，属主等
```
 [root@ansible ~]# ansible-doc -s copy	#查看模块参数
 src      #需要copy的文件的源路径
 dest     #需要copy的文件的目标路径
 backup   #对copy的文件进行备份

# 复制文件到远程主机并改名
[root@ansible ~]# ansible 192.168.1.31 -m copy -a 'dest=/tmp/a.sh src=/root/ansible_test.sh' 

# 复制文件到远程主机，并备份远程文件,安装时间信息备份文件（当更新文件内容后，重新copy时用到）
[root@ansible ~]# ansible 192.168.1.31 -m copy -a 'dest=/tmp/a.sh src=/root/ansible_test.sh backup=yes'

```
#### fetch 用于从被管理机器上面拉取文件，拉取下来的内容会保留目录结构，一般情况用在收集被管理机器的日志文件等
```

[root@ansible ~]# ansible-doc -s fetch		# 查看模块参数
src      #指定需要从远端机器拉取的文件路径
dest     #指定从远端机器拉取下来的文件存放路径

# 从被管理机器上拉取cron日志文件，默认会已管理节点地址创建一个目录，并存放在内
[root@ansible ~]# ansible 192.168.1.31 -m fetch -a 'dest=/tmp src=/var/log/cron'

[root@ansible ~]# tree /tmp/192.168.1.31/
/tmp/192.168.1.31/
└── var
    └── log
        └── cron
directories, 1 file
```
#### 软件包相关的模块： yum

```

 [root@ansible ~]# ansible-doc -s yum		# 查看模块参数
  name            #指定要操作的软件包名字
  download_dir    #指定下载软件包的存放路径，需要配合download_only一起使用
  download_only   #只下载软件包，而不进行安装，和yum --downloadonly一样
  list:
      installed   #列出所有已安装的软件包
      updates     #列出所有可以更新的软件包
      repos       #列出所有的yum仓库
  state:
      installed, present   #安装软件包(两者任选其一都可以)
      removed, absent      #卸载软件包
      latest      #安装最新软件包
  
 # 列出所有已安装的软件包
 [root@ansible ~]# ansible 192.168.1.31 -m yum -a 'list=installed'
  
 # 列出所有可更新的软件包
 [root@ansible ~]# ansible 192.168.1.31 -m yum -a 'list=updates'
 
 #列出所有的yum仓库
 [root@ansible ~]# ansible 192.168.1.31 -m yum -a 'list=repos'
 
 #只下载软件包并到指定目录下
 [root@ansible ~]# ansible 192.168.1.31 -m yum -a 'name=httpd download_only=yes download_dir=/tmp'
  
 #安装软件包
 [root@ansible ~]# ansible 192.168.1.31 -m yum -a 'name=httpd state=installed'
 
 #卸载软件包
 [root@ansible ~]# ansible 192.168.1.31 -m yum -a 'name=httpd state=removed'
```
### Ansible之Playbook

`Playbook`与`ad-hoc`相比,是一种完全不同的运用ansible的方式。
	`playbook`是由一个或多个`play`组成的列表，`play`的主要功能在于将事先归并为一组的主机装扮成事先通过`ansible`中的`task`定义好的角色。从根本上来讲，所谓的`task`无非是调用`ansible`的一个`module`。将多个`play`组织在一个`playbook`中，即可以让它们联合起来按事先编排的机制完成某一任务 
#### Playbook核心元素
- Hosts 执行的远程主机列表
- Tasks 任务集
- tags 标签，指定某条任务执行，用于选择运行playbook中的部分代码。
- Varniables 内置变量或自定义变量在playbook中调用
- Templates 模板，即使用模板语法的文件，比如配置文件等
- Handlers 和notity结合使用，由特定条件触发的操作，满足条件方才执行，否则不执行

#### Playbook语法
playbook使用yaml语法格式，后缀可以是yaml,也可以是yml。

在单一一个playbook文件中，可以连续三个连子号(---)区分多个play。还有选择性的连续三个点好(...)用来表示play的结尾，也可省略。
次行开始正常写playbook的内容，一般都会写上描述该playbook的功能。
使用#号注释代码。
缩进必须统一，不能空格和tab混用。
缩进的级别也必须是一致的，同样的缩进代表同样的级别，程序判别配置的级别是通过缩进结合换行实现的。
YAML文件内容和Linux系统大小写判断方式保持一致，是区分大小写的，k/v的值均需大小写敏感
k/v的值可同行写也可以换行写。同行使用:分隔。
v可以是个字符串，也可以是一个列表
一个完整的代码块功能需要最少元素包括 name: task

## Playbook的运行方式

通过`ansible-playbook`命令运行 格式：`ansible-playbook <filename.yml> ... [options]` 

```
[root@ansible PlayBook]# ansible-playbook -h
#ansible-playbook常用选项：
--check  or -C    #只检测可能会发生的改变，但不真正执行操作
--list-hosts      #列出运行任务的主机
--list-tags       #列出playbook文件中定义所有的tags
--list-tasks      #列出playbook文件中定义的所以任务集
--limit           #主机列表 只针对主机列表中的某个主机或者某个组执行
-f                #指定并发数，默认为5个
-t                #指定tags运行，运行某一个或者多个tags。（前提playbook中有定义tags）
-v                #显示过程  -vv  -vvv更详细
```

### tasks任务列表

​	每一个`task`必须有一个名称`name`,这样在运行`playbook`时，从其输出的任务执行信息中可以很清楚的辨别是属于哪一个`task`的，如果没有定义 `name`，`action`的值将会用作输出信息中标记特定的`task`。 每一个`playbook`中可以包含一个或者多个`tasks`任务列表，每一个`tasks`完成具体的一件事，（任务模块）比如创建一个用户或者安装一个软件等，在`hosts`中定义的主机或者主机组都将会执行这个被定义的`tasks`。 

###### 一个简单的示例
```
vim install_apache.yml
---							  #固定格式
- hosts: "{{host_group}}"		#定义需要执行主机
  vars:
    work_home: /home/apache/packages	#设定工作目录
  tasks:								#定义一个任务的开始
    - name: add user					#定义任务的名称
      tags: useradd
      become: yes
      become_user: root
      become_method: sudo
      user:
        name: "{{user_name}}"
        group: users
        shell: /bin/bash
        createhome: yes
        home: /home/{{user_name}}
        state: present
      ignore_errors: yes
    - name: copy install file
      tags: copy
      become: yes
      become_user: root
      become_method: sudo
      shell: cp -arf {{work_home}}/httpd-2.4.33 {{work_home}}/httpd-2.4.33_{{user_name}}
    - name: compile
      become: yes
      become_user: root
      become_method: sudo
      shell: cd {{work_home}}/httpd-2.4.33_{{user_name}} && ./configure --prefix=/home/{{user_name}}/ --enable-so --enable-mods-shared=all --enable-proxy=shared --enable-proxy-balancer=shared --enable-proxy-http=shared --enable-proxy-ajp --enable-deflate --enable-cache --enable-disk-cache --enable-mem-cache --enable-ssl=shared --with-ssl=/usr/local/ssl/ --with-apr=/usr/local/apr --with-apr-util=/usr/local/apr-util && make clean && make && make install
    - name: copy template config file
      tags: config
      become: yes
      become_user: root
      become_method: sudo
      template:
        src: templates/httpd-template.conf.j2
        dest: /home/{{user_name}}/conf/httpd-{{user_name}}.conf
        owner: "{{user_name}}"
        backup: no
        force: no
        mode: 0755
    - name: grant privileges to user
      tags: grant
      become: yes
      become_user: root
      become_method: sudo
      shell: chown -R {{user_name}}:users /home/{{user_name}}/
    - name: start application
      tags: start
      become: yes
      become_user: root
      become_method: sudo
      shell: su - {{user_name}} -c "httpd -f /home/{{user_name}}/conf/httpd-{{user_name}}.conf -k start"
      
      
      ansible-playbook -e "host_group={host_group} user_name={user_name} listen_port={listen_port} server_path={server_path}" install_apache.yml
      
       ansible-playbook -e "{'host_group':app1 'user_name':apache1 'listen_port':8088 'server_path':app01li" install_apache.yml
```
#####执行playbook， 第一次执行可以加-C选项，检查写的playbook是否ok
```
[root@ansible ~]# ansible-playbook playbook01.yml
PLAY [192.168.1.31] *********************************************************************************************
TASK [Gathering Facts] ******************************************************************************************
ok: [192.168.1.31]
TASK [create new file] ******************************************************************************************
changed: [192.168.1.31]
TASK [create new user] ******************************************************************************************
changed: [192.168.1.31]
TASK [install package] ******************************************************************************************
changed: [192.168.1.31]
TASK [config httpd] *********************************************************************************************
changed: [192.168.1.31]
TASK [copy index.html] ******************************************************************************************
changed: [192.168.1.31]
TASK [start httpd] **********************************************************************************************
changed: [192.168.1.31]
PLAY RECAP ******************************************************************************************************
192.168.1.31               : ok=7    changed=6    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0 
```
