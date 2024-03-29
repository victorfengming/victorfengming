---
title: "Python自然语言处理工具小结"
cover: "/img/lynk/91.jpg"
date:       2019-08-29
tags:
	- Python
	- background
	- solution
---












### Python 的几个自然语言处理工具

- NLTK:NLTK 在用 Python 处理自然语言的工具中处于领先的地位。它提供了 WordNet 这种方便处理词汇资源的借口，还有分类、分词、除茎、标注、语法分析、语义推理等类库。

- Pattern:Pattern 的自然语言处理工具有词性标注工具(Part-Of-Speech Tagger)，N元搜索(n-gram search)，情感分析(sentiment analysis)，WordNet。支持机器学习的向量空间模型，聚类，向量机。

- TextBlob:TextBlob 是一个处理文本数据的 Python 库。提供了一些简单的api解决一些自然语言处理的任务，例如词性标注、名词短语抽取、情感分析、分类、翻译等等。

- Gensim:Gensim 提供了对大型语料库的主题建模、文件索引、相似度检索的功能。它可以处理大于RAM内存的数据。作者说它是“实现无干预从纯文本语义建模的最强大、最高效、最无障碍的软件。

- PyNLPI:它的全称是：Python自然语言处理库（Python Natural Language Processing Library，音发作: pineapple） 这是一个各种自然语言处理任务的集合，PyNLPI可以用来处理N元搜索，计算频率表和分布，建立语言模型。他还可以处理向优先队列这种更加复杂的数据结构，或者像 Beam 搜索这种更加复杂的算法。

- spaCy:这是一个商业的开源软件。结合Python和Cython，它的自然语言处理能力达到了工业强度。是速度最快，领域内最先进的自然语言处理工具。

- Polyglot:Polyglot 支持对海量文本和多语言的处理。它支持对165种语言的分词，对196中语言的辨识，40种语言的专有名词识别，16种语言的词性标注，136种语言的情感分析，137种语言的嵌入，135种语言的形态分析，以及69中语言的翻译。

- MontyLingua:MontyLingua 是一个自由的、训练有素的、端到端的英文处理工具。输入原始英文文本到 MontyLingua ，就会得到这段文本的语义解释。适合用来进行信息检索和提取，问题处理，回答问题等任务。从英文文本中，它能提取出主动宾元组，形容词、名词和动词短语，人名、地名、事件，日期和时间，等语义信息。

- BLLIP Parser:BLLIP Parser（也叫做Charniak-Johnson parser）是一个集成了产生成分分析和最大熵排序的统计自然语言工具。包括 命令行 和 python接口 。

- Quepy:Quepy是一个Python框架，提供将自然语言转换成为数据库查询语言。可以轻松地实现不同类型的自然语言和数据库查询语言的转化。所以，通过Quepy，仅仅修改几行代码，就可以实现你自己的自然语言查询数据库系统。GitHub:https://github.com/machinalis/quepy

- HanNLP：HanLP是由一系列模型与算法组成的Java工具包，目标是普及自然语言处理在生产环境中的应用。不仅仅是分词，而是提供词法分析、句法分析、语义理解等完备的功能。HanLP具备功能完善、性能高效、架构清晰、语料时新、可自定义的特点。文档使用操作说明：Python调用自然语言处理包HanLP 和 菜鸟如何调用HanNLP