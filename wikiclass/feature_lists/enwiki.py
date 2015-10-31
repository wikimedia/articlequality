"""
English Wikipedia
+++++++++++++++++
"""

from revscoring.features import revision
from revscoring.features.modifiers import log, max
from revscoring.languages import english

from ..features.revision import templates_that_match

cite_templates = templates_that_match(
    r"cite", name="enwiki.revision.cite_templates")
infobox_templates = templates_that_match(
    r"infobox", name="enwiki.revision.infobox_templates")

proportion_of_templated_references = cite_templates / max(revision.ref_tags, 1)

CN_TEMPLATES = [
    r"Citation needed",
    r"Cn",
    r"Fact"
]
cn_templates = templates_that_match("|".join(CN_TEMPLATES),
                                    name="enwiki.revision.cn_templates")

who_templates = templates_that_match("Who",
                                     name="enwiki.revision.cn_templates")

main_article_templates = templates_that_match(
    "Main",
    name="enwiki.main_article_templates")

wp10 = [
    revision.category_links,
    log(revision.content_chars + 1),
    log(revision.image_links + 1),
    revision.image_links / max(revision.content_chars, 1),
    log(cite_templates + 1),
    log((revision.templates - cite_templates) + 1),
    infobox_templates,
    english.revision.infonoise,
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
    log(cn_templates + 1),
    cn_templates / max(revision.content_chars, 1),
    log(who_templates + 1),
    who_templates / max(revision.content_chars, 1),
    log(main_article_templates + 1),
    main_article_templates / max(revision.content_chars, 1)
]
"""
Based largely on work by Morten Warncke-Wang et al.[1] and with a few
improvements and extensions that Morten identified after publication.

1. Warncke-Wang, M., Cosley, D., & Riedl, J. (2013, August). Tell me more: An
   actionable quality model for wikipedia. In Proceedings of the 9th
   International Symposium on Open Collaboration (p. 8). ACM.
   http://opensym.org/wsos2013/proceedings/p0202-warncke.pdf
"""
