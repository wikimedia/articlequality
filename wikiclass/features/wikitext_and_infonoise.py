from math import log2

from .extractor import FeatureExtractor
from .metrics import infonoise, wikitext


class WikitextAndInfonoise(FeatureExtractor):
    
    FEATURES = ['loglength', 'logreferences', 'logpagelinks',
                'numimageslength', 'num_citetemplates',
                'lognoncitetemplates', 'num_categories',
                'infonoisescore', 'hasinfobox',
                'lvl2headings', 'lvl3headings']
    """
    Order of the columns used when _training_ the Random Forest
    classifier. Must be used when predicting otherwise they
    get mapped wrong and everything looks like a stub.
    """
    
    def __init__(self, language):
        self.language = language
    
    
    def extract(self, text):
        
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
