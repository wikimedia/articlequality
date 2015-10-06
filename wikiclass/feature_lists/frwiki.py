"""
French Wikipedia
+++++++++++++++++
"""

from revscoring.features import revision
from revscoring.features.modifiers import log, max
from revscoring.languages import french

wp10 = [
    revision.category_links,
    log(revision.content_chars + 1),
    log(revision.image_links + 1),
    revision.image_links / max(revision.content_chars, 1),
    french.revision.infonoise,
    log(revision.internal_links + 1),
    revision.internal_links / max(revision.content_chars, 1),
    revision.level_2_headings,
    revision.level_2_headings / max(revision.content_chars, 1),
    revision.level_3_headings,
    revision.level_3_headings / max(revision.content_chars, 1),
    log(revision.ref_tags + 1),
    revision.ref_tags / max(revision.content_chars, 1),
    revision.proportion_of_templated_references
]
