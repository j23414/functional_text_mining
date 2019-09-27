"""
The MLStipper and strip_tags functions are borrowed verbatim from Eloff (stackoverflow #753052)
"""

import xml.etree.ElementTree as et

import nltk.corpus.reader.xmldocs as xml
from html.parser import HTMLParser

class MLStripper(HTMLParser):
    def __init__(self):
        self.reset()
        self.strict = False
        self.convert_charrefs= True
        self.fed = []
    def handle_data(self, d):
        self.fed.append(d)
    def get_data(self):
        return ''.join(self.fed).strip()

def strip_tags(xmlObj):
    s = MLStripper()
    s.feed(et.tostring(xmlObj).decode())
    return s.get_data()

class Author():
    def __init__(self, author):
        self.given_names = author.findtext("./name/given-names")
        self.surname = author.findtext("./name/surname")
        self.orcid = author.findtext("./contrib-id[@contrib-id-type='orcid']")
        self.email = author.findtext("./address/email")
        self.is_corresponding_author = "corrsep" in author.attrib

class PmcArticle():

    def __init__(self, article):
        #  self.citations = [c.text for c in article.findall("./back/ref-list/ref/element-citation/pub-id")]
        meta = article.find("./front/article-meta")
        self.title = strip_tags(meta.find("./title-group/article-title"))
        self.pmid = meta.findtext("./article-id[@pub-id-type='pmid']")
        self.pmc = meta.findtext("./article-id[@pub-id-type='pmc']")
        self.doi = meta.findtext("./article-id[@pub-id-type='doi']")
        self.authors = [Author(a) for a in meta.findall("./contrib-group/contrib[@contrib-type='author']")]
        # date
        date = meta.find("./pub-date") # does pub-type matter? ["epub", "pmc-release", "collection"]
        self.year = date.findtext("./year")
        self.month = date.findtext("./month")
        self.day = date.findtext("./day")
        # journal infor
        self.journal_name = article.findtext("./front/journal-meta/journal-title-group/journal-title")

        #  try:
        #      self.acknowledgements = article.findtext(article, "./back/ack/p")
        #  except IndexError:
        #      pass
        #  self.body = "\n".join(strip_tags(p) for p in article.findall(".//p"))


class PmcCorpusReader(xml.XMLCorpusReader):

    def __init__(self, root, fileids):
        xml.XMLCorpusReader.__init__(self, root, fileids, wrap_etree=False)
        self.cache = dict()

    def _parse(self, fileid=None, store=True):
        try:
            return self.cache[fileid]
        except KeyError:
            articleSet = super().xml(fileid)
            articleObjects = [PmcArticle(articleXml) for articleXml in articleSet.findall("./article")]
            if store:
                self.cache[fileid] = articleObjects
            return articleObjects

    def articles(self, fileid=None, store=True):
        if fileid in self.fileids():
            return self._parse(fileid=fileid, store=store)
        elif fileid is None:
            for fileid in self.fileids():
                for article in self._parse(fileid):
                    yield article
