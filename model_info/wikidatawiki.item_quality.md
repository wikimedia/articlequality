Model Information:
	 - type: GradientBoosting
	 - version: 0.5.0
	 - params: {'n_iter_no_change': None, 'learning_rate': 0.01, 'loss': 'deviance', 'max_features': 'log2', 'ccp_alpha': 0.0, 'population_rates': None, 'scale': True, 'presort': 'deprecated', 'labels': ['A', 'B', 'C', 'D', 'E'], 'subsample': 1.0, 'min_weight_fraction_leaf': 0.0, 'criterion': 'friedman_mse', 'center': True, 'n_estimators': 500, 'init': None, 'label_weights': None, 'warm_start': False, 'validation_fraction': 0.1, 'verbose': 0, 'min_impurity_decrease': 0.0, 'tol': 0.0001, 'min_impurity_split': None, 'min_samples_leaf': 1, 'min_samples_split': 2, 'max_leaf_nodes': None, 'multilabel': False, 'max_depth': 5, 'random_state': None}
	Environment:
	 - revscoring_version: '2.8.2'
	 - platform: 'Linux-4.9.0-8-amd64-x86_64-with-debian-9.3'
	 - machine: 'x86_64'
	 - version: '#1 SMP Debian 4.9.144-3.1 (2019-02-19)'
	 - system: 'Linux'
	 - processor: ''
	 - python_build: ('default', 'Jul  9 2020 13:00:10')
	 - python_compiler: 'GCC 6.3.0 20170516'
	 - python_branch: ''
	 - python_implementation: 'CPython'
	 - python_revision: ''
	 - python_version: '3.5.3'
	 - release: '4.9.0-8-amd64'
	
	Statistics:
	counts (n=8988):
		label       n         ~A    ~B    ~C    ~D    ~E
		-------  ----  ---  ----  ----  ----  ----  ----
		'A'       895  -->   774    68    52     1     0
		'B'       786  -->    93   459   214    20     0
		'C'      2286  -->    43   123  1993   121     6
		'D'      1994  -->     0     7   118  1722   147
		'E'      3027  -->     0     0     3    87  2937
	rates:
		          'A'    'B'    'C'    'D'    'E'
		------  -----  -----  -----  -----  -----
		sample    0.1  0.087  0.254  0.222  0.337
	match_rate (micro=0.248, macro=0.2):
		    A      B      C      D      E
		-----  -----  -----  -----  -----
		0.101  0.073  0.265  0.217  0.344
	filter_rate (micro=0.752, macro=0.8):
		    A      B      C      D      E
		-----  -----  -----  -----  -----
		0.899  0.927  0.735  0.783  0.656
	recall (micro=0.877, macro=0.831):
		    A      B      C      D     E
		-----  -----  -----  -----  ----
		0.865  0.584  0.872  0.864  0.97
	!recall (micro=0.966, macro=0.969):
		    A      B      C      D      E
		-----  -----  -----  -----  -----
		0.983  0.976  0.942  0.967  0.974
	precision (micro=0.875, macro=0.844):
		    A      B      C      D     E
		-----  -----  -----  -----  ----
		0.851  0.699  0.837  0.883  0.95
	!precision (micro=0.97, macro=0.97):
		    A      B      C      D      E
		-----  -----  -----  -----  -----
		0.985  0.961  0.956  0.961  0.985
	f1 (micro=0.875, macro=0.836):
		    A      B      C      D     E
		-----  -----  -----  -----  ----
		0.858  0.636  0.854  0.873  0.96
	!f1 (micro=0.968, macro=0.969):
		    A      B      C      D     E
		-----  -----  -----  -----  ----
		0.984  0.968  0.949  0.964  0.98
	accuracy (micro=0.951, macro=0.951):
		    A      B      C      D      E
		-----  -----  -----  -----  -----
		0.971  0.942  0.924  0.944  0.973
	fpr (micro=0.034, macro=0.031):
		    A      B      C      D      E
		-----  -----  -----  -----  -----
		0.017  0.024  0.058  0.033  0.026
	roc_auc (micro=0.976, macro=0.972):
		    A      B      C      D      E
		-----  -----  -----  -----  -----
		0.981  0.953  0.968  0.972  0.988
	pr_auc (micro=0.918, macro=0.884):
		    A      B     C      D      E
		-----  -----  ----  -----  -----
		0.895  0.715  0.91  0.914  0.986
	
	 - score_schema: {'properties': {'probability': {'description': 'A mapping of probabilities onto each of the potential output labels', 'properties': {'D': {'type': 'number'}, 'A': {'type': 'number'}, 'C': {'type': 'number'}, 'B': {'type': 'number'}, 'E': {'type': 'number'}}, 'type': 'object'}, 'prediction': {'description': 'The most likely label predicted by the estimator', 'type': 'string'}}, 'title': 'Scikit learn-based classifier score with probability', 'type': 'object'}

