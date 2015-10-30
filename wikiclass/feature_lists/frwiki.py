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
    "Article",
    "Chapitre",
    "Jugement",
    "Lien[ _]web",
    "Loi",
    "Ouvrage"
]

cite_templates = templates_that_match("|".join(CITE_TEMPLATES),
                                      name="frwiki.cite_templates")
infobox_templates = templates_that_match(r"^infobox",
                                         name="frwiki.infobox_templates")

proportion_of_templates_references = cite_templates / revision.ref_tags

# Copied (2015-10-29) from:
# https://fr.wikipedia.org/wiki/Wikip%C3%A9dia:Citez_vos_sources#R.C3.A9clamation_et_contestation_de_sources
LVL1_CN_TEMPLATES = [
    r"Référence[ _]souhaitée",
    r"Citation[ _]nécessaire",
    r"Référence[ _]à[ _]confirmer",
    r"Référence[ _]nécessaire",
    r"Inédit"
]
lvl1_cn_templates = templates_that_match("|".join(LVL1_CN_TEMPLATES),
                                         name="frwiki.lvl1_cn_templates")

LVL2_CN_TEMPLATES = [
    r"Référence[ _]insuffisante",
    r"Référence[ _]incomplète",
    r"Détournement[ _]de[ _]sources",
    r"Section[ _]à[ _]sourcer"
]
lvl2_cn_templates = templates_that_match("|".join(lvl2_CN_TEMPLATES),
                                         name="frwiki.lvl2_cn_templates")

LVL3_CN_TEMPLATES = [
    r"Sources[ _]à[ _]lier",
    r"Sources[ _]obsolètes",
    r"Référence[ _]obsolète",
    r"À[ _]sourcer",
    r"Sources[ _]secondaires",
    r"BPV[ _]à[ _]sourcer"
]
lvl3_cn_templates = templates_that_match("|".join(lvl3_CN_TEMPLATES),
                                         name="frwiki.lvl3_cn_templates")

LVL4_CN_TEMPLATES = [
    r"À[ _]prouver",
    r"Faut[ _]sourcer"
]
lvl4_cn_templates = templates_that_match("|".join(lvl4_CN_TEMPLATES),
                                         name="frwiki.lvl4_cn_templates")

LVL5_CN_TEMPLATES = [
    r"À[ _]vérifier",
    r"Vérifiabilité"
]
lvl5_cn_templates = templates_that_match("|".join(lvl5_CN_TEMPLATES),
                                         name="frwiki.lvl5_cn_templates")

main_article_templates = templates_that_match(
    "Article[ _](principal|détaillé)",
    name="frwiki.main_article_templates")

date_templates = templates_that_match("date", name="frwiki.date_templates")

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
    date_templates / max(revision.content_chars, 1),
]
