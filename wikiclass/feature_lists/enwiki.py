"""
English Wikipedia
+++++++++++++++++
"""

from revscoring.features import revision
from revscoring.features.modifiers import log
from revscoring.languages import english

wp10 = [
    revision.category_links,
    log(revision.content_chars + 1),
    log(revision.image_links + 1),
    log(revision.cite_templates + 1),
    log((revision.templates - revision.cite_templates) + 1),
    revision.image_links / max(revision.content_chars, 1),
    revision.infobox_templates,
    english.revision.infonoise,
    log(revision.internal_links + 1),
    revision.level_2_headings,
    revision.level_3_headings,
    log(revision.ref_tags + 1),
    log(max((revision.ref_tags - revision.cite_templates) + 1, 1)),
    revision.proportion_of_templated_references
]
"""
Based largely on work by Morten Warncke-Wang et al.[1] and with a few
improvements and extensions that Morten identified after publication.

1. Warncke-Wang, M., Cosley, D., & Riedl, J. (2013, August). Tell me more: An
   actionable quality model for wikipedia. In Proceedings of the 9th
   International Symposium on Open Collaboration (p. 8). ACM.
   http://opensym.org/wsos2013/proceedings/p0202-warncke.pdf
"""
