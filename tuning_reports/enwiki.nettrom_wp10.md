# Model tuning report
- Revscoring version: 2.4.0
- Features: articlequality.feature_lists.enwiki.wp10
- Date: 2019-07-24T19:54:17.736136
- Observations: 32402
- Labels: ["Stub", "Start", "C", "B", "GA", "FA"]
- Statistic: accuracy.macro (maximize)
- Folds: 5

# Top scoring configurations
| model                  |   accuracy.macro | params                                                                         |
|:-----------------------|-----------------:|:-------------------------------------------------------------------------------|
| GradientBoosting       |           0.8936 | learning_rate=0.01, n_estimators=700, max_features="log2", max_depth=7         |
| GradientBoosting       |           0.8935 | learning_rate=0.01, n_estimators=500, max_features="log2", max_depth=7         |
| RandomForestClassifier |           0.8933 | criterion="gini", min_samples_leaf=1, max_features="log2", n_estimators=640    |
| RandomForestClassifier |           0.8933 | criterion="entropy", min_samples_leaf=3, max_features="log2", n_estimators=320 |
| RandomForestClassifier |           0.8933 | criterion="gini", min_samples_leaf=1, max_features="log2", n_estimators=320    |
| RandomForestClassifier |           0.8932 | criterion="entropy", min_samples_leaf=3, max_features="log2", n_estimators=640 |
| RandomForestClassifier |           0.8931 | criterion="entropy", min_samples_leaf=1, max_features="log2", n_estimators=640 |
| RandomForestClassifier |           0.8931 | criterion="gini", min_samples_leaf=3, max_features="log2", n_estimators=640    |
| RandomForestClassifier |           0.893  | criterion="entropy", min_samples_leaf=1, max_features="log2", n_estimators=320 |
| RandomForestClassifier |           0.8929 | criterion="gini", min_samples_leaf=3, max_features="log2", n_estimators=320    |

# Models
## LogisticRegression
|   accuracy.macro | params              |
|-----------------:|:--------------------|
|           0.8859 | C=10, penalty="l1"  |
|           0.8844 | C=1, penalty="l1"   |
|           0.8831 | C=0.1, penalty="l1" |
|           0.872  | C=1, penalty="l2"   |
|           0.8701 | C=0.1, penalty="l2" |
|           0.87   | C=10, penalty="l2"  |

## GaussianNB
|   accuracy.macro | params   |
|-----------------:|:---------|
|           0.8598 |          |

## GradientBoosting
|   accuracy.macro | params                                                                 |
|-----------------:|:-----------------------------------------------------------------------|
|           0.8936 | learning_rate=0.01, n_estimators=700, max_features="log2", max_depth=7 |
|           0.8935 | learning_rate=0.01, n_estimators=500, max_features="log2", max_depth=7 |
|           0.8923 | learning_rate=0.01, n_estimators=700, max_features="log2", max_depth=5 |
|           0.892  | learning_rate=0.01, n_estimators=300, max_features="log2", max_depth=7 |
|           0.8916 | learning_rate=0.01, n_estimators=500, max_features="log2", max_depth=5 |
|           0.8915 | learning_rate=0.1, n_estimators=100, max_features="log2", max_depth=7  |
|           0.891  | learning_rate=0.1, n_estimators=100, max_features="log2", max_depth=5  |
|           0.8909 | learning_rate=0.1, n_estimators=700, max_features="log2", max_depth=3  |
|           0.8909 | learning_rate=0.1, n_estimators=300, max_features="log2", max_depth=3  |
|           0.8908 | learning_rate=0.1, n_estimators=300, max_features="log2", max_depth=5  |
|           0.8908 | learning_rate=0.1, n_estimators=500, max_features="log2", max_depth=3  |
|           0.8902 | learning_rate=0.1, n_estimators=300, max_features="log2", max_depth=7  |
|           0.89   | learning_rate=0.01, n_estimators=300, max_features="log2", max_depth=5 |
|           0.89   | learning_rate=0.1, n_estimators=500, max_features="log2", max_depth=5  |
|           0.89   | learning_rate=0.1, n_estimators=500, max_features="log2", max_depth=7  |
|           0.8898 | learning_rate=0.1, n_estimators=100, max_features="log2", max_depth=3  |
|           0.8897 | learning_rate=0.1, n_estimators=700, max_features="log2", max_depth=7  |
|           0.8896 | learning_rate=0.01, n_estimators=100, max_features="log2", max_depth=7 |
|           0.8896 | learning_rate=0.1, n_estimators=700, max_features="log2", max_depth=5  |
|           0.889  | learning_rate=0.01, n_estimators=700, max_features="log2", max_depth=3 |
|           0.8875 | learning_rate=0.01, n_estimators=500, max_features="log2", max_depth=3 |
|           0.8871 | learning_rate=0.5, n_estimators=500, max_features="log2", max_depth=1  |
|           0.8868 | learning_rate=0.1, n_estimators=700, max_features="log2", max_depth=1  |
|           0.8868 | learning_rate=0.5, n_estimators=300, max_features="log2", max_depth=1  |
|           0.8865 | learning_rate=0.5, n_estimators=700, max_features="log2", max_depth=1  |
|           0.8864 | learning_rate=0.01, n_estimators=100, max_features="log2", max_depth=5 |
|           0.8864 | learning_rate=0.1, n_estimators=500, max_features="log2", max_depth=1  |
|           0.886  | learning_rate=0.1, n_estimators=300, max_features="log2", max_depth=1  |
|           0.8857 | learning_rate=0.5, n_estimators=100, max_features="log2", max_depth=3  |
|           0.8857 | learning_rate=1, n_estimators=300, max_features="log2", max_depth=1    |
|           0.8857 | learning_rate=1, n_estimators=500, max_features="log2", max_depth=1    |
|           0.8856 | learning_rate=0.5, n_estimators=100, max_features="log2", max_depth=1  |
|           0.8855 | learning_rate=0.01, n_estimators=300, max_features="log2", max_depth=3 |
|           0.8853 | learning_rate=0.5, n_estimators=500, max_features="log2", max_depth=7  |
|           0.8853 | learning_rate=1, n_estimators=700, max_features="log2", max_depth=1    |
|           0.8848 | learning_rate=0.5, n_estimators=700, max_features="log2", max_depth=7  |
|           0.8848 | learning_rate=1, n_estimators=100, max_features="log2", max_depth=1    |
|           0.8843 | learning_rate=0.5, n_estimators=300, max_features="log2", max_depth=7  |
|           0.8842 | learning_rate=0.5, n_estimators=300, max_features="log2", max_depth=3  |
|           0.8841 | learning_rate=0.5, n_estimators=500, max_features="log2", max_depth=3  |
|           0.8833 | learning_rate=0.01, n_estimators=100, max_features="log2", max_depth=3 |
|           0.8832 | learning_rate=0.1, n_estimators=100, max_features="log2", max_depth=1  |
|           0.8823 | learning_rate=0.5, n_estimators=100, max_features="log2", max_depth=5  |
|           0.8823 | learning_rate=0.5, n_estimators=700, max_features="log2", max_depth=3  |
|           0.882  | learning_rate=0.5, n_estimators=100, max_features="log2", max_depth=7  |
|           0.8817 | learning_rate=0.01, n_estimators=700, max_features="log2", max_depth=1 |
|           0.8817 | learning_rate=0.5, n_estimators=300, max_features="log2", max_depth=5  |
|           0.8804 | learning_rate=0.5, n_estimators=700, max_features="log2", max_depth=5  |
|           0.8803 | learning_rate=0.01, n_estimators=500, max_features="log2", max_depth=1 |
|           0.8803 | learning_rate=1, n_estimators=100, max_features="log2", max_depth=3    |
|           0.8778 | learning_rate=0.01, n_estimators=300, max_features="log2", max_depth=1 |
|           0.8778 | learning_rate=1, n_estimators=300, max_features="log2", max_depth=3    |
|           0.8776 | learning_rate=0.5, n_estimators=500, max_features="log2", max_depth=5  |
|           0.8768 | learning_rate=0.01, n_estimators=100, max_features="log2", max_depth=1 |
|           0.8742 | learning_rate=1, n_estimators=100, max_features="log2", max_depth=5    |
|           0.8729 | learning_rate=1, n_estimators=500, max_features="log2", max_depth=3    |
|           0.8707 | learning_rate=1, n_estimators=100, max_features="log2", max_depth=7    |
|           0.8583 | learning_rate=1, n_estimators=300, max_features="log2", max_depth=5    |
|           0.8302 | learning_rate=1, n_estimators=700, max_features="log2", max_depth=3    |
|           0.8228 | learning_rate=1, n_estimators=300, max_features="log2", max_depth=7    |
|           0.8061 | learning_rate=1, n_estimators=500, max_features="log2", max_depth=5    |
|           0.7895 | learning_rate=1, n_estimators=700, max_features="log2", max_depth=7    |
|           0.7784 | learning_rate=1, n_estimators=500, max_features="log2", max_depth=7    |
|           0.7671 | learning_rate=1, n_estimators=700, max_features="log2", max_depth=5    |

## RandomForestClassifier
|   accuracy.macro | params                                                                          |
|-----------------:|:--------------------------------------------------------------------------------|
|           0.8933 | criterion="gini", min_samples_leaf=1, max_features="log2", n_estimators=640     |
|           0.8933 | criterion="entropy", min_samples_leaf=3, max_features="log2", n_estimators=320  |
|           0.8933 | criterion="gini", min_samples_leaf=1, max_features="log2", n_estimators=320     |
|           0.8932 | criterion="entropy", min_samples_leaf=3, max_features="log2", n_estimators=640  |
|           0.8931 | criterion="entropy", min_samples_leaf=1, max_features="log2", n_estimators=640  |
|           0.8931 | criterion="gini", min_samples_leaf=3, max_features="log2", n_estimators=640     |
|           0.893  | criterion="entropy", min_samples_leaf=1, max_features="log2", n_estimators=320  |
|           0.8929 | criterion="gini", min_samples_leaf=3, max_features="log2", n_estimators=320     |
|           0.8928 | criterion="gini", min_samples_leaf=5, max_features="log2", n_estimators=320     |
|           0.8926 | criterion="gini", min_samples_leaf=3, max_features="log2", n_estimators=160     |
|           0.8925 | criterion="gini", min_samples_leaf=5, max_features="log2", n_estimators=640     |
|           0.8924 | criterion="entropy", min_samples_leaf=3, max_features="log2", n_estimators=160  |
|           0.8924 | criterion="gini", min_samples_leaf=5, max_features="log2", n_estimators=160     |
|           0.8924 | criterion="entropy", min_samples_leaf=5, max_features="log2", n_estimators=640  |
|           0.8923 | criterion="entropy", min_samples_leaf=5, max_features="log2", n_estimators=320  |
|           0.8923 | criterion="entropy", min_samples_leaf=7, max_features="log2", n_estimators=640  |
|           0.8922 | criterion="gini", min_samples_leaf=7, max_features="log2", n_estimators=640     |
|           0.8922 | criterion="entropy", min_samples_leaf=3, max_features="log2", n_estimators=80   |
|           0.8922 | criterion="gini", min_samples_leaf=1, max_features="log2", n_estimators=160     |
|           0.8921 | criterion="gini", min_samples_leaf=7, max_features="log2", n_estimators=320     |
|           0.8921 | criterion="entropy", min_samples_leaf=5, max_features="log2", n_estimators=160  |
|           0.8918 | criterion="entropy", min_samples_leaf=7, max_features="log2", n_estimators=320  |
|           0.8918 | criterion="gini", min_samples_leaf=7, max_features="log2", n_estimators=160     |
|           0.8917 | criterion="gini", min_samples_leaf=3, max_features="log2", n_estimators=80      |
|           0.8915 | criterion="entropy", min_samples_leaf=5, max_features="log2", n_estimators=80   |
|           0.8915 | criterion="entropy", min_samples_leaf=1, max_features="log2", n_estimators=160  |
|           0.8913 | criterion="entropy", min_samples_leaf=7, max_features="log2", n_estimators=160  |
|           0.8912 | criterion="gini", min_samples_leaf=5, max_features="log2", n_estimators=80      |
|           0.8912 | criterion="gini", min_samples_leaf=7, max_features="log2", n_estimators=80      |
|           0.8911 | criterion="entropy", min_samples_leaf=7, max_features="log2", n_estimators=80   |
|           0.891  | criterion="entropy", min_samples_leaf=1, max_features="log2", n_estimators=80   |
|           0.891  | criterion="entropy", min_samples_leaf=5, max_features="log2", n_estimators=40   |
|           0.8908 | criterion="entropy", min_samples_leaf=13, max_features="log2", n_estimators=320 |
|           0.8906 | criterion="gini", min_samples_leaf=13, max_features="log2", n_estimators=160    |
|           0.8906 | criterion="gini", min_samples_leaf=13, max_features="log2", n_estimators=640    |
|           0.8906 | criterion="entropy", min_samples_leaf=7, max_features="log2", n_estimators=40   |
|           0.8905 | criterion="entropy", min_samples_leaf=13, max_features="log2", n_estimators=640 |
|           0.8905 | criterion="entropy", min_samples_leaf=13, max_features="log2", n_estimators=160 |
|           0.8905 | criterion="gini", min_samples_leaf=1, max_features="log2", n_estimators=80      |
|           0.8905 | criterion="gini", min_samples_leaf=13, max_features="log2", n_estimators=320    |
|           0.8904 | criterion="gini", min_samples_leaf=13, max_features="log2", n_estimators=80     |
|           0.8903 | criterion="gini", min_samples_leaf=5, max_features="log2", n_estimators=40      |
|           0.8902 | criterion="entropy", min_samples_leaf=3, max_features="log2", n_estimators=40   |
|           0.8902 | criterion="entropy", min_samples_leaf=13, max_features="log2", n_estimators=80  |
|           0.8901 | criterion="gini", min_samples_leaf=7, max_features="log2", n_estimators=40      |
|           0.8898 | criterion="gini", min_samples_leaf=3, max_features="log2", n_estimators=40      |
|           0.8896 | criterion="entropy", min_samples_leaf=13, max_features="log2", n_estimators=40  |
|           0.8895 | criterion="entropy", min_samples_leaf=7, max_features="log2", n_estimators=20   |
|           0.8892 | criterion="gini", min_samples_leaf=13, max_features="log2", n_estimators=40     |
|           0.8891 | criterion="gini", min_samples_leaf=7, max_features="log2", n_estimators=20      |
|           0.889  | criterion="entropy", min_samples_leaf=1, max_features="log2", n_estimators=40   |
|           0.8888 | criterion="gini", min_samples_leaf=1, max_features="log2", n_estimators=40      |
|           0.8886 | criterion="gini", min_samples_leaf=5, max_features="log2", n_estimators=20      |
|           0.8884 | criterion="entropy", min_samples_leaf=13, max_features="log2", n_estimators=20  |
|           0.8884 | criterion="gini", min_samples_leaf=13, max_features="log2", n_estimators=20     |
|           0.8883 | criterion="gini", min_samples_leaf=3, max_features="log2", n_estimators=20      |
|           0.8881 | criterion="entropy", min_samples_leaf=3, max_features="log2", n_estimators=20   |
|           0.888  | criterion="entropy", min_samples_leaf=5, max_features="log2", n_estimators=20   |
|           0.8871 | criterion="gini", min_samples_leaf=13, max_features="log2", n_estimators=10     |
|           0.887  | criterion="entropy", min_samples_leaf=13, max_features="log2", n_estimators=10  |
|           0.8864 | criterion="gini", min_samples_leaf=7, max_features="log2", n_estimators=10      |
|           0.8862 | criterion="entropy", min_samples_leaf=7, max_features="log2", n_estimators=10   |
|           0.8859 | criterion="entropy", min_samples_leaf=3, max_features="log2", n_estimators=10   |
|           0.8857 | criterion="gini", min_samples_leaf=5, max_features="log2", n_estimators=10      |
|           0.8856 | criterion="gini", min_samples_leaf=1, max_features="log2", n_estimators=20      |
|           0.8851 | criterion="gini", min_samples_leaf=3, max_features="log2", n_estimators=10      |
|           0.8849 | criterion="entropy", min_samples_leaf=1, max_features="log2", n_estimators=20   |
|           0.8849 | criterion="entropy", min_samples_leaf=5, max_features="log2", n_estimators=10   |
|           0.8777 | criterion="gini", min_samples_leaf=1, max_features="log2", n_estimators=10      |
|           0.8777 | criterion="entropy", min_samples_leaf=1, max_features="log2", n_estimators=10   |

## BernoulliNB
|   accuracy.macro | params   |
|-----------------:|:---------|
|           0.8234 |          |

