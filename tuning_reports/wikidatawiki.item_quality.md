# Model tuning report
- Revscoring version: 1.3.10
- Features: wikiclass.feature_lists.wikidatawiki.item_quality
- Date: 2017-05-15T19:28:10.896906
- Observations: 4999
- Labels: ["B", "A", "C", "E", "D"]
- Scoring: accuracy
- Folds: 5

# Top scoring configurations
| model                  |   mean(scores) |   std(scores) | params                                                                         |
|:-----------------------|---------------:|--------------:|:-------------------------------------------------------------------------------|
| RandomForestClassifier |          0.807 |         0.049 | criterion="gini", n_estimators=20, min_samples_leaf=13, max_features="log2"    |
| RandomForestClassifier |          0.807 |         0.055 | criterion="gini", n_estimators=160, min_samples_leaf=7, max_features="log2"    |
| RandomForestClassifier |          0.806 |         0.051 | criterion="gini", n_estimators=10, min_samples_leaf=13, max_features="log2"    |
| RandomForestClassifier |          0.806 |         0.051 | criterion="gini", n_estimators=80, min_samples_leaf=7, max_features="log2"     |
| RandomForestClassifier |          0.806 |         0.053 | criterion="gini", n_estimators=320, min_samples_leaf=7, max_features="log2"    |
| RandomForestClassifier |          0.805 |         0.053 | criterion="entropy", n_estimators=320, min_samples_leaf=7, max_features="log2" |
| RandomForestClassifier |          0.805 |         0.049 | criterion="gini", n_estimators=40, min_samples_leaf=7, max_features="log2"     |
| RandomForestClassifier |          0.804 |         0.054 | criterion="gini", n_estimators=640, min_samples_leaf=7, max_features="log2"    |
| RandomForestClassifier |          0.804 |         0.053 | criterion="gini", n_estimators=160, min_samples_leaf=13, max_features="log2"   |
| RandomForestClassifier |          0.804 |         0.054 | criterion="entropy", n_estimators=40, min_samples_leaf=13, max_features="log2" |

# Models
## SVC
|   mean(scores) |   std(scores) | params                                                               |
|---------------:|--------------:|:---------------------------------------------------------------------|
|          0.787 |         0.057 | probability=true, kernel="rbf", C=10, cache_size=1000, gamma=0.0     |
|          0.778 |         0.042 | probability=true, kernel="rbf", C=1, cache_size=1000, gamma=0.0      |
|          0.719 |         0.036 | probability=true, kernel="rbf", C=0.1, cache_size=1000, gamma=0.0    |
|          0.715 |         0.039 | probability=true, kernel="rbf", C=10, cache_size=1000, gamma=0.001   |
|          0.696 |         0.042 | probability=true, kernel="rbf", C=1, cache_size=1000, gamma=0.001    |
|          0.696 |         0.042 | probability=true, kernel="rbf", C=10, cache_size=1000, gamma=0.0001  |
|          0.578 |         0.03  | probability=true, kernel="rbf", C=1, cache_size=1000, gamma=0.0001   |
|          0.578 |         0.03  | probability=true, kernel="rbf", C=0.1, cache_size=1000, gamma=0.001  |
|          0.444 |         0.111 | probability=true, kernel="rbf", C=0.1, cache_size=1000, gamma=0.0001 |

## GaussianNB
|   mean(scores) |   std(scores) | params   |
|---------------:|--------------:|:---------|
|          0.636 |         0.086 |          |

## BernoulliNB
|   mean(scores) |   std(scores) | params   |
|---------------:|--------------:|:---------|
|          0.689 |         0.027 |          |

## RandomForestClassifier
|   mean(scores) |   std(scores) | params                                                                          |
|---------------:|--------------:|:--------------------------------------------------------------------------------|
|          0.807 |         0.049 | criterion="gini", n_estimators=20, min_samples_leaf=13, max_features="log2"     |
|          0.807 |         0.055 | criterion="gini", n_estimators=160, min_samples_leaf=7, max_features="log2"     |
|          0.806 |         0.051 | criterion="gini", n_estimators=10, min_samples_leaf=13, max_features="log2"     |
|          0.806 |         0.051 | criterion="gini", n_estimators=80, min_samples_leaf=7, max_features="log2"      |
|          0.806 |         0.053 | criterion="gini", n_estimators=320, min_samples_leaf=7, max_features="log2"     |
|          0.805 |         0.053 | criterion="entropy", n_estimators=320, min_samples_leaf=7, max_features="log2"  |
|          0.805 |         0.049 | criterion="gini", n_estimators=40, min_samples_leaf=7, max_features="log2"      |
|          0.804 |         0.054 | criterion="gini", n_estimators=640, min_samples_leaf=7, max_features="log2"     |
|          0.804 |         0.053 | criterion="gini", n_estimators=160, min_samples_leaf=13, max_features="log2"    |
|          0.804 |         0.054 | criterion="entropy", n_estimators=40, min_samples_leaf=13, max_features="log2"  |
|          0.803 |         0.051 | criterion="gini", n_estimators=640, min_samples_leaf=13, max_features="log2"    |
|          0.803 |         0.042 | criterion="gini", n_estimators=10, min_samples_leaf=7, max_features="log2"      |
|          0.803 |         0.052 | criterion="entropy", n_estimators=640, min_samples_leaf=13, max_features="log2" |
|          0.803 |         0.054 | criterion="gini", n_estimators=80, min_samples_leaf=13, max_features="log2"     |
|          0.802 |         0.052 | criterion="entropy", n_estimators=320, min_samples_leaf=13, max_features="log2" |
|          0.801 |         0.055 | criterion="entropy", n_estimators=640, min_samples_leaf=7, max_features="log2"  |
|          0.801 |         0.052 | criterion="gini", n_estimators=320, min_samples_leaf=13, max_features="log2"    |
|          0.801 |         0.051 | criterion="entropy", n_estimators=160, min_samples_leaf=13, max_features="log2" |
|          0.801 |         0.059 | criterion="entropy", n_estimators=160, min_samples_leaf=7, max_features="log2"  |
|          0.8   |         0.054 | criterion="entropy", n_estimators=80, min_samples_leaf=13, max_features="log2"  |
|          0.8   |         0.056 | criterion="entropy", n_estimators=80, min_samples_leaf=7, max_features="log2"   |
|          0.8   |         0.054 | criterion="gini", n_estimators=640, min_samples_leaf=5, max_features="log2"     |
|          0.8   |         0.052 | criterion="gini", n_estimators=320, min_samples_leaf=5, max_features="log2"     |
|          0.798 |         0.054 | criterion="gini", n_estimators=160, min_samples_leaf=5, max_features="log2"     |
|          0.798 |         0.057 | criterion="entropy", n_estimators=320, min_samples_leaf=5, max_features="log2"  |
|          0.797 |         0.053 | criterion="gini", n_estimators=20, min_samples_leaf=7, max_features="log2"      |
|          0.797 |         0.053 | criterion="gini", n_estimators=80, min_samples_leaf=5, max_features="log2"      |
|          0.797 |         0.048 | criterion="entropy", n_estimators=10, min_samples_leaf=7, max_features="log2"   |
|          0.797 |         0.06  | criterion="gini", n_estimators=40, min_samples_leaf=13, max_features="log2"     |
|          0.797 |         0.059 | criterion="entropy", n_estimators=320, min_samples_leaf=3, max_features="log2"  |
|          0.797 |         0.056 | criterion="entropy", n_estimators=160, min_samples_leaf=5, max_features="log2"  |
|          0.796 |         0.059 | criterion="entropy", n_estimators=160, min_samples_leaf=3, max_features="log2"  |
|          0.796 |         0.061 | criterion="entropy", n_estimators=40, min_samples_leaf=7, max_features="log2"   |
|          0.796 |         0.058 | criterion="entropy", n_estimators=640, min_samples_leaf=5, max_features="log2"  |
|          0.796 |         0.058 | criterion="entropy", n_estimators=80, min_samples_leaf=3, max_features="log2"   |
|          0.796 |         0.058 | criterion="entropy", n_estimators=640, min_samples_leaf=3, max_features="log2"  |
|          0.794 |         0.057 | criterion="entropy", n_estimators=80, min_samples_leaf=5, max_features="log2"   |
|          0.794 |         0.056 | criterion="entropy", n_estimators=20, min_samples_leaf=7, max_features="log2"   |
|          0.793 |         0.05  | criterion="entropy", n_estimators=20, min_samples_leaf=13, max_features="log2"  |
|          0.792 |         0.057 | criterion="gini", n_estimators=20, min_samples_leaf=5, max_features="log2"      |
|          0.792 |         0.059 | criterion="entropy", n_estimators=40, min_samples_leaf=5, max_features="log2"   |
|          0.792 |         0.051 | criterion="entropy", n_estimators=20, min_samples_leaf=5, max_features="log2"   |
|          0.791 |         0.045 | criterion="entropy", n_estimators=10, min_samples_leaf=5, max_features="log2"   |
|          0.79  |         0.06  | criterion="gini", n_estimators=10, min_samples_leaf=5, max_features="log2"      |
|          0.789 |         0.058 | criterion="entropy", n_estimators=20, min_samples_leaf=3, max_features="log2"   |
|          0.788 |         0.05  | criterion="entropy", n_estimators=10, min_samples_leaf=13, max_features="log2"  |
|          0.788 |         0.065 | criterion="gini", n_estimators=40, min_samples_leaf=3, max_features="log2"      |
|          0.783 |         0.073 | criterion="gini", n_estimators=640, min_samples_leaf=3, max_features="log2"     |
|          0.783 |         0.069 | criterion="gini", n_estimators=80, min_samples_leaf=3, max_features="log2"      |
|          0.782 |         0.073 | criterion="gini", n_estimators=320, min_samples_leaf=3, max_features="log2"     |
|          0.781 |         0.071 | criterion="gini", n_estimators=160, min_samples_leaf=3, max_features="log2"     |
|          0.78  |         0.069 | criterion="gini", n_estimators=40, min_samples_leaf=5, max_features="log2"      |
|          0.78  |         0.066 | criterion="gini", n_estimators=320, min_samples_leaf=1, max_features="log2"     |
|          0.78  |         0.058 | criterion="gini", n_estimators=20, min_samples_leaf=1, max_features="log2"      |
|          0.779 |         0.065 | criterion="entropy", n_estimators=640, min_samples_leaf=1, max_features="log2"  |
|          0.779 |         0.07  | criterion="entropy", n_estimators=40, min_samples_leaf=3, max_features="log2"   |
|          0.779 |         0.063 | criterion="entropy", n_estimators=80, min_samples_leaf=1, max_features="log2"   |
|          0.779 |         0.062 | criterion="gini", n_estimators=80, min_samples_leaf=1, max_features="log2"      |
|          0.779 |         0.065 | criterion="entropy", n_estimators=320, min_samples_leaf=1, max_features="log2"  |
|          0.779 |         0.056 | criterion="entropy", n_estimators=40, min_samples_leaf=1, max_features="log2"   |
|          0.779 |         0.065 | criterion="entropy", n_estimators=160, min_samples_leaf=1, max_features="log2"  |
|          0.778 |         0.062 | criterion="gini", n_estimators=40, min_samples_leaf=1, max_features="log2"      |
|          0.777 |         0.066 | criterion="gini", n_estimators=160, min_samples_leaf=1, max_features="log2"     |
|          0.776 |         0.067 | criterion="gini", n_estimators=640, min_samples_leaf=1, max_features="log2"     |
|          0.776 |         0.055 | criterion="entropy", n_estimators=10, min_samples_leaf=3, max_features="log2"   |
|          0.776 |         0.073 | criterion="gini", n_estimators=20, min_samples_leaf=3, max_features="log2"      |
|          0.775 |         0.06  | criterion="entropy", n_estimators=20, min_samples_leaf=1, max_features="log2"   |
|          0.766 |         0.061 | criterion="gini", n_estimators=10, min_samples_leaf=1, max_features="log2"      |
|          0.763 |         0.081 | criterion="gini", n_estimators=10, min_samples_leaf=3, max_features="log2"      |
|          0.757 |         0.06  | criterion="entropy", n_estimators=10, min_samples_leaf=1, max_features="log2"   |

## LogisticRegression
|   mean(scores) |   std(scores) | params              |
|---------------:|--------------:|:--------------------|
|          0.706 |         0.055 | C=1, penalty="l1"   |
|          0.705 |         0.045 | C=0.1, penalty="l2" |
|          0.705 |         0.056 | C=10, penalty="l2"  |
|          0.705 |         0.058 | C=10, penalty="l1"  |
|          0.704 |         0.054 | C=1, penalty="l2"   |
|          0.698 |         0.051 | C=0.1, penalty="l1" |

## GradientBoostingClassifier
|   mean(scores) |   std(scores) | params                                                                 |
|---------------:|--------------:|:-----------------------------------------------------------------------|
|          0.8   |         0.06  | max_depth=1, max_features="log2", learning_rate=0.5, n_estimators=100  |
|          0.799 |         0.05  | max_depth=1, max_features="log2", learning_rate=0.1, n_estimators=300  |
|          0.795 |         0.061 | max_depth=3, max_features="log2", learning_rate=0.01, n_estimators=500 |
|          0.794 |         0.055 | max_depth=1, max_features="log2", learning_rate=0.1, n_estimators=700  |
|          0.794 |         0.058 | max_depth=1, max_features="log2", learning_rate=0.1, n_estimators=500  |
|          0.794 |         0.054 | max_depth=3, max_features="log2", learning_rate=0.01, n_estimators=300 |
|          0.791 |         0.058 | max_depth=5, max_features="log2", learning_rate=0.01, n_estimators=100 |
|          0.79  |         0.065 | max_depth=7, max_features="log2", learning_rate=0.01, n_estimators=300 |
|          0.79  |         0.064 | max_depth=3, max_features="log2", learning_rate=0.01, n_estimators=700 |
|          0.789 |         0.061 | max_depth=5, max_features="log2", learning_rate=0.01, n_estimators=300 |
|          0.788 |         0.039 | max_depth=1, max_features="log2", learning_rate=0.1, n_estimators=100  |
|          0.788 |         0.062 | max_depth=5, max_features="log2", learning_rate=0.01, n_estimators=500 |
|          0.786 |         0.061 | max_depth=7, max_features="log2", learning_rate=0.01, n_estimators=100 |
|          0.785 |         0.06  | max_depth=1, max_features="log2", learning_rate=1, n_estimators=100    |
|          0.785 |         0.064 | max_depth=7, max_features="log2", learning_rate=0.01, n_estimators=500 |
|          0.784 |         0.062 | max_depth=3, max_features="log2", learning_rate=0.1, n_estimators=100  |
|          0.783 |         0.061 | max_depth=7, max_features="log2", learning_rate=0.1, n_estimators=100  |
|          0.783 |         0.065 | max_depth=7, max_features="log2", learning_rate=0.01, n_estimators=700 |
|          0.781 |         0.066 | max_depth=5, max_features="log2", learning_rate=0.1, n_estimators=100  |
|          0.779 |         0.069 | max_depth=5, max_features="log2", learning_rate=0.01, n_estimators=700 |
|          0.778 |         0.058 | max_depth=5, max_features="log2", learning_rate=0.1, n_estimators=700  |
|          0.778 |         0.069 | max_depth=1, max_features="log2", learning_rate=0.5, n_estimators=300  |
|          0.778 |         0.042 | max_depth=3, max_features="log2", learning_rate=0.01, n_estimators=100 |
|          0.777 |         0.06  | max_depth=7, max_features="log2", learning_rate=0.1, n_estimators=300  |
|          0.777 |         0.059 | max_depth=7, max_features="log2", learning_rate=0.1, n_estimators=500  |
|          0.776 |         0.063 | max_depth=7, max_features="log2", learning_rate=0.1, n_estimators=700  |
|          0.775 |         0.059 | max_depth=5, max_features="log2", learning_rate=0.1, n_estimators=300  |
|          0.775 |         0.041 | max_depth=1, max_features="log2", learning_rate=0.01, n_estimators=700 |
|          0.775 |         0.067 | max_depth=1, max_features="log2", learning_rate=0.5, n_estimators=500  |
|          0.773 |         0.058 | max_depth=5, max_features="log2", learning_rate=0.1, n_estimators=500  |
|          0.773 |         0.069 | max_depth=3, max_features="log2", learning_rate=0.1, n_estimators=300  |
|          0.772 |         0.058 | max_depth=7, max_features="log2", learning_rate=0.5, n_estimators=500  |
|          0.771 |         0.065 | max_depth=5, max_features="log2", learning_rate=0.5, n_estimators=300  |
|          0.771 |         0.063 | max_depth=7, max_features="log2", learning_rate=0.5, n_estimators=100  |
|          0.77  |         0.07  | max_depth=1, max_features="log2", learning_rate=0.5, n_estimators=700  |
|          0.769 |         0.06  | max_depth=7, max_features="log2", learning_rate=0.5, n_estimators=300  |
|          0.768 |         0.064 | max_depth=5, max_features="log2", learning_rate=0.5, n_estimators=100  |
|          0.767 |         0.041 | max_depth=1, max_features="log2", learning_rate=0.01, n_estimators=500 |
|          0.766 |         0.063 | max_depth=7, max_features="log2", learning_rate=0.5, n_estimators=700  |
|          0.766 |         0.072 | max_depth=3, max_features="log2", learning_rate=0.1, n_estimators=700  |
|          0.765 |         0.063 | max_depth=5, max_features="log2", learning_rate=0.5, n_estimators=500  |
|          0.765 |         0.077 | max_depth=3, max_features="log2", learning_rate=0.1, n_estimators=500  |
|          0.764 |         0.068 | max_depth=1, max_features="log2", learning_rate=1, n_estimators=300    |
|          0.763 |         0.067 | max_depth=3, max_features="log2", learning_rate=0.5, n_estimators=100  |
|          0.76  |         0.071 | max_depth=1, max_features="log2", learning_rate=1, n_estimators=700    |
|          0.755 |         0.073 | max_depth=1, max_features="log2", learning_rate=1, n_estimators=500    |
|          0.743 |         0.037 | max_depth=1, max_features="log2", learning_rate=0.01, n_estimators=300 |
|          0.715 |         0.045 | max_depth=1, max_features="log2", learning_rate=0.01, n_estimators=100 |
|          0.699 |         0.139 | max_depth=3, max_features="log2", learning_rate=0.5, n_estimators=700  |
|          0.684 |         0.138 | max_depth=7, max_features="log2", learning_rate=1, n_estimators=100    |
|          0.65  |         0.206 | max_depth=7, max_features="log2", learning_rate=1, n_estimators=700    |
|          0.592 |         0.193 | max_depth=7, max_features="log2", learning_rate=1, n_estimators=500    |
|          0.588 |         0.173 | max_depth=3, max_features="log2", learning_rate=0.5, n_estimators=500  |
|          0.57  |         0.195 | max_depth=5, max_features="log2", learning_rate=0.5, n_estimators=700  |
|          0.515 |         0.281 | max_depth=3, max_features="log2", learning_rate=0.5, n_estimators=300  |
|          0.503 |         0.273 | max_depth=7, max_features="log2", learning_rate=1, n_estimators=300    |
|          0.482 |         0.302 | max_depth=3, max_features="log2", learning_rate=1, n_estimators=500    |
|          0.47  |         0.187 | max_depth=5, max_features="log2", learning_rate=1, n_estimators=300    |
|          0.469 |         0.258 | max_depth=5, max_features="log2", learning_rate=1, n_estimators=500    |
|          0.444 |         0.282 | max_depth=3, max_features="log2", learning_rate=1, n_estimators=700    |
|          0.426 |         0.171 | max_depth=5, max_features="log2", learning_rate=1, n_estimators=100    |
|          0.378 |         0.219 | max_depth=5, max_features="log2", learning_rate=1, n_estimators=700    |
|          0.357 |         0.292 | max_depth=3, max_features="log2", learning_rate=1, n_estimators=100    |
|          0.276 |         0.14  | max_depth=3, max_features="log2", learning_rate=1, n_estimators=300    |

