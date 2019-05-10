# Model tuning report
- Revscoring version: 2.3.4
- Features: articlequality.feature_lists.svwiki.wp10
- Date: 2019-05-08T14:38:28.581808
- Observations: 1960
- Labels: ["u", "b", "r", "s"]
- Statistic: roc_auc.macro (maximize)
- Folds: 5

# Top scoring configurations
| model                  |   roc_auc.macro | params                                                                      |
|:-----------------------|----------------:|:----------------------------------------------------------------------------|
| GradientBoosting       |          0.8638 | max_depth=3, n_estimators=500, learning_rate=0.01, max_features="log2"      |
| GradientBoosting       |          0.8624 | max_depth=3, n_estimators=700, learning_rate=0.01, max_features="log2"      |
| GradientBoosting       |          0.8619 | max_depth=5, n_estimators=300, learning_rate=0.01, max_features="log2"      |
| LogisticRegression     |          0.8617 | C=10, penalty="l1"                                                          |
| GradientBoosting       |          0.8612 | max_depth=3, n_estimators=100, learning_rate=0.1, max_features="log2"       |
| LogisticRegression     |          0.8611 | C=10, penalty="l2"                                                          |
| RandomForestClassifier |          0.8605 | min_samples_leaf=3, n_estimators=640, criterion="gini", max_features="log2" |
| GradientBoosting       |          0.8605 | max_depth=3, n_estimators=300, learning_rate=0.01, max_features="log2"      |
| GradientBoosting       |          0.8602 | max_depth=5, n_estimators=100, learning_rate=0.01, max_features="log2"      |
| GradientBoosting       |          0.8597 | max_depth=5, n_estimators=500, learning_rate=0.01, max_features="log2"      |

# Models
## GradientBoosting
|   roc_auc.macro | params                                                                 |
|----------------:|:-----------------------------------------------------------------------|
|          0.8638 | max_depth=3, n_estimators=500, learning_rate=0.01, max_features="log2" |
|          0.8624 | max_depth=3, n_estimators=700, learning_rate=0.01, max_features="log2" |
|          0.8619 | max_depth=5, n_estimators=300, learning_rate=0.01, max_features="log2" |
|          0.8612 | max_depth=3, n_estimators=100, learning_rate=0.1, max_features="log2"  |
|          0.8605 | max_depth=3, n_estimators=300, learning_rate=0.01, max_features="log2" |
|          0.8602 | max_depth=5, n_estimators=100, learning_rate=0.01, max_features="log2" |
|          0.8597 | max_depth=5, n_estimators=500, learning_rate=0.01, max_features="log2" |
|          0.8589 | max_depth=7, n_estimators=300, learning_rate=0.01, max_features="log2" |
|          0.8589 | max_depth=7, n_estimators=100, learning_rate=0.01, max_features="log2" |
|          0.8581 | max_depth=5, n_estimators=700, learning_rate=0.01, max_features="log2" |
|          0.8578 | max_depth=7, n_estimators=500, learning_rate=0.01, max_features="log2" |
|          0.8569 | max_depth=7, n_estimators=700, learning_rate=0.01, max_features="log2" |
|          0.8564 | max_depth=1, n_estimators=100, learning_rate=0.5, max_features="log2"  |
|          0.8555 | max_depth=1, n_estimators=300, learning_rate=0.1, max_features="log2"  |
|          0.8543 | max_depth=7, n_estimators=500, learning_rate=0.1, max_features="log2"  |
|          0.8543 | max_depth=5, n_estimators=100, learning_rate=0.1, max_features="log2"  |
|          0.8542 | max_depth=3, n_estimators=300, learning_rate=0.1, max_features="log2"  |
|          0.8526 | max_depth=5, n_estimators=300, learning_rate=0.1, max_features="log2"  |
|          0.8524 | max_depth=1, n_estimators=100, learning_rate=0.1, max_features="log2"  |
|          0.852  | max_depth=1, n_estimators=500, learning_rate=0.1, max_features="log2"  |
|          0.8519 | max_depth=7, n_estimators=700, learning_rate=0.1, max_features="log2"  |
|          0.8516 | max_depth=1, n_estimators=700, learning_rate=0.1, max_features="log2"  |
|          0.8516 | max_depth=7, n_estimators=300, learning_rate=0.1, max_features="log2"  |
|          0.8513 | max_depth=3, n_estimators=100, learning_rate=0.01, max_features="log2" |
|          0.8513 | max_depth=7, n_estimators=100, learning_rate=0.1, max_features="log2"  |
|          0.8505 | max_depth=1, n_estimators=700, learning_rate=0.01, max_features="log2" |
|          0.8478 | max_depth=3, n_estimators=500, learning_rate=0.1, max_features="log2"  |
|          0.8476 | max_depth=7, n_estimators=300, learning_rate=0.5, max_features="log2"  |
|          0.8473 | max_depth=5, n_estimators=700, learning_rate=0.1, max_features="log2"  |
|          0.8472 | max_depth=5, n_estimators=500, learning_rate=0.1, max_features="log2"  |
|          0.8461 | max_depth=1, n_estimators=300, learning_rate=0.5, max_features="log2"  |
|          0.8455 | max_depth=1, n_estimators=500, learning_rate=0.01, max_features="log2" |
|          0.8454 | max_depth=7, n_estimators=100, learning_rate=0.5, max_features="log2"  |
|          0.8451 | max_depth=7, n_estimators=700, learning_rate=0.5, max_features="log2"  |
|          0.8451 | max_depth=5, n_estimators=100, learning_rate=0.5, max_features="log2"  |
|          0.8446 | max_depth=3, n_estimators=100, learning_rate=0.5, max_features="log2"  |
|          0.8437 | max_depth=5, n_estimators=500, learning_rate=0.5, max_features="log2"  |
|          0.8432 | max_depth=3, n_estimators=700, learning_rate=0.1, max_features="log2"  |
|          0.8428 | max_depth=5, n_estimators=700, learning_rate=0.5, max_features="log2"  |
|          0.8415 | max_depth=7, n_estimators=500, learning_rate=0.5, max_features="log2"  |
|          0.8414 | max_depth=5, n_estimators=300, learning_rate=0.5, max_features="log2"  |
|          0.8385 | max_depth=1, n_estimators=300, learning_rate=0.01, max_features="log2" |
|          0.8383 | max_depth=1, n_estimators=500, learning_rate=0.5, max_features="log2"  |
|          0.836  | max_depth=1, n_estimators=100, learning_rate=1, max_features="log2"    |
|          0.836  | max_depth=1, n_estimators=700, learning_rate=0.5, max_features="log2"  |
|          0.8329 | max_depth=5, n_estimators=700, learning_rate=1, max_features="log2"    |
|          0.8327 | max_depth=3, n_estimators=300, learning_rate=0.5, max_features="log2"  |
|          0.8326 | max_depth=1, n_estimators=300, learning_rate=1, max_features="log2"    |
|          0.8317 | max_depth=3, n_estimators=300, learning_rate=1, max_features="log2"    |
|          0.8316 | max_depth=3, n_estimators=500, learning_rate=0.5, max_features="log2"  |
|          0.8313 | max_depth=7, n_estimators=500, learning_rate=1, max_features="log2"    |
|          0.8305 | max_depth=5, n_estimators=500, learning_rate=1, max_features="log2"    |
|          0.8301 | max_depth=7, n_estimators=700, learning_rate=1, max_features="log2"    |
|          0.8299 | max_depth=7, n_estimators=300, learning_rate=1, max_features="log2"    |
|          0.8297 | max_depth=7, n_estimators=100, learning_rate=1, max_features="log2"    |
|          0.8285 | max_depth=1, n_estimators=100, learning_rate=0.01, max_features="log2" |
|          0.8274 | max_depth=1, n_estimators=500, learning_rate=1, max_features="log2"    |
|          0.8274 | max_depth=3, n_estimators=700, learning_rate=0.5, max_features="log2"  |
|          0.8262 | max_depth=1, n_estimators=700, learning_rate=1, max_features="log2"    |
|          0.8251 | max_depth=5, n_estimators=100, learning_rate=1, max_features="log2"    |
|          0.8223 | max_depth=3, n_estimators=500, learning_rate=1, max_features="log2"    |
|          0.8088 | max_depth=3, n_estimators=100, learning_rate=1, max_features="log2"    |
|          0.7943 | max_depth=3, n_estimators=700, learning_rate=1, max_features="log2"    |
|          0.7613 | max_depth=5, n_estimators=300, learning_rate=1, max_features="log2"    |

## LogisticRegression
|   roc_auc.macro | params              |
|----------------:|:--------------------|
|          0.8617 | C=10, penalty="l1"  |
|          0.8611 | C=10, penalty="l2"  |
|          0.8592 | C=1, penalty="l1"   |
|          0.8591 | C=1, penalty="l2"   |
|          0.8532 | C=0.1, penalty="l2" |
|          0.8505 | C=0.1, penalty="l1" |

## RandomForestClassifier
|   roc_auc.macro | params                                                                          |
|----------------:|:--------------------------------------------------------------------------------|
|          0.8605 | min_samples_leaf=3, n_estimators=640, criterion="gini", max_features="log2"     |
|          0.8594 | min_samples_leaf=5, n_estimators=640, criterion="gini", max_features="log2"     |
|          0.8593 | min_samples_leaf=3, n_estimators=320, criterion="entropy", max_features="log2"  |
|          0.8588 | min_samples_leaf=5, n_estimators=320, criterion="gini", max_features="log2"     |
|          0.8586 | min_samples_leaf=3, n_estimators=320, criterion="gini", max_features="log2"     |
|          0.8586 | min_samples_leaf=5, n_estimators=160, criterion="gini", max_features="log2"     |
|          0.8581 | min_samples_leaf=3, n_estimators=640, criterion="entropy", max_features="log2"  |
|          0.858  | min_samples_leaf=3, n_estimators=160, criterion="gini", max_features="log2"     |
|          0.8576 | min_samples_leaf=5, n_estimators=320, criterion="entropy", max_features="log2"  |
|          0.8576 | min_samples_leaf=5, n_estimators=640, criterion="entropy", max_features="log2"  |
|          0.8575 | min_samples_leaf=1, n_estimators=640, criterion="gini", max_features="log2"     |
|          0.8575 | min_samples_leaf=7, n_estimators=160, criterion="entropy", max_features="log2"  |
|          0.8574 | min_samples_leaf=5, n_estimators=80, criterion="entropy", max_features="log2"   |
|          0.8572 | min_samples_leaf=7, n_estimators=320, criterion="gini", max_features="log2"     |
|          0.8572 | min_samples_leaf=7, n_estimators=80, criterion="gini", max_features="log2"      |
|          0.857  | min_samples_leaf=3, n_estimators=80, criterion="gini", max_features="log2"      |
|          0.8567 | min_samples_leaf=7, n_estimators=640, criterion="gini", max_features="log2"     |
|          0.8567 | min_samples_leaf=7, n_estimators=640, criterion="entropy", max_features="log2"  |
|          0.8567 | min_samples_leaf=5, n_estimators=160, criterion="entropy", max_features="log2"  |
|          0.8566 | min_samples_leaf=7, n_estimators=320, criterion="entropy", max_features="log2"  |
|          0.8563 | min_samples_leaf=1, n_estimators=640, criterion="entropy", max_features="log2"  |
|          0.8561 | min_samples_leaf=1, n_estimators=320, criterion="entropy", max_features="log2"  |
|          0.8561 | min_samples_leaf=1, n_estimators=320, criterion="gini", max_features="log2"     |
|          0.856  | min_samples_leaf=5, n_estimators=80, criterion="gini", max_features="log2"      |
|          0.8559 | min_samples_leaf=7, n_estimators=160, criterion="gini", max_features="log2"     |
|          0.8556 | min_samples_leaf=3, n_estimators=40, criterion="gini", max_features="log2"      |
|          0.8555 | min_samples_leaf=1, n_estimators=160, criterion="entropy", max_features="log2"  |
|          0.8554 | min_samples_leaf=13, n_estimators=320, criterion="gini", max_features="log2"    |
|          0.8554 | min_samples_leaf=3, n_estimators=160, criterion="entropy", max_features="log2"  |
|          0.8553 | min_samples_leaf=7, n_estimators=80, criterion="entropy", max_features="log2"   |
|          0.8551 | min_samples_leaf=3, n_estimators=80, criterion="entropy", max_features="log2"   |
|          0.8548 | min_samples_leaf=1, n_estimators=160, criterion="gini", max_features="log2"     |
|          0.8548 | min_samples_leaf=5, n_estimators=40, criterion="gini", max_features="log2"      |
|          0.8545 | min_samples_leaf=7, n_estimators=20, criterion="gini", max_features="log2"      |
|          0.8542 | min_samples_leaf=13, n_estimators=80, criterion="gini", max_features="log2"     |
|          0.8542 | min_samples_leaf=13, n_estimators=640, criterion="entropy", max_features="log2" |
|          0.854  | min_samples_leaf=13, n_estimators=160, criterion="gini", max_features="log2"    |
|          0.8539 | min_samples_leaf=7, n_estimators=40, criterion="gini", max_features="log2"      |
|          0.8534 | min_samples_leaf=13, n_estimators=640, criterion="gini", max_features="log2"    |
|          0.8534 | min_samples_leaf=13, n_estimators=320, criterion="entropy", max_features="log2" |
|          0.853  | min_samples_leaf=5, n_estimators=20, criterion="gini", max_features="log2"      |
|          0.8528 | min_samples_leaf=13, n_estimators=40, criterion="gini", max_features="log2"     |
|          0.8528 | min_samples_leaf=13, n_estimators=160, criterion="entropy", max_features="log2" |
|          0.8527 | min_samples_leaf=1, n_estimators=80, criterion="entropy", max_features="log2"   |
|          0.8516 | min_samples_leaf=5, n_estimators=40, criterion="entropy", max_features="log2"   |
|          0.8514 | min_samples_leaf=5, n_estimators=20, criterion="entropy", max_features="log2"   |
|          0.8511 | min_samples_leaf=1, n_estimators=80, criterion="gini", max_features="log2"      |
|          0.851  | min_samples_leaf=13, n_estimators=80, criterion="entropy", max_features="log2"  |
|          0.851  | min_samples_leaf=3, n_estimators=40, criterion="entropy", max_features="log2"   |
|          0.8507 | min_samples_leaf=13, n_estimators=20, criterion="entropy", max_features="log2"  |
|          0.8505 | min_samples_leaf=7, n_estimators=10, criterion="gini", max_features="log2"      |
|          0.8501 | min_samples_leaf=1, n_estimators=40, criterion="gini", max_features="log2"      |
|          0.8501 | min_samples_leaf=13, n_estimators=10, criterion="gini", max_features="log2"     |
|          0.8498 | min_samples_leaf=13, n_estimators=40, criterion="entropy", max_features="log2"  |
|          0.8497 | min_samples_leaf=1, n_estimators=40, criterion="entropy", max_features="log2"   |
|          0.8496 | min_samples_leaf=7, n_estimators=20, criterion="entropy", max_features="log2"   |
|          0.8488 | min_samples_leaf=5, n_estimators=10, criterion="entropy", max_features="log2"   |
|          0.8484 | min_samples_leaf=3, n_estimators=20, criterion="gini", max_features="log2"      |
|          0.8466 | min_samples_leaf=7, n_estimators=40, criterion="entropy", max_features="log2"   |
|          0.8461 | min_samples_leaf=3, n_estimators=20, criterion="entropy", max_features="log2"   |
|          0.846  | min_samples_leaf=13, n_estimators=20, criterion="gini", max_features="log2"     |
|          0.8442 | min_samples_leaf=13, n_estimators=10, criterion="entropy", max_features="log2"  |
|          0.8434 | min_samples_leaf=3, n_estimators=10, criterion="gini", max_features="log2"      |
|          0.8434 | min_samples_leaf=7, n_estimators=10, criterion="entropy", max_features="log2"   |
|          0.8426 | min_samples_leaf=3, n_estimators=10, criterion="entropy", max_features="log2"   |
|          0.8401 | min_samples_leaf=1, n_estimators=20, criterion="entropy", max_features="log2"   |
|          0.84   | min_samples_leaf=5, n_estimators=10, criterion="gini", max_features="log2"      |
|          0.8397 | min_samples_leaf=1, n_estimators=20, criterion="gini", max_features="log2"      |
|          0.8362 | min_samples_leaf=1, n_estimators=10, criterion="entropy", max_features="log2"   |
|          0.8212 | min_samples_leaf=1, n_estimators=10, criterion="gini", max_features="log2"      |

## GaussianNB
|   roc_auc.macro | params   |
|----------------:|:---------|
|          0.8074 |          |

## BernoulliNB
|   roc_auc.macro | params   |
|----------------:|:---------|
|          0.8135 |          |

