import nltk

from .language import Language, register

English = Language(
    "English",
    nltk.corpus.stopwords.words('english'),
    nltk.stem.SnowballStemmer('english')
)
register(English)
