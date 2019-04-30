# Model tuning report
- Revscoring version: 2.3.4
- Features: articlequality.feature_lists.svwiki.wp10
- Date: 2019-04-30T17:03:11.839892
- Observations: 1960
- Labels: ["u", "b", "r", "s"]
- Statistic: accuracy.macro (maximize)
- Folds: 5

# Top scoring configurations
| model              |   accuracy.macro | params                                                                 |
|:-------------------|-----------------:|:-----------------------------------------------------------------------|
| GaussianNB         |           0.8668 |                                                                        |
| LogisticRegression |           0.8611 | C=10, penalty="l2"                                                     |
| LogisticRegression |           0.8609 | C=0.1, penalty="l2"                                                    |
| LogisticRegression |           0.8607 | C=0.1, penalty="l1"                                                    |
| LogisticRegression |           0.8601 | C=1, penalty="l2"                                                      |
| LogisticRegression |           0.8598 | C=1, penalty="l1"                                                      |
| GradientBoosting   |           0.8552 | n_estimators=300, learning_rate=0.01, max_depth=7, max_features="log2" |
| LogisticRegression |           0.8551 | C=10, penalty="l1"                                                     |
| GradientBoosting   |           0.8549 | n_estimators=300, learning_rate=0.01, max_depth=5, max_features="log2" |
| GradientBoosting   |           0.8542 | n_estimators=100, learning_rate=0.1, max_depth=3, max_features="log2"  |

# Models
## GaussianNB
|   accuracy.macro | params   |
|-----------------:|:---------|
|           0.8668 |          |

## BernoulliNB
|   accuracy.macro | params   |
|-----------------:|:---------|
|           0.8374 |          |

## RandomForestClassifier
|   accuracy.macro | params                                                                          |
|-----------------:|:--------------------------------------------------------------------------------|
|           0.8535 | n_estimators=20, min_samples_leaf=5, criterion="entropy", max_features="log2"   |
|           0.8534 | n_estimators=640, min_samples_leaf=1, criterion="gini", max_features="log2"     |
|           0.8533 | n_estimators=160, min_samples_leaf=5, criterion="entropy", max_features="log2"  |
|           0.8528 | n_estimators=640, min_samples_leaf=5, criterion="entropy", max_features="log2"  |
|           0.8524 | n_estimators=160, min_samples_leaf=1, criterion="entropy", max_features="log2"  |
|           0.8522 | n_estimators=80, min_samples_leaf=3, criterion="entropy", max_features="log2"   |
|           0.8521 | n_estimators=320, min_samples_leaf=3, criterion="entropy", max_features="log2"  |
|           0.8518 | n_estimators=320, min_samples_leaf=1, criterion="gini", max_features="log2"     |
|           0.8517 | n_estimators=160, min_samples_leaf=3, criterion="gini", max_features="log2"     |
|           0.8515 | n_estimators=640, min_samples_leaf=1, criterion="entropy", max_features="log2"  |
|           0.8515 | n_estimators=160, min_samples_leaf=7, criterion="entropy", max_features="log2"  |
|           0.8514 | n_estimators=80, min_samples_leaf=1, criterion="gini", max_features="log2"      |
|           0.8513 | n_estimators=40, min_samples_leaf=1, criterion="gini", max_features="log2"      |
|           0.8513 | n_estimators=80, min_samples_leaf=3, criterion="gini", max_features="log2"      |
|           0.8498 | n_estimators=320, min_samples_leaf=1, criterion="entropy", max_features="log2"  |
|           0.8497 | n_estimators=80, min_samples_leaf=7, criterion="entropy", max_features="log2"   |
|           0.8493 | n_estimators=640, min_samples_leaf=3, criterion="entropy", max_features="log2"  |
|           0.8491 | n_estimators=640, min_samples_leaf=3, criterion="gini", max_features="log2"     |
|           0.8489 | n_estimators=320, min_samples_leaf=5, criterion="gini", max_features="log2"     |
|           0.8484 | n_estimators=40, min_samples_leaf=3, criterion="gini", max_features="log2"      |
|           0.848  | n_estimators=10, min_samples_leaf=5, criterion="entropy", max_features="log2"   |
|           0.8478 | n_estimators=160, min_samples_leaf=1, criterion="gini", max_features="log2"     |
|           0.8477 | n_estimators=320, min_samples_leaf=3, criterion="gini", max_features="log2"     |
|           0.8476 | n_estimators=20, min_samples_leaf=3, criterion="gini", max_features="log2"      |
|           0.8476 | n_estimators=80, min_samples_leaf=1, criterion="entropy", max_features="log2"   |
|           0.8474 | n_estimators=40, min_samples_leaf=3, criterion="entropy", max_features="log2"   |
|           0.8473 | n_estimators=320, min_samples_leaf=5, criterion="entropy", max_features="log2"  |
|           0.8466 | n_estimators=640, min_samples_leaf=5, criterion="gini", max_features="log2"     |
|           0.8464 | n_estimators=160, min_samples_leaf=3, criterion="entropy", max_features="log2"  |
|           0.8463 | n_estimators=160, min_samples_leaf=5, criterion="gini", max_features="log2"     |
|           0.8459 | n_estimators=20, min_samples_leaf=1, criterion="gini", max_features="log2"      |
|           0.8458 | n_estimators=320, min_samples_leaf=7, criterion="entropy", max_features="log2"  |
|           0.8458 | n_estimators=80, min_samples_leaf=5, criterion="gini", max_features="log2"      |
|           0.8453 | n_estimators=10, min_samples_leaf=3, criterion="gini", max_features="log2"      |
|           0.845  | n_estimators=320, min_samples_leaf=7, criterion="gini", max_features="log2"     |
|           0.8448 | n_estimators=640, min_samples_leaf=7, criterion="gini", max_features="log2"     |
|           0.8447 | n_estimators=320, min_samples_leaf=13, criterion="entropy", max_features="log2" |
|           0.8444 | n_estimators=640, min_samples_leaf=7, criterion="entropy", max_features="log2"  |
|           0.8435 | n_estimators=20, min_samples_leaf=3, criterion="entropy", max_features="log2"   |
|           0.8434 | n_estimators=80, min_samples_leaf=7, criterion="gini", max_features="log2"      |
|           0.8432 | n_estimators=40, min_samples_leaf=1, criterion="entropy", max_features="log2"   |
|           0.842  | n_estimators=80, min_samples_leaf=13, criterion="entropy", max_features="log2"  |
|           0.8415 | n_estimators=10, min_samples_leaf=5, criterion="gini", max_features="log2"      |
|           0.8406 | n_estimators=640, min_samples_leaf=13, criterion="entropy", max_features="log2" |
|           0.8405 | n_estimators=40, min_samples_leaf=5, criterion="entropy", max_features="log2"   |
|           0.8395 | n_estimators=10, min_samples_leaf=7, criterion="entropy", max_features="log2"   |
|           0.8395 | n_estimators=20, min_samples_leaf=1, criterion="entropy", max_features="log2"   |
|           0.839  | n_estimators=40, min_samples_leaf=13, criterion="gini", max_features="log2"     |
|           0.8387 | n_estimators=10, min_samples_leaf=1, criterion="entropy", max_features="log2"   |
|           0.8387 | n_estimators=20, min_samples_leaf=7, criterion="gini", max_features="log2"      |
|           0.8377 | n_estimators=40, min_samples_leaf=5, criterion="gini", max_features="log2"      |
|           0.8375 | n_estimators=40, min_samples_leaf=7, criterion="entropy", max_features="log2"   |
|           0.8374 | n_estimators=80, min_samples_leaf=5, criterion="entropy", max_features="log2"   |
|           0.8372 | n_estimators=20, min_samples_leaf=5, criterion="gini", max_features="log2"      |
|           0.8371 | n_estimators=20, min_samples_leaf=7, criterion="entropy", max_features="log2"   |
|           0.837  | n_estimators=40, min_samples_leaf=7, criterion="gini", max_features="log2"      |
|           0.8353 | n_estimators=160, min_samples_leaf=13, criterion="gini", max_features="log2"    |
|           0.8332 | n_estimators=160, min_samples_leaf=7, criterion="gini", max_features="log2"     |
|           0.8326 | n_estimators=80, min_samples_leaf=13, criterion="gini", max_features="log2"     |
|           0.8315 | n_estimators=20, min_samples_leaf=13, criterion="gini", max_features="log2"     |
|           0.8307 | n_estimators=160, min_samples_leaf=13, criterion="entropy", max_features="log2" |
|           0.83   | n_estimators=640, min_samples_leaf=13, criterion="gini", max_features="log2"    |
|           0.8291 | n_estimators=10, min_samples_leaf=7, criterion="gini", max_features="log2"      |
|           0.8285 | n_estimators=40, min_samples_leaf=13, criterion="entropy", max_features="log2"  |
|           0.8263 | n_estimators=320, min_samples_leaf=13, criterion="gini", max_features="log2"    |
|           0.8215 | n_estimators=20, min_samples_leaf=13, criterion="entropy", max_features="log2"  |
|           0.8213 | n_estimators=10, min_samples_leaf=1, criterion="gini", max_features="log2"      |
|           0.8168 | n_estimators=10, min_samples_leaf=3, criterion="entropy", max_features="log2"   |
|           0.8095 | n_estimators=10, min_samples_leaf=13, criterion="entropy", max_features="log2"  |
|           0.8074 | n_estimators=10, min_samples_leaf=13, criterion="gini", max_features="log2"     |

## GradientBoosting
|   accuracy.macro | params                                                                 |
|-----------------:|:-----------------------------------------------------------------------|
|           0.8552 | n_estimators=300, learning_rate=0.01, max_depth=7, max_features="log2" |
|           0.8549 | n_estimators=300, learning_rate=0.01, max_depth=5, max_features="log2" |
|           0.8542 | n_estimators=100, learning_rate=0.1, max_depth=3, max_features="log2"  |
|           0.8539 | n_estimators=100, learning_rate=0.01, max_depth=7, max_features="log2" |
|           0.8532 | n_estimators=700, learning_rate=0.01, max_depth=3, max_features="log2" |
|           0.8523 | n_estimators=500, learning_rate=0.5, max_depth=5, max_features="log2"  |
|           0.8517 | n_estimators=500, learning_rate=0.01, max_depth=5, max_features="log2" |
|           0.851  | n_estimators=500, learning_rate=0.01, max_depth=3, max_features="log2" |
|           0.8508 | n_estimators=700, learning_rate=0.01, max_depth=7, max_features="log2" |
|           0.8507 | n_estimators=500, learning_rate=0.01, max_depth=7, max_features="log2" |
|           0.8499 | n_estimators=700, learning_rate=0.01, max_depth=5, max_features="log2" |
|           0.8498 | n_estimators=100, learning_rate=0.1, max_depth=5, max_features="log2"  |
|           0.848  | n_estimators=100, learning_rate=0.1, max_depth=7, max_features="log2"  |
|           0.8471 | n_estimators=100, learning_rate=0.5, max_depth=7, max_features="log2"  |
|           0.847  | n_estimators=700, learning_rate=0.1, max_depth=5, max_features="log2"  |
|           0.8466 | n_estimators=300, learning_rate=0.1, max_depth=7, max_features="log2"  |
|           0.8464 | n_estimators=300, learning_rate=0.01, max_depth=3, max_features="log2" |
|           0.8448 | n_estimators=100, learning_rate=0.01, max_depth=5, max_features="log2" |
|           0.8444 | n_estimators=700, learning_rate=0.1, max_depth=7, max_features="log2"  |
|           0.8442 | n_estimators=500, learning_rate=0.1, max_depth=7, max_features="log2"  |
|           0.8439 | n_estimators=500, learning_rate=0.1, max_depth=5, max_features="log2"  |
|           0.8426 | n_estimators=700, learning_rate=1, max_depth=5, max_features="log2"    |
|           0.8425 | n_estimators=300, learning_rate=0.5, max_depth=5, max_features="log2"  |
|           0.8422 | n_estimators=700, learning_rate=0.5, max_depth=5, max_features="log2"  |
|           0.8414 | n_estimators=700, learning_rate=0.5, max_depth=7, max_features="log2"  |
|           0.8413 | n_estimators=500, learning_rate=0.1, max_depth=1, max_features="log2"  |
|           0.8412 | n_estimators=500, learning_rate=0.5, max_depth=7, max_features="log2"  |
|           0.8403 | n_estimators=300, learning_rate=0.1, max_depth=3, max_features="log2"  |
|           0.84   | n_estimators=300, learning_rate=0.1, max_depth=5, max_features="log2"  |
|           0.8388 | n_estimators=700, learning_rate=0.1, max_depth=3, max_features="log2"  |
|           0.8384 | n_estimators=100, learning_rate=0.5, max_depth=5, max_features="log2"  |
|           0.8375 | n_estimators=300, learning_rate=1, max_depth=5, max_features="log2"    |
|           0.8374 | n_estimators=100, learning_rate=1, max_depth=5, max_features="log2"    |
|           0.8357 | n_estimators=300, learning_rate=0.1, max_depth=1, max_features="log2"  |
|           0.8356 | n_estimators=100, learning_rate=0.5, max_depth=1, max_features="log2"  |
|           0.8353 | n_estimators=500, learning_rate=1, max_depth=3, max_features="log2"    |
|           0.835  | n_estimators=700, learning_rate=0.5, max_depth=3, max_features="log2"  |
|           0.835  | n_estimators=100, learning_rate=0.1, max_depth=1, max_features="log2"  |
|           0.8343 | n_estimators=300, learning_rate=0.5, max_depth=7, max_features="log2"  |
|           0.8341 | n_estimators=700, learning_rate=0.1, max_depth=1, max_features="log2"  |
|           0.8333 | n_estimators=500, learning_rate=0.1, max_depth=3, max_features="log2"  |
|           0.8325 | n_estimators=100, learning_rate=0.01, max_depth=3, max_features="log2" |
|           0.8311 | n_estimators=100, learning_rate=1, max_depth=1, max_features="log2"    |
|           0.8293 | n_estimators=300, learning_rate=1, max_depth=3, max_features="log2"    |
|           0.8285 | n_estimators=500, learning_rate=0.5, max_depth=3, max_features="log2"  |
|           0.8284 | n_estimators=100, learning_rate=0.5, max_depth=3, max_features="log2"  |
|           0.8283 | n_estimators=700, learning_rate=1, max_depth=7, max_features="log2"    |
|           0.828  | n_estimators=500, learning_rate=1, max_depth=7, max_features="log2"    |
|           0.8275 | n_estimators=100, learning_rate=1, max_depth=3, max_features="log2"    |
|           0.8266 | n_estimators=100, learning_rate=1, max_depth=7, max_features="log2"    |
|           0.8259 | n_estimators=500, learning_rate=1, max_depth=5, max_features="log2"    |
|           0.8232 | n_estimators=700, learning_rate=1, max_depth=3, max_features="log2"    |
|           0.8219 | n_estimators=500, learning_rate=0.5, max_depth=1, max_features="log2"  |
|           0.8206 | n_estimators=300, learning_rate=0.5, max_depth=3, max_features="log2"  |
|           0.8206 | n_estimators=300, learning_rate=1, max_depth=7, max_features="log2"    |
|           0.816  | n_estimators=700, learning_rate=0.01, max_depth=1, max_features="log2" |
|           0.8145 | n_estimators=700, learning_rate=0.5, max_depth=1, max_features="log2"  |
|           0.8077 | n_estimators=300, learning_rate=0.5, max_depth=1, max_features="log2"  |
|           0.8047 | n_estimators=500, learning_rate=0.01, max_depth=1, max_features="log2" |
|           0.7963 | n_estimators=500, learning_rate=1, max_depth=1, max_features="log2"    |
|           0.7921 | n_estimators=100, learning_rate=0.01, max_depth=1, max_features="log2" |
|           0.7902 | n_estimators=700, learning_rate=1, max_depth=1, max_features="log2"    |
|           0.7881 | n_estimators=300, learning_rate=1, max_depth=1, max_features="log2"    |
|           0.7802 | n_estimators=300, learning_rate=0.01, max_depth=1, max_features="log2" |

## LogisticRegression
|   accuracy.macro | params              |
|-----------------:|:--------------------|
|           0.8611 | C=10, penalty="l2"  |
|           0.8609 | C=0.1, penalty="l2" |
|           0.8607 | C=0.1, penalty="l1" |
|           0.8601 | C=1, penalty="l2"   |
|           0.8598 | C=1, penalty="l1"   |
|           0.8551 | C=10, penalty="l1"  |

