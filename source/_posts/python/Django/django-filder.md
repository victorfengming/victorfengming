---
title: "Django模板（过滤器）"
cover: "/img/lynk/53.jpg"
date:       2019-12-03
subtitle: "django内建的过滤器"
tags:
	- Python
	- solution
	- web
	- django
---






本文转自:https://www.cnblogs.com/qingtianyu2015/p/6064073.html


  
### 1、add  
使用形式为：{ {   value | add: "2" } }  
意义：将value的值增加2  
  
  
### 2、addslashes  
使用形式为：{ {   value | addslashes  } }  
意义：在value中的引号前增加反斜线  
  
  
### 3、capfirst  
使用形式为：{ {   value | capfirst  } }  
意义：value的第一个字符转化成大写形式  
  
  
### 4、cut  
使用形式为：{ {   value | cut:arg } }， 例如，如果value是“String with spaces” arg是" "那么输出是"Stringwithspaces"  
意义：从给定value中删除所有arg的值  
  
  
### 5、date  
使用形式为：：  
(a) { {   value | date:"D d M Y"  } }，例如，如果value是一个datetime对象(datetime.datetime.now())那么输出将是字符串"Wed 09 Jan 2008"  
(b) { {   value | date  } }，这种形式没有格式化字符串，这时候，格式化字符串会自动采用DATE_FORMAT所设置的形式。  
意义：将日期格式数据按照给定的格式输出  
  
  
### 6、default  
使用形式：{ {   value | default: "nothing"  } }，例如，如果value是“”，那么输出将是nothing  
意义：如果value的意义是False，那么输出使用缺省值  
  
  
### 7、default_if_none  
使用形式：{ {   value | default_if_none:"nothing"  } }，例如，如果value是None，那么输出将是nothing  
意义：如果value是None，那么输出将使用缺省值  
### 8、dictsort  
意义：如果value的值是一个字典，那么返回值是按照关键字排序的结果  
使用形式：{ {   value | dictsort:"name" } }，例如，  
如果value是：  
[  
{'name': 'zed', 'age': 19},  
{'name': 'amy', 'age': 22},  
{'name': 'joe', 'age': 31}, ]  
那么，输出是：  
[  
{'name': 'amy', 'age': 22},  
{'name': 'joe', 'age': 31},  
{'name': 'zed', 'age': 19}, ]  
  
  
### 9、dictsortreversed  
意义：如果value的值是一个字典，那么返回值是按照关键字排序的结果的反序  
使用形式：与上述(8)完全相同。  
  
  
### 10、divisibleby  
使用形式：{ {   value | divisibleby:arg } }，如果value是21，arg是3，那么输出将是True  
意义：如果value能够被arg整除，那么返回值将是True  
  
  
### 11、escape  
使用形式：{ {   value | escape } }  
意义：替换value中的某些字符，以适应HTML格式，包括：  
< is converted to &lt;  
> is converted to &gt;  
' (single quote) is converted to &#39;  
" (double quote) is converted to &quot;  
& is converted to &amp;  
  
注：escape仅仅在输出的时候才起作用，所以escape不能够用在链式过滤器的中间，  
他应该总是最后一个过滤器，如果想在链式过滤器的中间使用，那么可以使用force_escape  
  
### 12、escapejs  
使用形式：{ {   value | escapejs  } }  
意义：替换value中的某些字符，以适应JAVASCRIPT和JSON格式。  
  
  
### 13、filesizeformat  
使用形式：{ {   value | filesizeformat  } }  
意义：格式化value，使其成为易读的文件大小，例如：13KB，4.1MB等。  
  
  
### 14、first  
使用形式：{ {   value | first  } }  
意义：返回列表中的第一个Item，例如，如果value是列表['a','b','c']，那么输出将是'a'。  
### 15、floatformat  
使用形式：{ {   value | floatformat } }或者{ {  value|floatformat:arg } }， arg可以是正数也可以是负数。没有参数的floatformat相当于floatformat:-1  
  
#### 1、如果不带arg，那么引擎会四舍五入，同时最多只保留一位小数。  
34.23234{ {   value|floatformat  } }34.234.00000{ {   value|floatformat  } }3434.26000{ {   value|floatformat  } }34.3  
  
#### 2、如果arg是正数，那么引擎会四舍五入，同时保留arg位的小数。  
34.23234{ {   value|floatformat:3  } }34.23234.00000{ {   value|floatformat:3  } }34.00034.26000{ {   value|floatformat:3  } }34.260  
  
#### 3、如果arg是负数，那么引擎会四舍五入，如果有小数部分，那么保留arg位小数；否则，则没有任何小数部分。  
34.23234{ {   value|floatformat:"-3"  } }34.23234.00000{ {   value|floatformat:"-3"  } }3434.26000{ {   value|floatformat:"-3"  } }34.26(16)get_digit  
  
使用形式：{ {   value | get_digit:"arg" } }，例如，如果value是123456789，arg是2，那么输出是8  
意义：给定一个数字，返回，请求的数字，记住：1代表最右边的数字，如果value不是合法输入，那么会返回所有原有值。  
  
  
### 16、iriencode  
使用形式：{ {  value | iriencode } }  
意义：如果value中有非ASCII字符，那么将其进行抓化成URL中适合的编码，如果value已经进行过URLENCODE，  
改操作就不会再起作用。  
  
  
### 17、join  
使用形式：{ {   value | join:"arg" } }，如果value是['a','b','c']，arg是'//'那么输出是a//b//c  
意义：使用指定的字符串连接一个list，作用如同python的str.join(list)  
  
  
### 18、last  
使用形式：{ {   value | last  } }  
意义：返回列表中的最后一个Item  
  
  
### 19、length  
使用形式：{ {   value | length  } }  
意义：返回value的长度。  
  
  
### 20、length_is  
使用形式：{ {   value | length_is:"arg" } }  
意义：返回True，如果value的长度等于arg的时候，例如：如果value是['a','b','c']，arg是3，那么返回True  
  
  
### 21、linebreaks  
使用形式：{ {  value|linebreaks } }  
意义：value中的"\n"将被<br/>替代，并且整个value使用</p>包围起来，从而适和HTML的格式  
  
  
### 22、linebreaksbr  
使用形式：{ {  value |linebreaksbr } }  
意义：value中的"\n"将被<br/>替代  
  
  
### 23、linenumbers  
使用形式：{ {  value | linenumbers } }  
意义：显示的文本，带有行数。  
  
  
### 24、ljust  
使用形式：{ {  value | ljust } }  
意义：在一个给定宽度的字段中，左对齐显示value  
  
  
### 25、center  
使用形式：{ {  value | center } }  
意义：在一个给定宽度的字段中，中心对齐显示value  
  
  
### 26、rjust  
使用形式：{ {  value | rjust } }  
意义：在一个给定宽度的字段中，右对齐显示value  
  
  
### 27、lower  
使用形式：{ {  value | lower } }  
意义：将一个字符串转换成小写形式  
  
  
### 28、make_list  
使用形式：{ {  value | make_list } }  
意义：将value转换成一个list，对于字符串，转换成字符list；对于整数，转换成整数list  
例如value是Joel，那么输出将是[u'J',u'o',u'e',u'l']；value是123，那么输出将是[1,2,3]  
  
  
### 29、pluralize  
使用形式：{ {  value | pluralize } }，或者{ {  value | pluralize:"es" } }，或者{ {  value | pluralize:"y,ies" } }  
意义：如果value不是1，则返回一个复数后缀，缺省的后缀是's'  
  
  
### 30、random  
使用形式：{ {  value | random } }  
意义：从给定的list中返回一个任意的Item  
  
  
### 31、removetags  
使用形式：{ {  value | removetags:"tag1 tag2 tag3..." } }  
意义：删除value中tag1,tag2....的标签。例如，如果value是<b>Joel</b> <button>is</button> a <span>slug</span>  
tags是"b span"，那么输出将是：Joel <button>is</button> a slug  
  
  
### 32、safe  
使用形式：{ {  value | safe } }  
意义：当系统设置autoescaping打开的时候，该过滤器使得输出不进行escape转换  
  
  
### 33、safeseq  
与上述safe基本相同，但有一点不同的就是：safe是针对字符串，而safeseq是针对多个字符串组成的sequence  
  
  
### 34、slice  
使用形式：{ {  some_list | slice:":2" } }  
意义：与python语法中的slice相同，:2表示第一的第二个元素  
  
  
### 35、slugify  
使用形式：{ {  value | slugify } }  
意义：将value转换成小写形式，同事删除所有分单词字符，并将空格变成横线  
例如：如果value是Joel is a slug，那么输出将是joel-is-a-slug  
  
  
### 36、stringformat  
这个不经常用，先不说  
  
  
### 37、striptags  
使用形式：{ {  value | striptags } }  
意义：删除value中的所有HTML标签  
  
  
### 38、time  
使用形式：{ {  value | time:"H:i" } }或者{ {  value | time } }  
意义：格式化时间输出，如果time后面没有格式化参数，那么输出按照TIME_FORMAT中设置的进行。  
  
  
### 39、title  
转换一个字符串成为title格式。  
  
  
### 40、truncatewords  
使用形式：{ {  value | truncatewords:2 } }  
意义：将value切成truncatewords指定的单词数目  
例如，如果value是Joel is a slug 那么输出将是：Joel is ...  
  
  
### 41、truncatewords_html  
使用形式同(39)  
意义：truncation点之前如果某个标签打开了，但是没有关闭，那么在truncation点会立即关闭。  
因为这个操作的效率比truncatewords低，所有只有在value是html格式时，才考虑使用。  
  
  
### 42、upper  
转换一个字符串为大写形式  
  
  
### 43、urlencode  
将一个字符串进行URLEncode  
  
  
### 44、urlize  
意义：将一个字符串中的URL转化成可点击的形式。  
使用形式：{ {   value | urlize  } }  
例如，如果value是Check out www.djangoproject.com，那么输出将是：  
Check out <a href="http://www.djangoproject.com">www.djangoproject.com</a>  
  
  
### 45、urlizetrunc  
使用形式：{ {   value | urlizetrunc:15 } }  
意义：与(43)相同，但是有一点不同就是现实的链接字符会被truncate成特定的长度，后面以...现实。  
  
  
### 46、wordcount  
返回字符串中单词的数目  
  
  
### 47、wordwrap  
使用形式：{ {  value | wordwrap:5 } }  
意义：按照指定的长度包装字符串  
例如，如果value是Joel is a slug，那么输出将会是：  
Joel  
is a  
slug  
  
  
### 48、timesince  
使用形式：{ {  value | timesince:arg } }  
意义：返回参数arg到value的天数和小时数  
例如，如果 blog_date 是一个日期实例表示 2006-06-01 午夜， 而 comment_date 是一个日期实例表示 2006-06-01 早上8点，  
那么 { {   comment_date|timesince:blog_date  } } 将返回 "8 hours".  
  
  
### 49、timeuntil  
使用形式：{ {  value | timeuntil } }  
意义：与(47)基本相同，一个不同点就是，返回的是value距离当前日期的天数和小时数。