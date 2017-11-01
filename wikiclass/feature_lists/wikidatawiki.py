import pywikibase
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


def _process_source_claims(item):
    return [source_claim
            for pid, claims in item.claims.items()
            for claim in claims
            for source in claim.sources
            for source_pid, source_claims in source.items()
            for source_claim in source_claims]


source_claims = Datasource(
    name + ".revision.source_claims",
    _process_source_claims,
    depends_on=[wikibase_.revision.datasources.item])


def _process_wikimedia_sources(source_claims):
    return [source_claim
            for source_claim in source_claims
            if isinstance(source_claim.target, pywikibase.ItemPage) and
            source_claim.target.id in wikimedia.PROJECT_QIDS]


wikimedia_sources = Datasource(
    name + ".revision.wikimedia_sources",
    _process_wikimedia_sources, depends_on=[source_claims])


def _process_unique_sources(source_claims):
    return {(source_claim.id, simplify_target(source_claim.target))
            for source_claim in source_claims}


unique_sources = Datasource(
    name + ".revision.unique_sources",
    _process_unique_sources, depends_on=[source_claims])


def simplify_target(target):
    if hasattr(target, "id"):
        return target.id
    elif hasattr(target, "lstrip"):
        return target
    elif hasattr(target, "toTimestr"):
        return target.toTimestr()
    elif isinstance(target, dict) and 'text' in target:
        return target['text']
    elif target is None:
        return None
    else:
        raise RuntimeError("Could not simplify target {0}"
                           .format(target))


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


source_claims_count = aggregators.len(source_claims)
"`int` : A count of all sources in the revision"

wikimedia_sources_count = aggregators.len(wikimedia_sources)
"`int` : A count of all sources which come from Wikimedia projects"

external_sources_count = source_claims_count - wikimedia_sources_count
"`int` : A count of all sources which do not come from Wikimedia projects"

unique_sources_count = aggregators.len(unique_sources)
"`int` : A count of unique sources in the revision"

# Status
is_human = wikibase_.revision.has_property_value(
    properties.INSTANCE_OF, items.HUMAN, name=name + '.is_human')
has_birthday = wikibase_.revision.has_property(
    properties.DATE_OF_BIRTH, name='revision.has_birthday')
dead = wikibase_.revision.has_property(
    properties.DATE_OF_DEATH, name='revision.dead')
is_blp = has_birthday.and_(not_(dead))

local_wiki = [
    is_human,
    is_blp,
    aggregators.len(complete_translations),
    aggregators.len(important_label_translations),
    aggregators.len(important_description_translations),
    aggregators.len(important_complete_translations),
    source_claims_count,
    wikimedia_sources_count,
    wikimedia_sources_count / modifiers.max(source_claims_count, 1),
    external_sources_count,
    external_sources_count / modifiers.max(source_claims_count, 1),
    unique_sources_count,
    unique_sources_count / modifiers.max(source_claims_count, 1)
]

item_quality = wikibase.item + local_wiki
