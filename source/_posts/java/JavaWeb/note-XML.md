---
title: 'JavaWeb笔记01'
cover: "/img/lynk/7.jpg"
date:       2019-11-11
subtitle: 'XML'
tags:
	- Java
	- basis
	- JDBC
---
  
  
* content  
{:toc}  
  
  
  
  



# 今日内容
1. XML
    1. 概念
    2. 语法
    3. 解析
    
## XML:
### 概念:
Extensible Markup Language 可扩展标记语言
可扩展:标签都是自定义的.`<user><student>`

### 功能
#### 存储数据
1. 配置文件
2. 在网络中传输


### 一个故事
由于浏览器之间的竞争,导致HTML发展的十分不顺利

```
用户:唉,这怎么报错了呢?
浏览器1:我不用写引号就能应用属性.贼强
浏览器2:我不用写结束标签还行,NB吧!
浏览器3:我啥也不用写都行,就写有用的标签
浏览器1/2:卧槽,你才是真的NB
程序员:完美!O(∩_∩)O哈哈~,再也不怕写错代码了
W3C:你们太恶心了,不行,这样可不行,我才是老大,我说了算
    我来整个XML,这个就严格了,你随便写就不好使了
```
但是XML这个弟弟终究没干过他哥哥html,因为程序员们已经习惯了懒散的写法,没人爱用他

所以XML就找别人玩去了,这个人就是properties(配置文件)
```
XML:properties,你这个存配置信息存的不好,你没法区别不同用户的同类属性
    而我就不一样了,我用标签来存储,还能加上id来区分,NB吧!
properties:算你狠!
```

### XML与HTML区别
1. xml标签都是自定义的,html标签是预定义的
2. xml的语法严格,html语法松散
3. xml是存储数据的,html是展示数据的

### W3c:万维网联盟
他创建于1994年，是Web技术领域最具权威和影响力的国际中立性技术标准机构。

### 语法
#### 基本语法
- XML文档的后缀名 .xml
- XML的第一行不能空行,并且必须定义为文档声明
- XML有且仅有一个根标签
- 属性值必须使用引号(单双都可以)引起来
- 标签必须正确关闭
- XML标签区分大小写
#### 快速入门

```xml
<?xml version='1.0' ?>
<users>

    <user id='1'>
        <name>张三</name>
        <age>19</age>
        <gender>male</gender>
    </user>

    <user id='2'>
        <name>李四</name>
        <age>21</age>
        <gender>female</gender>
    </user>
    
</users>

```

所有的浏览器都可以解析XML文档,要是没报错就说明写对了

这个XML文档语法特别严格,就算你第一行空一行再写都不行了

#### 组成部分
1. 文档声明
    - 格式:`<?xml 属性列表 ?>`
    - 属性列表:
        - version:版本号(必须属性)
        - encoding:编码方式,告知解析引擎,当前文档使用的字符集(编码方式),默认字符集ISO--59(高级的开发工具能够根据你这个行写的啥来更改文件的编码方式,比如IDEA)
        - standalone:是否独立
            - 取值:
                - yes: 不依赖其他文件
                - no: 依赖其他文件
2. 指令(了解): 这个是为了结合css的,因为早期xml是要干掉html的,但是没干过
- `<?xml-stylesheet type="text/css" href="a.css"?>`
3. 标签
    1. 规则:
        - 名称可以包含字母,数字以及其他的字符
        - 名称不能以数字或者标点符号开始
        - 名称不能以字母xml(或者XML,Xml等等)开始
        - 名称不能包含空格
    可以使用任何字母,没有关键字        
4. 属性:
    - id属性值唯一
5. 文本:
    - CDATA区:这里面的内容会被原样展示
    ```xml
        <code>
            <![CDATA[
                if (a<b){}
            ]]>
        </code>
    ```
6. 约束:规定xml文档的书写规则

```
xml作为软件的配置文件
谁编写xml?
用户,软件使用者
谁解析xml?   
软件开发者
这个软件不是你理解的软件,而是半成品软件(框架)
```


- 作为框架的使用者(程序猿):
    - 能够在xml中引入约束文档
    - 能够简单的独栋约束文档(为什么是简单呢,因为智能的IDE会帮你提示)

- 分类:
    1. DTD:一种简单的约束技术
    2. SChema:一种复杂的约束技术
    
- DTD:
    - 引入dtd文档到xml文档中
        - 内部dtd:将约束规则定义在xml文档中
        - 外部dtd:将约束规则定义在外部文件中
            - 本地:<!DOCTYPE 根标签名 SYSTEM "dtd文件的位置">
            - 网络:<!DOCTYPE 根标签名 PUBLIC "dtd文件名字" "dtd文件的位置">
- Schema:
    - 引入:
        1. 填写xml文档的根元素
        2. 引入xsi前缀. `xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"`
        3. 引入xsd文件命名空间 `xsi:schemaLocation="http:www.itcast.cn/xml studnet.xsd"`
        4. 为每个xsd约束声明一个前缀,作为标识 `xmlns="http://www.itcast.cn/xml"`
        ```xml
        <students xmlns="http://www.itcast.cn/xml" 
            xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.itcast.cn/xml students.xsd">
        ```
- 解析:操作xml文档,将文件中你的数据读取到内存中
    - 操作xml文档
        1. 解析(读取):将文档中的数据读取到内存中
        2. 写入: 将内存中的数据保存到xml文档中.持久化的存储
    - 解析xml的方式:
        - DOM:将标记语言文档一次性加载进内存,在内存中形成一颗dom树
            - 优点:操作方便,可以对文档进行CRUD的所有操作
            - 缺点:占内存
        - SAX: 逐行读取,基于事件驱动的
            - 优点: 不占内存
            - 缺点: 只能读取,不能增删改
        - 一般在服务器端,我们用DOM的思想,而在移动端,我们用SAX的思想
    - xml常见的解析器:
        - JAXP: sun公司提供的解析器,支持dom和sax两种思想,(这种比较垃圾,没人用他)
        - DOM4J: 一款非常优秀的解析器
        - Jsoup: 
            - jsoup 是一款Java 的HTML解析器，可直接解析某个URL地址、HTML文本内容。它提供了一套非常省力的API，可通过DOM，CSS以及类似于jQuery的操作方法来取出和操作数据。
            - 本来是java的HTML解析器,由于他特别好用,所以用来解析xml
        - PULL: Android操作系统内置的解析器,sax方式的.
    - Jsoup使用:
        - 快速入门:
            - 步骤:
                1. 导入jar包
                2. 获取Document对象
                3. 获取对应的标签Element对象
                4. 获取数据
        - 代码:
        ```java
        // 2.获取Document对象,根据xml文档获取
                // 2.1 获取student.xml的path
                String path = JsoupDemo01.class.getClassLoader().getResource("student.xml").getPath();
                // 2.2 解析xml文档,加载文档进内存,获取dom树,-->Document
                    Document document = Jsoup.parse(new File(path),"utf-8");
                    //3. 获取元素对象Element
                Elements elements = document.getElementsByTag("name");
                System.out.println(elements.size());
                // 3.1 获取第一个name的Element对象
                Element element = elements.get(0);
                // 3.2 获取数据
                String name = element.text();
                System.out.println(name);
        ```
    - 对象的使用:
        - Jsoup: 工具类,可以解析html或xml文档,返回document对象
            - parse:解析html文档或xml文档,返回Document
            - parse(File in, String charsetName) : 解析xml或html文件
            - parse(String html) : 解析xml或html字符串
        - Document: 文档对象,代表内存中的DOM树
            - 获取Element对象
                - getElementById(String id):根据id属性值来获取唯一的Element对象
                - getElementsByTag(String tagName) : 根据标签名称获取元素对象集合
                - getElementsByAttribute(String key): 根据属性名称来获取元素对象集合
                - getElementsByAttributeValue(String key,String value): 根据属性名称来获取元素对象集合
        - Elements: 元素Element对象的集合.可以当做ArrayList<Element>来使用
        - Element: 元素对象
            - 获取子元素对象
                - getElementById(String id):根据id属性值获取唯一的element对象
                - getElementByTag(String tagName):根据标签名称获取元素对象集合
                - getElementByAttribute(String key):根据属性名称获取元素对象集合
                - getElementByAttributeValue(String key,String value):根据对应的属性名和属性值获取元素对象集合
            - 获取属性值
                - String attr(String key):根据属性名称获取属性值
            - 获取文本内容
                - String text():获取文本内容
                - String html():获取标签的所有内容(包括字标签的字符串内容)
        - Node: 节点对象
            - 是Document和Element的父类
    - 快捷查询方式:
        1. selector:选择器
            - 使用的方法:Elements select(String CSSQuery)
                - 语法:参考selector类中定义的语法
        2. XPath:XPath即为xml路径语言,它是一种用来确定XML(标准通用标记语言的子集)文档中某部分位置的语言
            - 使用Jsoup的XPath需要额外导入jar包
        
        
        
        

        
             