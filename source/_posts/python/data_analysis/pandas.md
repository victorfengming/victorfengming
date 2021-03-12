---
title: "数据分析之pandas笔记"
date:       2019-12-10
tags:
	- Python
	- solution
	- basis
	- data_analysis
	- pandas
---
  

### Pandas
一个用于表示表格类型的内容
- 课时4：jupyter21 分22 秒
- 课时5：pandas的内容24 分31 秒
- 课时6：series内容38 分19 秒
- 课时7：dataframe25 分50 秒


```python
# 载入pandas库
import pandas as pd
import numpy as np
```


```python
s = pd.Series([2,4,6,8,10])
```


```python
s
```

    0     2
    1     4
    2     6
    3     8
    4    10
    dtype: int64


```python
d = pd.DataFrame([
 [2,4,6,8,10],
 [7,3,4,7,15],
])

d
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>0</th>
      <th>1</th>
      <th>2</th>
      <th>3</th>
      <th>4</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2</td>
      <td>4</td>
      <td>6</td>
      <td>8</td>
      <td>10</td>
    </tr>
    <tr>
      <th>1</th>
      <td>7</td>
      <td>3</td>
      <td>4</td>
      <td>7</td>
      <td>15</td>
    </tr>
  </tbody>
</table>
</div>




```python
d[0]
```




    0    2
    1    7
    Name: 0, dtype: int64



这里要注意直接用中括号获取的是,列,因为比如我们要获取一个表中的age属性,通常的拿这age一列的数据出来,所以想要获取一条数据,需要再中括号一下

获取一行怎么获取



```python
d.loc[0]
```




    0     2
    1     4
    2     6
    3     8
    4    10
    Name: 0, dtype: int64



这个给我们返回的是一个series
实际上这个dataframe是由多个series组成的
所以我们可以这么写


```python
d2 = pd.DataFrame([
 pd.Series([2,4,6,8,10]),
 pd.Series([7,3,4,7,15]),
])
d2
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>0</th>
      <th>1</th>
      <th>2</th>
      <th>3</th>
      <th>4</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2</td>
      <td>4</td>
      <td>6</td>
      <td>8</td>
      <td>10</td>
    </tr>
    <tr>
      <th>1</th>
      <td>7</td>
      <td>3</td>
      <td>4</td>
      <td>7</td>
      <td>15</td>
    </tr>
  </tbody>
</table>
</div>




```python
class1 = pd.Series({'hong': 50, 'huang': 90, 'qing': 60})

# 修改字典索引
class1_values = {'hong': 50, 'huang': 90, 'qing': 60}
class1_index = ['hong', 'lv', 'lan']
# 这个地方的键是根据index参数设置的,然后前面的那个字典的键就不要了
class1 = pd.Series(class1_values, index=class1_index)
class1
```




    hong    50.0
    lv       NaN
    lan      NaN
    dtype: float64




```python
class1

# 值数据，输出类型为array，还是ndarray数组
class1.values

# 索引，输出index类型（Pandas独有的索引类型）,本质上就是ndarray
class1.index

class1.index[2]
class1.index.values


```




    array(['hong', 'lv', 'lan'], dtype=object)




```python
class1_index
class1.hong



```




    50.0




```python
class1[[1,2,0]]


```




    lv       NaN
    lan      NaN
    hong    50.0
    dtype: float64




```python
class1[0:1]
```




    hong    50.0
    dtype: float64




```python
# 直接就能记性判断
class1 > 6
# 这个Nan值你怎么判断都是False
```




    hong     True
    lv      False
    lan     False
    dtype: bool




```python
# 还能这样写
# 这种写法很类似于数据库的写法
class1[class1>6]
```




    hong    50.0
    dtype: float64




```python
# 直接就全都加一
class1+1

```




    hong    51.0
    lv       NaN
    lan      NaN
    dtype: float64



- 这种整体的加一,他是效率非常非常高的
- 如果是我们的列表,想要实现这个效果,那就得循环这个列表
从列表中获取一个数据,把这个数据+1,放到新的列表中
- 而我们这个是将三条数据同时拿出来(就像并发一样),然后同时进行+1操作
然后在同时放到一个新的里面.
- 我们可以通过那个运算时间的魔术命令来帮忙验证一下


```python
%%timeit
# 修改字典索引
class2_values = [1024,3,5,7,9,10,13,115,127,149,221]
# 这个地方的键是根据index参数设置的,然后前面的那个字典的键就不要了
class2 = pd.Series(class2_values)
class2+1
```

    198 µs ± 9.37 µs per loop (mean ± std. dev. of 7 runs, 10000 loops each)
    


```python
%%timeit
class2+1
```

    100 µs ± 3.56 µs per loop (mean ± std. dev. of 7 runs, 10000 loops each)
    


```python
%%timeit
for i in range(100000):
    i+=1
```

    4.12 ms ± 108 µs per loop (mean ± std. dev. of 7 runs, 100 loops each)
    


```python
%%timeit
a = pd.Series(range(100000))
a+1

```

    562 µs ± 72 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)
    

我猜可能是因为这个数据量不够大,还显示不出来这个库的优势,所以得多试试才行
有的时候需要用GPU来计算,如果用CPU,会非常耗CPU,因为GPU更擅长这种小量的计算,他就相当于一堆小学生,这中加减乘除,小学生比CPU数学家更厉害



```python
# 不仅能够进行加,减号,还能乘除,取余,底板除
print(class2 // 2) 
```

    11.0
    11.0
    


```python
class2 = pd.Series([1024,3,5,7,9,10,13,115,127,149,221])
# 平均数
print(class2.mean())
print(np.mean(class2))
class2

```

    153.0
    153.0
    




    0     1024
    1        3
    2        5
    3        7
    4        9
    5       10
    6       13
    7      115
    8      127
    9      149
    10     221
    dtype: int64




```python
class3 = pd.Series([1024,13,5,7,9,10,1,115,127,149,221])
# 中位数
# 通过库中的函数调用
print(np.median(class3))
# 自身属性调用写法
print(class3.median())
# 中位数如果有两个数据,那就是这两个数据的平均数

```

    13.0
    13.0
    


```python
# 方差
class2.var()
```




    89190.6




```python
# 标准差
class2.std()

```




    298.6479532827908




```python
print(class2)
print("-"*50)
print(class2+1)
print("-"*50)
# 全判断在不在容器中
# 这个容器包括类似于字典的键和值,都都算上,只有有都行,都算存在啊
print(10 in class2)
print("-"*50)
print(5 in class2 + 1)
# 浮点数运算不准的问题

```

    0     1024
    1        3
    2        5
    3        7
    4        9
    5       10
    6       13
    7      115
    8      127
    9      149
    10     221
    dtype: int64
    --------------------------------------------------
    0     1025
    1        4
    2        6
    3        8
    4       10
    5       11
    6       14
    7      116
    8      128
    9      150
    10     222
    dtype: int64
    --------------------------------------------------
    True
    --------------------------------------------------
    True
    


```python
# 然后问我们可以取出来values
print(4 in class2) 
print(4 in class2.values)
```

    True
    False
    


```python
# values值修改
class2['ming'] = 0
class2['hua'] = 0
class2['hong'] = 0

class2[['hua','hong']] = 55
class2[['hua','hong']] = [35, 55]
class2['hua','hong'] = [1, 2]  # 一层也可以
class2

```




    0       1024
    1          3
    2          5
    3          7
    4          9
    5         10
    6         13
    7        115
    8        127
    9        149
    10       221
    ming       0
    hua        1
    hong       2
    dtype: int64




```python
# 深拷贝
class4 = class2.copy()
class4 = class4+1
print(class2)
class4
```

    0       1024
    1          3
    2          5
    3          7
    4          9
    5         10
    6         13
    7        115
    8        127
    9        149
    10       221
    ming       0
    hua        1
    hong       2
    dtype: int64
    




    0       1025
    1          4
    2          6
    3          8
    4         10
    5         11
    6         14
    7        116
    8        128
    9        150
    10       222
    ming       1
    hua        2
    hong       3
    dtype: int64




```python
# 索引也可以单独的进行修改
```


```python
class2.index = [22,23,24,28,24,29,1,2,3,4,8,5,9,21]
class2
```




    22    1024
    23       3
    24       5
    28       7
    24       9
    29      10
    1       13
    2      115
    3      127
    4      149
    8      221
    5        0
    9        1
    21       2
    dtype: int64




```python
# 这个csv路径不能有中文,否则获取失败
df = pd.read_csv("./source/test.csv")
df

```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ro</th>
      <th>c1</th>
      <th>c2</th>
      <th>c3</th>
      <th>c4</th>
      <th>c5</th>
      <th>c6</th>
      <th>c7</th>
      <th>c8</th>
      <th>c9</th>
      <th>c10</th>
      <th>c11</th>
      <th>c12</th>
      <th>c13</th>
      <th>c14</th>
      <th>c15</th>
      <th>c16</th>
      <th>c17</th>
      <th>c18</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>a</td>
      <td>0</td>
      <td>5</td>
      <td>10</td>
      <td>10</td>
      <td>10</td>
      <td>10</td>
      <td>10</td>
      <td>10</td>
      <td>10</td>
      <td>10</td>
      <td>10</td>
      <td>10</td>
      <td>10</td>
      <td>10</td>
      <td>10</td>
      <td>10</td>
      <td>10</td>
      <td>10</td>
    </tr>
    <tr>
      <th>1</th>
      <td>b</td>
      <td>1</td>
      <td>6</td>
      <td>11</td>
      <td>11</td>
      <td>11</td>
      <td>11</td>
      <td>11</td>
      <td>11</td>
      <td>11</td>
      <td>11</td>
      <td>11</td>
      <td>11</td>
      <td>11</td>
      <td>11</td>
      <td>11</td>
      <td>11</td>
      <td>11</td>
      <td>11</td>
    </tr>
    <tr>
      <th>2</th>
      <td>c</td>
      <td>2</td>
      <td>7</td>
      <td>12</td>
      <td>12</td>
      <td>12</td>
      <td>12</td>
      <td>12</td>
      <td>12</td>
      <td>12</td>
      <td>12</td>
      <td>12</td>
      <td>12</td>
      <td>12</td>
      <td>12</td>
      <td>12</td>
      <td>12</td>
      <td>12</td>
      <td>12</td>
    </tr>
    <tr>
      <th>3</th>
      <td>d</td>
      <td>3</td>
      <td>8</td>
      <td>13</td>
      <td>13</td>
      <td>13</td>
      <td>13</td>
      <td>13</td>
      <td>13</td>
      <td>13</td>
      <td>13</td>
      <td>13</td>
      <td>13</td>
      <td>13</td>
      <td>13</td>
      <td>13</td>
      <td>13</td>
      <td>13</td>
      <td>13</td>
    </tr>
    <tr>
      <th>4</th>
      <td>e</td>
      <td>4</td>
      <td>9</td>
      <td>14</td>
      <td>14</td>
      <td>14</td>
      <td>14</td>
      <td>14</td>
      <td>14</td>
      <td>14</td>
      <td>14</td>
      <td>14</td>
      <td>14</td>
      <td>14</td>
      <td>14</td>
      <td>14</td>
      <td>14</td>
      <td>14</td>
      <td>14</td>
    </tr>
  </tbody>
</table>
</div>


csv中的数据都是用逗号隔开的,出自:
[python:pandas——read_csv方法](https://www.jianshu.com/p/9c12fb248ccc)