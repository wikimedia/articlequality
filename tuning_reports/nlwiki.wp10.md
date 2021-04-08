# Model tuning report
- Revscoring version: 2.8.2
- Features: articlequality.feature_lists.nlwiki.wp10
- Date: 2021-04-08T17:30:39.351127
- Observations: 1649
- Labels: ["E", "D", "C", "B", "A"]
- Statistic: accuracy.macro (maximize)
- Folds: 5

# Top scoring configurations
| model                  |   accuracy.macro | params                                                                         |
|:-----------------------|-----------------:|:-------------------------------------------------------------------------------|
| GradientBoosting       |           0.91   | learning_rate=0.01, max_features="log2", max_depth=1, n_estimators=500         |
| GradientBoosting       |           0.9093 | learning_rate=0.01, max_features="log2", max_depth=1, n_estimators=700         |
| GradientBoosting       |           0.9056 | learning_rate=0.01, max_features="log2", max_depth=1, n_estimators=300         |
| RandomForestClassifier |           0.9049 | min_samples_leaf=3, criterion="entropy", n_estimators=20, max_features="log2"  |
| RandomForestClassifier |           0.9047 | min_samples_leaf=3, criterion="entropy", n_estimators=160, max_features="log2" |
| GradientBoosting       |           0.9047 | learning_rate=0.01, max_features="log2", max_depth=3, n_estimators=300         |
| RandomForestClassifier |           0.9042 | min_samples_leaf=5, criterion="gini", n_estimators=160, max_features="log2"    |
| RandomForestClassifier |           0.9039 | min_samples_leaf=1, criterion="entropy", n_estimators=80, max_features="log2"  |
| RandomForestClassifier |           0.9039 | min_samples_leaf=3, criterion="gini", n_estimators=320, max_features="log2"    |
| RandomForestClassifier |           0.9039 | min_samples_leaf=5, criterion="gini", n_estimators=640, max_features="log2"    |

# Models
## GradientBoosting
|   accuracy.macro | params                                                                 |
|-----------------:|:-----------------------------------------------------------------------|
|           0.91   | learning_rate=0.01, max_features="log2", max_depth=1, n_estimators=500 |
|           0.9093 | learning_rate=0.01, max_features="log2", max_depth=1, n_estimators=700 |
|           0.9056 | learning_rate=0.01, max_features="log2", max_depth=1, n_estimators=300 |
|           0.9047 | learning_rate=0.01, max_features="log2", max_depth=3, n_estimators=300 |
|           0.9008 | learning_rate=0.01, max_features="log2", max_depth=1, n_estimators=100 |
|           0.8979 | learning_rate=0.5, max_features="log2", max_depth=5, n_estimators=700  |
|           0.8957 | learning_rate=0.1, max_features="log2", max_depth=7, n_estimators=100  |
|           0.8945 | learning_rate=0.1, max_features="log2", max_depth=5, n_estimators=100  |
|           0.8945 | learning_rate=0.1, max_features="log2", max_depth=7, n_estimators=500  |
|           0.8942 | learning_rate=0.01, max_features="log2", max_depth=3, n_estimators=500 |
|           0.8928 | learning_rate=0.01, max_features="log2", max_depth=5, n_estimators=700 |
|           0.8925 | learning_rate=0.1, max_features="log2", max_depth=1, n_estimators=500  |
|           0.8923 | learning_rate=0.1, max_features="log2", max_depth=5, n_estimators=300  |
|           0.8899 | learning_rate=0.1, max_features="log2", max_depth=5, n_estimators=700  |
|           0.8896 | learning_rate=0.1, max_features="log2", max_depth=3, n_estimators=100  |
|           0.8894 | learning_rate=0.5, max_features="log2", max_depth=7, n_estimators=300  |
|           0.8894 | learning_rate=0.01, max_features="log2", max_depth=3, n_estimators=700 |
|           0.8889 | learning_rate=0.5, max_features="log2", max_depth=5, n_estimators=300  |
|           0.8884 | learning_rate=0.1, max_features="log2", max_depth=1, n_estimators=300  |
|           0.8882 | learning_rate=0.1, max_features="log2", max_depth=1, n_estimators=700  |
|           0.886  | learning_rate=1, max_features="log2", max_depth=7, n_estimators=500    |
|           0.886  | learning_rate=0.5, max_features="log2", max_depth=7, n_estimators=700  |
|           0.8858 | learning_rate=0.01, max_features="log2", max_depth=3, n_estimators=100 |
|           0.885  | learning_rate=0.1, max_features="log2", max_depth=1, n_estimators=100  |
|           0.8841 | learning_rate=0.1, max_features="log2", max_depth=7, n_estimators=300  |
|           0.8831 | learning_rate=0.01, max_features="log2", max_depth=5, n_estimators=100 |
|           0.8821 | learning_rate=0.5, max_features="log2", max_depth=1, n_estimators=300  |
|           0.8819 | learning_rate=0.1, max_features="log2", max_depth=5, n_estimators=500  |
|           0.8816 | learning_rate=0.5, max_features="log2", max_depth=1, n_estimators=100  |
|           0.8807 | learning_rate=0.01, max_features="log2", max_depth=5, n_estimators=300 |
|           0.8804 | learning_rate=0.01, max_features="log2", max_depth=7, n_estimators=100 |
|           0.8802 | learning_rate=0.5, max_features="log2", max_depth=1, n_estimators=500  |
|           0.8799 | learning_rate=0.1, max_features="log2", max_depth=3, n_estimators=700  |
|           0.8794 | learning_rate=0.01, max_features="log2", max_depth=7, n_estimators=500 |
|           0.8794 | learning_rate=0.1, max_features="log2", max_depth=3, n_estimators=500  |
|           0.8794 | learning_rate=0.5, max_features="log2", max_depth=1, n_estimators=700  |
|           0.8792 | learning_rate=0.01, max_features="log2", max_depth=7, n_estimators=700 |
|           0.8792 | learning_rate=0.01, max_features="log2", max_depth=7, n_estimators=300 |
|           0.878  | learning_rate=0.5, max_features="log2", max_depth=3, n_estimators=500  |
|           0.8765 | learning_rate=0.5, max_features="log2", max_depth=3, n_estimators=100  |
|           0.8746 | learning_rate=0.1, max_features="log2", max_depth=3, n_estimators=300  |
|           0.8744 | learning_rate=0.5, max_features="log2", max_depth=3, n_estimators=300  |
|           0.8739 | learning_rate=0.1, max_features="log2", max_depth=7, n_estimators=700  |
|           0.8739 | learning_rate=1, max_features="log2", max_depth=3, n_estimators=300    |
|           0.8729 | learning_rate=0.5, max_features="log2", max_depth=7, n_estimators=100  |
|           0.8726 | learning_rate=1, max_features="log2", max_depth=1, n_estimators=500    |
|           0.8726 | learning_rate=1, max_features="log2", max_depth=1, n_estimators=300    |
|           0.869  | learning_rate=0.01, max_features="log2", max_depth=5, n_estimators=500 |
|           0.8637 | learning_rate=1, max_features="log2", max_depth=5, n_estimators=500    |
|           0.8634 | learning_rate=0.5, max_features="log2", max_depth=7, n_estimators=500  |
|           0.8617 | learning_rate=0.5, max_features="log2", max_depth=5, n_estimators=500  |
|           0.8613 | learning_rate=0.5, max_features="log2", max_depth=3, n_estimators=700  |
|           0.8596 | learning_rate=0.5, max_features="log2", max_depth=5, n_estimators=100  |
|           0.8554 | learning_rate=1, max_features="log2", max_depth=7, n_estimators=700    |
|           0.8397 | learning_rate=1, max_features="log2", max_depth=7, n_estimators=100    |
|           0.8367 | learning_rate=1, max_features="log2", max_depth=1, n_estimators=100    |
|           0.8355 | learning_rate=1, max_features="log2", max_depth=5, n_estimators=100    |
|           0.8341 | learning_rate=1, max_features="log2", max_depth=3, n_estimators=100    |
|           0.8234 | learning_rate=1, max_features="log2", max_depth=3, n_estimators=700    |
|           0.8171 | learning_rate=1, max_features="log2", max_depth=5, n_estimators=700    |
|           0.812  | learning_rate=1, max_features="log2", max_depth=5, n_estimators=300    |
|           0.8055 | learning_rate=1, max_features="log2", max_depth=7, n_estimators=300    |
|           0.7982 | learning_rate=1, max_features="log2", max_depth=3, n_estimators=500    |
|           0.7977 | learning_rate=1, max_features="log2", max_depth=1, n_estimators=700    |

## LogisticRegression
|   accuracy.macro | params              |
|-----------------:|:--------------------|
|           0.878  | penalty="l2", C=0.1 |
|           0.8739 | penalty="l2", C=1   |
|           0.8734 | penalty="l2", C=10  |

## GaussianNB
|   accuracy.macro | params   |
|-----------------:|:---------|
|           0.8453 |          |

## BernoulliNB
|   accuracy.macro | params   |
|-----------------:|:---------|
|           0.8918 |          |

## RandomForestClassifier
|   accuracy.macro | params                                                                          |
|-----------------:|:--------------------------------------------------------------------------------|
|           0.9049 | min_samples_leaf=3, criterion="entropy", n_estimators=20, max_features="log2"   |
|           0.9047 | min_samples_leaf=3, criterion="entropy", n_estimators=160, max_features="log2"  |
|           0.9042 | min_samples_leaf=5, criterion="gini", n_estimators=160, max_features="log2"     |
|           0.9039 | min_samples_leaf=1, criterion="entropy", n_estimators=80, max_features="log2"   |
|           0.9039 | min_samples_leaf=3, criterion="gini", n_estimators=320, max_features="log2"     |
|           0.9039 | min_samples_leaf=5, criterion="gini", n_estimators=640, max_features="log2"     |
|           0.9035 | min_samples_leaf=3, criterion="gini", n_estimators=160, max_features="log2"     |
|           0.9032 | min_samples_leaf=5, criterion="gini", n_estimators=80, max_features="log2"      |
|           0.9032 | min_samples_leaf=5, criterion="gini", n_estimators=320, max_features="log2"     |
|           0.903  | min_samples_leaf=5, criterion="entropy", n_estimators=640, max_features="log2"  |
|           0.903  | min_samples_leaf=3, criterion="gini", n_estimators=640, max_features="log2"     |
|           0.9027 | min_samples_leaf=1, criterion="entropy", n_estimators=640, max_features="log2"  |
|           0.9025 | min_samples_leaf=3, criterion="entropy", n_estimators=640, max_features="log2"  |
|           0.9022 | min_samples_leaf=5, criterion="entropy", n_estimators=320, max_features="log2"  |
|           0.9022 | min_samples_leaf=3, criterion="entropy", n_estimators=320, max_features="log2"  |
|           0.902  | min_samples_leaf=7, criterion="entropy", n_estimators=160, max_features="log2"  |
|           0.902  | min_samples_leaf=5, criterion="gini", n_estimators=20, max_features="log2"      |
|           0.9015 | min_samples_leaf=7, criterion="entropy", n_estimators=80, max_features="log2"   |
|           0.9015 | min_samples_leaf=1, criterion="gini", n_estimators=40, max_features="log2"      |
|           0.9015 | min_samples_leaf=7, criterion="gini", n_estimators=640, max_features="log2"     |
|           0.9013 | min_samples_leaf=13, criterion="entropy", n_estimators=160, max_features="log2" |
|           0.9013 | min_samples_leaf=7, criterion="entropy", n_estimators=640, max_features="log2"  |
|           0.9013 | min_samples_leaf=7, criterion="gini", n_estimators=20, max_features="log2"      |
|           0.9013 | min_samples_leaf=5, criterion="gini", n_estimators=40, max_features="log2"      |
|           0.9013 | min_samples_leaf=3, criterion="gini", n_estimators=80, max_features="log2"      |
|           0.901  | min_samples_leaf=5, criterion="entropy", n_estimators=160, max_features="log2"  |
|           0.901  | min_samples_leaf=7, criterion="gini", n_estimators=320, max_features="log2"     |
|           0.9008 | min_samples_leaf=5, criterion="entropy", n_estimators=20, max_features="log2"   |
|           0.9008 | min_samples_leaf=7, criterion="entropy", n_estimators=320, max_features="log2"  |
|           0.9008 | min_samples_leaf=7, criterion="gini", n_estimators=80, max_features="log2"      |
|           0.9001 | min_samples_leaf=3, criterion="entropy", n_estimators=80, max_features="log2"   |
|           0.9001 | min_samples_leaf=7, criterion="entropy", n_estimators=10, max_features="log2"   |
|           0.8998 | min_samples_leaf=13, criterion="entropy", n_estimators=80, max_features="log2"  |
|           0.8996 | min_samples_leaf=5, criterion="entropy", n_estimators=40, max_features="log2"   |
|           0.8996 | min_samples_leaf=1, criterion="entropy", n_estimators=320, max_features="log2"  |
|           0.8993 | min_samples_leaf=3, criterion="gini", n_estimators=20, max_features="log2"      |
|           0.8991 | min_samples_leaf=7, criterion="gini", n_estimators=160, max_features="log2"     |
|           0.8991 | min_samples_leaf=3, criterion="entropy", n_estimators=40, max_features="log2"   |
|           0.8988 | min_samples_leaf=5, criterion="gini", n_estimators=10, max_features="log2"      |
|           0.8986 | min_samples_leaf=1, criterion="entropy", n_estimators=20, max_features="log2"   |
|           0.8984 | min_samples_leaf=13, criterion="gini", n_estimators=160, max_features="log2"    |
|           0.8984 | min_samples_leaf=3, criterion="gini", n_estimators=10, max_features="log2"      |
|           0.8984 | min_samples_leaf=13, criterion="gini", n_estimators=10, max_features="log2"     |
|           0.8981 | min_samples_leaf=13, criterion="entropy", n_estimators=40, max_features="log2"  |
|           0.8981 | min_samples_leaf=7, criterion="entropy", n_estimators=40, max_features="log2"   |
|           0.8976 | min_samples_leaf=13, criterion="gini", n_estimators=320, max_features="log2"    |
|           0.8974 | min_samples_leaf=13, criterion="entropy", n_estimators=320, max_features="log2" |
|           0.8974 | min_samples_leaf=13, criterion="gini", n_estimators=640, max_features="log2"    |
|           0.8974 | min_samples_leaf=7, criterion="gini", n_estimators=40, max_features="log2"      |
|           0.8974 | min_samples_leaf=7, criterion="gini", n_estimators=10, max_features="log2"      |
|           0.8972 | min_samples_leaf=13, criterion="entropy", n_estimators=640, max_features="log2" |
|           0.8971 | min_samples_leaf=13, criterion="gini", n_estimators=40, max_features="log2"     |
|           0.8967 | min_samples_leaf=7, criterion="entropy", n_estimators=20, max_features="log2"   |
|           0.8964 | min_samples_leaf=13, criterion="gini", n_estimators=80, max_features="log2"     |
|           0.8964 | min_samples_leaf=5, criterion="entropy", n_estimators=80, max_features="log2"   |
|           0.8962 | min_samples_leaf=3, criterion="gini", n_estimators=40, max_features="log2"      |
|           0.8959 | min_samples_leaf=1, criterion="gini", n_estimators=640, max_features="log2"     |
|           0.8952 | min_samples_leaf=1, criterion="entropy", n_estimators=160, max_features="log2"  |
|           0.8945 | min_samples_leaf=13, criterion="entropy", n_estimators=20, max_features="log2"  |
|           0.8938 | min_samples_leaf=13, criterion="entropy", n_estimators=10, max_features="log2"  |
|           0.8928 | min_samples_leaf=13, criterion="gini", n_estimators=20, max_features="log2"     |
|           0.8928 | min_samples_leaf=1, criterion="gini", n_estimators=320, max_features="log2"     |
|           0.8918 | min_samples_leaf=3, criterion="entropy", n_estimators=10, max_features="log2"   |
|           0.8916 | min_samples_leaf=1, criterion="entropy", n_estimators=40, max_features="log2"   |
|           0.8904 | min_samples_leaf=1, criterion="gini", n_estimators=160, max_features="log2"     |
|           0.8843 | min_samples_leaf=1, criterion="gini", n_estimators=80, max_features="log2"      |
|           0.8828 | min_samples_leaf=5, criterion="entropy", n_estimators=10, max_features="log2"   |
|           0.877  | min_samples_leaf=1, criterion="gini", n_estimators=20, max_features="log2"      |
|           0.8712 | min_samples_leaf=1, criterion="gini", n_estimators=10, max_features="log2"      |
|           0.8705 | min_samples_leaf=1, criterion="entropy", n_estimators=10, max_features="log2"   |

