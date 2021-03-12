---
title: 'jQ实现放大镜特效'
date:       2019-09-05
tags:
	- JavaScript
	- web
	- jQuery
---












下面代码是[何杰](https://hejie615.github.io/)同学写的  
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Document</title>
    <script src="https://cdn.staticfile.org/jquery/1.10.2/jquery.min.js"></script>
    <style type="text/css">    
    *{margin:0px;
        padding:0px;}
    .img{
        width: 350px;
        height: 350px;
        border: 1px solid #ccc;
        margin: 100px;
        position: relative;
        cursor:move;
    }    
    .bimg{
        position: relative;
        top: -400px;
        left: 500px;         
        border: 1px solid #ccc;
        width: 400px;
        height: 400px;         
        overflow: hidden;
        display: none;
    }  
    #move{
        position: absolute;
        width: 100px;
        height: 100px;        
        background-color: rgba(8,152,202,0.2);
        top: 0px;        
        left: 0px;
        display: none;
      }   
    .simg{
        width: 350px;
        height: 350px;
    }
    .bimg>img{
        position: absolute;
        left: 0px;
        top: 0px;
       }
    </style>

</head>
<body>
    <div class="img">   
        <div class="simg"><!--小图片-->     
            <img src="2.jpg" style="width:350px;height: 350px;" />     
            <div id="move"></div><!--放大区域-->  
        </div>  
        <div class="bimg"><!--大图片-->    
            <img src="2.jpg" style="width:1400px;height: 1400px;" />  
        </div>
    </div>

    
    <script>
    $(document).ready(function(){

        //鼠标移动到图片显示，移除隐藏     
        $(".img").hover(function(){           
            $(".bimg").css("display","block");          
            $("#move").css("display","block");       
        },function(){       
            $(".bimg").css("display","none");         
            $("#move").css("display","none");       
        });
        //放大区域移动，大图片移动
        $(".img").mousemove(function(event){
            var x = event.pageX;          
            var y = event.pageY;                   
            var nx = x - $(".img").offset().left-$("#move").width()/2;            
            var ny = y - $(".img").offset().top-$("#move").height()/2;           
            if(nx < 0){ 
                nx = 0;
            }            
            if(nx > $(".img").width()-$("#move").width()){        
                nx = $(".img").width()-$("#move").width();         
            }            
            if(ny < 0){       
                ny = 0;            
            }            
            if(ny > $(".img").height()-$("#move").height()){       
                ny = $(".img").height()-$("#move").height();     
            }                
            $("#move").css({           
                left:nx+"px",           
                top:ny+"px"       
            });           
            $(".bimg>img").css({         
                left:-nx*$(".bimg").width()/$("#move").width()+"px",   
                top:-ny*$(".bimg").height()/$("#move").height()+"px"      
            });
        })
                                                      
    });


    </script>
    

</body>
</html>


```