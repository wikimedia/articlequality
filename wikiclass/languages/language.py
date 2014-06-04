
LANGUAGES = {}

class Language:
	
	def __init__(self, name, stopwords, stemmer):
		self.name = str(name)
		self.stopwords = set(stopwords)
		self.stemmer = stemmer
	
	def filter_stopwords(self, words):
		for word in words:
			if word.lower() not in stopwords:
				yield word
	
	def stem_words(self, stem):
		for word in words:
			try:
				yield stemmer(word)
			except:
				continue

def get(lang_name):
	return LANGUAGES[lang_name]

def register(language):
	LANGUAGES[language.name] = language
