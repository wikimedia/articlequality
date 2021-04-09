# Model tuning report
- Revscoring version: 2.8.2
- Features: articlequality.feature_lists.nlwiki.wp10
- Date: 2021-04-09T03:34:21.777148
- Observations: 1649
- Labels: ["E", "D", "C", "B", "A"]
- Statistic: accuracy.macro (maximize)
- Folds: 5

# Top scoring configurations
| model                  |   accuracy.macro | params                                                                         |
|:-----------------------|-----------------:|:-------------------------------------------------------------------------------|
| RandomForestClassifier |           0.9144 | min_samples_leaf=5, n_estimators=10, criterion="entropy", max_features="log2"  |
| RandomForestClassifier |           0.9132 | min_samples_leaf=5, n_estimators=20, criterion="entropy", max_features="log2"  |
| RandomForestClassifier |           0.9127 | min_samples_leaf=7, n_estimators=20, criterion="entropy", max_features="log2"  |
| RandomForestClassifier |           0.9127 | min_samples_leaf=5, n_estimators=10, criterion="gini", max_features="log2"     |
| RandomForestClassifier |           0.9124 | min_samples_leaf=13, n_estimators=20, criterion="gini", max_features="log2"    |
| GradientBoosting       |           0.9122 | max_depth=3, n_estimators=100, max_features="log2", learning_rate=0.01         |
| GradientBoosting       |           0.9122 | max_depth=1, n_estimators=700, max_features="log2", learning_rate=0.01         |
| GradientBoosting       |           0.9102 | max_depth=1, n_estimators=500, max_features="log2", learning_rate=0.01         |
| RandomForestClassifier |           0.9073 | min_samples_leaf=5, n_estimators=40, criterion="entropy", max_features="log2"  |
| RandomForestClassifier |           0.9052 | min_samples_leaf=7, n_estimators=160, criterion="entropy", max_features="log2" |

# Models
## BernoulliNB
|   accuracy.macro | params   |
|-----------------:|:---------|
|           0.8918 |          |

## LogisticRegression
|   accuracy.macro | params              |
|-----------------:|:--------------------|
|           0.878  | penalty="l2", C=0.1 |
|           0.8739 | penalty="l2", C=1   |
|           0.8734 | penalty="l2", C=10  |

## GradientBoosting
|   accuracy.macro | params                                                                 |
|-----------------:|:-----------------------------------------------------------------------|
|           0.9122 | max_depth=3, n_estimators=100, max_features="log2", learning_rate=0.01 |
|           0.9122 | max_depth=1, n_estimators=700, max_features="log2", learning_rate=0.01 |
|           0.9102 | max_depth=1, n_estimators=500, max_features="log2", learning_rate=0.01 |
|           0.9049 | max_depth=7, n_estimators=700, max_features="log2", learning_rate=0.1  |
|           0.9037 | max_depth=1, n_estimators=300, max_features="log2", learning_rate=0.01 |
|           0.901  | max_depth=1, n_estimators=100, max_features="log2", learning_rate=0.01 |
|           0.8979 | max_depth=3, n_estimators=300, max_features="log2", learning_rate=0.01 |
|           0.8957 | max_depth=3, n_estimators=500, max_features="log2", learning_rate=0.01 |
|           0.8955 | max_depth=5, n_estimators=500, max_features="log2", learning_rate=0.5  |
|           0.895  | max_depth=5, n_estimators=500, max_features="log2", learning_rate=0.1  |
|           0.8916 | max_depth=5, n_estimators=100, max_features="log2", learning_rate=0.1  |
|           0.8913 | max_depth=1, n_estimators=300, max_features="log2", learning_rate=0.1  |
|           0.8911 | max_depth=3, n_estimators=100, max_features="log2", learning_rate=0.5  |
|           0.8911 | max_depth=7, n_estimators=300, max_features="log2", learning_rate=0.1  |
|           0.8911 | max_depth=3, n_estimators=700, max_features="log2", learning_rate=0.01 |
|           0.8896 | max_depth=7, n_estimators=700, max_features="log2", learning_rate=0.01 |
|           0.8894 | max_depth=1, n_estimators=100, max_features="log2", learning_rate=0.1  |
|           0.8891 | max_depth=1, n_estimators=500, max_features="log2", learning_rate=0.1  |
|           0.8877 | max_depth=7, n_estimators=700, max_features="log2", learning_rate=0.5  |
|           0.8877 | max_depth=1, n_estimators=700, max_features="log2", learning_rate=0.1  |
|           0.887  | max_depth=3, n_estimators=700, max_features="log2", learning_rate=1    |
|           0.8865 | max_depth=5, n_estimators=300, max_features="log2", learning_rate=0.1  |
|           0.886  | max_depth=5, n_estimators=700, max_features="log2", learning_rate=0.01 |
|           0.8857 | max_depth=3, n_estimators=700, max_features="log2", learning_rate=0.1  |
|           0.8848 | max_depth=3, n_estimators=100, max_features="log2", learning_rate=0.1  |
|           0.8843 | max_depth=5, n_estimators=300, max_features="log2", learning_rate=0.5  |
|           0.8833 | max_depth=7, n_estimators=500, max_features="log2", learning_rate=0.1  |
|           0.8824 | max_depth=3, n_estimators=300, max_features="log2", learning_rate=0.5  |
|           0.8814 | max_depth=3, n_estimators=500, max_features="log2", learning_rate=0.1  |
|           0.8806 | max_depth=1, n_estimators=300, max_features="log2", learning_rate=0.5  |
|           0.8804 | max_depth=5, n_estimators=700, max_features="log2", learning_rate=0.1  |
|           0.8804 | max_depth=1, n_estimators=500, max_features="log2", learning_rate=0.5  |
|           0.8802 | max_depth=7, n_estimators=300, max_features="log2", learning_rate=0.01 |
|           0.8797 | max_depth=7, n_estimators=100, max_features="log2", learning_rate=0.1  |
|           0.8794 | max_depth=5, n_estimators=100, max_features="log2", learning_rate=0.01 |
|           0.8794 | max_depth=7, n_estimators=500, max_features="log2", learning_rate=0.01 |
|           0.8794 | max_depth=1, n_estimators=100, max_features="log2", learning_rate=1    |
|           0.8792 | max_depth=7, n_estimators=100, max_features="log2", learning_rate=0.01 |
|           0.879  | max_depth=5, n_estimators=300, max_features="log2", learning_rate=0.01 |
|           0.879  | max_depth=3, n_estimators=500, max_features="log2", learning_rate=0.5  |
|           0.8787 | max_depth=5, n_estimators=100, max_features="log2", learning_rate=0.5  |
|           0.8787 | max_depth=3, n_estimators=700, max_features="log2", learning_rate=0.5  |
|           0.8782 | max_depth=5, n_estimators=700, max_features="log2", learning_rate=0.5  |
|           0.8777 | max_depth=1, n_estimators=700, max_features="log2", learning_rate=0.5  |
|           0.8773 | max_depth=7, n_estimators=300, max_features="log2", learning_rate=0.5  |
|           0.8773 | max_depth=7, n_estimators=500, max_features="log2", learning_rate=0.5  |
|           0.8773 | max_depth=5, n_estimators=500, max_features="log2", learning_rate=0.01 |
|           0.8753 | max_depth=1, n_estimators=100, max_features="log2", learning_rate=0.5  |
|           0.8751 | max_depth=3, n_estimators=300, max_features="log2", learning_rate=0.1  |
|           0.8707 | max_depth=3, n_estimators=500, max_features="log2", learning_rate=1    |
|           0.869  | max_depth=7, n_estimators=100, max_features="log2", learning_rate=0.5  |
|           0.8632 | max_depth=1, n_estimators=300, max_features="log2", learning_rate=1    |
|           0.8632 | max_depth=7, n_estimators=300, max_features="log2", learning_rate=1    |
|           0.8615 | max_depth=5, n_estimators=500, max_features="log2", learning_rate=1    |
|           0.8566 | max_depth=5, n_estimators=100, max_features="log2", learning_rate=1    |
|           0.854  | max_depth=1, n_estimators=500, max_features="log2", learning_rate=1    |
|           0.8516 | max_depth=3, n_estimators=300, max_features="log2", learning_rate=1    |
|           0.8484 | max_depth=1, n_estimators=700, max_features="log2", learning_rate=1    |
|           0.8392 | max_depth=3, n_estimators=100, max_features="log2", learning_rate=1    |
|           0.8368 | max_depth=7, n_estimators=700, max_features="log2", learning_rate=1    |
|           0.8365 | max_depth=5, n_estimators=300, max_features="log2", learning_rate=1    |
|           0.8348 | max_depth=7, n_estimators=100, max_features="log2", learning_rate=1    |
|           0.8312 | max_depth=7, n_estimators=500, max_features="log2", learning_rate=1    |
|           0.8217 | max_depth=5, n_estimators=700, max_features="log2", learning_rate=1    |

## RandomForestClassifier
|   accuracy.macro | params                                                                          |
|-----------------:|:--------------------------------------------------------------------------------|
|           0.9144 | min_samples_leaf=5, n_estimators=10, criterion="entropy", max_features="log2"   |
|           0.9132 | min_samples_leaf=5, n_estimators=20, criterion="entropy", max_features="log2"   |
|           0.9127 | min_samples_leaf=7, n_estimators=20, criterion="entropy", max_features="log2"   |
|           0.9127 | min_samples_leaf=5, n_estimators=10, criterion="gini", max_features="log2"      |
|           0.9124 | min_samples_leaf=13, n_estimators=20, criterion="gini", max_features="log2"     |
|           0.9073 | min_samples_leaf=5, n_estimators=40, criterion="entropy", max_features="log2"   |
|           0.9052 | min_samples_leaf=7, n_estimators=160, criterion="entropy", max_features="log2"  |
|           0.9039 | min_samples_leaf=3, n_estimators=640, criterion="gini", max_features="log2"     |
|           0.9037 | min_samples_leaf=3, n_estimators=160, criterion="entropy", max_features="log2"  |
|           0.9035 | min_samples_leaf=5, n_estimators=320, criterion="gini", max_features="log2"     |
|           0.9032 | min_samples_leaf=3, n_estimators=640, criterion="entropy", max_features="log2"  |
|           0.9032 | min_samples_leaf=5, n_estimators=640, criterion="gini", max_features="log2"     |
|           0.903  | min_samples_leaf=5, n_estimators=640, criterion="entropy", max_features="log2"  |
|           0.903  | min_samples_leaf=5, n_estimators=80, criterion="gini", max_features="log2"      |
|           0.9027 | min_samples_leaf=7, n_estimators=160, criterion="gini", max_features="log2"     |
|           0.9025 | min_samples_leaf=1, n_estimators=320, criterion="entropy", max_features="log2"  |
|           0.9025 | min_samples_leaf=5, n_estimators=320, criterion="entropy", max_features="log2"  |
|           0.9025 | min_samples_leaf=5, n_estimators=160, criterion="gini", max_features="log2"     |
|           0.9025 | min_samples_leaf=3, n_estimators=160, criterion="gini", max_features="log2"     |
|           0.9025 | min_samples_leaf=3, n_estimators=320, criterion="gini", max_features="log2"     |
|           0.9022 | min_samples_leaf=3, n_estimators=320, criterion="entropy", max_features="log2"  |
|           0.9022 | min_samples_leaf=5, n_estimators=160, criterion="entropy", max_features="log2"  |
|           0.9018 | min_samples_leaf=3, n_estimators=80, criterion="gini", max_features="log2"      |
|           0.9018 | min_samples_leaf=7, n_estimators=640, criterion="gini", max_features="log2"     |
|           0.9015 | min_samples_leaf=1, n_estimators=160, criterion="entropy", max_features="log2"  |
|           0.9013 | min_samples_leaf=5, n_estimators=20, criterion="gini", max_features="log2"      |
|           0.9013 | min_samples_leaf=7, n_estimators=80, criterion="gini", max_features="log2"      |
|           0.9013 | min_samples_leaf=3, n_estimators=40, criterion="gini", max_features="log2"      |
|           0.901  | min_samples_leaf=7, n_estimators=40, criterion="entropy", max_features="log2"   |
|           0.901  | min_samples_leaf=7, n_estimators=10, criterion="gini", max_features="log2"      |
|           0.901  | min_samples_leaf=7, n_estimators=640, criterion="entropy", max_features="log2"  |
|           0.901  | min_samples_leaf=1, n_estimators=320, criterion="gini", max_features="log2"     |
|           0.9008 | min_samples_leaf=3, n_estimators=80, criterion="entropy", max_features="log2"   |
|           0.9008 | min_samples_leaf=7, n_estimators=320, criterion="gini", max_features="log2"     |
|           0.9008 | min_samples_leaf=5, n_estimators=40, criterion="gini", max_features="log2"      |
|           0.9005 | min_samples_leaf=7, n_estimators=80, criterion="entropy", max_features="log2"   |
|           0.9005 | min_samples_leaf=7, n_estimators=320, criterion="entropy", max_features="log2"  |
|           0.9005 | min_samples_leaf=5, n_estimators=80, criterion="entropy", max_features="log2"   |
|           0.8993 | min_samples_leaf=3, n_estimators=40, criterion="entropy", max_features="log2"   |
|           0.8991 | min_samples_leaf=13, n_estimators=640, criterion="entropy", max_features="log2" |
|           0.8991 | min_samples_leaf=13, n_estimators=20, criterion="entropy", max_features="log2"  |
|           0.8991 | min_samples_leaf=13, n_estimators=160, criterion="gini", max_features="log2"    |
|           0.8986 | min_samples_leaf=13, n_estimators=640, criterion="gini", max_features="log2"    |
|           0.8981 | min_samples_leaf=13, n_estimators=320, criterion="entropy", max_features="log2" |
|           0.8979 | min_samples_leaf=13, n_estimators=80, criterion="entropy", max_features="log2"  |
|           0.8974 | min_samples_leaf=13, n_estimators=160, criterion="entropy", max_features="log2" |
|           0.8971 | min_samples_leaf=13, n_estimators=320, criterion="gini", max_features="log2"    |
|           0.8971 | min_samples_leaf=13, n_estimators=40, criterion="gini", max_features="log2"     |
|           0.8967 | min_samples_leaf=13, n_estimators=40, criterion="entropy", max_features="log2"  |
|           0.8967 | min_samples_leaf=7, n_estimators=40, criterion="gini", max_features="log2"      |
|           0.8967 | min_samples_leaf=3, n_estimators=10, criterion="gini", max_features="log2"      |
|           0.8964 | min_samples_leaf=1, n_estimators=20, criterion="gini", max_features="log2"      |
|           0.8962 | min_samples_leaf=1, n_estimators=80, criterion="gini", max_features="log2"      |
|           0.8952 | min_samples_leaf=13, n_estimators=80, criterion="gini", max_features="log2"     |
|           0.895  | min_samples_leaf=1, n_estimators=80, criterion="entropy", max_features="log2"   |
|           0.8947 | min_samples_leaf=1, n_estimators=40, criterion="entropy", max_features="log2"   |
|           0.8945 | min_samples_leaf=1, n_estimators=640, criterion="entropy", max_features="log2"  |
|           0.8942 | min_samples_leaf=3, n_estimators=20, criterion="entropy", max_features="log2"   |
|           0.8937 | min_samples_leaf=1, n_estimators=640, criterion="gini", max_features="log2"     |
|           0.893  | min_samples_leaf=1, n_estimators=40, criterion="gini", max_features="log2"      |
|           0.893  | min_samples_leaf=7, n_estimators=10, criterion="entropy", max_features="log2"   |
|           0.8928 | min_samples_leaf=13, n_estimators=10, criterion="gini", max_features="log2"     |
|           0.8918 | min_samples_leaf=1, n_estimators=160, criterion="gini", max_features="log2"     |
|           0.8916 | min_samples_leaf=3, n_estimators=20, criterion="gini", max_features="log2"      |
|           0.887  | min_samples_leaf=7, n_estimators=20, criterion="gini", max_features="log2"      |
|           0.8853 | min_samples_leaf=1, n_estimators=20, criterion="entropy", max_features="log2"   |
|           0.8831 | min_samples_leaf=3, n_estimators=10, criterion="entropy", max_features="log2"   |
|           0.8826 | min_samples_leaf=13, n_estimators=10, criterion="entropy", max_features="log2"  |
|           0.8821 | min_samples_leaf=1, n_estimators=10, criterion="entropy", max_features="log2"   |
|           0.8678 | min_samples_leaf=1, n_estimators=10, criterion="gini", max_features="log2"      |

## GaussianNB
|   accuracy.macro | params   |
|-----------------:|:---------|
|           0.8453 |          |

