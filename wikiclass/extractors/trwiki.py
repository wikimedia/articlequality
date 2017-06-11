import logging
import re
import sys
import traceback

import mwparserfromhell as mwp

from .extractor import TemplateExtractor

logger = logging.getLogger(__name__)

PROJECT_NAME = "vikiproje"


def from_template(template):
    template_name = str(template.name).lower().strip()
    if template_name == "vikiproje" and template.has_param('Sınıf'):
        try:
            label = normalize_label(template.get('Sınıf').value)
            project_name = None
            if 'Proje' in template:
                project_name = template.get('Proje').value.strip().lower()
            project_name = project_name or PROJECT_NAME

            if label is not None:
                return project_name, label
            else:
                logger.debug("Class '{0}' not in possible classes."
                             .format(template.get('Sınıf').value))
                pass # not a quality assessment class

        except ValueError as e:
            logger.warning(traceback.format_exc())
            pass # no assessment class in template




LABEL_MATCHES = [
    ("sm", re.compile(r"\bsm\b", re.I)), # featured article 
    ("km", re.compile(r"\bkm\b", re.I)), # good article
    ("b", re.compile(r"\bb\b", re.I)), # B class
    ("c", re.compile(r"\bc\b", re.I)), # C class
    ("baslağıç", re.compile(r"\bbaşlanğıç\b", re.I)), # start class
    ("taslak", re.compile(r"\btaslak\b", re.I)) # stub class
]
def normalize_label(value):
    value = str(value.strip_code()).lower().replace("_", " ").strip()
    
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
hard-coded to "VikiProje"
""",
    namespaces={1},
    from_template=from_template)
