"""
Turkish Wikipedia
+++++++++++++++++
"""

from revscoring.features import wikitext
from revscoring.features.modifiers import max, sub

from . import wikipedia

cite_templates = wikitext.revision.template_names_matching(
    r"Kaynak|.*[ _]kaynağı",
    name="trwiki.revision.cite_templates")
proportion_of_templated_references = \
    cite_templates / max(wikitext.revision.ref_tags, 1)
non_templated_references = max(wikitext.revision.ref_tags - cite_templates, 0)
non_cite_templates = sub(
    wikitext.revision.templates, cite_templates,
    name="trwiki.revision.non_cite_templates"
)
infobox_templates = wikitext.revision.template_names_matching(
    r".*[ _]bilgi[ _]kutusu",
    name="trwiki.revision.infobox_templates")

# Copied (2015-10-29) from:
# https://fr.wikipedia.org/wiki/Wikip%C3%A9dia:Citez_vos_sources#R.C3.A9clamation_et_contestation_de_sources
cn_templates = wikitext.revision.template_names_matching(
    r"Kaynak[ _]belirt|Olgu|Fact|Delil",
    name="trwiki.revision.lvl1_cn_templates")

main_article_templates = wikitext.revision.template_names_matching(
    r"Ana|Anamadde",
    name="trwiki.main_article_templates")

# Links
category_links = wikitext.revision.wikilink_titles_matching(
    r"Category|Kategori\:", name="trwiki.revision.category_links")
image_links = wikitext.revision.wikilink_titles_matching(
    r"File|Image|Resim\:", name="rrwiki.revision.image_links")

local_wiki = [
    image_links,
    image_links / max(wikitext.revision.content_chars, 1),
    category_links,
    category_links / max(wikitext.revision.content_chars, 1),
    cite_templates,
    cite_templates / max(wikitext.revision.content_chars, 1),
    proportion_of_templated_references,
    non_templated_references,
    non_templated_references / max(wikitext.revision.content_chars, 1),
    non_cite_templates,
    non_cite_templates / max(wikitext.revision.content_chars, 1),
    infobox_templates,
    main_article_templates,
    main_article_templates / max(wikitext.revision.content_chars, 1),
    cn_templates,
    cn_templates / max(wikitext.revision.content_chars, 1)
]

wp10 = local_wiki + wikipedia.article
