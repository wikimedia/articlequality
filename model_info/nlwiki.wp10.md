Model Information:
	 - type: GradientBoosting
	 - version: 0.8.0
	 - params: {'validation_fraction': 0.1, 'min_impurity_split': None, 'max_features': 'log2', 'scale': True, 'min_weight_fraction_leaf': 0.0, 'population_rates': None, 'multilabel': False, 'ccp_alpha': 0.0, 'criterion': 'friedman_mse', 'tol': 0.0001, 'random_state': None, 'labels': ['E', 'D', 'C', 'B', 'A'], 'max_leaf_nodes': None, 'min_samples_leaf': 1, 'max_depth': 3, 'label_weights': None, 'init': None, 'loss': 'deviance', 'learning_rate': 0.01, 'subsample': 1.0, 'warm_start': False, 'verbose': 0, 'min_impurity_decrease': 0.0, 'presort': 'deprecated', 'min_samples_split': 2, 'n_iter_no_change': None, 'n_estimators': 300, 'center': True}
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
		'E'      330  -->   222   108     0     0     0
		'D'      330  -->     2   266    45    17     0
		'C'      330  -->     0    40   290     0     0
		'B'      330  -->     0    23     3   208    96
		'A'      329  -->     0     0     0    98   231
	rates:
		              'E'    'D'    'C'    'B'    'A'
		----------  -----  -----  -----  -----  -----
		sample        0.2    0.2    0.2    0.2    0.2
		population    0.2    0.2    0.2    0.2    0.2
	match_rate (micro=0.2, macro=0.2):
		    E      D      C      B      A
		-----  -----  -----  -----  -----
		0.136  0.265  0.205  0.196  0.199
	filter_rate (micro=0.8, macro=0.8):
		    E      D      C      B      A
		-----  -----  -----  -----  -----
		0.864  0.735  0.795  0.804  0.801
	recall (micro=0.738, macro=0.738):
		    E      D      C     B      A
		-----  -----  -----  ----  -----
		0.673  0.806  0.879  0.63  0.702
	!recall (micro=0.935, macro=0.935):
		    E     D      C      B      A
		-----  ----  -----  -----  -----
		0.998  0.87  0.964  0.913  0.927
	precision (micro=0.762, macro=0.762):
		    E      D      C      B      A
		-----  -----  -----  -----  -----
		0.991  0.609  0.858  0.644  0.707
	!precision (micro=0.935, macro=0.935):
		    E      D     C      B      A
		-----  -----  ----  -----  -----
		0.924  0.947  0.97  0.908  0.926
	f1 (micro=0.741, macro=0.741):
		    E      D      C      B      A
		-----  -----  -----  -----  -----
		0.801  0.693  0.868  0.637  0.705
	!f1 (micro=0.934, macro=0.934):
		   E      D      C     B      A
		----  -----  -----  ----  -----
		0.96  0.907  0.967  0.91  0.926
	accuracy (micro=0.895, macro=0.895):
		    E      D      C      B      A
		-----  -----  -----  -----  -----
		0.933  0.857  0.947  0.856  0.882
	fpr (micro=0.065, macro=0.065):
		    E     D      C      B      A
		-----  ----  -----  -----  -----
		0.002  0.13  0.036  0.087  0.073
	roc_auc (micro=0.945, macro=0.945):
		   E      D      C    B      A
		----  -----  -----  ---  -----
		0.99  0.919  0.979  0.9  0.938
	pr_auc (micro=0.802, macro=0.802):
		    E      D      C      B      A
		-----  -----  -----  -----  -----
		0.979  0.805  0.866  0.652  0.706
	
	 - score_schema: {'type': 'object', 'properties': {'probability': {'description': 'A mapping of probabilities onto each of the potential output labels', 'type': 'object', 'properties': {'A': {'type': 'number'}, 'D': {'type': 'number'}, 'B': {'type': 'number'}, 'C': {'type': 'number'}, 'E': {'type': 'number'}}}, 'prediction': {'description': 'The most likely label predicted by the estimator', 'type': 'string'}}, 'title': 'Scikit learn-based classifier score with probability'}

