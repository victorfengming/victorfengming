---
title: "Django笔记04-项目搭建"
date:       2019-11-26
subtitle: "Python开发的一个免费开源的Web框架"
tags:
	- Python
	- solution
	- web
	- django
---












# 项目开发流程
- 需求开发 
《用户需求说明书》
《软件需求规格说明书》
- 技术预研
《技术预研计划》
《技术预研报告》
- 系统设计
《体系结构设计报告》
《用户界面报告》
《数据库设计报告》
《模块设计报告》
- 实现与测试
《实现与测试计划》
《编程文档》
- 系统测试
《系统测试计划》
《测试用例》
《测试报告》
- Beta 测试
《Beta 测试协议》
《Beta 测试报告》
- 客户验收 《客户验收计划》
《客户验收报告》
- 技术评审
《技术评审计划》
《技术评审报告》
《技术评审检查表》
# 项目搭建

# 后台之会员编辑


### 地址的使用
在项目中头像上传时,使用的地址
- 为什么有些地方写 `/static/uploads/`
- 有些地方写 `./static/uploads/`
- 甚至`/home/yc/py16/py16-project/web/static/uploads/`


总结来说:两种情况
- 一种是系统操作(os模块),可以使用`./static/uploads/`或者 `/home/yc/py16/py16-project/web/static/uploads/`

- 第二种是给服务器使用,浏览器访问时使用 `/static/uploads/`,因为此处`/`代表当前服务器地址(`http://127.0.0.1:8000/`)


`127.0.0.1`
`localhost`

`location.href = /index`这个使用的也是当前服务器地址

### 分页优化解决方案
自定义模板标签

### 5. URL的反向解析
如果在视图、模板中使用硬编码的链接，在urlconf发生改变时，维护是一件非常麻烦的事情

- 解决：在做链接时，通过指向urlconf的名称，动态生成链接地址
- 视图：使用django.core.urlresolvers.reverse()函数
- 模板：使用url模板标签


### js中的知识点补充
`$(this)`
是一个伪变量,在不同的作用域里表示的不同

比如这样:
```js

// 删除
    $('.removeCate').click(function(){
        // 获取当前选择的分类的id
        var cid = $(this).attr('cid')
        var a = $(this)
        // 发送ajax请求.到后台执行删除
        $.get('url',{'cid':cid},function(data){
            // 判断当前的返回值
            if(data['code'] == 0){
                // 删除成功
                // $(this).parents('tr').remove()
                //  此处的 $(this) 是谁? ajax对象 XMLHttpRequest
                a.parents('tr').remove()
            }
            alert(data['msg'])
        },'json')
        

    })
```

