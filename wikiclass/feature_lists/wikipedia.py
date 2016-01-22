from revscoring.features import wikitext

article = [
    wikitext.revision.chars,
    wikitext.revision.content_chars,
    wikitext.revision.ref_tags,
    wikitext.revision.ref_tags / max(wikitext.revision.content_chars, 1),
    wikitext.revision.wikilinks,
    wikitext.revision.wikilinks / max(wikitext.revision.content_chars, 1),
    wikitext.revision.external_links,
    wikitext.revision.external_links / max(wikitext.revision.content_chars, 1),
    wikitext.revision.headings_by_level(2),
    wikitext.revision.headings_by_level(2) /
        max(wikitext.revision.content_chars, 1),
    wikitext.revision.headings_by_level(3),
    wikitext.revision.headings_by_level(3) /
        max(wikitext.revision.content_chars, 1)
]
