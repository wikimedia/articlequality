# Model tuning report
- Revscoring version: 1.3.5
- Features: wikiclass.feature_lists.trwiki.wp10
- Date: 2017-06-15T20:17:55.876271
- Observations: 1338
- Labels: ["km", "taslak", "sm", "b", "c"]
- Scoring: accuracy
- Folds: 20

# Top scoring configurations
| model                      |   mean(scores) |   std(scores) | params                                                                         |
|:---------------------------|---------------:|--------------:|:-------------------------------------------------------------------------------|
| RandomForestClassifier     |          0.739 |         0.044 | max_features="log2", min_samples_leaf=1, criterion="gini", n_estimators=160    |
| RandomForestClassifier     |          0.737 |         0.033 | max_features="log2", min_samples_leaf=1, criterion="gini", n_estimators=320    |
| RandomForestClassifier     |          0.736 |         0.04  | max_features="log2", min_samples_leaf=1, criterion="entropy", n_estimators=160 |
| GradientBoostingClassifier |          0.735 |         0.041 | max_depth=7, max_features="log2", n_estimators=300, learning_rate=0.1          |
| GradientBoostingClassifier |          0.734 |         0.044 | max_depth=5, max_features="log2", n_estimators=500, learning_rate=0.1          |
| GradientBoostingClassifier |          0.733 |         0.038 | max_depth=7, max_features="log2", n_estimators=500, learning_rate=0.1          |
| RandomForestClassifier     |          0.732 |         0.045 | max_features="log2", min_samples_leaf=1, criterion="gini", n_estimators=80     |
| GradientBoostingClassifier |          0.732 |         0.042 | max_depth=3, max_features="log2", n_estimators=300, learning_rate=0.1          |
| RandomForestClassifier     |          0.731 |         0.039 | max_features="log2", min_samples_leaf=1, criterion="entropy", n_estimators=320 |
| GradientBoostingClassifier |          0.731 |         0.042 | max_depth=5, max_features="log2", n_estimators=300, learning_rate=0.1          |

# Models
## LogisticRegression
|   mean(scores) |   std(scores) | params              |
|---------------:|--------------:|:--------------------|
|          0.636 |         0.046 | penalty="l1", C=10  |
|          0.61  |         0.051 | penalty="l1", C=0.1 |
|          0.598 |         0.059 | penalty="l2", C=10  |
|          0.597 |         0.059 | penalty="l1", C=1   |
|          0.59  |         0.041 | penalty="l2", C=0.1 |
|          0.579 |         0.067 | penalty="l2", C=1   |

## SVC
|   mean(scores) |   std(scores) | params                                                               |
|---------------:|--------------:|:---------------------------------------------------------------------|
|          0.474 |         0.043 | cache_size=1000, kernel="rbf", C=10, gamma=0.0001, probability=true  |
|          0.474 |         0.038 | cache_size=1000, kernel="rbf", C=1, gamma=0.0001, probability=true   |
|          0.394 |         0.045 | cache_size=1000, kernel="rbf", C=10, gamma=0.001, probability=true   |
|          0.387 |         0.046 | cache_size=1000, kernel="rbf", C=1, gamma=0.001, probability=true    |
|          0.311 |         0.035 | cache_size=1000, kernel="rbf", C=10, gamma=0.0, probability=true     |
|          0.308 |         0.036 | cache_size=1000, kernel="rbf", C=1, gamma=0.0, probability=true      |
|          0.229 |         0.031 | cache_size=1000, kernel="rbf", C=0.1, gamma=0.0001, probability=true |
|          0.209 |         0.039 | cache_size=1000, kernel="rbf", C=0.1, gamma=0.001, probability=true  |
|          0.202 |         0.006 | cache_size=1000, kernel="rbf", C=0.1, gamma=0.0, probability=true    |

## RandomForestClassifier
|   mean(scores) |   std(scores) | params                                                                          |
|---------------:|--------------:|:--------------------------------------------------------------------------------|
|          0.739 |         0.044 | max_features="log2", min_samples_leaf=1, criterion="gini", n_estimators=160     |
|          0.737 |         0.033 | max_features="log2", min_samples_leaf=1, criterion="gini", n_estimators=320     |
|          0.736 |         0.04  | max_features="log2", min_samples_leaf=1, criterion="entropy", n_estimators=160  |
|          0.732 |         0.045 | max_features="log2", min_samples_leaf=1, criterion="gini", n_estimators=80      |
|          0.731 |         0.039 | max_features="log2", min_samples_leaf=1, criterion="entropy", n_estimators=320  |
|          0.73  |         0.046 | max_features="log2", min_samples_leaf=1, criterion="gini", n_estimators=640     |
|          0.73  |         0.044 | max_features="log2", min_samples_leaf=1, criterion="entropy", n_estimators=640  |
|          0.727 |         0.042 | max_features="log2", min_samples_leaf=1, criterion="gini", n_estimators=40      |
|          0.725 |         0.039 | max_features="log2", min_samples_leaf=1, criterion="entropy", n_estimators=40   |
|          0.725 |         0.043 | max_features="log2", min_samples_leaf=1, criterion="entropy", n_estimators=80   |
|          0.722 |         0.043 | max_features="log2", min_samples_leaf=1, criterion="entropy", n_estimators=20   |
|          0.717 |         0.043 | max_features="log2", min_samples_leaf=1, criterion="gini", n_estimators=20      |
|          0.717 |         0.046 | max_features="log2", min_samples_leaf=1, criterion="entropy", n_estimators=10   |
|          0.715 |         0.038 | max_features="log2", min_samples_leaf=3, criterion="entropy", n_estimators=40   |
|          0.714 |         0.038 | max_features="log2", min_samples_leaf=3, criterion="entropy", n_estimators=80   |
|          0.713 |         0.035 | max_features="log2", min_samples_leaf=3, criterion="entropy", n_estimators=640  |
|          0.713 |         0.038 | max_features="log2", min_samples_leaf=3, criterion="entropy", n_estimators=160  |
|          0.713 |         0.038 | max_features="log2", min_samples_leaf=3, criterion="entropy", n_estimators=320  |
|          0.712 |         0.041 | max_features="log2", min_samples_leaf=3, criterion="gini", n_estimators=160     |
|          0.712 |         0.034 | max_features="log2", min_samples_leaf=3, criterion="gini", n_estimators=320     |
|          0.709 |         0.037 | max_features="log2", min_samples_leaf=3, criterion="gini", n_estimators=640     |
|          0.708 |         0.035 | max_features="log2", min_samples_leaf=3, criterion="gini", n_estimators=80      |
|          0.707 |         0.043 | max_features="log2", min_samples_leaf=3, criterion="gini", n_estimators=20      |
|          0.707 |         0.048 | max_features="log2", min_samples_leaf=3, criterion="entropy", n_estimators=20   |
|          0.704 |         0.034 | max_features="log2", min_samples_leaf=3, criterion="gini", n_estimators=40      |
|          0.704 |         0.043 | max_features="log2", min_samples_leaf=3, criterion="gini", n_estimators=10      |
|          0.703 |         0.036 | max_features="log2", min_samples_leaf=5, criterion="entropy", n_estimators=640  |
|          0.703 |         0.033 | max_features="log2", min_samples_leaf=5, criterion="gini", n_estimators=160     |
|          0.702 |         0.033 | max_features="log2", min_samples_leaf=5, criterion="entropy", n_estimators=320  |
|          0.701 |         0.043 | max_features="log2", min_samples_leaf=5, criterion="entropy", n_estimators=160  |
|          0.699 |         0.038 | max_features="log2", min_samples_leaf=5, criterion="entropy", n_estimators=40   |
|          0.699 |         0.038 | max_features="log2", min_samples_leaf=5, criterion="entropy", n_estimators=80   |
|          0.698 |         0.039 | max_features="log2", min_samples_leaf=5, criterion="gini", n_estimators=640     |
|          0.697 |         0.04  | max_features="log2", min_samples_leaf=3, criterion="entropy", n_estimators=10   |
|          0.697 |         0.045 | max_features="log2", min_samples_leaf=5, criterion="gini", n_estimators=80      |
|          0.696 |         0.049 | max_features="log2", min_samples_leaf=1, criterion="gini", n_estimators=10      |
|          0.695 |         0.042 | max_features="log2", min_samples_leaf=5, criterion="gini", n_estimators=20      |
|          0.694 |         0.038 | max_features="log2", min_samples_leaf=5, criterion="gini", n_estimators=320     |
|          0.694 |         0.053 | max_features="log2", min_samples_leaf=5, criterion="entropy", n_estimators=20   |
|          0.693 |         0.04  | max_features="log2", min_samples_leaf=5, criterion="gini", n_estimators=40      |
|          0.692 |         0.054 | max_features="log2", min_samples_leaf=7, criterion="entropy", n_estimators=40   |
|          0.692 |         0.046 | max_features="log2", min_samples_leaf=7, criterion="gini", n_estimators=40      |
|          0.691 |         0.043 | max_features="log2", min_samples_leaf=7, criterion="entropy", n_estimators=640  |
|          0.69  |         0.044 | max_features="log2", min_samples_leaf=7, criterion="entropy", n_estimators=80   |
|          0.69  |         0.041 | max_features="log2", min_samples_leaf=7, criterion="entropy", n_estimators=160  |
|          0.69  |         0.04  | max_features="log2", min_samples_leaf=7, criterion="entropy", n_estimators=320  |
|          0.689 |         0.037 | max_features="log2", min_samples_leaf=7, criterion="gini", n_estimators=320     |
|          0.688 |         0.045 | max_features="log2", min_samples_leaf=7, criterion="entropy", n_estimators=20   |
|          0.687 |         0.044 | max_features="log2", min_samples_leaf=7, criterion="gini", n_estimators=640     |
|          0.684 |         0.041 | max_features="log2", min_samples_leaf=7, criterion="gini", n_estimators=80      |
|          0.684 |         0.042 | max_features="log2", min_samples_leaf=5, criterion="gini", n_estimators=10      |
|          0.681 |         0.047 | max_features="log2", min_samples_leaf=5, criterion="entropy", n_estimators=10   |
|          0.68  |         0.044 | max_features="log2", min_samples_leaf=7, criterion="gini", n_estimators=160     |
|          0.679 |         0.044 | max_features="log2", min_samples_leaf=7, criterion="gini", n_estimators=10      |
|          0.672 |         0.049 | max_features="log2", min_samples_leaf=13, criterion="entropy", n_estimators=160 |
|          0.672 |         0.039 | max_features="log2", min_samples_leaf=7, criterion="gini", n_estimators=20      |
|          0.669 |         0.051 | max_features="log2", min_samples_leaf=13, criterion="entropy", n_estimators=40  |
|          0.665 |         0.052 | max_features="log2", min_samples_leaf=13, criterion="entropy", n_estimators=10  |
|          0.664 |         0.047 | max_features="log2", min_samples_leaf=13, criterion="gini", n_estimators=20     |
|          0.664 |         0.042 | max_features="log2", min_samples_leaf=13, criterion="entropy", n_estimators=320 |
|          0.663 |         0.051 | max_features="log2", min_samples_leaf=13, criterion="entropy", n_estimators=80  |
|          0.662 |         0.043 | max_features="log2", min_samples_leaf=13, criterion="gini", n_estimators=320    |
|          0.662 |         0.052 | max_features="log2", min_samples_leaf=13, criterion="gini", n_estimators=40     |
|          0.662 |         0.054 | max_features="log2", min_samples_leaf=13, criterion="gini", n_estimators=640    |
|          0.662 |         0.049 | max_features="log2", min_samples_leaf=13, criterion="entropy", n_estimators=640 |
|          0.661 |         0.05  | max_features="log2", min_samples_leaf=13, criterion="gini", n_estimators=160    |
|          0.66  |         0.052 | max_features="log2", min_samples_leaf=13, criterion="gini", n_estimators=80     |
|          0.66  |         0.043 | max_features="log2", min_samples_leaf=7, criterion="entropy", n_estimators=10   |
|          0.652 |         0.047 | max_features="log2", min_samples_leaf=13, criterion="gini", n_estimators=10     |
|          0.643 |         0.052 | max_features="log2", min_samples_leaf=13, criterion="entropy", n_estimators=20  |

## BernoulliNB
|   mean(scores) |   std(scores) | params   |
|---------------:|--------------:|:---------|
|          0.428 |         0.056 |          |

## GradientBoostingClassifier
|   mean(scores) |   std(scores) | params                                                                 |
|---------------:|--------------:|:-----------------------------------------------------------------------|
|          0.735 |         0.041 | max_depth=7, max_features="log2", n_estimators=300, learning_rate=0.1  |
|          0.734 |         0.044 | max_depth=5, max_features="log2", n_estimators=500, learning_rate=0.1  |
|          0.733 |         0.038 | max_depth=7, max_features="log2", n_estimators=500, learning_rate=0.1  |
|          0.732 |         0.042 | max_depth=3, max_features="log2", n_estimators=300, learning_rate=0.1  |
|          0.731 |         0.042 | max_depth=5, max_features="log2", n_estimators=300, learning_rate=0.1  |
|          0.73  |         0.042 | max_depth=7, max_features="log2", n_estimators=300, learning_rate=0.5  |
|          0.73  |         0.043 | max_depth=7, max_features="log2", n_estimators=100, learning_rate=0.1  |
|          0.729 |         0.045 | max_depth=7, max_features="log2", n_estimators=700, learning_rate=0.01 |
|          0.729 |         0.04  | max_depth=5, max_features="log2", n_estimators=700, learning_rate=0.01 |
|          0.728 |         0.045 | max_depth=7, max_features="log2", n_estimators=700, learning_rate=0.1  |
|          0.728 |         0.034 | max_depth=7, max_features="log2", n_estimators=300, learning_rate=0.01 |
|          0.726 |         0.038 | max_depth=7, max_features="log2", n_estimators=700, learning_rate=0.5  |
|          0.726 |         0.05  | max_depth=7, max_features="log2", n_estimators=100, learning_rate=0.5  |
|          0.726 |         0.031 | max_depth=5, max_features="log2", n_estimators=500, learning_rate=0.01 |
|          0.725 |         0.042 | max_depth=7, max_features="log2", n_estimators=500, learning_rate=0.01 |
|          0.724 |         0.044 | max_depth=5, max_features="log2", n_estimators=700, learning_rate=0.1  |
|          0.724 |         0.048 | max_depth=5, max_features="log2", n_estimators=700, learning_rate=0.5  |
|          0.724 |         0.047 | max_depth=7, max_features="log2", n_estimators=500, learning_rate=0.5  |
|          0.723 |         0.045 | max_depth=5, max_features="log2", n_estimators=300, learning_rate=0.5  |
|          0.722 |         0.041 | max_depth=3, max_features="log2", n_estimators=700, learning_rate=0.1  |
|          0.722 |         0.039 | max_depth=5, max_features="log2", n_estimators=100, learning_rate=0.1  |
|          0.721 |         0.042 | max_depth=3, max_features="log2", n_estimators=500, learning_rate=0.1  |
|          0.721 |         0.042 | max_depth=5, max_features="log2", n_estimators=500, learning_rate=0.5  |
|          0.719 |         0.029 | max_depth=5, max_features="log2", n_estimators=300, learning_rate=0.01 |
|          0.717 |         0.032 | max_depth=7, max_features="log2", n_estimators=100, learning_rate=0.01 |
|          0.716 |         0.04  | max_depth=3, max_features="log2", n_estimators=100, learning_rate=0.5  |
|          0.715 |         0.045 | max_depth=3, max_features="log2", n_estimators=700, learning_rate=0.5  |
|          0.714 |         0.04  | max_depth=3, max_features="log2", n_estimators=300, learning_rate=0.5  |
|          0.714 |         0.039 | max_depth=3, max_features="log2", n_estimators=500, learning_rate=0.5  |
|          0.714 |         0.065 | max_depth=5, max_features="log2", n_estimators=100, learning_rate=0.5  |
|          0.702 |         0.035 | max_depth=3, max_features="log2", n_estimators=100, learning_rate=0.1  |
|          0.7   |         0.105 | max_depth=5, max_features="log2", n_estimators=300, learning_rate=1    |
|          0.698 |         0.042 | max_depth=1, max_features="log2", n_estimators=500, learning_rate=0.5  |
|          0.697 |         0.036 | max_depth=3, max_features="log2", n_estimators=700, learning_rate=0.01 |
|          0.694 |         0.041 | max_depth=1, max_features="log2", n_estimators=700, learning_rate=0.5  |
|          0.693 |         0.051 | max_depth=5, max_features="log2", n_estimators=100, learning_rate=0.01 |
|          0.692 |         0.049 | max_depth=1, max_features="log2", n_estimators=700, learning_rate=0.1  |
|          0.692 |         0.038 | max_depth=1, max_features="log2", n_estimators=300, learning_rate=0.5  |
|          0.691 |         0.043 | max_depth=3, max_features="log2", n_estimators=500, learning_rate=0.01 |
|          0.69  |         0.05  | max_depth=1, max_features="log2", n_estimators=300, learning_rate=1    |
|          0.688 |         0.062 | max_depth=1, max_features="log2", n_estimators=700, learning_rate=1    |
|          0.686 |         0.043 | max_depth=1, max_features="log2", n_estimators=500, learning_rate=0.1  |
|          0.684 |         0.124 | max_depth=7, max_features="log2", n_estimators=100, learning_rate=1    |
|          0.681 |         0.047 | max_depth=1, max_features="log2", n_estimators=100, learning_rate=0.5  |
|          0.674 |         0.044 | max_depth=1, max_features="log2", n_estimators=300, learning_rate=0.1  |
|          0.674 |         0.052 | max_depth=1, max_features="log2", n_estimators=100, learning_rate=1    |
|          0.67  |         0.046 | max_depth=3, max_features="log2", n_estimators=300, learning_rate=0.01 |
|          0.667 |         0.154 | max_depth=3, max_features="log2", n_estimators=300, learning_rate=1    |
|          0.659 |         0.14  | max_depth=5, max_features="log2", n_estimators=100, learning_rate=1    |
|          0.655 |         0.165 | max_depth=3, max_features="log2", n_estimators=700, learning_rate=1    |
|          0.647 |         0.046 | max_depth=1, max_features="log2", n_estimators=100, learning_rate=0.1  |
|          0.646 |         0.151 | max_depth=3, max_features="log2", n_estimators=100, learning_rate=1    |
|          0.644 |         0.06  | max_depth=3, max_features="log2", n_estimators=100, learning_rate=0.01 |
|          0.64  |         0.127 | max_depth=1, max_features="log2", n_estimators=500, learning_rate=1    |
|          0.637 |         0.196 | max_depth=7, max_features="log2", n_estimators=500, learning_rate=1    |
|          0.636 |         0.05  | max_depth=1, max_features="log2", n_estimators=700, learning_rate=0.01 |
|          0.632 |         0.056 | max_depth=1, max_features="log2", n_estimators=300, learning_rate=0.01 |
|          0.629 |         0.053 | max_depth=1, max_features="log2", n_estimators=500, learning_rate=0.01 |
|          0.613 |         0.191 | max_depth=5, max_features="log2", n_estimators=500, learning_rate=1    |
|          0.609 |         0.198 | max_depth=3, max_features="log2", n_estimators=500, learning_rate=1    |
|          0.608 |         0.059 | max_depth=1, max_features="log2", n_estimators=100, learning_rate=0.01 |
|          0.604 |         0.186 | max_depth=5, max_features="log2", n_estimators=700, learning_rate=1    |
|          0.596 |         0.205 | max_depth=7, max_features="log2", n_estimators=700, learning_rate=1    |
|          0.569 |         0.222 | max_depth=7, max_features="log2", n_estimators=300, learning_rate=1    |

## GaussianNB
|   mean(scores) |   std(scores) | params   |
|---------------:|--------------:|:---------|
|          0.474 |         0.043 |          |

