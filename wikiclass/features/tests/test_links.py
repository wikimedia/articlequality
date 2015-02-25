from collections import namedtuple

from nose.tools import eq_

from ..links import category_links, image_links, internal_links

FakeLink = namedtuple("FakeLink", "title")

internal_links_datasource = [FakeLink("Foobar"),
                             FakeLink("File:Hat.jpg"),
                             FakeLink("file:Bum.gif"),
                             FakeLink("Category:Hats")]

def test_category_links():
    eq_(category_links(internal_links_datasource), 1)

def test_image_links():
    eq_(image_links(internal_links_datasource), 2)

def test_internal_links():
    eq_(internal_links(internal_links_datasource), 4)
