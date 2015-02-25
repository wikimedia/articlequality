import logging

from revscoring.scorers import ScikitLearnClassifier
from sklearn.ensemble import RandomForestClassifier

logger = logging.getLogger("wikiclass.scorers.rf_text")

class RFModel(ScikitLearnClassifier):
    
    def __init__(self, features, *, language=None, rf=None, **kwargs):
        
        if 'n_estimators' not in kwargs:
            kwargs['n_estimators'] = 501
        
        if 'min_samples_leaf' not in kwargs:
            kwargs['min_samples_leaf'] = 8
        
        if 'criterion' not in kwargs:
            kwargs['criterion'] = 'entropy'
        
        if rf is None: rf = RandomForestClassifier(**kwargs)
        
        super().__init__(features, classifier_model=rf, language=language)
