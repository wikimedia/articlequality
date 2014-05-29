# Order of the columns used when _training_ the Random Forest
# classifier. Must be used when predicting otherwise they
# get mapped wrong and everything looks like a stub.
FEATURE_ORDER = ['loglength', 'logreferences', 'logpagelinks',
                 'numimageslength', 'num_citetemplates',
                 'lognoncitetemplates', 'num_categories',
                 'infonoisescore', 'hasinfobox',
                 'lvl2headings', 'lvl3headings']

def generate_features(text, language=languages.get('en-us')):
	
	infonoise = metrics.infonoise.score(text, language)
	
	stats = metrics.wikitext.analyze(text)
	
	feature_values = {
		"infonoisescore": infonoise,
		"loglength": log2(stats['byte_length']),
		"logreferences": log2(stats['log_references']+1)),
		"logpagelinks": log2(stats['log_pagelinks']+1)),
		"numimageslength": float(stats['imagelinks'])/float(stats['byte_length']),
		"num_citetemplates": stats['citetemplates'],
		"lognoncitetemplates": log2(stats['noncitetemplates']+1),
		"num_categories": stats['num_categorylinks'],
		"hasinfobox": stats['infoboxes'] >= 1,
		"lvl2headings": stats['num_headings_lvl2'],
		"lvl3headings": stats['num_headings_lvl3']
	}
	
	features = pd.DataFrame(feature_values)
	features.reindex_axis(FEATURE_ORDER, axis=1)

def classify(features, model, language=languages.get('en-us')):
	
	# feat_cols used to ensure proper column order
	pred_class = self.model.predict(features)[0]
	pred_probs = self.model.predict_proba(features)[0]
	
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
	
	return pred_class, probs