# TREC
文件描述:
1. indexing.py建立索引的模块,建立在当前目录下,索引大约8.5G
2. utils.py 对语料库的xml文档提取docu_id, title, full_text三个属性，后续可以在上面添加提取别的属性
3. serarch.py 检索的模块, 对一个query进行查询，并且把top10000的结果对应的id和score输出
4. whooshDemo.py 自己测试用的，whoosh全过程简述
5. modifyIndex.py 更改schema的模块,现在还没用上，可能后续需要添加schema的除了id,title,content之外的其他field
6. test.py 自己测试用

