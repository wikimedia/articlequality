from collections import namedtuple

from mwtypes import Timestamp

from .. import ruwiki


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
            "{{Статья проекта WikiProject\n" +
            "|важность=высшая\n" +
            "|уровень=IV\n<!-- HTML test comment -->}}"
        ),
        Revision(
            2, Timestamp(1), "bbb", alice,
            "{{Статья проекта WikiProject\n" +
            "|важность=высшая\n" +
            "|уровень=III}}"
        ),
        Revision(
            3, Timestamp(2), "aaa", bob,
            "{{Статья проекта WikiProject\n" +
            "|важность=высшая\n" +
            "|уровень=IV<!-- HTML test comment -->}}"
        ),
        Revision(
            4, Timestamp(3), "bbb", bob,
            "{{Статья проекта WikiProject\n" +
            "|важность=высшая\n" +
            "|уровень=III}}"
        ),
        Revision(
            5, Timestamp(4), "ccc", alice,
            "{{Статья проекта WikiProject\n" +
            "|важность=высшая\n" +
            "|уровень=II}}"
        ),
        Revision(
            6, Timestamp(5), "bbb", bob,
            "{{Статья проекта WikiProject\n" +
            "|важность=высшая\n" +
            "|уровень=III}}"
        ),
        Revision(
            7, Timestamp(6), "ccc", bob,
            "{{Статья проекта WikiProject\n" +
            "|важность=высшая\n" +
            "|уровень=II}}"
        ),
        Revision(
            8, Timestamp(7), "ddd", alice,
            "{{Статья проекта WikiProject\n" +
            "|важность=высшая\n" +
            "|уровень=I}}"
        ),
        Revision(
            9, Timestamp(8), "eee", alice,
            "{{Статья проекта WikiProject\n" +
            "|важность=высшая\n" +
            "|уровень=ХС}}"
        ),
        Revision(
            10, Timestamp(9), "fff", alice,
            "{{Статья проекта WikiProject\n" +
            "|важность=высшая\n" +
            "|уровень=дс}}"
        ),
        Revision(
            11, Timestamp(10), "eee", bob,
            "{{Статья проекта WikiProject\n" +
            "|важность=высшая\n" +
            "|уровень=ХС}}"
        ),
        Revision(
            12, Timestamp(11), "fff", bob,
            "{{Статья проекта WikiProject\n" +
            "|важность=высшая\n" +
            "|уровень=дс}}"
        ),
        Revision(
            13, Timestamp(12), "ggg", alice,
            "{{Статья проекта WikiProject\n" +
            "|важность=высшая\n" +
            "|уровень=ИС<!-- HTML test comment -->}}"
        )
    ]
    page = Page("Foobar", 1, revisions)

    observations = ruwiki.extract(page)
    project_labels = {(ob['project'], ob['wp10']):
                      ob for ob in observations}

    expected = [("wikiproject", "IV", Timestamp(0)),
                ("wikiproject", "III", Timestamp(1)),
                ("wikiproject", "II", Timestamp(4)),
                ("wikiproject", "I", Timestamp(7)),
                ("wikiproject", "ХС", Timestamp(8)),
                ("wikiproject", "ДС", Timestamp(9)),
                ("wikiproject", "ИС", Timestamp(12))]

    print(project_labels)
    for proj, lab, timestamp in expected:
        ob = project_labels[(proj, lab)]
        assert ob['timestamp'] == timestamp
