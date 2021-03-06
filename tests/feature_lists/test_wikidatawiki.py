import json
import os

import mwbase
import pytest
from revscoring.dependencies import solve
from revscoring.features import wikibase as wikibase_
from revscoring.features.meta import aggregators

from articlequality.feature_lists import wikidatawiki
from articlequality.feature_lists.wikibase import item

entity = wikibase_.revision.datasources.entity


@pytest.fixture
def q7251():
    dir_name = os.path.dirname(__file__)
    with open(os.path.join(dir_name, 'Q7251.json'), 'r') as f:
        text = f.read()
    return mwbase.Entity.from_json(json.loads(text))


@pytest.fixture
def crab_nebula():
    crab_nebula = {
        'title': 'Q207436',
        'id': 'Q207436',
        'labels': {
            'en': {
                'value': 'Crab Nebula',
                'language': 'en'
            }
        },
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

    return mwbase.Entity.from_json(crab_nebula)


def test_human_related_features(q7251):
    assert solve(wikidatawiki.is_human, cache={entity: q7251}) is True
    assert solve(wikidatawiki.is_blp, cache={entity: q7251}) is False


def test_references_features(q7251):
    assert solve(wikidatawiki.references_count, cache={entity: q7251}) == 97
    assert solve(wikidatawiki.wikimedia_references_count,
                 cache={entity: q7251}) == 23
    assert solve(wikidatawiki.external_references_count,
                 cache={entity: q7251}) == 74


def test_non_external_id_statements_count(q7251):
    assert solve(
        wikidatawiki.non_external_id_statements_count,
        cache={
            entity: q7251}) == 80


def test_external_identifiers(q7251):
    assert solve(aggregators.len(wikidatawiki.external_identifiers),
                 cache={entity: q7251}) == 79


def test_is_astronomical_object(q7251, crab_nebula):
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


def test_has_image(q7251, crab_nebula):
    assert solve(wikidatawiki.has_image,
                 cache={entity: q7251}) is True
    assert solve(wikidatawiki.has_image,
                 cache={entity: crab_nebula}) is False


def test_has_commons_media(q7251, crab_nebula):
    assert solve(wikidatawiki.has_commons_media,
                 cache={entity: q7251}) is True
    assert solve(wikidatawiki.has_commons_media,
                 cache={entity: crab_nebula}) is False


def test_important_languages(q7251, crab_nebula):
    langs_count = len(wikidatawiki.IMPORTANT_LANG_CODES_LIST)
    assert list(
        solve(wikidatawiki.important_label_translation_features,
              cache={entity: q7251})) == [True] * langs_count
    assert list(
        solve(wikidatawiki.important_description_translation_features,
              cache={entity: q7251})) == [True] * langs_count
    assert list(
        solve(wikidatawiki.important_complete_translation_features,
              cache={entity: q7251})) == [True] * langs_count

    expected = [False, False, True, False, False, False, False, False]
    assert list(
        solve(wikidatawiki.important_label_translation_features,
              cache={entity: crab_nebula})) == expected
    assert list(
        solve(wikidatawiki.important_description_translation_features,
              cache={entity: crab_nebula})) == [False] * langs_count
    assert list(
        solve(wikidatawiki.important_complete_translation_features,
              cache={entity: crab_nebula})) == [False] * langs_count


def test_entity_parts(q7251):
    assert solve(wikibase_.revision.claims,
                 cache={entity: q7251}) == 159
    assert solve(wikibase_.revision.properties,
                 cache={entity: q7251}) == 127
    assert solve(wikibase_.revision.aliases,
                 cache={entity: q7251}) == 24
    assert solve(wikibase_.revision.sources,
                 cache={entity: q7251}) == 123
    assert solve(wikibase_.revision.qualifiers,
                 cache={entity: q7251}) == 31
    assert solve(wikibase_.revision.badges,
                 cache={entity: q7251}) == 5
    assert solve(wikibase_.revision.labels,
                 cache={entity: q7251}) == 153
    assert solve(wikibase_.revision.descriptions,
                 cache={entity: q7251}) == 48

    entity_features = list(solve(item, cache={entity: q7251}))
    assert entity_features == [
        5.075173815233827,
        4.852030263919617,
        3.2188758248682006,
        4.820281565605037,
        3.4657359027997265,
        1.791759469228055,
        5.0369526024136295,
        3.8918202981106265]
