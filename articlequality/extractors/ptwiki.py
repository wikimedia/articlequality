import logging
import re

from .extractor import TemplateExtractor

logger = logging.getLogger(__name__)


def from_template(template):
    project_name = normalize_project_name(template.name)
    if project_name == "marca de projeto":
        labels = extract_labels(template)
        if len(labels) >= 1:
            for project, label in labels[1:]:
                yield (normalize_project_name(project), label)


PROJECT_LABEL = re.compile(r"([^\|\{\{\}\}]+)\|([0-5\*])", re.I)


def extract_labels(template):
    return [(label.group(1), label.group(2))
            for label in re.finditer(PROJECT_LABEL, str(template))]


def normalize_project_name(template_name):
    return template_name.lower().replace("_", " ")


ptwiki = TemplateExtractor(
    __name__,
    doc="""
articlequality.extractors.ptwiki
++++++++++++++++++++++++++++++++
This extractor looks for instances of templates that contain
"class=<some class>" on article talk pages (namespace = 1) and parses the
template name to obtain a `project`.
""",
    namespaces={1},
    from_template=from_template
)
