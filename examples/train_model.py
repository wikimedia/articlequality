import pickle
import sys; sys.path.insert(0, ".")
import csv; csv.field_size_limit(sys.maxsize)

from articlequality import assessments, languages
from articlequality.models import RFTextModel
from articlequality.features import WikitextAndInfonoise

# Train and test set ("<assessment class>", "text content")
input_file = open("datasets/assessed_revisions.with_text.tsv")
train_set = []
test_set = []
for row in csv.DictReader(input_file, delimiter="\t"):
    if row['class'] == "A": continue
    if row['is_test'] == "FALSE":
        train_set.append((row['text'], row['class']))
    else:
        test_set.append((row['text'], row['class']))

model = RFTextModel.train(
    train_set,
    assessments=assessments.WP10,
    feature_extractor=WikitextAndInfonoise(languages.get('English'))
)

model.to_file(open("enwiki.rf_text.model", "wb"))
