# Model tuning report
- Revscoring version: 2.1.0
- Features: articlequality.feature_lists.enwiki.wp10
- Date: 2018-01-15T13:05:07.855569
- Observations: 32449
- Labels: ["Stub", "Start", "C", "B", "GA", "FA"]
- Statistic: accuracy.macro (maximize)
- Folds: 5

# Top scoring configurations
| model                  |   accuracy.macro | params                                                                         |
|:-----------------------|-----------------:|:-------------------------------------------------------------------------------|
| GradientBoosting       |           0.8923 | n_estimators=700, max_features="log2", learning_rate=0.01, max_depth=7         |
| RandomForestClassifier |           0.8921 | n_estimators=640, max_features="log2", min_samples_leaf=3, criterion="entropy" |
| GradientBoosting       |           0.892  | n_estimators=500, max_features="log2", learning_rate=0.01, max_depth=7         |
| RandomForestClassifier |           0.8919 | n_estimators=160, max_features="log2", min_samples_leaf=3, criterion="entropy" |
| RandomForestClassifier |           0.8919 | n_estimators=640, max_features="log2", min_samples_leaf=1, criterion="gini"    |
| RandomForestClassifier |           0.8918 | n_estimators=320, max_features="log2", min_samples_leaf=3, criterion="entropy" |
| RandomForestClassifier |           0.8917 | n_estimators=640, max_features="log2", min_samples_leaf=3, criterion="gini"    |
| RandomForestClassifier |           0.8916 | n_estimators=640, max_features="log2", min_samples_leaf=1, criterion="entropy" |
| RandomForestClassifier |           0.8915 | n_estimators=320, max_features="log2", min_samples_leaf=1, criterion="gini"    |
| RandomForestClassifier |           0.8914 | n_estimators=320, max_features="log2", min_samples_leaf=5, criterion="entropy" |

# Models
## GaussianNB
|   accuracy.macro | params   |
|-----------------:|:---------|
|           0.8565 |          |

## LogisticRegression
|   accuracy.macro | params              |
|-----------------:|:--------------------|
|           0.8847 | C=10, penalty="l1"  |
|           0.8835 | C=1, penalty="l1"   |
|           0.8823 | C=0.1, penalty="l1" |
|           0.8683 | C=1, penalty="l2"   |
|           0.8678 | C=10, penalty="l2"  |
|           0.8657 | C=0.1, penalty="l2" |

## RandomForestClassifier
|   accuracy.macro | params                                                                          |
|-----------------:|:--------------------------------------------------------------------------------|
|           0.8921 | n_estimators=640, max_features="log2", min_samples_leaf=3, criterion="entropy"  |
|           0.8919 | n_estimators=160, max_features="log2", min_samples_leaf=3, criterion="entropy"  |
|           0.8919 | n_estimators=640, max_features="log2", min_samples_leaf=1, criterion="gini"     |
|           0.8918 | n_estimators=320, max_features="log2", min_samples_leaf=3, criterion="entropy"  |
|           0.8917 | n_estimators=640, max_features="log2", min_samples_leaf=3, criterion="gini"     |
|           0.8916 | n_estimators=640, max_features="log2", min_samples_leaf=1, criterion="entropy"  |
|           0.8915 | n_estimators=320, max_features="log2", min_samples_leaf=1, criterion="gini"     |
|           0.8914 | n_estimators=320, max_features="log2", min_samples_leaf=5, criterion="entropy"  |
|           0.8914 | n_estimators=320, max_features="log2", min_samples_leaf=1, criterion="entropy"  |
|           0.8913 | n_estimators=160, max_features="log2", min_samples_leaf=1, criterion="entropy"  |
|           0.8913 | n_estimators=640, max_features="log2", min_samples_leaf=5, criterion="entropy"  |
|           0.8912 | n_estimators=640, max_features="log2", min_samples_leaf=7, criterion="entropy"  |
|           0.8912 | n_estimators=160, max_features="log2", min_samples_leaf=3, criterion="gini"     |
|           0.8911 | n_estimators=160, max_features="log2", min_samples_leaf=5, criterion="entropy"  |
|           0.8911 | n_estimators=320, max_features="log2", min_samples_leaf=7, criterion="gini"     |
|           0.891  | n_estimators=80, max_features="log2", min_samples_leaf=5, criterion="entropy"   |
|           0.891  | n_estimators=160, max_features="log2", min_samples_leaf=1, criterion="gini"     |
|           0.891  | n_estimators=320, max_features="log2", min_samples_leaf=7, criterion="entropy"  |
|           0.891  | n_estimators=320, max_features="log2", min_samples_leaf=3, criterion="gini"     |
|           0.891  | n_estimators=640, max_features="log2", min_samples_leaf=5, criterion="gini"     |
|           0.891  | n_estimators=160, max_features="log2", min_samples_leaf=7, criterion="gini"     |
|           0.8909 | n_estimators=80, max_features="log2", min_samples_leaf=3, criterion="gini"      |
|           0.8908 | n_estimators=80, max_features="log2", min_samples_leaf=3, criterion="entropy"   |
|           0.8908 | n_estimators=640, max_features="log2", min_samples_leaf=7, criterion="gini"     |
|           0.8908 | n_estimators=80, max_features="log2", min_samples_leaf=7, criterion="gini"      |
|           0.8907 | n_estimators=160, max_features="log2", min_samples_leaf=5, criterion="gini"     |
|           0.8907 | n_estimators=160, max_features="log2", min_samples_leaf=7, criterion="entropy"  |
|           0.8906 | n_estimators=320, max_features="log2", min_samples_leaf=5, criterion="gini"     |
|           0.8905 | n_estimators=80, max_features="log2", min_samples_leaf=1, criterion="gini"      |
|           0.8905 | n_estimators=80, max_features="log2", min_samples_leaf=5, criterion="gini"      |
|           0.8903 | n_estimators=80, max_features="log2", min_samples_leaf=7, criterion="entropy"   |
|           0.8902 | n_estimators=640, max_features="log2", min_samples_leaf=13, criterion="entropy" |
|           0.8901 | n_estimators=40, max_features="log2", min_samples_leaf=3, criterion="entropy"   |
|           0.8901 | n_estimators=40, max_features="log2", min_samples_leaf=5, criterion="entropy"   |
|           0.89   | n_estimators=640, max_features="log2", min_samples_leaf=13, criterion="gini"    |
|           0.8899 | n_estimators=320, max_features="log2", min_samples_leaf=13, criterion="entropy" |
|           0.8899 | n_estimators=40, max_features="log2", min_samples_leaf=5, criterion="gini"      |
|           0.8898 | n_estimators=80, max_features="log2", min_samples_leaf=13, criterion="gini"     |
|           0.8898 | n_estimators=40, max_features="log2", min_samples_leaf=3, criterion="gini"      |
|           0.8897 | n_estimators=40, max_features="log2", min_samples_leaf=7, criterion="entropy"   |
|           0.8897 | n_estimators=40, max_features="log2", min_samples_leaf=7, criterion="gini"      |
|           0.8897 | n_estimators=160, max_features="log2", min_samples_leaf=13, criterion="entropy" |
|           0.8897 | n_estimators=320, max_features="log2", min_samples_leaf=13, criterion="gini"    |
|           0.8896 | n_estimators=80, max_features="log2", min_samples_leaf=1, criterion="entropy"   |
|           0.8895 | n_estimators=80, max_features="log2", min_samples_leaf=13, criterion="entropy"  |
|           0.8894 | n_estimators=40, max_features="log2", min_samples_leaf=13, criterion="gini"     |
|           0.8893 | n_estimators=40, max_features="log2", min_samples_leaf=13, criterion="entropy"  |
|           0.889  | n_estimators=160, max_features="log2", min_samples_leaf=13, criterion="gini"    |
|           0.889  | n_estimators=20, max_features="log2", min_samples_leaf=7, criterion="gini"      |
|           0.8887 | n_estimators=20, max_features="log2", min_samples_leaf=7, criterion="entropy"   |
|           0.8885 | n_estimators=20, max_features="log2", min_samples_leaf=5, criterion="entropy"   |
|           0.8885 | n_estimators=40, max_features="log2", min_samples_leaf=1, criterion="gini"      |
|           0.8884 | n_estimators=20, max_features="log2", min_samples_leaf=13, criterion="entropy"  |
|           0.8883 | n_estimators=20, max_features="log2", min_samples_leaf=3, criterion="gini"      |
|           0.8882 | n_estimators=40, max_features="log2", min_samples_leaf=1, criterion="entropy"   |
|           0.8878 | n_estimators=20, max_features="log2", min_samples_leaf=5, criterion="gini"      |
|           0.8875 | n_estimators=20, max_features="log2", min_samples_leaf=13, criterion="gini"     |
|           0.8874 | n_estimators=20, max_features="log2", min_samples_leaf=3, criterion="entropy"   |
|           0.8865 | n_estimators=10, max_features="log2", min_samples_leaf=5, criterion="gini"      |
|           0.8862 | n_estimators=10, max_features="log2", min_samples_leaf=13, criterion="entropy"  |
|           0.8858 | n_estimators=10, max_features="log2", min_samples_leaf=7, criterion="entropy"   |
|           0.8856 | n_estimators=10, max_features="log2", min_samples_leaf=7, criterion="gini"      |
|           0.8856 | n_estimators=10, max_features="log2", min_samples_leaf=13, criterion="gini"     |
|           0.885  | n_estimators=10, max_features="log2", min_samples_leaf=5, criterion="entropy"   |
|           0.8844 | n_estimators=10, max_features="log2", min_samples_leaf=3, criterion="entropy"   |
|           0.8843 | n_estimators=20, max_features="log2", min_samples_leaf=1, criterion="gini"      |
|           0.8841 | n_estimators=10, max_features="log2", min_samples_leaf=3, criterion="gini"      |
|           0.8838 | n_estimators=20, max_features="log2", min_samples_leaf=1, criterion="entropy"   |
|           0.878  | n_estimators=10, max_features="log2", min_samples_leaf=1, criterion="entropy"   |
|           0.8776 | n_estimators=10, max_features="log2", min_samples_leaf=1, criterion="gini"      |

## BernoulliNB
|   accuracy.macro | params   |
|-----------------:|:---------|
|           0.8044 |          |

## GradientBoosting
|   accuracy.macro | params                                                                 |
|-----------------:|:-----------------------------------------------------------------------|
|           0.8923 | n_estimators=700, max_features="log2", learning_rate=0.01, max_depth=7 |
|           0.892  | n_estimators=500, max_features="log2", learning_rate=0.01, max_depth=7 |
|           0.891  | n_estimators=300, max_features="log2", learning_rate=0.01, max_depth=7 |
|           0.8909 | n_estimators=700, max_features="log2", learning_rate=0.01, max_depth=5 |
|           0.8906 | n_estimators=100, max_features="log2", learning_rate=0.1, max_depth=7  |
|           0.8906 | n_estimators=300, max_features="log2", learning_rate=0.1, max_depth=3  |
|           0.8904 | n_estimators=100, max_features="log2", learning_rate=0.1, max_depth=5  |
|           0.8902 | n_estimators=500, max_features="log2", learning_rate=0.01, max_depth=5 |
|           0.8902 | n_estimators=500, max_features="log2", learning_rate=0.1, max_depth=3  |
|           0.89   | n_estimators=700, max_features="log2", learning_rate=0.1, max_depth=3  |
|           0.8899 | n_estimators=300, max_features="log2", learning_rate=0.01, max_depth=5 |
|           0.8893 | n_estimators=500, max_features="log2", learning_rate=0.1, max_depth=5  |
|           0.8892 | n_estimators=100, max_features="log2", learning_rate=0.1, max_depth=3  |
|           0.8892 | n_estimators=300, max_features="log2", learning_rate=0.1, max_depth=7  |
|           0.8891 | n_estimators=100, max_features="log2", learning_rate=0.01, max_depth=7 |
|           0.8891 | n_estimators=300, max_features="log2", learning_rate=0.1, max_depth=5  |
|           0.8889 | n_estimators=500, max_features="log2", learning_rate=0.1, max_depth=7  |
|           0.8886 | n_estimators=700, max_features="log2", learning_rate=0.01, max_depth=3 |
|           0.8886 | n_estimators=700, max_features="log2", learning_rate=0.1, max_depth=5  |
|           0.8885 | n_estimators=700, max_features="log2", learning_rate=0.1, max_depth=7  |
|           0.8878 | n_estimators=500, max_features="log2", learning_rate=0.01, max_depth=3 |
|           0.887  | n_estimators=500, max_features="log2", learning_rate=0.5, max_depth=1  |
|           0.8869 | n_estimators=100, max_features="log2", learning_rate=0.01, max_depth=5 |
|           0.8865 | n_estimators=100, max_features="log2", learning_rate=0.5, max_depth=3  |
|           0.8864 | n_estimators=700, max_features="log2", learning_rate=0.1, max_depth=1  |
|           0.8862 | n_estimators=700, max_features="log2", learning_rate=0.5, max_depth=1  |
|           0.8862 | n_estimators=500, max_features="log2", learning_rate=0.1, max_depth=1  |
|           0.8859 | n_estimators=300, max_features="log2", learning_rate=0.5, max_depth=1  |
|           0.8856 | n_estimators=300, max_features="log2", learning_rate=0.01, max_depth=3 |
|           0.8853 | n_estimators=300, max_features="log2", learning_rate=0.1, max_depth=1  |
|           0.8852 | n_estimators=300, max_features="log2", learning_rate=1, max_depth=1    |
|           0.885  | n_estimators=500, max_features="log2", learning_rate=1, max_depth=1    |
|           0.8848 | n_estimators=100, max_features="log2", learning_rate=0.5, max_depth=1  |
|           0.8844 | n_estimators=700, max_features="log2", learning_rate=1, max_depth=1    |
|           0.8839 | n_estimators=100, max_features="log2", learning_rate=1, max_depth=1    |
|           0.8837 | n_estimators=500, max_features="log2", learning_rate=0.5, max_depth=7  |
|           0.8837 | n_estimators=300, max_features="log2", learning_rate=0.5, max_depth=3  |
|           0.8829 | n_estimators=100, max_features="log2", learning_rate=0.01, max_depth=3 |
|           0.8829 | n_estimators=700, max_features="log2", learning_rate=0.5, max_depth=7  |
|           0.8819 | n_estimators=500, max_features="log2", learning_rate=0.5, max_depth=5  |
|           0.8816 | n_estimators=100, max_features="log2", learning_rate=0.1, max_depth=1  |
|           0.8816 | n_estimators=500, max_features="log2", learning_rate=0.5, max_depth=3  |
|           0.8814 | n_estimators=700, max_features="log2", learning_rate=0.01, max_depth=1 |
|           0.8813 | n_estimators=100, max_features="log2", learning_rate=0.5, max_depth=7  |
|           0.8812 | n_estimators=100, max_features="log2", learning_rate=0.5, max_depth=5  |
|           0.8809 | n_estimators=700, max_features="log2", learning_rate=0.5, max_depth=5  |
|           0.8804 | n_estimators=700, max_features="log2", learning_rate=0.5, max_depth=3  |
|           0.88   | n_estimators=500, max_features="log2", learning_rate=0.01, max_depth=1 |
|           0.8798 | n_estimators=100, max_features="log2", learning_rate=1, max_depth=3    |
|           0.8786 | n_estimators=300, max_features="log2", learning_rate=0.5, max_depth=5  |
|           0.8785 | n_estimators=300, max_features="log2", learning_rate=0.5, max_depth=7  |
|           0.8778 | n_estimators=300, max_features="log2", learning_rate=0.01, max_depth=1 |
|           0.8759 | n_estimators=100, max_features="log2", learning_rate=0.01, max_depth=1 |
|           0.8746 | n_estimators=300, max_features="log2", learning_rate=1, max_depth=3    |
|           0.8734 | n_estimators=500, max_features="log2", learning_rate=1, max_depth=3    |
|           0.8714 | n_estimators=100, max_features="log2", learning_rate=1, max_depth=5    |
|           0.87   | n_estimators=100, max_features="log2", learning_rate=1, max_depth=7    |
|           0.8387 | n_estimators=700, max_features="log2", learning_rate=1, max_depth=3    |
|           0.8285 | n_estimators=300, max_features="log2", learning_rate=1, max_depth=5    |
|           0.7897 | n_estimators=500, max_features="log2", learning_rate=1, max_depth=5    |
|           0.7838 | n_estimators=300, max_features="log2", learning_rate=1, max_depth=7    |
|           0.7798 | n_estimators=700, max_features="log2", learning_rate=1, max_depth=7    |
|           0.7571 | n_estimators=700, max_features="log2", learning_rate=1, max_depth=5    |
|           0.7543 | n_estimators=500, max_features="log2", learning_rate=1, max_depth=7    |

