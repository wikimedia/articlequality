import pickle
import sys;sys.path.insert(0, ".")

from wikiclass import assessments, languages, RFTextModel
from wikiclass.features import WikitextAndInfonoise

# Train and test set ("<assessment class>", "text content")
train_set = [
    ("An '''anachronism''' (from the [[Ancient Greek|Greek]] ...", "C"),
    ("{{Infobox|Anachronism}} An '''anachronism''' (from the  ...", "B"),
    ("{{Infobox|Anachronism}} An '''anachronism'''<ref>Greater ...", "GA"),
    ("{{Infobox|Anachronism}}{{Cleanup|Foo}} Anachronism is ... ", "FA"),
    ("Anachronism the practice of getting dressed up in old-timey ... ", "Start"),
    ("Anachronism is people getting dressed up in old-timey ... ", "Stub")
]
test_set = [
    ("{{Infobox|Anachronism}}{{Cleanup|Foo}} Anachronism is ... ", "FA"),
    ("Anachronism the practice of getting dressed up in old-timey ... ", "Start"),
    ("Anachronism is people getting dressed up in old-timey ... ", "Stub")
]

model = RFTextModel.train(
    train_set,
    assessments=assessments.WP10,
    feature_extractor=WikitextAndInfonoise(languages.get('English'))
)

results = model.test(test_set)

print(results)

model.to_file(open("enwiki.rf_text.model", "wb"))
