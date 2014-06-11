

class FeatureExtractor:
    
    FEATURES = NotImplemented
    
    def extract(self, *args, **kwargs):
        raise NotImplementedError()

class TextFeatureExtractor:
    
    FEATURES = NotImplemented
    
    def extract(self, text):
        raise NotImplementedError()
    
