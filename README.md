# Functional Text Mining

Apply functional programming to text mining. The bash scripts are included to demonstrate the PMC ([PubMed Central](https://www.ncbi.nlm.nih.gov/pmc/)) API.

**File Structure:**

```
code/
  |_ pmc_ids.sh      # given a search term, return article IDs
  |_ pmc_xml.sh      # given IDs, return the fulltext in XML
  |_ pmc_pdf.sh      # given IDs, return pdf articles
  
data/                
  |_ neo4j.ids       # example article IDs
  |_ neo4j.xml       # .. article fulltext
  |_ PMC6239324.pdf  # .. pdf
  
```

**Example Behavior:**

```
bash pmc_ids.sh neo4j > neo4j.ids
bash pmc_xml.sh neo4j.ids > neo4j.xml
bash pmc_pdf.sh neo4j.ids     # pdfs save in local directory
```

**Possible exploration routes**

* reimplement using a functional language
* xml to tsv converter (title, authors, publication date, journal)
* compare programming languages used in academic papers (search different languages), compare their use-cases.

Feel free to explore.
