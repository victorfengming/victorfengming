---
title: "Django笔记03-模板引擎"
date:       2019-11-25
subtitle: "重量级选手中最有代表性的一位"
tags:
	- Python
	- solution
	- web
	- django
---



* content
{:toc}






# CSRF攻击
CSRF（Cross-site request forgery）跨站请求伪造，也被称为“One Click Attack”或者Session Riding，通常缩写为CSRF或者XSRF，是一种对网站的恶意利用。尽管听起来像跨站脚本XSS，但它与XSS非常不同，XSS利用站点内的信任用户，而CSRF则通过伪装来自受信任用户的请求来利用受信任的网站。与XSS攻击相比，CSRF攻击往往不大流行（因此对其进行防范的资源也相当稀少）和难以防范，所以被认为比XSS更具危险性

CSRF中间件和模板标签为防止跨站点请求伪造提供了易用的保护。

当恶意网站包含链接，表单按钮或某些旨在在您的网站上执行某些操作的JavaScript时，会使用在浏览器中访问恶意网站的登录用户的凭据进行此类攻击。

还介绍了一种相关攻击类型，即“登录CSRF”，攻击网站欺骗用户的浏览器，以便使用其他人的凭证登录到网站。

# Template模板
### 模板概念
作为Web 框架，Django 需要一种很便利的方法以动态地生成HTML。最常见的做法是使用模板。

模板包含所需HTML 输出的静态部分，以及一些特殊的语法，描述如何将动态内容插入。


### 模板语法

#### 1.变量
- 变量输出语法`{{ var }}`

- 当模版引擎遇到一个变量，将计算这个变量，然后将结果输出
- 变量名必须由字母、数字、下划线（不能以下划线开头）和点组成
- 当模版引擎遇到点(".")，会按照下列顺序查询：
    - 字典查询，例如：foo["bar"]
    - 属性或方法查询，例如：foo.bar
    - 数字索引查询，例如：foo[bar]
- 如果变量不存在， 模版系统将插入'' (空字符串)
- 在模板中调用方法时不能传递参数

#### 2.标签
- 语法`{ %  tag  % }`
- 作用
    - 在输出中创建文本
    - 控制循环或逻辑
    - 加载外部信息到模板中
##### for标签
```html
{ %  for ... in ...  % }
    循环逻辑
{ %  endfor  % }
```
##### if标签
```html
{ %  if ...  % }
    逻辑1
{ %  elif ...  % }
    逻辑2
{ %  else  % }
    逻辑3
{ %  endif  % }
```
##### comment标签
```html
{ %  comment  % }
    多行注释
{ %  endcomment  % }
```
##### include：加载模板并以标签内的参数渲染
```html
{ %  include "base/index.html"  % }
```
##### url：反向解析
```html
{ %  url 'name' p1 p2  % }
```
##### csrf_token：这个标签用于跨站请求伪造保护
```html
{ %  csrf_token  % }
```

### Django框架自带的后台
1. 在浏览器访问 admin
`http://127.0.0.1:8000/admin/`
2. 需要登录,因此要创建一个超级用户
在命令行执行下一个命令进行创建
`python3 manage.py createsuperuser`

3. 重新启动服务后 ,使用创建的用户进行后台的登录
4. 配置settings.py文件,配置语言和时区
```python
LANGUAGE_CODE = 'zh-Hans'
TIME_ZONE = 'Asia/Shanghai'
USE_I18N = True
USE_L10N = True
USE_TZ = False
```
# 自定义过滤/器
1. 在应用中创建一个templatetags文件夹
2. 在templatetags 包中定义一个模块文件diytags.py


```python

from django import template

register = template.Library()

''' 自定义过滤器'''
@register.filter
def yc_upper(val):
    return val.upper()


''' 自定义标签'''
from django.utils.html import format_html
@register.simple_tag
def jia(a,b):
    res = int(a) + int(b)
    return res

```
3. 在需要使用的模板中, 导入自定义的模块

# 验证码
这里调用的PIL库实现的

```python
from django.http import HttpResponse
def verifycode(request):
    #引入绘图模块
    from PIL import Image, ImageDraw, ImageFont
    #引入随机函数模块
    import random
    #定义变量，用于画面的背景色、宽、高
    bgcolor = (random.randrange(20, 100), random.randrange(
        20, 100), 255)
    width = 100
    height = 25
    #创建画面对象
    im = Image.new('RGB', (width, height), bgcolor)
    #创建画笔对象
    draw = ImageDraw.Draw(im)
    #调用画笔的point()函数绘制噪点
    for i in range(0, 100):
        xy = (random.randrange(0, width), random.randrange(0, height))
        fill = (random.randrange(0, 255), 255, random.randrange(0, 255))
        draw.point(xy, fill=fill)
    #定义验证码的备选值
    str1 = 'ABCD123EFGHIJK456LMNOPQRS789TUVWXYZ0'
    #随机选取4个值作为验证码
    rand_str = ''
    for i in range(0, 4):
        rand_str += str1[random.randrange(0, len(str1))]
    #构造字体对象
    font = ImageFont.truetype('FreeMono.ttf', 23)
    #构造字体颜色
    fontcolor = (255, random.randrange(0, 255), random.randrange(0, 255))
    #绘制4个字
    draw.text((5, 2), rand_str[0], font=font, fill=fontcolor)
    draw.text((25, 2), rand_str[1], font=font, fill=fontcolor)
    draw.text((50, 2), rand_str[2], font=font, fill=fontcolor)
    draw.text((75, 2), rand_str[3], font=font, fill=fontcolor)
    #释放画笔
    del draw
    #存入session，用于做进一步验证
    request.session['verifycode'] = rand_str
    #内存文件操作
    import cStringIO
    buf = cStringIO.StringIO()
    #将图片保存在内存中，文件类型为png
    im.save(buf, 'png')
    #将内存中的图片数据返回给客户端，MIME类型为图片png
    return HttpResponse(buf.getvalue(), 'image/png')

```
# ajax实现城市多级联动

#### 视图函数


```python
def citys(request):
    # 从数据库中获取所有的一级城市信息
    data = Citys.objects.filter(upid=0)
    # 分配数据
    content = {'data':data}
    return render(request,'citys.html',content)

```

#### urls路由


```python
urlpatterns = [

    url(r'^$', views.index,name="index"),
    url(r'^citys$', views.citys,name="citys"),
    # 获取城市信息的地址
    url(r'^get/city$', views.get_city,name="get_city"),
]

```


#### 前台界面

```html

<斯科瑞破特 type="text/java斯科瑞破特" src="/static/jquery-1.8.3.min.js"></斯科瑞破特>
<斯科瑞破特>
    // 第一步 获取选框 绑定称职时间
    // 这个绑定事件绑定不了动态加载的元素
     大括号 警号 刀乐符 ('斯莱克特').称职(方可神 () 大括号开始 警号 大括号回
    // 所以我们不用这个了,我们用一个或者的方法
    //
    刀乐符 ('斯莱克特').live('称职',方可神 () {
        // 获取当前选中的城市id
        哇 cid = 刀乐符(this).哇();
        // 发送ajax
        大括号开始 警号 刀乐符 .get('/get/city/',);警号 大括号回

        刀乐符.get('大括号开始百分号 url "get_city" 百分号大括号结束',大括号开始'cid':cid大括号结束,方可神 (data) 大括号开始
            console.log(data);
            // 动态创建下拉选框
            // 这叫创建标签
            哇 sel = 刀乐符('<斯莱克特></斯莱克特>');
            // 定义选项
            var ops = '<option>--请选择--</option>';
            for (var i = 0; i < data.length; i++) 大括号开始
                ops += '<option value="'+data[i].id+'">'+data[i].name+'</option>';
            大括号结束

            // 吧定义的选项设置到下拉框中
            sel.html(ops);
            // 吧创建的html添加到页面中
            刀乐符('body').append(sel);
        大括号结束,'json')
    大括号结束)
</斯科瑞破特>
``` 