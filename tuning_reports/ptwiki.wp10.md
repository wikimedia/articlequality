# Model tuning report
- Revscoring version: 2.7.2
- Features: articlequality.feature_lists.ptwiki.wp10
- Date: 2020-05-04T17:08:09.364778
- Observations: 8922
- Labels: ["1", "2", "3", "4", "5", "6"]
- Statistic: accuracy.macro (maximize)
- Folds: 5

# Top scoring configurations
| model                  |   accuracy.macro | params                                                                          |
|:-----------------------|-----------------:|:--------------------------------------------------------------------------------|
| RandomForestClassifier |           0.8988 | min_samples_leaf=7, n_estimators=640, max_features="log2", criterion="entropy"  |
| RandomForestClassifier |           0.8987 | min_samples_leaf=7, n_estimators=320, max_features="log2", criterion="entropy"  |
| RandomForestClassifier |           0.8985 | min_samples_leaf=13, n_estimators=320, max_features="log2", criterion="entropy" |
| RandomForestClassifier |           0.8983 | min_samples_leaf=5, n_estimators=160, max_features="log2", criterion="entropy"  |
| RandomForestClassifier |           0.8983 | min_samples_leaf=5, n_estimators=40, max_features="log2", criterion="entropy"   |
| RandomForestClassifier |           0.8982 | min_samples_leaf=13, n_estimators=640, max_features="log2", criterion="entropy" |
| RandomForestClassifier |           0.8982 | min_samples_leaf=7, n_estimators=160, max_features="log2", criterion="entropy"  |
| RandomForestClassifier |           0.8981 | min_samples_leaf=13, n_estimators=40, max_features="log2", criterion="entropy"  |
| GradientBoosting       |           0.898  | max_features="log2", n_estimators=300, max_depth=5, learning_rate=0.01          |
| RandomForestClassifier |           0.8979 | min_samples_leaf=13, n_estimators=80, max_features="log2", criterion="entropy"  |

# Models
## GaussianNB
|   accuracy.macro | params   |
|-----------------:|:---------|
|           0.8886 |          |

## LogisticRegression
|   accuracy.macro | params              |
|-----------------:|:--------------------|
|           0.8954 | C=1, penalty="l1"   |
|           0.8952 | C=1, penalty="l2"   |
|           0.8951 | C=0.1, penalty="l2" |
|           0.895  | C=0.1, penalty="l1" |
|           0.8949 | C=10, penalty="l1"  |
|           0.8946 | C=10, penalty="l2"  |

## GradientBoosting
|   accuracy.macro | params                                                                 |
|-----------------:|:-----------------------------------------------------------------------|
|           0.898  | max_features="log2", n_estimators=300, max_depth=5, learning_rate=0.01 |
|           0.8974 | max_features="log2", n_estimators=300, max_depth=7, learning_rate=0.01 |
|           0.8972 | max_features="log2", n_estimators=100, max_depth=7, learning_rate=0.01 |
|           0.8969 | max_features="log2", n_estimators=500, max_depth=7, learning_rate=0.01 |
|           0.8965 | max_features="log2", n_estimators=500, max_depth=5, learning_rate=0.01 |
|           0.8962 | max_features="log2", n_estimators=500, max_depth=3, learning_rate=0.01 |
|           0.8962 | max_features="log2", n_estimators=700, max_depth=7, learning_rate=0.01 |
|           0.896  | max_features="log2", n_estimators=100, max_depth=5, learning_rate=0.01 |
|           0.8958 | max_features="log2", n_estimators=700, max_depth=3, learning_rate=0.01 |
|           0.8955 | max_features="log2", n_estimators=700, max_depth=5, learning_rate=0.01 |
|           0.8949 | max_features="log2", n_estimators=300, max_depth=3, learning_rate=0.01 |
|           0.8936 | max_features="log2", n_estimators=100, max_depth=3, learning_rate=0.01 |
|           0.8933 | max_features="log2", n_estimators=500, max_depth=7, learning_rate=0.1  |
|           0.8931 | max_features="log2", n_estimators=100, max_depth=5, learning_rate=0.1  |
|           0.8929 | max_features="log2", n_estimators=100, max_depth=7, learning_rate=0.1  |
|           0.8922 | max_features="log2", n_estimators=100, max_depth=3, learning_rate=0.1  |
|           0.8921 | max_features="log2", n_estimators=300, max_depth=7, learning_rate=0.1  |
|           0.892  | max_features="log2", n_estimators=700, max_depth=7, learning_rate=0.1  |
|           0.8898 | max_features="log2", n_estimators=300, max_depth=5, learning_rate=0.1  |
|           0.8889 | max_features="log2", n_estimators=500, max_depth=5, learning_rate=0.1  |
|           0.8887 | max_features="log2", n_estimators=100, max_depth=7, learning_rate=0.5  |
|           0.8881 | max_features="log2", n_estimators=700, max_depth=5, learning_rate=0.1  |
|           0.8871 | max_features="log2", n_estimators=700, max_depth=1, learning_rate=0.01 |
|           0.8847 | max_features="log2", n_estimators=500, max_depth=1, learning_rate=0.01 |
|           0.8842 | max_features="log2", n_estimators=100, max_depth=5, learning_rate=0.5  |
|           0.8829 | max_features="log2", n_estimators=300, max_depth=1, learning_rate=0.01 |
|           0.8809 | max_features="log2", n_estimators=500, max_depth=3, learning_rate=0.1  |
|           0.8795 | max_features="log2", n_estimators=500, max_depth=5, learning_rate=0.5  |
|           0.8785 | max_features="log2", n_estimators=100, max_depth=1, learning_rate=0.1  |
|           0.8775 | max_features="log2", n_estimators=100, max_depth=1, learning_rate=0.01 |
|           0.8767 | max_features="log2", n_estimators=700, max_depth=3, learning_rate=0.1  |
|           0.8764 | max_features="log2", n_estimators=300, max_depth=3, learning_rate=0.1  |
|           0.8736 | max_features="log2", n_estimators=500, max_depth=1, learning_rate=0.1  |
|           0.8711 | max_features="log2", n_estimators=300, max_depth=5, learning_rate=0.5  |
|           0.8711 | max_features="log2", n_estimators=300, max_depth=1, learning_rate=0.1  |
|           0.87   | max_features="log2", n_estimators=300, max_depth=3, learning_rate=0.5  |
|           0.8695 | max_features="log2", n_estimators=100, max_depth=3, learning_rate=0.5  |
|           0.869  | max_features="log2", n_estimators=700, max_depth=1, learning_rate=0.1  |
|           0.8643 | max_features="log2", n_estimators=500, max_depth=1, learning_rate=0.5  |
|           0.8619 | max_features="log2", n_estimators=100, max_depth=1, learning_rate=1    |
|           0.8602 | max_features="log2", n_estimators=500, max_depth=3, learning_rate=0.5  |
|           0.8593 | max_features="log2", n_estimators=700, max_depth=7, learning_rate=0.5  |
|           0.8586 | max_features="log2", n_estimators=300, max_depth=1, learning_rate=0.5  |
|           0.8565 | max_features="log2", n_estimators=100, max_depth=3, learning_rate=1    |
|           0.8556 | max_features="log2", n_estimators=700, max_depth=1, learning_rate=1    |
|           0.8553 | max_features="log2", n_estimators=300, max_depth=7, learning_rate=0.5  |
|           0.8535 | max_features="log2", n_estimators=100, max_depth=1, learning_rate=0.5  |
|           0.8531 | max_features="log2", n_estimators=700, max_depth=1, learning_rate=0.5  |
|           0.8519 | max_features="log2", n_estimators=700, max_depth=5, learning_rate=0.5  |
|           0.8513 | max_features="log2", n_estimators=300, max_depth=1, learning_rate=1    |
|           0.8476 | max_features="log2", n_estimators=100, max_depth=5, learning_rate=1    |
|           0.8463 | max_features="log2", n_estimators=500, max_depth=7, learning_rate=0.5  |
|           0.8368 | max_features="log2", n_estimators=500, max_depth=7, learning_rate=1    |
|           0.828  | max_features="log2", n_estimators=700, max_depth=3, learning_rate=0.5  |
|           0.8172 | max_features="log2", n_estimators=300, max_depth=3, learning_rate=1    |
|           0.8166 | max_features="log2", n_estimators=500, max_depth=5, learning_rate=1    |
|           0.8068 | max_features="log2", n_estimators=100, max_depth=7, learning_rate=1    |
|           0.8049 | max_features="log2", n_estimators=500, max_depth=1, learning_rate=1    |
|           0.7899 | max_features="log2", n_estimators=700, max_depth=3, learning_rate=1    |
|           0.7839 | max_features="log2", n_estimators=500, max_depth=3, learning_rate=1    |
|           0.7641 | max_features="log2", n_estimators=300, max_depth=5, learning_rate=1    |
|           0.7577 | max_features="log2", n_estimators=300, max_depth=7, learning_rate=1    |
|           0.7522 | max_features="log2", n_estimators=700, max_depth=7, learning_rate=1    |
|           0.7347 | max_features="log2", n_estimators=700, max_depth=5, learning_rate=1    |

## RandomForestClassifier
|   accuracy.macro | params                                                                          |
|-----------------:|:--------------------------------------------------------------------------------|
|           0.8988 | min_samples_leaf=7, n_estimators=640, max_features="log2", criterion="entropy"  |
|           0.8987 | min_samples_leaf=7, n_estimators=320, max_features="log2", criterion="entropy"  |
|           0.8985 | min_samples_leaf=13, n_estimators=320, max_features="log2", criterion="entropy" |
|           0.8983 | min_samples_leaf=5, n_estimators=160, max_features="log2", criterion="entropy"  |
|           0.8983 | min_samples_leaf=5, n_estimators=40, max_features="log2", criterion="entropy"   |
|           0.8982 | min_samples_leaf=13, n_estimators=640, max_features="log2", criterion="entropy" |
|           0.8982 | min_samples_leaf=7, n_estimators=160, max_features="log2", criterion="entropy"  |
|           0.8981 | min_samples_leaf=13, n_estimators=40, max_features="log2", criterion="entropy"  |
|           0.8979 | min_samples_leaf=13, n_estimators=80, max_features="log2", criterion="entropy"  |
|           0.8978 | min_samples_leaf=7, n_estimators=160, max_features="log2", criterion="gini"     |
|           0.8978 | min_samples_leaf=13, n_estimators=640, max_features="log2", criterion="gini"    |
|           0.8976 | min_samples_leaf=13, n_estimators=320, max_features="log2", criterion="gini"    |
|           0.8976 | min_samples_leaf=13, n_estimators=160, max_features="log2", criterion="gini"    |
|           0.8976 | min_samples_leaf=7, n_estimators=80, max_features="log2", criterion="entropy"   |
|           0.8976 | min_samples_leaf=5, n_estimators=640, max_features="log2", criterion="entropy"  |
|           0.8975 | min_samples_leaf=13, n_estimators=80, max_features="log2", criterion="gini"     |
|           0.8974 | min_samples_leaf=5, n_estimators=320, max_features="log2", criterion="entropy"  |
|           0.8973 | min_samples_leaf=7, n_estimators=640, max_features="log2", criterion="gini"     |
|           0.8972 | min_samples_leaf=13, n_estimators=160, max_features="log2", criterion="entropy" |
|           0.8971 | min_samples_leaf=3, n_estimators=640, max_features="log2", criterion="entropy"  |
|           0.897  | min_samples_leaf=5, n_estimators=640, max_features="log2", criterion="gini"     |
|           0.897  | min_samples_leaf=3, n_estimators=160, max_features="log2", criterion="gini"     |
|           0.8968 | min_samples_leaf=5, n_estimators=320, max_features="log2", criterion="gini"     |
|           0.8968 | min_samples_leaf=5, n_estimators=80, max_features="log2", criterion="entropy"   |
|           0.8967 | min_samples_leaf=1, n_estimators=160, max_features="log2", criterion="entropy"  |
|           0.8967 | min_samples_leaf=3, n_estimators=320, max_features="log2", criterion="entropy"  |
|           0.8966 | min_samples_leaf=7, n_estimators=40, max_features="log2", criterion="gini"      |
|           0.8965 | min_samples_leaf=5, n_estimators=80, max_features="log2", criterion="gini"      |
|           0.8965 | min_samples_leaf=5, n_estimators=10, max_features="log2", criterion="entropy"   |
|           0.8965 | min_samples_leaf=13, n_estimators=40, max_features="log2", criterion="gini"     |
|           0.8965 | min_samples_leaf=7, n_estimators=320, max_features="log2", criterion="gini"     |
|           0.8964 | min_samples_leaf=1, n_estimators=320, max_features="log2", criterion="entropy"  |
|           0.8963 | min_samples_leaf=7, n_estimators=40, max_features="log2", criterion="entropy"   |
|           0.8962 | min_samples_leaf=7, n_estimators=20, max_features="log2", criterion="gini"      |
|           0.8962 | min_samples_leaf=3, n_estimators=320, max_features="log2", criterion="gini"     |
|           0.8961 | min_samples_leaf=3, n_estimators=80, max_features="log2", criterion="entropy"   |
|           0.8961 | min_samples_leaf=13, n_estimators=10, max_features="log2", criterion="gini"     |
|           0.896  | min_samples_leaf=7, n_estimators=80, max_features="log2", criterion="gini"      |
|           0.8959 | min_samples_leaf=3, n_estimators=160, max_features="log2", criterion="entropy"  |
|           0.8958 | min_samples_leaf=3, n_estimators=640, max_features="log2", criterion="gini"     |
|           0.8958 | min_samples_leaf=1, n_estimators=80, max_features="log2", criterion="entropy"   |
|           0.8956 | min_samples_leaf=7, n_estimators=10, max_features="log2", criterion="entropy"   |
|           0.8956 | min_samples_leaf=1, n_estimators=640, max_features="log2", criterion="entropy"  |
|           0.8955 | min_samples_leaf=3, n_estimators=80, max_features="log2", criterion="gini"      |
|           0.8955 | min_samples_leaf=5, n_estimators=160, max_features="log2", criterion="gini"     |
|           0.8953 | min_samples_leaf=1, n_estimators=640, max_features="log2", criterion="gini"     |
|           0.8952 | min_samples_leaf=13, n_estimators=20, max_features="log2", criterion="entropy"  |
|           0.8951 | min_samples_leaf=1, n_estimators=320, max_features="log2", criterion="gini"     |
|           0.895  | min_samples_leaf=5, n_estimators=20, max_features="log2", criterion="gini"      |
|           0.8948 | min_samples_leaf=1, n_estimators=40, max_features="log2", criterion="entropy"   |
|           0.8947 | min_samples_leaf=5, n_estimators=20, max_features="log2", criterion="entropy"   |
|           0.8946 | min_samples_leaf=7, n_estimators=20, max_features="log2", criterion="entropy"   |
|           0.8946 | min_samples_leaf=3, n_estimators=20, max_features="log2", criterion="entropy"   |
|           0.8946 | min_samples_leaf=3, n_estimators=40, max_features="log2", criterion="gini"      |
|           0.8945 | min_samples_leaf=13, n_estimators=20, max_features="log2", criterion="gini"     |
|           0.8942 | min_samples_leaf=3, n_estimators=40, max_features="log2", criterion="entropy"   |
|           0.894  | min_samples_leaf=5, n_estimators=40, max_features="log2", criterion="gini"      |
|           0.8938 | min_samples_leaf=13, n_estimators=10, max_features="log2", criterion="entropy"  |
|           0.8937 | min_samples_leaf=3, n_estimators=20, max_features="log2", criterion="gini"      |
|           0.8937 | min_samples_leaf=1, n_estimators=80, max_features="log2", criterion="gini"      |
|           0.8934 | min_samples_leaf=5, n_estimators=10, max_features="log2", criterion="gini"      |
|           0.8934 | min_samples_leaf=1, n_estimators=160, max_features="log2", criterion="gini"     |
|           0.893  | min_samples_leaf=1, n_estimators=20, max_features="log2", criterion="entropy"   |
|           0.892  | min_samples_leaf=7, n_estimators=10, max_features="log2", criterion="gini"      |
|           0.8916 | min_samples_leaf=1, n_estimators=20, max_features="log2", criterion="gini"      |
|           0.8907 | min_samples_leaf=3, n_estimators=10, max_features="log2", criterion="gini"      |
|           0.8906 | min_samples_leaf=3, n_estimators=10, max_features="log2", criterion="entropy"   |
|           0.8886 | min_samples_leaf=1, n_estimators=40, max_features="log2", criterion="gini"      |
|           0.8871 | min_samples_leaf=1, n_estimators=10, max_features="log2", criterion="entropy"   |
|           0.8848 | min_samples_leaf=1, n_estimators=10, max_features="log2", criterion="gini"      |

## BernoulliNB
|   accuracy.macro | params   |
|-----------------:|:---------|
|           0.8842 |          |

