# Model tuning report
- Revscoring version: 2.8.2
- Features: articlequality.feature_lists.nlwiki.wp10
- Date: 2021-01-31T02:57:47.881924
- Observations: 1650
- Labels: ["E", "D", "C", "B", "A"]
- Statistic: accuracy.macro (maximize)
- Folds: 5

# Top scoring configurations
| model                  |   accuracy.macro | params                                                                         |
|:-----------------------|-----------------:|:-------------------------------------------------------------------------------|
| RandomForestClassifier |           0.9067 | max_features="log2", n_estimators=10, criterion="gini", min_samples_leaf=5     |
| RandomForestClassifier |           0.8972 | max_features="log2", n_estimators=80, criterion="gini", min_samples_leaf=5     |
| RandomForestClassifier |           0.8958 | max_features="log2", n_estimators=80, criterion="gini", min_samples_leaf=13    |
| RandomForestClassifier |           0.8955 | max_features="log2", n_estimators=40, criterion="gini", min_samples_leaf=5     |
| RandomForestClassifier |           0.895  | max_features="log2", n_estimators=40, criterion="entropy", min_samples_leaf=13 |
| RandomForestClassifier |           0.895  | max_features="log2", n_estimators=40, criterion="gini", min_samples_leaf=7     |
| RandomForestClassifier |           0.8948 | max_features="log2", n_estimators=40, criterion="entropy", min_samples_leaf=5  |
| RandomForestClassifier |           0.8919 | max_features="log2", n_estimators=20, criterion="entropy", min_samples_leaf=3  |
| RandomForestClassifier |           0.8912 | max_features="log2", n_estimators=20, criterion="entropy", min_samples_leaf=13 |
| RandomForestClassifier |           0.8904 | max_features="log2", n_estimators=10, criterion="entropy", min_samples_leaf=13 |

# Models
## RandomForestClassifier
|   accuracy.macro | params                                                                          |
|-----------------:|:--------------------------------------------------------------------------------|
|           0.9067 | max_features="log2", n_estimators=10, criterion="gini", min_samples_leaf=5      |
|           0.8972 | max_features="log2", n_estimators=80, criterion="gini", min_samples_leaf=5      |
|           0.8958 | max_features="log2", n_estimators=80, criterion="gini", min_samples_leaf=13     |
|           0.8955 | max_features="log2", n_estimators=40, criterion="gini", min_samples_leaf=5      |
|           0.895  | max_features="log2", n_estimators=40, criterion="entropy", min_samples_leaf=13  |
|           0.895  | max_features="log2", n_estimators=40, criterion="gini", min_samples_leaf=7      |
|           0.8948 | max_features="log2", n_estimators=40, criterion="entropy", min_samples_leaf=5   |
|           0.8919 | max_features="log2", n_estimators=20, criterion="entropy", min_samples_leaf=3   |
|           0.8912 | max_features="log2", n_estimators=20, criterion="entropy", min_samples_leaf=13  |
|           0.8904 | max_features="log2", n_estimators=10, criterion="entropy", min_samples_leaf=13  |
|           0.8887 | max_features="log2", n_estimators=640, criterion="gini", min_samples_leaf=13    |
|           0.8873 | max_features="log2", n_estimators=320, criterion="gini", min_samples_leaf=7     |
|           0.8865 | max_features="log2", n_estimators=160, criterion="gini", min_samples_leaf=7     |
|           0.8861 | max_features="log2", n_estimators=160, criterion="entropy", min_samples_leaf=3  |
|           0.8858 | max_features="log2", n_estimators=20, criterion="gini", min_samples_leaf=13     |
|           0.8856 | max_features="log2", n_estimators=160, criterion="gini", min_samples_leaf=5     |
|           0.8856 | max_features="log2", n_estimators=320, criterion="gini", min_samples_leaf=5     |
|           0.8856 | max_features="log2", n_estimators=80, criterion="entropy", min_samples_leaf=3   |
|           0.8856 | max_features="log2", n_estimators=640, criterion="entropy", min_samples_leaf=13 |
|           0.8853 | max_features="log2", n_estimators=640, criterion="gini", min_samples_leaf=7     |
|           0.8851 | max_features="log2", n_estimators=80, criterion="gini", min_samples_leaf=3      |
|           0.8851 | max_features="log2", n_estimators=20, criterion="gini", min_samples_leaf=5      |
|           0.8851 | max_features="log2", n_estimators=160, criterion="entropy", min_samples_leaf=5  |
|           0.8851 | max_features="log2", n_estimators=20, criterion="entropy", min_samples_leaf=5   |
|           0.8851 | max_features="log2", n_estimators=160, criterion="entropy", min_samples_leaf=13 |
|           0.8848 | max_features="log2", n_estimators=320, criterion="entropy", min_samples_leaf=13 |
|           0.8846 | max_features="log2", n_estimators=40, criterion="gini", min_samples_leaf=1      |
|           0.8846 | max_features="log2", n_estimators=640, criterion="gini", min_samples_leaf=5     |
|           0.8846 | max_features="log2", n_estimators=320, criterion="entropy", min_samples_leaf=5  |
|           0.8844 | max_features="log2", n_estimators=40, criterion="entropy", min_samples_leaf=3   |
|           0.8844 | max_features="log2", n_estimators=320, criterion="entropy", min_samples_leaf=7  |
|           0.8844 | max_features="log2", n_estimators=640, criterion="entropy", min_samples_leaf=7  |
|           0.8841 | max_features="log2", n_estimators=640, criterion="entropy", min_samples_leaf=1  |
|           0.8841 | max_features="log2", n_estimators=80, criterion="entropy", min_samples_leaf=7   |
|           0.8839 | max_features="log2", n_estimators=320, criterion="gini", min_samples_leaf=13    |
|           0.8839 | max_features="log2", n_estimators=80, criterion="entropy", min_samples_leaf=1   |
|           0.8839 | max_features="log2", n_estimators=640, criterion="entropy", min_samples_leaf=5  |
|           0.8839 | max_features="log2", n_estimators=320, criterion="entropy", min_samples_leaf=3  |
|           0.8839 | max_features="log2", n_estimators=640, criterion="entropy", min_samples_leaf=3  |
|           0.8836 | max_features="log2", n_estimators=160, criterion="entropy", min_samples_leaf=7  |
|           0.8834 | max_features="log2", n_estimators=20, criterion="entropy", min_samples_leaf=1   |
|           0.8832 | max_features="log2", n_estimators=160, criterion="gini", min_samples_leaf=3     |
|           0.8832 | max_features="log2", n_estimators=160, criterion="gini", min_samples_leaf=13    |
|           0.8832 | max_features="log2", n_estimators=80, criterion="entropy", min_samples_leaf=13  |
|           0.8829 | max_features="log2", n_estimators=640, criterion="gini", min_samples_leaf=3     |
|           0.8829 | max_features="log2", n_estimators=10, criterion="gini", min_samples_leaf=7      |
|           0.8829 | max_features="log2", n_estimators=40, criterion="entropy", min_samples_leaf=7   |
|           0.8827 | max_features="log2", n_estimators=40, criterion="gini", min_samples_leaf=13     |
|           0.8827 | max_features="log2", n_estimators=320, criterion="gini", min_samples_leaf=3     |
|           0.8824 | max_features="log2", n_estimators=80, criterion="entropy", min_samples_leaf=5   |
|           0.8822 | max_features="log2", n_estimators=320, criterion="gini", min_samples_leaf=1     |
|           0.8822 | max_features="log2", n_estimators=20, criterion="entropy", min_samples_leaf=7   |
|           0.8819 | max_features="log2", n_estimators=40, criterion="gini", min_samples_leaf=3      |
|           0.8817 | max_features="log2", n_estimators=80, criterion="gini", min_samples_leaf=7      |
|           0.8817 | max_features="log2", n_estimators=320, criterion="entropy", min_samples_leaf=1  |
|           0.8815 | max_features="log2", n_estimators=20, criterion="gini", min_samples_leaf=3      |
|           0.881  | max_features="log2", n_estimators=10, criterion="entropy", min_samples_leaf=5   |
|           0.8798 | max_features="log2", n_estimators=10, criterion="gini", min_samples_leaf=3      |
|           0.8781 | max_features="log2", n_estimators=640, criterion="gini", min_samples_leaf=1     |
|           0.8776 | max_features="log2", n_estimators=20, criterion="gini", min_samples_leaf=7      |
|           0.8761 | max_features="log2", n_estimators=10, criterion="gini", min_samples_leaf=13     |
|           0.8742 | max_features="log2", n_estimators=80, criterion="gini", min_samples_leaf=1      |
|           0.873  | max_features="log2", n_estimators=10, criterion="entropy", min_samples_leaf=7   |
|           0.8727 | max_features="log2", n_estimators=160, criterion="entropy", min_samples_leaf=1  |
|           0.8718 | max_features="log2", n_estimators=160, criterion="gini", min_samples_leaf=1     |
|           0.8696 | max_features="log2", n_estimators=20, criterion="gini", min_samples_leaf=1      |
|           0.8664 | max_features="log2", n_estimators=10, criterion="gini", min_samples_leaf=1      |
|           0.8616 | max_features="log2", n_estimators=40, criterion="entropy", min_samples_leaf=1   |
|           0.857  | max_features="log2", n_estimators=10, criterion="entropy", min_samples_leaf=3   |
|           0.8558 | max_features="log2", n_estimators=10, criterion="entropy", min_samples_leaf=1   |

## GradientBoosting
|   accuracy.macro | params                                                                 |
|-----------------:|:-----------------------------------------------------------------------|
|           0.8856 | max_depth=1, n_estimators=100, max_features="log2", learning_rate=0.01 |
|           0.8841 | max_depth=3, n_estimators=300, max_features="log2", learning_rate=0.01 |
|           0.8839 | max_depth=7, n_estimators=700, max_features="log2", learning_rate=0.5  |
|           0.8819 | max_depth=3, n_estimators=100, max_features="log2", learning_rate=0.01 |
|           0.88   | max_depth=1, n_estimators=500, max_features="log2", learning_rate=0.01 |
|           0.8771 | max_depth=1, n_estimators=300, max_features="log2", learning_rate=0.01 |
|           0.8771 | max_depth=1, n_estimators=700, max_features="log2", learning_rate=0.01 |
|           0.8737 | max_depth=7, n_estimators=500, max_features="log2", learning_rate=1    |
|           0.872  | max_depth=5, n_estimators=300, max_features="log2", learning_rate=0.01 |
|           0.8713 | max_depth=7, n_estimators=100, max_features="log2", learning_rate=0.1  |
|           0.8701 | max_depth=5, n_estimators=100, max_features="log2", learning_rate=0.01 |
|           0.8696 | max_depth=7, n_estimators=500, max_features="log2", learning_rate=0.1  |
|           0.8693 | max_depth=5, n_estimators=700, max_features="log2", learning_rate=0.01 |
|           0.8693 | max_depth=7, n_estimators=100, max_features="log2", learning_rate=0.01 |
|           0.8691 | max_depth=3, n_estimators=700, max_features="log2", learning_rate=0.01 |
|           0.8691 | max_depth=7, n_estimators=700, max_features="log2", learning_rate=0.01 |
|           0.8691 | max_depth=5, n_estimators=100, max_features="log2", learning_rate=0.1  |
|           0.8686 | max_depth=7, n_estimators=300, max_features="log2", learning_rate=0.01 |
|           0.8686 | max_depth=1, n_estimators=100, max_features="log2", learning_rate=0.1  |
|           0.8684 | max_depth=3, n_estimators=500, max_features="log2", learning_rate=0.01 |
|           0.8684 | max_depth=5, n_estimators=500, max_features="log2", learning_rate=0.01 |
|           0.8684 | max_depth=7, n_estimators=500, max_features="log2", learning_rate=0.01 |
|           0.8681 | max_depth=5, n_estimators=700, max_features="log2", learning_rate=0.5  |
|           0.8672 | max_depth=7, n_estimators=700, max_features="log2", learning_rate=0.1  |
|           0.8662 | max_depth=5, n_estimators=300, max_features="log2", learning_rate=1    |
|           0.8659 | max_depth=5, n_estimators=300, max_features="log2", learning_rate=0.1  |
|           0.8657 | max_depth=7, n_estimators=300, max_features="log2", learning_rate=0.1  |
|           0.8657 | max_depth=5, n_estimators=100, max_features="log2", learning_rate=1    |
|           0.8633 | max_depth=7, n_estimators=700, max_features="log2", learning_rate=1    |
|           0.8616 | max_depth=5, n_estimators=500, max_features="log2", learning_rate=0.1  |
|           0.8613 | max_depth=5, n_estimators=700, max_features="log2", learning_rate=0.1  |
|           0.8601 | max_depth=7, n_estimators=100, max_features="log2", learning_rate=0.5  |
|           0.8594 | max_depth=3, n_estimators=100, max_features="log2", learning_rate=0.5  |
|           0.8587 | max_depth=5, n_estimators=500, max_features="log2", learning_rate=1    |
|           0.8584 | max_depth=5, n_estimators=100, max_features="log2", learning_rate=0.5  |
|           0.8577 | max_depth=1, n_estimators=300, max_features="log2", learning_rate=0.1  |
|           0.8575 | max_depth=1, n_estimators=500, max_features="log2", learning_rate=0.1  |
|           0.857  | max_depth=3, n_estimators=100, max_features="log2", learning_rate=0.1  |
|           0.8565 | max_depth=7, n_estimators=300, max_features="log2", learning_rate=0.5  |
|           0.856  | max_depth=5, n_estimators=500, max_features="log2", learning_rate=0.5  |
|           0.855  | max_depth=3, n_estimators=700, max_features="log2", learning_rate=0.5  |
|           0.855  | max_depth=1, n_estimators=700, max_features="log2", learning_rate=0.1  |
|           0.8548 | max_depth=3, n_estimators=700, max_features="log2", learning_rate=1    |
|           0.8543 | max_depth=3, n_estimators=700, max_features="log2", learning_rate=0.1  |
|           0.8536 | max_depth=3, n_estimators=300, max_features="log2", learning_rate=0.1  |
|           0.8536 | max_depth=3, n_estimators=500, max_features="log2", learning_rate=0.5  |
|           0.8536 | max_depth=7, n_estimators=500, max_features="log2", learning_rate=0.5  |
|           0.8533 | max_depth=5, n_estimators=300, max_features="log2", learning_rate=0.5  |
|           0.8531 | max_depth=3, n_estimators=500, max_features="log2", learning_rate=0.1  |
|           0.8528 | max_depth=1, n_estimators=300, max_features="log2", learning_rate=0.5  |
|           0.8516 | max_depth=1, n_estimators=100, max_features="log2", learning_rate=0.5  |
|           0.8509 | max_depth=1, n_estimators=500, max_features="log2", learning_rate=0.5  |
|           0.849  | max_depth=3, n_estimators=500, max_features="log2", learning_rate=1    |
|           0.8485 | max_depth=1, n_estimators=700, max_features="log2", learning_rate=0.5  |
|           0.8453 | max_depth=3, n_estimators=300, max_features="log2", learning_rate=0.5  |
|           0.8368 | max_depth=1, n_estimators=100, max_features="log2", learning_rate=1    |
|           0.8352 | max_depth=7, n_estimators=300, max_features="log2", learning_rate=1    |
|           0.8315 | max_depth=1, n_estimators=700, max_features="log2", learning_rate=1    |
|           0.8298 | max_depth=7, n_estimators=100, max_features="log2", learning_rate=1    |
|           0.8272 | max_depth=3, n_estimators=300, max_features="log2", learning_rate=1    |
|           0.8233 | max_depth=1, n_estimators=300, max_features="log2", learning_rate=1    |
|           0.8007 | max_depth=5, n_estimators=700, max_features="log2", learning_rate=1    |
|           0.7993 | max_depth=1, n_estimators=500, max_features="log2", learning_rate=1    |
|           0.793  | max_depth=3, n_estimators=100, max_features="log2", learning_rate=1    |

## BernoulliNB
|   accuracy.macro | params   |
|-----------------:|:---------|
|           0.8856 |          |

## LogisticRegression
|   accuracy.macro | params              |
|-----------------:|:--------------------|
|           0.8853 | penalty="l2", C=10  |
|           0.8834 | penalty="l2", C=1   |
|           0.8596 | penalty="l2", C=0.1 |

## GaussianNB
|   accuracy.macro | params   |
|-----------------:|:---------|
|           0.8422 |          |

