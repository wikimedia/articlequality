from revscoring import Feature
from revscoring.datasources import \
    revision_oriented as revision_oriented_datasources
from revscoring.datasources.datasource import Datasource
from revscoring.features import wikibase as wikibase_
from revscoring.features import modifiers
from revscoring.features.meta import aggregators
from revscoring.features.modifiers import not_

from . import wikibase, wikimedia

name = "wikidatawiki"

IMPORTANT_LANG_CODES = {'en', 'de', 'ar', 'zh', 'es', 'pt', 'ru', 'fr'}
"""
Language codes for important languages which are described in
https://www.wikidata.org/wiki/Wikidata:Item_quality#Translations
"""


class properties:
    """
    Mapping of english descriptions to property identifiers
    """
    INSTANCE_OF = 'P31'
    DATE_OF_BIRTH = 'P569'
    DATE_OF_DEATH = 'P570'


class items:
    """
    Mapping of english descriptions to item idenifiers
    """
    HUMAN = 'Q5'


def _process_references(entity):
    return [reference
            for pid, statements in entity.properties.items()
            for statement in statements
            for pid, references in statement.references.items()
            for reference in references]


references = Datasource(
    name + ".revision.references",
    _process_references,
    depends_on=[wikibase_.revision.datasources.entity])


def _process_wikimedia_references(references):
    return [reference
            for reference in references
            if (reference.datatype == 'wikibase-entityid' and
                reference.datavalue.id in wikimedia.PROJECT_QIDS)]


wikimedia_references = Datasource(
    name + ".revision.wikimedia_references",
    _process_wikimedia_references, depends_on=[references])


def _process_unique_references(references):
    return {(reference.property, str(reference.datavalue))
            for reference in references}


unique_references = Datasource(
    name + ".revision.unique_references",
    _process_unique_references, depends_on=[references])


def _process_complete_translations(item_labels, item_descriptions):
    return (item_labels.keys() & item_descriptions.keys())


complete_translations = Datasource(
    name + ".revision.complete_translations",
    _process_complete_translations,
    depends_on=[wikibase_.revision.datasources.labels,
                wikibase_.revision.datasources.descriptions],)


def _process_important_complete_translations(complete_translations):
    return (complete_translations & IMPORTANT_LANG_CODES)


important_complete_translations = Datasource(
    name + ".revision.important_complete_translations",
    _process_important_complete_translations,
    depends_on=[complete_translations])


def _process_important_label_translations(item_labels):
    return (item_labels.keys() & IMPORTANT_LANG_CODES)


important_label_translations = Datasource(
    name + ".revision.important_label_translations",
    _process_important_label_translations,
    depends_on=[wikibase_.revision.datasources.labels])


def _process_important_description_translations(item_descriptions):
    return (item_descriptions.keys() & IMPORTANT_LANG_CODES)


important_description_translations = Datasource(
    name + ".revision.important_description_translations",
    _process_important_description_translations,
    depends_on=[wikibase_.revision.datasources.descriptions])


references_count = aggregators.len(references)
"`int` : A count of all sources in the revision"

wikimedia_references_count = aggregators.len(wikimedia_references)
"`int` : A count of all sources which come from Wikimedia projects"

external_references_count = references_count - wikimedia_references_count
"`int` : A count of all sources which do not come from Wikimedia projects"

unique_references_count = aggregators.len(unique_references)
"`int` : A count of unique sources in the revision"


def _process_item_completeness(current_properties, properties_suggested):
    current_properties = set(current_properties.keys())

    all_prob = 0.0
    present_prob = 0.0
    for statement in properties_suggested:
        all_prob += float(statement['rating'])
        if statement['id'] in current_properties:
            present_prob += float(statement['rating'])

    return present_prob / all_prob if all_prob else 0.0


item_completeness = Feature(
    name + '.revision.page.item_completeness',
    _process_item_completeness,
    returns=float,
    depends_on=[
        wikibase_.revision.datasources.properties,
        revision_oriented_datasources.revision.page.suggested.properties])

# Status
is_human = wikibase_.revision.has_property_value(
    properties.INSTANCE_OF, items.HUMAN, name=name + '.revision.is_human')
has_birthday = wikibase_.revision.has_property(
    properties.DATE_OF_BIRTH, name=name + '.revision.has_birthday')
dead = wikibase_.revision.has_property(
    properties.DATE_OF_DEATH, name=name + '.revision.dead')
is_blp = has_birthday.and_(not_(dead))


local_wiki = [
    is_human,
    is_blp,
    aggregators.len(complete_translations),
    aggregators.len(important_label_translations),
    aggregators.len(important_description_translations),
    aggregators.len(important_complete_translations),
    references_count,
    wikimedia_references_count,
    wikimedia_references_count / modifiers.max(references_count, 1),
    external_references_count,
    external_references_count / modifiers.max(references_count, 1),
    unique_references_count,
    unique_references_count / modifiers.max(references_count, 1),
    item_completeness
]

item_quality = wikibase.item + local_wiki
