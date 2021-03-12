---
title: 'jQuery基础笔记和面试题'
date:       2019-09-01
tags:
	- JavaScript
	- web
	- jQuery
---


版权声明：本文为CSDN博主「软件大白」的原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接及本声明。   
原文链接：https://blog.csdn.net/qq_43645678/article/details/93380482

<div id="content_views" class="markdown_views prism-atom-one-dark">
                    <!-- flowchart 箭头图标 勿删 -->
                    <svg xmlns="http://www.w3.org/2000/svg" style="display: none;">
                        <path stroke-linecap="round" d="M5,0 0,2.5 5,5z" id="raphael-marker-block" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);"></path>
                    </svg>
                                            <p></p><div class="toc"><h3><a name="t0"></a>JQuery基础笔记及面试题</h3><ul><ul><li><a href="#1_jQuery__1" rel="nofollow" data-token="1ebbe8603d9a46efc7339617a93f9cad" target="_self">1. jQuery 是什么？</a></li><li><a href="#2__jQuery_29" rel="nofollow" data-token="e26aad90c9a5607aa8a4c88888b9b941" target="_self">2. 为什么要使用 jQuery?</a></li><li><a href="#3_jQuery__89" rel="nofollow" data-token="071daa6819456b90f422ddf7f9baa219" target="_self">3. jQuery 入口函数</a></li><ul><ul><li><a href="#1_jQueryJavaScript_90" rel="nofollow" data-token="e1e3323a7d25f704a388c4ed11f1533c" target="_self">1. jQuery与JavaScript加载模式对比</a></li><li><a href="#2_jQuery__158" rel="nofollow" data-token="5121bc31f9b3c6a4563285a178041c5c" target="_self">2. jQuery 其他写法</a></li><li><a href="#3__181" rel="nofollow" data-token="b793eacbbb3601b0b0aac800740b558e" target="_self">3. 解决$符号冲突问题</a></li><ul><ul><li><a href="#1____182" rel="nofollow" data-token="3c9cacbb1f8e7b7676a59ba3a6903452" target="_self">1. 释放 $ 使用权</a></li><li><a href="#2__191" rel="nofollow" data-token="5789283ca1c6688b839283d8745b0806" target="_self">2. 自定义访问符号</a></li></ul></ul></ul></ul><li><a href="#4_jQuery__200" rel="nofollow" data-token="f144cad15780114e737c4f1d3c8867c6" target="_self">4. jQuery 核心函数</a></li><li><a href="#5_jQuery__234" rel="nofollow" data-token="d4ea691e40a000aec36ab7efdaf5e39c" target="_self">5. jQuery 对象</a></li><ul><ul><li><a href="#1_jQuery__235" rel="nofollow" data-token="c7a852dabda87687ec4e635595f1f69f" target="_self">1. jQuery 对象的本质</a></li></ul></ul><li><a href="#6_jQuery__252" rel="nofollow" data-token="3290aafb414aa2ae4f55312bc532a47e" target="_self">6. jQuery 静态方法</a></li><ul><ul><li><a href="#1__253" rel="nofollow" data-token="f5181c752e8e90535593baf5248c8370" target="_self">1. 什么是静态方法</a></li><li><a href="#2_jQueryholdReady_278" rel="nofollow" data-token="cb5a6536de60ef5d594385c0364dbc37" target="_self">2. jQuery.holdReady()</a></li><li><a href="#3_each__302" rel="nofollow" data-token="0110106f1e97cb42df56fec6fd2c8cab" target="_self">3. each 方法</a></li><li><a href="#4_map__339" rel="nofollow" data-token="de127b5baec2634edb85b40a4565e524" target="_self">4. map 方法</a></li><li><a href="#5_trim__390" rel="nofollow" data-token="9017a2128cd776cde050739f792387f6" target="_self">5. trim 方法</a></li><li><a href="#6_isWindow__405" rel="nofollow" data-token="8db7baec5cb43e7ccdd8928e10d5e77f" target="_self">6. isWindow 方法</a></li><li><a href="#7_isArray__424" rel="nofollow" data-token="66ca9f6d3ebbcffb2f7914776ce8ac61" target="_self">7. isArray 方法</a></li><li><a href="#8_isFunction__440" rel="nofollow" data-token="8603d213253b09b1acd0ba9004e00899" target="_self">8. isFunction 方法</a></li></ul></ul><li><a href="#7_jQuery__463" rel="nofollow" data-token="a36b8ac7bb6beb1a9fe7d371adc35b40" target="_self">7. jQuery 选择器</a></li><ul><ul><li><a href="#1__464" rel="nofollow" data-token="5816df16573fc0cc123460c0e1b625e3" target="_self">1. 基础选择器</a></li><li><a href="#2__473" rel="nofollow" data-token="7e9d299bf8a1a4cc39def64a3948e643" target="_self">2. 层次选择器</a></li><li><a href="#3__481" rel="nofollow" data-token="6f96dd276abb46ee6fd335d078d679b3" target="_self">3. 内容过滤选择器</a></li><ul><ul><li><a href="#1_empty_489" rel="nofollow" data-token="12020e6caf984b1172409d86bcf54c97" target="_self">1. :empty</a></li><li><a href="#2_parent_520" rel="nofollow" data-token="9b8e87f27ca4c6cd93ba8b17325880ee" target="_self">2. :parent</a></li><li><a href="#3_containstext_551" rel="nofollow" data-token="232673dc5264e1b55ef80f7a2bbbb6a5" target="_self">3. :contains(text)</a></li><li><a href="#4_hasselector_583" rel="nofollow" data-token="270e23d01ae31692280c2b0a946ebbca" target="_self">4. :has(selector)</a></li></ul></ul></ul></ul><li><a href="#8_jQuery__620" rel="nofollow" data-token="b53fc50fcc26a89c93dbfb9a4168f9a6" target="_self">8. jQuery 属性操作</a></li><ul><ul><li><a href="#1__621" rel="nofollow" data-token="526f2cfdc2c55d24539cfefc4b7ee6bc" target="_self">1. 属性与属性节点</a></li><ul><ul><li><a href="#1_622" rel="nofollow" data-token="574f823ff59e166b593b766aa3f2aea3" target="_self">1.什么是属性?</a></li><li><a href="#2_626" rel="nofollow" data-token="a4869ef55a2697fe6c0e159ec37bf308" target="_self">2.如何操作属性?</a></li><li><a href="#3_634" rel="nofollow" data-token="5e1b7e5107c599cc0e424231213e0a64" target="_self">3.什么是属性节点?</a></li><li><a href="#4_642" rel="nofollow" data-token="23888c89443cc13662dce3f5744dbeed" target="_self">4.如何操作属性节点?</a></li><li><a href="#5_648" rel="nofollow" data-token="a009b64e2446e91e3b355c2e0213c1a4" target="_self">5.属性和属性节点有什么区别?</a></li></ul></ul><li><a href="#2__651" rel="nofollow" data-token="660bf590fd1eaea7fb35c66f4b076702" target="_self">2. 属性节点方法</a></li><ul><ul><li><a href="#1_attr__652" rel="nofollow" data-token="5bf91b4beb918e164a0c8efca4cde0c2" target="_self">1. attr 方法</a></li><li><a href="#2_removeAttr__680" rel="nofollow" data-token="2907add36583c982b0bccd23193792d1" target="_self">2. removeAttr 方法</a></li><li><a href="#3_prop__695" rel="nofollow" data-token="bdca49a8af58ad48d51fb44549fdbfc1" target="_self">3. prop 方法</a></li><li><a href="#4_removeProp__712" rel="nofollow" data-token="810bc8409aba847d2d77c5e3d0a6aba4" target="_self">4. removeProp 方法</a></li><li><a href="#5_attrprop_721" rel="nofollow" data-token="5daaa265654f47026733a029dadae1dd" target="_self">5. attr方法和prop方法区别</a></li></ul></ul></ul></ul><li><a href="#9_jQuery_Class__746" rel="nofollow" data-token="8a71f8032e43a79df94835138353253f" target="_self">9. jQuery Class 操作</a></li><ul><ul><li><a href="#1_jQuery_Class__747" rel="nofollow" data-token="59d04d840791757ece263f89b91c28d7" target="_self">1. jQuery Class 类操作</a></li><ul><ul><li><a href="#1_addClass_749" rel="nofollow" data-token="60dcee4557dad7186f5ca67df41ea2a8" target="_self">1. addClass</a></li><li><a href="#2_removeClass_766" rel="nofollow" data-token="ac883f9d0bec1c4d6e3a258324b2df42" target="_self">2. removeClass</a></li><li><a href="#3_toggleClass_784" rel="nofollow" data-token="7cd7b3fc45fcbace6811cc5c45c9952d" target="_self">3. toggleClass</a></li></ul></ul><li><a href="#2_jQuery__800" rel="nofollow" data-token="e00f707aedd087a80d8c56f524002733" target="_self">2. jQuery 文本值操作</a></li><ul><ul><li><a href="#1_html_801" rel="nofollow" data-token="e457f5fdfd946675ec729478472e2ca7" target="_self">1. html</a></li><li><a href="#2_text_836" rel="nofollow" data-token="70094919fd88b00be1e10ee48bac437e" target="_self">2. text</a></li><li><a href="#3_val_854" rel="nofollow" data-token="2e98d41daf76dc965a1770de5f76246c" target="_self">3. val</a></li></ul></ul><li><a href="#3_jQuery_CSS__871" rel="nofollow" data-token="8a3d95384c82efa0d803078feace94b0" target="_self">3. jQuery CSS 样式</a></li><ul><ul><li><a href="#1_css__872" rel="nofollow" data-token="ae9c6f4809376ebc02974a8785251647" target="_self">1. css 方法</a></li><li><a href="#2_width__901" rel="nofollow" data-token="c336fe6be98ca1da756bf6a920dacb31" target="_self">2. width 方法</a></li><li><a href="#3_height__917" rel="nofollow" data-token="6e5ee1bd8d3176bbd367f201d5e4bc7f" target="_self">3. height 方法</a></li></ul></ul><li><a href="#4_jQuery__934" rel="nofollow" data-token="5e87cf91efd006dcfca5d60a9c2f74c5" target="_self">4. jQuery 元素位置</a></li><ul><ul><li><a href="#1_offset__935" rel="nofollow" data-token="0cf8b403aa57461d714276f1e5172d16" target="_self">1. offset 方法</a></li><li><a href="#2_position__951" rel="nofollow" data-token="a201e64460fa74470c2a56ea5173a731" target="_self">2. position 方法</a></li></ul></ul><li><a href="#5_jQuery_scroll__968" rel="nofollow" data-token="83fa3a4c66946feda2f6b40281d95041" target="_self">5. jQuery scroll 方法</a></li><ul><ul><li><a href="#1_scrollTop__969" rel="nofollow" data-token="94a99ae0600fec17a0b133558d9381b4" target="_self">1. scrollTop 方法</a></li><li><a href="#2_scrollLeft__991" rel="nofollow" data-token="8283b11b09bde8aacc370555a4aed876" target="_self">2. scrollLeft 方法</a></li></ul></ul></ul></ul><li><a href="#10_jQuery__1016" rel="nofollow" data-token="fd67d046f0d3bfaa3bdb7f567ca05fc1" target="_self">10. jQuery 事件</a></li><ul><ul><li><a href="#1__1017" rel="nofollow" data-token="b0d3378557810b43ebdccbabe3aad9d7" target="_self">1. 事件绑定</a></li><li><a href="#2__1067" rel="nofollow" data-token="90c527dbfff05907b5324165cc424834" target="_self">2. 事件解绑</a></li><li><a href="#3__1093" rel="nofollow" data-token="c3e1abdbb5bbe56315e3169c89a380e6" target="_self">3. 事件坐标</a></li><li><a href="#4__1121" rel="nofollow" data-token="6edd40d059405a281a8da3d3dd41923d" target="_self">4. 事件冒泡</a></li><ul><ul><li><a href="#1__1122" rel="nofollow" data-token="54eefda561f2515173a024538a889b88" target="_self">1. 什么是事件冒泡</a></li><li><a href="#2__1124" rel="nofollow" data-token="b93f54b94c2b7cbc5c3ff67a562a1188" target="_self">2. 阻止事件冒泡</a></li></ul></ul><li><a href="#5__1140" rel="nofollow" data-token="843d4338f24ad1d33e718e6db6b81be1" target="_self">5. 默认行为</a></li><ul><ul><li><a href="#1__1141" rel="nofollow" data-token="13a998084e0e64ce445a3dec85c32a24" target="_self">1. 什么是默认行为</a></li><li><a href="#2__1143" rel="nofollow" data-token="893e96522c5ba95cfa98b7539bec5831" target="_self">2. 阻止默认行为</a></li></ul></ul><li><a href="#6__1159" rel="nofollow" data-token="59b5d32a578fe2586b1fb83dcffb8185" target="_self">6. 自动触发事件</a></li><ul><ul><li><a href="#1__1160" rel="nofollow" data-token="cbdaffaf1426e907ca080c1d863206b1" target="_self">1. 什么是自动触发事件</a></li><li><a href="#2__1162" rel="nofollow" data-token="82a3032ca5950e32fd9c00d00c83f2fb" target="_self">2. 自动触发方式</a></li></ul></ul><li><a href="#7__1201" rel="nofollow" data-token="3aa4a7b7bc9ef88ab57680034efb3f98" target="_self">7. 自定义事件</a></li><ul><ul><li><a href="#1__1202" rel="nofollow" data-token="08e14b24298e6245a74f91309446d7db" target="_self">1. 什么是自定义事件</a></li><li><a href="#2__1204" rel="nofollow" data-token="8e16ec142fd6577594e6bef1d976878b" target="_self">2. 自定义事件的条件</a></li></ul></ul><li><a href="#8__1219" rel="nofollow" data-token="7d3f14e44f84617421cb63f52404623c" target="_self">8. 事件命名空间</a></li><ul><ul><li><a href="#1__1220" rel="nofollow" data-token="8b417a3d92ff9429a2de7a53d717031e" target="_self">1. 什么是事件命名空间</a></li><li><a href="#2__1223" rel="nofollow" data-token="001f54d4ad86eedbba4eebf2088865b9" target="_self">2. 添加事件命名空间的条件</a></li><li><a href="#3__1226" rel="nofollow" data-token="d3dc7bc40f126d8a08ebbc9fc556e96e" target="_self">3. 事件命名空间注意点（面试题）</a></li></ul></ul><li><a href="#9__1263" rel="nofollow" data-token="dd8c999c9278987e10290982577c0447" target="_self">9. 事件委托</a></li><ul><ul><li><a href="#1__1264" rel="nofollow" data-token="dcb46830fadd2f976874394154ab599c" target="_self">1. 什么是事件委托</a></li><li><a href="#2__1268" rel="nofollow" data-token="89ff3a2fb4e35a3011d60e34e336d16f" target="_self">2. 事件委托的好处</a></li><li><a href="#3_jQuery__1275" rel="nofollow" data-token="ce1b80a2a89664930f2e8b090ee7430b" target="_self">3. jQuery 中添加事件委托</a></li></ul></ul><li><a href="#10__1342" rel="nofollow" data-token="e0396377b38cd0b16224d2bb0e6db32a" target="_self">10. 移入移出事件</a></li><ul><ul><li><a href="#1_mouseentermouseleave_1343" rel="nofollow" data-token="87cda0bcacd92fb03e64f59e7535cce0" target="_self">1. mouseenter/mouseleave</a></li><li><a href="#2_mouseovermouseout_1361" rel="nofollow" data-token="fac86912cfa9a9953661fc607fd3e922" target="_self">2. mouseover/mouseout</a></li><li><a href="#3_hover_1378" rel="nofollow" data-token="afea717873a5f473242a6a15492bf4e0" target="_self">3. hover</a></li></ul></ul></ul></ul><li><a href="#11_jQuery__1400" rel="nofollow" data-token="33128d82fedcecd613fd48c256d77bfd" target="_self">11. jQuery 动画效果</a></li><ul><ul><li><a href="#1__1401" rel="nofollow" data-token="a7fa6a58e876c097af27275df87432ed" target="_self">1. 显示，隐藏动画</a></li><ul><ul><li><a href="#1_show_1402" rel="nofollow" data-token="0c9292c529b76b26bd8d9d5598ba2402" target="_self">1. show</a></li><li><a href="#2_hide_1417" rel="nofollow" data-token="13ddff67c9893366c435625b66f84b45" target="_self">2. hide</a></li><li><a href="#3_toggle_1428" rel="nofollow" data-token="0546cd64b37b51347a63af5fdab9ce55" target="_self">3. toggle</a></li><li><a href="#4__1439" rel="nofollow" data-token="397b9542aafa36e1663e1377dceb070e" target="_self">4. 注意点</a></li></ul></ul><li><a href="#2__1448" rel="nofollow" data-token="b81eaf791e9dedfb2dfcf2895326250a" target="_self">2. 展开，收起动画</a></li><ul><ul><li><a href="#1_slideDown_1449" rel="nofollow" data-token="5f2ad4f092a7326997fd94f06096bfe2" target="_self">1. slideDown</a></li><li><a href="#2_slideUp_1458" rel="nofollow" data-token="2ee3b99665524e145484de6373fc1815" target="_self">2. slideUp</a></li><li><a href="#3_slideToggle_1467" rel="nofollow" data-token="9c90ca2a3e330c46ca204141965b0b86" target="_self">3. slideToggle</a></li></ul></ul><li><a href="#3__1477" rel="nofollow" data-token="05fb756caf8d73e7b96b0c6c4313caeb" target="_self">3. 淡入，淡出动画</a></li><ul><ul><li><a href="#1_fadeIn_1478" rel="nofollow" data-token="ae5a5366b4a5123328d323ae01e434d7" target="_self">1. fadeIn</a></li><li><a href="#2_fadeOut_1487" rel="nofollow" data-token="36fc4d36422ea767aef581aeccfb0861" target="_self">2. fadeOut</a></li><li><a href="#3_fadeToggle_1496" rel="nofollow" data-token="10a345c94eee22f91982923408438464" target="_self">3. fadeToggle</a></li><li><a href="#4_fadeTo_1505" rel="nofollow" data-token="04e6eff68196c4d3719364b4c05d1216" target="_self">4. fadeTo</a></li></ul></ul><li><a href="#4__1516" rel="nofollow" data-token="3e976b541d7ba5aad0cff6f411a4b49a" target="_self">4. 自定义动画</a></li><ul><ul><li><a href="#1_animate_1517" rel="nofollow" data-token="ae10a3fe9e873bc7b84987456b82ed86" target="_self">1. animate</a></li></ul></ul><li><a href="#5__1551" rel="nofollow" data-token="e67cf7880edccc3ffcbcbd5f7bb0a273" target="_self">5. 动画队列</a></li><li><a href="#6__1595" rel="nofollow" data-token="0429f55895c4d6bee45fc67e88afaf82" target="_self">6. 动画相关方法</a></li><ul><ul><li><a href="#1_delay_1596" rel="nofollow" data-token="b1300b99fcff243aaae76bf5b3cab97d" target="_self">1. delay</a></li><li><a href="#2_stop_1607" rel="nofollow" data-token="998b79faa19753735296e5ca0f5e4af7" target="_self">2. stop</a></li></ul></ul></ul></ul><li><a href="#12_jQuery__1627" rel="nofollow" data-token="d13dcaf1846f5523d3e1b5f0b50b3cee" target="_self">12. jQuery 文档处理</a></li><ul><ul><li><a href="#1__1628" rel="nofollow" data-token="347bcdd6996ad8c288179a76b98998c1" target="_self">1. 添加节点</a></li><ul><ul><li><a href="#1__1629" rel="nofollow" data-token="0f5f0ee85bf9d8c9595868bdd678d440" target="_self">1. 内部插入</a></li><li><a href="#2__1651" rel="nofollow" data-token="aeb109e75a85c7e4ce3c3bb612044761" target="_self">2. 外部插入</a></li></ul></ul><li><a href="#2__1673" rel="nofollow" data-token="92f9fe092fa9da4f47b18241e5b2275b" target="_self">2. 删除节点</a></li><li><a href="#3__1716" rel="nofollow" data-token="c03bf6b682a41c2135114a1cc095f70c" target="_self">3. 替换节点</a></li><li><a href="#4__1734" rel="nofollow" data-token="d5b91ae030b17068aa0d1cf2652edabd" target="_self">4. 复制节点</a></li><li><a href="#5__1760" rel="nofollow" data-token="4d2c06326247b19afd638e5abf871f72" target="_self">5. 包裹节点</a></li><li><a href="#6__1785" rel="nofollow" data-token="cab88d330ebcd89071b114363eeb9c26" target="_self">6. 遍历节点</a></li></ul></ul><li><a href="#13_jQuery__1800" rel="nofollow" data-token="cec26c0f2b9635d4b947e0c8f28f8eea" target="_self">13. jQuery 面试题</a></li><ul><ul><li><a href="#1_jQueryjquery_1801" rel="nofollow" data-token="11340e161ccadc92099217eea18c07d8" target="_self">1. 为什么要使用jQuery？jquery有哪些好处？</a></li><li><a href="#2_jQuery_1810" rel="nofollow" data-token="91cce21b57158f3fbfb1f96fd8287e6c" target="_self">2. jQuery能做什么？</a></li><li><a href="#3_jQuery____1818" rel="nofollow" data-token="37a82ffca4313d6e02903345a960460b" target="_self">3. jQuery 库中的 $() 是什么？</a></li><li><a href="#4_documentready__1823" rel="nofollow" data-token="47efba424b2c0d571b51166af3ee7b23" target="_self">4. $(document).ready() 是个什么函数？为什么要用它？</a></li><li><a href="#5_documentreadywindowonload_1828" rel="nofollow" data-token="d22075205764da2587d56ab12c7d50e2" target="_self">5. (document).ready()方法和window.onload有什么区别？</a></li><li><a href="#6_jQuerygetpost_1832" rel="nofollow" data-token="f90aad2a12a99df9ed91f69869b2ed0e" target="_self">6. jQuery中.get()提交和.post()提交的区别</a></li><li><a href="#7_jQuery_1838" rel="nofollow" data-token="4e490c5ab2cb3ee52deaaceaabee1fbe" target="_self">7. jQuery中有哪些方法可以遍历节点？</a></li><li><a href="#8_this__this__jQuery__1844" rel="nofollow" data-token="fdd14fb57ee2bfe9cc8c8e11c381aa53" target="_self">8. $(this) 和 this 关键字在 jQuery 中有何不同？</a></li><li><a href="#9__CDN__jQuery___1849" rel="nofollow" data-token="b72a21f019ed0b8c8e8c92aa2cb1917f" target="_self">9. 使用 CDN 加载 jQuery 库的主要优势是什么 ?</a></li><li><a href="#10__1854" rel="nofollow" data-token="09339dff98704d2c4d05262e4e9ac432" target="_self">10. 如何使用从服务器获取一个复杂数据(对象)?</a></li><li><a href="#11__1858" rel="nofollow" data-token="15b2d2d274822eee1b88da3998175253" target="_self">11. 在使用选择器的时要注意的地方?</a></li><li><a href="#12__1863" rel="nofollow" data-token="7b7e87c9392c323bb7c885dc27c069bc" target="_self">12. 有哪些查询节点的选择器？</a></li><li><a href="#13_jQuery____1873" rel="nofollow" data-token="54db6afb5521b94542eda8893ada1598" target="_self">13. jQuery是如何处理缓存的？ ( 要处理缓存就是禁用缓存 )</a></li><li><a href="#14_jquery_1881" rel="nofollow" data-token="5729e144d9c25cc9c7cf56a60f48b442" target="_self">14. 在jquery中你有没有编写过插件，插件有什么好处？你编写过那些插件？它应该注意那些？</a></li></ul></ul></ul></ul></div><p></p>
<h2><a name="t1"></a><a id="1_jQuery__1"></a>1. jQuery 是什么？</h2>
<p><img src="https://img-blog.csdnimg.cn/20190823203354877.png" alt="在这里插入图片描述"></p>
<ul>
<li>
<p>jQuery是一款优秀的 JavaScript 库，从命名可以看出 jquery 最主要的用途是用来做查询（ jQuery = js + Query),正如 jQuery 官方 Logo 副标题所说（write less, do more)使用 jQuery 能让我们对 HTML 文档遍历和操作，事件处理，动画以及 Ajax 变得更加简单</p>
</li>
<li>
<p>原生 JS 设置背景</p>
</li>
</ul>
<pre class="prettyprint"><code class="prism language-js has-numbering" onclick="mdcp.copyCode(event)" style="position: unset;">window<span class="token punctuation">.</span><span class="token function-variable function">onload</span> <span class="token operator">=</span> <span class="token keyword">function</span> <span class="token punctuation">(</span>ev<span class="token punctuation">)</span> <span class="token punctuation">{</span>
   <span class="token comment">// 1.利用原生的JS查找DOM元素</span>
   <span class="token keyword">var</span> div1 <span class="token operator">=</span> document<span class="token punctuation">.</span><span class="token function">getElementsByTagName</span><span class="token punctuation">(</span><span class="token string">"div"</span><span class="token punctuation">)</span><span class="token punctuation">[</span><span class="token number">0</span><span class="token punctuation">]</span><span class="token punctuation">;</span>
   <span class="token keyword">var</span> div2 <span class="token operator">=</span> document<span class="token punctuation">.</span><span class="token function">getElementsByClassName</span><span class="token punctuation">(</span><span class="token string">"box1"</span><span class="token punctuation">)</span><span class="token punctuation">[</span><span class="token number">0</span><span class="token punctuation">]</span><span class="token punctuation">;</span>
   <span class="token keyword">var</span> div3 <span class="token operator">=</span> document<span class="token punctuation">.</span><span class="token function">getElementById</span><span class="token punctuation">(</span><span class="token string">"box2"</span><span class="token punctuation">)</span><span class="token punctuation">;</span>

   <span class="token comment">// 2.利用原生的JS修改背景颜色</span>
   div1<span class="token punctuation">.</span>style<span class="token punctuation">.</span>backgroundColor <span class="token operator">=</span> <span class="token string">"red"</span><span class="token punctuation">;</span>
   div2<span class="token punctuation">.</span>style<span class="token punctuation">.</span>backgroundColor <span class="token operator">=</span> <span class="token string">"blue"</span><span class="token punctuation">;</span>
   div3<span class="token punctuation">.</span>style<span class="token punctuation">.</span>backgroundColor <span class="token operator">=</span> <span class="token string">"yellow"</span><span class="token punctuation">;</span>
<span class="token punctuation">}</span>
<div class="hljs-button {2}" data-title="复制"></div></code><ul class="pre-numbering" style=""><li style="color: rgb(153, 153, 153);">1</li><li style="color: rgb(153, 153, 153);">2</li><li style="color: rgb(153, 153, 153);">3</li><li style="color: rgb(153, 153, 153);">4</li><li style="color: rgb(153, 153, 153);">5</li><li style="color: rgb(153, 153, 153);">6</li><li style="color: rgb(153, 153, 153);">7</li><li style="color: rgb(153, 153, 153);">8</li><li style="color: rgb(153, 153, 153);">9</li><li style="color: rgb(153, 153, 153);">10</li><li style="color: rgb(153, 153, 153);">11</li></ul></pre>
<ul>
<li>使用 jQuery 设置背景</li>
</ul>
<pre class="prettyprint"><code class="prism language-js has-numbering" onclick="mdcp.copyCode(event)" style="position: unset;"><span class="token function">$</span><span class="token punctuation">(</span>document<span class="token punctuation">)</span><span class="token punctuation">.</span><span class="token function">ready</span><span class="token punctuation">(</span><span class="token keyword">function</span><span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token punctuation">{</span>
<span class="token comment">// 查询，操作 CSS 一步到位</span>
    <span class="token function">$</span><span class="token punctuation">(</span><span class="token string">"div"</span><span class="token punctuation">)</span><span class="token punctuation">.</span><span class="token function">eq</span><span class="token punctuation">(</span><span class="token number">0</span><span class="token punctuation">)</span><span class="token punctuation">.</span><span class="token function">css</span><span class="token punctuation">(</span><span class="token string">'background'</span><span class="token punctuation">,</span><span class="token string">'red'</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
    <span class="token function">$</span><span class="token punctuation">(</span><span class="token string">".one"</span><span class="token punctuation">)</span><span class="token punctuation">.</span><span class="token function">eq</span><span class="token punctuation">(</span><span class="token number">0</span><span class="token punctuation">)</span><span class="token punctuation">.</span><span class="token function">css</span><span class="token punctuation">(</span><span class="token string">'background'</span><span class="token punctuation">,</span><span class="token string">'blue'</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
    <span class="token function">$</span><span class="token punctuation">(</span><span class="token string">"#two"</span><span class="token punctuation">)</span><span class="token punctuation">.</span><span class="token function">css</span><span class="token punctuation">(</span><span class="token string">'background'</span><span class="token punctuation">,</span><span class="token string">'yellow'</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
<span class="token punctuation">}</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
<div class="hljs-button {2}" data-title="复制"></div></code><ul class="pre-numbering" style=""><li style="color: rgb(153, 153, 153);">1</li><li style="color: rgb(153, 153, 153);">2</li><li style="color: rgb(153, 153, 153);">3</li><li style="color: rgb(153, 153, 153);">4</li><li style="color: rgb(153, 153, 153);">5</li><li style="color: rgb(153, 153, 153);">6</li></ul></pre>
<h2><a name="t2"></a><a id="2__jQuery_29"></a>2. 为什么要使用 jQuery?</h2>
<ul>
<li>强大的选择器：方便快速查找 DOM 元素
<ul>
<li>通过 jQuery 查找 DOM 元素要比原生 js 快捷很多</li>
<li>jQuery允许开发者使用CSS1-CSS3几乎所有的选择器,以及jQuery独创的选择器</li>
</ul>
</li>
<li>链式调用: 可以通过 . 不断调用jQuery对象的方法
<ul>
<li>jQuery可以通过.（点）.不断调用jQuery对象的方法，而原生JavaScript则不一定</li>
</ul>
</li>
</ul>
<pre class="prettyprint"><code class="prism language-html has-numbering" onclick="mdcp.copyCode(event)" style="position: unset;"><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>script</span><span class="token punctuation">&gt;</span></span><span class="token script language-javascript">
    <span class="token comment">// 1.原生JavaScript</span>
    <span class="token keyword">var</span> div <span class="token operator">=</span> document<span class="token punctuation">.</span><span class="token function">getElementsByTagName</span><span class="token punctuation">(</span><span class="token string">"div"</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
    <span class="token comment">// 报错,必须分开写</span>
    div<span class="token punctuation">[</span><span class="token number">0</span><span class="token punctuation">]</span><span class="token punctuation">.</span>style<span class="token punctuation">.</span>backgroundColor <span class="token operator">=</span> <span class="token string">"red"</span><span class="token punctuation">.</span>width <span class="token operator">=</span> <span class="token number">200</span><span class="token operator">+</span><span class="token string">"px"</span><span class="token punctuation">;</span>
    <span class="token comment">// div[0].style.width = 200+"px";</span>
    
    <span class="token comment">// 2.jQuery</span>
    <span class="token function">$</span><span class="token punctuation">(</span>document<span class="token punctuation">)</span><span class="token punctuation">.</span><span class="token function">ready</span><span class="token punctuation">(</span><span class="token keyword">function</span> <span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
    <span class="token comment">// 不报错,后面还可以接着继续写</span>
        <span class="token function">$</span><span class="token punctuation">(</span><span class="token string">"div"</span><span class="token punctuation">)</span><span class="token punctuation">.</span><span class="token function">eq</span><span class="token punctuation">(</span><span class="token number">1</span><span class="token punctuation">)</span><span class="token punctuation">.</span><span class="token function">css</span><span class="token punctuation">(</span><span class="token string">'background'</span><span class="token punctuation">,</span> <span class="token string">'yellow'</span><span class="token punctuation">)</span><span class="token punctuation">.</span><span class="token function">css</span><span class="token punctuation">(</span><span class="token string">'width'</span><span class="token punctuation">,</span> <span class="token string">'200px'</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
    <span class="token punctuation">}</span><span class="token punctuation">)</span><span class="token punctuation">;</span> 
</span><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>script</span><span class="token punctuation">&gt;</span></span>
<div class="hljs-button {2}" data-title="复制"></div></code><ul class="pre-numbering" style=""><li style="color: rgb(153, 153, 153);">1</li><li style="color: rgb(153, 153, 153);">2</li><li style="color: rgb(153, 153, 153);">3</li><li style="color: rgb(153, 153, 153);">4</li><li style="color: rgb(153, 153, 153);">5</li><li style="color: rgb(153, 153, 153);">6</li><li style="color: rgb(153, 153, 153);">7</li><li style="color: rgb(153, 153, 153);">8</li><li style="color: rgb(153, 153, 153);">9</li><li style="color: rgb(153, 153, 153);">10</li><li style="color: rgb(153, 153, 153);">11</li><li style="color: rgb(153, 153, 153);">12</li><li style="color: rgb(153, 153, 153);">13</li></ul></pre>
<ul>
<li>隐式遍历(迭代): 一次操作多个元素</li>
</ul>
<pre class="prettyprint"><code class="prism language-html has-numbering" onclick="mdcp.copyCode(event)" style="position: unset;"><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>script</span><span class="token punctuation">&gt;</span></span><span class="token script language-javascript">
    <span class="token comment">// 1.原生JavaScript</span>
    <span class="token keyword">var</span> div <span class="token operator">=</span> document<span class="token punctuation">.</span><span class="token function">getElementsByTagName</span><span class="token punctuation">(</span><span class="token string">"div"</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
    <span class="token comment">// div.style.backgroundColor = "red";// 无效</span>
    <span class="token keyword">for</span><span class="token punctuation">(</span><span class="token keyword">var</span> i <span class="token operator">=</span> <span class="token number">0</span><span class="token punctuation">;</span> i<span class="token operator">&lt;</span>div<span class="token punctuation">.</span>length<span class="token punctuation">;</span> i<span class="token operator">++</span><span class="token punctuation">)</span><span class="token punctuation">{</span>
        div<span class="token punctuation">[</span>i<span class="token punctuation">]</span><span class="token punctuation">.</span>style<span class="token punctuation">.</span>backgroundColor <span class="token operator">=</span> <span class="token string">"red"</span><span class="token punctuation">;</span>
    <span class="token punctuation">}</span>

    <span class="token comment">// 2.jQuery</span>
    <span class="token function">$</span><span class="token punctuation">(</span>document<span class="token punctuation">)</span><span class="token punctuation">.</span><span class="token function">ready</span><span class="token punctuation">(</span><span class="token keyword">function</span> <span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
        <span class="token comment">// 隐式遍历(迭代)找到的所有div</span>
        <span class="token function">$</span><span class="token punctuation">(</span><span class="token string">"div"</span><span class="token punctuation">)</span><span class="token punctuation">.</span><span class="token function">css</span><span class="token punctuation">(</span><span class="token string">'background'</span><span class="token punctuation">,</span> <span class="token string">'yellow'</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
    <span class="token punctuation">}</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
</span><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>script</span><span class="token punctuation">&gt;</span></span>
<div class="hljs-button {2}" data-title="复制"></div></code><ul class="pre-numbering" style=""><li style="color: rgb(153, 153, 153);">1</li><li style="color: rgb(153, 153, 153);">2</li><li style="color: rgb(153, 153, 153);">3</li><li style="color: rgb(153, 153, 153);">4</li><li style="color: rgb(153, 153, 153);">5</li><li style="color: rgb(153, 153, 153);">6</li><li style="color: rgb(153, 153, 153);">7</li><li style="color: rgb(153, 153, 153);">8</li><li style="color: rgb(153, 153, 153);">9</li><li style="color: rgb(153, 153, 153);">10</li><li style="color: rgb(153, 153, 153);">11</li><li style="color: rgb(153, 153, 153);">12</li><li style="color: rgb(153, 153, 153);">13</li><li style="color: rgb(153, 153, 153);">14</li></ul></pre>
<ul>
<li>读写合一: 读数据/写数据使用是一个函数</li>
</ul>
<pre class="prettyprint"><code class="prism language-html has-numbering" onclick="mdcp.copyCode(event)" style="position: unset;"><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>script</span><span class="token punctuation">&gt;</span></span><span class="token script language-javascript">
    <span class="token function">$</span><span class="token punctuation">(</span>document<span class="token punctuation">)</span><span class="token punctuation">.</span><span class="token function">ready</span><span class="token punctuation">(</span><span class="token keyword">function</span> <span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
        <span class="token comment">// 读取数据</span>
        <span class="token keyword">var</span> $tx <span class="token operator">=</span> <span class="token function">$</span><span class="token punctuation">(</span><span class="token string">"div"</span><span class="token punctuation">)</span><span class="token punctuation">.</span><span class="token function">eq</span><span class="token punctuation">(</span><span class="token number">0</span><span class="token punctuation">)</span><span class="token punctuation">.</span><span class="token function">text</span><span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
        <span class="token function">alert</span><span class="token punctuation">(</span>$tx<span class="token punctuation">)</span><span class="token punctuation">;</span>
        <span class="token comment">// 写入数据</span>
        <span class="token function">$</span><span class="token punctuation">(</span><span class="token string">"div"</span><span class="token punctuation">)</span><span class="token punctuation">.</span><span class="token function">eq</span><span class="token punctuation">(</span><span class="token number">0</span><span class="token punctuation">)</span><span class="token punctuation">.</span><span class="token function">text</span><span class="token punctuation">(</span><span class="token string">"新的数据"</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
    <span class="token punctuation">}</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
</span><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>script</span><span class="token punctuation">&gt;</span></span>
<div class="hljs-button {2}" data-title="复制"></div></code><ul class="pre-numbering" style=""><li style="color: rgb(153, 153, 153);">1</li><li style="color: rgb(153, 153, 153);">2</li><li style="color: rgb(153, 153, 153);">3</li><li style="color: rgb(153, 153, 153);">4</li><li style="color: rgb(153, 153, 153);">5</li><li style="color: rgb(153, 153, 153);">6</li><li style="color: rgb(153, 153, 153);">7</li><li style="color: rgb(153, 153, 153);">8</li><li style="color: rgb(153, 153, 153);">9</li></ul></pre>
<ul>
<li>事件处理</li>
<li>DOM 操作（C增U改D删）</li>
<li>样式操作</li>
<li>动画</li>
<li>插件支持</li>
<li>浏览器兼容（建议学习1.x版本）
<ul>
<li>1.x：兼容ie678，但相对其它版本文件较大，官方只做BUG维护，功能不再新增，最终版本：1.12.4</li>
<li>2.x：不兼容ie678，相对1.x文件较小，官方只做BUG维护，功能不再新增，最终版本：2.2.4</li>
<li>3.x：不兼容ie678，只支持最新的浏览器，很多老的jQuery插件不支持这个版本，相对1.x文件较小，提供不包含Ajax/动画API版本</li>
</ul>
</li>
</ul>
<h2><a name="t3"></a><a id="3_jQuery__89"></a>3. jQuery 入口函数</h2>
<h4><a id="1_jQueryJavaScript_90"></a>1. jQuery与JavaScript加载模式对比</h4>
<ol>
<li>原生JS会等到DOM元素加载完毕,并且图片也加载完毕才会执行</li>
<li>jQuery会等到DOM元素加载完毕,但不会等到图片也加载完毕就会执行</li>
</ol>
<pre class="prettyprint"><code class="prism language-js has-numbering" onclick="mdcp.copyCode(event)" style="position: unset;"><span class="token comment">// js 原生入口函数</span>
window<span class="token punctuation">.</span><span class="token function-variable function">onload</span> <span class="token operator">=</span> <span class="token keyword">function</span> <span class="token punctuation">(</span>ev<span class="token punctuation">)</span> <span class="token punctuation">{</span>
   <span class="token comment">// 1.通过原生的JS入口函数可以拿到DOM元素</span>
   <span class="token keyword">var</span> images <span class="token operator">=</span> document<span class="token punctuation">.</span><span class="token function">getElementsByTagName</span><span class="token punctuation">(</span><span class="token string">"images"</span><span class="token punctuation">)</span><span class="token punctuation">[</span><span class="token number">0</span><span class="token punctuation">]</span><span class="token punctuation">;</span>
   
   <span class="token comment">// 2.通过原生的JS入口函数可以拿到DOM元素的宽高</span>
   <span class="token keyword">var</span> width <span class="token operator">=</span> window<span class="token punctuation">.</span><span class="token function">getComputedStyle</span><span class="token punctuation">(</span>images<span class="token punctuation">)</span><span class="token punctuation">.</span>width<span class="token punctuation">;</span>
            
<span class="token punctuation">}</span>
<div class="hljs-button {2}" data-title="复制"></div></code><ul class="pre-numbering" style=""><li style="color: rgb(153, 153, 153);">1</li><li style="color: rgb(153, 153, 153);">2</li><li style="color: rgb(153, 153, 153);">3</li><li style="color: rgb(153, 153, 153);">4</li><li style="color: rgb(153, 153, 153);">5</li><li style="color: rgb(153, 153, 153);">6</li><li style="color: rgb(153, 153, 153);">7</li><li style="color: rgb(153, 153, 153);">8</li><li style="color: rgb(153, 153, 153);">9</li></ul></pre>
<pre class="prettyprint"><code class="prism language-js has-numbering" onclick="mdcp.copyCode(event)" style="position: unset;"><span class="token comment">// jQuery 入口函数</span>
<span class="token function">$</span><span class="token punctuation">(</span>document<span class="token punctuation">)</span><span class="token punctuation">.</span><span class="token function">ready</span><span class="token punctuation">(</span><span class="token keyword">function</span> <span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
   <span class="token comment">// 1.通过jQuery入口函数可以拿到DOM元素</span>
   <span class="token keyword">var</span> $images <span class="token operator">=</span> <span class="token function">$</span><span class="token punctuation">(</span><span class="token string">"images"</span><span class="token punctuation">)</span><span class="token punctuation">;</span>

   <span class="token comment">// 2.通过jQuery入口函数不可以拿到DOM元素的宽高</span>
   <span class="token keyword">var</span> $width <span class="token operator">=</span> $images<span class="token punctuation">.</span><span class="token function">width</span><span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token punctuation">;</span>

<span class="token punctuation">}</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
<div class="hljs-button {2}" data-title="复制"></div></code><ul class="pre-numbering" style=""><li style="color: rgb(153, 153, 153);">1</li><li style="color: rgb(153, 153, 153);">2</li><li style="color: rgb(153, 153, 153);">3</li><li style="color: rgb(153, 153, 153);">4</li><li style="color: rgb(153, 153, 153);">5</li><li style="color: rgb(153, 153, 153);">6</li><li style="color: rgb(153, 153, 153);">7</li><li style="color: rgb(153, 153, 153);">8</li><li style="color: rgb(153, 153, 153);">9</li></ul></pre>
<ol>
<li>原生的JS如果编写了多个入口函数,后面编写的会覆盖前面编写的</li>
<li>jQuery中编写多个入口函数,后面的不会覆盖前面的</li>
</ol>
<pre class="prettyprint"><code class="prism language-js has-numbering" onclick="mdcp.copyCode(event)" style="position: unset;"><span class="token comment">// 原生 js</span>
window<span class="token punctuation">.</span><span class="token function-variable function">onload</span> <span class="token operator">=</span> <span class="token keyword">function</span> <span class="token punctuation">(</span>ev<span class="token punctuation">)</span> <span class="token punctuation">{</span>
    <span class="token function">alert</span><span class="token punctuation">(</span><span class="token string">"hello lnj1"</span><span class="token punctuation">)</span><span class="token punctuation">;</span><span class="token comment">// 不会显示</span>
<span class="token punctuation">}</span>
window<span class="token punctuation">.</span><span class="token function-variable function">onload</span> <span class="token operator">=</span> <span class="token keyword">function</span> <span class="token punctuation">(</span>ev<span class="token punctuation">)</span> <span class="token punctuation">{</span>
    <span class="token function">alert</span><span class="token punctuation">(</span><span class="token string">"hello lnj2"</span><span class="token punctuation">)</span><span class="token punctuation">;</span><span class="token comment">// 会显示</span>
<span class="token punctuation">}</span>

<span class="token comment">// jQuery</span>
<span class="token function">$</span><span class="token punctuation">(</span>document<span class="token punctuation">)</span><span class="token punctuation">.</span><span class="token function">ready</span><span class="token punctuation">(</span><span class="token keyword">function</span> <span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
    <span class="token function">alert</span><span class="token punctuation">(</span><span class="token string">"hello lnj1"</span><span class="token punctuation">)</span><span class="token punctuation">;</span><span class="token comment">// 会显示</span>
<span class="token punctuation">}</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
<span class="token function">$</span><span class="token punctuation">(</span>document<span class="token punctuation">)</span><span class="token punctuation">.</span><span class="token function">ready</span><span class="token punctuation">(</span><span class="token keyword">function</span> <span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
    <span class="token function">alert</span><span class="token punctuation">(</span><span class="token string">"hello lnj2"</span><span class="token punctuation">)</span><span class="token punctuation">;</span><span class="token comment">// 会显示</span>
<span class="token punctuation">}</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
<div class="hljs-button {2}" data-title="复制"></div></code><ul class="pre-numbering" style=""><li style="color: rgb(153, 153, 153);">1</li><li style="color: rgb(153, 153, 153);">2</li><li style="color: rgb(153, 153, 153);">3</li><li style="color: rgb(153, 153, 153);">4</li><li style="color: rgb(153, 153, 153);">5</li><li style="color: rgb(153, 153, 153);">6</li><li style="color: rgb(153, 153, 153);">7</li><li style="color: rgb(153, 153, 153);">8</li><li style="color: rgb(153, 153, 153);">9</li><li style="color: rgb(153, 153, 153);">10</li><li style="color: rgb(153, 153, 153);">11</li><li style="color: rgb(153, 153, 153);">12</li><li style="color: rgb(153, 153, 153);">13</li><li style="color: rgb(153, 153, 153);">14</li><li style="color: rgb(153, 153, 153);">15</li></ul></pre>
<ul>
<li>jQuery 不会覆盖的本质
<ul>
<li>jQuery框架本质是一个闭包,每次执行我们都会给ready函数传递一个新的函数,不同函数内部的数据不会相互干扰</li>
</ul>
</li>
<li>为何能访问$符号
<ul>
<li>因为$符号 jQuery 框架对外暴露的一个全局变量</li>
</ul>
</li>
<li>为何 window.jQuery = window.$ = jQuery;   而不是window.jQuery = jQuery;
<ul>
<li>jQuery框架不仅提供了jQuery访问还提供$访问,提升开发者的编码效率</li>
</ul>
</li>
<li>JavaScript中如何定义一个全局变量?
<ul>
<li>所有全局变量是 window 对象的属性</li>
<li>jQuery 框架源码实现</li>
</ul>
<pre class="prettyprint"><code class="prism language-js has-numbering" onclick="mdcp.copyCode(event)" style="position: unset;">window<span class="token punctuation">.</span>jQuery <span class="token operator">=</span> window<span class="token punctuation">.</span>$ <span class="token operator">=</span> jQuery<span class="token punctuation">;</span>
<div class="hljs-button {2}" data-title="复制"></div></code><ul class="pre-numbering" style=""><li style="color: rgb(153, 153, 153);">1</li></ul></pre>
<ul>
<li>使用 jQuery 框架只有两种方式
<ul>
<li>通过 $</li>
<li>通过 jQuery</li>
</ul>
</li>
</ul>
</li>
</ul>
<p><strong>总结：</strong></p>

<div class="table-box"><table>
<thead>
<tr>
<th></th>
<th>window.onload</th>
<th>$(document).ready()</th>
</tr>
</thead>
<tbody>
<tr>
<td>执行时机</td>
<td>必须等待网页全部加载完毕(包括 图片等),然后再执行包裹代码</td>
<td>只需要等待网页中的DOM结构 加载完毕,就能执行包裹的代码</td>
</tr>
<tr>
<td>执行次数</td>
<td>只能执行一次,如果第二次,那么 第一次的执行会被覆盖</td>
<td>可以执行多次,第N次都不会被上 一次覆盖</td>
</tr>
</tbody>
</table></div><h4><a id="2_jQuery__158"></a>2. jQuery 其他写法</h4>
<pre class="prettyprint"><code class="prism language-js has-numbering" onclick="mdcp.copyCode(event)" style="position: unset;"> <span class="token comment">// 1.第一种写法</span>
    <span class="token function">$</span><span class="token punctuation">(</span>document<span class="token punctuation">)</span><span class="token punctuation">.</span><span class="token function">ready</span><span class="token punctuation">(</span><span class="token keyword">function</span> <span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
        <span class="token comment">// alert("hello lnj");</span>
    <span class="token punctuation">}</span><span class="token punctuation">)</span><span class="token punctuation">;</span>

    <span class="token comment">// 2.第二种写法</span>
    <span class="token function">jQuery</span><span class="token punctuation">(</span>document<span class="token punctuation">)</span><span class="token punctuation">.</span><span class="token function">ready</span><span class="token punctuation">(</span><span class="token keyword">function</span> <span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
        <span class="token comment">// alert("hello lnj");</span>
    <span class="token punctuation">}</span><span class="token punctuation">)</span><span class="token punctuation">;</span>

    <span class="token comment">// 3.第三种写法(推荐)</span>
    <span class="token function">$</span><span class="token punctuation">(</span><span class="token keyword">function</span> <span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
        <span class="token comment">// alert("hello lnj");</span>
    <span class="token punctuation">}</span><span class="token punctuation">)</span><span class="token punctuation">;</span>

    <span class="token comment">// 4.第四种写法</span>
    <span class="token function">jQuery</span><span class="token punctuation">(</span><span class="token keyword">function</span> <span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
        <span class="token function">alert</span><span class="token punctuation">(</span><span class="token string">"hello lnj"</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
    <span class="token punctuation">}</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
<div class="hljs-button {2}" data-title="复制"></div></code><ul class="pre-numbering" style=""><li style="color: rgb(153, 153, 153);">1</li><li style="color: rgb(153, 153, 153);">2</li><li style="color: rgb(153, 153, 153);">3</li><li style="color: rgb(153, 153, 153);">4</li><li style="color: rgb(153, 153, 153);">5</li><li style="color: rgb(153, 153, 153);">6</li><li style="color: rgb(153, 153, 153);">7</li><li style="color: rgb(153, 153, 153);">8</li><li style="color: rgb(153, 153, 153);">9</li><li style="color: rgb(153, 153, 153);">10</li><li style="color: rgb(153, 153, 153);">11</li><li style="color: rgb(153, 153, 153);">12</li><li style="color: rgb(153, 153, 153);">13</li><li style="color: rgb(153, 153, 153);">14</li><li style="color: rgb(153, 153, 153);">15</li><li style="color: rgb(153, 153, 153);">16</li><li style="color: rgb(153, 153, 153);">17</li><li style="color: rgb(153, 153, 153);">18</li><li style="color: rgb(153, 153, 153);">19</li></ul></pre>
<h4><a id="3__181"></a>3. 解决$符号冲突问题</h4>
<h6><a id="1____182"></a>1. 释放 $ 使用权</h6>
<p><strong>当便捷访问符号发生冲突时,我们可以释放$使用权, 释放之后只能使用jQuery</strong></p>
<pre class="prettyprint"><code class="prism language-js has-numbering" onclick="mdcp.copyCode(event)" style="position: unset;">jQuery<span class="token punctuation">.</span><span class="token function">noConflict</span><span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
<div class="hljs-button {2}" data-title="复制"></div></code><ul class="pre-numbering" style=""><li style="color: rgb(153, 153, 153);">1</li></ul></pre>
<p><strong>注意点:</strong></p>
<ul>
<li>释放操作必须在编写其它jQuery代码之前编写</li>
<li>释放之后就不能再使用$,改为使用jQuery</li>
</ul>
<h6><a id="2__191"></a>2. 自定义访问符号</h6>
<pre class="prettyprint"><code class="prism language-js has-numbering" onclick="mdcp.copyCode(event)" style="position: unset;"> <span class="token comment">// 2.自定义一个访问符号</span>
    <span class="token keyword">var</span> nj <span class="token operator">=</span> jQuery<span class="token punctuation">.</span><span class="token function">noConflict</span><span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
    <span class="token function">nj</span><span class="token punctuation">(</span><span class="token keyword">function</span> <span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
        <span class="token function">alert</span><span class="token punctuation">(</span><span class="token string">"hello lnj"</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
    <span class="token punctuation">}</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
<div class="hljs-button {2}" data-title="复制"></div></code><ul class="pre-numbering" style=""><li style="color: rgb(153, 153, 153);">1</li><li style="color: rgb(153, 153, 153);">2</li><li style="color: rgb(153, 153, 153);">3</li><li style="color: rgb(153, 153, 153);">4</li><li style="color: rgb(153, 153, 153);">5</li></ul></pre>
<h2><a name="t4"></a><a id="4_jQuery__200"></a>4. jQuery 核心函数</h2>
<pre class="prettyprint"><code class="prism language-html has-numbering" onclick="mdcp.copyCode(event)" style="position: unset;">  <span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>script</span><span class="token punctuation">&gt;</span></span><span class="token script language-javascript">
        <span class="token function">$</span><span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token punctuation">;</span><span class="token comment">//jQuery原理();就代表调用jQuery的核心函数</span>

        <span class="token comment">// 1.接收一个函数</span>
        <span class="token function">$</span><span class="token punctuation">(</span><span class="token keyword">function</span> <span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
            <span class="token function">alert</span><span class="token punctuation">(</span><span class="token string">"hello lnj"</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
            
            <span class="token comment">// 2.接收一个字符串</span>
            <span class="token comment">// 2.1接收一个字符串选择器</span>
            <span class="token comment">// 返回一个jQuery对象, 对象中保存了找到的DOM元素</span>
            <span class="token keyword">var</span> $box1 <span class="token operator">=</span> <span class="token function">$</span><span class="token punctuation">(</span><span class="token string">".box1"</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
            <span class="token keyword">var</span> $box2 <span class="token operator">=</span> <span class="token function">$</span><span class="token punctuation">(</span><span class="token string">"#box2"</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
            
            <span class="token comment">// 2.2接收一个字符串代码片段</span>
            <span class="token comment">// 返回一个jQuery对象, 对象中保存了创建的DOM元素</span>
            <span class="token keyword">var</span> $p <span class="token operator">=</span> <span class="token function">$</span><span class="token punctuation">(</span><span class="token string">"&lt;p&gt;我是段落&lt;/p&gt;"</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
            $box1<span class="token punctuation">.</span><span class="token function">append</span><span class="token punctuation">(</span>$p<span class="token punctuation">)</span><span class="token punctuation">;</span>
            
            <span class="token comment">// 3.接收一个DOM元素</span>
            <span class="token comment">// 会被包装成一个jQuery对象返回给我们</span>
            <span class="token keyword">var</span> span <span class="token operator">=</span> document<span class="token punctuation">.</span><span class="token function">getElementsByTagName</span><span class="token punctuation">(</span><span class="token string">"span"</span><span class="token punctuation">)</span><span class="token punctuation">[</span><span class="token number">0</span><span class="token punctuation">]</span><span class="token punctuation">;</span>
            <span class="token keyword">var</span> $span <span class="token operator">=</span> <span class="token function">$</span><span class="token punctuation">(</span>span<span class="token punctuation">)</span><span class="token punctuation">;</span>

        <span class="token punctuation">}</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
    </span><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>script</span><span class="token punctuation">&gt;</span></span>
<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>body</span><span class="token punctuation">&gt;</span></span>
    <span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>div</span> <span class="token attr-name">class</span><span class="token attr-value"><span class="token punctuation">=</span><span class="token punctuation">"</span>box1<span class="token punctuation">"</span></span><span class="token punctuation">&gt;</span></span><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>div</span><span class="token punctuation">&gt;</span></span>
    <span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>div</span> <span class="token attr-name">id</span><span class="token attr-value"><span class="token punctuation">=</span><span class="token punctuation">"</span>box2<span class="token punctuation">"</span></span><span class="token punctuation">&gt;</span></span><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>div</span><span class="token punctuation">&gt;</span></span>
    <span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>span</span><span class="token punctuation">&gt;</span></span>我是span<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>span</span><span class="token punctuation">&gt;</span></span>
<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>body</span><span class="token punctuation">&gt;</span></span>
<div class="hljs-button {2}" data-title="复制"></div></code><ul class="pre-numbering" style=""><li style="color: rgb(153, 153, 153);">1</li><li style="color: rgb(153, 153, 153);">2</li><li style="color: rgb(153, 153, 153);">3</li><li style="color: rgb(153, 153, 153);">4</li><li style="color: rgb(153, 153, 153);">5</li><li style="color: rgb(153, 153, 153);">6</li><li style="color: rgb(153, 153, 153);">7</li><li style="color: rgb(153, 153, 153);">8</li><li style="color: rgb(153, 153, 153);">9</li><li style="color: rgb(153, 153, 153);">10</li><li style="color: rgb(153, 153, 153);">11</li><li style="color: rgb(153, 153, 153);">12</li><li style="color: rgb(153, 153, 153);">13</li><li style="color: rgb(153, 153, 153);">14</li><li style="color: rgb(153, 153, 153);">15</li><li style="color: rgb(153, 153, 153);">16</li><li style="color: rgb(153, 153, 153);">17</li><li style="color: rgb(153, 153, 153);">18</li><li style="color: rgb(153, 153, 153);">19</li><li style="color: rgb(153, 153, 153);">20</li><li style="color: rgb(153, 153, 153);">21</li><li style="color: rgb(153, 153, 153);">22</li><li style="color: rgb(153, 153, 153);">23</li><li style="color: rgb(153, 153, 153);">24</li><li style="color: rgb(153, 153, 153);">25</li><li style="color: rgb(153, 153, 153);">26</li><li style="color: rgb(153, 153, 153);">27</li><li style="color: rgb(153, 153, 153);">28</li><li style="color: rgb(153, 153, 153);">29</li><li style="color: rgb(153, 153, 153);">30</li></ul></pre>
<h2><a name="t5"></a><a id="5_jQuery__234"></a>5. jQuery 对象</h2>
<h4><a id="1_jQuery__235"></a>1. jQuery 对象的本质</h4>
<ul>
<li>jQuery 对象的本质是一个伪数组</li>
</ul>
<pre class="prettyprint"><code class="prism language-js has-numbering" onclick="mdcp.copyCode(event)" style="position: unset;"><span class="token keyword">var</span> $div <span class="token operator">=</span> <span class="token function">$</span><span class="token punctuation">(</span><span class="token string">"div"</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
    console<span class="token punctuation">.</span><span class="token function">log</span><span class="token punctuation">(</span>$div<span class="token punctuation">)</span><span class="token punctuation">;</span>
    
<span class="token keyword">var</span> arr <span class="token operator">=</span> <span class="token punctuation">[</span><span class="token number">1</span><span class="token punctuation">,</span> <span class="token number">3</span><span class="token punctuation">,</span> <span class="token number">5</span><span class="token punctuation">]</span><span class="token punctuation">;</span>
    console<span class="token punctuation">.</span><span class="token function">log</span><span class="token punctuation">(</span>arr<span class="token punctuation">)</span><span class="token punctuation">;</span>
<div class="hljs-button {2}" data-title="复制"></div></code><ul class="pre-numbering" style=""><li style="color: rgb(153, 153, 153);">1</li><li style="color: rgb(153, 153, 153);">2</li><li style="color: rgb(153, 153, 153);">3</li><li style="color: rgb(153, 153, 153);">4</li><li style="color: rgb(153, 153, 153);">5</li></ul></pre>
<ul>
<li>什么是伪数组
<ul>
<li>有 0 到 length-1 属性</li>
<li>并且有 length 属性<br>
<strong>例：</strong></li>
</ul>
</li>
</ul>
<pre class="prettyprint"><code class="prism language-js has-numbering" onclick="mdcp.copyCode(event)" style="position: unset;"><span class="token keyword">var</span> obj <span class="token operator">=</span> <span class="token punctuation">{</span><span class="token number">0</span><span class="token punctuation">:</span><span class="token string">"lnj"</span><span class="token punctuation">,</span> <span class="token number">1</span><span class="token punctuation">:</span><span class="token string">"33"</span><span class="token punctuation">,</span> <span class="token number">2</span><span class="token punctuation">:</span><span class="token string">"male"</span><span class="token punctuation">,</span> length<span class="token punctuation">:</span> <span class="token number">3</span><span class="token punctuation">}</span>
<div class="hljs-button {2}" data-title="复制"></div></code><ul class="pre-numbering" style=""><li style="color: rgb(153, 153, 153);">1</li></ul></pre>
<h2><a name="t6"></a><a id="6_jQuery__252"></a>6. jQuery 静态方法</h2>
<h4><a id="1__253"></a>1. 什么是静态方法</h4>
<p><strong>静态方法对应的是对象方法,对象方法用实例对象调用,而静态方法用类名调用</strong></p>
<pre class="prettyprint"><code class="prism language-js has-numbering" onclick="mdcp.copyCode(event)" style="position: unset;">  <span class="token comment">// 1.定义一个类</span>
  <span class="token keyword">function</span> <span class="token function">AClass</span><span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
   <span class="token punctuation">}</span>
   <span class="token comment">// 2.给这个类添加一个静态方法</span>
   <span class="token comment">// 直接添加给类的就是静态方法</span>
   AClass<span class="token punctuation">.</span><span class="token function-variable function">staticMethod</span> <span class="token operator">=</span> <span class="token keyword">function</span> <span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
       <span class="token function">alert</span><span class="token punctuation">(</span><span class="token string">"staticMethod"</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
   <span class="token punctuation">}</span>
   <span class="token comment">// 静态方法通过类名调用</span>
   AClass<span class="token punctuation">.</span><span class="token function">staticMethod</span><span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token punctuation">;</span>

   <span class="token comment">// 3.给这个类添加一个实例方法</span>
   AClass<span class="token punctuation">.</span>prototype<span class="token punctuation">.</span><span class="token function-variable function">instanceMethod</span> <span class="token operator">=</span> <span class="token keyword">function</span> <span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
       <span class="token function">alert</span><span class="token punctuation">(</span><span class="token string">"instanceMethod"</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
   <span class="token punctuation">}</span>
   <span class="token comment">// 实例方法通过类的实例调用</span>
   <span class="token comment">// 创建一个实例(创建一个对象)</span>
   <span class="token keyword">var</span> a <span class="token operator">=</span> <span class="token keyword">new</span> <span class="token class-name">AClass</span><span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
   <span class="token comment">// 通过实例调用实例方法</span>
   a<span class="token punctuation">.</span><span class="token function">instanceMethod</span><span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
<div class="hljs-button {2}" data-title="复制"></div></code><ul class="pre-numbering" style=""><li style="color: rgb(153, 153, 153);">1</li><li style="color: rgb(153, 153, 153);">2</li><li style="color: rgb(153, 153, 153);">3</li><li style="color: rgb(153, 153, 153);">4</li><li style="color: rgb(153, 153, 153);">5</li><li style="color: rgb(153, 153, 153);">6</li><li style="color: rgb(153, 153, 153);">7</li><li style="color: rgb(153, 153, 153);">8</li><li style="color: rgb(153, 153, 153);">9</li><li style="color: rgb(153, 153, 153);">10</li><li style="color: rgb(153, 153, 153);">11</li><li style="color: rgb(153, 153, 153);">12</li><li style="color: rgb(153, 153, 153);">13</li><li style="color: rgb(153, 153, 153);">14</li><li style="color: rgb(153, 153, 153);">15</li><li style="color: rgb(153, 153, 153);">16</li><li style="color: rgb(153, 153, 153);">17</li><li style="color: rgb(153, 153, 153);">18</li><li style="color: rgb(153, 153, 153);">19</li><li style="color: rgb(153, 153, 153);">20</li></ul></pre>
<h4><a id="2_jQueryholdReady_278"></a>2. jQuery.holdReady()</h4>
<ul>
<li>暂停或者恢复 jQuery.ready() 事件</li>
<li>传入 true 或 false</li>
</ul>
<pre class="prettyprint"><code class="prism language-html has-numbering" onclick="mdcp.copyCode(event)" style="position: unset;"><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>script</span><span class="token punctuation">&gt;</span></span><span class="token script language-javascript">
    <span class="token comment">// 使用$直接调用,是静态方法</span>
    $<span class="token punctuation">.</span><span class="token function">holdReady</span><span class="token punctuation">(</span><span class="token boolean">true</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
    <span class="token function">$</span><span class="token punctuation">(</span><span class="token keyword">function</span> <span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
       <span class="token function">$</span><span class="token punctuation">(</span><span class="token string">"#first"</span><span class="token punctuation">)</span><span class="token punctuation">.</span><span class="token function">click</span><span class="token punctuation">(</span><span class="token keyword">function</span> <span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
           <span class="token function">alert</span><span class="token punctuation">(</span><span class="token string">"我是你想要的弹窗"</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
       <span class="token punctuation">}</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
    <span class="token punctuation">}</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
</span><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>script</span><span class="token punctuation">&gt;</span></span>
<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>body</span><span class="token punctuation">&gt;</span></span>
    <span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>button</span> <span class="token attr-name">id</span><span class="token attr-value"><span class="token punctuation">=</span><span class="token punctuation">"</span>first<span class="token punctuation">"</span></span><span class="token punctuation">&gt;</span></span>点击测试弹出<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>button</span><span class="token punctuation">&gt;</span></span>
    <span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>button</span> <span class="token attr-name">id</span><span class="token attr-value"><span class="token punctuation">=</span><span class="token punctuation">"</span>second<span class="token punctuation">"</span></span><span class="token punctuation">&gt;</span></span>解除延迟<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>button</span><span class="token punctuation">&gt;</span></span>
<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>script</span><span class="token punctuation">&gt;</span></span><span class="token script language-javascript">
    <span class="token function">$</span><span class="token punctuation">(</span><span class="token string">"#second"</span><span class="token punctuation">)</span><span class="token punctuation">.</span><span class="token function">click</span><span class="token punctuation">(</span><span class="token keyword">function</span><span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token punctuation">{</span>
        $<span class="token punctuation">.</span><span class="token function">holdReady</span><span class="token punctuation">(</span><span class="token boolean">false</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
    <span class="token punctuation">}</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
</span><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>script</span><span class="token punctuation">&gt;</span></span>
<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>body</span><span class="token punctuation">&gt;</span></span>
<div class="hljs-button {2}" data-title="复制"></div></code><ul class="pre-numbering" style=""><li style="color: rgb(153, 153, 153);">1</li><li style="color: rgb(153, 153, 153);">2</li><li style="color: rgb(153, 153, 153);">3</li><li style="color: rgb(153, 153, 153);">4</li><li style="color: rgb(153, 153, 153);">5</li><li style="color: rgb(153, 153, 153);">6</li><li style="color: rgb(153, 153, 153);">7</li><li style="color: rgb(153, 153, 153);">8</li><li style="color: rgb(153, 153, 153);">9</li><li style="color: rgb(153, 153, 153);">10</li><li style="color: rgb(153, 153, 153);">11</li><li style="color: rgb(153, 153, 153);">12</li><li style="color: rgb(153, 153, 153);">13</li><li style="color: rgb(153, 153, 153);">14</li><li style="color: rgb(153, 153, 153);">15</li><li style="color: rgb(153, 153, 153);">16</li><li style="color: rgb(153, 153, 153);">17</li><li style="color: rgb(153, 153, 153);">18</li></ul></pre>
<h4><a id="3_each__302"></a>3. each 方法</h4>
<ul>
<li>js 原生 forEach 方法
<ul>
<li>原生的forEach方法只能遍历数组, 不能遍历伪数组</li>
</ul>
</li>
</ul>
<pre class="prettyprint"><code class="prism language-js has-numbering" onclick="mdcp.copyCode(event)" style="position: unset;"><span class="token comment">/*
  第一个参数: 遍历到的元素
  第二个参数: 当前遍历到的索引
*/</span>
    <span class="token keyword">var</span> arr <span class="token operator">=</span> <span class="token punctuation">[</span><span class="token number">1</span><span class="token punctuation">,</span> <span class="token number">3</span><span class="token punctuation">,</span> <span class="token number">5</span><span class="token punctuation">,</span> <span class="token number">7</span><span class="token punctuation">,</span> <span class="token number">9</span><span class="token punctuation">]</span><span class="token punctuation">;</span>
    <span class="token keyword">var</span> obj <span class="token operator">=</span> <span class="token punctuation">{</span><span class="token number">0</span><span class="token punctuation">:</span><span class="token number">1</span><span class="token punctuation">,</span> <span class="token number">1</span><span class="token punctuation">:</span><span class="token number">3</span><span class="token punctuation">,</span> <span class="token number">2</span><span class="token punctuation">:</span><span class="token number">5</span><span class="token punctuation">,</span> <span class="token number">3</span><span class="token punctuation">:</span><span class="token number">7</span><span class="token punctuation">,</span> <span class="token number">4</span><span class="token punctuation">:</span><span class="token number">9</span><span class="token punctuation">,</span> length<span class="token punctuation">:</span><span class="token number">5</span><span class="token punctuation">}</span><span class="token punctuation">;</span>
        
    arr<span class="token punctuation">.</span><span class="token function">forEach</span><span class="token punctuation">(</span><span class="token keyword">function</span> <span class="token punctuation">(</span>value<span class="token punctuation">,</span> index<span class="token punctuation">)</span> <span class="token punctuation">{</span>
        console<span class="token punctuation">.</span><span class="token function">log</span><span class="token punctuation">(</span>index<span class="token punctuation">,</span> value<span class="token punctuation">)</span><span class="token punctuation">;</span>
    <span class="token punctuation">}</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
    
    obj<span class="token punctuation">.</span><span class="token function">forEach</span><span class="token punctuation">(</span><span class="token keyword">function</span> <span class="token punctuation">(</span>value<span class="token punctuation">,</span> index<span class="token punctuation">)</span> <span class="token punctuation">{</span>
        console<span class="token punctuation">.</span><span class="token function">log</span><span class="token punctuation">(</span>index<span class="token punctuation">,</span> value<span class="token punctuation">)</span><span class="token punctuation">;</span><span class="token comment">// 报错</span>
    <span class="token punctuation">}</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
<div class="hljs-button {2}" data-title="复制"></div></code><ul class="pre-numbering" style=""><li style="color: rgb(153, 153, 153);">1</li><li style="color: rgb(153, 153, 153);">2</li><li style="color: rgb(153, 153, 153);">3</li><li style="color: rgb(153, 153, 153);">4</li><li style="color: rgb(153, 153, 153);">5</li><li style="color: rgb(153, 153, 153);">6</li><li style="color: rgb(153, 153, 153);">7</li><li style="color: rgb(153, 153, 153);">8</li><li style="color: rgb(153, 153, 153);">9</li><li style="color: rgb(153, 153, 153);">10</li><li style="color: rgb(153, 153, 153);">11</li><li style="color: rgb(153, 153, 153);">12</li><li style="color: rgb(153, 153, 153);">13</li><li style="color: rgb(153, 153, 153);">14</li></ul></pre>
<ul>
<li>jQuery 的 each 静态方法
<ul>
<li>遍历对象或数组(伪数组）</li>
<li>优点统一遍历对象和数组的方式</li>
<li>回调参数的顺序更符合我们的思维模式</li>
</ul>
</li>
</ul>
<pre class="prettyprint"><code class="prism language-js has-numbering" onclick="mdcp.copyCode(event)" style="position: unset;"><span class="token comment">// 1.利用jQuery的each静态方法遍历数组</span>
<span class="token comment">/*
第一个参数: 当前遍历到的索引
第二个参数: 遍历到的元素
*/</span>
    $<span class="token punctuation">.</span><span class="token function">each</span><span class="token punctuation">(</span>arr<span class="token punctuation">,</span> <span class="token keyword">function</span> <span class="token punctuation">(</span>index<span class="token punctuation">,</span> value<span class="token punctuation">)</span> <span class="token punctuation">{</span>
        console<span class="token punctuation">.</span><span class="token function">log</span><span class="token punctuation">(</span>index<span class="token punctuation">,</span> value<span class="token punctuation">)</span><span class="token punctuation">;</span>
    <span class="token punctuation">}</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
    $<span class="token punctuation">.</span><span class="token function">each</span><span class="token punctuation">(</span>obj<span class="token punctuation">,</span> <span class="token keyword">function</span> <span class="token punctuation">(</span>index<span class="token punctuation">,</span> value<span class="token punctuation">)</span> <span class="token punctuation">{</span>
        console<span class="token punctuation">.</span><span class="token function">log</span><span class="token punctuation">(</span>index<span class="token punctuation">,</span> value<span class="token punctuation">)</span><span class="token punctuation">;</span>
    <span class="token punctuation">}</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
<div class="hljs-button {2}" data-title="复制"></div></code><ul class="pre-numbering" style=""><li style="color: rgb(153, 153, 153);">1</li><li style="color: rgb(153, 153, 153);">2</li><li style="color: rgb(153, 153, 153);">3</li><li style="color: rgb(153, 153, 153);">4</li><li style="color: rgb(153, 153, 153);">5</li><li style="color: rgb(153, 153, 153);">6</li><li style="color: rgb(153, 153, 153);">7</li><li style="color: rgb(153, 153, 153);">8</li><li style="color: rgb(153, 153, 153);">9</li><li style="color: rgb(153, 153, 153);">10</li><li style="color: rgb(153, 153, 153);">11</li></ul></pre>
<h4><a id="4_map__339"></a>4. map 方法</h4>
<ul>
<li>js 原生 map 方法
<ul>
<li>不能遍历的伪数组</li>
</ul>
</li>
<li>jQuery 的 map 方法
<ul>
<li>遍历对象或数组,将回调函数的返回值组成一个新的数组返回</li>
</ul>
</li>
</ul>
<pre class="prettyprint"><code class="prism language-js has-numbering" onclick="mdcp.copyCode(event)" style="position: unset;"><span class="token function">$</span><span class="token punctuation">(</span><span class="token keyword">function</span> <span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
     <span class="token comment">// 4.1遍历数组</span>
     <span class="token keyword">var</span> arr <span class="token operator">=</span> <span class="token punctuation">[</span><span class="token number">1</span><span class="token punctuation">,</span> <span class="token number">3</span><span class="token punctuation">,</span> <span class="token number">5</span><span class="token punctuation">,</span> <span class="token number">7</span><span class="token punctuation">,</span> <span class="token number">9</span><span class="token punctuation">]</span><span class="token punctuation">;</span>
     <span class="token comment">// 4.1.1通过原生方法遍历数组</span>
     <span class="token comment">// 第一个回调函数参数是遍历到的元素</span>
     <span class="token comment">// 第二个回调函数参数是当前遍历的索引</span>
     <span class="token comment">// 第三个回调函数参数是当前被遍历的数组</span>
     <span class="token comment">// 返回值: 将回调函数返回值收集起来组成一个新的数组</span>
     <span class="token keyword">var</span> res <span class="token operator">=</span> arr<span class="token punctuation">.</span><span class="token function">map</span><span class="token punctuation">(</span><span class="token keyword">function</span> <span class="token punctuation">(</span>ele<span class="token punctuation">,</span> idx<span class="token punctuation">,</span> arr<span class="token punctuation">)</span> <span class="token punctuation">{</span>
         console<span class="token punctuation">.</span><span class="token function">log</span><span class="token punctuation">(</span>idx<span class="token punctuation">,</span> ele<span class="token punctuation">,</span> arr<span class="token punctuation">)</span><span class="token punctuation">;</span>
         <span class="token keyword">return</span> ele <span class="token operator">+</span> idx<span class="token punctuation">;</span>
     <span class="token punctuation">}</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
     console<span class="token punctuation">.</span><span class="token function">log</span><span class="token punctuation">(</span>res<span class="token punctuation">)</span><span class="token punctuation">;</span>
     
     <span class="token comment">// 4.1.2通过jQuery静态方法遍历数组</span>
     <span class="token comment">// 第一个回调函数参数是遍历到的元素</span>
     <span class="token comment">// 第二个回调函数参数是当前遍历的索引</span>
     <span class="token comment">// 返回值: 将回调函数返回值收集起来组成一个新的数组</span>
     <span class="token keyword">var</span> $res2 <span class="token operator">=</span> $<span class="token punctuation">.</span><span class="token function">map</span><span class="token punctuation">(</span>arr<span class="token punctuation">,</span> <span class="token keyword">function</span> <span class="token punctuation">(</span>ele<span class="token punctuation">,</span>idx<span class="token punctuation">)</span> <span class="token punctuation">{</span>
         console<span class="token punctuation">.</span><span class="token function">log</span><span class="token punctuation">(</span>idx<span class="token punctuation">,</span> ele<span class="token punctuation">)</span><span class="token punctuation">;</span>
         <span class="token keyword">return</span> ele <span class="token operator">+</span> idx<span class="token punctuation">;</span>
     <span class="token punctuation">}</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
     console<span class="token punctuation">.</span><span class="token function">log</span><span class="token punctuation">(</span>$res2<span class="token punctuation">)</span><span class="token punctuation">;</span>

     <span class="token comment">// 4.2遍历对象</span>
     <span class="token keyword">var</span> obj <span class="token operator">=</span> <span class="token punctuation">{</span>name<span class="token punctuation">:</span> <span class="token string">"lnj"</span><span class="token punctuation">,</span> age<span class="token punctuation">:</span><span class="token string">"33"</span><span class="token punctuation">,</span> gender<span class="token punctuation">:</span><span class="token string">"male"</span><span class="token punctuation">}</span><span class="token punctuation">;</span>
     <span class="token comment">/*
     obj.map(function (ele, idx, obj) {
         // 报错,原生JS没有map方法
         console.log(idx, ele, obj);
     });
     */</span>
     <span class="token keyword">var</span> $res <span class="token operator">=</span> $<span class="token punctuation">.</span><span class="token function">map</span><span class="token punctuation">(</span>obj<span class="token punctuation">,</span> <span class="token keyword">function</span> <span class="token punctuation">(</span>value<span class="token punctuation">,</span> key<span class="token punctuation">)</span> <span class="token punctuation">{</span>
         console<span class="token punctuation">.</span><span class="token function">log</span><span class="token punctuation">(</span>key<span class="token punctuation">,</span> value<span class="token punctuation">)</span><span class="token punctuation">;</span>
         <span class="token keyword">return</span> key <span class="token operator">+</span> value<span class="token punctuation">;</span>
     <span class="token punctuation">}</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
     console<span class="token punctuation">.</span><span class="token function">log</span><span class="token punctuation">(</span>$res<span class="token punctuation">)</span><span class="token punctuation">;</span>
 <span class="token punctuation">}</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
<div class="hljs-button {2}" data-title="复制"></div></code><ul class="pre-numbering" style=""><li style="color: rgb(153, 153, 153);">1</li><li style="color: rgb(153, 153, 153);">2</li><li style="color: rgb(153, 153, 153);">3</li><li style="color: rgb(153, 153, 153);">4</li><li style="color: rgb(153, 153, 153);">5</li><li style="color: rgb(153, 153, 153);">6</li><li style="color: rgb(153, 153, 153);">7</li><li style="color: rgb(153, 153, 153);">8</li><li style="color: rgb(153, 153, 153);">9</li><li style="color: rgb(153, 153, 153);">10</li><li style="color: rgb(153, 153, 153);">11</li><li style="color: rgb(153, 153, 153);">12</li><li style="color: rgb(153, 153, 153);">13</li><li style="color: rgb(153, 153, 153);">14</li><li style="color: rgb(153, 153, 153);">15</li><li style="color: rgb(153, 153, 153);">16</li><li style="color: rgb(153, 153, 153);">17</li><li style="color: rgb(153, 153, 153);">18</li><li style="color: rgb(153, 153, 153);">19</li><li style="color: rgb(153, 153, 153);">20</li><li style="color: rgb(153, 153, 153);">21</li><li style="color: rgb(153, 153, 153);">22</li><li style="color: rgb(153, 153, 153);">23</li><li style="color: rgb(153, 153, 153);">24</li><li style="color: rgb(153, 153, 153);">25</li><li style="color: rgb(153, 153, 153);">26</li><li style="color: rgb(153, 153, 153);">27</li><li style="color: rgb(153, 153, 153);">28</li><li style="color: rgb(153, 153, 153);">29</li><li style="color: rgb(153, 153, 153);">30</li><li style="color: rgb(153, 153, 153);">31</li><li style="color: rgb(153, 153, 153);">32</li><li style="color: rgb(153, 153, 153);">33</li><li style="color: rgb(153, 153, 153);">34</li><li style="color: rgb(153, 153, 153);">35</li><li style="color: rgb(153, 153, 153);">36</li><li style="color: rgb(153, 153, 153);">37</li><li style="color: rgb(153, 153, 153);">38</li></ul></pre>
<ul>
<li>jQuery中的each静态方法和map静态方法的区别:
<ol>
<li>each静态方法默认的返回值就是, 遍历谁就返回谁</li>
<li>map静态方法默认的返回值是一个空数组</li>
<li>each静态方法不支持在回调函数中对遍历的数组进行处理</li>
<li>map静态方法可以在回调函数中通过return对遍历的数组进行处理, 然后生成一个新的数组返回</li>
</ol>
</li>
</ul>
<h4><a id="5_trim__390"></a>5. trim 方法</h4>
<p><strong>作用:</strong> 去除字符串两端的空格<br>
<strong>参数:</strong> 需要去除空格的字符串<br>
<strong>返回值:</strong> 去除空格之后的字符串</p>
<pre class="prettyprint"><code class="prism language-html has-numbering" onclick="mdcp.copyCode(event)" style="position: unset;"><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>script</span><span class="token punctuation">&gt;</span></span><span class="token script language-javascript">
   <span class="token function">$</span><span class="token punctuation">(</span><span class="token keyword">function</span> <span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
       <span class="token keyword">var</span> str <span class="token operator">=</span> <span class="token string">"   lnj   "</span><span class="token punctuation">;</span>
       console<span class="token punctuation">.</span><span class="token function">log</span><span class="token punctuation">(</span><span class="token string">"---"</span><span class="token operator">+</span>str<span class="token operator">+</span><span class="token string">"---"</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
       <span class="token keyword">var</span> $res <span class="token operator">=</span> $<span class="token punctuation">.</span><span class="token function">trim</span><span class="token punctuation">(</span>str<span class="token punctuation">)</span><span class="token punctuation">;</span>
       console<span class="token punctuation">.</span><span class="token function">log</span><span class="token punctuation">(</span><span class="token string">"---"</span><span class="token operator">+</span>$res<span class="token operator">+</span><span class="token string">"---"</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
   <span class="token punctuation">}</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
</span><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>script</span><span class="token punctuation">&gt;</span></span>
<div class="hljs-button {2}" data-title="复制"></div></code><ul class="pre-numbering" style=""><li style="color: rgb(153, 153, 153);">1</li><li style="color: rgb(153, 153, 153);">2</li><li style="color: rgb(153, 153, 153);">3</li><li style="color: rgb(153, 153, 153);">4</li><li style="color: rgb(153, 153, 153);">5</li><li style="color: rgb(153, 153, 153);">6</li><li style="color: rgb(153, 153, 153);">7</li><li style="color: rgb(153, 153, 153);">8</li></ul></pre>
<h4><a id="6_isWindow__405"></a>6. isWindow 方法</h4>
<p><strong>作用:</strong> 判断传入的对象是否是window对象<br>
<strong>返回值:</strong> true/false</p>
<pre class="prettyprint"><code class="prism language-js has-numbering" onclick="mdcp.copyCode(event)" style="position: unset;"> <span class="token comment">// 真数组</span>
    <span class="token keyword">var</span> arr <span class="token operator">=</span> <span class="token punctuation">[</span><span class="token number">1</span><span class="token punctuation">,</span> <span class="token number">3</span><span class="token punctuation">,</span> <span class="token number">5</span><span class="token punctuation">,</span> <span class="token number">7</span><span class="token punctuation">,</span> <span class="token number">9</span><span class="token punctuation">]</span><span class="token punctuation">;</span>
    <span class="token comment">// 伪数组</span>
    <span class="token keyword">var</span> arrlike <span class="token operator">=</span> <span class="token punctuation">{</span><span class="token number">0</span><span class="token punctuation">:</span><span class="token number">1</span><span class="token punctuation">,</span> <span class="token number">1</span><span class="token punctuation">:</span><span class="token number">3</span><span class="token punctuation">,</span> <span class="token number">2</span><span class="token punctuation">:</span><span class="token number">5</span><span class="token punctuation">,</span> <span class="token number">3</span><span class="token punctuation">:</span><span class="token number">7</span><span class="token punctuation">,</span> <span class="token number">4</span><span class="token punctuation">:</span><span class="token number">9</span><span class="token punctuation">,</span> length<span class="token punctuation">:</span><span class="token number">5</span><span class="token punctuation">}</span><span class="token punctuation">;</span>
    <span class="token comment">// 对象</span>
    <span class="token keyword">var</span> obj <span class="token operator">=</span> <span class="token punctuation">{</span><span class="token string">"name"</span><span class="token punctuation">:</span><span class="token string">"lnj"</span><span class="token punctuation">,</span> age<span class="token punctuation">:</span><span class="token string">"33"</span><span class="token punctuation">}</span><span class="token punctuation">;</span>
    <span class="token comment">// 函数</span>
    <span class="token keyword">var</span> <span class="token function-variable function">fn</span> <span class="token operator">=</span> <span class="token keyword">function</span><span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token punctuation">{</span><span class="token punctuation">}</span><span class="token punctuation">;</span>
    <span class="token comment">// window对象</span>
    <span class="token keyword">var</span> w <span class="token operator">=</span> window<span class="token punctuation">;</span>
    
    <span class="token keyword">var</span> res <span class="token operator">=</span> $<span class="token punctuation">.</span><span class="token function">isWindow</span><span class="token punctuation">(</span>w<span class="token punctuation">)</span><span class="token punctuation">;</span>
    console<span class="token punctuation">.</span><span class="token function">log</span><span class="token punctuation">(</span>res<span class="token punctuation">)</span><span class="token punctuation">;</span>
<div class="hljs-button {2}" data-title="复制"></div></code><ul class="pre-numbering" style=""><li style="color: rgb(153, 153, 153);">1</li><li style="color: rgb(153, 153, 153);">2</li><li style="color: rgb(153, 153, 153);">3</li><li style="color: rgb(153, 153, 153);">4</li><li style="color: rgb(153, 153, 153);">5</li><li style="color: rgb(153, 153, 153);">6</li><li style="color: rgb(153, 153, 153);">7</li><li style="color: rgb(153, 153, 153);">8</li><li style="color: rgb(153, 153, 153);">9</li><li style="color: rgb(153, 153, 153);">10</li><li style="color: rgb(153, 153, 153);">11</li><li style="color: rgb(153, 153, 153);">12</li><li style="color: rgb(153, 153, 153);">13</li></ul></pre>
<h4><a id="7_isArray__424"></a>7. isArray 方法</h4>
<p><strong>作用:</strong> 判断传入的对象是否是真数组<br>
<strong>返回值:</strong> true/false</p>
<pre class="prettyprint"><code class="prism language-js has-numbering" onclick="mdcp.copyCode(event)" style="position: unset;"><span class="token function">$</span><span class="token punctuation">(</span><span class="token keyword">function</span> <span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
    <span class="token comment">// 对象</span>
    <span class="token keyword">var</span> obj <span class="token operator">=</span> <span class="token punctuation">{</span>name<span class="token punctuation">:</span><span class="token string">"lnj"</span><span class="token punctuation">,</span>age<span class="token punctuation">:</span> <span class="token string">"33"</span><span class="token punctuation">,</span> gender<span class="token punctuation">:</span><span class="token string">"male"</span><span class="token punctuation">}</span><span class="token punctuation">;</span>
    <span class="token comment">// 真数组</span>
    <span class="token keyword">var</span> arr <span class="token operator">=</span> <span class="token punctuation">[</span><span class="token number">1</span><span class="token punctuation">,</span> <span class="token number">3</span><span class="token punctuation">,</span> <span class="token number">5</span><span class="token punctuation">,</span> <span class="token number">7</span><span class="token punctuation">,</span> <span class="token number">9</span><span class="token punctuation">]</span><span class="token punctuation">;</span>
    <span class="token keyword">var</span> $res <span class="token operator">=</span> $<span class="token punctuation">.</span><span class="token function">isArray</span><span class="token punctuation">(</span>obj<span class="token punctuation">)</span><span class="token punctuation">;</span>
    console<span class="token punctuation">.</span><span class="token function">log</span><span class="token punctuation">(</span>$res<span class="token punctuation">)</span><span class="token punctuation">;</span><span class="token comment">// false</span>
    <span class="token keyword">var</span> $res2 <span class="token operator">=</span> $<span class="token punctuation">.</span><span class="token function">isArray</span><span class="token punctuation">(</span>arr<span class="token punctuation">)</span><span class="token punctuation">;</span>
    console<span class="token punctuation">.</span><span class="token function">log</span><span class="token punctuation">(</span>$res2<span class="token punctuation">)</span><span class="token punctuation">;</span><span class="token comment">// true</span>
<span class="token punctuation">}</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
<div class="hljs-button {2}" data-title="复制"></div></code><ul class="pre-numbering" style=""><li style="color: rgb(153, 153, 153);">1</li><li style="color: rgb(153, 153, 153);">2</li><li style="color: rgb(153, 153, 153);">3</li><li style="color: rgb(153, 153, 153);">4</li><li style="color: rgb(153, 153, 153);">5</li><li style="color: rgb(153, 153, 153);">6</li><li style="color: rgb(153, 153, 153);">7</li><li style="color: rgb(153, 153, 153);">8</li><li style="color: rgb(153, 153, 153);">9</li><li style="color: rgb(153, 153, 153);">10</li></ul></pre>
<h4><a id="8_isFunction__440"></a>8. isFunction 方法</h4>
<p><strong>作用:</strong> 判断传入的对象是否是一个函数<br>
<strong>返回值:</strong> true/false<br>
<strong>注意点:</strong></p>
<ul>
<li>jQuery框架本质上是一个函数</li>
<li>(function( window, undefined ) {})( window );</li>
</ul>
<pre class="prettyprint"><code class="prism language-js has-numbering" onclick="mdcp.copyCode(event)" style="position: unset;"><span class="token function">$</span><span class="token punctuation">(</span><span class="token keyword">function</span> <span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
    <span class="token keyword">var</span> obj <span class="token operator">=</span> <span class="token punctuation">{</span>name<span class="token punctuation">:</span><span class="token string">"lnj"</span><span class="token punctuation">,</span>age<span class="token punctuation">:</span> <span class="token string">"33"</span><span class="token punctuation">,</span> gender<span class="token punctuation">:</span><span class="token string">"male"</span><span class="token punctuation">}</span><span class="token punctuation">;</span>
    <span class="token keyword">var</span> arr <span class="token operator">=</span> <span class="token punctuation">[</span><span class="token number">1</span><span class="token punctuation">,</span> <span class="token number">3</span><span class="token punctuation">,</span> <span class="token number">5</span><span class="token punctuation">,</span> <span class="token number">7</span><span class="token punctuation">,</span> <span class="token number">9</span><span class="token punctuation">]</span><span class="token punctuation">;</span>
    <span class="token keyword">var</span> <span class="token function-variable function">fn</span> <span class="token operator">=</span> <span class="token keyword">function</span> <span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token punctuation">{</span><span class="token punctuation">}</span>
    <span class="token keyword">var</span> $res <span class="token operator">=</span> $<span class="token punctuation">.</span><span class="token function">isFunction</span><span class="token punctuation">(</span>obj<span class="token punctuation">)</span><span class="token punctuation">;</span>
    console<span class="token punctuation">.</span><span class="token function">log</span><span class="token punctuation">(</span>$res<span class="token punctuation">)</span><span class="token punctuation">;</span><span class="token comment">// false</span>
    $res <span class="token operator">=</span> $<span class="token punctuation">.</span><span class="token function">isFunction</span><span class="token punctuation">(</span>arr<span class="token punctuation">)</span><span class="token punctuation">;</span>
    console<span class="token punctuation">.</span><span class="token function">log</span><span class="token punctuation">(</span>$res<span class="token punctuation">)</span><span class="token punctuation">;</span>
    $res <span class="token operator">=</span> $<span class="token punctuation">.</span><span class="token function">isFunction</span><span class="token punctuation">(</span>fn<span class="token punctuation">)</span><span class="token punctuation">;</span>
    console<span class="token punctuation">.</span><span class="token function">log</span><span class="token punctuation">(</span>$res<span class="token punctuation">)</span><span class="token punctuation">;</span>
    <span class="token comment">// 通过该方法验证了我们前面所说的,jQuery框架本质是一个匿名函数</span>
    $res <span class="token operator">=</span> $<span class="token punctuation">.</span><span class="token function">isFunction</span><span class="token punctuation">(</span>$<span class="token punctuation">)</span><span class="token punctuation">;</span>
    console<span class="token punctuation">.</span><span class="token function">log</span><span class="token punctuation">(</span>$res<span class="token punctuation">)</span><span class="token punctuation">;</span>
<span class="token punctuation">}</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
<div class="hljs-button {2}" data-title="复制"></div></code><ul class="pre-numbering" style=""><li style="color: rgb(153, 153, 153);">1</li><li style="color: rgb(153, 153, 153);">2</li><li style="color: rgb(153, 153, 153);">3</li><li style="color: rgb(153, 153, 153);">4</li><li style="color: rgb(153, 153, 153);">5</li><li style="color: rgb(153, 153, 153);">6</li><li style="color: rgb(153, 153, 153);">7</li><li style="color: rgb(153, 153, 153);">8</li><li style="color: rgb(153, 153, 153);">9</li><li style="color: rgb(153, 153, 153);">10</li><li style="color: rgb(153, 153, 153);">11</li><li style="color: rgb(153, 153, 153);">12</li><li style="color: rgb(153, 153, 153);">13</li><li style="color: rgb(153, 153, 153);">14</li></ul></pre>
<h2><a name="t7"></a><a id="7_jQuery__463"></a>7. jQuery 选择器</h2>
<h4><a id="1__464"></a>1. 基础选择器</h4>

<div class="table-box"><table>
<thead>
<tr>
<th>选择器</th>
<th>名称</th>
<th>描述</th>
<th>返回</th>
<th>实例</th>
</tr>
</thead>
<tbody>
<tr>
<td>#id</td>
<td>id选择器</td>
<td>根据给定的id匹配一个元素</td>
<td>单个元素</td>
<td>$("#box");选取id为box元素</td>
</tr>
<tr>
<td>.class</td>
<td>类选择器</td>
<td>根据给定的类名匹配元素</td>
<td>集合元素</td>
<td>$(".box");选取所有类名为box元素</td>
</tr>
<tr>
<td>element</td>
<td>元素选择器</td>
<td>根据给定的元素名称匹配元素</td>
<td>集合元素</td>
<td>$(“p”);选取所有<p>元素</p></td>
</tr>
<tr>
<td>*</td>
<td>通配符选择器</td>
<td>匹配所有元素</td>
<td>集合元素</td>
<td>$("*");选取所有元素</td>
</tr>
<tr>
<td>selector1,selector2,selectorN</td>
<td>并集选择器</td>
<td>将所有选择器匹配到的元素合并后一起返回</td>
<td>集合元素</td>
<td>$(“div,p,.box”);选取所有<div>元素,所有<p>元素和所有类名为box元素</p></div></td>
</tr>
</tbody>
</table></div><h4><a id="2__473"></a>2. 层次选择器</h4>

<div class="table-box"><table>
<thead>
<tr>
<th>选择器</th>
<th>名称</th>
<th>描述</th>
<th>返回</th>
<th>实例</th>
</tr>
</thead>
<tbody>
<tr>
<td>$(“ancestor descendant”)</td>
<td>后代选择器</td>
<td>选取ancestor元素的所有descendant后代标签(不光是儿子,包括孙子/重孙子等)</td>
<td>集合元素</td>
<td>$(“div span”);选取<code>&lt;div&gt;</code>元素里所有的<code>&lt;span&gt;</code>元素</td>
</tr>
<tr>
<td>$(“parent &gt; child”)</td>
<td>子元素选择器</td>
<td>找到选取parent 元素中所有直接子元素child(只有儿子,不包括孙子/重孙子等)</td>
<td>集合元素</td>
<td>$(“div&gt;span”);选取<code>&lt;div&gt;</code>元素下元素名称是<code>&lt;span&gt;</code>的子元素</td>
</tr>
<tr>
<td>$(“prev + next”)</td>
<td>相邻兄弟选择器</td>
<td>选取prev元素后面紧跟的那个next元素</td>
<td>集合元素</td>
<td>$(".one+div");选取类名为one的下一个同级的<code>&lt;div&gt;</code>元素</td>
</tr>
<tr>
<td>$(“prev ~ siblings”)</td>
<td>通用兄弟选择器</td>
<td>选取prev元素后面的所有next元素</td>
<td>集合元素</td>
<td>$("#two~div");选取id名为two元素后面所有同级的<code>&lt;div&gt;</code>元素</td>
</tr>
</tbody>
</table></div><h4><a id="3__481"></a>3. 内容过滤选择器</h4>

<div class="table-box"><table>
<thead>
<tr>
<th>选择器</th>
<th>描述</th>
<th>返回</th>
</tr>
</thead>
<tbody>
<tr>
<td>:empty</td>
<td>选取不包含子元素或文本为空的元素</td>
<td>集合元素</td>
</tr>
<tr>
<td>:parent</td>
<td>选取含有子元素或文本的元素</td>
<td>集合元素</td>
</tr>
<tr>
<td>:contains(text)</td>
<td>选取含有文本内容为text的元素</td>
<td>集合元素</td>
</tr>
<tr>
<td>:has(selector)</td>
<td>选取含有选择器所匹配的元素的元素</td>
<td>集合元素</td>
</tr>
</tbody>
</table></div><h6><a id="1_empty_489"></a>1. :empty</h6>
<p><strong>作用:</strong> 找到既没有文本内容也没有子元素的指定元素</p>
<pre class="prettyprint"><code class="prism language-html has-numbering" onclick="mdcp.copyCode(event)" style="position: unset;"><span class="token doctype">&lt;!DOCTYPE html&gt;</span>
<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>html</span> <span class="token attr-name">lang</span><span class="token attr-value"><span class="token punctuation">=</span><span class="token punctuation">"</span>en<span class="token punctuation">"</span></span><span class="token punctuation">&gt;</span></span>
<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>head</span><span class="token punctuation">&gt;</span></span>
    <span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>meta</span> <span class="token attr-name">charset</span><span class="token attr-value"><span class="token punctuation">=</span><span class="token punctuation">"</span>UTF-8<span class="token punctuation">"</span></span><span class="token punctuation">&gt;</span></span>
    <span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>title</span><span class="token punctuation">&gt;</span></span>05-jQuery选择器<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>title</span><span class="token punctuation">&gt;</span></span>
    <span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>script</span> <span class="token attr-name">src</span><span class="token attr-value"><span class="token punctuation">=</span><span class="token punctuation">"</span>代码/js/jquery-1.12.4.js<span class="token punctuation">"</span></span><span class="token punctuation">&gt;</span></span><span class="token script language-javascript"></span><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>script</span><span class="token punctuation">&gt;</span></span>
    <span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>script</span><span class="token punctuation">&gt;</span></span><span class="token script language-javascript">
        <span class="token function">$</span><span class="token punctuation">(</span><span class="token keyword">function</span> <span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
           <span class="token comment">// 找到所有div中不包含文本内容或子元素的元素</span>
            <span class="token keyword">var</span> $res <span class="token operator">=</span> <span class="token function">$</span><span class="token punctuation">(</span><span class="token string">"div:empty"</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
            console<span class="token punctuation">.</span><span class="token function">log</span><span class="token punctuation">(</span>$res<span class="token punctuation">.</span>length<span class="token punctuation">)</span><span class="token punctuation">;</span> <span class="token comment">// 找到1个元素</span>
            $res<span class="token punctuation">.</span><span class="token function">each</span><span class="token punctuation">(</span><span class="token keyword">function</span> <span class="token punctuation">(</span>idx<span class="token punctuation">,</span>ele<span class="token punctuation">)</span> <span class="token punctuation">{</span>
                console<span class="token punctuation">.</span><span class="token function">log</span><span class="token punctuation">(</span>idx<span class="token punctuation">,</span> ele<span class="token punctuation">)</span><span class="token punctuation">;</span> <span class="token comment">// one</span>
            <span class="token punctuation">}</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
        <span class="token punctuation">}</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
    </span><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>script</span><span class="token punctuation">&gt;</span></span>
<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>head</span><span class="token punctuation">&gt;</span></span>
<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>body</span><span class="token punctuation">&gt;</span></span>
<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>div</span> <span class="token attr-name">class</span><span class="token attr-value"><span class="token punctuation">=</span><span class="token punctuation">"</span>one<span class="token punctuation">"</span></span><span class="token punctuation">&gt;</span></span><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>div</span><span class="token punctuation">&gt;</span></span>
<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>div</span> <span class="token attr-name">class</span><span class="token attr-value"><span class="token punctuation">=</span><span class="token punctuation">"</span>two<span class="token punctuation">"</span></span><span class="token punctuation">&gt;</span></span>zs<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>div</span><span class="token punctuation">&gt;</span></span><span class="token comment">&lt;!--包含内容不会被找到--&gt;</span>
<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>div</span> <span class="token attr-name">class</span><span class="token attr-value"><span class="token punctuation">=</span><span class="token punctuation">"</span>three<span class="token punctuation">"</span></span><span class="token punctuation">&gt;</span></span><span class="token comment">&lt;!--包含子元素不会被找到--&gt;</span>
    <span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>span</span><span class="token punctuation">&gt;</span></span>lnj<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>span</span><span class="token punctuation">&gt;</span></span>
<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>div</span><span class="token punctuation">&gt;</span></span>
<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>span</span> <span class="token attr-name">class</span><span class="token attr-value"><span class="token punctuation">=</span><span class="token punctuation">"</span>five<span class="token punctuation">"</span></span><span class="token punctuation">&gt;</span></span><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>span</span><span class="token punctuation">&gt;</span></span><span class="token comment">&lt;!--不是指定元素不会被找到--&gt;</span>
<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>body</span><span class="token punctuation">&gt;</span></span>
<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>html</span><span class="token punctuation">&gt;</span></span>
<div class="hljs-button {2}" data-title="复制"></div></code><ul class="pre-numbering" style=""><li style="color: rgb(153, 153, 153);">1</li><li style="color: rgb(153, 153, 153);">2</li><li style="color: rgb(153, 153, 153);">3</li><li style="color: rgb(153, 153, 153);">4</li><li style="color: rgb(153, 153, 153);">5</li><li style="color: rgb(153, 153, 153);">6</li><li style="color: rgb(153, 153, 153);">7</li><li style="color: rgb(153, 153, 153);">8</li><li style="color: rgb(153, 153, 153);">9</li><li style="color: rgb(153, 153, 153);">10</li><li style="color: rgb(153, 153, 153);">11</li><li style="color: rgb(153, 153, 153);">12</li><li style="color: rgb(153, 153, 153);">13</li><li style="color: rgb(153, 153, 153);">14</li><li style="color: rgb(153, 153, 153);">15</li><li style="color: rgb(153, 153, 153);">16</li><li style="color: rgb(153, 153, 153);">17</li><li style="color: rgb(153, 153, 153);">18</li><li style="color: rgb(153, 153, 153);">19</li><li style="color: rgb(153, 153, 153);">20</li><li style="color: rgb(153, 153, 153);">21</li><li style="color: rgb(153, 153, 153);">22</li><li style="color: rgb(153, 153, 153);">23</li><li style="color: rgb(153, 153, 153);">24</li><li style="color: rgb(153, 153, 153);">25</li><li style="color: rgb(153, 153, 153);">26</li></ul></pre>
<h6><a id="2_parent_520"></a>2. :parent</h6>
<p><strong>作用:</strong>  找到有文本内容或有子元素的指定元素</p>
<pre class="prettyprint"><code class="prism language-html has-numbering" onclick="mdcp.copyCode(event)" style="position: unset;"><span class="token doctype">&lt;!DOCTYPE html&gt;</span>
<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>html</span> <span class="token attr-name">lang</span><span class="token attr-value"><span class="token punctuation">=</span><span class="token punctuation">"</span>en<span class="token punctuation">"</span></span><span class="token punctuation">&gt;</span></span>
<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>head</span><span class="token punctuation">&gt;</span></span>
    <span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>meta</span> <span class="token attr-name">charset</span><span class="token attr-value"><span class="token punctuation">=</span><span class="token punctuation">"</span>UTF-8<span class="token punctuation">"</span></span><span class="token punctuation">&gt;</span></span>
    <span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>title</span><span class="token punctuation">&gt;</span></span>05-jQuery选择器<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>title</span><span class="token punctuation">&gt;</span></span>
    <span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>script</span> <span class="token attr-name">src</span><span class="token attr-value"><span class="token punctuation">=</span><span class="token punctuation">"</span>代码/js/jquery-1.12.4.js<span class="token punctuation">"</span></span><span class="token punctuation">&gt;</span></span><span class="token script language-javascript"></span><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>script</span><span class="token punctuation">&gt;</span></span>
    <span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>script</span><span class="token punctuation">&gt;</span></span><span class="token script language-javascript">
        <span class="token function">$</span><span class="token punctuation">(</span><span class="token keyword">function</span> <span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
           <span class="token comment">// 找到所有div中包含文本内容或子元素的元素</span>
            <span class="token keyword">var</span> $res <span class="token operator">=</span> <span class="token function">$</span><span class="token punctuation">(</span><span class="token string">"div:parent"</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
            console<span class="token punctuation">.</span><span class="token function">log</span><span class="token punctuation">(</span>$res<span class="token punctuation">.</span>length<span class="token punctuation">)</span><span class="token punctuation">;</span>
            $res<span class="token punctuation">.</span><span class="token function">each</span><span class="token punctuation">(</span><span class="token keyword">function</span> <span class="token punctuation">(</span>idx<span class="token punctuation">,</span> ele<span class="token punctuation">)</span> <span class="token punctuation">{</span>
                console<span class="token punctuation">.</span><span class="token function">log</span><span class="token punctuation">(</span>idx<span class="token punctuation">,</span> ele<span class="token punctuation">)</span><span class="token punctuation">;</span>
            <span class="token punctuation">}</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
        <span class="token punctuation">}</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
    </span><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>script</span><span class="token punctuation">&gt;</span></span>
<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>head</span><span class="token punctuation">&gt;</span></span>
<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>body</span><span class="token punctuation">&gt;</span></span>
<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>div</span> <span class="token attr-name">class</span><span class="token attr-value"><span class="token punctuation">=</span><span class="token punctuation">"</span>one<span class="token punctuation">"</span></span><span class="token punctuation">&gt;</span></span><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>div</span><span class="token punctuation">&gt;</span></span>
<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>div</span> <span class="token attr-name">class</span><span class="token attr-value"><span class="token punctuation">=</span><span class="token punctuation">"</span>two<span class="token punctuation">"</span></span><span class="token punctuation">&gt;</span></span>zs<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>div</span><span class="token punctuation">&gt;</span></span><span class="token comment">&lt;!--有文本内容会被找到--&gt;</span>
<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>div</span> <span class="token attr-name">class</span><span class="token attr-value"><span class="token punctuation">=</span><span class="token punctuation">"</span>three<span class="token punctuation">"</span></span><span class="token punctuation">&gt;</span></span><span class="token comment">&lt;!--有子元素会被找到--&gt;</span>
    <span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>span</span><span class="token punctuation">&gt;</span></span>lnj<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>span</span><span class="token punctuation">&gt;</span></span>
<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>div</span><span class="token punctuation">&gt;</span></span>
<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>span</span> <span class="token attr-name">class</span><span class="token attr-value"><span class="token punctuation">=</span><span class="token punctuation">"</span>five<span class="token punctuation">"</span></span><span class="token punctuation">&gt;</span></span><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>span</span><span class="token punctuation">&gt;</span></span>
<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>body</span><span class="token punctuation">&gt;</span></span>
<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>html</span><span class="token punctuation">&gt;</span></span>
<div class="hljs-button {2}" data-title="复制"></div></code><ul class="pre-numbering" style=""><li style="color: rgb(153, 153, 153);">1</li><li style="color: rgb(153, 153, 153);">2</li><li style="color: rgb(153, 153, 153);">3</li><li style="color: rgb(153, 153, 153);">4</li><li style="color: rgb(153, 153, 153);">5</li><li style="color: rgb(153, 153, 153);">6</li><li style="color: rgb(153, 153, 153);">7</li><li style="color: rgb(153, 153, 153);">8</li><li style="color: rgb(153, 153, 153);">9</li><li style="color: rgb(153, 153, 153);">10</li><li style="color: rgb(153, 153, 153);">11</li><li style="color: rgb(153, 153, 153);">12</li><li style="color: rgb(153, 153, 153);">13</li><li style="color: rgb(153, 153, 153);">14</li><li style="color: rgb(153, 153, 153);">15</li><li style="color: rgb(153, 153, 153);">16</li><li style="color: rgb(153, 153, 153);">17</li><li style="color: rgb(153, 153, 153);">18</li><li style="color: rgb(153, 153, 153);">19</li><li style="color: rgb(153, 153, 153);">20</li><li style="color: rgb(153, 153, 153);">21</li><li style="color: rgb(153, 153, 153);">22</li><li style="color: rgb(153, 153, 153);">23</li><li style="color: rgb(153, 153, 153);">24</li><li style="color: rgb(153, 153, 153);">25</li><li style="color: rgb(153, 153, 153);">26</li></ul></pre>
<h6><a id="3_containstext_551"></a>3. :contains(text)</h6>
<p><strong>作用:</strong> 找到包含指定文本内容的指定元素</p>
<pre class="prettyprint"><code class="prism language-html has-numbering" onclick="mdcp.copyCode(event)" style="position: unset;"><span class="token doctype">&lt;!DOCTYPE html&gt;</span>
<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>html</span> <span class="token attr-name">lang</span><span class="token attr-value"><span class="token punctuation">=</span><span class="token punctuation">"</span>en<span class="token punctuation">"</span></span><span class="token punctuation">&gt;</span></span>
<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>head</span><span class="token punctuation">&gt;</span></span>
    <span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>meta</span> <span class="token attr-name">charset</span><span class="token attr-value"><span class="token punctuation">=</span><span class="token punctuation">"</span>UTF-8<span class="token punctuation">"</span></span><span class="token punctuation">&gt;</span></span>
    <span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>title</span><span class="token punctuation">&gt;</span></span>05-jQuery选择器<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>title</span><span class="token punctuation">&gt;</span></span>
    <span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>script</span> <span class="token attr-name">src</span><span class="token attr-value"><span class="token punctuation">=</span><span class="token punctuation">"</span>代码/js/jquery-1.12.4.js<span class="token punctuation">"</span></span><span class="token punctuation">&gt;</span></span><span class="token script language-javascript"></span><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>script</span><span class="token punctuation">&gt;</span></span>
    <span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>script</span><span class="token punctuation">&gt;</span></span><span class="token script language-javascript">
        <span class="token function">$</span><span class="token punctuation">(</span><span class="token keyword">function</span> <span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
            <span class="token comment">// 找到所有div中包含文本内容为lnj的元素</span>
            <span class="token keyword">var</span> $res <span class="token operator">=</span> <span class="token function">$</span><span class="token punctuation">(</span><span class="token string">"div:contains('lnj')"</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
            console<span class="token punctuation">.</span><span class="token function">log</span><span class="token punctuation">(</span>$res<span class="token punctuation">.</span>length<span class="token punctuation">)</span><span class="token punctuation">;</span><span class="token comment">// 找到2个元素</span>
            $res<span class="token punctuation">.</span><span class="token function">each</span><span class="token punctuation">(</span><span class="token keyword">function</span> <span class="token punctuation">(</span>idx<span class="token punctuation">,</span> ele<span class="token punctuation">)</span> <span class="token punctuation">{</span>
                console<span class="token punctuation">.</span><span class="token function">log</span><span class="token punctuation">(</span>idx<span class="token punctuation">,</span> ele<span class="token punctuation">)</span><span class="token punctuation">;</span><span class="token comment">// one,three,four</span>
            <span class="token punctuation">}</span><span class="token punctuation">)</span>
        <span class="token punctuation">}</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
    </span><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>script</span><span class="token punctuation">&gt;</span></span>
<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>head</span><span class="token punctuation">&gt;</span></span>
<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>body</span><span class="token punctuation">&gt;</span></span>
<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>div</span> <span class="token attr-name">class</span><span class="token attr-value"><span class="token punctuation">=</span><span class="token punctuation">"</span>one<span class="token punctuation">"</span></span><span class="token punctuation">&gt;</span></span>lnj<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>div</span><span class="token punctuation">&gt;</span></span>
<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>div</span> <span class="token attr-name">class</span><span class="token attr-value"><span class="token punctuation">=</span><span class="token punctuation">"</span>two<span class="token punctuation">"</span></span><span class="token punctuation">&gt;</span></span>zs<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>div</span><span class="token punctuation">&gt;</span></span>
<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>div</span> <span class="token attr-name">class</span><span class="token attr-value"><span class="token punctuation">=</span><span class="token punctuation">"</span>three<span class="token punctuation">"</span></span><span class="token punctuation">&gt;</span></span>lnj<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>div</span><span class="token punctuation">&gt;</span></span>
<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>div</span> <span class="token attr-name">class</span><span class="token attr-value"><span class="token punctuation">=</span><span class="token punctuation">"</span>four<span class="token punctuation">"</span></span><span class="token punctuation">&gt;</span></span><span class="token comment">&lt;!--子元素中包含该文本也会被找到--&gt;</span>
    <span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>span</span><span class="token punctuation">&gt;</span></span>lnj<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>span</span><span class="token punctuation">&gt;</span></span>
<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>div</span><span class="token punctuation">&gt;</span></span>
<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>span</span> <span class="token attr-name">class</span><span class="token attr-value"><span class="token punctuation">=</span><span class="token punctuation">"</span>five<span class="token punctuation">"</span></span><span class="token punctuation">&gt;</span></span><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>span</span><span class="token punctuation">&gt;</span></span>
<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>body</span><span class="token punctuation">&gt;</span></span>
<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>html</span><span class="token punctuation">&gt;</span></span>
<div class="hljs-button {2}" data-title="复制"></div></code><ul class="pre-numbering" style=""><li style="color: rgb(153, 153, 153);">1</li><li style="color: rgb(153, 153, 153);">2</li><li style="color: rgb(153, 153, 153);">3</li><li style="color: rgb(153, 153, 153);">4</li><li style="color: rgb(153, 153, 153);">5</li><li style="color: rgb(153, 153, 153);">6</li><li style="color: rgb(153, 153, 153);">7</li><li style="color: rgb(153, 153, 153);">8</li><li style="color: rgb(153, 153, 153);">9</li><li style="color: rgb(153, 153, 153);">10</li><li style="color: rgb(153, 153, 153);">11</li><li style="color: rgb(153, 153, 153);">12</li><li style="color: rgb(153, 153, 153);">13</li><li style="color: rgb(153, 153, 153);">14</li><li style="color: rgb(153, 153, 153);">15</li><li style="color: rgb(153, 153, 153);">16</li><li style="color: rgb(153, 153, 153);">17</li><li style="color: rgb(153, 153, 153);">18</li><li style="color: rgb(153, 153, 153);">19</li><li style="color: rgb(153, 153, 153);">20</li><li style="color: rgb(153, 153, 153);">21</li><li style="color: rgb(153, 153, 153);">22</li><li style="color: rgb(153, 153, 153);">23</li><li style="color: rgb(153, 153, 153);">24</li><li style="color: rgb(153, 153, 153);">25</li><li style="color: rgb(153, 153, 153);">26</li><li style="color: rgb(153, 153, 153);">27</li></ul></pre>
<h6><a id="4_hasselector_583"></a>4. :has(selector)</h6>
<p><strong>作用:</strong> 找到包含指定子元素的指定元素<br>
<strong>和:parent区别:</strong> parent只要有子元素就会被找到,:has(selector)不仅要有子元素,而且子元素还必须满足条件</p>
<pre class="prettyprint"><code class="prism language-html has-numbering" onclick="mdcp.copyCode(event)" style="position: unset;"><span class="token doctype">&lt;!DOCTYPE html&gt;</span>
<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>html</span> <span class="token attr-name">lang</span><span class="token attr-value"><span class="token punctuation">=</span><span class="token punctuation">"</span>en<span class="token punctuation">"</span></span><span class="token punctuation">&gt;</span></span>
<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>head</span><span class="token punctuation">&gt;</span></span>
    <span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>meta</span> <span class="token attr-name">charset</span><span class="token attr-value"><span class="token punctuation">=</span><span class="token punctuation">"</span>UTF-8<span class="token punctuation">"</span></span><span class="token punctuation">&gt;</span></span>
    <span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>title</span><span class="token punctuation">&gt;</span></span>05-jQuery选择器<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>title</span><span class="token punctuation">&gt;</span></span>
    <span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>script</span> <span class="token attr-name">src</span><span class="token attr-value"><span class="token punctuation">=</span><span class="token punctuation">"</span>代码/js/jquery-1.12.4.js<span class="token punctuation">"</span></span><span class="token punctuation">&gt;</span></span><span class="token script language-javascript"></span><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>script</span><span class="token punctuation">&gt;</span></span>
    <span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>script</span><span class="token punctuation">&gt;</span></span><span class="token script language-javascript">
        <span class="token function">$</span><span class="token punctuation">(</span><span class="token keyword">function</span> <span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
            <span class="token comment">// 找到所有div中包含后代元素为span的元素</span>
            <span class="token keyword">var</span> $res <span class="token operator">=</span> <span class="token function">$</span><span class="token punctuation">(</span><span class="token string">"div:has('span')"</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
            console<span class="token punctuation">.</span><span class="token function">log</span><span class="token punctuation">(</span>$res<span class="token punctuation">.</span>length<span class="token punctuation">)</span><span class="token punctuation">;</span>
            $res<span class="token punctuation">.</span><span class="token function">each</span><span class="token punctuation">(</span><span class="token keyword">function</span> <span class="token punctuation">(</span>idx<span class="token punctuation">,</span> ele<span class="token punctuation">)</span> <span class="token punctuation">{</span>
                console<span class="token punctuation">.</span><span class="token function">log</span><span class="token punctuation">(</span>idx<span class="token punctuation">,</span> ele<span class="token punctuation">)</span><span class="token punctuation">;</span>
            <span class="token punctuation">}</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
        <span class="token punctuation">}</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
    </span><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>script</span><span class="token punctuation">&gt;</span></span>
<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>head</span><span class="token punctuation">&gt;</span></span>
<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>body</span><span class="token punctuation">&gt;</span></span>
<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>div</span> <span class="token attr-name">class</span><span class="token attr-value"><span class="token punctuation">=</span><span class="token punctuation">"</span>one<span class="token punctuation">"</span></span><span class="token punctuation">&gt;</span></span> <span class="token comment">&lt;!--后代中包含span元素会被找到--&gt;</span>
    <span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>span</span><span class="token punctuation">&gt;</span></span>jjj<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>span</span><span class="token punctuation">&gt;</span></span>
<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>div</span><span class="token punctuation">&gt;</span></span>
<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>div</span> <span class="token attr-name">class</span><span class="token attr-value"><span class="token punctuation">=</span><span class="token punctuation">"</span>two<span class="token punctuation">"</span></span><span class="token punctuation">&gt;</span></span><span class="token comment">&lt;!--后代中不包含span元素不会被找到--&gt;</span>
    <span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>p</span><span class="token punctuation">&gt;</span></span>zs<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>p</span><span class="token punctuation">&gt;</span></span>
<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>div</span><span class="token punctuation">&gt;</span></span>
<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>div</span> <span class="token attr-name">class</span><span class="token attr-value"><span class="token punctuation">=</span><span class="token punctuation">"</span>three<span class="token punctuation">"</span></span><span class="token punctuation">&gt;</span></span><span class="token comment">&lt;!--后代中包含span元素会被找到--&gt;</span>
    <span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>p</span><span class="token punctuation">&gt;</span></span>
        <span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>span</span><span class="token punctuation">&gt;</span></span>lnj<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>span</span><span class="token punctuation">&gt;</span></span>
    <span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>p</span><span class="token punctuation">&gt;</span></span>
<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>div</span><span class="token punctuation">&gt;</span></span>
<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>body</span><span class="token punctuation">&gt;</span></span>
<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>html</span><span class="token punctuation">&gt;</span></span>
<div class="hljs-button {2}" data-title="复制"></div></code><ul class="pre-numbering" style=""><li style="color: rgb(153, 153, 153);">1</li><li style="color: rgb(153, 153, 153);">2</li><li style="color: rgb(153, 153, 153);">3</li><li style="color: rgb(153, 153, 153);">4</li><li style="color: rgb(153, 153, 153);">5</li><li style="color: rgb(153, 153, 153);">6</li><li style="color: rgb(153, 153, 153);">7</li><li style="color: rgb(153, 153, 153);">8</li><li style="color: rgb(153, 153, 153);">9</li><li style="color: rgb(153, 153, 153);">10</li><li style="color: rgb(153, 153, 153);">11</li><li style="color: rgb(153, 153, 153);">12</li><li style="color: rgb(153, 153, 153);">13</li><li style="color: rgb(153, 153, 153);">14</li><li style="color: rgb(153, 153, 153);">15</li><li style="color: rgb(153, 153, 153);">16</li><li style="color: rgb(153, 153, 153);">17</li><li style="color: rgb(153, 153, 153);">18</li><li style="color: rgb(153, 153, 153);">19</li><li style="color: rgb(153, 153, 153);">20</li><li style="color: rgb(153, 153, 153);">21</li><li style="color: rgb(153, 153, 153);">22</li><li style="color: rgb(153, 153, 153);">23</li><li style="color: rgb(153, 153, 153);">24</li><li style="color: rgb(153, 153, 153);">25</li><li style="color: rgb(153, 153, 153);">26</li><li style="color: rgb(153, 153, 153);">27</li><li style="color: rgb(153, 153, 153);">28</li><li style="color: rgb(153, 153, 153);">29</li><li style="color: rgb(153, 153, 153);">30</li><li style="color: rgb(153, 153, 153);">31</li></ul></pre>
<h2><a name="t8"></a><a id="8_jQuery__620"></a>8. jQuery 属性操作</h2>
<h4><a id="1__621"></a>1. 属性与属性节点</h4>
<h6><a id="1_622"></a>1.什么是属性?</h6>
<ul>
<li>对象身上保存的变量就是属性</li>
<li>只要对象身上都可以添加属性(无论是自定义对象,还是DOM对象)</li>
</ul>
<h6><a id="2_626"></a>2.如何操作属性?</h6>
<ul>
<li>添加或修改属性(没有就会添加,有就会修改)
<ul>
<li><strong>对象.属性名称 = 值;</strong></li>
<li><strong>对象[“属性名称”] = 值;</strong></li>
</ul>
</li>
<li>获取属性
<ul>
<li><strong>对象.属性名称;</strong></li>
<li><strong>对象[“属性名称”];</strong></li>
</ul>
</li>
</ul>
<h6><a id="3_634"></a>3.什么是属性节点?</h6>
<ul>
<li>在编写HTML代码时,在HTML标签中添加的属性就是属性节点</li>
<li>在浏览器中找到span这个DOM元素之后, 展开看到的都是属性</li>
<li>在attributes属性中保存的所有内容都是属性节点</li>
</ul>
<pre class="prettyprint"><code class="prism language-html has-numbering" onclick="mdcp.copyCode(event)" style="position: unset;">&lt;span class= "box" nj="123"&gt;<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>span</span><span class="token punctuation">&gt;</span></span> // 这里的class和nj就是属性节点
<div class="hljs-button {2}" data-title="复制"></div></code><ul class="pre-numbering" style=""><li style="color: rgb(153, 153, 153);">1</li></ul></pre>
<h6><a id="4_642"></a>4.如何操作属性节点?</h6>
<ul>
<li>获取属性节点
<ul>
<li>DOM元素.getAttribute(“属性名称”);</li>
</ul>
</li>
<li>设置属性节点
<ul>
<li>DOM元素.setAttribute(“属性名称”, “值”);</li>
</ul>
</li>
</ul>
<h6><a id="5_648"></a>5.属性和属性节点有什么区别?</h6>
<p><strong>任何对象都有属性, 但是只有DOM对象才有属性节点</strong></p>
<h4><a id="2__651"></a>2. 属性节点方法</h4>
<h6><a id="1_attr__652"></a>1. attr 方法</h6>
<p><strong>作用:</strong> 获取或者设置属性节点的值</p>
<ul>
<li>可以传递一个参数, 也可以传递两个参数</li>
<li>如果传递一个参数, 代表获取属性节点的值</li>
<li>如果传递两个参数, 代表设置属性节点的值</li>
</ul>
<p><strong>注意点:</strong></p>
<ul>
<li>如果是获取:无论找到多少个元素, 都只会返回第一个元素指定的属性节点的值</li>
<li>如果是设置:找到多少个元素就会设置多少个元素</li>
<li>如果是设置: 如果设置的属性节点不存在, 那么系统会自动新增</li>
</ul>
<pre class="prettyprint"><code class="prism language-html has-numbering" onclick="mdcp.copyCode(event)" style="position: unset;"><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>script</span><span class="token punctuation">&gt;</span></span><span class="token script language-javascript">
   <span class="token function">$</span><span class="token punctuation">(</span><span class="token keyword">function</span> <span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
       <span class="token comment">// 1.获取指定属性节点值</span>
       <span class="token keyword">var</span> $res <span class="token operator">=</span> <span class="token function">$</span><span class="token punctuation">(</span><span class="token string">".span1"</span><span class="token punctuation">)</span><span class="token punctuation">.</span><span class="token function">attr</span><span class="token punctuation">(</span><span class="token string">"nj"</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
       console<span class="token punctuation">.</span><span class="token function">log</span><span class="token punctuation">(</span>$res<span class="token punctuation">)</span><span class="token punctuation">;</span>
       <span class="token comment">// 2.设置属性节点</span>
       <span class="token function">$</span><span class="token punctuation">(</span><span class="token string">".span1"</span><span class="token punctuation">)</span><span class="token punctuation">.</span><span class="token function">attr</span><span class="token punctuation">(</span><span class="token string">"nj"</span><span class="token punctuation">,</span> <span class="token string">"666"</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
       <span class="token function">$</span><span class="token punctuation">(</span><span class="token string">".span2"</span><span class="token punctuation">)</span><span class="token punctuation">.</span><span class="token function">attr</span><span class="token punctuation">(</span><span class="token string">"id"</span><span class="token punctuation">,</span> <span class="token string">"box1 box2"</span><span class="token punctuation">)</span><span class="token punctuation">;</span>

       <span class="token comment">// 3.注意点:</span>
       <span class="token comment">// 3.1.获取属性节点时,只会获取找到所有元素中第一个元素的属性节点</span>
       $res <span class="token operator">=</span> <span class="token function">$</span><span class="token punctuation">(</span><span class="token string">"span"</span><span class="token punctuation">)</span><span class="token punctuation">.</span><span class="token function">attr</span><span class="token punctuation">(</span><span class="token string">"class"</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
       console<span class="token punctuation">.</span><span class="token function">log</span><span class="token punctuation">(</span>$res<span class="token punctuation">)</span><span class="token punctuation">;</span>
        <span class="token function">$</span><span class="token punctuation">(</span><span class="token string">"span"</span><span class="token punctuation">)</span><span class="token punctuation">.</span><span class="token function">attr</span><span class="token punctuation">(</span><span class="token string">"class"</span><span class="token punctuation">,</span> <span class="token string">"lnj"</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
   <span class="token punctuation">}</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
</span><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>script</span><span class="token punctuation">&gt;</span></span>
<div class="hljs-button {2}" data-title="复制"></div></code><ul class="pre-numbering" style=""><li style="color: rgb(153, 153, 153);">1</li><li style="color: rgb(153, 153, 153);">2</li><li style="color: rgb(153, 153, 153);">3</li><li style="color: rgb(153, 153, 153);">4</li><li style="color: rgb(153, 153, 153);">5</li><li style="color: rgb(153, 153, 153);">6</li><li style="color: rgb(153, 153, 153);">7</li><li style="color: rgb(153, 153, 153);">8</li><li style="color: rgb(153, 153, 153);">9</li><li style="color: rgb(153, 153, 153);">10</li><li style="color: rgb(153, 153, 153);">11</li><li style="color: rgb(153, 153, 153);">12</li><li style="color: rgb(153, 153, 153);">13</li><li style="color: rgb(153, 153, 153);">14</li><li style="color: rgb(153, 153, 153);">15</li><li style="color: rgb(153, 153, 153);">16</li></ul></pre>
<h6><a id="2_removeAttr__680"></a>2. removeAttr 方法</h6>
<p><strong>作用:</strong> 删除属性节点</p>
<p><strong>注意点:</strong></p>
<ul>
<li>会删除所有找到元素指定的属性节点</li>
</ul>
<pre class="prettyprint"><code class="prism language-html has-numbering" onclick="mdcp.copyCode(event)" style="position: unset;"><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>script</span><span class="token punctuation">&gt;</span></span><span class="token script language-javascript">
   <span class="token function">$</span><span class="token punctuation">(</span><span class="token keyword">function</span> <span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
       <span class="token comment">// 1.设置属性节点时,会给所有找到元素设置属性节点</span>
       <span class="token function">$</span><span class="token punctuation">(</span><span class="token string">"span"</span><span class="token punctuation">)</span><span class="token punctuation">.</span><span class="token function">attr</span><span class="token punctuation">(</span><span class="token string">"test"</span><span class="token punctuation">,</span> <span class="token string">"jonathan"</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
       <span class="token comment">// 2.删除属性节点时,会删除所有找到元素的属性节点</span>
       <span class="token function">$</span><span class="token punctuation">(</span><span class="token string">"span"</span><span class="token punctuation">)</span><span class="token punctuation">.</span><span class="token function">removeAttr</span><span class="token punctuation">(</span><span class="token string">"test"</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
   <span class="token punctuation">}</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
</span><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>script</span><span class="token punctuation">&gt;</span></span>
<div class="hljs-button {2}" data-title="复制"></div></code><ul class="pre-numbering" style=""><li style="color: rgb(153, 153, 153);">1</li><li style="color: rgb(153, 153, 153);">2</li><li style="color: rgb(153, 153, 153);">3</li><li style="color: rgb(153, 153, 153);">4</li><li style="color: rgb(153, 153, 153);">5</li><li style="color: rgb(153, 153, 153);">6</li><li style="color: rgb(153, 153, 153);">7</li><li style="color: rgb(153, 153, 153);">8</li></ul></pre>
<h6><a id="3_prop__695"></a>3. prop 方法</h6>
<p><strong>作用:</strong> 设置或者获取元素的属性值<br>
<strong>注意点:</strong></p>
<ul>
<li>prop方法不仅能够操作属性, 他还能操作属性节点</li>
<li>官方推荐在操作属性节点时,具有 true 和 false 两个属性的属性节点，如 checked, selected 或者 disabled 使用prop()，其他的使用 attr()</li>
</ul>
<pre class="prettyprint"><code class="prism language-html has-numbering" onclick="mdcp.copyCode(event)" style="position: unset;"><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>script</span><span class="token punctuation">&gt;</span></span><span class="token script language-javascript">
   <span class="token function">$</span><span class="token punctuation">(</span><span class="token keyword">function</span> <span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
       <span class="token comment">// 1.设置属性</span>
       <span class="token comment">// 1.1.设置属性时,会设置所有找到元素的属性</span>
       <span class="token function">$</span><span class="token punctuation">(</span><span class="token string">"span"</span><span class="token punctuation">)</span><span class="token punctuation">.</span><span class="token function">prop</span><span class="token punctuation">(</span><span class="token string">"demo"</span><span class="token punctuation">,</span> <span class="token string">"lnj"</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
       <span class="token comment">// 2.获取属性</span>
       <span class="token comment">// 2.1.获取属性时,只会获取找到第一个元素的属性</span>
       console<span class="token punctuation">.</span><span class="token function">log</span><span class="token punctuation">(</span><span class="token function">$</span><span class="token punctuation">(</span><span class="token string">"span"</span><span class="token punctuation">)</span><span class="token punctuation">.</span><span class="token function">prop</span><span class="token punctuation">(</span><span class="token string">"demo"</span><span class="token punctuation">)</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
   <span class="token punctuation">}</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
</span><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>script</span><span class="token punctuation">&gt;</span></span>
<div class="hljs-button {2}" data-title="复制"></div></code><ul class="pre-numbering" style=""><li style="color: rgb(153, 153, 153);">1</li><li style="color: rgb(153, 153, 153);">2</li><li style="color: rgb(153, 153, 153);">3</li><li style="color: rgb(153, 153, 153);">4</li><li style="color: rgb(153, 153, 153);">5</li><li style="color: rgb(153, 153, 153);">6</li><li style="color: rgb(153, 153, 153);">7</li><li style="color: rgb(153, 153, 153);">8</li><li style="color: rgb(153, 153, 153);">9</li><li style="color: rgb(153, 153, 153);">10</li></ul></pre>
<h6><a id="4_removeProp__712"></a>4. removeProp 方法</h6>
<pre class="prettyprint"><code class="prism language-html has-numbering" onclick="mdcp.copyCode(event)" style="position: unset;"><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>script</span><span class="token punctuation">&gt;</span></span><span class="token script language-javascript">
        <span class="token function">$</span><span class="token punctuation">(</span><span class="token keyword">function</span> <span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
            <span class="token comment">// 删除所有找到元素的demo属性</span>
            <span class="token function">$</span><span class="token punctuation">(</span><span class="token string">"span"</span><span class="token punctuation">)</span><span class="token punctuation">.</span><span class="token function">removeProp</span><span class="token punctuation">(</span><span class="token string">"demo"</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
        <span class="token punctuation">}</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
</span><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>script</span><span class="token punctuation">&gt;</span></span>
<div class="hljs-button {2}" data-title="复制"></div></code><ul class="pre-numbering" style=""><li style="color: rgb(153, 153, 153);">1</li><li style="color: rgb(153, 153, 153);">2</li><li style="color: rgb(153, 153, 153);">3</li><li style="color: rgb(153, 153, 153);">4</li><li style="color: rgb(153, 153, 153);">5</li><li style="color: rgb(153, 153, 153);">6</li></ul></pre>
<h6><a id="5_attrprop_721"></a>5. attr方法和prop方法区别</h6>
<ul>
<li>既然所有的DOM对象，都有一个attributes属性,而prop可以操作属性,所以也可以操作属性节点</li>
<li>官方推荐在操作属性节点时,具有 true 和 false 两个属性的属性节点，如 checked, selected 或者 disabled 使用prop()，其他的使用 attr()</li>
<li>因为如果具有 true 和 false 两个属性的属性节点,如果没有编写默认attr返回undefined,而prop返回false</li>
</ul>
<pre class="prettyprint"><code class="prism language-html has-numbering" onclick="mdcp.copyCode(event)" style="position: unset;"><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>script</span><span class="token punctuation">&gt;</span></span><span class="token script language-javascript">
     <span class="token function">$</span><span class="token punctuation">(</span><span class="token keyword">function</span> <span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
         <span class="token comment">// 1.可以通过prop获取属性节点</span>
         console<span class="token punctuation">.</span><span class="token function">log</span><span class="token punctuation">(</span><span class="token function">$</span><span class="token punctuation">(</span><span class="token string">"input"</span><span class="token punctuation">)</span><span class="token punctuation">.</span><span class="token function">prop</span><span class="token punctuation">(</span><span class="token string">"class"</span><span class="token punctuation">)</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
         <span class="token comment">// 2.可以通过prop设置属性节点</span>
         <span class="token function">$</span><span class="token punctuation">(</span><span class="token string">"input"</span><span class="token punctuation">)</span><span class="token punctuation">.</span><span class="token function">prop</span><span class="token punctuation">(</span><span class="token string">"class"</span><span class="token punctuation">,</span> <span class="token string">"tag"</span><span class="token punctuation">)</span><span class="token punctuation">;</span>

         <span class="token comment">// 3.如果没有默认值,那么attr获取返回undefined</span>
         <span class="token comment">//console.log($("input[type=checkbox]").attr("checked"));</span>
         <span class="token comment">// 4.如果没有默认值,那么prop获取返回false</span>
         console<span class="token punctuation">.</span><span class="token function">log</span><span class="token punctuation">(</span><span class="token function">$</span><span class="token punctuation">(</span><span class="token string">"input[type=checkbox]"</span><span class="token punctuation">)</span><span class="token punctuation">.</span><span class="token function">prop</span><span class="token punctuation">(</span><span class="token string">"checked"</span><span class="token punctuation">)</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
         <span class="token comment">// 5.通过attr设置选中</span>
         <span class="token comment">//$("input[type=checkbox]").attr("checked", true);</span>
         
         <span class="token comment">// 6.通过prop设置选中</span>
         <span class="token function">$</span><span class="token punctuation">(</span><span class="token string">"input[type=checkbox]"</span><span class="token punctuation">)</span><span class="token punctuation">.</span><span class="token function">prop</span><span class="token punctuation">(</span><span class="token string">"checked"</span><span class="token punctuation">,</span> <span class="token boolean">true</span><span class="token punctuation">)</span>

     <span class="token punctuation">}</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
</span><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>script</span><span class="token punctuation">&gt;</span></span>
<div class="hljs-button {2}" data-title="复制"></div></code><ul class="pre-numbering" style=""><li style="color: rgb(153, 153, 153);">1</li><li style="color: rgb(153, 153, 153);">2</li><li style="color: rgb(153, 153, 153);">3</li><li style="color: rgb(153, 153, 153);">4</li><li style="color: rgb(153, 153, 153);">5</li><li style="color: rgb(153, 153, 153);">6</li><li style="color: rgb(153, 153, 153);">7</li><li style="color: rgb(153, 153, 153);">8</li><li style="color: rgb(153, 153, 153);">9</li><li style="color: rgb(153, 153, 153);">10</li><li style="color: rgb(153, 153, 153);">11</li><li style="color: rgb(153, 153, 153);">12</li><li style="color: rgb(153, 153, 153);">13</li><li style="color: rgb(153, 153, 153);">14</li><li style="color: rgb(153, 153, 153);">15</li><li style="color: rgb(153, 153, 153);">16</li><li style="color: rgb(153, 153, 153);">17</li><li style="color: rgb(153, 153, 153);">18</li><li style="color: rgb(153, 153, 153);">19</li></ul></pre>
<h2><a name="t9"></a><a id="9_jQuery_Class__746"></a>9. jQuery Class 操作</h2>
<h4><a id="1_jQuery_Class__747"></a>1. jQuery Class 类操作</h4>
<p><strong>jQuery CSS类相关方法都是用于操作DOM对象的class属性节点的值</strong></p>
<h6><a id="1_addClass_749"></a>1. addClass</h6>
<ul>
<li>给元素添加一个或多个类</li>
<li>如果要添加多个, 多个类名之间用空格隔开即可</li>
</ul>
<pre class="prettyprint"><code class="prism language-html has-numbering" onclick="mdcp.copyCode(event)" style="position: unset;"><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>script</span><span class="token punctuation">&gt;</span></span><span class="token script language-javascript">
<span class="token function">$</span><span class="token punctuation">(</span><span class="token keyword">function</span> <span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
    <span class="token function">$</span><span class="token punctuation">(</span><span class="token string">"button"</span><span class="token punctuation">)</span><span class="token punctuation">.</span><span class="token function">eq</span><span class="token punctuation">(</span><span class="token number">0</span><span class="token punctuation">)</span><span class="token punctuation">.</span><span class="token function">click</span><span class="token punctuation">(</span><span class="token keyword">function</span> <span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
        <span class="token comment">// 1.添加一个类</span>
        <span class="token comment">//$("div").addClass("class1");</span>
        <span class="token comment">// 2.再添加一个类</span>
        <span class="token comment">//$("div").addClass("class2");</span>
        <span class="token comment">// 3.一次性添加多个类(用空格隔开)</span>
        <span class="token function">$</span><span class="token punctuation">(</span><span class="token string">"div"</span><span class="token punctuation">)</span><span class="token punctuation">.</span><span class="token function">addClass</span><span class="token punctuation">(</span><span class="token string">"class1 class2"</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
    <span class="token punctuation">}</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
<span class="token punctuation">}</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
</span><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>script</span><span class="token punctuation">&gt;</span></span>
<div class="hljs-button {2}" data-title="复制"></div></code><ul class="pre-numbering" style=""><li style="color: rgb(153, 153, 153);">1</li><li style="color: rgb(153, 153, 153);">2</li><li style="color: rgb(153, 153, 153);">3</li><li style="color: rgb(153, 153, 153);">4</li><li style="color: rgb(153, 153, 153);">5</li><li style="color: rgb(153, 153, 153);">6</li><li style="color: rgb(153, 153, 153);">7</li><li style="color: rgb(153, 153, 153);">8</li><li style="color: rgb(153, 153, 153);">9</li><li style="color: rgb(153, 153, 153);">10</li><li style="color: rgb(153, 153, 153);">11</li><li style="color: rgb(153, 153, 153);">12</li></ul></pre>
<h6><a id="2_removeClass_766"></a>2. removeClass</h6>
<ul>
<li>删除元素的一个或多个类</li>
<li>如果想删除多个, 多个类名之间用空格隔开即可</li>
</ul>
<pre class="prettyprint"><code class="prism language-html has-numbering" onclick="mdcp.copyCode(event)" style="position: unset;"><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>script</span><span class="token punctuation">&gt;</span></span><span class="token script language-javascript">
    <span class="token function">$</span><span class="token punctuation">(</span><span class="token keyword">function</span> <span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
        <span class="token function">$</span><span class="token punctuation">(</span><span class="token string">"button"</span><span class="token punctuation">)</span><span class="token punctuation">.</span><span class="token function">eq</span><span class="token punctuation">(</span><span class="token number">1</span><span class="token punctuation">)</span><span class="token punctuation">.</span><span class="token function">click</span><span class="token punctuation">(</span><span class="token keyword">function</span> <span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
            <span class="token comment">// 4.删除一个类</span>
            <span class="token comment">//$("div").removeClass("class2");</span>
            <span class="token comment">// 5.再删除一个类</span>
            <span class="token comment">//$("div").removeClass("class1");</span>
            <span class="token comment">// 6.一次性删除多个类(用空格隔开)</span>
            <span class="token function">$</span><span class="token punctuation">(</span><span class="token string">"div"</span><span class="token punctuation">)</span><span class="token punctuation">.</span><span class="token function">removeClass</span><span class="token punctuation">(</span><span class="token string">"class1 class2"</span><span class="token punctuation">)</span><span class="token punctuation">;</span>

        <span class="token punctuation">}</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
    <span class="token punctuation">}</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
</span><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>script</span><span class="token punctuation">&gt;</span></span>
<div class="hljs-button {2}" data-title="复制"></div></code><ul class="pre-numbering" style=""><li style="color: rgb(153, 153, 153);">1</li><li style="color: rgb(153, 153, 153);">2</li><li style="color: rgb(153, 153, 153);">3</li><li style="color: rgb(153, 153, 153);">4</li><li style="color: rgb(153, 153, 153);">5</li><li style="color: rgb(153, 153, 153);">6</li><li style="color: rgb(153, 153, 153);">7</li><li style="color: rgb(153, 153, 153);">8</li><li style="color: rgb(153, 153, 153);">9</li><li style="color: rgb(153, 153, 153);">10</li><li style="color: rgb(153, 153, 153);">11</li><li style="color: rgb(153, 153, 153);">12</li><li style="color: rgb(153, 153, 153);">13</li></ul></pre>
<h6><a id="3_toggleClass_784"></a>3. toggleClass</h6>
<ul>
<li>切换类</li>
<li>添加或删除一个类(存在就删除不存在就添加)</li>
</ul>
<pre class="prettyprint"><code class="prism language-html has-numbering" onclick="mdcp.copyCode(event)" style="position: unset;"><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>script</span><span class="token punctuation">&gt;</span></span><span class="token script language-javascript">
    <span class="token function">$</span><span class="token punctuation">(</span><span class="token keyword">function</span> <span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
        <span class="token function">$</span><span class="token punctuation">(</span><span class="token string">"button"</span><span class="token punctuation">)</span><span class="token punctuation">.</span><span class="token function">eq</span><span class="token punctuation">(</span><span class="token number">2</span><span class="token punctuation">)</span><span class="token punctuation">.</span><span class="token function">click</span><span class="token punctuation">(</span><span class="token keyword">function</span> <span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
            <span class="token comment">// 7.切换一个类</span>
            <span class="token comment">//$("div").toggleClass("class2");</span>
            <span class="token comment">// 8.切换多个类</span>
            <span class="token function">$</span><span class="token punctuation">(</span><span class="token string">"div"</span><span class="token punctuation">)</span><span class="token punctuation">.</span><span class="token function">toggleClass</span><span class="token punctuation">(</span><span class="token string">"class1 class2"</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
        <span class="token punctuation">}</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
    <span class="token punctuation">}</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
</span><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>script</span><span class="token punctuation">&gt;</span></span>
<div class="hljs-button {2}" data-title="复制"></div></code><ul class="pre-numbering" style=""><li style="color: rgb(153, 153, 153);">1</li><li style="color: rgb(153, 153, 153);">2</li><li style="color: rgb(153, 153, 153);">3</li><li style="color: rgb(153, 153, 153);">4</li><li style="color: rgb(153, 153, 153);">5</li><li style="color: rgb(153, 153, 153);">6</li><li style="color: rgb(153, 153, 153);">7</li><li style="color: rgb(153, 153, 153);">8</li><li style="color: rgb(153, 153, 153);">9</li><li style="color: rgb(153, 153, 153);">10</li></ul></pre>
<h4><a id="2_jQuery__800"></a>2. jQuery 文本值操作</h4>
<h6><a id="1_html_801"></a>1. html</h6>
<ul>
<li>添加或获取元素中的HTML</li>
</ul>
<pre class="prettyprint"><code class="prism language-html has-numbering" onclick="mdcp.copyCode(event)" style="position: unset;"><span class="token doctype">&lt;!DOCTYPE html&gt;</span>
<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>html</span> <span class="token attr-name">lang</span><span class="token attr-value"><span class="token punctuation">=</span><span class="token punctuation">"</span>en<span class="token punctuation">"</span></span><span class="token punctuation">&gt;</span></span>
<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>head</span><span class="token punctuation">&gt;</span></span>
    <span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>meta</span> <span class="token attr-name">charset</span><span class="token attr-value"><span class="token punctuation">=</span><span class="token punctuation">"</span>UTF-8<span class="token punctuation">"</span></span><span class="token punctuation">&gt;</span></span>
    <span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>title</span><span class="token punctuation">&gt;</span></span>09-jQuery代码文本值<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>title</span><span class="token punctuation">&gt;</span></span>
    <span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>script</span> <span class="token attr-name">src</span><span class="token attr-value"><span class="token punctuation">=</span><span class="token punctuation">"</span>代码/js/jquery-1.12.4.js<span class="token punctuation">"</span></span><span class="token punctuation">&gt;</span></span><span class="token script language-javascript"></span><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>script</span><span class="token punctuation">&gt;</span></span>
    <span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>script</span><span class="token punctuation">&gt;</span></span><span class="token script language-javascript">
        <span class="token function">$</span><span class="token punctuation">(</span><span class="token keyword">function</span> <span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
            <span class="token keyword">var</span> $btns <span class="token operator">=</span> <span class="token function">$</span><span class="token punctuation">(</span><span class="token string">"button"</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
            <span class="token keyword">var</span> $div <span class="token operator">=</span> <span class="token function">$</span><span class="token punctuation">(</span><span class="token string">"div"</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
            $btns<span class="token punctuation">.</span><span class="token function">eq</span><span class="token punctuation">(</span><span class="token number">0</span><span class="token punctuation">)</span><span class="token punctuation">.</span><span class="token function">click</span><span class="token punctuation">(</span><span class="token keyword">function</span> <span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
                <span class="token comment">// 1.添加html, 相当于innerHTML</span>
                <span class="token comment">//$div.html("&lt;p&gt;我是p标签&lt;/p&gt;");</span>
                <span class="token comment">//$div.html("&lt;p&gt;&lt;span&gt;我是span标签&lt;/span&gt;&lt;/p&gt;");</span>
                $div<span class="token punctuation">.</span><span class="token function">html</span><span class="token punctuation">(</span><span class="token string">"我是文本"</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
            <span class="token punctuation">}</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
            $btns<span class="token punctuation">.</span><span class="token function">eq</span><span class="token punctuation">(</span><span class="token number">1</span><span class="token punctuation">)</span><span class="token punctuation">.</span><span class="token function">click</span><span class="token punctuation">(</span><span class="token keyword">function</span> <span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
                <span class="token comment">// 2.获取html</span>
                console<span class="token punctuation">.</span><span class="token function">log</span><span class="token punctuation">(</span>$div<span class="token punctuation">.</span><span class="token function">html</span><span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
            <span class="token punctuation">}</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
        <span class="token punctuation">}</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
    </span><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>script</span><span class="token punctuation">&gt;</span></span>
<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>head</span><span class="token punctuation">&gt;</span></span>
<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>body</span><span class="token punctuation">&gt;</span></span>
    <span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>button</span><span class="token punctuation">&gt;</span></span>添加html<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>button</span><span class="token punctuation">&gt;</span></span>
    <span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>button</span><span class="token punctuation">&gt;</span></span>获取html<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>button</span><span class="token punctuation">&gt;</span></span>
    <span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>button</span><span class="token punctuation">&gt;</span></span>添加文本<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>button</span><span class="token punctuation">&gt;</span></span>
    <span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>button</span><span class="token punctuation">&gt;</span></span>获取文本<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>button</span><span class="token punctuation">&gt;</span></span>
    <span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>div</span><span class="token punctuation">&gt;</span></span><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>div</span><span class="token punctuation">&gt;</span></span>
<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>body</span><span class="token punctuation">&gt;</span></span>
<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>html</span><span class="token punctuation">&gt;</span></span>
<div class="hljs-button {2}" data-title="复制"></div></code><ul class="pre-numbering" style=""><li style="color: rgb(153, 153, 153);">1</li><li style="color: rgb(153, 153, 153);">2</li><li style="color: rgb(153, 153, 153);">3</li><li style="color: rgb(153, 153, 153);">4</li><li style="color: rgb(153, 153, 153);">5</li><li style="color: rgb(153, 153, 153);">6</li><li style="color: rgb(153, 153, 153);">7</li><li style="color: rgb(153, 153, 153);">8</li><li style="color: rgb(153, 153, 153);">9</li><li style="color: rgb(153, 153, 153);">10</li><li style="color: rgb(153, 153, 153);">11</li><li style="color: rgb(153, 153, 153);">12</li><li style="color: rgb(153, 153, 153);">13</li><li style="color: rgb(153, 153, 153);">14</li><li style="color: rgb(153, 153, 153);">15</li><li style="color: rgb(153, 153, 153);">16</li><li style="color: rgb(153, 153, 153);">17</li><li style="color: rgb(153, 153, 153);">18</li><li style="color: rgb(153, 153, 153);">19</li><li style="color: rgb(153, 153, 153);">20</li><li style="color: rgb(153, 153, 153);">21</li><li style="color: rgb(153, 153, 153);">22</li><li style="color: rgb(153, 153, 153);">23</li><li style="color: rgb(153, 153, 153);">24</li><li style="color: rgb(153, 153, 153);">25</li><li style="color: rgb(153, 153, 153);">26</li><li style="color: rgb(153, 153, 153);">27</li><li style="color: rgb(153, 153, 153);">28</li><li style="color: rgb(153, 153, 153);">29</li><li style="color: rgb(153, 153, 153);">30</li><li style="color: rgb(153, 153, 153);">31</li></ul></pre>
<h6><a id="2_text_836"></a>2. text</h6>
<ul>
<li>添加或获取元素中的文本</li>
<li>text方法能做的html方法都能做,所以一般使用html方法即可</li>
</ul>
<pre class="prettyprint"><code class="prism language-html has-numbering" onclick="mdcp.copyCode(event)" style="position: unset;"><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>script</span><span class="token punctuation">&gt;</span></span><span class="token script language-javascript">
   <span class="token function">$</span><span class="token punctuation">(</span><span class="token keyword">function</span> <span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
       $btns<span class="token punctuation">.</span><span class="token function">eq</span><span class="token punctuation">(</span><span class="token number">2</span><span class="token punctuation">)</span><span class="token punctuation">.</span><span class="token function">click</span><span class="token punctuation">(</span><span class="token keyword">function</span> <span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
           <span class="token comment">// 3.添加文本, 相当于innerText</span>
           <span class="token comment">// 如下内容不会被转换为标签</span>
           <span class="token comment">// $div.text('&lt;p&gt;我是段落&lt;/p&gt;');</span>
          $div<span class="token punctuation">.</span><span class="token function">text</span><span class="token punctuation">(</span><span class="token string">'我是文本'</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
       <span class="token punctuation">}</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
       $btns<span class="token punctuation">.</span><span class="token function">eq</span><span class="token punctuation">(</span><span class="token number">3</span><span class="token punctuation">)</span><span class="token punctuation">.</span><span class="token function">click</span><span class="token punctuation">(</span><span class="token keyword">function</span> <span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
           <span class="token comment">// 4.获取文本</span>
           console<span class="token punctuation">.</span><span class="token function">log</span><span class="token punctuation">(</span>$div<span class="token punctuation">.</span><span class="token function">text</span><span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
       <span class="token punctuation">}</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
</span><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>script</span><span class="token punctuation">&gt;</span></span>
<div class="hljs-button {2}" data-title="复制"></div></code><ul class="pre-numbering" style=""><li style="color: rgb(153, 153, 153);">1</li><li style="color: rgb(153, 153, 153);">2</li><li style="color: rgb(153, 153, 153);">3</li><li style="color: rgb(153, 153, 153);">4</li><li style="color: rgb(153, 153, 153);">5</li><li style="color: rgb(153, 153, 153);">6</li><li style="color: rgb(153, 153, 153);">7</li><li style="color: rgb(153, 153, 153);">8</li><li style="color: rgb(153, 153, 153);">9</li><li style="color: rgb(153, 153, 153);">10</li><li style="color: rgb(153, 153, 153);">11</li><li style="color: rgb(153, 153, 153);">12</li><li style="color: rgb(153, 153, 153);">13</li></ul></pre>
<h6><a id="3_val_854"></a>3. val</h6>
<ul>
<li>添加或获取元素value属性的值</li>
</ul>
<pre class="prettyprint"><code class="prism language-html has-numbering" onclick="mdcp.copyCode(event)" style="position: unset;"><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>script</span><span class="token punctuation">&gt;</span></span><span class="token script language-javascript">
    <span class="token function">$</span><span class="token punctuation">(</span><span class="token keyword">function</span> <span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
        $btns<span class="token punctuation">.</span><span class="token function">eq</span><span class="token punctuation">(</span><span class="token number">4</span><span class="token punctuation">)</span><span class="token punctuation">.</span><span class="token function">click</span><span class="token punctuation">(</span><span class="token keyword">function</span> <span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
            <span class="token comment">// 4.添加value值</span>
            <span class="token function">$</span><span class="token punctuation">(</span><span class="token string">"input"</span><span class="token punctuation">)</span><span class="token punctuation">.</span><span class="token function">val</span><span class="token punctuation">(</span><span class="token string">"我是一个输入框"</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
        <span class="token punctuation">}</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
        $btns<span class="token punctuation">.</span><span class="token function">eq</span><span class="token punctuation">(</span><span class="token number">5</span><span class="token punctuation">)</span><span class="token punctuation">.</span><span class="token function">click</span><span class="token punctuation">(</span><span class="token keyword">function</span> <span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
            <span class="token comment">// 4.获取value值</span>
            console<span class="token punctuation">.</span><span class="token function">log</span><span class="token punctuation">(</span><span class="token function">$</span><span class="token punctuation">(</span><span class="token string">"input"</span><span class="token punctuation">)</span><span class="token punctuation">.</span><span class="token function">val</span><span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
        <span class="token punctuation">}</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
    <span class="token punctuation">}</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
</span><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>script</span><span class="token punctuation">&gt;</span></span>
<div class="hljs-button {2}" data-title="复制"></div></code><ul class="pre-numbering" style=""><li style="color: rgb(153, 153, 153);">1</li><li style="color: rgb(153, 153, 153);">2</li><li style="color: rgb(153, 153, 153);">3</li><li style="color: rgb(153, 153, 153);">4</li><li style="color: rgb(153, 153, 153);">5</li><li style="color: rgb(153, 153, 153);">6</li><li style="color: rgb(153, 153, 153);">7</li><li style="color: rgb(153, 153, 153);">8</li><li style="color: rgb(153, 153, 153);">9</li><li style="color: rgb(153, 153, 153);">10</li><li style="color: rgb(153, 153, 153);">11</li><li style="color: rgb(153, 153, 153);">12</li></ul></pre>
<h4><a id="3_jQuery_CSS__871"></a>3. jQuery CSS 样式</h4>
<h6><a id="1_css__872"></a>1. css 方法</h6>
<ul>
<li>设置或获取元素CSS样式</li>
<li>格式1:DOM元素.css(“样式名称”, “值”);</li>
<li>格式2:DOM元素.css({“样式名称1”:“值1”,“样式名称2”:“值2”});</li>
</ul>
<pre class="prettyprint"><code class="prism language-html has-numbering" onclick="mdcp.copyCode(event)" style="position: unset;"><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>script</span><span class="token punctuation">&gt;</span></span><span class="token script language-javascript">
     <span class="token function">$</span><span class="token punctuation">(</span><span class="token keyword">function</span> <span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
         <span class="token function">$</span><span class="token punctuation">(</span><span class="token string">"button"</span><span class="token punctuation">)</span><span class="token punctuation">.</span><span class="token function">click</span><span class="token punctuation">(</span><span class="token keyword">function</span> <span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
            <span class="token comment">// 1.单个样式设置</span>
            <span class="token function">$</span><span class="token punctuation">(</span><span class="token string">"div"</span><span class="token punctuation">)</span><span class="token punctuation">.</span><span class="token function">css</span><span class="token punctuation">(</span><span class="token string">"width"</span><span class="token punctuation">,</span> <span class="token string">"100px"</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
            <span class="token function">$</span><span class="token punctuation">(</span><span class="token string">"div"</span><span class="token punctuation">)</span><span class="token punctuation">.</span><span class="token function">css</span><span class="token punctuation">(</span><span class="token string">"height"</span><span class="token punctuation">,</span> <span class="token string">"100px"</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
            <span class="token function">$</span><span class="token punctuation">(</span><span class="token string">"div"</span><span class="token punctuation">)</span><span class="token punctuation">.</span><span class="token function">css</span><span class="token punctuation">(</span><span class="token string">"background"</span><span class="token punctuation">,</span> <span class="token string">"red"</span><span class="token punctuation">)</span><span class="token punctuation">;</span>

             <span class="token comment">// 2.链式设置样式</span>
             <span class="token function">$</span><span class="token punctuation">(</span><span class="token string">"div"</span><span class="token punctuation">)</span><span class="token punctuation">.</span><span class="token function">css</span><span class="token punctuation">(</span><span class="token string">"width"</span><span class="token punctuation">,</span> <span class="token string">"100px"</span><span class="token punctuation">)</span><span class="token punctuation">.</span><span class="token function">css</span><span class="token punctuation">(</span><span class="token string">"height"</span><span class="token punctuation">,</span> <span class="token string">"100px"</span><span class="token punctuation">)</span><span class="token punctuation">.</span><span class="token function">css</span><span class="token punctuation">(</span><span class="token string">"background"</span><span class="token punctuation">,</span> <span class="token string">"red"</span><span class="token punctuation">)</span><span class="token punctuation">;</span>

             <span class="token comment">// 3.传入对象一次性设置样式</span>
             <span class="token function">$</span><span class="token punctuation">(</span><span class="token string">"div"</span><span class="token punctuation">)</span><span class="token punctuation">.</span><span class="token function">css</span><span class="token punctuation">(</span><span class="token punctuation">{</span>
                <span class="token string">"width"</span><span class="token punctuation">:</span><span class="token string">"100px"</span><span class="token punctuation">,</span>
                 <span class="token string">"height"</span><span class="token punctuation">:</span><span class="token string">"100px"</span><span class="token punctuation">,</span>
                 <span class="token string">"background"</span><span class="token punctuation">:</span><span class="token string">"blue"</span>
             <span class="token punctuation">}</span><span class="token punctuation">)</span><span class="token punctuation">;</span>

             <span class="token comment">// 4.获取指定样式的值</span>
             console<span class="token punctuation">.</span><span class="token function">log</span><span class="token punctuation">(</span><span class="token function">$</span><span class="token punctuation">(</span><span class="token string">"div"</span><span class="token punctuation">)</span><span class="token punctuation">.</span><span class="token function">css</span><span class="token punctuation">(</span><span class="token string">"width"</span><span class="token punctuation">)</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
         <span class="token punctuation">}</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
     <span class="token punctuation">}</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
</span><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>script</span><span class="token punctuation">&gt;</span></span>
<div class="hljs-button {2}" data-title="复制"></div></code><ul class="pre-numbering" style=""><li style="color: rgb(153, 153, 153);">1</li><li style="color: rgb(153, 153, 153);">2</li><li style="color: rgb(153, 153, 153);">3</li><li style="color: rgb(153, 153, 153);">4</li><li style="color: rgb(153, 153, 153);">5</li><li style="color: rgb(153, 153, 153);">6</li><li style="color: rgb(153, 153, 153);">7</li><li style="color: rgb(153, 153, 153);">8</li><li style="color: rgb(153, 153, 153);">9</li><li style="color: rgb(153, 153, 153);">10</li><li style="color: rgb(153, 153, 153);">11</li><li style="color: rgb(153, 153, 153);">12</li><li style="color: rgb(153, 153, 153);">13</li><li style="color: rgb(153, 153, 153);">14</li><li style="color: rgb(153, 153, 153);">15</li><li style="color: rgb(153, 153, 153);">16</li><li style="color: rgb(153, 153, 153);">17</li><li style="color: rgb(153, 153, 153);">18</li><li style="color: rgb(153, 153, 153);">19</li><li style="color: rgb(153, 153, 153);">20</li><li style="color: rgb(153, 153, 153);">21</li><li style="color: rgb(153, 153, 153);">22</li><li style="color: rgb(153, 153, 153);">23</li></ul></pre>
<h6><a id="2_width__901"></a>2. width 方法</h6>
<ul>
<li>设置或获取元素宽度(相当于获取width属性值)</li>
</ul>
<pre class="prettyprint"><code class="prism language-html has-numbering" onclick="mdcp.copyCode(event)" style="position: unset;"><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>script</span><span class="token punctuation">&gt;</span></span><span class="token script language-javascript">
        <span class="token function">$</span><span class="token punctuation">(</span><span class="token keyword">function</span> <span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
            <span class="token function">$</span><span class="token punctuation">(</span><span class="token string">"button"</span><span class="token punctuation">)</span><span class="token punctuation">.</span><span class="token function">eq</span><span class="token punctuation">(</span><span class="token number">0</span><span class="token punctuation">)</span><span class="token punctuation">.</span><span class="token function">click</span><span class="token punctuation">(</span><span class="token keyword">function</span> <span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
                <span class="token comment">// 1.获取元素宽度(不包括padding和border)</span>
                <span class="token comment">// alert($('.son').width());</span>
            <span class="token punctuation">}</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
            <span class="token function">$</span><span class="token punctuation">(</span><span class="token string">"button"</span><span class="token punctuation">)</span><span class="token punctuation">.</span><span class="token function">eq</span><span class="token punctuation">(</span><span class="token number">1</span><span class="token punctuation">)</span><span class="token punctuation">.</span><span class="token function">click</span><span class="token punctuation">(</span><span class="token keyword">function</span> <span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
                <span class="token comment">// 2.设置元素宽度(不包括padding和border)</span>
                <span class="token comment">// $(".son").width("50px");</span>
            <span class="token punctuation">}</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
        <span class="token punctuation">}</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
    </span><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>script</span><span class="token punctuation">&gt;</span></span>
<div class="hljs-button {2}" data-title="复制"></div></code><ul class="pre-numbering" style=""><li style="color: rgb(153, 153, 153);">1</li><li style="color: rgb(153, 153, 153);">2</li><li style="color: rgb(153, 153, 153);">3</li><li style="color: rgb(153, 153, 153);">4</li><li style="color: rgb(153, 153, 153);">5</li><li style="color: rgb(153, 153, 153);">6</li><li style="color: rgb(153, 153, 153);">7</li><li style="color: rgb(153, 153, 153);">8</li><li style="color: rgb(153, 153, 153);">9</li><li style="color: rgb(153, 153, 153);">10</li><li style="color: rgb(153, 153, 153);">11</li><li style="color: rgb(153, 153, 153);">12</li></ul></pre>
<h6><a id="3_height__917"></a>3. height 方法</h6>
<ul>
<li>设置或获取元素宽度(相当于获取height属性值)</li>
</ul>
<pre class="prettyprint"><code class="prism language-html has-numbering" onclick="mdcp.copyCode(event)" style="position: unset;"><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>script</span><span class="token punctuation">&gt;</span></span><span class="token script language-javascript">
    <span class="token function">$</span><span class="token punctuation">(</span><span class="token keyword">function</span> <span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
        <span class="token function">$</span><span class="token punctuation">(</span><span class="token string">"button"</span><span class="token punctuation">)</span><span class="token punctuation">.</span><span class="token function">eq</span><span class="token punctuation">(</span><span class="token number">0</span><span class="token punctuation">)</span><span class="token punctuation">.</span><span class="token function">click</span><span class="token punctuation">(</span><span class="token keyword">function</span> <span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
            <span class="token comment">// 1.获取元素宽度(不包括padding和border)</span>
            <span class="token comment">// alert($('.son').width());</span>
        <span class="token punctuation">}</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
        <span class="token function">$</span><span class="token punctuation">(</span><span class="token string">"button"</span><span class="token punctuation">)</span><span class="token punctuation">.</span><span class="token function">eq</span><span class="token punctuation">(</span><span class="token number">1</span><span class="token punctuation">)</span><span class="token punctuation">.</span><span class="token function">click</span><span class="token punctuation">(</span><span class="token keyword">function</span> <span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
            <span class="token comment">// 2.设置元素宽度(不包括padding和border)</span>
            <span class="token comment">// $(".son").width("50px");</span>
        <span class="token punctuation">}</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
    <span class="token punctuation">}</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
</span><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>script</span><span class="token punctuation">&gt;</span></span>
<div class="hljs-button {2}" data-title="复制"></div></code><ul class="pre-numbering" style=""><li style="color: rgb(153, 153, 153);">1</li><li style="color: rgb(153, 153, 153);">2</li><li style="color: rgb(153, 153, 153);">3</li><li style="color: rgb(153, 153, 153);">4</li><li style="color: rgb(153, 153, 153);">5</li><li style="color: rgb(153, 153, 153);">6</li><li style="color: rgb(153, 153, 153);">7</li><li style="color: rgb(153, 153, 153);">8</li><li style="color: rgb(153, 153, 153);">9</li><li style="color: rgb(153, 153, 153);">10</li><li style="color: rgb(153, 153, 153);">11</li><li style="color: rgb(153, 153, 153);">12</li></ul></pre>
<h4><a id="4_jQuery__934"></a>4. jQuery 元素位置</h4>
<h6><a id="1_offset__935"></a>1. offset 方法</h6>
<ul>
<li>获取或设置元素相对窗口的偏移位</li>
</ul>
<pre class="prettyprint"><code class="prism language-html has-numbering" onclick="mdcp.copyCode(event)" style="position: unset;"><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>script</span><span class="token punctuation">&gt;</span></span><span class="token script language-javascript">
    <span class="token function">$</span><span class="token punctuation">(</span><span class="token keyword">function</span> <span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
        <span class="token function">$</span><span class="token punctuation">(</span><span class="token string">"button"</span><span class="token punctuation">)</span><span class="token punctuation">.</span><span class="token function">eq</span><span class="token punctuation">(</span><span class="token number">0</span><span class="token punctuation">)</span><span class="token punctuation">.</span><span class="token function">click</span><span class="token punctuation">(</span><span class="token keyword">function</span> <span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
            <span class="token comment">// 1.获取距离窗口的偏移位(从border开始)</span>
            <span class="token function">alert</span><span class="token punctuation">(</span><span class="token function">$</span><span class="token punctuation">(</span><span class="token string">'.son'</span><span class="token punctuation">)</span><span class="token punctuation">.</span><span class="token function">offset</span><span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token punctuation">.</span>left<span class="token punctuation">)</span><span class="token punctuation">;</span> <span class="token comment">// 100</span>
        <span class="token punctuation">}</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
        <span class="token function">$</span><span class="token punctuation">(</span><span class="token string">"button"</span><span class="token punctuation">)</span><span class="token punctuation">.</span><span class="token function">eq</span><span class="token punctuation">(</span><span class="token number">1</span><span class="token punctuation">)</span><span class="token punctuation">.</span><span class="token function">click</span><span class="token punctuation">(</span><span class="token keyword">function</span> <span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
            <span class="token comment">// 2.设置距离窗口的偏移位</span>
            <span class="token function">$</span><span class="token punctuation">(</span><span class="token string">'.son'</span><span class="token punctuation">)</span><span class="token punctuation">.</span><span class="token function">offset</span><span class="token punctuation">(</span><span class="token punctuation">{</span>left<span class="token punctuation">:</span><span class="token number">10</span><span class="token punctuation">,</span> top<span class="token punctuation">:</span><span class="token number">10</span><span class="token punctuation">}</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
        <span class="token punctuation">}</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
    <span class="token punctuation">}</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
</span><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>script</span><span class="token punctuation">&gt;</span></span>
<div class="hljs-button {2}" data-title="复制"></div></code><ul class="pre-numbering" style=""><li style="color: rgb(153, 153, 153);">1</li><li style="color: rgb(153, 153, 153);">2</li><li style="color: rgb(153, 153, 153);">3</li><li style="color: rgb(153, 153, 153);">4</li><li style="color: rgb(153, 153, 153);">5</li><li style="color: rgb(153, 153, 153);">6</li><li style="color: rgb(153, 153, 153);">7</li><li style="color: rgb(153, 153, 153);">8</li><li style="color: rgb(153, 153, 153);">9</li><li style="color: rgb(153, 153, 153);">10</li><li style="color: rgb(153, 153, 153);">11</li><li style="color: rgb(153, 153, 153);">12</li></ul></pre>
<h6><a id="2_position__951"></a>2. position 方法</h6>
<ul>
<li>获取相对于它最近的具有相对位置(position:relative或position:absolute)的父级元素的距离</li>
</ul>
<pre class="prettyprint"><code class="prism language-html has-numbering" onclick="mdcp.copyCode(event)" style="position: unset;"><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>script</span><span class="token punctuation">&gt;</span></span><span class="token script language-javascript">
    <span class="token function">$</span><span class="token punctuation">(</span><span class="token keyword">function</span> <span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
        <span class="token function">$</span><span class="token punctuation">(</span><span class="token string">"button"</span><span class="token punctuation">)</span><span class="token punctuation">.</span><span class="token function">eq</span><span class="token punctuation">(</span><span class="token number">0</span><span class="token punctuation">)</span><span class="token punctuation">.</span><span class="token function">click</span><span class="token punctuation">(</span><span class="token keyword">function</span> <span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
            <span class="token comment">// 1.获取匹配元素相对父元素的偏移</span>
            <span class="token function">alert</span><span class="token punctuation">(</span><span class="token function">$</span><span class="token punctuation">(</span><span class="token string">'.son'</span><span class="token punctuation">)</span><span class="token punctuation">.</span><span class="token function">position</span><span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token punctuation">.</span>left<span class="token punctuation">)</span><span class="token punctuation">;</span><span class="token comment">// 50</span>
        <span class="token punctuation">}</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
        <span class="token function">$</span><span class="token punctuation">(</span><span class="token string">"button"</span><span class="token punctuation">)</span><span class="token punctuation">.</span><span class="token function">eq</span><span class="token punctuation">(</span><span class="token number">1</span><span class="token punctuation">)</span><span class="token punctuation">.</span><span class="token function">click</span><span class="token punctuation">(</span><span class="token keyword">function</span> <span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
            <span class="token comment">// 2.无效,不能设置相对定位元素的偏移位</span>
            <span class="token function">$</span><span class="token punctuation">(</span><span class="token string">'.son'</span><span class="token punctuation">)</span><span class="token punctuation">.</span><span class="token function">position</span><span class="token punctuation">(</span><span class="token punctuation">{</span>left<span class="token punctuation">:</span><span class="token number">10</span><span class="token punctuation">,</span> top<span class="token punctuation">:</span><span class="token number">10</span><span class="token punctuation">}</span><span class="token punctuation">)</span>
        <span class="token punctuation">}</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
    <span class="token punctuation">}</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
</span><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>script</span><span class="token punctuation">&gt;</span></span>
<div class="hljs-button {2}" data-title="复制"></div></code><ul class="pre-numbering" style=""><li style="color: rgb(153, 153, 153);">1</li><li style="color: rgb(153, 153, 153);">2</li><li style="color: rgb(153, 153, 153);">3</li><li style="color: rgb(153, 153, 153);">4</li><li style="color: rgb(153, 153, 153);">5</li><li style="color: rgb(153, 153, 153);">6</li><li style="color: rgb(153, 153, 153);">7</li><li style="color: rgb(153, 153, 153);">8</li><li style="color: rgb(153, 153, 153);">9</li><li style="color: rgb(153, 153, 153);">10</li><li style="color: rgb(153, 153, 153);">11</li><li style="color: rgb(153, 153, 153);">12</li></ul></pre>
<h4><a id="5_jQuery_scroll__968"></a>5. jQuery scroll 方法</h4>
<h6><a id="1_scrollTop__969"></a>1. scrollTop 方法</h6>
<ul>
<li>设置或获取匹配元素相对滚动条顶部的偏移</li>
</ul>
<pre class="prettyprint"><code class="prism language-html has-numbering" onclick="mdcp.copyCode(event)" style="position: unset;"><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>script</span><span class="token punctuation">&gt;</span></span><span class="token script language-javascript">
    <span class="token function">$</span><span class="token punctuation">(</span><span class="token keyword">function</span> <span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
        <span class="token function">$</span><span class="token punctuation">(</span><span class="token string">"button"</span><span class="token punctuation">)</span><span class="token punctuation">.</span><span class="token function">eq</span><span class="token punctuation">(</span><span class="token number">0</span><span class="token punctuation">)</span><span class="token punctuation">.</span><span class="token function">click</span><span class="token punctuation">(</span><span class="token keyword">function</span> <span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
            <span class="token comment">// 7.获取匹配元素相对滚动条顶部的偏移</span>
         <span class="token comment">// alert($('.scroll').scrollTop());</span>
         <span class="token comment">// alert($('html').scrollTop());</span>
            <span class="token comment">// 兼容所有浏览器写法</span>
            <span class="token function">alert</span><span class="token punctuation">(</span><span class="token function">$</span><span class="token punctuation">(</span><span class="token string">'html'</span><span class="token punctuation">)</span><span class="token punctuation">.</span><span class="token function">scrollTop</span><span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token operator">+</span><span class="token function">$</span><span class="token punctuation">(</span><span class="token string">'body'</span><span class="token punctuation">)</span><span class="token punctuation">.</span><span class="token function">scrollTop</span><span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
        <span class="token punctuation">}</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
        <span class="token function">$</span><span class="token punctuation">(</span><span class="token string">"button"</span><span class="token punctuation">)</span><span class="token punctuation">.</span><span class="token function">eq</span><span class="token punctuation">(</span><span class="token number">1</span><span class="token punctuation">)</span><span class="token punctuation">.</span><span class="token function">click</span><span class="token punctuation">(</span><span class="token keyword">function</span> <span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
            <span class="token comment">// 8.设置匹配元素相对滚动条顶部的偏移</span>
         <span class="token comment">// $('.scroll').scrollTop(100);</span>
         <span class="token comment">// $('html').scrollTop(100);</span>
            <span class="token comment">// 兼容所有浏览器写法</span>
            <span class="token function">$</span><span class="token punctuation">(</span><span class="token string">'html,body'</span><span class="token punctuation">)</span><span class="token punctuation">.</span><span class="token function">scrollTop</span><span class="token punctuation">(</span><span class="token number">100</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
        <span class="token punctuation">}</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
    <span class="token punctuation">}</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
</span><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>script</span><span class="token punctuation">&gt;</span></span>
<div class="hljs-button {2}" data-title="复制"></div></code><ul class="pre-numbering" style=""><li style="color: rgb(153, 153, 153);">1</li><li style="color: rgb(153, 153, 153);">2</li><li style="color: rgb(153, 153, 153);">3</li><li style="color: rgb(153, 153, 153);">4</li><li style="color: rgb(153, 153, 153);">5</li><li style="color: rgb(153, 153, 153);">6</li><li style="color: rgb(153, 153, 153);">7</li><li style="color: rgb(153, 153, 153);">8</li><li style="color: rgb(153, 153, 153);">9</li><li style="color: rgb(153, 153, 153);">10</li><li style="color: rgb(153, 153, 153);">11</li><li style="color: rgb(153, 153, 153);">12</li><li style="color: rgb(153, 153, 153);">13</li><li style="color: rgb(153, 153, 153);">14</li><li style="color: rgb(153, 153, 153);">15</li><li style="color: rgb(153, 153, 153);">16</li><li style="color: rgb(153, 153, 153);">17</li><li style="color: rgb(153, 153, 153);">18</li></ul></pre>
<h6><a id="2_scrollLeft__991"></a>2. scrollLeft 方法</h6>
<ul>
<li>scrollLeft() 方法返回或设置匹配元素的滚动条的水平位置。</li>
<li>滚动条的水平位置指的是从其左侧滚动过的像素数。</li>
<li>当滚动条位于最左侧时，位置是 0。</li>
</ul>
<pre class="prettyprint"><code class="prism language-html has-numbering" onclick="mdcp.copyCode(event)" style="position: unset;"><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>script</span><span class="token punctuation">&gt;</span></span><span class="token script language-javascript">
    <span class="token function">$</span><span class="token punctuation">(</span><span class="token keyword">function</span> <span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
        <span class="token function">$</span><span class="token punctuation">(</span><span class="token string">"button"</span><span class="token punctuation">)</span><span class="token punctuation">.</span><span class="token function">eq</span><span class="token punctuation">(</span><span class="token number">0</span><span class="token punctuation">)</span><span class="token punctuation">.</span><span class="token function">click</span><span class="token punctuation">(</span><span class="token keyword">function</span> <span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
            <span class="token comment">// 7.获取匹配元素相对滚动条水平的偏移</span>
            <span class="token comment">// alert($('.scroll').scrollLeft());</span>
            <span class="token comment">// alert($('html').scrollLeft());</span>
            <span class="token comment">// 兼容所有浏览器写法</span>
            <span class="token function">alert</span><span class="token punctuation">(</span><span class="token function">$</span><span class="token punctuation">(</span><span class="token string">'html'</span><span class="token punctuation">)</span><span class="token punctuation">.</span><span class="token function">scrollLeft</span><span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token operator">+</span><span class="token function">$</span><span class="token punctuation">(</span><span class="token string">'body'</span><span class="token punctuation">)</span><span class="token punctuation">.</span><span class="token function">scrollLeft</span><span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
        <span class="token punctuation">}</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
        <span class="token function">$</span><span class="token punctuation">(</span><span class="token string">"button"</span><span class="token punctuation">)</span><span class="token punctuation">.</span><span class="token function">eq</span><span class="token punctuation">(</span><span class="token number">1</span><span class="token punctuation">)</span><span class="token punctuation">.</span><span class="token function">click</span><span class="token punctuation">(</span><span class="token keyword">function</span> <span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
            <span class="token comment">// 8.设置匹配元素相对滚动条水平的偏移</span>
            <span class="token comment">// $('.scroll').scrollLeft(100);</span>
            <span class="token comment">// $('html').scrollLeft(100);</span>
            <span class="token comment">// 兼容所有浏览器写法</span>
            <span class="token function">$</span><span class="token punctuation">(</span><span class="token string">'html,body'</span><span class="token punctuation">)</span><span class="token punctuation">.</span><span class="token function">scrollLeft</span><span class="token punctuation">(</span><span class="token number">100</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
        <span class="token punctuation">}</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
    <span class="token punctuation">}</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
</span><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>script</span><span class="token punctuation">&gt;</span></span>
<div class="hljs-button {2}" data-title="复制"></div></code><ul class="pre-numbering" style=""><li style="color: rgb(153, 153, 153);">1</li><li style="color: rgb(153, 153, 153);">2</li><li style="color: rgb(153, 153, 153);">3</li><li style="color: rgb(153, 153, 153);">4</li><li style="color: rgb(153, 153, 153);">5</li><li style="color: rgb(153, 153, 153);">6</li><li style="color: rgb(153, 153, 153);">7</li><li style="color: rgb(153, 153, 153);">8</li><li style="color: rgb(153, 153, 153);">9</li><li style="color: rgb(153, 153, 153);">10</li><li style="color: rgb(153, 153, 153);">11</li><li style="color: rgb(153, 153, 153);">12</li><li style="color: rgb(153, 153, 153);">13</li><li style="color: rgb(153, 153, 153);">14</li><li style="color: rgb(153, 153, 153);">15</li><li style="color: rgb(153, 153, 153);">16</li><li style="color: rgb(153, 153, 153);">17</li><li style="color: rgb(153, 153, 153);">18</li></ul></pre>
<h2><a name="t10"></a><a id="10_jQuery__1016"></a>10. jQuery 事件</h2>
<h4><a id="1__1017"></a>1. 事件绑定</h4>
<ul>
<li>
<p>事件绑定方式一</p>
<ul>
<li>eventName(function(){})</li>
<li>绑定对应事件名的监听, 例如：$(’#div’).click(function(){});</li>
<li>优点：编码效率略高</li>
<li>缺点：部分事件jQuery没有实现,所以不能添加</li>
</ul>
</li>
<li>
<p>事件绑定方式二</p>
<ul>
<li>on(eventName, funcion(){})</li>
<li>通用的绑定事件监听, 例如：$(’#div’).on(‘click’, function(){});</li>
<li>优点：编码效率略低</li>
<li>缺点：所有js事件都可以添加</li>
<li>注意点：可以添加多个相同或者不同类型的事件,不会覆盖</li>
</ul>
</li>
</ul>
<p><strong>建议：</strong><br>
能用eventName就用eventName, 不能用eventName就用on</p>
<pre class="prettyprint"><code class="prism language-html has-numbering" onclick="mdcp.copyCode(event)" style="position: unset;"><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>script</span><span class="token punctuation">&gt;</span></span><span class="token script language-javascript">
    <span class="token function">$</span><span class="token punctuation">(</span><span class="token keyword">function</span> <span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
        <span class="token comment">// 1.通过eventName绑定事件</span>
        <span class="token function">$</span><span class="token punctuation">(</span><span class="token string">"button"</span><span class="token punctuation">)</span><span class="token punctuation">.</span><span class="token function">click</span><span class="token punctuation">(</span><span class="token keyword">function</span> <span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
             <span class="token function">alert</span><span class="token punctuation">(</span><span class="token string">"hello lnj"</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
         <span class="token punctuation">}</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
        <span class="token function">$</span><span class="token punctuation">(</span><span class="token string">"button"</span><span class="token punctuation">)</span><span class="token punctuation">.</span><span class="token function">click</span><span class="token punctuation">(</span><span class="token keyword">function</span> <span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
             <span class="token function">alert</span><span class="token punctuation">(</span><span class="token string">"hello 123"</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
         <span class="token punctuation">}</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
        <span class="token function">$</span><span class="token punctuation">(</span><span class="token string">"button"</span><span class="token punctuation">)</span><span class="token punctuation">.</span><span class="token function">mouseleave</span><span class="token punctuation">(</span><span class="token keyword">function</span> <span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
             <span class="token function">alert</span><span class="token punctuation">(</span><span class="token string">"hello mouseleave"</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
         <span class="token punctuation">}</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
        <span class="token function">$</span><span class="token punctuation">(</span><span class="token string">"button"</span><span class="token punctuation">)</span><span class="token punctuation">.</span><span class="token function">mouseenter</span><span class="token punctuation">(</span><span class="token keyword">function</span> <span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
             <span class="token function">alert</span><span class="token punctuation">(</span><span class="token string">"hello mouseenter"</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
         <span class="token punctuation">}</span><span class="token punctuation">)</span><span class="token punctuation">;</span>

        <span class="token comment">// 2.通过on绑定事件</span>
        <span class="token function">$</span><span class="token punctuation">(</span><span class="token string">"button"</span><span class="token punctuation">)</span><span class="token punctuation">.</span><span class="token function">on</span><span class="token punctuation">(</span><span class="token string">"click"</span><span class="token punctuation">,</span> <span class="token keyword">function</span> <span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
            <span class="token function">alert</span><span class="token punctuation">(</span><span class="token string">"hello click1"</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
        <span class="token punctuation">}</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
        <span class="token function">$</span><span class="token punctuation">(</span><span class="token string">"button"</span><span class="token punctuation">)</span><span class="token punctuation">.</span><span class="token function">on</span><span class="token punctuation">(</span><span class="token string">"click"</span><span class="token punctuation">,</span> <span class="token keyword">function</span> <span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
            <span class="token function">alert</span><span class="token punctuation">(</span><span class="token string">"hello click2"</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
        <span class="token punctuation">}</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
        <span class="token function">$</span><span class="token punctuation">(</span><span class="token string">"button"</span><span class="token punctuation">)</span><span class="token punctuation">.</span><span class="token function">on</span><span class="token punctuation">(</span><span class="token string">"mouseleave"</span><span class="token punctuation">,</span> <span class="token keyword">function</span> <span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
            <span class="token function">alert</span><span class="token punctuation">(</span><span class="token string">"hello mouseleave"</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
        <span class="token punctuation">}</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
        <span class="token function">$</span><span class="token punctuation">(</span><span class="token string">"button"</span><span class="token punctuation">)</span><span class="token punctuation">.</span><span class="token function">on</span><span class="token punctuation">(</span><span class="token string">"mouseenter"</span><span class="token punctuation">,</span> <span class="token keyword">function</span> <span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
            <span class="token function">alert</span><span class="token punctuation">(</span><span class="token string">"hello mouseenter"</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
        <span class="token punctuation">}</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
    <span class="token punctuation">}</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
</span><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>script</span><span class="token punctuation">&gt;</span></span>
<div class="hljs-button {2}" data-title="复制"></div></code><ul class="pre-numbering" style=""><li style="color: rgb(153, 153, 153);">1</li><li style="color: rgb(153, 153, 153);">2</li><li style="color: rgb(153, 153, 153);">3</li><li style="color: rgb(153, 153, 153);">4</li><li style="color: rgb(153, 153, 153);">5</li><li style="color: rgb(153, 153, 153);">6</li><li style="color: rgb(153, 153, 153);">7</li><li style="color: rgb(153, 153, 153);">8</li><li style="color: rgb(153, 153, 153);">9</li><li style="color: rgb(153, 153, 153);">10</li><li style="color: rgb(153, 153, 153);">11</li><li style="color: rgb(153, 153, 153);">12</li><li style="color: rgb(153, 153, 153);">13</li><li style="color: rgb(153, 153, 153);">14</li><li style="color: rgb(153, 153, 153);">15</li><li style="color: rgb(153, 153, 153);">16</li><li style="color: rgb(153, 153, 153);">17</li><li style="color: rgb(153, 153, 153);">18</li><li style="color: rgb(153, 153, 153);">19</li><li style="color: rgb(153, 153, 153);">20</li><li style="color: rgb(153, 153, 153);">21</li><li style="color: rgb(153, 153, 153);">22</li><li style="color: rgb(153, 153, 153);">23</li><li style="color: rgb(153, 153, 153);">24</li><li style="color: rgb(153, 153, 153);">25</li><li style="color: rgb(153, 153, 153);">26</li><li style="color: rgb(153, 153, 153);">27</li><li style="color: rgb(153, 153, 153);">28</li><li style="color: rgb(153, 153, 153);">29</li><li style="color: rgb(153, 153, 153);">30</li><li style="color: rgb(153, 153, 153);">31</li></ul></pre>
<h4><a id="2__1067"></a>2. 事件解绑</h4>
<ul>
<li>jQuery中可以通过off(eventName,function);解绑事件</li>
<li>off方法如果不传递参数, 会移除所有的事件（ // $(“button”).off(); ）</li>
<li>off方法如果传递一个参数, 会移除所有指定类型的事件（ // $(“button”).off(“click”); ）</li>
<li>off方法如果传递两个参数, 会移除所有指定类型的指定事件（ $(“button”).off(“click”, test1); ）</li>
</ul>
<pre class="prettyprint"><code class="prism language-html has-numbering" onclick="mdcp.copyCode(event)" style="position: unset;"><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>script</span><span class="token punctuation">&gt;</span></span><span class="token script language-javascript">
    <span class="token function">$</span><span class="token punctuation">(</span><span class="token keyword">function</span> <span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
        <span class="token keyword">function</span> <span class="token function">test1</span><span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
            <span class="token function">alert</span><span class="token punctuation">(</span><span class="token string">"son1"</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
        <span class="token punctuation">}</span>
        <span class="token keyword">function</span> <span class="token function">test2</span><span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
            <span class="token function">alert</span><span class="token punctuation">(</span><span class="token string">"son2"</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
        <span class="token punctuation">}</span>
        <span class="token keyword">function</span> <span class="token function">test3</span><span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
            <span class="token function">alert</span><span class="token punctuation">(</span><span class="token string">"son3"</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
        <span class="token punctuation">}</span>
        <span class="token function">$</span><span class="token punctuation">(</span><span class="token string">".son"</span><span class="token punctuation">)</span><span class="token punctuation">.</span><span class="token function">click</span><span class="token punctuation">(</span>test1<span class="token punctuation">)</span><span class="token punctuation">;</span>
        <span class="token function">$</span><span class="token punctuation">(</span><span class="token string">".son"</span><span class="token punctuation">)</span><span class="token punctuation">.</span><span class="token function">click</span><span class="token punctuation">(</span>test2<span class="token punctuation">)</span><span class="token punctuation">;</span>
        <span class="token function">$</span><span class="token punctuation">(</span><span class="token string">".son"</span><span class="token punctuation">)</span><span class="token punctuation">.</span><span class="token function">on</span><span class="token punctuation">(</span><span class="token string">"mouseleave"</span><span class="token punctuation">,</span> test3<span class="token punctuation">)</span><span class="token punctuation">;</span>

        <span class="token function">$</span><span class="token punctuation">(</span><span class="token string">".son"</span><span class="token punctuation">)</span><span class="token punctuation">.</span><span class="token function">off</span><span class="token punctuation">(</span><span class="token string">"click"</span><span class="token punctuation">,</span> test1<span class="token punctuation">)</span><span class="token punctuation">;</span>
    <span class="token punctuation">}</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
</span><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>script</span><span class="token punctuation">&gt;</span></span>
<div class="hljs-button {2}" data-title="复制"></div></code><ul class="pre-numbering" style=""><li style="color: rgb(153, 153, 153);">1</li><li style="color: rgb(153, 153, 153);">2</li><li style="color: rgb(153, 153, 153);">3</li><li style="color: rgb(153, 153, 153);">4</li><li style="color: rgb(153, 153, 153);">5</li><li style="color: rgb(153, 153, 153);">6</li><li style="color: rgb(153, 153, 153);">7</li><li style="color: rgb(153, 153, 153);">8</li><li style="color: rgb(153, 153, 153);">9</li><li style="color: rgb(153, 153, 153);">10</li><li style="color: rgb(153, 153, 153);">11</li><li style="color: rgb(153, 153, 153);">12</li><li style="color: rgb(153, 153, 153);">13</li><li style="color: rgb(153, 153, 153);">14</li><li style="color: rgb(153, 153, 153);">15</li><li style="color: rgb(153, 153, 153);">16</li><li style="color: rgb(153, 153, 153);">17</li><li style="color: rgb(153, 153, 153);">18</li></ul></pre>
<h4><a id="3__1093"></a>3. 事件坐标</h4>
<ul>
<li>
<p>当事件被触发时,系统会将事件对象(event)传递给回调函数,通过event对象我们就能获取时间的坐标</p>
</li>
<li>
<p>获取事件坐标有三种方式</p>
<ul>
<li>event.offsetX, event.offsetY 相对于事件元素左上角</li>
<li>event.pageX, event.pageY  相对于页面的左上角</li>
<li>event.clientX, event.clientY  相对于视口的左上角</li>
</ul>
</li>
<li>
<p>event.page和event.client区别</p>
<ul>
<li>网页是可以滚动的,而视口是固定的</li>
<li>所以想获取距离可视区域坐标通过event.client</li>
<li>想获取距离网页左上角的坐标通过event.client</li>
</ul>
</li>
</ul>
<pre class="prettyprint"><code class="prism language-html has-numbering" onclick="mdcp.copyCode(event)" style="position: unset;"><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>script</span><span class="token punctuation">&gt;</span></span><span class="token script language-javascript">
    <span class="token function">$</span><span class="token punctuation">(</span><span class="token keyword">function</span> <span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
        <span class="token comment">// 获取事件的坐标</span>
        <span class="token function">$</span><span class="token punctuation">(</span><span class="token string">".son"</span><span class="token punctuation">)</span><span class="token punctuation">.</span><span class="token function">click</span><span class="token punctuation">(</span><span class="token keyword">function</span> <span class="token punctuation">(</span>event<span class="token punctuation">)</span> <span class="token punctuation">{</span>
            <span class="token comment">// 获取相对于事件元素左上角坐标</span>
            console<span class="token punctuation">.</span><span class="token function">log</span><span class="token punctuation">(</span>event<span class="token punctuation">.</span>offsetX<span class="token punctuation">,</span> event<span class="token punctuation">.</span>offsetY<span class="token punctuation">)</span><span class="token punctuation">;</span>
            <span class="token comment">// 获取相对于视口左上角坐标</span>
            console<span class="token punctuation">.</span><span class="token function">log</span><span class="token punctuation">(</span>event<span class="token punctuation">.</span>clientX<span class="token punctuation">,</span> event<span class="token punctuation">.</span>clientY<span class="token punctuation">)</span><span class="token punctuation">;</span>
            <span class="token comment">// 获取相对于页面左上角坐标</span>
            console<span class="token punctuation">.</span><span class="token function">log</span><span class="token punctuation">(</span>event<span class="token punctuation">.</span>pageX<span class="token punctuation">,</span> event<span class="token punctuation">.</span>pageY<span class="token punctuation">)</span><span class="token punctuation">;</span>
        <span class="token punctuation">}</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
    <span class="token punctuation">}</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
</span><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>script</span><span class="token punctuation">&gt;</span></span>
<div class="hljs-button {2}" data-title="复制"></div></code><ul class="pre-numbering" style=""><li style="color: rgb(153, 153, 153);">1</li><li style="color: rgb(153, 153, 153);">2</li><li style="color: rgb(153, 153, 153);">3</li><li style="color: rgb(153, 153, 153);">4</li><li style="color: rgb(153, 153, 153);">5</li><li style="color: rgb(153, 153, 153);">6</li><li style="color: rgb(153, 153, 153);">7</li><li style="color: rgb(153, 153, 153);">8</li><li style="color: rgb(153, 153, 153);">9</li><li style="color: rgb(153, 153, 153);">10</li><li style="color: rgb(153, 153, 153);">11</li><li style="color: rgb(153, 153, 153);">12</li><li style="color: rgb(153, 153, 153);">13</li></ul></pre>
<h4><a id="4__1121"></a>4. 事件冒泡</h4>
<h6><a id="1__1122"></a>1. 什么是事件冒泡</h6>
<ul>
<li>事件冒泡是从目标元素逐级向上传播到根节点的过程</li>
</ul>
<h6><a id="2__1124"></a>2. 阻止事件冒泡</h6>
<ul>
<li>如果希望在触发一个元素的事件处理程序时，不影响它的父元素, 此时便可以使用停止事件冒泡</li>
</ul>
<pre class="prettyprint"><code class="prism language-html has-numbering" onclick="mdcp.copyCode(event)" style="position: unset;"><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>script</span><span class="token punctuation">&gt;</span></span><span class="token script language-javascript">
    <span class="token function">$</span><span class="token punctuation">(</span><span class="token keyword">function</span> <span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
        <span class="token function">$</span><span class="token punctuation">(</span><span class="token string">".son"</span><span class="token punctuation">)</span><span class="token punctuation">.</span><span class="token function">click</span><span class="token punctuation">(</span><span class="token keyword">function</span> <span class="token punctuation">(</span>event<span class="token punctuation">)</span> <span class="token punctuation">{</span>
            console<span class="token punctuation">.</span><span class="token function">log</span><span class="token punctuation">(</span><span class="token string">".son"</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
            <span class="token comment">// 在子元素中停止事件冒泡,时间不会继续向上传播,所以父元素click方法不会被触发</span>
            event<span class="token punctuation">.</span><span class="token function">stopPropagation</span><span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
        <span class="token punctuation">}</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
        <span class="token function">$</span><span class="token punctuation">(</span><span class="token string">".father"</span><span class="token punctuation">)</span><span class="token punctuation">.</span><span class="token function">click</span><span class="token punctuation">(</span><span class="token keyword">function</span> <span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
            console<span class="token punctuation">.</span><span class="token function">log</span><span class="token punctuation">(</span><span class="token string">".father"</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
        <span class="token punctuation">}</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
    <span class="token punctuation">}</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
</span><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>script</span><span class="token punctuation">&gt;</span></span>
<div class="hljs-button {2}" data-title="复制"></div></code><ul class="pre-numbering" style=""><li style="color: rgb(153, 153, 153);">1</li><li style="color: rgb(153, 153, 153);">2</li><li style="color: rgb(153, 153, 153);">3</li><li style="color: rgb(153, 153, 153);">4</li><li style="color: rgb(153, 153, 153);">5</li><li style="color: rgb(153, 153, 153);">6</li><li style="color: rgb(153, 153, 153);">7</li><li style="color: rgb(153, 153, 153);">8</li><li style="color: rgb(153, 153, 153);">9</li><li style="color: rgb(153, 153, 153);">10</li><li style="color: rgb(153, 153, 153);">11</li><li style="color: rgb(153, 153, 153);">12</li></ul></pre>
<h4><a id="5__1140"></a>5. 默认行为</h4>
<h6><a id="1__1141"></a>1. 什么是默认行为</h6>
<ul>
<li>网页中的元素有自己的默认行为,例如单击超链接后会跳转,点击提交表单按钮会提交</li>
</ul>
<h6><a id="2__1143"></a>2. 阻止默认行为</h6>
<ul>
<li>可以使用event.preventDefault();方法阻止事件默认行为方法</li>
</ul>
<pre class="prettyprint"><code class="prism language-html has-numbering" onclick="mdcp.copyCode(event)" style="position: unset;"><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>script</span><span class="token punctuation">&gt;</span></span><span class="token script language-javascript">
    <span class="token function">$</span><span class="token punctuation">(</span><span class="token keyword">function</span> <span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
        <span class="token function">$</span><span class="token punctuation">(</span><span class="token string">"a"</span><span class="token punctuation">)</span><span class="token punctuation">.</span><span class="token function">click</span><span class="token punctuation">(</span><span class="token keyword">function</span> <span class="token punctuation">(</span>event<span class="token punctuation">)</span> <span class="token punctuation">{</span>
            <span class="token keyword">var</span> str <span class="token operator">=</span> <span class="token function">$</span><span class="token punctuation">(</span><span class="token string">"a"</span><span class="token punctuation">)</span><span class="token punctuation">.</span><span class="token function">attr</span><span class="token punctuation">(</span><span class="token string">"href"</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
            <span class="token comment">// 如果超链接是百度就不跳转</span>
            <span class="token keyword">if</span><span class="token punctuation">(</span>str<span class="token punctuation">.</span><span class="token function">indexOf</span><span class="token punctuation">(</span><span class="token string">"baidu"</span><span class="token punctuation">)</span> <span class="token operator">&gt;</span> <span class="token number">0</span><span class="token punctuation">)</span><span class="token punctuation">{</span>
                <span class="token comment">// 阻止默认行为</span>
                event<span class="token punctuation">.</span><span class="token function">preventDefault</span><span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
            <span class="token punctuation">}</span>
        <span class="token punctuation">}</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
    <span class="token punctuation">}</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
</span><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>script</span><span class="token punctuation">&gt;</span></span>
<div class="hljs-button {2}" data-title="复制"></div></code><ul class="pre-numbering" style=""><li style="color: rgb(153, 153, 153);">1</li><li style="color: rgb(153, 153, 153);">2</li><li style="color: rgb(153, 153, 153);">3</li><li style="color: rgb(153, 153, 153);">4</li><li style="color: rgb(153, 153, 153);">5</li><li style="color: rgb(153, 153, 153);">6</li><li style="color: rgb(153, 153, 153);">7</li><li style="color: rgb(153, 153, 153);">8</li><li style="color: rgb(153, 153, 153);">9</li><li style="color: rgb(153, 153, 153);">10</li><li style="color: rgb(153, 153, 153);">11</li><li style="color: rgb(153, 153, 153);">12</li></ul></pre>
<h4><a id="6__1159"></a>6. 自动触发事件</h4>
<h6><a id="1__1160"></a>1. 什么是自动触发事件</h6>
<ul>
<li>通过代码控制事件, 不用人为点击/移入/移除等事件就能被触发</li>
</ul>
<h6><a id="2__1162"></a>2. 自动触发方式</h6>
<ul>
<li>$(“selector”).trigger(“eventName”);
<ul>
<li>触发事件的同时会触发事件冒泡</li>
<li>触发事件的同时会触发事件默认行为</li>
</ul>
</li>
<li>$(“selector”).triggerHandler(“eventName”);
<ul>
<li>触发事件的同时不会触发事件冒泡</li>
<li>触发事件的同时不会触发事件默认行为</li>
</ul>
</li>
</ul>
<pre class="prettyprint"><code class="prism language-html has-numbering" onclick="mdcp.copyCode(event)" style="position: unset;"> <span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>script</span><span class="token punctuation">&gt;</span></span><span class="token script language-javascript">
     <span class="token function">$</span><span class="token punctuation">(</span><span class="token keyword">function</span> <span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
         <span class="token comment">/*
         $(".son").click(function () {
             alert("son");
         });
         $(".father").click(function () {
             alert("father");
         });

         // trigger会触发事件冒泡
         // $(".father").trigger("click");
         // $(".son").trigger("click");

         // triggerHandler不会触发事件冒泡
         // $(".father").triggerHandler("click");
         // $(".son").triggerHandler("click");
         */</span>

         <span class="token function">$</span><span class="token punctuation">(</span><span class="token string">"input[type='submit']"</span><span class="token punctuation">)</span><span class="token punctuation">.</span><span class="token function">click</span><span class="token punctuation">(</span><span class="token keyword">function</span> <span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
             <span class="token function">alert</span><span class="token punctuation">(</span><span class="token string">"点击了A标签"</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
         <span class="token punctuation">}</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
         <span class="token comment">// trigger会触发系统默认事件</span>
         <span class="token comment">// $("input[type='submit']").trigger("click");</span>
         <span class="token comment">// triggerHandler不会触发系统默认事件</span>
         <span class="token function">$</span><span class="token punctuation">(</span><span class="token string">"input[type='submit']"</span><span class="token punctuation">)</span><span class="token punctuation">.</span><span class="token function">triggerHandler</span><span class="token punctuation">(</span><span class="token string">"click"</span><span class="token punctuation">)</span><span class="token punctuation">;</span>

     <span class="token punctuation">}</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
</span><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>script</span><span class="token punctuation">&gt;</span></span>
<div class="hljs-button {2}" data-title="复制"></div></code><ul class="pre-numbering" style=""><li style="color: rgb(153, 153, 153);">1</li><li style="color: rgb(153, 153, 153);">2</li><li style="color: rgb(153, 153, 153);">3</li><li style="color: rgb(153, 153, 153);">4</li><li style="color: rgb(153, 153, 153);">5</li><li style="color: rgb(153, 153, 153);">6</li><li style="color: rgb(153, 153, 153);">7</li><li style="color: rgb(153, 153, 153);">8</li><li style="color: rgb(153, 153, 153);">9</li><li style="color: rgb(153, 153, 153);">10</li><li style="color: rgb(153, 153, 153);">11</li><li style="color: rgb(153, 153, 153);">12</li><li style="color: rgb(153, 153, 153);">13</li><li style="color: rgb(153, 153, 153);">14</li><li style="color: rgb(153, 153, 153);">15</li><li style="color: rgb(153, 153, 153);">16</li><li style="color: rgb(153, 153, 153);">17</li><li style="color: rgb(153, 153, 153);">18</li><li style="color: rgb(153, 153, 153);">19</li><li style="color: rgb(153, 153, 153);">20</li><li style="color: rgb(153, 153, 153);">21</li><li style="color: rgb(153, 153, 153);">22</li><li style="color: rgb(153, 153, 153);">23</li><li style="color: rgb(153, 153, 153);">24</li><li style="color: rgb(153, 153, 153);">25</li><li style="color: rgb(153, 153, 153);">26</li><li style="color: rgb(153, 153, 153);">27</li><li style="color: rgb(153, 153, 153);">28</li><li style="color: rgb(153, 153, 153);">29</li></ul></pre>
<h4><a id="7__1201"></a>7. 自定义事件</h4>
<h6><a id="1__1202"></a>1. 什么是自定义事件</h6>
<ul>
<li>自定义事件就是自己起一个不存在的事件名称来注册事件, 然后通过这个名称还能触发对应的方法执行, 这就是传说中的自定义事件</li>
</ul>
<h6><a id="2__1204"></a>2. 自定义事件的条件</h6>
<ul>
<li>事件必须是通过on绑定的</li>
<li>事件必须通过trigger来触发</li>
<li>因为trigger方法可以自动触发对应名称的事件,所以只要事件的名称和传递给trigger的名称一致就能执行对应的事件方法</li>
</ul>
<pre class="prettyprint"><code class="prism language-html has-numbering" onclick="mdcp.copyCode(event)" style="position: unset;"><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>script</span><span class="token punctuation">&gt;</span></span><span class="token script language-javascript">
    <span class="token function">$</span><span class="token punctuation">(</span><span class="token keyword">function</span> <span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
        <span class="token function">$</span><span class="token punctuation">(</span><span class="token string">".father"</span><span class="token punctuation">)</span><span class="token punctuation">.</span><span class="token function">on</span><span class="token punctuation">(</span><span class="token string">"njClick"</span><span class="token punctuation">,</span> <span class="token keyword">function</span> <span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
            <span class="token function">alert</span><span class="token punctuation">(</span><span class="token string">"njClick"</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
        <span class="token punctuation">}</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
        <span class="token function">$</span><span class="token punctuation">(</span><span class="token string">".father"</span><span class="token punctuation">)</span><span class="token punctuation">.</span><span class="token function">trigger</span><span class="token punctuation">(</span><span class="token string">"njClick"</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
    <span class="token punctuation">}</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
</span><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>script</span><span class="token punctuation">&gt;</span></span>
<div class="hljs-button {2}" data-title="复制"></div></code><ul class="pre-numbering" style=""><li style="color: rgb(153, 153, 153);">1</li><li style="color: rgb(153, 153, 153);">2</li><li style="color: rgb(153, 153, 153);">3</li><li style="color: rgb(153, 153, 153);">4</li><li style="color: rgb(153, 153, 153);">5</li><li style="color: rgb(153, 153, 153);">6</li><li style="color: rgb(153, 153, 153);">7</li><li style="color: rgb(153, 153, 153);">8</li></ul></pre>
<h4><a id="8__1219"></a>8. 事件命名空间</h4>
<h6><a id="1__1220"></a>1. 什么是事件命名空间</h6>
<ul>
<li>事件命名空间主要用于区分相同类型的事件,区分不同前提条件下到底应该触发哪个人编写的事件</li>
<li>格式: “eventName.命名空间”</li>
</ul>
<h6><a id="2__1223"></a>2. 添加事件命名空间的条件</h6>
<ul>
<li>事件是通过on来绑定的</li>
<li>通过trigger触发事件</li>
</ul>
<h6><a id="3__1226"></a>3. 事件命名空间注意点（面试题）</h6>
<ul>
<li>不带命名空间事件被trigger调用,会触发带命名空间事件</li>
<li>带命名空间事件被trigger调用,只会触发带命名空间事件</li>
<li>下级不带命名空间事件被trigger调用,会冒泡触发上级不带命名空间和带命名空间事件</li>
<li>下级带命名空间事件被trigger调用,不会触发上级不带命名空间事件</li>
<li>下级带命名空间事件被trigger调用,会触发上级带命名空间事件</li>
</ul>
<pre class="prettyprint"><code class="prism language-html has-numbering" onclick="mdcp.copyCode(event)" style="position: unset;"><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>script</span><span class="token punctuation">&gt;</span></span><span class="token script language-javascript">
    <span class="token function">$</span><span class="token punctuation">(</span><span class="token keyword">function</span> <span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
        <span class="token comment">// 给父元素添加不带命名空间事件</span>
        <span class="token function">$</span><span class="token punctuation">(</span><span class="token string">".father"</span><span class="token punctuation">)</span><span class="token punctuation">.</span><span class="token function">on</span><span class="token punctuation">(</span><span class="token string">"click"</span><span class="token punctuation">,</span> <span class="token keyword">function</span> <span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
            <span class="token function">alert</span><span class="token punctuation">(</span><span class="token string">"father"</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
        <span class="token punctuation">}</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
        <span class="token comment">// 给父元素添加带命名空间事件</span>
        <span class="token function">$</span><span class="token punctuation">(</span><span class="token string">".father"</span><span class="token punctuation">)</span><span class="token punctuation">.</span><span class="token function">on</span><span class="token punctuation">(</span><span class="token string">"click.66"</span><span class="token punctuation">,</span> <span class="token keyword">function</span> <span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
            <span class="token function">alert</span><span class="token punctuation">(</span><span class="token string">"66 - father"</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
        <span class="token punctuation">}</span><span class="token punctuation">)</span><span class="token punctuation">;</span>

        <span class="token function">$</span><span class="token punctuation">(</span><span class="token string">".son"</span><span class="token punctuation">)</span><span class="token punctuation">.</span><span class="token function">on</span><span class="token punctuation">(</span><span class="token string">"click.nj"</span><span class="token punctuation">,</span> <span class="token keyword">function</span> <span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
            <span class="token function">alert</span><span class="token punctuation">(</span><span class="token string">"nj - 向左走"</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
        <span class="token punctuation">}</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
        <span class="token function">$</span><span class="token punctuation">(</span><span class="token string">".son"</span><span class="token punctuation">)</span><span class="token punctuation">.</span><span class="token function">on</span><span class="token punctuation">(</span><span class="token string">"click.66"</span><span class="token punctuation">,</span> <span class="token keyword">function</span> <span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
            <span class="token function">alert</span><span class="token punctuation">(</span><span class="token string">"66 - 向右走"</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
        <span class="token punctuation">}</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
        <span class="token comment">// 会同时触发NJ和66编写的click事件</span>
        <span class="token comment">// 事件会冒泡到不带命名空间上级元素和带相同命名空间的上级元素</span>
        <span class="token comment">// $(".son").trigger("click");</span>
        <span class="token comment">// 只会触发NJ编写的click事件</span>
        <span class="token comment">// 事件不会冒泡到不带命名空间上级元素</span>
        <span class="token comment">// $(".son").trigger("click.nj");</span>
        <span class="token comment">// 只会触发66编写的click事件</span>
        <span class="token comment">// 事件只会冒泡到带相同命名空间的上级元素</span>
        <span class="token function">$</span><span class="token punctuation">(</span><span class="token string">".son"</span><span class="token punctuation">)</span><span class="token punctuation">.</span><span class="token function">trigger</span><span class="token punctuation">(</span><span class="token string">"click.66"</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
    <span class="token punctuation">}</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
</span><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>script</span><span class="token punctuation">&gt;</span></span>
<div class="hljs-button {2}" data-title="复制"></div></code><ul class="pre-numbering" style=""><li style="color: rgb(153, 153, 153);">1</li><li style="color: rgb(153, 153, 153);">2</li><li style="color: rgb(153, 153, 153);">3</li><li style="color: rgb(153, 153, 153);">4</li><li style="color: rgb(153, 153, 153);">5</li><li style="color: rgb(153, 153, 153);">6</li><li style="color: rgb(153, 153, 153);">7</li><li style="color: rgb(153, 153, 153);">8</li><li style="color: rgb(153, 153, 153);">9</li><li style="color: rgb(153, 153, 153);">10</li><li style="color: rgb(153, 153, 153);">11</li><li style="color: rgb(153, 153, 153);">12</li><li style="color: rgb(153, 153, 153);">13</li><li style="color: rgb(153, 153, 153);">14</li><li style="color: rgb(153, 153, 153);">15</li><li style="color: rgb(153, 153, 153);">16</li><li style="color: rgb(153, 153, 153);">17</li><li style="color: rgb(153, 153, 153);">18</li><li style="color: rgb(153, 153, 153);">19</li><li style="color: rgb(153, 153, 153);">20</li><li style="color: rgb(153, 153, 153);">21</li><li style="color: rgb(153, 153, 153);">22</li><li style="color: rgb(153, 153, 153);">23</li><li style="color: rgb(153, 153, 153);">24</li><li style="color: rgb(153, 153, 153);">25</li><li style="color: rgb(153, 153, 153);">26</li><li style="color: rgb(153, 153, 153);">27</li><li style="color: rgb(153, 153, 153);">28</li></ul></pre>
<h4><a id="9__1263"></a>9. 事件委托</h4>
<h6><a id="1__1264"></a>1. 什么是事件委托</h6>
<ul>
<li>事件委托就是请其他人帮忙做我们想做的事</li>
<li>做完之后最终的结果还是会反馈到我们这里</li>
</ul>
<h6><a id="2__1268"></a>2. 事件委托的好处</h6>
<ul>
<li>减少监听数量
<ul>
<li>添加到页面上的事件处理程序数量将直接关系到页面的整体运行性能，因为需要不断的与dom节点进行交互，访问dom的次数越多，引起浏览器重绘与重排的次数也就越多，就会延长整个页面的交互就绪时间</li>
<li>每个监听的函数都是一个对象，是对象就会占用内存，对象越多，内存占用率就越大，自然性能就越差</li>
</ul>
</li>
<li>新增元素自动有事件响应处理
<ul>
<li>默认情况下新增的元素无法响应新增前添加的事件</li>
</ul>
</li>
</ul>
<h6><a id="3_jQuery__1275"></a>3. jQuery 中添加事件委托</h6>
<ul>
<li>添加前
<ul>
<li>$(“li”).click隐式迭代给界面上所有li都添加了click事件(监听数量众多)</li>
<li>通过$(“ul”).append新添加的li无法影响click事件</li>
</ul>
</li>
</ul>
<pre class="prettyprint"><code class="prism language-html has-numbering" onclick="mdcp.copyCode(event)" style="position: unset;"><span class="token doctype">&lt;!DOCTYPE html&gt;</span>
<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>html</span> <span class="token attr-name">lang</span><span class="token attr-value"><span class="token punctuation">=</span><span class="token punctuation">"</span>en<span class="token punctuation">"</span></span><span class="token punctuation">&gt;</span></span>
<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>head</span><span class="token punctuation">&gt;</span></span>
    <span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>meta</span> <span class="token attr-name">charset</span><span class="token attr-value"><span class="token punctuation">=</span><span class="token punctuation">"</span>UTF-8<span class="token punctuation">"</span></span><span class="token punctuation">&gt;</span></span>
    <span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>title</span><span class="token punctuation">&gt;</span></span>18-jQuery事件委托<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>title</span><span class="token punctuation">&gt;</span></span>
    <span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>script</span> <span class="token attr-name">src</span><span class="token attr-value"><span class="token punctuation">=</span><span class="token punctuation">"</span>../day01/代码/js/jquery-1.12.4.js<span class="token punctuation">"</span></span><span class="token punctuation">&gt;</span></span><span class="token script language-javascript"></span><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>script</span><span class="token punctuation">&gt;</span></span>
    <span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>script</span><span class="token punctuation">&gt;</span></span><span class="token script language-javascript">
        <span class="token function">$</span><span class="token punctuation">(</span><span class="token keyword">function</span> <span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
            <span class="token comment">// 1.监听li点击事件</span>
            <span class="token function">$</span><span class="token punctuation">(</span><span class="token string">"li"</span><span class="token punctuation">)</span><span class="token punctuation">.</span><span class="token function">click</span><span class="token punctuation">(</span><span class="token keyword">function</span> <span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
                <span class="token comment">// 弹出当前点击行内容</span>
                <span class="token function">alert</span><span class="token punctuation">(</span><span class="token function">$</span><span class="token punctuation">(</span><span class="token keyword">this</span><span class="token punctuation">)</span><span class="token punctuation">.</span><span class="token function">html</span><span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
            <span class="token punctuation">}</span><span class="token punctuation">)</span><span class="token punctuation">;</span>

            <span class="token comment">// 2.监听新增按钮点击</span>
            <span class="token keyword">var</span> count <span class="token operator">=</span> <span class="token number">0</span><span class="token punctuation">;</span>
            <span class="token function">$</span><span class="token punctuation">(</span><span class="token string">"button"</span><span class="token punctuation">)</span><span class="token punctuation">.</span><span class="token function">eq</span><span class="token punctuation">(</span><span class="token number">0</span><span class="token punctuation">)</span><span class="token punctuation">.</span><span class="token function">click</span><span class="token punctuation">(</span><span class="token keyword">function</span> <span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
                count<span class="token operator">++</span><span class="token punctuation">;</span>
                <span class="token comment">// 新增一行内容</span>
                <span class="token function">$</span><span class="token punctuation">(</span><span class="token string">"ul"</span><span class="token punctuation">)</span><span class="token punctuation">.</span><span class="token function">append</span><span class="token punctuation">(</span><span class="token string">"&lt;li&gt;我是新增内容"</span><span class="token operator">+</span>count<span class="token operator">+</span><span class="token string">"&lt;/li&gt;"</span><span class="token punctuation">)</span>
            <span class="token punctuation">}</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
        <span class="token punctuation">}</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
    </span><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>script</span><span class="token punctuation">&gt;</span></span>
<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>head</span><span class="token punctuation">&gt;</span></span>
<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>body</span><span class="token punctuation">&gt;</span></span>
<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>ul</span><span class="token punctuation">&gt;</span></span>
    <span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>li</span><span class="token punctuation">&gt;</span></span>我是第1行<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>li</span><span class="token punctuation">&gt;</span></span>
    <span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>li</span><span class="token punctuation">&gt;</span></span>我是第2行<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>li</span><span class="token punctuation">&gt;</span></span>
    <span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>li</span><span class="token punctuation">&gt;</span></span>我是第3行<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>li</span><span class="token punctuation">&gt;</span></span>
<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>ul</span><span class="token punctuation">&gt;</span></span>
<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>button</span><span class="token punctuation">&gt;</span></span>新增一行<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>button</span><span class="token punctuation">&gt;</span></span>
<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>button</span><span class="token punctuation">&gt;</span></span>移除事件委托<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>button</span><span class="token punctuation">&gt;</span></span>
<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>body</span><span class="token punctuation">&gt;</span></span>
<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>html</span><span class="token punctuation">&gt;</span></span>
<div class="hljs-button {2}" data-title="复制"></div></code><ul class="pre-numbering" style=""><li style="color: rgb(153, 153, 153);">1</li><li style="color: rgb(153, 153, 153);">2</li><li style="color: rgb(153, 153, 153);">3</li><li style="color: rgb(153, 153, 153);">4</li><li style="color: rgb(153, 153, 153);">5</li><li style="color: rgb(153, 153, 153);">6</li><li style="color: rgb(153, 153, 153);">7</li><li style="color: rgb(153, 153, 153);">8</li><li style="color: rgb(153, 153, 153);">9</li><li style="color: rgb(153, 153, 153);">10</li><li style="color: rgb(153, 153, 153);">11</li><li style="color: rgb(153, 153, 153);">12</li><li style="color: rgb(153, 153, 153);">13</li><li style="color: rgb(153, 153, 153);">14</li><li style="color: rgb(153, 153, 153);">15</li><li style="color: rgb(153, 153, 153);">16</li><li style="color: rgb(153, 153, 153);">17</li><li style="color: rgb(153, 153, 153);">18</li><li style="color: rgb(153, 153, 153);">19</li><li style="color: rgb(153, 153, 153);">20</li><li style="color: rgb(153, 153, 153);">21</li><li style="color: rgb(153, 153, 153);">22</li><li style="color: rgb(153, 153, 153);">23</li><li style="color: rgb(153, 153, 153);">24</li><li style="color: rgb(153, 153, 153);">25</li><li style="color: rgb(153, 153, 153);">26</li><li style="color: rgb(153, 153, 153);">27</li><li style="color: rgb(153, 153, 153);">28</li><li style="color: rgb(153, 153, 153);">29</li><li style="color: rgb(153, 153, 153);">30</li><li style="color: rgb(153, 153, 153);">31</li><li style="color: rgb(153, 153, 153);">32</li><li style="color: rgb(153, 153, 153);">33</li><li style="color: rgb(153, 153, 153);">34</li></ul></pre>
<ul>
<li>添加后
<ul>
<li>格式:$(parentSelector).delegate(childrenSelector, eventName, callback)</li>
<li>$(“ul”).delegate隐式迭代所有ul添加事件(相比开始迭代li,必然ul的个数会少很多)</li>
<li>当事件被触发时,系统会自动动态查找当前是哪个li触发了事件,所以新增的li也能响应到事件</li>
</ul>
</li>
</ul>
<pre class="prettyprint"><code class="prism language-html has-numbering" onclick="mdcp.copyCode(event)" style="position: unset;"><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>script</span><span class="token punctuation">&gt;</span></span><span class="token script language-javascript">
     <span class="token function">$</span><span class="token punctuation">(</span><span class="token keyword">function</span> <span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
         <span class="token comment">// 1.委托ul监听li的点击事件</span>
         <span class="token function">$</span><span class="token punctuation">(</span><span class="token string">"ul"</span><span class="token punctuation">)</span><span class="token punctuation">.</span><span class="token function">delegate</span><span class="token punctuation">(</span><span class="token string">"li"</span><span class="token punctuation">,</span><span class="token string">"click"</span><span class="token punctuation">,</span><span class="token keyword">function</span> <span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
             <span class="token comment">// 前面我们说过事件委托就是让别人帮忙做事,但最终的结果还是会返回到我们手里,所以这里的this是触发事件的li</span>
             <span class="token comment">// 这里的this之所以是触发事件的li,本质是因为"事件冒泡", 触发事件的li向上传递到ul,触发了click事件.</span>
    <span class="token comment">// console.log(this);</span>
             <span class="token comment">// 弹出当前点击行内容</span>
             <span class="token function">alert</span><span class="token punctuation">(</span><span class="token function">$</span><span class="token punctuation">(</span><span class="token keyword">this</span><span class="token punctuation">)</span><span class="token punctuation">.</span><span class="token function">html</span><span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
         <span class="token punctuation">}</span><span class="token punctuation">)</span><span class="token punctuation">;</span>

         <span class="token comment">// 2.监听新增按钮点击</span>
         <span class="token keyword">var</span> count <span class="token operator">=</span> <span class="token number">0</span><span class="token punctuation">;</span>
         <span class="token function">$</span><span class="token punctuation">(</span><span class="token string">"button"</span><span class="token punctuation">)</span><span class="token punctuation">.</span><span class="token function">eq</span><span class="token punctuation">(</span><span class="token number">0</span><span class="token punctuation">)</span><span class="token punctuation">.</span><span class="token function">click</span><span class="token punctuation">(</span><span class="token keyword">function</span> <span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
             count<span class="token operator">++</span><span class="token punctuation">;</span>
             <span class="token comment">// 新增一行内容</span>
             <span class="token function">$</span><span class="token punctuation">(</span><span class="token string">"ul"</span><span class="token punctuation">)</span><span class="token punctuation">.</span><span class="token function">append</span><span class="token punctuation">(</span><span class="token string">"&lt;li&gt;我是新增内容"</span><span class="token operator">+</span>count<span class="token operator">+</span><span class="token string">"&lt;/li&gt;"</span><span class="token punctuation">)</span>
         <span class="token punctuation">}</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
     <span class="token punctuation">}</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
</span><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>script</span><span class="token punctuation">&gt;</span></span>
<div class="hljs-button {2}" data-title="复制"></div></code><ul class="pre-numbering" style=""><li style="color: rgb(153, 153, 153);">1</li><li style="color: rgb(153, 153, 153);">2</li><li style="color: rgb(153, 153, 153);">3</li><li style="color: rgb(153, 153, 153);">4</li><li style="color: rgb(153, 153, 153);">5</li><li style="color: rgb(153, 153, 153);">6</li><li style="color: rgb(153, 153, 153);">7</li><li style="color: rgb(153, 153, 153);">8</li><li style="color: rgb(153, 153, 153);">9</li><li style="color: rgb(153, 153, 153);">10</li><li style="color: rgb(153, 153, 153);">11</li><li style="color: rgb(153, 153, 153);">12</li><li style="color: rgb(153, 153, 153);">13</li><li style="color: rgb(153, 153, 153);">14</li><li style="color: rgb(153, 153, 153);">15</li><li style="color: rgb(153, 153, 153);">16</li><li style="color: rgb(153, 153, 153);">17</li><li style="color: rgb(153, 153, 153);">18</li><li style="color: rgb(153, 153, 153);">19</li><li style="color: rgb(153, 153, 153);">20</li></ul></pre>
<h4><a id="10__1342"></a>10. 移入移出事件</h4>
<h6><a id="1_mouseentermouseleave_1343"></a>1. mouseenter/mouseleave</h6>
<ul>
<li>移动到子元素不会触发事件</li>
</ul>
<pre class="prettyprint"><code class="prism language-html has-numbering" onclick="mdcp.copyCode(event)" style="position: unset;"><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>script</span><span class="token punctuation">&gt;</span></span><span class="token script language-javascript">
    <span class="token function">$</span><span class="token punctuation">(</span><span class="token keyword">function</span> <span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
        <span class="token comment">// 移动到子元素不会触发事件</span>
         <span class="token comment">// 2.1移入事件</span>
         <span class="token function">$</span><span class="token punctuation">(</span><span class="token string">'.father'</span><span class="token punctuation">)</span><span class="token punctuation">.</span><span class="token function">mouseenter</span><span class="token punctuation">(</span><span class="token keyword">function</span> <span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
           console<span class="token punctuation">.</span><span class="token function">log</span><span class="token punctuation">(</span><span class="token string">'mouseenter'</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
         <span class="token punctuation">}</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
         <span class="token comment">// 2.2移除事件</span>
         <span class="token function">$</span><span class="token punctuation">(</span><span class="token string">'.father'</span><span class="token punctuation">)</span><span class="token punctuation">.</span><span class="token function">mouseleave</span><span class="token punctuation">(</span><span class="token keyword">function</span> <span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
           console<span class="token punctuation">.</span><span class="token function">log</span><span class="token punctuation">(</span><span class="token string">'mouseleave'</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
         <span class="token punctuation">}</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
    <span class="token punctuation">}</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
</span><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>script</span><span class="token punctuation">&gt;</span></span>
<div class="hljs-button {2}" data-title="复制"></div></code><ul class="pre-numbering" style=""><li style="color: rgb(153, 153, 153);">1</li><li style="color: rgb(153, 153, 153);">2</li><li style="color: rgb(153, 153, 153);">3</li><li style="color: rgb(153, 153, 153);">4</li><li style="color: rgb(153, 153, 153);">5</li><li style="color: rgb(153, 153, 153);">6</li><li style="color: rgb(153, 153, 153);">7</li><li style="color: rgb(153, 153, 153);">8</li><li style="color: rgb(153, 153, 153);">9</li><li style="color: rgb(153, 153, 153);">10</li><li style="color: rgb(153, 153, 153);">11</li><li style="color: rgb(153, 153, 153);">12</li><li style="color: rgb(153, 153, 153);">13</li></ul></pre>
<h6><a id="2_mouseovermouseout_1361"></a>2. mouseover/mouseout</h6>
<ul>
<li>移动到子元素会触发事件</li>
</ul>
<pre class="prettyprint"><code class="prism language-html has-numbering" onclick="mdcp.copyCode(event)" style="position: unset;"><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>script</span><span class="token punctuation">&gt;</span></span><span class="token script language-javascript">
     <span class="token function">$</span><span class="token punctuation">(</span><span class="token keyword">function</span> <span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
          <span class="token comment">// 2.1移入事件</span>
          <span class="token function">$</span><span class="token punctuation">(</span><span class="token string">'.father'</span><span class="token punctuation">)</span><span class="token punctuation">.</span><span class="token function">mouseover</span><span class="token punctuation">(</span><span class="token keyword">function</span> <span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
            console<span class="token punctuation">.</span><span class="token function">log</span><span class="token punctuation">(</span><span class="token string">'mouseover'</span><span class="token punctuation">)</span> <span class="token punctuation">;</span>
          <span class="token punctuation">}</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
          <span class="token comment">// 2.2移除事件</span>
          <span class="token function">$</span><span class="token punctuation">(</span><span class="token string">'.father'</span><span class="token punctuation">)</span><span class="token punctuation">.</span><span class="token function">mouseout</span><span class="token punctuation">(</span><span class="token keyword">function</span> <span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
            console<span class="token punctuation">.</span><span class="token function">log</span><span class="token punctuation">(</span><span class="token string">'mouseout'</span><span class="token punctuation">)</span> <span class="token punctuation">;</span>
          <span class="token punctuation">}</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
     <span class="token punctuation">}</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
</span><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>script</span><span class="token punctuation">&gt;</span></span>
<div class="hljs-button {2}" data-title="复制"></div></code><ul class="pre-numbering" style=""><li style="color: rgb(153, 153, 153);">1</li><li style="color: rgb(153, 153, 153);">2</li><li style="color: rgb(153, 153, 153);">3</li><li style="color: rgb(153, 153, 153);">4</li><li style="color: rgb(153, 153, 153);">5</li><li style="color: rgb(153, 153, 153);">6</li><li style="color: rgb(153, 153, 153);">7</li><li style="color: rgb(153, 153, 153);">8</li><li style="color: rgb(153, 153, 153);">9</li><li style="color: rgb(153, 153, 153);">10</li><li style="color: rgb(153, 153, 153);">11</li><li style="color: rgb(153, 153, 153);">12</li></ul></pre>
<h6><a id="3_hover_1378"></a>3. hover</h6>
<ul>
<li>内容监听移入和移出</li>
<li>内部实现就是调用mouseenter和mouseleave</li>
</ul>
<pre class="prettyprint"><code class="prism language-html has-numbering" onclick="mdcp.copyCode(event)" style="position: unset;"><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>script</span><span class="token punctuation">&gt;</span></span><span class="token script language-javascript">
     <span class="token function">$</span><span class="token punctuation">(</span><span class="token keyword">function</span> <span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
         <span class="token comment">/*
        // 传入两个回调函数,一个监听移入,一个监听移出
         $(".father").hover(function () {
             console.log("mouseenter");
         }, function () {
             console.log("mouseleave");
         });
         */</span>
         <span class="token comment">// 如果只传入一个方式,那么这个方式既监听移入也监听移出</span>
         <span class="token function">$</span><span class="token punctuation">(</span><span class="token string">".father"</span><span class="token punctuation">)</span><span class="token punctuation">.</span><span class="token function">hover</span><span class="token punctuation">(</span><span class="token keyword">function</span> <span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
             console<span class="token punctuation">.</span><span class="token function">log</span><span class="token punctuation">(</span><span class="token string">"移入移除"</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
         <span class="token punctuation">}</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
     <span class="token punctuation">}</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
</span><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>script</span><span class="token punctuation">&gt;</span></span>
<div class="hljs-button {2}" data-title="复制"></div></code><ul class="pre-numbering" style=""><li style="color: rgb(153, 153, 153);">1</li><li style="color: rgb(153, 153, 153);">2</li><li style="color: rgb(153, 153, 153);">3</li><li style="color: rgb(153, 153, 153);">4</li><li style="color: rgb(153, 153, 153);">5</li><li style="color: rgb(153, 153, 153);">6</li><li style="color: rgb(153, 153, 153);">7</li><li style="color: rgb(153, 153, 153);">8</li><li style="color: rgb(153, 153, 153);">9</li><li style="color: rgb(153, 153, 153);">10</li><li style="color: rgb(153, 153, 153);">11</li><li style="color: rgb(153, 153, 153);">12</li><li style="color: rgb(153, 153, 153);">13</li><li style="color: rgb(153, 153, 153);">14</li><li style="color: rgb(153, 153, 153);">15</li><li style="color: rgb(153, 153, 153);">16</li></ul></pre>
<h2><a name="t11"></a><a id="11_jQuery__1400"></a>11. jQuery 动画效果</h2>
<h4><a id="1__1401"></a>1. 显示，隐藏动画</h4>
<h6><a id="1_show_1402"></a>1. show</h6>
<ul>
<li>显示动画</li>
<li>内部实现原理根据当前操作的元素是块级还是行内决定, 块级内部调用display:block;,行内内部调用display:inline;</li>
</ul>
<pre class="prettyprint"><code class="prism language-js has-numbering" onclick="mdcp.copyCode(event)" style="position: unset;"><span class="token comment">// 编写jQuery相关代码</span>
<span class="token function">$</span><span class="token punctuation">(</span><span class="token string">"button"</span><span class="token punctuation">)</span><span class="token punctuation">.</span><span class="token function">eq</span><span class="token punctuation">(</span><span class="token number">0</span><span class="token punctuation">)</span><span class="token punctuation">.</span><span class="token function">click</span><span class="token punctuation">(</span><span class="token keyword">function</span> <span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
    <span class="token comment">// $("div").css("display", "block");</span>
    <span class="token comment">// 注意: 这里的时间是毫秒</span>
    <span class="token function">$</span><span class="token punctuation">(</span><span class="token string">"div"</span><span class="token punctuation">)</span><span class="token punctuation">.</span><span class="token function">show</span><span class="token punctuation">(</span><span class="token number">1000</span><span class="token punctuation">,</span> <span class="token keyword">function</span> <span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
        <span class="token comment">// 作用: 动画执行完毕之后调用</span>
        <span class="token function">alert</span><span class="token punctuation">(</span><span class="token string">"显示动画执行完毕"</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
    <span class="token punctuation">}</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
<span class="token punctuation">}</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
<div class="hljs-button {2}" data-title="复制"></div></code><ul class="pre-numbering" style=""><li style="color: rgb(153, 153, 153);">1</li><li style="color: rgb(153, 153, 153);">2</li><li style="color: rgb(153, 153, 153);">3</li><li style="color: rgb(153, 153, 153);">4</li><li style="color: rgb(153, 153, 153);">5</li><li style="color: rgb(153, 153, 153);">6</li><li style="color: rgb(153, 153, 153);">7</li><li style="color: rgb(153, 153, 153);">8</li><li style="color: rgb(153, 153, 153);">9</li></ul></pre>
<h6><a id="2_hide_1417"></a>2. hide</h6>
<ul>
<li>隐藏动画</li>
</ul>
<pre class="prettyprint"><code class="prism language-js has-numbering" onclick="mdcp.copyCode(event)" style="position: unset;"><span class="token function">$</span><span class="token punctuation">(</span><span class="token string">"button"</span><span class="token punctuation">)</span><span class="token punctuation">.</span><span class="token function">eq</span><span class="token punctuation">(</span><span class="token number">1</span><span class="token punctuation">)</span><span class="token punctuation">.</span><span class="token function">click</span><span class="token punctuation">(</span><span class="token keyword">function</span> <span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
    <span class="token comment">// $("div").css("display", "none");</span>
    <span class="token function">$</span><span class="token punctuation">(</span><span class="token string">"div"</span><span class="token punctuation">)</span><span class="token punctuation">.</span><span class="token function">hide</span><span class="token punctuation">(</span><span class="token number">1000</span><span class="token punctuation">,</span> <span class="token keyword">function</span> <span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
        <span class="token function">alert</span><span class="token punctuation">(</span><span class="token string">"隐藏动画执行完毕"</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
    <span class="token punctuation">}</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
<span class="token punctuation">}</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
<div class="hljs-button {2}" data-title="复制"></div></code><ul class="pre-numbering" style=""><li style="color: rgb(153, 153, 153);">1</li><li style="color: rgb(153, 153, 153);">2</li><li style="color: rgb(153, 153, 153);">3</li><li style="color: rgb(153, 153, 153);">4</li><li style="color: rgb(153, 153, 153);">5</li><li style="color: rgb(153, 153, 153);">6</li></ul></pre>
<h6><a id="3_toggle_1428"></a>3. toggle</h6>
<ul>
<li>切换动画（显示变隐藏，隐藏变显示）</li>
</ul>
<pre class="prettyprint"><code class="prism language-js has-numbering" onclick="mdcp.copyCode(event)" style="position: unset;"><span class="token function">$</span><span class="token punctuation">(</span><span class="token string">"button"</span><span class="token punctuation">)</span><span class="token punctuation">.</span><span class="token function">eq</span><span class="token punctuation">(</span><span class="token number">2</span><span class="token punctuation">)</span><span class="token punctuation">.</span><span class="token function">click</span><span class="token punctuation">(</span><span class="token keyword">function</span> <span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
    <span class="token function">$</span><span class="token punctuation">(</span><span class="token string">"div"</span><span class="token punctuation">)</span><span class="token punctuation">.</span><span class="token function">toggle</span><span class="token punctuation">(</span><span class="token number">1000</span><span class="token punctuation">,</span> <span class="token keyword">function</span> <span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
        <span class="token function">alert</span><span class="token punctuation">(</span><span class="token string">"切换动画执行完毕"</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
    <span class="token punctuation">}</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
<span class="token punctuation">}</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
<div class="hljs-button {2}" data-title="复制"></div></code><ul class="pre-numbering" style=""><li style="color: rgb(153, 153, 153);">1</li><li style="color: rgb(153, 153, 153);">2</li><li style="color: rgb(153, 153, 153);">3</li><li style="color: rgb(153, 153, 153);">4</li><li style="color: rgb(153, 153, 153);">5</li></ul></pre>
<h6><a id="4__1439"></a>4. 注意点</h6>
<ul>
<li>show(1000, function () {}😉 第一个参数单位是毫秒, 1000毫秒等于1秒</li>
<li>默认的动画时长是400毫秒</li>
<li>除了指定毫秒以外还可以指定三个预设参数 slow、normal、fast
<ul>
<li>slow本质是600毫秒</li>
<li>normal本质是400毫秒</li>
<li>fast本质是200毫秒</li>
</ul>
</li>
<li>其它两个方法同理可证</li>
</ul>
<h4><a id="2__1448"></a>2. 展开，收起动画</h4>
<h6><a id="1_slideDown_1449"></a>1. slideDown</h6>
<ul>
<li>展开动画</li>
</ul>
<pre class="prettyprint"><code class="prism language-js has-numbering" onclick="mdcp.copyCode(event)" style="position: unset;"><span class="token function">$</span><span class="token punctuation">(</span><span class="token string">"button"</span><span class="token punctuation">)</span><span class="token punctuation">.</span><span class="token function">eq</span><span class="token punctuation">(</span><span class="token number">0</span><span class="token punctuation">)</span><span class="token punctuation">.</span><span class="token function">click</span><span class="token punctuation">(</span><span class="token keyword">function</span> <span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
    <span class="token function">$</span><span class="token punctuation">(</span><span class="token string">"div"</span><span class="token punctuation">)</span><span class="token punctuation">.</span><span class="token function">slideDown</span><span class="token punctuation">(</span><span class="token number">1000</span><span class="token punctuation">,</span> <span class="token keyword">function</span> <span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
        <span class="token function">alert</span><span class="token punctuation">(</span><span class="token string">"展开完毕"</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
    <span class="token punctuation">}</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
<span class="token punctuation">}</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
<div class="hljs-button {2}" data-title="复制"></div></code><ul class="pre-numbering" style=""><li style="color: rgb(153, 153, 153);">1</li><li style="color: rgb(153, 153, 153);">2</li><li style="color: rgb(153, 153, 153);">3</li><li style="color: rgb(153, 153, 153);">4</li><li style="color: rgb(153, 153, 153);">5</li></ul></pre>
<h6><a id="2_slideUp_1458"></a>2. slideUp</h6>
<ul>
<li>收起动画</li>
</ul>
<pre class="prettyprint"><code class="prism language-js has-numbering" onclick="mdcp.copyCode(event)" style="position: unset;"><span class="token function">$</span><span class="token punctuation">(</span><span class="token string">"button"</span><span class="token punctuation">)</span><span class="token punctuation">.</span><span class="token function">eq</span><span class="token punctuation">(</span><span class="token number">1</span><span class="token punctuation">)</span><span class="token punctuation">.</span><span class="token function">click</span><span class="token punctuation">(</span><span class="token keyword">function</span> <span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
    <span class="token function">$</span><span class="token punctuation">(</span><span class="token string">"div"</span><span class="token punctuation">)</span><span class="token punctuation">.</span><span class="token function">slideUp</span><span class="token punctuation">(</span><span class="token number">1000</span><span class="token punctuation">,</span> <span class="token keyword">function</span> <span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
        <span class="token function">alert</span><span class="token punctuation">(</span><span class="token string">"收起完毕"</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
    <span class="token punctuation">}</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
<span class="token punctuation">}</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
<div class="hljs-button {2}" data-title="复制"></div></code><ul class="pre-numbering" style=""><li style="color: rgb(153, 153, 153);">1</li><li style="color: rgb(153, 153, 153);">2</li><li style="color: rgb(153, 153, 153);">3</li><li style="color: rgb(153, 153, 153);">4</li><li style="color: rgb(153, 153, 153);">5</li></ul></pre>
<h6><a id="3_slideToggle_1467"></a>3. slideToggle</h6>
<ul>
<li>切换动画（ 展开变收起,收起变展开）</li>
</ul>
<pre class="prettyprint"><code class="prism language-js has-numbering" onclick="mdcp.copyCode(event)" style="position: unset;"><span class="token function">$</span><span class="token punctuation">(</span><span class="token string">"button"</span><span class="token punctuation">)</span><span class="token punctuation">.</span><span class="token function">eq</span><span class="token punctuation">(</span><span class="token number">2</span><span class="token punctuation">)</span><span class="token punctuation">.</span><span class="token function">click</span><span class="token punctuation">(</span><span class="token keyword">function</span> <span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
    <span class="token function">$</span><span class="token punctuation">(</span><span class="token string">"div"</span><span class="token punctuation">)</span><span class="token punctuation">.</span><span class="token function">slideToggle</span><span class="token punctuation">(</span><span class="token number">1000</span><span class="token punctuation">,</span> <span class="token keyword">function</span> <span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
        <span class="token function">alert</span><span class="token punctuation">(</span><span class="token string">"收起完毕"</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
    <span class="token punctuation">}</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
<span class="token punctuation">}</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
<div class="hljs-button {2}" data-title="复制"></div></code><ul class="pre-numbering" style=""><li style="color: rgb(153, 153, 153);">1</li><li style="color: rgb(153, 153, 153);">2</li><li style="color: rgb(153, 153, 153);">3</li><li style="color: rgb(153, 153, 153);">4</li><li style="color: rgb(153, 153, 153);">5</li></ul></pre>
<h4><a id="3__1477"></a>3. 淡入，淡出动画</h4>
<h6><a id="1_fadeIn_1478"></a>1. fadeIn</h6>
<ul>
<li>淡入动画</li>
</ul>
<pre class="prettyprint"><code class="prism language-js has-numbering" onclick="mdcp.copyCode(event)" style="position: unset;"><span class="token function">$</span><span class="token punctuation">(</span><span class="token string">"button"</span><span class="token punctuation">)</span><span class="token punctuation">.</span><span class="token function">eq</span><span class="token punctuation">(</span><span class="token number">0</span><span class="token punctuation">)</span><span class="token punctuation">.</span><span class="token function">click</span><span class="token punctuation">(</span><span class="token keyword">function</span> <span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
    <span class="token function">$</span><span class="token punctuation">(</span><span class="token string">"div"</span><span class="token punctuation">)</span><span class="token punctuation">.</span><span class="token function">fadeIn</span><span class="token punctuation">(</span><span class="token number">1000</span><span class="token punctuation">,</span> <span class="token keyword">function</span> <span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
        <span class="token function">alert</span><span class="token punctuation">(</span><span class="token string">"淡入完毕"</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
    <span class="token punctuation">}</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
<span class="token punctuation">}</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
<div class="hljs-button {2}" data-title="复制"></div></code><ul class="pre-numbering" style=""><li style="color: rgb(153, 153, 153);">1</li><li style="color: rgb(153, 153, 153);">2</li><li style="color: rgb(153, 153, 153);">3</li><li style="color: rgb(153, 153, 153);">4</li><li style="color: rgb(153, 153, 153);">5</li></ul></pre>
<h6><a id="2_fadeOut_1487"></a>2. fadeOut</h6>
<ul>
<li>淡出动画</li>
</ul>
<pre class="prettyprint"><code class="prism language-js has-numbering" onclick="mdcp.copyCode(event)" style="position: unset;"><span class="token function">$</span><span class="token punctuation">(</span><span class="token string">"button"</span><span class="token punctuation">)</span><span class="token punctuation">.</span><span class="token function">eq</span><span class="token punctuation">(</span><span class="token number">1</span><span class="token punctuation">)</span><span class="token punctuation">.</span><span class="token function">click</span><span class="token punctuation">(</span><span class="token keyword">function</span> <span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
    <span class="token function">$</span><span class="token punctuation">(</span><span class="token string">"div"</span><span class="token punctuation">)</span><span class="token punctuation">.</span><span class="token function">fadeOut</span><span class="token punctuation">(</span><span class="token number">1000</span><span class="token punctuation">,</span> <span class="token keyword">function</span> <span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
        <span class="token function">alert</span><span class="token punctuation">(</span><span class="token string">"淡出完毕"</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
    <span class="token punctuation">}</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
<span class="token punctuation">}</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
<div class="hljs-button {2}" data-title="复制"></div></code><ul class="pre-numbering" style=""><li style="color: rgb(153, 153, 153);">1</li><li style="color: rgb(153, 153, 153);">2</li><li style="color: rgb(153, 153, 153);">3</li><li style="color: rgb(153, 153, 153);">4</li><li style="color: rgb(153, 153, 153);">5</li></ul></pre>
<h6><a id="3_fadeToggle_1496"></a>3. fadeToggle</h6>
<ul>
<li>切换动画（显示变淡出，不显示变淡入）</li>
</ul>
<pre class="prettyprint"><code class="prism language-js has-numbering" onclick="mdcp.copyCode(event)" style="position: unset;"><span class="token function">$</span><span class="token punctuation">(</span><span class="token string">"button"</span><span class="token punctuation">)</span><span class="token punctuation">.</span><span class="token function">eq</span><span class="token punctuation">(</span><span class="token number">2</span><span class="token punctuation">)</span><span class="token punctuation">.</span><span class="token function">click</span><span class="token punctuation">(</span><span class="token keyword">function</span> <span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
    <span class="token function">$</span><span class="token punctuation">(</span><span class="token string">"div"</span><span class="token punctuation">)</span><span class="token punctuation">.</span><span class="token function">fadeToggle</span><span class="token punctuation">(</span><span class="token number">1000</span><span class="token punctuation">,</span> <span class="token keyword">function</span> <span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
        <span class="token function">alert</span><span class="token punctuation">(</span><span class="token string">"切换完毕"</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
    <span class="token punctuation">}</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
<span class="token punctuation">}</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
<div class="hljs-button {2}" data-title="复制"></div></code><ul class="pre-numbering" style=""><li style="color: rgb(153, 153, 153);">1</li><li style="color: rgb(153, 153, 153);">2</li><li style="color: rgb(153, 153, 153);">3</li><li style="color: rgb(153, 153, 153);">4</li><li style="color: rgb(153, 153, 153);">5</li></ul></pre>
<h6><a id="4_fadeTo_1505"></a>4. fadeTo</h6>
<ul>
<li>淡入到指定透明度动画</li>
<li>可以通过第二个参数,淡入到指定的透明度(取值范围0~1)</li>
</ul>
<pre class="prettyprint"><code class="prism language-js has-numbering" onclick="mdcp.copyCode(event)" style="position: unset;"><span class="token function">$</span><span class="token punctuation">(</span><span class="token string">"button"</span><span class="token punctuation">)</span><span class="token punctuation">.</span><span class="token function">eq</span><span class="token punctuation">(</span><span class="token number">3</span><span class="token punctuation">)</span><span class="token punctuation">.</span><span class="token function">click</span><span class="token punctuation">(</span><span class="token keyword">function</span> <span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
    <span class="token function">$</span><span class="token punctuation">(</span><span class="token string">"div"</span><span class="token punctuation">)</span><span class="token punctuation">.</span><span class="token function">fadeTo</span><span class="token punctuation">(</span><span class="token number">1000</span><span class="token punctuation">,</span> <span class="token number">0.2</span><span class="token punctuation">,</span> <span class="token keyword">function</span> <span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
        <span class="token function">alert</span><span class="token punctuation">(</span><span class="token string">"淡入完毕"</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
    <span class="token punctuation">}</span><span class="token punctuation">)</span>
<span class="token punctuation">}</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
<div class="hljs-button {2}" data-title="复制"></div></code><ul class="pre-numbering" style=""><li style="color: rgb(153, 153, 153);">1</li><li style="color: rgb(153, 153, 153);">2</li><li style="color: rgb(153, 153, 153);">3</li><li style="color: rgb(153, 153, 153);">4</li><li style="color: rgb(153, 153, 153);">5</li></ul></pre>
<h4><a id="4__1516"></a>4. 自定义动画</h4>
<h6><a id="1_animate_1517"></a>1. animate</h6>
<pre class="prettyprint"><code class="prism language-js has-numbering" onclick="mdcp.copyCode(event)" style="position: unset;"><span class="token comment">/*
第一个参数: 接收一个对象, 可以在对象中修改属性
第二个参数: 指定动画时长
第三个参数: 指定动画节奏, 默认就是swing
第四个参数: 动画执行完毕之后的回调函数
*/</span>
<span class="token function">$</span><span class="token punctuation">(</span><span class="token string">".two"</span><span class="token punctuation">)</span><span class="token punctuation">.</span><span class="token function">animate</span><span class="token punctuation">(</span><span class="token punctuation">{</span>
    marginLeft<span class="token punctuation">:</span> <span class="token number">500</span>
<span class="token punctuation">}</span><span class="token punctuation">,</span> <span class="token number">5000</span><span class="token punctuation">,</span> <span class="token string">"linear"</span><span class="token punctuation">,</span> <span class="token keyword">function</span> <span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
    <span class="token comment">// alert("自定义动画执行完毕");</span>
<span class="token punctuation">}</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
<div class="hljs-button {2}" data-title="复制"></div></code><ul class="pre-numbering" style=""><li style="color: rgb(153, 153, 153);">1</li><li style="color: rgb(153, 153, 153);">2</li><li style="color: rgb(153, 153, 153);">3</li><li style="color: rgb(153, 153, 153);">4</li><li style="color: rgb(153, 153, 153);">5</li><li style="color: rgb(153, 153, 153);">6</li><li style="color: rgb(153, 153, 153);">7</li><li style="color: rgb(153, 153, 153);">8</li><li style="color: rgb(153, 153, 153);">9</li><li style="color: rgb(153, 153, 153);">10</li><li style="color: rgb(153, 153, 153);">11</li></ul></pre>
<ul>
<li>每次开始运动都必须是初始位置或者初始状态,如果想在上一次位置或者状态下再次进行动画可以使用累加动画</li>
</ul>
<pre class="prettyprint"><code class="prism language-js has-numbering" onclick="mdcp.copyCode(event)" style="position: unset;"><span class="token function">$</span><span class="token punctuation">(</span><span class="token string">"button"</span><span class="token punctuation">)</span><span class="token punctuation">.</span><span class="token function">eq</span><span class="token punctuation">(</span><span class="token number">1</span><span class="token punctuation">)</span><span class="token punctuation">.</span><span class="token function">click</span><span class="token punctuation">(</span><span class="token keyword">function</span> <span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
    <span class="token function">$</span><span class="token punctuation">(</span><span class="token string">".one"</span><span class="token punctuation">)</span><span class="token punctuation">.</span><span class="token function">animate</span><span class="token punctuation">(</span><span class="token punctuation">{</span>
        width<span class="token punctuation">:</span> <span class="token string">"+=100"</span>
    <span class="token punctuation">}</span><span class="token punctuation">,</span> <span class="token number">1000</span><span class="token punctuation">,</span> <span class="token keyword">function</span> <span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
        <span class="token function">alert</span><span class="token punctuation">(</span><span class="token string">"自定义动画执行完毕"</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
    <span class="token punctuation">}</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
<span class="token punctuation">}</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
<div class="hljs-button {2}" data-title="复制"></div></code><ul class="pre-numbering" style=""><li style="color: rgb(153, 153, 153);">1</li><li style="color: rgb(153, 153, 153);">2</li><li style="color: rgb(153, 153, 153);">3</li><li style="color: rgb(153, 153, 153);">4</li><li style="color: rgb(153, 153, 153);">5</li><li style="color: rgb(153, 153, 153);">6</li><li style="color: rgb(153, 153, 153);">7</li></ul></pre>
<ul>
<li>同时操作多个属性,自定义动画会执行同步动画,多个被操作的属性一起执行动画</li>
</ul>
<pre class="prettyprint"><code class="prism language-js has-numbering" onclick="mdcp.copyCode(event)" style="position: unset;"><span class="token function">$</span><span class="token punctuation">(</span><span class="token string">".one"</span><span class="token punctuation">)</span><span class="token punctuation">.</span><span class="token function">animate</span><span class="token punctuation">(</span><span class="token punctuation">{</span>
    width<span class="token punctuation">:</span> <span class="token number">500</span><span class="token punctuation">,</span>
    height<span class="token punctuation">:</span> <span class="token number">500</span>
<span class="token punctuation">}</span><span class="token punctuation">,</span> <span class="token number">1000</span><span class="token punctuation">,</span> <span class="token keyword">function</span> <span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
    <span class="token function">alert</span><span class="token punctuation">(</span><span class="token string">"自定义动画执行完毕"</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
<span class="token punctuation">}</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
<div class="hljs-button {2}" data-title="复制"></div></code><ul class="pre-numbering" style=""><li style="color: rgb(153, 153, 153);">1</li><li style="color: rgb(153, 153, 153);">2</li><li style="color: rgb(153, 153, 153);">3</li><li style="color: rgb(153, 153, 153);">4</li><li style="color: rgb(153, 153, 153);">5</li><li style="color: rgb(153, 153, 153);">6</li></ul></pre>
<h4><a id="5__1551"></a>5. 动画队列</h4>
<ul>
<li>多个动画方法链式编程,会等到前面的动画执行完毕再依次执行后续动画</li>
</ul>
<pre class="prettyprint"><code class="prism language-js has-numbering" onclick="mdcp.copyCode(event)" style="position: unset;"><span class="token function">$</span><span class="token punctuation">(</span><span class="token string">"div"</span><span class="token punctuation">)</span><span class="token punctuation">.</span><span class="token function">slideDown</span><span class="token punctuation">(</span><span class="token number">1000</span><span class="token punctuation">)</span><span class="token punctuation">.</span><span class="token function">slideUp</span><span class="token punctuation">(</span><span class="token number">1000</span><span class="token punctuation">)</span><span class="token punctuation">.</span><span class="token function">show</span><span class="token punctuation">(</span><span class="token number">1000</span><span class="token punctuation">)</span><span class="token punctuation">;</span>

<span class="token function">$</span><span class="token punctuation">(</span><span class="token string">".one"</span><span class="token punctuation">)</span><span class="token punctuation">.</span><span class="token function">slideDown</span><span class="token punctuation">(</span><span class="token number">1000</span><span class="token punctuation">,</span><span class="token keyword">function</span> <span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
    <span class="token function">$</span><span class="token punctuation">(</span><span class="token string">".one"</span><span class="token punctuation">)</span><span class="token punctuation">.</span><span class="token function">slideUp</span><span class="token punctuation">(</span><span class="token number">1000</span><span class="token punctuation">,</span> <span class="token keyword">function</span> <span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
        <span class="token function">$</span><span class="token punctuation">(</span><span class="token string">".one"</span><span class="token punctuation">)</span><span class="token punctuation">.</span><span class="token function">show</span><span class="token punctuation">(</span><span class="token number">1000</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
    <span class="token punctuation">}</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
<span class="token punctuation">}</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
<div class="hljs-button {2}" data-title="复制"></div></code><ul class="pre-numbering" style=""><li style="color: rgb(153, 153, 153);">1</li><li style="color: rgb(153, 153, 153);">2</li><li style="color: rgb(153, 153, 153);">3</li><li style="color: rgb(153, 153, 153);">4</li><li style="color: rgb(153, 153, 153);">5</li><li style="color: rgb(153, 153, 153);">6</li><li style="color: rgb(153, 153, 153);">7</li></ul></pre>
<ul>
<li>但是如果后面紧跟一个非动画方法则会被立即执行</li>
</ul>
<pre class="prettyprint"><code class="prism language-js has-numbering" onclick="mdcp.copyCode(event)" style="position: unset;"><span class="token comment">// 立刻变为黄色,然后再执行动画</span>
<span class="token function">$</span><span class="token punctuation">(</span><span class="token string">".one"</span><span class="token punctuation">)</span><span class="token punctuation">.</span><span class="token function">slideDown</span><span class="token punctuation">(</span><span class="token number">1000</span><span class="token punctuation">)</span><span class="token punctuation">.</span><span class="token function">slideUp</span><span class="token punctuation">(</span><span class="token number">1000</span><span class="token punctuation">)</span><span class="token punctuation">.</span><span class="token function">show</span><span class="token punctuation">(</span><span class="token number">1000</span><span class="token punctuation">)</span><span class="token punctuation">.</span><span class="token function">css</span><span class="token punctuation">(</span><span class="token string">"background"</span><span class="token punctuation">,</span> <span class="token string">"yellow"</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
<div class="hljs-button {2}" data-title="复制"></div></code><ul class="pre-numbering" style=""><li style="color: rgb(153, 153, 153);">1</li><li style="color: rgb(153, 153, 153);">2</li></ul></pre>
<ul>
<li>如果想颜色再动画执行完毕之后设置
<ul>
<li>1.使用回调</li>
<li>2.使用动画队列</li>
</ul>
</li>
</ul>
<pre class="prettyprint"><code class="prism language-js has-numbering" onclick="mdcp.copyCode(event)" style="position: unset;"><span class="token function">$</span><span class="token punctuation">(</span><span class="token string">".one"</span><span class="token punctuation">)</span><span class="token punctuation">.</span><span class="token function">slideDown</span><span class="token punctuation">(</span><span class="token number">1000</span><span class="token punctuation">,</span><span class="token keyword">function</span> <span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
    <span class="token function">$</span><span class="token punctuation">(</span><span class="token string">".one"</span><span class="token punctuation">)</span><span class="token punctuation">.</span><span class="token function">slideUp</span><span class="token punctuation">(</span><span class="token number">1000</span><span class="token punctuation">,</span> <span class="token keyword">function</span> <span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
        <span class="token function">$</span><span class="token punctuation">(</span><span class="token string">".one"</span><span class="token punctuation">)</span><span class="token punctuation">.</span><span class="token function">show</span><span class="token punctuation">(</span><span class="token number">1000</span><span class="token punctuation">,</span> <span class="token keyword">function</span> <span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
            <span class="token function">$</span><span class="token punctuation">(</span><span class="token string">".one"</span><span class="token punctuation">)</span><span class="token punctuation">.</span><span class="token function">css</span><span class="token punctuation">(</span><span class="token string">"background"</span><span class="token punctuation">,</span> <span class="token string">"yellow"</span><span class="token punctuation">)</span>
        <span class="token punctuation">}</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
    <span class="token punctuation">}</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
<span class="token punctuation">}</span><span class="token punctuation">)</span><span class="token punctuation">;</span>

<span class="token function">$</span><span class="token punctuation">(</span><span class="token string">".one"</span><span class="token punctuation">)</span><span class="token punctuation">.</span><span class="token function">slideDown</span><span class="token punctuation">(</span><span class="token number">1000</span><span class="token punctuation">)</span><span class="token punctuation">.</span><span class="token function">slideUp</span><span class="token punctuation">(</span><span class="token number">1000</span><span class="token punctuation">)</span><span class="token punctuation">.</span><span class="token function">show</span><span class="token punctuation">(</span><span class="token number">1000</span><span class="token punctuation">)</span><span class="token punctuation">.</span><span class="token function">queue</span><span class="token punctuation">(</span><span class="token keyword">function</span> <span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
    <span class="token function">$</span><span class="token punctuation">(</span><span class="token string">".one"</span><span class="token punctuation">)</span><span class="token punctuation">.</span><span class="token function">css</span><span class="token punctuation">(</span><span class="token string">"background"</span><span class="token punctuation">,</span> <span class="token string">"yellow"</span><span class="token punctuation">)</span>
<span class="token punctuation">}</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
<div class="hljs-button {2}" data-title="复制"></div></code><ul class="pre-numbering" style=""><li style="color: rgb(153, 153, 153);">1</li><li style="color: rgb(153, 153, 153);">2</li><li style="color: rgb(153, 153, 153);">3</li><li style="color: rgb(153, 153, 153);">4</li><li style="color: rgb(153, 153, 153);">5</li><li style="color: rgb(153, 153, 153);">6</li><li style="color: rgb(153, 153, 153);">7</li><li style="color: rgb(153, 153, 153);">8</li><li style="color: rgb(153, 153, 153);">9</li><li style="color: rgb(153, 153, 153);">10</li><li style="color: rgb(153, 153, 153);">11</li></ul></pre>
<ul>
<li>注意：
<ul>
<li>动画队列方法queue()后面不能继续直接添加queue()</li>
<li>如果想继续添加必须在上一个queue()方法中next()方法</li>
</ul>
</li>
</ul>
<pre class="prettyprint"><code class="prism language-js has-numbering" onclick="mdcp.copyCode(event)" style="position: unset;"><span class="token function">$</span><span class="token punctuation">(</span><span class="token string">".one"</span><span class="token punctuation">)</span><span class="token punctuation">.</span><span class="token function">slideDown</span><span class="token punctuation">(</span><span class="token number">1000</span><span class="token punctuation">)</span><span class="token punctuation">.</span><span class="token function">slideUp</span><span class="token punctuation">(</span><span class="token number">1000</span><span class="token punctuation">)</span><span class="token punctuation">.</span><span class="token function">show</span><span class="token punctuation">(</span><span class="token number">1000</span><span class="token punctuation">)</span><span class="token punctuation">.</span><span class="token function">queue</span><span class="token punctuation">(</span><span class="token keyword">function</span> <span class="token punctuation">(</span>next<span class="token punctuation">)</span> <span class="token punctuation">{</span>
    <span class="token function">$</span><span class="token punctuation">(</span><span class="token string">".one"</span><span class="token punctuation">)</span><span class="token punctuation">.</span><span class="token function">css</span><span class="token punctuation">(</span><span class="token string">"background"</span><span class="token punctuation">,</span> <span class="token string">"yellow"</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
    <span class="token function">next</span><span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token punctuation">;</span> <span class="token comment">// 关键点</span>
<span class="token punctuation">}</span><span class="token punctuation">)</span><span class="token punctuation">.</span><span class="token function">queue</span><span class="token punctuation">(</span><span class="token keyword">function</span> <span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
    <span class="token function">$</span><span class="token punctuation">(</span><span class="token string">".one"</span><span class="token punctuation">)</span><span class="token punctuation">.</span><span class="token function">css</span><span class="token punctuation">(</span><span class="token string">"width"</span><span class="token punctuation">,</span> <span class="token string">"500px"</span><span class="token punctuation">)</span>
<span class="token punctuation">}</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
<div class="hljs-button {2}" data-title="复制"></div></code><ul class="pre-numbering" style=""><li style="color: rgb(153, 153, 153);">1</li><li style="color: rgb(153, 153, 153);">2</li><li style="color: rgb(153, 153, 153);">3</li><li style="color: rgb(153, 153, 153);">4</li><li style="color: rgb(153, 153, 153);">5</li><li style="color: rgb(153, 153, 153);">6</li></ul></pre>
<h4><a id="6__1595"></a>6. 动画相关方法</h4>
<h6><a id="1_delay_1596"></a>1. delay</h6>
<ul>
<li>设置动画延迟时长</li>
</ul>
<pre class="prettyprint"><code class="prism language-js has-numbering" onclick="mdcp.copyCode(event)" style="position: unset;"><span class="token function">$</span><span class="token punctuation">(</span><span class="token string">".one"</span><span class="token punctuation">)</span><span class="token punctuation">.</span><span class="token function">animate</span><span class="token punctuation">(</span><span class="token punctuation">{</span>
    width<span class="token punctuation">:</span> <span class="token number">500</span>
    <span class="token comment">// height: 500</span>
<span class="token punctuation">}</span><span class="token punctuation">,</span> <span class="token number">1000</span><span class="token punctuation">)</span><span class="token punctuation">.</span><span class="token function">delay</span><span class="token punctuation">(</span><span class="token number">2000</span><span class="token punctuation">)</span><span class="token punctuation">.</span><span class="token function">animate</span><span class="token punctuation">(</span><span class="token punctuation">{</span>
    height<span class="token punctuation">:</span> <span class="token number">500</span>
<span class="token punctuation">}</span><span class="token punctuation">,</span> <span class="token number">1000</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
<div class="hljs-button {2}" data-title="复制"></div></code><ul class="pre-numbering" style=""><li style="color: rgb(153, 153, 153);">1</li><li style="color: rgb(153, 153, 153);">2</li><li style="color: rgb(153, 153, 153);">3</li><li style="color: rgb(153, 153, 153);">4</li><li style="color: rgb(153, 153, 153);">5</li><li style="color: rgb(153, 153, 153);">6</li></ul></pre>
<h6><a id="2_stop_1607"></a>2. stop</h6>
<ul>
<li>停止指定元素上正在执行的动画</li>
</ul>
<pre class="prettyprint"><code class="prism language-js has-numbering" onclick="mdcp.copyCode(event)" style="position: unset;"> <span class="token comment">// 立即停止当前动画, 继续执行后续的动画</span>
    <span class="token function">$</span><span class="token punctuation">(</span><span class="token string">"div"</span><span class="token punctuation">)</span><span class="token punctuation">.</span><span class="token function">stop</span><span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
    <span class="token function">$</span><span class="token punctuation">(</span><span class="token string">"div"</span><span class="token punctuation">)</span><span class="token punctuation">.</span><span class="token function">stop</span><span class="token punctuation">(</span><span class="token boolean">false</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
    <span class="token function">$</span><span class="token punctuation">(</span><span class="token string">"div"</span><span class="token punctuation">)</span><span class="token punctuation">.</span><span class="token function">stop</span><span class="token punctuation">(</span><span class="token boolean">false</span><span class="token punctuation">,</span> <span class="token boolean">false</span><span class="token punctuation">)</span><span class="token punctuation">;</span>

    <span class="token comment">// 立即停止当前和后续所有的动画</span>
    <span class="token function">$</span><span class="token punctuation">(</span><span class="token string">"div"</span><span class="token punctuation">)</span><span class="token punctuation">.</span><span class="token function">stop</span><span class="token punctuation">(</span><span class="token boolean">true</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
    <span class="token function">$</span><span class="token punctuation">(</span><span class="token string">"div"</span><span class="token punctuation">)</span><span class="token punctuation">.</span><span class="token function">stop</span><span class="token punctuation">(</span><span class="token boolean">true</span><span class="token punctuation">,</span> <span class="token boolean">false</span><span class="token punctuation">)</span><span class="token punctuation">;</span>

    <span class="token comment">// 立即完成当前的, 继续执行后续动画</span>
    <span class="token function">$</span><span class="token punctuation">(</span><span class="token string">"div"</span><span class="token punctuation">)</span><span class="token punctuation">.</span><span class="token function">stop</span><span class="token punctuation">(</span><span class="token boolean">false</span><span class="token punctuation">,</span> <span class="token boolean">true</span><span class="token punctuation">)</span><span class="token punctuation">;</span>

    <span class="token comment">// 立即完成当前的, 并且停止后续所有的</span>
    <span class="token function">$</span><span class="token punctuation">(</span><span class="token string">"div"</span><span class="token punctuation">)</span><span class="token punctuation">.</span><span class="token function">stop</span><span class="token punctuation">(</span><span class="token boolean">true</span><span class="token punctuation">,</span> <span class="token boolean">true</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
<div class="hljs-button {2}" data-title="复制"></div></code><ul class="pre-numbering" style=""><li style="color: rgb(153, 153, 153);">1</li><li style="color: rgb(153, 153, 153);">2</li><li style="color: rgb(153, 153, 153);">3</li><li style="color: rgb(153, 153, 153);">4</li><li style="color: rgb(153, 153, 153);">5</li><li style="color: rgb(153, 153, 153);">6</li><li style="color: rgb(153, 153, 153);">7</li><li style="color: rgb(153, 153, 153);">8</li><li style="color: rgb(153, 153, 153);">9</li><li style="color: rgb(153, 153, 153);">10</li><li style="color: rgb(153, 153, 153);">11</li><li style="color: rgb(153, 153, 153);">12</li><li style="color: rgb(153, 153, 153);">13</li><li style="color: rgb(153, 153, 153);">14</li></ul></pre>
<h2><a name="t12"></a><a id="12_jQuery__1627"></a>12. jQuery 文档处理</h2>
<h4><a id="1__1628"></a>1. 添加节点</h4>
<h6><a id="1__1629"></a>1. 内部插入</h6>
<ul>
<li>append</li>
<li>appendTo
<ul>
<li>将元素添加到指定元素内部的最后</li>
</ul>
</li>
</ul>
<pre class="prettyprint"><code class="prism language-js has-numbering" onclick="mdcp.copyCode(event)" style="position: unset;"><span class="token comment">// 1.创建一个节点</span>
<span class="token keyword">var</span> $li <span class="token operator">=</span> <span class="token function">$</span><span class="token punctuation">(</span><span class="token string">"&lt;li&gt;新增的li&lt;/li&gt;"</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
<span class="token comment">// 2.添加节点</span>
<span class="token comment">// $("ul").append($li);</span>
$li<span class="token punctuation">.</span><span class="token function">appendTo</span><span class="token punctuation">(</span><span class="token string">"ul"</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
<div class="hljs-button {2}" data-title="复制"></div></code><ul class="pre-numbering" style=""><li style="color: rgb(153, 153, 153);">1</li><li style="color: rgb(153, 153, 153);">2</li><li style="color: rgb(153, 153, 153);">3</li><li style="color: rgb(153, 153, 153);">4</li><li style="color: rgb(153, 153, 153);">5</li></ul></pre>
<ul>
<li>prepend</li>
<li>prependTo
<ul>
<li>将元素添加到指定元素内部的最前面</li>
</ul>
</li>
</ul>
<pre class="prettyprint"><code class="prism language-js has-numbering" onclick="mdcp.copyCode(event)" style="position: unset;"><span class="token comment">// 1.创建一个节点</span>
<span class="token keyword">var</span> $li <span class="token operator">=</span> <span class="token function">$</span><span class="token punctuation">(</span><span class="token string">"&lt;li&gt;新增的li&lt;/li&gt;"</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
<span class="token comment">// 2.添加节点</span>
<span class="token comment">// $("ul").prepend($li);</span>
$li<span class="token punctuation">.</span><span class="token function">prependTo</span><span class="token punctuation">(</span><span class="token string">"ul"</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
<div class="hljs-button {2}" data-title="复制"></div></code><ul class="pre-numbering" style=""><li style="color: rgb(153, 153, 153);">1</li><li style="color: rgb(153, 153, 153);">2</li><li style="color: rgb(153, 153, 153);">3</li><li style="color: rgb(153, 153, 153);">4</li><li style="color: rgb(153, 153, 153);">5</li></ul></pre>
<h6><a id="2__1651"></a>2. 外部插入</h6>
<ul>
<li>after</li>
<li>insertAfter
<ul>
<li>将元素添加到指定元素外部的后面</li>
</ul>
</li>
</ul>
<pre class="prettyprint"><code class="prism language-js has-numbering" onclick="mdcp.copyCode(event)" style="position: unset;"><span class="token comment">// 1.创建一个节点</span>
<span class="token keyword">var</span> $li <span class="token operator">=</span> <span class="token function">$</span><span class="token punctuation">(</span><span class="token string">"&lt;li&gt;新增的li&lt;/li&gt;"</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
<span class="token comment">// 2.添加节点</span>
<span class="token comment">// $("ul").after($li);</span>
$li<span class="token punctuation">.</span><span class="token function">insertAfter</span><span class="token punctuation">(</span><span class="token string">"ul"</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
<div class="hljs-button {2}" data-title="复制"></div></code><ul class="pre-numbering" style=""><li style="color: rgb(153, 153, 153);">1</li><li style="color: rgb(153, 153, 153);">2</li><li style="color: rgb(153, 153, 153);">3</li><li style="color: rgb(153, 153, 153);">4</li><li style="color: rgb(153, 153, 153);">5</li></ul></pre>
<ul>
<li>before</li>
<li>insertBefore
<ul>
<li>将元素添加到指定元素外部的前面</li>
</ul>
</li>
</ul>
<pre class="prettyprint"><code class="prism language-js has-numbering" onclick="mdcp.copyCode(event)" style="position: unset;"><span class="token comment">// 1.创建一个节点</span>
<span class="token keyword">var</span> $li <span class="token operator">=</span> <span class="token function">$</span><span class="token punctuation">(</span><span class="token string">"&lt;li&gt;新增的li&lt;/li&gt;"</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
<span class="token comment">// 2.添加节点</span>
<span class="token comment">// $("ul").before($li);</span>
$li<span class="token punctuation">.</span><span class="token function">insertBefore</span><span class="token punctuation">(</span><span class="token string">"ul"</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
<div class="hljs-button {2}" data-title="复制"></div></code><ul class="pre-numbering" style=""><li style="color: rgb(153, 153, 153);">1</li><li style="color: rgb(153, 153, 153);">2</li><li style="color: rgb(153, 153, 153);">3</li><li style="color: rgb(153, 153, 153);">4</li><li style="color: rgb(153, 153, 153);">5</li></ul></pre>
<h4><a id="2__1673"></a>2. 删除节点</h4>
<ul>
<li>empty()
<ul>
<li>删除指定元素的内容和子元素, 指定元素自身不会被删除</li>
</ul>
</li>
</ul>
<pre class="prettyprint"><code class="prism language-js has-numbering" onclick="mdcp.copyCode(event)" style="position: unset;"><span class="token function">$</span><span class="token punctuation">(</span><span class="token string">"div"</span><span class="token punctuation">)</span><span class="token punctuation">.</span><span class="token function">empty</span><span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
<div class="hljs-button {2}" data-title="复制"></div></code><ul class="pre-numbering" style=""><li style="color: rgb(153, 153, 153);">1</li></ul></pre>
<ul>
<li>remove()
<ul>
<li>删除指定元素</li>
</ul>
</li>
</ul>
<pre class="prettyprint"><code class="prism language-js has-numbering" onclick="mdcp.copyCode(event)" style="position: unset;"><span class="token comment">// 删除所有div</span>
<span class="token function">$</span><span class="token punctuation">(</span><span class="token string">"div"</span><span class="token punctuation">)</span><span class="token punctuation">.</span><span class="token function">remove</span><span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
<span class="token comment">// 删除div中id是box1的那个div</span>
<span class="token function">$</span><span class="token punctuation">(</span><span class="token string">"div"</span><span class="token punctuation">)</span><span class="token punctuation">.</span><span class="token function">remove</span><span class="token punctuation">(</span><span class="token string">"#box1"</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
<div class="hljs-button {2}" data-title="复制"></div></code><ul class="pre-numbering" style=""><li style="color: rgb(153, 153, 153);">1</li><li style="color: rgb(153, 153, 153);">2</li><li style="color: rgb(153, 153, 153);">3</li><li style="color: rgb(153, 153, 153);">4</li></ul></pre>
<ul>
<li>detach()</li>
</ul>
<pre class="prettyprint"><code class="prism language-js has-numbering" onclick="mdcp.copyCode(event)" style="position: unset;"><span class="token comment">// 删除所有div</span>
<span class="token function">$</span><span class="token punctuation">(</span><span class="token string">"div"</span><span class="token punctuation">)</span><span class="token punctuation">.</span><span class="token function">detach</span><span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
<span class="token comment">// 删除div中id是box1的那个div</span>
<span class="token function">$</span><span class="token punctuation">(</span><span class="token string">"div"</span><span class="token punctuation">)</span><span class="token punctuation">.</span><span class="token function">detach</span><span class="token punctuation">(</span><span class="token string">"#box1"</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
<div class="hljs-button {2}" data-title="复制"></div></code><ul class="pre-numbering" style=""><li style="color: rgb(153, 153, 153);">1</li><li style="color: rgb(153, 153, 153);">2</li><li style="color: rgb(153, 153, 153);">3</li><li style="color: rgb(153, 153, 153);">4</li></ul></pre>
<ul>
<li>remove和detach区别
<ul>
<li>remove删除元素后,元素上的事件会被移出</li>
<li>detach删除元素后,元素上的事件会被保留</li>
</ul>
</li>
</ul>
<pre class="prettyprint"><code class="prism language-js has-numbering" onclick="mdcp.copyCode(event)" style="position: unset;"><span class="token function">$</span><span class="token punctuation">(</span><span class="token string">"button"</span><span class="token punctuation">)</span><span class="token punctuation">.</span><span class="token function">click</span><span class="token punctuation">(</span><span class="token keyword">function</span> <span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
    <span class="token comment">// $("div").remove();</span>
    <span class="token comment">// $("div").empty();</span>
    <span class="token comment">// $("li").remove(".item");</span>

    <span class="token comment">// 利用remove删除之后再重新添加,原有的事件无法响应</span>
    <span class="token comment">// var $div = $("div").remove();</span>
    <span class="token comment">// 利用detach删除之后再重新添加,原有事件可以响应</span>
    <span class="token keyword">var</span> $div <span class="token operator">=</span> <span class="token function">$</span><span class="token punctuation">(</span><span class="token string">"div"</span><span class="token punctuation">)</span><span class="token punctuation">.</span><span class="token function">detach</span><span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
    <span class="token comment">// console.log($div);</span>
    <span class="token comment">// 将删除的返回值重新添加到body上</span>
    <span class="token function">$</span><span class="token punctuation">(</span><span class="token string">"body"</span><span class="token punctuation">)</span><span class="token punctuation">.</span><span class="token function">append</span><span class="token punctuation">(</span>$div<span class="token punctuation">)</span><span class="token punctuation">;</span>
<span class="token punctuation">}</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
<span class="token function">$</span><span class="token punctuation">(</span><span class="token string">"div"</span><span class="token punctuation">)</span><span class="token punctuation">.</span><span class="token function">click</span><span class="token punctuation">(</span><span class="token keyword">function</span> <span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
    <span class="token function">alert</span><span class="token punctuation">(</span><span class="token string">"div被点击了"</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
<span class="token punctuation">}</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
<div class="hljs-button {2}" data-title="复制"></div></code><ul class="pre-numbering" style=""><li style="color: rgb(153, 153, 153);">1</li><li style="color: rgb(153, 153, 153);">2</li><li style="color: rgb(153, 153, 153);">3</li><li style="color: rgb(153, 153, 153);">4</li><li style="color: rgb(153, 153, 153);">5</li><li style="color: rgb(153, 153, 153);">6</li><li style="color: rgb(153, 153, 153);">7</li><li style="color: rgb(153, 153, 153);">8</li><li style="color: rgb(153, 153, 153);">9</li><li style="color: rgb(153, 153, 153);">10</li><li style="color: rgb(153, 153, 153);">11</li><li style="color: rgb(153, 153, 153);">12</li><li style="color: rgb(153, 153, 153);">13</li><li style="color: rgb(153, 153, 153);">14</li><li style="color: rgb(153, 153, 153);">15</li><li style="color: rgb(153, 153, 153);">16</li></ul></pre>
<h4><a id="3__1716"></a>3. 替换节点</h4>
<ul>
<li>replaceWith
<ul>
<li>将所有匹配的元素替换成指定的HTML或DOM元素</li>
<li>replaceWith参数可以是一个DOM元素</li>
<li>replaceWith参数也可以是一个代码片段</li>
</ul>
</li>
<li>replaceAll
<ul>
<li>用匹配的元素替换掉所有 selector匹配到的元素</li>
</ul>
</li>
</ul>
<pre class="prettyprint"><code class="prism language-js has-numbering" onclick="mdcp.copyCode(event)" style="position: unset;"><span class="token comment">// 编写jQuery相关代码</span>
<span class="token function">$</span><span class="token punctuation">(</span><span class="token string">"button"</span><span class="token punctuation">)</span><span class="token punctuation">.</span><span class="token function">click</span><span class="token punctuation">(</span><span class="token keyword">function</span> <span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
    <span class="token comment">// 创建一个新的节点</span>
    <span class="token keyword">var</span> $item <span class="token operator">=</span> <span class="token function">$</span><span class="token punctuation">(</span><span class="token string">"&lt;h6&gt;我是标题6&lt;/h6&gt;"</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
    <span class="token comment">// 利用新的节点替换旧的节点</span>
    <span class="token comment">// $("h1").replaceWith($item);</span>
    $item<span class="token punctuation">.</span><span class="token function">replaceAll</span><span class="token punctuation">(</span><span class="token string">"h1"</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
<span class="token punctuation">}</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
<div class="hljs-button {2}" data-title="复制"></div></code><ul class="pre-numbering" style=""><li style="color: rgb(153, 153, 153);">1</li><li style="color: rgb(153, 153, 153);">2</li><li style="color: rgb(153, 153, 153);">3</li><li style="color: rgb(153, 153, 153);">4</li><li style="color: rgb(153, 153, 153);">5</li><li style="color: rgb(153, 153, 153);">6</li><li style="color: rgb(153, 153, 153);">7</li><li style="color: rgb(153, 153, 153);">8</li></ul></pre>
<h4><a id="4__1734"></a>4. 复制节点</h4>
<ul>
<li>clone
<ul>
<li>复制一个节点</li>
<li>浅复制不会复制节点的事件</li>
<li>深复制会复制节点的事件</li>
</ul>
</li>
</ul>
<pre class="prettyprint"><code class="prism language-js has-numbering" onclick="mdcp.copyCode(event)" style="position: unset;"><span class="token function">$</span><span class="token punctuation">(</span><span class="token keyword">function</span> <span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
    <span class="token comment">// clone([Even[,deepEven]])</span>
    <span class="token function">$</span><span class="token punctuation">(</span><span class="token string">"button"</span><span class="token punctuation">)</span><span class="token punctuation">.</span><span class="token function">eq</span><span class="token punctuation">(</span><span class="token number">0</span><span class="token punctuation">)</span><span class="token punctuation">.</span><span class="token function">click</span><span class="token punctuation">(</span><span class="token keyword">function</span> <span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
        <span class="token comment">// 1.浅复制一个元素</span>
        <span class="token keyword">var</span> $li <span class="token operator">=</span> <span class="token function">$</span><span class="token punctuation">(</span><span class="token string">"li:first"</span><span class="token punctuation">)</span><span class="token punctuation">.</span><span class="token function">clone</span><span class="token punctuation">(</span><span class="token boolean">false</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
        <span class="token comment">// 2.将复制的元素添加到ul中</span>
        <span class="token function">$</span><span class="token punctuation">(</span><span class="token string">"ul"</span><span class="token punctuation">)</span><span class="token punctuation">.</span><span class="token function">append</span><span class="token punctuation">(</span>$li<span class="token punctuation">)</span><span class="token punctuation">;</span> <span class="token comment">// 点击li无法响应事件</span>
    <span class="token punctuation">}</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
    <span class="token function">$</span><span class="token punctuation">(</span><span class="token string">"button"</span><span class="token punctuation">)</span><span class="token punctuation">.</span><span class="token function">eq</span><span class="token punctuation">(</span><span class="token number">1</span><span class="token punctuation">)</span><span class="token punctuation">.</span><span class="token function">click</span><span class="token punctuation">(</span><span class="token keyword">function</span> <span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
        <span class="token comment">// 1.深复制一个元素</span>
        <span class="token keyword">var</span> $li <span class="token operator">=</span> <span class="token function">$</span><span class="token punctuation">(</span><span class="token string">"li:first"</span><span class="token punctuation">)</span><span class="token punctuation">.</span><span class="token function">clone</span><span class="token punctuation">(</span><span class="token boolean">true</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
        <span class="token comment">// 2.将复制的元素添加到ul中</span>
        <span class="token function">$</span><span class="token punctuation">(</span><span class="token string">"ul"</span><span class="token punctuation">)</span><span class="token punctuation">.</span><span class="token function">append</span><span class="token punctuation">(</span>$li<span class="token punctuation">)</span><span class="token punctuation">;</span> <span class="token comment">// 点击li可以响应事件</span>
    <span class="token punctuation">}</span><span class="token punctuation">)</span><span class="token punctuation">;</span>

    <span class="token function">$</span><span class="token punctuation">(</span><span class="token string">"li"</span><span class="token punctuation">)</span><span class="token punctuation">.</span><span class="token function">click</span><span class="token punctuation">(</span><span class="token keyword">function</span> <span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
        <span class="token function">alert</span><span class="token punctuation">(</span><span class="token function">$</span><span class="token punctuation">(</span><span class="token keyword">this</span><span class="token punctuation">)</span><span class="token punctuation">.</span><span class="token function">html</span><span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
    <span class="token punctuation">}</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
<span class="token punctuation">}</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
<div class="hljs-button {2}" data-title="复制"></div></code><ul class="pre-numbering" style=""><li style="color: rgb(153, 153, 153);">1</li><li style="color: rgb(153, 153, 153);">2</li><li style="color: rgb(153, 153, 153);">3</li><li style="color: rgb(153, 153, 153);">4</li><li style="color: rgb(153, 153, 153);">5</li><li style="color: rgb(153, 153, 153);">6</li><li style="color: rgb(153, 153, 153);">7</li><li style="color: rgb(153, 153, 153);">8</li><li style="color: rgb(153, 153, 153);">9</li><li style="color: rgb(153, 153, 153);">10</li><li style="color: rgb(153, 153, 153);">11</li><li style="color: rgb(153, 153, 153);">12</li><li style="color: rgb(153, 153, 153);">13</li><li style="color: rgb(153, 153, 153);">14</li><li style="color: rgb(153, 153, 153);">15</li><li style="color: rgb(153, 153, 153);">16</li><li style="color: rgb(153, 153, 153);">17</li><li style="color: rgb(153, 153, 153);">18</li><li style="color: rgb(153, 153, 153);">19</li></ul></pre>
<h4><a id="5__1760"></a>5. 包裹节点</h4>
<ul>
<li>wrap()
<ul>
<li>将指定节点用其他标记包裹起来</li>
<li>该方法对于需要在文档中插入额外的结构化标记非常有用, 而且不会破坏原始文档的语义</li>
</ul>
</li>
<li>wrapAll()
<ul>
<li>将所有匹配的元素用一个元素来包裹</li>
<li>而 wrap() 方法是将所有的元素进行单独包裹</li>
</ul>
</li>
<li>wrapInner()
<ul>
<li>将每一个匹配的元素的子内容（包括文本节点）用其他结构化标记包裹起来</li>
</ul>
</li>
</ul>
<pre class="prettyprint"><code class="prism language-html has-numbering" onclick="mdcp.copyCode(event)" style="position: unset;"><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>script</span> <span class="token attr-name">type</span><span class="token attr-value"><span class="token punctuation">=</span><span class="token punctuation">"</span>text/javascript<span class="token punctuation">"</span></span><span class="token punctuation">&gt;</span></span><span class="token script language-javascript">
    <span class="token comment">//测试使用 jQuery wrap, wrapAll, wrapInner</span>
    <span class="token function">$</span><span class="token punctuation">(</span><span class="token keyword">function</span><span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token punctuation">{</span>
        <span class="token comment">//包装 li 本身</span>
        <span class="token function">$</span><span class="token punctuation">(</span><span class="token string">"#box1 li"</span><span class="token punctuation">)</span><span class="token punctuation">.</span><span class="token function">wrap</span><span class="token punctuation">(</span><span class="token string">"&lt;font color='red'&gt;&lt;/font&gt;"</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
    
        <span class="token comment">//包装所有的 li</span>
        <span class="token function">$</span><span class="token punctuation">(</span><span class="token string">"#box2 li"</span><span class="token punctuation">)</span><span class="token punctuation">.</span><span class="token function">wrapAll</span><span class="token punctuation">(</span><span class="token string">"&lt;font color='red'&gt;&lt;/font&gt;"</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
    
        <span class="token comment">//包装 li 里边的文字. </span>
        <span class="token function">$</span><span class="token punctuation">(</span><span class="token string">"#box3 li"</span><span class="token punctuation">)</span><span class="token punctuation">.</span><span class="token function">wrapInner</span><span class="token punctuation">(</span><span class="token string">"&lt;font color='red'&gt;&lt;/font&gt;"</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
    <span class="token punctuation">}</span><span class="token punctuation">)</span>
</span><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>script</span><span class="token punctuation">&gt;</span></span>
<div class="hljs-button {2}" data-title="复制"></div></code><ul class="pre-numbering" style=""><li style="color: rgb(153, 153, 153);">1</li><li style="color: rgb(153, 153, 153);">2</li><li style="color: rgb(153, 153, 153);">3</li><li style="color: rgb(153, 153, 153);">4</li><li style="color: rgb(153, 153, 153);">5</li><li style="color: rgb(153, 153, 153);">6</li><li style="color: rgb(153, 153, 153);">7</li><li style="color: rgb(153, 153, 153);">8</li><li style="color: rgb(153, 153, 153);">9</li><li style="color: rgb(153, 153, 153);">10</li><li style="color: rgb(153, 153, 153);">11</li><li style="color: rgb(153, 153, 153);">12</li><li style="color: rgb(153, 153, 153);">13</li></ul></pre>
<h4><a id="6__1785"></a>6. 遍历节点</h4>
<ul>
<li>children() ：只考虑子元素，不考虑后代元素。</li>
<li>next() ：同辈紧邻后面一个元素。</li>
<li>nextAll() ：同辈紧邻后面所有兄弟元素。</li>
<li>prev() ：同辈紧邻前一个兄弟元素。</li>
<li>prevAll() ：同辈紧邻前所有兄弟元素。</li>
<li>siblings() ：同辈所有兄弟元素。</li>
<li>find(‘span’) ：返回被选元素的后代元素，括号内必填写，如果查找所有后代使用 “*”，起查找作用。</li>
<li>filter(‘div’) ：指定选择器的xx元素，括号内必填写，符合条件的同级元素，非后代元素，起过滤作用。</li>
<li>has(‘div’) ：符合条件的后代元素，不包含自身，括号内必填写，起过滤作用。</li>
<li>parents() ：获取所有祖先元素，参数为筛选条件。</li>
<li>closest(‘.new’) ：用来取得最近的匹配元素，包括自身。
<ul>
<li>首选检查自身是否符合，如果符合返回元素本身；如果不匹配，向上查找父元素，逐级向上直到匹配到选择器的元素。</li>
<li>如果什么没找到，返回一个空的jq对象。必须填写筛选条件，且只能找到一个元素。</li>
</ul>
</li>
<li>parentsUntil() ：截止到xx位置的祖先节点。</li>
</ul>
<h2><a name="t13"></a><a id="13_jQuery__1800"></a>13. jQuery 面试题</h2>
<h4><a id="1_jQueryjquery_1801"></a>1. 为什么要使用jQuery？jquery有哪些好处？</h4>
<ul>
<li>jQuery是轻量级的框架</li>
<li>强大的选择器，出色的DOM操作的封装</li>
<li>可靠的事件处理机制（jQuery在处理事件绑定的时候相当的可靠）</li>
<li>ajax封装的非常的好，不需要考虑复杂浏览器的兼容性和XMLHttpRequest对象的创建和使用的问题</li>
<li>出色的浏览器的兼容性</li>
<li>支持链式操作，隐式迭代</li>
<li>行为层和结构层的分离，还支持丰富的插件，jquery 的文档也非常的丰富</li>
</ul>
<h4><a id="2_jQuery_1810"></a>2. jQuery能做什么？</h4>
<ul>
<li>获取页面的元素</li>
<li>修改页面的外观</li>
<li>改变页面大的内容</li>
<li>响应用户的页面操作</li>
<li>为页面添加动态效果</li>
<li>无需刷新页面，即可以从服务器获取信息</li>
<li>简化常见的javascript任务</li>
</ul>
<h4><a id="3_jQuery____1818"></a>3. jQuery 库中的 $() 是什么？</h4>
<ul>
<li>$() 函数是 jQuery() 函数的别称</li>
<li>$() 函数用于将任何对象包裹成 jQuery 对象</li>
<li>允许调用定义在 jQuery 对象上的多个不同方法</li>
</ul>
<h4><a id="4_documentready__1823"></a>4. $(document).ready() 是个什么函数？为什么要用它？</h4>
<ul>
<li>ready() 函数用于在文档进入ready状态时执行代码</li>
<li>当DOM 完全加载（例如HTML被完全解析DOM树构建完成时），jQuery允许你执行代码</li>
<li>使用$(document).ready()的最大好处在于它适用于所有浏览器，jQuery帮你解决了跨浏览器的难题</li>
</ul>
<h4><a id="5_documentreadywindowonload_1828"></a>5. (document).ready()方法和window.onload有什么区别？</h4>
<ul>
<li>window.onload方法是在网页中所有的元素完全加载到浏览器后才执行</li>
<li>$(document).ready() 可以在DOM载入就绪是就对其进行操纵，并调用执行绑定的函数</li>
</ul>
<h4><a id="6_jQuerygetpost_1832"></a>6. jQuery中.get()提交和.post()提交的区别</h4>
<ul>
<li>.get()使用GET方法来进行异步提交，.post()使用POST方法来进行异步提交</li>
<li>get请求方式将参数跟在url后进行传递用户可见 post请求则是作为http消息的实体内容发送给服务器，用户不可见</li>
<li>post传输数据比get大</li>
<li>get请求的数据会被浏览器缓存，不安全</li>
</ul>
<h4><a id="7_jQuery_1838"></a>7. jQuery中有哪些方法可以遍历节点？</h4>
<ul>
<li>children():获取匹配元素的子元素集合，不考虑后代元素 <span class="katex--inline">KaTeX parse error: Expected '}', got 'EOF' at end of input: (function(){</span>(“div”).children()})</li>
<li>next()获取匹配元素后面紧邻的同级元素</li>
<li>prev()获取匹配元素前紧邻的同级元素</li>
<li>siblings()获取匹配元素前后的所有同辈元素</li>
</ul>
<h4><a id="8_this__this__jQuery__1844"></a>8. $(this) 和 this 关键字在 jQuery 中有何不同？</h4>
<ul>
<li>$(this) 返回一个 jQuery 对象，可以对它调用多个 jQuery 方法</li>
<li>this 代表当前元素，它是 JavaScript 关键词中的一个，表示上下文中的当前 DOM 元素。</li>
<li>不能对 this 调用 jQuery 方法，直到 this 被 $() 函数包裹，例如 $(this)。</li>
</ul>
<h4><a id="9__CDN__jQuery___1849"></a>9. 使用 CDN 加载 jQuery 库的主要优势是什么 ?</h4>
<ul>
<li>报错节省服务器带宽</li>
<li>更快的下载速度</li>
<li>如果浏览器已经从同一个CDN下载类相同的 jQuery 版本, 那么它就不会再去下载它一次</li>
</ul>
<h4><a id="10__1854"></a>10. 如何使用从服务器获取一个复杂数据(对象)?</h4>
<ul>
<li>通常会把这个数据转换为通用的数据交换格式，如xml或json。由于xml解析比较麻烦，所以使用json比较多。</li>
<li>在jQuery中有专门的获取服务器json数据的方法，getJSON()，在回调中，jQuery会自动将json转换为java对象。</li>
</ul>
<h4><a id="11__1858"></a>11. 在使用选择器的时要注意的地方?</h4>
<ul>
<li>选择器中含有\等特殊字符的时候需要进行转译</li>
<li>属性选择器的引号问题</li>
<li>选择器中含有空格的注意事项</li>
</ul>
<h4><a id="12__1863"></a>12. 有哪些查询节点的选择器？</h4>
<ul>
<li>:first 查询第一个</li>
<li>:last 查询最后一个，</li>
<li>:odd查询奇数但是索引从0开始</li>
<li>:even 查询偶数</li>
<li>:eq(index)查询相等的</li>
<li>:gt(index)查询大于index的</li>
<li>:lt查询小于index</li>
<li>:header 选取所有的标题等</li>
</ul>
<h4><a id="13_jQuery____1873"></a>13. jQuery是如何处理缓存的？ ( 要处理缓存就是禁用缓存 )</h4>
<ul>
<li>通过<code>$.post()</code>方法来获取数据，那么默认就是禁用缓存的</li>
<li>通过<code>$.get()</code>方法来获取数据，可以通过设置时间戳来避免缓存。 可以在URL后面加上+(+new Date)</li>
</ul>
<pre class="prettyprint"><code class="prism language-js has-numbering" onclick="mdcp.copyCode(event)" style="position: unset;">$<span class="token punctuation">.</span><span class="token keyword">get</span><span class="token punctuation">(</span><span class="token string">'ajax.xml?'</span><span class="token operator">+</span><span class="token punctuation">(</span><span class="token operator">+</span><span class="token keyword">new</span> <span class="token class-name">Date</span><span class="token punctuation">)</span><span class="token punctuation">,</span><span class="token keyword">function</span> <span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token punctuation">{</span> <span class="token comment">//内容});</span>
<div class="hljs-button {2}" data-title="复制"></div></code><ul class="pre-numbering" style=""><li style="color: rgb(153, 153, 153);">1</li></ul></pre>
<ul>
<li>通过<code>$.ajax</code>方法来获取数据，只要设置cache:false即可。</li>
</ul>
<h4><a id="14_jquery_1881"></a>14. 在jquery中你有没有编写过插件，插件有什么好处？你编写过那些插件？它应该注意那些？</h4>
<ul>
<li><strong>插件的好处 :</strong>
<ul>
<li>对已有的一系列方法或函数的封装，以便在其他地方重新利用</li>
<li>方便后期维护和提高开发效率插件的分类：封装对象方法插件、封装全局函数插件、选择器插件</li>
</ul>
</li>
<li><strong>注意的地方：</strong>
<ul>
<li>插件的文件名推荐命名为jquery.[插件名].js，以免和其他的javaScript库插件混淆</li>
<li>所有的对象方法都应当附加到jQuery.fn对象上，而所有的全局函数都应当附加到jQuery对象本身上</li>
<li>插件应该返回一个jQuery对象，以保证插件的可链式操作</li>
<li>避免在插件内部使用$作为jQuery对象的别名,而应使用完整的jQuery来表示，这样可以避免冲突或使用闭包来避免</li>
<li>所有的方法或函数插件，都应当分好结尾，否则压缩的时候可能出现问题。在插件头部加上分号，这样可以避免他人的不规范代码给插件带来影响</li>
<li>在插件中通过<code>$.extent({})</code>封装全局函数,选择器插件，扩展已有的object对象过<code>$.fn.extend({})</code>封装对象方法插件</li>
</ul>
</li>
</ul>

                                    </div>