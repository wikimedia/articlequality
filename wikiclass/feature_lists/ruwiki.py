"""
Russian Wikipedia
+++++++++++++++++
"""

from revscoring.features import wikitext
from revscoring.features.modifiers import max
from revscoring.languages import russian

from . import wikipedia

cn_templates = wikitext.revision.template_names_matching(
    r"Нет[ _]АИ",
    name="ruwiki.revision.cn_templates")

# Links
category_links = wikitext.revision.wikilink_titles_matching(
    r"Category|Категория\:", name="revision.category_links")
image_links = wikitext.revision.wikilink_titles_matching(
    r"File|Image|Файл\:", name="revision.image_links")

local_wiki = [
    russian.stemmed.revision.stem_chars,
    (russian.stemmed.revision.stem_chars /
     max(wikitext.revision.content_chars, 1)),
    image_links,
    image_links / max(wikitext.revision.content_chars, 1),
    category_links,
    category_links / max(wikitext.revision.content_chars, 1),
    russian.dictionary.revision.dict_words,
    russian.dictionary.revision.dict_words / max(wikitext.revision.words, 1),
    cn_templates,
    cn_templates / max(wikitext.revision.content_chars, 1),
]

wp10 = local_wiki + wikipedia.article
