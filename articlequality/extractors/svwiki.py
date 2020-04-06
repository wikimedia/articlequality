import logging
import re

from .extractor import TemplateExtractor

logger = logging.getLogger(__name__)

PROJECT_NAME = "wikiproject"
TEMPLATE_MATCHES = [
    ("u", re.compile(r"Utmärkt", re.I)),        # featured article
    ("b", re.compile(r"Bra", re.I)),            # good article
    ("r", re.compile(r"Rekommenderad", re.I)),  # B class
    ("s", re.compile(r"stub", re.I)),           # stub
]


def filter_text(text):
    return re.search(r'(utmärkt|bra|rekommenderad|stub)', text, re.I)


def from_template(template):
    template_name = str(template.name).lower().strip()

    for label, regex in TEMPLATE_MATCHES:
        if regex.match(template_name):
            yield (PROJECT_NAME, label)


svwiki = TemplateExtractor(
    __name__,
    doc="""
articlequality.extractors.svwiki
++++++++++++++++++++++++++++++++

This extractor looks for instances of templates on article pages
(namespace =0 ) with names "Utmärkt", "Bra", "Rekommenderad",
or containing "stub". All `project` s are hard-coded to "wikiproject"
""",
    namespaces={0},
    from_template=from_template,
    filter_text=filter_text)
