'''
class Prediction():
    """
    Results of a quality prediction.  Contains properties for
    the assessed class, probabilities for each class, as well
    as the associated quality metrics (unless asked to not
    store them).

    @param predicted_class: predicted most probably assessment class
    @type predicted_class: str

    @param class_probs: per-class probability from the random forest
    @type class_probs: dict

    @param quality_features: quality features that were used as input
    @type quality_features: qualmetrics.QualityFeatures
    """
    def __init__(self, predicted_class, class_probs,
                 quality_features):
        self.predclass = predicted_class
        self.classprobs = class_probs
        self.qualfeatures = quality_features
'''

Precition = namedtuple("Prediction", ['class', 'probabilities', 'metrics'])
