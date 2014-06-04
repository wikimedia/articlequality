from mwqual import RFTextClassifier
from mwqual import languages

# Construct a new classifier
classifier = RFTextClassifier(language=languages.get('English'))

# Train and test set
train_set = [
    ("C", "An '''anachronism''' (from the [[Ancient Greek|Greek]] ..."),
    ("B", "{{Infobox|Anachronism}} An '''anachronism''' (from the  ..."),
    ("GA", "{{Infobox|Anachronism}} An '''anachronism'''<ref>Greater ...")
]
test_set = [
    ("FA", "{{Infobox|Anachronism}}{{Cleanup|Foo}} Anachronism is ... "),
    ("Stub", "Anachronism is people getting dressed up in old-timey ... ")
]

classifier.train(train_set)

results = classifier.test(test_set)

print(results)
