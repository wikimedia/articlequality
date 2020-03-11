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
            "{{Marca de projeto|3|Brasil|3|rev=20170714}}"
        ),
        Revision(
            2, Timestamp(2), "bbb",
            "{{Marca de projeto|3|Biografias|4|rev=20170714}}"
        )
    ]
    page = Page("Foobar", 1, revisions)

    observations = ptwiki.extract(page)
    project_labels = {(ob['project'], ob['wp10']): ob
                      for ob in observations}

    expected = [("brasil", "3", Timestamp(1)),
                ("biografias", "4", Timestamp(2))]

    print(project_labels)
    for proj, lab, timestamp in expected:
        ob = project_labels[(proj, lab)]
        assert ob['timestamp'] == timestamp
