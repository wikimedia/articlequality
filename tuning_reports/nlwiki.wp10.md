# Model tuning report
- Revscoring version: 2.11.0
- Features: articlequality.feature_lists.nlwiki.wp10
- Date: 2021-09-23T15:59:55.081386
- Observations: 1713
- Labels: ["E", "D", "C", "B", "A"]
- Statistic: accuracy.macro (maximize)
- Folds: 5

# Top scoring configurations
| model                  |   accuracy.macro | params                                                                         |
|:-----------------------|-----------------:|:-------------------------------------------------------------------------------|
| GradientBoosting       |           0.9133 | n_estimators=700, max_depth=5, max_features="log2", learning_rate=0.1          |
| GradientBoosting       |           0.9119 | n_estimators=500, max_depth=5, max_features="log2", learning_rate=0.1          |
| RandomForestClassifier |           0.9113 | min_samples_leaf=3, n_estimators=80, max_features="log2", criterion="gini"     |
| GradientBoosting       |           0.9103 | n_estimators=300, max_depth=3, max_features="log2", learning_rate=0.1          |
| GradientBoosting       |           0.9103 | n_estimators=300, max_depth=3, max_features="log2", learning_rate=0.01         |
| RandomForestClassifier |           0.91   | min_samples_leaf=1, n_estimators=160, max_features="log2", criterion="entropy" |
| GradientBoosting       |           0.9098 | n_estimators=700, max_depth=5, max_features="log2", learning_rate=0.01         |
| RandomForestClassifier |           0.9097 | min_samples_leaf=3, n_estimators=160, max_features="log2", criterion="gini"    |
| RandomForestClassifier |           0.9096 | min_samples_leaf=3, n_estimators=320, max_features="log2", criterion="entropy" |
| RandomForestClassifier |           0.9094 | min_samples_leaf=1, n_estimators=320, max_features="log2", criterion="entropy" |

# Models
## GaussianNB
|   accuracy.macro | params   |
|-----------------:|:---------|
|           0.8419 |          |

## GradientBoosting
|   accuracy.macro | params                                                                 |
|-----------------:|:-----------------------------------------------------------------------|
|           0.9133 | n_estimators=700, max_depth=5, max_features="log2", learning_rate=0.1  |
|           0.9119 | n_estimators=500, max_depth=5, max_features="log2", learning_rate=0.1  |
|           0.9103 | n_estimators=300, max_depth=3, max_features="log2", learning_rate=0.1  |
|           0.9103 | n_estimators=300, max_depth=3, max_features="log2", learning_rate=0.01 |
|           0.9098 | n_estimators=700, max_depth=5, max_features="log2", learning_rate=0.01 |
|           0.9091 | n_estimators=700, max_depth=7, max_features="log2", learning_rate=0.1  |
|           0.9078 | n_estimators=500, max_depth=7, max_features="log2", learning_rate=0.01 |
|           0.9072 | n_estimators=300, max_depth=7, max_features="log2", learning_rate=0.1  |
|           0.9064 | n_estimators=500, max_depth=5, max_features="log2", learning_rate=0.01 |
|           0.9062 | n_estimators=100, max_depth=7, max_features="log2", learning_rate=0.1  |
|           0.9062 | n_estimators=100, max_depth=3, max_features="log2", learning_rate=0.01 |
|           0.9059 | n_estimators=100, max_depth=5, max_features="log2", learning_rate=0.1  |
|           0.9041 | n_estimators=100, max_depth=5, max_features="log2", learning_rate=0.01 |
|           0.9036 | n_estimators=700, max_depth=1, max_features="log2", learning_rate=0.01 |
|           0.9025 | n_estimators=500, max_depth=1, max_features="log2", learning_rate=0.01 |
|           0.9021 | n_estimators=700, max_depth=7, max_features="log2", learning_rate=0.01 |
|           0.902  | n_estimators=100, max_depth=3, max_features="log2", learning_rate=0.1  |
|           0.9018 | n_estimators=700, max_depth=3, max_features="log2", learning_rate=0.01 |
|           0.9012 | n_estimators=300, max_depth=5, max_features="log2", learning_rate=0.01 |
|           0.9001 | n_estimators=500, max_depth=5, max_features="log2", learning_rate=0.5  |
|           0.8993 | n_estimators=300, max_depth=7, max_features="log2", learning_rate=0.5  |
|           0.8981 | n_estimators=300, max_depth=1, max_features="log2", learning_rate=0.01 |
|           0.8977 | n_estimators=500, max_depth=3, max_features="log2", learning_rate=0.1  |
|           0.8976 | n_estimators=500, max_depth=3, max_features="log2", learning_rate=0.01 |
|           0.8971 | n_estimators=500, max_depth=7, max_features="log2", learning_rate=0.1  |
|           0.8968 | n_estimators=100, max_depth=7, max_features="log2", learning_rate=0.01 |
|           0.8967 | n_estimators=500, max_depth=1, max_features="log2", learning_rate=0.1  |
|           0.8966 | n_estimators=300, max_depth=7, max_features="log2", learning_rate=0.01 |
|           0.8965 | n_estimators=100, max_depth=3, max_features="log2", learning_rate=0.5  |
|           0.8961 | n_estimators=300, max_depth=5, max_features="log2", learning_rate=0.5  |
|           0.8956 | n_estimators=500, max_depth=7, max_features="log2", learning_rate=0.5  |
|           0.8941 | n_estimators=700, max_depth=5, max_features="log2", learning_rate=0.5  |
|           0.8941 | n_estimators=300, max_depth=5, max_features="log2", learning_rate=1    |
|           0.8937 | n_estimators=300, max_depth=5, max_features="log2", learning_rate=0.1  |
|           0.8927 | n_estimators=100, max_depth=1, max_features="log2", learning_rate=0.1  |
|           0.8915 | n_estimators=700, max_depth=3, max_features="log2", learning_rate=0.1  |
|           0.8905 | n_estimators=500, max_depth=3, max_features="log2", learning_rate=0.5  |
|           0.8895 | n_estimators=100, max_depth=1, max_features="log2", learning_rate=0.01 |
|           0.888  | n_estimators=700, max_depth=3, max_features="log2", learning_rate=0.5  |
|           0.8874 | n_estimators=300, max_depth=1, max_features="log2", learning_rate=0.1  |
|           0.8852 | n_estimators=100, max_depth=5, max_features="log2", learning_rate=0.5  |
|           0.8832 | n_estimators=100, max_depth=7, max_features="log2", learning_rate=0.5  |
|           0.8809 | n_estimators=700, max_depth=7, max_features="log2", learning_rate=0.5  |
|           0.8796 | n_estimators=300, max_depth=7, max_features="log2", learning_rate=1    |
|           0.8792 | n_estimators=500, max_depth=1, max_features="log2", learning_rate=0.5  |
|           0.8773 | n_estimators=100, max_depth=5, max_features="log2", learning_rate=1    |
|           0.8771 | n_estimators=500, max_depth=3, max_features="log2", learning_rate=1    |
|           0.8757 | n_estimators=100, max_depth=1, max_features="log2", learning_rate=0.5  |
|           0.8754 | n_estimators=700, max_depth=1, max_features="log2", learning_rate=0.1  |
|           0.8737 | n_estimators=300, max_depth=3, max_features="log2", learning_rate=0.5  |
|           0.8697 | n_estimators=300, max_depth=1, max_features="log2", learning_rate=0.5  |
|           0.8595 | n_estimators=700, max_depth=1, max_features="log2", learning_rate=0.5  |
|           0.8558 | n_estimators=100, max_depth=1, max_features="log2", learning_rate=1    |
|           0.8549 | n_estimators=500, max_depth=5, max_features="log2", learning_rate=1    |
|           0.8514 | n_estimators=500, max_depth=1, max_features="log2", learning_rate=1    |
|           0.8495 | n_estimators=500, max_depth=7, max_features="log2", learning_rate=1    |
|           0.8454 | n_estimators=700, max_depth=1, max_features="log2", learning_rate=1    |
|           0.844  | n_estimators=100, max_depth=7, max_features="log2", learning_rate=1    |
|           0.8438 | n_estimators=300, max_depth=3, max_features="log2", learning_rate=1    |
|           0.8437 | n_estimators=700, max_depth=5, max_features="log2", learning_rate=1    |
|           0.8256 | n_estimators=700, max_depth=7, max_features="log2", learning_rate=1    |
|           0.8218 | n_estimators=100, max_depth=3, max_features="log2", learning_rate=1    |
|           0.8085 | n_estimators=300, max_depth=1, max_features="log2", learning_rate=1    |
|           0.7979 | n_estimators=700, max_depth=3, max_features="log2", learning_rate=1    |

## BernoulliNB
|   accuracy.macro | params   |
|-----------------:|:---------|
|           0.8785 |          |

## RandomForestClassifier
|   accuracy.macro | params                                                                          |
|-----------------:|:--------------------------------------------------------------------------------|
|           0.9113 | min_samples_leaf=3, n_estimators=80, max_features="log2", criterion="gini"      |
|           0.91   | min_samples_leaf=1, n_estimators=160, max_features="log2", criterion="entropy"  |
|           0.9097 | min_samples_leaf=3, n_estimators=160, max_features="log2", criterion="gini"     |
|           0.9096 | min_samples_leaf=3, n_estimators=320, max_features="log2", criterion="entropy"  |
|           0.9094 | min_samples_leaf=1, n_estimators=320, max_features="log2", criterion="entropy"  |
|           0.9094 | min_samples_leaf=5, n_estimators=80, max_features="log2", criterion="entropy"   |
|           0.9092 | min_samples_leaf=5, n_estimators=20, max_features="log2", criterion="gini"      |
|           0.9087 | min_samples_leaf=3, n_estimators=160, max_features="log2", criterion="entropy"  |
|           0.9085 | min_samples_leaf=3, n_estimators=320, max_features="log2", criterion="gini"     |
|           0.9085 | min_samples_leaf=5, n_estimators=320, max_features="log2", criterion="entropy"  |
|           0.9082 | min_samples_leaf=3, n_estimators=20, max_features="log2", criterion="entropy"   |
|           0.908  | min_samples_leaf=7, n_estimators=160, max_features="log2", criterion="gini"     |
|           0.908  | min_samples_leaf=3, n_estimators=640, max_features="log2", criterion="entropy"  |
|           0.908  | min_samples_leaf=7, n_estimators=640, max_features="log2", criterion="entropy"  |
|           0.908  | min_samples_leaf=5, n_estimators=160, max_features="log2", criterion="entropy"  |
|           0.9078 | min_samples_leaf=5, n_estimators=640, max_features="log2", criterion="entropy"  |
|           0.9076 | min_samples_leaf=13, n_estimators=160, max_features="log2", criterion="entropy" |
|           0.9076 | min_samples_leaf=7, n_estimators=160, max_features="log2", criterion="entropy"  |
|           0.9075 | min_samples_leaf=7, n_estimators=320, max_features="log2", criterion="entropy"  |
|           0.9074 | min_samples_leaf=13, n_estimators=320, max_features="log2", criterion="entropy" |
|           0.9071 | min_samples_leaf=13, n_estimators=160, max_features="log2", criterion="gini"    |
|           0.9071 | min_samples_leaf=13, n_estimators=80, max_features="log2", criterion="entropy"  |
|           0.9071 | min_samples_leaf=1, n_estimators=320, max_features="log2", criterion="gini"     |
|           0.9071 | min_samples_leaf=1, n_estimators=640, max_features="log2", criterion="entropy"  |
|           0.9069 | min_samples_leaf=5, n_estimators=160, max_features="log2", criterion="gini"     |
|           0.9069 | min_samples_leaf=7, n_estimators=640, max_features="log2", criterion="gini"     |
|           0.9066 | min_samples_leaf=7, n_estimators=20, max_features="log2", criterion="gini"      |
|           0.9066 | min_samples_leaf=7, n_estimators=320, max_features="log2", criterion="gini"     |
|           0.9064 | min_samples_leaf=5, n_estimators=640, max_features="log2", criterion="gini"     |
|           0.9064 | min_samples_leaf=3, n_estimators=640, max_features="log2", criterion="gini"     |
|           0.9062 | min_samples_leaf=13, n_estimators=320, max_features="log2", criterion="gini"    |
|           0.9061 | min_samples_leaf=1, n_estimators=640, max_features="log2", criterion="gini"     |
|           0.9061 | min_samples_leaf=13, n_estimators=10, max_features="log2", criterion="gini"     |
|           0.9059 | min_samples_leaf=5, n_estimators=320, max_features="log2", criterion="gini"     |
|           0.9058 | min_samples_leaf=13, n_estimators=640, max_features="log2", criterion="entropy" |
|           0.9057 | min_samples_leaf=13, n_estimators=80, max_features="log2", criterion="gini"     |
|           0.9055 | min_samples_leaf=7, n_estimators=40, max_features="log2", criterion="gini"      |
|           0.9051 | min_samples_leaf=1, n_estimators=40, max_features="log2", criterion="entropy"   |
|           0.9051 | min_samples_leaf=13, n_estimators=640, max_features="log2", criterion="gini"    |
|           0.905  | min_samples_leaf=1, n_estimators=10, max_features="log2", criterion="gini"      |
|           0.9049 | min_samples_leaf=7, n_estimators=10, max_features="log2", criterion="gini"      |
|           0.9048 | min_samples_leaf=5, n_estimators=80, max_features="log2", criterion="gini"      |
|           0.9045 | min_samples_leaf=7, n_estimators=80, max_features="log2", criterion="entropy"   |
|           0.904  | min_samples_leaf=5, n_estimators=20, max_features="log2", criterion="entropy"   |
|           0.9039 | min_samples_leaf=7, n_estimators=80, max_features="log2", criterion="gini"      |
|           0.9038 | min_samples_leaf=1, n_estimators=160, max_features="log2", criterion="gini"     |
|           0.9038 | min_samples_leaf=13, n_estimators=40, max_features="log2", criterion="gini"     |
|           0.9036 | min_samples_leaf=13, n_estimators=20, max_features="log2", criterion="entropy"  |
|           0.9034 | min_samples_leaf=13, n_estimators=40, max_features="log2", criterion="entropy"  |
|           0.9034 | min_samples_leaf=13, n_estimators=20, max_features="log2", criterion="gini"     |
|           0.9031 | min_samples_leaf=7, n_estimators=40, max_features="log2", criterion="entropy"   |
|           0.903  | min_samples_leaf=13, n_estimators=10, max_features="log2", criterion="entropy"  |
|           0.9029 | min_samples_leaf=1, n_estimators=10, max_features="log2", criterion="entropy"   |
|           0.9028 | min_samples_leaf=3, n_estimators=10, max_features="log2", criterion="gini"      |
|           0.9026 | min_samples_leaf=1, n_estimators=80, max_features="log2", criterion="entropy"   |
|           0.9022 | min_samples_leaf=5, n_estimators=40, max_features="log2", criterion="gini"      |
|           0.9003 | min_samples_leaf=3, n_estimators=40, max_features="log2", criterion="gini"      |
|           0.8971 | min_samples_leaf=5, n_estimators=10, max_features="log2", criterion="entropy"   |
|           0.8968 | min_samples_leaf=5, n_estimators=40, max_features="log2", criterion="entropy"   |
|           0.8968 | min_samples_leaf=1, n_estimators=80, max_features="log2", criterion="gini"      |
|           0.8957 | min_samples_leaf=3, n_estimators=80, max_features="log2", criterion="entropy"   |
|           0.8953 | min_samples_leaf=1, n_estimators=20, max_features="log2", criterion="entropy"   |
|           0.8951 | min_samples_leaf=1, n_estimators=40, max_features="log2", criterion="gini"      |
|           0.8936 | min_samples_leaf=3, n_estimators=40, max_features="log2", criterion="entropy"   |
|           0.8925 | min_samples_leaf=3, n_estimators=10, max_features="log2", criterion="entropy"   |
|           0.8921 | min_samples_leaf=5, n_estimators=10, max_features="log2", criterion="gini"      |
|           0.8916 | min_samples_leaf=3, n_estimators=20, max_features="log2", criterion="gini"      |
|           0.8912 | min_samples_leaf=7, n_estimators=10, max_features="log2", criterion="entropy"   |
|           0.8905 | min_samples_leaf=1, n_estimators=20, max_features="log2", criterion="gini"      |
|           0.8813 | min_samples_leaf=7, n_estimators=20, max_features="log2", criterion="entropy"   |

## LogisticRegression
|   accuracy.macro | params              |
|-----------------:|:--------------------|
|           0.882  | C=10, penalty="l2"  |
|           0.8801 | C=1, penalty="l2"   |
|           0.8773 | C=0.1, penalty="l2" |

