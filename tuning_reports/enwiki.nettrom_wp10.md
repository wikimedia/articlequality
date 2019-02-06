# Model tuning report
- Revscoring version: 2.3.0
- Features: articlequality.feature_lists.enwiki.wp10
- Date: 2019-01-29T01:40:33.762685
- Observations: 32415
- Labels: ["Stub", "Start", "C", "B", "GA", "FA"]
- Statistic: accuracy.macro (maximize)
- Folds: 5

# Top scoring configurations
| model                  |   accuracy.macro | params                                                                         |
|:-----------------------|-----------------:|:-------------------------------------------------------------------------------|
| RandomForestClassifier |           0.8932 | n_estimators=640, criterion="gini", min_samples_leaf=1, max_features="log2"    |
| RandomForestClassifier |           0.8926 | n_estimators=640, criterion="gini", min_samples_leaf=3, max_features="log2"    |
| GradientBoosting       |           0.8926 | learning_rate=0.01, n_estimators=500, max_depth=7, max_features="log2"         |
| RandomForestClassifier |           0.8925 | n_estimators=640, criterion="entropy", min_samples_leaf=1, max_features="log2" |
| RandomForestClassifier |           0.8924 | n_estimators=320, criterion="gini", min_samples_leaf=1, max_features="log2"    |
| GradientBoosting       |           0.8924 | learning_rate=0.01, n_estimators=700, max_depth=7, max_features="log2"         |
| RandomForestClassifier |           0.8924 | n_estimators=640, criterion="entropy", min_samples_leaf=3, max_features="log2" |
| RandomForestClassifier |           0.8922 | n_estimators=640, criterion="entropy", min_samples_leaf=5, max_features="log2" |
| GradientBoosting       |           0.8921 | learning_rate=0.01, n_estimators=700, max_depth=5, max_features="log2"         |
| RandomForestClassifier |           0.8921 | n_estimators=320, criterion="gini", min_samples_leaf=3, max_features="log2"    |

# Models
## LogisticRegression
|   accuracy.macro | params              |
|-----------------:|:--------------------|
|           0.8851 | penalty="l1", C=10  |
|           0.8842 | penalty="l1", C=1   |
|           0.8829 | penalty="l1", C=0.1 |
|           0.8718 | penalty="l2", C=10  |
|           0.8713 | penalty="l2", C=1   |
|           0.8707 | penalty="l2", C=0.1 |

## BernoulliNB
|   accuracy.macro | params   |
|-----------------:|:---------|
|           0.8265 |          |

## RandomForestClassifier
|   accuracy.macro | params                                                                          |
|-----------------:|:--------------------------------------------------------------------------------|
|           0.8932 | n_estimators=640, criterion="gini", min_samples_leaf=1, max_features="log2"     |
|           0.8926 | n_estimators=640, criterion="gini", min_samples_leaf=3, max_features="log2"     |
|           0.8925 | n_estimators=640, criterion="entropy", min_samples_leaf=1, max_features="log2"  |
|           0.8924 | n_estimators=320, criterion="gini", min_samples_leaf=1, max_features="log2"     |
|           0.8924 | n_estimators=640, criterion="entropy", min_samples_leaf=3, max_features="log2"  |
|           0.8922 | n_estimators=640, criterion="entropy", min_samples_leaf=5, max_features="log2"  |
|           0.8921 | n_estimators=320, criterion="gini", min_samples_leaf=3, max_features="log2"     |
|           0.8921 | n_estimators=160, criterion="entropy", min_samples_leaf=1, max_features="log2"  |
|           0.8921 | n_estimators=320, criterion="entropy", min_samples_leaf=1, max_features="log2"  |
|           0.892  | n_estimators=160, criterion="gini", min_samples_leaf=3, max_features="log2"     |
|           0.8919 | n_estimators=160, criterion="entropy", min_samples_leaf=3, max_features="log2"  |
|           0.8919 | n_estimators=640, criterion="gini", min_samples_leaf=5, max_features="log2"     |
|           0.8918 | n_estimators=320, criterion="entropy", min_samples_leaf=3, max_features="log2"  |
|           0.8916 | n_estimators=320, criterion="entropy", min_samples_leaf=5, max_features="log2"  |
|           0.8916 | n_estimators=640, criterion="entropy", min_samples_leaf=7, max_features="log2"  |
|           0.8916 | n_estimators=160, criterion="gini", min_samples_leaf=1, max_features="log2"     |
|           0.8915 | n_estimators=160, criterion="gini", min_samples_leaf=7, max_features="log2"     |
|           0.8915 | n_estimators=320, criterion="gini", min_samples_leaf=5, max_features="log2"     |
|           0.8915 | n_estimators=640, criterion="gini", min_samples_leaf=7, max_features="log2"     |
|           0.8914 | n_estimators=80, criterion="entropy", min_samples_leaf=3, max_features="log2"   |
|           0.8914 | n_estimators=160, criterion="gini", min_samples_leaf=5, max_features="log2"     |
|           0.8913 | n_estimators=160, criterion="entropy", min_samples_leaf=5, max_features="log2"  |
|           0.8913 | n_estimators=80, criterion="gini", min_samples_leaf=3, max_features="log2"      |
|           0.8912 | n_estimators=80, criterion="entropy", min_samples_leaf=5, max_features="log2"   |
|           0.8912 | n_estimators=320, criterion="entropy", min_samples_leaf=7, max_features="log2"  |
|           0.891  | n_estimators=320, criterion="gini", min_samples_leaf=7, max_features="log2"     |
|           0.891  | n_estimators=40, criterion="gini", min_samples_leaf=5, max_features="log2"      |
|           0.8909 | n_estimators=160, criterion="entropy", min_samples_leaf=7, max_features="log2"  |
|           0.8908 | n_estimators=80, criterion="entropy", min_samples_leaf=7, max_features="log2"   |
|           0.8906 | n_estimators=80, criterion="gini", min_samples_leaf=1, max_features="log2"      |
|           0.8905 | n_estimators=80, criterion="gini", min_samples_leaf=7, max_features="log2"      |
|           0.8905 | n_estimators=80, criterion="gini", min_samples_leaf=5, max_features="log2"      |
|           0.8904 | n_estimators=320, criterion="entropy", min_samples_leaf=13, max_features="log2" |
|           0.8902 | n_estimators=40, criterion="entropy", min_samples_leaf=3, max_features="log2"   |
|           0.8902 | n_estimators=320, criterion="gini", min_samples_leaf=13, max_features="log2"    |
|           0.8902 | n_estimators=40, criterion="gini", min_samples_leaf=3, max_features="log2"      |
|           0.8901 | n_estimators=640, criterion="gini", min_samples_leaf=13, max_features="log2"    |
|           0.8901 | n_estimators=80, criterion="gini", min_samples_leaf=13, max_features="log2"     |
|           0.8901 | n_estimators=160, criterion="entropy", min_samples_leaf=13, max_features="log2" |
|           0.8901 | n_estimators=40, criterion="gini", min_samples_leaf=7, max_features="log2"      |
|           0.89   | n_estimators=80, criterion="entropy", min_samples_leaf=1, max_features="log2"   |
|           0.89   | n_estimators=640, criterion="entropy", min_samples_leaf=13, max_features="log2" |
|           0.8899 | n_estimators=160, criterion="gini", min_samples_leaf=13, max_features="log2"    |
|           0.8899 | n_estimators=40, criterion="entropy", min_samples_leaf=7, max_features="log2"   |
|           0.8899 | n_estimators=40, criterion="entropy", min_samples_leaf=5, max_features="log2"   |
|           0.8896 | n_estimators=80, criterion="entropy", min_samples_leaf=13, max_features="log2"  |
|           0.8893 | n_estimators=40, criterion="gini", min_samples_leaf=13, max_features="log2"     |
|           0.8893 | n_estimators=40, criterion="entropy", min_samples_leaf=13, max_features="log2"  |
|           0.889  | n_estimators=20, criterion="gini", min_samples_leaf=5, max_features="log2"      |
|           0.8888 | n_estimators=20, criterion="gini", min_samples_leaf=7, max_features="log2"      |
|           0.8888 | n_estimators=40, criterion="gini", min_samples_leaf=1, max_features="log2"      |
|           0.8887 | n_estimators=40, criterion="entropy", min_samples_leaf=1, max_features="log2"   |
|           0.8887 | n_estimators=20, criterion="gini", min_samples_leaf=13, max_features="log2"     |
|           0.8883 | n_estimators=20, criterion="entropy", min_samples_leaf=7, max_features="log2"   |
|           0.888  | n_estimators=20, criterion="entropy", min_samples_leaf=13, max_features="log2"  |
|           0.8877 | n_estimators=20, criterion="gini", min_samples_leaf=3, max_features="log2"      |
|           0.8876 | n_estimators=10, criterion="gini", min_samples_leaf=13, max_features="log2"     |
|           0.8871 | n_estimators=10, criterion="gini", min_samples_leaf=7, max_features="log2"      |
|           0.887  | n_estimators=20, criterion="entropy", min_samples_leaf=5, max_features="log2"   |
|           0.8867 | n_estimators=20, criterion="entropy", min_samples_leaf=3, max_features="log2"   |
|           0.8859 | n_estimators=10, criterion="entropy", min_samples_leaf=7, max_features="log2"   |
|           0.8856 | n_estimators=10, criterion="gini", min_samples_leaf=5, max_features="log2"      |
|           0.8854 | n_estimators=10, criterion="entropy", min_samples_leaf=13, max_features="log2"  |
|           0.8847 | n_estimators=10, criterion="gini", min_samples_leaf=3, max_features="log2"      |
|           0.8846 | n_estimators=10, criterion="entropy", min_samples_leaf=5, max_features="log2"   |
|           0.8845 | n_estimators=20, criterion="entropy", min_samples_leaf=1, max_features="log2"   |
|           0.8843 | n_estimators=10, criterion="entropy", min_samples_leaf=3, max_features="log2"   |
|           0.8843 | n_estimators=20, criterion="gini", min_samples_leaf=1, max_features="log2"      |
|           0.8785 | n_estimators=10, criterion="entropy", min_samples_leaf=1, max_features="log2"   |
|           0.8775 | n_estimators=10, criterion="gini", min_samples_leaf=1, max_features="log2"      |

## GradientBoosting
|   accuracy.macro | params                                                                 |
|-----------------:|:-----------------------------------------------------------------------|
|           0.8926 | learning_rate=0.01, n_estimators=500, max_depth=7, max_features="log2" |
|           0.8924 | learning_rate=0.01, n_estimators=700, max_depth=7, max_features="log2" |
|           0.8921 | learning_rate=0.01, n_estimators=700, max_depth=5, max_features="log2" |
|           0.8916 | learning_rate=0.01, n_estimators=300, max_depth=7, max_features="log2" |
|           0.8911 | learning_rate=0.01, n_estimators=500, max_depth=5, max_features="log2" |
|           0.8911 | learning_rate=0.1, n_estimators=500, max_depth=3, max_features="log2"  |
|           0.8909 | learning_rate=0.1, n_estimators=100, max_depth=7, max_features="log2"  |
|           0.8907 | learning_rate=0.1, n_estimators=100, max_depth=5, max_features="log2"  |
|           0.8906 | learning_rate=0.1, n_estimators=300, max_depth=3, max_features="log2"  |
|           0.8904 | learning_rate=0.1, n_estimators=300, max_depth=5, max_features="log2"  |
|           0.89   | learning_rate=0.1, n_estimators=300, max_depth=7, max_features="log2"  |
|           0.8899 | learning_rate=0.1, n_estimators=700, max_depth=3, max_features="log2"  |
|           0.8899 | learning_rate=0.01, n_estimators=300, max_depth=5, max_features="log2" |
|           0.8899 | learning_rate=0.01, n_estimators=100, max_depth=7, max_features="log2" |
|           0.8895 | learning_rate=0.1, n_estimators=700, max_depth=7, max_features="log2"  |
|           0.8895 | learning_rate=0.1, n_estimators=100, max_depth=3, max_features="log2"  |
|           0.8895 | learning_rate=0.1, n_estimators=500, max_depth=7, max_features="log2"  |
|           0.8893 | learning_rate=0.1, n_estimators=500, max_depth=5, max_features="log2"  |
|           0.8892 | learning_rate=0.01, n_estimators=700, max_depth=3, max_features="log2" |
|           0.8887 | learning_rate=0.1, n_estimators=700, max_depth=5, max_features="log2"  |
|           0.8881 | learning_rate=0.01, n_estimators=500, max_depth=3, max_features="log2" |
|           0.8872 | learning_rate=0.5, n_estimators=300, max_depth=1, max_features="log2"  |
|           0.8871 | learning_rate=0.1, n_estimators=700, max_depth=1, max_features="log2"  |
|           0.8869 | learning_rate=0.01, n_estimators=100, max_depth=5, max_features="log2" |
|           0.8869 | learning_rate=0.5, n_estimators=700, max_depth=1, max_features="log2"  |
|           0.8866 | learning_rate=0.1, n_estimators=500, max_depth=1, max_features="log2"  |
|           0.8861 | learning_rate=0.5, n_estimators=500, max_depth=1, max_features="log2"  |
|           0.886  | learning_rate=0.5, n_estimators=100, max_depth=3, max_features="log2"  |
|           0.8858 | learning_rate=0.01, n_estimators=300, max_depth=3, max_features="log2" |
|           0.8858 | learning_rate=1, n_estimators=300, max_depth=1, max_features="log2"    |
|           0.8857 | learning_rate=1, n_estimators=500, max_depth=1, max_features="log2"    |
|           0.8857 | learning_rate=0.1, n_estimators=300, max_depth=1, max_features="log2"  |
|           0.8856 | learning_rate=0.5, n_estimators=500, max_depth=7, max_features="log2"  |
|           0.8855 | learning_rate=0.5, n_estimators=300, max_depth=7, max_features="log2"  |
|           0.8853 | learning_rate=0.5, n_estimators=700, max_depth=7, max_features="log2"  |
|           0.8848 | learning_rate=0.5, n_estimators=100, max_depth=1, max_features="log2"  |
|           0.8842 | learning_rate=1, n_estimators=700, max_depth=1, max_features="log2"    |
|           0.8837 | learning_rate=0.5, n_estimators=300, max_depth=3, max_features="log2"  |
|           0.8834 | learning_rate=0.01, n_estimators=100, max_depth=3, max_features="log2" |
|           0.8833 | learning_rate=1, n_estimators=100, max_depth=1, max_features="log2"    |
|           0.8828 | learning_rate=0.1, n_estimators=100, max_depth=1, max_features="log2"  |
|           0.8819 | learning_rate=0.5, n_estimators=500, max_depth=5, max_features="log2"  |
|           0.8816 | learning_rate=0.01, n_estimators=700, max_depth=1, max_features="log2" |
|           0.8815 | learning_rate=0.5, n_estimators=100, max_depth=5, max_features="log2"  |
|           0.8814 | learning_rate=0.5, n_estimators=500, max_depth=3, max_features="log2"  |
|           0.8813 | learning_rate=0.5, n_estimators=100, max_depth=7, max_features="log2"  |
|           0.8801 | learning_rate=0.01, n_estimators=500, max_depth=1, max_features="log2" |
|           0.8793 | learning_rate=1, n_estimators=100, max_depth=3, max_features="log2"    |
|           0.879  | learning_rate=0.5, n_estimators=700, max_depth=3, max_features="log2"  |
|           0.8787 | learning_rate=0.5, n_estimators=300, max_depth=5, max_features="log2"  |
|           0.8783 | learning_rate=0.01, n_estimators=300, max_depth=1, max_features="log2" |
|           0.8763 | learning_rate=0.01, n_estimators=100, max_depth=1, max_features="log2" |
|           0.8758 | learning_rate=1, n_estimators=300, max_depth=3, max_features="log2"    |
|           0.8753 | learning_rate=0.5, n_estimators=700, max_depth=5, max_features="log2"  |
|           0.8722 | learning_rate=1, n_estimators=100, max_depth=5, max_features="log2"    |
|           0.8705 | learning_rate=1, n_estimators=100, max_depth=7, max_features="log2"    |
|           0.87   | learning_rate=1, n_estimators=500, max_depth=3, max_features="log2"    |
|           0.8642 | learning_rate=1, n_estimators=300, max_depth=5, max_features="log2"    |
|           0.8635 | learning_rate=1, n_estimators=700, max_depth=3, max_features="log2"    |
|           0.8255 | learning_rate=1, n_estimators=500, max_depth=5, max_features="log2"    |
|           0.8168 | learning_rate=1, n_estimators=300, max_depth=7, max_features="log2"    |
|           0.8138 | learning_rate=1, n_estimators=500, max_depth=7, max_features="log2"    |
|           0.8065 | learning_rate=1, n_estimators=700, max_depth=5, max_features="log2"    |
|           0.7741 | learning_rate=1, n_estimators=700, max_depth=7, max_features="log2"    |

## GaussianNB
|   accuracy.macro | params   |
|-----------------:|:---------|
|           0.8594 |          |

