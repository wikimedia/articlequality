Model Information:
	 - type: GradientBoosting
	 - version: 0.5.0
	 - params: {'scale': True, 'center': True, 'labels': ['A', 'B', 'C', 'D', 'E'], 'multilabel': False, 'population_rates': None, 'ccp_alpha': 0.0, 'criterion': 'friedman_mse', 'init': None, 'learning_rate': 0.01, 'loss': 'deviance', 'max_depth': 5, 'max_features': 'log2', 'max_leaf_nodes': None, 'min_impurity_decrease': 0.0, 'min_impurity_split': None, 'min_samples_leaf': 1, 'min_samples_split': 2, 'min_weight_fraction_leaf': 0.0, 'n_estimators': 500, 'n_iter_no_change': None, 'presort': 'deprecated', 'random_state': None, 'subsample': 1.0, 'tol': 0.0001, 'validation_fraction': 0.1, 'verbose': 0, 'warm_start': False, 'label_weights': None}
	Environment:
	 - revscoring_version: '2.8.2'
	 - platform: 'Linux-4.19.0-10-amd64-x86_64-with-debian-10.5'
	 - machine: 'x86_64'
	 - version: '#1 SMP Debian 4.19.132-1 (2020-07-24)'
	 - system: 'Linux'
	 - processor: ''
	 - python_build: ('default', 'Jul 25 2020 13:03:44')
	 - python_compiler: 'GCC 8.3.0'
	 - python_branch: ''
	 - python_implementation: 'CPython'
	 - python_revision: ''
	 - python_version: '3.7.3'
	 - release: '4.19.0-10-amd64'
	
	Statistics:
	counts (n=8985):
		label       n         ~A    ~B    ~C    ~D    ~E
		-------  ----  ---  ----  ----  ----  ----  ----
		'A'       894  -->   778    67    48     1     0
		'B'       785  -->    93   454   209    29     0
		'C'      2284  -->    38   134  1959   145     8
		'D'      1991  -->     0     8   119  1710   154
		'E'      3031  -->     0     0     4    76  2951
	rates:
		          'A'    'B'    'C'    'D'    'E'
		------  -----  -----  -----  -----  -----
		sample  0.099  0.087  0.254  0.222  0.337
	match_rate (micro=0.248, macro=0.2):
		    A      B     C      D      E
		-----  -----  ----  -----  -----
		0.101  0.074  0.26  0.218  0.346
	filter_rate (micro=0.752, macro=0.8):
		    A      B     C      D      E
		-----  -----  ----  -----  -----
		0.899  0.926  0.74  0.782  0.654
	recall (micro=0.874, macro=0.828):
		   A      B      C      D      E
		----  -----  -----  -----  -----
		0.87  0.578  0.858  0.859  0.974
	!recall (micro=0.965, macro=0.968):
		    A      B      C      D      E
		-----  -----  -----  -----  -----
		0.984  0.975  0.943  0.964  0.973
	precision (micro=0.871, macro=0.84):
		    A      B      C      D      E
		-----  -----  -----  -----  -----
		0.856  0.685  0.838  0.872  0.948
	!precision (micro=0.969, macro=0.969):
		    A     B      C     D      E
		-----  ----  -----  ----  -----
		0.986  0.96  0.951  0.96  0.986
	f1 (micro=0.872, macro=0.833):
		    A      B      C      D      E
		-----  -----  -----  -----  -----
		0.863  0.627  0.848  0.865  0.961
	!f1 (micro=0.967, macro=0.968):
		    A      B      C      D     E
		-----  -----  -----  -----  ----
		0.985  0.967  0.947  0.962  0.98
	accuracy (micro=0.95, macro=0.95):
		    A     B      C      D      E
		-----  ----  -----  -----  -----
		0.973  0.94  0.922  0.941  0.973
	fpr (micro=0.035, macro=0.032):
		    A      B      C      D      E
		-----  -----  -----  -----  -----
		0.016  0.025  0.057  0.036  0.027
	roc_auc (micro=0.975, macro=0.972):
		    A      B      C      D      E
		-----  -----  -----  -----  -----
		0.982  0.953  0.966  0.971  0.988
	pr_auc (micro=0.918, macro=0.884):
		    A      B     C      D      E
		-----  -----  ----  -----  -----
		0.905  0.707  0.91  0.912  0.985
	
	 - score_schema: {'title': 'Scikit learn-based classifier score with probability', 'type': 'object', 'properties': {'prediction': {'description': 'The most likely label predicted by the estimator', 'type': 'string'}, 'probability': {'description': 'A mapping of probabilities onto each of the potential output labels', 'type': 'object', 'properties': {'A': {'type': 'number'}, 'B': {'type': 'number'}, 'C': {'type': 'number'}, 'D': {'type': 'number'}, 'E': {'type': 'number'}}}}}

