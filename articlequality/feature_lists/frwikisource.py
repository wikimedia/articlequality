"""
French Wikisource
+++++++++++++++++
"""

from revscoring.features import wikitext
from revscoring.features.modifiers import max
from revscoring.languages import french

from . import wikisource

local_wiki = [
    wikitext.revision.chars,
    french.stemmed.revision.stem_chars,
    (french.stemmed.revision.stem_chars /
     max(wikitext.revision.chars, 1)),
    french.dictionary.revision.dict_words / max(wikitext.revision.words, 1),
    french.dictionary.revision.dict_words /
    max(french.dictionary.revision.non_dict_words, 1)
]

pagelevel = local_wiki + wikisource.page
