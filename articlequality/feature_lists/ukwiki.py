"""
Ukrainian Wikipedia
+++++++++++++++++++
"""
import re

from revscoring.datasources.meta import filters, mappers
from revscoring.features import wikitext
from revscoring import Feature
from revscoring.features.meta import aggregators
from revscoring.features.modifiers import log, max, sub
from revscoring.languages import ukrainian

from . import wikipedia

# Templates
infobox_templates = wikipedia.infobox_templates()
CN_TEMPLATES = [
    r"Citation[_ ]needed",
    r"Cn",
    r"Fact"
]
cn_templates = wikitext.revision.template_names_matching(
    "|".join(CN_TEMPLATES), name="ukwiki.revision.cn_templates")
MAIN_TEMPLATES = [
    r"Main",
    r"Докладніше"
]
main_article_templates = wikitext.revision.template_names_matching(
    "|".join(MAIN_TEMPLATES), name="ukwiki.revision.main_article_templates")
CITE_TEMPLATES = [
]
cite_templates = wikitext.revision.template_names_matching(
    "|".join(CITE_TEMPLATES), name="ukwiki.revision.cite_templates")
SFN_TEMPLATES = [
]
shortened_footnote_templates = wikitext.revision.template_names_matching(
    "|".join(SFN_TEMPLATES),
    name="ukwiki.revision.shortened_footnote_templates")
all_ref_tags = shortened_footnote_templates + wikitext.revision.ref_tags
all_cite_templates = cite_templates + shortened_footnote_templates
proportion_of_templates_references = \
    all_cite_templates / max(all_ref_tags, 1)
non_templated_references = max(all_ref_tags - all_cite_templates, 0)
non_cite_templates = sub(
        wikitext.revision.templates, all_cite_templates,
        name="ukwiki.revision.non_cite_templates"
)

# Links
CATEGORY_LINKS = [
]
category_links = wikitext.revision.wikilink_titles_matching(
    "|".join(CATEGORY_LINKS), name="ukwiki.revision.category_links")

IMAGE_LINKS = [
]
image_links = wikitext.revision.wikilink_titles_matching(
    "|".join(IMAGE_LINKS), name="ukwiki.revision.image_links")

IMAGE_TEMPLATES = [
]
image_templates = wikitext.revision.template_names_matching(
    "|".join(IMAGE_TEMPLATES), name="ukwiki.revision.image_template")


def get_images(strs):
    """
    Parses a list of strings, expected to be tags or templates
    to get matching image patterns and returns a count of the matches.
    """
    matches = re.findall(
        r"image[1-9]{1,2}|File:|Image:|photo[1-9][a-z]",
        "".join(strs), re.I)
    return len(matches)


IMAGE_TEMPLATES_STR = [
]
image_templates_str = wikitext.revision.datasources.templates_str_matching(
    "|".join(IMAGE_TEMPLATES_STR), name="ukwiki.revision.image_template_str")

images_in_templates = Feature("ukwiki.revision.images_in_templates",
                              get_images,
                              depends_on=[image_templates_str],
                              returns=int)

IMAGE_TAGS_STR = [
]
image_tags_str = wikitext.revision.datasources.tags_str_matching(
    "|".join(IMAGE_TAGS_STR), name="ukwiki.revision.image_tags_str")

images_in_tags = Feature("ukwiki.revision.images_in_tags",
                         get_images,
                         depends_on=[image_tags_str],
                         returns=int)


def get_infobox_images(strs):
    matches = re.findall(
         r"\.(jpg|jpeg|png|gif|svg|tiff|pdf|ogg|djvu)", "".join(strs), re.I)
    return len(matches)


infobox_templates_str = wikipedia.infobox_templates()

infobox_images = Feature("ukwiki.infobox_images",
                         get_infobox_images,
                         depends_on=[infobox_templates_str],
                         returns=int)

all_images = image_links + image_templates +\
    images_in_templates + images_in_tags + infobox_images

# References
paragraphs = mappers.map(
    str, wikitext.revision.datasources.paragraphs_sentences_and_whitespace,
    name="ukwiki.revision.paragraphs"
)
paragraphs_without_refs = filters.regex_matching(
    r"",  # Insert string to match ref tags
    paragraphs, name="ukwiki.revision.paragraphs_without_refs"
)
paragraphs_without_refs_total_length = aggregators.sum(
    mappers.map(len, paragraphs_without_refs),
    name="ukwiki.revision.paragraph_without_refs_total_length"
)

# Do we have words to watch for ukwiki?

local_wiki = [
    all_images,
    all_images / max(wikitext.revision.content_chars, 1),
    category_links,
    category_links / max(wikitext.revision.content_chars, 1),
    all_ref_tags,
    all_ref_tags / max(wikitext.revision.content_chars, 1),
    all_cite_templates,
    all_cite_templates / max(wikitext.revision.content_chars, 1),
    non_templated_references,
    non_templated_references / max(wikitext.revision.content_chars, 1),
    non_cite_templates,
    non_cite_templates / max(wikitext.revision.content_chars, 1),
    infobox_templates,
    cn_templates + 1,
    cn_templates / max(wikitext.revision.content_chars, 1),
    main_article_templates,
    main_article_templates / max(wikitext.revision.content_chars, 1),
    (ukrainian.stemmed.revision.stem_chars /
     max(wikitext.revision.content_chars, 1)),
    log(paragraphs_without_refs_total_length + 1),
]

wp10 = wikipedia.article + local_wiki
