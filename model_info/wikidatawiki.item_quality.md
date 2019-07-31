Model Information:
	 - type: GradientBoosting
	 - version: 0.4.0
	 - params: {'max_depth': 5, 'max_features': 'log2', 'loss': 'deviance', 'scale': True, 'min_samples_leaf': 1, 'labels': ['A', 'B', 'C', 'D', 'E'], 'criterion': 'friedman_mse', 'warm_start': False, 'min_impurity_decrease': 0.0, 'min_samples_split': 2, 'min_impurity_split': None, 'init': None, 'max_leaf_nodes': None, 'min_weight_fraction_leaf': 0.0, 'subsample': 1.0, 'tol': 0.0001, 'label_weights': None, 'learning_rate': 0.01, 'verbose': 0, 'n_estimators': 500, 'multilabel': False, 'population_rates': None, 'random_state': None, 'n_iter_no_change': None, 'center': True, 'validation_fraction': 0.1, 'presort': 'auto'}
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
	counts (n=4959):
		label       n         ~A    ~B    ~C    ~D    ~E
		-------  ----  ---  ----  ----  ----  ----  ----
		'A'       322  -->   257    26    39     0     0
		'B'       438  -->    16   263   156     3     0
		'C'      1756  -->    26    47  1631    48     4
		'D'       996  -->     0     0   212   671   113
		'E'      1447  -->     0     0     2   101  1344
	rates:
		          'A'    'B'    'C'    'D'    'E'
		------  -----  -----  -----  -----  -----
		sample  0.065  0.088  0.354  0.201  0.292
	match_rate (micro=0.275, macro=0.2):
		   A      E      B      D      C
		----  -----  -----  -----  -----
		0.06  0.295  0.068  0.166  0.411
	filter_rate (micro=0.725, macro=0.8):
		   A      E      B      D      C
		----  -----  -----  -----  -----
		0.94  0.705  0.932  0.834  0.589
	recall (micro=0.84, macro=0.786):
		    A      E    B      D      C
		-----  -----  ---  -----  -----
		0.798  0.929  0.6  0.674  0.929
	!recall (micro=0.935, macro=0.955):
		    A      E      B      D      C
		-----  -----  -----  -----  -----
		0.991  0.967  0.984  0.962  0.872
	precision (micro=0.84, macro=0.835):
		   A     E      B      D    C
		----  ----  -----  -----  ---
		0.86  0.92  0.783  0.815  0.8
	!precision (micro=0.956, macro=0.959):
		    A      E      B      D      C
		-----  -----  -----  -----  -----
		0.986  0.971  0.962  0.921  0.957
	f1 (micro=0.836, macro=0.806):
		    A      E     B      D      C
		-----  -----  ----  -----  -----
		0.828  0.924  0.68  0.738  0.859
	!f1 (micro=0.945, macro=0.957):
		    A      E      B      D      C
		-----  -----  -----  -----  -----
		0.988  0.969  0.973  0.941  0.913
	accuracy (micro=0.924, macro=0.936):
		    A      E     B      D      C
		-----  -----  ----  -----  -----
		0.978  0.956  0.95  0.904  0.892
	fpr (micro=0.065, macro=0.045):
		    A      E      B      D      C
		-----  -----  -----  -----  -----
		0.009  0.033  0.016  0.038  0.128
	roc_auc (micro=0.964, macro=0.965):
		    A      E      B      D      C
		-----  -----  -----  -----  -----
		0.985  0.986  0.952  0.949  0.954
	pr_auc (micro=0.89, macro=0.864):
		    A     E      B     D      C
		-----  ----  -----  ----  -----
		0.894  0.97  0.744  0.81  0.905
	
	 - score_schema: {'title': 'Scikit learn-based classifier score with probability', 'type': 'object', 'properties': {'prediction': {'type': 'string', 'description': 'The most likely label predicted by the estimator'}, 'probability': {'type': 'object', 'description': 'A mapping of probabilities onto each of the potential output labels', 'properties': {'A': {'type': 'number'}, 'E': {'type': 'number'}, 'B': {'type': 'number'}, 'D': {'type': 'number'}, 'C': {'type': 'number'}}}}}

