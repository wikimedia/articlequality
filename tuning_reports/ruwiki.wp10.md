# Model tuning report
- Revscoring version: 1.2.6
- Features: articlequality.feature_lists.ruwiki.wp10
- Date: 2016-06-07T17:10:13.130504
- Observations: 7961
- Labels: ["ga", "sa", "I", "III", "II", "IV", "fa"]
- Scoring: accuracy
- Folds: 5

# Top scoring configurations
| model                      |   mean(scores) |   std(scores) | params                                                                         |
|:---------------------------|---------------:|--------------:|:-------------------------------------------------------------------------------|
| GradientBoostingClassifier |          0.555 |         0.004 | max_depth=5, learning_rate=0.01, max_features="log2", n_estimators=300         |
| GradientBoostingClassifier |          0.554 |         0.004 | max_depth=5, learning_rate=0.01, max_features="log2", n_estimators=500         |
| RandomForestClassifier     |          0.553 |         0.009 | min_samples_leaf=7, criterion="entropy", n_estimators=640, max_features="log2" |
| RandomForestClassifier     |          0.553 |         0.007 | min_samples_leaf=5, criterion="entropy", n_estimators=160, max_features="log2" |
| RandomForestClassifier     |          0.552 |         0.009 | min_samples_leaf=5, criterion="gini", n_estimators=40, max_features="log2"     |
| RandomForestClassifier     |          0.551 |         0.007 | min_samples_leaf=3, criterion="gini", n_estimators=640, max_features="log2"    |
| RandomForestClassifier     |          0.551 |         0.008 | min_samples_leaf=5, criterion="gini", n_estimators=160, max_features="log2"    |
| RandomForestClassifier     |          0.551 |         0.008 | min_samples_leaf=5, criterion="entropy", n_estimators=320, max_features="log2" |
| RandomForestClassifier     |          0.551 |         0.006 | min_samples_leaf=5, criterion="gini", n_estimators=640, max_features="log2"    |
| RandomForestClassifier     |          0.551 |         0.01  | min_samples_leaf=7, criterion="entropy", n_estimators=80, max_features="log2"  |

# Models
## BernoulliNB
|   mean(scores) |   std(scores) | params   |
|---------------:|--------------:|:---------|
|          0.324 |         0.006 |          |

## LogisticRegression
|   mean(scores) |   std(scores) | params              |
|---------------:|--------------:|:--------------------|
|          0.493 |         0.01  | C=10, penalty="l1"  |
|          0.476 |         0.007 | C=1, penalty="l1"   |
|          0.472 |         0.008 | C=0.1, penalty="l1" |
|          0.44  |         0.017 | C=10, penalty="l2"  |
|          0.436 |         0.023 | C=0.1, penalty="l2" |
|          0.427 |         0.014 | C=1, penalty="l2"   |

## GradientBoostingClassifier
|   mean(scores) |   std(scores) | params                                                                 |
|---------------:|--------------:|:-----------------------------------------------------------------------|
|          0.555 |         0.004 | max_depth=5, learning_rate=0.01, max_features="log2", n_estimators=300 |
|          0.554 |         0.004 | max_depth=5, learning_rate=0.01, max_features="log2", n_estimators=500 |
|          0.551 |         0.003 | max_depth=7, learning_rate=0.01, max_features="log2", n_estimators=300 |
|          0.551 |         0.007 | max_depth=7, learning_rate=0.01, max_features="log2", n_estimators=100 |
|          0.55  |         0.004 | max_depth=5, learning_rate=0.01, max_features="log2", n_estimators=700 |
|          0.55  |         0.005 | max_depth=3, learning_rate=0.01, max_features="log2", n_estimators=700 |
|          0.547 |         0.007 | max_depth=7, learning_rate=0.01, max_features="log2", n_estimators=700 |
|          0.547 |         0.002 | max_depth=7, learning_rate=0.01, max_features="log2", n_estimators=500 |
|          0.547 |         0.006 | max_depth=3, learning_rate=0.01, max_features="log2", n_estimators=500 |
|          0.544 |         0.008 | max_depth=3, learning_rate=0.1, max_features="log2", n_estimators=100  |
|          0.543 |         0.007 | max_depth=3, learning_rate=0.1, max_features="log2", n_estimators=300  |
|          0.542 |         0.008 | max_depth=5, learning_rate=0.1, max_features="log2", n_estimators=100  |
|          0.541 |         0.008 | max_depth=1, learning_rate=0.1, max_features="log2", n_estimators=500  |
|          0.54  |         0.007 | max_depth=5, learning_rate=0.01, max_features="log2", n_estimators=100 |
|          0.54  |         0.006 | max_depth=3, learning_rate=0.01, max_features="log2", n_estimators=300 |
|          0.539 |         0.007 | max_depth=1, learning_rate=0.1, max_features="log2", n_estimators=700  |
|          0.539 |         0.008 | max_depth=1, learning_rate=0.5, max_features="log2", n_estimators=100  |
|          0.537 |         0.005 | max_depth=1, learning_rate=0.1, max_features="log2", n_estimators=300  |
|          0.535 |         0.01  | max_depth=1, learning_rate=0.5, max_features="log2", n_estimators=300  |
|          0.534 |         0.008 | max_depth=3, learning_rate=0.1, max_features="log2", n_estimators=500  |
|          0.533 |         0.009 | max_depth=7, learning_rate=0.1, max_features="log2", n_estimators=500  |
|          0.532 |         0.008 | max_depth=7, learning_rate=0.1, max_features="log2", n_estimators=100  |
|          0.532 |         0.004 | max_depth=7, learning_rate=0.1, max_features="log2", n_estimators=300  |
|          0.532 |         0.008 | max_depth=7, learning_rate=0.1, max_features="log2", n_estimators=700  |
|          0.531 |         0.009 | max_depth=1, learning_rate=0.1, max_features="log2", n_estimators=100  |
|          0.529 |         0.008 | max_depth=1, learning_rate=0.5, max_features="log2", n_estimators=500  |
|          0.528 |         0.01  | max_depth=5, learning_rate=0.1, max_features="log2", n_estimators=300  |
|          0.527 |         0.009 | max_depth=3, learning_rate=0.1, max_features="log2", n_estimators=700  |
|          0.525 |         0.004 | max_depth=5, learning_rate=0.1, max_features="log2", n_estimators=500  |
|          0.524 |         0.006 | max_depth=1, learning_rate=0.5, max_features="log2", n_estimators=700  |
|          0.524 |         0.012 | max_depth=1, learning_rate=1, max_features="log2", n_estimators=100    |
|          0.523 |         0.004 | max_depth=5, learning_rate=0.1, max_features="log2", n_estimators=700  |
|          0.522 |         0.008 | max_depth=1, learning_rate=0.01, max_features="log2", n_estimators=700 |
|          0.521 |         0.01  | max_depth=3, learning_rate=0.01, max_features="log2", n_estimators=100 |
|          0.517 |         0.004 | max_depth=1, learning_rate=1, max_features="log2", n_estimators=300    |
|          0.517 |         0.006 | max_depth=7, learning_rate=0.5, max_features="log2", n_estimators=100  |
|          0.517 |         0.012 | max_depth=1, learning_rate=1, max_features="log2", n_estimators=500    |
|          0.516 |         0.008 | max_depth=1, learning_rate=0.01, max_features="log2", n_estimators=500 |
|          0.51  |         0.012 | max_depth=5, learning_rate=0.5, max_features="log2", n_estimators=100  |
|          0.51  |         0.007 | max_depth=3, learning_rate=0.5, max_features="log2", n_estimators=100  |
|          0.507 |         0.01  | max_depth=1, learning_rate=0.01, max_features="log2", n_estimators=300 |
|          0.501 |         0.009 | max_depth=3, learning_rate=0.5, max_features="log2", n_estimators=300  |
|          0.495 |         0.019 | max_depth=3, learning_rate=0.5, max_features="log2", n_estimators=700  |
|          0.49  |         0.009 | max_depth=1, learning_rate=0.01, max_features="log2", n_estimators=100 |
|          0.479 |         0.007 | max_depth=3, learning_rate=1, max_features="log2", n_estimators=100    |
|          0.458 |         0.12  | max_depth=7, learning_rate=0.5, max_features="log2", n_estimators=500  |
|          0.452 |         0.017 | max_depth=5, learning_rate=1, max_features="log2", n_estimators=100    |
|          0.447 |         0.065 | max_depth=5, learning_rate=0.5, max_features="log2", n_estimators=300  |
|          0.444 |         0.139 | max_depth=5, learning_rate=0.5, max_features="log2", n_estimators=500  |
|          0.442 |         0.146 | max_depth=7, learning_rate=0.5, max_features="log2", n_estimators=700  |
|          0.441 |         0.148 | max_depth=1, learning_rate=1, max_features="log2", n_estimators=700    |
|          0.413 |         0.15  | max_depth=3, learning_rate=0.5, max_features="log2", n_estimators=500  |
|          0.406 |         0.137 | max_depth=7, learning_rate=0.5, max_features="log2", n_estimators=300  |
|          0.345 |         0.137 | max_depth=5, learning_rate=0.5, max_features="log2", n_estimators=700  |
|          0.325 |         0.189 | max_depth=3, learning_rate=1, max_features="log2", n_estimators=300    |
|          0.289 |         0.173 | max_depth=7, learning_rate=1, max_features="log2", n_estimators=100    |
|          0.236 |         0.134 | max_depth=3, learning_rate=1, max_features="log2", n_estimators=700    |
|          0.218 |         0.144 | max_depth=7, learning_rate=1, max_features="log2", n_estimators=500    |
|          0.215 |         0.154 | max_depth=7, learning_rate=1, max_features="log2", n_estimators=300    |
|          0.201 |         0.065 | max_depth=7, learning_rate=1, max_features="log2", n_estimators=700    |
|          0.197 |         0.156 | max_depth=3, learning_rate=1, max_features="log2", n_estimators=500    |
|          0.184 |         0.07  | max_depth=5, learning_rate=1, max_features="log2", n_estimators=700    |
|          0.178 |         0.071 | max_depth=5, learning_rate=1, max_features="log2", n_estimators=300    |
|          0.159 |         0.057 | max_depth=5, learning_rate=1, max_features="log2", n_estimators=500    |

## SVC
|   mean(scores) |   std(scores) | params                                                               |
|---------------:|--------------:|:---------------------------------------------------------------------|
|          0.292 |         0.007 | probability=true, gamma=0.0001, C=10, cache_size=1000, kernel="rbf"  |
|          0.289 |         0.005 | probability=true, gamma=0.0001, C=1, cache_size=1000, kernel="rbf"   |
|          0.184 |         0.005 | probability=true, gamma=0.001, C=10, cache_size=1000, kernel="rbf"   |
|          0.178 |         0.003 | probability=true, gamma=0.001, C=1, cache_size=1000, kernel="rbf"    |
|          0.144 |         0.001 | probability=true, gamma=0.0001, C=0.1, cache_size=1000, kernel="rbf" |
|          0.144 |         0     | probability=true, gamma=0.0, C=0.1, cache_size=1000, kernel="rbf"    |
|          0.144 |         0     | probability=true, gamma=0.001, C=0.1, cache_size=1000, kernel="rbf"  |
|          0.144 |         0.001 | probability=true, gamma=0.0, C=1, cache_size=1000, kernel="rbf"      |
|          0.143 |         0.001 | probability=true, gamma=0.0, C=10, cache_size=1000, kernel="rbf"     |

## RandomForestClassifier
|   mean(scores) |   std(scores) | params                                                                          |
|---------------:|--------------:|:--------------------------------------------------------------------------------|
|          0.553 |         0.009 | min_samples_leaf=7, criterion="entropy", n_estimators=640, max_features="log2"  |
|          0.553 |         0.007 | min_samples_leaf=5, criterion="entropy", n_estimators=160, max_features="log2"  |
|          0.552 |         0.009 | min_samples_leaf=5, criterion="gini", n_estimators=40, max_features="log2"      |
|          0.551 |         0.007 | min_samples_leaf=3, criterion="gini", n_estimators=640, max_features="log2"     |
|          0.551 |         0.008 | min_samples_leaf=5, criterion="gini", n_estimators=160, max_features="log2"     |
|          0.551 |         0.008 | min_samples_leaf=5, criterion="entropy", n_estimators=320, max_features="log2"  |
|          0.551 |         0.006 | min_samples_leaf=5, criterion="gini", n_estimators=640, max_features="log2"     |
|          0.551 |         0.01  | min_samples_leaf=7, criterion="entropy", n_estimators=80, max_features="log2"   |
|          0.551 |         0.008 | min_samples_leaf=3, criterion="entropy", n_estimators=640, max_features="log2"  |
|          0.551 |         0.008 | min_samples_leaf=3, criterion="gini", n_estimators=320, max_features="log2"     |
|          0.55  |         0.01  | min_samples_leaf=7, criterion="entropy", n_estimators=160, max_features="log2"  |
|          0.55  |         0.006 | min_samples_leaf=7, criterion="gini", n_estimators=160, max_features="log2"     |
|          0.549 |         0.006 | min_samples_leaf=5, criterion="entropy", n_estimators=640, max_features="log2"  |
|          0.549 |         0.006 | min_samples_leaf=3, criterion="entropy", n_estimators=320, max_features="log2"  |
|          0.549 |         0.004 | min_samples_leaf=3, criterion="entropy", n_estimators=160, max_features="log2"  |
|          0.549 |         0.011 | min_samples_leaf=7, criterion="gini", n_estimators=80, max_features="log2"      |
|          0.549 |         0.007 | min_samples_leaf=5, criterion="entropy", n_estimators=80, max_features="log2"   |
|          0.549 |         0.006 | min_samples_leaf=5, criterion="gini", n_estimators=320, max_features="log2"     |
|          0.549 |         0.009 | min_samples_leaf=13, criterion="entropy", n_estimators=80, max_features="log2"  |
|          0.548 |         0.007 | min_samples_leaf=7, criterion="gini", n_estimators=320, max_features="log2"     |
|          0.548 |         0.006 | min_samples_leaf=5, criterion="gini", n_estimators=80, max_features="log2"      |
|          0.548 |         0.005 | min_samples_leaf=7, criterion="gini", n_estimators=640, max_features="log2"     |
|          0.548 |         0.009 | min_samples_leaf=7, criterion="entropy", n_estimators=320, max_features="log2"  |
|          0.548 |         0.004 | min_samples_leaf=13, criterion="gini", n_estimators=160, max_features="log2"    |
|          0.547 |         0.007 | min_samples_leaf=3, criterion="gini", n_estimators=160, max_features="log2"     |
|          0.547 |         0.009 | min_samples_leaf=1, criterion="entropy", n_estimators=640, max_features="log2"  |
|          0.547 |         0.006 | min_samples_leaf=3, criterion="entropy", n_estimators=40, max_features="log2"   |
|          0.546 |         0.006 | min_samples_leaf=7, criterion="entropy", n_estimators=40, max_features="log2"   |
|          0.546 |         0.009 | min_samples_leaf=13, criterion="entropy", n_estimators=320, max_features="log2" |
|          0.546 |         0.008 | min_samples_leaf=1, criterion="entropy", n_estimators=320, max_features="log2"  |
|          0.546 |         0.009 | min_samples_leaf=13, criterion="entropy", n_estimators=640, max_features="log2" |
|          0.546 |         0.01  | min_samples_leaf=13, criterion="entropy", n_estimators=160, max_features="log2" |
|          0.546 |         0.007 | min_samples_leaf=7, criterion="gini", n_estimators=40, max_features="log2"      |
|          0.545 |         0.007 | min_samples_leaf=13, criterion="gini", n_estimators=320, max_features="log2"    |
|          0.544 |         0.007 | min_samples_leaf=3, criterion="gini", n_estimators=40, max_features="log2"      |
|          0.544 |         0.008 | min_samples_leaf=13, criterion="gini", n_estimators=640, max_features="log2"    |
|          0.544 |         0.007 | min_samples_leaf=13, criterion="entropy", n_estimators=40, max_features="log2"  |
|          0.544 |         0.007 | min_samples_leaf=1, criterion="entropy", n_estimators=80, max_features="log2"   |
|          0.543 |         0.008 | min_samples_leaf=1, criterion="gini", n_estimators=640, max_features="log2"     |
|          0.543 |         0.004 | min_samples_leaf=3, criterion="gini", n_estimators=80, max_features="log2"      |
|          0.543 |         0.005 | min_samples_leaf=5, criterion="entropy", n_estimators=40, max_features="log2"   |
|          0.543 |         0.001 | min_samples_leaf=5, criterion="gini", n_estimators=20, max_features="log2"      |
|          0.543 |         0.01  | min_samples_leaf=7, criterion="entropy", n_estimators=20, max_features="log2"   |
|          0.543 |         0.01  | min_samples_leaf=3, criterion="entropy", n_estimators=80, max_features="log2"   |
|          0.543 |         0.006 | min_samples_leaf=1, criterion="entropy", n_estimators=160, max_features="log2"  |
|          0.542 |         0.009 | min_samples_leaf=13, criterion="gini", n_estimators=80, max_features="log2"     |
|          0.542 |         0.006 | min_samples_leaf=1, criterion="gini", n_estimators=160, max_features="log2"     |
|          0.542 |         0.006 | min_samples_leaf=13, criterion="gini", n_estimators=40, max_features="log2"     |
|          0.542 |         0.005 | min_samples_leaf=1, criterion="gini", n_estimators=320, max_features="log2"     |
|          0.541 |         0.008 | min_samples_leaf=1, criterion="gini", n_estimators=80, max_features="log2"      |
|          0.541 |         0.011 | min_samples_leaf=13, criterion="entropy", n_estimators=20, max_features="log2"  |
|          0.54  |         0.008 | min_samples_leaf=7, criterion="gini", n_estimators=20, max_features="log2"      |
|          0.54  |         0.008 | min_samples_leaf=3, criterion="entropy", n_estimators=20, max_features="log2"   |
|          0.539 |         0.005 | min_samples_leaf=5, criterion="entropy", n_estimators=20, max_features="log2"   |
|          0.539 |         0.006 | min_samples_leaf=13, criterion="entropy", n_estimators=10, max_features="log2"  |
|          0.538 |         0.005 | min_samples_leaf=13, criterion="gini", n_estimators=20, max_features="log2"     |
|          0.538 |         0.01  | min_samples_leaf=5, criterion="entropy", n_estimators=10, max_features="log2"   |
|          0.538 |         0.009 | min_samples_leaf=7, criterion="gini", n_estimators=10, max_features="log2"      |
|          0.536 |         0.004 | min_samples_leaf=13, criterion="gini", n_estimators=10, max_features="log2"     |
|          0.534 |         0.009 | min_samples_leaf=1, criterion="gini", n_estimators=40, max_features="log2"      |
|          0.534 |         0.006 | min_samples_leaf=1, criterion="entropy", n_estimators=40, max_features="log2"   |
|          0.532 |         0.007 | min_samples_leaf=3, criterion="gini", n_estimators=20, max_features="log2"      |
|          0.532 |         0.008 | min_samples_leaf=7, criterion="entropy", n_estimators=10, max_features="log2"   |
|          0.53  |         0.005 | min_samples_leaf=5, criterion="gini", n_estimators=10, max_features="log2"      |
|          0.528 |         0.008 | min_samples_leaf=3, criterion="entropy", n_estimators=10, max_features="log2"   |
|          0.527 |         0.006 | min_samples_leaf=1, criterion="gini", n_estimators=20, max_features="log2"      |
|          0.526 |         0.01  | min_samples_leaf=1, criterion="entropy", n_estimators=20, max_features="log2"   |
|          0.526 |         0.005 | min_samples_leaf=3, criterion="gini", n_estimators=10, max_features="log2"      |
|          0.508 |         0.012 | min_samples_leaf=1, criterion="gini", n_estimators=10, max_features="log2"      |
|          0.504 |         0.006 | min_samples_leaf=1, criterion="entropy", n_estimators=10, max_features="log2"   |

## GaussianNB
|   mean(scores) |   std(scores) | params   |
|---------------:|--------------:|:---------|
|          0.401 |         0.009 |          |

