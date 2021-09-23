"""
Dutch Wikipedia
+++++++++++++++++
"""

from revscoring.features import wikitext
from revscoring.features.modifiers import max
from revscoring.features.meta import aggregators
from revscoring.languages import dutch
from revscoring.datasources.meta import mappers, filters
from . import wikipedia

cn_templates = wikitext.revision.template_names_matching(
    r"Bron\??|Fact|Wikify|reden|Twijfel|Geenbron|Wanneer?|" +
    r"Feit|Refnodig|Referentie[ _]gewenst",
    name="nlwiki.revision.cn_templates")

infobox_templates = wikitext.revision.template_names_matching(
    r"Infobox", name="nlwiki.revision.infobox_templates")

# Links
category_links = wikitext.revision.wikilink_titles_matching(
    r"Category|Categorie\:", name="revision.category_links")
image_links = wikitext.revision.wikilink_titles_matching(
    r"File|Image|Afbeelding|Bestand\:", name="revision.image_links")

# References
paragraphs = mappers.map(
    str, wikitext.revision.datasources.paragraphs_sentences_and_whitespace,
    name="enwiki.revision.paragraphs"
)
paragraphs_without_refs = filters.regex_matching(
    r"^(?!\s*$)((?!<ref>)(.|\n))*$",
    paragraphs,
    name="enwiki.revision.paragraphs_without_refs"
)
paragraphs_without_refs_total_length = aggregators.sum(
    mappers.map(len, paragraphs_without_refs),
    name="enwiki.revision.paragraphs_without_refs_total_length"
)

local_wiki = [
    dutch.stemmed.revision.stem_chars,
    (dutch.stemmed.revision.stem_chars /
     max(wikitext.revision.content_chars, 1)),
    image_links,
    image_links / max(wikitext.revision.content_chars, 1),
    category_links,
    category_links / max(wikitext.revision.content_chars, 1),
    dutch.dictionary.revision.dict_words,
    dutch.dictionary.revision.dict_words / max(wikitext.revision.words, 1),
    paragraphs_without_refs_total_length,
    paragraphs_without_refs_total_length /
        max(wikitext.revision.content_chars, 1),
    cn_templates,
    cn_templates / max(wikitext.revision.content_chars, 1),
    infobox_templates,
    infobox_templates / max(wikitext.revision.content_chars, 1)
]

wp10 = local_wiki + wikipedia.article
