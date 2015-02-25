from collections import namedtuple

from nose.tools import eq_

from ..parsed_revision_text import (content, content_words, headings,
                                    internal_links, parsed_revision_text, tags,
                                    templates)


def test_content():
    FakeParsedRevisionText = namedtuple("FakeParsedRevisionText",
                                        ['strip_code'])
    parsed_revision_text = FakeParsedRevisionText(lambda: "some content")
    
    eq_(content(parsed_revision_text), "some content")

def test_content_words():
    content = "some content, and stuff 漢字?"
    
    eq_(content_words(content), ["some", "content", "and", "stuff", "漢字"])

def test_headings():
    FakeParsedRevisionText = namedtuple("FakeParsedRevisionText",
                                        ['filter_headings'])
    parsed_revision_text = FakeParsedRevisionText(lambda: ['h', 'h', 'h'])
    
    eq_(headings(parsed_revision_text), ['h', 'h', 'h'])

def test_internal_links():
    FakeParsedRevisionText = namedtuple("FakeParsedRevisionText",
                                        ['filter_wikilinks'])
    parsed_revision_text = FakeParsedRevisionText(lambda: ['l', 'l', 'l'])
    
    eq_(internal_links(parsed_revision_text), ['l', 'l', 'l'])

def test_parsed_revision_text():
    # Nothing to really test here.  Let's just make sure it runs.
    assert parsed_revision_text("Some text") is not None

def test_tags():
    FakeParsedRevisionText = namedtuple("FakeParsedRevisionText",
                                        ['filter_tags'])
    parsed_revision_text = FakeParsedRevisionText(lambda: ['t', 't', 't'])
    
    eq_(tags(parsed_revision_text), ['t', 't', 't'])

def test_tags():
    FakeParsedRevisionText = namedtuple("FakeParsedRevisionText",
                                        ['filter_templates'])
    parsed_revision_text = FakeParsedRevisionText(lambda: ['t', 't', 't'])
    
    eq_(templates(parsed_revision_text), ['t', 't', 't'])
