from .language import Language, register

import nltk

English = Language(
	"English",
	nltk.corpus.stopwords.words('english'),
	nltk.stem.SnowballStemmer('english').stem
)
register(English)
