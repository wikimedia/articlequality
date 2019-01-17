# Model tuning report
- Revscoring version: 2.3.0
- Features: articlequality.feature_lists.wikidatawiki.item_quality
- Date: 2019-01-17T21:00:15.762563
- Observations: 4964
- Labels: ["A", "B", "C", "D", "E"]
- Statistic: accuracy.macro (maximize)
- Folds: 5

# Top scoring configurations
| model                  |   accuracy.macro | params                                                                         |
|:-----------------------|-----------------:|:-------------------------------------------------------------------------------|
| GradientBoosting       |           0.9707 | learning_rate=0.01, n_estimators=500, max_features="log2", max_depth=5         |
| RandomForestClassifier |           0.9703 | criterion="entropy", n_estimators=640, max_features="log2", min_samples_leaf=3 |
| RandomForestClassifier |           0.9702 | criterion="gini", n_estimators=20, max_features="log2", min_samples_leaf=3     |
| RandomForestClassifier |           0.9702 | criterion="entropy", n_estimators=320, max_features="log2", min_samples_leaf=3 |
| GradientBoosting       |           0.9701 | learning_rate=0.01, n_estimators=700, max_features="log2", max_depth=5         |
| RandomForestClassifier |           0.97   | criterion="gini", n_estimators=160, max_features="log2", min_samples_leaf=3    |
| RandomForestClassifier |           0.9699 | criterion="gini", n_estimators=160, max_features="log2", min_samples_leaf=1    |
| RandomForestClassifier |           0.9699 | criterion="entropy", n_estimators=160, max_features="log2", min_samples_leaf=3 |
| GradientBoosting       |           0.9699 | learning_rate=0.01, n_estimators=300, max_features="log2", max_depth=5         |
| RandomForestClassifier |           0.9699 | criterion="gini", n_estimators=640, max_features="log2", min_samples_leaf=1    |

# Models
## GaussianNB
|   accuracy.macro | params   |
|-----------------:|:---------|
|            0.882 |          |

## RandomForestClassifier
|   accuracy.macro | params                                                                          |
|-----------------:|:--------------------------------------------------------------------------------|
|           0.9703 | criterion="entropy", n_estimators=640, max_features="log2", min_samples_leaf=3  |
|           0.9702 | criterion="gini", n_estimators=20, max_features="log2", min_samples_leaf=3      |
|           0.9702 | criterion="entropy", n_estimators=320, max_features="log2", min_samples_leaf=3  |
|           0.97   | criterion="gini", n_estimators=160, max_features="log2", min_samples_leaf=3     |
|           0.9699 | criterion="gini", n_estimators=160, max_features="log2", min_samples_leaf=1     |
|           0.9699 | criterion="entropy", n_estimators=160, max_features="log2", min_samples_leaf=3  |
|           0.9699 | criterion="gini", n_estimators=640, max_features="log2", min_samples_leaf=1     |
|           0.9698 | criterion="gini", n_estimators=320, max_features="log2", min_samples_leaf=3     |
|           0.9698 | criterion="gini", n_estimators=640, max_features="log2", min_samples_leaf=3     |
|           0.9697 | criterion="gini", n_estimators=80, max_features="log2", min_samples_leaf=3      |
|           0.9697 | criterion="entropy", n_estimators=40, max_features="log2", min_samples_leaf=3   |
|           0.9696 | criterion="entropy", n_estimators=20, max_features="log2", min_samples_leaf=3   |
|           0.9695 | criterion="gini", n_estimators=40, max_features="log2", min_samples_leaf=3      |
|           0.9695 | criterion="entropy", n_estimators=320, max_features="log2", min_samples_leaf=5  |
|           0.9695 | criterion="entropy", n_estimators=640, max_features="log2", min_samples_leaf=5  |
|           0.9694 | criterion="entropy", n_estimators=160, max_features="log2", min_samples_leaf=5  |
|           0.9692 | criterion="entropy", n_estimators=80, max_features="log2", min_samples_leaf=3   |
|           0.9691 | criterion="gini", n_estimators=640, max_features="log2", min_samples_leaf=5     |
|           0.9691 | criterion="entropy", n_estimators=40, max_features="log2", min_samples_leaf=5   |
|           0.9691 | criterion="gini", n_estimators=320, max_features="log2", min_samples_leaf=1     |
|           0.9691 | criterion="gini", n_estimators=40, max_features="log2", min_samples_leaf=5      |
|           0.9691 | criterion="gini", n_estimators=160, max_features="log2", min_samples_leaf=5     |
|           0.9691 | criterion="gini", n_estimators=320, max_features="log2", min_samples_leaf=5     |
|           0.9691 | criterion="entropy", n_estimators=80, max_features="log2", min_samples_leaf=5   |
|           0.9691 | criterion="gini", n_estimators=80, max_features="log2", min_samples_leaf=5      |
|           0.969  | criterion="gini", n_estimators=80, max_features="log2", min_samples_leaf=1      |
|           0.969  | criterion="entropy", n_estimators=160, max_features="log2", min_samples_leaf=1  |
|           0.969  | criterion="entropy", n_estimators=640, max_features="log2", min_samples_leaf=1  |
|           0.9689 | criterion="gini", n_estimators=20, max_features="log2", min_samples_leaf=5      |
|           0.9689 | criterion="gini", n_estimators=40, max_features="log2", min_samples_leaf=7      |
|           0.9688 | criterion="entropy", n_estimators=320, max_features="log2", min_samples_leaf=1  |
|           0.9687 | criterion="entropy", n_estimators=640, max_features="log2", min_samples_leaf=7  |
|           0.9687 | criterion="entropy", n_estimators=160, max_features="log2", min_samples_leaf=7  |
|           0.9686 | criterion="entropy", n_estimators=80, max_features="log2", min_samples_leaf=7   |
|           0.9685 | criterion="gini", n_estimators=320, max_features="log2", min_samples_leaf=7     |
|           0.9685 | criterion="entropy", n_estimators=320, max_features="log2", min_samples_leaf=7  |
|           0.9684 | criterion="gini", n_estimators=640, max_features="log2", min_samples_leaf=7     |
|           0.9684 | criterion="entropy", n_estimators=80, max_features="log2", min_samples_leaf=1   |
|           0.9682 | criterion="gini", n_estimators=160, max_features="log2", min_samples_leaf=7     |
|           0.9682 | criterion="entropy", n_estimators=40, max_features="log2", min_samples_leaf=7   |
|           0.9681 | criterion="entropy", n_estimators=20, max_features="log2", min_samples_leaf=5   |
|           0.9681 | criterion="entropy", n_estimators=20, max_features="log2", min_samples_leaf=7   |
|           0.968  | criterion="entropy", n_estimators=40, max_features="log2", min_samples_leaf=1   |
|           0.9679 | criterion="gini", n_estimators=80, max_features="log2", min_samples_leaf=7      |
|           0.9678 | criterion="gini", n_estimators=20, max_features="log2", min_samples_leaf=7      |
|           0.9676 | criterion="gini", n_estimators=640, max_features="log2", min_samples_leaf=13    |
|           0.9676 | criterion="entropy", n_estimators=160, max_features="log2", min_samples_leaf=13 |
|           0.9675 | criterion="gini", n_estimators=40, max_features="log2", min_samples_leaf=1      |
|           0.9675 | criterion="entropy", n_estimators=10, max_features="log2", min_samples_leaf=5   |
|           0.9675 | criterion="entropy", n_estimators=640, max_features="log2", min_samples_leaf=13 |
|           0.9674 | criterion="gini", n_estimators=320, max_features="log2", min_samples_leaf=13    |
|           0.9674 | criterion="entropy", n_estimators=80, max_features="log2", min_samples_leaf=13  |
|           0.9673 | criterion="entropy", n_estimators=10, max_features="log2", min_samples_leaf=3   |
|           0.9672 | criterion="gini", n_estimators=160, max_features="log2", min_samples_leaf=13    |
|           0.9672 | criterion="entropy", n_estimators=10, max_features="log2", min_samples_leaf=7   |
|           0.9671 | criterion="gini", n_estimators=10, max_features="log2", min_samples_leaf=5      |
|           0.9671 | criterion="gini", n_estimators=80, max_features="log2", min_samples_leaf=13     |
|           0.9671 | criterion="entropy", n_estimators=320, max_features="log2", min_samples_leaf=13 |
|           0.9669 | criterion="gini", n_estimators=40, max_features="log2", min_samples_leaf=13     |
|           0.9665 | criterion="entropy", n_estimators=40, max_features="log2", min_samples_leaf=13  |
|           0.9663 | criterion="gini", n_estimators=20, max_features="log2", min_samples_leaf=1      |
|           0.9661 | criterion="entropy", n_estimators=20, max_features="log2", min_samples_leaf=1   |
|           0.9661 | criterion="gini", n_estimators=10, max_features="log2", min_samples_leaf=3      |
|           0.9659 | criterion="entropy", n_estimators=10, max_features="log2", min_samples_leaf=1   |
|           0.9657 | criterion="gini", n_estimators=20, max_features="log2", min_samples_leaf=13     |
|           0.9654 | criterion="gini", n_estimators=10, max_features="log2", min_samples_leaf=7      |
|           0.9654 | criterion="gini", n_estimators=10, max_features="log2", min_samples_leaf=1      |
|           0.9649 | criterion="entropy", n_estimators=20, max_features="log2", min_samples_leaf=13  |
|           0.9648 | criterion="gini", n_estimators=10, max_features="log2", min_samples_leaf=13     |
|           0.9641 | criterion="entropy", n_estimators=10, max_features="log2", min_samples_leaf=13  |

## LogisticRegression
|   accuracy.macro | params              |
|-----------------:|:--------------------|
|           0.9305 | penalty="l1", C=10  |
|           0.93   | penalty="l1", C=1   |
|           0.9299 | penalty="l2", C=10  |
|           0.9273 | penalty="l2", C=1   |
|           0.9245 | penalty="l1", C=0.1 |
|           0.9226 | penalty="l2", C=0.1 |

## GradientBoosting
|   accuracy.macro | params                                                                 |
|-----------------:|:-----------------------------------------------------------------------|
|           0.9707 | learning_rate=0.01, n_estimators=500, max_features="log2", max_depth=5 |
|           0.9701 | learning_rate=0.01, n_estimators=700, max_features="log2", max_depth=5 |
|           0.9699 | learning_rate=0.01, n_estimators=300, max_features="log2", max_depth=5 |
|           0.9698 | learning_rate=0.01, n_estimators=700, max_features="log2", max_depth=3 |
|           0.9698 | learning_rate=0.01, n_estimators=300, max_features="log2", max_depth=7 |
|           0.9698 | learning_rate=0.1, n_estimators=100, max_features="log2", max_depth=3  |
|           0.9691 | learning_rate=0.01, n_estimators=100, max_features="log2", max_depth=7 |
|           0.9688 | learning_rate=0.01, n_estimators=500, max_features="log2", max_depth=7 |
|           0.9687 | learning_rate=0.01, n_estimators=500, max_features="log2", max_depth=3 |
|           0.9686 | learning_rate=0.1, n_estimators=300, max_features="log2", max_depth=3  |
|           0.9685 | learning_rate=0.1, n_estimators=100, max_features="log2", max_depth=5  |
|           0.9684 | learning_rate=0.01, n_estimators=700, max_features="log2", max_depth=7 |
|           0.968  | learning_rate=0.1, n_estimators=100, max_features="log2", max_depth=7  |
|           0.9678 | learning_rate=0.1, n_estimators=500, max_features="log2", max_depth=3  |
|           0.9678 | learning_rate=0.1, n_estimators=700, max_features="log2", max_depth=7  |
|           0.9678 | learning_rate=0.5, n_estimators=100, max_features="log2", max_depth=1  |
|           0.9676 | learning_rate=0.1, n_estimators=500, max_features="log2", max_depth=5  |
|           0.9676 | learning_rate=0.1, n_estimators=700, max_features="log2", max_depth=1  |
|           0.9676 | learning_rate=0.1, n_estimators=300, max_features="log2", max_depth=7  |
|           0.9674 | learning_rate=0.1, n_estimators=300, max_features="log2", max_depth=5  |
|           0.9674 | learning_rate=0.1, n_estimators=700, max_features="log2", max_depth=3  |
|           0.9667 | learning_rate=0.1, n_estimators=500, max_features="log2", max_depth=1  |
|           0.9667 | learning_rate=0.1, n_estimators=500, max_features="log2", max_depth=7  |
|           0.9666 | learning_rate=0.5, n_estimators=100, max_features="log2", max_depth=7  |
|           0.9666 | learning_rate=0.5, n_estimators=300, max_features="log2", max_depth=1  |
|           0.9666 | learning_rate=0.5, n_estimators=300, max_features="log2", max_depth=7  |
|           0.9665 | learning_rate=0.1, n_estimators=700, max_features="log2", max_depth=5  |
|           0.9663 | learning_rate=0.01, n_estimators=300, max_features="log2", max_depth=3 |
|           0.9661 | learning_rate=0.5, n_estimators=100, max_features="log2", max_depth=5  |
|           0.9658 | learning_rate=0.5, n_estimators=500, max_features="log2", max_depth=7  |
|           0.9656 | learning_rate=0.1, n_estimators=300, max_features="log2", max_depth=1  |
|           0.9655 | learning_rate=0.01, n_estimators=100, max_features="log2", max_depth=5 |
|           0.9655 | learning_rate=0.5, n_estimators=700, max_features="log2", max_depth=7  |
|           0.9654 | learning_rate=1, n_estimators=100, max_features="log2", max_depth=1    |
|           0.9654 | learning_rate=0.5, n_estimators=700, max_features="log2", max_depth=3  |
|           0.9654 | learning_rate=0.5, n_estimators=700, max_features="log2", max_depth=5  |
|           0.9649 | learning_rate=0.5, n_estimators=500, max_features="log2", max_depth=1  |
|           0.9649 | learning_rate=0.5, n_estimators=500, max_features="log2", max_depth=5  |
|           0.9649 | learning_rate=0.5, n_estimators=500, max_features="log2", max_depth=3  |
|           0.9639 | learning_rate=0.5, n_estimators=700, max_features="log2", max_depth=1  |
|           0.9626 | learning_rate=1, n_estimators=500, max_features="log2", max_depth=1    |
|           0.9614 | learning_rate=0.01, n_estimators=100, max_features="log2", max_depth=3 |
|           0.9593 | learning_rate=1, n_estimators=700, max_features="log2", max_depth=1    |
|           0.9583 | learning_rate=0.5, n_estimators=100, max_features="log2", max_depth=3  |
|           0.9561 | learning_rate=0.1, n_estimators=100, max_features="log2", max_depth=1  |
|           0.9529 | learning_rate=0.01, n_estimators=700, max_features="log2", max_depth=1 |
|           0.9483 | learning_rate=0.01, n_estimators=500, max_features="log2", max_depth=1 |
|           0.9371 | learning_rate=0.01, n_estimators=300, max_features="log2", max_depth=1 |
|           0.9306 | learning_rate=1, n_estimators=300, max_features="log2", max_depth=7    |
|           0.9305 | learning_rate=0.5, n_estimators=300, max_features="log2", max_depth=3  |
|           0.9229 | learning_rate=0.01, n_estimators=100, max_features="log2", max_depth=1 |
|           0.9218 | learning_rate=1, n_estimators=500, max_features="log2", max_depth=7    |
|           0.9203 | learning_rate=1, n_estimators=700, max_features="log2", max_depth=7    |
|           0.9185 | learning_rate=0.5, n_estimators=300, max_features="log2", max_depth=5  |
|           0.9018 | learning_rate=1, n_estimators=100, max_features="log2", max_depth=3    |
|           0.8937 | learning_rate=1, n_estimators=300, max_features="log2", max_depth=1    |
|           0.8929 | learning_rate=1, n_estimators=100, max_features="log2", max_depth=5    |
|           0.877  | learning_rate=1, n_estimators=100, max_features="log2", max_depth=7    |
|           0.8129 | learning_rate=1, n_estimators=700, max_features="log2", max_depth=3    |
|           0.7994 | learning_rate=1, n_estimators=500, max_features="log2", max_depth=5    |
|           0.7868 | learning_rate=1, n_estimators=300, max_features="log2", max_depth=5    |
|           0.7828 | learning_rate=1, n_estimators=300, max_features="log2", max_depth=3    |
|           0.7564 | learning_rate=1, n_estimators=700, max_features="log2", max_depth=5    |
|           0.6884 | learning_rate=1, n_estimators=500, max_features="log2", max_depth=3    |

## BernoulliNB
|   accuracy.macro | params   |
|-----------------:|:---------|
|           0.8856 |          |

