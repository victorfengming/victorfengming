---
title: "ELK启动问题解决方案"
cover: "/img/lynk/77.jpg"
date:       2021-03-12
subtitle: ""
tags:
	- solution
	- elk
---

## elk

elasticsearch

lotstash

kibana

# 安装

报错解决:

- [csdn](https://blog.csdn.net/ywdhzxf/article/details/89740406)

- [csdn](https://blog.csdn.net/zxz9325/article/details/110262417?utm_medium=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-1.control&dist_request_id=&depth_1-utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-1.control)

- [voidcn](http://www.voidcn.com/article/p-raygpaqb-bys.html)


## 更多: 

[elk课件](http://victorfengming.gitee.io/elk/)


---





版本





 elasticsearch kibana logstash filebeat 都用6.8.0的哈



机器

10.221.154.185

10.221.154.186

10.221.154.187



https://blog.csdn.net/yehongzhi1994/article/details/109459225

官网下载



> filebeat-6.8.0-linux-x86_64.tar.gz
>
> logstash-6.8.0.tar.gz
>
> elasticsearch-6.8.0.tar.gz
>
> kibana-6.8.0-linux-x86_64.tar.gz



 找到config目录下的elasticsearch.yml文件，修改配置： 

```yml
cluster.name: 154-es
node.name: node-185
bootstrap.memory_lock: true
bootstrap.system_call_filter: false
network.host: 10.221.154.185
http.port: 9003
discovery.zen.ping.unicast.hosts: ["10.221.154.182", "10.221.154.183"]
discovery.zen.minimum_master_nodes: 2
node.master: false
node.data: true
node.ingest: false
```





es配置

```yml
cluster.name: 154-es
node.name: node-185
network.host: 10.221.154.185
http.port: 9003
path.data: /opt/app/elk6.8.0/elasticsearch-6.8.0/data
path.logs: /opt/app/elk6.8.0/elasticsearch-6.8.0/logs

xpack.security.enabled: true

xpack.security.transport.ssl.enable: true

xpack.security.transport.ssl.verification_mode: certificate
xpack.security.transport.ssl.keystore.path: /opt/app/elk6.8.0/elasticsearch-6.8.0/elastic-certificates.p12
xpack.security.transport.ssl.truststore.path: /opt/app/elk6.8.0/elasticsearch-6.8.0/elastic-certificates.p12
```





修改配置

```shell
cd /opt/app/elk6.8.0/elasticsearch-6.8.0/config/
vi elasticsearch.yml
```

查找替换

```
 :%s/\/\//#/g 
```

%s全局

\/\/  待匹配的字符

`# 要替换的字符`

g匹配到的全替换

查找替换

```shell
 :%s/#/\r# /g
```





配置

```yml
network.host: 10.221.154.185
http.port: 9003
path:
    data: /opt/app/elk6.8.0/elasticsearch-6.8.0/data
    logs: /opt/app/elk6.8.0/elasticsearch-6.8.0/logs
bootstrap.memory_lock: false
bootstrap.system_call_filter: false


xpack.security.enabled: true

xpack.security.transport.ssl.enable: true

xpack.security.transport.ssl.verification_mode: certificate
xpack.security.transport.ssl.keystore.path: /opt/app/elk6.8.0/elasticsearch-6.8.0/elastic-certificates.p12
xpack.security.transport.ssl.truststore.path: /opt/app/elk6.8.0/elasticsearch-6.8.0/elastic-certificates.p12
```





# elasticsearch

## 启动es

>ps -ef|grep ela


```
cd /opt/app/elk6.8.0/elasticsearch-6.8.0

rm output.log

nohup ./bin/elasticsearch >> output.log 2>&1 &

ps -ef|grep ela

tail -f output.log
```

## 解决方案

解决1: [es check the logs and fix your configuration or disable system call filters](https://blog.csdn.net/qq_21383435/article/details/108962457)





# kibana



配置文件

```yml

#修改如下配置
server.port: 8080
server.host: "0.0.0.0"
##修改为自己es的端口
elasticsearch.url: "http://10.221.154.185:9003"
kibana.index: ".kibana"
i18n.locale: "zh-CN"	# 配置中文 6.7以后版本可直接配置
```



启动脚本

```

cd /opt/app/elk6.8.0/kibana-6.8.0-linux-x86_64/bin

rm output.log

nohup ./kibana >> output.log 2>&1 &

ps -ef|grep kibana
```







---





# filebeat

## 完整 filebeat-logstash-ES

10.221.154.188

https://www.cnblogs.com/lwx57280/p/13742433.html


配值

```shell
cd /opt/app/elk6.8.0/filebeat-6.8.0-linux-x86_64

vi f2l2e-log.yml
```


```yml
filebeat.inputs:
- type: log
  enabled: true
  paths:
    - /opt/applog/*.log
  tags: ["web", "test"]
  fields:
    from: test-web
  fields_under_root: false
setup.template.settings:
  index.number_of_shards: 1
output.logstash:
  hosts: ["10.221.154.186:5044"]
setup.kibana:
  hosts: "10.221.154.187:8080"
```



启动

```shell
cd /opt/app/elk6.8.0/filebeat-6.8.0-linux-x86_64

rm output1.log

nohup ./filebeat -e -c ./f2l2e-log.yml  >> output1.log 2>&1 &
# -e 标准启动 -c 指定配置文件
ps -ef|grep filebeat

```

---

```shell
cd /opt/applog/

echo "victor279" >> q.log
```





## 测试 filebeat-ES

配值

```shell
cd /opt/app/elk6.8.0/filebeat-6.8.0-linux-x86_64

vi f2e-log.yml
```


```yml
filebeat.inputs:
- type: log
  enabled: true
  paths:
    - /opt/applog/*.log
  tags: ["web", "test"]
  fields:
    from: test-web
  fields_under_root: false 
setup.template.settings:
  index.number_of_shards: 1
output.elasticsearch:
  hosts: ["10.221.154.185:9003"]
```



启动

```shell
cd /opt/app/elk6.8.0/filebeat-6.8.0-linux-x86_64

rm output2.log

nohup ./filebeat -e -c ./f2e-log.yml  >> output2.log 2>&1 &
# -e 标准启动 -c 指定配置文件

ps -ef|grep filebeat

```



---

```shell
cd /opt/applog/

echo "victor990" >> c.log
```










ELK : https://blog.csdn.net/beyond_qjm/article/details/81943187



# Logstash



## 完整 filebeat-logstash-ES



https://blog.csdn.net/beyond_qjm/article/details/81945527



```shell

# ./logstash -f ../config/logstash-sample.conf 

cd /opt/app/elk6.8.0/logstash-6.8.0/

rm output.log

nohup ./bin/logstash -f ./config/f2l2e-pipelines.yml   >> output.log 2>&1 &

ps -ef|grep logstash

tail -f output.log
```



---

## 测试 logstash-ES



---

```yml
input {
    file {
        path => "/opt/applog/*.log"
        start_position => "beginning"
    }
}
filter {
    mutate {
        split => {"message"=>"|"}
    }
}
output {
    elasticsearch {
        hosts => ["10.221.154.185:9003"]
    }
}
```

```shell
cd /opt/app/elk6.8.0/logstash-6.8.0

rm output.log

nohup ./bin/logstash -f ./config/l2e-piplines.yml  >> output.log 2>&1 &

ps -ef|grep logstash

cat output.log
```



---

```shell
cd /opt/applog/

echo "victor494" >> f.log
```



## input from filebeat




```yml
input {
   beats {
     port => 5044   #要监听的端口
   }
}
filter {
    mutate {
        split => {"message"=>"|"}
    }
}
output {
    elasticsearch {
        hosts => ["10.221.154.185:9003"]
    }
}
```


```shell
cd /opt/app/elk6.8.0/logstash-6.8.0

rm output.log

nohup ./bin/logstash -f ./config/f2l2e-pipelines.yml  >> output.log 2>&1 &

ps -ef|grep logstash

tail -f output.log
```



```shell
cd /opt/applog/

echo "victor991" >> f.log
```

# todo

单独测试 

filebeat 连 logstash

 ```
touch f2l-pipelines.yml
 ```

```yml
input {
   beats {
     port => 5044   #要监听的端口
   }
}
output {
    stdout { codec => rubydebug }
}
```

```shell
cd /opt/app/elk6.8.0/logstash-6.8.0

rm output.log

nohup ./bin/logstash -f ./config/f2l-pipelines.yml  >> output.log 2>&1 &

ps -ef|grep logstash
```



---







```yml
filebeat.inputs:
- type: log
  enabled: true
  paths:
    - /opt/applog/*.log
  tags: ["web", "test"]
  fields:
    from: test-web
  fields_under_root: false
setup.template.settings:
  index.number_of_shards: 1
output.logstash:
  hosts: ["10.221.154.186:5044"]
```

```shell
cd /opt/app/elk6.8.0/filebeat-6.8.0-linux-x86_64

rm output.log

nohup ./filebeat -e -c ./f2l-log.yml  >> output1.log 2>&1 &
# -e 标准启动 -c 指定配置文件
ps -ef|grep filebeat



```

