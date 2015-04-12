import logging

import nltk

from ... import languages
from .wikitext import filter_markup

logger = logging.getLogger("features.metrics.infonoise")

def score(text, language=languages.get('English')):
	"""
	Calculate the InfoNoiseScore for the given parsed code
	with an associated raw wikitext length.  The definition of
	InfoNoiseScore is found in Table 1 of the appendix of
	Assessing Information Quality of a Community-Based Encyclopedia
	by Stvilia, Twidale, Smith, and Gasser (2005).
	
	:Parameters:
		text : str
			The text to generate the score for.  Usually this is wikitext with
			the markup trimmed.
		language : `mwqual.Language`
			A language to use for stemming and filtering stopwords.
	"""
	
	# Filter out wikimarkup
	clean_text = filter_markup(text)
	
	# Tokenize words
	words = nltk.tokenize.wordpunct_tokenize(clean_text)

	# Filter stopwords
	nonstops = list(language.filter_stopwords(words))

	# Stem words
	stemmed_nonstops = list(language.stem_words(nonstops))
	
	logging.info("length={l}, ".format(l=len(text)) + \
                     "words={w}, ".format(w=len(words)) + \
                     "non-stopwords={nsw}, ".format(nsw=len(nonstops)) + \
                     "stemmed words={sw}, ".format(sw=len(stemmed_nonstops)))
	
	# Calculate info noise
	# 1.0 - 
        # but some pages can have zero words (all mark-up)
	if len(text) == 0:
		return 1
	else:
		infonoise = 1.0 - (1.0*len(' '.join(stemmed_nonstops))/len(text.encode('utf-8')))
		logging.info("infonoise={0}".format(infonoise))
		return infonoise
