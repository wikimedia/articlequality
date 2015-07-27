import re
import sys

from .extractor import TemplateExtractor

TRANSLATIONS = {'maths rating': 'wikiproject mathematics'}

def from_template(template):

    if str(template.name) in TRANSLATIONS:
        template_name = TRANSLATIONS[str(template.name)]
    else:
        template_name = str(template.name)

    if re.match('wikiproject', template_name, re.I) \
       or template.has_param('class'):

        project = normalize_project(template_name)
        try:
            label = str(template.get('class').value).strip().lower()
            return project, label

        except ValueError:
            pass # no assessment class in template


def normalize_project(name):
    name = str(name).replace("_", " ").lower()

    return name.split(" ", 1)[1]

enwiki = TemplateExtractor(from_template, namespaces={1})

sys.modules[__name__] = enwiki
