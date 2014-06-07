import logging

from pandas import Categorical, DataFrame

from sklearn.ensemble import RandomForestClassifier

from .. import assessments, languages
from ..features import FeatureExtractor, WikiTextAndInfonoise
from .model import TextModel

logger = logging.getLogger("models.rf_text")

class RFTextModel(TextModel):
    
    def __init__(self, rf_model, feature_extractor, assessments):
        
        if not hasattr(rf_model, "predict"):
            raise TypeError("rf_model is wrong type " + \
                            "expected {0}".format(RandomForestClassifier) + \
                            "got {0}".format(type(rf_model)))
        else:
            self.rf_model = rf_model
        
        if not isinstance(feature_extractor, FeatureExtractor):
            raise TypeError("feature_extractor is wrong type " + \
                            "expected {0}".format(FeatureExtractor) + \
                            "got {0}".format(type(feature_extractor)))
        else:
            self.feature_extractor = WikiTextAndInfonoise(language)
        
        # Assessments need to be sorted
        self.assessments = assessments
    
    
    def classify(self, text):
        
        features = self.feature_extractor.extract(text)
        features_pd = DataFrame({fn:[v] for fn, v in features.items()})
        
        pred_class = self.rf_model.predict(features)[0]
        prob_list = self.rf_model.predict_proba(features)[0]
        
        # Classes are in alphabetical sorted order, so we use the
        # sorted list of assessment classes to build up a dictionary.
        pred_probs = {self.assessments[i]:prob
                      for i, prob in enumerate(prob_list)}
        
        return pred_class, pred_probs
        
    
    def test(self, test_set):
        
        features, classes = \
            self._prepare_observations(self.feature_extractor, test_set,
                                       self.assessments)

        preds = self.rf_model.predict(features)

        return pd.crosstab(classes, preds,
                           rownames=['real assessment'],
                           colnames=['pred assessment'])
        
    
    @classmethod
    def _prepare_observations(cls, feature_extractor, text_classes, assessments):
        texts, classes = zip(*text_classes)
        
        features_lists = {fn:[] for fn in feature_extractor.FEATURES}
        
        for text in texts:
            
            features = feature_extractor.extract(text)
            assert features_lists.keys() == features.keys()
            
            for feature_name, value in features.items():
                features_lists[feature_name].append(value)
            
        
        features_pd = DataFrame(features_lists)
        # ensure proper column order
        features_pd.reindex_axis(feature_extractor.FEATURES, axis=1)
        
        # Convert classes to a categorical
        ass_map = {c:i for i, c in enumerate(assessments)} # Int map
        cl_int = [ass_map[c] for c in classes] # Convert to int
        classes_pd = DataFrame(
                {'class': Categorical(cl_int, levels=assessments)},
                index = list(range(0, len(cl_int)))) #
        
        return classes_pd, features_pd
    
    @classmethod
    def train(cls, train_set, *,
                   feature_extractor=WikiTextAndInfonoise(languages.get('English')),
                   assessments=assessments.WP10,
                   random_state=42, criterion='gini', **kwargs):
            '''
            Trains a Random Forrest classifier based on a set of texts and
            manually applied assessment classes.
            
            :Parameters:
                train_set : `iterable` of (text:`str`, class:`str`)
                    A set of texts and assessment classes to train a model over.
                feature_extractor : :class:`~wikiclass.models.TextFeatureExtractor`
                    A text feature extractor
                assessments : `list` of `str
                    A list of assessment classes ordered from highest to lowest
                    quality.
                estimators : `int`
                    ???
                samples_leaf : ???
                    ???
                random_state : `int`
                    ???
                cirterion : `str`
                    ???
            '''
            
            logger.info('Extracting features...')
            features, classes =  cls._prepare_observations(feature_extractor,
                                                           train_set,
                                                           assessments)
            
            logger.info('Constructing an RF model.')
            rf_model = RandomForestClassifier(random_state=random_state,
                                              criterion=criterion,
                                              **kwargs)
            
            
            logger.info("Training the model...")
            rf_model.fit(features, classes)
            logger.info("Model training complete.")
            
            return cls(rf_model, feature_extractor, assessments)
