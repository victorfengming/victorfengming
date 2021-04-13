---
title: "python之禅"
cover: "/img/lynk/54.jpg"
date:       2019-11-28
subtitle: "python的设计哲学：优雅，简洁。。。"
tags:
	- Python
	- solution
	- interview
---



可以在编译器里面输入如下语句来查看python语言的设计哲学：

```python
C:\Users\victor>python
Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 23:09:28) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> import this
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
```

中英文释义如下：



```python
Beautiful is better than ugly.
# 优美胜于丑陋（Python以编写优美的代码为目标）
Explicit is better than implicit.
# 明了胜于晦涩（优美的代码应当是明了的，命名规范，风格相似） 
Simple is better than complex.
# 简洁胜于复杂（优美的代码应当是简洁的，不要有复杂的内部实现） 
Complex is better than complicated.
# 复杂胜于凌乱（如果复杂不可避免，那代码间也不能有难懂的关系，要保持接口简洁）
Flat is better than nested.
# 扁平胜于嵌套（优美的代码应当是扁平的，不能有太多的嵌套） 
Sparse is better than dense.
# 间隔胜于紧凑（优美的代码有适当的间隔，不要奢望一行代码解决问题） 
Readability counts.
# 可读性很重要（优美的代码是可读的） 
Special cases aren't special enough to break the rules.
Although practicality beats purity.
# 即便假借特例的实用性之名，也不可违背这些规则（这些规则至高无上） 
Errors should never pass silently.
Unless explicitly silenced.
# 不要包容所有错误，除非你确定需要这样做（精准地捕获异常，不写except:pass风格的代码） 
In the face of ambiguity, refuse the temptation to guess.
# 当存在多种可能，不要尝试去猜测 
There should be one-- and preferably only one --obvious way to do it.
# 而是尽量找一种，最好是唯一一种明显的解决方案（如果不确定，就用穷举法） 
Although that way may not be obvious at first unless you're Dutch.
# 虽然这并不容易，因为你不是 Python 之父（这里的Dutch是指Guido）
Now is better than never.
Although never is often better than *right* now.
# 做也许好过不做，但不假思索就动手还不如不做（动手之前要细思量）
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
# 如果你无法向人描述你的方案，那肯定不是一个好方案；反之亦然（方案测评标准） 
Namespaces are one honking great idea -- let's do more of those!
# 命名空间是一种绝妙的理念，我们应当多加利用（倡导与号召）
```

然后，我尝试了里面的一段demo代码：


```python
# coding = utf-82 print ("""
my name is yufengming
my blogs url is:https://victorfengming.gitee.io/
life is so short,I need python
""")
```

运行结果是可以成功运行的，但打印出来的结果前面，专门提及了python的设计哲学，说明，这段代码是不够简洁高效的。。。

突然明白一个道理：学习一门编程语言，一定要了解这门语言的特性。。。

其实做一件事学一门技术也一样（不限于编程语言，虽然编程语言也是一门技术、手段），要了解它的特性，才能更好的使用它，发挥它的作用！！！

引以为戒啊，兄弟