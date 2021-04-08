Model Information:
	 - type: GradientBoosting
	 - version: 0.8.0
	 - params: {'labels': ['E', 'D', 'C', 'B', 'A'], 'n_estimators': 300, 'min_samples_leaf': 1, 'learning_rate': 0.01, 'max_depth': 3, 'scale': True, 'loss': 'deviance', 'ccp_alpha': 0.0, 'min_impurity_split': None, 'validation_fraction': 0.1, 'verbose': 0, 'population_rates': None, 'max_features': 'log2', 'label_weights': None, 'min_weight_fraction_leaf': 0.0, 'random_state': None, 'subsample': 1.0, 'presort': 'deprecated', 'center': True, 'init': None, 'max_leaf_nodes': None, 'min_impurity_decrease': 0.0, 'n_iter_no_change': None, 'tol': 0.0001, 'multilabel': False, 'min_samples_split': 2, 'warm_start': False, 'criterion': 'friedman_mse'}
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
		'E'      330  -->   218   112     0     0     0
		'D'      330  -->     2   269    42    17     0
		'C'      330  -->     0    43   287     0     0
		'B'      330  -->     0    23     3   209    95
		'A'      329  -->     0     0     0   101   228
	rates:
		              'E'    'D'    'C'    'B'    'A'
		----------  -----  -----  -----  -----  -----
		sample        0.2    0.2    0.2    0.2    0.2
		population    0.2    0.2    0.2    0.2    0.2
	match_rate (micro=0.2, macro=0.2):
		    E      D      C      B      A
		-----  -----  -----  -----  -----
		0.133  0.271  0.201  0.198  0.196
	filter_rate (micro=0.8, macro=0.8):
		    E      D      C      B      A
		-----  -----  -----  -----  -----
		0.867  0.729  0.799  0.802  0.804
	recall (micro=0.734, macro=0.734):
		    E      D     C      B      A
		-----  -----  ----  -----  -----
		0.661  0.815  0.87  0.633  0.693
	!recall (micro=0.934, macro=0.934):
		    E      D      C      B      A
		-----  -----  -----  -----  -----
		0.998  0.865  0.966  0.911  0.928
	precision (micro=0.76, macro=0.76):
		    E      D      C      B      A
		-----  -----  -----  -----  -----
		0.991  0.602  0.864  0.639  0.707
	!precision (micro=0.934, macro=0.934):
		    E      D      C      B      A
		-----  -----  -----  -----  -----
		0.922  0.949  0.967  0.909  0.924
	f1 (micro=0.738, macro=0.738):
		    E      D      C      B    A
		-----  -----  -----  -----  ---
		0.793  0.692  0.867  0.636  0.7
	!f1 (micro=0.933, macro=0.933):
		    E      D      C     B      A
		-----  -----  -----  ----  -----
		0.959  0.905  0.967  0.91  0.926
	accuracy (micro=0.894, macro=0.894):
		    E      D      C      B      A
		-----  -----  -----  -----  -----
		0.931  0.855  0.947  0.855  0.881
	fpr (micro=0.066, macro=0.066):
		    E      D      C      B      A
		-----  -----  -----  -----  -----
		0.002  0.135  0.034  0.089  0.072
	roc_auc (micro=0.946, macro=0.946):
		    E      D      C      B      A
		-----  -----  -----  -----  -----
		0.989  0.921  0.979  0.902  0.939
	pr_auc (micro=0.803, macro=0.803):
		    E    D      C      B      A
		-----  ---  -----  -----  -----
		0.978  0.8  0.863  0.663  0.712
	
	 - score_schema: {'properties': {'probability': {'properties': {'A': {'type': 'number'}, 'D': {'type': 'number'}, 'B': {'type': 'number'}, 'C': {'type': 'number'}, 'E': {'type': 'number'}}, 'description': 'A mapping of probabilities onto each of the potential output labels', 'type': 'object'}, 'prediction': {'description': 'The most likely label predicted by the estimator', 'type': 'string'}}, 'title': 'Scikit learn-based classifier score with probability', 'type': 'object'}

