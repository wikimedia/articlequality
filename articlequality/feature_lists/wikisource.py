from revscoring.features import wikitext
from revscoring.features.modifiers import max
from revscoring.features.meta import aggregators
from revscoring.languages.features import RegexMatches

# TODO: This is designed for English and French
# TODO: This ends up being case insensitive even though taht doesn't
#       make any sense.
weird_regexes = [
    # capital letters in the middle of a word
    r'\w[^\WA-Z\u00c0-\u00dd]*[A-Z\u00c0-\u00dd][^\WA-Z\u00c0-\u00dd]+',
    # non-text chars in the middle of a word
    r'\w+[^\w\s]\w+',
    # not actually french quotes e.g. "<<" and ">>" as opposed to « or »
    r'<<|>>'
]
weird_word_things = RegexMatches(
    "wikitext.revision.weird_word_things", weird_regexes)

# proportion of brackets and semi-colons
nonsense_markup = aggregators.len(
    wikitext.revision.datasources.tokens_matching(r"[\{\}\[\]\|\;\\\/\:]"),
    name="wikitext.revision.nonsense_markup")

# <ref name="derp">...</ref> (in another page
# <ref following="derp" name="otherderp">...</ref>)
# TODO

# <big>,<small>,<center>,<div>,<span>,<b>,<i>,<poem>,<section>,''',''
good_tags = wikitext.revision.tag_names_matching(
    r"big|small|center|div|span|b|i|poem|section",
    name="wikitext.revision.good_tags")
expected_markup = aggregators.len(
    wikitext.revision.datasources.tokens_matching(r"'''|''"),
    name="wiktext.revision.expected_markup")

page = [
    wikitext.revision.chars,
    wikitext.revision.content_chars,
    wikitext.revision.content_chars / max(wikitext.revision.chars, 1),
    wikitext.revision.markup_chars,
    wikitext.revision.markup_chars / max(wikitext.revision.chars, 1),
    wikitext.revision.whitespace_chars,
    wikitext.revision.whitespace_chars / max(wikitext.revision.chars, 1),
    wikitext.revision.entity_chars,
    wikitext.revision.entity_chars / max(wikitext.revision.chars, 1),
    wikitext.revision.punctuation_chars,
    wikitext.revision.punctuation_chars / max(wikitext.revision.chars, 1),
    wikitext.revision.longest_repeated_char,
    wikitext.revision.numbers,
    wikitext.revision.numbers / max(wikitext.revision.words, 1),
    wikitext.revision.uppercase_words,
    wikitext.revision.uppercase_words / max(wikitext.revision.words, 1),
    wikitext.revision.longest_token,
    wikitext.revision.longest_word,
    wikitext.revision.ref_tags,
    wikitext.revision.ref_tags / max(wikitext.revision.chars, 1),
    weird_word_things.revision.matches,
    weird_word_things.revision.matches / max(wikitext.revision.chars, 1),
    nonsense_markup,
    nonsense_markup / max(wikitext.revision.chars, 1),
    good_tags,
    good_tags / max(wikitext.revision.chars, 1),
    expected_markup,
    expected_markup / max(wikitext.revision.chars, 1)
]
