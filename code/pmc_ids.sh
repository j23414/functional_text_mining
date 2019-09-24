#! /usr/bin/env bash
# Auth: Jennifer Chang
# Date: 2018/05/21

# ==== Variables
TERM=$1

RETMAX=100000      # Hacky way of getting more results

# ==== Fetch Publication IDs
curl -g "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pmc&term=${TERM}&retmax=${RETMAX}&usehistory=y&sort=pub+date" |\
    grep "<Id>" |\
    sed 's/<Id>//g; s/<\/Id>//g' |\
    tr '\t' ' ' |\
    sed 's/ //g'
