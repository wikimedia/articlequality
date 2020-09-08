# Model tuning report
- Revscoring version: 2.8.2
- Features: articlequality.feature_lists.wikidatawiki.item_quality
- Date: 2020-09-08T23:14:39.070565
- Observations: 8818
- Labels: ["A", "B", "C", "D", "E"]
- Statistic: accuracy.macro (maximize)
- Folds: 5

# Top scoring configurations
| model                  |   accuracy.macro | params                                                                         |
|:-----------------------|-----------------:|:-------------------------------------------------------------------------------|
| GradientBoosting       |           0.9552 | learning_rate=0.01, max_depth=7, max_features="log2", n_estimators=500         |
| GradientBoosting       |           0.9549 | learning_rate=0.01, max_depth=7, max_features="log2", n_estimators=700         |
| RandomForestClassifier |           0.9548 | criterion="gini", max_features="log2", min_samples_leaf=1, n_estimators=640    |
| GradientBoosting       |           0.9547 | learning_rate=0.01, max_depth=5, max_features="log2", n_estimators=500         |
| RandomForestClassifier |           0.9547 | criterion="gini", max_features="log2", min_samples_leaf=3, n_estimators=80     |
| RandomForestClassifier |           0.9546 | criterion="entropy", max_features="log2", min_samples_leaf=1, n_estimators=640 |
| GradientBoosting       |           0.9545 | learning_rate=0.01, max_depth=7, max_features="log2", n_estimators=300         |
| GradientBoosting       |           0.9545 | learning_rate=0.1, max_depth=7, max_features="log2", n_estimators=100          |
| RandomForestClassifier |           0.9545 | criterion="gini", max_features="log2", min_samples_leaf=1, n_estimators=160    |
| RandomForestClassifier |           0.9545 | criterion="entropy", max_features="log2", min_samples_leaf=1, n_estimators=80  |

# Models
## GradientBoosting
|   accuracy.macro | params                                                                 |
|-----------------:|:-----------------------------------------------------------------------|
|           0.9552 | learning_rate=0.01, max_depth=7, max_features="log2", n_estimators=500 |
|           0.9549 | learning_rate=0.01, max_depth=7, max_features="log2", n_estimators=700 |
|           0.9547 | learning_rate=0.01, max_depth=5, max_features="log2", n_estimators=500 |
|           0.9545 | learning_rate=0.01, max_depth=7, max_features="log2", n_estimators=300 |
|           0.9545 | learning_rate=0.1, max_depth=7, max_features="log2", n_estimators=100  |
|           0.9543 | learning_rate=0.01, max_depth=5, max_features="log2", n_estimators=700 |
|           0.9542 | learning_rate=0.1, max_depth=5, max_features="log2", n_estimators=100  |
|           0.9541 | learning_rate=0.1, max_depth=5, max_features="log2", n_estimators=500  |
|           0.9541 | learning_rate=0.1, max_depth=7, max_features="log2", n_estimators=300  |
|           0.9538 | learning_rate=0.1, max_depth=3, max_features="log2", n_estimators=500  |
|           0.9537 | learning_rate=0.1, max_depth=7, max_features="log2", n_estimators=500  |
|           0.9536 | learning_rate=0.1, max_depth=3, max_features="log2", n_estimators=300  |
|           0.9535 | learning_rate=0.01, max_depth=7, max_features="log2", n_estimators=100 |
|           0.9535 | learning_rate=0.1, max_depth=7, max_features="log2", n_estimators=700  |
|           0.9534 | learning_rate=0.1, max_depth=5, max_features="log2", n_estimators=700  |
|           0.9533 | learning_rate=0.1, max_depth=3, max_features="log2", n_estimators=700  |
|           0.9531 | learning_rate=0.5, max_depth=7, max_features="log2", n_estimators=700  |
|           0.9528 | learning_rate=0.5, max_depth=7, max_features="log2", n_estimators=500  |
|           0.9527 | learning_rate=0.1, max_depth=5, max_features="log2", n_estimators=300  |
|           0.9526 | learning_rate=0.5, max_depth=7, max_features="log2", n_estimators=300  |
|           0.9525 | learning_rate=0.1, max_depth=3, max_features="log2", n_estimators=100  |
|           0.9523 | learning_rate=0.01, max_depth=5, max_features="log2", n_estimators=300 |
|           0.9519 | learning_rate=0.5, max_depth=5, max_features="log2", n_estimators=300  |
|           0.9518 | learning_rate=0.01, max_depth=3, max_features="log2", n_estimators=700 |
|           0.9512 | learning_rate=0.01, max_depth=3, max_features="log2", n_estimators=500 |
|           0.9505 | learning_rate=0.01, max_depth=5, max_features="log2", n_estimators=100 |
|           0.9505 | learning_rate=0.5, max_depth=3, max_features="log2", n_estimators=100  |
|           0.9501 | learning_rate=0.5, max_depth=1, max_features="log2", n_estimators=500  |
|           0.9497 | learning_rate=0.1, max_depth=1, max_features="log2", n_estimators=500  |
|           0.9495 | learning_rate=0.1, max_depth=1, max_features="log2", n_estimators=700  |
|           0.9492 | learning_rate=0.5, max_depth=1, max_features="log2", n_estimators=100  |
|           0.949  | learning_rate=0.5, max_depth=1, max_features="log2", n_estimators=300  |
|           0.9487 | learning_rate=0.5, max_depth=1, max_features="log2", n_estimators=700  |
|           0.9482 | learning_rate=1, max_depth=1, max_features="log2", n_estimators=700    |
|           0.9482 | learning_rate=0.1, max_depth=1, max_features="log2", n_estimators=300  |
|           0.9481 | learning_rate=0.01, max_depth=3, max_features="log2", n_estimators=300 |
|           0.9481 | learning_rate=1, max_depth=1, max_features="log2", n_estimators=500    |
|           0.9479 | learning_rate=1, max_depth=1, max_features="log2", n_estimators=100    |
|           0.9391 | learning_rate=0.1, max_depth=1, max_features="log2", n_estimators=100  |
|           0.9391 | learning_rate=0.5, max_depth=5, max_features="log2", n_estimators=100  |
|           0.9369 | learning_rate=0.01, max_depth=3, max_features="log2", n_estimators=100 |
|           0.936  | learning_rate=1, max_depth=3, max_features="log2", n_estimators=100    |
|           0.935  | learning_rate=0.01, max_depth=1, max_features="log2", n_estimators=700 |
|           0.9311 | learning_rate=0.01, max_depth=1, max_features="log2", n_estimators=500 |
|           0.9235 | learning_rate=1, max_depth=1, max_features="log2", n_estimators=300    |
|           0.9234 | learning_rate=0.01, max_depth=1, max_features="log2", n_estimators=300 |
|           0.9101 | learning_rate=0.01, max_depth=1, max_features="log2", n_estimators=100 |
|           0.9012 | learning_rate=0.5, max_depth=3, max_features="log2", n_estimators=300  |
|           0.8956 | learning_rate=0.5, max_depth=3, max_features="log2", n_estimators=500  |
|           0.8751 | learning_rate=1, max_depth=3, max_features="log2", n_estimators=300    |
|           0.8546 | learning_rate=0.5, max_depth=3, max_features="log2", n_estimators=700  |
|           0.8517 | learning_rate=0.5, max_depth=5, max_features="log2", n_estimators=500  |
|           0.845  | learning_rate=0.5, max_depth=7, max_features="log2", n_estimators=100  |
|           0.8416 | learning_rate=0.5, max_depth=5, max_features="log2", n_estimators=700  |
|           0.8159 | learning_rate=1, max_depth=7, max_features="log2", n_estimators=100    |
|           0.7956 | learning_rate=1, max_depth=5, max_features="log2", n_estimators=100    |
|           0.7915 | learning_rate=1, max_depth=5, max_features="log2", n_estimators=300    |
|           0.7784 | learning_rate=1, max_depth=7, max_features="log2", n_estimators=700    |
|           0.759  | learning_rate=1, max_depth=3, max_features="log2", n_estimators=700    |
|           0.757  | learning_rate=1, max_depth=7, max_features="log2", n_estimators=300    |
|           0.7525 | learning_rate=1, max_depth=5, max_features="log2", n_estimators=700    |
|           0.7416 | learning_rate=1, max_depth=7, max_features="log2", n_estimators=500    |
|           0.7338 | learning_rate=1, max_depth=5, max_features="log2", n_estimators=500    |
|           0.7201 | learning_rate=1, max_depth=3, max_features="log2", n_estimators=500    |

## LogisticRegression
|   accuracy.macro | params              |
|-----------------:|:--------------------|
|           0.8921 | C=10, penalty="l2"  |
|           0.8914 | C=1, penalty="l2"   |
|           0.8891 | C=0.1, penalty="l2" |

## GaussianNB
|   accuracy.macro | params   |
|-----------------:|:---------|
|           0.8838 |          |

## BernoulliNB
|   accuracy.macro | params   |
|-----------------:|:---------|
|           0.8587 |          |

## RandomForestClassifier
|   accuracy.macro | params                                                                          |
|-----------------:|:--------------------------------------------------------------------------------|
|           0.9548 | criterion="gini", max_features="log2", min_samples_leaf=1, n_estimators=640     |
|           0.9547 | criterion="gini", max_features="log2", min_samples_leaf=3, n_estimators=80      |
|           0.9546 | criterion="entropy", max_features="log2", min_samples_leaf=1, n_estimators=640  |
|           0.9545 | criterion="gini", max_features="log2", min_samples_leaf=1, n_estimators=160     |
|           0.9545 | criterion="entropy", max_features="log2", min_samples_leaf=1, n_estimators=80   |
|           0.9544 | criterion="gini", max_features="log2", min_samples_leaf=1, n_estimators=320     |
|           0.9544 | criterion="gini", max_features="log2", min_samples_leaf=3, n_estimators=640     |
|           0.9544 | criterion="entropy", max_features="log2", min_samples_leaf=3, n_estimators=640  |
|           0.9543 | criterion="entropy", max_features="log2", min_samples_leaf=3, n_estimators=80   |
|           0.9542 | criterion="entropy", max_features="log2", min_samples_leaf=1, n_estimators=160  |
|           0.9541 | criterion="gini", max_features="log2", min_samples_leaf=3, n_estimators=320     |
|           0.9541 | criterion="entropy", max_features="log2", min_samples_leaf=3, n_estimators=320  |
|           0.954  | criterion="entropy", max_features="log2", min_samples_leaf=1, n_estimators=320  |
|           0.9539 | criterion="gini", max_features="log2", min_samples_leaf=1, n_estimators=40      |
|           0.9539 | criterion="entropy", max_features="log2", min_samples_leaf=3, n_estimators=40   |
|           0.9539 | criterion="entropy", max_features="log2", min_samples_leaf=3, n_estimators=20   |
|           0.9538 | criterion="gini", max_features="log2", min_samples_leaf=3, n_estimators=40      |
|           0.9537 | criterion="gini", max_features="log2", min_samples_leaf=3, n_estimators=160     |
|           0.9536 | criterion="entropy", max_features="log2", min_samples_leaf=3, n_estimators=160  |
|           0.9535 | criterion="gini", max_features="log2", min_samples_leaf=5, n_estimators=40      |
|           0.9534 | criterion="entropy", max_features="log2", min_samples_leaf=5, n_estimators=320  |
|           0.9533 | criterion="gini", max_features="log2", min_samples_leaf=5, n_estimators=640     |
|           0.9531 | criterion="gini", max_features="log2", min_samples_leaf=1, n_estimators=80      |
|           0.9531 | criterion="entropy", max_features="log2", min_samples_leaf=5, n_estimators=640  |
|           0.953  | criterion="entropy", max_features="log2", min_samples_leaf=5, n_estimators=80   |
|           0.953  | criterion="entropy", max_features="log2", min_samples_leaf=5, n_estimators=40   |
|           0.953  | criterion="gini", max_features="log2", min_samples_leaf=5, n_estimators=160     |
|           0.953  | criterion="entropy", max_features="log2", min_samples_leaf=5, n_estimators=160  |
|           0.9529 | criterion="gini", max_features="log2", min_samples_leaf=5, n_estimators=320     |
|           0.9529 | criterion="entropy", max_features="log2", min_samples_leaf=1, n_estimators=40   |
|           0.9527 | criterion="entropy", max_features="log2", min_samples_leaf=1, n_estimators=20   |
|           0.9527 | criterion="gini", max_features="log2", min_samples_leaf=5, n_estimators=80      |
|           0.9525 | criterion="gini", max_features="log2", min_samples_leaf=5, n_estimators=20      |
|           0.9524 | criterion="gini", max_features="log2", min_samples_leaf=3, n_estimators=20      |
|           0.9524 | criterion="entropy", max_features="log2", min_samples_leaf=7, n_estimators=320  |
|           0.9524 | criterion="gini", max_features="log2", min_samples_leaf=7, n_estimators=320     |
|           0.9523 | criterion="gini", max_features="log2", min_samples_leaf=7, n_estimators=160     |
|           0.9523 | criterion="entropy", max_features="log2", min_samples_leaf=3, n_estimators=10   |
|           0.9523 | criterion="entropy", max_features="log2", min_samples_leaf=7, n_estimators=640  |
|           0.9522 | criterion="gini", max_features="log2", min_samples_leaf=1, n_estimators=20      |
|           0.9522 | criterion="gini", max_features="log2", min_samples_leaf=7, n_estimators=640     |
|           0.9522 | criterion="entropy", max_features="log2", min_samples_leaf=7, n_estimators=160  |
|           0.9521 | criterion="entropy", max_features="log2", min_samples_leaf=7, n_estimators=80   |
|           0.952  | criterion="gini", max_features="log2", min_samples_leaf=7, n_estimators=80      |
|           0.9518 | criterion="gini", max_features="log2", min_samples_leaf=7, n_estimators=40      |
|           0.9517 | criterion="gini", max_features="log2", min_samples_leaf=7, n_estimators=20      |
|           0.9516 | criterion="entropy", max_features="log2", min_samples_leaf=5, n_estimators=20   |
|           0.9516 | criterion="entropy", max_features="log2", min_samples_leaf=5, n_estimators=10   |
|           0.9516 | criterion="entropy", max_features="log2", min_samples_leaf=7, n_estimators=40   |
|           0.9514 | criterion="entropy", max_features="log2", min_samples_leaf=7, n_estimators=20   |
|           0.9513 | criterion="gini", max_features="log2", min_samples_leaf=13, n_estimators=80     |
|           0.9513 | criterion="gini", max_features="log2", min_samples_leaf=13, n_estimators=160    |
|           0.9513 | criterion="gini", max_features="log2", min_samples_leaf=13, n_estimators=320    |
|           0.9513 | criterion="entropy", max_features="log2", min_samples_leaf=13, n_estimators=160 |
|           0.9512 | criterion="entropy", max_features="log2", min_samples_leaf=13, n_estimators=640 |
|           0.9509 | criterion="entropy", max_features="log2", min_samples_leaf=13, n_estimators=80  |
|           0.9509 | criterion="entropy", max_features="log2", min_samples_leaf=13, n_estimators=320 |
|           0.9508 | criterion="gini", max_features="log2", min_samples_leaf=3, n_estimators=10      |
|           0.9507 | criterion="gini", max_features="log2", min_samples_leaf=13, n_estimators=640    |
|           0.9506 | criterion="gini", max_features="log2", min_samples_leaf=7, n_estimators=10      |
|           0.9506 | criterion="entropy", max_features="log2", min_samples_leaf=13, n_estimators=40  |
|           0.9506 | criterion="entropy", max_features="log2", min_samples_leaf=7, n_estimators=10   |
|           0.9505 | criterion="gini", max_features="log2", min_samples_leaf=1, n_estimators=10      |
|           0.9505 | criterion="gini", max_features="log2", min_samples_leaf=13, n_estimators=40     |
|           0.9501 | criterion="entropy", max_features="log2", min_samples_leaf=1, n_estimators=10   |
|           0.95   | criterion="gini", max_features="log2", min_samples_leaf=5, n_estimators=10      |
|           0.9496 | criterion="entropy", max_features="log2", min_samples_leaf=13, n_estimators=20  |
|           0.9492 | criterion="gini", max_features="log2", min_samples_leaf=13, n_estimators=20     |
|           0.9489 | criterion="entropy", max_features="log2", min_samples_leaf=13, n_estimators=10  |
|           0.9482 | criterion="gini", max_features="log2", min_samples_leaf=13, n_estimators=10     |

