# Model tuning report
- Revscoring version: 2.6.9
- Features: articlequality.feature_lists.ptwiki.wp10
- Date: 2020-04-06T19:49:02.070233
- Observations: 7137
- Labels: ["1", "2", "3", "4", "5", "6"]
- Statistic: accuracy.macro (maximize)
- Folds: 5

# Top scoring configurations
| model                  |   accuracy.macro | params                                                                          |
|:-----------------------|-----------------:|:--------------------------------------------------------------------------------|
| GaussianNB             |           0.8942 |                                                                                 |
| RandomForestClassifier |           0.8892 | min_samples_leaf=5, max_features="log2", criterion="entropy", n_estimators=160  |
| RandomForestClassifier |           0.8889 | min_samples_leaf=1, max_features="log2", criterion="gini", n_estimators=320     |
| RandomForestClassifier |           0.8888 | min_samples_leaf=3, max_features="log2", criterion="entropy", n_estimators=640  |
| RandomForestClassifier |           0.8887 | min_samples_leaf=7, max_features="log2", criterion="gini", n_estimators=640     |
| RandomForestClassifier |           0.8886 | min_samples_leaf=3, max_features="log2", criterion="gini", n_estimators=320     |
| RandomForestClassifier |           0.8885 | min_samples_leaf=13, max_features="log2", criterion="entropy", n_estimators=160 |
| RandomForestClassifier |           0.8884 | min_samples_leaf=3, max_features="log2", criterion="entropy", n_estimators=320  |
| RandomForestClassifier |           0.8883 | min_samples_leaf=7, max_features="log2", criterion="entropy", n_estimators=640  |
| GradientBoosting       |           0.888  | max_depth=7, n_estimators=300, max_features="log2", learning_rate=0.01          |

# Models
## GradientBoosting
|   accuracy.macro | params                                                                 |
|-----------------:|:-----------------------------------------------------------------------|
|           0.888  | max_depth=7, n_estimators=300, max_features="log2", learning_rate=0.01 |
|           0.8874 | max_depth=7, n_estimators=100, max_features="log2", learning_rate=0.01 |
|           0.8855 | max_depth=7, n_estimators=500, max_features="log2", learning_rate=0.01 |
|           0.8851 | max_depth=5, n_estimators=500, max_features="log2", learning_rate=0.01 |
|           0.8849 | max_depth=5, n_estimators=100, max_features="log2", learning_rate=0.01 |
|           0.8843 | max_depth=7, n_estimators=700, max_features="log2", learning_rate=0.01 |
|           0.8832 | max_depth=5, n_estimators=700, max_features="log2", learning_rate=0.01 |
|           0.8832 | max_depth=5, n_estimators=300, max_features="log2", learning_rate=0.01 |
|           0.8831 | max_depth=7, n_estimators=700, max_features="log2", learning_rate=0.1  |
|           0.8829 | max_depth=3, n_estimators=500, max_features="log2", learning_rate=0.01 |
|           0.8828 | max_depth=3, n_estimators=300, max_features="log2", learning_rate=0.01 |
|           0.8827 | max_depth=7, n_estimators=100, max_features="log2", learning_rate=0.1  |
|           0.8819 | max_depth=7, n_estimators=500, max_features="log2", learning_rate=0.1  |
|           0.8817 | max_depth=3, n_estimators=700, max_features="log2", learning_rate=0.01 |
|           0.8817 | max_depth=3, n_estimators=100, max_features="log2", learning_rate=0.01 |
|           0.8812 | max_depth=7, n_estimators=300, max_features="log2", learning_rate=0.1  |
|           0.8802 | max_depth=3, n_estimators=100, max_features="log2", learning_rate=0.1  |
|           0.8792 | max_depth=5, n_estimators=300, max_features="log2", learning_rate=0.1  |
|           0.8789 | max_depth=5, n_estimators=500, max_features="log2", learning_rate=0.1  |
|           0.8787 | max_depth=5, n_estimators=700, max_features="log2", learning_rate=0.1  |
|           0.8777 | max_depth=5, n_estimators=100, max_features="log2", learning_rate=0.1  |
|           0.8776 | max_depth=3, n_estimators=500, max_features="log2", learning_rate=0.1  |
|           0.8769 | max_depth=7, n_estimators=700, max_features="log2", learning_rate=0.5  |
|           0.8765 | max_depth=1, n_estimators=100, max_features="log2", learning_rate=0.1  |
|           0.8759 | max_depth=1, n_estimators=700, max_features="log2", learning_rate=0.01 |
|           0.8754 | max_depth=7, n_estimators=500, max_features="log2", learning_rate=0.5  |
|           0.8752 | max_depth=1, n_estimators=500, max_features="log2", learning_rate=0.01 |
|           0.8751 | max_depth=7, n_estimators=100, max_features="log2", learning_rate=0.5  |
|           0.8747 | max_depth=3, n_estimators=700, max_features="log2", learning_rate=0.1  |
|           0.8745 | max_depth=1, n_estimators=300, max_features="log2", learning_rate=0.1  |
|           0.8741 | max_depth=3, n_estimators=300, max_features="log2", learning_rate=0.1  |
|           0.8733 | max_depth=1, n_estimators=300, max_features="log2", learning_rate=0.5  |
|           0.8727 | max_depth=1, n_estimators=300, max_features="log2", learning_rate=0.01 |
|           0.8719 | max_depth=5, n_estimators=500, max_features="log2", learning_rate=0.5  |
|           0.8714 | max_depth=1, n_estimators=100, max_features="log2", learning_rate=0.01 |
|           0.8691 | max_depth=1, n_estimators=500, max_features="log2", learning_rate=0.1  |
|           0.8689 | max_depth=7, n_estimators=300, max_features="log2", learning_rate=0.5  |
|           0.8675 | max_depth=3, n_estimators=500, max_features="log2", learning_rate=0.5  |
|           0.8669 | max_depth=1, n_estimators=700, max_features="log2", learning_rate=0.1  |
|           0.8637 | max_depth=3, n_estimators=700, max_features="log2", learning_rate=0.5  |
|           0.8637 | max_depth=1, n_estimators=100, max_features="log2", learning_rate=0.5  |
|           0.8622 | max_depth=5, n_estimators=100, max_features="log2", learning_rate=0.5  |
|           0.8617 | max_depth=1, n_estimators=300, max_features="log2", learning_rate=1    |
|           0.861  | max_depth=1, n_estimators=500, max_features="log2", learning_rate=0.5  |
|           0.8599 | max_depth=1, n_estimators=700, max_features="log2", learning_rate=0.5  |
|           0.8597 | max_depth=3, n_estimators=300, max_features="log2", learning_rate=0.5  |
|           0.8579 | max_depth=3, n_estimators=100, max_features="log2", learning_rate=0.5  |
|           0.8554 | max_depth=1, n_estimators=100, max_features="log2", learning_rate=1    |
|           0.8515 | max_depth=5, n_estimators=700, max_features="log2", learning_rate=0.5  |
|           0.8462 | max_depth=1, n_estimators=500, max_features="log2", learning_rate=1    |
|           0.8431 | max_depth=1, n_estimators=700, max_features="log2", learning_rate=1    |
|           0.8415 | max_depth=3, n_estimators=100, max_features="log2", learning_rate=1    |
|           0.8406 | max_depth=3, n_estimators=300, max_features="log2", learning_rate=1    |
|           0.8401 | max_depth=5, n_estimators=100, max_features="log2", learning_rate=1    |
|           0.8386 | max_depth=5, n_estimators=300, max_features="log2", learning_rate=0.5  |
|           0.838  | max_depth=7, n_estimators=700, max_features="log2", learning_rate=1    |
|           0.8365 | max_depth=7, n_estimators=100, max_features="log2", learning_rate=1    |
|           0.8011 | max_depth=7, n_estimators=500, max_features="log2", learning_rate=1    |
|           0.7776 | max_depth=3, n_estimators=500, max_features="log2", learning_rate=1    |
|           0.7617 | max_depth=3, n_estimators=700, max_features="log2", learning_rate=1    |
|           0.7535 | max_depth=7, n_estimators=300, max_features="log2", learning_rate=1    |
|           0.7513 | max_depth=5, n_estimators=500, max_features="log2", learning_rate=1    |
|           0.744  | max_depth=5, n_estimators=300, max_features="log2", learning_rate=1    |
|           0.7156 | max_depth=5, n_estimators=700, max_features="log2", learning_rate=1    |

## BernoulliNB
|   accuracy.macro | params   |
|-----------------:|:---------|
|           0.8811 |          |

## GaussianNB
|   accuracy.macro | params   |
|-----------------:|:---------|
|           0.8942 |          |

## RandomForestClassifier
|   accuracy.macro | params                                                                          |
|-----------------:|:--------------------------------------------------------------------------------|
|           0.8892 | min_samples_leaf=5, max_features="log2", criterion="entropy", n_estimators=160  |
|           0.8889 | min_samples_leaf=1, max_features="log2", criterion="gini", n_estimators=320     |
|           0.8888 | min_samples_leaf=3, max_features="log2", criterion="entropy", n_estimators=640  |
|           0.8887 | min_samples_leaf=7, max_features="log2", criterion="gini", n_estimators=640     |
|           0.8886 | min_samples_leaf=3, max_features="log2", criterion="gini", n_estimators=320     |
|           0.8885 | min_samples_leaf=13, max_features="log2", criterion="entropy", n_estimators=160 |
|           0.8884 | min_samples_leaf=3, max_features="log2", criterion="entropy", n_estimators=320  |
|           0.8883 | min_samples_leaf=7, max_features="log2", criterion="entropy", n_estimators=640  |
|           0.8879 | min_samples_leaf=13, max_features="log2", criterion="entropy", n_estimators=320 |
|           0.8878 | min_samples_leaf=13, max_features="log2", criterion="entropy", n_estimators=640 |
|           0.8877 | min_samples_leaf=5, max_features="log2", criterion="gini", n_estimators=640     |
|           0.8877 | min_samples_leaf=7, max_features="log2", criterion="entropy", n_estimators=80   |
|           0.8876 | min_samples_leaf=1, max_features="log2", criterion="gini", n_estimators=640     |
|           0.8876 | min_samples_leaf=1, max_features="log2", criterion="entropy", n_estimators=640  |
|           0.8876 | min_samples_leaf=5, max_features="log2", criterion="gini", n_estimators=320     |
|           0.8875 | min_samples_leaf=3, max_features="log2", criterion="entropy", n_estimators=160  |
|           0.8875 | min_samples_leaf=5, max_features="log2", criterion="gini", n_estimators=80      |
|           0.8874 | min_samples_leaf=13, max_features="log2", criterion="entropy", n_estimators=80  |
|           0.8874 | min_samples_leaf=5, max_features="log2", criterion="entropy", n_estimators=320  |
|           0.8873 | min_samples_leaf=13, max_features="log2", criterion="gini", n_estimators=640    |
|           0.8872 | min_samples_leaf=7, max_features="log2", criterion="entropy", n_estimators=160  |
|           0.8872 | min_samples_leaf=3, max_features="log2", criterion="entropy", n_estimators=80   |
|           0.8872 | min_samples_leaf=3, max_features="log2", criterion="gini", n_estimators=160     |
|           0.8872 | min_samples_leaf=7, max_features="log2", criterion="gini", n_estimators=80      |
|           0.8871 | min_samples_leaf=5, max_features="log2", criterion="entropy", n_estimators=640  |
|           0.887  | min_samples_leaf=7, max_features="log2", criterion="entropy", n_estimators=320  |
|           0.8869 | min_samples_leaf=13, max_features="log2", criterion="gini", n_estimators=320    |
|           0.8869 | min_samples_leaf=5, max_features="log2", criterion="gini", n_estimators=160     |
|           0.8869 | min_samples_leaf=1, max_features="log2", criterion="entropy", n_estimators=320  |
|           0.8866 | min_samples_leaf=1, max_features="log2", criterion="entropy", n_estimators=160  |
|           0.8865 | min_samples_leaf=7, max_features="log2", criterion="gini", n_estimators=160     |
|           0.8865 | min_samples_leaf=3, max_features="log2", criterion="gini", n_estimators=640     |
|           0.8864 | min_samples_leaf=5, max_features="log2", criterion="entropy", n_estimators=40   |
|           0.8864 | min_samples_leaf=13, max_features="log2", criterion="gini", n_estimators=160    |
|           0.8864 | min_samples_leaf=3, max_features="log2", criterion="gini", n_estimators=40      |
|           0.8863 | min_samples_leaf=5, max_features="log2", criterion="gini", n_estimators=40      |
|           0.8863 | min_samples_leaf=7, max_features="log2", criterion="gini", n_estimators=320     |
|           0.8862 | min_samples_leaf=1, max_features="log2", criterion="gini", n_estimators=160     |
|           0.8861 | min_samples_leaf=1, max_features="log2", criterion="entropy", n_estimators=80   |
|           0.8861 | min_samples_leaf=13, max_features="log2", criterion="gini", n_estimators=80     |
|           0.8861 | min_samples_leaf=13, max_features="log2", criterion="entropy", n_estimators=40  |
|           0.8861 | min_samples_leaf=1, max_features="log2", criterion="gini", n_estimators=80      |
|           0.886  | min_samples_leaf=5, max_features="log2", criterion="entropy", n_estimators=80   |
|           0.8859 | min_samples_leaf=5, max_features="log2", criterion="entropy", n_estimators=20   |
|           0.8856 | min_samples_leaf=7, max_features="log2", criterion="entropy", n_estimators=20   |
|           0.8855 | min_samples_leaf=7, max_features="log2", criterion="entropy", n_estimators=40   |
|           0.8853 | min_samples_leaf=7, max_features="log2", criterion="gini", n_estimators=40      |
|           0.885  | min_samples_leaf=13, max_features="log2", criterion="gini", n_estimators=40     |
|           0.885  | min_samples_leaf=3, max_features="log2", criterion="entropy", n_estimators=20   |
|           0.8845 | min_samples_leaf=13, max_features="log2", criterion="entropy", n_estimators=20  |
|           0.8844 | min_samples_leaf=1, max_features="log2", criterion="gini", n_estimators=40      |
|           0.8844 | min_samples_leaf=3, max_features="log2", criterion="gini", n_estimators=80      |
|           0.8839 | min_samples_leaf=13, max_features="log2", criterion="entropy", n_estimators=10  |
|           0.8837 | min_samples_leaf=1, max_features="log2", criterion="entropy", n_estimators=40   |
|           0.8835 | min_samples_leaf=7, max_features="log2", criterion="gini", n_estimators=20      |
|           0.8832 | min_samples_leaf=13, max_features="log2", criterion="gini", n_estimators=20     |
|           0.8828 | min_samples_leaf=5, max_features="log2", criterion="entropy", n_estimators=10   |
|           0.8822 | min_samples_leaf=1, max_features="log2", criterion="entropy", n_estimators=20   |
|           0.8818 | min_samples_leaf=3, max_features="log2", criterion="gini", n_estimators=20      |
|           0.8817 | min_samples_leaf=3, max_features="log2", criterion="entropy", n_estimators=40   |
|           0.8814 | min_samples_leaf=13, max_features="log2", criterion="gini", n_estimators=10     |
|           0.8812 | min_samples_leaf=1, max_features="log2", criterion="entropy", n_estimators=10   |
|           0.8808 | min_samples_leaf=1, max_features="log2", criterion="gini", n_estimators=10      |
|           0.8801 | min_samples_leaf=1, max_features="log2", criterion="gini", n_estimators=20      |
|           0.8792 | min_samples_leaf=7, max_features="log2", criterion="gini", n_estimators=10      |
|           0.8791 | min_samples_leaf=7, max_features="log2", criterion="entropy", n_estimators=10   |
|           0.8785 | min_samples_leaf=5, max_features="log2", criterion="gini", n_estimators=10      |
|           0.8768 | min_samples_leaf=5, max_features="log2", criterion="gini", n_estimators=20      |
|           0.8758 | min_samples_leaf=3, max_features="log2", criterion="entropy", n_estimators=10   |
|           0.8756 | min_samples_leaf=3, max_features="log2", criterion="gini", n_estimators=10      |

## LogisticRegression
|   accuracy.macro | params              |
|-----------------:|:--------------------|
|           0.8816 | penalty="l1", C=1   |
|           0.8813 | penalty="l1", C=0.1 |
|           0.8812 | penalty="l2", C=0.1 |
|           0.8811 | penalty="l2", C=10  |
|           0.8811 | penalty="l1", C=10  |
|           0.881  | penalty="l2", C=1   |

