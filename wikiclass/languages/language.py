
LANGUAGES = {}

class Language:
    """
    An abstract language class.  Provides utilities for operating on text
    of a specific language.  
    """
    def __init__(self, name, stopwords, stemmer):
        self.name = str(name)
        self.stopwords = set(stopwords)
        self.stemmer = stemmer
    
    def filter_stopwords(self, words):
        for word in words:
            if word.lower() not in self.stopwords:
                yield word
    
    def stem_words(self, words):
        for word in words:
            try:
                yield stemmer.stem(word)
            except:
                continue

def get(lang_name):
    """
    Gets a registered :class:`Language` by it's name.
    
    :Parameters:
        lang_name : str
            Language name
    """
    return LANGUAGES[lang_name]

def register(language):
    """
    Registers a new language.
    
    :Parameters:
        language : :class:`Language`
            A language to register.
    """
    LANGUAGES[language.name] = language
