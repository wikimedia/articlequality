import logging
import re
import traceback

from .extractor import TemplateExtractor

logger = logging.getLogger(__name__)

NORMALIZED_LABELS = {
        "ВС": ["ВС", "вс", "Вибрана стаття", "вибрана стаття"],
        "ДС": ["ДС", "дс", "Добра стаття", "добра стаття"],
        "I": ["I", "1"],
        "II": ["II", "2"],
        "III": ["III", "3"],
        "IV": ["IV", "4", "Stub", "stub"]
}


def from_template(template):

    if template.has_param('class') or template.has_param('рівень'):
        template_name = normalize_template_name(template.name)
        project_name = normalize_project_name(template_name)
        try:
            label = get_quality(template)

            if label in POSSIBLE_LABELS:
                yield (project_name, label)
            else:
                logger.debug("Class {0} not in possible classes."
                              .format(label))
                pass  # not a quality assessment class

        except ValueError as e:
            logger.warning(traceback.format_exc())
            pass  # no assessment class in template


def get_quality(template):
    LABEL_MAP = {observed_label: normalized_label
             for normalized_label, observed_labels in 
             NORMALIZED_LABELS.items()
             for observed_label in observed_labels}

def normalize_template_name(template_name):
    template_name = str(template_name).lower().replace("_", " ")


def normalize_project_name(template_name):
    return WP_PREFIX.sub('', template_name.lower().replace("_", " ")).strip()


ukwiki = TemplateExtractor(
    __name__,
    doc="""
articlequality.extractors.ukwiki
++++++++++++++++++++++++++++++++
This extractor looks for instances of the template on
article talk pages (namespace = 1) with the first unname parameter
""",
    namespaces={1}
    from_template=from_template
)
