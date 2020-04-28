import logging
import re

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
TEMPLATE_ARGS = [
    (re.compile(r"marca de projeto"), [1, "qualidade"]),
    (re.compile(r"/marca$"), ["qualidade"]),
    (re.compile(r"^classificação/"), ["qualidade"]),
    (re.compile(r"tmbox/classificação"), ["qualidade"]),
    (re.compile(r"álbuns"), ["qualidade"]),
    (re.compile(r"projetos/subdivisões do brasil/artigo membro"),
        ["qualidade"]),
    (re.compile(r"wikiprojecto escolares e universitários"), ["qualidade"]),
    (re.compile(r"marca-música portuguesa"), ["qualidade"]),
    (re.compile(r"brojetobd"), ["qualidade"]),
    (re.compile(r"canções"), ["qualidade"])
]


def from_template(template):
    template_name = normalize_template_name(template.name)

    for regex, args in TEMPLATE_ARGS:
        if regex.search(template_name):
            label = extract_label(template, args)
            if label is not None:
                yield (PROJECT_NAME, label)
            break


def extract_label(template, args):
    ignored_labels = ["?", "qualidade"]
    # Get the label from the first specified parameter which is available
    for arg in args:
        # Disregard missing/empty arguments
        if template.has(arg, True):
            label = template.get(arg).value
            normalized_label = normalize_label(label)
            if normalized_label is None and label not in ignored_labels:
                logger.warning(
                    "Could not extract label from {0}".format(str(template)))
                return None
            else:
                return normalized_label


def normalize_label(label):
    label = label.lower()
    if label in POSSIBLE_LABELS:
        return POSSIBLE_LABELS[label]
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
