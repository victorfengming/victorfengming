---
title: "Java笔记09-【继承、super、this、抽象类】"
date:       2019-10-21
tags:
	- Java
	
---

* content
{:toc}




# 目录
### 今日内容 
- 三大特性- 继承 
- 方法重写
- super关键字
- this关键字
- 抽象类

### 继承
  <li>基本概念
    <ol>
      <li>当多个类之间有相同的特征和行为时，可以将相同的内容提取出来组成一个公共类，让多个公共类吸收公共类中已有特征和行为而在多个类的内部编写自己独有特征和行为的方式，叫做继承</li>
      <li>使用继承可以提高代码的复用性和扩展性以及可维护性</li>
      <li>在Java语言中使用extends(
 扩展)关键字来表达继承关系
        <div class="language-java highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="err">如：</span>
<span class="kd">public</span> <span class="kd">class</span> <span class="nc">Student</span> <span class="kd">extends</span> <span class="nc">Person</span><span class="o">{}</span>
<span class="err">表示</span><span class="n">Student</span><span class="err">类继承自</span><span class="n">Person</span><span class="err">类</span>
<span class="err">其中</span><span class="n">Person</span><span class="err">类叫做基类、父类、超类</span>
<span class="err">其中</span><span class="n">Student</span><span class="err">类叫做派生类、子类、孩子类</span>
</code></pre></div>        </div>
      </li>
    </ol>
  </li>
  <li>注意事项
    <ol>
      <li>子类可以继承父类的成员变量和成员方法，其中私有成员变量可以继承但不可以直接使用。子类不可以继承父类的构造方法和私有方法</li>
      <li>无论使用何种方式构造子类对象时，都会自动调用父类中的无参构造方法来初始化从父类继承下来的成员变量，相当于在子类构造方法的第一行增加代码:super()的效果
        <div class="language-java highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="err">以后写代码一律带着</span><span class="kd">super</span><span class="o">()</span><span class="err">格式写</span>
<span class="err">如：</span>
<span class="kd">public</span> <span class="nf">Worker</span><span class="o">(){</span>
 <span class="kd">super</span><span class="o">();</span>
 <span class="o">}</span>
<span class="kd">public</span> <span class="nf">Worker</span><span class="o">(</span><span class="nc">String</span> <span class="n">name</span><span class="o">,</span><span class="kt">int</span> <span class="n">age</span><span class="o">,</span><span class="kt">int</span> <span class="n">salary</span><span class="o">){</span>
 <span class="kd">super</span><span class="o">(</span><span class="n">name</span><span class="o">,</span><span class="n">age</span><span class="o">);</span>
 <span class="n">setSalary</span><span class="o">(</span><span class="n">salary</span><span class="o">);</span>
 <span class="o">}</span>  
</code></pre></div>        </div>
      </li>
      <li>使用继承必须满足 子类is a父类 的逻辑关系，也就是不能滥用继承</li>
      <li>Java语言中只支持单继承，不支持多继承，也就是一个子类只能有一个父类，但一个父类可以有多个子类</li>
    </ol>
  </li>
  
  

### 方法重写

  <li>方法重写
    <ol>
      <li>基本概念：当父类中继承下来的方法不满足子类的需求时，就需要在子类中重新写一个与父类中一样的方法来覆盖从父类中继承的版本，这种方式就叫做重写</li>
      <li>重写的原则：
        <ol>
          <li>方法名相同，参数列表相同，返回值类型相同，从jdk1.5开始允许返回子类类型</li>
          <li>要求方法访问权限不能变小，可以相同或者变大</li>
          <li>不能抛出更大的异常</li>
        </ol>
      </li>
      <li>语法格式
        <div class="language-java highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="nd">@Override</span>
<span class="kd">public</span> <span class="kt">void</span> <span class="nf">show</span><span class="o">(){</span>
 <span class="kd">super</span><span class="o">.</span><span class="na">show</span><span class="o">();</span>
 <span class="nc">System</span><span class="o">.</span><span class="na">out</span><span class="o">.</span><span class="na">println</span><span class="o">(</span><span class="s">"我一个月能挣"</span><span class="o">+</span><span class="n">getSalary</span><span class="o">()+</span><span class="s">"呢"</span><span class="o">);</span>
<span class="o">}</span>
</code></pre></div>        </div>
      </li>
    </ol>
  </li>

### 方法重载
<li>方法重载(Overload 会用即可)
    <ol>
      <li>基本概念：在Java语言中若方法名称相同但参数列表不同，这样的方法构成方法重载</li>
      <li>体现形式：方法重载的主要形式有：参数的个数不同、参数的类型不同、参数的顺序不同，与形参变量名和返回值类型无关，但建议返回值类型最好相同</li>
      <li>实际意义：对于调用者来说只需要记住一个方法名就可以调用各种不同的版本实现不同的效果</li>
    </ol>
  </li>
  
  
### this关键字
  <li>基本概念
    <ol>
      <li>在构造方法中，this关键字代表当前正在构造的对象</li>
      <li>在成员方法中，this关键字代表当前正在调用的对象</li>
    </ol>
  </li>
  <li>使用方式
    <ol>
      <li>当形参变量和成员变量同名时，在构造方法或成员方法中通常优先使用形参变量，若希望使用成员变量就需要在变量名的前面加上this.进行说明(重中之重)</li>
      <li>在构造方法的第一行使用this(实参)的方式可以调用本类中的其他构造方法(了解)</li>
    </ol>
  </li>

### 抽象类
<ol>
  <li>抽象方法的概念：抽象方法就是指不能具体实现的方法，也就是没有方法体并使用abstract关键字修饰
    <ol>
      <li>语法格式
        <div class="language-java highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="err">访问控制符</span> <span class="kd">abstract</span> <span class="err">返回值类型</span> <span class="err">方法名称</span><span class="o">(</span><span class="err">形参列表</span><span class="o">);</span>
<span class="err">如：</span>
<span class="kd">public</span> <span class="kd">abstract</span> <span class="kt">void</span> <span class="nf">cry</span><span class="o">();</span>
</code></pre></div>        </div>
      </li>
    </ol>
  </li>
  <li>抽象类的概念：不能具体实例化的类，也就是不能创建对象并使用abstract的类</li>
  <li>注意事项
    <ol>
      <li>抽象类中可以有成员变量，构造方法以及成员方法</li>
      <li>抽象类中可以有抽象方法也可以没有抽象方法</li>
      <li>拥有抽象方法的类必须是抽象类，因此严格来说，具有抽象方法并使用abstract关键字修饰的类才算真正意义上的抽象类</li>
    </ol>
  </li>
  <li>实际意义
    <ol>
      <li>抽象类的意义不在于自身创建对象而在于被继承，当一个类继承抽象类后必须重写抽象类中的抽象方法，否则该类也变成抽象类</li>
      <li>也就是说抽象类对子类具有强制性和规范性，因此叫做模板设计模式</li>
    </ol>
  </li>
  <li>经验分享
    <ol>
      <li>在以后的开发中推荐使用多态的语法格式，当父类的引用指向子类对象时，那么父类引用直接调用的所有方法一定是父类拥有的方法，若希望更换子类时，只需要将new关键字后面的类型修改而其他地方无需更改立即生效，从而提高了代码的可维护性。</li>
      <li>缺点是：父类引用不能直接访问子类独有的方法，若访问则需要强转</li>
    </ol>
  </li>
</ol>


### 笔试题考点
<ol>
  <li>请问abstract和final关键字能不能共同修饰一个方法？</li>
  <li>答：不能，abstract修饰的方法是一个抽象方法，抽象方法是没有方法体的，它本身没有意义。它的意义体现在被继承和被重写。而final修饰的方法不能被重写，所以他俩不能共存</li>
  <li>请问abstract和static关键字能不能共同修饰一个方法？</li>
  <li>答：不能，abstract关键字不能创建对象的意义在于防止不小心调用抽象方法，而static将它体到类层级，可以直接通过类名调用，也就失去了本来的意义</li>
  <li>请问abstract和private关键字能不能共同修饰一个方法？</li>
  <li>答：不能，abstract修饰的方法是一个抽象方法，抽象方法是没有方法体的，它本身没有意义。它的意义体现在被继承和被重写。而private修饰的方法不能被继承，所以他俩不能共存</li>
</ol>