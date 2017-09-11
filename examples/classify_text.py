from pprint import pprint

import wikiclass
from revscoring import Model

scorer_model = Model.load(open('../revscoring_models/enwiki.nettrom_wp10.gradient_boosting.model', 'rb'))

# Classifies a revision of an article based on wikitext alone
text = "An '''anachronism''' {{cite }}(from the [[Ancient Greek|Greek]] <ref ..."
prediction_results = wikiclass.score(scorer_model, text)

# Print predicted assessment class and probabilities for all classes.
pprint(("assessment", prediction_results['prediction']))
pprint(("probs", prediction_results['probability']))
