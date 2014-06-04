from mwqual import RFTextClassifier
from mwqual import languages

# Loads an RFTextClassifier from pickled model
rf_model = pickle.load(open("enwiki.model.pkl"))
classifier = RFTextClassifier(rf_model=rf_model,
                              language=languages.get("English"))


# Classifies a revision based on wikitext
text = "An '''anachronism''' (from the [[Ancient Greek|Greek]] ἀνά ''ana'' ..."
assessment, probs = classifier.classify(text)

# Print predicted assessment class and probabilities for all classes.
print("assessment={0}".format(assessment))
print("probs={0}".format(probs))
