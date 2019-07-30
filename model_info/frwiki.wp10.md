Model Information:
	 - type: GradientBoosting
	 - version: 0.8.0
	 - params: {'center': True, 'max_leaf_nodes': None, 'min_impurity_split': None, 'min_samples_split': 2, 'population_rates': None, 'n_iter_no_change': None, 'n_estimators': 100, 'loss': 'deviance', 'label_weights': None, 'criterion': 'friedman_mse', 'verbose': 0, 'multilabel': False, 'scale': True, 'max_depth': 7, 'min_weight_fraction_leaf': 0.0, 'random_state': None, 'min_samples_leaf': 1, 'min_impurity_decrease': 0.0, 'validation_fraction': 0.1, 'subsample': 1.0, 'labels': ['e', 'bd', 'b', 'a', 'ba', 'adq'], 'init': None, 'max_features': 'log2', 'learning_rate': 0.01, 'tol': 0.0001, 'presort': 'auto', 'warm_start': False}
	Environment:
	 - revscoring_version: '2.5.1'
	 - platform: 'Linux-4.9.0-9-amd64-x86_64-with-debian-9.9'
	 - machine: 'x86_64'
	 - version: '#1 SMP Debian 4.9.168-1+deb9u2 (2019-05-13)'
	 - system: 'Linux'
	 - processor: ''
	 - python_build: ('default', 'Sep 27 2018 17:25:39')
	 - python_compiler: 'GCC 6.3.0 20170516'
	 - python_branch: ''
	 - python_implementation: 'CPython'
	 - python_revision: ''
	 - python_version: '3.5.3'
	 - release: '4.9.0-9-amd64'
	
	Statistics:
	counts (n=8930):
		label       n         ~e    ~bd    ~b    ~a    ~ba    ~adq
		-------  ----  ---  ----  -----  ----  ----  -----  ------
		'e'      1491  -->  1078    369    41     3      0       0
		'bd'     1477  -->   258    882   306    14     15       2
		'b'      1487  -->    60    282   756   113    180      96
		'a'      1494  -->    41    100   273   228    473     379
		'ba'     1490  -->    10     15    93   135    819     418
		'adq'    1491  -->     0      1    54    76    341    1019
	rates:
		              'e'    'bd'    'b'    'a'    'ba'    'adq'
		----------  -----  ------  -----  -----  ------  -------
		sample      0.167   0.165  0.167  0.167   0.167    0.167
		population  0.731   0.231  0.03   0.003   0.002    0.001
	match_rate (micro=0.451, macro=0.196):
		    a     ba      b    adq      e     bd
		-----  -----  -----  -----  -----  -----
		0.046  0.137  0.115  0.121  0.542  0.217
	filter_rate (micro=0.549, macro=0.804):
		    a     ba      b    adq      e     bd
		-----  -----  -----  -----  -----  -----
		0.954  0.863  0.885  0.879  0.458  0.783
	recall (micro=0.685, macro=0.536):
		    a    ba      b    adq      e     bd
		-----  ----  -----  -----  -----  -----
		0.153  0.55  0.508  0.683  0.723  0.597
	!recall (micro=0.936, macro=0.907):
		    a     ba      b    adq     e     bd
		-----  -----  -----  -----  ----  -----
		0.954  0.864  0.897   0.88  0.95  0.897
	precision (micro=0.865, macro=0.295):
		   a    ba      b    adq      e     bd
		----  ----  -----  -----  -----  -----
		0.01  0.01  0.133  0.008  0.975  0.636
	!precision (micro=0.648, macro=0.903):
		    a     ba      b    adq      e     bd
		-----  -----  -----  -----  -----  -----
		0.997  0.999  0.983  0.999  0.557  0.881
	f1 (micro=0.757, macro=0.285):
		    a     ba      b    adq     e     bd
		-----  -----  -----  -----  ----  -----
		0.018  0.019  0.211  0.016  0.83  0.616
	!f1 (micro=0.755, macro=0.895):
		    a     ba      b    adq      e     bd
		-----  -----  -----  -----  -----  -----
		0.975  0.927  0.938  0.936  0.703  0.889
	accuracy (micro=0.798, macro=0.865):
		    a     ba      b    adq      e     bd
		-----  -----  -----  -----  -----  -----
		0.952  0.864  0.885  0.879  0.784  0.828
	fpr (micro=0.064, macro=0.093):
		    a     ba      b    adq     e     bd
		-----  -----  -----  -----  ----  -----
		0.046  0.136  0.103   0.12  0.05  0.103
	roc_auc (micro=0.935, macro=0.862):
		    a     ba      b    adq      e    bd
		-----  -----  -----  -----  -----  ----
		0.757  0.844  0.825  0.903  0.955  0.89
	pr_auc (micro=0.879, macro=0.309):
		    a    ba      b    adq      e     bd
		-----  ----  -----  -----  -----  -----
		0.018  0.01  0.141  0.021  0.979  0.687
	
	 - score_schema: {'properties': {'probability': {'properties': {'a': {'type': 'number'}, 'ba': {'type': 'number'}, 'b': {'type': 'number'}, 'adq': {'type': 'number'}, 'e': {'type': 'number'}, 'bd': {'type': 'number'}}, 'type': 'object', 'description': 'A mapping of probabilities onto each of the potential output labels'}, 'prediction': {'type': 'string', 'description': 'The most likely label predicted by the estimator'}}, 'type': 'object', 'title': 'Scikit learn-based classifier score with probability'}

