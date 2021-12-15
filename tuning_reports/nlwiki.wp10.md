# Model tuning report
- Revscoring version: 2.11.1
- Features: articlequality.feature_lists.nlwiki.wp10
- Date: 2021-12-13T01:05:08.849662
- Observations: 160
- Labels: ["E", "D", "C", "B", "A"]
- Statistic: accuracy.macro (maximize)
- Folds: 5

# Top scoring configurations
| model                  |   accuracy.macro | params                                                                         |
|:-----------------------|-----------------:|:-------------------------------------------------------------------------------|
| GradientBoosting       |           0.8725 | learning_rate=0.5, max_depth=5, max_features="log2", n_estimators=300          |
| RandomForestClassifier |           0.8725 | n_estimators=160, min_samples_leaf=5, max_features="log2", criterion="entropy" |
| RandomForestClassifier |           0.87   | n_estimators=640, min_samples_leaf=5, max_features="log2", criterion="entropy" |
| RandomForestClassifier |           0.8675 | n_estimators=20, min_samples_leaf=3, max_features="log2", criterion="entropy"  |
| RandomForestClassifier |           0.865  | n_estimators=40, min_samples_leaf=5, max_features="log2", criterion="gini"     |
| RandomForestClassifier |           0.8625 | n_estimators=80, min_samples_leaf=5, max_features="log2", criterion="entropy"  |
| GradientBoosting       |           0.8625 | learning_rate=0.01, max_depth=1, max_features="log2", n_estimators=100         |
| RandomForestClassifier |           0.8625 | n_estimators=640, min_samples_leaf=7, max_features="log2", criterion="gini"    |
| RandomForestClassifier |           0.8625 | n_estimators=10, min_samples_leaf=13, max_features="log2", criterion="gini"    |
| RandomForestClassifier |           0.8625 | n_estimators=40, min_samples_leaf=13, max_features="log2", criterion="gini"    |

# Models
## GaussianNB
|   accuracy.macro | params   |
|-----------------:|:---------|
|           0.7775 |          |

## BernoulliNB
|   accuracy.macro | params   |
|-----------------:|:---------|
|           0.8375 |          |

## GradientBoosting
|   accuracy.macro | params                                                                 |
|-----------------:|:-----------------------------------------------------------------------|
|           0.8725 | learning_rate=0.5, max_depth=5, max_features="log2", n_estimators=300  |
|           0.8625 | learning_rate=0.01, max_depth=1, max_features="log2", n_estimators=100 |
|           0.86   | learning_rate=0.01, max_depth=1, max_features="log2", n_estimators=300 |
|           0.855  | learning_rate=0.01, max_depth=3, max_features="log2", n_estimators=500 |
|           0.855  | learning_rate=0.5, max_depth=3, max_features="log2", n_estimators=700  |
|           0.8525 | learning_rate=0.01, max_depth=1, max_features="log2", n_estimators=500 |
|           0.8525 | learning_rate=0.1, max_depth=1, max_features="log2", n_estimators=100  |
|           0.8525 | learning_rate=0.1, max_depth=5, max_features="log2", n_estimators=300  |
|           0.8525 | learning_rate=0.01, max_depth=5, max_features="log2", n_estimators=300 |
|           0.85   | learning_rate=0.01, max_depth=3, max_features="log2", n_estimators=700 |
|           0.85   | learning_rate=0.01, max_depth=7, max_features="log2", n_estimators=500 |
|           0.8475 | learning_rate=0.01, max_depth=1, max_features="log2", n_estimators=700 |
|           0.8475 | learning_rate=0.01, max_depth=3, max_features="log2", n_estimators=100 |
|           0.8475 | learning_rate=0.01, max_depth=5, max_features="log2", n_estimators=500 |
|           0.8475 | learning_rate=0.01, max_depth=5, max_features="log2", n_estimators=700 |
|           0.8475 | learning_rate=0.01, max_depth=7, max_features="log2", n_estimators=700 |
|           0.8475 | learning_rate=0.1, max_depth=3, max_features="log2", n_estimators=700  |
|           0.8475 | learning_rate=0.1, max_depth=5, max_features="log2", n_estimators=700  |
|           0.8475 | learning_rate=0.1, max_depth=7, max_features="log2", n_estimators=100  |
|           0.845  | learning_rate=0.1, max_depth=3, max_features="log2", n_estimators=300  |
|           0.845  | learning_rate=0.1, max_depth=3, max_features="log2", n_estimators=100  |
|           0.845  | learning_rate=0.5, max_depth=7, max_features="log2", n_estimators=500  |
|           0.8425 | learning_rate=0.01, max_depth=5, max_features="log2", n_estimators=100 |
|           0.84   | learning_rate=0.01, max_depth=3, max_features="log2", n_estimators=300 |
|           0.84   | learning_rate=0.01, max_depth=7, max_features="log2", n_estimators=100 |
|           0.84   | learning_rate=0.01, max_depth=7, max_features="log2", n_estimators=300 |
|           0.84   | learning_rate=0.1, max_depth=5, max_features="log2", n_estimators=500  |
|           0.84   | learning_rate=0.1, max_depth=7, max_features="log2", n_estimators=300  |
|           0.84   | learning_rate=0.5, max_depth=3, max_features="log2", n_estimators=500  |
|           0.8375 | learning_rate=0.1, max_depth=1, max_features="log2", n_estimators=500  |
|           0.8375 | learning_rate=0.1, max_depth=7, max_features="log2", n_estimators=500  |
|           0.8375 | learning_rate=0.1, max_depth=7, max_features="log2", n_estimators=700  |
|           0.8375 | learning_rate=0.5, max_depth=7, max_features="log2", n_estimators=700  |
|           0.835  | learning_rate=0.1, max_depth=3, max_features="log2", n_estimators=500  |
|           0.835  | learning_rate=0.1, max_depth=5, max_features="log2", n_estimators=100  |
|           0.835  | learning_rate=0.5, max_depth=5, max_features="log2", n_estimators=700  |
|           0.8325 | learning_rate=1, max_depth=3, max_features="log2", n_estimators=700    |
|           0.8325 | learning_rate=0.5, max_depth=7, max_features="log2", n_estimators=300  |
|           0.83   | learning_rate=0.1, max_depth=1, max_features="log2", n_estimators=300  |
|           0.83   | learning_rate=0.5, max_depth=1, max_features="log2", n_estimators=300  |
|           0.8275 | learning_rate=0.5, max_depth=3, max_features="log2", n_estimators=100  |
|           0.8275 | learning_rate=1, max_depth=5, max_features="log2", n_estimators=500    |
|           0.825  | learning_rate=0.1, max_depth=1, max_features="log2", n_estimators=700  |
|           0.825  | learning_rate=0.5, max_depth=3, max_features="log2", n_estimators=300  |
|           0.825  | learning_rate=0.5, max_depth=7, max_features="log2", n_estimators=100  |
|           0.825  | learning_rate=1, max_depth=1, max_features="log2", n_estimators=700    |
|           0.8225 | learning_rate=1, max_depth=3, max_features="log2", n_estimators=500    |
|           0.82   | learning_rate=0.5, max_depth=1, max_features="log2", n_estimators=700  |
|           0.8175 | learning_rate=0.5, max_depth=1, max_features="log2", n_estimators=100  |
|           0.8175 | learning_rate=0.5, max_depth=5, max_features="log2", n_estimators=100  |
|           0.8175 | learning_rate=1, max_depth=5, max_features="log2", n_estimators=300    |
|           0.815  | learning_rate=0.5, max_depth=1, max_features="log2", n_estimators=500  |
|           0.8125 | learning_rate=1, max_depth=3, max_features="log2", n_estimators=300    |
|           0.81   | learning_rate=1, max_depth=3, max_features="log2", n_estimators=100    |
|           0.81   | learning_rate=1, max_depth=1, max_features="log2", n_estimators=100    |
|           0.8075 | learning_rate=0.5, max_depth=5, max_features="log2", n_estimators=500  |
|           0.8075 | learning_rate=1, max_depth=7, max_features="log2", n_estimators=300    |
|           0.805  | learning_rate=1, max_depth=5, max_features="log2", n_estimators=700    |
|           0.8025 | learning_rate=1, max_depth=7, max_features="log2", n_estimators=700    |
|           0.8    | learning_rate=1, max_depth=5, max_features="log2", n_estimators=100    |
|           0.8    | learning_rate=1, max_depth=7, max_features="log2", n_estimators=100    |
|           0.7925 | learning_rate=1, max_depth=7, max_features="log2", n_estimators=500    |
|           0.7925 | learning_rate=1, max_depth=1, max_features="log2", n_estimators=300    |
|           0.775  | learning_rate=1, max_depth=1, max_features="log2", n_estimators=500    |

## LogisticRegression
|   accuracy.macro | params              |
|-----------------:|:--------------------|
|           0.8325 | C=1, penalty="l2"   |
|           0.83   | C=0.1, penalty="l2" |
|           0.8125 | C=10, penalty="l2"  |

## RandomForestClassifier
|   accuracy.macro | params                                                                          |
|-----------------:|:--------------------------------------------------------------------------------|
|           0.8725 | n_estimators=160, min_samples_leaf=5, max_features="log2", criterion="entropy"  |
|           0.87   | n_estimators=640, min_samples_leaf=5, max_features="log2", criterion="entropy"  |
|           0.8675 | n_estimators=20, min_samples_leaf=3, max_features="log2", criterion="entropy"   |
|           0.865  | n_estimators=40, min_samples_leaf=5, max_features="log2", criterion="gini"      |
|           0.8625 | n_estimators=80, min_samples_leaf=5, max_features="log2", criterion="entropy"   |
|           0.8625 | n_estimators=640, min_samples_leaf=7, max_features="log2", criterion="gini"     |
|           0.8625 | n_estimators=10, min_samples_leaf=13, max_features="log2", criterion="gini"     |
|           0.8625 | n_estimators=40, min_samples_leaf=13, max_features="log2", criterion="gini"     |
|           0.8625 | n_estimators=320, min_samples_leaf=13, max_features="log2", criterion="gini"    |
|           0.8625 | n_estimators=160, min_samples_leaf=7, max_features="log2", criterion="entropy"  |
|           0.86   | n_estimators=80, min_samples_leaf=3, max_features="log2", criterion="gini"      |
|           0.86   | n_estimators=10, min_samples_leaf=3, max_features="log2", criterion="entropy"   |
|           0.86   | n_estimators=320, min_samples_leaf=5, max_features="log2", criterion="entropy"  |
|           0.86   | n_estimators=40, min_samples_leaf=13, max_features="log2", criterion="entropy"  |
|           0.8575 | n_estimators=10, min_samples_leaf=7, max_features="log2", criterion="gini"      |
|           0.8575 | n_estimators=160, min_samples_leaf=13, max_features="log2", criterion="entropy" |
|           0.8575 | n_estimators=40, min_samples_leaf=3, max_features="log2", criterion="gini"      |
|           0.8575 | n_estimators=80, min_samples_leaf=7, max_features="log2", criterion="entropy"   |
|           0.8575 | n_estimators=640, min_samples_leaf=7, max_features="log2", criterion="entropy"  |
|           0.8575 | n_estimators=640, min_samples_leaf=13, max_features="log2", criterion="entropy" |
|           0.855  | n_estimators=640, min_samples_leaf=3, max_features="log2", criterion="gini"     |
|           0.855  | n_estimators=10, min_samples_leaf=5, max_features="log2", criterion="gini"      |
|           0.855  | n_estimators=640, min_samples_leaf=5, max_features="log2", criterion="gini"     |
|           0.855  | n_estimators=320, min_samples_leaf=7, max_features="log2", criterion="gini"     |
|           0.855  | n_estimators=160, min_samples_leaf=13, max_features="log2", criterion="gini"    |
|           0.855  | n_estimators=320, min_samples_leaf=7, max_features="log2", criterion="entropy"  |
|           0.855  | n_estimators=80, min_samples_leaf=13, max_features="log2", criterion="entropy"  |
|           0.855  | n_estimators=20, min_samples_leaf=3, max_features="log2", criterion="gini"      |
|           0.8525 | n_estimators=320, min_samples_leaf=3, max_features="log2", criterion="gini"     |
|           0.8525 | n_estimators=320, min_samples_leaf=5, max_features="log2", criterion="gini"     |
|           0.8525 | n_estimators=80, min_samples_leaf=7, max_features="log2", criterion="gini"      |
|           0.8525 | n_estimators=160, min_samples_leaf=7, max_features="log2", criterion="gini"     |
|           0.8525 | n_estimators=640, min_samples_leaf=13, max_features="log2", criterion="gini"    |
|           0.8525 | n_estimators=80, min_samples_leaf=3, max_features="log2", criterion="entropy"   |
|           0.8525 | n_estimators=320, min_samples_leaf=3, max_features="log2", criterion="entropy"  |
|           0.85   | n_estimators=20, min_samples_leaf=5, max_features="log2", criterion="gini"      |
|           0.85   | n_estimators=80, min_samples_leaf=5, max_features="log2", criterion="gini"      |
|           0.85   | n_estimators=40, min_samples_leaf=7, max_features="log2", criterion="gini"      |
|           0.85   | n_estimators=160, min_samples_leaf=3, max_features="log2", criterion="entropy"  |
|           0.85   | n_estimators=40, min_samples_leaf=5, max_features="log2", criterion="entropy"   |
|           0.85   | n_estimators=20, min_samples_leaf=7, max_features="log2", criterion="entropy"   |
|           0.85   | n_estimators=40, min_samples_leaf=7, max_features="log2", criterion="entropy"   |
|           0.8475 | n_estimators=160, min_samples_leaf=1, max_features="log2", criterion="entropy"  |
|           0.8475 | n_estimators=640, min_samples_leaf=3, max_features="log2", criterion="entropy"  |
|           0.8475 | n_estimators=160, min_samples_leaf=3, max_features="log2", criterion="gini"     |
|           0.8475 | n_estimators=20, min_samples_leaf=7, max_features="log2", criterion="gini"      |
|           0.8475 | n_estimators=80, min_samples_leaf=13, max_features="log2", criterion="gini"     |
|           0.8475 | n_estimators=10, min_samples_leaf=1, max_features="log2", criterion="entropy"   |
|           0.8475 | n_estimators=320, min_samples_leaf=13, max_features="log2", criterion="entropy" |
|           0.845  | n_estimators=80, min_samples_leaf=1, max_features="log2", criterion="gini"      |
|           0.845  | n_estimators=160, min_samples_leaf=5, max_features="log2", criterion="gini"     |
|           0.845  | n_estimators=20, min_samples_leaf=1, max_features="log2", criterion="entropy"   |
|           0.845  | n_estimators=640, min_samples_leaf=1, max_features="log2", criterion="entropy"  |
|           0.845  | n_estimators=20, min_samples_leaf=1, max_features="log2", criterion="gini"      |
|           0.845  | n_estimators=40, min_samples_leaf=3, max_features="log2", criterion="entropy"   |
|           0.8425 | n_estimators=160, min_samples_leaf=1, max_features="log2", criterion="gini"     |
|           0.8425 | n_estimators=320, min_samples_leaf=1, max_features="log2", criterion="gini"     |
|           0.8425 | n_estimators=640, min_samples_leaf=1, max_features="log2", criterion="gini"     |
|           0.8425 | n_estimators=320, min_samples_leaf=1, max_features="log2", criterion="entropy"  |
|           0.8425 | n_estimators=20, min_samples_leaf=13, max_features="log2", criterion="gini"     |
|           0.84   | n_estimators=40, min_samples_leaf=1, max_features="log2", criterion="gini"      |
|           0.84   | n_estimators=40, min_samples_leaf=1, max_features="log2", criterion="entropy"   |
|           0.84   | n_estimators=20, min_samples_leaf=13, max_features="log2", criterion="entropy"  |
|           0.8375 | n_estimators=80, min_samples_leaf=1, max_features="log2", criterion="entropy"   |
|           0.8375 | n_estimators=20, min_samples_leaf=5, max_features="log2", criterion="entropy"   |
|           0.8375 | n_estimators=10, min_samples_leaf=7, max_features="log2", criterion="entropy"   |
|           0.835  | n_estimators=10, min_samples_leaf=3, max_features="log2", criterion="gini"      |
|           0.8325 | n_estimators=10, min_samples_leaf=5, max_features="log2", criterion="entropy"   |
|           0.8325 | n_estimators=10, min_samples_leaf=13, max_features="log2", criterion="entropy"  |
|           0.815  | n_estimators=10, min_samples_leaf=1, max_features="log2", criterion="gini"      |

