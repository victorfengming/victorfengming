---
title: 'Mustache简介'
cover: "/img/lynk/44.jpg"
subtitle: '前端框架最常用的胡须语法'
date:       2020-10-19
tags:
	- web
	- front
---
  
  
Mustache 是一款经典的前端模板引擎，在前后端分离的技术架构下面，前端模板引擎是一种可以被考虑的技术选型，随着重型框架（AngularJS、ReactJS、Vue）的流行，前端的模板技术已经成为了某种形式上的标配，Mustache 的价值在于其稳定和经典： 
 
主页：https://github.com/janl/mustache.js/  
文档：https://mustache.github.io/mustache.5.html  
  
Mustache 在使用的时候，会在页面上出现 { { person} }  这样的标签，载入的时候回显示出来，然后立即被替换掉，这个对于页面的呈现是不够友好的，这是我在使用的过程中遇到的一个痛点。  
  
Mustache 功能非常经典，这里就能全部罗列出来：  
  
### 变量  
{ { person} }   
  
### 带有HTML的变量  
{ { { person} } }   
  
### 循环  
{ { #persons} }   
......  
{ { /persons} }   
  
数组循环的时候可以用.作为下标  
{  "musketeers": ["Athos", "Aramis", "Porthos", "D'Artagnan"] }   
{ { #musketeers} }   
{ { .} }   
{ { /musketeers} }   
  
### 对象  
正常使用：  
{  "name": {  "first": "Michael", "last": "Jackson" } , "age": "RIP" }   
{ { name.first} }  { { name.last} }   
{ { age} }   
  
循环使用：  
{  "stooges": [ {  "name": "Moe" } , {  "name": "Larry" } , {  "name": "Curly" }  ] }   
{ { #stooges} }   
{ { name} }   
{ { /stooges} }   
  
### if else  
{ { #person} }   
......  
{ { /person} }   
{ { ^person} }   
......  
{ { /person} }   
  
### 布尔判断  
和前面循环的语法是一样的，取决于变量是否是一个数组  
{ { #person} }   
......  
{ { /person} }   
  
### 数组的布尔判断  
当一个数组没有任何值的时候，可能会希望不做任何的显示，所以需要这个判断  
{ { #persons.length} }   
......  
{ { /persons.length} }   
  
### Lambdas  
遇到和前面的循环和布尔表达式一样，取决于参数的类型  
{ { #person} }   
{ { name} }  is awesome.  
{ { /person} }   
  
{  "name": "Willy", "person": function() {  return function(text, render) {  return "<b>" + render(text) + "</b>" }  }  }   
  
输出  
<b>Willy is awesome.</b>  
  
### 注释  
这玩意儿有啥用呢？  
{ { ! ignore me } }   
  
### Trick  
在做<tr></tr>的循环输出的时候，需要使用类似这样的形式（感觉这就是BUG啊，或者是HTML标准的问题？）：  
``  
<tr> <td>{ { name} } </td> <td>{ { age} } </td> </tr>  
  
### 两个核心方法  
Mustache.parse(template);  
Mustache.render(template, obj);  
  
因为动态载入到 HTML 上的事件或者元素会丢失，所以我封装了一个对模板的缓存：  
  
```javascript  
$(templateKey).each(function(i){   
    templateExist = false;  
    $(templateArray).each(function(index){   
        if (templateArray[index][0] == templateKey+i)  
        {   
            templateExist = true;  
            template = templateArray[index][1];  
        }   
     } )  
          
    if (templateExist != true)  
    {   
        template = $(this).html();  
        templateArray.push([templateKey+i, template]);  
    }   
  
    Mustache.parse(template);  
    $(this).html(Mustache.render(template, item.data)).show();  
    if (callbackFunction)  
    {   
        callbackFunction(item.data);  
    } ;  
} )  
```  
顺便简单学习了一下 Handlebars，这款也非常的知名，并且是基于 Mustache 的模板引擎：  
Handlebars：http://handlebarsjs.com/  
  
如果你希望像传统模板引擎一样可以有函数和参数处理等等的功能，那么 Mustache 就不是好的选择，但是再复杂了往上走的话，就不如选用 `Vue` 了  
  
    
