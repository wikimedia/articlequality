from revscoring.features import wikitext, modifiers

article = [
    wikitext.revision.chars,
    wikitext.revision.content_chars,
    wikitext.revision.ref_tags,
    (wikitext.revision.ref_tags /
     modifiers.max(wikitext.revision.content_chars, 1)),
    wikitext.revision.wikilinks,
    (wikitext.revision.wikilinks /
     modifiers.max(wikitext.revision.content_chars, 1)),
    wikitext.revision.external_links,
    (wikitext.revision.external_links /
     modifiers.max(wikitext.revision.content_chars, 1)),
    wikitext.revision.headings_by_level(2),
    (wikitext.revision.headings_by_level(2) /
     modifiers.max(wikitext.revision.content_chars, 1)),
    wikitext.revision.headings_by_level(3),
    (wikitext.revision.headings_by_level(3) /
     modifiers.max(wikitext.revision.content_chars, 1))
]
