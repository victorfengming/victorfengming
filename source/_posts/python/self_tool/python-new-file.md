---
title: "Python实现从文件中读取文件名,并创建文件"
cover: "/img/lynk/98.jpg"
date:       2021-03-08
tags:
	- Python
	- solution
---



## 代码

```python
"""
根据文件内容,创建文件
"""
def newFile(file):
    with open(file, "r", encoding="utf-8") as f1:
        for line in f1:
            print("==================")
            # 新建文件的文件名,最后一行的\n去掉
            newName = line[:-1]
            print(newName)
            with open(newName, "w", encoding="utf-8") as f2:
                f2.write("#"+line)


newFile("D:\\WebstormProjects\\react\\sgg\\README.md")
```

问题分析

这个创建的文件的位置是在脚本的同级目录,但是我这里想要创建到readme.md文件同级目录中
## 升级版本

获取文件夹路径

>os.path.dirname()
>
>

```python
"""
根据文件内容,创建文件
"""
def newFile(file):
    # 获取目录
    dirname = os.path.dirname(file)
    with open(file, "r", encoding="utf-8") as f1:
        for line in f1:
            print("==================")
            # 新建文件的文件名,最后一行的\n去掉
            newName = dirname+"\\"+line[:-1]
            print(newName)
            with open(newName, "w", encoding="utf-8") as f2:
                f2.write("# "+line)


newFile("D:\\WebstormProjects\\react\\sgg\\README.md")
'''

       ┌─┐       ┌─┐ + +
    ┌──┘ ┴───────┘ ┴──┐++
    │                 │
    │       ───       │++ + + +
    ███████───███████ │+
    │                 │+
    │       ─┴─       │
    │                 │
    └───┐         ┌───┘
        │         │
        │         │   + +
        │         │
        │         └──────────────┐
        │                        │
        │                        ├─┐
        │                        ┌─┘
        │                        │
        └─┐  ┐  ┌───────┬──┐  ┌──┘  + + + +
          │ ─┤ ─┤       │ ─┤ ─┤
          └──┴──┘       └──┴──┘  + + + +
                 神兽保佑
                代码无BUG!

'''

```
