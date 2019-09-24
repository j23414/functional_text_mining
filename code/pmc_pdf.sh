#! /usr/bin/env bash
# Auth: Jennifer Chang
# Date: 2019/09/22

set -e
set -u

while read pmcid
do
    echo "PMC${pmcid}"
    curl --location "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC${pmcid}/pdf" > PMC${pmcid}.pdf
    sleep 0.5
done < $1

