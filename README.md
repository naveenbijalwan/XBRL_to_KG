Here’s the updated `README.md` including the usage of Arelle to extract facts:

---

````markdown
# Amazon XBRL to RDF Knowledge Graph

## Tools Used

* Python 3.x
* Arelle CLI (`arelleCmdLine.exe`)
* RDFLib (for RDF creation)
* NetworkX and Matplotlib (for visualization)
* Gremlin Python (for Neptune DB insertion)
* AiohttpTransport for secure WebSocket

## Steps

1. Extract facts using Arelle:
   ```bash
   D:\Arelle\arelleCmdLine.exe --file amzn-20241231_htm.xml --facts amzn_facts.json
````

2. Parsed `amzn_facts.json` to extract XBRL concepts and values.

3. Created nodes for each fact (concept + context) in Amazon Neptune via Gremlin.

4. Parsed XBRL linkbases:

   * `amzn-20241231_cal.xml` (calculationArc)
   * `amzn-20241231_def.xml` (definitionArc)
   * `amzn-20241231_lab.xml` (labelArc)
   * `amzn-20241231_pre.xml` (presentationArc)

5. Established corresponding edges between facts in Neptune using label mappings.

6. Built a **custom temporal linkbase** to connect identical concepts across 2022, 2023, and 2024 using `temporal` edges.

7. Queried the graph using Gremlin for connected facts and temporal sequences.

## Graph Highlights

* 1,372 XBRL fact nodes added.
* Temporal edges created between facts with same concept but different contexts (e.g., 2022 → 2023 → 2024).
* Linkbase edges (`label`, `presentation`, `calculation`, `definition`) connect related concepts (though some may be sparse based on linkbase content).
* Graph visualizations can be generated with:

  ```gremlin
  %%gremlin -d id -g id -de label -l 20
  g.V().hasLabel('Fact').outE().inV().path().by(elementMap()).limit(20)
  ```

## SPARQL Query Example (for GraphDB alternative)

```sparql
SELECT ?year ?value WHERE {
  ?fact ex:concept "Revenue" .
  ?fact ex:year ?year .
  ?fact ex:value ?value .
}
```

## Assumptions

* XBRL data conforms to standard US-GAAP taxonomy.
* Facts are extracted using Arelle with `"factList"` structure.
* ContextRef is used to simulate year-based differentiation.
* Temporal relationships are simulated across years using sorted contextRef entries.