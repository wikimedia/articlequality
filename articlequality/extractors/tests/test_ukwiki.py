from collections import namedtuple
from mwtypes import Timestamp

from .. import ukwiki


def test_extractor():

    Revision = namedtuple("Revisions", ['id', 'timestamp', 'sha1', 'text'])

    class Page:

        def __init__(self, title, namespace, revisions):
            self.title = title
            self.namespace = namespace
            self.revisions = revisions

        def __iter__(self):
            return iter(self.revisions)

    revisions = []
    page = Page("Foobar", 1, revisions)

    observations = ukwiki.extract(page)
    project_labels = {(ob['project'], ob['wp10']): ob
                      for ob in observations}

    expected = []

    print(project_labels)
    for proj, lab, timestamp in expected:
        ob = project_labels[(proj, lab)]
        assert ob['timestamp'] == timestamp
