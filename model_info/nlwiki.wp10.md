Model Information:
	 - type: GradientBoosting
	 - version: 0.9.0
	 - params: {'label_weights': None, 'max_features': 'log2', 'multilabel': False, 'subsample': 1.0, 'min_samples_leaf': 1, 'min_impurity_decrease': 0.0, 'verbose': 0, 'validation_fraction': 0.1, 'presort': 'deprecated', 'min_weight_fraction_leaf': 0.0, 'max_depth': 5, 'n_estimators': 700, 'center': True, 'tol': 0.0001, 'min_samples_split': 2, 'random_state': None, 'init': None, 'ccp_alpha': 0.0, 'labels': ['E', 'D', 'C', 'B', 'A'], 'criterion': 'friedman_mse', 'loss': 'deviance', 'min_impurity_split': None, 'warm_start': False, 'n_iter_no_change': None, 'population_rates': None, 'learning_rate': 0.1, 'max_leaf_nodes': None, 'scale': True}
	Environment:
	 - revscoring_version: '2.11.0'
	 - platform: 'Linux-4.19.0-0.bpo.14-amd64-x86_64-with-debian-9.4'
	 - machine: 'x86_64'
	 - version: '#1 SMP Debian 4.19.171-2~deb9u1 (2021-02-08)'
	 - system: 'Linux'
	 - processor: ''
	 - python_build: ('default', 'Sep 27 2018 17:25:39')
	 - python_compiler: 'GCC 6.3.0 20170516'
	 - python_branch: ''
	 - python_implementation: 'CPython'
	 - python_revision: ''
	 - python_version: '3.5.3'
	 - release: '4.19.0-0.bpo.14-amd64'
	
	Statistics:
	counts (n=1713):
		label      n         ~E    ~D    ~C    ~B    ~A
		-------  ---  ---  ----  ----  ----  ----  ----
		'E'      360  -->   269    90     0     1     0
		'D'      349  -->     5   283    45    16     0
		'C'      340  -->     0    39   297     4     0
		'B'      334  -->     0    14     4   212   104
		'A'      330  -->     0     0     0   109   221
	rates:
		              'E'    'D'    'C'    'B'    'A'
		----------  -----  -----  -----  -----  -----
		sample       0.21  0.204  0.198  0.195  0.193
		population   0.2   0.2    0.2    0.2    0.2
	match_rate (micro=0.2, macro=0.2):
		    E      D      C      B      A
		-----  -----  -----  -----  -----
		0.152  0.246  0.203  0.202  0.194
	filter_rate (micro=0.8, macro=0.8):
		    E      D      C      B      A
		-----  -----  -----  -----  -----
		0.848  0.754  0.797  0.798  0.806
	recall (micro=0.747, macro=0.747):
		    E      D      C      B     A
		-----  -----  -----  -----  ----
		0.747  0.811  0.874  0.635  0.67
	!recall (micro=0.937, macro=0.937):
		    E      D      C      B      A
		-----  -----  -----  -----  -----
		0.996  0.895  0.964  0.906  0.925
	precision (micro=0.763, macro=0.763):
		    E      D     C      B     A
		-----  -----  ----  -----  ----
		0.981  0.659  0.86  0.627  0.69
	!precision (micro=0.937, macro=0.937):
		   E     D      C      B      A
		----  ----  -----  -----  -----
		0.94  0.95  0.968  0.908  0.918
	f1 (micro=0.751, macro=0.751):
		    E      D      C      B     A
		-----  -----  -----  -----  ----
		0.848  0.727  0.866  0.631  0.68
	!f1 (micro=0.937, macro=0.937):
		    E      D      C      B      A
		-----  -----  -----  -----  -----
		0.968  0.922  0.966  0.907  0.921
	accuracy (micro=0.899, macro=0.899):
		    E      D      C      B      A
		-----  -----  -----  -----  -----
		0.946  0.878  0.946  0.852  0.874
	fpr (micro=0.063, macro=0.063):
		    E      D      C      B      A
		-----  -----  -----  -----  -----
		0.004  0.105  0.036  0.094  0.075
	roc_auc (micro=0.933, macro=0.933):
		    E      D      C      B      A
		-----  -----  -----  -----  -----
		0.977  0.914  0.967  0.892  0.916
	pr_auc (micro=0.798, macro=0.798):
		   E      D      C      B      A
		----  -----  -----  -----  -----
		0.97  0.778  0.895  0.662  0.684
	
	 - score_schema: {'title': 'Scikit learn-based classifier score with probability', 'type': 'object', 'properties': {'probability': {'description': 'A mapping of probabilities onto each of the potential output labels', 'properties': {'A': {'type': 'number'}, 'D': {'type': 'number'}, 'E': {'type': 'number'}, 'B': {'type': 'number'}, 'C': {'type': 'number'}}, 'type': 'object'}, 'prediction': {'description': 'The most likely label predicted by the estimator', 'type': 'string'}}}

