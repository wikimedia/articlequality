from revscoring.datasources import revision_text
from revscoring.features import Feature


def process_char_length(revision_text):
    return len(revision_text)

char_length = Feature("char_length", process_char_length, returns=int,
                      depends_on=[revision_text])
