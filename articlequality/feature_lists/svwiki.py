"""
Swedish Wikipedia
+++++++++++++++++
"""

from revscoring.features import wikitext
from revscoring.features.modifiers import max
from revscoring.languages import swedish

from . import wikipedia

cn_templates = wikitext.revision.template_names_matching(
    r"Källa[ _]behövs|Kb",
    name="svwiki.revision.cn_templates")

# Links
category_links = wikitext.revision.wikilink_titles_matching(
    r"Category|Kategori\:", name="revision.category_links")
image_links = wikitext.revision.wikilink_titles_matching(
    r"File|Image|Fil\:", name="revision.image_links")

local_wiki = [
    image_links,
    image_links / max(wikitext.revision.content_chars, 1),
    category_links,
    category_links / max(wikitext.revision.content_chars, 1),
    swedish.dictionary.revision.dict_words,
    swedish.dictionary.revision.dict_words / max(wikitext.revision.words, 1),
    cn_templates,
    cn_templates / max(wikitext.revision.content_chars, 1),
]

wp10 = local_wiki + wikipedia.article
