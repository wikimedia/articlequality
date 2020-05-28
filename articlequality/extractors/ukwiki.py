import logging
import re

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

LABEL_MAP = {observed_label: normalized_label
             for normalized_label, observed_labels in
             NORMALIZED_LABELS.items()
             for observed_label in observed_labels}

WP_PREFIX = re.compile(r"стаття про[еє]кту|вікіпро[еє]кт|про[еє]кт")


def from_template(template):

    template_name = normalize_template_name(template.name)
    if WP_PREFIX.match(template_name):
        project_name = normalize_project_name(template_name)
        label = get_quality_label(template)
        if label is None:
            logger.warning("Couldn't extract label from {0}".format(template))
        else:
            yield (project_name, label)


def get_quality_label(template):
    if template.has_param("рівень") or template.has_param("class"):
        if template.has_param("рівень"):
            label = template.get_param("рівень")
        else:
            label = template.has_param("class")
        return LABEL_MAP.get(label)
    else:
        return None


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
    namespaces={1},
    from_template=from_template
)
