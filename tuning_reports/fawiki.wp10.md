# Model tuning report
- Revscoring version: 2.2.4
- Features: articlequality.feature_lists.fawiki.wp10
- Date: 2018-07-10T14:21:40.948634
- Observations: 665
- Labels: ["Stub", "Start", "C", "B", "GA", "FA"]
- Statistic: accuracy.macro (maximize)
- Folds: 5

# Top scoring configurations
| model                  |   accuracy.macro | params                                                                         |
|:-----------------------|-----------------:|:-------------------------------------------------------------------------------|
| GradientBoosting       |           0.8236 | n_estimators=100, max_depth=7, max_features="log2", learning_rate=0.5          |
| GradientBoosting       |           0.823  | n_estimators=500, max_depth=5, max_features="log2", learning_rate=1            |
| RandomForestClassifier |           0.821  | n_estimators=320, criterion="entropy", min_samples_leaf=1, max_features="log2" |
| GradientBoosting       |           0.8202 | n_estimators=300, max_depth=7, max_features="log2", learning_rate=0.5          |
| RandomForestClassifier |           0.818  | n_estimators=320, criterion="gini", min_samples_leaf=1, max_features="log2"    |
| GradientBoosting       |           0.8179 | n_estimators=700, max_depth=7, max_features="log2", learning_rate=0.1          |
| RandomForestClassifier |           0.8176 | n_estimators=20, criterion="entropy", min_samples_leaf=3, max_features="log2"  |
| GradientBoosting       |           0.8173 | n_estimators=700, max_depth=5, max_features="log2", learning_rate=0.1          |
| GradientBoosting       |           0.8172 | n_estimators=500, max_depth=7, max_features="log2", learning_rate=0.1          |
| RandomForestClassifier |           0.8171 | n_estimators=20, criterion="gini", min_samples_leaf=3, max_features="log2"     |

# Models
## BernoulliNB
|   accuracy.macro | params   |
|-----------------:|:---------|
|           0.7993 |          |

## GaussianNB
|   accuracy.macro | params   |
|-----------------:|:---------|
|            0.769 |          |

## RandomForestClassifier
|   accuracy.macro | params                                                                          |
|-----------------:|:--------------------------------------------------------------------------------|
|           0.821  | n_estimators=320, criterion="entropy", min_samples_leaf=1, max_features="log2"  |
|           0.818  | n_estimators=320, criterion="gini", min_samples_leaf=1, max_features="log2"     |
|           0.8176 | n_estimators=20, criterion="entropy", min_samples_leaf=3, max_features="log2"   |
|           0.8171 | n_estimators=20, criterion="gini", min_samples_leaf=3, max_features="log2"      |
|           0.8165 | n_estimators=320, criterion="entropy", min_samples_leaf=3, max_features="log2"  |
|           0.8159 | n_estimators=160, criterion="gini", min_samples_leaf=1, max_features="log2"     |
|           0.8158 | n_estimators=40, criterion="entropy", min_samples_leaf=7, max_features="log2"   |
|           0.8157 | n_estimators=80, criterion="gini", min_samples_leaf=3, max_features="log2"      |
|           0.8145 | n_estimators=80, criterion="gini", min_samples_leaf=1, max_features="log2"      |
|           0.8142 | n_estimators=320, criterion="gini", min_samples_leaf=3, max_features="log2"     |
|           0.8139 | n_estimators=160, criterion="entropy", min_samples_leaf=5, max_features="log2"  |
|           0.8139 | n_estimators=320, criterion="entropy", min_samples_leaf=7, max_features="log2"  |
|           0.8139 | n_estimators=10, criterion="gini", min_samples_leaf=7, max_features="log2"      |
|           0.8138 | n_estimators=640, criterion="entropy", min_samples_leaf=3, max_features="log2"  |
|           0.8136 | n_estimators=80, criterion="gini", min_samples_leaf=5, max_features="log2"      |
|           0.8131 | n_estimators=640, criterion="gini", min_samples_leaf=3, max_features="log2"     |
|           0.8127 | n_estimators=40, criterion="gini", min_samples_leaf=5, max_features="log2"      |
|           0.8127 | n_estimators=10, criterion="gini", min_samples_leaf=13, max_features="log2"     |
|           0.8125 | n_estimators=160, criterion="entropy", min_samples_leaf=3, max_features="log2"  |
|           0.8121 | n_estimators=640, criterion="entropy", min_samples_leaf=5, max_features="log2"  |
|           0.8121 | n_estimators=640, criterion="gini", min_samples_leaf=1, max_features="log2"     |
|           0.8121 | n_estimators=80, criterion="entropy", min_samples_leaf=7, max_features="log2"   |
|           0.812  | n_estimators=640, criterion="entropy", min_samples_leaf=7, max_features="log2"  |
|           0.8119 | n_estimators=80, criterion="entropy", min_samples_leaf=13, max_features="log2"  |
|           0.8116 | n_estimators=160, criterion="entropy", min_samples_leaf=1, max_features="log2"  |
|           0.8111 | n_estimators=320, criterion="entropy", min_samples_leaf=5, max_features="log2"  |
|           0.811  | n_estimators=640, criterion="entropy", min_samples_leaf=1, max_features="log2"  |
|           0.8108 | n_estimators=40, criterion="gini", min_samples_leaf=1, max_features="log2"      |
|           0.8107 | n_estimators=20, criterion="gini", min_samples_leaf=5, max_features="log2"      |
|           0.8107 | n_estimators=40, criterion="entropy", min_samples_leaf=1, max_features="log2"   |
|           0.8103 | n_estimators=640, criterion="gini", min_samples_leaf=5, max_features="log2"     |
|           0.8101 | n_estimators=10, criterion="gini", min_samples_leaf=3, max_features="log2"      |
|           0.8099 | n_estimators=160, criterion="entropy", min_samples_leaf=7, max_features="log2"  |
|           0.8098 | n_estimators=10, criterion="gini", min_samples_leaf=5, max_features="log2"      |
|           0.8098 | n_estimators=160, criterion="gini", min_samples_leaf=5, max_features="log2"     |
|           0.8092 | n_estimators=80, criterion="entropy", min_samples_leaf=3, max_features="log2"   |
|           0.809  | n_estimators=80, criterion="gini", min_samples_leaf=13, max_features="log2"     |
|           0.8089 | n_estimators=80, criterion="entropy", min_samples_leaf=5, max_features="log2"   |
|           0.8089 | n_estimators=80, criterion="entropy", min_samples_leaf=1, max_features="log2"   |
|           0.8088 | n_estimators=640, criterion="entropy", min_samples_leaf=13, max_features="log2" |
|           0.8088 | n_estimators=20, criterion="gini", min_samples_leaf=1, max_features="log2"      |
|           0.8086 | n_estimators=40, criterion="entropy", min_samples_leaf=13, max_features="log2"  |
|           0.8085 | n_estimators=320, criterion="gini", min_samples_leaf=13, max_features="log2"    |
|           0.8085 | n_estimators=40, criterion="gini", min_samples_leaf=13, max_features="log2"     |
|           0.8083 | n_estimators=160, criterion="entropy", min_samples_leaf=13, max_features="log2" |
|           0.8081 | n_estimators=160, criterion="gini", min_samples_leaf=3, max_features="log2"     |
|           0.8077 | n_estimators=320, criterion="gini", min_samples_leaf=7, max_features="log2"     |
|           0.8076 | n_estimators=160, criterion="gini", min_samples_leaf=7, max_features="log2"     |
|           0.8075 | n_estimators=40, criterion="entropy", min_samples_leaf=3, max_features="log2"   |
|           0.8071 | n_estimators=320, criterion="entropy", min_samples_leaf=13, max_features="log2" |
|           0.8071 | n_estimators=80, criterion="gini", min_samples_leaf=7, max_features="log2"      |
|           0.8071 | n_estimators=40, criterion="entropy", min_samples_leaf=5, max_features="log2"   |
|           0.807  | n_estimators=40, criterion="gini", min_samples_leaf=3, max_features="log2"      |
|           0.8067 | n_estimators=640, criterion="gini", min_samples_leaf=13, max_features="log2"    |
|           0.8062 | n_estimators=640, criterion="gini", min_samples_leaf=7, max_features="log2"     |
|           0.8061 | n_estimators=10, criterion="entropy", min_samples_leaf=7, max_features="log2"   |
|           0.806  | n_estimators=20, criterion="entropy", min_samples_leaf=7, max_features="log2"   |
|           0.8054 | n_estimators=10, criterion="entropy", min_samples_leaf=5, max_features="log2"   |
|           0.8053 | n_estimators=160, criterion="gini", min_samples_leaf=13, max_features="log2"    |
|           0.8052 | n_estimators=10, criterion="gini", min_samples_leaf=1, max_features="log2"      |
|           0.8051 | n_estimators=20, criterion="gini", min_samples_leaf=7, max_features="log2"      |
|           0.8049 | n_estimators=320, criterion="gini", min_samples_leaf=5, max_features="log2"     |
|           0.8046 | n_estimators=20, criterion="gini", min_samples_leaf=13, max_features="log2"     |
|           0.8045 | n_estimators=40, criterion="gini", min_samples_leaf=7, max_features="log2"      |
|           0.8038 | n_estimators=10, criterion="entropy", min_samples_leaf=3, max_features="log2"   |
|           0.8014 | n_estimators=20, criterion="entropy", min_samples_leaf=13, max_features="log2"  |
|           0.7986 | n_estimators=20, criterion="entropy", min_samples_leaf=5, max_features="log2"   |
|           0.7984 | n_estimators=10, criterion="entropy", min_samples_leaf=1, max_features="log2"   |
|           0.798  | n_estimators=20, criterion="entropy", min_samples_leaf=1, max_features="log2"   |
|           0.7957 | n_estimators=10, criterion="entropy", min_samples_leaf=13, max_features="log2"  |

## GradientBoosting
|   accuracy.macro | params                                                                 |
|-----------------:|:-----------------------------------------------------------------------|
|           0.8236 | n_estimators=100, max_depth=7, max_features="log2", learning_rate=0.5  |
|           0.823  | n_estimators=500, max_depth=5, max_features="log2", learning_rate=1    |
|           0.8202 | n_estimators=300, max_depth=7, max_features="log2", learning_rate=0.5  |
|           0.8179 | n_estimators=700, max_depth=7, max_features="log2", learning_rate=0.1  |
|           0.8173 | n_estimators=700, max_depth=5, max_features="log2", learning_rate=0.1  |
|           0.8172 | n_estimators=500, max_depth=7, max_features="log2", learning_rate=0.1  |
|           0.8169 | n_estimators=500, max_depth=7, max_features="log2", learning_rate=1    |
|           0.8168 | n_estimators=300, max_depth=7, max_features="log2", learning_rate=0.01 |
|           0.8166 | n_estimators=500, max_depth=7, max_features="log2", learning_rate=0.01 |
|           0.8165 | n_estimators=500, max_depth=5, max_features="log2", learning_rate=0.5  |
|           0.8152 | n_estimators=700, max_depth=3, max_features="log2", learning_rate=0.1  |
|           0.815  | n_estimators=100, max_depth=7, max_features="log2", learning_rate=0.01 |
|           0.8146 | n_estimators=300, max_depth=5, max_features="log2", learning_rate=0.1  |
|           0.8138 | n_estimators=300, max_depth=7, max_features="log2", learning_rate=0.1  |
|           0.813  | n_estimators=500, max_depth=7, max_features="log2", learning_rate=0.5  |
|           0.813  | n_estimators=700, max_depth=7, max_features="log2", learning_rate=0.5  |
|           0.8127 | n_estimators=500, max_depth=3, max_features="log2", learning_rate=0.5  |
|           0.8125 | n_estimators=700, max_depth=5, max_features="log2", learning_rate=0.01 |
|           0.8121 | n_estimators=700, max_depth=3, max_features="log2", learning_rate=0.5  |
|           0.812  | n_estimators=700, max_depth=7, max_features="log2", learning_rate=0.01 |
|           0.8117 | n_estimators=100, max_depth=5, max_features="log2", learning_rate=0.1  |
|           0.8116 | n_estimators=100, max_depth=5, max_features="log2", learning_rate=0.01 |
|           0.8108 | n_estimators=300, max_depth=5, max_features="log2", learning_rate=0.5  |
|           0.8107 | n_estimators=700, max_depth=5, max_features="log2", learning_rate=0.5  |
|           0.8106 | n_estimators=500, max_depth=5, max_features="log2", learning_rate=0.01 |
|           0.8106 | n_estimators=100, max_depth=7, max_features="log2", learning_rate=1    |
|           0.8103 | n_estimators=500, max_depth=3, max_features="log2", learning_rate=0.1  |
|           0.8098 | n_estimators=300, max_depth=5, max_features="log2", learning_rate=0.01 |
|           0.8093 | n_estimators=500, max_depth=5, max_features="log2", learning_rate=0.1  |
|           0.808  | n_estimators=300, max_depth=3, max_features="log2", learning_rate=0.5  |
|           0.8078 | n_estimators=300, max_depth=3, max_features="log2", learning_rate=0.01 |
|           0.8077 | n_estimators=700, max_depth=1, max_features="log2", learning_rate=0.1  |
|           0.8072 | n_estimators=100, max_depth=3, max_features="log2", learning_rate=0.5  |
|           0.807  | n_estimators=100, max_depth=1, max_features="log2", learning_rate=0.5  |
|           0.8068 | n_estimators=100, max_depth=5, max_features="log2", learning_rate=0.5  |
|           0.8063 | n_estimators=500, max_depth=3, max_features="log2", learning_rate=0.01 |
|           0.8061 | n_estimators=300, max_depth=3, max_features="log2", learning_rate=0.1  |
|           0.806  | n_estimators=100, max_depth=7, max_features="log2", learning_rate=0.1  |
|           0.8052 | n_estimators=500, max_depth=1, max_features="log2", learning_rate=0.1  |
|           0.805  | n_estimators=700, max_depth=3, max_features="log2", learning_rate=0.01 |
|           0.8046 | n_estimators=300, max_depth=1, max_features="log2", learning_rate=0.1  |
|           0.8032 | n_estimators=300, max_depth=1, max_features="log2", learning_rate=0.5  |
|           0.8031 | n_estimators=100, max_depth=3, max_features="log2", learning_rate=0.1  |
|           0.8027 | n_estimators=100, max_depth=1, max_features="log2", learning_rate=0.1  |
|           0.8024 | n_estimators=500, max_depth=1, max_features="log2", learning_rate=0.01 |
|           0.8011 | n_estimators=700, max_depth=1, max_features="log2", learning_rate=0.5  |
|           0.8011 | n_estimators=700, max_depth=1, max_features="log2", learning_rate=0.01 |
|           0.8006 | n_estimators=500, max_depth=1, max_features="log2", learning_rate=0.5  |
|           0.8    | n_estimators=700, max_depth=5, max_features="log2", learning_rate=1    |
|           0.7997 | n_estimators=300, max_depth=1, max_features="log2", learning_rate=0.01 |
|           0.7978 | n_estimators=100, max_depth=3, max_features="log2", learning_rate=0.01 |
|           0.7937 | n_estimators=100, max_depth=1, max_features="log2", learning_rate=0.01 |
|           0.7921 | n_estimators=300, max_depth=7, max_features="log2", learning_rate=1    |
|           0.7856 | n_estimators=100, max_depth=5, max_features="log2", learning_rate=1    |
|           0.7792 | n_estimators=700, max_depth=3, max_features="log2", learning_rate=1    |
|           0.7742 | n_estimators=700, max_depth=7, max_features="log2", learning_rate=1    |
|           0.7726 | n_estimators=500, max_depth=3, max_features="log2", learning_rate=1    |
|           0.7692 | n_estimators=300, max_depth=1, max_features="log2", learning_rate=1    |
|           0.766  | n_estimators=100, max_depth=3, max_features="log2", learning_rate=1    |
|           0.7617 | n_estimators=100, max_depth=1, max_features="log2", learning_rate=1    |
|           0.7508 | n_estimators=500, max_depth=1, max_features="log2", learning_rate=1    |
|           0.7455 | n_estimators=300, max_depth=5, max_features="log2", learning_rate=1    |
|           0.7395 | n_estimators=700, max_depth=1, max_features="log2", learning_rate=1    |
|           0.7268 | n_estimators=300, max_depth=3, max_features="log2", learning_rate=1    |

## LogisticRegression
|   accuracy.macro | params              |
|-----------------:|:--------------------|
|           0.8014 | C=0.1, penalty="l2" |
|           0.7948 | C=1, penalty="l2"   |
|           0.7945 | C=10, penalty="l2"  |
|           0.7942 | C=1, penalty="l1"   |
|           0.793  | C=10, penalty="l1"  |
|           0.7899 | C=0.1, penalty="l1" |

