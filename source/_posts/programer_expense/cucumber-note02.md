---
title: 'cucumber自动化测试'
date:       2020-07-08
tags:  
---


### cucumber自动化测试
cucumber是一款测试工具.可用于大多数主流编程语言.比如Java,JS,Ruby,C++,lua,Android,kotlin,C#/F#,PHP,Python,Go,groovy,scala等等.

其中,Java,JS,Ruby的代码托管在cucumber下.官方建议选择与生产代码相同的平台或编程语言的实现.

本文主要是Java平台下的介绍教程.使用方法非常简单,创建一个mvn工程,在pom.xml文件引入一下依赖即可.


```xml
<dependency>
    <groupId>io.cucumber</groupId>
    <artifactId>cucumber-java8</artifactId>
    <version>4.2.0</version>
    <scope>test</scope>
</dependency>
```

也可根据骨架创建cucumber项目.
### 创建一个空的cucumber项目
我们首先使用cucumber-prototype Maven插件创建一个新项目目录.打开终端,转到要创建项目的目录(比如本文是hellocucumber),运行一下命令:

```cmd
mvn archetype:generate                      \
   -DarchetypeGroupId=io.cucumber           \
   -DarchetypeArtifactId=cucumber-archetype \
   -DarchetypeVersion=2.3.1.2               \
   -DgroupId=hellocucumber                  \
   -DartifactId=hellocucumber               \
   -Dpackage=hellocucumber                  \
   -Dversion=1.0.0-SNAPSHOT                 \
   -DinteractiveMode=false
```

你应该得到如下结果:
```cmd
[INFO] Project created from Archetype in dir: hellocucumber/cucumber
[INFO] ------------------------------------------------------------------------
[INFO] BUILD SUCCESS
[INFO] ------------------------------------------------------------------------
```

切换到刚才运行命令创建的目录:
```cmd
cd hellocucumber
```

在idea中打开项目:
文件->打开...->(选择pom.xml)
选择open as project

现在,您已经安装了一个简单的cucumber项目.

### 验证cucumber安装

```cmd
mvn test
```

您应该看到如下内容:
```xml
-------------------------------------------------------
 T E S T S
-------------------------------------------------------
Running hellocucumber.RunCucumberTest
No features found at [classpath:hellocucumber]

0 Scenarios
0 Steps
0m0.004s

Tests run: 0, Failures: 0, Errors: 0, Skipped: 0, Time elapsed: 0.541 sec

Results :

Tests run: 0, Failures: 0, Errors: 0, Skipped: 0

[INFO] ------------------------------------------------------------------------
[INFO] BUILD SUCCESS
[INFO] ------------------------------------------------------------------------


cucumber的输出告诉我们它没有找到任何可以运行的东西.

### 写一个scenario(场景)
当我们使用cucumber进行行为驱动开发时,我们使用具体的例子来指定我们希望软件做什么.scenario是在生产代码之前编写的.它们以可执行规范的形式开始生命.随着生产代码的出现,场景扮演了事实文档和自动化测试的角色.

在cucumber中,一个example称为scenario. scenario定义在.feature文件中,这些文件存储在src/test/resources/hellocucumber目录(或子目录)中.

一个具体的例子就是:星期天不是星期五.

创建一个名为`src/test/resources/hellocucumber/is_it_friday_yet.feature`的文件,文件包括以下内容:

```xml
Feature: Is it Friday yet?
  Everybody wants to know when it's Friday

  Scenario: Sunday isn't Friday
    Given today is Sunday
    When I ask whether it's Friday yet
    Then I should be told "Nope"
```

这个文件的第一行以关键字'''Feature'''开始: 后面跟着一个名称.最好使用与文件名类似的名称.

第二行是对该特性的简要描述.cucumber并不执行这一行,它只是一个文档.

第4行,场景:sunday is not friday 是一个scenario, 它是说明软件应该如何工作的具体示例.
最后三行以Given开头,when和then是我们的场景的步骤.这就是cucumber将要执行的操作.

### 看一个未定义的scenario报告
现在我们有了场景,我们可以让cucumber执行它:
mvn test
cucumber告诉我们有一个undefined的场景和三个undefined的步骤.它还建议我们使用一些代码片段来define这些步骤:

```
-------------------------------------------------------
 T E S T S
-------------------------------------------------------
```java
Running hellocucumber.RunCucumberTest
Feature: Is it Friday yet?
  Everybody wants to know when it's Friday

  Scenario: Sunday isn't Friday        # hellocucumber/is_it_friday_yet.feature:4
    Given today is Sunday              # null
    When I ask whether it's Friday yet # null
    Then I should be told "Nope"       # null

1 Scenarios (1 undefined)
3 Steps (3 undefined)
0m0.040s


You can implement missing steps with the snippets below:

@Given("^today is Sunday$")
public void today_is_Sunday() {
    // Write code here that turns the phrase above into concrete actions
    throw new PendingException();
}

@When("^I ask whether it's Friday yet$")
public void i_ask_whether_it_s_Friday_yet() {
    // Write code here that turns the phrase above into concrete actions
    throw new PendingException();
}

@Then("^I should be told \"([^\"]*)\"$")
public void i_should_be_told(String arg1) {
    // Write code here that turns the phrase above into concrete actions
    throw new PendingException();
}
```

## 重构
现在我们有了工作代码，我们应该做一些重构:

我们应该将isItFriday方法从测试代码移到生产代码中。
我们可以在某个时候从步骤定义中提取helper方法，用于我们在几个地方使用的方法。
## 总结
在这个简短的教程中，您已经了解了如何安装Cucumber，如何遵循BDD流程来开发一个非常简单的方法，以及如何使用该方法来评估多个场景!

作者：Graddy
链接：https://www.jianshu.com/p/60122d38a08a
来源：简书
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


---

# 自动化测试之cucumber(一)
## 简介
cucumber是BDD(behavior-driven development,行为驱动开发)的一个自动化测试的副产品.它使用自然语言来描述测试,使得非程序员可以理解他们.

Gherkin是这种自然语言测试的简单语法,而cucumber是可以执行它们的工具.关于BDD有兴趣自行了解.附cucumber[官网链接](https://links.jianshu.com/go?to=https%3A%2F%2Fcucumber.io%2F),里面也有关于BDD的信息.

cucumber本质上是使用根据正则表达式匹配自然语言,然后依次执行对应的方法,以达到测试的目的.

本文基本上只是官网的搬运工,摘要了部分信息,最好还是看官网文档.

## Gherkin

gherkin是自然语言测试的简单语法.
一个完整的测试是由多个step组成的,step即最小单元,如何复用step是非常关键的问题.多个step组成一个scenario,即一个完整的测试case.多个scenario组成一个Feature,即一组相关的测试case.

## 关键字
- Feature
- Example(or Scenario)
- Given, When, Then, And, But(steps)
- Background
- Scenario Outline(or Scenario Template)
- Examples(or Scenarios)

## 一个简单的例子
```javascript
Feature: Is it friday yet?
  this is a descriptions
  Everybody want to know when it's Friday

  Scenario: Sunday isn't Friday
    Given today is Sunday
    When I ask whether it's Friday yet
    Then I should be told "Nope"

  Scenario: Friday is Friday
    Given today is Friday
    When I ask whether it's Friday yet
    Then I should be told "TGIF"
```

## Feature
Feature是所有测试的开头.后面跟一段描述性的文字,表明这个测试文件是干什么的.

## description
description是一段扩展性的文字描述,可以跟在Feature,Example,Background,Scenario,Scenario Outline 下面.

## Example和Scenario
Example和Scenario是一对儿同义词,是一个具体的测试case,包含了多个step.一般情况下,都是由Given(给定一个初始条件),When(发生了什么),Then(结果是什么)组成的.

## Steps
step是cucumber的最下单元,每个step是由Given,When,Then,And,或者But开头的.如果关键词后面的内容是完全一样的话,那么cucumber会认为这两句话是重复的,哪怕前面的关键词不一样,如


---

# Gherkin是什么
Gherkin,cucumber解释器可以理解的语言.这是一个商业可读性,领域特定语言,描述软件的行为而不需要关心这个行为的如何实现的.

Gherkin有两个目的 - 文档和自动化测试.第三个额外特色:当它被标记为红色叉叉时,让你知道接下来的代码如何写.

Gherkin的语法定义为Treetop语法(Treetop--基于Ruby的PEG解析器生成器)所以可以被cucumber解释执行(cucumber是一个解释程序,就像ruby命令执行解释.rb文件里的Ruby代码一样,cucumber用来执行解释.Feature文件里的Gehrkin代码.)该语法适用在不同语言中,让您的团队可以使用自己的语言中的关键字.

个人理解:
Gherkin是一种语法,使用Given,when,then等关键来描述一个User Story.形成的代码不论是User,BA都能读懂的形式,同时也非常便于使用specflow转化成BDD所需要的文件.

### 通用约定
-> Gherkin的单个文件包含对一个功能点的描述
-> 源文件使用.feature作为扩展名

### Gherkin语法
像Python和YAML,Gherkin是一种面向行的语言.使用缩进来定义结构.行结尾终止语句(例如,步骤).空格或制表符可用于缩进(但空格更方便些),每一行以关键字开始.

注释允许出现在文件的任何一行,但是要以#开始,仅支持单行注释.

当你开始运行一个行为时,feature关键字的后面部分,也就是详细步骤,这是一段Ruby风格的代码片段,会被解析器分析出所有的功能,情景和步骤.

Gherkin文件格式如下:
成人带婴儿旅客,联程,一件行李,两段均进行ET改期.feature