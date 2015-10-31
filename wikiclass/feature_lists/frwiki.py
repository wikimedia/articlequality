"""
French Wikipedia
+++++++++++++++++
"""

from revscoring.features import revision
from revscoring.features.modifiers import log, max
from revscoring.languages import french

from ..features.revision import templates_that_match

# Copied (2015-10-29) from:
# https://fr.wikipedia.org/wiki/Cat%C3%A9gorie:Mod%C3%A8le_pour_bibliographie
CITE_TEMPLATES = [
    r"Article",
    r"Chapitre",
    r"Jugement",
    r"Lien web",
    r"Loi",
    r"Ouvrage"
]

cite_templates = templates_that_match(
    "|".join(CITE_TEMPLATES),
    name="frwiki.revision.cite_templates")
infobox_templates = templates_that_match(
    r"^infobox",
    name="frwiki.revision.infobox_templates")

proportion_of_templated_references = cite_templates / max(revision.ref_tags, 1)

# Copied (2015-10-29) from:
# https://fr.wikipedia.org/wiki/Wikip%C3%A9dia:Citez_vos_sources#R.C3.A9clamation_et_contestation_de_sources
LVL1_CN_TEMPLATES = [
    r"Référence souhaitée",
    r"Citation nécessaire",
    r"Référence à confirmer",
    r"Référence nécessaire",
    r"Inédit"
]
lvl1_cn_templates = templates_that_match(
    "|".join(LVL1_CN_TEMPLATES),
    name="frwiki.revision.lvl1_cn_templates")

LVL2_CN_TEMPLATES = [
    r"Référence insuffisante",
    r"Référence incomplète",
    r"Détournement de sources",
    r"Section à sourcer"
]
lvl2_cn_templates = templates_that_match(
    "|".join(LVL2_CN_TEMPLATES),
    name="frwiki.revision.lvl2_cn_templates")

LVL3_CN_TEMPLATES = [
    r"Sources à lier",
    r"Sources obsolètes",
    r"Référence obsolète",
    r"À sourcer",
    r"Sources secondaires",
    r"BPV à sourcer"
]
lvl3_cn_templates = templates_that_match(
    "|".join(LVL3_CN_TEMPLATES),
    name="frwiki.revision.lvl3_cn_templates")

LVL4_CN_TEMPLATES = [
    r"À prouver",
    r"Faut sourcer"
]
lvl4_cn_templates = templates_that_match(
    "|".join(LVL4_CN_TEMPLATES),
    name="frwiki.revision.lvl4_cn_templates")

LVL5_CN_TEMPLATES = [
    r"À vérifier",
    r"Vérifiabilité"
]
lvl5_cn_templates = templates_that_match(
    "|".join(LVL5_CN_TEMPLATES),
    name="frwiki.revision.lvl5_cn_templates")

main_article_templates = templates_that_match(
    "Article (principal|détaillé)",
    name="frwiki.main_article_templates")

date_templates = templates_that_match("date",
                                      name="frwiki.revision.date_templates")

wp10 = [
    revision.category_links,
    log(revision.content_chars + 1),
    log(revision.image_links + 1),
    revision.image_links / max(revision.content_chars, 1),
    log(cite_templates + 1),
    log((revision.templates - cite_templates) + 1),
    infobox_templates,
    french.revision.infonoise,
    log(revision.internal_links + 1),
    revision.internal_links / max(revision.content_chars, 1),
    revision.level_2_headings,
    revision.level_2_headings / max(revision.content_chars, 1),
    revision.level_3_headings,
    revision.level_3_headings / max(revision.content_chars, 1),
    log(revision.ref_tags + 1),
    revision.ref_tags / max(revision.content_chars, 1),
    log(max((revision.ref_tags - cite_templates) + 1, 1)),
    proportion_of_templated_references,
    lvl1_cn_templates / max(revision.content_chars, 1),
    lvl2_cn_templates / max(revision.content_chars, 1),
    lvl3_cn_templates / max(revision.content_chars, 1),
    lvl4_cn_templates / max(revision.content_chars, 1),
    lvl5_cn_templates / max(revision.content_chars, 1),
    main_article_templates / max(revision.content_chars, 1),
    date_templates / max(revision.content_chars, 1)
]
