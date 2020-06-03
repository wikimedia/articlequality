# Model tuning report
- Revscoring version: 2.7.2
- Features: articlequality.feature_lists.ptwiki.wp10
- Date: 2020-05-22T21:41:21.553864
- Observations: 3884
- Labels: ["1", "2", "3", "4", "5", "6"]
- Statistic: accuracy.macro (maximize)
- Folds: 5

# Top scoring configurations
| model                  |   accuracy.macro | params                                                                         |
|:-----------------------|-----------------:|:-------------------------------------------------------------------------------|
| GradientBoosting       |           0.8544 | max_features="log2", n_estimators=100, learning_rate=0.01, max_depth=7         |
| RandomForestClassifier |           0.8539 | max_features="log2", n_estimators=160, min_samples_leaf=3, criterion="entropy" |
| GradientBoosting       |           0.8528 | max_features="log2", n_estimators=300, learning_rate=0.01, max_depth=5         |
| RandomForestClassifier |           0.8523 | max_features="log2", n_estimators=40, min_samples_leaf=7, criterion="entropy"  |
| GradientBoosting       |           0.8523 | max_features="log2", n_estimators=100, learning_rate=0.01, max_depth=5         |
| RandomForestClassifier |           0.8523 | max_features="log2", n_estimators=80, min_samples_leaf=3, criterion="entropy"  |
| RandomForestClassifier |           0.8521 | max_features="log2", n_estimators=320, min_samples_leaf=5, criterion="gini"    |
| RandomForestClassifier |           0.852  | max_features="log2", n_estimators=640, min_samples_leaf=7, criterion="entropy" |
| RandomForestClassifier |           0.8519 | max_features="log2", n_estimators=320, min_samples_leaf=5, criterion="entropy" |
| RandomForestClassifier |           0.8516 | max_features="log2", n_estimators=640, min_samples_leaf=5, criterion="gini"    |

# Models
## GradientBoosting
|   accuracy.macro | params                                                                 |
|-----------------:|:-----------------------------------------------------------------------|
|           0.8544 | max_features="log2", n_estimators=100, learning_rate=0.01, max_depth=7 |
|           0.8528 | max_features="log2", n_estimators=300, learning_rate=0.01, max_depth=5 |
|           0.8523 | max_features="log2", n_estimators=100, learning_rate=0.01, max_depth=5 |
|           0.8512 | max_features="log2", n_estimators=500, learning_rate=0.01, max_depth=5 |
|           0.8506 | max_features="log2", n_estimators=300, learning_rate=0.01, max_depth=7 |
|           0.8502 | max_features="log2", n_estimators=700, learning_rate=0.01, max_depth=5 |
|           0.8499 | max_features="log2", n_estimators=500, learning_rate=0.01, max_depth=7 |
|           0.8499 | max_features="log2", n_estimators=300, learning_rate=0.01, max_depth=3 |
|           0.8497 | max_features="log2", n_estimators=500, learning_rate=0.01, max_depth=3 |
|           0.8495 | max_features="log2", n_estimators=700, learning_rate=0.01, max_depth=3 |
|           0.8477 | max_features="log2", n_estimators=700, learning_rate=0.01, max_depth=7 |
|           0.8474 | max_features="log2", n_estimators=100, learning_rate=0.01, max_depth=3 |
|           0.8467 | max_features="log2", n_estimators=100, learning_rate=0.1, max_depth=3  |
|           0.8439 | max_features="log2", n_estimators=300, learning_rate=0.1, max_depth=7  |
|           0.8434 | max_features="log2", n_estimators=700, learning_rate=0.1, max_depth=7  |
|           0.8428 | max_features="log2", n_estimators=500, learning_rate=0.1, max_depth=3  |
|           0.8426 | max_features="log2", n_estimators=100, learning_rate=0.1, max_depth=7  |
|           0.8426 | max_features="log2", n_estimators=500, learning_rate=0.1, max_depth=7  |
|           0.8423 | max_features="log2", n_estimators=100, learning_rate=0.1, max_depth=5  |
|           0.8419 | max_features="log2", n_estimators=100, learning_rate=0.1, max_depth=1  |
|           0.8414 | max_features="log2", n_estimators=300, learning_rate=0.5, max_depth=7  |
|           0.8411 | max_features="log2", n_estimators=700, learning_rate=0.5, max_depth=7  |
|           0.8409 | max_features="log2", n_estimators=700, learning_rate=0.01, max_depth=1 |
|           0.8404 | max_features="log2", n_estimators=700, learning_rate=0.1, max_depth=3  |
|           0.8401 | max_features="log2", n_estimators=700, learning_rate=0.1, max_depth=5  |
|           0.84   | max_features="log2", n_estimators=700, learning_rate=0.5, max_depth=5  |
|           0.8396 | max_features="log2", n_estimators=500, learning_rate=0.1, max_depth=5  |
|           0.8395 | max_features="log2", n_estimators=300, learning_rate=0.1, max_depth=5  |
|           0.8393 | max_features="log2", n_estimators=300, learning_rate=0.1, max_depth=3  |
|           0.8392 | max_features="log2", n_estimators=300, learning_rate=0.1, max_depth=1  |
|           0.8388 | max_features="log2", n_estimators=100, learning_rate=0.5, max_depth=1  |
|           0.8388 | max_features="log2", n_estimators=500, learning_rate=0.5, max_depth=7  |
|           0.8383 | max_features="log2", n_estimators=500, learning_rate=0.1, max_depth=1  |
|           0.8379 | max_features="log2", n_estimators=300, learning_rate=0.5, max_depth=1  |
|           0.8376 | max_features="log2", n_estimators=500, learning_rate=0.01, max_depth=1 |
|           0.837  | max_features="log2", n_estimators=700, learning_rate=0.1, max_depth=1  |
|           0.837  | max_features="log2", n_estimators=100, learning_rate=0.5, max_depth=7  |
|           0.836  | max_features="log2", n_estimators=500, learning_rate=0.5, max_depth=5  |
|           0.8358 | max_features="log2", n_estimators=500, learning_rate=1, max_depth=5    |
|           0.8357 | max_features="log2", n_estimators=300, learning_rate=0.01, max_depth=1 |
|           0.8353 | max_features="log2", n_estimators=100, learning_rate=0.5, max_depth=5  |
|           0.8352 | max_features="log2", n_estimators=300, learning_rate=0.5, max_depth=5  |
|           0.8343 | max_features="log2", n_estimators=500, learning_rate=0.5, max_depth=1  |
|           0.8329 | max_features="log2", n_estimators=300, learning_rate=0.5, max_depth=3  |
|           0.8318 | max_features="log2", n_estimators=700, learning_rate=0.5, max_depth=3  |
|           0.8312 | max_features="log2", n_estimators=100, learning_rate=0.01, max_depth=1 |
|           0.8311 | max_features="log2", n_estimators=500, learning_rate=0.5, max_depth=3  |
|           0.8291 | max_features="log2", n_estimators=500, learning_rate=1, max_depth=1    |
|           0.8275 | max_features="log2", n_estimators=700, learning_rate=0.5, max_depth=1  |
|           0.8274 | max_features="log2", n_estimators=100, learning_rate=1, max_depth=7    |
|           0.8256 | max_features="log2", n_estimators=100, learning_rate=1, max_depth=1    |
|           0.8214 | max_features="log2", n_estimators=100, learning_rate=0.5, max_depth=3  |
|           0.8209 | max_features="log2", n_estimators=700, learning_rate=1, max_depth=5    |
|           0.8203 | max_features="log2", n_estimators=100, learning_rate=1, max_depth=3    |
|           0.8203 | max_features="log2", n_estimators=700, learning_rate=1, max_depth=1    |
|           0.8158 | max_features="log2", n_estimators=500, learning_rate=1, max_depth=7    |
|           0.8143 | max_features="log2", n_estimators=100, learning_rate=1, max_depth=5    |
|           0.8089 | max_features="log2", n_estimators=300, learning_rate=1, max_depth=7    |
|           0.8072 | max_features="log2", n_estimators=700, learning_rate=1, max_depth=7    |
|           0.8007 | max_features="log2", n_estimators=300, learning_rate=1, max_depth=1    |
|           0.7846 | max_features="log2", n_estimators=300, learning_rate=1, max_depth=3    |
|           0.7813 | max_features="log2", n_estimators=500, learning_rate=1, max_depth=3    |
|           0.7795 | max_features="log2", n_estimators=300, learning_rate=1, max_depth=5    |
|           0.7256 | max_features="log2", n_estimators=700, learning_rate=1, max_depth=3    |

## GaussianNB
|   accuracy.macro | params   |
|-----------------:|:---------|
|           0.8403 |          |

## LogisticRegression
|   accuracy.macro | params              |
|-----------------:|:--------------------|
|           0.8485 | C=0.1, penalty="l2" |
|           0.8469 | C=1, penalty="l1"   |
|           0.8466 | C=0.1, penalty="l1" |
|           0.8464 | C=1, penalty="l2"   |
|           0.845  | C=10, penalty="l2"  |
|           0.8411 | C=10, penalty="l1"  |

## RandomForestClassifier
|   accuracy.macro | params                                                                          |
|-----------------:|:--------------------------------------------------------------------------------|
|           0.8539 | max_features="log2", n_estimators=160, min_samples_leaf=3, criterion="entropy"  |
|           0.8523 | max_features="log2", n_estimators=40, min_samples_leaf=7, criterion="entropy"   |
|           0.8523 | max_features="log2", n_estimators=80, min_samples_leaf=3, criterion="entropy"   |
|           0.8521 | max_features="log2", n_estimators=320, min_samples_leaf=5, criterion="gini"     |
|           0.852  | max_features="log2", n_estimators=640, min_samples_leaf=7, criterion="entropy"  |
|           0.8519 | max_features="log2", n_estimators=320, min_samples_leaf=5, criterion="entropy"  |
|           0.8516 | max_features="log2", n_estimators=640, min_samples_leaf=5, criterion="gini"     |
|           0.8515 | max_features="log2", n_estimators=80, min_samples_leaf=7, criterion="entropy"   |
|           0.8515 | max_features="log2", n_estimators=640, min_samples_leaf=5, criterion="entropy"  |
|           0.8515 | max_features="log2", n_estimators=40, min_samples_leaf=13, criterion="entropy"  |
|           0.8515 | max_features="log2", n_estimators=320, min_samples_leaf=1, criterion="entropy"  |
|           0.8512 | max_features="log2", n_estimators=640, min_samples_leaf=13, criterion="entropy" |
|           0.8511 | max_features="log2", n_estimators=320, min_samples_leaf=7, criterion="entropy"  |
|           0.8509 | max_features="log2", n_estimators=320, min_samples_leaf=13, criterion="entropy" |
|           0.8509 | max_features="log2", n_estimators=640, min_samples_leaf=7, criterion="gini"     |
|           0.8508 | max_features="log2", n_estimators=80, min_samples_leaf=13, criterion="entropy"  |
|           0.8507 | max_features="log2", n_estimators=640, min_samples_leaf=3, criterion="gini"     |
|           0.8507 | max_features="log2", n_estimators=640, min_samples_leaf=1, criterion="entropy"  |
|           0.8506 | max_features="log2", n_estimators=320, min_samples_leaf=3, criterion="entropy"  |
|           0.8506 | max_features="log2", n_estimators=160, min_samples_leaf=3, criterion="gini"     |
|           0.8506 | max_features="log2", n_estimators=640, min_samples_leaf=3, criterion="entropy"  |
|           0.8503 | max_features="log2", n_estimators=80, min_samples_leaf=1, criterion="entropy"   |
|           0.8502 | max_features="log2", n_estimators=160, min_samples_leaf=5, criterion="entropy"  |
|           0.8502 | max_features="log2", n_estimators=80, min_samples_leaf=5, criterion="entropy"   |
|           0.8502 | max_features="log2", n_estimators=160, min_samples_leaf=1, criterion="gini"     |
|           0.8501 | max_features="log2", n_estimators=320, min_samples_leaf=3, criterion="gini"     |
|           0.85   | max_features="log2", n_estimators=160, min_samples_leaf=13, criterion="entropy" |
|           0.8498 | max_features="log2", n_estimators=320, min_samples_leaf=13, criterion="gini"    |
|           0.8498 | max_features="log2", n_estimators=160, min_samples_leaf=7, criterion="entropy"  |
|           0.8496 | max_features="log2", n_estimators=80, min_samples_leaf=1, criterion="gini"      |
|           0.8496 | max_features="log2", n_estimators=80, min_samples_leaf=3, criterion="gini"      |
|           0.8494 | max_features="log2", n_estimators=320, min_samples_leaf=1, criterion="gini"     |
|           0.8494 | max_features="log2", n_estimators=320, min_samples_leaf=7, criterion="gini"     |
|           0.8493 | max_features="log2", n_estimators=160, min_samples_leaf=5, criterion="gini"     |
|           0.8492 | max_features="log2", n_estimators=640, min_samples_leaf=13, criterion="gini"    |
|           0.8492 | max_features="log2", n_estimators=640, min_samples_leaf=1, criterion="gini"     |
|           0.8489 | max_features="log2", n_estimators=160, min_samples_leaf=1, criterion="entropy"  |
|           0.8487 | max_features="log2", n_estimators=160, min_samples_leaf=13, criterion="gini"    |
|           0.8486 | max_features="log2", n_estimators=80, min_samples_leaf=7, criterion="gini"      |
|           0.8485 | max_features="log2", n_estimators=40, min_samples_leaf=3, criterion="entropy"   |
|           0.8483 | max_features="log2", n_estimators=40, min_samples_leaf=1, criterion="entropy"   |
|           0.848  | max_features="log2", n_estimators=160, min_samples_leaf=7, criterion="gini"     |
|           0.848  | max_features="log2", n_estimators=80, min_samples_leaf=5, criterion="gini"      |
|           0.8476 | max_features="log2", n_estimators=10, min_samples_leaf=13, criterion="entropy"  |
|           0.8475 | max_features="log2", n_estimators=40, min_samples_leaf=5, criterion="entropy"   |
|           0.8469 | max_features="log2", n_estimators=40, min_samples_leaf=3, criterion="gini"      |
|           0.8468 | max_features="log2", n_estimators=20, min_samples_leaf=3, criterion="entropy"   |
|           0.8467 | max_features="log2", n_estimators=40, min_samples_leaf=13, criterion="gini"     |
|           0.8466 | max_features="log2", n_estimators=80, min_samples_leaf=13, criterion="gini"     |
|           0.8463 | max_features="log2", n_estimators=40, min_samples_leaf=7, criterion="gini"      |
|           0.8461 | max_features="log2", n_estimators=20, min_samples_leaf=7, criterion="gini"      |
|           0.846  | max_features="log2", n_estimators=20, min_samples_leaf=5, criterion="entropy"   |
|           0.846  | max_features="log2", n_estimators=20, min_samples_leaf=7, criterion="entropy"   |
|           0.8455 | max_features="log2", n_estimators=40, min_samples_leaf=5, criterion="gini"      |
|           0.8453 | max_features="log2", n_estimators=20, min_samples_leaf=5, criterion="gini"      |
|           0.8444 | max_features="log2", n_estimators=40, min_samples_leaf=1, criterion="gini"      |
|           0.8433 | max_features="log2", n_estimators=20, min_samples_leaf=3, criterion="gini"      |
|           0.8432 | max_features="log2", n_estimators=20, min_samples_leaf=1, criterion="gini"      |
|           0.8431 | max_features="log2", n_estimators=20, min_samples_leaf=13, criterion="entropy"  |
|           0.8429 | max_features="log2", n_estimators=10, min_samples_leaf=5, criterion="gini"      |
|           0.8428 | max_features="log2", n_estimators=20, min_samples_leaf=13, criterion="gini"     |
|           0.8419 | max_features="log2", n_estimators=10, min_samples_leaf=7, criterion="gini"      |
|           0.8415 | max_features="log2", n_estimators=10, min_samples_leaf=13, criterion="gini"     |
|           0.8405 | max_features="log2", n_estimators=10, min_samples_leaf=5, criterion="entropy"   |
|           0.8402 | max_features="log2", n_estimators=10, min_samples_leaf=3, criterion="gini"      |
|           0.8401 | max_features="log2", n_estimators=20, min_samples_leaf=1, criterion="entropy"   |
|           0.84   | max_features="log2", n_estimators=10, min_samples_leaf=1, criterion="gini"      |
|           0.8396 | max_features="log2", n_estimators=10, min_samples_leaf=7, criterion="entropy"   |
|           0.8392 | max_features="log2", n_estimators=10, min_samples_leaf=3, criterion="entropy"   |
|           0.839  | max_features="log2", n_estimators=10, min_samples_leaf=1, criterion="entropy"   |

## BernoulliNB
|   accuracy.macro | params   |
|-----------------:|:---------|
|            0.833 |          |

