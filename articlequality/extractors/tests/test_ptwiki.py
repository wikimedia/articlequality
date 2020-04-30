from collections import namedtuple

from mwtypes import Timestamp

from .. import ptwiki


def test_extractor():

    Revision = namedtuple("Revision", ['id', 'timestamp', 'sha1', 'text'])

    class Page:

        def __init__(self, title, namespace, revisions):
            self.title = title
            self.namespace = namespace
            self.revisions = revisions

        def __iter__(self):
            return iter(self.revisions)

    revisions = [
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
    ]
    page = Page("Foobar", 1, revisions)

    observations = ptwiki.extract(page)
    project_labels = {(ob['project'], ob['wp10']): ob
                      for ob in observations}

    expected = [("marca de projeto", "1", Timestamp(1)),
                ("marca de projeto", "2", Timestamp(3)),
                ("marca de projeto", "3", Timestamp(5)),
                ("marca de projeto", "5", Timestamp(6)),
                ("marca de projeto", "6", Timestamp(8))]

    for proj, lab, timestamp in expected:
        ob = project_labels[(proj, lab)]
        assert ob['timestamp'] == timestamp
