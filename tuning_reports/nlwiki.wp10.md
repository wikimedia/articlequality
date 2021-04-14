# Model tuning report
- Revscoring version: 2.8.2
- Features: articlequality.feature_lists.nlwiki.wp10
- Date: 2021-04-14T16:25:04.789280
- Observations: 1649
- Labels: ["E", "D", "C", "B", "A"]
- Statistic: accuracy.macro (maximize)
- Folds: 5

# Top scoring configurations
| model                  |   accuracy.macro | params                                                                         |
|:-----------------------|-----------------:|:-------------------------------------------------------------------------------|
| RandomForestClassifier |           0.9153 | n_estimators=40, min_samples_leaf=5, criterion="entropy", max_features="log2"  |
| RandomForestClassifier |           0.9153 | n_estimators=20, min_samples_leaf=5, criterion="entropy", max_features="log2"  |
| RandomForestClassifier |           0.9129 | n_estimators=10, min_samples_leaf=5, criterion="gini", max_features="log2"     |
| RandomForestClassifier |           0.911  | n_estimators=20, min_samples_leaf=13, criterion="entropy", max_features="log2" |
| RandomForestClassifier |           0.9107 | n_estimators=10, min_samples_leaf=7, criterion="gini", max_features="log2"     |
| GradientBoosting       |           0.909  | n_estimators=500, max_depth=1, learning_rate=0.01, max_features="log2"         |
| GradientBoosting       |           0.9085 | n_estimators=700, max_depth=1, learning_rate=0.01, max_features="log2"         |
| GradientBoosting       |           0.9066 | n_estimators=300, max_depth=3, learning_rate=0.01, max_features="log2"         |
| GradientBoosting       |           0.9052 | n_estimators=300, max_depth=1, learning_rate=0.01, max_features="log2"         |
| RandomForestClassifier |           0.9047 | n_estimators=160, min_samples_leaf=5, criterion="entropy", max_features="log2" |

# Models
## LogisticRegression
|   accuracy.macro | params              |
|-----------------:|:--------------------|
|           0.878  | C=0.1, penalty="l2" |
|           0.8739 | C=1, penalty="l2"   |
|           0.8734 | C=10, penalty="l2"  |

## BernoulliNB
|   accuracy.macro | params   |
|-----------------:|:---------|
|           0.8918 |          |

## RandomForestClassifier
|   accuracy.macro | params                                                                          |
|-----------------:|:--------------------------------------------------------------------------------|
|           0.9153 | n_estimators=40, min_samples_leaf=5, criterion="entropy", max_features="log2"   |
|           0.9153 | n_estimators=20, min_samples_leaf=5, criterion="entropy", max_features="log2"   |
|           0.9129 | n_estimators=10, min_samples_leaf=5, criterion="gini", max_features="log2"      |
|           0.911  | n_estimators=20, min_samples_leaf=13, criterion="entropy", max_features="log2"  |
|           0.9107 | n_estimators=10, min_samples_leaf=7, criterion="gini", max_features="log2"      |
|           0.9047 | n_estimators=160, min_samples_leaf=5, criterion="entropy", max_features="log2"  |
|           0.9044 | n_estimators=160, min_samples_leaf=3, criterion="gini", max_features="log2"     |
|           0.9044 | n_estimators=320, min_samples_leaf=5, criterion="gini", max_features="log2"     |
|           0.9044 | n_estimators=640, min_samples_leaf=5, criterion="gini", max_features="log2"     |
|           0.9035 | n_estimators=640, min_samples_leaf=3, criterion="gini", max_features="log2"     |
|           0.9032 | n_estimators=80, min_samples_leaf=3, criterion="gini", max_features="log2"      |
|           0.903  | n_estimators=20, min_samples_leaf=7, criterion="gini", max_features="log2"      |
|           0.903  | n_estimators=160, min_samples_leaf=5, criterion="gini", max_features="log2"     |
|           0.903  | n_estimators=640, min_samples_leaf=3, criterion="entropy", max_features="log2"  |
|           0.903  | n_estimators=640, min_samples_leaf=1, criterion="entropy", max_features="log2"  |
|           0.903  | n_estimators=320, min_samples_leaf=3, criterion="entropy", max_features="log2"  |
|           0.9025 | n_estimators=160, min_samples_leaf=3, criterion="entropy", max_features="log2"  |
|           0.9022 | n_estimators=80, min_samples_leaf=3, criterion="entropy", max_features="log2"   |
|           0.9022 | n_estimators=640, min_samples_leaf=5, criterion="entropy", max_features="log2"  |
|           0.9022 | n_estimators=320, min_samples_leaf=5, criterion="entropy", max_features="log2"  |
|           0.9018 | n_estimators=80, min_samples_leaf=5, criterion="entropy", max_features="log2"   |
|           0.9018 | n_estimators=80, min_samples_leaf=1, criterion="entropy", max_features="log2"   |
|           0.9018 | n_estimators=160, min_samples_leaf=7, criterion="gini", max_features="log2"     |
|           0.9015 | n_estimators=320, min_samples_leaf=7, criterion="entropy", max_features="log2"  |
|           0.9015 | n_estimators=320, min_samples_leaf=3, criterion="gini", max_features="log2"     |
|           0.9013 | n_estimators=320, min_samples_leaf=7, criterion="gini", max_features="log2"     |
|           0.901  | n_estimators=80, min_samples_leaf=5, criterion="gini", max_features="log2"      |
|           0.9008 | n_estimators=160, min_samples_leaf=7, criterion="entropy", max_features="log2"  |
|           0.9008 | n_estimators=640, min_samples_leaf=7, criterion="gini", max_features="log2"     |
|           0.9005 | n_estimators=640, min_samples_leaf=7, criterion="entropy", max_features="log2"  |
|           0.9005 | n_estimators=40, min_samples_leaf=3, criterion="gini", max_features="log2"      |
|           0.9003 | n_estimators=40, min_samples_leaf=7, criterion="gini", max_features="log2"      |
|           0.9003 | n_estimators=10, min_samples_leaf=3, criterion="gini", max_features="log2"      |
|           0.9003 | n_estimators=80, min_samples_leaf=7, criterion="gini", max_features="log2"      |
|           0.9003 | n_estimators=40, min_samples_leaf=3, criterion="entropy", max_features="log2"   |
|           0.9001 | n_estimators=160, min_samples_leaf=13, criterion="entropy", max_features="log2" |
|           0.8996 | n_estimators=320, min_samples_leaf=13, criterion="entropy", max_features="log2" |
|           0.8991 | n_estimators=80, min_samples_leaf=7, criterion="entropy", max_features="log2"   |
|           0.8986 | n_estimators=80, min_samples_leaf=13, criterion="gini", max_features="log2"     |
|           0.8986 | n_estimators=320, min_samples_leaf=13, criterion="gini", max_features="log2"    |
|           0.8986 | n_estimators=20, min_samples_leaf=7, criterion="entropy", max_features="log2"   |
|           0.8986 | n_estimators=40, min_samples_leaf=1, criterion="entropy", max_features="log2"   |
|           0.8984 | n_estimators=640, min_samples_leaf=13, criterion="entropy", max_features="log2" |
|           0.8984 | n_estimators=40, min_samples_leaf=13, criterion="gini", max_features="log2"     |
|           0.8981 | n_estimators=40, min_samples_leaf=7, criterion="entropy", max_features="log2"   |
|           0.8979 | n_estimators=160, min_samples_leaf=1, criterion="entropy", max_features="log2"  |
|           0.8976 | n_estimators=160, min_samples_leaf=13, criterion="gini", max_features="log2"    |
|           0.8974 | n_estimators=640, min_samples_leaf=13, criterion="gini", max_features="log2"    |
|           0.8969 | n_estimators=10, min_samples_leaf=5, criterion="entropy", max_features="log2"   |
|           0.8967 | n_estimators=80, min_samples_leaf=13, criterion="entropy", max_features="log2"  |
|           0.8955 | n_estimators=40, min_samples_leaf=13, criterion="entropy", max_features="log2"  |
|           0.895  | n_estimators=20, min_samples_leaf=3, criterion="gini", max_features="log2"      |
|           0.8947 | n_estimators=320, min_samples_leaf=1, criterion="entropy", max_features="log2"  |
|           0.8945 | n_estimators=640, min_samples_leaf=1, criterion="gini", max_features="log2"     |
|           0.894  | n_estimators=20, min_samples_leaf=13, criterion="gini", max_features="log2"     |
|           0.8937 | n_estimators=160, min_samples_leaf=1, criterion="gini", max_features="log2"     |
|           0.8928 | n_estimators=20, min_samples_leaf=3, criterion="entropy", max_features="log2"   |
|           0.8923 | n_estimators=40, min_samples_leaf=1, criterion="gini", max_features="log2"      |
|           0.8921 | n_estimators=80, min_samples_leaf=1, criterion="gini", max_features="log2"      |
|           0.8921 | n_estimators=320, min_samples_leaf=1, criterion="gini", max_features="log2"     |
|           0.8916 | n_estimators=10, min_samples_leaf=13, criterion="gini", max_features="log2"     |
|           0.8913 | n_estimators=10, min_samples_leaf=1, criterion="entropy", max_features="log2"   |
|           0.8911 | n_estimators=20, min_samples_leaf=5, criterion="gini", max_features="log2"      |
|           0.8906 | n_estimators=10, min_samples_leaf=13, criterion="entropy", max_features="log2"  |
|           0.8889 | n_estimators=20, min_samples_leaf=1, criterion="entropy", max_features="log2"   |
|           0.8862 | n_estimators=10, min_samples_leaf=7, criterion="entropy", max_features="log2"   |
|           0.886  | n_estimators=40, min_samples_leaf=5, criterion="gini", max_features="log2"      |
|           0.8826 | n_estimators=10, min_samples_leaf=3, criterion="entropy", max_features="log2"   |
|           0.8734 | n_estimators=20, min_samples_leaf=1, criterion="gini", max_features="log2"      |
|           0.8571 | n_estimators=10, min_samples_leaf=1, criterion="gini", max_features="log2"      |

## GradientBoosting
|   accuracy.macro | params                                                                 |
|-----------------:|:-----------------------------------------------------------------------|
|           0.909  | n_estimators=500, max_depth=1, learning_rate=0.01, max_features="log2" |
|           0.9085 | n_estimators=700, max_depth=1, learning_rate=0.01, max_features="log2" |
|           0.9066 | n_estimators=300, max_depth=3, learning_rate=0.01, max_features="log2" |
|           0.9052 | n_estimators=300, max_depth=1, learning_rate=0.01, max_features="log2" |
|           0.9025 | n_estimators=700, max_depth=7, learning_rate=0.5, max_features="log2"  |
|           0.902  | n_estimators=500, max_depth=5, learning_rate=0.1, max_features="log2"  |
|           0.901  | n_estimators=100, max_depth=5, learning_rate=0.1, max_features="log2"  |
|           0.896  | n_estimators=100, max_depth=1, learning_rate=0.01, max_features="log2" |
|           0.8959 | n_estimators=100, max_depth=7, learning_rate=0.5, max_features="log2"  |
|           0.8942 | n_estimators=700, max_depth=7, learning_rate=0.1, max_features="log2"  |
|           0.894  | n_estimators=700, max_depth=3, learning_rate=0.01, max_features="log2" |
|           0.8935 | n_estimators=100, max_depth=3, learning_rate=0.01, max_features="log2" |
|           0.8921 | n_estimators=500, max_depth=3, learning_rate=0.01, max_features="log2" |
|           0.8918 | n_estimators=100, max_depth=3, learning_rate=0.1, max_features="log2"  |
|           0.8906 | n_estimators=500, max_depth=1, learning_rate=0.1, max_features="log2"  |
|           0.8896 | n_estimators=300, max_depth=5, learning_rate=0.5, max_features="log2"  |
|           0.8891 | n_estimators=500, max_depth=5, learning_rate=0.5, max_features="log2"  |
|           0.8884 | n_estimators=100, max_depth=1, learning_rate=0.1, max_features="log2"  |
|           0.8874 | n_estimators=500, max_depth=7, learning_rate=0.5, max_features="log2"  |
|           0.887  | n_estimators=300, max_depth=5, learning_rate=0.1, max_features="log2"  |
|           0.8867 | n_estimators=100, max_depth=1, learning_rate=0.5, max_features="log2"  |
|           0.8862 | n_estimators=500, max_depth=3, learning_rate=0.5, max_features="log2"  |
|           0.8862 | n_estimators=500, max_depth=7, learning_rate=0.1, max_features="log2"  |
|           0.8862 | n_estimators=700, max_depth=1, learning_rate=0.1, max_features="log2"  |
|           0.8838 | n_estimators=300, max_depth=7, learning_rate=0.5, max_features="log2"  |
|           0.8838 | n_estimators=700, max_depth=7, learning_rate=0.01, max_features="log2" |
|           0.8833 | n_estimators=300, max_depth=1, learning_rate=0.1, max_features="log2"  |
|           0.8828 | n_estimators=300, max_depth=1, learning_rate=0.5, max_features="log2"  |
|           0.8819 | n_estimators=700, max_depth=5, learning_rate=0.01, max_features="log2" |
|           0.8819 | n_estimators=300, max_depth=1, learning_rate=1, max_features="log2"    |
|           0.8816 | n_estimators=700, max_depth=5, learning_rate=0.1, max_features="log2"  |
|           0.8816 | n_estimators=500, max_depth=5, learning_rate=0.01, max_features="log2" |
|           0.8816 | n_estimators=500, max_depth=1, learning_rate=0.5, max_features="log2"  |
|           0.8807 | n_estimators=100, max_depth=7, learning_rate=0.01, max_features="log2" |
|           0.8802 | n_estimators=100, max_depth=5, learning_rate=0.01, max_features="log2" |
|           0.8802 | n_estimators=300, max_depth=7, learning_rate=0.1, max_features="log2"  |
|           0.8792 | n_estimators=300, max_depth=3, learning_rate=0.1, max_features="log2"  |
|           0.8792 | n_estimators=300, max_depth=7, learning_rate=0.01, max_features="log2" |
|           0.8785 | n_estimators=700, max_depth=1, learning_rate=0.5, max_features="log2"  |
|           0.8782 | n_estimators=500, max_depth=7, learning_rate=0.01, max_features="log2" |
|           0.878  | n_estimators=300, max_depth=5, learning_rate=0.01, max_features="log2" |
|           0.8777 | n_estimators=100, max_depth=3, learning_rate=0.5, max_features="log2"  |
|           0.8775 | n_estimators=100, max_depth=7, learning_rate=0.1, max_features="log2"  |
|           0.877  | n_estimators=700, max_depth=5, learning_rate=0.5, max_features="log2"  |
|           0.8756 | n_estimators=700, max_depth=3, learning_rate=0.1, max_features="log2"  |
|           0.8739 | n_estimators=100, max_depth=5, learning_rate=0.5, max_features="log2"  |
|           0.8731 | n_estimators=500, max_depth=3, learning_rate=0.1, max_features="log2"  |
|           0.8675 | n_estimators=100, max_depth=1, learning_rate=1, max_features="log2"    |
|           0.8659 | n_estimators=100, max_depth=5, learning_rate=1, max_features="log2"    |
|           0.8656 | n_estimators=700, max_depth=3, learning_rate=1, max_features="log2"    |
|           0.8608 | n_estimators=300, max_depth=3, learning_rate=0.5, max_features="log2"  |
|           0.86   | n_estimators=700, max_depth=3, learning_rate=0.5, max_features="log2"  |
|           0.8535 | n_estimators=300, max_depth=5, learning_rate=1, max_features="log2"    |
|           0.852  | n_estimators=100, max_depth=7, learning_rate=1, max_features="log2"    |
|           0.8513 | n_estimators=700, max_depth=1, learning_rate=1, max_features="log2"    |
|           0.846  | n_estimators=300, max_depth=3, learning_rate=1, max_features="log2"    |
|           0.8426 | n_estimators=500, max_depth=5, learning_rate=1, max_features="log2"    |
|           0.8414 | n_estimators=700, max_depth=5, learning_rate=1, max_features="log2"    |
|           0.8385 | n_estimators=700, max_depth=7, learning_rate=1, max_features="log2"    |
|           0.8319 | n_estimators=300, max_depth=7, learning_rate=1, max_features="log2"    |
|           0.8203 | n_estimators=100, max_depth=3, learning_rate=1, max_features="log2"    |
|           0.8152 | n_estimators=500, max_depth=3, learning_rate=1, max_features="log2"    |
|           0.8057 | n_estimators=500, max_depth=1, learning_rate=1, max_features="log2"    |
|           0.779  | n_estimators=500, max_depth=7, learning_rate=1, max_features="log2"    |

## GaussianNB
|   accuracy.macro | params   |
|-----------------:|:---------|
|           0.8453 |          |

