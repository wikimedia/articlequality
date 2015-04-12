import pickle
import sys;sys.path.insert(0, ".")
from pprint import pprint

from wikiclass.models import RFContentModel

model = RFContentModel.from_file(open("models/enwiki.rf_content.model", "rb"))

# Classifies a revision of an article based on wikitext alone
text = "An '''anachronism''' {{cite }}(from the [[Ancient Greek|Greek]] <ref ..."
assessment, probs = model.classify(text)

# Print predicted assessment class and probabilities for all classes.
pprint(("assessment", assessment))
pprint(("probs", probs))
