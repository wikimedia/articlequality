Model Information:
	 - type: GradientBoosting
	 - version: 0.8.0
	 - params: {'presort': 'deprecated', 'min_impurity_decrease': 0.0, 'n_estimators': 100, 'verbose': 0, 'criterion': 'friedman_mse', 'max_depth': 7, 'min_samples_leaf': 1, 'ccp_alpha': 0.0, 'random_state': None, 'labels': ['e', 'bd', 'b', 'a', 'ba', 'adq'], 'multilabel': False, 'warm_start': False, 'loss': 'deviance', 'population_rates': None, 'validation_fraction': 0.1, 'center': True, 'init': None, 'label_weights': None, 'subsample': 1.0, 'max_features': 'log2', 'n_iter_no_change': None, 'scale': True, 'min_impurity_split': None, 'min_samples_split': 2, 'tol': 0.0001, 'max_leaf_nodes': None, 'learning_rate': 0.01, 'min_weight_fraction_leaf': 0.0}
	Environment:
	 - revscoring_version: '2.8.2'
	 - platform: 'Linux-4.9.0-11-amd64-x86_64-with-debian-9.12'
	 - machine: 'x86_64'
	 - version: '#1 SMP Debian 4.9.189-3+deb9u1 (2019-09-20)'
	 - system: 'Linux'
	 - processor: ''
	 - python_build: ('default', 'Sep 27 2018 17:25:39')
	 - python_compiler: 'GCC 6.3.0 20170516'
	 - python_branch: ''
	 - python_implementation: 'CPython'
	 - python_revision: ''
	 - python_version: '3.5.3'
	 - release: '4.9.0-11-amd64'
	
	Statistics:
	counts (n=8930):
		label       n         ~e    ~bd    ~b    ~a    ~ba    ~adq
		-------  ----  ---  ----  -----  ----  ----  -----  ------
		'e'      1491  -->  1083    368    37     3      0       0
		'bd'     1477  -->   253    878   310    18     14       4
		'b'      1487  -->    63    286   746   119    179      94
		'a'      1494  -->    37    105   269   227    475     381
		'ba'     1490  -->    10     16    92   139    819     414
		'adq'    1491  -->     0      1    59    78    337    1016
	rates:
		              'e'    'bd'    'b'    'a'    'ba'    'adq'
		----------  -----  ------  -----  -----  ------  -------
		sample      0.167   0.165  0.167  0.167   0.167    0.167
		population  0.731   0.231  0.03   0.003   0.002    0.001
	match_rate (micro=0.453, macro=0.197):
		    e     bd      b      a     ba    adq
		-----  -----  -----  -----  -----  -----
		0.544  0.218  0.115  0.048  0.136  0.121
	filter_rate (micro=0.547, macro=0.803):
		    e     bd      b      a     ba    adq
		-----  -----  -----  -----  -----  -----
		0.456  0.782  0.885  0.952  0.864  0.879
	recall (micro=0.687, macro=0.534):
		    e     bd      b      a    ba    adq
		-----  -----  -----  -----  ----  -----
		0.726  0.594  0.502  0.152  0.55  0.681
	!recall (micro=0.936, macro=0.907):
		    e     bd      b      a     ba    adq
		-----  -----  -----  -----  -----  -----
		0.951  0.896  0.897  0.952  0.865   0.88
	precision (micro=0.864, macro=0.295):
		    e     bd      b      a    ba    adq
		-----  -----  -----  -----  ----  -----
		0.976  0.632  0.132  0.009  0.01  0.008
	!precision (micro=0.65, macro=0.903):
		    e    bd      b      a     ba    adq
		-----  ----  -----  -----  -----  -----
		0.561  0.88  0.983  0.997  0.999  0.999
	f1 (micro=0.757, macro=0.285):
		    e     bd      b      a     ba    adq
		-----  -----  -----  -----  -----  -----
		0.833  0.613  0.209  0.017  0.019  0.016
	!f1 (micro=0.756, macro=0.895):
		    e     bd      b      a     ba    adq
		-----  -----  -----  -----  -----  -----
		0.705  0.888  0.938  0.974  0.927  0.936
	accuracy (micro=0.8, macro=0.865):
		    e     bd      b     a     ba    adq
		-----  -----  -----  ----  -----  -----
		0.787  0.826  0.885  0.95  0.864   0.88
	fpr (micro=0.064, macro=0.093):
		    e     bd      b      a     ba    adq
		-----  -----  -----  -----  -----  -----
		0.049  0.104  0.103  0.048  0.135   0.12
	roc_auc (micro=0.935, macro=0.862):
		    e    bd      b      a     ba    adq
		-----  ----  -----  -----  -----  -----
		0.954  0.89  0.824  0.754  0.845  0.902
	pr_auc (micro=0.88, macro=0.309):
		    e     bd      b      a    ba    adq
		-----  -----  -----  -----  ----  -----
		0.979  0.689  0.137  0.018  0.01  0.021
	
	 - score_schema: {'properties': {'prediction': {'type': 'string', 'description': 'The most likely label predicted by the estimator'}, 'probability': {'properties': {'e': {'type': 'number'}, 'bd': {'type': 'number'}, 'a': {'type': 'number'}, 'b': {'type': 'number'}, 'ba': {'type': 'number'}, 'adq': {'type': 'number'}}, 'type': 'object', 'description': 'A mapping of probabilities onto each of the potential output labels'}}, 'title': 'Scikit learn-based classifier score with probability', 'type': 'object'}

