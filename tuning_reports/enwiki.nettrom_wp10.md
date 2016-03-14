# Model tuning report
- Revscoring version: 1.0.0rc1
- Features: wikiclass.feature_lists.enwiki.wp10
- Date: 2016-01-21T00:47:38.681426
- Observations: 29414
- Labels: ["Start", "Stub", "B", "C", "FA", "GA"]
- Scoring: accuracy
- Folds: 5

# Top scoring configurations
| model                      |   mean(scores) |   std(scores) | params                                                                         |
|:---------------------------|---------------:|--------------:|:-------------------------------------------------------------------------------|
| GradientBoostingClassifier |          0.626 |         0.006 | n_estimators=700, learning_rate=0.01, max_features="log2", max_depth=7         |
| RandomForestClassifier     |          0.625 |         0.006 | min_samples_leaf=3, criterion="entropy", max_features="log2", n_estimators=320 |
| RandomForestClassifier     |          0.624 |         0.006 | min_samples_leaf=1, criterion="gini", max_features="log2", n_estimators=640    |
| RandomForestClassifier     |          0.624 |         0.006 | min_samples_leaf=1, criterion="entropy", max_features="log2", n_estimators=640 |
| GradientBoostingClassifier |          0.623 |         0.007 | n_estimators=500, learning_rate=0.01, max_features="log2", max_depth=7         |
| RandomForestClassifier     |          0.623 |         0.007 | min_samples_leaf=1, criterion="gini", max_features="log2", n_estimators=320    |
| RandomForestClassifier     |          0.623 |         0.007 | min_samples_leaf=3, criterion="gini", max_features="log2", n_estimators=640    |
| RandomForestClassifier     |          0.623 |         0.008 | min_samples_leaf=1, criterion="entropy", max_features="log2", n_estimators=320 |
| RandomForestClassifier     |          0.623 |         0.007 | min_samples_leaf=3, criterion="gini", max_features="log2", n_estimators=320    |
| RandomForestClassifier     |          0.623 |         0.007 | min_samples_leaf=3, criterion="entropy", max_features="log2", n_estimators=640 |

# Models
## SVC
|   mean(scores) |   std(scores) | params                                                               |
|---------------:|--------------:|:---------------------------------------------------------------------|
|          0.529 |         0.005 | gamma=0.0001, C=1, probability=true, kernel="rbf", cache_size=1000   |
|          0.524 |         0.007 | gamma=0.0001, C=10, probability=true, kernel="rbf", cache_size=1000  |
|          0.5   |         0.004 | gamma=0.001, C=1, probability=true, kernel="rbf", cache_size=1000    |
|          0.489 |         0.005 | gamma=0.001, C=10, probability=true, kernel="rbf", cache_size=1000   |
|          0.478 |         0.005 | gamma=0.0001, C=0.1, probability=true, kernel="rbf", cache_size=1000 |
|          0.382 |         0.005 | gamma=0.001, C=0.1, probability=true, kernel="rbf", cache_size=1000  |
|          0.338 |         0.004 | gamma=0.0, C=10, probability=true, kernel="rbf", cache_size=1000     |
|          0.331 |         0.003 | gamma=0.0, C=1, probability=true, kernel="rbf", cache_size=1000      |
|          0.202 |         0.001 | gamma=0.0, C=0.1, probability=true, kernel="rbf", cache_size=1000    |

## RandomForestClassifier
|   mean(scores) |   std(scores) | params                                                                          |
|---------------:|--------------:|:--------------------------------------------------------------------------------|
|          0.625 |         0.006 | min_samples_leaf=3, criterion="entropy", max_features="log2", n_estimators=320  |
|          0.624 |         0.006 | min_samples_leaf=1, criterion="gini", max_features="log2", n_estimators=640     |
|          0.624 |         0.006 | min_samples_leaf=1, criterion="entropy", max_features="log2", n_estimators=640  |
|          0.623 |         0.007 | min_samples_leaf=1, criterion="gini", max_features="log2", n_estimators=320     |
|          0.623 |         0.007 | min_samples_leaf=3, criterion="gini", max_features="log2", n_estimators=640     |
|          0.623 |         0.008 | min_samples_leaf=1, criterion="entropy", max_features="log2", n_estimators=320  |
|          0.623 |         0.007 | min_samples_leaf=3, criterion="gini", max_features="log2", n_estimators=320     |
|          0.623 |         0.007 | min_samples_leaf=3, criterion="entropy", max_features="log2", n_estimators=640  |
|          0.622 |         0.006 | min_samples_leaf=1, criterion="gini", max_features="log2", n_estimators=160     |
|          0.622 |         0.006 | min_samples_leaf=3, criterion="gini", max_features="log2", n_estimators=80      |
|          0.622 |         0.006 | min_samples_leaf=3, criterion="gini", max_features="log2", n_estimators=160     |
|          0.622 |         0.007 | min_samples_leaf=1, criterion="entropy", max_features="log2", n_estimators=160  |
|          0.622 |         0.006 | min_samples_leaf=5, criterion="gini", max_features="log2", n_estimators=640     |
|          0.622 |         0.006 | min_samples_leaf=5, criterion="gini", max_features="log2", n_estimators=160     |
|          0.622 |         0.006 | min_samples_leaf=5, criterion="entropy", max_features="log2", n_estimators=320  |
|          0.621 |         0.006 | min_samples_leaf=5, criterion="entropy", max_features="log2", n_estimators=640  |
|          0.621 |         0.006 | min_samples_leaf=3, criterion="entropy", max_features="log2", n_estimators=160  |
|          0.621 |         0.006 | min_samples_leaf=5, criterion="gini", max_features="log2", n_estimators=80      |
|          0.62  |         0.008 | min_samples_leaf=3, criterion="entropy", max_features="log2", n_estimators=80   |
|          0.62  |         0.006 | min_samples_leaf=5, criterion="entropy", max_features="log2", n_estimators=160  |
|          0.62  |         0.007 | min_samples_leaf=3, criterion="entropy", max_features="log2", n_estimators=40   |
|          0.619 |         0.006 | min_samples_leaf=5, criterion="gini", max_features="log2", n_estimators=320     |
|          0.619 |         0.005 | min_samples_leaf=7, criterion="gini", max_features="log2", n_estimators=640     |
|          0.619 |         0.006 | min_samples_leaf=7, criterion="gini", max_features="log2", n_estimators=320     |
|          0.619 |         0.007 | min_samples_leaf=5, criterion="entropy", max_features="log2", n_estimators=80   |
|          0.619 |         0.007 | min_samples_leaf=7, criterion="entropy", max_features="log2", n_estimators=80   |
|          0.619 |         0.009 | min_samples_leaf=1, criterion="entropy", max_features="log2", n_estimators=80   |
|          0.619 |         0.005 | min_samples_leaf=7, criterion="gini", max_features="log2", n_estimators=160     |
|          0.618 |         0.007 | min_samples_leaf=1, criterion="gini", max_features="log2", n_estimators=80      |
|          0.618 |         0.006 | min_samples_leaf=7, criterion="entropy", max_features="log2", n_estimators=640  |
|          0.618 |         0.007 | min_samples_leaf=5, criterion="entropy", max_features="log2", n_estimators=40   |
|          0.618 |         0.007 | min_samples_leaf=7, criterion="gini", max_features="log2", n_estimators=80      |
|          0.618 |         0.005 | min_samples_leaf=7, criterion="entropy", max_features="log2", n_estimators=160  |
|          0.617 |         0.006 | min_samples_leaf=7, criterion="entropy", max_features="log2", n_estimators=320  |
|          0.617 |         0.007 | min_samples_leaf=3, criterion="gini", max_features="log2", n_estimators=40      |
|          0.616 |         0.006 | min_samples_leaf=13, criterion="entropy", max_features="log2", n_estimators=320 |
|          0.616 |         0.006 | min_samples_leaf=13, criterion="entropy", max_features="log2", n_estimators=80  |
|          0.615 |         0.005 | min_samples_leaf=13, criterion="gini", max_features="log2", n_estimators=640    |
|          0.615 |         0.007 | min_samples_leaf=7, criterion="gini", max_features="log2", n_estimators=40      |
|          0.615 |         0.006 | min_samples_leaf=13, criterion="gini", max_features="log2", n_estimators=320    |
|          0.615 |         0.006 | min_samples_leaf=13, criterion="entropy", max_features="log2", n_estimators=640 |
|          0.615 |         0.007 | min_samples_leaf=5, criterion="gini", max_features="log2", n_estimators=40      |
|          0.615 |         0.006 | min_samples_leaf=13, criterion="gini", max_features="log2", n_estimators=40     |
|          0.615 |         0.006 | min_samples_leaf=13, criterion="gini", max_features="log2", n_estimators=160    |
|          0.614 |         0.006 | min_samples_leaf=7, criterion="entropy", max_features="log2", n_estimators=40   |
|          0.614 |         0.005 | min_samples_leaf=13, criterion="entropy", max_features="log2", n_estimators=160 |
|          0.613 |         0.006 | min_samples_leaf=13, criterion="gini", max_features="log2", n_estimators=80     |
|          0.613 |         0.007 | min_samples_leaf=1, criterion="gini", max_features="log2", n_estimators=40      |
|          0.613 |         0.006 | min_samples_leaf=5, criterion="entropy", max_features="log2", n_estimators=20   |
|          0.612 |         0.006 | min_samples_leaf=1, criterion="entropy", max_features="log2", n_estimators=40   |
|          0.612 |         0.006 | min_samples_leaf=13, criterion="entropy", max_features="log2", n_estimators=40  |
|          0.611 |         0.006 | min_samples_leaf=7, criterion="entropy", max_features="log2", n_estimators=20   |
|          0.611 |         0.008 | min_samples_leaf=7, criterion="gini", max_features="log2", n_estimators=20      |
|          0.61  |         0.004 | min_samples_leaf=13, criterion="gini", max_features="log2", n_estimators=20     |
|          0.61  |         0.006 | min_samples_leaf=5, criterion="gini", max_features="log2", n_estimators=20      |
|          0.61  |         0.006 | min_samples_leaf=3, criterion="entropy", max_features="log2", n_estimators=20   |
|          0.609 |         0.01  | min_samples_leaf=3, criterion="gini", max_features="log2", n_estimators=20      |
|          0.608 |         0.007 | min_samples_leaf=13, criterion="entropy", max_features="log2", n_estimators=20  |
|          0.607 |         0.005 | min_samples_leaf=13, criterion="entropy", max_features="log2", n_estimators=10  |
|          0.605 |         0.003 | min_samples_leaf=13, criterion="gini", max_features="log2", n_estimators=10     |
|          0.605 |         0.004 | min_samples_leaf=7, criterion="gini", max_features="log2", n_estimators=10      |
|          0.605 |         0.006 | min_samples_leaf=1, criterion="entropy", max_features="log2", n_estimators=20   |
|          0.604 |         0.004 | min_samples_leaf=7, criterion="entropy", max_features="log2", n_estimators=10   |
|          0.602 |         0.006 | min_samples_leaf=3, criterion="gini", max_features="log2", n_estimators=10      |
|          0.602 |         0.008 | min_samples_leaf=5, criterion="entropy", max_features="log2", n_estimators=10   |
|          0.601 |         0.008 | min_samples_leaf=5, criterion="gini", max_features="log2", n_estimators=10      |
|          0.6   |         0.007 | min_samples_leaf=1, criterion="gini", max_features="log2", n_estimators=20      |
|          0.598 |         0.004 | min_samples_leaf=3, criterion="entropy", max_features="log2", n_estimators=10   |
|          0.586 |         0.004 | min_samples_leaf=1, criterion="entropy", max_features="log2", n_estimators=10   |
|          0.585 |         0.004 | min_samples_leaf=1, criterion="gini", max_features="log2", n_estimators=10      |

## GradientBoostingClassifier
|   mean(scores) |   std(scores) | params                                                                 |
|---------------:|--------------:|:-----------------------------------------------------------------------|
|          0.626 |         0.006 | n_estimators=700, learning_rate=0.01, max_features="log2", max_depth=7 |
|          0.623 |         0.007 | n_estimators=500, learning_rate=0.01, max_features="log2", max_depth=7 |
|          0.621 |         0.006 | n_estimators=700, learning_rate=0.01, max_features="log2", max_depth=5 |
|          0.621 |         0.006 | n_estimators=300, learning_rate=0.01, max_features="log2", max_depth=7 |
|          0.62  |         0.006 | n_estimators=100, learning_rate=0.1, max_features="log2", max_depth=5  |
|          0.619 |         0.004 | n_estimators=500, learning_rate=0.01, max_features="log2", max_depth=5 |
|          0.619 |         0.005 | n_estimators=100, learning_rate=0.1, max_features="log2", max_depth=7  |
|          0.618 |         0.004 | n_estimators=300, learning_rate=0.1, max_features="log2", max_depth=5  |
|          0.617 |         0.004 | n_estimators=300, learning_rate=0.1, max_features="log2", max_depth=3  |
|          0.616 |         0.009 | n_estimators=300, learning_rate=0.1, max_features="log2", max_depth=7  |
|          0.616 |         0.005 | n_estimators=700, learning_rate=0.1, max_features="log2", max_depth=3  |
|          0.616 |         0.007 | n_estimators=500, learning_rate=0.1, max_features="log2", max_depth=5  |
|          0.615 |         0.005 | n_estimators=500, learning_rate=0.1, max_features="log2", max_depth=3  |
|          0.615 |         0.008 | n_estimators=500, learning_rate=0.1, max_features="log2", max_depth=7  |
|          0.614 |         0.008 | n_estimators=700, learning_rate=0.1, max_features="log2", max_depth=7  |
|          0.613 |         0.006 | n_estimators=700, learning_rate=0.1, max_features="log2", max_depth=5  |
|          0.612 |         0.005 | n_estimators=300, learning_rate=0.01, max_features="log2", max_depth=5 |
|          0.611 |         0.004 | n_estimators=100, learning_rate=0.01, max_features="log2", max_depth=7 |
|          0.611 |         0.005 | n_estimators=100, learning_rate=0.1, max_features="log2", max_depth=3  |
|          0.608 |         0.004 | n_estimators=700, learning_rate=0.01, max_features="log2", max_depth=3 |
|          0.605 |         0.004 | n_estimators=500, learning_rate=0.01, max_features="log2", max_depth=3 |
|          0.605 |         0.003 | n_estimators=500, learning_rate=0.5, max_features="log2", max_depth=1  |
|          0.604 |         0.004 | n_estimators=100, learning_rate=0.5, max_features="log2", max_depth=3  |
|          0.603 |         0.004 | n_estimators=700, learning_rate=0.1, max_features="log2", max_depth=1  |
|          0.602 |         0.004 | n_estimators=500, learning_rate=0.1, max_features="log2", max_depth=1  |
|          0.602 |         0.004 | n_estimators=700, learning_rate=0.5, max_features="log2", max_depth=1  |
|          0.601 |         0.004 | n_estimators=300, learning_rate=0.5, max_features="log2", max_depth=1  |
|          0.599 |         0.005 | n_estimators=100, learning_rate=0.01, max_features="log2", max_depth=5 |
|          0.599 |         0.004 | n_estimators=100, learning_rate=0.5, max_features="log2", max_depth=1  |
|          0.599 |         0.005 | n_estimators=300, learning_rate=0.1, max_features="log2", max_depth=1  |
|          0.598 |         0.005 | n_estimators=700, learning_rate=0.5, max_features="log2", max_depth=7  |
|          0.598 |         0.004 | n_estimators=500, learning_rate=1, max_features="log2", max_depth=1    |
|          0.598 |         0.007 | n_estimators=500, learning_rate=0.5, max_features="log2", max_depth=7  |
|          0.597 |         0.005 | n_estimators=300, learning_rate=0.01, max_features="log2", max_depth=3 |
|          0.597 |         0.008 | n_estimators=300, learning_rate=0.5, max_features="log2", max_depth=7  |
|          0.596 |         0.008 | n_estimators=300, learning_rate=1, max_features="log2", max_depth=1    |
|          0.596 |         0.01  | n_estimators=700, learning_rate=1, max_features="log2", max_depth=1    |
|          0.595 |         0.01  | n_estimators=300, learning_rate=0.5, max_features="log2", max_depth=3  |
|          0.595 |         0.006 | n_estimators=500, learning_rate=0.5, max_features="log2", max_depth=3  |
|          0.595 |         0.008 | n_estimators=100, learning_rate=1, max_features="log2", max_depth=1    |
|          0.593 |         0.007 | n_estimators=100, learning_rate=0.5, max_features="log2", max_depth=5  |
|          0.591 |         0.007 | n_estimators=100, learning_rate=0.5, max_features="log2", max_depth=7  |
|          0.589 |         0.013 | n_estimators=500, learning_rate=0.5, max_features="log2", max_depth=5  |
|          0.584 |         0.015 | n_estimators=300, learning_rate=0.5, max_features="log2", max_depth=5  |
|          0.584 |         0.004 | n_estimators=100, learning_rate=1, max_features="log2", max_depth=3    |
|          0.582 |         0.004 | n_estimators=100, learning_rate=0.1, max_features="log2", max_depth=1  |
|          0.579 |         0.004 | n_estimators=100, learning_rate=0.01, max_features="log2", max_depth=3 |
|          0.578 |         0.005 | n_estimators=700, learning_rate=0.01, max_features="log2", max_depth=1 |
|          0.573 |         0.006 | n_estimators=500, learning_rate=0.01, max_features="log2", max_depth=1 |
|          0.566 |         0.029 | n_estimators=700, learning_rate=0.5, max_features="log2", max_depth=3  |
|          0.564 |         0.004 | n_estimators=100, learning_rate=1, max_features="log2", max_depth=5    |
|          0.558 |         0.005 | n_estimators=300, learning_rate=0.01, max_features="log2", max_depth=1 |
|          0.534 |         0.009 | n_estimators=100, learning_rate=1, max_features="log2", max_depth=7    |
|          0.533 |         0.007 | n_estimators=100, learning_rate=0.01, max_features="log2", max_depth=1 |
|          0.529 |         0.037 | n_estimators=300, learning_rate=1, max_features="log2", max_depth=5    |
|          0.522 |         0.072 | n_estimators=300, learning_rate=1, max_features="log2", max_depth=3    |
|          0.499 |         0.144 | n_estimators=700, learning_rate=0.5, max_features="log2", max_depth=5  |
|          0.388 |         0.141 | n_estimators=500, learning_rate=1, max_features="log2", max_depth=3    |
|          0.372 |         0.105 | n_estimators=300, learning_rate=1, max_features="log2", max_depth=7    |
|          0.36  |         0.098 | n_estimators=500, learning_rate=1, max_features="log2", max_depth=5    |
|          0.303 |         0.038 | n_estimators=700, learning_rate=1, max_features="log2", max_depth=7    |
|          0.28  |         0.15  | n_estimators=700, learning_rate=1, max_features="log2", max_depth=3    |
|          0.236 |         0.028 | n_estimators=700, learning_rate=1, max_features="log2", max_depth=5    |
|          0.229 |         0.025 | n_estimators=500, learning_rate=1, max_features="log2", max_depth=7    |

## BernoulliNB
|   mean(scores) |   std(scores) | params   |
|---------------:|--------------:|:---------|
|          0.403 |         0.007 |          |

## GaussianNB
|   mean(scores) |   std(scores) | params   |
|---------------:|--------------:|:---------|
|          0.472 |         0.011 |          |

## LogisticRegression
|   mean(scores) |   std(scores) | params              |
|---------------:|--------------:|:--------------------|
|          0.571 |         0.007 | C=1, penalty="l1"   |
|          0.57  |         0.01  | C=1, penalty="l2"   |
|          0.57  |         0.005 | C=0.1, penalty="l2" |
|          0.57  |         0.008 | C=10, penalty="l1"  |
|          0.568 |         0.005 | C=10, penalty="l2"  |
|          0.568 |         0.007 | C=0.1, penalty="l1" |

