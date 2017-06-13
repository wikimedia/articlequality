from revscoring.features import wikibase as wikibase_features
from revscoring.features.modifiers import not_
from wikiclass.wikiclass.feature_lists import wikidata
from . import wikibase 

name = "wikidatawiki"


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


# Status
revision = wikibase_features.revision
is_human = revision.has_property_value(properties.INSTANCE_OF, items.HUMAN,
                                       name=name + '.is_human')
has_birthday = revision.has_property(properties.DATE_OF_BIRTH,
                                     name='revision.has_birthday')
dead = revision.has_property(properties.DATE_OF_DEATH,
                             name='revision.dead')
is_blp = has_birthday.and_(not_(dead))


local_wiki = [
    is_human,
    is_blp,
	wikidata.revision.external_sources_ratio,
	wikidata.revision.unique_sources,
	wikidata.revision.complete_translations,
	wikidata.revision.complete_important_translations,
	wikidata.revision.all_sources,
	wikidata.revision.all_wikimedia_sources,
	wikidata.revision.all_external_sources
]

item_quality = wikibase.item + local_wiki

