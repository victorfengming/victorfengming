---
title: "python实现猴子爬山算法"
cover: "/img/lynk/55.jpg"
date:       2021-04-25
subtitle: "排列组合"
author: "victor"
tags:
	- Python
	- solution
---
  

猴子爬山一只顽猴在一座有N级台阶的小山上爬山跳跃。上山时需从山脚至山顶往上跳N级台阶，一步可跳1级，或跳3级，求上山有多少种不同的跳法？ （N<50）

问题分析:

 每一次都可以选择1,2,3有3种跳法

直接使用递归

```python
jumpWay = [1, 3]

footstep = int(input())

jumping = 0

#first write

def jump(nowstep, footstep, jumpWay):
    if nowstep == footstep:
        global jumping
        jumping += 1
        return
    elif nowstep > footstep:
        return
    else:
        for i in range(len(jumpWay)):
            jump(nowstep + jumpWay[i], footstep, jumpWay)


jump(0, footstep, jumpWay)
```

但是这种方式会提示 递归层数过多

想办法对算法进行合理优化,排列组合

```python
size = int(input())
n3 = size//3
res = 0

# 求阶乘
def jiecheng(n):
    num = 1
    if n==1:
        return 1
    else:
        for i in range(1,n+1):
            num*=i
        return num

# 求排列
def c43(n4,n3):
    # return jiecheng
    # 3!/(4-3)!*3!
    # j3 = jiecheng(3)
    return jiecheng(n4)//(jiecheng(n4-n3)*jiecheng(n3))

# a32不用了
# def a32(n3,n2):
#    return jiecheng(n2)//jiecheng(n3)-jiecheng(n2)

# 循环
for i in range(size+1):
    # i 为有几个 1步的情况
    for j in range(n3+1):
        # j为有 几个 3步的情况
        if (i+j*3) == size:
            # temp 为总数
            temp = j+i
            res+=c43(temp,j)
print(res)
```


