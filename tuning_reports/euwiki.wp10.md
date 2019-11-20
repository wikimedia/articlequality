# Model tuning report
- Revscoring version: 2.6.1
- Features: articlequality.feature_lists.euwiki.wp10
- Date: 2019-11-05T06:43:28.787483
- Observations: 454
- Labels: ["Stub", "Start", "C", "B", "GA", "FA"]
- Statistic: accuracy.macro (maximize)
- Folds: 5

# Top scoring configurations
| model                  |   accuracy.macro | params                                                                         |
|:-----------------------|-----------------:|:-------------------------------------------------------------------------------|
| RandomForestClassifier |           0.9075 | min_samples_leaf=3, max_features="log2", n_estimators=320, criterion="gini"    |
| RandomForestClassifier |           0.9075 | min_samples_leaf=3, max_features="log2", n_estimators=160, criterion="gini"    |
| RandomForestClassifier |           0.9075 | min_samples_leaf=3, max_features="log2", n_estimators=160, criterion="entropy" |
| RandomForestClassifier |           0.9075 | min_samples_leaf=5, max_features="log2", n_estimators=160, criterion="entropy" |
| RandomForestClassifier |           0.9068 | min_samples_leaf=7, max_features="log2", n_estimators=320, criterion="gini"    |
| RandomForestClassifier |           0.9068 | min_samples_leaf=5, max_features="log2", n_estimators=320, criterion="entropy" |
| RandomForestClassifier |           0.9068 | min_samples_leaf=7, max_features="log2", n_estimators=640, criterion="entropy" |
| RandomForestClassifier |           0.906  | min_samples_leaf=3, max_features="log2", n_estimators=320, criterion="entropy" |
| RandomForestClassifier |           0.906  | min_samples_leaf=5, max_features="log2", n_estimators=80, criterion="entropy"  |
| RandomForestClassifier |           0.906  | min_samples_leaf=5, max_features="log2", n_estimators=640, criterion="entropy" |

# Models
## LogisticRegression
|   accuracy.macro | params              |
|-----------------:|:--------------------|
|           0.8568 | C=10, penalty="l1"  |
|           0.8524 | C=1, penalty="l1"   |
|           0.8524 | C=10, penalty="l2"  |
|           0.8517 | C=1, penalty="l2"   |
|           0.851  | C=0.1, penalty="l2" |
|           0.851  | C=0.1, penalty="l1" |

## RandomForestClassifier
|   accuracy.macro | params                                                                          |
|-----------------:|:--------------------------------------------------------------------------------|
|           0.9075 | min_samples_leaf=3, max_features="log2", n_estimators=320, criterion="gini"     |
|           0.9075 | min_samples_leaf=3, max_features="log2", n_estimators=160, criterion="gini"     |
|           0.9075 | min_samples_leaf=3, max_features="log2", n_estimators=160, criterion="entropy"  |
|           0.9075 | min_samples_leaf=5, max_features="log2", n_estimators=160, criterion="entropy"  |
|           0.9068 | min_samples_leaf=7, max_features="log2", n_estimators=320, criterion="gini"     |
|           0.9068 | min_samples_leaf=5, max_features="log2", n_estimators=320, criterion="entropy"  |
|           0.9068 | min_samples_leaf=7, max_features="log2", n_estimators=640, criterion="entropy"  |
|           0.906  | min_samples_leaf=3, max_features="log2", n_estimators=320, criterion="entropy"  |
|           0.906  | min_samples_leaf=5, max_features="log2", n_estimators=80, criterion="entropy"   |
|           0.906  | min_samples_leaf=5, max_features="log2", n_estimators=640, criterion="entropy"  |
|           0.9053 | min_samples_leaf=3, max_features="log2", n_estimators=80, criterion="entropy"   |
|           0.9053 | min_samples_leaf=5, max_features="log2", n_estimators=640, criterion="gini"     |
|           0.9053 | min_samples_leaf=3, max_features="log2", n_estimators=640, criterion="gini"     |
|           0.9046 | min_samples_leaf=5, max_features="log2", n_estimators=320, criterion="gini"     |
|           0.9046 | min_samples_leaf=3, max_features="log2", n_estimators=640, criterion="entropy"  |
|           0.9038 | min_samples_leaf=7, max_features="log2", n_estimators=320, criterion="entropy"  |
|           0.9038 | min_samples_leaf=13, max_features="log2", n_estimators=160, criterion="entropy" |
|           0.9031 | min_samples_leaf=5, max_features="log2", n_estimators=160, criterion="gini"     |
|           0.9031 | min_samples_leaf=7, max_features="log2", n_estimators=40, criterion="entropy"   |
|           0.9031 | min_samples_leaf=7, max_features="log2", n_estimators=160, criterion="entropy"  |
|           0.9023 | min_samples_leaf=3, max_features="log2", n_estimators=80, criterion="gini"      |
|           0.9023 | min_samples_leaf=5, max_features="log2", n_estimators=40, criterion="gini"      |
|           0.9023 | min_samples_leaf=7, max_features="log2", n_estimators=640, criterion="gini"     |
|           0.9023 | min_samples_leaf=7, max_features="log2", n_estimators=80, criterion="entropy"   |
|           0.9023 | min_samples_leaf=13, max_features="log2", n_estimators=640, criterion="entropy" |
|           0.9016 | min_samples_leaf=1, max_features="log2", n_estimators=160, criterion="gini"     |
|           0.9016 | min_samples_leaf=5, max_features="log2", n_estimators=20, criterion="entropy"   |
|           0.9016 | min_samples_leaf=1, max_features="log2", n_estimators=160, criterion="entropy"  |
|           0.9009 | min_samples_leaf=5, max_features="log2", n_estimators=80, criterion="gini"      |
|           0.9009 | min_samples_leaf=13, max_features="log2", n_estimators=320, criterion="entropy" |
|           0.9009 | min_samples_leaf=1, max_features="log2", n_estimators=320, criterion="gini"     |
|           0.9009 | min_samples_leaf=7, max_features="log2", n_estimators=160, criterion="gini"     |
|           0.9009 | min_samples_leaf=1, max_features="log2", n_estimators=80, criterion="entropy"   |
|           0.9001 | min_samples_leaf=13, max_features="log2", n_estimators=80, criterion="entropy"  |
|           0.9001 | min_samples_leaf=1, max_features="log2", n_estimators=640, criterion="entropy"  |
|           0.8994 | min_samples_leaf=13, max_features="log2", n_estimators=320, criterion="gini"    |
|           0.8994 | min_samples_leaf=3, max_features="log2", n_estimators=40, criterion="gini"      |
|           0.8987 | min_samples_leaf=1, max_features="log2", n_estimators=640, criterion="gini"     |
|           0.8987 | min_samples_leaf=5, max_features="log2", n_estimators=20, criterion="gini"      |
|           0.8987 | min_samples_leaf=1, max_features="log2", n_estimators=320, criterion="entropy"  |
|           0.8987 | min_samples_leaf=3, max_features="log2", n_estimators=40, criterion="entropy"   |
|           0.8987 | min_samples_leaf=13, max_features="log2", n_estimators=10, criterion="entropy"  |
|           0.8979 | min_samples_leaf=5, max_features="log2", n_estimators=40, criterion="entropy"   |
|           0.8979 | min_samples_leaf=13, max_features="log2", n_estimators=40, criterion="entropy"  |
|           0.8979 | min_samples_leaf=7, max_features="log2", n_estimators=80, criterion="gini"      |
|           0.8979 | min_samples_leaf=13, max_features="log2", n_estimators=160, criterion="gini"    |
|           0.8979 | min_samples_leaf=1, max_features="log2", n_estimators=20, criterion="entropy"   |
|           0.8979 | min_samples_leaf=1, max_features="log2", n_estimators=40, criterion="entropy"   |
|           0.8972 | min_samples_leaf=3, max_features="log2", n_estimators=20, criterion="gini"      |
|           0.8972 | min_samples_leaf=13, max_features="log2", n_estimators=640, criterion="gini"    |
|           0.8965 | min_samples_leaf=13, max_features="log2", n_estimators=40, criterion="gini"     |
|           0.8965 | min_samples_leaf=13, max_features="log2", n_estimators=80, criterion="gini"     |
|           0.8965 | min_samples_leaf=7, max_features="log2", n_estimators=20, criterion="entropy"   |
|           0.8957 | min_samples_leaf=13, max_features="log2", n_estimators=20, criterion="entropy"  |
|           0.895  | min_samples_leaf=7, max_features="log2", n_estimators=10, criterion="gini"      |
|           0.895  | min_samples_leaf=7, max_features="log2", n_estimators=20, criterion="gini"      |
|           0.895  | min_samples_leaf=7, max_features="log2", n_estimators=10, criterion="entropy"   |
|           0.8928 | min_samples_leaf=1, max_features="log2", n_estimators=40, criterion="gini"      |
|           0.8928 | min_samples_leaf=13, max_features="log2", n_estimators=20, criterion="gini"     |
|           0.8928 | min_samples_leaf=3, max_features="log2", n_estimators=10, criterion="entropy"   |
|           0.8928 | min_samples_leaf=3, max_features="log2", n_estimators=20, criterion="entropy"   |
|           0.8921 | min_samples_leaf=3, max_features="log2", n_estimators=10, criterion="gini"      |
|           0.8921 | min_samples_leaf=1, max_features="log2", n_estimators=10, criterion="gini"      |
|           0.8906 | min_samples_leaf=7, max_features="log2", n_estimators=40, criterion="gini"      |
|           0.8899 | min_samples_leaf=1, max_features="log2", n_estimators=80, criterion="gini"      |
|           0.8899 | min_samples_leaf=5, max_features="log2", n_estimators=10, criterion="gini"      |
|           0.8891 | min_samples_leaf=5, max_features="log2", n_estimators=10, criterion="entropy"   |
|           0.8884 | min_samples_leaf=13, max_features="log2", n_estimators=10, criterion="gini"     |
|           0.8855 | min_samples_leaf=1, max_features="log2", n_estimators=20, criterion="gini"      |
|           0.8855 | min_samples_leaf=1, max_features="log2", n_estimators=10, criterion="entropy"   |

## GradientBoosting
|   accuracy.macro | params                                                                 |
|-----------------:|:-----------------------------------------------------------------------|
|           0.906  | max_features="log2", learning_rate=0.01, n_estimators=500, max_depth=1 |
|           0.9038 | max_features="log2", learning_rate=0.01, n_estimators=100, max_depth=3 |
|           0.9031 | max_features="log2", learning_rate=0.01, n_estimators=700, max_depth=1 |
|           0.9001 | max_features="log2", learning_rate=0.01, n_estimators=300, max_depth=3 |
|           0.8987 | max_features="log2", learning_rate=0.01, n_estimators=500, max_depth=3 |
|           0.8987 | max_features="log2", learning_rate=0.01, n_estimators=300, max_depth=1 |
|           0.8979 | max_features="log2", learning_rate=0.1, n_estimators=100, max_depth=1  |
|           0.8972 | max_features="log2", learning_rate=0.01, n_estimators=300, max_depth=7 |
|           0.8972 | max_features="log2", learning_rate=0.1, n_estimators=100, max_depth=5  |
|           0.8965 | max_features="log2", learning_rate=0.1, n_estimators=500, max_depth=5  |
|           0.8965 | max_features="log2", learning_rate=0.1, n_estimators=100, max_depth=3  |
|           0.8957 | max_features="log2", learning_rate=0.01, n_estimators=300, max_depth=5 |
|           0.8957 | max_features="log2", learning_rate=0.01, n_estimators=700, max_depth=7 |
|           0.8957 | max_features="log2", learning_rate=0.5, n_estimators=100, max_depth=5  |
|           0.895  | max_features="log2", learning_rate=0.01, n_estimators=500, max_depth=5 |
|           0.895  | max_features="log2", learning_rate=0.1, n_estimators=300, max_depth=5  |
|           0.895  | max_features="log2", learning_rate=0.1, n_estimators=300, max_depth=7  |
|           0.895  | max_features="log2", learning_rate=0.1, n_estimators=100, max_depth=7  |
|           0.8943 | max_features="log2", learning_rate=0.01, n_estimators=100, max_depth=5 |
|           0.8943 | max_features="log2", learning_rate=0.01, n_estimators=500, max_depth=7 |
|           0.8943 | max_features="log2", learning_rate=0.1, n_estimators=700, max_depth=5  |
|           0.8943 | max_features="log2", learning_rate=0.01, n_estimators=700, max_depth=3 |
|           0.8935 | max_features="log2", learning_rate=0.01, n_estimators=700, max_depth=5 |
|           0.8921 | max_features="log2", learning_rate=0.1, n_estimators=500, max_depth=7  |
|           0.8921 | max_features="log2", learning_rate=0.01, n_estimators=100, max_depth=7 |
|           0.8921 | max_features="log2", learning_rate=0.5, n_estimators=500, max_depth=3  |
|           0.8913 | max_features="log2", learning_rate=0.1, n_estimators=700, max_depth=3  |
|           0.8913 | max_features="log2", learning_rate=0.01, n_estimators=100, max_depth=1 |
|           0.8913 | max_features="log2", learning_rate=0.1, n_estimators=500, max_depth=3  |
|           0.8913 | max_features="log2", learning_rate=0.1, n_estimators=700, max_depth=7  |
|           0.8906 | max_features="log2", learning_rate=0.5, n_estimators=300, max_depth=3  |
|           0.8906 | max_features="log2", learning_rate=0.5, n_estimators=700, max_depth=7  |
|           0.8899 | max_features="log2", learning_rate=0.1, n_estimators=300, max_depth=3  |
|           0.8899 | max_features="log2", learning_rate=0.5, n_estimators=300, max_depth=5  |
|           0.8884 | max_features="log2", learning_rate=0.5, n_estimators=700, max_depth=3  |
|           0.8877 | max_features="log2", learning_rate=0.1, n_estimators=500, max_depth=1  |
|           0.8869 | max_features="log2", learning_rate=0.1, n_estimators=300, max_depth=1  |
|           0.8869 | max_features="log2", learning_rate=0.5, n_estimators=100, max_depth=1  |
|           0.8869 | max_features="log2", learning_rate=0.5, n_estimators=700, max_depth=5  |
|           0.8862 | max_features="log2", learning_rate=0.5, n_estimators=500, max_depth=7  |
|           0.8862 | max_features="log2", learning_rate=1, n_estimators=500, max_depth=7    |
|           0.8855 | max_features="log2", learning_rate=1, n_estimators=500, max_depth=5    |
|           0.8847 | max_features="log2", learning_rate=1, n_estimators=700, max_depth=3    |
|           0.8847 | max_features="log2", learning_rate=0.1, n_estimators=700, max_depth=1  |
|           0.884  | max_features="log2", learning_rate=0.5, n_estimators=500, max_depth=5  |
|           0.884  | max_features="log2", learning_rate=0.5, n_estimators=300, max_depth=7  |
|           0.884  | max_features="log2", learning_rate=1, n_estimators=100, max_depth=3    |
|           0.8833 | max_features="log2", learning_rate=0.5, n_estimators=100, max_depth=7  |
|           0.8833 | max_features="log2", learning_rate=1, n_estimators=500, max_depth=1    |
|           0.8825 | max_features="log2", learning_rate=0.5, n_estimators=100, max_depth=3  |
|           0.8825 | max_features="log2", learning_rate=1, n_estimators=300, max_depth=5    |
|           0.8818 | max_features="log2", learning_rate=1, n_estimators=100, max_depth=5    |
|           0.8811 | max_features="log2", learning_rate=0.5, n_estimators=300, max_depth=1  |
|           0.8803 | max_features="log2", learning_rate=1, n_estimators=700, max_depth=1    |
|           0.8796 | max_features="log2", learning_rate=1, n_estimators=300, max_depth=3    |
|           0.8789 | max_features="log2", learning_rate=0.5, n_estimators=500, max_depth=1  |
|           0.8789 | max_features="log2", learning_rate=0.5, n_estimators=700, max_depth=1  |
|           0.8781 | max_features="log2", learning_rate=1, n_estimators=700, max_depth=5    |
|           0.8781 | max_features="log2", learning_rate=1, n_estimators=100, max_depth=7    |
|           0.8774 | max_features="log2", learning_rate=1, n_estimators=500, max_depth=3    |
|           0.8767 | max_features="log2", learning_rate=1, n_estimators=300, max_depth=7    |
|           0.8759 | max_features="log2", learning_rate=1, n_estimators=100, max_depth=1    |
|           0.8722 | max_features="log2", learning_rate=1, n_estimators=300, max_depth=1    |
|           0.8708 | max_features="log2", learning_rate=1, n_estimators=700, max_depth=7    |

## GaussianNB
|   accuracy.macro | params   |
|-----------------:|:---------|
|           0.8216 |          |

## BernoulliNB
|   accuracy.macro | params   |
|-----------------:|:---------|
|           0.7863 |          |

