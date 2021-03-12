---
title: 'CSS中id与class 命名规则及编码的6个最佳习惯'
cover: "/img/lynk/98.jpg"
date:       2019-09-12
tags:
	- web
	- html
	- solution
	- standard
	- css
---
  
### 一、用class_name方式写类名  
  
以前喜欢用class-name写，不过好像两样也没什么差别。但我比较反对用className写类名，因为始终对浏览器大小写敏感的问题抱有怀疑态度。但是id我会写成驼峰式，理由见下一条。  
  
### 二、样式都用class而不用id  
  
有三个理由。  
  
1，id不可以重复，所以用class的话，可以肆无忌惮的用无数次。  
  
2，id的优先级太高，若是写了一个#page_contenta{color:#f60}，那你完蛋了，里面要改链接颜色，都必须加上#page_content才能越过这个优先级。  
  
3，id专门留给JS用，这样才符合表现与行为分离的原则。所以id我用驼峰式，也是为了体现这一点。  
  
### 三、margin和padding，尽量省略最后一个值  
  
比如margin:20px10px5px10px;，左右值是一样的，就应该省略掉最后一个值，写成margin:20px10px5px;这样到时候要改左右间距，改一个就好，免得改漏了。其实这个问题虽然很细小，但是可以看得出对margin四个值省略规则的熟练程度。  
  
### 四、按标准写css，再针对特定浏览器作hack  
  
比如，通常我们会遇到如下的写法：  
  
### ExampleSourceCode  
```  
.side_col_52CSS{    
float:left;    
display:inline;    
margin-left:20px;    
}  
```  
而我的写法会是：  
  
### ExampleSourceCode  
```  
.side_col_52CSS{    
float:left;    
margin-left:20px;    
}    
*.side_col_52CSS{    
_display:inline;/*hackedforIE6*/    
}  
```  
看明白了么？不应该把hack混在一起，也不应该用一种侥幸的心态，觉得float:left与display:inline写在一起没事。嗯，它们俩确实没事儿，但是其他的hack就不一定了。而且这里写display:inline纯粹就是为了解决IE6的bug，所以前面加上下划线，以明确的表达你的目的。  
  
另外不要以为凡是hack都是为IE准备的。其实有些hack是针对其他浏览器的，比如FF。这就要求你对css标准的熟练掌握，能够自信的判断哪些渲染是遵守标准，哪些违反标准的。  
此外，我喜欢在hack前面加上星号，其实这纯粹是个人习惯了。可能过段时间我就不这么用了，呵呵。  
  
五、记得加空格  
  
.class_name{property:value;}。我个人觉得合理的空格是优秀代码的一个指标。按英文的习惯，标点后面都应该带空格（如果你写Thisisapen.That’sapencil.句点后面不加空格，word里面会有错误提示）。所以既然css是外国人发明的，应该按他们的格式来写。类似的，在JS里vara=b+c;里面的空格也应该都要加。  
  
六、适当的层叠（Cascading)或缩进以定义css的“作用域”  
  
什么是“css的作用域”？其实并不是所有的样式都在所有的地方使用。有的样式只用在某一块里面，比如“导航栏”里的“搜索框”，可能应该写成：  
  
ExampleSourceCode  
  
.nav .search{}  
而有时候用层叠会增加代码优先级，所以也可以用缩进来“象征性的”体现作用域。像这样：  
  
ExampleSourceCode  
  
.login_box{}    
.forgot_pwd{}  
缩进，是为了表示它们对应的标签具有父子关系。但这样只能起一个提醒的作用。