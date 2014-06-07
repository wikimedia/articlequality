from mwqual import languages, RFTextModel

model = pickle.load(open("enwiki.rf_text_classifier.pkl"))

# Classifies a revision of an article based on wikitext alone
text = "An '''anachronism''' (from the [[Ancient Greek|Greek]] ἀνά ''ana'' ..."
assessment, probs = model.classify(text)

# Print predicted assessment class and probabilities for all classes.
print("assessment={0}".format(assessment))
print("probs={0}".format(probs))
