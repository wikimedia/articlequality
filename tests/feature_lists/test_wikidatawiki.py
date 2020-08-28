import json
import os

import mwbase
import pytest
from revscoring.datasources import \
    revision_oriented as revision_oriented_datasources
from revscoring.dependencies import solve
from revscoring.features import wikibase as wikibase_
from revscoring.features.meta import aggregators

from articlequality.feature_lists import wikidatawiki

present_properties = wikibase_.revision.datasources.properties
suggested_properties = \
    revision_oriented_datasources.revision.page.suggested.properties
entity = wikibase_.revision.datasources.entity


@pytest.fixture
def q7251():
    dir_name = os.path.dirname(__file__)
    with open(os.path.join(dir_name, 'Q7251.json'), 'r') as f:
        text = f.read()
    return mwbase.Entity.from_json(json.loads(text))


def test_item_completeness_empty():
    cache = {present_properties: {}, suggested_properties: {}}

    assert solve(wikidatawiki.item_completeness, cache=cache) == 0.0


def test_item_completeness():
    present = {'P123': {}, 'P234': {}}
    suggested = [{'id': 'P123', 'rating': 0.8}, {'id': 'P404', 'rating': 0.6}]

    cache = {present_properties: present, suggested_properties: suggested}
    expected = 0.8 / (0.8 + 0.6)

    assert solve(wikidatawiki.item_completeness, cache=cache) == expected


def test_human_related_features(q7251):
    assert solve(wikidatawiki.is_human, cache={entity: q7251}) is True
    assert solve(wikidatawiki.is_blp, cache={entity: q7251}) is False


def test_references_features(q7251):
    assert solve(wikidatawiki.references_count, cache={entity: q7251}) == 97
    assert solve(wikidatawiki.wikimedia_references_count,
                 cache={entity: q7251}) == 23
    assert solve(wikidatawiki.external_references_count,
                 cache={entity: q7251}) == 74


def test_external_identifiers(q7251):
    assert solve(aggregators.len(wikidatawiki.external_identifiers),
                 cache={entity: q7251}) == 79


def test_is_astronomical_object(q7251):
    crab_nebula = {
        'title': 'Q207436',
        'id': 'Q207436',
        'claims': {
            'P31': [
                {
                    'mainsnak': {
                        'snaktype': 'value',
                        'property': 'P31',
                        'datavalue': {
                            'value': {
                                'entity-type': 'item',
                                'numeric-id': 1931185,
                                'id': 'Q1931185'
                            },
                            'type': 'wikibase-entityid'
                        },
                        'datatype': 'wikibase-item'
                    },
                    'type': 'statement',
                    'id': 'Q10934$46D9E951-DD5A-4832-A2D2-DB0CE0425E0E',
                    'rank': 'normal'
                }
            ]
        }
    }

    crab_nebula = mwbase.Entity.from_json(crab_nebula)

    assert solve(wikidatawiki.is_astronomical_object,
                 cache={entity: crab_nebula}) is True
    assert solve(wikidatawiki.is_astronomical_object,
                 cache={entity: q7251}) is False


def test_references_ratio_features(q7251):
    assert solve(wikidatawiki.referenced_claims_ratio,
                 cache={entity: q7251}) == 0.6
    assert solve(wikidatawiki.wikimedia_referenced_ratio,
                 cache={entity: q7251}) == 0.2875
    assert solve(wikidatawiki.externally_referenced_claims_ratio,
                 cache={entity: q7251}) == 0.425
