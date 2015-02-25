from collections import namedtuple

from nose.tools import eq_

from ..references import ref_tags

FakeTag = namedtuple("FakeTag", ['tag'])

tags_datasource = [FakeTag('derp'),
                   FakeTag('ref'), FakeTag('ref'),
                   FakeTag('herp')]

def test_ref_tags():
    eq_(ref_tags(tags_datasource), 2)
