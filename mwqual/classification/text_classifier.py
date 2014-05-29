from .prediction import prediction

# Order of the columns used when _training_ the Random Forest
# classifier. Must be used when predicting otherwise they
# get mapped wrong and everything looks like a stub.
COLUMNS = ['loglength', 'logreferences', 'logpagelinks',
           'numimageslength', 'num_citetemplates',
           'lognoncitetemplates', 'num_categories',
           'infonoisescore', 'hasinfobox',
           'lvl2headings', 'lvl3headings']

# Mapping from columns used in our classifier to functions
# that calculate them given a qualmetrics.QualityFeatures object.
translations = [
	"loglength": lambda m: log2(m['byte_length']+1),
	"logreferences": lambda m: log2(m['log_references']+1)),
	"logpagelinks": lambda m: log2(m['log_pagelinks']+1)),
	"numimageslength": lambda m: float(m['imagelinks'])/float(['byte_length']),
	"num_citetemplates": lambda m: m['citetemplates'],
	"lognoncitetemplates": lambda m: log2(1 + m['noncitetemplates']),
	"num_categories": lambda m: m['num_categorylinks'],
	"infonoisescore": lambda m: m['infonoise'],
	"hasinfobox": lambda m: m['infoboxes'] >= 1,
	"lvl2headings": lambda m: m['num_headings_lvl2'],
	"lvl3headings": lambda m: m['num_headings_lvl3']
}

class Classifier:
	
	def __init__(self, model, language):
		self.model = model
		self.language = language
		
	def predict(self, text):
		
		metrics = metrics.wikitext.analyze(text)
		
		metrics['infoscore'] = metrics.infonoise.score(text, language)
		
		features = {}
		for (key, translate) in translations.iteritems():
			features[key] = [translate(metrics)]
		
		df = pd.DataFrame(features)
			
		# feat_cols used to ensure proper column order
		pred_class = self.model.predict(df.loc[:,COLUMNS])[0]
	
		
		logging.info(u'predicted class: {0}'.format(pred_class))
		pred_probs = self.model.predict_proba(df.loc[:,COLUMNS])[0]
	
		# Classes are in alphabetical sorted order, so
		# B-class has index 0, FA index 2, and so on
		probs = {
			'FA': pred_probs[2],
			'GA': pred_probs[3],
			'B': pred_probs[0],
			'C': pred_probs[1],
			'Start': pred_probs[4],
			'Stub': pred_probs[5]
		}
	
		return pred_class, probs, metrics