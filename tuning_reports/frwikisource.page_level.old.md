# Model tuning report
- Revscoring version: 1.3.11
- Features: articlequality.feature_lists.frwikisource.pagelevel
- Date: 2017-05-24T21:16:09.914863
- Observations: 20000
- Labels: ["3", "1", "0", "4"]
- Scoring: accuracy
- Folds: 5

# Top scoring configurations
| model                      |   mean(scores) |   std(scores) | params                                                                         |
|:---------------------------|---------------:|--------------:|:-------------------------------------------------------------------------------|
| GradientBoostingClassifier |          0.654 |         0.007 | learning_rate=0.01, max_depth=7, max_features="log2", n_estimators=500         |
| GradientBoostingClassifier |          0.653 |         0.006 | learning_rate=0.01, max_depth=7, max_features="log2", n_estimators=700         |
| GradientBoostingClassifier |          0.653 |         0.005 | learning_rate=0.01, max_depth=7, max_features="log2", n_estimators=300         |
| GradientBoostingClassifier |          0.653 |         0.007 | learning_rate=0.01, max_depth=5, max_features="log2", n_estimators=700         |
| RandomForestClassifier     |          0.651 |         0.003 | n_estimators=320, criterion="gini", max_features="log2", min_samples_leaf=3    |
| RandomForestClassifier     |          0.651 |         0.007 | n_estimators=80, criterion="entropy", max_features="log2", min_samples_leaf=3  |
| RandomForestClassifier     |          0.651 |         0.002 | n_estimators=320, criterion="entropy", max_features="log2", min_samples_leaf=5 |
| RandomForestClassifier     |          0.651 |         0.003 | n_estimators=320, criterion="entropy", max_features="log2", min_samples_leaf=7 |
| RandomForestClassifier     |          0.651 |         0.005 | n_estimators=160, criterion="gini", max_features="log2", min_samples_leaf=3    |
| RandomForestClassifier     |          0.651 |         0.003 | n_estimators=640, criterion="gini", max_features="log2", min_samples_leaf=3    |

# Models
## RandomForestClassifier
|   mean(scores) |   std(scores) | params                                                                          |
|---------------:|--------------:|:--------------------------------------------------------------------------------|
|          0.651 |         0.003 | n_estimators=320, criterion="gini", max_features="log2", min_samples_leaf=3     |
|          0.651 |         0.007 | n_estimators=80, criterion="entropy", max_features="log2", min_samples_leaf=3   |
|          0.651 |         0.002 | n_estimators=320, criterion="entropy", max_features="log2", min_samples_leaf=5  |
|          0.651 |         0.003 | n_estimators=320, criterion="entropy", max_features="log2", min_samples_leaf=7  |
|          0.651 |         0.005 | n_estimators=160, criterion="gini", max_features="log2", min_samples_leaf=3     |
|          0.651 |         0.003 | n_estimators=640, criterion="gini", max_features="log2", min_samples_leaf=3     |
|          0.651 |         0.003 | n_estimators=160, criterion="entropy", max_features="log2", min_samples_leaf=5  |
|          0.651 |         0.002 | n_estimators=320, criterion="entropy", max_features="log2", min_samples_leaf=3  |
|          0.651 |         0.005 | n_estimators=160, criterion="entropy", max_features="log2", min_samples_leaf=7  |
|          0.65  |         0.003 | n_estimators=320, criterion="gini", max_features="log2", min_samples_leaf=7     |
|          0.65  |         0.003 | n_estimators=640, criterion="entropy", max_features="log2", min_samples_leaf=7  |
|          0.65  |         0.002 | n_estimators=320, criterion="gini", max_features="log2", min_samples_leaf=5     |
|          0.65  |         0.003 | n_estimators=640, criterion="gini", max_features="log2", min_samples_leaf=5     |
|          0.65  |         0.003 | n_estimators=80, criterion="entropy", max_features="log2", min_samples_leaf=7   |
|          0.65  |         0.003 | n_estimators=640, criterion="entropy", max_features="log2", min_samples_leaf=3  |
|          0.65  |         0.005 | n_estimators=640, criterion="entropy", max_features="log2", min_samples_leaf=5  |
|          0.65  |         0.004 | n_estimators=640, criterion="gini", max_features="log2", min_samples_leaf=7     |
|          0.65  |         0.004 | n_estimators=160, criterion="entropy", max_features="log2", min_samples_leaf=3  |
|          0.65  |         0.004 | n_estimators=640, criterion="entropy", max_features="log2", min_samples_leaf=1  |
|          0.649 |         0.004 | n_estimators=320, criterion="gini", max_features="log2", min_samples_leaf=1     |
|          0.649 |         0.005 | n_estimators=640, criterion="gini", max_features="log2", min_samples_leaf=1     |
|          0.649 |         0.006 | n_estimators=320, criterion="entropy", max_features="log2", min_samples_leaf=1  |
|          0.649 |         0.004 | n_estimators=160, criterion="gini", max_features="log2", min_samples_leaf=5     |
|          0.649 |         0.005 | n_estimators=40, criterion="entropy", max_features="log2", min_samples_leaf=5   |
|          0.649 |         0.004 | n_estimators=160, criterion="gini", max_features="log2", min_samples_leaf=7     |
|          0.648 |         0.004 | n_estimators=80, criterion="gini", max_features="log2", min_samples_leaf=3      |
|          0.648 |         0.004 | n_estimators=80, criterion="entropy", max_features="log2", min_samples_leaf=5   |
|          0.648 |         0.004 | n_estimators=160, criterion="gini", max_features="log2", min_samples_leaf=1     |
|          0.648 |         0.002 | n_estimators=160, criterion="entropy", max_features="log2", min_samples_leaf=13 |
|          0.648 |         0.004 | n_estimators=160, criterion="entropy", max_features="log2", min_samples_leaf=1  |
|          0.648 |         0.004 | n_estimators=640, criterion="entropy", max_features="log2", min_samples_leaf=13 |
|          0.648 |         0.004 | n_estimators=320, criterion="entropy", max_features="log2", min_samples_leaf=13 |
|          0.648 |         0.005 | n_estimators=80, criterion="gini", max_features="log2", min_samples_leaf=13     |
|          0.648 |         0.003 | n_estimators=80, criterion="gini", max_features="log2", min_samples_leaf=5      |
|          0.648 |         0.003 | n_estimators=80, criterion="gini", max_features="log2", min_samples_leaf=7      |
|          0.647 |         0.003 | n_estimators=640, criterion="gini", max_features="log2", min_samples_leaf=13    |
|          0.647 |         0.003 | n_estimators=80, criterion="entropy", max_features="log2", min_samples_leaf=1   |
|          0.647 |         0.004 | n_estimators=160, criterion="gini", max_features="log2", min_samples_leaf=13    |
|          0.647 |         0.005 | n_estimators=80, criterion="entropy", max_features="log2", min_samples_leaf=13  |
|          0.647 |         0.005 | n_estimators=80, criterion="gini", max_features="log2", min_samples_leaf=1      |
|          0.647 |         0.004 | n_estimators=320, criterion="gini", max_features="log2", min_samples_leaf=13    |
|          0.647 |         0.004 | n_estimators=40, criterion="gini", max_features="log2", min_samples_leaf=3      |
|          0.646 |         0.003 | n_estimators=40, criterion="gini", max_features="log2", min_samples_leaf=5      |
|          0.646 |         0.006 | n_estimators=40, criterion="gini", max_features="log2", min_samples_leaf=7      |
|          0.646 |         0.005 | n_estimators=40, criterion="gini", max_features="log2", min_samples_leaf=13     |
|          0.645 |         0.003 | n_estimators=40, criterion="entropy", max_features="log2", min_samples_leaf=7   |
|          0.645 |         0.005 | n_estimators=40, criterion="entropy", max_features="log2", min_samples_leaf=3   |
|          0.645 |         0.005 | n_estimators=20, criterion="entropy", max_features="log2", min_samples_leaf=13  |
|          0.644 |         0.007 | n_estimators=20, criterion="gini", max_features="log2", min_samples_leaf=13     |
|          0.644 |         0.005 | n_estimators=20, criterion="entropy", max_features="log2", min_samples_leaf=5   |
|          0.644 |         0.007 | n_estimators=40, criterion="entropy", max_features="log2", min_samples_leaf=13  |
|          0.644 |         0.007 | n_estimators=40, criterion="gini", max_features="log2", min_samples_leaf=1      |
|          0.643 |         0.003 | n_estimators=20, criterion="entropy", max_features="log2", min_samples_leaf=7   |
|          0.643 |         0.004 | n_estimators=40, criterion="entropy", max_features="log2", min_samples_leaf=1   |
|          0.642 |         0.004 | n_estimators=20, criterion="entropy", max_features="log2", min_samples_leaf=3   |
|          0.642 |         0.006 | n_estimators=20, criterion="gini", max_features="log2", min_samples_leaf=7      |
|          0.641 |         0.009 | n_estimators=20, criterion="gini", max_features="log2", min_samples_leaf=5      |
|          0.64  |         0.006 | n_estimators=20, criterion="gini", max_features="log2", min_samples_leaf=3      |
|          0.64  |         0.005 | n_estimators=10, criterion="entropy", max_features="log2", min_samples_leaf=13  |
|          0.639 |         0.006 | n_estimators=10, criterion="gini", max_features="log2", min_samples_leaf=7      |
|          0.638 |         0.006 | n_estimators=10, criterion="entropy", max_features="log2", min_samples_leaf=7   |
|          0.637 |         0.007 | n_estimators=10, criterion="entropy", max_features="log2", min_samples_leaf=5   |
|          0.636 |         0.007 | n_estimators=10, criterion="gini", max_features="log2", min_samples_leaf=13     |
|          0.636 |         0.004 | n_estimators=20, criterion="entropy", max_features="log2", min_samples_leaf=1   |
|          0.635 |         0.006 | n_estimators=20, criterion="gini", max_features="log2", min_samples_leaf=1      |
|          0.633 |         0.004 | n_estimators=10, criterion="entropy", max_features="log2", min_samples_leaf=3   |
|          0.632 |         0.006 | n_estimators=10, criterion="gini", max_features="log2", min_samples_leaf=5      |
|          0.631 |         0.004 | n_estimators=10, criterion="gini", max_features="log2", min_samples_leaf=3      |
|          0.623 |         0.008 | n_estimators=10, criterion="gini", max_features="log2", min_samples_leaf=1      |
|          0.622 |         0.005 | n_estimators=10, criterion="entropy", max_features="log2", min_samples_leaf=1   |

## SVC
|   mean(scores) |   std(scores) | params                                                               |
|---------------:|--------------:|:---------------------------------------------------------------------|
|          0.606 |         0.007 | C=10, gamma=0.0001, kernel="rbf", probability=true, cache_size=1000  |
|          0.594 |         0.006 | C=1, gamma=0.001, kernel="rbf", probability=true, cache_size=1000    |
|          0.594 |         0.004 | C=1, gamma=0.0001, kernel="rbf", probability=true, cache_size=1000   |
|          0.59  |         0.005 | C=10, gamma=0.001, kernel="rbf", probability=true, cache_size=1000   |
|          0.574 |         0.006 | C=0.1, gamma=0.0001, kernel="rbf", probability=true, cache_size=1000 |
|          0.571 |         0.005 | C=0.1, gamma=0.001, kernel="rbf", probability=true, cache_size=1000  |
|          0.521 |         0.006 | C=10, gamma=0.0, kernel="rbf", probability=true, cache_size=1000     |
|          0.518 |         0.003 | C=1, gamma=0.0, kernel="rbf", probability=true, cache_size=1000      |
|          0.492 |         0.004 | C=0.1, gamma=0.0, kernel="rbf", probability=true, cache_size=1000    |

## GradientBoostingClassifier
|   mean(scores) |   std(scores) | params                                                                 |
|---------------:|--------------:|:-----------------------------------------------------------------------|
|          0.654 |         0.007 | learning_rate=0.01, max_depth=7, max_features="log2", n_estimators=500 |
|          0.653 |         0.006 | learning_rate=0.01, max_depth=7, max_features="log2", n_estimators=700 |
|          0.653 |         0.005 | learning_rate=0.01, max_depth=7, max_features="log2", n_estimators=300 |
|          0.653 |         0.007 | learning_rate=0.01, max_depth=5, max_features="log2", n_estimators=700 |
|          0.651 |         0.006 | learning_rate=0.01, max_depth=5, max_features="log2", n_estimators=500 |
|          0.65  |         0.007 | learning_rate=0.1, max_depth=5, max_features="log2", n_estimators=100  |
|          0.648 |         0.005 | learning_rate=0.1, max_depth=5, max_features="log2", n_estimators=300  |
|          0.648 |         0.006 | learning_rate=0.1, max_depth=7, max_features="log2", n_estimators=100  |
|          0.648 |         0.004 | learning_rate=0.1, max_depth=3, max_features="log2", n_estimators=500  |
|          0.648 |         0.005 | learning_rate=0.01, max_depth=7, max_features="log2", n_estimators=100 |
|          0.647 |         0.005 | learning_rate=0.1, max_depth=3, max_features="log2", n_estimators=300  |
|          0.646 |         0.005 | learning_rate=0.1, max_depth=3, max_features="log2", n_estimators=700  |
|          0.646 |         0.004 | learning_rate=0.01, max_depth=5, max_features="log2", n_estimators=300 |
|          0.646 |         0.006 | learning_rate=0.1, max_depth=7, max_features="log2", n_estimators=300  |
|          0.645 |         0.006 | learning_rate=0.1, max_depth=5, max_features="log2", n_estimators=500  |
|          0.642 |         0.006 | learning_rate=0.1, max_depth=3, max_features="log2", n_estimators=100  |
|          0.641 |         0.005 | learning_rate=0.01, max_depth=3, max_features="log2", n_estimators=700 |
|          0.641 |         0.004 | learning_rate=0.1, max_depth=7, max_features="log2", n_estimators=500  |
|          0.641 |         0.004 | learning_rate=0.5, max_depth=3, max_features="log2", n_estimators=100  |
|          0.64  |         0.004 | learning_rate=0.01, max_depth=5, max_features="log2", n_estimators=100 |
|          0.64  |         0.006 | learning_rate=0.1, max_depth=7, max_features="log2", n_estimators=700  |
|          0.64  |         0.005 | learning_rate=0.01, max_depth=3, max_features="log2", n_estimators=500 |
|          0.639 |         0.007 | learning_rate=0.1, max_depth=5, max_features="log2", n_estimators=700  |
|          0.636 |         0.004 | learning_rate=0.01, max_depth=3, max_features="log2", n_estimators=300 |
|          0.634 |         0.007 | learning_rate=0.5, max_depth=3, max_features="log2", n_estimators=300  |
|          0.631 |         0.007 | learning_rate=0.1, max_depth=1, max_features="log2", n_estimators=700  |
|          0.631 |         0.007 | learning_rate=0.5, max_depth=1, max_features="log2", n_estimators=300  |
|          0.631 |         0.004 | learning_rate=0.1, max_depth=1, max_features="log2", n_estimators=300  |
|          0.63  |         0.008 | learning_rate=0.1, max_depth=1, max_features="log2", n_estimators=500  |
|          0.63  |         0.003 | learning_rate=0.5, max_depth=5, max_features="log2", n_estimators=100  |
|          0.63  |         0.007 | learning_rate=0.5, max_depth=1, max_features="log2", n_estimators=100  |
|          0.63  |         0.007 | learning_rate=0.5, max_depth=1, max_features="log2", n_estimators=500  |
|          0.63  |         0.008 | learning_rate=0.5, max_depth=7, max_features="log2", n_estimators=100  |
|          0.63  |         0.007 | learning_rate=1, max_depth=1, max_features="log2", n_estimators=500    |
|          0.629 |         0.009 | learning_rate=0.5, max_depth=1, max_features="log2", n_estimators=700  |
|          0.628 |         0.006 | learning_rate=1, max_depth=1, max_features="log2", n_estimators=100    |
|          0.628 |         0.007 | learning_rate=1, max_depth=1, max_features="log2", n_estimators=300    |
|          0.628 |         0.006 | learning_rate=0.1, max_depth=1, max_features="log2", n_estimators=100  |
|          0.626 |         0.001 | learning_rate=0.5, max_depth=5, max_features="log2", n_estimators=300  |
|          0.626 |         0.004 | learning_rate=0.01, max_depth=3, max_features="log2", n_estimators=100 |
|          0.625 |         0.005 | learning_rate=1, max_depth=3, max_features="log2", n_estimators=100    |
|          0.625 |         0.005 | learning_rate=1, max_depth=1, max_features="log2", n_estimators=700    |
|          0.625 |         0.005 | learning_rate=0.5, max_depth=3, max_features="log2", n_estimators=500  |
|          0.623 |         0.005 | learning_rate=0.01, max_depth=1, max_features="log2", n_estimators=700 |
|          0.62  |         0.005 | learning_rate=0.01, max_depth=1, max_features="log2", n_estimators=500 |
|          0.617 |         0.004 | learning_rate=0.01, max_depth=1, max_features="log2", n_estimators=300 |
|          0.612 |         0.014 | learning_rate=1, max_depth=5, max_features="log2", n_estimators=100    |
|          0.611 |         0.005 | learning_rate=0.01, max_depth=1, max_features="log2", n_estimators=100 |
|          0.608 |         0.007 | learning_rate=1, max_depth=3, max_features="log2", n_estimators=300    |
|          0.59  |         0.019 | learning_rate=1, max_depth=3, max_features="log2", n_estimators=500    |
|          0.582 |         0.038 | learning_rate=0.5, max_depth=5, max_features="log2", n_estimators=500  |
|          0.581 |         0.094 | learning_rate=0.5, max_depth=3, max_features="log2", n_estimators=700  |
|          0.561 |         0.093 | learning_rate=1, max_depth=7, max_features="log2", n_estimators=100    |
|          0.529 |         0.132 | learning_rate=0.5, max_depth=5, max_features="log2", n_estimators=700  |
|          0.516 |         0.149 | learning_rate=0.5, max_depth=7, max_features="log2", n_estimators=300  |
|          0.505 |         0.154 | learning_rate=0.5, max_depth=7, max_features="log2", n_estimators=700  |
|          0.5   |         0.158 | learning_rate=0.5, max_depth=7, max_features="log2", n_estimators=500  |
|          0.477 |         0.125 | learning_rate=1, max_depth=5, max_features="log2", n_estimators=300    |
|          0.452 |         0.209 | learning_rate=1, max_depth=7, max_features="log2", n_estimators=300    |
|          0.413 |         0.179 | learning_rate=1, max_depth=7, max_features="log2", n_estimators=500    |
|          0.393 |         0.14  | learning_rate=1, max_depth=5, max_features="log2", n_estimators=500    |
|          0.362 |         0.13  | learning_rate=1, max_depth=5, max_features="log2", n_estimators=700    |
|          0.312 |         0.156 | learning_rate=1, max_depth=3, max_features="log2", n_estimators=700    |
|          0.211 |         0.073 | learning_rate=1, max_depth=7, max_features="log2", n_estimators=700    |

## GaussianNB
|   mean(scores) |   std(scores) | params   |
|---------------:|--------------:|:---------|
|          0.521 |         0.018 |          |

## LogisticRegression
|   mean(scores) |   std(scores) | params              |
|---------------:|--------------:|:--------------------|
|          0.587 |         0.003 | C=10, penalty="l1"  |
|          0.578 |         0.004 | C=1, penalty="l1"   |
|          0.566 |         0.004 | C=0.1, penalty="l1" |
|          0.564 |         0.006 | C=1, penalty="l2"   |
|          0.563 |         0.004 | C=10, penalty="l2"  |
|          0.56  |         0.002 | C=0.1, penalty="l2" |

## BernoulliNB
|   mean(scores) |   std(scores) | params   |
|---------------:|--------------:|:---------|
|          0.531 |         0.003 |          |

