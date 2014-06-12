import pickle
import sys;sys.path.insert(0, ".")
from pprint import pprint

from wikiclass.models import RFTextModel

model = RFTextModel.from_file(open("enwiki.rf_text.model", "rb"))

# Classifies a revision of an article based on wikitext alone
text = "An '''anachronism''' {{cite }}(from the [[Ancient Greek|Greek]] <ref ..."
assessment, probs = model.classify(text)

# Print predicted assessment class and probabilities for all classes.
pprint(("assessment", assessment))
pprint(("probs", probs))
