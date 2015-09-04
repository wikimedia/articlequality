import logging
import re
import sys
import traceback

from .extractor import TemplateExtractor

logger = logging.getLogger(__name__)

POSSIBLE_LABELS = ("stub", "start", "c", "b", "a", "ga", "fa")
def from_template(template):

    if template.has_param('class'):
        template_name = normalize_template_name(template.name)
        project_name = normalize_project_name(template_name)
        try:
            label = str(template.get('class').value).strip().lower()
            if label in POSSIBLE_LABELS:
                return project_name, label
            else:
                logger.debug("Class '{0}' not in possible classes."
                             .format(label))
                pass # not a quality assessment class

        except ValueError as e:
            logger.warning(traceback.format_exc())
            pass # no assessment class in template


TRANSLATIONS = {'maths rating': 'wikiproject mathematics'}
def normalize_template_name(template_name):
    template_name = str(template_name).lower().replace("_", " ")
    if str(template_name) in TRANSLATIONS:
        return TRANSLATIONS[template_name]
    else:
        return template_name

WP_PREFIX = re.compile("^(wp|wikiproject) ?", re.I)
def normalize_project_name(template_name):
    return WP_PREFIX.sub('', template_name.lower().replace("_", " ")).strip()

sys.modules[__name__] = TemplateExtractor(
    __name__,
    doc="""
wikiclass.extractors.enwiki
+++++++++++++++++++++++++++

This extractor looks for instances of templates that contain
"class=<some class>" on article talk pages (namespace = 1) and parses the
template name to obtain a `project`.
""",
    namespaces={1},
    from_template=from_template
)
