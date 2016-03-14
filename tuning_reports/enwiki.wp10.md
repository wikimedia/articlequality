# Model tuning report
- Revscoring version: 1.0.0rc1
- Features: wikiclass.feature_lists.enwiki.wp10
- Date: 2016-01-21T15:49:46.989508
- Observations: 25966
- Labels: ["stub", "b", "ga", "fa", "start", "c"]
- Scoring: accuracy
- Folds: 5

# Top scoring configurations
| model                      |   mean(scores) |   std(scores) | params                                                                         |
|:---------------------------|---------------:|--------------:|:-------------------------------------------------------------------------------|
| GradientBoostingClassifier |          0.553 |         0.016 | max_features="log2", n_estimators=500, learning_rate=0.01, max_depth=7         |
| GradientBoostingClassifier |          0.553 |         0.012 | max_features="log2", n_estimators=700, learning_rate=0.01, max_depth=7         |
| GradientBoostingClassifier |          0.552 |         0.016 | max_features="log2", n_estimators=300, learning_rate=0.01, max_depth=7         |
| GradientBoostingClassifier |          0.552 |         0.018 | max_features="log2", n_estimators=500, learning_rate=0.01, max_depth=5         |
| GradientBoostingClassifier |          0.551 |         0.016 | max_features="log2", n_estimators=700, learning_rate=0.01, max_depth=5         |
| GradientBoostingClassifier |          0.551 |         0.012 | max_features="log2", n_estimators=100, learning_rate=0.1, max_depth=5          |
| RandomForestClassifier     |          0.549 |         0.016 | max_features="log2", n_estimators=640, criterion="gini", min_samples_leaf=7    |
| RandomForestClassifier     |          0.549 |         0.016 | max_features="log2", n_estimators=320, criterion="gini", min_samples_leaf=7    |
| RandomForestClassifier     |          0.549 |         0.016 | max_features="log2", n_estimators=320, criterion="entropy", min_samples_leaf=7 |
| GradientBoostingClassifier |          0.549 |         0.014 | max_features="log2", n_estimators=300, learning_rate=0.1, max_depth=3          |

# Models
## GaussianNB
|   mean(scores) |   std(scores) | params   |
|---------------:|--------------:|:---------|
|          0.397 |         0.022 |          |

## LogisticRegression
|   mean(scores) |   std(scores) | params              |
|---------------:|--------------:|:--------------------|
|          0.509 |         0.021 | penalty="l2", C=1   |
|          0.506 |         0.02  | penalty="l1", C=10  |
|          0.505 |         0.021 | penalty="l2", C=10  |
|          0.505 |         0.019 | penalty="l2", C=0.1 |
|          0.502 |         0.021 | penalty="l1", C=1   |
|          0.5   |         0.023 | penalty="l1", C=0.1 |

## GradientBoostingClassifier
|   mean(scores) |   std(scores) | params                                                                 |
|---------------:|--------------:|:-----------------------------------------------------------------------|
|          0.553 |         0.016 | max_features="log2", n_estimators=500, learning_rate=0.01, max_depth=7 |
|          0.553 |         0.012 | max_features="log2", n_estimators=700, learning_rate=0.01, max_depth=7 |
|          0.552 |         0.016 | max_features="log2", n_estimators=300, learning_rate=0.01, max_depth=7 |
|          0.552 |         0.018 | max_features="log2", n_estimators=500, learning_rate=0.01, max_depth=5 |
|          0.551 |         0.016 | max_features="log2", n_estimators=700, learning_rate=0.01, max_depth=5 |
|          0.551 |         0.012 | max_features="log2", n_estimators=100, learning_rate=0.1, max_depth=5  |
|          0.549 |         0.014 | max_features="log2", n_estimators=300, learning_rate=0.1, max_depth=3  |
|          0.549 |         0.011 | max_features="log2", n_estimators=500, learning_rate=0.1, max_depth=3  |
|          0.549 |         0.018 | max_features="log2", n_estimators=300, learning_rate=0.01, max_depth=5 |
|          0.548 |         0.01  | max_features="log2", n_estimators=700, learning_rate=0.1, max_depth=3  |
|          0.546 |         0.017 | max_features="log2", n_estimators=100, learning_rate=0.01, max_depth=7 |
|          0.546 |         0.01  | max_features="log2", n_estimators=100, learning_rate=0.1, max_depth=7  |
|          0.544 |         0.018 | max_features="log2", n_estimators=100, learning_rate=0.1, max_depth=3  |
|          0.544 |         0.02  | max_features="log2", n_estimators=700, learning_rate=0.01, max_depth=3 |
|          0.543 |         0.01  | max_features="log2", n_estimators=300, learning_rate=0.1, max_depth=5  |
|          0.542 |         0.019 | max_features="log2", n_estimators=500, learning_rate=0.01, max_depth=3 |
|          0.542 |         0.009 | max_features="log2", n_estimators=500, learning_rate=0.1, max_depth=5  |
|          0.541 |         0.017 | max_features="log2", n_estimators=700, learning_rate=0.1, max_depth=1  |
|          0.541 |         0.016 | max_features="log2", n_estimators=500, learning_rate=0.5, max_depth=1  |
|          0.539 |         0.017 | max_features="log2", n_estimators=500, learning_rate=0.1, max_depth=1  |
|          0.539 |         0.018 | max_features="log2", n_estimators=300, learning_rate=0.5, max_depth=1  |
|          0.538 |         0.018 | max_features="log2", n_estimators=300, learning_rate=0.01, max_depth=3 |
|          0.538 |         0.02  | max_features="log2", n_estimators=100, learning_rate=0.01, max_depth=5 |
|          0.537 |         0.01  | max_features="log2", n_estimators=300, learning_rate=0.1, max_depth=7  |
|          0.537 |         0.01  | max_features="log2", n_estimators=100, learning_rate=0.5, max_depth=3  |
|          0.537 |         0.02  | max_features="log2", n_estimators=300, learning_rate=0.1, max_depth=1  |
|          0.536 |         0.007 | max_features="log2", n_estimators=500, learning_rate=0.1, max_depth=7  |
|          0.536 |         0.006 | max_features="log2", n_estimators=700, learning_rate=0.1, max_depth=5  |
|          0.535 |         0.016 | max_features="log2", n_estimators=100, learning_rate=0.5, max_depth=1  |
|          0.535 |         0.012 | max_features="log2", n_estimators=500, learning_rate=1, max_depth=1    |
|          0.535 |         0.009 | max_features="log2", n_estimators=700, learning_rate=0.1, max_depth=7  |
|          0.533 |         0.016 | max_features="log2", n_estimators=100, learning_rate=1, max_depth=1    |
|          0.53  |         0.021 | max_features="log2", n_estimators=300, learning_rate=1, max_depth=1    |
|          0.529 |         0.007 | max_features="log2", n_estimators=300, learning_rate=0.5, max_depth=3  |
|          0.527 |         0.018 | max_features="log2", n_estimators=100, learning_rate=0.1, max_depth=1  |
|          0.524 |         0.03  | max_features="log2", n_estimators=700, learning_rate=0.5, max_depth=1  |
|          0.523 |         0.02  | max_features="log2", n_estimators=700, learning_rate=0.01, max_depth=1 |
|          0.523 |         0.02  | max_features="log2", n_estimators=100, learning_rate=0.01, max_depth=3 |
|          0.52  |         0.012 | max_features="log2", n_estimators=100, learning_rate=0.5, max_depth=5  |
|          0.518 |         0.009 | max_features="log2", n_estimators=500, learning_rate=0.5, max_depth=7  |
|          0.517 |         0.003 | max_features="log2", n_estimators=300, learning_rate=0.5, max_depth=7  |
|          0.517 |         0.017 | max_features="log2", n_estimators=500, learning_rate=0.01, max_depth=1 |
|          0.517 |         0.009 | max_features="log2", n_estimators=100, learning_rate=1, max_depth=3    |
|          0.516 |         0.006 | max_features="log2", n_estimators=500, learning_rate=0.5, max_depth=3  |
|          0.513 |         0.009 | max_features="log2", n_estimators=500, learning_rate=0.5, max_depth=5  |
|          0.511 |         0.007 | max_features="log2", n_estimators=100, learning_rate=0.5, max_depth=7  |
|          0.505 |         0.018 | max_features="log2", n_estimators=300, learning_rate=0.01, max_depth=1 |
|          0.505 |         0.008 | max_features="log2", n_estimators=300, learning_rate=0.5, max_depth=5  |
|          0.491 |         0.022 | max_features="log2", n_estimators=700, learning_rate=0.5, max_depth=5  |
|          0.489 |         0.016 | max_features="log2", n_estimators=100, learning_rate=0.01, max_depth=1 |
|          0.485 |         0.016 | max_features="log2", n_estimators=100, learning_rate=1, max_depth=5    |
|          0.467 |         0.013 | max_features="log2", n_estimators=100, learning_rate=1, max_depth=7    |
|          0.457 |         0.129 | max_features="log2", n_estimators=700, learning_rate=0.5, max_depth=7  |
|          0.456 |         0.097 | max_features="log2", n_estimators=300, learning_rate=1, max_depth=3    |
|          0.448 |         0.163 | max_features="log2", n_estimators=700, learning_rate=1, max_depth=1    |
|          0.423 |         0.117 | max_features="log2", n_estimators=700, learning_rate=0.5, max_depth=3  |
|          0.401 |         0.108 | max_features="log2", n_estimators=300, learning_rate=1, max_depth=5    |
|          0.319 |         0.148 | max_features="log2", n_estimators=500, learning_rate=1, max_depth=3    |
|          0.284 |         0.109 | max_features="log2", n_estimators=700, learning_rate=1, max_depth=7    |
|          0.268 |         0.114 | max_features="log2", n_estimators=700, learning_rate=1, max_depth=3    |
|          0.252 |         0.103 | max_features="log2", n_estimators=300, learning_rate=1, max_depth=7    |
|          0.252 |         0.029 | max_features="log2", n_estimators=500, learning_rate=1, max_depth=7    |
|          0.224 |         0.037 | max_features="log2", n_estimators=500, learning_rate=1, max_depth=5    |
|          0.192 |         0.074 | max_features="log2", n_estimators=700, learning_rate=1, max_depth=5    |

## BernoulliNB
|   mean(scores) |   std(scores) | params   |
|---------------:|--------------:|:---------|
|          0.366 |         0.033 |          |

## RandomForestClassifier
|   mean(scores) |   std(scores) | params                                                                          |
|---------------:|--------------:|:--------------------------------------------------------------------------------|
|          0.549 |         0.016 | max_features="log2", n_estimators=640, criterion="gini", min_samples_leaf=7     |
|          0.549 |         0.016 | max_features="log2", n_estimators=320, criterion="gini", min_samples_leaf=7     |
|          0.549 |         0.016 | max_features="log2", n_estimators=320, criterion="entropy", min_samples_leaf=7  |
|          0.549 |         0.016 | max_features="log2", n_estimators=320, criterion="gini", min_samples_leaf=5     |
|          0.549 |         0.017 | max_features="log2", n_estimators=640, criterion="gini", min_samples_leaf=13    |
|          0.548 |         0.016 | max_features="log2", n_estimators=320, criterion="entropy", min_samples_leaf=3  |
|          0.548 |         0.015 | max_features="log2", n_estimators=160, criterion="entropy", min_samples_leaf=5  |
|          0.548 |         0.016 | max_features="log2", n_estimators=160, criterion="gini", min_samples_leaf=5     |
|          0.548 |         0.016 | max_features="log2", n_estimators=640, criterion="entropy", min_samples_leaf=7  |
|          0.548 |         0.015 | max_features="log2", n_estimators=640, criterion="entropy", min_samples_leaf=5  |
|          0.548 |         0.014 | max_features="log2", n_estimators=80, criterion="entropy", min_samples_leaf=7   |
|          0.548 |         0.015 | max_features="log2", n_estimators=640, criterion="gini", min_samples_leaf=5     |
|          0.548 |         0.013 | max_features="log2", n_estimators=320, criterion="gini", min_samples_leaf=1     |
|          0.548 |         0.015 | max_features="log2", n_estimators=320, criterion="gini", min_samples_leaf=3     |
|          0.548 |         0.013 | max_features="log2", n_estimators=80, criterion="entropy", min_samples_leaf=5   |
|          0.547 |         0.013 | max_features="log2", n_estimators=640, criterion="entropy", min_samples_leaf=1  |
|          0.547 |         0.017 | max_features="log2", n_estimators=640, criterion="entropy", min_samples_leaf=13 |
|          0.547 |         0.017 | max_features="log2", n_estimators=320, criterion="entropy", min_samples_leaf=5  |
|          0.547 |         0.013 | max_features="log2", n_estimators=640, criterion="gini", min_samples_leaf=1     |
|          0.547 |         0.014 | max_features="log2", n_estimators=640, criterion="gini", min_samples_leaf=3     |
|          0.547 |         0.018 | max_features="log2", n_estimators=160, criterion="gini", min_samples_leaf=13    |
|          0.547 |         0.018 | max_features="log2", n_estimators=160, criterion="entropy", min_samples_leaf=7  |
|          0.547 |         0.017 | max_features="log2", n_estimators=320, criterion="entropy", min_samples_leaf=13 |
|          0.547 |         0.017 | max_features="log2", n_estimators=80, criterion="gini", min_samples_leaf=7      |
|          0.546 |         0.016 | max_features="log2", n_estimators=80, criterion="gini", min_samples_leaf=13     |
|          0.546 |         0.016 | max_features="log2", n_estimators=640, criterion="entropy", min_samples_leaf=3  |
|          0.546 |         0.018 | max_features="log2", n_estimators=320, criterion="gini", min_samples_leaf=13    |
|          0.546 |         0.016 | max_features="log2", n_estimators=160, criterion="entropy", min_samples_leaf=13 |
|          0.546 |         0.015 | max_features="log2", n_estimators=160, criterion="gini", min_samples_leaf=7     |
|          0.546 |         0.013 | max_features="log2", n_estimators=80, criterion="entropy", min_samples_leaf=3   |
|          0.546 |         0.016 | max_features="log2", n_estimators=80, criterion="gini", min_samples_leaf=5      |
|          0.545 |         0.014 | max_features="log2", n_estimators=160, criterion="gini", min_samples_leaf=3     |
|          0.545 |         0.016 | max_features="log2", n_estimators=40, criterion="entropy", min_samples_leaf=13  |
|          0.545 |         0.016 | max_features="log2", n_estimators=80, criterion="entropy", min_samples_leaf=13  |
|          0.545 |         0.015 | max_features="log2", n_estimators=160, criterion="entropy", min_samples_leaf=3  |
|          0.545 |         0.014 | max_features="log2", n_estimators=320, criterion="entropy", min_samples_leaf=1  |
|          0.544 |         0.013 | max_features="log2", n_estimators=160, criterion="gini", min_samples_leaf=1     |
|          0.544 |         0.016 | max_features="log2", n_estimators=40, criterion="entropy", min_samples_leaf=5   |
|          0.544 |         0.012 | max_features="log2", n_estimators=160, criterion="entropy", min_samples_leaf=1  |
|          0.544 |         0.014 | max_features="log2", n_estimators=40, criterion="gini", min_samples_leaf=5      |
|          0.543 |         0.017 | max_features="log2", n_estimators=40, criterion="gini", min_samples_leaf=13     |
|          0.543 |         0.015 | max_features="log2", n_estimators=80, criterion="gini", min_samples_leaf=3      |
|          0.543 |         0.017 | max_features="log2", n_estimators=20, criterion="gini", min_samples_leaf=13     |
|          0.543 |         0.014 | max_features="log2", n_estimators=40, criterion="entropy", min_samples_leaf=7   |
|          0.543 |         0.013 | max_features="log2", n_estimators=80, criterion="gini", min_samples_leaf=1      |
|          0.542 |         0.015 | max_features="log2", n_estimators=40, criterion="gini", min_samples_leaf=7      |
|          0.541 |         0.014 | max_features="log2", n_estimators=40, criterion="gini", min_samples_leaf=3      |
|          0.54  |         0.014 | max_features="log2", n_estimators=40, criterion="entropy", min_samples_leaf=3   |
|          0.54  |         0.014 | max_features="log2", n_estimators=80, criterion="entropy", min_samples_leaf=1   |
|          0.539 |         0.012 | max_features="log2", n_estimators=20, criterion="gini", min_samples_leaf=7      |
|          0.538 |         0.017 | max_features="log2", n_estimators=20, criterion="entropy", min_samples_leaf=13  |
|          0.537 |         0.014 | max_features="log2", n_estimators=20, criterion="entropy", min_samples_leaf=7   |
|          0.537 |         0.014 | max_features="log2", n_estimators=20, criterion="gini", min_samples_leaf=5      |
|          0.537 |         0.014 | max_features="log2", n_estimators=10, criterion="gini", min_samples_leaf=13     |
|          0.536 |         0.015 | max_features="log2", n_estimators=10, criterion="entropy", min_samples_leaf=13  |
|          0.536 |         0.013 | max_features="log2", n_estimators=20, criterion="entropy", min_samples_leaf=5   |
|          0.535 |         0.013 | max_features="log2", n_estimators=20, criterion="entropy", min_samples_leaf=3   |
|          0.535 |         0.01  | max_features="log2", n_estimators=40, criterion="gini", min_samples_leaf=1      |
|          0.534 |         0.012 | max_features="log2", n_estimators=20, criterion="gini", min_samples_leaf=3      |
|          0.533 |         0.01  | max_features="log2", n_estimators=40, criterion="entropy", min_samples_leaf=1   |
|          0.531 |         0.014 | max_features="log2", n_estimators=10, criterion="gini", min_samples_leaf=7      |
|          0.531 |         0.013 | max_features="log2", n_estimators=10, criterion="entropy", min_samples_leaf=7   |
|          0.527 |         0.011 | max_features="log2", n_estimators=10, criterion="gini", min_samples_leaf=5      |
|          0.527 |         0.013 | max_features="log2", n_estimators=10, criterion="entropy", min_samples_leaf=5   |
|          0.527 |         0.008 | max_features="log2", n_estimators=20, criterion="entropy", min_samples_leaf=1   |
|          0.525 |         0.01  | max_features="log2", n_estimators=20, criterion="gini", min_samples_leaf=1      |
|          0.524 |         0.016 | max_features="log2", n_estimators=10, criterion="gini", min_samples_leaf=3      |
|          0.522 |         0.011 | max_features="log2", n_estimators=10, criterion="entropy", min_samples_leaf=3   |
|          0.508 |         0.007 | max_features="log2", n_estimators=10, criterion="entropy", min_samples_leaf=1   |
|          0.507 |         0.01  | max_features="log2", n_estimators=10, criterion="gini", min_samples_leaf=1      |

## SVC
|   mean(scores) |   std(scores) | params                                                               |
|---------------:|--------------:|:---------------------------------------------------------------------|
|          0.47  |         0.012 | gamma=0.0001, kernel="rbf", cache_size=1000, probability=true, C=1   |
|          0.468 |         0.009 | gamma=0.0001, kernel="rbf", cache_size=1000, probability=true, C=10  |
|          0.42  |         0.01  | gamma=0.001, kernel="rbf", cache_size=1000, probability=true, C=1    |
|          0.41  |         0.018 | gamma=0.0001, kernel="rbf", cache_size=1000, probability=true, C=0.1 |
|          0.403 |         0.011 | gamma=0.001, kernel="rbf", cache_size=1000, probability=true, C=10   |
|          0.361 |         0.014 | gamma=0.001, kernel="rbf", cache_size=1000, probability=true, C=0.1  |
|          0.312 |         0.014 | gamma=0.0, kernel="rbf", cache_size=1000, probability=true, C=10     |
|          0.309 |         0.014 | gamma=0.0, kernel="rbf", cache_size=1000, probability=true, C=1      |
|          0.191 |         0.001 | gamma=0.0, kernel="rbf", cache_size=1000, probability=true, C=0.1    |

