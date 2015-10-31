from nose.tools import eq_
from revscoring.datasources.revision import text as revision_text
from revscoring.dependencies import solve

from .. import frwiki


def test_cite_templates():
    text = """
    This is some text with a citation.<ref>{{Article|title=Made up}}</ref>
    This is some more text. {{foo}} {{{cite}}}

    I am a new paragraph.<ref>{{Chapitre|title=The stuff}}</ref>
    {{Jugement|ascii=_n_}}{{Lien_web}}{{Loi}}{{Ouvrage}}
    """
    eq_(solve(frwiki.cite_templates, cache={revision_text: text}), 6)


def test_infobox_templates():
    text = """
    {{Infobox pants|hats=2|pajams=23}}
    This is some text with a citation.<ref>{{cite lol|title=Made up}}</ref>
    This is some more text.

    I am a new paragraph.<ref>{{cite book|title=The stuff}}</ref>
    {{Cite hat|ascii=_n_}}
    """
    eq_(solve(frwiki.infobox_templates, cache={revision_text: text}), 1)


def test_lvl1_cn_templates():
    text = """
    {{Référence nécessaire|hats=2|pajams=23}}
    This is some text with a citation.{{Citation nécessaire}}
    This is some more text. {{Référence_à_confirmer}}

    I am a new paragraph.{{fact|date=never}}

    I am a new paragraph.{{Référence souhaitée|date=never}}{{Inédit}}
    """
    eq_(solve(frwiki.lvl1_cn_templates, cache={revision_text: text}), 5)


def test_lvl2_cn_templates():
    text = """
    {{Référence insuffisante|hats=2|pajams=23}}
    This is some text with a citation.{{Référence incomplète}}
    This is some more text. {{Détournement de sources}}

    I am a new paragraph.{{Section à sourcer|date=never}}

    I am a new paragraph.{{Référence souhaitée|date=never}}{{Inédit}}
    """
    eq_(solve(frwiki.lvl2_cn_templates, cache={revision_text: text}), 4)


def test_lvl3_cn_templates():
    text = """
    {{Sources à lier|hats=2|pajams=23}}
    This is some text with a citation.{{Référence obsolète}}
    This is some more text. {{À sourcer}}

    I am a new paragraph.{{Sources obsolètes|date=never}}

    I am a new paragraph.{{Sources secondaires|date=never}}{{BPV à sourcer}}
    """
    eq_(solve(frwiki.lvl3_cn_templates, cache={revision_text: text}), 6)


def test_lvl4_cn_templates():
    text = """
    {{À prouver|hats=2|pajams=23}}
    This is some text with a citation.{{Référence obsolète}}
    This is some more text. {{À sourcer}}

    I am a new paragraph.{{Faut sourcer|date=never}}

    I am a new paragraph.{{Sources secondaires|date=never}}{{BPV à sourcer}}
    """
    eq_(solve(frwiki.lvl4_cn_templates, cache={revision_text: text}), 2)


def test_lvl5_cn_templates():
    text = """
    {{À vérifier|hats=2|pajams=23}}
    This is some text with a citation.{{Référence obsolète}}
    This is some more text. {{À sourcer}}

    I am a new paragraph.{{Faut sourcer|date=never}}

    I am a new paragraph.{{Vérifiabilité|date=never}}{{BPV à sourcer}}
    """
    eq_(solve(frwiki.lvl5_cn_templates, cache={revision_text: text}), 2)


def test_main_article_templates():
    text = """
    This is some text with a citation.{{cn}}
    This is some more text. {{foo}}

    == Some section ==
    {{Article principal|section}}
    {{Article_détaillé|le section}}

    I am a new paragraph.{{who|date=today}}
    """
    eq_(solve(frwiki.main_article_templates, cache={revision_text: text}), 2)
