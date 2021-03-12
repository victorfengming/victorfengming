---
title: 'js和jq选择相关'
date:       2019-09-07
subtitle: '判断select是否选中、获取select选中的值'
tags:
	- JavaScript
	- web
	- solution
---













### 原生js
```

var   mySelect = document.getElementById(”testSelect”);//定位id(获取select)
    
var   index =mySelect.selectedIndex;// 选中索引(选取select中option选中的第几个)
    
var   text =mySelect.options[index].text; // 选中文本
    
var   value =mySelect.options[index].value; // 选中值
 
mySelect.options[index].selected // 判断select中的某个option是否选中   true为选中   false 为未选中
```

```
if(mySelect.options[1].selected == true){
   console.log(1)
}
```


### JQ部分
### 1.判断option是否被选中
```
$("#id").is(":checked")//为false时是未被选中的，为true时是被选中

$("#id").attr('checked')==undefined//为false时是未被选中的，为true时是被选中
```
### 2.获取select选中的值
```
$("#mySelect option:selected").text()

$("#mySelect").find('option:selected').text()

$("#mySelect").val();
```
### 3.获取select选中的索引
```
$("#mySelect").get(0).selectedindex
```
### 4.添加option
```
$("#mySelect").append("<option value="+value+">"+text+"<option>");
```
### 5.删除option
```
$("#myOption").remove()
```