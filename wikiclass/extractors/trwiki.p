import logging
import re
import sys
import traceback

import mwparserfromhell as mwp

from .extractor import TemplateExtractor

logger = logging.getLogger(__name__)

PROJECT_NAME = "VikiProje"


def from_template(template):
    template_name = str(template.name).lower().strip()
    if template_name == "VikiProje" and template.has_param('Sınıf'):
        try:
            label = normalize_label(template.get('Sınıf').value)

            if label is not None:
                return PROJECT_NAME, label
            else:
                logger.debug("Class '{0}' not in possible classes."
                             .format(template.get('Sınıf').value))
                pass # not a quality assessment class

        except ValueError as e:
            logger.warning(traceback.format_exc())
            pass # no assessment class in template




LABEL_MATCHES = [
    ("sm", re.compile(r"\bsm|sl\b", re.I)), #featured article or list
    ("a", re.compile(r"\ba\b", re.I)),
    ("km", re.compile(r"\bkm\b", re.I)),
    ("b", re.compile(r"\bb\b", re.I)),
    ("c", re.compile(r"\bc\b", re.I)),
    ("baslağıç", re.compile(r"\bbaşlanğıç\b", re.I))
    ("taslak", re.compile(r"\btaslak\b", re.I)) #stub
]
def normalize_label(value):
    value = str(value).lower().replace("_", " ").strip()
    if re.search(r'<!--', value): # HTML comment in param value?
        value = mwp.parse(value)
        value.remove(value.filter_comments())
        value = str(value).strip()
    
    for label, regex in LABEL_MATCHES:
        if regex.match(value):
            return label

    return None

sys.modules[__name__] = TemplateExtractor(
    __name__,
    doc="""
wikiclass.extractors.trwiki
+++++++++++++++++++++++++++

This extractor looks for instances of the "VikiProje" template on article talk
pages (namespace = 1) with a parameter called "Sınıf".  All `project` s are
hard-coded to "wikiprojet"
""",
    namespaces={1},
    from_template=from_template)
