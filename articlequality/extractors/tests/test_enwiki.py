from collections import namedtuple

from mwtypes import Timestamp

from .. import enwiki


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
            "{{talk page}}{{WikiProject Medicine|class=Stub}}..."
        ),
        Revision(
            2, Timestamp(1), "bbb", bob,
            "{{talk page}}{{WikiProject Medicine|class=B}}..."
        ),
        Revision(
            3, Timestamp(2), "aaa", bob,
            "{{talk page}}{{WikiProject Medicine|class=Stub<!--" +
            " test HTML comment -->}}..."
        ),
        Revision(
            4, Timestamp(3), "ccc", alice,
            "{{talk page}}{{WikiProject Medicine|class=C}}..."
        ),
        Revision(
            5, Timestamp(4), "aaa", bob,
            "{{talk page}}{{WikiProject Medicine|class=Stub}}..."
        ),
        Revision(
            6, Timestamp(4), "ccc", bob,
            "{{talk page}}{{WikiProject Medicine|class= C}}..."
        ),
        Revision(
            7, Timestamp(5), "ddd", alice,
            "{{talk page}}{{WikiProject Medicine|class=B}}\n" +
            "{{WP_Hats|class=B}}..."
        ),
        Revision(
            8, Timestamp(6), "eee", alice,
            """{{talkheader}}
{{WikiProjectBannerShell|1=
{{WPMILHIST|class=C
<!-- B-Class 5-criteria checklist -->
|B1 <!-- Referencing and citations --> =n
|B2 <!-- Coverage and accuracy --> =y
|B3 <!-- Structure --> =y
|B4 <!-- Grammar and style --> =y
|B5 <!-- Supporting materials --> =y
|National=y|African=y}}
{{AfricaProject|class=C|importance=Top|Djibouti=y|Djibouti-importance=Top}}
}}"""
        )
    ]
    page = Page("Foobar", 1, revisions)

    observations = enwiki.extract(page)
    project_labels = {(ob['project'], ob['wp10']): ob
                      for ob in observations}

    expected = [("medicine", "stub", Timestamp(0)),
                ("medicine", "c", Timestamp(3)),
                ("medicine", "b", Timestamp(5)),
                ("hats", "b", Timestamp(5)),
                ("milhist", "c", Timestamp(6)),
                ("africaproject", "c", Timestamp(6))]

    print(project_labels)
    for proj, lab, timestamp in expected:
        ob = project_labels[(proj, lab)]
        assert ob['timestamp'] == timestamp
