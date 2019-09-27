#!/usr/bin/env python3

import sys
import PmcCorpusReader as pmc

if __name__ == '__main__':
    root = sys.argv[1]
    pattern = sys.argv[2]
    pmcCorpus = pmc.PmcCorpusReader(root=sys.argv[1], fileids=sys.argv[2])

    for article in pmcCorpus.articles(): 
        authorList = ", ".join([f'{author.given_names} {author.surname}' for author in article.authors])
        row = (
            article.pmid,
            "PMC" + article.pmc,
            article.doi,
            "-".join([article.year, article.month, article.day]),
            article.title,
            article.journal_name,
            authorList
        )
        print("\t".join(row))
