Model Information:
	 - type: GradientBoosting
	 - version: 0.8.0
	 - params: {'tol': 0.0001, 'population_rates': None, 'random_state': None, 'n_estimators': 300, 'init': None, 'verbose': 0, 'min_impurity_split': None, 'center': True, 'labels': ['E', 'D', 'C', 'B', 'A'], 'min_samples_split': 2, 'criterion': 'friedman_mse', 'multilabel': False, 'scale': True, 'max_depth': 3, 'subsample': 1.0, 'ccp_alpha': 0.0, 'max_features': 'log2', 'validation_fraction': 0.1, 'learning_rate': 0.01, 'min_weight_fraction_leaf': 0.0, 'min_samples_leaf': 1, 'loss': 'deviance', 'warm_start': False, 'min_impurity_decrease': 0.0, 'n_iter_no_change': None, 'label_weights': None, 'max_leaf_nodes': None, 'presort': 'deprecated'}
	Environment:
	 - revscoring_version: '2.8.2'
	 - platform: 'Linux-4.19.0-0.bpo.14-amd64-x86_64-with-debian-9.4'
	 - machine: 'x86_64'
	 - version: '#1 SMP Debian 4.19.171-2~deb9u1 (2021-02-08)'
	 - system: 'Linux'
	 - processor: ''
	 - python_build: ('default', 'Nov 18 2020 21:09:16')
	 - python_compiler: 'GCC 6.3.0 20170516'
	 - python_branch: ''
	 - python_implementation: 'CPython'
	 - python_revision: ''
	 - python_version: '3.5.3'
	 - release: '4.19.0-0.bpo.14-amd64'
	
	Statistics:
	counts (n=1649):
		label      n         ~E    ~D    ~C    ~B    ~A
		-------  ---  ---  ----  ----  ----  ----  ----
		'E'      330  -->   240    90     0     0     0
		'D'      330  -->     2   268    44    16     0
		'C'      330  -->     0    41   289     0     0
		'B'      330  -->     0    23     3   205    99
		'A'      329  -->     0     0     0   102   227
	rates:
		              'E'    'D'    'C'    'B'    'A'
		----------  -----  -----  -----  -----  -----
		sample        0.2    0.2    0.2    0.2    0.2
		population    0.2    0.2    0.2    0.2    0.2
	match_rate (micro=0.2, macro=0.2):
		    E      D      C      B      A
		-----  -----  -----  -----  -----
		0.147  0.256  0.204  0.196  0.198
	filter_rate (micro=0.8, macro=0.8):
		    E      D      C      B      A
		-----  -----  -----  -----  -----
		0.853  0.744  0.796  0.804  0.802
	recall (micro=0.745, macro=0.745):
		    E      D      C      B     A
		-----  -----  -----  -----  ----
		0.727  0.812  0.876  0.621  0.69
	!recall (micro=0.936, macro=0.936):
		    E      D      C      B      A
		-----  -----  -----  -----  -----
		0.998  0.883  0.964  0.911  0.925
	precision (micro=0.764, macro=0.764):
		    E      D     C      B      A
		-----  -----  ----  -----  -----
		0.992  0.635  0.86  0.634  0.697
	!precision (micro=0.937, macro=0.937):
		    E     D      C      B      A
		-----  ----  -----  -----  -----
		0.936  0.95  0.969  0.906  0.923
	f1 (micro=0.748, macro=0.748):
		    E      D      C      B      A
		-----  -----  -----  -----  -----
		0.839  0.713  0.868  0.628  0.693
	!f1 (micro=0.936, macro=0.936):
		    E      D      C      B      A
		-----  -----  -----  -----  -----
		0.966  0.915  0.967  0.908  0.924
	accuracy (micro=0.898, macro=0.898):
		    E      D      C      B      A
		-----  -----  -----  -----  -----
		0.944  0.869  0.947  0.853  0.878
	fpr (micro=0.064, macro=0.064):
		    E      D      C      B      A
		-----  -----  -----  -----  -----
		0.002  0.117  0.036  0.089  0.075
	roc_auc (micro=0.946, macro=0.946):
		    E      D      C      B      A
		-----  -----  -----  -----  -----
		0.989  0.921  0.979  0.902  0.939
	pr_auc (micro=0.804, macro=0.804):
		    E      D      C      B      A
		-----  -----  -----  -----  -----
		0.977  0.803  0.873  0.666  0.703
	
	 - score_schema: {'title': 'Scikit learn-based classifier score with probability', 'properties': {'prediction': {'description': 'The most likely label predicted by the estimator', 'type': 'string'}, 'probability': {'description': 'A mapping of probabilities onto each of the potential output labels', 'properties': {'C': {'type': 'number'}, 'B': {'type': 'number'}, 'E': {'type': 'number'}, 'D': {'type': 'number'}, 'A': {'type': 'number'}}, 'type': 'object'}}, 'type': 'object'}

