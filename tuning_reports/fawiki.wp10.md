# Model tuning report
- Revscoring version: 2.2.4
- Features: articlequality.feature_lists.fawiki.wp10
- Date: 2018-07-09T13:23:12.421584
- Observations: 665
- Labels: ["Stub", "Start", "C", "B", "GA", "FA"]
- Statistic: accuracy.macro (maximize)
- Folds: 5

# Top scoring configurations
| model                  |   accuracy.macro | params                                                                         |
|:-----------------------|-----------------:|:-------------------------------------------------------------------------------|
| GradientBoosting       |           0.8281 | n_estimators=300, max_features="log2", max_depth=5, learning_rate=0.5          |
| GradientBoosting       |           0.8264 | n_estimators=700, max_features="log2", max_depth=7, learning_rate=0.1          |
| RandomForestClassifier |           0.8264 | criterion="gini", max_features="log2", min_samples_leaf=1, n_estimators=320    |
| RandomForestClassifier |           0.8252 | criterion="entropy", max_features="log2", min_samples_leaf=7, n_estimators=20  |
| GradientBoosting       |           0.8248 | n_estimators=300, max_features="log2", max_depth=7, learning_rate=0.01         |
| GradientBoosting       |           0.8243 | n_estimators=500, max_features="log2", max_depth=7, learning_rate=0.1          |
| GradientBoosting       |           0.8236 | n_estimators=100, max_features="log2", max_depth=5, learning_rate=0.5          |
| GradientBoosting       |           0.8234 | n_estimators=700, max_features="log2", max_depth=7, learning_rate=0.5          |
| RandomForestClassifier |           0.8232 | criterion="entropy", max_features="log2", min_samples_leaf=1, n_estimators=640 |
| RandomForestClassifier |           0.8231 | criterion="gini", max_features="log2", min_samples_leaf=3, n_estimators=80     |

# Models
## GaussianNB
|   accuracy.macro | params   |
|-----------------:|:---------|
|           0.7838 |          |

## GradientBoosting
|   accuracy.macro | params                                                                 |
|-----------------:|:-----------------------------------------------------------------------|
|           0.8281 | n_estimators=300, max_features="log2", max_depth=5, learning_rate=0.5  |
|           0.8264 | n_estimators=700, max_features="log2", max_depth=7, learning_rate=0.1  |
|           0.8248 | n_estimators=300, max_features="log2", max_depth=7, learning_rate=0.01 |
|           0.8243 | n_estimators=500, max_features="log2", max_depth=7, learning_rate=0.1  |
|           0.8236 | n_estimators=100, max_features="log2", max_depth=5, learning_rate=0.5  |
|           0.8234 | n_estimators=700, max_features="log2", max_depth=7, learning_rate=0.5  |
|           0.823  | n_estimators=300, max_features="log2", max_depth=7, learning_rate=0.1  |
|           0.8229 | n_estimators=100, max_features="log2", max_depth=7, learning_rate=0.5  |
|           0.8228 | n_estimators=700, max_features="log2", max_depth=5, learning_rate=0.5  |
|           0.822  | n_estimators=700, max_features="log2", max_depth=7, learning_rate=0.01 |
|           0.8218 | n_estimators=300, max_features="log2", max_depth=7, learning_rate=0.5  |
|           0.8212 | n_estimators=500, max_features="log2", max_depth=7, learning_rate=0.01 |
|           0.8206 | n_estimators=300, max_features="log2", max_depth=5, learning_rate=0.01 |
|           0.8195 | n_estimators=500, max_features="log2", max_depth=5, learning_rate=0.01 |
|           0.8193 | n_estimators=500, max_features="log2", max_depth=5, learning_rate=0.5  |
|           0.819  | n_estimators=300, max_features="log2", max_depth=3, learning_rate=0.1  |
|           0.8189 | n_estimators=700, max_features="log2", max_depth=5, learning_rate=0.01 |
|           0.8189 | n_estimators=700, max_features="log2", max_depth=3, learning_rate=0.1  |
|           0.8182 | n_estimators=100, max_features="log2", max_depth=3, learning_rate=0.5  |
|           0.8178 | n_estimators=100, max_features="log2", max_depth=7, learning_rate=0.01 |
|           0.8173 | n_estimators=500, max_features="log2", max_depth=5, learning_rate=0.1  |
|           0.8172 | n_estimators=700, max_features="log2", max_depth=5, learning_rate=0.1  |
|           0.8168 | n_estimators=300, max_features="log2", max_depth=1, learning_rate=0.1  |
|           0.8168 | n_estimators=500, max_features="log2", max_depth=7, learning_rate=0.5  |
|           0.8167 | n_estimators=100, max_features="log2", max_depth=7, learning_rate=0.1  |
|           0.8162 | n_estimators=300, max_features="log2", max_depth=3, learning_rate=0.01 |
|           0.8157 | n_estimators=300, max_features="log2", max_depth=5, learning_rate=0.1  |
|           0.815  | n_estimators=500, max_features="log2", max_depth=1, learning_rate=0.1  |
|           0.8148 | n_estimators=500, max_features="log2", max_depth=3, learning_rate=0.1  |
|           0.8148 | n_estimators=700, max_features="log2", max_depth=3, learning_rate=0.01 |
|           0.8147 | n_estimators=500, max_features="log2", max_depth=3, learning_rate=0.5  |
|           0.8142 | n_estimators=100, max_features="log2", max_depth=5, learning_rate=0.1  |
|           0.8139 | n_estimators=700, max_features="log2", max_depth=1, learning_rate=0.1  |
|           0.8135 | n_estimators=100, max_features="log2", max_depth=3, learning_rate=0.1  |
|           0.813  | n_estimators=300, max_features="log2", max_depth=3, learning_rate=0.5  |
|           0.8129 | n_estimators=500, max_features="log2", max_depth=3, learning_rate=0.01 |
|           0.8129 | n_estimators=700, max_features="log2", max_depth=3, learning_rate=0.5  |
|           0.8102 | n_estimators=500, max_features="log2", max_depth=1, learning_rate=0.01 |
|           0.8099 | n_estimators=100, max_features="log2", max_depth=5, learning_rate=0.01 |
|           0.8099 | n_estimators=300, max_features="log2", max_depth=7, learning_rate=1    |
|           0.8097 | n_estimators=100, max_features="log2", max_depth=7, learning_rate=1    |
|           0.8091 | n_estimators=100, max_features="log2", max_depth=1, learning_rate=0.5  |
|           0.8091 | n_estimators=100, max_features="log2", max_depth=3, learning_rate=0.01 |
|           0.8088 | n_estimators=700, max_features="log2", max_depth=1, learning_rate=0.01 |
|           0.8079 | n_estimators=100, max_features="log2", max_depth=1, learning_rate=0.1  |
|           0.8073 | n_estimators=500, max_features="log2", max_depth=1, learning_rate=0.5  |
|           0.807  | n_estimators=300, max_features="log2", max_depth=1, learning_rate=0.01 |
|           0.806  | n_estimators=300, max_features="log2", max_depth=1, learning_rate=0.5  |
|           0.8042 | n_estimators=500, max_features="log2", max_depth=7, learning_rate=1    |
|           0.8033 | n_estimators=700, max_features="log2", max_depth=1, learning_rate=0.5  |
|           0.8015 | n_estimators=700, max_features="log2", max_depth=1, learning_rate=1    |
|           0.8001 | n_estimators=100, max_features="log2", max_depth=1, learning_rate=0.01 |
|           0.798  | n_estimators=700, max_features="log2", max_depth=7, learning_rate=1    |
|           0.7972 | n_estimators=100, max_features="log2", max_depth=5, learning_rate=1    |
|           0.7965 | n_estimators=300, max_features="log2", max_depth=3, learning_rate=1    |
|           0.7941 | n_estimators=500, max_features="log2", max_depth=3, learning_rate=1    |
|           0.7913 | n_estimators=500, max_features="log2", max_depth=5, learning_rate=1    |
|           0.7881 | n_estimators=300, max_features="log2", max_depth=1, learning_rate=1    |
|           0.7831 | n_estimators=300, max_features="log2", max_depth=5, learning_rate=1    |
|           0.7798 | n_estimators=700, max_features="log2", max_depth=5, learning_rate=1    |
|           0.7696 | n_estimators=100, max_features="log2", max_depth=1, learning_rate=1    |
|           0.7607 | n_estimators=700, max_features="log2", max_depth=3, learning_rate=1    |
|           0.7475 | n_estimators=100, max_features="log2", max_depth=3, learning_rate=1    |
|           0.7385 | n_estimators=500, max_features="log2", max_depth=1, learning_rate=1    |

## BernoulliNB
|   accuracy.macro | params   |
|-----------------:|:---------|
|           0.8002 |          |

## RandomForestClassifier
|   accuracy.macro | params                                                                          |
|-----------------:|:--------------------------------------------------------------------------------|
|           0.8264 | criterion="gini", max_features="log2", min_samples_leaf=1, n_estimators=320     |
|           0.8252 | criterion="entropy", max_features="log2", min_samples_leaf=7, n_estimators=20   |
|           0.8232 | criterion="entropy", max_features="log2", min_samples_leaf=1, n_estimators=640  |
|           0.8231 | criterion="gini", max_features="log2", min_samples_leaf=3, n_estimators=80      |
|           0.8218 | criterion="gini", max_features="log2", min_samples_leaf=1, n_estimators=160     |
|           0.8215 | criterion="entropy", max_features="log2", min_samples_leaf=1, n_estimators=80   |
|           0.821  | criterion="gini", max_features="log2", min_samples_leaf=3, n_estimators=160     |
|           0.821  | criterion="entropy", max_features="log2", min_samples_leaf=1, n_estimators=160  |
|           0.8201 | criterion="entropy", max_features="log2", min_samples_leaf=3, n_estimators=640  |
|           0.8199 | criterion="entropy", max_features="log2", min_samples_leaf=1, n_estimators=320  |
|           0.8197 | criterion="entropy", max_features="log2", min_samples_leaf=1, n_estimators=20   |
|           0.8196 | criterion="entropy", max_features="log2", min_samples_leaf=3, n_estimators=40   |
|           0.8196 | criterion="entropy", max_features="log2", min_samples_leaf=5, n_estimators=160  |
|           0.8195 | criterion="entropy", max_features="log2", min_samples_leaf=3, n_estimators=320  |
|           0.8193 | criterion="gini", max_features="log2", min_samples_leaf=1, n_estimators=640     |
|           0.8192 | criterion="gini", max_features="log2", min_samples_leaf=1, n_estimators=80      |
|           0.819  | criterion="gini", max_features="log2", min_samples_leaf=3, n_estimators=40      |
|           0.8187 | criterion="gini", max_features="log2", min_samples_leaf=3, n_estimators=640     |
|           0.8186 | criterion="gini", max_features="log2", min_samples_leaf=5, n_estimators=20      |
|           0.8184 | criterion="entropy", max_features="log2", min_samples_leaf=3, n_estimators=80   |
|           0.8184 | criterion="entropy", max_features="log2", min_samples_leaf=1, n_estimators=40   |
|           0.8183 | criterion="entropy", max_features="log2", min_samples_leaf=5, n_estimators=320  |
|           0.8181 | criterion="entropy", max_features="log2", min_samples_leaf=3, n_estimators=10   |
|           0.8181 | criterion="entropy", max_features="log2", min_samples_leaf=3, n_estimators=160  |
|           0.8179 | criterion="gini", max_features="log2", min_samples_leaf=3, n_estimators=320     |
|           0.8177 | criterion="entropy", max_features="log2", min_samples_leaf=7, n_estimators=160  |
|           0.8176 | criterion="gini", max_features="log2", min_samples_leaf=1, n_estimators=40      |
|           0.8175 | criterion="gini", max_features="log2", min_samples_leaf=5, n_estimators=40      |
|           0.8174 | criterion="entropy", max_features="log2", min_samples_leaf=5, n_estimators=640  |
|           0.8172 | criterion="entropy", max_features="log2", min_samples_leaf=7, n_estimators=640  |
|           0.8168 | criterion="entropy", max_features="log2", min_samples_leaf=7, n_estimators=320  |
|           0.8162 | criterion="gini", max_features="log2", min_samples_leaf=7, n_estimators=320     |
|           0.815  | criterion="gini", max_features="log2", min_samples_leaf=5, n_estimators=160     |
|           0.8149 | criterion="entropy", max_features="log2", min_samples_leaf=5, n_estimators=40   |
|           0.8148 | criterion="gini", max_features="log2", min_samples_leaf=5, n_estimators=320     |
|           0.8144 | criterion="entropy", max_features="log2", min_samples_leaf=5, n_estimators=10   |
|           0.8142 | criterion="gini", max_features="log2", min_samples_leaf=5, n_estimators=640     |
|           0.8141 | criterion="gini", max_features="log2", min_samples_leaf=7, n_estimators=160     |
|           0.8137 | criterion="gini", max_features="log2", min_samples_leaf=13, n_estimators=80     |
|           0.8136 | criterion="gini", max_features="log2", min_samples_leaf=3, n_estimators=20      |
|           0.8136 | criterion="gini", max_features="log2", min_samples_leaf=5, n_estimators=10      |
|           0.8135 | criterion="gini", max_features="log2", min_samples_leaf=7, n_estimators=10      |
|           0.8134 | criterion="gini", max_features="log2", min_samples_leaf=5, n_estimators=80      |
|           0.813  | criterion="entropy", max_features="log2", min_samples_leaf=13, n_estimators=160 |
|           0.8126 | criterion="gini", max_features="log2", min_samples_leaf=7, n_estimators=640     |
|           0.8126 | criterion="entropy", max_features="log2", min_samples_leaf=5, n_estimators=80   |
|           0.8123 | criterion="gini", max_features="log2", min_samples_leaf=13, n_estimators=640    |
|           0.8119 | criterion="gini", max_features="log2", min_samples_leaf=7, n_estimators=40      |
|           0.8117 | criterion="entropy", max_features="log2", min_samples_leaf=13, n_estimators=20  |
|           0.8115 | criterion="entropy", max_features="log2", min_samples_leaf=7, n_estimators=40   |
|           0.8106 | criterion="entropy", max_features="log2", min_samples_leaf=1, n_estimators=10   |
|           0.8104 | criterion="entropy", max_features="log2", min_samples_leaf=5, n_estimators=20   |
|           0.8103 | criterion="gini", max_features="log2", min_samples_leaf=7, n_estimators=80      |
|           0.8102 | criterion="gini", max_features="log2", min_samples_leaf=7, n_estimators=20      |
|           0.8102 | criterion="gini", max_features="log2", min_samples_leaf=13, n_estimators=320    |
|           0.8096 | criterion="entropy", max_features="log2", min_samples_leaf=13, n_estimators=80  |
|           0.8087 | criterion="entropy", max_features="log2", min_samples_leaf=13, n_estimators=40  |
|           0.8083 | criterion="gini", max_features="log2", min_samples_leaf=13, n_estimators=160    |
|           0.8082 | criterion="gini", max_features="log2", min_samples_leaf=13, n_estimators=40     |
|           0.8078 | criterion="entropy", max_features="log2", min_samples_leaf=7, n_estimators=80   |
|           0.8075 | criterion="entropy", max_features="log2", min_samples_leaf=13, n_estimators=320 |
|           0.8069 | criterion="entropy", max_features="log2", min_samples_leaf=13, n_estimators=640 |
|           0.8068 | criterion="entropy", max_features="log2", min_samples_leaf=3, n_estimators=20   |
|           0.8067 | criterion="gini", max_features="log2", min_samples_leaf=1, n_estimators=20      |
|           0.8066 | criterion="gini", max_features="log2", min_samples_leaf=1, n_estimators=10      |
|           0.8054 | criterion="gini", max_features="log2", min_samples_leaf=3, n_estimators=10      |
|           0.805  | criterion="gini", max_features="log2", min_samples_leaf=13, n_estimators=10     |
|           0.8043 | criterion="gini", max_features="log2", min_samples_leaf=13, n_estimators=20     |
|           0.8042 | criterion="entropy", max_features="log2", min_samples_leaf=13, n_estimators=10  |
|           0.8035 | criterion="entropy", max_features="log2", min_samples_leaf=7, n_estimators=10   |

## LogisticRegression
|   accuracy.macro | params              |
|-----------------:|:--------------------|
|           0.8042 | penalty="l2", C=0.1 |
|           0.7998 | penalty="l2", C=10  |
|           0.7995 | penalty="l1", C=1   |
|           0.7995 | penalty="l2", C=1   |
|           0.7978 | penalty="l1", C=10  |
|           0.7934 | penalty="l1", C=0.1 |

