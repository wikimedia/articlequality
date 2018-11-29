# Model tuning report
- Revscoring version: 2.2.6
- Features: articlequality.feature_lists.glwiki.wp10
- Date: 2018-11-28T21:25:54.847496
- Observations: 401
- Labels: ["Stub", "Start", "C", "B", "GA", "FA"]
- Statistic: accuracy.macro (maximize)
- Folds: 5

# Top scoring configurations
| model                  |   accuracy.macro | params                                                                        |
|:-----------------------|-----------------:|:------------------------------------------------------------------------------|
| GradientBoosting       |           0.847  | learning_rate=0.01, n_estimators=500, max_depth=3, max_features="log2"        |
| GradientBoosting       |           0.8454 | learning_rate=0.01, n_estimators=100, max_depth=3, max_features="log2"        |
| GradientBoosting       |           0.8454 | learning_rate=0.1, n_estimators=100, max_depth=1, max_features="log2"         |
| GradientBoosting       |           0.8454 | learning_rate=0.5, n_estimators=100, max_depth=5, max_features="log2"         |
| GradientBoosting       |           0.8446 | learning_rate=0.01, n_estimators=700, max_depth=3, max_features="log2"        |
| GradientBoosting       |           0.8446 | learning_rate=0.1, n_estimators=500, max_depth=3, max_features="log2"         |
| GradientBoosting       |           0.8437 | learning_rate=0.01, n_estimators=300, max_depth=5, max_features="log2"        |
| GradientBoosting       |           0.8437 | learning_rate=0.01, n_estimators=300, max_depth=7, max_features="log2"        |
| GradientBoosting       |           0.8437 | learning_rate=0.1, n_estimators=300, max_depth=5, max_features="log2"         |
| RandomForestClassifier |           0.8437 | n_estimators=80, criterion="entropy", max_features="log2", min_samples_leaf=1 |

# Models
## GaussianNB
|   accuracy.macro | params   |
|-----------------:|:---------|
|           0.8063 |          |

## BernoulliNB
|   accuracy.macro | params   |
|-----------------:|:---------|
|           0.7614 |          |

## GradientBoosting
|   accuracy.macro | params                                                                 |
|-----------------:|:-----------------------------------------------------------------------|
|           0.847  | learning_rate=0.01, n_estimators=500, max_depth=3, max_features="log2" |
|           0.8454 | learning_rate=0.01, n_estimators=100, max_depth=3, max_features="log2" |
|           0.8454 | learning_rate=0.1, n_estimators=100, max_depth=1, max_features="log2"  |
|           0.8454 | learning_rate=0.5, n_estimators=100, max_depth=5, max_features="log2"  |
|           0.8446 | learning_rate=0.01, n_estimators=700, max_depth=3, max_features="log2" |
|           0.8446 | learning_rate=0.1, n_estimators=500, max_depth=3, max_features="log2"  |
|           0.8437 | learning_rate=0.01, n_estimators=300, max_depth=5, max_features="log2" |
|           0.8437 | learning_rate=0.01, n_estimators=300, max_depth=7, max_features="log2" |
|           0.8437 | learning_rate=0.1, n_estimators=300, max_depth=5, max_features="log2"  |
|           0.8429 | learning_rate=0.01, n_estimators=300, max_depth=1, max_features="log2" |
|           0.8429 | learning_rate=0.01, n_estimators=700, max_depth=5, max_features="log2" |
|           0.8429 | learning_rate=0.01, n_estimators=100, max_depth=7, max_features="log2" |
|           0.8421 | learning_rate=0.01, n_estimators=300, max_depth=3, max_features="log2" |
|           0.8421 | learning_rate=0.01, n_estimators=100, max_depth=5, max_features="log2" |
|           0.8412 | learning_rate=0.01, n_estimators=500, max_depth=7, max_features="log2" |
|           0.8404 | learning_rate=0.1, n_estimators=700, max_depth=3, max_features="log2"  |
|           0.8404 | learning_rate=0.1, n_estimators=300, max_depth=3, max_features="log2"  |
|           0.8396 | learning_rate=0.01, n_estimators=500, max_depth=1, max_features="log2" |
|           0.8396 | learning_rate=0.01, n_estimators=500, max_depth=5, max_features="log2" |
|           0.8396 | learning_rate=0.01, n_estimators=700, max_depth=7, max_features="log2" |
|           0.8396 | learning_rate=0.1, n_estimators=500, max_depth=5, max_features="log2"  |
|           0.8396 | learning_rate=0.1, n_estimators=700, max_depth=5, max_features="log2"  |
|           0.8396 | learning_rate=0.1, n_estimators=500, max_depth=7, max_features="log2"  |
|           0.8387 | learning_rate=0.5, n_estimators=100, max_depth=3, max_features="log2"  |
|           0.8379 | learning_rate=0.5, n_estimators=300, max_depth=3, max_features="log2"  |
|           0.8371 | learning_rate=0.01, n_estimators=700, max_depth=1, max_features="log2" |
|           0.8371 | learning_rate=0.1, n_estimators=700, max_depth=7, max_features="log2"  |
|           0.8371 | learning_rate=0.5, n_estimators=700, max_depth=5, max_features="log2"  |
|           0.8371 | learning_rate=0.5, n_estimators=700, max_depth=7, max_features="log2"  |
|           0.8362 | learning_rate=0.1, n_estimators=100, max_depth=3, max_features="log2"  |
|           0.8354 | learning_rate=0.5, n_estimators=500, max_depth=5, max_features="log2"  |
|           0.8346 | learning_rate=0.1, n_estimators=100, max_depth=5, max_features="log2"  |
|           0.8346 | learning_rate=0.1, n_estimators=300, max_depth=7, max_features="log2"  |
|           0.8346 | learning_rate=0.5, n_estimators=500, max_depth=7, max_features="log2"  |
|           0.8337 | learning_rate=0.01, n_estimators=100, max_depth=1, max_features="log2" |
|           0.8337 | learning_rate=0.1, n_estimators=100, max_depth=7, max_features="log2"  |
|           0.8337 | learning_rate=1, n_estimators=700, max_depth=7, max_features="log2"    |
|           0.8329 | learning_rate=0.5, n_estimators=500, max_depth=3, max_features="log2"  |
|           0.8329 | learning_rate=0.5, n_estimators=700, max_depth=3, max_features="log2"  |
|           0.8321 | learning_rate=0.1, n_estimators=300, max_depth=1, max_features="log2"  |
|           0.8304 | learning_rate=1, n_estimators=100, max_depth=5, max_features="log2"    |
|           0.8304 | learning_rate=0.5, n_estimators=300, max_depth=5, max_features="log2"  |
|           0.8296 | learning_rate=1, n_estimators=100, max_depth=1, max_features="log2"    |
|           0.8296 | learning_rate=1, n_estimators=500, max_depth=3, max_features="log2"    |
|           0.8288 | learning_rate=0.5, n_estimators=300, max_depth=7, max_features="log2"  |
|           0.8288 | learning_rate=1, n_estimators=300, max_depth=5, max_features="log2"    |
|           0.8279 | learning_rate=0.1, n_estimators=500, max_depth=1, max_features="log2"  |
|           0.8279 | learning_rate=0.5, n_estimators=300, max_depth=1, max_features="log2"  |
|           0.8279 | learning_rate=1, n_estimators=100, max_depth=7, max_features="log2"    |
|           0.8263 | learning_rate=0.5, n_estimators=100, max_depth=1, max_features="log2"  |
|           0.8263 | learning_rate=1, n_estimators=500, max_depth=7, max_features="log2"    |
|           0.8254 | learning_rate=0.1, n_estimators=700, max_depth=1, max_features="log2"  |
|           0.8254 | learning_rate=1, n_estimators=300, max_depth=1, max_features="log2"    |
|           0.8254 | learning_rate=1, n_estimators=700, max_depth=3, max_features="log2"    |
|           0.8254 | learning_rate=1, n_estimators=500, max_depth=5, max_features="log2"    |
|           0.8229 | learning_rate=1, n_estimators=700, max_depth=5, max_features="log2"    |
|           0.8221 | learning_rate=0.5, n_estimators=100, max_depth=7, max_features="log2"  |
|           0.8213 | learning_rate=1, n_estimators=300, max_depth=3, max_features="log2"    |
|           0.818  | learning_rate=0.5, n_estimators=500, max_depth=1, max_features="log2"  |
|           0.818  | learning_rate=0.5, n_estimators=700, max_depth=1, max_features="log2"  |
|           0.818  | learning_rate=1, n_estimators=100, max_depth=3, max_features="log2"    |
|           0.8121 | learning_rate=1, n_estimators=700, max_depth=1, max_features="log2"    |
|           0.8113 | learning_rate=1, n_estimators=300, max_depth=7, max_features="log2"    |
|           0.8038 | learning_rate=1, n_estimators=500, max_depth=1, max_features="log2"    |

## LogisticRegression
|   accuracy.macro | params              |
|-----------------:|:--------------------|
|           0.8362 | penalty="l1", C=1   |
|           0.8337 | penalty="l1", C=10  |
|           0.8321 | penalty="l1", C=0.1 |
|           0.8321 | penalty="l2", C=0.1 |
|           0.8313 | penalty="l2", C=10  |
|           0.8263 | penalty="l2", C=1   |

## RandomForestClassifier
|   accuracy.macro | params                                                                          |
|-----------------:|:--------------------------------------------------------------------------------|
|           0.8437 | n_estimators=80, criterion="entropy", max_features="log2", min_samples_leaf=1   |
|           0.8429 | n_estimators=20, criterion="entropy", max_features="log2", min_samples_leaf=7   |
|           0.8429 | n_estimators=160, criterion="gini", max_features="log2", min_samples_leaf=3     |
|           0.8429 | n_estimators=640, criterion="gini", max_features="log2", min_samples_leaf=3     |
|           0.8429 | n_estimators=40, criterion="entropy", max_features="log2", min_samples_leaf=3   |
|           0.8429 | n_estimators=640, criterion="entropy", max_features="log2", min_samples_leaf=3  |
|           0.8421 | n_estimators=320, criterion="entropy", max_features="log2", min_samples_leaf=3  |
|           0.8421 | n_estimators=160, criterion="entropy", max_features="log2", min_samples_leaf=13 |
|           0.8421 | n_estimators=40, criterion="gini", max_features="log2", min_samples_leaf=1      |
|           0.8412 | n_estimators=20, criterion="gini", max_features="log2", min_samples_leaf=7      |
|           0.8404 | n_estimators=20, criterion="gini", max_features="log2", min_samples_leaf=3      |
|           0.8404 | n_estimators=40, criterion="gini", max_features="log2", min_samples_leaf=3      |
|           0.8404 | n_estimators=320, criterion="gini", max_features="log2", min_samples_leaf=3     |
|           0.8396 | n_estimators=80, criterion="gini", max_features="log2", min_samples_leaf=1      |
|           0.8396 | n_estimators=320, criterion="gini", max_features="log2", min_samples_leaf=1     |
|           0.8396 | n_estimators=20, criterion="entropy", max_features="log2", min_samples_leaf=5   |
|           0.8387 | n_estimators=320, criterion="entropy", max_features="log2", min_samples_leaf=1  |
|           0.8387 | n_estimators=80, criterion="entropy", max_features="log2", min_samples_leaf=7   |
|           0.8379 | n_estimators=640, criterion="entropy", max_features="log2", min_samples_leaf=1  |
|           0.8379 | n_estimators=160, criterion="entropy", max_features="log2", min_samples_leaf=3  |
|           0.8379 | n_estimators=80, criterion="entropy", max_features="log2", min_samples_leaf=5   |
|           0.8379 | n_estimators=320, criterion="gini", max_features="log2", min_samples_leaf=5     |
|           0.8379 | n_estimators=320, criterion="gini", max_features="log2", min_samples_leaf=7     |
|           0.8379 | n_estimators=160, criterion="entropy", max_features="log2", min_samples_leaf=5  |
|           0.8379 | n_estimators=80, criterion="entropy", max_features="log2", min_samples_leaf=13  |
|           0.8371 | n_estimators=80, criterion="entropy", max_features="log2", min_samples_leaf=3   |
|           0.8371 | n_estimators=80, criterion="gini", max_features="log2", min_samples_leaf=7      |
|           0.8371 | n_estimators=320, criterion="entropy", max_features="log2", min_samples_leaf=5  |
|           0.8371 | n_estimators=160, criterion="entropy", max_features="log2", min_samples_leaf=7  |
|           0.8362 | n_estimators=80, criterion="gini", max_features="log2", min_samples_leaf=3      |
|           0.8362 | n_estimators=80, criterion="gini", max_features="log2", min_samples_leaf=5      |
|           0.8362 | n_estimators=640, criterion="gini", max_features="log2", min_samples_leaf=5     |
|           0.8362 | n_estimators=40, criterion="gini", max_features="log2", min_samples_leaf=7      |
|           0.8362 | n_estimators=160, criterion="gini", max_features="log2", min_samples_leaf=7     |
|           0.8362 | n_estimators=640, criterion="gini", max_features="log2", min_samples_leaf=7     |
|           0.8362 | n_estimators=640, criterion="entropy", max_features="log2", min_samples_leaf=5  |
|           0.8354 | n_estimators=10, criterion="entropy", max_features="log2", min_samples_leaf=7   |
|           0.8354 | n_estimators=160, criterion="entropy", max_features="log2", min_samples_leaf=1  |
|           0.8354 | n_estimators=10, criterion="entropy", max_features="log2", min_samples_leaf=3   |
|           0.8346 | n_estimators=160, criterion="gini", max_features="log2", min_samples_leaf=1     |
|           0.8346 | n_estimators=640, criterion="gini", max_features="log2", min_samples_leaf=1     |
|           0.8346 | n_estimators=10, criterion="gini", max_features="log2", min_samples_leaf=5      |
|           0.8346 | n_estimators=320, criterion="gini", max_features="log2", min_samples_leaf=13    |
|           0.8346 | n_estimators=20, criterion="entropy", max_features="log2", min_samples_leaf=3   |
|           0.8346 | n_estimators=640, criterion="entropy", max_features="log2", min_samples_leaf=13 |
|           0.8337 | n_estimators=160, criterion="gini", max_features="log2", min_samples_leaf=13    |
|           0.8337 | n_estimators=40, criterion="entropy", max_features="log2", min_samples_leaf=5   |
|           0.8337 | n_estimators=320, criterion="entropy", max_features="log2", min_samples_leaf=13 |
|           0.8337 | n_estimators=40, criterion="entropy", max_features="log2", min_samples_leaf=1   |
|           0.8329 | n_estimators=640, criterion="gini", max_features="log2", min_samples_leaf=13    |
|           0.8329 | n_estimators=20, criterion="entropy", max_features="log2", min_samples_leaf=1   |
|           0.8329 | n_estimators=320, criterion="entropy", max_features="log2", min_samples_leaf=7  |
|           0.8329 | n_estimators=640, criterion="entropy", max_features="log2", min_samples_leaf=7  |
|           0.8321 | n_estimators=20, criterion="gini", max_features="log2", min_samples_leaf=5      |
|           0.8321 | n_estimators=40, criterion="gini", max_features="log2", min_samples_leaf=5      |
|           0.8321 | n_estimators=160, criterion="gini", max_features="log2", min_samples_leaf=5     |
|           0.8321 | n_estimators=80, criterion="gini", max_features="log2", min_samples_leaf=13     |
|           0.8321 | n_estimators=10, criterion="entropy", max_features="log2", min_samples_leaf=5   |
|           0.8321 | n_estimators=40, criterion="entropy", max_features="log2", min_samples_leaf=7   |
|           0.8313 | n_estimators=10, criterion="gini", max_features="log2", min_samples_leaf=7      |
|           0.8313 | n_estimators=20, criterion="entropy", max_features="log2", min_samples_leaf=13  |
|           0.8304 | n_estimators=40, criterion="gini", max_features="log2", min_samples_leaf=13     |
|           0.8304 | n_estimators=40, criterion="entropy", max_features="log2", min_samples_leaf=13  |
|           0.8296 | n_estimators=20, criterion="gini", max_features="log2", min_samples_leaf=1      |
|           0.8288 | n_estimators=10, criterion="entropy", max_features="log2", min_samples_leaf=1   |
|           0.8288 | n_estimators=10, criterion="entropy", max_features="log2", min_samples_leaf=13  |
|           0.8271 | n_estimators=10, criterion="gini", max_features="log2", min_samples_leaf=13     |
|           0.8271 | n_estimators=20, criterion="gini", max_features="log2", min_samples_leaf=13     |
|           0.8188 | n_estimators=10, criterion="gini", max_features="log2", min_samples_leaf=1      |
|           0.818  | n_estimators=10, criterion="gini", max_features="log2", min_samples_leaf=3      |

