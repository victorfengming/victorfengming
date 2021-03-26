---
title: "gitbook添加valine评论功能"
date: 2021-03-26 06:07:08
cover: "/img/lynk/03.jpg"
author: "victor"
tags:
    - valine
    - gitbook
---


>首先你需要获取appId和appKey


可以参考https://valine.js.org/quickstart.html

![image-20210326140936833](image-20210326140936833.png)

![image-20210326141024110](image-20210326141024110.png)

![image-20210326141011256](image-20210326141011256.png)

![image-20210326141048200](image-20210326141048200.png)

![image-20210326141125850](image-20210326141125850.png)

---

在创建好应用后

在你的gitbook目录中,创建`book.json`

添加内容到`book.json`

```json
{
    "plugins": ["valine"],
    "pluginsConfig": {
        "valine": {
            "appId": "your appId",
            "appKey": "your appKey"
        }
    }
}
```

安装插件

```bash
gitbook install ./
```

接着可使用插件了，效果如下：

![image-20210326141326925](image-20210326141326925.png)