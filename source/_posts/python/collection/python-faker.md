---
title: "Python中的faker"
date:       2020-02-24
subtitle: "(伪装者)创建假数据"
tags:
	- Python
	- background
	- solution
	- database
---









## 起步
faker (伪装者)创建假数据  
工作中，有时候我们需要伪造一些假数据，如何使用 Python 伪造这些看起来一点也不假的假数据呢？   
Python 有一个包叫 Faker，使用它可以轻易地伪造姓名、地址、手机号等等信息。

## 1.安装faker包

```
pip install faker
```

## 2.安装完成后
使用时需要先创建一个 Faker 对象，创建方法有两种，一种是直接通过构造函数来创建，另一种是通过工厂函数来创建。

```
>>> from faker import Faker, Factory
>>> fake1 = Factory.create() # 通过工厂函数来创建
>>> fake1.name() # 随机生成一个姓名
'Austin Parker'
>>> fake2 = Faker() # 通过构造函数来创建
>>> fake2.name() # 随机生成一个姓名
'Linda Castaneda'
```

## 3.各种数据项
### 3.1中国人名

```
>>> fake = Faker("zh_CN")
>>> fake.name()
'西建平'
```

### 3.2地址

```
>>> fake.city() # 城市名称
'辛集县'
>>> fake.street_name() # 街道名称
'荆街'
>>> fake.country_code() # 国家编号
'DM'
>>> fake.longitude() # 经度
Decimal('134.520688')
>>> fake.address() # 地址
'吉林省宜都市清河俞街j座 292426'
>>> fake.province() # 省份
'宁夏回族自治区'
>>> fake.latitude() # 纬度
Decimal('-14.386640')
>>> fake.street_address() # 街道地址
'益路v座'
>>> fake.city_suffix() # 市
'市'
>>> fake.postcode() # 邮政编码
'530435'
>>> fake.country() # 国家
'维尔京群岛'
>>> fake.street_suffix() # 街道后缀
'街'
>>> fake.district() # 区
'安次'
>>> fake.geo_coordinate(center=None, radius=0.001) # 地理坐标
Decimal('52.985293')
>>> fake.city_name() # 城市名称
'沈阳'
>>> fake.building_number() # 建筑编号
'C座'
```

### 3.3车牌号

```
>>> fake.license_plate() # 车牌号
'26FX4'
```

## 4.条形码

```
>>> fake.bank_country()
'GB'
>>> fake.iban()
'GB39SNOA2073712937476'
>>> fake.bban()
'NYJX570813729289
```

## 5.颜色

```
>>> fake.color_name() # 颜色名称
'SlateGray'
>>> fake.safe_hex_color() # safe 颜色 16 进制编号
'#111100'
>>> fake.safe_color_name() # safe颜色名称
'black'
>>> fake.rgb_color() # 颜色的 rgb 值
'46,180,218'
>>> fake.hex_color() # 颜色 16 进制编号
'#81b632'
>>> fake.rgb_css_color()
'rgb(27,224,190)'
```

## 6.公司

```
>>> fake.catch_phrase()
'Persistent bandwidth-monitored system engine'
>>> fake.company_prefix() # 公司名前缀
'联通时科'
>>> fake.company() # 公司名
'方正科技信息有限公司'
>>> fake.company_suffix() # 公司名后缀
'信息有限公司'
>>> fake.bs()
'transition revolutionary action-items'
```

## 7.信用卡

```
>>> fake.credit_card_full(card_type=None) # 完整卡信息
'JCB 15 digit\n秀梅 段\n180053229428785 07/21\nCVC: 628\n'
>>> fake.credit_card_provider(card_type=None) # 卡的提供者
'VISA 16 digit'
>>> fake.credit_card_expire(start="now", end="+10y", date_format="%m/%y") # 卡的有效期
'06/19'
>>> fake.credit_card_number(card_type=None) # 卡号
'4946562273912'
>>> fake.credit_card_security_code(card_type=None) # 卡的安全密码
'985'
```

## 8.货币


```
>>> fake.cryptocurrency()
('BTC', 'Bitcoin')
>>> fake.cryptocurrency_code()
'USDT'
>>> fake.currency_code()
'SZL'
>>> fake.currency_name()
'Dominican peso'
>>> fake.currency()
('ZWD', 'Zimbabwean dollar')
>>> fake.cryptocurrency_name()
'Cardano'
```

## 9.时间日期

```
>>> fake.date_time(tzinfo=None) # 随机日期时间
datetime.datetime(2001, 3, 18, 17, 57, 44)
>>> fake.iso8601(tzinfo=None) # 以iso8601标准输出的日期
'1973-11-16T22:58:37'
>>> fake.date_time_this_month(before_now=True, after_now=False, tzinfo=None) # 本月的某个日期
datetime.datetime(2017, 11, 1, 14, 33, 48)
>>> fake.date_time_this_year(before_now=True, after_now=False, tzinfo=None) # 本年的某个日期
datetime.datetime(2017, 3, 2, 13, 55, 31)
>>> fake.date_time_this_decade(before_now=True, after_now=False, tzinfo=None)  # 本年代内的一个日期
datetime.datetime(2010, 3, 26, 6, 33, 23)
>>> fake.date_time_this_century(before_now=True, after_now=False, tzinfo=None)  # 本世纪一个日期
datetime.datetime(2015, 7, 21, 19, 27, 53)
>>> fake.date_time_between(start_date="-30y", end_date="now", tzinfo=None)  # 两个时间间的一个随机时间
datetime.datetime(2005, 12, 3, 17, 17, 15)
>>> fake.timezone() # 时区
'America/Guatemala'
>>> fake.time(pattern="%H:%M:%S") # 时间（可自定义格式）
'11:21:52'
>>> fake.am_pm() # 随机上午下午
'PM'
>>> fake.month() # 随机月份
'02'
>>> fake.month_name() # 随机月份名字
'August'
>>> fake.year() # 随机年
'1974'
>>> fake.day_of_week() # 随机星期几
'Sunday'
>>> fake.day_of_month() # 随机月中某一天
'02'
>>> fake.time_delta() # 随机时间延迟
datetime.timedelta(13371, 27637)
>>> fake.date_object()  # 随机日期对象
datetime.date(1983, 1, 26)
>>> fake.time_object() # 随机时间对象
datetime.time(17, 8, 56)
>>> fake.unix_time() # 随机unix时间（时间戳）
1223246848
>>> fake.date(pattern="%Y-%m-%d") # 随机日期（可自定义格式）
'1984-04-20'
>>> fake.date_time_ad(tzinfo=None)  # 公元后随机日期
datetime.datetime(341, 9, 11, 8, 6, 9)
```

## 10.工作

```
>>> fake.job()
'Development worker, community'
```

## 11.文件

```
>>> fake.unix_partition(prefix=None) # unix 分区
'/dev/sdg5'
>>> fake.file_name(category=None, extension=None) # 文件名
'看到.flac'
>>> fake.unix_device(prefix=None) # unix 设备
'/dev/vdu'
>>> fake.file_path(depth=1, category=None, extension=None)
'/合作/国家.webm'
>>> fake.file_extension(category=None) # 文件扩展信息
'mp3'
>>> fake.mime_type(category=None)
'text/csv'
```

## 12.互联网

```
>>> fake.ipv4(network=False)  # ipv4地址
'104.225.105.10'
>>> fake.ipv6(network=False)  # ipv6地址
'dea6:ca11:39d0:b49f:fff1:82f1:bf88:698b'
>>> fake.uri_path(deep=None) # uri路径
'search/categories'
>>> fake.uri_extension() # uri扩展名
'.htm'
>>> fake.uri() # uri
'https://www.wei.com/terms/'
>>> fake.url() # url
'http://zheng.org/'
>>> fake.image_url(width=None, height=None)  # 图片url
'https://www.lorempixel.com/700/990'
>>> fake.domain_word() # 域名主体
'hu'
>>> fake.domain_name() # 域名
'hu.cn'
>>> fake.tld() # 域名后缀
'com'
>>> fake.user_name() # 用户名
'xia13'
>>> fake.user_agent() # UA
'Opera/8.33.(Windows NT 5.1; an-ES) Presto/2.9.171 Version/10.00'
>>> fake.mac_address() # MAC地址
'd6:38:cc:2a:76:b2'
>>> fake.safe_email() # 安全邮箱
'mingli@example.net'
>>> fake.free_email() # 免费邮箱
'tao44@gmail.com'
>>> fake.company_email()  # 公司邮箱
'jingzhong@wang.cn'
>>> fake.email() # 邮箱
'changjun@hao.com'
```

## 13.电话号码

```
>>> fake.phonenumber_prefix() # 运营商号段，手机号前三位
132
>>> fake.msisdn()
'5445934248280'
>>> fake.phone_number() # 手机号
'18666613199'
```

## 14.身份证号码

```
>>> fake.ssn(min_age=18, max_age=90)
'460201193310128795'
人物
```

## 15.人物

```
>>> fake.suffix_female()
''
>>> fake.last_name() # 姓
'董'
>>> fake.suffix_male()
''
>>> fake.first_name_male() # 男性名
'淑兰'
>>> fake.name() # 姓名
'空丹'
>>> fake.first_name() # 名
'凯'
>>> fake.last_name_male() # 男性姓
'却'
>>> fake.name_male() # 女性姓名
'申柳'
>>> fake.romanized_name()
'Xia Xu'
>>> fake.suffix()
''
>>> fake.first_name_female()
'琴'
>>> fake.last_name_female()
'羿'
>>> fake.prefix_male()
''
>>> fake.name_female()
'明璐'
>>> fake.prefix_female()
''
>>> fake.first_romanized_name()
'Li'
>>> fake.prefix()
''
>>> fake.last_romanized_name()
'Tan'
```

## 16.profile 人物属性

```
>>> fake.profile(fields=None, sex=None)
{'residence': '广东省呼和浩特县锡山龙街N座 403716', 'sex': 'M', 'website': ['http://zheng.org/'], 'birthdate': '1971-02-20', 'ssn': '513226197904080189', 'mail': 'jing95@hotmail.com', 'job': 'Ceramics designer', 'current_location': (Decimal('-86.424001'), Decimal('-153.969207')), 'blood_group': '0+', 'address': '广东省北京市永川深圳街w座 974761', 'company': '双敏电子传媒有限公司', 'username': 'xiajiang', 'name': '韩玉华'}
>>> fake.simple_profile(sex=None)
{'mail': 'dengna@yahoo.com', 'address': '西藏自治区楠市江北闻街v座 524952', 'username': 'guiying17', 'sex': 'F', 'birthdate': '1995-10-14', 'name': '姜敏'}
```

## 17.lorem

```
>>> fake.paragraphs(nb=3, ext_word_list=None)
['当然分析选择得到感觉关于.', '位置之间应用这种能够.', '你的处理上海.人员下载主要来自只是首页.图片有些所有详细发布.']
>>> fake.word(ext_word_list=None)
'最大'
>>> fake.text(max_nb_chars=200, ext_word_list=None)
'相关图片完成以及人民你的.出现语言计划浏览注意处理非常.\n一样制作个人留言留言这是说明.记者主要由于规定点击时候一个.公司时候系列推荐日期.\n汽车学校发现方法.合作学生她的查看各种次数所有或者.\n深圳世界文化不是结果一切.部分具有商品进行评论市场最后.数据回复名称谢谢系列.\n政府威望两个那些一个加入.以下那些需要以下.\n他 们不会工作资源那个这些所有文章.不会目前为什系统.'
>>> fake.sentences(nb=3, ext_word_list=None)
['具有信息东西方式教育发布自己.', '业务类型社会作品方法.', '帖子作者都是.']
>>> fake.paragraph(nb_sentences=3, variable_nb_sentences=True, ext_word_list=None)
'不能加入最大重要.发现注意免费生产这是.'
>>> fake.words(nb=3, ext_word_list=None)
['关于', '实现', '首页']
>>> fake.sentence(nb_words=6, variable_nb_words=True, ext_word_list=None)
'发现成功一点系统空间全国比较.'
```