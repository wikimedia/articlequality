import logging, pickle

from pandas import Categorical, DataFrame, crosstab

from sklearn.ensemble import RandomForestClassifier

from .. import assessments, languages
from ..features import TextFeatureExtractor, WikitextAndInfonoise
from .model import TextModel, ModelFile

logger = logging.getLogger("models.rf_text")

class RFTextModel(TextModel):
    """
    Constructs a trained RFTextModel.  It's uncommon to need to make use of
    this methid.  You probably want to call :func:`train` or
    :func:`from_file` instade.
    
    :Parameters:
        rf_model : `sklearn.ensemble.RandomForestClassifier`
            A trained RFClassifier built on features from feature_extractor
        feature_extractor : `wikiclass.features.TextFeatureExtractor`
            A feature extractor for extracting features from text
        assessments : `list` of `str`
            A sorted (lowest to highest) list of distinct quality classes
    """
    
    def __init__(self, rf_model, feature_extractor, assessments):
        
        if not hasattr(rf_model, "predict"):
            raise TypeError("rf_model is wrong type " + \
                            "expected {0} ".format(RandomForestClassifier) + \
                            "got {0}".format(type(rf_model)))
        else:
            self.rf_model = rf_model
        
        if not isinstance(feature_extractor, TextFeatureExtractor):
            raise TypeError("feature_extractor is wrong type.  " + \
                            "Expected {0} ".format(TextFeatureExtractor) + \
                            "got {0}".format(type(feature_extractor)))
        else:
            self.feature_extractor = feature_extractor
        
        # Assessments need to be sorted
        self.assessments = assessments
    
    
    def classify(self, text):
        """
        Classifies revision text.
        
        :Parameters:
            text : str
                Revision text (wikitext)
            
        :Returns:
            A tuple of two values: (<predicted_class> : `str`,
            <class_probabilities> : `dict`)
        """
        features = self.feature_extractor.extract(text)
        features_pd = DataFrame({fn:[v] for fn, v in features.items()})
        
        pred_class = self.rf_model.predict(features_pd)[0]
        prob_list = self.rf_model.predict_proba(features_pd)[0]
        
        # Classes are in alphabetical sorted order, so we use the
        # sorted list of assessment classes to build up a dictionary.
        pred_probs = {self.assessments[i]:prob
                      for i, prob in enumerate(prob_list)}
        
        return pred_class, pred_probs
        
    
    def test(self, test_set):
        """
        Runs a test set of (<class> : str, <text> : str) pairs through the model
        and returns a cross-tabulation of the resulting predicted assessment
        classes.
        """
        features, classes = \
            self._prepare_observations(self.feature_extractor, test_set,
                                       self.assessments)

        preds = self.rf_model.predict(features)

        return crosstab(classes['class'], preds,
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
        ass_int = [ass_map[c] for c in classes] # Convert to int
        classes_pd = DataFrame(
                {'class': Categorical(ass_int, levels=assessments)},
                index = list(range(1, len(ass_int)+1))) #
        
        return features_pd, classes_pd
    
    @classmethod
    def train(cls, train_set, *,
                   feature_extractor=WikitextAndInfonoise(languages.get('English')),
                   assessments=assessments.WP10,
                   criterion='entropy', **kwargs):
            """
            Constructs a trained a Random Forrest classifier based on a set of
            texts and manually applied assessment classes.
            
            :Parameters:
                train_set : `iterable` of (text:`str`, class:`str`)
                    A set of texts and assessment classes to train a model over.
                feature_extractor : :class:`~wikiclass.models.TextFeatureExtractor`
                    A text feature extractor
                assessments : `list` of `str`
                    A list of assessment classes ordered from highest to lowest
                    quality.
                citerion : `str`
                    The function to measure the quality of a split. Supported
                    criteria are "gini" for the Gini impurity and "entropy" for
                    the information gain.
                **kwargs : dict
                    Additional arguments to
                    `sklearn.ensemble.RandomForestClassifier`
            """
            
            logger.info('Extracting features...')
            features, classes =  cls._prepare_observations(feature_extractor,
                                                           train_set,
                                                           assessments)
            
            logger.info('Constructing an RF model.')
            rf_model = RandomForestClassifier(criterion=criterion,
                                              **kwargs)
            
            
            logger.info("Training the model...")
            rf_model.fit(features, classes['class'])
            logger.info("Model training complete.")
            
            return cls(rf_model, feature_extractor, assessments)
        
    def to_file(self, f):
        """
        Writes the state of the model out to a file.
        
        :Parameters:
            f : `file-like-object`
                The file to write the model to
            
        """
        args = (self.rf_model, self.feature_extractor, self.assessments)
        kwargs = {}
        model_file = ModelFile(self.__class__.__name__, args, kwargs)
        
        pickle.dump(model_file, f)
    
    @classmethod
    def from_file(cls, f):
        """
        Constructs the model in from a previously written model file.
        
        :Parameters:
            f : `file-like-object`
                The file to read the model's state from
        
        
        """
        model_file = pickle.load(f)
        class_name, args, kwargs = model_file
        
        if class_name != cls.__name__:
            raise TypeError("Loading {0}. ".format(class_name) + \
                            "Expected {0}.".format(cls.__name__))
        else:
            return cls(*args, **kwargs)
