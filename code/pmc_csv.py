#!/usr/bin/env python3

import sys
import re
import PmcCorpusReader as pmc

def usage():
    print("USAGE  pmc_csv.py <root> <fileid_expr>", file=sys.stderr)
    print(" where  <root> is the directory where the PMC XML files are written", file=sys.stderr)
    print("        <fileid_expr> is a Perl-style regular expression that should match one or more files in <root>", file=sys.stderr)

if __name__ == '__main__':

    if len(sys.argv) == 1 or sys.argv[1] in {"-h", "--help", "-?"}:
        usage()
        sys.exit(0)

    if len(sys.argv) != 3:
        print("ERROR: Expected 2 arguments, got {len(sys.argv)}", file=sys.stderr)
        usage()
        sys.exit(1)

    root = sys.argv[1]
    pattern = sys.argv[2]
    try:
        pmcCorpus = pmc.PmcCorpusReader(root=sys.argv[1], fileids=sys.argv[2])
    except re.error as e:
        print(f"Bad regular expression ('{sys.argv[2]}'), expect a Perl-style regex like '.*.xml':", file=sys.stderr)
        print("  UNIX globs like '*.xml' will NOT work", file=sys.stderr)
        print(f'  {str(e)}', file=sys.stderr)
        sys.exit(1)

    for article in pmcCorpus.articles():

        authorList = ", ".join([author.fullname() for author in article.authors])

        row = (
            article.get_pmid(),
            "PMC" + article.get_pmc(),
            article.get_doi(),
            article.get_date(),
            article.get_title(),
            article.get_journal_name(),
            authorList
        )
        print("\t".join(row))
