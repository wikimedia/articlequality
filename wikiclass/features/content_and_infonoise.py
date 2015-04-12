from math import log

from .extractor import TextFeatureExtractor
from .metrics import infonoise, wikitext
from ..languages import Language

import copyreg
import types

## From http://stackoverflow.com/questions/6583326/is-this-the-right-way-to-pickle-instance-methods-if-yes-why-isnt-it-in-python
def _pickle_method(method):
    func_name = method.__func__.__name__
    obj = method.__self__
    cls = method.__self__.__class__
    return _unpickle_method, (func_name, obj, cls)

def _unpickle_method(func_name, obj, cls):
    for cls in cls.mro():
        try:
            func = cls.__dict__[func_name]
        except KeyError:
            pass
        else:
            break
    return func.__get__(obj, cls)

copyreg.pickle(types.MethodType, _pickle_method, _unpickle_method)

class ContentAndInfonoise(TextFeatureExtractor):
    """
    Constructs a content and information noise feature extractor.
    
    :Parameters:
        language : :class:`~wikiclass.languages.Language`
    """
    
    FEATURES = ['logcontentlength', 'logreferences', 'logpagelinks',
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
        num_images_length = float(stats['imagelinks'])/float(stats['byte_length'])
        log_noncitetemplates = log(1+stats['noncitetemplates'], 2)
        
        features = {
            "infonoisescore": infonoisescore,
            "logcontentlength": log(1+stats['content_length'], 2),
            "logreferences": log(1+stats['references'], 2),
            "logpagelinks": log(1+stats['pagelinks'], 2),
            "numimageslength": num_images_length,
            "num_citetemplates": stats['citetemplates'],
            "lognoncitetemplates": log(1+stats['noncitetemplates'], 2),
            "num_categories": stats['categorylinks'],
            "hasinfobox": stats['infoboxes'] >= 1,
            "lvl2headings": stats['headings_lvl2'],
            "lvl3headings": stats['headings_lvl3']
        }
        
        return features
