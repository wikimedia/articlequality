import re

import mwparserfromhell as mwp
from revscoring.datasources import Datasource, revision_text


def process_parsed_revision_text(revision_text):
    return mwp.parse(revision_text)
parsed_revision_text = Datasource("parsed_revision_text",
                                  process_parsed_revision_text,
                                  depends_on=[revision_text])

def process_content(parsed_revision_text):
    return parsed_revision_text.strip_code()
content = Datasource("content", process_content,
                     depends_on=[parsed_revision_text])

WORD_RE = re.compile("\w+", re.I|re.U)

def process_content_words(content):
    return [m.group(0) for m in WORD_RE.finditer(content)]
content_words = Datasource("content_words", process_content_words,
                 depends_on=[content])

def process_headings(parsed_revision_text):
    return parsed_revision_text.filter_headings()
headings = Datasource("headings", process_headings,
                      depends_on=[parsed_revision_text])

def process_internal_links(parsed_revision_text):
    return parsed_revision_text.filter_wikilinks()
internal_links = Datasource("internal_links", process_internal_links,
                            depends_on=[parsed_revision_text])

def process_tags(parsed_revision_text):
    return parsed_revision_text.filter_tags()
tags = Datasource("tags", process_tags, depends_on=[parsed_revision_text])


def profess_templates(parsed_revision_text):
    return parsed_revision_text.filter_templates()
templates = Datasource("templates", profess_templates,
                       depends_on=[parsed_revision_text])
