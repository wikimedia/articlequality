# Model tuning report
- Revscoring version: 1.3.11
- Features: articlequality.feature_lists.frwikisource.pagelevel
- Date: 2017-05-25T16:03:02.310610
- Observations: 20000
- Labels: ["1", "3", "4", "0"]
- Scoring: accuracy
- Folds: 5

# Top scoring configurations
| model                      |   mean(scores) |   std(scores) | params                                                                         |
|:---------------------------|---------------:|--------------:|:-------------------------------------------------------------------------------|
| GradientBoostingClassifier |          0.763 |         0.003 | n_estimators=700, max_features="log2", learning_rate=0.1, max_depth=7          |
| GradientBoostingClassifier |          0.761 |         0.004 | n_estimators=500, max_features="log2", learning_rate=0.1, max_depth=7          |
| GradientBoostingClassifier |          0.761 |         0.003 | n_estimators=300, max_features="log2", learning_rate=0.1, max_depth=7          |
| RandomForestClassifier     |          0.76  |         0.005 | criterion="entropy", n_estimators=640, max_features="log2", min_samples_leaf=1 |
| GradientBoostingClassifier |          0.759 |         0.003 | n_estimators=500, max_features="log2", learning_rate=0.1, max_depth=5          |
| GradientBoostingClassifier |          0.757 |         0.003 | n_estimators=700, max_features="log2", learning_rate=0.1, max_depth=5          |
| GradientBoostingClassifier |          0.756 |         0.005 | n_estimators=100, max_features="log2", learning_rate=0.1, max_depth=7          |
| RandomForestClassifier     |          0.756 |         0.007 | criterion="gini", n_estimators=640, max_features="log2", min_samples_leaf=1    |
| RandomForestClassifier     |          0.755 |         0.006 | criterion="entropy", n_estimators=320, max_features="log2", min_samples_leaf=1 |
| RandomForestClassifier     |          0.754 |         0.004 | criterion="entropy", n_estimators=640, max_features="log2", min_samples_leaf=3 |

# Models
## GradientBoostingClassifier
|   mean(scores) |   std(scores) | params                                                                 |
|---------------:|--------------:|:-----------------------------------------------------------------------|
|          0.763 |         0.003 | n_estimators=700, max_features="log2", learning_rate=0.1, max_depth=7  |
|          0.761 |         0.004 | n_estimators=500, max_features="log2", learning_rate=0.1, max_depth=7  |
|          0.761 |         0.003 | n_estimators=300, max_features="log2", learning_rate=0.1, max_depth=7  |
|          0.759 |         0.003 | n_estimators=500, max_features="log2", learning_rate=0.1, max_depth=5  |
|          0.757 |         0.003 | n_estimators=700, max_features="log2", learning_rate=0.1, max_depth=5  |
|          0.756 |         0.005 | n_estimators=100, max_features="log2", learning_rate=0.1, max_depth=7  |
|          0.754 |         0.004 | n_estimators=700, max_features="log2", learning_rate=0.01, max_depth=7 |
|          0.754 |         0.006 | n_estimators=700, max_features="log2", learning_rate=0.5, max_depth=7  |
|          0.753 |         0.003 | n_estimators=300, max_features="log2", learning_rate=0.1, max_depth=5  |
|          0.752 |         0.004 | n_estimators=300, max_features="log2", learning_rate=0.5, max_depth=7  |
|          0.752 |         0.005 | n_estimators=500, max_features="log2", learning_rate=0.5, max_depth=7  |
|          0.75  |         0.003 | n_estimators=500, max_features="log2", learning_rate=0.01, max_depth=7 |
|          0.745 |         0.006 | n_estimators=100, max_features="log2", learning_rate=0.5, max_depth=7  |
|          0.745 |         0.002 | n_estimators=700, max_features="log2", learning_rate=0.1, max_depth=3  |
|          0.744 |         0.004 | n_estimators=100, max_features="log2", learning_rate=0.1, max_depth=5  |
|          0.742 |         0.003 | n_estimators=500, max_features="log2", learning_rate=0.1, max_depth=3  |
|          0.739 |         0.005 | n_estimators=300, max_features="log2", learning_rate=0.01, max_depth=7 |
|          0.739 |         0.007 | n_estimators=100, max_features="log2", learning_rate=0.5, max_depth=5  |
|          0.737 |         0.004 | n_estimators=700, max_features="log2", learning_rate=0.01, max_depth=5 |
|          0.737 |         0.004 | n_estimators=300, max_features="log2", learning_rate=0.5, max_depth=3  |
|          0.737 |         0.008 | n_estimators=700, max_features="log2", learning_rate=0.5, max_depth=3  |
|          0.736 |         0.005 | n_estimators=500, max_features="log2", learning_rate=0.5, max_depth=3  |
|          0.736 |         0.002 | n_estimators=300, max_features="log2", learning_rate=0.1, max_depth=3  |
|          0.735 |         0.01  | n_estimators=300, max_features="log2", learning_rate=0.5, max_depth=5  |
|          0.733 |         0.005 | n_estimators=100, max_features="log2", learning_rate=1, max_depth=7    |
|          0.733 |         0.003 | n_estimators=100, max_features="log2", learning_rate=0.5, max_depth=3  |
|          0.73  |         0.003 | n_estimators=500, max_features="log2", learning_rate=0.01, max_depth=5 |
|          0.73  |         0.018 | n_estimators=500, max_features="log2", learning_rate=0.5, max_depth=5  |
|          0.722 |         0.006 | n_estimators=100, max_features="log2", learning_rate=1, max_depth=3    |
|          0.718 |         0.005 | n_estimators=300, max_features="log2", learning_rate=0.01, max_depth=5 |
|          0.718 |         0.028 | n_estimators=300, max_features="log2", learning_rate=1, max_depth=5    |
|          0.718 |         0.01  | n_estimators=500, max_features="log2", learning_rate=1, max_depth=3    |
|          0.717 |         0.006 | n_estimators=100, max_features="log2", learning_rate=1, max_depth=5    |
|          0.711 |         0.004 | n_estimators=100, max_features="log2", learning_rate=0.1, max_depth=3  |
|          0.711 |         0.005 | n_estimators=700, max_features="log2", learning_rate=0.5, max_depth=1  |
|          0.709 |         0.003 | n_estimators=500, max_features="log2", learning_rate=0.5, max_depth=1  |
|          0.709 |         0.003 | n_estimators=700, max_features="log2", learning_rate=0.01, max_depth=3 |
|          0.708 |         0.002 | n_estimators=300, max_features="log2", learning_rate=1, max_depth=1    |
|          0.708 |         0.004 | n_estimators=300, max_features="log2", learning_rate=0.5, max_depth=1  |
|          0.708 |         0.006 | n_estimators=100, max_features="log2", learning_rate=0.01, max_depth=7 |
|          0.705 |         0.004 | n_estimators=500, max_features="log2", learning_rate=1, max_depth=1    |
|          0.704 |         0.002 | n_estimators=700, max_features="log2", learning_rate=1, max_depth=1    |
|          0.704 |         0.031 | n_estimators=700, max_features="log2", learning_rate=0.5, max_depth=5  |
|          0.703 |         0.005 | n_estimators=100, max_features="log2", learning_rate=1, max_depth=1    |
|          0.701 |         0.005 | n_estimators=500, max_features="log2", learning_rate=0.01, max_depth=3 |
|          0.7   |         0.004 | n_estimators=700, max_features="log2", learning_rate=0.1, max_depth=1  |
|          0.697 |         0.005 | n_estimators=100, max_features="log2", learning_rate=0.5, max_depth=1  |
|          0.697 |         0.005 | n_estimators=500, max_features="log2", learning_rate=0.1, max_depth=1  |
|          0.689 |         0.005 | n_estimators=300, max_features="log2", learning_rate=0.1, max_depth=1  |
|          0.686 |         0.006 | n_estimators=100, max_features="log2", learning_rate=0.01, max_depth=5 |
|          0.683 |         0.005 | n_estimators=300, max_features="log2", learning_rate=0.01, max_depth=3 |
|          0.675 |         0.066 | n_estimators=700, max_features="log2", learning_rate=1, max_depth=3    |
|          0.662 |         0.001 | n_estimators=100, max_features="log2", learning_rate=0.1, max_depth=1  |
|          0.655 |         0.004 | n_estimators=700, max_features="log2", learning_rate=0.01, max_depth=1 |
|          0.654 |         0.175 | n_estimators=300, max_features="log2", learning_rate=1, max_depth=7    |
|          0.649 |         0.008 | n_estimators=100, max_features="log2", learning_rate=0.01, max_depth=3 |
|          0.649 |         0.006 | n_estimators=500, max_features="log2", learning_rate=0.01, max_depth=1 |
|          0.645 |         0.142 | n_estimators=300, max_features="log2", learning_rate=1, max_depth=3    |
|          0.638 |         0.007 | n_estimators=300, max_features="log2", learning_rate=0.01, max_depth=1 |
|          0.63  |         0.006 | n_estimators=100, max_features="log2", learning_rate=0.01, max_depth=1 |
|          0.617 |         0.139 | n_estimators=500, max_features="log2", learning_rate=1, max_depth=5    |
|          0.583 |         0.2   | n_estimators=700, max_features="log2", learning_rate=1, max_depth=5    |
|          0.563 |         0.222 | n_estimators=700, max_features="log2", learning_rate=1, max_depth=7    |
|          0.447 |         0.257 | n_estimators=500, max_features="log2", learning_rate=1, max_depth=7    |

## LogisticRegression
|   mean(scores) |   std(scores) | params              |
|---------------:|--------------:|:--------------------|
|          0.607 |         0.006 | penalty="l1", C=10  |
|          0.603 |         0.006 | penalty="l1", C=1   |
|          0.592 |         0.006 | penalty="l1", C=0.1 |
|          0.591 |         0.006 | penalty="l2", C=10  |
|          0.588 |         0.007 | penalty="l2", C=1   |
|          0.587 |         0.005 | penalty="l2", C=0.1 |

## BernoulliNB
|   mean(scores) |   std(scores) | params   |
|---------------:|--------------:|:---------|
|          0.574 |         0.006 |          |

## RandomForestClassifier
|   mean(scores) |   std(scores) | params                                                                          |
|---------------:|--------------:|:--------------------------------------------------------------------------------|
|          0.76  |         0.005 | criterion="entropy", n_estimators=640, max_features="log2", min_samples_leaf=1  |
|          0.756 |         0.007 | criterion="gini", n_estimators=640, max_features="log2", min_samples_leaf=1     |
|          0.755 |         0.006 | criterion="entropy", n_estimators=320, max_features="log2", min_samples_leaf=1  |
|          0.754 |         0.004 | criterion="entropy", n_estimators=640, max_features="log2", min_samples_leaf=3  |
|          0.754 |         0.009 | criterion="gini", n_estimators=160, max_features="log2", min_samples_leaf=1     |
|          0.754 |         0.006 | criterion="gini", n_estimators=320, max_features="log2", min_samples_leaf=1     |
|          0.754 |         0.005 | criterion="entropy", n_estimators=160, max_features="log2", min_samples_leaf=1  |
|          0.753 |         0.008 | criterion="gini", n_estimators=640, max_features="log2", min_samples_leaf=3     |
|          0.752 |         0.006 | criterion="entropy", n_estimators=160, max_features="log2", min_samples_leaf=3  |
|          0.752 |         0.005 | criterion="entropy", n_estimators=320, max_features="log2", min_samples_leaf=3  |
|          0.751 |         0.006 | criterion="gini", n_estimators=320, max_features="log2", min_samples_leaf=3     |
|          0.751 |         0.006 | criterion="entropy", n_estimators=80, max_features="log2", min_samples_leaf=1   |
|          0.75  |         0.004 | criterion="entropy", n_estimators=640, max_features="log2", min_samples_leaf=5  |
|          0.75  |         0.008 | criterion="gini", n_estimators=80, max_features="log2", min_samples_leaf=1      |
|          0.749 |         0.006 | criterion="gini", n_estimators=160, max_features="log2", min_samples_leaf=3     |
|          0.748 |         0.003 | criterion="entropy", n_estimators=80, max_features="log2", min_samples_leaf=3   |
|          0.748 |         0.004 | criterion="entropy", n_estimators=160, max_features="log2", min_samples_leaf=5  |
|          0.748 |         0.006 | criterion="entropy", n_estimators=320, max_features="log2", min_samples_leaf=5  |
|          0.748 |         0.005 | criterion="gini", n_estimators=160, max_features="log2", min_samples_leaf=5     |
|          0.747 |         0.006 | criterion="gini", n_estimators=320, max_features="log2", min_samples_leaf=5     |
|          0.746 |         0.007 | criterion="gini", n_estimators=80, max_features="log2", min_samples_leaf=3      |
|          0.746 |         0.004 | criterion="entropy", n_estimators=40, max_features="log2", min_samples_leaf=3   |
|          0.746 |         0.006 | criterion="gini", n_estimators=40, max_features="log2", min_samples_leaf=1      |
|          0.746 |         0.006 | criterion="gini", n_estimators=640, max_features="log2", min_samples_leaf=5     |
|          0.745 |         0.009 | criterion="entropy", n_estimators=40, max_features="log2", min_samples_leaf=1   |
|          0.745 |         0.006 | criterion="entropy", n_estimators=160, max_features="log2", min_samples_leaf=7  |
|          0.744 |         0.006 | criterion="entropy", n_estimators=640, max_features="log2", min_samples_leaf=7  |
|          0.744 |         0.005 | criterion="entropy", n_estimators=320, max_features="log2", min_samples_leaf=7  |
|          0.744 |         0.007 | criterion="entropy", n_estimators=80, max_features="log2", min_samples_leaf=5   |
|          0.742 |         0.006 | criterion="gini", n_estimators=320, max_features="log2", min_samples_leaf=7     |
|          0.742 |         0.004 | criterion="gini", n_estimators=80, max_features="log2", min_samples_leaf=5      |
|          0.742 |         0.005 | criterion="entropy", n_estimators=80, max_features="log2", min_samples_leaf=7   |
|          0.742 |         0.006 | criterion="gini", n_estimators=640, max_features="log2", min_samples_leaf=7     |
|          0.742 |         0.005 | criterion="gini", n_estimators=40, max_features="log2", min_samples_leaf=5      |
|          0.741 |         0.005 | criterion="gini", n_estimators=160, max_features="log2", min_samples_leaf=7     |
|          0.741 |         0.004 | criterion="gini", n_estimators=40, max_features="log2", min_samples_leaf=3      |
|          0.739 |         0.006 | criterion="entropy", n_estimators=20, max_features="log2", min_samples_leaf=3   |
|          0.739 |         0.004 | criterion="entropy", n_estimators=40, max_features="log2", min_samples_leaf=5   |
|          0.738 |         0.005 | criterion="gini", n_estimators=80, max_features="log2", min_samples_leaf=7      |
|          0.738 |         0.006 | criterion="entropy", n_estimators=40, max_features="log2", min_samples_leaf=7   |
|          0.737 |         0.003 | criterion="entropy", n_estimators=20, max_features="log2", min_samples_leaf=1   |
|          0.737 |         0.004 | criterion="gini", n_estimators=40, max_features="log2", min_samples_leaf=7      |
|          0.736 |         0.006 | criterion="entropy", n_estimators=320, max_features="log2", min_samples_leaf=13 |
|          0.735 |         0.009 | criterion="entropy", n_estimators=20, max_features="log2", min_samples_leaf=5   |
|          0.735 |         0.007 | criterion="gini", n_estimators=20, max_features="log2", min_samples_leaf=3      |
|          0.734 |         0.004 | criterion="entropy", n_estimators=640, max_features="log2", min_samples_leaf=13 |
|          0.734 |         0.007 | criterion="entropy", n_estimators=160, max_features="log2", min_samples_leaf=13 |
|          0.734 |         0.006 | criterion="gini", n_estimators=640, max_features="log2", min_samples_leaf=13    |
|          0.733 |         0.004 | criterion="gini", n_estimators=320, max_features="log2", min_samples_leaf=13    |
|          0.732 |         0.009 | criterion="gini", n_estimators=20, max_features="log2", min_samples_leaf=5      |
|          0.732 |         0.009 | criterion="entropy", n_estimators=20, max_features="log2", min_samples_leaf=7   |
|          0.732 |         0.005 | criterion="gini", n_estimators=80, max_features="log2", min_samples_leaf=13     |
|          0.731 |         0.005 | criterion="gini", n_estimators=160, max_features="log2", min_samples_leaf=13    |
|          0.731 |         0.004 | criterion="entropy", n_estimators=80, max_features="log2", min_samples_leaf=13  |
|          0.73  |         0.006 | criterion="entropy", n_estimators=40, max_features="log2", min_samples_leaf=13  |
|          0.73  |         0.008 | criterion="gini", n_estimators=20, max_features="log2", min_samples_leaf=1      |
|          0.73  |         0.006 | criterion="gini", n_estimators=20, max_features="log2", min_samples_leaf=7      |
|          0.727 |         0.007 | criterion="entropy", n_estimators=10, max_features="log2", min_samples_leaf=3   |
|          0.725 |         0.006 | criterion="gini", n_estimators=40, max_features="log2", min_samples_leaf=13     |
|          0.725 |         0.003 | criterion="gini", n_estimators=20, max_features="log2", min_samples_leaf=13     |
|          0.723 |         0.005 | criterion="entropy", n_estimators=20, max_features="log2", min_samples_leaf=13  |
|          0.723 |         0.007 | criterion="entropy", n_estimators=10, max_features="log2", min_samples_leaf=1   |
|          0.72  |         0.005 | criterion="entropy", n_estimators=10, max_features="log2", min_samples_leaf=13  |
|          0.72  |         0.006 | criterion="gini", n_estimators=10, max_features="log2", min_samples_leaf=3      |
|          0.72  |         0.009 | criterion="entropy", n_estimators=10, max_features="log2", min_samples_leaf=5   |
|          0.719 |         0.007 | criterion="entropy", n_estimators=10, max_features="log2", min_samples_leaf=7   |
|          0.718 |         0.007 | criterion="gini", n_estimators=10, max_features="log2", min_samples_leaf=5      |
|          0.717 |         0.005 | criterion="gini", n_estimators=10, max_features="log2", min_samples_leaf=7      |
|          0.717 |         0.004 | criterion="gini", n_estimators=10, max_features="log2", min_samples_leaf=13     |
|          0.717 |         0.004 | criterion="gini", n_estimators=10, max_features="log2", min_samples_leaf=1      |

## GaussianNB
|   mean(scores) |   std(scores) | params   |
|---------------:|--------------:|:---------|
|          0.537 |         0.014 |          |

## SVC
|   mean(scores) |   std(scores) | params                                                               |
|---------------:|--------------:|:---------------------------------------------------------------------|
|          0.636 |         0.005 | probability=true, kernel="rbf", gamma=0.0001, C=10, cache_size=1000  |
|          0.626 |         0.004 | probability=true, kernel="rbf", gamma=0.0001, C=1, cache_size=1000   |
|          0.614 |         0.003 | probability=true, kernel="rbf", gamma=0.001, C=1, cache_size=1000    |
|          0.601 |         0.005 | probability=true, kernel="rbf", gamma=0.0001, C=0.1, cache_size=1000 |
|          0.594 |         0.001 | probability=true, kernel="rbf", gamma=0.001, C=10, cache_size=1000   |
|          0.575 |         0.005 | probability=true, kernel="rbf", gamma=0.001, C=0.1, cache_size=1000  |
|          0.504 |         0.002 | probability=true, kernel="rbf", gamma=0.0, C=10, cache_size=1000     |
|          0.5   |         0.002 | probability=true, kernel="rbf", gamma=0.0, C=1, cache_size=1000      |
|          0.483 |         0.003 | probability=true, kernel="rbf", gamma=0.0, C=0.1, cache_size=1000    |

