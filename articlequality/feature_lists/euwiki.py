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
infobox_templates = wikitext.revision.template_names_matching(
    r"[\w\s_]*infotaula[ _]automatikoa$",
    name="euwiki.revision.infobox_templates")
cn_templates = wikitext.revision.template_names_matching(
    r"erref[ _]behar", name="euwiki.revision.cn_templates")

# Links
category_links = wikitext.revision.wikilink_titles_matching(
    r"(Kategoria|Category)\:", name="euwiki.revision.category_links")
image_links = wikitext.revision.wikilink_titles_matching(
    r"(File|Image|Fitxategi)\:", name="euwiki.revision.image_links")

# References
revision = Revision(
    "euwiki.revision.revision",
    wikitext.revision.datasources,
)
paragraphs = mappers.map(
    str, revision.paragraphs_sentences_and_whitespace,
    name="euwiki.revision.paragraphs"
)
paragraphs_without_refs = filters.regex_matching(
    r"^(?!\s*$)((?!<ref>)(.|\n))*$",
    paragraphs,
    name="euwiki.revision.paragraphs_without_refs"
)
paragraphs_without_refs_total_length = aggregators.sum(
    mappers.map(len, paragraphs_without_refs),
    name="euwiki.revision.paragraphs_without_refs_total_length"
)

local_wiki = [
    image_links,
    image_links / max(wikitext.revision.content_chars, 1),
    category_links,
    category_links / max(wikitext.revision.content_chars, 1),
    infobox_templates,
    cn_templates + 1,
    cn_templates / max(wikitext.revision.content_chars, 1),
    log(paragraphs_without_refs_total_length + 1),
]

wp10 = wikipedia.article + local_wiki
