from whoosh.index import open_dir
from whoosh.fields import Schema, TEXT, KEYWORD, ID, STORED
from whoosh.fields import Schema, TEXT, KEYWORD, ID, STORED
ix = open_dir("indexDirTest")
writer = ix.writer()
writer.add_field("publication_day_of_week", TEXT(stored=True))
writer.add


