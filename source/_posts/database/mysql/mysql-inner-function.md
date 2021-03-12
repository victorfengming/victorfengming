---
title: "mysql中的内置函数"
date:       2019-10-03
tags:
	- Linux
	- database
	- mysql
---

<div id="cnblogs_post_body" class="blogpost-body cnblogs-markdown">
    <p>mysql内置函数列表可以从<a href="http://dev.mysql.com/doc/refman/5.6/en/func-op-summary-ref.html">mysql官方文档</a>查询，这里仅分类简单介绍一些可能会用到的函数。</p>
<h3 id="数学函数">1 数学函数</h3>
<p>abs(x)<br>
pi()<br>
mod(x,y)<br>
sqrt(x)<br>
ceil(x)或者ceiling(x)<br>
rand(),rand(N):返回0-1间的浮点数，使用不同的seed N可以获得不同的随机数<br>
round(x, D)：四舍五入保留D位小数，D默认为0， 可以为负数， 如round(19, -1)返回20<br>
truncate(x, D):截断至保留D位小数，D可以为负数， 如trancate(19,-1)返回10<br>
sign(x): 返回x的符号，正负零分别返回1， -1， 0<br>
pow(x,y)或者power(x,y)<br>
exp(x)：e^x<br>
log(x)：自然对数<br>
log10(x)：以10为底的对数<br>
radians(x):角度换弧度<br>
degrees(x):弧度换角度<br>
sin(x)和asin(x):<br>
cos(x)和acos(x):<br>
tan(x)和atan(x):<br>
cot(x):</p>
<h3 id="字符串函数">2 字符串函数</h3>
<p>char_length(str):返回str所包含的字符数，一个多字节字符算一个字符<br>
length(str): 返回字符串的字节长度，如utf8中，一个汉字3字节，数字和字母算一个字节<br>
concat(s1, s1, ...): 返回连接参数产生的字符串<br>
concat_ws(x, s1, s2, ...): 使用连接符x连接其他参数产生的字符串<br>
INSERT(str,pos,len,newstr):返回str,其起始于pos，长度为len的子串被newstr取代。<br>
1. 若pos不在str范围内，则返回原字符串str<br>
2. 若str中从pos开始的子串不足len,则将从pos开始的剩余字符用newstr取代<br>
3. 计算pos时从1开始，若pos=3,则从第3个字符开始替换<br>
lower（str)或者lcase(str):<br>
upper(str)或者ucase(str):<br>
left(s,n):返回字符串s最左边n个字符<br>
right(s,n): 返回字符串最右边n个字符<br>
lpad(s1, len, s2): 用s2在s1左边填充至长度为len, 若s1的长度大于len,则截断字符串s1至长度len返回<br>
rpad(s1, len, s2):<br>
ltrim(s):删除s左侧空格字符<br>
rtrim(s):<br>
TRIM([{BOTH | LEADING | TRAILING} [remstr] FROM] str)或TRIM([remstr FROM] str)：从str中删除remstr, remstr默认为空白字符<br>
REPEAT(str,count)：返回str重复count次得到的新字符串<br>
REPLACE(str,from_str,to_str)： 将str中的from_str全部替换成to_str<br>
SPACE(N):返回长度为N的空白字符串<br>
STRCMP(str1,str2):若str1和str2相同，返回0， 若str1小于str2, 返回-1， 否则返回1.<br>
SUBSTRING(str,pos), SUBSTRING(str FROM pos), SUBSTRING(str,pos,len), SUBSTRING(str FROM pos FOR len),MID(str,pos,len): 获取特定位置，特定长度的子字符串<br>
LOCATE(substr,str), LOCATE(substr,str,pos),INSTR(str,substr),POSITION(substr IN str): 返回字符串中特定子串的位置，注意这里INSTR与其他函数的参数位置是相反的<br>
REVERSE(str)<br>
ELT(N,str1,str2,str3,...)：返回参数strN, 若N大于str参数个数，则返回NULL<br>
FIELD(str,str1,str2,str3,...): 返回str在后面的str列表中第一次出现的位置，若找不到str或者str为NULL, 则返回0<br>
FIND_IN_SET(str,strlist)：strlist是由','分隔的字符串，若str不在strlist或者strlist为空字符串，则返回0；若任意一个参数为NULL则返回ＮＵＬＬ<br>
MAKE_SET(bits,str1,str2,...): 由bits的作为位图来选取strN参数，选中的参数用','连接后返回</p>
<h3 id="日期和时间函数">3 日期和时间函数</h3>
<p>CURDATE(), CURRENT_DATE, CURRENT_DATE():用于获取当前日期，格式为'YYYY-MM-DD'; 若+0则返回YYYYMMDD<br>
UTC_DATE, UTC_DATE():返回当前世界标准时间<br>
CURTIME([fsp]), CURRENT_TIME, CURRENT_TIME([fsp]): 用于获取当前时间， 格式为'HH:MM:SS' 若+0则返回 HHMMSS<br>
UTC_TIME, UTC_TIME([fsp])<br>
CURRENT_TIMESTAMP, CURRENT_TIMESTAMP([fsp]), LOCALTIME, LOCALTIME([fsp]), SYSDATE([fsp]), NOW([fsp]): 用于获取当前的时间日期，格式为'YYYY-MM-DD HH:MM:SS'，若+0则返回YYYYMMDDHHMMSS<br>
UTC_TIMESTAMP, UTC_TIMESTAMP([fsp])<br>
UNIX_TIMESTAMP(), UNIX_TIMESTAMP(date)：返回一个unix时间戳（'1970-01-01 00:00:00' UTC至今或者date的秒数），这实际上是从字符串到整数的一个转化过程<br>
FROM_UNIXTIME(unix_timestamp), FROM_UNIXTIME(unix_timestamp,format)：从时间戳返回'YYYY-MM-DD HH:MM:SS' 或者YYYYMMDDHHMMSS，加入format后根据所需的format显示。<br>
MONTH(date)<br>
MONTHNAME(date)<br>
DAYNAME(date)<br>
DAY(date)，DAYOFMONTH(date)：1-31或者0<br>
DAYOFWEEK(date)：1-7==&gt;星期天-星期六<br>
DAYOFYEAR(date)： 1-365（366）<br>
WEEK(date[,mode])：判断是一年的第几周，如果1-1所在周在新的一年多于4天，则将其定为第一周；否则将其定为上一年的最后一周。mode是用来人为定义一周从星期几开始。<br>
WEEKOFYEAR(date)：类似week(date,3)，从周一开始计算一周。<br>
QUARTER(date)：返回1-4<br>
HOUR(time)：返回时间中的小时数，可以大于24<br>
MINUTE(time)：<br>
SECOND(time)：<br>
EXTRACT(unit FROM date)：提取日期时间中的要素</p>
<pre class="sql"><code class="hljs">    <span class="hljs-keyword">SELECT</span> <span class="hljs-keyword">EXTRACT</span>(<span class="hljs-keyword">YEAR</span> <span class="hljs-keyword">FROM</span> <span class="hljs-string">'2009-07-02'</span>); ##2009
    <span class="hljs-keyword">SELECT</span> <span class="hljs-keyword">EXTRACT</span>(YEAR_MONTH <span class="hljs-keyword">FROM</span> <span class="hljs-string">'2009-07-02 01:02:03'</span>);##200907
    <span class="hljs-keyword">SELECT</span> <span class="hljs-keyword">EXTRACT</span>(DAY_MINUTE <span class="hljs-keyword">FROM</span> <span class="hljs-string">'2009-07-02 01:02:03'</span>);##20102
    <span class="hljs-keyword">SELECT</span> <span class="hljs-keyword">EXTRACT</span>(<span class="hljs-keyword">MICROSECOND</span> <span class="hljs-keyword">FROM</span> <span class="hljs-string">'2003-01-02 10:30:00.000123'</span>);##123</code></pre>
<p>TIME_TO_SEC(time)<br>
SEC_TO_TIME(seconds)</p>
<p>TO_DAYS(date): 从第0年开始的天数<br>
TO_SECNDS(expr)：从第0年开始的秒数</p>
<p>ADDDATE(date,INTERVAL expr unit), ADDDATE(expr,days),DATE_ADD(date,INTERVAL expr unit)<br>
DATE_SUB(date,INTERVAL expr unit), DATE_SUB(date,INTERVAL expr unit)<br>
ADDTIME(expr1,expr2)<br>
SUBTIME(expr1,expr2)</p>
<pre class="sql"><code class="hljs">    <span class="hljs-keyword">SELECT</span> <span class="hljs-keyword">ADDTIME</span>(<span class="hljs-string">'2007-12-31 23:59:59.999999'</span>, <span class="hljs-string">'1 1:1:1.000002'</span>);##'2008-01-02 01:01:01.000001'
    <span class="hljs-keyword">SELECT</span> <span class="hljs-keyword">ADDTIME</span>(<span class="hljs-string">'01:00:00.999999'</span>, <span class="hljs-string">'02:00:00.999998'</span>);##'03:00:01.999997'</code></pre>
<p>注意：时间日期的加减也可以直接用+/-来进行</p>
<pre class="sql"><code class="hljs">    date + INTERVAL expr unit
    date - INTERVAL expr unit
    如：
    <span class="hljs-keyword">SELECT</span> <span class="hljs-string">'2008-12-31 23:59:59'</span> + <span class="hljs-built_in">INTERVAL</span> <span class="hljs-number">1</span> <span class="hljs-keyword">SECOND</span>;##'2009-01-01 00:00:00'
    <span class="hljs-keyword">SELECT</span> <span class="hljs-built_in">INTERVAL</span> <span class="hljs-number">1</span> <span class="hljs-keyword">DAY</span> + <span class="hljs-string">'2008-12-31'</span>;##'2009-01-01'
    <span class="hljs-keyword">SELECT</span> <span class="hljs-string">'2005-01-01'</span> - <span class="hljs-built_in">INTERVAL</span> <span class="hljs-number">1</span> <span class="hljs-keyword">SECOND</span>;##'2004-12-31 23:59:59'</code></pre>
<p>DATE_FORMAT(date,format):<br>
DATEDIFF(expr1,expr2):返回相差的天数<br>
TIMEDIFF(expr1,expr2)：返回相隔的时间</p>
<h3 id="条件判断函数">4 条件判断函数</h3>
<p>IF(expr1,expr2,expr3)：如果expr1不为0或者NULL,则返回expr2的值，否则返回expr3的值<br>
IFNULL(expr1,expr2)：如果expr1不为NULL,返回expr1,否则返回expr2<br>
NULLIF(expr1,expr2): 如果expr1=expr2则返回NULL, 否则返回expr2<br>
CASE value WHEN [compare_value] THEN result [WHEN [compare_value] THEN result ...] [ELSE result] END<br>
当compare_value=value时返回result<br>
CASE WHEN [condition] THEN result [WHEN [condition] THEN result ...] [ELSE result] END<br>
当condition为TRUE时返回result</p>
<pre class="sql"><code class="hljs">    <span class="hljs-keyword">SELECT</span> <span class="hljs-keyword">CASE</span> <span class="hljs-number">1</span> <span class="hljs-keyword">WHEN</span> <span class="hljs-number">1</span> <span class="hljs-keyword">THEN</span> <span class="hljs-string">'one'</span>
        <span class="hljs-keyword">WHEN</span> <span class="hljs-number">2</span> <span class="hljs-keyword">THEN</span> <span class="hljs-string">'two'</span> <span class="hljs-keyword">ELSE</span> <span class="hljs-string">'more'</span> <span class="hljs-keyword">END</span>;##'one'
    <span class="hljs-keyword">SELECT</span> <span class="hljs-keyword">CASE</span> <span class="hljs-keyword">WHEN</span> <span class="hljs-number">1</span>&gt;<span class="hljs-number">0</span> <span class="hljs-keyword">THEN</span> <span class="hljs-string">'true'</span> <span class="hljs-keyword">ELSE</span> <span class="hljs-string">'false'</span> <span class="hljs-keyword">END</span>;##'true'
    <span class="hljs-keyword">SELECT</span> <span class="hljs-keyword">CASE</span> <span class="hljs-built_in">BINARY</span> <span class="hljs-string">'B'</span>
        <span class="hljs-keyword">WHEN</span> <span class="hljs-string">'a'</span> <span class="hljs-keyword">THEN</span> <span class="hljs-number">1</span> <span class="hljs-keyword">WHEN</span> <span class="hljs-string">'b'</span> <span class="hljs-keyword">THEN</span> <span class="hljs-number">2</span> <span class="hljs-keyword">END</span>;##NULL</code></pre>
<h3 id="系统信息函数">5 系统信息函数</h3>
<p>VERSION():返回mysql服务器的版本，是utf8编码的字符串<br>
CONNECTION_ID()：显示连接号（连接的线程号）<br>
DATABASE()，SCHEMA()：显示当前使用的数据库<br>
SESSION_USER(), SYSTEM_USER(), USER(), CURRENT_USER, CURRENT_USER():返回当前的用户名@主机，utf8编码字符串<br>
CHARSET(str)<br>
COLLATION(str)<br>
LAST_INSERT_ID()：自动返回最后一个insert或者update查询， 为auto_increment列设置的第一个发生的值</p>
<h3 id="加密和压缩函数">6 加密和压缩函数</h3>
<p>PASSWORD(str):这个函数的输出与变量old_password有关。old_password 在mysql5.6中默认为0。 不同取值的效果如下表<br>
<img src="https://images2015.cnblogs.com/blog/865265/201602/865265-20160224150201724-1500361171.png"><br>
old_password=1时， password(str)的效果与old_password(str)相同，由于其不够安全已经弃用（5.6.5以后）。<br>
old_password=2时，在生成哈希密码时会随机加盐。</p>
<p>MD5(str):计算MD5 128位校验和，返回32位16进制数构成的字符串，当str为NULL时返回NULL。可以用作哈希密码<br>
SHA1(str), SHA(str)：计算160位校验和，返回40位16进制数构成的字符串，当str为NULL时返回NULL。<br>
SHA2(str, hash_length)：计算SHA-2系列的哈希方法(SHA-224, SHA-256, SHA-384, and SHA-512). 第一个参数为待校验字符串，第二个参数为结果的位数（224， 256， 384， 512）<br>
ENCRYPT(str[,salt]): 用unix crypt()来加密str. salt至少要有两位字符，否则会返回NULL。若未指定salt参数，则会随机添加salt。</p>
<p>ECODE(crypt_str,pass_str):解密crypt_str, pass_str用作密码<br>
ENCODE(str,pass_str)：用pass_str作为密码加密str</p>
<p>DES_ENCRYPT(str[,{key_num|key_str}])：用Triple-DES算法编码str， 这个函数只有在mysql配置成支持ssl时才可用。<br>
DES_DECRYPT(crypt_str[,key_str])</p>
<p>AES_ENCRYPT(str,key_str[,init_vector])<br>
AES_DECRYPT(crypt_str,key_str[,init_vector])</p>
<p>COMPRESS(string_to_compress)：返回二进制码<br>
UNCOMPRESS(string_to_uncompress)</p>
<h3 id="聚合函数">7 聚合函数</h3>
<p>若在没使用group by时使用聚合函数，相当于把所有的行都归于一组来进行处理。除非特殊说明，一般聚合函数会忽略掉NULL.<br>
AVG([DISTINCT] expr): 返回expr的平均值，distinct选项用于忽略重复值<br>
COUNT([DISTINCT] expr)：返回select中expr的非0值个数，返回值为bigint类型<br>
group_concat:连接组内的非空值，若无非空值，则返回NULL</p>
<pre class="sql"><code class="hljs">        GROUP_CONCAT([DISTINCT] expr [,expr ...]
             [ORDER BY {unsigned_integer | col_name | expr}
                    [ASC | DESC] [,col_name ...]]
            [SEPARATOR str_val])</code></pre>
<p>MAX([DISTINCT] expr)<br>
MIN([DISTINCT] expr)</p>
<p>SUM([DISTINCT] expr)<br>
VAR_POP(expr)<br>
VARIANCE(expr)：同VAR_POP(expr)，但是这是标准sql的一个扩展函数<br>
VAR_SAMP(expr)<br>
STD(expr): 这是标准sql的一个扩展函数<br>
STDDEV(expr)：这个函数是为了跟oracle兼容而设置的<br>
STDDEV_POP(expr)：这个是sql标准函数</p>
<p>STDDEV_SAMP(expr)：样本标准差</p>
<h3 id="格式或类型转化函数">8 格式或类型转化函数</h3>
<p>FORMAT(X,D[,locale])：将数字X转化成'#,###,###.##'格式，D为保留的小数位数<br>
CONV(N,from_base,to_base)：改变数字N的进制，返回值为该进制下的数字构成的字符串<br>
INET_ATON(expr)：ip字符串转数字<br>
INET_NTOA(expr)：数字转ip字符串<br>
CAST(expr AS type)：转换数据类型<br>
CONVERT(expr,type), CONVERT(expr USING transcoding_name)： type可以为BINARY[(N)]，CHAR[(N)]，DATE，DATETIME， DECIMAL[(M[,D])]，DECIMAL[(M[,D])]，TIME，UNSIGNED [INTEGER]等等。transcoding_name如utf8等等</p>

</div>