"""
Basque Wikipedia
++++++++++++++++
"""

from revscoring.datasources.meta import filters, mappers
from revscoring.features import wikitext
from revscoring.features.meta import aggregators
from revscoring.features.modifiers import log, max
from revscoring.features.wikitext.datasources import Revision

from . import wikipedia

# Templates
# Infoboxes:
#   https://gl.wikipedia.org/wiki/Categor%C3%ADa:Caixas_de_informaci%C3%B3n
# They don't have a common naming scheme.
cn_templates = wikitext.revision.template_names_matching(
    r"cómpre[ _]referencia|cando|quen|clarificar|" +
    r"sen[ _]referencias|cómpre[ _]páxina|" +
    r"verificar[ _]credibilidade", name="glwiki.revision.cn_templates")

# Links
category_links = wikitext.revision.wikilink_titles_matching(
    r"(Categoría|Category)\:", name="glwiki.revision.category_links")
image_links = wikitext.revision.wikilink_titles_matching(
    r"(File|Image|Ficheiro)\:", name="glwiki.revision.image_links")

# References
revision = Revision(
    "glwiki.revision.revision",
    wikitext.revision.datasources,
)
paragraphs = mappers.map(
    str, revision.paragraphs_sentences_and_whitespace,
    name="glwiki.revision.paragraphs"
)
paragraphs_without_refs = filters.regex_matching(
    r"^(?!\s*$)((?!<ref>)(.|\n))*$",
    paragraphs,
    name="glwiki.revision.paragraphs_without_refs"
)
paragraphs_without_refs_total_length = aggregators.sum(
    mappers.map(len, paragraphs_without_refs),
    name="glwiki.revision.paragraphs_without_refs_total_length"
)

local_wiki = [
    image_links,
    image_links / max(wikitext.revision.content_chars, 1),
    category_links,
    category_links / max(wikitext.revision.content_chars, 1),
    cn_templates + 1,
    cn_templates / max(wikitext.revision.content_chars, 1),
    log(paragraphs_without_refs_total_length + 1),
    paragraphs_without_refs_total_length /
    max(wikitext.revision.content_chars, 1),
]

wp10 = wikipedia.article + local_wiki
