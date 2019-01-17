Model Information:
	 - type: GradientBoosting
	 - version: 0.4.0
	 - params: {'max_leaf_nodes': None, 'labels': ['A', 'B', 'C', 'D', 'E'], 'min_samples_split': 2, 'max_depth': 5, 'multilabel': False, 'n_estimators': 500, 'min_impurity_decrease': 0.0, 'verbose': 0, 'min_samples_leaf': 1, 'population_rates': None, 'loss': 'deviance', 'random_state': None, 'presort': 'auto', 'center': True, 'learning_rate': 0.01, 'subsample': 1.0, 'label_weights': None, 'warm_start': False, 'init': None, 'min_weight_fraction_leaf': 0.0, 'criterion': 'friedman_mse', 'max_features': 'log2', 'min_impurity_split': None, 'scale': True}
	Environment:
	 - revscoring_version: '2.3.0'
	 - platform: 'Linux-4.9.0-8-amd64-x86_64-with-debian-9.5'
	 - machine: 'x86_64'
	 - version: '#1 SMP Debian 4.9.110-3+deb9u6 (2018-10-08)'
	 - system: 'Linux'
	 - processor: ''
	 - python_build: ('default', 'Sep 27 2018 17:25:39')
	 - python_compiler: 'GCC 6.3.0 20170516'
	 - python_branch: ''
	 - python_implementation: 'CPython'
	 - python_revision: ''
	 - python_version: '3.5.3'
	 - release: '4.9.0-8-amd64'
	
	Statistics:
	counts (n=4964):
		label       n         ~A    ~B    ~C    ~D    ~E
		-------  ----  ---  ----  ----  ----  ----  ----
		'A'       322  -->   255    34    33     0     0
		'B'       438  -->    24   262   148     4     0
		'C'      1756  -->    33    52  1613    51     7
		'D'       996  -->     0     0    31   835   130
		'E'      1452  -->     0     0     2    18  1432
	rates:
		          'A'    'B'    'C'    'D'    'E'
		------  -----  -----  -----  -----  -----
		sample  0.065  0.088  0.354  0.201  0.293
	match_rate (micro=0.27, macro=0.2):
		    A      E     B      C      D
		-----  -----  ----  -----  -----
		0.063  0.316  0.07  0.368  0.183
	filter_rate (micro=0.73, macro=0.8):
		    A      E     B      C      D
		-----  -----  ----  -----  -----
		0.937  0.684  0.93  0.632  0.817
	recall (micro=0.886, macro=0.827):
		    A      E      B      C      D
		-----  -----  -----  -----  -----
		0.792  0.986  0.598  0.919  0.838
	!recall (micro=0.959, macro=0.969):
		    A      E      B      C      D
		-----  -----  -----  -----  -----
		0.988  0.961  0.981  0.933  0.982
	precision (micro=0.883, macro=0.857):
		    A      E      B      C     D
		-----  -----  -----  -----  ----
		0.817  0.913  0.753  0.883  0.92
	!precision (micro=0.97, macro=0.971):
		    A      E      B      C     D
		-----  -----  -----  -----  ----
		0.986  0.994  0.962  0.954  0.96
	f1 (micro=0.883, macro=0.839):
		    A      E      B    C      D
		-----  -----  -----  ---  -----
		0.804  0.948  0.667  0.9  0.877
	!f1 (micro=0.964, macro=0.97):
		    A      E      B      C      D
		-----  -----  -----  -----  -----
		0.987  0.977  0.971  0.944  0.971
	accuracy (micro=0.95, macro=0.954):
		    A      E      B      C      D
		-----  -----  -----  -----  -----
		0.975  0.968  0.947  0.928  0.953
	fpr (micro=0.041, macro=0.031):
		    A      E      B      C      D
		-----  -----  -----  -----  -----
		0.012  0.039  0.019  0.067  0.018
	roc_auc (micro=0.972, macro=0.971):
		    A      E      B      C      D
		-----  -----  -----  -----  -----
		0.984  0.988  0.951  0.966  0.965
	pr_auc (micro=0.915, macro=0.884):
		    A      E      B      C      D
		-----  -----  -----  -----  -----
		0.889  0.973  0.734  0.929  0.896
	
	 - score_schema: {'title': 'Scikit learn-based classifier score with probability', 'properties': {'probability': {'properties': {'A': {'type': 'number'}, 'E': {'type': 'number'}, 'B': {'type': 'number'}, 'C': {'type': 'number'}, 'D': {'type': 'number'}}, 'description': 'A mapping of probabilities onto each of the potential output labels', 'type': 'object'}, 'prediction': {'description': 'The most likely label predicted by the estimator', 'type': 'string'}}, 'type': 'object'}

