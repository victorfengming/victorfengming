---
title: 'cucumber介绍'
cover: "/img/lynk/58.jpg"
date:       2020-07-10
tags:  
---


### cucumber介绍
cucumber 是一个支持BDD(behavior Driven Development),即行为驱动开发的自动化测试框架.在进行单元测试或者集成测试之前,事先将测试的步骤和验证信息用通用的语言(英语)定义好,使得测试的步骤、单元测试和集成测试每一步执行的目的能被非开发人员读懂,并且写单元测设和集成测试的人员可以根据事先写好的框架进行代码的编写,达到行为驱动开发的目的.

### cucumber框架的搭建
1. 将cucumber插件导入eclipse中,此处同其他插件导入方法相同,不作说明.
2. 新建Java工程,将cucumber所需要的jar包导入Java工程中(最好新建一个文件夹,将jar包放到该文件夹下).
3. 通过Build Path添加刚导入的JARs
4. 新建用来定义步骤的feature格式的文件,新建的feature格式文件会自动填写模板文件,具体使用方法后续说明.同上,最好将其放在特定的文件夹 里,本例Feature文件夹.
5. 将被测试的包导入Java工程中,本例测试一个简单的Calculator类.
6. 新建一个包,包名必须为test.java或main.java 否则后续创建cucumber定义步骤时会出错.
7. 在test.java包中新建一个Step-Definition class.

### cucumber框架相关文件及其内容的说明
1. .feature文件
定义了测试的步骤,包括以下几个关键字
Feature: 一个.feature文件有且仅有一个Feature关键字.描述要测试的对象,一般为测试标题.

Scenario: 一个.feature文件可以有0个或多个Scenario关键字.测试对象的场景,如测试Add()方法,可以有两个整数相加的和两个负数相加等多种场景.

Given: 一个.feature文件有且仅有一个Given关键字.相当于测试用例中的预置条件.如想要表达多个预置条件,可以通过And关键字添加.

When: 一个.feature文件有且仅有一个When关键字.具体的操作步骤,类似于测试用例的中的预期结果.如想要表达多个预期结果,可以通过And关键字添加.

Then: 一个.feature文件有且仅有一个Then关键字.相当于测试用例的中的预期结果.如想要表达多个预期结果,可以通过and关键字添加.

And: 一个.feature文件可以有0个或多个And关键字.And元素可以补充额外的预置条件或操作步骤.

But: 一个.feature文件可以有0个或多个But关键字.But和And一样,可以同Given、When、Then连用,用于添加否定类型的描述,一般只适用于负面条件.比如:

THEN login should be successful.

BUT home page should not be missing

Scenario Outline: 一个.feature文件可以有0个或多个Scenario Outline 关键字.用于场景中有多数组数值时,必须配合Example一起使用,成对出现.
Example: 和Scenario Outline成对出现,其下有多组测试数值的列表 

2. Step-definition文件
cucumber的Step-definition和其他的Java格式文件基本相同,但是在创建时可以根据需要选择性勾选并自动添加Give,When,Then,And,But注释.

完成后会自动生成一个Java模板文件,包括了之前勾选的注释,本例勾选了Given,When,Then和And.注释的格式为:

@关键字("^*********$")
@Given("^you are in Given annotation$")

关键字后括号里的内容必须和先前定义的.feature文件的关键字的内容一一对应,识别大小写并且包括空格数目等都要一样,以^开头,$结尾.
注释之后为具体实现的方法,在方法中添加符合关键字后描述的操作代码.

3. 测试执行文件
cucumber 的测试执行文件一般为一个空的Junit Test Case, 即不需要Test注释,更不需要Before和After等注释.当必须添加RunWith注释和CucumberOption注释.
RunWith注释每一个Cucumber框架的测试文件都是相同的,为RunWith(Cucumber.class). CucumberOption注释的内容是根据实际情况需要手动更改的.

CucumberOption注释选项一般有features,glue,monochrome和dryrun等.其中.feature和glue是必写项,monochrome和dryrun选填项.
feature定义了.feature文件的相对路径,格式为features=".feature文件在改工程的文件夹/.feature文件的名字".

eg.features="Feature/calculatorAdd.feature"

glue定义了Step-difinition的包名,格式为glue="完整的包名".
eg.test.javacucumberDefinition.

monochrome选项有两个值,分别为true和false,默认为false,格式为monochrome=boolean.用来控制测试结果的可读性,当monochrome=true时,测试结果可读性更好.monochrome=true时,测试结果可读性比较差.

dryrun选项暂时不了解

cucumber框架的使用

通过以上介绍,cucumber框架基本搭建完成,对cucumber各文件的作用也有所了解,接下来就是通过对框架的修改来实现一个简单的BDD模式的单元测试.
测试Calculator类中的Add()成员方法

1. 新建testAdd.feature文件,并修改其内容
```javascript
@tag
Feature: Test add function of calculator
@tag1
Scenario: Add two numbers
Given init the object of calculator
When clear the result to zero
And and num1 and num2
Then check the actual result
```

2. 新建stepDefinition.java文件,使用Given,when,Then,和And关键字,修改注释内容并根据注释内容填写方法中的代码.
```
package test.java.cucumberDefinition

import cucumber.api.java.en.Given;
import cucumber.api.java.en.When;
import cucumber.api.java.en.Then;


import static org.junit.Assert.assertEquals;

import com.calculator.Calculator;

import cucumber.api.java.en.And;

public class stepDefinition{
    Calculator cal;
    int result;
    @Given("init the object of calculator$")
    public void given() throws Throwable{
        cal = new Calculator();
    }   
}

@When("^clear the result to zero$")
public void when() throws Throwable{
    cal.clear();      
}

@Then("^add num1 and num2$")
public void then() throws Throwable{
    cal.add(2);
    cal.add(3);
}

@And("^check the actual result$")
public void and() throws Throwable {
int expected = 5;
result = cal.getResult();
assertEquals(expected,result);
}

}


```

3. 新建一个Junit Test Case，并将其内容清空，最后添加RunWith和CucumberOptions注释。


package com.calculator.test;

import static org.junit.Assert.*;

import org.junit.Test;
import org.junit.runner.RunWith;

import cucumber.api.CucumberOptions;
import cucumber.api.junit.Cucumber;

@RunWith(Cucumber.class)
@CucumberOptions(features="Feature/calculatorAdd.feature"

,glue="test.java.cucumberDefinition",monochrome=true)
public class testAdd {

}
4. 右键testAdd.java，执行run as junit case进行测试。



## cucumber简单介绍
### 简介
cucumber是一个能够理解用普通语言描述的测试用例的行为驱动开发(BDD)的自动化测试工具,
其本质上是使用根据正则表达式匹配自然语言,然后依次执行对应的方法,以达到测试的目的.

优点:
- 支持不同的语言,例如Java, .net, Ruby
- 它充当业务与技术间的桥梁的角色.可以通过在纯英文文本中创建一个测试用例来实现这一点
- 他允许在不知道任何代码的情况下编写测试脚本,它允许非程序员参与.
- 由于简单的测设脚本架构,cucumber提供了代码可重用性

### 组成
组成:Feature,Step_definitions,Cucumber command

Feature:功能
- 基于Gerkins.支持多种语言,
- 以.feature命名
- 每个features包含多个scenarios,每个scenarios包含多个step

Step_definitions
- 根据feature文件中定义的step编写对应的测试代码.

cucumber command
- 运行: *.feature 文件.cucumber会分析feature文件中定义的step,然后去step-definition找到相匹配的step,执行step中的代码.
- 对于cucumber而言,除了顶层的features文件夹是强制性的之外,其它目录结构都不是强制性的,cucumber将对features文件夹下的所有内容进行扁平化(flatten)处理和首字母排序.具体来说,cucumber在运行时,首先将递归的执行features文件夹下的所有Ruby文件(其中则包括Step文件),然后通过相同的方式执行Feature文件.但是,如果features文件夹下存在support子文件夹,并且support下有名为env.rb的文件,cucumber将首先执行该文件,然后执行support下的其他文件,在递归执行features下的其他文件


 在cucumber项目中,当我们执行cucumber命令时,会首先执行features/support目录下的几个支持文件:env,hooks,world和transforms.cucumber的这些系统文件的执行顺序如下图所示:
 
 1. env.rb:通常用于准备环境变量;
 2. transform.rb: 用于转换feature描述中需要正则匹配的字符串,通过调用cucumber::RbRupport::RbDsl的Transform方法,完成字符串到自定义类型的转换;
 3. hooks.rb: 是一个钩子,其中定义了Before,After 与 at_exit方法,通过提供block执行场景前,后以及退出执行后的相关逻辑
 
 4. world.rb: World可以看做是cucumber在每个场景之前所要创建的对象的实例,它使得每个Step Definition可以调用该实例的方法.World在cucumber中被定义为方法,接受可变参数mudules,以及一个proc
 
 Gerkin(cucumber的语言输出)
 Gherkin是自然语言测试的简单语法.一个完整的测试是由多个step组成的,step即最小单元,如何复用step是非常关键的问题.多个step组成一个SCenario,即一个完整的测试case.多个Scenario组成一个Feature,即一组相关的测试case.
 
 关键字
 - Feature
 - Example(or Scenario)
 - Given, When, Then, And, But













