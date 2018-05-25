# Model tuning report
- Revscoring version: 2.2.3
- Features: articlequality.feature_lists.euwiki.wp10
- Date: 2018-05-20T12:39:37.852088
- Observations: 282
- Labels: ["Stub", "Start", "C", "B", "GA", "FA"]
- Statistic: accuracy.macro (maximize)
- Folds: 5

# Top scoring configurations
| model                  |   accuracy.macro | params                                                                          |
|:-----------------------|-----------------:|:--------------------------------------------------------------------------------|
| RandomForestClassifier |           0.883  | min_samples_leaf=13, criterion="entropy", n_estimators=40, max_features="log2"  |
| GradientBoosting       |           0.8806 | learning_rate=0.01, max_depth=3, n_estimators=100, max_features="log2"          |
| RandomForestClassifier |           0.8794 | min_samples_leaf=13, criterion="gini", n_estimators=40, max_features="log2"     |
| RandomForestClassifier |           0.8794 | min_samples_leaf=7, criterion="gini", n_estimators=80, max_features="log2"      |
| RandomForestClassifier |           0.8794 | min_samples_leaf=13, criterion="entropy", n_estimators=640, max_features="log2" |
| RandomForestClassifier |           0.8783 | min_samples_leaf=3, criterion="entropy", n_estimators=40, max_features="log2"   |
| RandomForestClassifier |           0.8771 | min_samples_leaf=3, criterion="gini", n_estimators=320, max_features="log2"     |
| RandomForestClassifier |           0.8771 | min_samples_leaf=1, criterion="entropy", n_estimators=10, max_features="log2"   |
| RandomForestClassifier |           0.8771 | min_samples_leaf=1, criterion="gini", n_estimators=40, max_features="log2"      |
| RandomForestClassifier |           0.8771 | min_samples_leaf=7, criterion="gini", n_estimators=160, max_features="log2"     |

# Models
## GradientBoosting
|   accuracy.macro | params                                                                 |
|-----------------:|:-----------------------------------------------------------------------|
|           0.8806 | learning_rate=0.01, max_depth=3, n_estimators=100, max_features="log2" |
|           0.8759 | learning_rate=0.01, max_depth=1, n_estimators=300, max_features="log2" |
|           0.8759 | learning_rate=0.01, max_depth=3, n_estimators=300, max_features="log2" |
|           0.8747 | learning_rate=0.1, max_depth=5, n_estimators=300, max_features="log2"  |
|           0.8735 | learning_rate=0.01, max_depth=5, n_estimators=500, max_features="log2" |
|           0.8712 | learning_rate=0.01, max_depth=7, n_estimators=100, max_features="log2" |
|           0.8712 | learning_rate=0.1, max_depth=1, n_estimators=100, max_features="log2"  |
|           0.8712 | learning_rate=0.1, max_depth=5, n_estimators=500, max_features="log2"  |
|           0.8712 | learning_rate=0.01, max_depth=5, n_estimators=700, max_features="log2" |
|           0.87   | learning_rate=0.01, max_depth=1, n_estimators=700, max_features="log2" |
|           0.87   | learning_rate=0.01, max_depth=7, n_estimators=700, max_features="log2" |
|           0.87   | learning_rate=0.1, max_depth=7, n_estimators=700, max_features="log2"  |
|           0.87   | learning_rate=1, max_depth=5, n_estimators=500, max_features="log2"    |
|           0.87   | learning_rate=0.01, max_depth=1, n_estimators=500, max_features="log2" |
|           0.87   | learning_rate=0.01, max_depth=5, n_estimators=100, max_features="log2" |
|           0.8688 | learning_rate=0.01, max_depth=7, n_estimators=500, max_features="log2" |
|           0.8688 | learning_rate=0.1, max_depth=3, n_estimators=300, max_features="log2"  |
|           0.8688 | learning_rate=0.1, max_depth=7, n_estimators=300, max_features="log2"  |
|           0.8688 | learning_rate=0.5, max_depth=5, n_estimators=700, max_features="log2"  |
|           0.8676 | learning_rate=0.5, max_depth=5, n_estimators=100, max_features="log2"  |
|           0.8676 | learning_rate=0.5, max_depth=5, n_estimators=300, max_features="log2"  |
|           0.8676 | learning_rate=0.01, max_depth=3, n_estimators=500, max_features="log2" |
|           0.8676 | learning_rate=0.01, max_depth=3, n_estimators=700, max_features="log2" |
|           0.8676 | learning_rate=0.1, max_depth=3, n_estimators=100, max_features="log2"  |
|           0.8664 | learning_rate=0.1, max_depth=3, n_estimators=500, max_features="log2"  |
|           0.8664 | learning_rate=0.1, max_depth=5, n_estimators=100, max_features="log2"  |
|           0.8664 | learning_rate=0.1, max_depth=5, n_estimators=700, max_features="log2"  |
|           0.8652 | learning_rate=0.01, max_depth=7, n_estimators=300, max_features="log2" |
|           0.8652 | learning_rate=0.01, max_depth=5, n_estimators=300, max_features="log2" |
|           0.8652 | learning_rate=0.1, max_depth=3, n_estimators=700, max_features="log2"  |
|           0.8652 | learning_rate=0.1, max_depth=7, n_estimators=100, max_features="log2"  |
|           0.8652 | learning_rate=0.1, max_depth=7, n_estimators=500, max_features="log2"  |
|           0.8652 | learning_rate=0.5, max_depth=5, n_estimators=500, max_features="log2"  |
|           0.8652 | learning_rate=0.5, max_depth=7, n_estimators=500, max_features="log2"  |
|           0.8652 | learning_rate=1, max_depth=7, n_estimators=100, max_features="log2"    |
|           0.8641 | learning_rate=0.5, max_depth=1, n_estimators=100, max_features="log2"  |
|           0.8617 | learning_rate=0.5, max_depth=3, n_estimators=500, max_features="log2"  |
|           0.8617 | learning_rate=0.5, max_depth=1, n_estimators=700, max_features="log2"  |
|           0.8605 | learning_rate=0.5, max_depth=7, n_estimators=300, max_features="log2"  |
|           0.8605 | learning_rate=0.1, max_depth=1, n_estimators=300, max_features="log2"  |
|           0.8605 | learning_rate=0.5, max_depth=1, n_estimators=500, max_features="log2"  |
|           0.8605 | learning_rate=0.5, max_depth=7, n_estimators=100, max_features="log2"  |
|           0.8605 | learning_rate=1, max_depth=1, n_estimators=500, max_features="log2"    |
|           0.8593 | learning_rate=0.5, max_depth=3, n_estimators=100, max_features="log2"  |
|           0.8593 | learning_rate=1, max_depth=3, n_estimators=300, max_features="log2"    |
|           0.8593 | learning_rate=1, max_depth=5, n_estimators=700, max_features="log2"    |
|           0.8582 | learning_rate=0.5, max_depth=7, n_estimators=700, max_features="log2"  |
|           0.8582 | learning_rate=1, max_depth=7, n_estimators=700, max_features="log2"    |
|           0.857  | learning_rate=0.1, max_depth=1, n_estimators=700, max_features="log2"  |
|           0.857  | learning_rate=0.01, max_depth=1, n_estimators=100, max_features="log2" |
|           0.8558 | learning_rate=0.1, max_depth=1, n_estimators=500, max_features="log2"  |
|           0.8558 | learning_rate=0.5, max_depth=1, n_estimators=300, max_features="log2"  |
|           0.8558 | learning_rate=0.5, max_depth=3, n_estimators=300, max_features="log2"  |
|           0.8558 | learning_rate=1, max_depth=1, n_estimators=100, max_features="log2"    |
|           0.8558 | learning_rate=1, max_depth=1, n_estimators=300, max_features="log2"    |
|           0.8558 | learning_rate=1, max_depth=3, n_estimators=100, max_features="log2"    |
|           0.8546 | learning_rate=1, max_depth=7, n_estimators=300, max_features="log2"    |
|           0.8522 | learning_rate=0.5, max_depth=3, n_estimators=700, max_features="log2"  |
|           0.8522 | learning_rate=1, max_depth=5, n_estimators=100, max_features="log2"    |
|           0.8499 | learning_rate=1, max_depth=5, n_estimators=300, max_features="log2"    |
|           0.8499 | learning_rate=1, max_depth=7, n_estimators=500, max_features="log2"    |
|           0.8416 | learning_rate=1, max_depth=3, n_estimators=500, max_features="log2"    |
|           0.8286 | learning_rate=1, max_depth=3, n_estimators=700, max_features="log2"    |
|           0.8227 | learning_rate=1, max_depth=1, n_estimators=700, max_features="log2"    |

## BernoulliNB
|   accuracy.macro | params   |
|-----------------:|:---------|
|           0.7849 |          |

## RandomForestClassifier
|   accuracy.macro | params                                                                          |
|-----------------:|:--------------------------------------------------------------------------------|
|           0.883  | min_samples_leaf=13, criterion="entropy", n_estimators=40, max_features="log2"  |
|           0.8794 | min_samples_leaf=13, criterion="gini", n_estimators=40, max_features="log2"     |
|           0.8794 | min_samples_leaf=7, criterion="gini", n_estimators=80, max_features="log2"      |
|           0.8794 | min_samples_leaf=13, criterion="entropy", n_estimators=640, max_features="log2" |
|           0.8783 | min_samples_leaf=3, criterion="entropy", n_estimators=40, max_features="log2"   |
|           0.8771 | min_samples_leaf=3, criterion="gini", n_estimators=320, max_features="log2"     |
|           0.8771 | min_samples_leaf=1, criterion="entropy", n_estimators=10, max_features="log2"   |
|           0.8771 | min_samples_leaf=1, criterion="gini", n_estimators=40, max_features="log2"      |
|           0.8771 | min_samples_leaf=7, criterion="gini", n_estimators=160, max_features="log2"     |
|           0.8771 | min_samples_leaf=13, criterion="gini", n_estimators=640, max_features="log2"    |
|           0.8759 | min_samples_leaf=1, criterion="gini", n_estimators=160, max_features="log2"     |
|           0.8759 | min_samples_leaf=1, criterion="entropy", n_estimators=320, max_features="log2"  |
|           0.8759 | min_samples_leaf=13, criterion="gini", n_estimators=160, max_features="log2"    |
|           0.8759 | min_samples_leaf=3, criterion="entropy", n_estimators=640, max_features="log2"  |
|           0.8759 | min_samples_leaf=5, criterion="entropy", n_estimators=320, max_features="log2"  |
|           0.8747 | min_samples_leaf=13, criterion="gini", n_estimators=20, max_features="log2"     |
|           0.8747 | min_samples_leaf=1, criterion="gini", n_estimators=20, max_features="log2"      |
|           0.8747 | min_samples_leaf=1, criterion="gini", n_estimators=640, max_features="log2"     |
|           0.8747 | min_samples_leaf=7, criterion="gini", n_estimators=320, max_features="log2"     |
|           0.8747 | min_samples_leaf=7, criterion="gini", n_estimators=640, max_features="log2"     |
|           0.8747 | min_samples_leaf=5, criterion="entropy", n_estimators=40, max_features="log2"   |
|           0.8747 | min_samples_leaf=7, criterion="entropy", n_estimators=80, max_features="log2"   |
|           0.8735 | min_samples_leaf=7, criterion="gini", n_estimators=40, max_features="log2"      |
|           0.8735 | min_samples_leaf=13, criterion="gini", n_estimators=10, max_features="log2"     |
|           0.8735 | min_samples_leaf=1, criterion="entropy", n_estimators=640, max_features="log2"  |
|           0.8735 | min_samples_leaf=5, criterion="entropy", n_estimators=160, max_features="log2"  |
|           0.8723 | min_samples_leaf=1, criterion="gini", n_estimators=80, max_features="log2"      |
|           0.8723 | min_samples_leaf=3, criterion="gini", n_estimators=10, max_features="log2"      |
|           0.8723 | min_samples_leaf=3, criterion="gini", n_estimators=40, max_features="log2"      |
|           0.8723 | min_samples_leaf=13, criterion="gini", n_estimators=80, max_features="log2"     |
|           0.8723 | min_samples_leaf=13, criterion="gini", n_estimators=320, max_features="log2"    |
|           0.8723 | min_samples_leaf=1, criterion="entropy", n_estimators=40, max_features="log2"   |
|           0.8723 | min_samples_leaf=1, criterion="entropy", n_estimators=160, max_features="log2"  |
|           0.8723 | min_samples_leaf=3, criterion="entropy", n_estimators=160, max_features="log2"  |
|           0.8723 | min_samples_leaf=7, criterion="entropy", n_estimators=160, max_features="log2"  |
|           0.8723 | min_samples_leaf=7, criterion="entropy", n_estimators=320, max_features="log2"  |
|           0.8723 | min_samples_leaf=7, criterion="entropy", n_estimators=640, max_features="log2"  |
|           0.8712 | min_samples_leaf=1, criterion="gini", n_estimators=320, max_features="log2"     |
|           0.8712 | min_samples_leaf=3, criterion="entropy", n_estimators=320, max_features="log2"  |
|           0.8712 | min_samples_leaf=7, criterion="entropy", n_estimators=40, max_features="log2"   |
|           0.8712 | min_samples_leaf=5, criterion="gini", n_estimators=80, max_features="log2"      |
|           0.87   | min_samples_leaf=5, criterion="gini", n_estimators=320, max_features="log2"     |
|           0.87   | min_samples_leaf=13, criterion="entropy", n_estimators=320, max_features="log2" |
|           0.8688 | min_samples_leaf=3, criterion="gini", n_estimators=160, max_features="log2"     |
|           0.8688 | min_samples_leaf=3, criterion="gini", n_estimators=640, max_features="log2"     |
|           0.8688 | min_samples_leaf=5, criterion="gini", n_estimators=640, max_features="log2"     |
|           0.8688 | min_samples_leaf=1, criterion="entropy", n_estimators=20, max_features="log2"   |
|           0.8688 | min_samples_leaf=3, criterion="entropy", n_estimators=80, max_features="log2"   |
|           0.8688 | min_samples_leaf=5, criterion="entropy", n_estimators=640, max_features="log2"  |
|           0.8688 | min_samples_leaf=7, criterion="gini", n_estimators=20, max_features="log2"      |
|           0.8688 | min_samples_leaf=5, criterion="entropy", n_estimators=20, max_features="log2"   |
|           0.8688 | min_samples_leaf=5, criterion="entropy", n_estimators=80, max_features="log2"   |
|           0.8688 | min_samples_leaf=7, criterion="entropy", n_estimators=10, max_features="log2"   |
|           0.8688 | min_samples_leaf=13, criterion="entropy", n_estimators=20, max_features="log2"  |
|           0.8676 | min_samples_leaf=5, criterion="gini", n_estimators=20, max_features="log2"      |
|           0.8676 | min_samples_leaf=5, criterion="gini", n_estimators=160, max_features="log2"     |
|           0.8676 | min_samples_leaf=3, criterion="entropy", n_estimators=20, max_features="log2"   |
|           0.8676 | min_samples_leaf=5, criterion="entropy", n_estimators=10, max_features="log2"   |
|           0.8676 | min_samples_leaf=13, criterion="entropy", n_estimators=80, max_features="log2"  |
|           0.8676 | min_samples_leaf=13, criterion="entropy", n_estimators=160, max_features="log2" |
|           0.8664 | min_samples_leaf=3, criterion="gini", n_estimators=80, max_features="log2"      |
|           0.8664 | min_samples_leaf=1, criterion="gini", n_estimators=10, max_features="log2"      |
|           0.8664 | min_samples_leaf=1, criterion="entropy", n_estimators=80, max_features="log2"   |
|           0.8664 | min_samples_leaf=3, criterion="entropy", n_estimators=10, max_features="log2"   |
|           0.8652 | min_samples_leaf=3, criterion="gini", n_estimators=20, max_features="log2"      |
|           0.8652 | min_samples_leaf=5, criterion="gini", n_estimators=40, max_features="log2"      |
|           0.8641 | min_samples_leaf=7, criterion="entropy", n_estimators=20, max_features="log2"   |
|           0.8629 | min_samples_leaf=13, criterion="entropy", n_estimators=10, max_features="log2"  |
|           0.8617 | min_samples_leaf=5, criterion="gini", n_estimators=10, max_features="log2"      |
|           0.8546 | min_samples_leaf=7, criterion="gini", n_estimators=10, max_features="log2"      |

## LogisticRegression
|   accuracy.macro | params              |
|-----------------:|:--------------------|
|           0.8499 | penalty="l2", C=0.1 |
|           0.8487 | penalty="l2", C=1   |
|           0.8487 | penalty="l2", C=10  |
|           0.844  | penalty="l1", C=0.1 |
|           0.8381 | penalty="l1", C=1   |
|           0.8381 | penalty="l1", C=10  |

## GaussianNB
|   accuracy.macro | params   |
|-----------------:|:---------|
|           0.8298 |          |

