from collections import namedtuple

from mwtypes import Timestamp

from .. import frwiki


def test_extractor():

    User = namedtuple("User", ['id', 'text'])
    Revision = namedtuple("Revisions", ['id', 'timestamp', 'sha1', 'user',
                                        'text'])

    class Page:

        def __init__(self, title, namespace, revisions):
            self.title = title
            self.namespace = namespace
            self.revisions = revisions

        def __iter__(self):
            return iter(self.revisions)

    alice = User(1, 'Alice')
    bob = User(2, 'Bob')

    revisions = [
        Revision(
            1, Timestamp(0), "aaa", alice,
            "{{Wikiprojet\n" +
            "|Seconde Guerre mondiale|maximum\n" +
            "|Japon|maximum\n" +
            "|Forces armées des États-Unis|maximum\n" +
            "|Nucléaire|maximum\n" +
            "|avancement=e}}"
        ),
        Revision(
            2, Timestamp(1), "bbb", bob,
            "{{talk page}}" +
            "{{Wikiprojet\n" +
            "|Seconde Guerre mondiale|maximum\n" +
            "|Japon|maximum\n" +
            "|Forces armées des États-Unis|maximum\n" +
            "|Nucléaire|maximum\n" +
            "|avancement=AdQ}}"
        ),
        Revision(
            3, Timestamp(2), "aaa", bob,
            "{{talk page}}" +
            "{{Wikiprojet\n" +
            "|Seconde Guerre mondiale|maximum\n" +
            "|Japon|maximum\n" +
            "|Forces armées des États-Unis|maximum\n" +
            "|Nucléaire|maximum\n" +
            "|avancement=e}}"
        ),
        Revision(
            4, Timestamp(3), "ccc", bob,
            "{{talk page}}" +
            "{{Wikiprojet\n" +
            "|Seconde Guerre mondiale|maximum\n" +
            "|Japon|maximum\n" +
            "|Forces armées des États-Unis|maximum\n" +
            "|Nucléaire|maximum\n" +
            "|Sélection transversale|faible\n" +
            "|avancement=Ébauche}}"
        ),
        Revision(
            5, Timestamp(4), "aaa", bob,
            "{{talk page}}" +
            "{{Wikiprojet\n" +
            "|Seconde Guerre mondiale|maximum\n" +
            "|Japon|maximum\n" +
            "|Forces armées des États-Unis|maximum\n" +
            "|Nucléaire|maximum\n" +
            "|avancement=e}}"
        ),
        Revision(
            6, Timestamp(4), "ccc", bob,
            "{{talk page}}" +
            "{{Wikiprojet\n" +
            "|Seconde Guerre mondiale|maximum\n" +
            "|Japon|maximum\n" +
            "|Forces armées des États-Unis|maximum\n" +
            "|Nucléaire|maximum\n" +
            "|Sélection transversale|faible\n" +
            "|avancement=Ébauche}}"
        ),
        Revision(
            7, Timestamp(5), "ddd", alice,
            "{{talk page}}" +
            "{{Wikiprojet\n" +
            "|Seconde Guerre mondiale|maximum\n" +
            "|Japon|maximum\n" +
            "|Forces armées des États-Unis|maximum\n" +
            "|Nucléaire|maximum\n" +
            "|Sélection transversale|faible\n" +
            "|avancement= bd }}"
        ),
        Revision(
            8, Timestamp(6), "eee", alice,
            "{{talk page}}" +
            "{{Wikiprojet\n" +
            "|Seconde Guerre mondiale|maximum\n" +
            "|Japon|maximum\n" +
            "|Forces armées des États-Unis|maximum\n" +
            "|Nucléaire|maximum\n" +
            "|Sélection transversale|faible\n" +
            "|avancement= Bon début }}"
        ),
        Revision(
            9, Timestamp(6), "eee", bob,
            "{{talk page}}" +
            "{{Wikiprojet\n" +
            "|Seconde Guerre mondiale|maximum\n" +
            "|Japon|maximum\n" +
            "|Forces armées des États-Unis|maximum\n" +
            "|Nucléaire|maximum\n" +
            "|Sélection transversale|faible\n" +
            "|avancement= b }}"
        ),
        Revision(
            10, Timestamp(7), "fff", alice,
            "{{talk page}}" +
            "{{Wikiprojet\n" +
            "|Seconde Guerre mondiale|maximum\n" +
            "|Japon|maximum\n" +
            "|Forces armées des États-Unis|maximum\n" +
            "|Nucléaire|maximum\n" +
            "|Sélection transversale|faible\n" +
            "|avancement= a }}"
        ),
        Revision(
            11, Timestamp(8), "fff", alice,
            "{{talk page}}" +
            "{{Wikiprojet\n" +
            "|Seconde Guerre mondiale|maximum\n" +
            "|Japon|maximum\n" +
            "|Forces armées des États-Unis|maximum\n" +
            "|Nucléaire|maximum\n" +
            "|Sélection transversale|faible\n" +
            "|avancement= ba }}"
        ),
        Revision(
            12, Timestamp(9), "fff", alice,
            "{{talk page}}" +
            "{{Wikiprojet\n" +
            "|Seconde Guerre mondiale|maximum\n" +
            "|Japon|maximum\n" +
            "|Forces armées des États-Unis|maximum\n" +
            "|Nucléaire|maximum\n" +
            "|Sélection transversale|faible\n" +
            "|avancement= AdQ }}"
        )
    ]
    page = Page("Foobar", 1, revisions)

    observations = frwiki.extract(page)
    project_labels = {(ob['project'], ob['wp10']): ob
                      for ob in observations}

    expected = [("wikiprojet", "e", Timestamp(0)),
                ("wikiprojet", "bd", Timestamp(5)),
                ("wikiprojet", "b", Timestamp(6)),
                ("wikiprojet", "a", Timestamp(7)),
                ("wikiprojet", "ba", Timestamp(8)),
                ("wikiprojet", "adq", Timestamp(9))]

    print(project_labels)
    for proj, lab, timestamp in expected:
        ob = project_labels[(proj, lab)]
        assert ob['timestamp'] == timestamp
