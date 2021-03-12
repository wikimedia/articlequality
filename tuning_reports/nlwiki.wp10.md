# Model tuning report
- Revscoring version: 2.8.2
- Features: articlequality.feature_lists.nlwiki.wp10
- Date: 2021-03-11T16:55:47.377015
- Observations: 1649
- Labels: ["E", "D", "C", "B", "A"]
- Statistic: accuracy.macro (maximize)
- Folds: 5

# Top scoring configurations
| model                  |   accuracy.macro | params                                                                         |
|:-----------------------|-----------------:|:-------------------------------------------------------------------------------|
| RandomForestClassifier |           0.9144 | n_estimators=40, min_samples_leaf=13, criterion="entropy", max_features="log2" |
| RandomForestClassifier |           0.9112 | n_estimators=80, min_samples_leaf=13, criterion="entropy", max_features="log2" |
| GradientBoosting       |           0.9107 | n_estimators=500, learning_rate=0.01, max_depth=1, max_features="log2"         |
| RandomForestClassifier |           0.9066 | n_estimators=10, min_samples_leaf=13, criterion="entropy", max_features="log2" |
| GradientBoosting       |           0.9064 | n_estimators=300, learning_rate=0.01, max_depth=1, max_features="log2"         |
| GradientBoosting       |           0.9047 | n_estimators=300, learning_rate=0.01, max_depth=3, max_features="log2"         |
| RandomForestClassifier |           0.9025 | n_estimators=320, min_samples_leaf=3, criterion="entropy", max_features="log2" |
| RandomForestClassifier |           0.9025 | n_estimators=80, min_samples_leaf=3, criterion="entropy", max_features="log2"  |
| RandomForestClassifier |           0.9022 | n_estimators=320, min_samples_leaf=1, criterion="entropy", max_features="log2" |
| RandomForestClassifier |           0.9022 | n_estimators=320, min_samples_leaf=3, criterion="gini", max_features="log2"    |

# Models
## BernoulliNB
|   accuracy.macro | params   |
|-----------------:|:---------|
|           0.8904 |          |

## GaussianNB
|   accuracy.macro | params   |
|-----------------:|:---------|
|            0.845 |          |

## GradientBoosting
|   accuracy.macro | params                                                                 |
|-----------------:|:-----------------------------------------------------------------------|
|           0.9107 | n_estimators=500, learning_rate=0.01, max_depth=1, max_features="log2" |
|           0.9064 | n_estimators=300, learning_rate=0.01, max_depth=1, max_features="log2" |
|           0.9047 | n_estimators=300, learning_rate=0.01, max_depth=3, max_features="log2" |
|           0.9018 | n_estimators=100, learning_rate=0.01, max_depth=1, max_features="log2" |
|           0.8996 | n_estimators=700, learning_rate=0.1, max_depth=7, max_features="log2"  |
|           0.8988 | n_estimators=100, learning_rate=0.5, max_depth=7, max_features="log2"  |
|           0.8959 | n_estimators=100, learning_rate=0.01, max_depth=3, max_features="log2" |
|           0.8947 | n_estimators=500, learning_rate=0.1, max_depth=7, max_features="log2"  |
|           0.8908 | n_estimators=700, learning_rate=0.01, max_depth=1, max_features="log2" |
|           0.8908 | n_estimators=100, learning_rate=0.01, max_depth=7, max_features="log2" |
|           0.8908 | n_estimators=100, learning_rate=0.1, max_depth=1, max_features="log2"  |
|           0.8908 | n_estimators=500, learning_rate=0.01, max_depth=3, max_features="log2" |
|           0.8896 | n_estimators=300, learning_rate=0.5, max_depth=7, max_features="log2"  |
|           0.8896 | n_estimators=300, learning_rate=0.1, max_depth=7, max_features="log2"  |
|           0.8891 | n_estimators=700, learning_rate=0.01, max_depth=3, max_features="log2" |
|           0.8889 | n_estimators=700, learning_rate=0.01, max_depth=7, max_features="log2" |
|           0.8882 | n_estimators=500, learning_rate=0.1, max_depth=1, max_features="log2"  |
|           0.8877 | n_estimators=500, learning_rate=0.01, max_depth=5, max_features="log2" |
|           0.8874 | n_estimators=500, learning_rate=0.5, max_depth=3, max_features="log2"  |
|           0.8867 | n_estimators=300, learning_rate=0.1, max_depth=1, max_features="log2"  |
|           0.8843 | n_estimators=700, learning_rate=0.1, max_depth=1, max_features="log2"  |
|           0.8833 | n_estimators=300, learning_rate=0.01, max_depth=7, max_features="log2" |
|           0.8824 | n_estimators=100, learning_rate=0.1, max_depth=3, max_features="log2"  |
|           0.8809 | n_estimators=300, learning_rate=0.1, max_depth=5, max_features="log2"  |
|           0.8809 | n_estimators=500, learning_rate=0.5, max_depth=7, max_features="log2"  |
|           0.8804 | n_estimators=100, learning_rate=0.01, max_depth=5, max_features="log2" |
|           0.8802 | n_estimators=300, learning_rate=0.5, max_depth=1, max_features="log2"  |
|           0.8799 | n_estimators=100, learning_rate=0.1, max_depth=5, max_features="log2"  |
|           0.8787 | n_estimators=100, learning_rate=0.5, max_depth=5, max_features="log2"  |
|           0.8782 | n_estimators=300, learning_rate=0.01, max_depth=5, max_features="log2" |
|           0.878  | n_estimators=100, learning_rate=0.5, max_depth=1, max_features="log2"  |
|           0.8777 | n_estimators=100, learning_rate=0.1, max_depth=7, max_features="log2"  |
|           0.877  | n_estimators=700, learning_rate=0.1, max_depth=5, max_features="log2"  |
|           0.876  | n_estimators=700, learning_rate=0.01, max_depth=5, max_features="log2" |
|           0.8758 | n_estimators=300, learning_rate=0.1, max_depth=3, max_features="log2"  |
|           0.8756 | n_estimators=700, learning_rate=0.5, max_depth=7, max_features="log2"  |
|           0.8756 | n_estimators=100, learning_rate=0.5, max_depth=3, max_features="log2"  |
|           0.8741 | n_estimators=300, learning_rate=1, max_depth=3, max_features="log2"    |
|           0.8727 | n_estimators=500, learning_rate=0.1, max_depth=3, max_features="log2"  |
|           0.8727 | n_estimators=700, learning_rate=0.5, max_depth=1, max_features="log2"  |
|           0.8724 | n_estimators=500, learning_rate=0.5, max_depth=1, max_features="log2"  |
|           0.8714 | n_estimators=300, learning_rate=0.5, max_depth=3, max_features="log2"  |
|           0.8707 | n_estimators=500, learning_rate=0.1, max_depth=5, max_features="log2"  |
|           0.87   | n_estimators=100, learning_rate=1, max_depth=1, max_features="log2"    |
|           0.869  | n_estimators=700, learning_rate=0.5, max_depth=3, max_features="log2"  |
|           0.8685 | n_estimators=700, learning_rate=0.5, max_depth=5, max_features="log2"  |
|           0.868  | n_estimators=700, learning_rate=0.1, max_depth=3, max_features="log2"  |
|           0.8654 | n_estimators=300, learning_rate=0.5, max_depth=5, max_features="log2"  |
|           0.8642 | n_estimators=500, learning_rate=0.01, max_depth=7, max_features="log2" |
|           0.861  | n_estimators=500, learning_rate=0.5, max_depth=5, max_features="log2"  |
|           0.8588 | n_estimators=300, learning_rate=1, max_depth=7, max_features="log2"    |
|           0.852  | n_estimators=100, learning_rate=1, max_depth=7, max_features="log2"    |
|           0.8513 | n_estimators=500, learning_rate=1, max_depth=1, max_features="log2"    |
|           0.8469 | n_estimators=700, learning_rate=1, max_depth=5, max_features="log2"    |
|           0.8457 | n_estimators=100, learning_rate=1, max_depth=5, max_features="log2"    |
|           0.8396 | n_estimators=300, learning_rate=1, max_depth=1, max_features="log2"    |
|           0.8351 | n_estimators=500, learning_rate=1, max_depth=5, max_features="log2"    |
|           0.8348 | n_estimators=300, learning_rate=1, max_depth=5, max_features="log2"    |
|           0.8273 | n_estimators=500, learning_rate=1, max_depth=3, max_features="log2"    |
|           0.8166 | n_estimators=700, learning_rate=1, max_depth=1, max_features="log2"    |
|           0.8101 | n_estimators=100, learning_rate=1, max_depth=3, max_features="log2"    |
|           0.7938 | n_estimators=700, learning_rate=1, max_depth=7, max_features="log2"    |
|           0.7732 | n_estimators=500, learning_rate=1, max_depth=7, max_features="log2"    |
|           0.7601 | n_estimators=700, learning_rate=1, max_depth=3, max_features="log2"    |

## RandomForestClassifier
|   accuracy.macro | params                                                                          |
|-----------------:|:--------------------------------------------------------------------------------|
|           0.9144 | n_estimators=40, min_samples_leaf=13, criterion="entropy", max_features="log2"  |
|           0.9112 | n_estimators=80, min_samples_leaf=13, criterion="entropy", max_features="log2"  |
|           0.9066 | n_estimators=10, min_samples_leaf=13, criterion="entropy", max_features="log2"  |
|           0.9025 | n_estimators=320, min_samples_leaf=3, criterion="entropy", max_features="log2"  |
|           0.9025 | n_estimators=80, min_samples_leaf=3, criterion="entropy", max_features="log2"   |
|           0.9022 | n_estimators=320, min_samples_leaf=1, criterion="entropy", max_features="log2"  |
|           0.9022 | n_estimators=320, min_samples_leaf=3, criterion="gini", max_features="log2"     |
|           0.902  | n_estimators=160, min_samples_leaf=3, criterion="gini", max_features="log2"     |
|           0.9018 | n_estimators=640, min_samples_leaf=7, criterion="gini", max_features="log2"     |
|           0.9018 | n_estimators=640, min_samples_leaf=5, criterion="entropy", max_features="log2"  |
|           0.9018 | n_estimators=80, min_samples_leaf=5, criterion="gini", max_features="log2"      |
|           0.9015 | n_estimators=160, min_samples_leaf=3, criterion="entropy", max_features="log2"  |
|           0.9015 | n_estimators=640, min_samples_leaf=3, criterion="gini", max_features="log2"     |
|           0.9013 | n_estimators=640, min_samples_leaf=3, criterion="entropy", max_features="log2"  |
|           0.9013 | n_estimators=640, min_samples_leaf=5, criterion="gini", max_features="log2"     |
|           0.9008 | n_estimators=160, min_samples_leaf=5, criterion="gini", max_features="log2"     |
|           0.9005 | n_estimators=160, min_samples_leaf=7, criterion="entropy", max_features="log2"  |
|           0.9005 | n_estimators=40, min_samples_leaf=5, criterion="gini", max_features="log2"      |
|           0.9003 | n_estimators=640, min_samples_leaf=7, criterion="entropy", max_features="log2"  |
|           0.9003 | n_estimators=80, min_samples_leaf=3, criterion="gini", max_features="log2"      |
|           0.9003 | n_estimators=320, min_samples_leaf=5, criterion="gini", max_features="log2"     |
|           0.9001 | n_estimators=640, min_samples_leaf=13, criterion="gini", max_features="log2"    |
|           0.9001 | n_estimators=160, min_samples_leaf=7, criterion="gini", max_features="log2"     |
|           0.9001 | n_estimators=20, min_samples_leaf=3, criterion="entropy", max_features="log2"   |
|           0.9001 | n_estimators=320, min_samples_leaf=7, criterion="gini", max_features="log2"     |
|           0.8996 | n_estimators=40, min_samples_leaf=7, criterion="gini", max_features="log2"      |
|           0.8996 | n_estimators=320, min_samples_leaf=7, criterion="entropy", max_features="log2"  |
|           0.8996 | n_estimators=40, min_samples_leaf=3, criterion="gini", max_features="log2"      |
|           0.8993 | n_estimators=640, min_samples_leaf=13, criterion="entropy", max_features="log2" |
|           0.8993 | n_estimators=160, min_samples_leaf=5, criterion="entropy", max_features="log2"  |
|           0.8993 | n_estimators=640, min_samples_leaf=1, criterion="entropy", max_features="log2"  |
|           0.8993 | n_estimators=80, min_samples_leaf=7, criterion="entropy", max_features="log2"   |
|           0.8991 | n_estimators=20, min_samples_leaf=1, criterion="gini", max_features="log2"      |
|           0.8988 | n_estimators=320, min_samples_leaf=13, criterion="entropy", max_features="log2" |
|           0.8988 | n_estimators=80, min_samples_leaf=13, criterion="gini", max_features="log2"     |
|           0.8988 | n_estimators=80, min_samples_leaf=5, criterion="entropy", max_features="log2"   |
|           0.8988 | n_estimators=80, min_samples_leaf=7, criterion="gini", max_features="log2"      |
|           0.8988 | n_estimators=40, min_samples_leaf=5, criterion="entropy", max_features="log2"   |
|           0.8986 | n_estimators=320, min_samples_leaf=5, criterion="entropy", max_features="log2"  |
|           0.8986 | n_estimators=10, min_samples_leaf=13, criterion="gini", max_features="log2"     |
|           0.8984 | n_estimators=80, min_samples_leaf=1, criterion="entropy", max_features="log2"   |
|           0.8981 | n_estimators=320, min_samples_leaf=13, criterion="gini", max_features="log2"    |
|           0.8981 | n_estimators=20, min_samples_leaf=7, criterion="gini", max_features="log2"      |
|           0.8979 | n_estimators=160, min_samples_leaf=13, criterion="gini", max_features="log2"    |
|           0.8976 | n_estimators=10, min_samples_leaf=3, criterion="entropy", max_features="log2"   |
|           0.8974 | n_estimators=20, min_samples_leaf=13, criterion="gini", max_features="log2"     |
|           0.8974 | n_estimators=20, min_samples_leaf=5, criterion="entropy", max_features="log2"   |
|           0.8969 | n_estimators=10, min_samples_leaf=5, criterion="entropy", max_features="log2"   |
|           0.8964 | n_estimators=10, min_samples_leaf=7, criterion="gini", max_features="log2"      |
|           0.8962 | n_estimators=20, min_samples_leaf=5, criterion="gini", max_features="log2"      |
|           0.8959 | n_estimators=20, min_samples_leaf=7, criterion="entropy", max_features="log2"   |
|           0.8957 | n_estimators=40, min_samples_leaf=3, criterion="entropy", max_features="log2"   |
|           0.8957 | n_estimators=40, min_samples_leaf=13, criterion="gini", max_features="log2"     |
|           0.895  | n_estimators=160, min_samples_leaf=13, criterion="entropy", max_features="log2" |
|           0.8938 | n_estimators=80, min_samples_leaf=1, criterion="gini", max_features="log2"      |
|           0.8933 | n_estimators=10, min_samples_leaf=5, criterion="gini", max_features="log2"      |
|           0.893  | n_estimators=640, min_samples_leaf=1, criterion="gini", max_features="log2"     |
|           0.8928 | n_estimators=10, min_samples_leaf=3, criterion="gini", max_features="log2"      |
|           0.8925 | n_estimators=160, min_samples_leaf=1, criterion="gini", max_features="log2"     |
|           0.8923 | n_estimators=320, min_samples_leaf=1, criterion="gini", max_features="log2"     |
|           0.8921 | n_estimators=10, min_samples_leaf=1, criterion="entropy", max_features="log2"   |
|           0.8906 | n_estimators=160, min_samples_leaf=1, criterion="entropy", max_features="log2"  |
|           0.8874 | n_estimators=20, min_samples_leaf=3, criterion="gini", max_features="log2"      |
|           0.8853 | n_estimators=40, min_samples_leaf=7, criterion="entropy", max_features="log2"   |
|           0.8843 | n_estimators=20, min_samples_leaf=1, criterion="entropy", max_features="log2"   |
|           0.8838 | n_estimators=40, min_samples_leaf=1, criterion="entropy", max_features="log2"   |
|           0.8826 | n_estimators=10, min_samples_leaf=7, criterion="entropy", max_features="log2"   |
|           0.8794 | n_estimators=20, min_samples_leaf=13, criterion="entropy", max_features="log2"  |
|           0.8647 | n_estimators=40, min_samples_leaf=1, criterion="gini", max_features="log2"      |
|           0.8634 | n_estimators=10, min_samples_leaf=1, criterion="gini", max_features="log2"      |

## LogisticRegression
|   accuracy.macro | params              |
|-----------------:|:--------------------|
|           0.8894 | C=1, penalty="l2"   |
|           0.8872 | C=10, penalty="l2"  |
|           0.8797 | C=0.1, penalty="l2" |

