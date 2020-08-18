from collections import namedtuple

from mwtypes import Timestamp

from articlequality.extractors import ptwiki


def test_extractor():

    Revision = namedtuple("Revision", ['id', 'timestamp', 'sha1', 'text'])

    class Page:

        def __init__(self, title, namespace, revisions):
            self.title = title
            self.namespace = namespace
            self.revisions = revisions

        def __iter__(self):
            return iter(self.revisions)

    pages = [
        Page("Page without reverts", 1, [
            Revision(
                1, Timestamp(1), "aaa",
                "{{Brasil/Marca|qualidade=1|importância=3}}\n" +
                "{{Geografia/Marca|qualidade=1|importância=?|rev=20110614}}"
            ),
            Revision(
                2, Timestamp(2), "bbb",
                "{{marca de projeto|rev=20120715|1|Brasil|3}}"
            ),
            Revision(
                3, Timestamp(3), "ccc",
                "{{Classificação/Anfíbios|qualidade=2|importância=1}}"
            ),
            Revision(
                4, Timestamp(4), "ddd",
                "{{Marca de projeto|qualidade=3|Biografias|4|rev=20140917}}"
            ),
            Revision(
                5, Timestamp(5), "eee",
                "{{Marca de projeto|qualidade=3||Biografias|2|rev=20151018}}"
            ),
            Revision(
                6, Timestamp(6), "fff",
                "{{Wikipedia:Projetos/Subdivisões do Brasil/Artigo membro" +
                "|qualidade=5|importância=2}}"
            ),
            Revision(
                7, Timestamp(7), "ggg",
                "{{Marca de projeto|AB}}"
            ),
            Revision(
                8, Timestamp(8), "hhh",
                "{{Marca de projeto|AD|Biografias|4}}"
            )
        ]),
        Page("Page with single revert", 1, [
            Revision(
                1, Timestamp(1), "aaa",
                "{{Marca de projeto|2}}"
            ),
            Revision(
                2, Timestamp(2), "bbb",
                "{{Marca de projeto|3}}"
            ),
            Revision(
                3, Timestamp(3), "ccc",
                "{{Marca de projeto|4}}"
            ),
            Revision(
                4, Timestamp(4), "aaa",
                "{{Marca de projeto|2}}"  # Vandal messing up the template
            ),
            Revision(
                5, Timestamp(5), "ccc",
                "{{Marca de projeto|4}}"  # Patroller reverting vandal
            )
        ]),
        Page("Page with overlaping reverts", 1, [
            Revision(
                1, Timestamp(1), "aaa",
                "{{Marca de projeto|1}}"
            ),
            Revision(
                2, Timestamp(2), "bbb",
                "{{Marca de projeto|2}}"
            ),
            Revision(
                3, Timestamp(3), "ccc",
                "{{Marca de projeto|3}}"
            ),
            Revision(
                4, Timestamp(4), "aaa",
                "{{Marca de projeto|1}}"  # Vandal messing up the template
            ),
            Revision(
                5, Timestamp(5), "ccc",
                "{{Marca de projeto|3}}"  # Rollback
            ),
            Revision(
                6, Timestamp(6), "bbb",
                "{{Marca de projeto|2}}"  # Active editor reevaluates the page
            ),
            Revision(
                7, Timestamp(7), "ddd",
                "{{Marca de projeto|4}}"  # Later on, the page is improved
            )
        ]),
        Page("Page with concentric reverts", 1, [
            Revision(
                1, Timestamp(1), "aaa",
                "{{Marca de projeto|1}}"
            ),
            Revision(
                2, Timestamp(2), "bbb",
                "{{Marca de projeto|2}}"
            ),
            Revision(
                3, Timestamp(3), "ccc",
                "{{Marca de projeto|3}}"
            ),
            Revision(
                4, Timestamp(4), "aaa",
                "{{Marca de projeto|1}}"  # Vandal messing up the template
            ),
            Revision(
                5, Timestamp(5), "ccc",
                "{{Marca de projeto|3}}"  # Rollback
            ),
            Revision(
                6, Timestamp(6), "ddd",
                "{{Marca de projeto|2}}<!-- re-evaluation -->"
            )
        ])
    ]
    expectations = [
        [
            ("marca de projeto", "1", Timestamp(1)),
            ("marca de projeto", "2", Timestamp(3)),
            ("marca de projeto", "3", Timestamp(5)),
            ("marca de projeto", "5", Timestamp(6)),
            ("marca de projeto", "6", Timestamp(8))
        ],
        [
            ("marca de projeto", "2", Timestamp(1)),
            ("marca de projeto", "3", Timestamp(2)),
            ("marca de projeto", "4", Timestamp(3))
        ],
        [
            ("marca de projeto", "1", Timestamp(1)),
            ("marca de projeto", "2", Timestamp(2)),
            ("marca de projeto", "4", Timestamp(7))
        ],
        [
            ("marca de projeto", "1", Timestamp(1)),
            ("marca de projeto", "2", Timestamp(2)),
            ("marca de projeto", "3", Timestamp(3)),
            ("marca de projeto", "2", Timestamp(6))
        ]
    ]
    for page, expected in zip(pages, expectations):
        observations = list(ptwiki.extract(page))
        lab_tuples = [(ob['project'], ob['wp10'], ob['timestamp'])
                      for ob in observations]
        assert lab_tuples == expected
