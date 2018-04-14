# Model tuning report
- Revscoring version: 2.1.0
- Features: articlequality.feature_lists.fawiki.wp10
- Date: 2018-04-14T15:51:53.731902
- Observations: 665
- Labels: ["Stub", "Start", "C", "B", "GA", "FA"]
- Statistic: accuracy.macro (maximize)
- Folds: 5

# Top scoring configurations
| model                  |   accuracy.macro | params                                                                         |
|:-----------------------|-----------------:|:-------------------------------------------------------------------------------|
| GradientBoosting       |           0.8531 | max_depth=7, max_features="log2", learning_rate=0.01, n_estimators=700         |
| GradientBoosting       |           0.8531 | max_depth=7, max_features="log2", learning_rate=0.1, n_estimators=700          |
| GradientBoosting       |           0.8521 | max_depth=7, max_features="log2", learning_rate=0.01, n_estimators=500         |
| GradientBoosting       |           0.8511 | max_depth=7, max_features="log2", learning_rate=0.1, n_estimators=300          |
| RandomForestClassifier |           0.8511 | criterion="entropy", max_features="log2", min_samples_leaf=5, n_estimators=640 |
| GradientBoosting       |           0.8506 | max_depth=5, max_features="log2", learning_rate=0.1, n_estimators=300          |
| GradientBoosting       |           0.8506 | max_depth=7, max_features="log2", learning_rate=0.5, n_estimators=500          |
| RandomForestClassifier |           0.8506 | criterion="entropy", max_features="log2", min_samples_leaf=3, n_estimators=640 |
| RandomForestClassifier |           0.8501 | criterion="gini", max_features="log2", min_samples_leaf=3, n_estimators=160    |
| RandomForestClassifier |           0.8501 | criterion="gini", max_features="log2", min_samples_leaf=5, n_estimators=320    |

# Models
## GaussianNB
|   accuracy.macro | params   |
|-----------------:|:---------|
|           0.8025 |          |

## GradientBoosting
|   accuracy.macro | params                                                                 |
|-----------------:|:-----------------------------------------------------------------------|
|           0.8531 | max_depth=7, max_features="log2", learning_rate=0.01, n_estimators=700 |
|           0.8531 | max_depth=7, max_features="log2", learning_rate=0.1, n_estimators=700  |
|           0.8521 | max_depth=7, max_features="log2", learning_rate=0.01, n_estimators=500 |
|           0.8511 | max_depth=7, max_features="log2", learning_rate=0.1, n_estimators=300  |
|           0.8506 | max_depth=5, max_features="log2", learning_rate=0.1, n_estimators=300  |
|           0.8506 | max_depth=7, max_features="log2", learning_rate=0.5, n_estimators=500  |
|           0.8501 | max_depth=7, max_features="log2", learning_rate=0.01, n_estimators=300 |
|           0.8496 | max_depth=5, max_features="log2", learning_rate=0.1, n_estimators=700  |
|           0.8496 | max_depth=7, max_features="log2", learning_rate=0.1, n_estimators=100  |
|           0.8491 | max_depth=7, max_features="log2", learning_rate=0.1, n_estimators=500  |
|           0.8491 | max_depth=7, max_features="log2", learning_rate=0.5, n_estimators=300  |
|           0.8481 | max_depth=7, max_features="log2", learning_rate=0.01, n_estimators=100 |
|           0.8481 | max_depth=3, max_features="log2", learning_rate=0.1, n_estimators=700  |
|           0.8476 | max_depth=5, max_features="log2", learning_rate=0.01, n_estimators=500 |
|           0.8476 | max_depth=5, max_features="log2", learning_rate=0.01, n_estimators=700 |
|           0.8471 | max_depth=5, max_features="log2", learning_rate=0.01, n_estimators=300 |
|           0.8471 | max_depth=5, max_features="log2", learning_rate=0.5, n_estimators=300  |
|           0.8471 | max_depth=5, max_features="log2", learning_rate=0.5, n_estimators=500  |
|           0.8466 | max_depth=3, max_features="log2", learning_rate=0.1, n_estimators=300  |
|           0.8466 | max_depth=7, max_features="log2", learning_rate=0.5, n_estimators=100  |
|           0.8461 | max_depth=5, max_features="log2", learning_rate=0.5, n_estimators=700  |
|           0.8456 | max_depth=5, max_features="log2", learning_rate=0.1, n_estimators=500  |
|           0.8456 | max_depth=3, max_features="log2", learning_rate=0.5, n_estimators=300  |
|           0.8451 | max_depth=3, max_features="log2", learning_rate=0.1, n_estimators=500  |
|           0.8446 | max_depth=5, max_features="log2", learning_rate=0.01, n_estimators=100 |
|           0.8441 | max_depth=3, max_features="log2", learning_rate=0.01, n_estimators=700 |
|           0.8436 | max_depth=7, max_features="log2", learning_rate=0.5, n_estimators=700  |
|           0.8426 | max_depth=3, max_features="log2", learning_rate=0.5, n_estimators=500  |
|           0.8421 | max_depth=1, max_features="log2", learning_rate=0.01, n_estimators=500 |
|           0.8421 | max_depth=1, max_features="log2", learning_rate=0.1, n_estimators=300  |
|           0.8421 | max_depth=3, max_features="log2", learning_rate=0.5, n_estimators=700  |
|           0.8416 | max_depth=3, max_features="log2", learning_rate=0.01, n_estimators=500 |
|           0.8416 | max_depth=5, max_features="log2", learning_rate=0.5, n_estimators=100  |
|           0.8411 | max_depth=5, max_features="log2", learning_rate=0.1, n_estimators=100  |
|           0.8401 | max_depth=3, max_features="log2", learning_rate=0.01, n_estimators=100 |
|           0.8396 | max_depth=3, max_features="log2", learning_rate=0.01, n_estimators=300 |
|           0.8391 | max_depth=1, max_features="log2", learning_rate=0.01, n_estimators=700 |
|           0.8391 | max_depth=1, max_features="log2", learning_rate=0.1, n_estimators=700  |
|           0.8381 | max_depth=7, max_features="log2", learning_rate=1, n_estimators=100    |
|           0.8381 | max_depth=7, max_features="log2", learning_rate=1, n_estimators=700    |
|           0.8376 | max_depth=3, max_features="log2", learning_rate=0.1, n_estimators=100  |
|           0.8376 | max_depth=1, max_features="log2", learning_rate=0.1, n_estimators=500  |
|           0.8356 | max_depth=1, max_features="log2", learning_rate=0.1, n_estimators=100  |
|           0.8351 | max_depth=1, max_features="log2", learning_rate=0.01, n_estimators=300 |
|           0.8336 | max_depth=1, max_features="log2", learning_rate=0.5, n_estimators=100  |
|           0.8326 | max_depth=7, max_features="log2", learning_rate=1, n_estimators=500    |
|           0.8301 | max_depth=1, max_features="log2", learning_rate=0.5, n_estimators=500  |
|           0.8291 | max_depth=1, max_features="log2", learning_rate=0.5, n_estimators=300  |
|           0.8286 | max_depth=1, max_features="log2", learning_rate=0.5, n_estimators=700  |
|           0.8281 | max_depth=1, max_features="log2", learning_rate=0.01, n_estimators=100 |
|           0.8206 | max_depth=3, max_features="log2", learning_rate=0.5, n_estimators=100  |
|           0.812  | max_depth=5, max_features="log2", learning_rate=1, n_estimators=700    |
|           0.812  | max_depth=3, max_features="log2", learning_rate=1, n_estimators=700    |
|           0.7965 | max_depth=7, max_features="log2", learning_rate=1, n_estimators=300    |
|           0.795  | max_depth=5, max_features="log2", learning_rate=1, n_estimators=300    |
|           0.7935 | max_depth=5, max_features="log2", learning_rate=1, n_estimators=500    |
|           0.7895 | max_depth=3, max_features="log2", learning_rate=1, n_estimators=300    |
|           0.7855 | max_depth=1, max_features="log2", learning_rate=1, n_estimators=500    |
|           0.7835 | max_depth=5, max_features="log2", learning_rate=1, n_estimators=100    |
|           0.7789 | max_depth=3, max_features="log2", learning_rate=1, n_estimators=500    |
|           0.7644 | max_depth=1, max_features="log2", learning_rate=1, n_estimators=300    |
|           0.7614 | max_depth=3, max_features="log2", learning_rate=1, n_estimators=100    |
|           0.7524 | max_depth=1, max_features="log2", learning_rate=1, n_estimators=100    |
|           0.7353 | max_depth=1, max_features="log2", learning_rate=1, n_estimators=700    |

## BernoulliNB
|   accuracy.macro | params   |
|-----------------:|:---------|
|            0.808 |          |

## LogisticRegression
|   accuracy.macro | params              |
|-----------------:|:--------------------|
|           0.8326 | penalty="l2", C=0.1 |
|           0.8286 | penalty="l1", C=1   |
|           0.8271 | penalty="l2", C=1   |
|           0.8256 | penalty="l1", C=0.1 |
|           0.8246 | penalty="l2", C=10  |
|           0.8241 | penalty="l1", C=10  |

## RandomForestClassifier
|   accuracy.macro | params                                                                          |
|-----------------:|:--------------------------------------------------------------------------------|
|           0.8511 | criterion="entropy", max_features="log2", min_samples_leaf=5, n_estimators=640  |
|           0.8506 | criterion="entropy", max_features="log2", min_samples_leaf=3, n_estimators=640  |
|           0.8501 | criterion="gini", max_features="log2", min_samples_leaf=3, n_estimators=160     |
|           0.8501 | criterion="gini", max_features="log2", min_samples_leaf=5, n_estimators=320     |
|           0.8501 | criterion="gini", max_features="log2", min_samples_leaf=7, n_estimators=80      |
|           0.8501 | criterion="entropy", max_features="log2", min_samples_leaf=5, n_estimators=40   |
|           0.8496 | criterion="gini", max_features="log2", min_samples_leaf=1, n_estimators=320     |
|           0.8496 | criterion="entropy", max_features="log2", min_samples_leaf=3, n_estimators=160  |
|           0.8491 | criterion="gini", max_features="log2", min_samples_leaf=3, n_estimators=320     |
|           0.8491 | criterion="gini", max_features="log2", min_samples_leaf=3, n_estimators=40      |
|           0.8491 | criterion="gini", max_features="log2", min_samples_leaf=5, n_estimators=10      |
|           0.8491 | criterion="entropy", max_features="log2", min_samples_leaf=1, n_estimators=80   |
|           0.8491 | criterion="entropy", max_features="log2", min_samples_leaf=1, n_estimators=320  |
|           0.8491 | criterion="entropy", max_features="log2", min_samples_leaf=1, n_estimators=640  |
|           0.8486 | criterion="gini", max_features="log2", min_samples_leaf=1, n_estimators=40      |
|           0.8486 | criterion="gini", max_features="log2", min_samples_leaf=3, n_estimators=80      |
|           0.8486 | criterion="entropy", max_features="log2", min_samples_leaf=3, n_estimators=20   |
|           0.8486 | criterion="entropy", max_features="log2", min_samples_leaf=3, n_estimators=320  |
|           0.8481 | criterion="gini", max_features="log2", min_samples_leaf=3, n_estimators=640     |
|           0.8481 | criterion="entropy", max_features="log2", min_samples_leaf=1, n_estimators=160  |
|           0.8481 | criterion="entropy", max_features="log2", min_samples_leaf=7, n_estimators=160  |
|           0.8481 | criterion="gini", max_features="log2", min_samples_leaf=1, n_estimators=80      |
|           0.8481 | criterion="entropy", max_features="log2", min_samples_leaf=5, n_estimators=10   |
|           0.8481 | criterion="entropy", max_features="log2", min_samples_leaf=7, n_estimators=80   |
|           0.8476 | criterion="gini", max_features="log2", min_samples_leaf=3, n_estimators=20      |
|           0.8476 | criterion="gini", max_features="log2", min_samples_leaf=13, n_estimators=80     |
|           0.8476 | criterion="gini", max_features="log2", min_samples_leaf=1, n_estimators=640     |
|           0.8471 | criterion="gini", max_features="log2", min_samples_leaf=1, n_estimators=160     |
|           0.8471 | criterion="entropy", max_features="log2", min_samples_leaf=1, n_estimators=40   |
|           0.8471 | criterion="entropy", max_features="log2", min_samples_leaf=3, n_estimators=80   |
|           0.8466 | criterion="gini", max_features="log2", min_samples_leaf=5, n_estimators=640     |
|           0.8466 | criterion="gini", max_features="log2", min_samples_leaf=7, n_estimators=320     |
|           0.8466 | criterion="entropy", max_features="log2", min_samples_leaf=1, n_estimators=10   |
|           0.8466 | criterion="entropy", max_features="log2", min_samples_leaf=3, n_estimators=40   |
|           0.8466 | criterion="entropy", max_features="log2", min_samples_leaf=13, n_estimators=20  |
|           0.8466 | criterion="entropy", max_features="log2", min_samples_leaf=5, n_estimators=20   |
|           0.8461 | criterion="gini", max_features="log2", min_samples_leaf=1, n_estimators=20      |
|           0.8461 | criterion="gini", max_features="log2", min_samples_leaf=13, n_estimators=320    |
|           0.8461 | criterion="entropy", max_features="log2", min_samples_leaf=1, n_estimators=20   |
|           0.8461 | criterion="gini", max_features="log2", min_samples_leaf=7, n_estimators=160     |
|           0.8461 | criterion="entropy", max_features="log2", min_samples_leaf=5, n_estimators=80   |
|           0.8461 | criterion="entropy", max_features="log2", min_samples_leaf=5, n_estimators=160  |
|           0.8456 | criterion="gini", max_features="log2", min_samples_leaf=13, n_estimators=640    |
|           0.8456 | criterion="entropy", max_features="log2", min_samples_leaf=7, n_estimators=320  |
|           0.8456 | criterion="entropy", max_features="log2", min_samples_leaf=13, n_estimators=160 |
|           0.8451 | criterion="entropy", max_features="log2", min_samples_leaf=13, n_estimators=640 |
|           0.8446 | criterion="gini", max_features="log2", min_samples_leaf=13, n_estimators=40     |
|           0.8446 | criterion="entropy", max_features="log2", min_samples_leaf=7, n_estimators=640  |
|           0.8441 | criterion="entropy", max_features="log2", min_samples_leaf=13, n_estimators=10  |
|           0.8441 | criterion="entropy", max_features="log2", min_samples_leaf=13, n_estimators=320 |
|           0.8441 | criterion="gini", max_features="log2", min_samples_leaf=5, n_estimators=80      |
|           0.8436 | criterion="gini", max_features="log2", min_samples_leaf=3, n_estimators=10      |
|           0.8436 | criterion="gini", max_features="log2", min_samples_leaf=5, n_estimators=160     |
|           0.8436 | criterion="gini", max_features="log2", min_samples_leaf=7, n_estimators=640     |
|           0.8431 | criterion="gini", max_features="log2", min_samples_leaf=7, n_estimators=40      |
|           0.8431 | criterion="entropy", max_features="log2", min_samples_leaf=5, n_estimators=320  |
|           0.8431 | criterion="entropy", max_features="log2", min_samples_leaf=7, n_estimators=20   |
|           0.8426 | criterion="gini", max_features="log2", min_samples_leaf=5, n_estimators=20      |
|           0.8426 | criterion="gini", max_features="log2", min_samples_leaf=13, n_estimators=20     |
|           0.8426 | criterion="entropy", max_features="log2", min_samples_leaf=13, n_estimators=80  |
|           0.8426 | criterion="gini", max_features="log2", min_samples_leaf=5, n_estimators=40      |
|           0.8416 | criterion="entropy", max_features="log2", min_samples_leaf=7, n_estimators=10   |
|           0.8416 | criterion="gini", max_features="log2", min_samples_leaf=13, n_estimators=160    |
|           0.8416 | criterion="gini", max_features="log2", min_samples_leaf=13, n_estimators=10     |
|           0.8411 | criterion="entropy", max_features="log2", min_samples_leaf=7, n_estimators=40   |
|           0.8406 | criterion="gini", max_features="log2", min_samples_leaf=7, n_estimators=10      |
|           0.8406 | criterion="gini", max_features="log2", min_samples_leaf=7, n_estimators=20      |
|           0.8396 | criterion="entropy", max_features="log2", min_samples_leaf=3, n_estimators=10   |
|           0.8376 | criterion="entropy", max_features="log2", min_samples_leaf=13, n_estimators=40  |
|           0.8371 | criterion="gini", max_features="log2", min_samples_leaf=1, n_estimators=10      |

