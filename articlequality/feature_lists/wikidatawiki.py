from revscoring import Feature
from revscoring.datasources.datasource import Datasource
from revscoring.features import wikibase as wikibase_
from revscoring.features import modifiers
from revscoring.features.meta import aggregators, bools
from revscoring.features.modifiers import not_

from . import wikibase
from .wikidatawiki_data import property_datatypes, items_lists

name = "wikidatawiki"

IMPORTANT_LANG_CODES = {'en', 'de', 'ar', 'zh', 'es', 'pt', 'ru', 'fr'}
IMPORTANT_LANG_CODES_LIST = sorted(list(IMPORTANT_LANG_CODES))
"""
Language codes for important languages which are described in
https://www.wikidata.org/wiki/Wikidata:Item_quality#Translations
"""


class properties:
    """
    Mapping of english descriptions to property identifiers
    """
    IMAGE = 'P18'
    INSTANCE_OF = 'P31'
    DATE_OF_BIRTH = 'P569'
    DATE_OF_DEATH = 'P570'
    IMPORTED_FROM_WIKIMEDIA = 'P143'


class items:
    """
    Mapping of english descriptions to item idenifiers
    """
    HUMAN = 'Q5'
    SCHOLARLY_ARTICLE = 'Q13442814'


def _filter_nonexternal_identifier_statements(entity):
    return [
        statement
        for pid, statements in entity.properties.items()
        if pid in property_datatypes.NONEXTERNAL_IDENTIFIERS
        for statement in statements]


def _process_references(entity):
    nonexternal_identifier_statements = \
        _filter_nonexternal_identifier_statements(entity)
    return [reference
            for statement in nonexternal_identifier_statements
            for pid, references in statement.references.items()
            for reference in references]


references = Datasource(
    name + ".revision.references",
    _process_references,
    depends_on=[wikibase_.revision.datasources.entity])


def _process_external_identifiers(entity):
    return [statement
            for pid, statements in entity.properties.items()
            if pid not in property_datatypes.NONEXTERNAL_IDENTIFIERS
            for statement in statements]


external_identifiers = Datasource(
    name + ".revision.external_identifiers",
    _process_external_identifiers,
    depends_on=[wikibase_.revision.datasources.entity])


def _process_commons_media(entity):
    for pid in entity.properties.keys():
        if pid in property_datatypes.COMMONS_MEDIA:
            return True
    return False


has_commons_media = Feature(
    name + ".revision.has_commons_media",
    _process_commons_media,
    returns=bool,
    depends_on=[wikibase_.revision.datasources.entity])


def _process_wikimedia_references(references):
    return [reference
            for reference in references
            if (reference.property == properties.IMPORTED_FROM_WIKIMEDIA)]


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


def _process_non_external_id_statements(entity):
    return [statement
            for pid, statements in entity.properties.items()
            if pid in property_datatypes.NONEXTERNAL_IDENTIFIERS
            for statement in statements]


non_external_id_statements = Datasource(
    name + ".revision.non_external_id_statements",
    _process_non_external_id_statements,
    depends_on=[wikibase_.revision.datasources.entity])


references_count = aggregators.len(references)
"`int` : A count of all sources in the revision"

wikimedia_references_count = aggregators.len(wikimedia_references)
"`int` : A count of all sources which come from Wikimedia projects"

external_references_count = references_count - wikimedia_references_count
"`int` : A count of all sources which do not come from Wikimedia projects"

unique_references_count = aggregators.len(unique_references)
"`int` : A count of unique sources in the revision"

non_external_id_statements_count = aggregators.len(non_external_id_statements)
"`int` : A count of all statements that are not external identifiers"


def _process_is_astronomical_object(entity):
    statements = entity.properties.get(properties.INSTANCE_OF, [])
    for s in statements:
        if str(s.claim.datavalue) in items_lists.ASTRONOMICAL_OBJECTS:
            return True
    return False


def _process_referenced_claims_ratio(entity):
    statements = _filter_nonexternal_identifier_statements(entity)

    referenced_statements = [
        statement
        for statement in statements
        if statement.references]
    return len(referenced_statements) / max([len(statements), 1])


def _process_wikimedia_referenced_ratio(entity):
    statements = _filter_nonexternal_identifier_statements(entity)

    wikimedia_referenced_statements = 0
    for statement in statements:
        wikimedia_referenced = False
        for ref_pid in statement.references:
            if ref_pid == properties.IMPORTED_FROM_WIKIMEDIA:
                wikimedia_referenced = True
                break
        if wikimedia_referenced:
            wikimedia_referenced_statements += 1

    return wikimedia_referenced_statements / max([len(statements), 1])


def _process_externally_referenced_claims_ratio(entity):
    statements = _filter_nonexternal_identifier_statements(entity)

    externally_referenced_statements = 0
    for statement in statements:
        externally_referenced = False
        for ref_pid in statement.references:
            if ref_pid != properties.IMPORTED_FROM_WIKIMEDIA:
                externally_referenced = True
                break
        if externally_referenced:
            externally_referenced_statements += 1

    return externally_referenced_statements / max([len(statements), 1])


# Status
is_human = wikibase_.revision.has_property_value(
    properties.INSTANCE_OF, items.HUMAN, name=name + '.revision.is_human')
has_birthday = wikibase_.revision.has_property(
    properties.DATE_OF_BIRTH, name=name + '.revision.has_birthday')
dead = wikibase_.revision.has_property(
    properties.DATE_OF_DEATH, name=name + '.revision.dead')
is_blp = has_birthday.and_(not_(dead))

is_scholarlyarticle = wikibase_.revision.has_property_value(
    properties.INSTANCE_OF,
    items.SCHOLARLY_ARTICLE,
    name=name + '.revision.is_scholarlyarticle'
)
is_astronomical_object = Feature(
    name + '.revision.page.is_astronomical_object',
    _process_is_astronomical_object,
    returns=bool,
    depends_on=[wikibase_.revision.datasources.entity])
has_image = wikibase_.revision.has_property(
    properties.IMAGE, name=name + '.revision.has_image')

referenced_claims_ratio = Feature(
    name + '.revision.page.referenced_claims_ratio',
    _process_referenced_claims_ratio,
    returns=float,
    depends_on=[wikibase_.revision.datasources.entity])

wikimedia_referenced_ratio = Feature(
    name + '.revision.page.wikimedia_referenced_ratio',
    _process_wikimedia_referenced_ratio,
    returns=float,
    depends_on=[wikibase_.revision.datasources.entity])

externally_referenced_claims_ratio = Feature(
    name + '.revision.page.externally_referenced_claims_ratio',
    _process_externally_referenced_claims_ratio,
    returns=float,
    depends_on=[wikibase_.revision.datasources.entity])

important_label_translation_features = [
    bools.item_in_set(i, important_label_translations)
    for i in IMPORTANT_LANG_CODES_LIST
]
important_description_translation_features = [
    bools.item_in_set(i, important_description_translations)
    for i in IMPORTANT_LANG_CODES_LIST
]
important_complete_translation_features = [
    bools.item_in_set(i, important_complete_translations)
    for i in IMPORTANT_LANG_CODES_LIST
]

local_wiki = \
    important_label_translation_features + \
    important_description_translation_features + \
    important_complete_translation_features + \
    [
        is_scholarlyarticle,
        is_astronomical_object,
        is_human,
        is_blp,
        has_image,
        has_commons_media,
        aggregators.len(complete_translations),
        aggregators.len(important_label_translations),
        aggregators.len(important_description_translations),
        aggregators.len(important_complete_translations),
        references_count,
        referenced_claims_ratio,
        wikimedia_references_count,
        wikimedia_references_count / modifiers.max(references_count, 1),
        wikimedia_referenced_ratio,
        external_references_count,
        external_references_count / modifiers.max(references_count, 1),
        externally_referenced_claims_ratio,
        unique_references_count,
        unique_references_count / modifiers.max(references_count, 1),
        aggregators.len(external_identifiers),
        non_external_id_statements_count
    ]

item_quality = wikibase.item + local_wiki
