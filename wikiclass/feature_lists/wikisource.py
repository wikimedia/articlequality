from revscoring.features import wikitext
from revscoring.features.meta import aggregators
from revscoring.languages.features import RegexMatches

# TODO: This is designed for English and French
weird_regexes = [
    # capital letters in the middle of a word
    r'\w[^\WA-Z\u00c0-\u00dd]*[A-Z\u00c0-\u00dd][^\WA-Z\u00c0-\u00dd]+',
    # non-text chars in the middle of a word
    r'\w+[^\w\s]\w+',
    # not actually french quotes e.g. "<<" and ">>" as opposed to « or »
    r'<<|>>'
]
weird_word_things = RegexMatches(
    "wikitext.revision.weird_word_things", weird_regexes, regex_flags=None)

# proportion of brackets and semi-colons
nonsense_markup = aggregators.len(
    wikitext.revision.datasource.tokens_matching(r"[\{\}\[\]\|\;\\\/\:]"),
    name="wikitext.revision.nonsense_markup")

# <ref name="derp">...</ref> (in another page
# <ref following="derp" name="otherderp">...</ref>)
# TODO

# <big>,<small>,<center>,<div>,<span>,<b>,<i>,<poem>,<section>,''',''
good_tags = wikitext.revision.tag_names_matching(
    r"big|small|center|div|span|b|i|poem|section",
    name="wikitext.revision.good_tags")
expected_markup = wikitext.revision.datasources.tokens_matching(
    r"'''|''", name="wiktext.revision.expected_markup")

page = [
    wikitext.revision.ref_tags,
    wikitext.revision.ref_tags / wikitext.revision.chars,
    weird_word_things.revision.matches,
    weird_word_things.revision.matches / wikitext.revision.chars,
    nonsense_markup,
    nonsense_markup / wikitext.revision.chars,
    good_tags,
    good_tags / wikitext.revision.chars,
    expected_markup,
    expected_markup / wikitext.revision.chars
]
