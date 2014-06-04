from .model import TextModel

FEATURE_ORDER = ['loglength', 'logreferences', 'logpagelinks',
                 'numimageslength', 'num_citetemplates',
                 'lognoncitetemplates', 'num_categories',
                 'infonoisescore', 'hasinfobox',
                 'lvl2headings', 'lvl3headings']
"""
Order of the columns used when _training_ the Random Forest
classifier. Must be used when predicting otherwise they
get mapped wrong and everything looks like a stub.
"""

def append_to_dict(d, values):
    for k, v in values:
        d[k].append(v)
    
    return d


def rejigger_observations(text_classes, language):
    logging.info('Transforming observation set.')
    
    pd_features_input = autovivifying.Dict(vivifier=lambda k:[])
    pd_class_input = {'class': []}
    
    for text, class in text_classes:
        
        features = wikitext.extract(text, language)
        
        append_to_dict(pd_features_input, features)
        assert pd_features_input.keys() == features.keys()
        
        pd_class_input['class'].append(class)
    
    features_pd = pd.DataFrame(pd_features_input)
    # ensure proper column order
    features_pd.reindex_axis(FEATURE_ORDER, axis=1)
    
    class_pd = pd.DataFrame(pd_class_input)
    
    return features_pd, class_pd

class WikiTextAndInfonoise:
    
    COLUMNS = ['loglength', 'logreferences', 'logpagelinks',
               'numimageslength', 'num_citetemplates',
               'lognoncitetemplates', 'num_categories',
               'infonoisescore', 'hasinfobox',
               'lvl2headings', 'lvl3headings']
    
    def __init__(self, language):
        self.language = language
    
    def extract(self, text):
        
        infonoise = metrics.infonoise.score(text, self.language)
        
        stats = metrics.wikitext.analyze(text)
        
        features = {
            "infonoisescore": infonoise,
            "loglength": log2(stats['byte_length']),
            "logreferences": log2(stats['log_references']+1)),
            "logpagelinks": log2(stats['log_pagelinks']+1)),
            "numimageslength": float(stats['imagelinks'])/float(stats['byte_length']),
            "num_citetemplates": stats['citetemplates'],
            "lognoncitetemplates": log2(stats['noncitetemplates']+1),
            "num_categories": stats['num_categorylinks'],
            "hasinfobox": stats['infoboxes'] >= 1,
            "lvl2headings": stats['num_headings_lvl2'],
            "lvl3headings": stats['num_headings_lvl3']
        }
        
        return features

def extract_text_features(text, language):
    
    

class RFTextClassifier(TextModel):
    
    def __init__(self, rf_classifier=None, feature_extractor=WikiTextAndInfonoise(languages.get('en-us')):
        
        if rf_classifier != None and hasattr(rf_classifier, "fit"):
            self.rf_classifier = rf_classifier
        else:
            raise TypeError("rf_classifier not of expected type " + \
                            "{0}".format(repr(type(rf_classifier))))
        
        self.feature_extractor = feature_extractor
    
    
    def classify(self, text):
        if self.rf_classifier == None:
            raise Exception("Model not yet trained.")
        
        features = feature_extractor.extract(text)
        features_pd = pd.DataFrame(k:[v] for k,v in )
        # ensure proper column order
        features_pd.reindex_axis(feature_extractor.COLUMNS, axis=1)
        
        pred_class = self.model.predict(features_pd)[0]
        prob_list = self.model.predict_proba(features_pd)[0]
        
        # Classes are in alphabetical sorted order, so
        # B-class has index 0, FA index 2, and so on
        # TODO: this should be better.
        pred_probs = {
            'B': prob_list[0],
            'C': prob_list[1],
            'FA': prob_list[2],
            'GA': prob_list[3],
            'Start': prob_list[4],
            'Stub': prob_list[5]
        }
        
        return pred_class, pred_probs
        
    
    def test(self, text_classes):
        if self.rf_classifier == None:
            raise Exception("Model not yet trained.")
        
        text_features, classes = rejigger_observations(text_classes,
                                                       self.feature
                                                       self.language)

        preds = self.rf.predict(text_features)

        return pd.crosstab(classes, preds,
                           rownames=['real assessment'],
                           colnames=['pred assessment'])
        
    
    
    @class_method
    def train(cls, text_classes, estimators=Mone, samples_leaf=None,
                   random_state=42, criterion='gini',
                   language=languages.get('en-us')):
            '''
            TODO: cleanup old docs
            Train the Random Forest classifier with a given size
            and a given minimum size of leaves.

            Note: n_trees translates to n_estimators, and
                  nodesize translates to min_samples_leaf
                  from R to scikit learn's RandomForestClassifier

            @param n_trees: number of trees in the forest
            @type n_trees: int

            @param nodesize: minimum number of items (samples) in
                             a leaf (terminating node) in a tree
            @type nodesize: int
            '''
            
            text_features, classes = rejigger_observations(text_classes,
                                                           self.language)
            
            # Turn class into a factor
            # self.train_set['class'] = pd.Categorical(self.train_set['class'])
            logging.info('Training classifier')
            rf_classifier = RandomForestClassifier(n_estimators=estimators,
                                                   samples_leaf=samples_leaf,
                                                   random_state=random_state,
                                                   criterion=criterion)
            
            
            
            # Train the classifier
            rf_classifier.fit(self.train_set.loc[:,self.feat_cols],
                        self.train_set['class'])
            
            return cls(rf_classifier)
