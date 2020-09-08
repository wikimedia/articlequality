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
	counts (n=8818):
		label       n         ~A    ~B    ~C    ~D    ~E
		-------  ----  ---  ----  ----  ----  ----  ----
		'A'       821  -->   708    67    45     1     0
		'B'       766  -->    84   457   205    20     0
		'C'      2257  -->    39   122  1978   114     4
		'D'      1946  -->     0    11   104  1698   133
		'E'      3028  -->     0     0     3    83  2942
	rates:
		          'A'    'B'    'C'    'D'    'E'
		------  -----  -----  -----  -----  -----
		sample  0.093  0.087  0.256  0.221  0.343
	match_rate (micro=0.251, macro=0.2):
		    A      B      C      D      E
		-----  -----  -----  -----  -----
		0.094  0.075  0.265  0.217  0.349
	filter_rate (micro=0.749, macro=0.8):
		    A      B      C      D      E
		-----  -----  -----  -----  -----
		0.906  0.925  0.735  0.783  0.651
	recall (micro=0.883, macro=0.836):
		    A      B      C      D      E
		-----  -----  -----  -----  -----
		0.862  0.597  0.876  0.873  0.972
	!recall (micro=0.967, macro=0.97):
		    A      B      C      D      E
		-----  -----  -----  -----  -----
		0.985  0.975  0.946  0.968  0.976
	precision (micro=0.88, macro=0.847):
		    A      B      C      D      E
		-----  -----  -----  -----  -----
		0.852  0.696  0.847  0.886  0.956
	!precision (micro=0.971, macro=0.971):
		    A      B      C      D      E
		-----  -----  -----  -----  -----
		0.986  0.962  0.957  0.964  0.985
	f1 (micro=0.881, macro=0.841):
		    A      B      C      D      E
		-----  -----  -----  -----  -----
		0.857  0.642  0.861  0.879  0.963
	!f1 (micro=0.969, macro=0.97):
		    A      B      C      D      E
		-----  -----  -----  -----  -----
		0.985  0.969  0.951  0.966  0.981
	accuracy (micro=0.954, macro=0.953):
		    A      B      C      D      E
		-----  -----  -----  -----  -----
		0.973  0.942  0.928  0.947  0.975
	fpr (micro=0.033, macro=0.03):
		    A      B      C      D      E
		-----  -----  -----  -----  -----
		0.015  0.025  0.054  0.032  0.024
	roc_auc (micro=0.976, macro=0.973):
		    A      B      C      D      E
		-----  -----  -----  -----  -----
		0.981  0.955  0.969  0.973  0.989
	pr_auc (micro=0.921, macro=0.887):
		    A     B      C      D      E
		-----  ----  -----  -----  -----
		0.895  0.72  0.919  0.914  0.985
	
	 - score_schema: {'title': 'Scikit learn-based classifier score with probability', 'type': 'object', 'properties': {'prediction': {'description': 'The most likely label predicted by the estimator', 'type': 'string'}, 'probability': {'description': 'A mapping of probabilities onto each of the potential output labels', 'type': 'object', 'properties': {'A': {'type': 'number'}, 'B': {'type': 'number'}, 'C': {'type': 'number'}, 'D': {'type': 'number'}, 'E': {'type': 'number'}}}}}

