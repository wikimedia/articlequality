# Model tuning report
- Revscoring version: 2.9.3
- Features: articlequality.feature_lists.nlwiki.wp10
- Date: 2021-02-26T19:14:10.272270
- Observations: 1649
- Labels: ["E", "D", "C", "B", "A"]
- Statistic: accuracy.macro (maximize)
- Folds: 5

# Top scoring configurations
| model                  |   accuracy.macro | params                                                                        |
|:-----------------------|-----------------:|:------------------------------------------------------------------------------|
| GradientBoosting       |           0.9107 | learning_rate=0.01, max_depth=1, max_features="log2", n_estimators=500        |
| RandomForestClassifier |           0.9068 | criterion="gini", max_features="log2", min_samples_leaf=5, n_estimators=10    |
| RandomForestClassifier |           0.9066 | criterion="gini", max_features="log2", min_samples_leaf=13, n_estimators=20   |
| GradientBoosting       |           0.9059 | learning_rate=0.01, max_depth=1, max_features="log2", n_estimators=300        |
| RandomForestClassifier |           0.9027 | criterion="gini", max_features="log2", min_samples_leaf=5, n_estimators=640   |
| RandomForestClassifier |           0.9022 | criterion="entropy", max_features="log2", min_samples_leaf=7, n_estimators=80 |
| RandomForestClassifier |           0.902  | criterion="gini", max_features="log2", min_samples_leaf=5, n_estimators=160   |
| RandomForestClassifier |           0.902  | criterion="gini", max_features="log2", min_samples_leaf=3, n_estimators=640   |
| RandomForestClassifier |           0.9018 | criterion="gini", max_features="log2", min_samples_leaf=3, n_estimators=160   |
| RandomForestClassifier |           0.9015 | criterion="entropy", max_features="log2", min_samples_leaf=5, n_estimators=40 |

# Models
## GradientBoosting
|   accuracy.macro | params                                                                 |
|-----------------:|:-----------------------------------------------------------------------|
|           0.9107 | learning_rate=0.01, max_depth=1, max_features="log2", n_estimators=500 |
|           0.9059 | learning_rate=0.01, max_depth=1, max_features="log2", n_estimators=300 |
|           0.9013 | learning_rate=0.01, max_depth=1, max_features="log2", n_estimators=100 |
|           0.901  | learning_rate=0.5, max_depth=5, max_features="log2", n_estimators=500  |
|           0.9003 | learning_rate=0.01, max_depth=1, max_features="log2", n_estimators=700 |
|           0.9001 | learning_rate=0.5, max_depth=5, max_features="log2", n_estimators=100  |
|           0.8986 | learning_rate=0.5, max_depth=7, max_features="log2", n_estimators=500  |
|           0.8984 | learning_rate=0.01, max_depth=3, max_features="log2", n_estimators=100 |
|           0.8964 | learning_rate=0.5, max_depth=5, max_features="log2", n_estimators=300  |
|           0.8938 | learning_rate=0.01, max_depth=3, max_features="log2", n_estimators=700 |
|           0.8925 | learning_rate=0.5, max_depth=7, max_features="log2", n_estimators=100  |
|           0.8923 | learning_rate=0.01, max_depth=3, max_features="log2", n_estimators=300 |
|           0.8916 | learning_rate=0.01, max_depth=3, max_features="log2", n_estimators=500 |
|           0.8891 | learning_rate=0.1, max_depth=1, max_features="log2", n_estimators=100  |
|           0.8867 | learning_rate=0.1, max_depth=1, max_features="log2", n_estimators=300  |
|           0.8862 | learning_rate=0.1, max_depth=1, max_features="log2", n_estimators=500  |
|           0.8855 | learning_rate=0.5, max_depth=1, max_features="log2", n_estimators=100  |
|           0.8853 | learning_rate=0.5, max_depth=5, max_features="log2", n_estimators=700  |
|           0.8848 | learning_rate=0.1, max_depth=3, max_features="log2", n_estimators=100  |
|           0.8845 | learning_rate=0.1, max_depth=7, max_features="log2", n_estimators=300  |
|           0.8826 | learning_rate=0.5, max_depth=1, max_features="log2", n_estimators=300  |
|           0.8821 | learning_rate=0.01, max_depth=7, max_features="log2", n_estimators=100 |
|           0.8819 | learning_rate=0.1, max_depth=7, max_features="log2", n_estimators=700  |
|           0.8819 | learning_rate=0.5, max_depth=3, max_features="log2", n_estimators=300  |
|           0.8816 | learning_rate=0.01, max_depth=5, max_features="log2", n_estimators=700 |
|           0.8811 | learning_rate=0.01, max_depth=7, max_features="log2", n_estimators=700 |
|           0.8811 | learning_rate=1, max_depth=1, max_features="log2", n_estimators=100    |
|           0.8802 | learning_rate=0.01, max_depth=5, max_features="log2", n_estimators=100 |
|           0.8797 | learning_rate=0.1, max_depth=5, max_features="log2", n_estimators=500  |
|           0.8792 | learning_rate=0.5, max_depth=7, max_features="log2", n_estimators=300  |
|           0.879  | learning_rate=0.1, max_depth=5, max_features="log2", n_estimators=300  |
|           0.879  | learning_rate=0.01, max_depth=5, max_features="log2", n_estimators=500 |
|           0.8787 | learning_rate=0.01, max_depth=7, max_features="log2", n_estimators=300 |
|           0.8785 | learning_rate=0.1, max_depth=5, max_features="log2", n_estimators=100  |
|           0.8777 | learning_rate=0.1, max_depth=3, max_features="log2", n_estimators=500  |
|           0.8773 | learning_rate=0.1, max_depth=5, max_features="log2", n_estimators=700  |
|           0.877  | learning_rate=0.01, max_depth=5, max_features="log2", n_estimators=300 |
|           0.8768 | learning_rate=0.01, max_depth=7, max_features="log2", n_estimators=500 |
|           0.8763 | learning_rate=0.1, max_depth=1, max_features="log2", n_estimators=700  |
|           0.8743 | learning_rate=0.1, max_depth=3, max_features="log2", n_estimators=700  |
|           0.8739 | learning_rate=0.1, max_depth=3, max_features="log2", n_estimators=300  |
|           0.8702 | learning_rate=0.5, max_depth=1, max_features="log2", n_estimators=500  |
|           0.8697 | learning_rate=0.1, max_depth=7, max_features="log2", n_estimators=100  |
|           0.8693 | learning_rate=0.1, max_depth=7, max_features="log2", n_estimators=500  |
|           0.869  | learning_rate=0.5, max_depth=3, max_features="log2", n_estimators=700  |
|           0.8673 | learning_rate=1, max_depth=5, max_features="log2", n_estimators=700    |
|           0.8673 | learning_rate=0.5, max_depth=3, max_features="log2", n_estimators=100  |
|           0.8671 | learning_rate=0.5, max_depth=1, max_features="log2", n_estimators=700  |
|           0.8663 | learning_rate=0.5, max_depth=7, max_features="log2", n_estimators=700  |
|           0.862  | learning_rate=0.5, max_depth=3, max_features="log2", n_estimators=500  |
|           0.8494 | learning_rate=1, max_depth=3, max_features="log2", n_estimators=100    |
|           0.8474 | learning_rate=1, max_depth=7, max_features="log2", n_estimators=300    |
|           0.844  | learning_rate=1, max_depth=3, max_features="log2", n_estimators=700    |
|           0.8433 | learning_rate=1, max_depth=1, max_features="log2", n_estimators=300    |
|           0.8292 | learning_rate=1, max_depth=5, max_features="log2", n_estimators=100    |
|           0.8278 | learning_rate=1, max_depth=3, max_features="log2", n_estimators=300    |
|           0.8276 | learning_rate=1, max_depth=7, max_features="log2", n_estimators=100    |
|           0.8244 | learning_rate=1, max_depth=5, max_features="log2", n_estimators=300    |
|           0.8198 | learning_rate=1, max_depth=7, max_features="log2", n_estimators=700    |
|           0.8193 | learning_rate=1, max_depth=1, max_features="log2", n_estimators=500    |
|           0.8125 | learning_rate=1, max_depth=3, max_features="log2", n_estimators=500    |
|           0.812  | learning_rate=1, max_depth=5, max_features="log2", n_estimators=500    |
|           0.77   | learning_rate=1, max_depth=7, max_features="log2", n_estimators=500    |
|           0.7465 | learning_rate=1, max_depth=1, max_features="log2", n_estimators=700    |

## LogisticRegression
|   accuracy.macro | params              |
|-----------------:|:--------------------|
|           0.8884 | C=1, penalty="l2"   |
|           0.8872 | C=10, penalty="l2"  |
|           0.8799 | C=0.1, penalty="l2" |

## GaussianNB
|   accuracy.macro | params   |
|-----------------:|:---------|
|            0.845 |          |

## BernoulliNB
|   accuracy.macro | params   |
|-----------------:|:---------|
|           0.8904 |          |

## RandomForestClassifier
|   accuracy.macro | params                                                                          |
|-----------------:|:--------------------------------------------------------------------------------|
|           0.9068 | criterion="gini", max_features="log2", min_samples_leaf=5, n_estimators=10      |
|           0.9066 | criterion="gini", max_features="log2", min_samples_leaf=13, n_estimators=20     |
|           0.9027 | criterion="gini", max_features="log2", min_samples_leaf=5, n_estimators=640     |
|           0.9022 | criterion="entropy", max_features="log2", min_samples_leaf=7, n_estimators=80   |
|           0.902  | criterion="gini", max_features="log2", min_samples_leaf=5, n_estimators=160     |
|           0.902  | criterion="gini", max_features="log2", min_samples_leaf=3, n_estimators=640     |
|           0.9018 | criterion="gini", max_features="log2", min_samples_leaf=3, n_estimators=160     |
|           0.9015 | criterion="entropy", max_features="log2", min_samples_leaf=5, n_estimators=40   |
|           0.9013 | criterion="gini", max_features="log2", min_samples_leaf=1, n_estimators=320     |
|           0.9013 | criterion="gini", max_features="log2", min_samples_leaf=3, n_estimators=320     |
|           0.901  | criterion="entropy", max_features="log2", min_samples_leaf=5, n_estimators=640  |
|           0.901  | criterion="gini", max_features="log2", min_samples_leaf=7, n_estimators=160     |
|           0.901  | criterion="entropy", max_features="log2", min_samples_leaf=1, n_estimators=640  |
|           0.901  | criterion="entropy", max_features="log2", min_samples_leaf=3, n_estimators=640  |
|           0.9005 | criterion="entropy", max_features="log2", min_samples_leaf=7, n_estimators=320  |
|           0.9005 | criterion="gini", max_features="log2", min_samples_leaf=3, n_estimators=40      |
|           0.9003 | criterion="entropy", max_features="log2", min_samples_leaf=7, n_estimators=40   |
|           0.9003 | criterion="entropy", max_features="log2", min_samples_leaf=5, n_estimators=320  |
|           0.8998 | criterion="entropy", max_features="log2", min_samples_leaf=7, n_estimators=20   |
|           0.8998 | criterion="entropy", max_features="log2", min_samples_leaf=7, n_estimators=640  |
|           0.8998 | criterion="gini", max_features="log2", min_samples_leaf=7, n_estimators=640     |
|           0.8998 | criterion="entropy", max_features="log2", min_samples_leaf=3, n_estimators=320  |
|           0.8998 | criterion="gini", max_features="log2", min_samples_leaf=7, n_estimators=320     |
|           0.8996 | criterion="gini", max_features="log2", min_samples_leaf=13, n_estimators=640    |
|           0.8996 | criterion="entropy", max_features="log2", min_samples_leaf=3, n_estimators=40   |
|           0.8996 | criterion="entropy", max_features="log2", min_samples_leaf=5, n_estimators=160  |
|           0.8996 | criterion="gini", max_features="log2", min_samples_leaf=5, n_estimators=80      |
|           0.8996 | criterion="gini", max_features="log2", min_samples_leaf=5, n_estimators=320     |
|           0.8993 | criterion="entropy", max_features="log2", min_samples_leaf=13, n_estimators=320 |
|           0.8993 | criterion="entropy", max_features="log2", min_samples_leaf=13, n_estimators=640 |
|           0.8993 | criterion="entropy", max_features="log2", min_samples_leaf=3, n_estimators=160  |
|           0.8993 | criterion="entropy", max_features="log2", min_samples_leaf=5, n_estimators=80   |
|           0.8991 | criterion="entropy", max_features="log2", min_samples_leaf=7, n_estimators=160  |
|           0.8991 | criterion="gini", max_features="log2", min_samples_leaf=7, n_estimators=80      |
|           0.8991 | criterion="entropy", max_features="log2", min_samples_leaf=1, n_estimators=320  |
|           0.8991 | criterion="gini", max_features="log2", min_samples_leaf=3, n_estimators=80      |
|           0.8984 | criterion="gini", max_features="log2", min_samples_leaf=7, n_estimators=40      |
|           0.8984 | criterion="gini", max_features="log2", min_samples_leaf=13, n_estimators=80     |
|           0.8984 | criterion="gini", max_features="log2", min_samples_leaf=7, n_estimators=20      |
|           0.8984 | criterion="gini", max_features="log2", min_samples_leaf=3, n_estimators=20      |
|           0.8981 | criterion="gini", max_features="log2", min_samples_leaf=13, n_estimators=320    |
|           0.8979 | criterion="gini", max_features="log2", min_samples_leaf=5, n_estimators=40      |
|           0.8979 | criterion="gini", max_features="log2", min_samples_leaf=5, n_estimators=20      |
|           0.8979 | criterion="gini", max_features="log2", min_samples_leaf=7, n_estimators=10      |
|           0.8976 | criterion="entropy", max_features="log2", min_samples_leaf=13, n_estimators=80  |
|           0.8976 | criterion="gini", max_features="log2", min_samples_leaf=13, n_estimators=40     |
|           0.8976 | criterion="gini", max_features="log2", min_samples_leaf=1, n_estimators=40      |
|           0.8976 | criterion="entropy", max_features="log2", min_samples_leaf=5, n_estimators=10   |
|           0.8974 | criterion="entropy", max_features="log2", min_samples_leaf=3, n_estimators=80   |
|           0.8974 | criterion="entropy", max_features="log2", min_samples_leaf=7, n_estimators=10   |
|           0.8972 | criterion="gini", max_features="log2", min_samples_leaf=13, n_estimators=160    |
|           0.8967 | criterion="entropy", max_features="log2", min_samples_leaf=5, n_estimators=20   |
|           0.8962 | criterion="entropy", max_features="log2", min_samples_leaf=13, n_estimators=20  |
|           0.8959 | criterion="entropy", max_features="log2", min_samples_leaf=13, n_estimators=160 |
|           0.895  | criterion="gini", max_features="log2", min_samples_leaf=3, n_estimators=10      |
|           0.8933 | criterion="entropy", max_features="log2", min_samples_leaf=1, n_estimators=160  |
|           0.8933 | criterion="gini", max_features="log2", min_samples_leaf=1, n_estimators=160     |
|           0.893  | criterion="gini", max_features="log2", min_samples_leaf=1, n_estimators=640     |
|           0.8925 | criterion="gini", max_features="log2", min_samples_leaf=13, n_estimators=10     |
|           0.8916 | criterion="gini", max_features="log2", min_samples_leaf=1, n_estimators=80      |
|           0.8865 | criterion="entropy", max_features="log2", min_samples_leaf=13, n_estimators=40  |
|           0.8862 | criterion="entropy", max_features="log2", min_samples_leaf=1, n_estimators=40   |
|           0.8848 | criterion="entropy", max_features="log2", min_samples_leaf=3, n_estimators=20   |
|           0.8838 | criterion="entropy", max_features="log2", min_samples_leaf=1, n_estimators=20   |
|           0.8838 | criterion="entropy", max_features="log2", min_samples_leaf=3, n_estimators=10   |
|           0.8838 | criterion="gini", max_features="log2", min_samples_leaf=1, n_estimators=20      |
|           0.8814 | criterion="entropy", max_features="log2", min_samples_leaf=1, n_estimators=80   |
|           0.8792 | criterion="entropy", max_features="log2", min_samples_leaf=13, n_estimators=10  |
|           0.8748 | criterion="gini", max_features="log2", min_samples_leaf=1, n_estimators=10      |
|           0.8678 | criterion="entropy", max_features="log2", min_samples_leaf=1, n_estimators=10   |

