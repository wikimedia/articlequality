from revscoring.features import wikibase
from revscoring.features.modifiers import log

item = [
    log(wikibase.revision.claims + 1),
    log(wikibase.revision.properties + 1),
    log(wikibase.revision.aliases + 1),
    log(wikibase.revision.sources + 1),
    log(wikibase.revision.qualifiers + 1),
    log(wikibase.revision.badges + 1),
    log(wikibase.revision.labels + 1),
    log(wikibase.revision.sitelinks + 1),
    log(wikibase.revision.descriptions + 1)
]
