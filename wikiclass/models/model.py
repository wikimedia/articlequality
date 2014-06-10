
from collections import namedtuple

ModelFile = namedtuple("ModelFile", ['class_name', 'args', 'kwargs'])

class Model:
    
    def __init__(self, *args, **kwargs):
        pass
    
    def train(self):
        raise NotImplementedError()
    
    def test(self):
        raise NotImplementedError()
    
    def classify(self):
        raise NotImplementedError()
    

class TextModel(Model):
    
    def train(self, text_classes):
        raise NotImplementedError()
    
    def test(self, text_classes):
        raise NotImplementedError()
    
    def classify(self, text):
        raise NotImplementedError()
