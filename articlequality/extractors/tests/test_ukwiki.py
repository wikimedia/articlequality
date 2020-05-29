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

    revisions = [
        Revision(
            1, Timestamp(1), "aaa",
            "{{Проект:Адміністративні одиниці країн світу|Польща}}"
        ),
        Revision(
            2, Timestamp(2), "bbb",
            "{{Стаття проекту Крим|важливість=найвища|рівень=ДС}}"
        ),
        Revision(
            3, Timestamp(3), "ccc",
            "{{Стаття проекту Крим|важливість=найвища|рівень=ВС}}"
        ),
            ]
    page = Page("Foobar", 1, revisions)

    observations = ukwiki.extract(page)
    project_labels = {(ob['project'], ob['wp10']): ob
                      for ob in observations}

    expected = []

    print(project_labels)
    for proj, lab, timestamp in expected:
        ob = project_labels[(proj, lab)]
        assert ob['timestamp'] == timestamp
