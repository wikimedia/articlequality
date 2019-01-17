from revscoring.datasources import \
    revision_oriented as revision_oriented_datasources
from revscoring.features import wikibase as wikibase_
from revscoring.dependencies import solve

from .. import wikidatawiki

present_properties = wikibase_.revision.datasources.properties
suggested_properties = \
    revision_oriented_datasources.revision.page.suggested.properties


def test_item_completeness_empty():
    cache = {present_properties: {}, suggested_properties: {}}

    assert solve(wikidatawiki.item_completeness, cache=cache) == 0.0


def test_item_completeness():
    present = {'P123': {}, 'P234': {}}
    suggested = [{'id': 'P123', 'rating': 0.8}, {'id': 'P404', 'rating': 0.6}]

    cache = {present_properties: present, suggested_properties: suggested}
    expected = 0.8 / (0.8 + 0.6)

    assert solve(wikidatawiki.item_completeness, cache=cache) == expected
