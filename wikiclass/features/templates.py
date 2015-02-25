import re

from revscoring.features import Feature

from ..datasources import templates

CITE_RE = re.compile(r"cite", re.I|re.U)
INFOBOX_RE = re.compile(r"infobox|sidebar", re.I|re.U)

def cite_templates_process(templates):
    return sum(1 for t in templates if CITE_RE.search(str(t.name)))

cite_templates = Feature("cite_templates", cite_templates_process,
                         returns=int, depends_on=[templates])

def infobox_templates_process(templates):
    return sum(1 for t in templates if INFOBOX_RE.search(str(t.name)))

infobox_templates = Feature("infobox_templates", infobox_templates_process,
                            returns=int, depends_on=[templates])
