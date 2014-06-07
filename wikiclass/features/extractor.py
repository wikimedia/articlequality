

class FeatureExtractor:
    
    FEATURES = NotImplemented
    
    def extract(self, *args, **kwargs):
        raise NotImplemented
