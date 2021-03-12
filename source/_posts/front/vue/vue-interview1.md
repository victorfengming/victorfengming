---
title: "Vue面试题合集"
cover: "/img/lynk/88.jpg"
date:       2020-02-23
subtitle: "前端面试题"
tags:
	- JavaScript
	- web
	- vue
	- front
---



作者：李棠辉  
链接：https://www.jianshu.com/p/e54a9a34a773  
来源：简书  
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。  

## 一. 请谈谈Vue中的MVVM模式
MVVM全称是Model-View-ViewModel

Vue是以数据为驱动的,`Vue`自身将`DOM`和数据进行绑定,一旦创建绑定,DOM和数据将保持同步,每当数据发生变化,`DOM`会跟着变化.ViewModel是`Vue`的核心,他是`Vue`的一个实例.

`Vue`实例时作用域某个HTML元素上的这个HTML元素可以是body,也可以是某个`id`所指代的元素.

DOMListeners和DataBindings是实现双向绑定的关键。DOMListeners监听页面所有View层DOM元素的变化，当发生变化，Model层的数据随之变化；DataBindings监听Model层的数据，当数据发生变化，View层的DOM元素随之变化。


## 二. `v-show`和`v-if`指令的共同点和不同点?
- `v-show`指令是通过修改元素的displayCSS属性让其显示或者隐藏
- `v-if`指令是直接销毁和重建DOM达到让元素显示和隐藏的效果

## 三. 如何让CSS只在当前组件中起作用?
将当前组件的`<style>`修改为`<style scoped>`

## 四. `<keep-alive></keep-alive>`的作用是什么?
`<keep-alive></keep-alive>` 包包裹动态组件时,会缓存不活动的组建实例,主要用于保留组件状态或避免重新渲染.

人话: 比如有一个列表和一个详情,那么客户就会经常执行

打开详情,==>>>返回列表==>>>打开详情...


这样的话列表和详情都是一个频率很高的页面,那么就可以对列表组件使用<keep-alive></keep-alive>进行缓存,这样sb用户每次返回列表的时候,都能从缓存中快速渲染,而不是重新加载数据.


## 五.Vue中引入组件的步骤?
1. 采用ES6的import...from... 语法或commonJS的require()方法引入组件
2. 对组件进行注册,代码如下:
```javascript
// 注册
Vue.component('my-component',{
    template:'<div>A custom component!</div>'
})
```
3. 使用组件`<my-component></my-component>`

## 六.指令v-el的作用是什么?
提供一个在页面上已存在的DOM元素作为Vue实例的挂载目标.可以是CSS选择器,也可以是一个HTMLElemen实例. 

## 七. 在Vue中使用插件的步骤
1. 采用ES6的import...from... 语法或commonJS的require()方法引入插件
2. 使用全局方法Vue.use(plugin)使用插件,可以传入一个选项对象Vue.use(MyPlugin,{someOption:true})

## 八.请列举出3个Vue中常用的生命周期钩子函数?
1. created:实例已经创建完成之后自动调用,在这一步,实例已经完成数据观测,属性和方法的运算,watch/event事件回调.然而,挂载阶段还没有开始,$el属性目前还不可见

2. mounted:`el`呗新创建出来`vm.$el`替换,并挂载到实例上去之后调用该钩子.如果`root`实例挂载了一个文档内元素,当mounted被调用时`vm.$el`也在文档内.

3. activated:`keep-alive`组件激活时调用

## 九. 请简述一下Vuex的原理和使用方法
一个应用可以看做是有上面三部分构成,组成`View`,`Actions`,`State`,数据的流动也是View=>Actions=>State=>View以此达到数据的单向流动,但是项目较大的,组件嵌套过多的时候,多组件共享同一个State会在数据传递时出现很多问题.Vuex就是为了解决这些问题而产生的.

Vuex可以被看做项目中所有组件的数据中心,我们将所有组件中共享的State抽离出来,任何组件都可以访问和操作我们是数据中心.

上图可以很好的说明VUex的组成,一个实例化的Vuex.Store有state,mutation和actions三个属性组成:
- state中保存着公有数据
- 改变state中的数据有且只有通过mutation中的方法,且mutation中的方法必须是同步的
- 如果要写异步的方法需要在actions中,并通过commit到mutations中进行state中数据的更改.

## 十.请谈谈vue框架和Angular.js和React的不同

### react
react和Vue有许多相似之处,它们都有:
- 使用virtual Dom
- 提供了响应式(Reactive)和组件化(composable)的视图组件.
- 将注意力集中保持在核心库,而将其他功能如路由和全局状态管理交给相关的库.

由于有着众多的相似之处,我们会用更多的时间在这一块进行比较.这里我们不知保证技术内容的准确性,同时也兼顾了平衡的考量.我们需要承认react比Vue更好的地方,比如更丰富的生态系统.

### 运行时的性能
react和Vue都是非常快的,所以速度并不是它们之中做选择的决定性因素.对于具体的数据表现,再说吧!

优化
在react应用中,当某个组件的状态发生改变时,它会以该组件为跟,重洗渲染整个组件子树。

如要避免不必要的子组件的重渲染，你需要在所有可能的地方使用 PureComponent，或是手动实现 shouldComponentUpdate 方法。同时你可能会需要使用不可变的数据结构来使得你的组件更容易被优化。

然而，使用 PureComponent 和 shouldComponentUpdate 时，需要保证该组件的整个子树的渲染输出都是由该组件的 props 所决定的。如果不符合这个情况，那么此类优化就会导致难以察觉的渲染结果不一致。这使得 React 中的组件优化伴随着相当的心智负担。

在 Vue 应用中，组件的依赖是在渲染过程中自动追踪的，所以系统能精确知晓哪个组件确实需要被重渲染。你可以理解为每一个组件都已经自动获得了 shouldComponentUpdate，并且没有上述的子树问题限制。

Vue 的这个特点使得开发者不再需要考虑此类优化，从而能够更好地专注于应用本身。






