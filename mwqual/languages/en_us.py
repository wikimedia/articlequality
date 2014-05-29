from .language import Language, register

import nltk

USEnglish = Language(
	"en-us",
	nltk.stem.SnowballStemmer('english').stem
	nltk.corpus.stopwords.words('english')
)
register(USEnglish)