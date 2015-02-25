from revscoring.scorers import ScikitLearnClassifier
from sklearn.ensemble import RandomForestClassifier

from .. import assessments, languages
from ..features import TextFeatureExtractor, WikitextAndInfonoise
from .model import ModelFile, TextModel

logger = logging.getLogger("wikiclass.scorers.rf_text")

class RFModel(ScikitLearnClassifier):
    
    def __init__(self, features, *, language=None, rf=None, **kwargs):
        
        if rf is None: rf = RandomForestClassifier(**kwargs)
        
        super().__init__(features, classifier_model=rf, language=language)
