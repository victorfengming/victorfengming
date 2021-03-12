---
title: "Python脚本实现汉字转拼音"
date:       2019-11-25
subtitle: "Python无所不能"
tags:
	- Python
	- background
	- solution
---







### 起步
中华文化博大精深，是中华民族的财富，吸收和继承发扬中 华文化，是现代每个炎黄子孙无可推卸的天职。

今天小编就交大家用python写一个脚本,实现汉子和拼音之间的转换

### pinyin.py

汉字转拼音,With Python


Example:
```python
from pinyin import PinYin

test = PinYin()
test.load_word()
test.hanzi2pinyin(string='钓鱼岛是中国的')
```


Out:

    test.hanzi2pinyin(string='钓鱼岛是中国的')
    ['diao', 'yu', 'dao', 'shi', 'zhong', 'guo', 'de']    
    test.hanzi2pinyin_split(string='钓鱼岛是中国的', split="-")
    diao-yu-dao-shi-zhong-guo-de


### 主程序
```python
#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
    Author:cleverdeng
    E-mail:clverdeng@gmail.com
"""

__version__ = '0.9'
__all__ = ["PinYin"]

import os.path


class PinYin(object):
    def __init__(self, dict_file='word.data'):
        self.word_dict = {}
        self.dict_file = dict_file


    def load_word(self):
        if not os.path.exists(self.dict_file):
            raise IOError("NotFoundFile")

        with open(self.dict_file) as f_obj:
            for f_line in f_obj.readlines():
                try:
                    line = f_line.split('    ')
                    self.word_dict[line[0]] = line[1]
                except:
                    line = f_line.split('   ')
                    self.word_dict[line[0]] = line[1]


    def hanzi2pinyin(self, string=""):
        result = []
        if not isinstance(string, str):
            string = string.decode("utf-8")
        
        for char in string:
            key = '%X' % ord(char)
            result.append(self.word_dict.get(key, char).split()[0][:-1].lower())

        return result


    def hanzi2pinyin_split(self, string="", split=""):
        result = self.hanzi2pinyin(string=string)
        if split == "":
            return result
        else:
            return split.join(result)


if __name__ == "__main__":
    test = PinYin()
    test.load_word()
    string = "钓鱼岛是中国的"
    print("in: %s" % string)
    print("out: %s" % str(test.hanzi2pinyin(string=string)))
    print("out: %s" % test.hanzi2pinyin_split(string=string, split="-"))

```

### 字典
这里我们需要一个转换库
```shell script
3400    QIU1
3401    TIAN3 TIAN4
3404    KUA4
3405    WU3
3406    YIN3
340C    SI4 YI2
3416    YE4
341C    CHOU2
3421    NUO4
3424    QIU2
3428    XU4
3429    XING2
342B    XIONG1
342C    LIU2
342D    LIN3
342E    XIANG1
342F    YONG1
3430    XIN4
3431    ZHEN3
3432    DAI4
3433    WU4
3434    PAN1
3437    MA3 MA4 MIAN2
```
### 转载说明 
CSDN:https://blog.csdn.net/u011389474/article/details/60144194　　　

作者:cleverdeng

项目地址: https://github.com/cleverdeng/pinyin.py