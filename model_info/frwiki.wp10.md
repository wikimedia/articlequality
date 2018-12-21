Model Information:
	 - type: GradientBoosting
	 - version: 0.8.0
	 - params: {'label_weights': None, 'scale': True, 'presort': 'auto', 'subsample': 1.0, 'min_samples_split': 2, 'max_depth': 7, 'labels': ['e', 'bd', 'b', 'a', 'ba', 'adq'], 'min_samples_leaf': 1, 'init': None, 'learning_rate': 0.01, 'min_impurity_split': None, 'n_estimators': 100, 'random_state': None, 'max_leaf_nodes': None, 'min_weight_fraction_leaf': 0.0, 'population_rates': None, 'warm_start': False, 'criterion': 'friedman_mse', 'loss': 'deviance', 'min_impurity_decrease': 0.0, 'multilabel': False, 'verbose': 0, 'max_features': 'log2', 'center': True}
	Environment:
	 - revscoring_version: '2.3.0'
	 - platform: 'Linux-4.9.0-8-amd64-x86_64-with-debian-9.5'
	 - machine: 'x86_64'
	 - version: '#1 SMP Debian 4.9.110-3+deb9u6 (2018-10-08)'
	 - system: 'Linux'
	 - processor: ''
	 - python_build: ('default', 'Jan 19 2017 14:11:04')
	 - python_compiler: 'GCC 6.3.0 20170118'
	 - python_branch: ''
	 - python_implementation: 'CPython'
	 - python_revision: ''
	 - python_version: '3.5.3'
	 - release: '4.9.0-8-amd64'
	
	Statistics:
	counts (n=8930):
		label       n         ~e    ~bd    ~b    ~a    ~ba    ~adq
		-------  ----  ---  ----  -----  ----  ----  -----  ------
		'e'      1491  -->  1084    361    42     4      0       0
		'bd'     1477  -->   254    878   309    16     16       4
		'b'      1487  -->    63    283   743   120    185      93
		'a'      1494  -->    37    102   267   236    474     378
		'ba'     1490  -->    10     14    96   126    840     404
		'adq'    1491  -->     0      1    55    83    347    1005
	rates:
		              'e'    'bd'    'b'    'a'    'ba'    'adq'
		----------  -----  ------  -----  -----  ------  -------
		sample      0.167   0.165  0.167  0.167   0.167    0.167
		population  0.731   0.231  0.03   0.003   0.002    0.001
	match_rate (micro=0.453, macro=0.197):
		    e     bd    adq      b     ba      a
		-----  -----  -----  -----  -----  -----
		0.545  0.216  0.119  0.115  0.138  0.047
	filter_rate (micro=0.547, macro=0.803):
		    e     bd    adq      b     ba      a
		-----  -----  -----  -----  -----  -----
		0.455  0.784  0.881  0.885  0.862  0.953
	recall (micro=0.687, macro=0.536):
		    e     bd    adq    b     ba      a
		-----  -----  -----  ---  -----  -----
		0.727  0.594  0.674  0.5  0.564  0.158
	!recall (micro=0.937, macro=0.907):
		    e     bd    adq      b     ba      a
		-----  -----  -----  -----  -----  -----
		0.951  0.898  0.882  0.897  0.863  0.953
	precision (micro=0.865, macro=0.295):
		    e     bd    adq      b    ba     a
		-----  -----  -----  -----  ----  ----
		0.976  0.637  0.008  0.131  0.01  0.01
	!precision (micro=0.651, macro=0.903):
		    e    bd    adq      b     ba      a
		-----  ----  -----  -----  -----  -----
		0.561  0.88  0.999  0.983  0.999  0.997
	f1 (micro=0.758, macro=0.285):
		    e     bd    adq      b    ba      a
		-----  -----  -----  -----  ----  -----
		0.833  0.615  0.016  0.208  0.02  0.018
	!f1 (micro=0.757, macro=0.895):
		    e     bd    adq      b     ba      a
		-----  -----  -----  -----  -----  -----
		0.706  0.889  0.937  0.938  0.926  0.975
	accuracy (micro=0.8, macro=0.866):
		    e     bd    adq      b     ba      a
		-----  -----  -----  -----  -----  -----
		0.787  0.828  0.882  0.885  0.862  0.951
	fpr (micro=0.063, macro=0.093):
		    e     bd    adq      b     ba      a
		-----  -----  -----  -----  -----  -----
		0.049  0.102  0.118  0.103  0.137  0.047
	roc_auc (micro=0.935, macro=0.862):
		    e    bd    adq      b     ba      a
		-----  ----  -----  -----  -----  -----
		0.955  0.89  0.903  0.823  0.844  0.758
	pr_auc (micro=0.88, macro=0.309):
		    e     bd    adq      b    ba      a
		-----  -----  -----  -----  ----  -----
		0.979  0.687  0.021  0.139  0.01  0.018
	
	 - score_schema: {'title': 'Scikit learn-based classifier score with probability', 'type': 'object', 'properties': {'probability': {'description': 'A mapping of probabilities onto each of the potential output labels', 'type': 'object', 'properties': {'bd': {'type': 'number'}, 'adq': {'type': 'number'}, 'e': {'type': 'number'}, 'ba': {'type': 'number'}, 'a': {'type': 'number'}, 'b': {'type': 'number'}}}, 'prediction': {'description': 'The most likely label predicted by the estimator', 'type': 'string'}}}

