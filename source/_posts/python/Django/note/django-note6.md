---
title: "Django笔记06-auth认证"
date:       2019-12-19
subtitle: "Python开发的一个免费开源的Web框架"
tags:
	- Python
	- solution
	- web
	- django
---









#auth认证系统的主要组成部分
https://docs.djangoproject.com/en/1.11/ref/contrib/auth/


1,用户 

2,组

3,权限



## 自定义权限认证管理 
https://docs.djangoproject.com/en/1.11/topics/auth/customizing/#custom-permissions

### 第一步  自定义权限

    需要在定义模型中 使用 元 选项

```python
    class Task(models.Model):
    ...
    class Meta:
        permissions = (
            ("view_task", "Can see available tasks"),
            ("change_task_status", "Can change the status of tasks"),
            ("close_task", "Can remove a task by setting its status as closed"),
        )

```

### 第二步,在后台中实现 对管理员和组的管理

```
    管理员添加
        from django.contrib.auth.models import User
        创建用户
        User.objects.create_user()
        创建超级用户
        User.objects.create_superuser(用户名，电子邮件，密码，** extra_fields)
        https://docs.djangoproject.com/en/1.11/ref/contrib/auth/#django.contrib.auth.models.UserManager.create_user


        # 判断是否需要为用户分配组 
        gs = request.POST.getlist('gs',None)
        if gs:
            # 给当前用户分组
            ob.groups.set(gs)
            ob.save()


    组添加

        # 创建组
        g = Group(name=request.POST['name'])
        g.save()

        #给组添加权限
        https://docs.djangoproject.com/en/1.11/ref/contrib/auth/#group-model

        # 获取选择的所有权限
        prms  = request.POST.getlist('prms',None)
        # 判断是否需要给组添加权限
        if prms:
            # 给组分配权限
            g.permissions.set(prms)
            g.save()
        

    权限获取
        # 读取所有权限信息
        # Permission.objects.all()
        # 读取所有权限信息,并排除以Can开头的系统默认生成权限
        perms = Permission.objects.exclude(name__istartswith='Can')

```
    



### 第三步,进行验证,验证是否登录,验证是否具有权限

```
    login()  logout()
    https://docs.djangoproject.com/en/1.11/topics/auth/default/#how-to-log-a-user-in


    检查用户是否具有特定权限是相对常见的任务。出于这个原因，Django为这种情况提供了一个快捷方式： permission_required()装饰器：
    https://docs.djangoproject.com/en/1.11/topics/auth/default/#the-permission-required-decorator

    使用中间件来验证用户是否登陆

    使用 装饰器 来验证是否具有操作权限
```


### 第四步,在html模板中判断当前登录的用户是否能查看

```html
    在模板中操作权限
    https://docs.djangoproject.com/en/1.11/topics/auth/default/#permissions


     { { perms } }




     <ul>
         { % if request.user.is_superuser or 'demo.show_users' in perms % }
             <li>用户管理</li>
         { % endif % }

         { % if request.user.is_superuser or 'demo.show_types' in perms % }
             <li>分类管理</li>
         { % endif % }

         { % if request.user.is_superuser or 'demo.show_goods' in perms % }
             <li>商品管理</li>
         { % endif % }
     </ul>

```

###其他操作

```python
    # 获取当前会话的用户对象
        obj = get_user(request)


    # 获取当前用户拥有的所有权限
        pms = obj.get_all_permissions()


    # # 检查当前用户是否具有 perm 权限
        # res = obj.has_perm('demo.add_types')
```