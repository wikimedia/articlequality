Model Information:
	 - type: GradientBoosting
	 - version: 0.8.0
	 - params: {'scale': True, 'center': True, 'labels': ['E', 'D', 'C', 'B', 'A'], 'multilabel': False, 'population_rates': None, 'ccp_alpha': 0.0, 'criterion': 'friedman_mse', 'init': None, 'learning_rate': 0.01, 'loss': 'deviance', 'max_depth': 3, 'max_features': 'log2', 'max_leaf_nodes': None, 'min_impurity_decrease': 0.0, 'min_impurity_split': None, 'min_samples_leaf': 1, 'min_samples_split': 2, 'min_weight_fraction_leaf': 0.0, 'n_estimators': 300, 'n_iter_no_change': None, 'presort': 'deprecated', 'random_state': None, 'subsample': 1.0, 'tol': 0.0001, 'validation_fraction': 0.1, 'verbose': 0, 'warm_start': False, 'label_weights': None}
	Environment:
	 - revscoring_version: '2.9.3'
	 - platform: 'Linux-5.8.0-44-generic-x86_64-with-glibc2.29'
	 - machine: 'x86_64'
	 - version: '#50~20.04.1-Ubuntu SMP Wed Feb 10 21:07:30 UTC 2021'
	 - system: 'Linux'
	 - processor: 'x86_64'
	 - python_build: ('default', 'Jan 27 2021 15:41:15')
	 - python_compiler: 'GCC 9.3.0'
	 - python_branch: ''
	 - python_implementation: 'CPython'
	 - python_revision: ''
	 - python_version: '3.8.5'
	 - release: '5.8.0-44-generic'
	
	Statistics:
	counts (n=1649):
		label      n         ~E    ~D    ~C    ~B    ~A
		-------  ---  ---  ----  ----  ----  ----  ----
		'E'      330  -->   190   140     0     0     0
		'D'      330  -->     2   267    45    16     0
		'C'      330  -->     0    42   288     0     0
		'B'      330  -->     0    24     2   208    96
		'A'      329  -->     0     0     0   101   228
	rates:
		              'E'    'D'    'C'    'B'    'A'
		----------  -----  -----  -----  -----  -----
		sample        0.2    0.2    0.2    0.2    0.2
		population    0.2    0.2    0.2    0.2    0.2
	match_rate (micro=0.2, macro=0.2):
		    E      D      C      B      A
		-----  -----  -----  -----  -----
		0.116  0.287  0.203  0.197  0.197
	filter_rate (micro=0.8, macro=0.8):
		    E      D      C      B      A
		-----  -----  -----  -----  -----
		0.884  0.713  0.797  0.803  0.803
	recall (micro=0.716, macro=0.716):
		    E      D      C     B      A
		-----  -----  -----  ----  -----
		0.576  0.809  0.873  0.63  0.693
	!recall (micro=0.929, macro=0.929):
		    E      D      C      B      A
		-----  -----  -----  -----  -----
		0.998  0.844  0.964  0.911  0.927
	precision (micro=0.752, macro=0.752):
		   E      D     C     B      A
		----  -----  ----  ----  -----
		0.99  0.564  0.86  0.64  0.704
	!precision (micro=0.93, macro=0.93):
		    E      D      C      B      A
		-----  -----  -----  -----  -----
		0.904  0.946  0.968  0.908  0.924
	f1 (micro=0.719, macro=0.719):
		    E      D      C      B      A
		-----  -----  -----  -----  -----
		0.728  0.665  0.866  0.635  0.699
	!f1 (micro=0.928, macro=0.928):
		    E      D      C     B      A
		-----  -----  -----  ----  -----
		0.949  0.892  0.966  0.91  0.925
	accuracy (micro=0.886, macro=0.886):
		    E      D      C      B     A
		-----  -----  -----  -----  ----
		0.914  0.837  0.946  0.855  0.88
	fpr (micro=0.071, macro=0.071):
		    E      D      C      B      A
		-----  -----  -----  -----  -----
		0.002  0.156  0.036  0.089  0.073
	roc_auc (micro=0.945, macro=0.945):
		    E      D      C      B      A
		-----  -----  -----  -----  -----
		0.989  0.918  0.978  0.901  0.938
	pr_auc (micro=0.802, macro=0.802):
		    E    D      C      B      A
		-----  ---  -----  -----  -----
		0.973  0.8  0.873  0.666  0.696
	
	 - score_schema: {'title': 'Scikit learn-based classifier score with probability', 'type': 'object', 'properties': {'prediction': {'description': 'The most likely label predicted by the estimator', 'type': 'string'}, 'probability': {'description': 'A mapping of probabilities onto each of the potential output labels', 'type': 'object', 'properties': {'E': {'type': 'number'}, 'D': {'type': 'number'}, 'C': {'type': 'number'}, 'B': {'type': 'number'}, 'A': {'type': 'number'}}}}}

