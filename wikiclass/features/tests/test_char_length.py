from nose.tools import eq_

from ..char_length import char_length


def test_char_length():
    eq_(char_length("0123456789abcdef"), 16)
    eq_(char_length("漢字"), 2)
