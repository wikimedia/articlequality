from revscoring.features import Feature, modifiers

from ..datasources import tags
from .templates import cite_templates


def ref_tags_process(tags):
    return sum(1 for tag in tags if tag.tag == "ref")

ref_tags = Feature("ref_tags", ref_tags_process, returns=int, depends_on=[tags])


proportion_of_templated_references = cite_templates / modifiers.max(ref_tags, 1)
