# Model tuning report
- Revscoring version: 1.3.15
- Features: articlequality.feature_lists.wikidatawiki.item_quality
- Date: 2017-06-30T16:21:20.213856
- Observations: 4996
- Labels: ["E", "D", "C", "A", "B"]
- Scoring: accuracy
- Folds: 5

# Top scoring configurations
| model                  |   mean(scores) |   std(scores) | params                                                                          |
|:-----------------------|---------------:|--------------:|:--------------------------------------------------------------------------------|
| RandomForestClassifier |          0.883 |         0.028 | max_features="log2", criterion="entropy", min_samples_leaf=13, n_estimators=160 |
| RandomForestClassifier |          0.883 |         0.024 | max_features="log2", criterion="entropy", min_samples_leaf=13, n_estimators=10  |
| RandomForestClassifier |          0.882 |         0.028 | max_features="log2", criterion="entropy", min_samples_leaf=7, n_estimators=20   |
| RandomForestClassifier |          0.881 |         0.033 | max_features="log2", criterion="entropy", min_samples_leaf=13, n_estimators=20  |
| RandomForestClassifier |          0.878 |         0.036 | max_features="log2", criterion="gini", min_samples_leaf=13, n_estimators=320    |
| RandomForestClassifier |          0.878 |         0.041 | max_features="log2", criterion="gini", min_samples_leaf=7, n_estimators=20      |
| RandomForestClassifier |          0.878 |         0.034 | max_features="log2", criterion="entropy", min_samples_leaf=13, n_estimators=320 |
| RandomForestClassifier |          0.877 |         0.039 | max_features="log2", criterion="gini", min_samples_leaf=7, n_estimators=320     |
| RandomForestClassifier |          0.877 |         0.041 | max_features="log2", criterion="gini", min_samples_leaf=7, n_estimators=10      |
| RandomForestClassifier |          0.876 |         0.036 | max_features="log2", criterion="gini", min_samples_leaf=13, n_estimators=80     |

# Models
## LogisticRegression
|   mean(scores) |   std(scores) | params              |
|---------------:|--------------:|:--------------------|
|          0.768 |         0.053 | C=10, penalty="l1"  |
|          0.766 |         0.053 | C=1, penalty="l1"   |
|          0.751 |         0.057 | C=0.1, penalty="l1" |
|          0.746 |         0.04  | C=10, penalty="l2"  |
|          0.744 |         0.056 | C=1, penalty="l2"   |
|          0.736 |         0.046 | C=0.1, penalty="l2" |

## SVC
|   mean(scores) |   std(scores) | params                                                               |
|---------------:|--------------:|:---------------------------------------------------------------------|
|          0.77  |         0.063 | C=10, probability=true, gamma=0.001, kernel="rbf", cache_size=1000   |
|          0.722 |         0.058 | C=1, probability=true, gamma=0.0, kernel="rbf", cache_size=1000      |
|          0.72  |         0.063 | C=10, probability=true, gamma=0.0, kernel="rbf", cache_size=1000     |
|          0.709 |         0.106 | C=0.1, probability=true, gamma=0.001, kernel="rbf", cache_size=1000  |
|          0.707 |         0.081 | C=1, probability=true, gamma=0.001, kernel="rbf", cache_size=1000    |
|          0.7   |         0.073 | C=10, probability=true, gamma=0.0001, kernel="rbf", cache_size=1000  |
|          0.678 |         0.079 | C=1, probability=true, gamma=0.0001, kernel="rbf", cache_size=1000   |
|          0.654 |         0.07  | C=0.1, probability=true, gamma=0.0, kernel="rbf", cache_size=1000    |
|          0.617 |         0.1   | C=0.1, probability=true, gamma=0.0001, kernel="rbf", cache_size=1000 |

## GradientBoostingClassifier
|   mean(scores) |   std(scores) | params                                                                 |
|---------------:|--------------:|:-----------------------------------------------------------------------|
|          0.865 |         0.046 | max_features="log2", learning_rate=0.01, max_depth=3, n_estimators=100 |
|          0.859 |         0.05  | max_features="log2", learning_rate=0.01, max_depth=3, n_estimators=300 |
|          0.857 |         0.062 | max_features="log2", learning_rate=0.01, max_depth=3, n_estimators=700 |
|          0.856 |         0.062 | max_features="log2", learning_rate=0.01, max_depth=5, n_estimators=300 |
|          0.854 |         0.06  | max_features="log2", learning_rate=0.01, max_depth=5, n_estimators=500 |
|          0.854 |         0.061 | max_features="log2", learning_rate=0.1, max_depth=1, n_estimators=700  |
|          0.854 |         0.065 | max_features="log2", learning_rate=0.1, max_depth=3, n_estimators=100  |
|          0.852 |         0.057 | max_features="log2", learning_rate=0.01, max_depth=5, n_estimators=100 |
|          0.852 |         0.067 | max_features="log2", learning_rate=0.01, max_depth=3, n_estimators=500 |
|          0.851 |         0.065 | max_features="log2", learning_rate=0.1, max_depth=1, n_estimators=500  |
|          0.848 |         0.043 | max_features="log2", learning_rate=0.1, max_depth=1, n_estimators=100  |
|          0.848 |         0.063 | max_features="log2", learning_rate=0.01, max_depth=5, n_estimators=700 |
|          0.847 |         0.066 | max_features="log2", learning_rate=0.01, max_depth=7, n_estimators=100 |
|          0.847 |         0.064 | max_features="log2", learning_rate=0.1, max_depth=1, n_estimators=300  |
|          0.845 |         0.063 | max_features="log2", learning_rate=0.1, max_depth=3, n_estimators=300  |
|          0.844 |         0.068 | max_features="log2", learning_rate=0.5, max_depth=1, n_estimators=100  |
|          0.844 |         0.069 | max_features="log2", learning_rate=0.5, max_depth=1, n_estimators=300  |
|          0.844 |         0.071 | max_features="log2", learning_rate=1, max_depth=1, n_estimators=100    |
|          0.843 |         0.058 | max_features="log2", learning_rate=0.1, max_depth=5, n_estimators=100  |
|          0.843 |         0.065 | max_features="log2", learning_rate=0.01, max_depth=7, n_estimators=300 |
|          0.841 |         0.06  | max_features="log2", learning_rate=0.01, max_depth=7, n_estimators=500 |
|          0.838 |         0.057 | max_features="log2", learning_rate=0.1, max_depth=7, n_estimators=100  |
|          0.838 |         0.055 | max_features="log2", learning_rate=0.01, max_depth=7, n_estimators=700 |
|          0.838 |         0.054 | max_features="log2", learning_rate=0.1, max_depth=5, n_estimators=300  |
|          0.837 |         0.055 | max_features="log2", learning_rate=0.1, max_depth=5, n_estimators=500  |
|          0.836 |         0.058 | max_features="log2", learning_rate=0.1, max_depth=3, n_estimators=700  |
|          0.836 |         0.063 | max_features="log2", learning_rate=0.1, max_depth=3, n_estimators=500  |
|          0.835 |         0.054 | max_features="log2", learning_rate=0.1, max_depth=7, n_estimators=500  |
|          0.835 |         0.075 | max_features="log2", learning_rate=0.5, max_depth=1, n_estimators=500  |
|          0.835 |         0.074 | max_features="log2", learning_rate=0.5, max_depth=1, n_estimators=700  |
|          0.834 |         0.056 | max_features="log2", learning_rate=0.1, max_depth=7, n_estimators=700  |
|          0.833 |         0.056 | max_features="log2", learning_rate=0.1, max_depth=7, n_estimators=300  |
|          0.832 |         0.054 | max_features="log2", learning_rate=0.5, max_depth=5, n_estimators=300  |
|          0.832 |         0.054 | max_features="log2", learning_rate=0.01, max_depth=1, n_estimators=700 |
|          0.832 |         0.057 | max_features="log2", learning_rate=0.5, max_depth=5, n_estimators=100  |
|          0.832 |         0.072 | max_features="log2", learning_rate=1, max_depth=1, n_estimators=300    |
|          0.831 |         0.054 | max_features="log2", learning_rate=0.5, max_depth=7, n_estimators=300  |
|          0.829 |         0.058 | max_features="log2", learning_rate=0.1, max_depth=5, n_estimators=700  |
|          0.828 |         0.054 | max_features="log2", learning_rate=0.5, max_depth=7, n_estimators=500  |
|          0.827 |         0.053 | max_features="log2", learning_rate=0.5, max_depth=7, n_estimators=700  |
|          0.826 |         0.059 | max_features="log2", learning_rate=0.5, max_depth=7, n_estimators=100  |
|          0.826 |         0.058 | max_features="log2", learning_rate=0.5, max_depth=5, n_estimators=500  |
|          0.825 |         0.06  | max_features="log2", learning_rate=0.5, max_depth=5, n_estimators=700  |
|          0.824 |         0.063 | max_features="log2", learning_rate=0.5, max_depth=3, n_estimators=700  |
|          0.816 |         0.055 | max_features="log2", learning_rate=0.01, max_depth=1, n_estimators=500 |
|          0.816 |         0.05  | max_features="log2", learning_rate=0.5, max_depth=3, n_estimators=100  |
|          0.816 |         0.067 | max_features="log2", learning_rate=1, max_depth=7, n_estimators=500    |
|          0.815 |         0.069 | max_features="log2", learning_rate=1, max_depth=1, n_estimators=700    |
|          0.776 |         0.04  | max_features="log2", learning_rate=0.01, max_depth=1, n_estimators=300 |
|          0.773 |         0.152 | max_features="log2", learning_rate=0.5, max_depth=3, n_estimators=300  |
|          0.758 |         0.059 | max_features="log2", learning_rate=0.01, max_depth=1, n_estimators=100 |
|          0.721 |         0.186 | max_features="log2", learning_rate=0.5, max_depth=3, n_estimators=500  |
|          0.716 |         0.281 | max_features="log2", learning_rate=1, max_depth=1, n_estimators=500    |
|          0.703 |         0.255 | max_features="log2", learning_rate=1, max_depth=3, n_estimators=100    |
|          0.692 |         0.165 | max_features="log2", learning_rate=1, max_depth=7, n_estimators=100    |
|          0.679 |         0.252 | max_features="log2", learning_rate=1, max_depth=7, n_estimators=300    |
|          0.65  |         0.211 | max_features="log2", learning_rate=1, max_depth=5, n_estimators=300    |
|          0.643 |         0.25  | max_features="log2", learning_rate=1, max_depth=7, n_estimators=700    |
|          0.576 |         0.291 | max_features="log2", learning_rate=1, max_depth=3, n_estimators=700    |
|          0.557 |         0.291 | max_features="log2", learning_rate=1, max_depth=5, n_estimators=700    |
|          0.482 |         0.283 | max_features="log2", learning_rate=1, max_depth=3, n_estimators=500    |
|          0.457 |         0.272 | max_features="log2", learning_rate=1, max_depth=5, n_estimators=500    |
|          0.427 |         0.299 | max_features="log2", learning_rate=1, max_depth=3, n_estimators=300    |
|          0.368 |         0.112 | max_features="log2", learning_rate=1, max_depth=5, n_estimators=100    |

## RandomForestClassifier
|   mean(scores) |   std(scores) | params                                                                          |
|---------------:|--------------:|:--------------------------------------------------------------------------------|
|          0.883 |         0.028 | max_features="log2", criterion="entropy", min_samples_leaf=13, n_estimators=160 |
|          0.883 |         0.024 | max_features="log2", criterion="entropy", min_samples_leaf=13, n_estimators=10  |
|          0.882 |         0.028 | max_features="log2", criterion="entropy", min_samples_leaf=7, n_estimators=20   |
|          0.881 |         0.033 | max_features="log2", criterion="entropy", min_samples_leaf=13, n_estimators=20  |
|          0.878 |         0.036 | max_features="log2", criterion="gini", min_samples_leaf=13, n_estimators=320    |
|          0.878 |         0.041 | max_features="log2", criterion="gini", min_samples_leaf=7, n_estimators=20      |
|          0.878 |         0.034 | max_features="log2", criterion="entropy", min_samples_leaf=13, n_estimators=320 |
|          0.877 |         0.039 | max_features="log2", criterion="gini", min_samples_leaf=7, n_estimators=320     |
|          0.877 |         0.041 | max_features="log2", criterion="gini", min_samples_leaf=7, n_estimators=10      |
|          0.876 |         0.036 | max_features="log2", criterion="gini", min_samples_leaf=13, n_estimators=80     |
|          0.876 |         0.038 | max_features="log2", criterion="entropy", min_samples_leaf=7, n_estimators=640  |
|          0.875 |         0.043 | max_features="log2", criterion="gini", min_samples_leaf=13, n_estimators=20     |
|          0.875 |         0.041 | max_features="log2", criterion="gini", min_samples_leaf=7, n_estimators=640     |
|          0.875 |         0.036 | max_features="log2", criterion="entropy", min_samples_leaf=7, n_estimators=40   |
|          0.875 |         0.043 | max_features="log2", criterion="entropy", min_samples_leaf=7, n_estimators=160  |
|          0.875 |         0.04  | max_features="log2", criterion="gini", min_samples_leaf=13, n_estimators=640    |
|          0.874 |         0.041 | max_features="log2", criterion="gini", min_samples_leaf=13, n_estimators=160    |
|          0.873 |         0.033 | max_features="log2", criterion="entropy", min_samples_leaf=13, n_estimators=40  |
|          0.872 |         0.041 | max_features="log2", criterion="entropy", min_samples_leaf=13, n_estimators=640 |
|          0.872 |         0.048 | max_features="log2", criterion="gini", min_samples_leaf=7, n_estimators=160     |
|          0.871 |         0.046 | max_features="log2", criterion="entropy", min_samples_leaf=7, n_estimators=320  |
|          0.87  |         0.043 | max_features="log2", criterion="entropy", min_samples_leaf=7, n_estimators=10   |
|          0.869 |         0.048 | max_features="log2", criterion="gini", min_samples_leaf=7, n_estimators=80      |
|          0.868 |         0.05  | max_features="log2", criterion="entropy", min_samples_leaf=7, n_estimators=80   |
|          0.867 |         0.046 | max_features="log2", criterion="gini", min_samples_leaf=5, n_estimators=160     |
|          0.867 |         0.037 | max_features="log2", criterion="entropy", min_samples_leaf=5, n_estimators=20   |
|          0.867 |         0.048 | max_features="log2", criterion="entropy", min_samples_leaf=13, n_estimators=80  |
|          0.866 |         0.047 | max_features="log2", criterion="gini", min_samples_leaf=5, n_estimators=640     |
|          0.865 |         0.045 | max_features="log2", criterion="entropy", min_samples_leaf=5, n_estimators=160  |
|          0.864 |         0.048 | max_features="log2", criterion="entropy", min_samples_leaf=5, n_estimators=320  |
|          0.864 |         0.054 | max_features="log2", criterion="gini", min_samples_leaf=13, n_estimators=40     |
|          0.863 |         0.046 | max_features="log2", criterion="entropy", min_samples_leaf=5, n_estimators=640  |
|          0.861 |         0.042 | max_features="log2", criterion="gini", min_samples_leaf=13, n_estimators=10     |
|          0.859 |         0.05  | max_features="log2", criterion="entropy", min_samples_leaf=5, n_estimators=80   |
|          0.854 |         0.053 | max_features="log2", criterion="gini", min_samples_leaf=5, n_estimators=40      |
|          0.851 |         0.058 | max_features="log2", criterion="gini", min_samples_leaf=5, n_estimators=320     |
|          0.85  |         0.061 | max_features="log2", criterion="gini", min_samples_leaf=5, n_estimators=80      |
|          0.849 |         0.063 | max_features="log2", criterion="gini", min_samples_leaf=7, n_estimators=40      |
|          0.849 |         0.064 | max_features="log2", criterion="gini", min_samples_leaf=3, n_estimators=160     |
|          0.848 |         0.066 | max_features="log2", criterion="gini", min_samples_leaf=3, n_estimators=80      |
|          0.848 |         0.068 | max_features="log2", criterion="entropy", min_samples_leaf=5, n_estimators=10   |
|          0.848 |         0.064 | max_features="log2", criterion="entropy", min_samples_leaf=3, n_estimators=160  |
|          0.847 |         0.065 | max_features="log2", criterion="gini", min_samples_leaf=3, n_estimators=320     |
|          0.847 |         0.063 | max_features="log2", criterion="entropy", min_samples_leaf=3, n_estimators=640  |
|          0.846 |         0.059 | max_features="log2", criterion="entropy", min_samples_leaf=5, n_estimators=40   |
|          0.846 |         0.065 | max_features="log2", criterion="gini", min_samples_leaf=3, n_estimators=640     |
|          0.846 |         0.062 | max_features="log2", criterion="gini", min_samples_leaf=3, n_estimators=10      |
|          0.846 |         0.065 | max_features="log2", criterion="gini", min_samples_leaf=3, n_estimators=20      |
|          0.844 |         0.065 | max_features="log2", criterion="entropy", min_samples_leaf=3, n_estimators=320  |
|          0.844 |         0.061 | max_features="log2", criterion="entropy", min_samples_leaf=3, n_estimators=20   |
|          0.844 |         0.072 | max_features="log2", criterion="entropy", min_samples_leaf=3, n_estimators=40   |
|          0.844 |         0.069 | max_features="log2", criterion="entropy", min_samples_leaf=3, n_estimators=80   |
|          0.843 |         0.068 | max_features="log2", criterion="gini", min_samples_leaf=3, n_estimators=40      |
|          0.841 |         0.07  | max_features="log2", criterion="gini", min_samples_leaf=5, n_estimators=20      |
|          0.839 |         0.059 | max_features="log2", criterion="gini", min_samples_leaf=1, n_estimators=10      |
|          0.836 |         0.06  | max_features="log2", criterion="entropy", min_samples_leaf=1, n_estimators=40   |
|          0.834 |         0.061 | max_features="log2", criterion="gini", min_samples_leaf=1, n_estimators=80      |
|          0.834 |         0.061 | max_features="log2", criterion="entropy", min_samples_leaf=1, n_estimators=80   |
|          0.834 |         0.063 | max_features="log2", criterion="entropy", min_samples_leaf=1, n_estimators=640  |
|          0.833 |         0.069 | max_features="log2", criterion="entropy", min_samples_leaf=3, n_estimators=10   |
|          0.833 |         0.063 | max_features="log2", criterion="entropy", min_samples_leaf=1, n_estimators=160  |
|          0.832 |         0.069 | max_features="log2", criterion="gini", min_samples_leaf=1, n_estimators=640     |
|          0.832 |         0.067 | max_features="log2", criterion="gini", min_samples_leaf=1, n_estimators=320     |
|          0.832 |         0.055 | max_features="log2", criterion="entropy", min_samples_leaf=1, n_estimators=10   |
|          0.831 |         0.068 | max_features="log2", criterion="entropy", min_samples_leaf=1, n_estimators=20   |
|          0.83  |         0.061 | max_features="log2", criterion="gini", min_samples_leaf=1, n_estimators=40      |
|          0.83  |         0.065 | max_features="log2", criterion="entropy", min_samples_leaf=1, n_estimators=320  |
|          0.83  |         0.069 | max_features="log2", criterion="gini", min_samples_leaf=5, n_estimators=10      |
|          0.829 |         0.066 | max_features="log2", criterion="gini", min_samples_leaf=1, n_estimators=160     |
|          0.826 |         0.07  | max_features="log2", criterion="gini", min_samples_leaf=1, n_estimators=20      |

## BernoulliNB
|   mean(scores) |   std(scores) | params   |
|---------------:|--------------:|:---------|
|           0.66 |         0.044 |          |

## GaussianNB
|   mean(scores) |   std(scores) | params   |
|---------------:|--------------:|:---------|
|           0.65 |         0.072 |          |

