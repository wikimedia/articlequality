from collections import namedtuple

import mwparserfromhell as mwp
from mw import Timestamp
from nose.tools import eq_

from .. import enwiki


def test_extractor():

    Revision = namedtuple("Revisions", ['id', 'timestamp', 'sha1', 'text'])

    class Page:

        def __init__(self, title, namespace, revisions):
            self.title = title
            self.namespace = namespace
            self.revisions = revisions

        def __iter__(self):
            return iter(self.revisions)

    revisions = [
        Revision(
            1, Timestamp(0), "aaa",
            "{{talk page}}{{WikiProject Medicine|class=Stub}}..."
        ),
        Revision(
            2, Timestamp(1), "bbb",
            "{{talk page}}{{WikiProject Medicine|class=B}}..."
        ),
        Revision(
            3, Timestamp(2), "aaa",
            "{{talk page}}{{WikiProject Medicine|class=Stub}}..."
        ),
        Revision(
            4, Timestamp(3), "ccc",
            "{{talk page}}{{WikiProject Medicine|class=C}}..."
        ),
        Revision(
            5, Timestamp(4), "aaa",
            "{{talk page}}{{WikiProject Medicine|class=Stub}}..."
        ),
        Revision(
            6, Timestamp(4), "ccc",
            "{{talk page}}{{WikiProject Medicine|class= C}}..."
        ),
        Revision(
            7, Timestamp(5), "ddd",
            "{{talk page}}{{WikiProject Medicine|class=B}}\n" +
            "{{WP_Hats|class=B}}..."
        )
    ]
    page = Page("Foobar", 1, revisions)

    observations = enwiki.extract(page)
    project_labels = {(ob['project'], ob['label']): ob for ob in observations}

    expected = [("medicine", "stub", Timestamp(0)),
                ("medicine", "c", Timestamp(3)),
                ("medicine", "b", Timestamp(5)),
                ("hats", "b", Timestamp(5))]

    print(project_labels)
    for proj, lab, timestamp in expected:
        ob = project_labels[(proj, lab)]
        eq_(ob['timestamp'], timestamp)
