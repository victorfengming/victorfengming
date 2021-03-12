---
title: "Django笔记05-后台展示"
date:       2019-11-28
subtitle: "一个广受欢迎的服务器端框架"
tags:
	- Python
	- solution
	- web
	- django
---









# 后台商品数据展示

# 中间件
### 引言
后台的权限,实际上只能是管理员能访问,而我们现在谁都能访问

这里我们需要做一个验证

这次我们先做一个模拟的,(假的),等前台都写完了,会有权限管理来用

这个不需要用过多的时间

如果要进行身份验证,我们做各种操作都需要验证

因此我们框架中有一个中间件

### 中间件概念
中间件是一个轻量级、底层的插件系统，可以介入Django的请求和响应处理过程，修改Django的输入或输出
激活：添加到Django配置文件中的MIDDLEWARE_CLASSES元组中
使用中间件，可以干扰整个处理过程，每次请求中都会执行中间件的这个方法

### 比如这样
```python
from django.http import HttpResponse
import re

class AdminLoginMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):

        # 用户的请求路径# /myadmin/cate/index/
        path = request.path
        # 定义允许访问的路径
        arr = ['/myadmin/login/','/myadmin/dologin/','/myadmin/verifycode/']
        # 检测用户是否访问后台,并且不是进入登录页面
        if re.match('/myadmin/',path) and path not in arr:
            # 检测是否已经登录
            AdminUser = request.session.get('AdminUser',None)
            if not AdminUser:
                # 没有登录
                return HttpResponse('<script>alert("请先登录");location.href="/myadmin/login/"</script>')


        response = self.get_response(request)
        return response
```

### 验证码那点事儿

静态资源如果重复访问,不会产生

所以验证码的刷新要在this.src后面加上?1

像这样:
```html
<img src="大括号开始 百分号 url 'myadmin_verifycode' 百分号 大括号结束" alt="" style="position:absolute; right: 2px; top: 5px" onclick="this.src = this.src+'?1'">
```
这样会越加越多,升级版本(用随机数字):
```html
<img src="大括号开始 百分号 url 'myadmin_vcode' 百分号大括号结束" onclick="this.src='大括号开始百分号 url 'myadmin_vcode' 百分号 大括号结束'+'?'+Math.random()" style="position: absolute;top:-5px;right: 2px;">
```

### 前台页面的基本搭建

后台是增删改查的流程

前台多数时候是查询
