---
title: "Flask 蓝图（Blueprint）使用方式解析"
cover: "/img/lynk/20.jpg"
date:       2019-11-29
subtitle: "模块化管理程序路由的功能"
tags:
	- Python
	- solution
	- web
	- flask
---


本文转自:https://www.jianshu.com/p/95b584e4f76e

<p>Flask蓝图提供了模块化管理程序路由的功能，使程序结构清晰、简单易懂。下面分析蓝图的使用方法</p>
<p>
    假如说我们要为某所学校的每个人建立一份档案，一个很自然的优化方式就是这些档案如果能分类管理，就是说假如分为老师、学生、后勤人员等类别，那么后续查找和管理这些档案就方便清晰许多。Flask的蓝图就提供了类似“分类”的功能。</p>
<p>下面先上一张较大型程序的组织结构图</p>
<p><br></p>
<div class="image-package">
    <div class="image-container" style="max-width: 274px; max-height: 305px; background-color: transparent;">
        <div class="image-container-fill" style="padding-bottom: 111.31%;"></div>
        <div class="image-view" data-width="274" data-height="305"><img
                data-original-src="//upload-images.jianshu.io/upload_images/3986433-8846a26e0dfcee93.png"
                data-original-width="274" data-original-height="305" data-original-format="image/png"
                data-original-filesize="35561" class="" data-image-index="0" style="cursor: zoom-in;"
                src="//upload-images.jianshu.io/upload_images/3986433-8846a26e0dfcee93.png?imageMogr2/auto-orient/strip|imageView2/2/w/274/format/webp">
        </div>
    </div>
    <div class="image-caption">
        <div>1</div>
    </div>
</div>
<p>可以看到在app文件夹下有两个文件夹main和auth内含有视图函数，而main和auth就是注册的两个蓝图。</p><h4>1. 蓝图的创建及注册</h4>
<p>在图1中，以main文件夹为例。在main文件夹的__init__.py文件中，可创建蓝图，代码如下：</p>
<p><br></p>
<div class="image-package">
    <div class="image-container" style="max-width: 303px; max-height: 130px; background-color: transparent;">
        <div class="image-container-fill" style="padding-bottom: 42.9%;"></div>
        <div class="image-view" data-width="303" data-height="130"><img
                data-original-src="//upload-images.jianshu.io/upload_images/3986433-232c3555da7e247a.png"
                data-original-width="303" data-original-height="130" data-original-format="image/png"
                data-original-filesize="24573" class="" data-image-index="1" style="cursor: zoom-in;"
                src="//upload-images.jianshu.io/upload_images/3986433-232c3555da7e247a.png?imageMogr2/auto-orient/strip|imageView2/2/w/303/format/webp">
        </div>
    </div>
    <div class="image-caption">2</div>
</div>
<p>从Flask中导入Blueprint类，再创建一个实例即可。Blueprint接受两个参数实例化，分别为蓝本的名字和蓝本所在的包或模块，大多数情况下第二个参数使用Python 的__name__ 变量即可。</p>
<p><br></p>
<div class="image-package">
    <div class="image-container" style="max-width: 514px; max-height: 111px; background-color: transparent;">
        <div class="image-container-fill" style="padding-bottom: 21.6%;"></div>
        <div class="image-view" data-width="514" data-height="111"><img
                data-original-src="//upload-images.jianshu.io/upload_images/3986433-9b53b1e2c92d4f72.png"
                data-original-width="514" data-original-height="111" data-original-format="image/png"
                data-original-filesize="35580" class="" data-image-index="2" style="cursor: zoom-in;"
                src="//upload-images.jianshu.io/upload_images/3986433-9b53b1e2c92d4f72.png?imageMogr2/auto-orient/strip|imageView2/2/w/514/format/webp">
        </div>
    </div>
    <div class="image-caption">3</div>
</div>
<p>在图3中，是在Flask文件夹下的__init__.py文件中注册这两个模块（请结合图1理解文件夹的组织结构）。该__init__.py文件中包含app创建函数，创建app后，即可注册已创立的蓝图。</p>
<p>最后一部是在main文件夹下的view文件中导入创建的蓝图，使用from . import main命令。不要忘记这一步，应为视图函数实在view文件种定义的，不导入蓝图的话，无法用蓝图定义路由。</p>
<p>另请注意在图2中，在main = Blueprint('main', __name__) 命令下有一个from . import views,
    errors命令。该命令的意思是导入在views和errors整个模块。在此我们发现views模块和__init__模块之间存在相互导入。一定要保证__init__模块中，from . import views,
    error命令在main = Blueprint('main', __name__)之后，否则会产生依赖循环导入的错误。</p><h4>2.&nbsp;使用蓝图创建路由</h4>
<p>使用蓝图创建路由的示例如下图：</p>
<p><br></p>
<div class="image-package">
    <div class="image-container" style="max-width: 363px; max-height: 88px; background-color: transparent;">
        <div class="image-container-fill" style="padding-bottom: 24.240000000000002%;"></div>
        <div class="image-view" data-width="363" data-height="88"><img
                data-original-src="//upload-images.jianshu.io/upload_images/3986433-5eaea53732c9baa6.png"
                data-original-width="363" data-original-height="88" data-original-format="image/png"
                data-original-filesize="20124" class="" data-image-index="3" style="cursor: zoom-in;"
                src="//upload-images.jianshu.io/upload_images/3986433-5eaea53732c9baa6.png?imageMogr2/auto-orient/strip|imageView2/2/w/363/format/webp">
        </div>
    </div>
    <div class="image-caption">4</div>
</div>
<p>
    该路由的创建有两点要注意，一是@main.route修饰器，在使用蓝图之前，所有的路由均通过@app.route注册，在此可对比创建蓝图后的不同。二是url_for函数的参数，该参数是一个“端点”名称，就是和在路由中定义的视图函数的名称，此处的‘
    .index ’端点名是一种简写的方式，就是表示main蓝图下的index函数。如果我们要指向‘auth’蓝图下的index函数，应该使用‘ auth.index ’ 端点名称</p>
<p>
    另请注意图4中生成的url和通过@app.route修饰器生成的url没有区别，是因为在注册main蓝图时（见图2）没有加“前缀”。回到图2，对比main蓝图和auth蓝图的注册，会发现auth在注册时多了一个url_prefix='/auth'
    ，这个就是加的前缀。假如我们通过@auth.route('/student')创建了一个路由，那么我们在访问该路由时，要输入www.somehost.com/auth/student 才能行。</p><h4>3.
    从蓝图回到全局</h4>
<p>创建蓝本后，会对Flask已定义的一些功能造成改变。例如在Flask中提供了一个before_request
    钩子，通过该钩子，可以注册在请求之前必须先完成的函数。在创建蓝本前，当访问通过@app.route修饰器创建的所有路由时，均要先完成在钩子中注册的函数。但注册蓝本后，如果使用@main.before_request钩子，那么我们访问通过别的蓝本注册的路由时，可不用先完成在钩子中注册的函数。如果仍要保持“全局”的功能，应该使用@main.before_app_request钩子。</p>
<p>回到文章的起点，蓝本的使用是程序结构明晰，在后续使用中如果有其他心得，笔者会继续补充。<br></p>

