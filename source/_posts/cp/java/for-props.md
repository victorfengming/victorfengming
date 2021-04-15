---
title: "Java遍历对象所有属性"
cover: "/img/lynk/17.jpg"
date:       2021-04-14
tags:
	- base
	- java
---



## 写在前面

> 要获取对象的所有属性可以使用`getDeclaredFields()`
> 
> 方法会返回一个`Field`数组
> 
遍历这个数组几个遍历所有属性
> 
> 注意: 使用这个方法会抛出4个异常
> 
> 然后,根据属性的类型选择执行对应的内容
> 


## 代码演示

```java
public static void eachProperties(Object model) throws NoSuchMethodException, IllegalAccessException, IllegalArgumentException, InvocationTargetException{
    Field[] field = model.getClass().getDeclaredFields(); //获取实体类的所有属性，返回Field数组
    for(int j=0 ; j<field.length ; j++){ //遍历所有属性
        String name = field[j].getName(); //获取属性的名字
 
        System.out.println("attribute name:"+name);
        name = name.substring(0,1).toUpperCase()+name.substring(1); //将属性的首字符大写，方便构造get，set方法
        String type = field[j].getGenericType().toString(); //获取属性的类型
        if(type.equals("class java.lang.String")){ //如果type是类类型，则前面包含"class "，后面跟类名
          ...
        }
        if(type.equals("class java.lang.Integer")){
          ...
        }
        if(type.equals("class java.lang.Short")){
          ...
        }
        if(type.equals("class java.lang.Double")){
          ...
        }
        if(type.equals("class java.lang.Boolean")){
          ...
        }
        if(type.equals("class java.util.Date")){
          ...
        }
    }
}
```

>具体执行的内容就是重点了
> 

我们知道模型的属性都会有对应的`getter`和`setter`方法

只需要得到对应的`getter`和`setter`方法即可获取和设置属性

> 
> 这里就需要用到getMethod方法
> 

## 获得getter方法

>方法有分带参数和不带参数,我们知道getter方法是不带参数的
> 

获得getter方法如下


```java
Method m = model.getClass().getMethod("get"+name);
```


## 获得setter方法

>如果是带参数的setter方法,就应该把参数的类型做封装成一个Class<?>泛型数组传入getMethod方法的第二个参数
> 
> 
例如参数是String类型的setter方法如下

```java
Method m = model.getClass().getMethod("set"+name, new Class[] {String.class});
```

## 执行getter方法

```java
String value = (String) m.invoke(model);
```


## 执行setter方法

```java
m.invoke(model,new Object[] {new String("new value")});
```


## 链接
参考: from: http://zhenhappy.github.io/2015/10/26/Java/Java-Each-Properties/

转载于:https://www.cnblogs.com/GarfieldEr007/p/7056817.html

原文: https://blog.csdn.net/weixin_30588675/article/details/97631029



## java 获取类和父类的属性和方法

### 问题
在日常开发中，经常需要获取当前类和父类的所有属性，没办法只能查API了。


### getDeclaredFields VS getFields
查阅API得知，class.getDeclaredFields()能获取所有属性（public、protected、default、private），但不包括父类属性，相对的class.getFields() 获取类的属性（public），包括父类；

显然以上二者都不能满足需求，这么常见的需求，肯定有开源包实现了，功夫不负有心人果然查到了。apache commons包下的FieldUtils.getAllFields()可以获取类和父类的所有(public、protected、default、private)属性。

为了加深理解，看一下源码


```java
 public static Field[] getAllFields(final Class<?> cls) {
        final List<Field> allFieldsList = getAllFieldsList(cls);
        return allFieldsList.toArray(new Field[allFieldsList.size()]);
    }
```

```java
 public static List<Field> getAllFieldsList(final Class<?> cls) {
        Validate.isTrue(cls != null, "The class must not be null");
        final List<Field> allFields = new ArrayList<Field>();
        Class<?> currentClass = cls;
        while (currentClass != null) {
            final Field[] declaredFields = currentClass.getDeclaredFields();
            for (final Field field : declaredFields) {
                allFields.add(field);
            }
            currentClass = currentClass.getSuperclass();
        }
        return allFields;
    }
```


通过class.getDeclaredFields()获取所有的属性，然后再获取类的父类，再获取所有属性，直到父类为null截止；

### 获取类和父类的方法

类似的，API中也有getDeclaredMethods()和getMethods()

class.getDeclaredMethods() 获取类的所有方法（public、protected、default、private），但不包括继承的方法；

class.getMethods() 获取当前类和父类的public方法。

apache commons包提供了MethodUtils.getMethodsWithAnnotation(class,annotation),获取类及父类的注解为annotation的public方法；


### 总结
- 获取类的所有属性（public、protected、default、private），包括父类的属性，则使用FieldUtils.getAllFields()
- 获取类标注某个注解的方法（包括类及父类），使用MethodUtils.getMethodsWithAnnotation(class,annotation)

原文: https://blog.csdn.net/wangjun5159/article/details/79289244/

