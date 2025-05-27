import os
from arelle import Cntlr, ModelManager, ModelXbrl
from rdflib import Graph, URIRef, Literal, Namespace
from rdflib.namespace import RDF, XSD

# Define input
XBRL_FILE = "amzn-20241231_htm.xml"

# Setup RDF namespaces
EX = Namespace("http://example.org/xbrl/")
g = Graph()
g.bind("ex", EX)

# Arelle controller
cntlr = Cntlr.Cntlr(logFileName="logToPrint")
model_xbrl = ModelXbrl.load(cntlr, XBRL_FILE)

# Extract and convert to RDF
for fact in model_xbrl.facts:
    fact_uri = URIRef(EX[str(fact.contextID) + "/" + str(fact.qname.localName)])
    g.add((fact_uri, RDF.type, EX.XBRLFact))
    g.add((fact_uri, EX.contextRef, Literal(fact.contextID)))
    g.add((fact_uri, EX.concept, Literal(fact.qname.localName)))
    g.add((fact_uri, EX.value, Literal(fact.value)))
    if fact.unitID:
        g.add((fact_uri, EX.unit, Literal(fact.unitID)))

# Save RDF
g.serialize(destination="output.rdf", format="xml")
