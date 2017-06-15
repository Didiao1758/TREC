from whoosh.index import create_in
from whoosh.fields import *
import  os.path
from whoosh.index import open_dir
from uitls import  parseXmlFile







path = "F:\\BaiduNetdiskDownload\\nyt_corpus_LDC2008T19\\nyt_corpus\\data\\2007\\01"
# print  parseXmlFile(path)
count = 0

for i in  os.walk(path):
    count += 1
    path = os.path.join(i[0], i[2][0])
    print path
    print  parseXmlFile(path)

    break





print '---------------------------------'














schema = Schema(title=TEXT(stored=True), path=ID(stored=True), content=TEXT)

if not os.path.exists("index"):
    os.mkdir("index")
ix = create_in("index", schema)
ixRead = open_dir("index")
writer = ix.writer()
writer.add_document(title=u"First document", path=u"/a",content=u"This is the first document we've added!")
writer.add_document(title=u"Second document", path=u"/b",content=u"The second one is even more interesting!")
writer.commit()
from whoosh.qparser import QueryParser
with ix.searcher() as searcher:
    query = QueryParser("content", ix.schema).parse("first")
    results = searcher.search(query)
    print(results[0])

ixRead = open_dir("index")
# {"title": u"First document", "path": u"/a"}