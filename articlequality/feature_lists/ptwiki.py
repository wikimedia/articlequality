"""
Portuguese Wikipedia
++++++++++++++++++++
"""
import re

from revscoring import Feature
from revscoring.datasources.meta import filters, mappers
from revscoring.features import wikitext
from revscoring.features.meta import aggregators
from revscoring.features.modifiers import log, max, sub
from revscoring.languages import portuguese

from . import wikipedia

# Templates
infobox_templates = wikitext.revision.template_names_matching(
    r"Info", name="ptwiki.revision.infobox_templates")
CN_TEMPLATES = [
    r"Carece de fontes",
    r"Carece de fontes2",
    r"Carece de fontes/bloco",
    r"Carece de fontes/bloco2"
]
cn_templates = wikitext.revision.template_names_matching(
    "|".join(CN_TEMPLATES), name="ptwiki.revision.cn_templates")
MAIN_TEMPLATES = [
    r"Artigo[ _]principal",
    r"Ver[ _]artigo[ _]principali",
    r"Principal",
    r"Ver[ _]também artigo[ _]principal",
    r"Main",
    r"Detalhes",
    r"Mais",
    r"Artigoprincipal",
    r"AP", r"Details", r"Ver[ _]artigo"
]
main_article_templates = wikitext.revision.template_names_matching(
    "|".join(MAIN_TEMPLATES), name="ptwiki.main_article_templates")
CITE_TEMPLATES = [
    r"Cite",
    r"Citar",
    r"Citar web",
    r"Citar livro",
    r"Harvard[_ ]citation[_ ]no[_ ]brackets", r"harvnb",
    r"Harvard citation", r"harv",
    r"Harvard citation text", r"harvtxt",
    r"Harvcoltxt",
    r"Harvcol",
    r"Harvcolnb",
    r"Harvard citations", r"harvs",
    r"Harvp"
]
cite_templates = wikitext.revision.template_names_matching(
    "|".join(CITE_TEMPLATES), name="ptwiki.revision.cite_templates")
shortened_footnote_templates = wikitext.revision.template_names_matching(
    r"sfn", name="ptwiki.revision.shortened_footnote_templates")
all_ref_tags = shortened_footnote_templates + wikitext.revision.ref_tags
all_cite_templates = cite_templates + shortened_footnote_templates
proportion_of_templated_references = \
    all_cite_templates / max(all_ref_tags, 1)
non_templated_references = max(all_ref_tags - all_cite_templates, 0)
non_cite_templates = sub(
    wikitext.revision.templates, all_cite_templates,
    name="ptwiki.revision.non_cite_templates"
)

# Links
category_links = wikitext.revision.wikilink_titles_matching(
    r"(Category|Categoria)\:", name="ptwiki.revision.category_links")

image_links = wikitext.revision.wikilink_titles_matching(
    r"(File|Ficheiro|Arquivo|Image|Imagem)\:",
    name="ptwiki.revision.image_links")

image_templates = wikitext.revision.template_names_matching(
    r"(Scalable[ _]image|Panorama|Imagem[ _]vertical)|Panorama|Panorama 2",
    name='ptwiki.revision.image_template')


def get_images(strs):
    """
    Parses a list of strings, expected to be tags or templates
    to get matching image patterns and returns a count of the matches.
    """
    matches = re.findall(
        r"image[1-9]{1,2}|(File|Ficheiro|" +
        r"Image|Imagem|Archivo):|photo[1-9][a-z]",
        "".join(strs), re.I)
    return len(matches)


image_templates_str = wikitext.revision.datasources.templates_str_matching(
    r"{{(imagem multipla|galeria|multiple image|image array|gallery)",
    name='ptwiki.revision.image_templates_str')

images_in_templates = Feature("ptwiki.revision.images_in_templates",
                              get_images,
                              depends_on=[image_templates_str],
                              returns=int)

image_tags_str = wikitext.revision.datasources.tags_str_matching(
    r"<(gallery|imagemap)",
    name='ptwiki.revision.image_tags_str')

images_in_tags = Feature("ptwiki.revision.images_in_tags",
                         get_images,
                         depends_on=[image_tags_str],
                         returns=int)


def get_infobox_images(strs):
    matches = re.findall(
        r"\.(jpg|jpeg|png|gif|svg|tiff|pdf|ogg|djvu)", "".join(strs), re.I)
    return len(matches)


infobox_templates_str = wikitext.revision.datasources.templates_str_matching(
    r"{{Infobox",
    name='ptwiki.revision.infobox_templates_str')

infobox_images = Feature("ptwiki.infobox_images",
                         get_infobox_images,
                         depends_on=[infobox_templates_str],
                         returns=int)

all_images = image_links + image_templates +\
    images_in_templates + images_in_tags + infobox_images

# References
paragraphs = mappers.map(
    str, wikitext.revision.datasources.paragraphs_sentences_and_whitespace,
    name="ptwiki.revision.paragraphs"
)
paragraphs_without_refs = filters.regex_matching(
    r"^(?!\s*$)((?!<ref>)(.|\n))*$",
    paragraphs,
    name="ptwiki.revision.paragraphs_without_refs"
)
paragraphs_without_refs_total_length = aggregators.sum(
    mappers.map(len, paragraphs_without_refs),
    name="ptwiki.revision.paragraphs_without_refs_total_length"
)

local_wiki = [
    all_images,
    all_images / max(wikitext.revision.content_chars, 1),
    category_links,
    category_links / max(wikitext.revision.content_chars, 1),
    all_ref_tags,
    all_ref_tags / max(wikitext.revision.content_chars, 1),
    all_cite_templates,
    all_cite_templates / max(wikitext.revision.content_chars, 1),
    proportion_of_templated_references,
    non_templated_references,
    non_templated_references / max(wikitext.revision.content_chars, 1),
    non_cite_templates,
    non_cite_templates / max(wikitext.revision.content_chars, 1),
    infobox_templates,
    cn_templates + 1,
    cn_templates / max(wikitext.revision.content_chars, 1),
    main_article_templates,
    main_article_templates / max(wikitext.revision.content_chars, 1),
    (portuguese.stemmed.revision.stem_chars /
     max(wikitext.revision.content_chars, 1)),
    log(paragraphs_without_refs_total_length + 1)
]

wp10 = wikipedia.article + local_wiki
