import pickle
import sys;sys.path.insert(0, ".")

from wikiclass import RFTextModel

model = RFTextModel.from_file(open("enwiki.rf_text.model", "rb"))

# Classifies a revision of an article based on wikitext alone
text = "An '''anachronism''' (from the [[Ancient Greek|Greek]] ..."
assessment, probs = model.classify(text)

# Print predicted assessment class and probabilities for all classes.
print("assessment={0}".format(assessment))
print("probs={0}".format(probs))
