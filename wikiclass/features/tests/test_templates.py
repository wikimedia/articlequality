from collections import namedtuple

from nose.tools import eq_

from ..templates import cite_templates, infobox_templates

FakeTemplate = namedtuple("FakeTemplate", ['name'])

templates_datasource = [FakeTemplate("Hat"),
                        FakeTemplate("Cite"),
                        FakeTemplate("Cite waffle"),
                        FakeTemplate("Research project/Infobox"),
                        FakeTemplate("Infobox"),
                        FakeTemplate("DerpInfobox"),
                        FakeTemplate("Anarchism/Sidebar")]

def test_cite_templates():
    eq_(cite_templates(templates_datasource), 2)
    
def test_infobox_templates():
    eq_(infobox_templates(templates_datasource), 4)
