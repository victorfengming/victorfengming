---
title: "Gradle配置阿里云镜像"
cover: "/img/lynk/45.jpg"
date:       2021-08-31
subtitle: "项目自动化构建开源工具"
tags:
	- solution
---

# 概念

Gradle是一个基于Apache Ant和Apache Maven概念的项目自动化构建开源工具。它使用一种基于Groovy的特定领域语言(DSL)来声明项目设置，目前也增加了基于Kotlin语言的kotlin-based DSL，抛弃了基于XML的各种 繁琐配置。

# 镜像源配置


## 单个项目

使用阿里云国内镜像


生效，在项目中的build.gradle修改内容


```groovy
buildscript {
    repositories {
        maven { url 'http://maven.aliyun.com/nexus/content/groups/public/' }
                maven{ url 'http://maven.aliyun.com/nexus/content/repositories/jcenter'}
    }
    dependencies {
        classpath 'com.android.tools.build:gradle:2.2.3'

        // NOTE: Do not place your application dependencies here; they belong
        // in the individual module build.gradle files
    }        
}

allprojects {
    repositories {
        maven { url 'http://maven.aliyun.com/nexus/content/groups/public/' }
        maven{ url 'http://maven.aliyun.com/nexus/content/repositories/jcenter'}
    }
}
```



## 默认源配置


对所有项目生效，在USER_HOME/.gradle/下创建init.gradle文件

```groovy

allprojects{
    repositories {
        def ALIYUN_REPOSITORY_URL = 'http://maven.aliyun.com/nexus/content/groups/public'
        def ALIYUN_JCENTER_URL = 'http://maven.aliyun.com/nexus/content/repositories/jcenter'
        def GRADLE_LOCAL_RELEASE_URL = 'https://repo.gradle.org/gradle/libs-releases-local'
        def ALIYUN_SPRING_RELEASE_URL = 'https://maven.aliyun.com/repository/spring-plugin'
        
        all { ArtifactRepository repo ->
            if(repo instanceof MavenArtifactRepository){
                def url = repo.url.toString()
                if (url.startsWith('https://repo1.maven.org/maven2')) {
                    project.logger.lifecycle "Repository ${repo.url} replaced by $ALIYUN_REPOSITORY_URL."
                    remove repo
                }
                if (url.startsWith('https://jcenter.bintray.com/')) {
                    project.logger.lifecycle "Repository ${repo.url} replaced by $ALIYUN_JCENTER_URL."
                    remove repo
                }
                if (url.startsWith('http://repo.spring.io/plugins-release')) {
                    project.logger.lifecycle "Repository ${repo.url} replaced by $ALIYUN_SPRING_RELEASE_URL."
                    remove repo
                }
                
            }
        }
        maven {
            url ALIYUN_REPOSITORY_URL     
        }
        
        maven {            
            url ALIYUN_JCENTER_URL          
        }
        maven {            
            url ALIYUN_SPRING_RELEASE_URL
        }
        maven {
            url GRADLE_LOCAL_RELEASE_URL
        }
        
    }
    

}
```


## 网上搜集的常用仓库地址

```groovy
epositories {

    mavenCentral()

    maven { url "https://jitpack.io" }

    maven { url "http://maven.aliyun.com/nexus/content/groups/public/" }

    maven { url 'http://maven.oschina.net/content/groups/public/' }

    maven { url 'https://oss.sonatype.org/content/repositories/snapshots/' }

    maven { url "http://maven.springframework.org/release" }

    maven { url "http://maven.restlet.org" }

    maven { url "http://mirrors.ibiblio.org/maven2" }

    maven {

        url "http://repo.baichuan-android.taobao.com/content/groups/BaichuanRepositories/"

    }

    maven { url 'https://maven.fabric.io/public' }

    jcenter()

    google()

}
```

## 阿里仓库集合

```groovy
apache snapshots	
proxy	
SNAPSHOT	
https://maven.aliyun.com/repository/apache-snapshots
central	
proxy	
RELEASE	
https://maven.aliyun.com/repository/central
google	
proxy	
RELEASE	
https://maven.aliyun.com/repository/google
gradle-plugin	
proxy	
RELEASE	
https://maven.aliyun.com/repository/gradle-plugin
jcenter	
proxy	
RELEASE	
https://maven.aliyun.com/repository/jcenter
spring	
proxy	
RELEASE	
https://maven.aliyun.com/repository/spring
spring-plugin	
proxy	
RELEASE	
https://maven.aliyun.com/repository/spring-plugin
public	
group	
RELEASE	
https://maven.aliyun.com/repository/public
releases	
hosted	
RELEASE	
https://maven.aliyun.com/repository/releases
snapshots	
hosted	
SNAPSHOT	
https://maven.aliyun.com/repository/snapshots
grails-core	
proxy	
RELEASE	
https://maven.aliyun.com/repository/grails-core
```


## 注意事项

build.gradle 文件内 对于 顺序有要求(注意避坑)


