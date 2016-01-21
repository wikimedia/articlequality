# Model tuning report
- Revscoring version: 1.0.0rc1
- Features: wikiclass.feature_lists.frwiki.wp10
- Date: 2016-01-21T17:31:54.615159
- Observations: 8975
- Labels: ["bd", "adq", "b", "a", "ba", "e"]
- Scoring: accuracy
- Folds: 5

# Top scoring configurations
| model                      |   mean(scores) |   std(scores) | params                                                                          |
|:---------------------------|---------------:|--------------:|:--------------------------------------------------------------------------------|
| GradientBoostingClassifier |          0.545 |         0.002 | learning_rate=0.01, max_features="log2", n_estimators=100, max_depth=7          |
| GradientBoostingClassifier |          0.544 |         0.003 | learning_rate=0.01, max_features="log2", n_estimators=300, max_depth=7          |
| GradientBoostingClassifier |          0.542 |         0.005 | learning_rate=0.01, max_features="log2", n_estimators=500, max_depth=7          |
| RandomForestClassifier     |          0.542 |         0.004 | n_estimators=320, criterion="entropy", max_features="log2", min_samples_leaf=7  |
| GradientBoostingClassifier |          0.541 |         0.006 | learning_rate=0.01, max_features="log2", n_estimators=700, max_depth=5          |
| RandomForestClassifier     |          0.541 |         0.003 | n_estimators=320, criterion="entropy", max_features="log2", min_samples_leaf=13 |
| GradientBoostingClassifier |          0.541 |         0.006 | learning_rate=0.01, max_features="log2", n_estimators=500, max_depth=5          |
| RandomForestClassifier     |          0.54  |         0.005 | n_estimators=640, criterion="entropy", max_features="log2", min_samples_leaf=7  |
| RandomForestClassifier     |          0.54  |         0.008 | n_estimators=320, criterion="entropy", max_features="log2", min_samples_leaf=5  |
| RandomForestClassifier     |          0.54  |         0.005 | n_estimators=640, criterion="gini", max_features="log2", min_samples_leaf=7     |

# Models
## GradientBoostingClassifier
|   mean(scores) |   std(scores) | params                                                                 |
|---------------:|--------------:|:-----------------------------------------------------------------------|
|          0.545 |         0.002 | learning_rate=0.01, max_features="log2", n_estimators=100, max_depth=7 |
|          0.544 |         0.003 | learning_rate=0.01, max_features="log2", n_estimators=300, max_depth=7 |
|          0.542 |         0.005 | learning_rate=0.01, max_features="log2", n_estimators=500, max_depth=7 |
|          0.541 |         0.006 | learning_rate=0.01, max_features="log2", n_estimators=700, max_depth=5 |
|          0.541 |         0.006 | learning_rate=0.01, max_features="log2", n_estimators=500, max_depth=5 |
|          0.539 |         0.006 | learning_rate=0.01, max_features="log2", n_estimators=300, max_depth=5 |
|          0.537 |         0.008 | learning_rate=0.01, max_features="log2", n_estimators=700, max_depth=7 |
|          0.535 |         0.005 | learning_rate=0.1, max_features="log2", n_estimators=100, max_depth=3  |
|          0.534 |         0.005 | learning_rate=0.01, max_features="log2", n_estimators=500, max_depth=3 |
|          0.534 |         0.009 | learning_rate=0.1, max_features="log2", n_estimators=100, max_depth=5  |
|          0.534 |         0.006 | learning_rate=0.01, max_features="log2", n_estimators=700, max_depth=3 |
|          0.533 |         0.003 | learning_rate=0.01, max_features="log2", n_estimators=100, max_depth=5 |
|          0.53  |         0.002 | learning_rate=0.1, max_features="log2", n_estimators=500, max_depth=3  |
|          0.53  |         0.007 | learning_rate=0.1, max_features="log2", n_estimators=300, max_depth=3  |
|          0.53  |         0.005 | learning_rate=0.01, max_features="log2", n_estimators=300, max_depth=3 |
|          0.529 |         0.002 | learning_rate=0.1, max_features="log2", n_estimators=700, max_depth=1  |
|          0.529 |         0.008 | learning_rate=0.1, max_features="log2", n_estimators=700, max_depth=3  |
|          0.527 |         0.008 | learning_rate=0.1, max_features="log2", n_estimators=100, max_depth=7  |
|          0.527 |         0.005 | learning_rate=0.5, max_features="log2", n_estimators=300, max_depth=1  |
|          0.526 |         0.005 | learning_rate=0.1, max_features="log2", n_estimators=500, max_depth=1  |
|          0.526 |         0.009 | learning_rate=0.1, max_features="log2", n_estimators=300, max_depth=5  |
|          0.524 |         0.008 | learning_rate=0.1, max_features="log2", n_estimators=300, max_depth=7  |
|          0.523 |         0.005 | learning_rate=0.1, max_features="log2", n_estimators=500, max_depth=7  |
|          0.523 |         0.005 | learning_rate=0.1, max_features="log2", n_estimators=700, max_depth=7  |
|          0.523 |         0.004 | learning_rate=0.1, max_features="log2", n_estimators=300, max_depth=1  |
|          0.522 |         0.007 | learning_rate=1, max_features="log2", n_estimators=300, max_depth=1    |
|          0.521 |         0.006 | learning_rate=0.1, max_features="log2", n_estimators=500, max_depth=5  |
|          0.521 |         0.006 | learning_rate=0.5, max_features="log2", n_estimators=500, max_depth=1  |
|          0.521 |         0.003 | learning_rate=0.5, max_features="log2", n_estimators=100, max_depth=1  |
|          0.52  |         0.009 | learning_rate=0.1, max_features="log2", n_estimators=700, max_depth=5  |
|          0.52  |         0.006 | learning_rate=0.01, max_features="log2", n_estimators=700, max_depth=1 |
|          0.519 |         0.003 | learning_rate=0.1, max_features="log2", n_estimators=100, max_depth=1  |
|          0.519 |         0.008 | learning_rate=0.5, max_features="log2", n_estimators=700, max_depth=1  |
|          0.518 |         0.006 | learning_rate=1, max_features="log2", n_estimators=100, max_depth=1    |
|          0.517 |         0.003 | learning_rate=0.01, max_features="log2", n_estimators=100, max_depth=3 |
|          0.517 |         0.004 | learning_rate=0.01, max_features="log2", n_estimators=500, max_depth=1 |
|          0.515 |         0.01  | learning_rate=0.5, max_features="log2", n_estimators=100, max_depth=3  |
|          0.515 |         0.011 | learning_rate=0.5, max_features="log2", n_estimators=700, max_depth=7  |
|          0.514 |         0.006 | learning_rate=1, max_features="log2", n_estimators=500, max_depth=1    |
|          0.513 |         0.009 | learning_rate=1, max_features="log2", n_estimators=700, max_depth=1    |
|          0.51  |         0.003 | learning_rate=0.01, max_features="log2", n_estimators=300, max_depth=1 |
|          0.509 |         0.003 | learning_rate=0.5, max_features="log2", n_estimators=500, max_depth=5  |
|          0.508 |         0.007 | learning_rate=0.5, max_features="log2", n_estimators=300, max_depth=5  |
|          0.506 |         0.01  | learning_rate=0.5, max_features="log2", n_estimators=300, max_depth=7  |
|          0.505 |         0.005 | learning_rate=0.5, max_features="log2", n_estimators=100, max_depth=7  |
|          0.504 |         0.009 | learning_rate=0.5, max_features="log2", n_estimators=700, max_depth=5  |
|          0.502 |         0.008 | learning_rate=0.5, max_features="log2", n_estimators=300, max_depth=3  |
|          0.501 |         0.008 | learning_rate=0.5, max_features="log2", n_estimators=500, max_depth=3  |
|          0.5   |         0.008 | learning_rate=0.5, max_features="log2", n_estimators=500, max_depth=7  |
|          0.498 |         0.007 | learning_rate=0.5, max_features="log2", n_estimators=100, max_depth=5  |
|          0.495 |         0.006 | learning_rate=0.01, max_features="log2", n_estimators=100, max_depth=1 |
|          0.494 |         0.012 | learning_rate=0.5, max_features="log2", n_estimators=700, max_depth=3  |
|          0.488 |         0.008 | learning_rate=1, max_features="log2", n_estimators=100, max_depth=3    |
|          0.47  |         0.011 | learning_rate=1, max_features="log2", n_estimators=300, max_depth=3    |
|          0.459 |         0.023 | learning_rate=1, max_features="log2", n_estimators=100, max_depth=5    |
|          0.444 |         0.091 | learning_rate=1, max_features="log2", n_estimators=300, max_depth=7    |
|          0.418 |         0.098 | learning_rate=1, max_features="log2", n_estimators=100, max_depth=7    |
|          0.392 |         0.114 | learning_rate=1, max_features="log2", n_estimators=500, max_depth=7    |
|          0.336 |         0.128 | learning_rate=1, max_features="log2", n_estimators=300, max_depth=5    |
|          0.313 |         0.138 | learning_rate=1, max_features="log2", n_estimators=500, max_depth=3    |
|          0.282 |         0.117 | learning_rate=1, max_features="log2", n_estimators=700, max_depth=7    |
|          0.274 |         0.142 | learning_rate=1, max_features="log2", n_estimators=700, max_depth=3    |
|          0.258 |         0.129 | learning_rate=1, max_features="log2", n_estimators=500, max_depth=5    |
|          0.217 |         0.061 | learning_rate=1, max_features="log2", n_estimators=700, max_depth=5    |

## SVC
|   mean(scores) |   std(scores) | params                                                               |
|---------------:|--------------:|:---------------------------------------------------------------------|
|          0.457 |         0.005 | probability=true, gamma=0.0001, C=1, cache_size=1000, kernel="rbf"   |
|          0.446 |         0.005 | probability=true, gamma=0.0001, C=10, cache_size=1000, kernel="rbf"  |
|          0.37  |         0.009 | probability=true, gamma=0.001, C=1, cache_size=1000, kernel="rbf"    |
|          0.361 |         0.006 | probability=true, gamma=0.0001, C=0.1, cache_size=1000, kernel="rbf" |
|          0.361 |         0.008 | probability=true, gamma=0.001, C=10, cache_size=1000, kernel="rbf"   |
|          0.285 |         0.006 | probability=true, gamma=0.001, C=0.1, cache_size=1000, kernel="rbf"  |
|          0.254 |         0.004 | probability=true, gamma=0.0, C=10, cache_size=1000, kernel="rbf"     |
|          0.248 |         0.005 | probability=true, gamma=0.0, C=1, cache_size=1000, kernel="rbf"      |
|          0.176 |         0.002 | probability=true, gamma=0.0, C=0.1, cache_size=1000, kernel="rbf"    |

## BernoulliNB
|   mean(scores) |   std(scores) | params   |
|---------------:|--------------:|:---------|
|          0.378 |         0.013 |          |

## LogisticRegression
|   mean(scores) |   std(scores) | params              |
|---------------:|--------------:|:--------------------|
|          0.491 |         0.006 | penalty="l1", C=10  |
|          0.471 |         0.006 | penalty="l1", C=0.1 |
|          0.471 |         0.008 | penalty="l1", C=1   |
|          0.464 |         0.007 | penalty="l2", C=0.1 |
|          0.464 |         0.01  | penalty="l2", C=1   |
|          0.462 |         0.011 | penalty="l2", C=10  |

## GaussianNB
|   mean(scores) |   std(scores) | params   |
|---------------:|--------------:|:---------|
|          0.403 |         0.006 |          |

## RandomForestClassifier
|   mean(scores) |   std(scores) | params                                                                          |
|---------------:|--------------:|:--------------------------------------------------------------------------------|
|          0.542 |         0.004 | n_estimators=320, criterion="entropy", max_features="log2", min_samples_leaf=7  |
|          0.541 |         0.003 | n_estimators=320, criterion="entropy", max_features="log2", min_samples_leaf=13 |
|          0.54  |         0.005 | n_estimators=640, criterion="entropy", max_features="log2", min_samples_leaf=7  |
|          0.54  |         0.008 | n_estimators=320, criterion="entropy", max_features="log2", min_samples_leaf=5  |
|          0.54  |         0.005 | n_estimators=640, criterion="gini", max_features="log2", min_samples_leaf=7     |
|          0.539 |         0.005 | n_estimators=40, criterion="entropy", max_features="log2", min_samples_leaf=7   |
|          0.539 |         0.004 | n_estimators=160, criterion="entropy", max_features="log2", min_samples_leaf=7  |
|          0.539 |         0.005 | n_estimators=640, criterion="gini", max_features="log2", min_samples_leaf=5     |
|          0.539 |         0.007 | n_estimators=320, criterion="entropy", max_features="log2", min_samples_leaf=3  |
|          0.539 |         0.005 | n_estimators=320, criterion="gini", max_features="log2", min_samples_leaf=3     |
|          0.538 |         0.006 | n_estimators=640, criterion="entropy", max_features="log2", min_samples_leaf=13 |
|          0.538 |         0.005 | n_estimators=640, criterion="entropy", max_features="log2", min_samples_leaf=5  |
|          0.538 |         0.01  | n_estimators=320, criterion="gini", max_features="log2", min_samples_leaf=5     |
|          0.538 |         0.006 | n_estimators=80, criterion="entropy", max_features="log2", min_samples_leaf=7   |
|          0.538 |         0.003 | n_estimators=80, criterion="gini", max_features="log2", min_samples_leaf=13     |
|          0.538 |         0.003 | n_estimators=160, criterion="entropy", max_features="log2", min_samples_leaf=13 |
|          0.538 |         0.007 | n_estimators=160, criterion="entropy", max_features="log2", min_samples_leaf=5  |
|          0.537 |         0.005 | n_estimators=80, criterion="gini", max_features="log2", min_samples_leaf=5      |
|          0.537 |         0.006 | n_estimators=640, criterion="entropy", max_features="log2", min_samples_leaf=3  |
|          0.537 |         0.006 | n_estimators=40, criterion="entropy", max_features="log2", min_samples_leaf=13  |
|          0.537 |         0.003 | n_estimators=640, criterion="gini", max_features="log2", min_samples_leaf=13    |
|          0.537 |         0.007 | n_estimators=160, criterion="gini", max_features="log2", min_samples_leaf=5     |
|          0.537 |         0.005 | n_estimators=320, criterion="gini", max_features="log2", min_samples_leaf=7     |
|          0.537 |         0.004 | n_estimators=160, criterion="gini", max_features="log2", min_samples_leaf=3     |
|          0.537 |         0.004 | n_estimators=320, criterion="gini", max_features="log2", min_samples_leaf=13    |
|          0.537 |         0.007 | n_estimators=80, criterion="entropy", max_features="log2", min_samples_leaf=3   |
|          0.537 |         0.006 | n_estimators=80, criterion="entropy", max_features="log2", min_samples_leaf=5   |
|          0.537 |         0.006 | n_estimators=40, criterion="gini", max_features="log2", min_samples_leaf=5      |
|          0.536 |         0.006 | n_estimators=160, criterion="entropy", max_features="log2", min_samples_leaf=3  |
|          0.536 |         0.005 | n_estimators=160, criterion="gini", max_features="log2", min_samples_leaf=7     |
|          0.536 |         0.001 | n_estimators=80, criterion="entropy", max_features="log2", min_samples_leaf=13  |
|          0.536 |         0.006 | n_estimators=40, criterion="gini", max_features="log2", min_samples_leaf=7      |
|          0.535 |         0.006 | n_estimators=80, criterion="gini", max_features="log2", min_samples_leaf=7      |
|          0.535 |         0.009 | n_estimators=640, criterion="gini", max_features="log2", min_samples_leaf=1     |
|          0.535 |         0.006 | n_estimators=640, criterion="gini", max_features="log2", min_samples_leaf=3     |
|          0.535 |         0.005 | n_estimators=160, criterion="gini", max_features="log2", min_samples_leaf=13    |
|          0.534 |         0.002 | n_estimators=40, criterion="entropy", max_features="log2", min_samples_leaf=5   |
|          0.533 |         0.005 | n_estimators=320, criterion="gini", max_features="log2", min_samples_leaf=1     |
|          0.533 |         0.005 | n_estimators=20, criterion="entropy", max_features="log2", min_samples_leaf=7   |
|          0.533 |         0.004 | n_estimators=20, criterion="entropy", max_features="log2", min_samples_leaf=13  |
|          0.532 |         0.006 | n_estimators=640, criterion="entropy", max_features="log2", min_samples_leaf=1  |
|          0.532 |         0.004 | n_estimators=20, criterion="gini", max_features="log2", min_samples_leaf=13     |
|          0.532 |         0.004 | n_estimators=40, criterion="gini", max_features="log2", min_samples_leaf=13     |
|          0.532 |         0.008 | n_estimators=80, criterion="gini", max_features="log2", min_samples_leaf=3      |
|          0.532 |         0.007 | n_estimators=40, criterion="entropy", max_features="log2", min_samples_leaf=3   |
|          0.531 |         0.003 | n_estimators=40, criterion="gini", max_features="log2", min_samples_leaf=3      |
|          0.531 |         0.005 | n_estimators=160, criterion="entropy", max_features="log2", min_samples_leaf=1  |
|          0.531 |         0.008 | n_estimators=320, criterion="entropy", max_features="log2", min_samples_leaf=1  |
|          0.53  |         0.004 | n_estimators=20, criterion="entropy", max_features="log2", min_samples_leaf=5   |
|          0.529 |         0.008 | n_estimators=80, criterion="gini", max_features="log2", min_samples_leaf=1      |
|          0.529 |         0.007 | n_estimators=160, criterion="gini", max_features="log2", min_samples_leaf=1     |
|          0.528 |         0.007 | n_estimators=10, criterion="gini", max_features="log2", min_samples_leaf=7      |
|          0.527 |         0.006 | n_estimators=10, criterion="gini", max_features="log2", min_samples_leaf=5      |
|          0.526 |         0.007 | n_estimators=20, criterion="gini", max_features="log2", min_samples_leaf=5      |
|          0.526 |         0.006 | n_estimators=10, criterion="entropy", max_features="log2", min_samples_leaf=13  |
|          0.525 |         0.007 | n_estimators=80, criterion="entropy", max_features="log2", min_samples_leaf=1   |
|          0.525 |         0.008 | n_estimators=20, criterion="entropy", max_features="log2", min_samples_leaf=3   |
|          0.524 |         0.007 | n_estimators=20, criterion="gini", max_features="log2", min_samples_leaf=7      |
|          0.523 |         0.007 | n_estimators=10, criterion="gini", max_features="log2", min_samples_leaf=13     |
|          0.523 |         0.006 | n_estimators=40, criterion="entropy", max_features="log2", min_samples_leaf=1   |
|          0.521 |         0.006 | n_estimators=20, criterion="gini", max_features="log2", min_samples_leaf=3      |
|          0.521 |         0.006 | n_estimators=40, criterion="gini", max_features="log2", min_samples_leaf=1      |
|          0.52  |         0.01  | n_estimators=10, criterion="entropy", max_features="log2", min_samples_leaf=5   |
|          0.519 |         0.01  | n_estimators=10, criterion="entropy", max_features="log2", min_samples_leaf=7   |
|          0.512 |         0.008 | n_estimators=10, criterion="entropy", max_features="log2", min_samples_leaf=3   |
|          0.511 |         0.005 | n_estimators=20, criterion="gini", max_features="log2", min_samples_leaf=1      |
|          0.511 |         0.007 | n_estimators=20, criterion="entropy", max_features="log2", min_samples_leaf=1   |
|          0.507 |         0.003 | n_estimators=10, criterion="gini", max_features="log2", min_samples_leaf=3      |
|          0.488 |         0.007 | n_estimators=10, criterion="entropy", max_features="log2", min_samples_leaf=1   |
|          0.485 |         0.008 | n_estimators=10, criterion="gini", max_features="log2", min_samples_leaf=1      |

