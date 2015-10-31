from nose.tools import eq_
from revscoring.datasources.revision import text as revision_text
from revscoring.dependencies import solve

from .. import enwiki


def test_cite_templates():
    text = """
    This is some text with a citation.<ref>{{cite lol|title=Made up}}</ref>
    This is some more text. {{foo}} {{{cite}}}

    I am a new paragraph.<ref>{{cite book|title=The stuff}}</ref>
    {{Cite hat|ascii=_n_}}
    """
    eq_(solve(enwiki.cite_templates, cache={revision_text: text}), 3)


def test_infobox_templates():
    text = """
    {{Infobox pants|hats=2|pajams=23}}
    This is some text with a citation.<ref>{{cite lol|title=Made up}}</ref>
    This is some more text.

    I am a new paragraph.<ref>{{cite book|title=The stuff}}</ref>
    {{Cite hat|ascii=_n_}}
    """
    eq_(solve(enwiki.infobox_templates, cache={revision_text: text}), 1)


def test_cn_templates():
    text = """
    {{Infobox pants|hats=2|pajams=23}}
    This is some text with a citation.{{cn}}
    This is some more text. {{foo}}

    I am a new paragraph.{{fact|date=never}}

    I am a new paragraph.{{Citation_needed|date=never}}
    """
    eq_(solve(enwiki.cn_templates, cache={revision_text: text}), 3)


def test_who_templates():
    text = """
    This is some text with a citation.{{cn}}
    This is some more text. {{foo}}

    I am a new paragraph.{{who}}

    I am a new paragraph.{{who|date=today}}
    """
    eq_(solve(enwiki.who_templates, cache={revision_text: text}), 2)


def test_main_article_templates():
    text = """
    This is some text with a citation.{{cn}}
    This is some more text. {{foo}}

    == Some section ==
    {{Main|section}}

    I am a new paragraph.{{who|date=today}}
    """
    eq_(solve(enwiki.main_article_templates, cache={revision_text: text}), 1)
