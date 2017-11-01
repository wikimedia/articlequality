"""
French Wikipedia
+++++++++++++++++
"""

from revscoring.features import wikitext
from revscoring.features.modifiers import max, sub
from revscoring.languages import french

from . import wikipedia

# Copied (2015-10-29) from:
# https://fr.wikipedia.org/wiki/Cat%C3%A9gorie:Mod%C3%A8le_pour_bibliographie
CITE_TEMPLATES = [
    r"Article",
    r"Chapitre",
    r"Jugement",
    r"Lien[ _]web",
    r"Loi",
    r"Ouvrage"
]
cite_templates = wikitext.revision.template_names_matching(
    "|".join(CITE_TEMPLATES),
    name="frwiki.revision.cite_templates")
proportion_of_templated_references = \
    cite_templates / max(wikitext.revision.ref_tags, 1)
non_templated_references = max(wikitext.revision.ref_tags - cite_templates, 0)
non_cite_templates = sub(
    wikitext.revision.templates, cite_templates,
    name="frwiki.revision.non_cite_templates"
)
infobox_templates = wikitext.revision.template_names_matching(
    r"^infobox",
    name="frwiki.revision.infobox_templates")

# Copied (2015-10-29) from:
# https://fr.wikipedia.org/wiki/Wikip%C3%A9dia:Citez_vos_sources#R.C3.A9clamation_et_contestation_de_sources
LVL1_CN_TEMPLATES = [r"Référence[ _]souhaitée", r"Citation[ _]nécessaire",
                     r"Référence[ _]à[ _]confirmer",
                     r"Référence[ _]nécessaire", r"Inédit"]
lvl1_cn_templates = wikitext.revision.template_names_matching(
    "|".join(LVL1_CN_TEMPLATES),
    name="frwiki.revision.lvl1_cn_templates")

LVL2_CN_TEMPLATES = [r"Référence[ _]insuffisante", r"Référence[ _]incomplète",
                     r"Détournement[ _]de[ _]sources",
                     r"Section[ _]à[ _]sourcer"]
lvl2_cn_templates = wikitext.revision.template_names_matching(
    "|".join(LVL2_CN_TEMPLATES),
    name="frwiki.revision.lvl2_cn_templates")

LVL3_CN_TEMPLATES = [r"Sources[ _]à[ _]lier", r"Sources[ _]obsolètes",
                     r"Référence[ _]obsolète", r"À[ _]sourcer",
                     r"Sources[ _]secondaires", r"BPV[ _]à[ _]sourcer"]
lvl3_cn_templates = wikitext.revision.template_names_matching(
    "|".join(LVL3_CN_TEMPLATES),
    name="frwiki.revision.lvl3_cn_templates")

LVL4_CN_TEMPLATES = [r"À[ _]prouver", r"Faut[ _]sourcer"]
lvl4_cn_templates = wikitext.revision.template_names_matching(
    "|".join(LVL4_CN_TEMPLATES),
    name="frwiki.revision.lvl4_cn_templates")

LVL5_CN_TEMPLATES = [r"À[ _]vérifier", r"Vérifiabilité"]
lvl5_cn_templates = wikitext.revision.template_names_matching(
    "|".join(LVL5_CN_TEMPLATES),
    name="frwiki.revision.lvl5_cn_templates")
main_article_templates = wikitext.revision.template_names_matching(
    r"Article[ _](principal|détaillé)",
    name="frwiki.main_article_templates")
date_templates = wikitext.revision.template_names_matching(
    r"date",
    name="frwiki.revision.date_templates")

# Links
category_links = wikitext.revision.wikilink_titles_matching(
    r"Category|Catégorie\:", name="frwiki.revision.category_links")
image_links = wikitext.revision.wikilink_titles_matching(
    r"File|Image|Fichier\:", name="frwiki.revision.image_links")

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
    (french.stemmed.revision.stem_chars /
     max(wikitext.revision.content_chars, 1)),
    french.dictionary.revision.dict_words / max(wikitext.revision.words, 1),
    lvl1_cn_templates,
    lvl1_cn_templates / max(wikitext.revision.content_chars, 1),
    lvl2_cn_templates,
    lvl2_cn_templates / max(wikitext.revision.content_chars, 1),
    lvl3_cn_templates,
    lvl3_cn_templates / max(wikitext.revision.content_chars, 1),
    lvl4_cn_templates,
    lvl4_cn_templates / max(wikitext.revision.content_chars, 1),
    lvl5_cn_templates,
    lvl5_cn_templates / max(wikitext.revision.content_chars, 1),
    date_templates,
    date_templates / max(wikitext.revision.content_chars, 1)
]

wp10 = local_wiki + wikipedia.article
