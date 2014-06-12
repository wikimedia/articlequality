from math import log2

from .extractor import TextFeatureExtractor
from .metrics import infonoise, wikitext
from ..languages import Language


class WikitextAndInfonoise(TextFeatureExtractor):
    """
    Constructs a wikitext and information noise feature extractor.
    
    :Parameters:
        language : :class:`~wikiclass.languages.Language`
    """
    
    FEATURES = ['loglength', 'logreferences', 'logpagelinks',
                'numimageslength', 'num_citetemplates',
                'lognoncitetemplates', 'num_categories',
                'infonoisescore', 'hasinfobox',
                'lvl2headings', 'lvl3headings']
    """
    Order of the columns
    """
    
    def __init__(self, language):
        if not isinstance(language, Language):
            raise TypeError("Expected {0}".format(Language) + \
                            "got {0}.".format(type(language)))
        
        self.language = language
    
    def extract(self, text):
        """
        Extracts a set of features from ``text``.
        """
        infonoisescore = infonoise.score(text, self.language)
        
        stats = wikitext.analyze(text)
        
        features = {
            "infonoisescore": infonoisescore,
            "loglength": log2(stats['byte_length']),
            "logreferences": log2(stats['log_references']+1),
            "logpagelinks": log2(stats['log_pagelinks']+1),
            "numimageslength": float(stats['imagelinks'])/float(stats['byte_length']),
            "num_citetemplates": stats['citetemplates'],
            "lognoncitetemplates": log2(stats['noncitetemplates']+1),
            "num_categories": stats['num_categorylinks'],
            "hasinfobox": stats['infoboxes'] >= 1,
            "lvl2headings": stats['num_headings_lvl2'],
            "lvl3headings": stats['num_headings_lvl3']
        }
        
        return features
