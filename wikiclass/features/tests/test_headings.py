from collections import namedtuple

from nose.tools import eq_

from ..headings import level_2_headings, level_3_headings

FakeHeading = namedtuple("FakeHeading", ['level'])

headings_datasource = [FakeHeading(2), FakeHeading(3), FakeHeading(4),
                       FakeHeading(2)]

def test_level_2_headings():
    eq_(level_2_headings, 2)

def test_level_3_headings():
    eq_(level_3_headings, 1)
