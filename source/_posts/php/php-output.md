---
title: "PHP中的输出语句对比"
date:       2019-10-10
tags:
	- php
	- background
	- basis
---

通过前面的学习了解了php的基本语法，今天向大家简单介绍php的几种输出方式：

1.   echo 常用的输出语句，例如：echo 'helloworld！';
2.   print() 输出语句，有返回值。例如：print('helloworld！'); 输出成功返回1，失败返回0。
3.   printf(); 格式化输出字符串。例如：printf("%d,%f",12,12.3);
4.   print_r(); 输出数组、对象等复合数据类型。例如：print_r($array);
5.  var_dump(); 可以判断一个变量的类型与长度,并输出变量的数值。例如：var_dump('helloworld！');
6.  sprintf 函数也用做字符串格式化。例如： $formatted = sprintf ( "%01.2f ", '123.1' ) ;  

为方便我们的记忆，先对这几种不同的输出方式做个对比。

- echo   - 可以输出一个或多个字符串
- print   - 只能输出简单类型变量的值,如int,string
- print_r - 可以输出复杂类型变量的值,如数组,对象
- printf -函数用于格式化输出字符串，主要用于字符串中以%开头的格式字符串替换。
- sprintf -函数也用做字符串格式化。该函数与 printf 函数基本相同， 但它可以将转换后的结果保存到一个字符串变量中，而不是直接输出。(因为跟printf类似，下面就不做详细演示了)
- var_dump -打印变量的相关信息,包括表达式的类型与值,通过缩进显示其结构。

**提示**：echo输出的速度比print快,echo是PHP语句,没有返回值,print和print_r是PHP函数,函数有返回值。

print返回值为1(int类型),print_r返回值为true(bool类型)。

### echo
echo 是一个语言结构，使用的时候可以不用加括号，也可以加上括号： echo 或 echo()。

##### 显示字符串

下面的实例演示了如何使用 echo 命令输出字符串（字符串可以包含 HTML 标签）：

```php
<?php
echo "<h2>PHP is fun!</h2>";
echo "Hello world!<br>";
echo "I'm about to learn PHP!<br>";
echo "This", " string", " was", " made", " with multiple parameters.";
?>
```

上面echo输出结果：

```
PHP is fun!
 
Hello world!
I'm about to learn PHP!
This string was made with multiple parameters.
```


##### 显示变量
下面的实例演示了如何使用 echo 命令输出变量和字符串：
```php
<?php
$txt1="Learn PHP";
$txt2="w3cschool.cn";
$cars=array("Volvo","BMW","Toyota");
 
echo $txt1;
echo "<br>";
echo "Study PHP at $txt2"; //这里外面用的是双引号，在php里，双引号是可以解析变量的
echo "My car is a {$cars[0]}";
?>
```

上面echo输出结果：

```
Learn PHP
Study PHP at w3cschool.cn
My car is a Volvo
```
### print 语句
print 同样是一个语言结构，可以使用括号，也可以不使用括号： print 或 print()。
##### 显示字符串

下面的实例演示了如何使用 print 命令输出字符串（字符串可以包含 HTML 标签）：

```php
<?php
print "<h2>PHP is fun!</h2>";
print "Hello world!<br>";
print "I'm about to learn PHP!";
?>
```

运行结果：

```
PHP is fun!
 
Hello world!
I'm about to learn PHP!
```

##### 显示变量
下面的实例演示了如何使用 print 命令输出变量和字符串：

```php
<?php
$txt1="Learn PHP";
$txt2="w3cschool.cn";
$cars=array("Volvo","BMW","Toyota");
 
print $txt1;
print "<br>";
print "Study PHP at $txt2";
print "My car is a {$cars[0]}";
?>
```
运行结果：

```
Learn PHP
Study PHP at w3cschool.cn
My car is a Volvo
```

### print_r 语句
print_r 显示关于一个变量的易于理解的信息,如果给出的是 `string`、`integer` 或 `float`，将打印变量值本身。

如果给出的是 `array`，将会按照一定格式显示键和元素。`object`与数组类似。

使用时必须加上括号:print_r()。

小提示:print_r()会将把数组的指针移到最后边。使用 `reset() `可让指针回到开始处。

##### 显示字符串

下面的实例演示了如何使用 print_r 命令输出字符串（字符串可以包含 HTML 标签）：

```php
<?php
print_r("Hello World!");
print_r("Goodbye World!");
?>
```

运行结果：

```
Hello World! Goodbye World
```

显示变量

下面的实例演示了如何使用 print_r 命令输出变量和字符串：

```php
<?php
$txt1="Hello World!";
$cars=array("Volvo","BMW","Toyota");
 
print_r($txt1);
print_r($cars);
?>


```
运行结果：
```
Hello World!Array ( [0] => Volvo [1] => BMW [2] => Toyota ) <!-- 后面array是打印的$cars数组 -->
```

### printf
printf() 函数输出格式化的字符串。

arg1、arg2、arg++ 参数将被插入到主字符串中的百分号（%）符号处。该函数是逐步执行的。在第一个 % 符号处，插入 arg1，在第二个 % 符号处，插入 arg2，依此类推。

**注释**：如果 % 符号多于 arg 参数，则您必须使用占位符。占位符被插入到 % 符号之后，由数字和 "$" 组成。

##### 语法

<table class="dataintable" style="height: 543px; width: 1233px;">
<tbody>
<tr><th>参数</th><th>描述</th></tr>
<tr>
<td><em>format</em></td>
<td>
<p>必需。规定字符串以及如何格式化其中的变量。</p>
<p>可能的格式值：</p>
<ul class="listintable">
<li>%% - 返回一个百分号 %</li>
<li>%b - 二进制数</li>
<li>%c - ASCII 值对应的字符</li>
<li>%d - 包含正负号的十进制数（负数、0、正数）</li>
<li>%e - 使用小写的科学计数法（例如 1.2e+2）</li>
<li>%E - 使用大写的科学计数法（例如 1.2E+2）</li>
<li>%u - 不包含正负号的十进制数（大于等于 0）</li>
<li>%f - 浮点数（本地设置）</li>
<li>%F - 浮点数（非本地设置）</li>
<li>%g - 较短的 %e 和 %f</li>
<li>%G - 较短的 %E 和 %f</li>
<li>%o - 八进制数</li>
<li>%s - 字符串</li>
<li>%x - 十六进制数（小写字母）</li>
<li>%X - 十六进制数（大写字母）</li>
</ul>
<p>附加的格式值。必需放置在 % 和字母之间（例如 %.2f）：</p>
<ul class="listintable">
<li>+ （在数字前面加上 + 或 - 来定义数字的正负性。默认地，只有负数做标记，正数不做标记）</li>
<li>' （规定使用什么作为填充，默认是空格。它必须与宽度指定器一起使用。）</li>
<li>- （左调整变量值）</li>
<li>[0-9] （规定变量值的最小宽度）</li>
<li>.[0-9] （规定小数位数或最大字符串长度）</li>
</ul>
<p class="note">注释：如果使用多个上述的格式值，它们必须按照上面的顺序进行使用，不能打乱。</p>
</td>
</tr>
<tr>
<td><em>arg1</em></td>
<td>必需。规定插到<span class="Apple-converted-space">&nbsp;<em>format</em><span class="Apple-converted-space">&nbsp;字符串中第一个 % 符号处的参数。</span></span></td>
</tr>
<tr>
<td><em>arg2</em></td>
<td>必需。规定插到<span class="Apple-converted-space">&nbsp;<em>format</em><span class="Apple-converted-space">&nbsp;字符串中第二个 % 符号处的参数。</span></span></td>
</tr>
<tr>
<td><em>arg++</em></td>
<td>可选。规定插到<span class="Apple-converted-space">&nbsp;<em>format</em><span class="Apple-converted-space">&nbsp;字符串中第三、四等等 % 符号处的参数。</span></span></td>
</tr>
</tbody>
</table>


提示：相关函数：sprintf()、 vprintf()、 vsprintf()、 fprintf() 和 vfprintf()

```php
<?php
$number = 9;
$str = "北京";
printf("在%s有 %u 百万辆自行车。",$str,$number);
?>
```　　
运行结果：
```
在北京有 9 百万辆自行车。
```

使用格式值 %f：

```php
<?php
$number = 123;
printf("%f",$number);
?>
```　　
运行结果：
```
123.000000  这里默认省略到小数点后六位
```
使用占位符：

```php
<?php
$number = 123;
printf("有两位小数：%1\$.2f<br>没有小数：%1\$u",$number);
?>
```　　
运行结果：
```
有两位小数：123.00
没有小数：123
```

**所有可能的格式值的演示：**

```php
<?php
$num1 = 123456789;
$num2 = -123456789;
$char = 50; // ASCII 字符 50 是 2
 
// 注释：格式值 "%%" 返回百分号
printf("%%b = %b <br>",$num1); // 二进制数
printf("%%c = %c <br>",$char); // ASCII 字符
printf("%%d = %d <br>",$num1); // 带符号的十进制数
printf("%%d = %d <br>",$num2); // 带符号的十进制数
printf("%%e = %e <br>",$num1); // 科学计数法（小写）
printf("%%E = %E <br>",$num1); // 科学计数法（大写）
printf("%%u = %u <br>",$num1); // 不带符号的十进制数（正）
printf("%%u = %u <br>",$num2); // 不带符号的十进制数（负）
printf("%%f = %f <br>",$num1); // 浮点数（视本地设置）
printf("%%F = %F <br>",$num1); // 浮点数（不视本地设置）
printf("%%g = %g <br>",$num1); // 短于 %e 和 %f
printf("%%G = %G <br>",$num1); // 短于 %E 和 %f
printf("%%o = %o <br>",$num1); // 八进制数
printf("%%s = %s <br>",$num1); // 字符串
printf("%%x = %x <br>",$num1); // 十六进制数（小写）
printf("%%X = %X <br>",$num1); // 十六进制数（大写）
printf("%%+d = %+d <br>",$num1); // 符号说明符（正）
printf("%%+d = %+d <br>",$num2); // 符号说明符（负）
?>
```　　
运行结果：
```
%b = 111010110111100110100010101
%c = 2
%d = 123456789
%d = -123456789
%e = 1.234568e+8
%E = 1.234568E+8
%u = 123456789
%u = 4171510507
%f = 123456789.000000
%F = 123456789.000000
%g = 1.23457e+8
%G = 1.23457E+8
%o = 726746425
%s = 123456789
%x = 75bcd15
%X = 75BCD15
%+d = +123456789
%+d = -123456789
```

##### 字符串说明符的演示：

```php
<?php
$str1 = "Hello";
$str2 = "Hello world!";
 
printf("[%s]<br>",$str1);
printf("[%8s]<br>",$str1);
printf("[%-8s]<br>",$str1);
printf("[%08s]<br>",$str1);
printf("[%'*8s]<br>",$str1);
printf("[%8.8s]<br>",$str2);
?>
```　
　
运行结果：
```
[Hello]
[ Hello]
[Hello ]
[000Hello]
[***Hello]
[Hello wo]
```

### var_dump
 — 打印变量的相关信息，此函数显示关于一个或多个表达式的结构信息，包括表达式的类型与值。数组将递归展开值，通过缩进显示其结构。

```php
<?php
$a = array(1, 2, array("a", "b", "c"));
var_dump($a);
?>
```
运行结果：
```
array(3) {
  [0]=>
  int(1) 前面是类型
  [1]=>
  int(2)
  [2]=>
  array(3) {
    [0]=>
    string(1) "a"
    [1]=>
    string(1) "b"
    [2]=>
    string(1) "c"
  }
}
```
再来一个例子
```php
<?php
 
$b = 3.1;
$c = true;
var_dump($b, $c);

?>
```
运行结果如下：
```
float(3.1)
bool(true)
```
