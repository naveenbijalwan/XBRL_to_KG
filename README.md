# Amazon XBRL to RDF Knowledge Graph

## Tools Used
- Arelle (XBRL parser)
- RDFLib (Python RDF handling)
- GraphDB (for RDF visualization and SPARQL)
- Python 3.x

## Steps
1. Parsed `amzn-20241231_htm.xml` with Arelle.
2. Extracted XBRL facts (concept, context, unit, value).
3. Converted facts to RDF using RDFLib.
4. Output written to `output.rdf`.
5. Loaded into GraphDB for SPARQL queries and visualization.
6. Created temporal linkbase to connect 2022–2024 Revenue etc.

## SPARQL Query Example
```sparql
SELECT ?year ?value WHERE {
  ?fact ex:concept "Revenues" .
  ?fact ex:contextRef ?year .
  ?fact ex:value ?value .
}
