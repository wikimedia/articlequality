from revscoring.features import Feature
from revscoring.languages import is_stopword, stem_word

from ..datasources import content_words


def process_infonoise(is_stopword, stem_word, content_words):
    non_stopwords = (w for w in content_words if not is_stopword(w))
    non_stopword_stems = (stem_word(w) for w in non_stopwords)
    
    
    
    return sum(len(w) for w in non_stopword_stems) / \
           max(sum(len(w) for w in content_words), 1)

infonoise = Feature("infonoise", process_infonoise, returns=float,
                    depends_on=[is_stopword, stem_word, content_words])
