---
title: "压缩软件"
date:       2019-09-23
subtitle: "基于tkinter的GUI界面"
tags:
	- Python
	- background
	- tkinter
---


### 控制台版本,未加入图形化界面
```python
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by xiaoming

# 本模块的功能:<仅仅实现压缩功能,暂时不用图形化界面开发>
#

import zipfile


class Zip_file:
    # 成员属性
    file_list = []
    # depress_list = []


    # 成员方法
    def __init__(self):
        # 调用主方法
        self.main()
    # 添加文件
    def add_file(self):
        print('添加文件')
        ori_path = input('请输入要压缩的文件路径')
        self.file_list.append(ori_path)
        print('添加文件成功!列表如下:')
        for i in self.file_list:
            print(i)
        pass


    # 压缩文件
    def press_file(self):
        print('压缩文件')
        # 目标
        des_path = input('请输入目标路径')
        zp = zipfile.ZipFile(des_path, 'w',zipfile.ZIP_DEFLATED)
        for i in self.file_list:
            zp.write(i,self.get_file_name(i))
        print('压缩文件成功')
        # print('目标文件位置为:')
        # print(res)
        pass


    # 解压文件
    def depress_file(self):
        print('解压文件')
        src_path = input('请输入要解压的文件路径')
        # self.depress_list.append(src_path)
        # zipfile.ZipFile.extractall(src_path)
        # print('解压文件到当前文件夹')
        des_path = input('请输入目标文件路径')
        zp = zipfile.ZipFile(src_path,'r')
        for file in zp.namelist():
            zp.extract(file, self.get_file_name(file))
        else:
            print('解压缩成功')
        zp.close()
        pass


    # 用于获取路径后面的文件名称
    def get_file_name(self,path):
        import os
        new_name = os.path.split(path)[1]
        return new_name


    # 定义逻辑主函数,用于模拟tkinter的操作,简化程序先
    def main(self):
        info = '''
                1.添加文件
                2.压缩文件
                3.解压文件
                0.退出
                '''

        print(info)
        cho = input('请选择:')
        # print('控制逻辑部分')
        if cho == '1':
            self.add_file()
            # self.add_file()
            self.main()
        elif cho == '2':
            self.press_file()
            self.main()
        elif cho == '3':
            self.depress_file()
            self.main()
        elif cho == '0':
            return
        else:
            print('输入有误!重新输入')
            self.main()


# 实例化对象
z = Zip_file()



```

### 图形化开发版本
```python
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by xiaoming

# 本模块的功能:<tkinter图形化界面开发,实现压缩功能>
# 本次加入了提示弹窗的功能

# 在添加文件的时候,不能追加添加,添加多次的结果就是最后一次选中的文件(以完善)
# 类的使用,在类的成员方法中可以使用类中的成员属性,而不需要考虑变量的作用域的问题
# 只需要在变量前面加上一个self的对象本身调用
# 进行实例化类的同时,执行了__init__ 初始化方法
# 并在__init__方法中 调用控制函数 进行其他方法的执行,并加入了tkinter的图形化操作

# TODO 1.重名文件覆盖问题(加yesno框)
# TODO 2.自动清空文件列表(已完成)


# 导入 压缩模块
import zipfile
# 导入 系统模块,用于判断文件是否存在
import os
# 导入 tkinter模块 ,图形化界面
import tkinter
import tkinter.filedialog
import tkinter.messagebox
import tkinter.simpledialog

# 定义压缩类
class Zip_file:
    # 成员属性
    file_list = []

    # 成员方法
    def __init__(self):
        # 调用逻辑处理
        self.logic()

    # 控制窗口逻辑
    def logic(self):
        # 创建窗口对象
        root = tkinter.Tk()
        root.minsize(300, 300)
        
        btn_add = tkinter.Button(root, text='添加文件到列表', command=self.add_file)
        btn_add.grid(row=1, column=0)
        btn_ys = tkinter.Button(root, text='开始压缩', command=self.press_file)
        btn_ys.grid(row=1, column=1)
        btn_jy = tkinter.Button(root, text='开始解压', command=self.depress_file)
        btn_jy.grid(row=1, column=2)
        btn_jy = tkinter.Button(root, text='清空当前文件列表', command=self.clear_file)
        btn_jy.grid(row=3, column=0, columnspan = 3)

        self.val = tkinter.StringVar()
        self.val.set('                 暂无文件信息                 ')
        label1 = tkinter.Label(root, textvariable=self.val, bg='pink')
        label1.grid(row=2, column=0, columnspan=3)

        self.val2 = tkinter.StringVar()
        self.val2.set('    压缩或解压前请先添加文件到列表    ')
        label2 = tkinter.Label(root, textvariable=self.val2, bg='yellow')
        label2.grid(row=0, column=0, columnspan = 3)

        # 加入主消息循环
        root.mainloop()

    # 清空文件列表
    def clear_file(self):
        self.file_list.clear()
        self.val.set('暂无文件信息!')

    # 添加文件
    def add_file(self):
        print('添加文件')
        # 获得需要添加的文件路径列表
        file_name_temp = list(tkinter.filedialog.askopenfilenames(title='请选择要压缩的文件'))
        # 判断用户取消没
        if file_name_temp:
            pass
        else:
            return
        self.file_list += file_name_temp
        file_set = set(self.file_list)
        file_set_list = list(file_set)
        # ori_path = input('请输入要压缩的文件路径')
        # self.file_list.append(ori_path)
        tkinter.messagebox.showinfo('提示', '文件添加成功,可在列表中查看')
        # print('添加文件成功!文件列表如下:')
        for i in file_set:
            print(i)

        self.val.set('\n'.join(file_set_list))
        pass


    # 压缩文件
    def press_file(self):
        # tkinter.simpledialog
        print('压缩文件')

        # 目标
        # 弹出对话框返回压缩路径
        self.des_path = tkinter.filedialog.askdirectory(title='请选择压缩包保存的路径')
        # 如果用户取消选择
        if self.des_path:
            pass
        else:
            return
        print('压缩的路径是:')
        print(self.des_path)


        # 提示输入压缩文件名
        file_name = tkinter.simpledialog.askstring(\
            title='获取信息', prompt='给你的新压缩包起个名字吧', initialvalue='demo')
        file_name = file_name + '.zip'
        print(file_name)

        # 判断文件存在否
        if os.path.exists(self.des_path+'/'+file_name):
            # 文件已经存在
            # 询问用户

            result = tkinter.messagebox.askquestion(title='系统提醒', message='文件已存在,是否替换原文件')
            print(result)
            if result == 'yes':
                print('用户选择的是')
                # 返回 ,重新选择路径
                # 警告用户错误
                pass
            else:
                tkinter.messagebox.showwarning(title='警告', message='请重新选择目录')
                self.press_file()
                # print(result)
        else:
            # 路径不存在,正常执行
            pass


        zp = zipfile.ZipFile(self.des_path+'/'+file_name, 'w',zipfile.ZIP_DEFLATED)
        for i in set(self.file_list):
            zp.write(i,self.get_file_name(i)[1])
        else:
            tkinter.messagebox.showinfo(\
                '提示', '压缩文件%s保存成功' % self.des_path+'/'+file_name)
        # print('压缩文件成功')
        zp.close()
        self.clear_file()

        pass


    # 解压文件
    def depress_file(self):
        print('解压文件')
        # # 方式1
        # src_path_list = tkinter.filedialog.askopenfilenames(title='请选择解压文件路径')
        #
        # # 判断用户取消没
        # if src_path_list:
        #     pass
        # else:
        #     return
        # 方式2
        src_path_list = set(self.file_list)


        # 选择保存位置
        des_path = tkinter.filedialog.askdirectory(title='请选择解压后文件保存的路径')

        # 判断用户取消没
        if des_path:
            pass
        else:
            return

        # des_path = self.get_file_name(self.src_path)[0]
        # 这里测试出一个bug
        # 如果用户没有添加文件,而直接点击了解压文件按钮
        # TODO 应该提供一个提示信息

        for src_path in src_path_list:
            # des_path = self.get_file_name(src_path)[0]
            zp = zipfile.ZipFile(src_path,'r')
            for file in zp.namelist():
                print(file)
                zp.extract(file,des_path)
            else:
                tkinter.messagebox.showinfo('提示', '解压缩文件%s成功' % src_path)
                # print()
            zp.close()
        self.clear_file()
        pass


    # 用于获取路径后面的文件名称
    def get_file_name(self,path):
        import os
        new_name = os.path.split(path)
        return new_name

# 实例化对象
z = Zip_file()
```