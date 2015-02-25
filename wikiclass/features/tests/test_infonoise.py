from nose.tools import eq_

from ..infonoise import infonoise


def test_infonoise():
    is_stopword = lambda w: w == "is"
    stem_word = lambda w: w[0] # Just the first character
    content_words = ["This", "is", "twelve"] # 12 characters of content words
    
    eq_(infonoise(is_stopword, stem_word, content_words), 2/12)
