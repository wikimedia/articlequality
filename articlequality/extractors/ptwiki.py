import logging

from .extractor import TemplateExtractor

logger = logging.getLogger(__name__)


PROJECT_NAME = "marca de projeto"
POSSIBLE_LABELS = {
    "1": "1",
    "2": "2",
    "3": "3",
    "4": "4",
    "5": "5",
    "6": "6",
    "ab": "5",
    "ad": "6"
}


def from_template(template):
    template_name = normalize_template_name(template.name)
    if template_name == "marca de projeto":
        label = extract_label(template)
        if label is not None:
            yield (PROJECT_NAME, label)


def extract_label(template):
    # Try to get the label from {{{1}}}
    try:
        label = normalize_label(template.get(1).value)
    except ValueError:
        label = None
    if label is None or label == "?":
        # Try to get the label from {{{qualidade}}}
        try:
            label = normalize_label(template.get("qualidade").value)
        except ValueError:
            label = label or None
    # If we failed, log a warning
    if label is None:
        logger.warn("Could not extract label from {0}".format(str(template)))
        return None
    else:
        return label


def normalize_label(label):
    label = label.lower()
    if label in POSSIBLE_LABELS:
        return POSSIBLE_LABELS[label]
    elif label == "?":
        return label
    else:
        return None


def normalize_template_name(template_name):
    return template_name.lower().replace("_", " ")


ptwiki = TemplateExtractor(
    __name__,
    doc="""
articlequality.extractors.ptwiki
++++++++++++++++++++++++++++++++
This extractor looks for instances of the "marca de projeto" template on
article talk pages (namespace = 1) with the first unnamed parameter, or the
"qualidade" parameter, set to <some class>. All `project` s are hard-coded to
"marca de projeto"
""",
    namespaces={1},
    from_template=from_template
)
