# -*- coding: utf-8 -*-
from whoosh.index import create_in
from whoosh.fields import *
import  os.path
from whoosh.index import open_dir
from uitls import  parseXmlFile
import whoosh.index as index
import datetime
from whoosh.analysis import StemmingAnalyzer

starttime = datetime.datetime.now()
print ('index is processing...')
if not os.path.exists("indexDirStemming"):
    os.mkdir("indexDirStemming")

schema = Schema(title=TEXT(stored=False),
                content=TEXT(analyzer=analysis.StemmingAnalyzer(), stored=False),
                doc_id=ID(stored=True))
ix = create_in("indexDirStemming", schema)


# path of the NYTCORUPS
pathDataDir = u"/home/trec/jiaoliying/data"

ix = index.open_dir("indexDirStemming")
writer = ix.writer(limitmb=1024,procs=8,multisegment=True)
for i in  os.walk(pathDataDir):
    if(len(i[2]) != 0):
        for j in range(len(i[2])):
            path = os.path.join(i[0], i[2][j])
            (title1, content1, doc_id1) = parseXmlFile(path)
            # title1_unicode = unicode(title1, "utf-8")
            # content1_unicode = unicode(content1, "utf-8")
            # doc_id1_unicode = unicode(doc_id1, "utf-8")
            writer.add_document(title = title1, content = content1, doc_id = doc_id1)
writer.commit()

endtime = datetime.datetime.now()

print ('index is ending...')
print (endtime - starttime).seconds











#
# writer = ix.writer()
# writer.add_document(title=u"My document", content=u"This is my document!")
# writer.add_document(title=u"Second try", content=u"This is the second example.")
# writer.add_document(title=u"Third time's the charm", content=u"Examples are many.")
# writer.commit()

# writer = BufferedWriter(ix, period=120, limit=20)


















# writer = ix.writer()
# writer.add_document(title=u"First document", path=u"/a",content=u"This is the first document we've added!")
# writer.add_document(title=u"Second document", path=u"/b",content=u"The second one is even more interesting!")
# writer.commit()



#
# ixRead = open_dir("indexDir")
# from whoosh.qparser import QueryParser
# with ix.searcher() as searcher:
#     query = QueryParser("content", ix.schema).parse("first")
#     results = searcher.search(query)
#     print(results[0])
#
# ixRead = open_dir("index")
#

# {"title": u"First document", "path": u"/a"}
