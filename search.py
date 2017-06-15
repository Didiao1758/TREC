from whoosh.index import open_dir
from whoosh.qparser import QueryParser
import datetime
from whoosh import qparser
starttime = datetime.datetime.now()
ix = open_dir("indexDirStemming")
#ix = open_dir("indexDir")
time1 = datetime.datetime.now()
with ix.searcher() as searcher:
    query = QueryParser("content", ix.schema,group=qparser.OrGroup).parse(u"heroic acts")
    results = searcher.search(query,scored=True,limit=10000)
    print (len(results))
    time2 = datetime.datetime.now()
    print ("serarch time :")
    print (time2 - time1)

    print ('--------------------------')
    time3 = datetime.datetime.now()
    query1 = QueryParser("content", ix.schema,group=qparser.OrGroup).parse(u"New Hydroelectric Projects hydroelectric projects  under construction  country and location.  nature, extent, purpose, problem. ")
    results1 = searcher.search(query1,scored=True,limit=10000)
    print (len(results1))
    for temp in results1.items():
        print (temp)   
    time4 = datetime.datetime.now()
    print ('search1 time:')
    print (time4 - time3)
    print ('--------------------------')





    #for temp in results:
    #print (results[0])
endtime = datetime.datetime.now()
print (endtime - starttime) 	
print ('end')	
