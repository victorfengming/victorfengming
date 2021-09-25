---
title: 'RabbitMQ面试题'
cover: "/img/lynk/97.jpg"
date:       2021-09-25
subtitle: 'Erlang语言编写的面向消息的中间件'
tags:
  - base
---




<h2 id="RabbitMQ是什么？"><a href="#RabbitMQ是什么？" class="headerlink" title="RabbitMQ是什么？" data-pjax-state=""></a>RabbitMQ 是什么？</h2><p>RabbitMQ 是实现了高级消息队列协议（<code>AMQP</code>）的开源消息代理软件（亦称面向消息的中间件）。RabbitMQ 服务器是用 Erlang 语言编写的，而群集和故障转移是构建在开放电信平台框架上的。所有主要的编程语言均有与代理接口通讯的客户端库。</p>
<p>PS: 也可能直接问什么是消息队列？消息队列就是一个使用队列来通信的组件。</p>
<h2 id="RabbitMQ特点"><a href="#RabbitMQ特点" class="headerlink" title="RabbitMQ特点?" data-pjax-state=""></a>RabbitMQ 特点？</h2>
<p><strong>可靠性</strong>: RabbitMQ 使用一些机制来保证可靠性， 如持久化、传输确认及发布确认等。</p>

<p><strong>灵活的路由</strong> : 在消息进入队列之前，通过交换器来路由消息。对于典型的路由功能， RabbitMQ 己经提供了一些内置的交换器来实现。针对更复杂的路由功能，可以将多个 交换器绑定在一起， 也可以通过插件机制来实现自己的交换器。</p>

<p><strong>扩展性</strong>: 多个 RabbitMQ 节点可以组成一个集群，也可以根据实际业务情况动态地扩展 集群中节点。</p>

<p><strong>高可用性</strong> : 队列可以在集群中的机器上设置镜像，使得在部分节点出现问题的情况下队 列仍然可用。</p>

<p><strong>多种协议</strong>: RabbitMQ 除了原生支持 AMQP 协议，还支持 STOMP， MQTT 等多种消息 中间件协议。</p>

<p><strong>多语言客户端</strong> :RabbitMQ 几乎支持所有常用语言，比如 Java、 Python、 Ruby、 PHP、 C#、 JavaScript 等。</p>

<p><strong>管理界面</strong> : RabbitMQ 提供了一个易用的用户界面，使得用户可以监控和管理消息、集 群中的节点等。</p>

<p><strong>插件机制</strong> : RabbitMQ 提供了许多插件 ， 以实现从多方面进行扩展，当然也可以编写自 己的插件。</p>



<h2 id="AMQP是什么"><a href="#AMQP是什么" class="headerlink" title="AMQP是什么?" data-pjax-state=""></a>AMQP 是什么？</h2><p>RabbitMQ 就是 AMQP 协议的 <code>Erlang</code> 的实现 (当然 RabbitMQ 还支持 <code>STOMP2</code>、 <code>MQTT3</code> 等协议 ) AMQP 的模型架构 和 RabbitMQ 的模型架构是一样的，生产者将消息发送给交换器，交换器和队列绑定 。</p>
<p>RabbitMQ 中的交换器、交换器类型、队列、绑定、路由键等都是遵循的 AMQP 协议中相 应的概念。目前 RabbitMQ 最新版本默认支持的是 AMQP 0-9-1。</p>
<h2 id="AMQP协议3层？"><a href="#AMQP协议3层？" class="headerlink" title="AMQP协议3层？" data-pjax-state=""></a>AMQP 协议 3 层？</h2>
<p><strong>Module Layer</strong>: 协议最高层，主要定义了一些客户端调用的命令，客户端可以用这些命令实现自己的业务逻辑。</p>

<p><strong>Session Layer</strong>: 中间层，主要负责客户端命令发送给服务器，再将服务端应答返回客户端，提供可靠性同步机制和错误处理。</p>

<p><strong>TransportLayer</strong>: 最底层，主要传输二进制数据流，提供帧的处理、信道服用、错误检测和数据表示等。</p>


<h2 id="AMQP模型的几大组件？"><a href="#AMQP模型的几大组件？" class="headerlink" title="AMQP模型的几大组件？" data-pjax-state=""></a>AMQP 模型的几大组件？</h2>
交换器 (Exchange)：消息代理服务器中用于把消息路由到队列的组件。
队列 (Queue)：用来存储消息的数据结构，位于硬盘或内存中。
绑定 (Binding)：一套规则，告知交换器消息应该将消息投递给哪个队列。


<h2 id="说说生产者Producer和消费者Consumer"><a href="#说说生产者Producer和消费者Consumer" class="headerlink" title="说说生产者Producer和消费者Consumer?" data-pjax-state=""></a>说说生产者 Producer 和消费者 Consumer?</h2><p>生产者</p>

消息生产者，就是投递消息的一方。
消息一般包含两个部分：消息体（<code>payload</code>) 和标签 (<code>Label</code>)。

<p>消费者</p>

消费消息，也就是接收消息的一方。
消费者连接到 RabbitMQ 服务器，并订阅到队列上。消费消息时只消费消息体，丢弃标签。

<h2 id="为什么需要消息队列？"><a href="#为什么需要消息队列？" class="headerlink" title="为什么需要消息队列？" data-pjax-state=""></a>为什么需要消息队列？</h2><p>从本质上来说是因为互联网的快速发展，业务不断扩张，促使技术架构需要不断的演进。</p>
<p>从以前的单体架构到现在的微服务架构，成百上千的服务之间相互调用和依赖。从互联网初期一个服务器上有 100 个在线用户已经很了不得，到现在坐拥 10 亿日活的微信。此时，我们需要有一个「工具」来解耦服务之间的关系、控制资源合理合时的使用以及缓冲流量洪峰等等。因此，消息队列就应运而生了。</p>
<p>它常用来实现：<code>异步处理</code>、<code>服务解耦</code>、<code>流量控制（削峰）</code>。</p>
<h2 id="说说Broker服务节点、Queue队列、Exchange交换器？"><a href="#说说Broker服务节点、Queue队列、Exchange交换器？" class="headerlink" title="说说Broker服务节点、Queue队列、Exchange交换器？" data-pjax-state=""></a>说说 Broker 服务节点、Queue 队列、Exchange 交换器？</h2>
Broker 可以看做 RabbitMQ 的服务节点。一般请下一个 Broker 可以看做一个 RabbitMQ 服务器。
Queue:RabbitMQ 的内部对象，用于存储消息。多个消费者可以订阅同一队列，这时队列中的消息会被平摊（轮询）给多个消费者进行处理。
Exchange: 生产者将消息发送到交换器，由交换器将消息路由到一个或者多个队列中。当路由不到时，或返回给生产者或直接丢弃。

<h2 id="消息队列有什么优缺点"><a href="#消息队列有什么优缺点" class="headerlink" title="消息队列有什么优缺点" data-pjax-state=""></a>消息队列有什么优缺点</h2><p>优点上面已经说了，就是在特殊场景下有其对应的好处，解耦、异步、削峰。缺点有以下几个：</p>

系统可用性降低 系统引入的外部依赖越多，越容易挂掉。万一 MQ 挂了，MQ 一挂，整套系统崩 溃，你不就完了？
系统复杂度提高 硬生生加个 MQ 进来，你怎么保证消息没有重复消费？怎么处理消息丢失的情况？
怎么保证消息传递的顺序性？问题一大堆。
一致性问题 A 系统处理完了直接返回成功了，人都以为你这个请求就成功了；但是问题是，要是 BCD 三个系统那里，BD 两个系统写库成功了，结果 C 系统写库失败了，咋整？你这数据就不一致 了。

<h2 id="如何保证消息的可靠性？"><a href="#如何保证消息的可靠性？" class="headerlink" title="如何保证消息的可靠性？" data-pjax-state=""></a>如何保证消息的可靠性？</h2><p>消息到 MQ 的过程中搞丢，MQ 自己搞丢，MQ 到消费过程中搞丢。</p>
<p><code>生产者到RabbitMQ</code>：事务机制和 Confirm 机制，注意：事务机制和 Confirm 机制是互斥的，两者不能共存，会导致 RabbitMQ 报错。</p>
<p><code>RabbitMQ自身</code>：持久化、集群、普通模式、镜像模式。</p>
<p><code>RabbitMQ到消费者</code>：basicAck 机制、死信队列、消息补偿机制。</p>
<h2 id="什么是RoutingKey路由键？"><a href="#什么是RoutingKey路由键？" class="headerlink" title="什么是RoutingKey路由键？" data-pjax-state=""></a>什么是 RoutingKey 路由键？</h2><p>生产者将消息发送给交换器的时候，会指定一个 <code>RoutingKey</code>, 用来指定这个消息的路由规则，这个 <code>RoutingKey</code> 需要与交换器类型和绑定键 (<code>BindingKey</code>) 联合使用才能最终生效。</p>
<h2 id="Binding绑定？"><a href="#Binding绑定？" class="headerlink" title="Binding绑定？" data-pjax-state=""></a>Binding 绑定？</h2><p>通过绑定将交换器和队列关联起来，一般会指定一个 <code>BindingKey</code>, 这样 RabbitMq 就知道如何正确路由消息到队列了。</p>
<h2 id="交换器4种类型？"><a href="#交换器4种类型？" class="headerlink" title="交换器4种类型？" data-pjax-state=""></a>交换器 4 种类型？</h2><p>主要有以下 4 种。</p>

fanout: 把所有发送到该交换器的消息路由到所有与该交换器绑定的队列中。
direct: 把消息路由到 BindingKey 和 RoutingKey 完全匹配的队列中。
topic:
 匹配规则：

<figure class="highlight plain"><div class="highlight-tools "><i class="fas fa-angle-down expand "></i><div class="code-lang">Code</div><div class="copy-notice"></div><i class="fas fa-paste copy-button"></i></div><table><tbody><tr><td class="gutter"><pre><span class="line">1</span><br></pre></td><td class="code"><pre><span class="line">RoutingKey` 为一个 点号'.': 分隔的字符串。比如: `java.xiaoka.show</span><br></pre></td></tr></tbody></table></figure>


<p><code>BindingKey</code> 和 <code>RoutingKey</code> 一样也是点号 “.“分隔的字符串。</p>
<p><code>BindingKey</code> 可使用 * 和 # 用于做模糊匹配，* 匹配一个单词，# 匹配多个或者 0 个</p>
<p><code>headers</code>: 不依赖路由键匹配规则路由消息。是根据发送消息内容中的 <code>headers</code> 属性进行匹配。性能差，基本用不到。</p>
<h2 id="生产者消息运转？"><a href="#生产者消息运转？" class="headerlink" title="生产者消息运转？" data-pjax-state=""></a>生产者消息运转？</h2>
<p><code>Producer</code> 先连接到 Broker, 建立连接 Connection, 开启一个信道 (Channel)。</p>

<p><code>Producer</code> 声明一个交换器并设置好相关属性。</p>

<p><code>Producer</code> 声明一个队列并设置好相关属性。</p>

<p><code>Producer</code> 通过路由键将交换器和队列绑定起来。</p>

<p><code>Producer</code> 发送消息到 <code>Broker</code>, 其中包含路由键、交换器等信息。</p>

<p>相应的交换器根据接收到的路由键查找匹配的队列。</p>

<p>如果找到，将消息存入对应的队列，如果没有找到，会根据生产者的配置丢弃或者退回给生产者。</p>

<p>关闭信道。</p>

<p>管理连接。</p>


<h2 id="消费者接收消息过程？"><a href="#消费者接收消息过程？" class="headerlink" title="消费者接收消息过程？" data-pjax-state=""></a>消费者接收消息过程？</h2>
<p><code>Producer</code> 先连接到 <code>Broker</code>, 建立连接 <code>Connection</code>, 开启一个信道 (<code>Channel</code>)。</p>

<p>向 <code>Broker</code> 请求消费响应的队列中消息，可能会设置响应的回调函数。</p>

<p>等待 <code>Broker</code> 回应并投递相应队列中的消息，接收消息。</p>

<p>消费者确认收到的消息，<code>ack</code>。</p>

<p><code>RabbitMq</code> 从队列中删除已经确定的消息。</p>

<p>关闭信道。</p>

<p>关闭连接。</p>


<h3 id="交换器无法根据自身类型和路由键找到符合条件队列时，有哪些处理？"><a href="#交换器无法根据自身类型和路由键找到符合条件队列时，有哪些处理？" class="headerlink" title="交换器无法根据自身类型和路由键找到符合条件队列时，有哪些处理？" data-pjax-state=""></a>交换器无法根据自身类型和路由键找到符合条件队列时，有哪些处理？</h3>
mandatory ：true 返回消息给生产者。
mandatory: false 直接丢弃。

<h2 id="死信队列？"><a href="#死信队列？" class="headerlink" title="死信队列？" data-pjax-state=""></a>死信队列？</h2><p>DLX，全称为 <code>Dead-Letter-Exchange</code>，死信交换器，死信邮箱。当消息在一个队列中变成死信 (<code>dead message</code>) 之后，它能被重新被发送到另一个交换器中，这个交换器就是 DLX，绑定 DLX 的队列就称之为死信队列。</p>
<h2 id="导致的死信的几种原因？"><a href="#导致的死信的几种原因？" class="headerlink" title="导致的死信的几种原因？" data-pjax-state=""></a>导致的死信的几种原因？</h2>
消息被拒（<code>Basic.Reject /Basic.Nack</code>) 且 <code>requeue = false</code>。
消息 TTL 过期。
队列满了，无法再添加。

<h2 id="延迟队列？"><a href="#延迟队列？" class="headerlink" title="延迟队列？" data-pjax-state=""></a>延迟队列？</h2><p>存储对应的延迟消息，指当消息被发送以后，并不想让消费者立刻拿到消息，而是等待特定时间后，消费者才能拿到这个消息进行消费。</p>
<h2 id="优先级队列？"><a href="#优先级队列？" class="headerlink" title="优先级队列？" data-pjax-state=""></a>优先级队列？</h2>
优先级高的队列会先被消费。
可以通过 <code>x-max-priority</code> 参数来实现。
当消费速度大于生产速度且 Broker 没有堆积的情况下，优先级显得没有意义。

<h2 id="事务机制？"><a href="#事务机制？" class="headerlink" title="事务机制？" data-pjax-state=""></a>事务机制？</h2><p>RabbitMQ 客户端中与事务机制相关的方法有三个:</p>

<p><code>channel.txSelect</code> 用于将当前的信道设置成事务模式。</p>

<p><code>channel . txCommit</code> 用于提交事务 。</p>

<p><code>channel . txRollback</code> 用于事务回滚，如果在事务提交执行之前由于 RabbitMQ 异常崩溃或者其他原因抛出异常，通过 txRollback 来回滚。</p>


<h2 id="发送确认机制？"><a href="#发送确认机制？" class="headerlink" title="发送确认机制？" data-pjax-state=""></a>发送确认机制？</h2><p>生产者把信道设置为 <code>confirm</code> 确认模式，设置后，所有再改信道发布的消息都会被指定一个唯一的 ID，一旦消息被投递到所有匹配的队列之后，RabbitMQ 就会发送一个确认（<code>Basic.Ack</code>) 给生产者（包含消息的唯一 ID)，这样生产者就知道消息到达对应的目的地了。</p>
<h2 id="消费者获取消息的方式？"><a href="#消费者获取消息的方式？" class="headerlink" title="消费者获取消息的方式？" data-pjax-state=""></a>消费者获取消息的方式？</h2>
推
拉

<h2 id="消费者某些原因无法处理当前接受的消息如何来拒绝？"><a href="#消费者某些原因无法处理当前接受的消息如何来拒绝？" class="headerlink" title="消费者某些原因无法处理当前接受的消息如何来拒绝？" data-pjax-state=""></a>消费者某些原因无法处理当前接受的消息如何来拒绝？</h2><p>channel .basicNack channel .basicReject</p>
<h2 id="消息传输保证层级？"><a href="#消息传输保证层级？" class="headerlink" title="消息传输保证层级？" data-pjax-state=""></a>消息传输保证层级？</h2>
<p><code>At most once</code>: 最多一次。消息可能会丢失，但不会重复传输。</p>

<p><code>At least once</code>：最少一次。消息绝不会丢失，但可能会重复传输。</p>

<p><code>Exactly once</code>:  恰好一次，每条消息肯定仅传输一次。</p>


<h2 id="了解Virtual-Host吗"><a href="#了解Virtual-Host吗" class="headerlink" title="了解Virtual Host吗?" data-pjax-state=""></a>了解 Virtual Host 吗？</h2><p>每一个 RabbitMQ 服务器都能创建虚拟的消息服务器，也叫虚拟主机 (virtual host)，简称 vhost。默认为 “/”。</p>
<h2 id="集群中的节点类型？"><a href="#集群中的节点类型？" class="headerlink" title="集群中的节点类型？" data-pjax-state=""></a>集群中的节点类型？</h2>
<p>内存节点：ram, 将变更写入内存。</p>

<p>磁盘节点：disc, 磁盘写入操作。</p>

<p>RabbitMQ 要求最少有一个磁盘节点。</p>


<h2 id="队列结构？"><a href="#队列结构？" class="headerlink" title="队列结构？" data-pjax-state=""></a>队列结构？</h2><p>通常由以下两部分组成？</p>

<p><code>rabbit_amqqueue_process</code>: 负责协议相关的消息处理，即接收生产者发布的消息、向消费者交付消息、处理消息的确认 (包括生产端的 confirm 和消费端的 ack) 等。</p>

<p><code>backing_queue</code>: 是消息存储的具体形式和引擎，并向 rabbit a<code>mqqueue process</code> 提供相关的接口以供调用。</p>


<h2 id="RabbitMQ中消息可能有的几种状态"><a href="#RabbitMQ中消息可能有的几种状态" class="headerlink" title="RabbitMQ中消息可能有的几种状态?" data-pjax-state=""></a>RabbitMQ 中消息可能有的几种状态？</h2>
<p><code>alpha</code>: 消息内容 (包括消息体、属性和 headers) 和消息索引都存储在内存中 。</p>

<p><code>beta</code>: 消息内容保存在磁盘中，消息索引保存在内存中。</p>

<p><code>gamma</code>: 消息内容保存在磁盘中，消息索引在磁盘和内存中都有 。</p>

<p><code>delta</code>: 消息内容和索引都在磁盘中 。</p>


<h2 id="在何种场景下使用了消息中间件？"><a href="#在何种场景下使用了消息中间件？" class="headerlink" title="在何种场景下使用了消息中间件？" data-pjax-state=""></a>在何种场景下使用了消息中间件？</h2>
接口之间耦合比较严重
面对大流量并发时，容易被冲垮
存在性能问题

<h2 id="生产者如何将消息可靠投递到MQ？"><a href="#生产者如何将消息可靠投递到MQ？" class="headerlink" title="生产者如何将消息可靠投递到MQ？" data-pjax-state=""></a>生产者如何将消息可靠投递到 MQ？</h2>
<p>Client 发送消息给 MQ；</p>

<p>MQ 将消息持久化后，发送 Ack 消息给 Client，此处有可能因为网络问题导致 Ack 消息无法发送到 Client，那么 Client 在等待超时后，会重传消息；</p>

<p>Client 收到 Ack 消息后，认为消息已经投递成功。</p>


<h2 id="MQ如何将消息可靠投递到消费者？"><a href="#MQ如何将消息可靠投递到消费者？" class="headerlink" title="MQ如何将消息可靠投递到消费者？" data-pjax-state=""></a>MQ 如何将消息可靠投递到消费者？</h2>
<p>MQ 将消息 push 给 Client（或 Client 来 pull 消息）</p>

<p>Client 得到消息并做完业务逻辑</p>

<p>Client 发送 Ack 消息给 MQ，通知 MQ 删除该消息，此处有可能因为网络问题导致 Ack 失败，那么 Client 会重复消息，这里就引出消费幂等的问题；</p>

<p>MQ 将已消费的消息删除</p>


<h2 id="如何保证RabbitMQ消息队列的高可用"><a href="#如何保证RabbitMQ消息队列的高可用" class="headerlink" title="如何保证RabbitMQ消息队列的高可用?" data-pjax-state=""></a>如何保证 RabbitMQ 消息队列的高可用？</h2><p>RabbitMQ 有三种模式：<code>单机模式</code>，<code>普通集群模式</code>，<code>镜像集群模式</code>。</p>

<p><strong>单机模式</strong>：就是 demo 级别的，一般就是你本地启动了玩玩儿的，没人生产用单机模式。</p>

<p><strong>普通集群模式</strong>：意思就是在多台机器上启动多个 RabbitMQ 实例，每个机器启动一个。</p>

<p><strong>镜像集群模式</strong>：这种模式，才是所谓的 RabbitMQ 的高可用模式，跟普通集群模式不一样的是，你创建的 queue，无论元数据 (元数据指 RabbitMQ 的配置数据) 还是 queue 里的消息都会存在于多个实例上，然后每次你写消息到 queue 的时候，都会自动把消息到多个实例的 queue 里进行消息同步。</p>



# 原文链接:

[zhangc233](https://zhangc233.github.io/2021/07/30/RabbitMQ%E9%9D%A2%E8%AF%95%E9%A2%98/#%E9%98%9F%E5%88%97%E7%BB%93%E6%9E%84%EF%BC%9F)


# 参考文档

[sgg_rabbitmq](https://victorfengming.gitee.io/file/pdf/rabbitmq/sgg_rabbitmq.pdf)